# Retained-transfer range calculation — working checkpoint

Approved target and prior SPECIALIZE coverage:
`drafts/literature/2026-10-09-retained-transfer-word-count-range.md`.
Main gap: universal eventual descent. Intermediate target: maximal initial
range for the fixed factor-2 forward transfer, existing seed and length
conversion. Downstream use: exclude more of the restricted cycle language.
Continue if an all-real exclusion or first-failure scalar certificate is
established; stop this comparison once its first failure is certified.

Inputs read: L041's all-r proof including seed (6), own-word bounds (7),
occurrence partition and length conversion (11); L044's transfer (3)-(6)
and assembly (7); L043's scalar comparison. Attempt 019 and history 069
preserve independent guard-only and full-minimum-count failures; history
109 supplies the thirteen-word audit. No source refresh is needed.

Provisional reasoning, not yet certified: R_r=2^r-1; cyclic induction
gives K<(15/4)R_r((133/10)log N+9+log r). Conversion gives
N<(399/5)R_r log N+(54+6log r)R_r+69r/1034. At r=17,
log C<20, log17<3 give RHS<1668*131071+1173/1034<C,
and A_17<C supplies all-real monotonicity. At r=18 use the old scalar
K=225640001,L=131990940,N=357630941 with J_0=12,H_0=225639812,
a_0=131990860 and seventeen minimal entries (2,3,2). Check every
integer guard, aggregate K/N bounds, primitive scaling and signed
linear-form bounds exactly. This tuple is not a word or cycle.

Remaining conditions: actual positive closure, all individual wordwise
heights and valuations, universal entry, unrestricted counts/cycles,
divergence and eventual descent. Published computational qualifications
and unchecked Mathlib/external Lean coverage are unchanged.

First exact run: 98/99 checks passed; the provisional a_0 was 10 modulo
18, so that parameter allocation was invalid. Full failed evidence is
preserved in `scripts/postspell-word-count/retained-range-initial-certificate.json`.
Correction preserves the same K,L,N: use every J_i=2, H_0=225639842,
a_0=131990870 and H_i=3,a_i=2 for 1<=i<=17. The changed allocation
is subject to a fresh exact run; the failed allocation is not a witness.

Completed result: L045 gives the general-r assembled K/N inequalities,
an all-real exclusion through r=17 and simultaneous scalar feasibility
at r=18 for the corrected allocation. The final run passes all 99 exact
checks. Complete selected exclusion, witness and rational-log evidence
were inspected with the shared JSON inspector. Maximality concerns only
the explicitly retained aggregate system; individual heights, parities
and closure are omitted. Canonical reasoning and citations are in L045.
The fixed comparison stops at this first failure; a separate critical
audit is the sole continuation and its scope remains REVIEW_REQUIRED.
