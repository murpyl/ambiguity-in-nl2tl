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

Completed run: [five_model_v1](../annotation_runs/five_model_v1/README.md).
All ten stages completed; 810 interpretations form 326 reviewed groups. The final
threshold-3 dataset retains 66/88 requirements with all 88 audited. Authorized
fixes omit unsupported temperature for Claude/GPT and compact the Stage 2 schema.
Original sources and successful stages remain unchanged.

Cleanup plan: retain code/tests, all final outputs and the 60 run files required
for regeneration, frozen-stage validation and successful-call provenance. Move
redundant logs, exports, historical snapshots and review drafts into the ignored
annotation_archive directory without deleting data. Preserve original state paths
as history and record relocation hashes. Verify unchanged evidence and isolated,
network-free regeneration from retained files; make no model calls or new tests.
