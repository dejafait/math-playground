# Higher-moment concentration source comparison

TARGET: Prove meas{t in [H,2H]:D(t)>0}>=c H^(1/2)(log H)^(-K) for some fixed c>0 and K>=0 and every sufficiently large real H, using L401's exact weight and unconditional higher moments of ordinary Hardy jets through order two.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched twelfth/higher moments of zeta and Hardy derivatives, continuous derivative upper bounds and Cauchy/strip-convexity transfer; inspected Heath-Brown's original paper, Ivic's primary finite-log restatement, Curran-Heycock Section 4 and Arguin-Ouimet-Radziwill Proposition 3.3/Corollary 3.4/Lemma 3.5 with their proof; narrow local checks found no duplicate half-power concentration result.
SOURCE_EVIDENCE: Heath-Brown 1978 Theorem 1, p. 444, has scalar twelfth moment O(T^2(log T)^17), explicitly recoverable in Ivic arXiv:1406.0604v1 Lemma 10, p. 7; Curran-Heycock arXiv:2403.00902v1 Section 4, p. 8, supplies Cauchy/Holder derivative transfer; AOR arXiv:1901.04061v4 pp. 22-24 supplies unconditional strip convexity and entire analytic windows with arbitrarily high polynomial tail decay.
COMPARISON: The finite-log scalar moment has the height power required by the degree-four concentration budget. The published transfer mechanism covers fixed derivative order, but its final sharp k=6 conclusion assumes RH and is not imported; the weaker unconditional scalar bound must be used instead. No inspected source states the physical discriminant measure target directly.
GAP: Write and verify the weaker twelfth-moment specialization for ordinary Hardy jets of orders 0,1,2, including uniform small shifts, pole cancellation, full localization tails and sharp all-real-H endpoints; then apply it to L401's exact square weight and L390's full physical pointwise bound. These conclusions remain unproved in this literature turn.
REASON: Essential source coverage is sufficient for a separate known-tool specialization, not a direct import of the target; no new lemma, derivative-moment proof, concentration derivation or mathematical script is written here.
LITERATURE_REASON: The proposed concentration mechanism needs an essential unread higher-moment theorem outside the ready fourth-moment/order-zero pointwise coverage of L402.
SCOPE: Fixed orders at most two, exponent twelve with a finite logarithmic loss, ordinary Hardy jets, complete bounded response, sharp real dyadic intervals and the exact saved half-power threshold; excludes sharp conjectural moments, growing orders/heads, asymptotics for higher moments and positive density.

## Target and relevance

The main gap is still global actual-theta mixed positivity; the total
L367 signed margin and actual common-zero upper counts are independently
unresolved. The saved intermediate target concerns the concentration of
positive physical discriminant exceptions. It could constrain weakened
discriminant strategies but would imply neither positive density nor RH.

Use audited L401 (1), (3), the exact W=Re(RZ)f and complete
Z=zeta(5/2+it); L390's full pointwise |Delta|<=C U, with
U=f^2+(f'/L)^2+(f''/L^2)^2 and L=log(2+t); L389's constant-sign
ordinary Hardy identification; and L391 (3)'s zero-safe ordinary jet
formulas, including Omega'. L402 is the audited weaker benchmark.
No lower bound on W, phase independence, growing head, simplicity,
disjointness, common-zero upper count or favorable pencil margin is used.

The continuation test is a proof of normalized ordinary-jet twelfth
moments bounded by H^2 times a fixed logarithmic power on every sufficiently
large real [H,2H]. Such a scale is compatible with the saved threshold
for the degree-four weighted integrand. An H^(2+epsilon) bound alone
does not pass the exact finite-log threshold. If the localization or
derivative transfer incurs a positive height-power loss, stop that
implementation rather than assume the sharper moment. No concentration
inequality has been evaluated to prove the target in this review.

## Search and duplicate checks

Queries included “Heath Brown twelfth moment zeta derivatives
unconditional”, “zeta function derivatives moments upper bounds
unconditional 12th moment”, “Hardy twelfth derivatives moment”,
“moments derivatives Cauchy unconditionally zeta upper bound”, and exact
finite-log and Gabriel/analytic-window searches. Search snippets and
third-party research portfolios were discovery aids only, not evidence.
There is no novelty claim from failure to locate the exact statistic.

The narrow local search covered the October 12 assessments/histories,
L389/L390/L401/L402 and October 12 ATTEMPTS. The only recorded
higher-moment concentration proposal was the supplied pending assessment.
L394/L399/L400's stopped weights remain stopped; this target reuses
L401's already positive direction rather than another signed-weight
search. L402's pointwise method is preserved.

## Inspected primary statements and qualifications

1. D. R. Heath-Brown, *The twelfth power moment of the Riemann
   zeta-function*, Q. J. Math. Oxford (2) 29 (1978), 443–462,
   [Theorem 1, p. 444](https://wiki.math.ntnu.no/_media/ma3001/2025h/analyticnumbertheory/heathbrowntwelfthmoment.pdf#page=2),
   DOI [10.1093/qmath/29.4.443](https://doi.org/10.1093/qmath/29.4.443).
   The needed unconditional scalar statement is

       integral_0^T |zeta(1/2+it)|^12 dt << T^2(log T)^17.

   The scan's extracted text omits its displayed Theorem 1 formula.
   Screenshot requests returned only text markers, so visual reading
   is not claimed. The exact formula and its unconditional scalar scope
   were independently read in A. Ivic, *On some mean value results for
   the zeta-function and a divisor problem*,
   [arXiv:1406.0604v1, 3 June 2014, Lemma 10 and proof, p. 7](https://arxiv.org/pdf/1406.0604v1#page=7).
   This primary paper explicitly attributes the finite-log endpoint
   to Heath-Brown. W. G. Zhai, *Asymptotics for a class of arithmetic
   functions*, Acta Arith. 170 (2015), 135–160,
   [proof of Lemma 3.3, p. 140](https://www.impan.pl/shop/publication/transaction/download/product/82193#page=6),
   supplies the same readable corroboration. No derivative version
   is asserted by these statements. We import the named theorem,
   not a reproof of Heath-Brown's large-value argument.

2. M. J. Curran and A. Heycock, *Sharp bounds for joint moments of
   the Riemann zeta function*,
   [arXiv:2403.00902v1, 1 March 2024, Section 4, p. 8](https://arxiv.org/pdf/2403.00902v1#page=8).
   For fixed n and k>=1/2 their Cauchy/Hölder calculation bounds the
   2k moment of zeta^(n) by (log T)^(2nk) times the maximum shifted
   scalar 2k moment over |z|=1/log T. Their subsequent sharp bound
   is unconditional only for k<=2, and assumes RH for k>2.
   We use only the transfer calculation at k=6, with the weaker
   Heath-Brown input, and must justify that shifted input separately.
   The printed Cauchy prefactor is reciprocal n!, a typo: any later
   proof must use the standard n! prefactor. For fixed n it changes
   only the constant, not this source's big-O transfer. Their Gabriel
   reference lists 1972; the original publication is 1927. Neither
   reference typo supplies a mathematical hypothesis. The referenced
   FHK Lemma 22 has different content in v1 and is not imported.

3. L.-P. Arguin, F. Ouimet and M. Radziwill, *Moments of the Riemann
   zeta function on short intervals of the critical line*, Ann. Probab.
   49 (2021), 3106–3141,
   [arXiv:1901.04061v4, 29 April 2021, Proposition 3.3, Corollary 3.4 and Lemma 3.5, pp. 22–24](https://arxiv.org/pdf/1901.04061v4#page=22).
   Their strip convexity applies for any p>0 to a function analytic
   on the closed strip and tending uniformly to zero at imaginary
   infinity; I(sigma)=integral_R |F(sigma+it)|^p dt is log-convex.
   Corollary 3.4 adds right-half-plane analyticity and I(sigma)->0.
   Lemma 3.5 constructs entire rectangle windows for b1 in (0,1)
   and positive Delta,L,A,b2, with interior approximation and tails
   of arbitrarily high polynomial order. Its full proof was read,
   including the compact positive-frequency construction, integration
   by parts, Fourier inversion and horizontal decay. These results
   are unconditional. Their Proposition 3.6's probabilistic
   unsmoothing conclusion is not used as an all-height theorem.

## Authorized later specialization, not a completed proof

The separate research attempt may specialize the inspected scalar moment,
Cauchy/Hölder transfer and analytic strip-convexity/localization tools to
orders n=0,1,2 and then to the exact saved concentration target. It must
write the following applicability checks explicitly:

- Cancel or exclude zeta's pole before applying strip convexity to an
  analytic localized function; verify uniform decay and finite boundary
  integrals. Control complete localization tails with the global scalar
  moment, rather than discard them or assert compact analytic support.
- Bound every shift on the Cauchy circle uniformly. For negative
  horizontal shifts use the standard zeta functional equation and a
  bounded gamma multiplier on the O(1/log H) strip; retain the small
  vertical endpoint shifts. Use nonnegative majorization on enlarged
  dyadic intervals, with no signed subtraction or exceptional-height
  quantifier and no H^epsilon substituted for a logarithmic loss.
- Transfer complex s derivatives to ordinary f derivatives through
  L391 (3), retaining Omega, Omega' and all powers of i. L389's
  f=constant-sign Hardy identity holds even at zeros. Divisors L^j
  are taken after differentiation. Any finite logarithmic loss suffices;
  no optimal logarithmic exponent or higher-moment asymptotic is required.
- Use L390's complete physical |Delta| bound and L401's actual square
  weight, without a finite response approximation, an independent carrier
  or a lower bound for the weight. The positive mean must be absorbed at
  a fixed onset for every sufficiently large real H. Record the resulting
  finite K honestly and compare the achieved threshold with the target.

This is a known-tool application: a new proof is needed only for the
family-specific specialization and concentration conclusion absent from
the sources. No sharp eighth/twelfth moment conjecture, RH, derivative
moment conjecture or unproved mixed moment is authorized. If the input
specialization fails, preserve the failure and park that implementation.
The review does not establish the proposed Hardy moment or measure bound.

## Mathlib

Full matching higher-moment and physical discriminant measure theorems
have not been checked in Mathlib. Availability is unknown, not absent.
The informal step imports named analytic theorems with the hypotheses
above; Mathlib coverage is not a completion gate.
