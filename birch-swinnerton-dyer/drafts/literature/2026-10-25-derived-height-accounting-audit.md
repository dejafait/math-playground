# Derived-height accounting — proposed critical audit coverage

TARGET: Audit L118's finite derived-height formula for delta against Howard's exact Selmer conventions, tower hypotheses and all localization and termination steps.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 489 reuses the 2026-10-04 full-Selmer and 2026-10-25 specialization/duplicate reviews; read L118 and L002 fully and checked ATTEMPTS/002 and ATTEMPTS/031 plus L019's recorded obstruction. No changed theorem target requires fresh broad discovery.
SOURCE_EVIDENCE: Reopened Howard arXiv:1202.6343v1 (2012-02-28), Section 3 setup and Propositions 3.4--3.5 with all local proof cases, Section 4 equation (9), Lemma 4.1 with proof, Theorem 4.2 with proof and Corollary 4.3 with proof, printed pp.12--17 (PDF pages 12--17).
COMPARISON: Howard gives the filtered-space dimensions and augmentation-block interpretation; L002 gives localized finite-length blocks. L118's proposed finite accounting is their standard specialization, not a new height theorem.
GAP: The newly written L118 proof has not received a separate critical audit of source applicability, inverse-limit identification, localized layer counts and treatment of the zero/free/error cases.
REASON: A separate check can detect a wrong Selmer identification or discarded augmentation contribution before the formula is used; the existing assessment covers the mathematics, so no new discovery search is proposed.
SCOPE: Audit only L118 under its stated hypotheses, using L002 and the already inspected primary Howard theorem; no finite Sha, residual conditions, rational-point replacement, height nondegeneracy or complex-order comparison may be added.
LITERATURE_REASON: The supervisor requires separate approval of the newly saved audit assessment; this turn checks the essential source cases and exact scope before research resumes, without reopening the ready theorem discovery.

Step 489 completes the separate source-coverage approval. The exact TARGET
is ready for one research audit; its mathematical verdict remains pending.
No audit has been performed or certified by approving this assessment.
The anticipated completed-step classification is REPRODUCTION.

Reuse [the prior assessment](2026-10-25-derived-height-defect-accounting.md)
and [Howard's primary text](https://arxiv.org/pdf/1202.6343v1#page=15).
The audit must read the full [canonical specialization](../../lemmas/L118-derived-height-augmentation-defect-accounting.md)
and L002's exact hypotheses/proof, then verify each source input in its
actual scope. In particular distinguish the compact inverse coefficient
limit from the discrete infinite-level group, and dimension equalities
from canonical identifications. Check the cyclotomic bad-prime condition,
the zero module, torsion/free part, nonaugmentation factors and
finite/pseudo-null errors. Check that every direct mathematical input is
represented in DAG.md and that no rational-rank assertion was smuggled in.

Continue if the exact finite identity survives; repair or withdraw its
unsupported scope if any load-bearing identification fails. Even a
successful audit leaves production of arithmetic layer bounds, Sha
corank control and complex-order comparison unresolved. The former
formal radical-to-Sha inference remains obstructed by L019.

## Source comparison completed in step 489

Primary retrieval covered the complete stated comparison passages, rather
than relying on search snippets. Proposition 3.4 matches the classical
infinite-level group. Proposition 3.5 treats good primes away from p, bad
primes away from p, and primes above p separately. Its first-arrow bound
also uses ramification above p. These are the local cases the audit must
match; finite-coefficient equality is not an imported claim.

Section 4 defines coefficient transitions by multiplication by p.
Equation (9) supplies ranks for each filtration index; no bound uniform
in that index should be presumed. Lemma 4.1 uses bounded comparison
maps and the finite-level torsion kernel to reach compact Selmer spaces
after rationalization. Theorem 4.2 gives dimensions and successive
pairing kernels. Its proof imports the discrete-coefficient properties;
the additional argument addresses universal norms. Corollary 4.3 retains
the free contribution, separately from augmentation blocks.

Coverage therefore permits the saved audit without a new arithmetic
theorem search. It does not certify L118's tower verification,
localization, summation or treatment of errors. Test these arguments
directly, including fixed-index versus simultaneous termination. The
source-level hypotheses are accessible; no essential source blocker
remains for this bounded target. The stronger rationality inference and
ordinary-to-strict localization route remain outside this approval.

## Mathlib

Full arithmetic filtration theorem and supporting library matches remain
not checked. Howard supplies the imported arithmetic theorem; no new
Mathlib absence claim is part of this audit target.
