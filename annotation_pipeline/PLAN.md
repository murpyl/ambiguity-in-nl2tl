# Five-model annotation plan

1. Freeze the authoritative worksheet's 88 entries, administrative mappings,
   original reading IDs and source hashes in an allowlisted scope manifest.
2. Run the exact five configured models serially. Validate and persist each
   complete Stage 1 before supplying Stage 2 readings. Preserve successful
   responses, exact prompts, receipts and completion state; never repeat success.
3. Certify model/settings/context/output prerequisites using the public catalog,
   without paid test calls. Pause globally on failure and require explicit user
   continuation. Keep concurrent-run and unknown-outcome protections.
4. Have the coordinator and semantic subagents review every Stage 1 interpretation.
   Preserve scope, timing, quantification, endpoints, termination and vacuity in
   editable groups. Keep Stage 2 additions separate from Stage 1 votes.
5. Regenerate locally with the fixed five-model population. Default threshold is
   3/5; reading labels require a unique highest qualifying count. Preserve ties,
   exclusions, family pairs and complete vote audits.
6. Reuse existing mocked and critical checks. Add tests only for failures or to
   prevent wasted paid calls. Never spend OpenRouter credits on pipeline tests.

Completed dataset and regeneration instructions: [five_model_v1](../annotation_final/README.md).
All ten stages completed; 810 interpretations form 326 reviewed groups. The final
threshold-3 dataset retains 66/88 requirements with all 88 audited. Authorized
fixes omit unsupported temperature for Claude/GPT and compact the Stage 2 schema.
Original sources and successful stages remain unchanged.

Cleanup plan: keep only the 23 files consumed by offline aggregation in
annotation_runs/five_model_v1: config, scope, final grouping, and the validated
data/success receipt for each of ten model stages. Preserve all other run data
and provenance in the ignored annotation_archive directory with relocation
hashes. The reduced run is regeneration-only; original state and response text
must be restored before any annotation runner use. Keep all final outputs and
verify byte-identical regeneration in isolation with network blocked. Make no
model calls, code changes or new tests.

Combined export plan: extend offline aggregation to write `dataset.jsonl`, one
eligible requirement per line in source review order. Combine existing paired
family fields with global review/family identity, all Stage 1 group audits,
reading votes, per-model Stage 2 additions/comments and input-hash provenance.
Preserve voting, run inputs and existing family/audit JSONL files unchanged.
Include the new file in generated metadata and use the same regeneration
command documented in annotation_final/README.md. Reuse the existing 24 tests
and compilation checks; make no model calls or new routine tests.
