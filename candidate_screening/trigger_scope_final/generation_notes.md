# Trigger-scope generation notes

Final candidate source: `trigger_scope_candidates.jsonl` (10 records).
Final reports: this directory. Earlier 12-record reports in `../trigger_scope` are superseded and preserved for provenance.

The request sought 15–20 candidates, but structurally distinct, plausible candidates were not padded to reach that range. Two initial structures were excluded after review:

- `trigger_scope_005`, eventual permanence: `F(a & F G b)` versus `G(a -> F G b)`.
- `trigger_scope_006`, recurring response: `F(a & G F b)` versus `G(a -> G F b)`.

For both, the formulas agree on every trace containing a trigger. They differ only in whether a trigger must exist, which is too weak a realization of one-response-versus-every-response for this batch. The numerical ID gaps preserve provenance.

The family overlaps `order_scope` in existential versus universal trigger quantification; temporal strictness alone does not establish an independent linguistic mechanism. Some generic-singular sentences may strongly favor the universal reading. Strong/weak release, immediate timing, and enable/stop contexts are held fixed within each contrast.

Both final commands passed:

```
/opt/miniconda3/envs/ltl/bin/python check_candidates.py candidate_screening/trigger_scope_final/trigger_scope_candidates.jsonl --out-dir candidate_screening/trigger_scope_final
/opt/miniconda3/envs/ltl/bin/python dataset_checks.py candidate_screening/trigger_scope_final/trigger_scope_candidates.jsonl --stage candidates
```

Spot 2.16: 10 checked, 10 eligible, 0 equivalent pairs, 0 errors. Dataset checks: 0 issues.
These are candidate-screening outcomes, not human acceptance. Formula-to-English fidelity, linguistic plausibility, rewrite clarity, and semantic distinctness across records remain unvalidated. No scripts or configuration were changed.
