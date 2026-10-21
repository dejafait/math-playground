# Smooth-action branch quantitative remainder — completed source comparison

TARGET: Assess source coverage for the smooth-action branch bound |V_i-a^(-3)K_(i,Vmix)|<=C_i N^(5/2)log(eN)^2 against L179's coefficient, for both actual probes.
CHECKED: 2026-10-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Read L175's statement/order, L176--L179's complete relevant arguments, L159's tensor multiplier proof, L156's prefix covariance, L028's consistency statement, histories 207/209 and ATTEMPTS/030/038/045; searched exact local target fields and the five external queries below. No matching quantitative theorem was established; no novelty is inferred.
SOURCE_EVIDENCE: Reused the ready cubic-residual/action, smooth-action audit, complete-coefficient, reverse-crossed and gradient-base assessments; reinspected Benzi--Simoncini 1501.07376v1 Theorems 4.1--4.4, section 5, Theorem 6.1/proof, Corollaries 6.2--6.3 and section 6.2 (6.3)--(6.4), printed pp. 6--8, 11--15.
COMPARISON: Explicit L175--L177 errors and L178's finite polynomial error are reusable; L179's successive fixed-mass/degree limits give no quantitative mesh remainder. Scalar matrix decay, scalar Toeplitz rates and renormalized Ward/flow finiteness do not directly cover this two-level pinned trace. L255 concerns another branch.
GAP: Quantify the second-prefix replacement without its present left-mass loss, then control the remaining ordered static trace, relative boundary, coefficient/heat matching and comparison with exactly L179(7); the full stated remainder remains unproved.
REASON: The bounded comparison supplies ready tool coverage for the stated rate investigation and the separately specified first test below; no essential source is inaccessible. EXPLORE approves an attempt, not a bound or originality claim.
LITERATURE_REASON: The target changes from the audited action-Hessian branch to a quantitative smooth-action companion remainder; existing qualitative-limit coverage does not establish coverage for this rate.
SCOPE: Same relative SU(2) box, even N, a=8/N, tau=1/16, lower-rooted forest, stored coordinates, bare-first order and probes 3,6; preserve both long axial profiles, separate coefficient levels, both subtractions, all action faces, constant modes and complete heat sums.
COVERED_TARGET: Test the massless second-prefix bound |W_i^0-U_i^0(F^0)|<=C_i N^(5/2) for both actual probes, with U_i^0 given by L177(2) at H=M tensor G.

This literature-only turn establishes no estimate and changes no lemma or
mathematical script. The original full-rate target is preserved. The covered
first test is a proposed strengthening, not a consequence asserted here.

The main gap remains ultraviolet-uniform interacting matching with reflected
error <=c_box/2, followed by the continuum axioms and finite positive infrared
mass. The intermediate full remainder would support quantitative assembly of
the cubic residual/action response with L255. It would neither bound the
interacting remainder nor finish L011's other components. K_(i,Vmix) is
exactly L179(7)'s coefficient, distinct from L120's K_(i,V); L180's evaluation
does not provide a remainder.

## Existing estimates and the precise missing information

The following are quotations of existing bounds, not newly derived rates.

| Input | Available conclusion | Qualification for the proposed rate |
| --- | --- | --- |
| L175(2)--(3) | V_i differs from the ordered K m J F A^gen M_h S trace by O(N^(5/2)log(eN)^(1/4)). | Direct Hodge, both Q subtractions, axial transport and midpoint errors are already accounted for; reuse them. |
| L176(3) | Replacing only K by M tensor G costs O(N^(5/2)sqrt(log(eN))); its left mass costs O(N^3 epsilon^(1/4)). | F remains the full relative prefix inverse. No coefficient freezing has occurred. |
| L177(3) | Replacing F by F^0 costs O(N^2 epsilon^(-1/2)); second mass delta costs O(epsilon^(-1/2)[N^2+N^3 delta^(3/4)]). | The first bound loses the left mass. The energy square for the second change has two terms; neither may be dropped. |
| L178(3) | Scaled polynomial error <=C_i epsilon^(-2)[6/(6+epsilon)]^(d+1). | Uniform in N, but absolute row sums and later freezing must retain mass/degree dependence. |
| L179(5)--(7) | Signed fixed-degree/fixed-mass limit, followed by degree and mass removal; coefficient mass error O(epsilon^(1/4)). | Five-dimensional Riemann convergence is at fixed parameters. No uniform finite-mesh localization/freezing modulus is supplied. |

L179 proof sections 1--4 retain the actual raw forest column, the action
column at eta and the generator/probe at xi. Its moving-cut strip is
O(a) with a constant depending on the fixed approximation. This is not
permission to use the same conclusion at an N-dependent degree. L176 and
L177 give finite inequalities before limits; L179's subsequent convergence
cannot be assigned varying parameters without new uniform estimates.
No optimized parameter schedule or impossibility result is derived here.

The proposed first test isolates L177's first replacement. Define U_i^0
by its same finite trace (2) with H=M tensor G, F=Phi Sigma and
F^0=(P tensor G)E_1. Thus W_i^0 is the existing L176 trace on F.
At finite N, G is the positive inverse of the transverse Dirichlet
Laplacian; this definition is not a singular infinite-volume limit.
L177(7)--(8) already give the exact difference and its positive energy
square. L159(12)--(13) already cover the massless mixed-energy multiplier
on the lower-anchored/upper-free axial domain. These are ready inputs,
not a proof of the covered target. The missing specialization is an
ordered full-spectrum trace estimate without using the left inverse's
operator supremum. No value or improved power is established this turn.

## Primary sources and applicability

Benzi--Simoncini, [*Decay bounds for functions of matrices with banded or
Kronecker structure*](https://arxiv.org/pdf/1501.07376v1), v1, 29 January
2015, printed pp. 6--8, 11--15: Theorems 4.1--4.2 assume Hermitian
positive semidefinite matrices with spectrum in [0,4rho]; polynomial
propagation proves two distance/time bounds. Theorem 4.4 integrates
three time ranges for positive definite matrices and Laplace--Stieltjes
functions, retaining the lowest eigenvalue. Section 5 uses graph distance;
dimension-uniform finite sections require no nearby function singularity.
Theorem 6.1 and Corollaries 6.2--6.3 factor tensor heat kernels; section
6.2 integrates their products. These support scalar relative tensor
localization. They do not estimate the full M,P-weighted signed trace or
remove its mass dependence. Near-diagonal and long-time cases remain
necessary. No theorem is reproved or imported as the requested remainder.

Reuse the inspected primary comparisons recorded in
[the reverse assessment](2026-10-19-reverse-crossed-quantitative-remainder.md)
and [the gradient-base assessment](2026-10-20-gradient-base-crossed-quantitative-remainder.md):

- Lawler--Limic, *Random Walk: A Modern Introduction* (2010),
  [author-hosted text](https://www.math.uchicago.edu/~lawler/srwbook.pdf),
  Theorem 4.3.1, Corollary 4.3.3, pp. 81--84, and Theorem 6.3.8(a),
  p. 131: transient symmetric finite-range scalar walks and interior
  harmonic differences. Delta_T=6(I-P_walk) fixes the transverse scalar
  normalization. These are supporting Green tools, not a vector prefix
  trace theorem or scalar Dirichlet conditions on every link component.
- Ginovyan--Sahakyan,
  [*On the trace approximations of products of Toeplitz matrices*](https://arxiv.org/pdf/1405.3568v1),
  v1, Theorem 2, printed p. 6, proof pp. 8--9: real symmetric scalar
  circle symbols in Lip(p,gamma), Lip(q,gamma), 0<gamma<=1,
  1/p+1/q<=1/2 give O(n^(-gamma+zeta)) normalized error for every
  zeta>0 for the squared two-factor product. Its Holder/Dirichlet-kernel
  proof does not cover the present multidimensional, position-dependent
  product with two long axial profiles and a triangular selector.
- Klein--Reiss--Rosenberger,
  [*Weyl asymptotics for pseudodifferential operators in a discrete setting*](https://arxiv.org/pdf/2510.11193v1),
  Hypothesis 1.1 and Theorem 3.6, pp. 3, 15--16, (3.39)--(3.50):
  the smooth elliptic symbol, essential spectral separation and compactly
  supported smooth functional-calculus hypotheses have not been verified
  for this pinned cumulative trace. Its smooth whole-lattice trace
  expansion is not a uniform small-mass estimate for this target.

The [original cubic-residual/action assessment](2026-10-12-cubic-residual-action-cubic-scale.md)
and [smooth-action audit assessment](2026-10-14-smooth-action-coefficient-critical-audit.md)
already inspected Del Debbio--Patella--Rago 1306.1173v1, section 6,
(6.1)--(6.16), pp. 13--16; Luscher--Weisz 1101.0963v2, sections
7.1--7.4, 8.2, 8.4, pp. 20--25; and Adams--Lee 0709.0781v3,
section II (7)--(15), Appendix A (A1), p. 19. Reuse their exact
comparisons: full matched Ward identities, renormalized positive-time
finiteness, and translation-invariant infrared-finite lattice integrals
do not certify this isolated bare pinned-forest coefficient's rate.
No new general framework needs reproof. The previously recorded official
Jaffe--Witten version remains the unchanged main target. No primary
source access blocker is essential to the proposed finite-matrix test.

## Search, duplicates and failures

External queries on 2026-10-20 were:

- `"prefix" "resolvent" "trace" lattice Dirichlet quantitative`
- `"smooth-action" "Yang-Mills" remainder`
- `Benzi Simoncini 1501.07376 decay bounds functions matrices banded Kronecker structure theorem`
- `"min(s,t)" "prefix" resolvent trace asymptotic`
- `"lattice" "Dirichlet" "resolvent" "trace" remainder variable coefficients`

The matrix-decay primary text was read as specified above; other search
hits were unrelated trace formulae, continuum boundary operators and
metadata, not theorem evidence. The exact local TARGET/COVERED_TARGET
search found the full-rate registration and the older coefficient audit,
but no massless second-prefix bound. This bounded search establishes no
novelty or global absence. The ready assessments supply the other
theorem-level comparisons without repeated external browsing.

L175--L179 provide the canonical ordered reduction and qualitative limit,
not duplicates to recreate. L255 is the action-Hessian branch; L248's
reverse trace and the gradient-base bounds have different orders and are
not imported as V_i estimates. Histories 207/209 confirm the original
second-prefix continuation. ATTEMPTS/038 stops isolated cubic-scale
vanishing, not a remainder about its nonzero coefficient. ATTEMPTS/030
preserves the fixed-mass-to-varying-mass failure; /045 excludes assigning
uniform smoothness to a rough projection-prefix factor. The proposed
test uses the exact finite energy square and smooth action multiplier,
not either stopped mechanism. Earlier unfinished work is preserved.

## Bounded continuation and stopping test

Essential inputs for the covered first test are L028 L156 L159 L175
L176 L177. Retain L179's coefficient as the downstream comparison.
Keep both actual probes, -6 once, both generator orders, all action/source
and normal end rows, both subtractions already accounted for in L175,
the constant axial mode and the entire heat sum. Never commute J_j,
a multiplier or a prefix through G. The signed trace is not positive;
positivity applies only to genuine covariance/energy squares.

Continue this mechanism if a full finite-mesh proof reaches the stated
N^(5/2) bound with a heat-summable polynomial mode envelope, or yields
an informative sharper partial estimate. Abandon this particular
factorization if retaining all rows and the actual order leaves only
the old mass-dependent supremum estimate or an above-threshold count;
record the precise loss rather than claiming signed growth. This test
does not require solving the independent static localization, boundary,
freezing, heat-matching or coefficient-comparison obligations.
The full N^(5/2)log(eN)^2 branch remainder and all interacting/construction
requirements remain open. Full matching and supporting Mathlib coverage
are **not checked**; unknown availability is not absence. No candidate
solution is claimed.
