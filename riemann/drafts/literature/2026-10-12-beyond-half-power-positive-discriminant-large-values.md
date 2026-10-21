# Beyond-half-power concentration — source coverage ready

TARGET: Test whether unconditional large-value bounds for ordinary Hardy jets through order two improve L403's positive-discriminant measure bound to c H^(1/2+delta)(log H)^(-K), for some fixed delta>0 and K>=0 and every sufficiently large real H.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched unconditional critical-line large values, stronger twelfth/eighth moments and derivative upper bounds; followed the October 2026 reference in arXiv:2506.16766v2; checked the October 12 local concentration records and L154's different-statistic failure.
SOURCE_EVIDENCE: Read de Faveri–Pandey arXiv:2610.01035v1 Theorem 10.1 and its complete three-range proof, p. 18; Theorem 9.1 and relevant proof cases, pp. 15–18; Trudgian–Yang arXiv:2306.05599v3 Lemma 5.1 and its exponent-pair sequence, pp. 21–22; Guth–Maynard v2 Theorem 1.1, Proposition 3.1 and both subdivision cases, pp. 1–2, 9–10, and Proposition 12.1, pp. 47–48; Durkan–Palojarvi–Trudgian v2 Corollary 1, p. 2.
COMPARISON: L403's scalar height exponent is two; the inspected new scalar theorem has a fixed saving d=520/445121 before epsilon. This supplies the previously missing source input; ordinary-jet localization and the exact positive-set specialization still require proof. A logarithmic improvement alone would not meet the saved target.
GAP: Transfer the improved scalar bound uniformly to ordinary jets through order two and apply it to the exact complete Y=Delta[Re(R zeta(5/2+it))f]^2, retaining a fixed height saving after every loss and all-real-H quantifiers.
REASON: The theorem is unconditional and quantitatively relevant; cite it directly and derive only the family-specific transfer and concentration conclusion in a later research turn. Neither local improvement nor originality is established by this source review.
LITERATURE_REASON: Essential stronger scalar distributional coverage was missing at invocation; a newly found primary theorem changes the source comparison and permits ending this literature-only step.
SCOPE: The unchanged saved target; fixed ordinary jet orders 0,1,2; complete bounded right-line response; Gaussian pole cancellation, strip convexity, small-shift functional equation, Cauchy transfer and positive-set Holder restriction. No direct separated-value transfer or growing head/order is approved.

The main gap remains global actual-theta mixed positivity. This proposed
intermediate test could further constrain attempts to ignore the positive
physical-discriminant set in a weakened sign strategy. It would still
leave the total L367 signed margin and actual common-zero upper counts
unresolved, and would give no RH conclusion by itself.

Reuse L403 (1)-(3), L401 (1), (3) with its exact positive square weight,
L390's full physical |Delta|<=C U and L391's zero-safe ordinary jet
formulas. The response is complete and bounded. Orders remain fixed at
0,1,2 and constants must be independent of real H. No RH, conjectural
moment, independent carrier, weight lower bound or growing head is allowed.
The initial pending record above identified the missing source. The
completed comparison below supplies coverage, not the local conclusion.

The continuation test is still a uniform ordinary-jet estimate with a
fixed height saving that survives the complete physical concentration
argument. Fix epsilon sufficiently smaller than d, independently of H;
retain explicit slack for logarithmic losses. Stop the specialization if
localization, shifts or ordinary derivatives consume the saving. Do not
claim a specific improved delta or K until that argument is written.

Full matching Mathlib coverage is not checked. Existing L402 and L403
bounds and L394/L399/L400 failures remain preserved.

## Completed source comparison — step 95

Queries included “zeta large values Guth Maynard twelfth moment”,
“Riemann zeta large values twelve moment improvement unconditional 2026
derivative”, and “Trudgian Yang Toward optimal exponent pairs Lemma 5.1”.
Search results were leads only. Narrow local checks found no use of the
new scalar input in the October 12 concentration records. No exhaustive
novelty search is claimed.

### Essential scalar input

A. de Faveri and M. Pandey, *The sixth moment of the Riemann zeta
function*, [arXiv:2610.01035v1, 1 October 2026, Theorem 10.1, p. 18](https://arxiv.org/pdf/2610.01035v1#page=18):
for every real T>=1 and epsilon>0,

    integral_0^T |zeta(1/2+it)|^12 dt
        <<_epsilon T^(2-520/445121+epsilon).

This is an unconditional preprint theorem, not an independently audited
proof here. Read its complete proof: low values use the fourth moment,
the middle range uses Theorem 9.1 with k=6, and large values use the
exponent-pair estimate plus Bourgain's cutoff; dyadic summation covers
all heights. Read Theorem 5.1's hypotheses and Section 9's perturbation,
spacing and energy applications. Its conclusion is scalar, not a Hardy-jet or
discriminant theorem. Import the stated moment, without reproving its
large-value mechanism. No unquantified logarithmic version is needed.

T. S. Trudgian and A. Yang, *Toward optimal exponent pairs*, Math.
Comp. 94 (2025), 1467–1502,
[arXiv:2306.05599v3, Lemma 5.1 and the following sequence, pp. 21–22](https://arxiv.org/pdf/2306.05599v3#page=21),
supplies the high-value supporting input. For an exponent pair
(k,l), k>0, epsilon>0, values at points |t_r|<=T with mutual distance
at least one satisfy

    R <<_epsilon T^(1+epsilon) V^(-6)
           + T^(1+l/k+epsilon) V^(-2(1+2k+2l)/k).

Its B-transformed sequence permits pairs with arbitrarily small positive
epsilon perturbation of the first coordinate; that perturbation must
not be silently removed from a big-O assertion. This source's role is
already included in the imported moment theorem; no separate
application to the notebook's jets is proposed.

### Screened alternatives and qualifications

L. Guth and J. Maynard, *New large value estimates for Dirichlet
polynomials*, Ann. Math. 203 (2026), 623–675,
[arXiv:2405.20552v2, 7 April 2026, Theorem 1.1, pp. 1–2](https://arxiv.org/pdf/2405.20552v2#page=1),
assumes |b_n|<=1 and 1-separated points in [0,T] where the sum over
N<=n<=2N has modulus at least V. It gives

    R <= T^o(1) [N^2 V^(-2)+N^(18/5)V^(-4)+T N^(12/5)V^(-4)].

Read the shorter/longer interval cases deriving this from Proposition
3.1 and the long-polynomial refinement, Proposition 12.1. Neither is a
direct continuous ordinary-jet estimate. A zero-density corollary is
not the required concentration input. No blanket obstruction to using
this theorem in other mechanisms is asserted.

B. Durkan, N. Palojarvi and T. S. Trudgian, *The error term of the
fourth moment of the Riemann zeta-function*,
[arXiv:2506.16766v2, 4 October 2026, Corollary 1 and Remark 1, p. 2](https://arxiv.org/pdf/2506.16766v2#page=2),
gives, for fixed 8<=k<=12, the upper bound
T^(1+(k-4)/8)(log T)^((11k-12)/8), including
T^2(log T)^15 at k=12. This alone improves logarithms, not the requested
height exponent. Its reference list supplied the decisive new lead.

N. Ng, Q. Shen and P.-J. Wong, *The eighth moment of the Riemann
zeta function*, JEMS 28 (2026), 4175–4237,
[published introduction and Theorem 1.1](https://ems.press/content/serial-article-files/53325),
assumes RH and a quaternary additive-divisor conjecture for its
asymptotic. It is excluded. Florea's
[arXiv:2509.20335v1, Section 3.2, p. 9](https://arxiv.org/pdf/2509.20335v1#page=9)
was screened for moment terminology and unconditional/conditional
scope, not used as evidence against later results. Lower-bound and
discrete derivative search hits were not imported as upper tails.

## Later specialization obligations

Reuse the already assessed AOR Proposition 3.3 and fixed-order Cauchy
transfer from the half-power assessment; L403's audit verified their
hypotheses for that input. The stronger power changes the boundary
budget, so the later proof must recheck the following applications:

- The entire window (s-1)zeta(s)exp((s-3iH/2)^2/H^2)/H cancels
  the pole. Bound both full Gaussian tails with the new global scalar
  theorem and conjugation, with constants independent of real H.
  Compare the right boundary's O(H) term with the stronger budget;
  verify finite boundary integrals and uniform decay before convexity.
- Retain every shift |w|<=1/log H and the enlarged sharp interval.
  Use the small-strip functional equation for negative horizontal
  shifts, correct j! Cauchy factors and nonnegative restrictions.
  Do not infer jet large-value counts merely from scalar separated points.
- Use L391 (3)'s exact ordinary formulas, including Omega', with
  L^j divided after differentiation. Keep orders fixed and values
  zero-safe; absorb all logarithmic costs with explicitly reserved slack.
- Use L390's full physical |Delta|<=C U and L401 (1), (3)'s exact
  W=Re(RZ)f with complete Z=zeta(5/2+it). Apply the positive-set
  restriction already proved in L403, without a weight lower bound,
  phase independence, growing response head or a total pencil margin.
  Choose one fixed epsilon and one onset valid for every real H.

This gives adequate source coverage for a later REPRODUCTION attempt
at the unchanged target. The family-specific estimate is absent from
the inspected theorem statements and needs that applicability proof.
Coverage approval does not establish the estimate. The main mixed
positivity gap, total L367 margin and actual common-zero upper counts
remain open; no new RH argument or UNVERIFIED CANDIDATE is proposed.
No lemmas or mathematical scripts were modified in this literature turn.
