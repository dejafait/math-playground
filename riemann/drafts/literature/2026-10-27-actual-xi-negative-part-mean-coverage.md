# Actual-Xi first-sign negative part — completed source comparison

TARGET: Assess unconditional source coverage for a dyadic o(T log^3 T) bound on the gamma-normalized negative part of actual Xi's first Laguerre form.
CHECKED: 2026-10-27
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched exact negative-part/Laguerre/Hardy-derivative terminology, stronger mean and almost-everywhere statements, and zero-window localization; inspected the primary statements and relevant cases listed below. No matching little-o theorem was established by this bounded search; this is not a novelty claim.
SOURCE_EVIDENCE: Bui–Hall arXiv:2304.05178v1, definition, (1), Theorems 1–3, Proposition 3 and Sections 5–7; Csordas arXiv:1309.0055v2, Definition 1.1, Proposition 2.2/proof (2.3), Proposition 2.3 and Open Problem 4.7; bramble_trace paper 41 v4, Theorems 3–4 and Section 8.6 (63a)–(63e); paper 36 v4, Corollary 5, Theorem 6/proof and qualification after (22); span_of_dilates paper 50 v2, Lemma 1/proof and Corollary 1/proof. Direct links and qualifications below.
COMPARISON: Known signed moments, linear-filter positivity, fixed-positive-density sign coverage and diverging-order mean approximation do not state the fixed first-order negative-part saving. The fixed-order error in paper 41 has no little-o saving. The gamma normalization is covered locally by L465; converting it into an integrated estimate remains mathematical work.
GAP: The unchecked difference is displacement-sensitive, amplitude-weighted negative mass at fixed order, uniformly over dyadic heights and including central zeros and multiplicities. No inspected theorem supplies it; global signs and localization at prescribed heights remain independent gaps.
REASON: Essential comparison is complete enough for a bounded attempt using known zero-pair identities and ordinary moment inputs, without assuming positivity. A separate continuation assessment specifies the new test. This literature turn proves no majorant, gauge-transfer estimate or negative-part bound.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target concerns a different actual-Xi statistic from the ready physical-pencil moment assessments and requires its own primary fixed-order and zero-window comparison.
SCOPE: Actual Xi of L018, positive real heights T>=2, ordinary derivatives and D_1(Xi;t)=Xi'(t)^2-Xi(t)Xi''(t). No RH, simplicity, Laguerre–Polya membership, external fixed-half-plane premise or probabilistic independence assumption.

## Exact proposed threshold and purpose

For s=1/2+it put

    A(t)=|(s(s-1)/2) pi^(-s/2) Gamma(s/2)|,
    N(T)=integral_[T,2T] max(0,-D_1(Xi;t))/A(t)^2 dt.

A(t) is nonzero at these heights. The target is
N(T)=o(T(log T)^3) as real T tends to infinity. This is a proposed
comparison threshold, not an established estimate, claimed optimal scale
or statement imported from a moment theorem. No gauge differentiation
or mean evaluation was performed in preparing this assessment.

The main gap remains all-height initial signs and global mixed
positivity. A bound for this statistic could provide one quantitative
input on exceptional negative signs. It cannot alone exclude a single
negative height, an off-line zero or all mixed forms. Localization,
control of tiny exceptional sets and higher initial signs would remain
unresolved. The warning in
`ATTEMPTS/2026-09-24-endpoint-relative-mean-square-test.md` applies:
small averaged error or density does not control prescribed heights.

## Primary comparison completed on 27 October 2026

This is a LITERATURE / NOVELTY_UNCHECKED / EXPLORATION step. It establishes
source scope, not an estimate beyond the inspected literature. No lemma,
mathematical script, DAG row or main argument was changed.

1. H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function
   Z(t)*, [arXiv:2304.05178v1, 11 April 2023](https://arxiv.org/html/2304.05178v1).
   The definition uses the gamma phase and ordinary derivatives. Equation
   (1) is a signed second-product mean; Theorem 3 is a fixed-order fourth
   product asymptotic. For orders k,l,m,n its scale is
   T(log T)^(k+l+m+n+4), with error one logarithmic power smaller.
   Proposition 3 covers the sharp dyadic interval and complex shifts
   O(1/log T); Sections 5 and 7 differentiate using Cauchy contours.
   Its proof is omitted by the authors, rather than independently audited
   here. Theorem 1 gives a lower proportion 3/25 for ZZ''<0, not an
   upper bound for the negative part of D_1. These unconditional inputs
   can support moment bounds; they do not state the requested saving.
   Reused local assessment: `2026-10-10-negative-discriminant-set-measure.md`.

2. bramble_trace, *Generalized Laguerre positivity at growing orders*,
   [paper 41, displayed v4, 24 October 2026 07:18 UTC](https://rstation.ai/problems/riemann_hypothesis/papers/41).
   Read Theorems 3–4 and Section 8.6, including the derivative estimate
   (63a), complementary arcs (63d), gauge case and remainder (63e).
   Theorem 3's (7d) bounds the absolute mean error for
   Q_n^Xi=n!D_(n/2)/(b^2 ell_t^n) by O_b(T log T/n^2) throughout
   even 2<=n<=b log T. At fixed n=2 it has no vanishing factor as
   height grows; increasing a fixed truncation order does not change
   that fact. Theorem 4 and Corollary 4a require a diverging lower
   order. Equation (2) supplies the positive b and Xi=-bZ. This is a
   platform manuscript, compared at theorem/proof-case level, not an
   independently audited import. Search returned an older v2 extract;
   the directly opened v4 controls this comparison.

3. bramble_trace, *Signs and uniform filtered positivity in fourth
   moments of Hardy's function*, [paper 36, displayed v4,
   21 October 2026 23:18 UTC](https://rstation.ai/problems/riemann_hypothesis/papers/36).
   Read Corollary 5, Theorem 6 and its complete sine-kernel proof.
   Corollary 5 concerns products of Laguerre forms with scale
   T(log T)^(2p+2q+4). Theorem 6 tests a Laguerre form against the
   square of a fixed real linear derivative filter. The qualification
   after (22) explicitly excludes arbitrary nonlinear jet tests and
   arbitrary height localizers. Those hypotheses do not cover the
   indicator of a negative form or its clipped magnitude. No uniform
   growing-filter assertion is needed or independently verified here.

4. George Csordas, *Fourier transforms of positive definite kernels
   and the Riemann xi-Function*, [arXiv:1309.0055v2,
   21 February 2014](https://arxiv.org/html/1309.0055v2).
   Definition 1.1 assumes a real genus-one product, nonpositive
   quadratic exponential, strip zeros and summable inverse squares.
   Read Proposition 2.2 and its proof (2.3), pp. 3–4: the conjugate-pair
   contribution has sign determined by squared ordinate distance minus
   squared displacement. Its displayed proposition assumes f(0)!=0
   and a wider zero-free vertical interval; the finer window condition
   is in the proof, not the literal proposition statement. Singular
   logarithmic differentiation cannot simply be used at real zeros.
   Proposition 2.3 depends on a fixed remaining factor; it gives no
   uniform actual-zeta negative mass. Open Problem 4.7 is pointwise
   first-sign positivity in a scaled normalization, not this mean target.
   The original 1991 paper was not retrieved; no uninspected theorem
   from it is imported. Reused September comparison cited below.

5. span_of_dilates, *Laguerre signs at the height of an off-line zero:
   a window lemma, a crossing index, and a two-sided depth meter*,
   [paper 50, displayed v2, 24 October 2026 22:01 UTC](https://rstation.ai/problems/riemann_hypothesis/papers/50).
   Lemma 1 assumes every right-side zero beta+i gamma obeys
   |t-gamma|>=beta-1/2, and concludes all-order nonnegativity at t.
   Its proof retains on-line multiplicities, a positive normalization
   at central zeros, and coefficient convergence of the paired product.
   Corollary 1 gives lower density 1-log(11/4)/(2pi) for good heights.
   Read its Littlewood/Jensen/mollifier argument and endpoint case;
   it estimates window lengths, not amplitude-weighted negative mass.
   Its older mollifier inputs were not independently re-audited or
   imported here. The positive constant density does not itself supply
   the requested vanishing normalized mass. Its window argument is
   useful source coverage for a later pair-localized test.

## Normalization, duplicates and remaining application

L018 fixes exactly the completed Xi used here. L465 Section 1 already
identifies its positive real b and Hardy branch; Section 5, (14), proves
(log b)''=O(t^(-2)) with the required paired-gamma cancellation. Compare
the displayed b with the proposed A using s(s-1)=-(t^2+1/4); hence this
is the same modulus. A future calculation must retain the polynomial
factor and the differentiated gauge, and must be valid at real Xi zeros.
No derivative formula for D_1 or integrated gauge error is proved today.

The September assessment `2026-09-27-first-laguerre-zero-compensation.md`
already records the known reciprocal-pair identity and density/spacing
limitations. `ATTEMPTS/2026-09-27-count-and-gap-first-sign-test.md`
records L354's count-and-gap countermodel; coarse zero counts cannot
be reused as pointwise compensation. L251's real-root masking shows
that even all first signs would not suffice for RH. The proposed next
mechanism instead keeps actual-Xi amplitude and pair displacement
inside the integral. It must not claim that those old countermodels
prove failure of this different weighted estimate. The endpoint
relative-mean-square warning remains applicable to any later use at
prescribed heights. No source match establishes novelty; Mathlib
matching/supporting coverage remains unchecked.

Representative queries actually searched: `Hardy function Z derivative
Laguerre inequality mean square negative`; `Laguerre zeta almost all`;
`Xi Laguerre inequality density`; `Riemann Xi negative mean Laguerre`;
`Laguerre negative-part zeta`; `Hardy Z Laguerre o(T)`; and the
Csordas–Ruttan–Varga title. Irrelevant Laguerre-operator and Hardy-space
results were excluded. Search snippets were leads, not theorem evidence.

Continuation/abandonment test: seek a zero-safe displacement-weighted
majorant and a source-supported summation saving, or isolate the precise
additional zero-weighted estimate it needs. Returning only a signed
mean, full-scale O bound or fixed density fails this test. Park that
implementation if it erases displacement before summation or assumes
the desired pointwise sign. The separate new continuation assessment
requires later approval before its mathematical invocation.
