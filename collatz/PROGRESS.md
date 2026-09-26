# Current checkpoint

STATUS: IN_PROGRESS
STEP_ID: collatz-2026-09-26-011-nondescending-first-merge
STEP_OUTCOME: ADVANCE
STEP_EVIDENCE: L011 proves common suffixes through depth three and reduces every deeper first merge to adjacent odd-run lengths and two forced (1,2) contractions with paired states z=4y+1; lemmas/L011-nondescending-first-merge-reduction.md. Exact word screening through depth six found no failure.
Bottleneck: Universal eventual descent remains unproved. Even all-depth suffix rigidity for the four-type alphabet is open, and would still not bound non-descent depth from a fixed start or cover other block types.
Route decision: Continue with the forced pair relation from L011; determine whether earlier growth can compensate both contractions while the companion history also stays above its own start. No finite-depth computation is an all-depth estimate.
Exploration turns used: 0 consecutive without ADVANCE/NEGATIVE; this one focused test established a new necessary condition for failures at arbitrary depth.
NEXT_REVIEW: drafts/literature/2026-09-26-current-target.md
Next action: Derive the backward transition rules for (z,y)=(4y+1,y) from L011, retaining their one-block depth offset, and test whether they force descent below one of the two original starting values.
