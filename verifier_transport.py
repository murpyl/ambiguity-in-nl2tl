"""OpenRouter batches and content-addressed audit cache for the dataset verifier.

Importing this module does not import the SDK, read credentials, or use a network.
"""

import hashlib
import json
import os
from pathlib import Path
import re
import time


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def digest(value):
    return hashlib.sha256(canonical(value).encode("utf-8")).hexdigest()


def request_directory_name(identity):
    """Readable stage/model/settings label with a short content fingerprint."""
    def slug(value):
        return re.sub(r"[^a-zA-Z0-9._-]+", "-", str(value)).strip("-._") or "unnamed"

    model = "__".join(slug(part) for part in identity["model"].split("/"))
    return (f"{slug(identity['stage'])}__{model}__"
            f"tokens-{slug(identity['settings']['max_tokens'])}__{digest(identity)[:12]}")


def _redact(value):
    """Keep audit data exact except credentials, even if a provider echoes them."""
    secret = os.environ.get("OPENROUTER_API_KEY", "")

    def clean(item):
        if isinstance(item, str):
            return item.replace(secret, "[REDACTED]") if secret else item
        if isinstance(item, dict):
            result = {}
            for key, child in item.items():
                normalized = str(key).lower().replace("-", "_")
                sensitive = normalized in {"authorization", "proxy_authorization", "api_key", "apikey", "x_api_key"}
                result[clean(key)] = "[REDACTED]" if sensitive else clean(child)
            return result
        if isinstance(item, (list, tuple)):
            return [clean(child) for child in item]
        return item

    return clean(value)


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(_redact(value), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(path)


class BatchError(RuntimeError):
    """A technical batch failure, never a linguistic rejection."""

    def __init__(self, category, message, retryable=False):
        super().__init__(f"{category}: {message}")
        self.category = category
        self.retryable = retryable


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON object key")
        result[key] = value
    return result


def parse_response(raw):
    """Reject partial, refused, non-JSON, and ambiguous JSON responses."""
    if not isinstance(raw, dict):
        raise BatchError("invalid_response", "expected a response object", True)
    if raw.get("error"):
        raise _api_error(raw["error"])
    choices = raw.get("choices")
    if not isinstance(choices, list) or len(choices) != 1:
        raise BatchError("invalid_response", "expected exactly one choice", True)
    choice = choices[0]
    if not isinstance(choice, dict):
        raise BatchError("invalid_response", "invalid choice object", True)
    reason = choice.get("finish_reason")
    if reason in ("length", "max_tokens"):
        raise BatchError("output_truncated", "increase the output token limit; batch was not split")
    if reason != "stop":
        raise BatchError("invalid_response", "completion did not finish normally", True)
    message = choice.get("message")
    if not isinstance(message, dict) or message.get("refusal"):
        raise BatchError("refusal", "missing message or explicit refusal", True)
    content = message.get("content")
    if not isinstance(content, str) or not content.strip():
        raise BatchError("invalid_response", "expected nonempty JSON text", True)
    try:
        return json.loads(content, object_pairs_hook=_unique_object,
                          parse_constant=lambda value: (_ for _ in ()).throw(ValueError("nonfinite JSON number")))
    except (ValueError, TypeError) as exc:
        raise BatchError("invalid_json", "response is not strict JSON", True) from exc


def _api_error(body=None, status=None, exception_name=""):
    """Classify without persisting provider messages, headers, URLs, or credentials."""
    error = body.get("error", body) if isinstance(body, dict) else {}
    if not isinstance(error, dict):
        error = {}
    # OpenRouter can put a generic message outside a JSON-encoded provider error
    # in metadata.raw. Inspect the whole nested body, never persist its text.
    text = json.dumps(body, ensure_ascii=False, default=str).lower()
    code = str(error.get("code", "")).lower()
    if any(token in text + " " + code for token in (
        "context_length", "context length", "context window", "too many tokens", "maximum context",
    )):
        return BatchError("context_limit", "full batch exceeds model context; batch was not split")
    if any(token in text for token in (
        "maximum output", "output token limit", "max_tokens must", "max_tokens is too",
        "max_output_tokens must", "max_completion_tokens must", "requested output tokens",
        "max_tokens exceeds", "max_tokens cannot exceed",
    )):
        return BatchError("output_limit", "requested output limit exceeds model allowance; reduce max-tokens")
    if status is None and isinstance(error.get("code"), int):
        status = error["code"]
    if status in (408, 409, 429) or isinstance(status, int) and status >= 500:
        return BatchError("transient_api", f"HTTP {status}", True)
    if exception_name in ("APITimeoutError", "APIConnectionError", "TimeoutError", "ConnectionError"):
        return BatchError("transient_api", exception_name, True)
    suffix = f"HTTP {status}" if isinstance(status, int) else "provider request failed"
    return BatchError("api_error", suffix)


class OpenRouterTransport:
    def __init__(self, settings, retries=2):
        from dotenv import load_dotenv
        from openai import OpenAI

        load_dotenv()
        key = os.environ.get("OPENROUTER_API_KEY")
        if not key:
            raise BatchError("configuration", "OPENROUTER_API_KEY is not set")
        self.settings = dict(settings)
        self.retries = retries
        # This module owns bounded retries so SDK retries cannot multiply them.
        self.client = OpenAI(api_key=key, base_url="https://openrouter.ai/api/v1",
                             max_retries=0, timeout=600)

    def check_models(self, models):
        for attempt in range(self.retries + 1):
            try:
                raw = self.client.models.list().model_dump(mode="json")
                break
            except Exception as exc:
                error = _api_error(getattr(exc, "body", None), getattr(exc, "status_code", None),
                                   type(exc).__name__)
                if not error.retryable or attempt == self.retries:
                    raise error from None
                time.sleep(min(2 ** attempt, 8))
        available = {entry["id"]: entry for entry in raw.get("data", []) if isinstance(entry, dict) and "id" in entry}
        missing = sorted(set(models) - available.keys())
        if missing:
            raise BatchError("model_unavailable", "requested exact model IDs unavailable: " + ", ".join(missing))
        return {"requested_models": list(models), "models": [available[model] for model in models]}

    def complete(self, model, messages, settings):
        try:
            response = self.client.chat.completions.create(model=model, messages=messages, **settings)
            return response.model_dump(mode="json")
        except Exception as exc:
            error = _api_error(getattr(exc, "body", None), getattr(exc, "status_code", None),
                               type(exc).__name__)
            error.response_body = getattr(exc, "body", None)
            raise error from None


class BatchCache:
    """Successful identical requests are reused; failed attempts remain auditable."""

    def __init__(self, output, transport, settings, retries=2, model_max_tokens=None):
        if retries < 0:
            raise ValueError("retries must be nonnegative")
        self.output = Path(output)
        self.transport = transport
        self.settings = dict(settings)
        self.model_max_tokens = dict(model_max_tokens or {})
        self.retries = retries
        self.records = []

    def request(self, stage, model, messages, validate):
        settings = dict(self.settings)
        if model in self.model_max_tokens:
            settings["max_tokens"] = self.model_max_tokens[model]
        identity = {"cache_version": 1, "stage": stage, "model": model,
                    "messages": messages, "settings": settings}
        key = digest(identity)
        relative_directory = Path("requests") / request_directory_name(identity)
        directory = self.output / relative_directory
        request_file = directory / "request.json"
        if directory.exists() and not directory.is_dir():
            raise BatchError("cache_identity", "request cache path is not a directory")
        if request_file.exists():
            try:
                saved_identity = json.loads(request_file.read_text(encoding="utf-8"))
            except (ValueError, OSError) as exc:
                raise BatchError("cache_identity", "cannot read existing request identity") from exc
            if saved_identity != identity:
                raise BatchError("cache_identity", "existing request identity differs; cache was not overwritten")
        else:
            if directory.exists() and any(directory.iterdir()):
                raise BatchError("cache_identity", "nonempty request directory has no request identity")
            write_json(request_file, identity)
        record = {"stage": stage, "model": model, "cache_key": key,
                  "request_directory": relative_directory.as_posix()}
        success = directory / "success.json"
        if success.exists():
            saved = json.loads(success.read_text(encoding="utf-8"))
            raw = json.loads((directory / saved["response_file"]).read_text(encoding="utf-8"))
            parsed = self._validate(raw, validate)
            write_json(directory / "parsed.json", parsed)
            self.records.append({**record, "resumed": True})
            return parsed
        attempts_file = directory / "attempts.json"
        attempts = json.loads(attempts_file.read_text(encoding="utf-8")) if attempts_file.exists() else []
        for attempt in range(self.retries + 1):
            number = len(attempts) + 1
            response_file = f"response_{number:04d}.json"
            entry = {"attempt": number}
            try:
                raw = self.transport.complete(model, messages, settings)
                write_json(directory / response_file, raw)
                entry["response_file"] = response_file
                parsed = self._validate(raw, validate)
            except Exception as exc:
                error = exc if isinstance(exc, BatchError) else BatchError("processing_error", type(exc).__name__)
                if getattr(error, "response_body", None) is not None:
                    write_json(directory / response_file, error.response_body)
                    entry["response_file"] = response_file
                entry.update({"status": "error", "category": error.category,
                              "message": str(error), "retryable": error.retryable})
                attempts.append(entry)
                write_json(attempts_file, attempts)
                if not error.retryable or attempt == self.retries:
                    self.records.append({**record, "resumed": False, "error": str(error)})
                    raise error from None
                time.sleep(min(2 ** attempt, 8))
                continue
            entry["status"] = "success"
            attempts.append(entry)
            write_json(attempts_file, attempts)
            write_json(directory / "parsed.json", parsed)
            write_json(success, {"response_file": response_file})
            self.records.append({**record, "resumed": False})
            return parsed

    @staticmethod
    def _validate(raw, validate):
        content = parse_response(raw)
        try:
            return validate(content)
        except BatchError:
            raise
        except (ValueError, KeyError, TypeError) as exc:
            raise BatchError("invalid_batch", str(exc), True) from exc
