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
