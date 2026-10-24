# Coverage review: rounded endpoint at every height

TARGET: Review literature and local estimate coverage for proving D_{n(a)}(Ξ;a)>0 for every sufficiently large real a, with n(a)=ceil(log(a/(2π))/4), retaining the pinned external-input qualification.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched Riemann Xi generalized Laguerre inequalities large order/uniform/logarithmic/saddle point and shifted Laguerre-Pólya results; inspected Csordas 1309.0055v2, Wagner 2108.01827v2 and the Wang–Yang institutional manuscript at theorem level. Scoped local checks compared L296, L299–L304, L330, C294a/C294b and the endpoint freezing/Mellin/Liouville failures; reused the October overlap and Littlewood assessments. No inspected theorem states the rounded-index claim; no novelty or exhaustive-search claim.
SOURCE_EVIDENCE: Csordas, arXiv:1309.0055v2, Definition 1.2, Theorem 3.5, Lemma 3.6 and Theorem 3.7 with proof; Wagner, arXiv:2108.01827v2 (27 June 2022), shifted-class definition, Theorems 1.2/1.4 and proof of 1.2; Wang–Yang, Laguerre inequalities and complete monotonicity for the Riemann Xi-function and the partition function, institutional manuscript, equations (1.1)–(1.4), Theorem 1.3, pp. 1–4. Read the complete local L288 and L299–L304 proofs, L330's relative-error proof, C294a/C294b proofs, L296 and the general L269 contour/parameter formulas; L452 (1) and C452a's complete audited assembly supply the already covered analytic and normalization inputs.
COMPARISON: Associated-kernel criteria retain an unproved positive-definiteness premise; shifted-derivative and coefficient inequalities concern different functions/indices. C452a covers paired heights and L296 excludes h tending to 5. Their proofs supply concrete exact-summand, moving-boundary and Mellin mechanisms for a bounded parameter specialization, but not an already uniform rounded-index theorem.
GAP: Establish the exact ceiling-to-saddle parameter domain, then extend the clipped-patch sums, both same-sign strips, both mixed sectors and normalized Mellin kernel to that domain with one onset and error smaller than a proved zeta-square margin. Neither that extension nor the rounded-index sign is proved by this review.
REASON: The changed rounding domain is outside the completed audit. Essential source comparison is now complete for one bounded specialization attempt; reproof of Littlewood interpolation or the pinned half-plane theorem is unnecessary. A matching source theorem cannot be imported in place of the remaining parameter-uniformity argument.
SCOPE: One attempt on the exact rounded-index target using existing endpoint sector/Mellin methods and the pinned external input; no fixed-r all-height positivity, arbitrary-phase positivity, smaller-index extension, new zero-free region or RH claim.
LITERATURE_REASON: The ceiling prescription changes C452a's coupled parameter domain; its sector and kernel uniformity had not been assessed, while the fixed-strip source hypothesis itself is unchanged.
COVERED_TARGET: Attempt to prove D_{n(a)}(Ξ;a)>0 for every sufficiently large real a, with n(a)=ceil(log(a/(2π))/4), by extending the endpoint sector and Mellin estimates uniformly, retaining the pinned external-input qualification.

## Relevance and decision

The main gap remains global mixed positivity. The intermediate target is
one sign at the stated rounded index for every sufficiently large height.
It could remove C452a's discrete-height restriction and support subsequent
comparisons with the logarithmic witness range. It would not cover the
initial segment of smaller indices, bounded exterior heights, or all
mixed forms. No full route to RH is asserted.

The decision approves coverage for an attempt, not the truth of a uniform
extension. The newly written continuation needs the supervisor's separate
approval next turn. Mathematical work should be classified REPRODUCTION
if it is confined to this known-method specialization; this source review
does not certify originality. No mathematical derivation is undertaken here.

## Primary-source comparison

The bounded searches used `"Riemann Xi" "Laguerre" inequalities large order uniform`,
`"generalized Laguerre" "zeta" logarithmic`, `"Riemann" "Laguerre" inequalities saddle point`,
`Csordas "Fourier Transforms" "Laguerre" 2013 kernels`, and shifted-class terminology.
Results about classical Laguerre polynomials and unverified proof claims were
not theorem inputs. The earlier [theta-moment screen](../../ATTEMPTS/2026-09-21-theta-moment-literature-screen.md)
already separates coefficient inequalities from the notebook's global sign
problem; its inspected overlap is reused, rather than claimed as new discovery.

George Csordas, [*Fourier transforms of positive definite kernels and the
Riemann ξ-Function*, arXiv:1309.0055v2, 21 February 2014](https://arxiv.org/html/1309.0055v2),
Definition 1.2, requires a smooth, strictly positive, even kernel, decreasing
on the positive axis, with all derivatives decaying faster than a Gaussian
of some power greater than two. Theorem 3.5 adds strict logarithmic
concavity and establishes admissibility of the associated kernels. Lemma
3.6 and Theorem 3.7 identify their cosine transforms with the generalized
Laguerre expressions; real-rootedness still requires positive definiteness
of every associated kernel. Their proofs and normalization were inspected.
This is a representation/criterion, not the needed rounded-index estimate;
kernel positivity is not its positive-definiteness premise. No new theorem
application or normalization conversion is asserted here.

Ian Wagner, [*On a new class of Laguerre-Pólya type functions with
applications in number theory*, arXiv:2108.01827v2, 27 June 2022](https://arxiv.org/html/2108.01827v2),
Theorem 1.2 assumes membership in the shifted Laguerre–Pólya class and,
for each fixed degree d, states nonnegative inequalities of orders at most
d for sufficiently high derivatives. Theorem 1.4 concerns shifted Taylor
coefficients of suitable completed L-functions or modular forms. Read the
class definition, both statements and the derivative-approximation proof
of 1.2. Neither statement removes the derivative shift to give the original
Ξ at an unbounded real argument with its Laguerre order tied to that height.
No reproof, applicability claim beyond this comparison, or audit of that
paper's full proof is needed.

Larry X. W. Wang and Neil N. Y. Yang, [*Laguerre inequalities and complete
monotonicity for the Riemann Xi-function and the partition function*,
institution-hosted manuscript](https://cfc.nankai.edu.cn/_upload/article/files/81/18/f83d37e449ebaf1b2f4141fa59be/9323c2fc-4d6a-4610-a747-1bd985a7be41.pdf),
pp. 1–4, equations (1.1)–(1.4) and Theorem 1.3, concerns the Maclaurin
sequence γ(n). The printed quantifiers are: for each order r there exists
c such that the coefficient inequality holds for n>cr³. The manuscript
has placeholder publication metadata, so no final journal pagination or
order-independent c is inferred. Its sequence index is not the real height
a in D_n(Ξ;a). This confirms the earlier screen's scope comparison and
does not supply a rounding theorem.

The [Littlewood assessment](2026-10-21-fixed-half-plane-endpoint-derivative-review.md)
and [assembly assessment](2026-10-22-fixed-half-plane-endpoint-assembly.md)
remain adequate for the unchanged analytic input. They record direct
inspection of Titchmarsh, second edition (1986), Theorem 14.2 and proof,
pp. 336–337, and Section 14.3, pp. 338–339. Its printed RH hypothesis
is not being imported. L452 is the separately audited fixed-disk
specialization under OpenAI's pinned September 30, 2026, Theorem 1.1,
commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`. Its (1) is uniform
for all sufficiently large t and 63/64≤Re(s)≤2; its (2) has only the
stated paired parameters. Reuse (1) and the existing kernel argument,
without treating (2) as a theorem about changed kernels. The
[external-input register](../../foundations/2026-10-quasi-riemann-input.md)
retains the strict Re(s)>7/8 boundary, allowed pole, and unaudited external
manuscript/formal-import closure. No fresh external-input audit is claimed.

## Exact local uniformity questions

The following are coverage findings about existing proofs, not proofs
that their estimates extend.

L269 defines the saddle by `(2πexp(2r))²=a²+(n/r+9/2)²` and
`h=n/r+9/2`. L296 already records the exact map
`r_a(h)=log(a/(2π))/2+log(1+h²/a²)/4` and
`n=r_a(h)(h−9/2)`. The proposed ceiling uses the uncorrected logarithm.
A proof must first identify its exact saddle domain, including which
side of h=5 occurs near ceiling jumps; it must not assume h≥5 or r=2n.
No bounds for that new domain are proved here. This is also why neither
continuity at a_n nor the fixed compact bands in L296 settle the target.

L288's exact central weight, before its fixed-head limiting argument, is
`(jk)^(−1/2)(1−log(jk)/(2r))^(2n)`. L299's clipped patches and L300's
complement instead specialize the exponent to r. The needed extension
must retain the exact 2n exponent, prove uniform normalized amplitude
derivatives on every nonempty patch, and bound the full moving-boundary
weight mass. Their Fresnel primitive bounds and fixed real phase change
are already explicit and uniform over interval endpoints. L300's finite
harmonic head and exponentially cut off tail supply a concrete alternative
to L288's nonuniform infinite summability as h approaches 5. Merely taking
h₀ down to 5 in L288/L296 would revive the recorded harmonic obstruction.

L301's same-sign strip proof uses polynomial derivatives through order
two, a strict curvature saving below a fixed sum-coordinate cutoff, and
retained lower endpoints in its tail variation. L295 supplies its exact
general-2n amplitude and tangent bound. A changed exponent requires a
uniform recheck of both parts; dropping the polynomial curvature loses
the demonstrated boundary saving. C294a's mixed estimate has a strict
positive decay rate at h=5; C294b gives an inspected uniform interval
below 5. Neither statement alone is a theorem on a neighborhood crossing
5. Their exact general-exponent amplitude, derivative maximization,
integrable tails and vanishing boundary terms specify what to recheck
on the rounding domain. No new mixed estimate is established here.

L303's scalar inversion and its full-series identity are exact, and L304
already allows real r. However their kernel exponent and Γ-factor follow
the weight exponent r; real-r coverage does not free 2n from r. The next
attempt must obtain the correct changed Mellin kernel, normalize its
integral exactly, choose an absolutely convergent zeta line, and prove
bounded absolute mass and a sufficiently small complete tail. Then it
must verify L330's integrated relative-variation argument on that kernel
using L452 (1) at both shifted heights. The reciprocal-series lower bound
must be used only to the right of 1. No generalized kernel formula or
sign is derived or approved as already true by this review.

Finally the whole-plane assembly must retain every sector, coefficient
extraction, reflection and positive Jacobian factor. C452a's audited
normalization is the reference, not a license to substitute parameters
in its asymptotic. A single uniform onset must work for the full continuum,
including each side of the ceiling jumps and the jump heights themselves.

## Failures, bounded test and continuation

The [absolute-freezing failure](../../ATTEMPTS/2026-09-24-endpoint-saddle-freezing-test.md)
has coefficientwise error r²+O(r), versus a guaranteed square of order
r^(−2). The [old derivative-envelope failure](../../ATTEMPTS/2026-09-24-endpoint-logarithmic-derivative-test.md)
concerns the old shrinking regions, superseded only for actual ζ by
the qualified L452 input. The [Mellin failure](../../ATTEMPTS/2026-09-24-endpoint-mellin-test.md)
excludes automatic positive averaging, not a controlled relative comparison.
L335 and [its recorded attempt](../../ATTEMPTS/2026-09-24-endpoint-liouville-phase-test.md)
give negative arithmetic values at arbitrarily late heights for fixed r;
this is not the new domain in which r changes with a. All these stops
remain intact. The local search found no already stated rounded-index
theorem; this is a scoped duplicate check, not an assertion of novelty.

Continue the separately approved attempt only if the exact parameter
conversion, complete sector/cutoff error and generalized-kernel variation
give an error strictly smaller than a proved positive frozen-square margin,
with constants independent of the rounding position. A uniform relative
o(1) comparison and an additive error little-o of the reciprocal-series
lower margin are a sufficient test; the Mellin tail need not be smaller
than the sector error if compared with the square first. If any sector,
normalization, convergence line or jump endpoint fails this test, record
that specific obstruction and stop this implementation without claiming
a negative actual coefficient. Do not reopen fixed-r phase-uniform signing
or replace signed integrals by positive averages.

Essential continuation inputs are C452a, L452, L302, L303, L304 and L330,
with L269/L288/L295/L296, L299–L301 and C294a/C294b supplying the inspected
parameter and sector mechanisms. Unresolved assumptions are the proposed
uniform extension and the unchanged external-input qualification. Smaller
indices, bounded exterior heights, global mixed positivity and selected-law/
regulator gaps remain unresolved. Full matching Mathlib coverage is not
checked; no absence is asserted. No lemma, mathematical script, DAG or main
argument changed in this literature-only step.
