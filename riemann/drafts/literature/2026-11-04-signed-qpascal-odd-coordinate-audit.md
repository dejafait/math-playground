# Actual odd-coordinate obstruction — proposed critical audit

TARGET: Critically audit L774's eventual negative e_1 coordinate at k=r-1, including adjacent finite-value error amplification and determinant-transfer signs.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the signed-matrix comparison in drafts/literature/2026-11-04-signed-qpascal-symmetric-part-review.md and the exact calculation assessment in drafts/literature/2026-11-04-signed-qpascal-odd-coordinate-test.md; no expanded theorem search or novelty claim in step415.
SOURCE_EVIDENCE: Direct primary sources rechecked 2026-11-04: https://arxiv.org/html/2007.13582v2#S1 Theorem1.4/(1.2)/(1.8); https://arxiv.org/html/2607.16795v1#S4 Lemma4.1 and proof, with (6)/Section6 at https://arxiv.org/html/2607.16795v1#S5 and https://arxiv.org/html/2607.16795v1#S6; https://arxiv.org/html/2601.18977v1#S4 Lemmas4.1/4.2 and proofs. Earlier Section7 asymptotic proof-case assessment is reused unchanged.
COMPARISON: The audit has exactly the actual coefficient, finite normalization and integer-asymptotic hypotheses covered by the prior SPECIALIZE assessment; L774's new proof is the object to check, not a new imported input. No tail theorem or new determinant theorem is needed.
GAP: Source-scope approval is complete in step416; mathematical verification of L774's cancellation, O(log(k)^2/k) adjacent-defect error, positive normalizer and reversal factors remains undone.
REASON: Step416 separately approves this exact audit scope and repairs its missing direct URLs, reusing ready coverage. Next turn should perform the audit without another approval loop; neither this approval nor retrieval certifies L774 or reopens accretivity.
SCOPE: Exactly L774 with k=d=r-1 and e_1; no new vector family, model, preconditioner, theorem, scan, effective onset or full source-manuscript audit.

The continuation inputs are L018/L021 for actual coefficients and
L765's explicitly stated finite-value expansion and corrected finite
normalization. Do not import L765's k=1024r endpoint conclusion at the
new center. The original calculation assessment remains the coverage
baseline. The new source comparison should reuse its ready evidence,
checking only that the audit stays within those covered hypotheses.

In the mathematical audit, verify all of L774's proof, particularly:
row1 of L^(-1), |D_1|, the constant-term cancellation in Q_r,
the exact error combination for both adjacent defects, the uniform
explicit-main-term bounds, the positive normalization and strict limiting
sign. No bounded coefficient index enters this coordinate asymptotic.
Check the extension of the finite factorization to the full boundary
matrix with a_0>0, the direction of rho normalization and the cancellation
of the column-reversal/signature signs. Cite the existing determinant
theorem rather than reprove it.

Pass only if eventual Q_r<0 follows with a vanishing error and no hidden
positivity premise. A passing audit confirms a sufficient-method stop,
not negative actual minors or RH. An inconclusive audit must record the
precise missing bound. The result is a local specialization, not certified
original mathematics. Mathlib matching coverage remains unchecked.

After verifying this stop, an independently testable signed mechanism
needs its own exact target and source coverage. No justified creative
uniform-sign target is currently ready; the absent independent signed
input remains the blocker. This audit is not a reopening of accretivity.

## Separate scope approval and URL repair — step416

LITERATURE_REASON: Supervisor recovery requires direct source URLs in this
assessment; the exact target and mathematical hypotheses are unchanged.
This is a source-scope check, not the critical mathematical audit.

The versioned O'Sullivan source above was reopened at (1.2), Theorem1.4
and (1.8). Its fixed-K integer asymptotic has a K-dependent remainder
O(log(n)^K/n^K). It supports the planned finite-value check, without
licensing differentiated unknown remainders or effective onsets. The
previously inspected Section7 proof cases are reused, not reread.

Michałowski v1 Lemma4.1 and its complete proof were reopened: the finite
factorization requires r>=2 and 0<q<1. Section6 was checked for the
separate norm premise in inertia preservation. Neither the cubic-tail
conclusion nor that norm premise is approved at k=r-1. The source's
normalization must be checked against the local corrected finite identity;
source access alone does not validate the boundary specialization.

Zhang v1 Section4 Lemmas4.1/4.2 and their complete proofs were reopened.
The determinant implication concerns real matrices and requires positive
definiteness for strict positivity; the semidefinite case uses an epsilon-I
limit. Import Lemma4.2 directly. No new determinant proof is justified.

The prior exact-target searches and local stop record
ATTEMPTS/2026-11-04-signed-qpascal-odd-coordinate-stop.md remain applicable.
No expanded search, new mechanism or novelty finding is asserted. This
approval covers only the saved L774 audit, including L765's finite-value
input, not its different-ray endpoint conclusion. Pass requires a vanishing
amplified error and valid positive/sign factors; otherwise report the
precise audit defect. All actual minor signs and RH remain unresolved.
Mathlib matching coverage remains unchecked. No lemma or script changed.
