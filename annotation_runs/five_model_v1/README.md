# Five-model annotation run

Status: **complete; new final dataset published locally** in
../../annotation_final/five_model_v1. All five exact models completed one
validated Stage 1 and one validated Stage 2 covering all 88 entries. There were
15 annotation attempts total: ten successful stages, one Claude Stage 2 HTTP
400 (grammar too large), and four Qwen Stage 1 HTTP 429 upstream rate limits.
Each failure paused globally; subsequent attempts occurred only after explicit
user continuation. No paid test completions, repair calls, automatic retries,
model substitutions or repeated successful stages occurred. Original failed
attempts and authorization histories are preserved.

Known reported usage is 136,672 prompt tokens, 122,892 completion tokens,
259,564 total tokens and $0.139743691 cost. The five failed requests reported
no usage/cost; their costs remain unknown, not assumed zero. This is the only
remaining reporting gap. See status.json, state.json and per-attempt envelopes.

The coordinating Codex agent read all 810 Stage 1 interpretations and reviewed
all draft groups, with four semantic subagents covering R001-R088 and a final
independent semantic auditor. Editable grouping.json contains 326 stable groups,
canonical meanings, exact original texts, model/index memberships and merge/
separation explanations. Every original appears once. Review records and
coordinator/auditor refinements are in semantic_review. No Stage 2 label or
aggregation outcome was used to choose group membership; Stage 2 additions
remain separate and never count as independent Stage 1 votes.

At the default threshold of three distinct models out of the fixed five,
66 requirements are eligible and 22 excluded. Five lack a threshold Stage 1
group; 17 have unresolved reading-a labels. All 12 negation_scope entries have
2 Supported / 2 Not supported / 1 Uncertain on reading a, so that family's paired
files are intentionally empty. All 88 requirements remain in vote_summary.jsonl
and all exclusions are explained in exclusions.jsonl. No tie is broken.

Family retained counts: joint_separate 11; negation_scope 0; next_later 6;
or_scope 9; order_scope 9; same_later 10; trigger_scope_final 10;
until_termination 11. The output has paired family JSONL, full vote/exclusion
audits, 440 separate model/requirement Stage 2 addition rows, and hashed metadata.
publication_manifest.json records the final file hashes.

Critical paid-call protection fixes: explicitly omit unsupported temperature only
for Claude Haiku 5.5 and GPT 5.6 Luna, and compact Stage 2's strict grammar from
51,446 to 694 bytes. Gemini's successful Stage 2 retains the original schema;
all later successful Stage 2 calls use the authorized compact schema. Exact
requests preserve this difference. Stage 1 prompts/schema stayed unchanged.
Generation settings are max output 60,000, timeout 900 seconds, temperature 0
for Gemini/DeepSeek/Qwen and omitted for Claude/GPT. Provider defaults apply to
unspecified settings. Routing disables fallbacks and requires parameter support.
Catalog and preflight save actual model/context/output limits and settings;
current conservative required context is 170,977, within all five limits.

Verification: all 24 existing/critical regression tests passed before the final
paid continuation; Python compilation passed. All ten success receipts and
source hashes validate, previous stages remain unchanged, grouping covers all
810 originals exactly once, five-model counts/threshold/ties and paired family
IDs pass artifact checks. A socket-blocked regeneration produced byte-identical
files. See verification.txt. Original raw response envelopes retain provider keepalive
whitespace byte for byte; the whitespace check passes for code, docs and
generated data when those raw envelopes are excluded. No source forms, original reading IDs, worksheet,
formulas or solver reports were modified. Historical catalog/preflight/failure
files document earlier checks and are not the current run status.

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
The default output budget is 60,000 tokens, temperature 0 where supported, timeout 900 seconds;
preflight blocks if the catalog cannot certify this budget. Settings and source
are bound to the run, so change generation settings only before annotation.

The completed editable grouping.json uses this schema (all originals have
already been reviewed; edit and regenerate locally to revise grouping):

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
