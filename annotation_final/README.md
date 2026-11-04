# Final five-model annotation dataset

Published local dataset: [five_model_v1](five_model_v1/metadata.json).

All five exact models completed both stages for all 88 source requirements.
The reviewed consensus retains 66 requirements and excludes 22 at threshold 3
out of the fixed population of 5. Every source requirement remains audited.
The negation_scope family has empty paired files because all 12 reading-a votes
tie 2 Supported / 2 Not supported / 1 Uncertain; ties remain unresolved.

Family files are paired *_open_interpretations.jsonl and
*_reading_assessment.jsonl. vote_summary.jsonl preserves all votes and reviewed
groups; exclusions.jsonl explains removals; stage2_additional_interpretations.jsonl
keeps additions separate from Stage 1 voting. metadata.json hashes inputs.

From the repository root, regenerate with no network or model calls:

```sh
python -m annotation_pipeline.aggregate --run annotation_runs/five_model_v1 --output annotation_final/five_model_v1
```

Change min_agreeing_models in annotation_runs/five_model_v1/config.json, or use
--min-agreeing-models N with integer N from 1 through 5. Default is 3; a label
must reach threshold and be the unique highest count. Majority Uncertain never
qualifies a reading. Use a fresh output path for a separate threshold version.

Full provenance, costs, generation settings, commands, editable grouping and
semantic review records: [run README](../annotation_runs/five_model_v1/README.md).
