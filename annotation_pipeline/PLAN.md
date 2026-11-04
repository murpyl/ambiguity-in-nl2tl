# Five-model annotation plan

1. Inspect repository instructions, authoritative worksheet, mappings, and schemas.
   Initial inspection (before user push): no AGENTS.md existed in this checkout. Existing forms in check_candidates.py
   establish interpretation lists and reading-ID keyed supports dictionaries.
2. Freeze an allowlisted scope manifest extracted from human_annotation.md: 88
   unique review IDs, administrative identities/families, Stage 1 instructions,
   requirements/propositions, Stage 2 instructions/readings. Hash the source.
   Do not infer missing source content. This step was initially blocked: the
   entire candidate_screening directory is absent from HEAD and origin/main.
3. Implement a serial, fail-closed two-call runner with catalog-only preflight,
   conservative context/output budgets, immutable successful stages, original
   response Markdown, raw metadata, no retries, and explicit resume authorization.
4. Independently implement deterministic local aggregation and editable semantic
   grouping validation. Require all five completed models; retain all votes and
   exclusion reasons. Use the fixed population and unique-model counts.
5. Before paid calls, reuse the existing mocked full-run fixtures, including isolation, invalid responses,
   failure pause/resume, threshold ties, grouping coverage, paired output IDs,
   and offline regeneration. Have independent auditor subagents review changes.
6. Only after source recovery, catalog availability, credential/network checks,
   budget validation, and tests: run exactly two annotation calls per model.
   Pause globally on any failure. No test completions or repair calls.
7. After actual completion, coordinator and subagent review every Stage 1
   interpretation semantically; save editable groups with explanations. Keep
   Stage 2 additions separate. Regenerate and verify family-partitioned outputs.

Current blockers: missing authoritative worksheet/mappings/blank source forms;
OpenRouter is absent from enforced network allowlist, and the configured proxy
is unreachable. Credentials are reported ready by managed environment status.
No paid annotation calls are authorized past these preflight blockers. Preparation
must not be described as a completed annotation run or final dataset.

Update after user push: fetched and fast-forwarded to f7fe173; AGENTS.md and
worksheet are now available. Source extraction proceeds from the recovered
worksheet. Supported network permission fixed Git connectivity, but the
OpenRouter public catalog is denied by proxy policy with HTTP tunnel 403.

Current continuation goal is saved in
../annotation_runs/five_model_v1/GOAL.md. The source-recovery blocker above is
resolved: all 88 entries are now frozen. The remaining observed blocker is the
active environment proxy denying the OpenRouter catalog with HTTP tunnel 403.

Updated testing policy: only write new tests when something breaks, or when
needed before paid calls to prevent wasted calls. Reuse existing tests and run
the mocked end-to-end and critical validation checks before paid annotation.
Do not create routine tests for documentation edits or unrelated changes.

Continuation preflight: the live catalog advertises no temperature parameter
for Claude Haiku 5.5 or GPT 5.6 Luna, while the frozen configuration requests
temperature 0 with require_parameters enabled. Add a critical preflight guard
and regression before paid calls; preserve configuration and pause on this
unsupported setting rather than spending credits or silently changing sampling.

Authorized continuation: user approved omitting unsupported temperature only for
Claude Haiku 5.5 and GPT 5.6 Luna. Add explicit omit_temperature_models config,
validate its known unique model IDs, record effective per-model settings in
preflight, and use those exact settings in requests. Preserve temperature 0 for
the other three models and the existing output/timeout budgets. Reuse mocked
end-to-end checks and add only the paid-call protection regression before calls.

Authorized grammar fix: Claude Stage 2 returned HTTP 400 because the compiled
88-branch strict schema was too large. Replace review-ID branches with a shared
row schema and support shapes deduplicated by reading-ID keyset. Preserve Stage
1 prompts/schema and frozen responses. Keep exact 88-entry/ID/reading-label
validation locally. Before resuming, test schema compactness, validation rejection
and mocked failure/resume preserving the three successful stages. Resume only
after independent audit; retain the failed attempt and all successful artifacts.

Completion: all five exact models finished both validated stages after explicit
user-authorized continuations. Coordinator and four semantic review subagents
reviewed all810 originals; final independent audit refinements are recorded.
Final326 groups preserve exact membership and stable IDs. Network-free
regeneration at threshold3 retained66/88, with all88 audited and22 exclusions.
No original source files or successful stages were changed.
