# Completed five-model annotation run

All five exact models completed both stages for all 88 requirements. The reviewed
326 semantic groups cover all 810 Stage 1 interpretations exactly once. At the
default threshold of 3 distinct models out of 5, the final dataset retains 66
requirements and excludes 22. See [final dataset](../../annotation_final/README.md).

Known reported usage: 259,564 tokens and $0.139743691. There were 15 attempts:
10 successful stages, one Claude HTTP 400 and four Qwen HTTP 429 failures. Failed
requests reported no usage/cost; those costs remain unknown. Each failure paused
the run and continuation required explicit user authorization. No successful
stage was repeated and no paid test completion was made.

## Files kept in Git

This completed run keeps 60 core files:

| Files | Why kept |
| --- | --- |
| `config.json`, `scope.json`, `grouping.json` | Frozen source identity, generation/voting settings and editable reviewed meanings; direct regeneration inputs. |
| Each model's `stage1/2.validated.json` and `stage1/2.success.json` | Complete annotations and hashed receipts required by aggregation. |
| Each model's `stage1/2.content.txt` | Exact original response text checked by the runner; preserves frozen Stage 1. |
| Successful `stage*.attempt*.request.json` and `.response.json` | Exact paid prompts/settings and original response envelopes, including usage and provider metadata. |
| `state.json`, `status.json` | Completion/resume protection, attempt history and concise final results/cost summary. |
| `preflight.json` | Compact record of actual model limits, effective settings and catalog hash. |
| `semantic_review/coordinator_review.json`, `semantic_review/final_audit.json` | Final review scope, decisions and independent audit conclusion. |
| `publication_manifest.json` | Hashes of final dataset files and core regeneration inputs. |
| This README | Commands, file decisions and known limitations. |

Source worksheets/forms, pipeline code/tests and every final dataset file remain
in Git. Empty negation-scope family files are intentional: all 12 requirements
have a 2 Supported / 2 Not supported / 1 Uncertain tie for reading `a`.

## Local archive

111 redundant run files were moved, without changing their bytes, to
`annotation_archive/five_model_v1/` at the repository root. That directory is
Git-ignored. Its `archive_manifest.json` records each original path, archive path,
size and SHA-256, plus pre-cleanup hashes of retained inputs and final outputs.
Previous versions of this README and the pipeline plan are also archived, along
with two earlier workspace diagnostics created during environment recovery.

Archived categories: old failure/preflight logs, full public model catalog,
HTTP debug headers, response Markdown wrappers, duplicate per-model JSONL and
worksheets, historical state/code/config snapshots, obsolete continuation GOAL,
console verification logs, semantic review inputs/draft groups/working notes,
and the inactive run lock. The completeness summary duplicates final status and
success receipts, so it is archived too.

The original state and review records were not rewritten. Their historical paths
to failed attempts, snapshots and review drafts identify where files were at run
time; use the archive manifest to locate them now. The catalog hash in
`preflight.json` refers to the archived complete catalog. None of these archived
files is required to regenerate the dataset or validate completed stages.
The archive is local-only and is not included in a fresh Git checkout. Earlier
commits still contain the old artifacts; this cleanup does not rewrite history.

## Regenerate without network or model calls

From the repository root:

```sh
python -m annotation_pipeline.aggregate --run annotation_runs/five_model_v1 --output annotation_final/five_model_v1
python -m annotation_pipeline.aggregate --run annotation_runs/five_model_v1 --output annotation_final/five_model_v1_t4 --min-agreeing-models 4
```

Edit `min_agreeing_models` in config.json to change the default, or pass
`--min-agreeing-models N` for one regeneration. N must be an integer from 1 to 5.
A reading label must reach threshold and be the unique highest count; ties and
majority Uncertain never qualify. Eligibility also requires a retained Stage 1
group. Stage 2 additions stay separate and never become Stage 1 votes. Use a
fresh output directory for a separately published threshold version.

Generation settings: 60,000 maximum output tokens, 900-second timeout,
temperature 0 for Gemini/DeepSeek/Qwen and omitted for Claude/GPT. Stage 1 prompts
and schema were unchanged. Gemini's successful Stage 2 used the original schema;
later stages used the authorized compact schema (51,446 to 694 bytes). Exact
successful requests preserve that difference. Routing disabled fallbacks and
required parameter support. Unspecified settings used provider defaults.

## Verification and completion safety

All 24 existing/critical tests and Python compilation passed. Final verification
checked all ten receipts, all source hashes, exact grouping coverage, fixed
five-model voting, paired family IDs and byte-identical network-free regeneration.
The cleanup additionally verifies moved-file hashes and regenerates from retained
files in an isolated temporary run directory with network access blocked.

The annotation runner is already complete; do not rerun paid calls to regenerate
outputs. Successful stages remain at their original paths with unchanged hashes.
`state.json` retains the completed binding and attempt history. A future runner
invocation can recreate archived diagnostic/derivative files; that does not make
them required inputs. Runtime `.run.lock` files are ignored. No dependencies or
database migrations were added. Never put OPENROUTER_API_KEY in tracked files.
