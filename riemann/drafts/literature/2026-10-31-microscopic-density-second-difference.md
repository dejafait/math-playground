# Microscopic density differences: completed source comparison

TARGET: Assess source coverage and recorded overlap for an actual-height microscopic second-difference L1 lower bound for |A_M|^2 at h=1/log T and scale T log T, with L477's fixed M.
CHECKED: 2026-10-31
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Completed finite-difference, shifted-density, translation-L1 and microscopic size-biased searches; compared the specified local ratio, Hardy/Haar, saturation, coarea and actual-phase failure records. No matching sharp-polynomial absolute-difference theorem was identified; this is not a novelty or impossibility claim.
SOURCE_EVIDENCE: Inspected Kovaleva arXiv:2401.13725v1 Theorem 1.1 pp. 2--3, Lemma 3.1 p. 13, Proposition 3.3 pp. 15--16 and Section 5 opening p. 20; Curran arXiv:2303.10123v2 Theorem 1.1, Lemmas 2.1/2.3 and proof outline; de Boor, Divided Differences, Surveys in Approximation Theory 1 (2005), Section 9 (46)--(48), p. 62, including its proof. Reused Heap--Soundararajan v1 Section 5 (14), p. 9, and checked its full finite-sum derivation. Exact primary links and qualifications below.
COMPARISON: Kovaleva covers microscopic products of full-zeta densities, not this absolute difference of a sharp finite polynomial. Curran's general shifted upper bound assumes RH. Standard finite-height polynomial mean values and the Peano representation are usable supporting inputs, but neither supplies the requested L1 lower bound.
GAP: The c T log T absolute-difference bound, or an adequate actual-height joint-density mechanism proving it, remains unestablished; no full-zeta-to-sharp-polynomial transfer is available from the inspected results. The finite-interval curvature interface is separately source-covered but not specialized in this literature turn.
REASON: Park direct import of a joint shifted-density lower bound from these sources. Source scope, rather than source access, blocks that import. A narrower independent Peano-kernel specialization can resolve the explicitly recorded transfer gap without assuming the unproved density bound; no new mathematical result is asserted here.
LITERATURE_REASON: The previously unassessed observable changes from a grouped coefficient certificate to an absolute microscopic density difference; exact primary hypotheses and a finite-interval transfer source were essential unread inputs.
SCOPE: Literature and local overlap only. This decision does not authorize a joint-law theorem, a sharp-polynomial replacement, a norm lower bound, or new mathematics in this completed turn.

## Completed comparison, 31 October 2026

### Gap, target, use and decision test

The main gap is actual-Xi all-degree positivity, including initial
indices at unbounded heights. The intermediate target is precisely the
T log T bound in TARGET and in the preserved nomination below. A
curvature transfer could make it useful for the actual L481 ratio norm;
comparison with the complete L477 residual, both defect thresholds,
negative mass and Xi signs would still be independent gaps.

Continue a direct source import only if a theorem covers the exact
sharp M, microscopic shifts, actual finite height interval and an
absolute lower bound with a fixed positive normalized constant. Park
that import if only product moments, RH-dependent bounds or fixed-N
Haar limits are available. This review meets the parking condition for
that import, not a mathematical abandonment test for the conjectured
bound. No proof of its falsity or novelty follows.

### Primary inputs actually read

**Kovaleva, Correlations of the squares of the Riemann zeta on the
critical line, arXiv:2401.13725v1 (24 January 2024).**
[Primary version](https://arxiv.org/pdf/2401.13725v1).
Theorem 1.1, pp. 2--3: T>=10, alpha,beta>=0, delta=beta-alpha>=0;
the integral of the two shifted full-zeta absolute squares has explicit
diagonal/off-diagonal main terms and error
O_epsilon((T+alpha)^(2/3+epsilon)+(T+alpha)^(1/2+epsilon)delta^(1/3)+delta^(1/2)).
Microscopic shifts are not excluded. Inspected Lemma 3.1's functional-
equation expansion, Proposition 3.3's smoothed divisor-weighted double
sum, and the small-shift conditions (5.1)--(5.2)/weight (5.3).
These are full-zeta product computations, not the sharp rectangular
n,m<=M density. No deletion of a second functional-equation piece or
uniform sharp-cutoff replacement is justified here. Even the product
formula is not itself an absolute second-difference lower bound. This
is a scope comparison, not an audit of the complete manuscript.

**Curran, Correlations of the Riemann zeta function,
arXiv:2303.10123v2, Theorem 1.1.**
[Primary version](https://arxiv.org/html/2303.10123v2).
For fixed nonnegative beta_k and |alpha_k|<=T/2, sufficiently large T
in terms of the exponents, the theorem bounds the shifted product
moment above by

    T (log T)^(sum beta_k^2)
       product_(j<k)|zeta(1+i(alpha_j-alpha_k)+1/log T)|^(2 beta_j beta_k),

with an exponent-dependent constant, **assuming RH**. Read Lemma
2.1 and the proof opening: the log-zeta majorant uses that assumption.
It cannot be used as an unconditional input toward RH. Lemma 2.3,
the Montgomery--Vaughan finite-polynomial mean square, is separately
unconditional. The theorem supplies neither a sharp-polynomial
absolute difference nor its desired lower bound.

**Heap--Soundararajan, Lower bounds for moments of zeta and L-functions
revisited, arXiv:2007.13154v1, Section 5 (14), p. 9.**
[Primary version](https://arxiv.org/pdf/2007.13154v1).
Reuse the assessment in
`2026-10-29-complete-residual-short-resonator-fourth-moment.md`
and L481 Section 1. The arbitrary complex coefficients mean square is
(T+O(N log N)) sum |a_n|^2. Checked its preceding diagonal/off-diagonal
expansion and coefficient-square bound. This allows growing finite
polynomials with the stated error retained. It does not replace
absolute nonlinear observables by their diagonal. Products must keep
their actual multiplied length; the disjoint-prime-support splitting
formula is not applicable to overlapping full-integer polynomials.
No shifted density moment or interpolation bound was derived here.

**de Boor, Divided Differences, Surveys in Approximation Theory 1
(2005), 46--69, Section 9, p. 62, (46)--(48).**
[Primary journal text](https://surveys-in-approximation-theory.com/papers/2/2.pdf).
For real knots tau=(tau_0,...,tau_k) in [a,b], with tau_0<tau_k,
and f smooth enough for Taylor's integral formula, the normalized
B-spline representation is

    [tau_0,...,tau_k]f = (1/k!) integral_a^b M(y|tau) f^(k)(y) dy,
    M(y|tau)=k DD_tau g_y, with g_y(x)=(x-y)_+^(k-1).

The kernel has integral one. Read the proof: Taylor's integral remainder,
annihilation of polynomials of degree less than k, and commuting the
finite evaluation functional with integration. Our proposed application
has three distinct equally spaced real knots and a finite smooth
exponential polynomial, so no weak-regularity extension or new theorem
is needed. Equal-spacing constants, identification with L481's U, and
the finite-interval integration are reserved for the separate research
specialization; no such argument is derived in this review.

### Narrow local comparison

Read L477's hypotheses/conclusion and Sections 3--4 for its exact fixed
cutoff and both residual components; read L481's hypotheses/conclusion
and Section 1 for U, its finite-height tool and concentration stop.
Read the L572 and constructive-chirp ATTEMPTS records. Reuse the
completed Hardy-L1, Euler-phase and coarea comparisons. Specifically:

- L572 stops the complete ascending-rank coefficient certificate only.
  It neither tests this density difference nor bounds the actual norm.
- L481 stops the complete-residual second/fourth-moment certificate.
  It does not prove that the new observable has a useful moment ratio.
  Repeating that certificate without changed information is not a new
  mechanism.
- Global and weighted saturation, sign-boundary/chirp, Haar-transfer
  and stationary-involution limitations remain. Finite differences
  alone remove none of those issues for the complete residual.
- A scoped search of L477--L486, the 29--31 October assessments and
  corresponding failure records found no completed Peano transfer or
  exact matching density-difference lower bound. This is a duplicate
  check, not an originality claim. No sibling notebook was read.

### Search and access record

Queries included `Dirichlet polynomial modulus squared small shifts
L1 second difference lower bound`, `Riemann zeta absolute difference
squared modulus microscopic shifts mean value`, `Dirichlet polynomials
short intervals second differences L1 norm Bernstein inequality`,
`zeta differences absolute shifts moment`, `Dirichlet polynomials
shifted moments mean value`, `zeta modulus small shifts difference`,
`zeta difference squares shifted moment absolute`, `Dirichlet
polynomial modulus variation norm`, `zeta microscopic size-biased`,
`zeta absolute difference moments`, `Dirichlet polynomials translation
L1`, and `de Boor divided differences Genocchi pdf`.

Searches also surfaced Bernstein inequalities, projection constants,
random multiplicative models and arithmetic short-interval variances;
these were not inspected as matching theorems and are not inputs.
Kovaleva's Corollary 1.3 was seen but is not imported or specialized.
Curran's cited unconditional two-shift work arXiv:2301.10634 and his
subsequent lower-bound work remain unread leads, not evidence for this
absolute sharp-polynomial observable. No inference of novelty follows
from these searches.

The guessed Kovaleva v2 HTML endpoint returned 404; v1 PDF theorem and
proof-case text were accessible through the web reader. Shell download
failed DNS and the first screenshot timed out; neither prevented the
specified primary reads. No inaccessible source is asserted to be an
essential blocker. The blocking issue is missing theorem scope.
Full matching and supporting Mathlib coverage remain unchecked.

### Next bounded work and its limit

A separate assessment nominates the known Peano formula's specialization
in `2026-10-31-density-curvature-peano-transfer.md`. It addresses the
previously explicit interface gap without needing a joint-density law.
The full T log T bound is preserved as unproved, and this is not a
creative proof mechanism for it. Creative routing remains blocked by
the lack of a concrete source-covered density-norm mechanism, rather
than by the absence of a generic calculus formula. The newly written
assessment requires separate continuation approval next turn.

## Original nomination, preserved; source status superseded above

The proposed object is the exact finite polynomial

    A_M(t)=sum_(1<=n<=M) n^(-1/2-it),
    M=floor(sqrt(T/(2pi))), h=1/log T,
    F_M(t)=|A_M(t)|^2,
    Delta_h^2 F_M(t)=F_M(t+h)-2F_M(t)+F_M(t-h).

The proposed test is a fixed positive lower bound c T log T for the
integral of |Delta_h^2 F_M| on [T+h,2T-h], for all sufficiently large
real T. A theorem restricted to an explicitly justified unbounded
sequence may still be useful, but must be distinguished from this
uniform target. No such bound, limiting distribution, sign or
derivative-transfer theorem is asserted here.

The intended downstream use is to seek a full-scale lower bound for
the actual L481 ratio norm through a rigorously justified relation to
density curvature. The relation and its finite-interval boundary costs
must themselves be checked against precise hypotheses. Even a successful
ratio lower bound would leave its transfer to the full L477 residual,
both defect thresholds, negative-mass saving and Xi positivity open.

First compare the specific finite-difference and shifted-density
functional with the local ratio, concentration, saturation and actual
phase failure records. Then retrieve primary statements for microscopic
shifts of finite Dirichlet-polynomial densities, their L1 differences,
and any essential finite-interval norm comparison. Moment formulae
alone do not establish the desired absolute lower bound; no finite-height
Haar replacement, independent-phase model, ignored cutoff term, or
unspecified uniform integrability is allowed. Record unread leads as
unread, and do not infer novelty from unsuccessful searches.

Continue only if the comparison identifies an applicable known theorem
or a genuinely different bounded test with adequate inputs. Park this
candidate if it is an equivalent reformulation of a recorded failed
certificate without new usable information, or if essential joint-shift
coverage remains persistently unavailable. Full and supporting Mathlib
coverage are unchecked. There is no cross-notebook input.

This nomination is not a ready research gate. A future creative attempt
would require a separately covered mechanism and an explicit decisive
test at the named T log T threshold; no proof-purpose escalation is
claimed during this completed ordinary L572 audit.
