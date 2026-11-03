# Continuing task prompt

Complete the reproducible five-model annotation run for the 88 entries in
candidate_screening/human_annotation.md, then publish the new locally generated
final dataset. Continue from the existing implementation rather than recreating
it. Read AGENTS.md, annotation_pipeline/PLAN.md, and this run's README.md first.

## Work already completed

- Implemented worksheet extraction in annotation_pipeline/prepare.py. scope.json
  freezes all 88 entries, administrative mappings, original reading IDs, and
  source hashes. It uses trigger_scope_final and preserves all source files.
- Implemented the serial two-stage runner in annotation_pipeline/runner.py with
  frozen Stage 1 responses, catalog-only preflight, context/output checks,
  saved prompts/responses/provenance, global failure pause, no automatic retries,
  concurrent-run protection, and resumability from successful stages.
- Implemented network-free regeneration in annotation_pipeline/aggregate.py,
  with editable reviewed semantic groups, fixed five-model voting, threshold
  overrides, tie preservation, paired family outputs, votes and exclusion audits.
- Added 19 tests covering critical behavior and a mocked ten-call end-to-end run.
  All 19 passed; Python compilation passed. Auditor subagents reviewed the code
  and the identified blocking implementation issues were fixed.
- No paid annotation calls have run. No real model stages, reviewed grouping,
  or final dataset exist. No secrets were printed or saved.

## Remaining work

1. Recheck the active environment and OpenRouter catalog. The last check found
   enforced configuration revision 1 with no custom allowed hosts and a proxy
   403 for openrouter.ai, despite the user's updated published configuration.
   OPENROUTER_API_KEY was reported ready. Availability of the exact model IDs
   and their context/output limits remains unverified. Do not bypass the proxy.
2. Before any paid annotation calls, run the existing mocked checks and inspect
   failures, scope integrity, exact model availability, generation settings,
   and both stages' context/output budgets so paid calls are not wasted. Do not
   send paid test completions. If prerequisites fail, save diagnostics and pause.
3. Run exactly one complete Stage 1 call and one complete Stage 2 call per model:
   google/gemini-3.8-flash, anthropic/claude-haiku-5.5, openai/gpt-5.6-luna,
   deepseek/deepseek-v4.1-flash, qwen/qwen3.8-flash. Do not substitute models.
   Supply no Stage 2 readings before that model's complete Stage 1 is validated
   and persisted. Preserve Stage 1 unchanged. Models must not inspect repository
   files, other responses, formulas, assessments, solver reports or aggregation.
4. On any annotation failure, preserve all available data, stop all further
   calls, report stage/reason/known usage or cost, and wait for explicit user
   continuation. Do not retry automatically, batch, or make repair calls. Never
   repeat successful stages; reconcile unknown in-flight outcomes locally.
5. After all five complete, coordinating Codex and a subagent must semantically
   review all Stage 1 interpretations and create editable grouping.json with
   stable group IDs, canonical meanings, original texts, model memberships and
   explanations. Preserve differences in scope, quantification, simultaneity,
   timing inclusivity, endpoints, termination and vacuity. Stage 2 additions
   remain separate and never become independent Stage 1 votes.
6. Regenerate final family-partitioned JSONL and all audits. Default threshold
   is 3 distinct models out of the fixed 5. A reading label must meet threshold
   and be the unique highest count; ties are unresolved. A requirement needs
   a retained Stage 1 group and qualifying Supported/Not supported labels for
   every reading. Majority Uncertain does not qualify. All five models must
   pass completeness validation before a complete final dataset is published.
7. Report status, key changes, configuration, actual verification outcomes,
   remaining issues, exact annotation/regeneration commands and how to change
   the threshold (config.json or --min-agreeing-models, integer 1 through 5).

## Testing policy (updated by user)

Only write new tests when something breaks, or when a test is needed before
paid calls to prevent wasting paid calls. Reuse the existing tests; do not add
routine tests for unrelated changes or documentation edits. Before paid calls,
run the existing mocked end-to-end and critical validation checks and resolve
any failure first. Never spend OpenRouter credits to test the pipeline.
