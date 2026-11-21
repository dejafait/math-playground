# Signed neutral tail beyond the coefficient envelope: source comparison, step 233

TARGET: Assess source coverage for an o(1) norm bound for the exact signed neutral-tail functional on W_floor(sqrt(N)), using the complete Gram dual and actual Möbius coefficients.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the two named prior assessments and L729; scoped duplicate searches and external neutral/Gram-dual/Mobius-tail/inverse-Gram searches found no matching bound. New inspected leads are paper 21/v2 Theorem 2(c) and Section 7, paper 22/v3 (19l)--(19n') and its proof, Ehm Proposition 2.1, and Green--Tao Theorem 1.1/(1.1); details below.
SOURCE_EVIDENCE: Primary statements and relevant tail proof cases were read at rStation papers 18/v3, 21/v2, 22/v3, Ehm arXiv:2405.06349v2 Theorem 2.1/Proposition 2.1, and Green--Tao Annals 175 (2012), pp. 542--543. No result inspected estimates the prescribed signed functional in the complete neutral Gram dual at K=floor(sqrt(N)).
COMPARISON: L729 gives O(N^(1/4)) at this cutoff, not o(1). Coordinate uniformity, moment cancellation, Bernoulli kernel asymptotics and scalar Mobius orthogonality leave a distinct growing-unit-ball norm estimate unpaid; no applicable stronger theorem or actual-arithmetic lower bound was identified.
GAP: A quantitative signed-tail bound uniform for complex unit vectors in W_floor(sqrt(N)) remains unproved. Exact kernels and fixed-coordinate limits do not supply it; this review proves neither failure nor truth of the threshold.
REASON: The nominated continuation test fails to find a discriminating estimate beyond kernel algebra and coefficient bounds. Park this cutoff pending a new quantitative mechanism; nominate the independently testable constructive neutral-density source audit instead.
SCOPE: Completed literature-only comparison. EXPLORE records no adequate source match and does not approve another Gram reformulation at this cutoff. No new lemma, derivation, mathematical script or theorem import was made. New continuation coverage requires separate approval next turn.

## Proposed intermediate target, not a result

Use exactly H, rho_m, g_N, A, B, T_u and Q from L729, with the
ordinary arithmetic mu and Lambda, integer N>=4 and K=floor(sqrt(N)).
Let W_K consist of complex u in span(rho_2,...,rho_K) with A(u)=B(u)=0.
The proposed quantity is

    R(N,K)=sup_(u in W_K, ||u||=1)
       |sum_(n>N) mu(n)(log N-log n) conjugate(T_u(n))|,

with value zero if W_K={0}. The proposed threshold is R(N,K)=o(1)
as N tends to infinity through integers. This is a target, not an
assertion. L729 supplies the exact functional and absolute convergence;
no RH, representer, moment or simplicity assumption is permitted.

The proposed mechanism retains the signed tail vector and the complete
Gram quadratic form simultaneously, instead of bounding every
coefficient separately. A source assessment must determine whether an
existing theorem pays it, whether a known obstruction applies, and
whether there is a specific arithmetic cancellation estimate to test.
Exact Gram evaluation alone did not pay the full-update contraction
in step 231; this narrower normalized-observation test must not silently
reopen that target or presume that changing coordinates creates a bound.

A later bounded mathematical attempt would need a quantitative dual
estimate from that mechanism, or an actual-arithmetic lower bound that
obstructs the threshold. A generic coefficient countermodel, numerical
samples, or the existing O(N^(1/4)) upper bound cannot decide it.
If comparison finds only kernel algebra and no discriminating estimate,
park the stronger cutoff rather than repeat unpaid norm reformulations.
The cutoff is chosen to test a strict enlargement of the validated
polynomial range; no claim that this enlargement resolves RH is made.

Possible downstream use: neutral preconditioners with larger support.
Full residual norm, complementary component, saturation, signs and
anchored-to-unanchored transfer remain open, independent obligations.
This is a proposed mechanism for research, not certified novelty.
Mathlib coverage of the stronger target has not been checked.
No cross-notebook input is used.

## Completed source review

LITERATURE_REASON: The changed cutoff exceeds L729's validated vanishing
range; essential signed operator-norm comparison was not covered by the
prior arithmetic audit. This review does not repeat that proof or the
conditional full-norm literature.

### Search and reuse

Reuse [the arithmetic assessment](2026-11-03-neutral-arithmetic-tail-audit.md)
and [the dyadic comparison](2026-11-03-triangular-mobius-dyadic-energy-contraction.md)
for the complete kernel and existing failures. Specific local searches
covered these assessments, the triangular-Mobius assessments, the
step-232 history, L729, and the Mobius ATTEMPTS files. They found no
recorded signed-dual estimate at the new cutoff. The full-update stop
and correlated-ratio warnings remain qualified evidence, not global bans.

External searches included `Nyman Gram inverse Mobius`, `neutral Selberg
growing Mobius`, `Mobius fractional part Gram matrix uniform tail norm
square root N`, `neutral Gram Mobius tail`, and `Nyman inverse Gram
estimates`. A second lead search used `Mobius periodic uniform Davenport
theorem exponential sums`. Only primary sources below support the
comparison; unrelated hits, search snippets and automatic acceptance
reports are not theorem evidence. No novelty inference is made.

### Exact comparison with inspected theorems

1. [bramble_trace, paper 18](https://rstation.ai/problems/riemann_hypothesis/papers/18),
   displayed v3, 22 October 2026: (32), (36)--(42), including the full
   cancellation/jump proof, match the real version of L729's estimate.
   This source bounds neutral projections only. The known polynomial
   range and the uncontrolled complement were already recorded; no
   stronger signed theorem appears in these inspected statements.

2. [halasz_resonator, paper 21](https://rstation.ai/problems/riemann_hypothesis/papers/21),
   displayed v2, 18 October 2026: Theorem 2(c), (31)--(35'), its full
   Tonelli/telescoping proof, and Section 7. The scalar theorem covers
   all integers N,m>=2, keeping the two moment errors and the physical
   tail. Its stated coordinate range is much larger than the neutral
   operator range. Section 7 explicitly requires control of growing
   coefficient/inverse-Gram factors. It does not prove such control.
   The finite-probe energy bound concerns a different vector, the
   fixed gradient C, and cannot be substituted for this signed error.

3. [halasz_resonator, paper 22](https://rstation.ai/problems/riemann_hypothesis/papers/22),
   displayed v3, 19 October 2026: part (e) in the fixed-gradient
   development, equations (19l)--(19n'), and the concluding proof
   paragraph after the Binet argument were read. Here
   m K_m(k)=R_1(k/m)-R_1(k). Its finite-N identity keeps a tail weighted
   by c_N(k)-Lambda(k)/log N; the claimed polynomial-range uniformity
   is for the moment term only. The fixed-m tail assertion and the
   nonvanishing Mellin amplitude are neither a growing-dual bound nor
   an impossibility theorem. The paper's introductory attribution to
   “Theorem 3(e)” is not used as the locator: the displayed equations
   identify the exact inspected passage. No twisted-family estimate
   is silently applied to this ordinary mu target.

4. [Ehm, arXiv:2405.06349v2](https://arxiv.org/html/2405.06349v2),
   13 May 2024: Theorem 2.1, q=1, has arbitrary real u,v>0;
   Proposition 2.1/(12) gives
   R_1(x)=B_2({x})/(2x^2)+B_3({x})/(3x^3)+O(x^(-4)) as x->infinity.
   The opening proof calculation in Section 7.2 uses harmonic-number
   expansion and bounded fractional parts. This is a kernel lead, not an
   estimate of its Mobius-weighted inverse-Gram norm. Earlier kernel
   and moment comparisons remain reusable; none is rederived here.

5. [Green--Tao, *The Mobius function is strongly orthogonal to
   nilsequences*, Annals 175 (2012), 541--566](https://annals.math.princeton.edu/wp-content/uploads/annals-v175-n2-p03-p.pdf),
   Theorem 1.1, pp. 542--543: for a dimension-m nilmanifold with a
   degree-d filtration and a Q-rational Mal'cev basis, a polynomial
   sequence g and Lipschitz F:G/Gamma->[-1,1], the normalized Mobius
   correlation is bounded by
   Q^(O_(m,d,A)(1)) (1+||F||_Lip) (log X)^(-A), with an ineffective
   implied constant depending on m,d,A. Their (1.1) records Davenport's
   frequency-uniform linear exponential bound. The theorem statement,
   dependence and ineffectivity remarks were inspected, not the full
   nilsequence proof. No application is asserted: a reduction of our
   entire unit ball with controlled complexity/Lipschitz or Fourier
   norm and summable physical tails is missing. Scalar orthogonality
   alone is insufficient source coverage. No power-saving consequence
   or obstruction is claimed from this comparison.

The rStation papers are manuscript claims; their reviewer reports are
not independent validation. The comparison uses their stated scope,
not their unreviewed conclusions as new inputs. Ehm and Green--Tao do
not give the missing Gram-dual inequality in the passages inspected.

### Decision and independently testable continuation

**Park the stronger cutoff.** The source review found no paid bound and
no concrete signed estimate that meets the nomination's continuation
test. This is new scope evidence from primary tail and uniformity
statements, not a disproof of R(N,floor(sqrt(N)))=o(1). Reopening needs
a quantitative unit-ball cancellation mechanism or an actual-arithmetic
lower-bound test; another exact matrix expression is insufficient.

A separate source-audit continuation is prepared in
[the constructive-density assessment](2026-11-03-constructive-neutral-density-audit.md).
Its purpose is to check whether the two constraints lose any part of
the closed arithmetic span, using a fixed-vector two-generator repair.
It does not extend the cutoff or assume that this span is the entire
step space. This is known-source reproduction, not a creative attempt.
Creative priority remains; no bounded central mechanism with the
required quantitative test was justified in this comparison.

Mathlib matching coverage of the signed target was not checked. No
absence claim, cross-notebook input, RH assumption or new result is used.
