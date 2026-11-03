# Five-model annotation run

Status: **blocked before paid annotation**. The authoritative worksheet was
recovered by fetching the user's update (`f7fe173`). The managed environment
reports OPENROUTER_API_KEY ready. OpenRouter's public catalog request fails at
the configured proxy: `Tunnel connection failed: 403 Forbidden`.
`openrouter.ai` needs to be added to the managed environment network allowlist.
No catalog availability, context limits, model usage, or cost has been verified.
Zero paid annotation calls have been made; zero stages are completed. No final
dataset or semantic grouping exists. See catalog.failure.json for actual time.

The critical implementation parts are source extraction, frozen two-stage
orchestration, reviewed semantic grouping, and deterministic aggregation. Code
and tests live in ../../annotation_pipeline. PLAN.md records the plan before
coding. No dependencies or database migrations are required (Python 3.10+ on
Linux). Never put OPENROUTER_API_KEY in tracked files or print it.

GOAL.md contains the updated continuing task prompt and remaining work. Only
write new tests when something breaks, or when needed before paid calls to
avoid wasted calls. Reuse the existing suite; before paid calls, run its mocked
end-to-end and critical validation checks and resolve all failures. Do not add
routine tests for documentation changes or use paid completions for testing.

From the repository root:

```sh
python -m annotation_pipeline.prepare --run-dir annotation_runs/five_model_v1
python -m unittest discover -s annotation_pipeline -p 'test_*.py' -v
python -m annotation_pipeline.runner --run-dir annotation_runs/five_model_v1
```

The runner first checks the public OpenRouter model catalog, exact five IDs,
credential presence, and conservative context/output budgets for both calls.
It makes no paid test requests. Every Stage 1 request contains all 88 entries
and no proposed readings. Only after all 88 responses validate and are saved
does Stage 2 receive the original frozen response plus all 88 proposed-reading
entries. A run lock prevents concurrent duplication. Raw response envelopes,
original response Markdown (including invalid attempts), exact request bodies,
settings, actual timestamps, usage, errors, and hashed success receipts are
saved in each model folder. No SDK retries, repair calls, batching, substitution,
or automatic retries occur. The runner is serial, so no later call is in flight
when a failure occurs. State and completed stages survive a stop.

After any failure, inspect state.json and saved responses and obtain explicit
user authorization before continuing:

```sh
python -m annotation_pipeline.runner --run-dir annotation_runs/five_model_v1 --authorize-resume
```

Validated stages are skipped. An unknown interrupted in-flight request or a
valid returned response without a completed success receipt requires local
reconciliation before another call; the runner refuses to repeat that call.
The default output budget is 60,000 tokens, temperature 0, timeout 900 seconds;
preflight blocks if the catalog cannot certify this budget. Settings and source
are bound to the run, so change generation settings only before annotation.

After all five models complete, the coordinating Codex agent and a subagent
must review every original Stage 1 interpretation and write grouping.json:

```json
{
  "reviewed_by": ["coordinating Codex agent", "semantic review subagent"],
  "groups": [{
    "group_id": "R001-G001",
    "review_id": "R001",
    "canonical": "Canonical meaning, written after semantic review",
    "explanation": "Explain merges and relevant separations",
    "members": [{
      "model": "google/gemini-3.8-flash",
      "interpretation_index": 0,
      "text": "Exact original Stage 1 interpretation"
    }]
  }]
}
```

This is a format example, not an annotation or a proposed grouping decision.
Use stable group IDs; cover every original interpretation once and preserve
original text. Count each model at most once per group. Merge only equivalent
meanings, preserving temporal scope, quantification, simultaneity, strict versus
inclusive timing, endpoints, termination and vacuity. Do not use string
similarity or OpenRouter to make grouping decisions. Stage 2 additions are
recorded separately and never count as independent Stage 1 votes. Grouping is
editable; correcting it needs no model calls.

Default aggregation rules (config.json min_agreeing_models = 3):

- Retain Stage 1 semantic groups supplied by at least three distinct models.
- Count Supported, Not supported and Uncertain separately for each reading.
  A label qualifies only if it reaches the threshold and is the unique highest
  count. Ties remain unresolved, including with lower thresholds.
- Include a requirement only with at least one retained group and qualifying
  Supported or Not supported labels for every reading. Majority Uncertain
  does not satisfy eligibility.
- Keep the fixed five-model population. Missing or invalid annotations never
  lower the denominator or become negative votes. Regeneration requires all
  five models' complete validated stages and reviewed grouping.

Offline regeneration (no network or API calls):

```sh
python -m annotation_pipeline.aggregate --run annotation_runs/five_model_v1 --output annotation_final/five_model_v1
python -m annotation_pipeline.aggregate --run annotation_runs/five_model_v1 --output annotation_final/five_model_v1_t4 --min-agreeing-models 4
```

To change the default permanently, edit `min_agreeing_models` in config.json
from `3` to an integer `1` through `5`, then regenerate. The override changes
one regeneration only. Generated metadata records the effective threshold.
Output files are partitioned by source family with paired eligible annotation
IDs, explicit aggregate annotator identity, full vote/group audits, exclusions,
and separate Stage 2 additions. Source files and blank forms remain untouched.
Use a fresh output directory for each published version: replacement of an
existing generated directory is validated but is not fully crash-atomic.
