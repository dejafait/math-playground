# Fixed-depth witness — critical audit working record

STEP_ID: BSD-2026-10-05-046-positive-valuation-critical-audit

Approved target: Critically audit L023's fixed-depth two-prime valuation-h witness under L021's hypotheses for every m > h, checking coefficient identification, eligible prime selection, both dual localizations, strict/transverse equality and actual Sakamoto scalar normalization.

Prior assessment: drafts/literature/2026-10-05-positive-valuation-specialization-critical-audit.md (SPECIALIZE).

Main gap: rational rank versus complex order at analytic rank at least two. The intermediate target is correctness of L023's conditional finite-depth witness. Its plausible downstream use is a Selmer construction retaining finite index after inverting p; neither rational membership nor complex comparison follows.

Test: retain the claim only if two eligible selections preserve F, the modified structures are self-dual, and the actual Sakamoto basis scalar has valuation h for every m > h. Include h=0 and m=h+1; record a failure instead of strengthening the depth or inserting an unknown normalization factor.

Read L021/L023 in full, ATTEMPTS/021, the prior restricted-index assessment and the original attempt record. Preexisting changes are preserved. The explicit finite-module kernel computation checks out. Mazur--Rubin Proposition 3.6.1's p>4 branch allows repeated primal/dual classes; Lemma 4.1.7(ii) concerns the dual transverse/strict equality, so self-duality is essential. Primary verification is part of this covered proof audit, not expanded literature discovery.

Unfinished: complete the checks of the precise prime-set hypotheses, coefficient-induced local conditions, modified Cartesian/self-dual conditions and Sakamoto's basis/Fitting identity. No audit verdict is recorded yet. No calculation script is needed.

## Completed audit

The saved unfinished checks are now complete in canonical L023's proof,
including its dated critical-audit paragraphs. Its conditional conclusion
survives for every m>h; the statement and DAG inputs are unchanged.
Made the induced Kummer local conditions and persistence of Cartesianity
explicit. Checked both boundary cases and the actual family's scalar
normalization. These are applicability checks of known results, not a
new theorem beyond the assessed sources. No BSD candidate is asserted.

The next proposed target concerns the actual prime-deletion cohomology
classes, which this scalar audit does not cover. Its separate assessment
is marked REVIEW_REQUIRED; no class-extraction assertion is approved or
derived in this turn. See PROGRESS.md for the sole current next action.
