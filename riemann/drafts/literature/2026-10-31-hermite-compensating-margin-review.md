# Actual-Hermite compensating margin: completed source comparison

TARGET: Compare known actual-Xi Hermite interval-margin and signed-tail estimates for D(P_N)>=|B_N|+|R_N'^2-R_NR_N''| on [T,2T], N=ceil(16(T+1)^2), and nominate one bounded compensation test.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the completed interval-transfer and actual-Hermite cross-term assessments; searched the exact joint margin, Hermite truncation/Laguerre remainder and multiplicity/perturbation terminology; inspected the primary statements and proof cases below. No inspected theorem supplies the joint actual-coefficient margin. This bounded negative search establishes neither novelty nor impossibility.
SOURCE_EVIDENCE: Romik arXiv:1902.06330v3 Theorem 2.1/(2.1)-(2.3), (2.20)-(2.22), https://arxiv.org/html/1902.06330v3#S2.SS3; Nie-Zhang arXiv:2404.17717v2 Section 4, (4.2)-(4.3), (4.6)-(4.7), Theorems 4.1/4.6, https://arxiv.org/html/2404.17717v2#S4; Csordas-Escassut, Ann. Math. Blaise Pascal 12(2) (2005), 331-345, Definitions 1.1-1.2, Theorem 2.1 and complete proof, pp.331-334, https://www.numdam.org/item/AMBP_2005__12_2_331_0.pdf.
COMPARISON: Romik and L564 provide convergence/absolute derivative errors, not a signed lower bound; interval SOS exactness characterizes polynomial nonnegativity but supplies no actual margin. The classical Laguerre equality case explicitly retains multiple zeros and gives no quantitative positive surplus there. Whether the proposed nonstrict absolute budget can retain this equality is an independent, uncomputed compatibility question.
GAP: The proposed all-T joint inequality is unproved. No source-supported mechanism for moving-height compensation without excluding multiple zeros was identified. Exact multiple-zero compatibility, actual polynomial margins, complete correlated losses, cutoff jumps and all higher forms remain unresolved.
REASON: Complete the requested comparison without nominating an unsupported positive compensation test. Park direct all-height margin development; nominate a bounded local two-jet compatibility audit as an independently testable prerequisite, with no actual-Xi realization claim or new algebraic conclusion in this literature turn.
LITERATURE_REASON: The changed joint-margin target required essential coverage beyond the completed L568 audit; this turn adds the primary Laguerre equality-case comparison and reuses adequate existing Hermite/interval coverage.
SCOPE: Literature-only comparison of the unchanged TARGET; no new lemma, inequality proof, calculation or mathematical script. The distinct bounded audit is nominated in 2026-10-31-hermite-compensation-multiple-zero-audit.md and awaits separate continuation approval.

The target reviewed uses the
same actual coefficients and normalization as L564, R_N=Xi-P_N and
B_N as in L568, with D(f)=f'^2-f f''. The proposed sufficient threshold
is to be compared with the literature, not assumed true. Do not derive
or test it in the source-only turn. Do not weaken it silently to a
sampled margin, a different cutoff or a nonvanishing-jet hypothesis.

The main gap is actual-Xi all-degree positivity. A validated
compensating-margin mechanism would address only the first form;
its plausible downstream use is signed transfer despite the negative
linear term. All higher forms and any remaining all-height or
multiplicity conditions must remain explicit.

Essential local inputs: L564's complete derivative-tail proof and
normalization, C567a's audited coefficient enclosures, and L568's
audited negative first variation. Reuse the primary hypotheses and
failure comparisons in
`2026-10-31-hermite-interval-signed-transfer-discovery.md`.
L568's independent complete certificate is
`scripts/hermite-gram/l568-certificate-audit.json`.
No cross-notebook input is proposed.

The comparison must distinguish an interval positivity representation
from a proof of the actual margin, and inspect whether multiple zeros
make this proposed absolute compensation too restrictive. The first
source question is joint quantitative control on the moving intervals,
not another low-height Xi-sign verification, global SOS screen, generic
Pruefer import, or expanded B_N probe grid. Existing L565/C567a stops
are scoped and do not by themselves forbid interval certificates.

Continuation test: nominate a concrete compensation test only if a
specific source-supported mechanism can control the proposed losses
and has a stated path to uniform moving-height estimates without
excluding multiple zeros. Otherwise record the precise mismatch and
choose a materially different mechanism in bounded discovery. A
finite interval result alone cannot support an all-height conclusion.
No justified creative proof target is yet available: none of the
inspected sources supplies an all-height margin or a mechanism that
preserves the needed equality cases. Mathlib coverage of the joint
target has not been checked.

## Precise primary comparison

Romik's Theorem 2.1 gives the actual even Hermite expansion, uniformly
on each compact complex set, with compact-dependent constants in
(2.3). Read (2.20)-(2.22), including the exact remainder before the
absolute-value estimate and its fixed-compact qualification. Reuse the
previous complete two-region/coefficient comparison rather than repeat
it. These statements supply no lower bound for D(P_N) and no signed
joint loss estimate. L564's audited (3)-(4) supplies the explicit real
moving-interval derivative bounds; its conclusion expressly excludes
a discriminant sign. No new specialization is performed here.

Nie-Zhang assumes a real univariate polynomial h, a nondegenerate
compact interval [a,b], and h>=0 there. Equations (4.2)-(4.3) give the
odd/even interval representations with degree bounds; the even Gram
form is (4.6). Read Theorem 4.1's proof, the even-case passage after
(4.7), and Theorem 4.6's attainment statement; reuse the earlier
assessment of its scope. This is a complete certificate language for
a polynomial budget, not a bound for actual Xi coefficients. The
losses in the present target contain the nonpolynomial R_N, so applying
this language would additionally require a justified polynomial or
constant majorant. No such majorant-plus-margin certificate is supplied.

The additional primary comparison is George Csordas and Alain
Escassut, *The Laguerre inequality and the distribution of zeros of
entire functions*, Ann. Math. Blaise Pascal **12**(2) (2005), 331-345,
[Theorem 2.1, pp.333-334](https://www.numdam.org/item/AMBP_2005__12_2_331_0.pdf#page=4).
For a nonzero function f in the Laguerre-Polya class, D(f)>=0 on R;
equality holds precisely at a multiple zero, apart from the family
f(x)=C exp(bx), C,b real. Definitions 1.1-1.2 allow the canonical
product C exp(-a z^2+bz) z^m product (1-z/x_k)exp(z/x_k), with
a>=0, b real, real nonzero x_k and sum |x_k|^(-2)<infinity; finite
products are included. Read the exponential exception and complete
logarithmic-derivative proof, including the passage back to zeros.
The formula is used off the zeros, with their equality case handled
separately. This is a source theorem, not a new lemma or a proof of
Xi membership in that class.

Applicability limit: assuming this class membership for Xi would
already assume the unresolved reality of its zeros. Thus the theorem
is a comparison of admissible equality behavior, not an unconditional
lower-margin input for Xi. It does not say that Xi has a multiple zero,
and it does not decide the proposed nonstrict compensation inequality.
Even a positive result for its first form would leave the higher-form
gap. No reproof of the known Laguerre theorem is needed or attempted.

## Search, overlap and access record

Queries actually used included `Riemann xi Hermite expansion Laguerre
inequality truncation remainder lower bound`, `Romik Hermite xi
polynomials real zeros Turan inequalities`, `"Riemann" "Hermite"
"remainder" "Laguerre"`, `"Riemann xi" "Hermite" "signed" remainder
margin`, `"Romik" "Hermite" "Laguerre" inequality margin`, `"Level
sets" "Laguerre inequalities" Csordas Smith Varga pdf`, `"Laguerre
inequality" "perturbation" "multiple zeros"`, and `"Laguerre expression"
"perturbations" zeros`. Search hits about Jensen coefficient signs,
single Hermite polynomials, Laguerre spectral series, and third-party
RH portfolios are not theorem evidence for this target. The stronger
O'Sullivan coefficient/hyperbolicity comparison is reused from
`2026-10-31-actual-hermite-signed-cross-term-review.md`; its different
coefficient families and unverified real-root hypotheses remain.

The 1992 Csordas-Smith-Varga paper at the Kent author PDF URL
`https://www.math.kent.edu/~varga/pub/paper_192.pdf` exposed no readable
lines or inspectable screenshot content through the available web
interface. Do not treat its index text or ResearchGate quotations as
an inspected theorem. The accessible 2005 primary paper contains the
complete equality theorem/proof needed here, so this optional lead is
not an essential source blocker and is parked without repeated access.

Local overlap checks read L564's full proof/application audit, L568's
statement/decomposition and audit scope, C567a's exact evaluation
statement, the two saved Hermite source comparisons and the B_N stop.
The bounded jet question was searched in notebook-local assessments
and failure records. L469 was read as a contrast: its audited regular
first-order differential-barrier obstruction is a different predicate,
not an input for the algebraic compensation question. No duplicate
classification of the absolute compensation budget's multiple-zero
two-jets was located in these checks; no originality claim follows.
No cross-notebook theorem is used. Existing unfinished work is retained.

## Decision and bounded continuation

No positive compensation test with the specified moving-height path
has passed the source test. Do not enlarge L568's probe grid, revive
B_N>=0, or label the absence of a matching theorem a refutation of
compensation. The next independently testable target is only the
local compatibility of the proposed absolute budget at hypothetical
multiple zeros, retaining both mixed and quadratic terms. Its exact
scope and stopping test are in
`2026-10-31-hermite-compensation-multiple-zero-audit.md`.

The intended benefit is deciding whether absolute loss separation
already imposes extra jet equalities or excludes arbitrarily small
generic perturbations at admissible zeros. Those are questions for
the next mathematical attempt, not conclusions of this review. If
extra restrictions appear, actual Hermite correlations would have to
justify them before this budget could support transfer; if they do
not, an all-height actual margin is still missing. Full signed
cancellation, other cutoffs, higher forms and Xi realization remain
outside this bounded test. Newly written ready coverage receives its
separate approval next turn; no dependent mathematics is done now.
