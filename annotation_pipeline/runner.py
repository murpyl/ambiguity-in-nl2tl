"""Fail-closed two-stage annotation orchestration; no SDK and no retries."""
import argparse
import hashlib
import fcntl
import http.client
import json
import os
from pathlib import Path
import urllib.error
import urllib.request
from datetime import datetime, timezone

MODELS = ['google/gemini-3.8-flash', 'anthropic/claude-haiku-5.5',
          'openai/gpt-5.6-luna', 'deepseek/deepseek-v4.1-flash', 'qwen/qwen3.8-flash']
LABELS = {'Supported', 'Not supported', 'Uncertain'}
BASE = 'https://openrouter.ai/api/v1'


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def parse_json(raw):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError('Duplicate JSON key: ' + key)
            result[key] = value
        return result
    return json.loads(raw, object_pairs_hook=unique)


def read(path):
    return parse_json(Path(path).read_text())


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    tmp.replace(path)


def text_required(value):
    return isinstance(value, str) and bool(value.strip())


def validate_scope(scope, count=88):
    entries = scope['entries']
    if len(entries) != count:
        raise ValueError(f'Expected {count} entries')
    for field in ('review_id',):
        values = [e[field] for e in entries]
        if len(set(values)) != count or not all(map(text_required, values)):
            raise ValueError(f'Invalid/duplicate {field}')
    if len({(e['source_family'], e['annotation_id']) for e in entries}) != count:
        raise ValueError('Duplicate family/annotation identity')
    for e in entries:
        if not text_required(e['annotation_id']):
            raise ValueError('Missing annotation identity')
        family = e['source_family']
        if not text_required(family) or any(c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-' for c in family) or family == 'trigger_scope':
            raise ValueError('Invalid source family')
        if not text_required(e['requirement']) or not e['propositions']:
            raise ValueError('Missing requirement/propositions')
        ids = [r['reading_id'] for r in e['readings']]
        if not ids or len(ids) != len(set(ids)) or not all(map(text_required, ids)) or not all(text_required(r['plain']) for r in e['readings']):
            raise ValueError('Invalid readings')
    for key in ('stage1_instructions', 'stage2_instructions'):
        if not text_required(scope[key]):
            raise ValueError(f'Missing {key}')
    return entries


def validate(data, entries, stage):
    if not isinstance(data, dict) or set(data) != {'entries'}:
        raise ValueError('Unexpected annotation root fields')
    rows = data.get('entries')
    expected = {e['review_id']: e for e in entries}
    if not isinstance(rows, list) or len(rows) != len(expected):
        raise ValueError('Missing/extra answers')
    if {r.get('review_id') for r in rows} != set(expected):
        raise ValueError('Duplicate/unknown review IDs')
    for row in rows:
        fields = {'review_id', 'comments', 'interpretations'} if stage == 1 else {'review_id', 'comments', 'supports', 'additional_interpretations'}
        if set(row) != fields:
            raise ValueError('Unexpected annotation row fields')
        if not isinstance(row.get('comments'), str):
            raise ValueError('Missing comments field')
        field = 'interpretations' if stage == 1 else 'additional_interpretations'
        values = row.get(field)
        if not isinstance(values, list) or not all(map(text_required, values)) or (stage == 1 and not values):
            raise ValueError(f'Invalid {field}')
        if stage == 2:
            supports = row.get('supports')
            ids = {r['reading_id'] for r in expected[row['review_id']]['readings']}
            if not isinstance(supports, dict) or set(supports) != ids or not all(v in LABELS for v in supports.values()):
                raise ValueError('Missing/invalid reading assessments')
    return data


def schema(stage, entries=None):
    string = {'type': 'string'}
    fields = {'review_id': string, 'comments': string}
    fields['interpretations' if stage == 1 else 'additional_interpretations'] = {'type': 'array', 'items': string, 'minItems': 1 if stage == 1 else 0}
    if stage == 2:
        # Share the support shape across requirements instead of compiling one
        # near-identical grammar branch per review ID. Exact per-entry coverage
        # and reading-key membership remain enforced by validate().
        keysets = sorted({tuple(sorted(r['reading_id'] for r in entry['readings']))
                          for entry in entries or []})
        if not keysets:
            raise ValueError('Stage 2 schema requires reading entries')
        variants = []
        for keys in keysets:
            properties = {key: {'type': 'string', 'enum': sorted(LABELS)} for key in keys}
            variants.append({'type': 'object', 'properties': properties,
                             'required': list(keys), 'additionalProperties': False})
        fields['supports'] = variants[0] if len(variants) == 1 else {'anyOf': variants}
    return {'type': 'object', 'properties': {'entries': {'type': 'array', 'items': {
        'type': 'object', 'properties': fields, 'required': list(fields), 'additionalProperties': False}}},
        'required': ['entries'], 'additionalProperties': False}


def messages(scope, stage, frozen=None):
    # Explicit allowlist prevents administrative/source metadata and readings leaking.
    first = [{'review_id': e['review_id'], 'requirement': e['requirement'],
              'propositions': e['propositions'], **({'scenario': e['scenario']} if e.get('scenario') else {})}
             for e in scope['entries']]
    instruction = ('Return one JSON object matching this schema, covering every review_id. '
                   'These are model-generated annotations. Do not report completion times.\n')
    result = [{'role': 'user', 'content': scope['stage1_instructions'] + '\n' + instruction +
               json.dumps(schema(1)) + '\n' + json.dumps(first, ensure_ascii=False)}]
    if stage == 2:
        result += [{'role': 'assistant', 'content': frozen}, {'role': 'user', 'content':
            scope['stage2_instructions'] + '\nKeep all frozen Stage 1 answers unchanged. '
            'Record newly discovered interpretations only in additional_interpretations.\n' + instruction +
            json.dumps(schema(2, scope['entries'])) + '\n' + json.dumps([
                {'review_id': e['review_id'], 'readings': e['readings']} for e in scope['entries']], ensure_ascii=False)}]
    return result


def request(method, endpoint, key=None, payload=None, timeout=60):
    headers = {'Content-Type': 'application/json'}
    if key:
        headers['Authorization'] = 'Bearer ' + key
    req = urllib.request.Request(BASE + endpoint, headers=headers, method=method,
                                 data=None if payload is None else json.dumps(payload).encode())
    with urllib.request.urlopen(req, timeout=timeout) as response:
        chunks = []
        try:
            while True:
                chunk = response.read(65536)
                if not chunk:
                    break
                chunks.append(chunk)
        except BaseException as error:
            error.annotation_partial = b''.join(chunks) + getattr(error, 'partial', b'')
            raise
        return b''.join(chunks), dict(response.headers)


def preflight(run, scope, config, transport=request):
    # Catalog only: never a paid test completion. Save complete public catalog.
    write(run / 'preflight.started.json', {'started_at': now(), 'endpoint': BASE + '/models'})
    try:
        raw, headers = transport('GET', '/models')
    except BaseException as error:
        if isinstance(error, urllib.error.HTTPError):
            (run / 'catalog.failure.md').write_bytes(error.read())
        write(run / 'preflight.failure.json', {'failed_at': now(), 'error_type': type(error).__name__, 'reason': str(error)})
        raise
    (run / 'catalog.response.json').write_bytes(raw)
    catalog = {m['id']: m for m in json.loads(raw)['data']}
    missing = [m for m in MODELS if m not in catalog]
    if missing:
        raise ValueError('Unavailable exact model IDs: ' + ', '.join(missing))
    omitted = config.get('omit_temperature_models', [])
    if (not isinstance(omitted, list) or any(not isinstance(model, str) or model not in MODELS for model in omitted)
            or len(omitted) != len(set(omitted))):
        raise ValueError('omit_temperature_models must contain unique exact known model IDs')
    unsupported_temperature = [model for model in MODELS if model not in omitted
                               and 'temperature' not in catalog[model].get('supported_parameters', [])]
    if unsupported_temperature:
        raise ValueError('Configured temperature is not supported by catalog for: '
                         + ', '.join(unsupported_temperature))
    maxout = config['max_output_tokens']
    if type(maxout) is not int or maxout < 1:
        raise ValueError('Invalid output budget')
    # UTF-8 bytes upper-bound input tokens conservatively. Frozen assistant response
    # uses the same model/tokenizer; reserve the entire Stage 1 generation budget.
    base = (sum(len(m['content'].encode()) for m in messages(scope, 2, ''))
            + len(json.dumps(schema(2, scope['entries'])).encode()) + 4096)
    budgets = {}
    for model in MODELS:
        item = catalog[model]
        top = item.get('top_provider') or {}
        limit = top.get('max_completion_tokens')
        context = top.get('context_length') or item.get('context_length')
        if not limit or not context or maxout > limit or base + 2 * maxout > context:
            raise ValueError(f'Cannot certify two-call context/output budget for {model}: context={context}, output={limit}, required_context={base + 2 * maxout}')
        settings = {'max_tokens': maxout}
        if model not in omitted:
            settings['temperature'] = config['temperature']
        budgets[model] = {'context': context, 'output_limit': limit, 'required_context': base + 2 * maxout,
                          'structured': 'structured_outputs' in item.get('supported_parameters', []),
                          'generation_settings': settings}
    if not os.environ.get('OPENROUTER_API_KEY'):
        raise ValueError('OPENROUTER_API_KEY is missing')
    write(run / 'preflight.json', {'checked_at': now(), 'budgets': budgets,
                                 'catalog_sha256': digest(raw)})
    return budgets


def successful(folder, stage, entries):
    marker = folder / f'stage{stage}.success.json'
    if not marker.exists():
        return None
    meta = read(marker)
    raw = (folder / f'stage{stage}.validated.json').read_bytes()
    response = (folder / f'stage{stage}.content.txt').read_bytes()
    if digest(raw) != meta['validated_sha256'] or digest(response) != meta['content_sha256']:
        raise ValueError('Frozen stage digest mismatch')
    return validate(json.loads(raw), entries, stage)


def export_model(folder, scope, model):
    one = {r['review_id']: r for r in read(folder / 'stage1.validated.json')['entries']}
    two = {r['review_id']: r for r in read(folder / 'stage2.validated.json')['entries']}
    opens, assessments = [], []
    receipts = {stage: read(folder / f'stage{stage}.success.json') for stage in (1, 2)}
    worksheet = ['# Model-generated annotation worksheet', f'Model: {model}',
                 'Times below are actual orchestration timestamps (UTC).',
                 f"Stage 1 started: {receipts[1]['started_at']}; completed: {receipts[1]['completed_at']}",
                 f"Stage 2 started: {receipts[2]['started_at']}; completed: {receipts[2]['completed_at']}",
                 '\n## Stage 1 (frozen)']
    for e in scope['entries']:
        common = {k: e[k] for k in ('annotation_id', 'requirement', 'propositions')}
        common['annotator_id'] = 'model:' + model
        if e.get('scenario'):
            common['scenario'] = e['scenario']
        opens.append({**common, **{k: one[e['review_id']][k] for k in ('interpretations', 'comments')}})
        assessments.append({**common, 'readings': e['readings'], **{k: two[e['review_id']][k] for k in ('supports', 'additional_interpretations', 'comments')}})
        worksheet += [f"\n### {e['review_id']} / {e['annotation_id']} ({e['source_family']})", e['requirement'], json.dumps(e['propositions']), json.dumps(one[e['review_id']], ensure_ascii=False)]
    worksheet += ['\n## Stage 2']
    for e in scope['entries']:
        worksheet += [f"\n### {e['review_id']}", json.dumps(e['readings'], ensure_ascii=False), json.dumps(two[e['review_id']], ensure_ascii=False)]
    for filename, rows in [('open_interpretations', opens), ('reading_assessment', assessments)]:
        (folder / (filename + '.jsonl')).write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows))
    (folder / 'worksheet.md').write_text('\n'.join(worksheet) + '\n')


def annotate(run, scope, config, transport=request, resume=False):
    run = Path(run)
    run.mkdir(parents=True, exist_ok=True)
    with (run / '.run.lock').open('a') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise ValueError('Another annotation process holds the run lock')
        return _annotate(run, scope, config, transport, resume)


def _annotate(run, scope, config, transport=request, resume=False):
    entries = validate_scope(scope)
    if config['expected_models'] != MODELS:
        raise ValueError('Expected the exact fixed five-model population')
    binding = digest(json.dumps({'scope': scope, 'config': config}, sort_keys=True).encode())
    statepath = run / 'state.json'
    state = read(statepath) if statepath.exists() else {'binding': binding, 'status': 'ready', 'attempts': []}
    if state['binding'] != binding:
        raise ValueError('Run scope/config changed')
    if state['status'] in ('paused', 'in_flight') and not resume:
        raise ValueError('Run paused; explicit --authorize-resume required')
    if state['status'] == 'in_flight':
        raise ValueError('Unknown in-flight outcome: reconcile saved response before resuming; never repeat blindly')
    try:
        budgets = preflight(run, scope, config, transport)
        for model in MODELS:
            folder = run / model.replace('/', '_')
            folder.mkdir(exist_ok=True)
            for stage in (1, 2):
                if successful(folder, stage, entries) is not None:
                    continue
                if stage == 2 and successful(folder, 1, entries) is None:
                    raise ValueError('Stage 1 is not frozen')
                frozen = (folder / 'stage1.content.txt').read_text() if stage == 2 else None
                payload = {'model': model, 'messages': messages(scope, stage, frozen),
                           **budgets[model]['generation_settings'],
                           'stream': False, 'provider': {'allow_fallbacks': False, 'require_parameters': True}}
                if budgets[model]['structured']:
                    payload['response_format'] = {'type': 'json_schema', 'json_schema': {
                        'name': 'annotation', 'strict': True, 'schema': schema(stage, entries)}}
                # A returned response without a success marker requires reconciliation;
                # never issue a second successful annotation after a disk failure.
                for previous in state['attempts']:
                    if previous['model'] == model and previous['stage'] == stage:
                        response_path = Path(previous['request_file'].replace('.request.json', '.response.json'))
                        if response_path.exists():
                            try:
                                prior = json.loads(response_path.read_bytes())
                                choice = prior['choices'][0]
                                if choice['finish_reason'] == 'stop':
                                    validate(parse_json(choice['message']['content']), entries, stage)
                                    raise RuntimeError('A valid returned annotation needs local reconciliation; refusing to repeat successful call')
                            except (ValueError, KeyError, IndexError, TypeError):
                                pass
                index = len(state['attempts']) + 1
                stem = folder / f'stage{stage}.attempt{index:03d}'
                write(str(stem) + '.request.json', payload)
                attempt = {'model': model, 'stage': stage, 'started_at': now(), 'request_file': str(stem) + '.request.json'}
                state['attempts'].append(attempt)
                state['status'] = 'in_flight'
                write(statepath, state)
                raw = b''
                try:
                    raw, headers = transport('POST', '/chat/completions', os.environ['OPENROUTER_API_KEY'], payload, config['timeout_seconds'])
                    Path(str(stem) + '.response.json').write_bytes(raw)
                    Path(str(stem) + '.response.md').write_text('# Original model response envelope\n\n' + raw.decode(errors='replace'))
                    write(str(stem) + '.http.json', {'received_at': now(), 'headers': {k: v for k, v in headers.items() if k.lower() in {'content-type', 'x-request-id', 'request-id', 'date'}}})
                    response = parse_json(raw)
                    attempt['usage'] = response.get('usage')
                    attempt['response_id'] = response.get('id')
                    if response.get('model') != model:
                        raise ValueError('Returned model does not match requested exact ID')
                    choices = response['choices']
                    if len(choices) != 1 or choices[0]['finish_reason'] != 'stop':
                        raise ValueError('Incomplete/truncated response')
                    content = choices[0]['message']['content']
                    Path(str(stem) + '.response.md').write_text('# Original model-generated annotation\n\n' + content)
                    data = validate(parse_json(content), entries, stage)
                    write(folder / f'stage{stage}.validated.json', data)
                    (folder / f'stage{stage}.content.txt').write_text(content)
                    write(folder / f'stage{stage}.success.json', {
                        'model': model, 'stage': stage, 'scope_sha256': digest(json.dumps(scope, sort_keys=True).encode()), 'started_at': attempt['started_at'], 'completed_at': now(),
                        'validated_sha256': digest((folder / f'stage{stage}.validated.json').read_bytes()),
                        'content_sha256': digest(content.encode()), 'attempt': index})
                    attempt['status'] = 'validated'
                    state['status'] = 'ready'
                except BaseException as error:
                    if hasattr(error, 'annotation_partial') or isinstance(error, http.client.IncompleteRead):
                        raw = getattr(error, 'annotation_partial', getattr(error, 'partial', b''))
                        Path(str(stem) + '.response.json').write_bytes(raw)
                    if isinstance(error, urllib.error.HTTPError):
                        raw = error.read()
                        Path(str(stem) + '.response.json').write_bytes(raw)
                    if not Path(str(stem) + '.response.md').exists():
                        Path(str(stem) + '.response.md').write_text('# Failed annotation attempt\n\n' + raw.decode(errors='replace'))
                    attempt['status'] = 'failed'
                    attempt['error'] = type(error).__name__ + ': ' + str(error)
                    raise
                finally:
                    attempt['ended_at'] = now()
                    write(statepath, state)
            export_model(folder, scope, model)
        state['status'] = 'annotations_complete'
    except BaseException as error:
        state['status'] = 'in_flight' if isinstance(error, (KeyboardInterrupt, SystemExit)) and state['status'] == 'in_flight' else 'paused'
        state['error'] = type(error).__name__ + ': ' + str(error)
        raise
    finally:
        write(statepath, state)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run-dir', type=Path, required=True)
    parser.add_argument('--authorize-resume', action='store_true')
    args = parser.parse_args()
    run = args.run_dir
    config = read(run / 'config.json')
    source = Path('candidate_screening/human_annotation.md')
    if not source.is_file():
        parser.exit(2, f'Blocked: missing authoritative worksheet {source}\n')
    if not (run / 'scope.json').is_file():
        parser.exit(2, 'Blocked: worksheet extraction adapter/scope manifest is not yet available.\n')
    scope = read(run / 'scope.json')
    if scope.get('source_sha256') != digest(source.read_bytes()):
        parser.exit(2, 'Blocked: authoritative worksheet hash mismatch\n')
    try:
        annotate(run, scope, config, resume=args.authorize_resume)
    except Exception as error:
        parser.exit(2, f'Paused: {error}\n')


if __name__ == '__main__':
    main()
