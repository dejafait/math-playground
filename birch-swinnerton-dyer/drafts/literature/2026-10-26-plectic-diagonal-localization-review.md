# Same-prime localization of partially global plectic classes — review

TARGET: Assess the defining integrals for Fornea's r=2 class over F=Q to determine whether vanishing of its Q-invariant same-prime localization is a viable bounded arithmetic test without assuming Conjectures 1.9-1.10.
CHECKED: 2026-10-26
DECISION: EXPLORE
SEARCH_EVIDENCE: Exact-title searches with same-prime, localization, complex conjugation and symmetric found no inspected same-prime vanishing theorem; notebook-local duplicate/failure checks found the prior proposal and direct-import stops only.
SOURCE_EVIDENCE: Fornea arXiv:2603.28327v2 Sections 4.1-4.2, (63)-(68), Theorem 5.3 and complete Section 5.4 proof, Proposition 5.9/Remark 5.10 and Corollary 5.12 inspected; earlier hypothesis/Theorems A-C coverage reused; details in drafts/source-notes/2026-10-26-plectic-diagonal-localization-coverage.md.
COMPARISON: The complete integral is defined before arithmetic projection; degree-zero comparison recovers only the mock projection, constant-component vanishing does not state full-kernel cancellation, and auxiliary-place localization is unavailable at the same prime over Q.
GAP: No proved c-transformation or zero same-prime localization for the retained component was found; local finite membership, rational Kummer membership and nonvanishing remain distinct from the proposed zero test.
REASON: Definitions expose an actual complete-integral test independent of assuming the determinant conjecture; allow a separately approved bounded split-component attempt, with no vanishing identity imported or derived in this review.

LITERATURE_REASON: The target has changed from importing a rational exterior class to testing same-prime localization of the new 2026 partially global class; the defining integral and comparison proof cases essential to this test were not needed for the completed import rejection and remain unread.

## Original proposed object and bounded question

Use [Fornea, *Plectic Heegner classes*, arXiv:2603.28327v2](https://arxiv.org/html/2603.28327v2),
F=Q, imaginary quadratic K, incoherent set S_cal={p}, and trivial
anticyclotomic character (conductor one). Retain Assumptions 1.1, 1.4
and, for the mock comparison, the corrected 1.5. Thus p>=5 is inert
and multiplicative, the inert conductor is square-free, the incoherence
parity holds, and the residual image contains SL_2(F_p). Do not change
the reduction type to good ordinary. The trivial character's global
factor is over K after its justified descent; it is not a Q-point.

Write V=V_p(A) and U=H_f^1(K_p,V). The source constructs an object in
U tensor H^1(K,V). A proposed diagnostic, not a proved identity, is
the localization tensor obtained by applying (1+c)/2 to the global
factor and (1+sigma_p)/2 to the local factor, then localizing the global
factor at the same prime p. Here c is the nontrivial element of
Gal(K/Q), acting on global cohomology, and sigma_p is its local action.
Both actions and compatibility of the chosen localization must be
checked from the source rather than inferred from the word plectic.
The final object initially lies in U tensor H^1(K_p,V), not necessarily
in a tensor square of U. Do not interchange factors or call it
alternating before proving the requisite local membership.

The review should identify the actual integral expression for this
diagnostic and whether an attempted vanishing test is justified by
proved identities, contradicted by a nonzero term, or still equivalent
to an unproved Selmer/rationality assertion. A ready follow-up would
attempt one explicit local cancellation or obstruction in that formula,
not assume the whole determinant conjecture. A surviving strict
cohomology direction would still need rational Kummer membership and
nonvanishing, and a justified replacement for L005's good-prime
threshold before its arithmetic use. The complex-order gap remains.

This proposal is materially different from pointwise visibility or
abstract auxiliary-field variation: it names the actual partially
global source class and its same-prime local tensor. Continue only if
its formula exposes a test independent of the conjectural conclusions;
otherwise park this local mechanism and choose an independent target.
No mathematical derivation or script has been performed. The original
REVIEW_REQUIRED proposal above has now received its source review.

## Completed step 512

The [source notes](../source-notes/2026-10-26-plectic-diagonal-localization-coverage.md)
record the defining integral, exact projection/descent order, action
coverage and missing c-transformation. The direct inference from
Theorem 4.13 or Theorem 5.3 to same-prime zero localization is rejected.
The question itself survives as bounded exploration, most sharply on
the split-multiplicative retained plus component. This is new negative
source evidence against an automatic cancellation, not a counterexample
to cancellation or an advance beyond the checked mathematics.

The next mathematical target has its own assessment,
`2026-10-26-plectic-retained-plus-cancellation.md`. It is newly written
and requires separate next-turn approval before execution. No lemma,
mathematical script, or research attempt is part of this literature turn.
