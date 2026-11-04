# Final five-model annotation dataset

Combined final dataset: [dataset.jsonl](five_model_v1/dataset.jsonl).
All five exact models completed both stages for all 88 source requirements.
The 326 reviewed semantic groups cover all 810 original Stage 1 interpretations.
At threshold 3 out of the fixed 5 models, 66 requirements are retained and 22
excluded. Every requirement remains audited. All 12 negation-scope reading-a
votes tie 2 Supported / 2 Not supported / 1 Uncertain, so that family's paired
files are intentionally empty.

`dataset.jsonl` has one retained requirement per line in source review order.
Each row combines the paired family fields: annotation and annotator IDs,
requirement, propositions, optional scenario, retained interpretations,
readings, aggregate support labels, additional interpretations and comments.
`review_id` and `source_family` identify the requirement across families.
`stage1_groups` includes every reviewed group for that requirement, its original
texts and model memberships, explanation, vote count and retained flag.
`reading_votes` records each model's labels, counts and aggregate decisions.
`stage2_annotations` preserves each model's additions, Stage 2 comments and
separate Stage 1 comments, with `counts_as_stage1_vote: false`. Individual model
additions live there; the top-level `additional_interpretations` retains the
aggregate field from the family output.
Per-row `provenance` records the five exact models, threshold, population and
the same input SHA-256 hashes as metadata. Only eligible requirements appear
in this combined file; the separate audits still cover all 88 requirements.

Family outputs are paired `*_open_interpretations.jsonl` and
`*_reading_assessment.jsonl`. `vote_summary.jsonl` preserves all votes and groups;
`exclusions.jsonl` explains removals; `stage2_additional_interpretations.jsonl`
keeps additions separate from Stage 1 voting. `metadata.json` hashes inputs and
lists all 21 generated files, including the combined dataset.

## Minimal run inputs

`annotation_runs/five_model_v1/` now contains exactly 23 files:

- `config.json`: the five exact models, generation settings and voting threshold.
- `scope.json`: frozen source entries, identities, reading IDs and source hashes.
- `grouping.json`: editable final meanings, exact memberships and explanations.
- Each model's `stage1.validated.json`, `stage2.validated.json`,
  `stage1.success.json` and `stage2.success.json`: ten complete stage datasets
  and ten receipts used to validate model identity, scope and data hashes.

These are the complete dependencies of the existing aggregator. No validation
was removed and the program was not changed to accommodate cleanup.

## Regenerate without network or model calls

From the repository root:

```sh
python -m annotation_pipeline.aggregate --run annotation_runs/five_model_v1 --output annotation_final/five_model_v1
```

Edit `min_agreeing_models` in config.json, or pass `--min-agreeing-models N`,
where N is an integer from 1 through 5. Default is 3. A label must reach threshold
and be the unique highest count; ties and majority Uncertain never qualify.
Eligibility also needs a retained Stage 1 group. Use a fresh output path for a
separate threshold version. Stage 2 additions never become Stage 1 votes.

## Archived provenance

Everything else from the run is preserved locally in the Git-ignored
`annotation_archive/five_model_v1/`: original response text and raw envelopes,
exact requests, state/status, preflight, publication manifest, review records,
old logs, snapshots and duplicate exports. `archive_manifest.json` maps the
first cleanup; `minimal_run_manifest.json` maps the further 37-file reduction.
Both record original paths, archive paths and SHA-256 hashes. Historical paths
inside archived state or `grouping.json` identify original locations; the
manifests locate those records now. No archived file is required by aggregation.
The local archive does not accompany a fresh checkout. Older commits retain
previously tracked artifacts; this cleanup does not rewrite Git history.

This run folder is now **regeneration-only**, not ready for annotation-runner
resumption. Before any annotation runner use, restore the archived original
`state.json` and each stage's `.content.txt` to their original paths; never start
new paid work against the reduced run folder. The annotation task is complete;
there is no need to rerun models to regenerate the dataset.

Known reported usage was 259,564 tokens and $0.139743691. Fifteen attempts
included ten successes, one Claude HTTP 400 and four Qwen HTTP 429 failures.
Failed requests reported no usage/cost. Original stages were never repeated;
failures paused until explicit continuation. Generation settings were 60,000
maximum output tokens, 900-second timeout, temperature 0 for Gemini/DeepSeek/Qwen
and omitted for Claude/GPT. The authorized compact Stage 2 schema applied after
Gemini completed with the original schema. Exact archived requests preserve it.

Verification: all 24 existing tests and compilation pass. The reduced 23-file
run supports offline regeneration. The combined export preserves the 19 existing
family/audit JSONL files byte for byte; only metadata changes to list the new
dataset. Source files, retained inputs and all ten receipts are unchanged.
No paid calls or new tests were needed for this export.
