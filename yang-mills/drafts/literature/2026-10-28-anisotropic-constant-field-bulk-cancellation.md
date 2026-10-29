# Constant anisotropic weight — completed source comparison

TARGET: Determine whether the complete constant-field Wilson/density bulk tensor exists and vanishes for every constant 12-plaquette weight rho in [1/2,3/2] on the same transverse slice.
CHECKED: 2026-10-28
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed the bounded anisotropic Wilson/self-energy/zero-momentum searches recorded below and compared the primary action, gauge, density and cancellation statements; reused the local isotropic assessment and screened ATTEMPTS/047--050. No inspected result matches the complete frozen-weight covariance-removal tensor; no novelty conclusion follows.
SOURCE_EVIDENCE: Inspected Burgio--Feo--Peardon--Ryan hep-lat/0303005v1 II.B (5)--(6), selected III.A--C gauge/measure/ghost statements (16)--(28), III.D--F action/counterterm/BPHZ statements (31),(33)--(36) and IV.A before (37); Giordano 1506.04529v2 selected ranges in sections 2--2.2.2: (2.3),(2.6)--(2.8),(2.14)--(2.18),(2.26)--(2.31),(2.49)--(2.54) and footnote 14; reused Luescher--Weisz hep-lat/9504006v1 sections 4--7 and reopened (5.10)--(5.14),(6.24)--(7.1), including section 7(b). Local comparison read L280(1)--(7), L282(2),(6), L289 section 2 and L297(6)--(8); earlier isotropic proof/audit coverage is reused.
COMPARISON: Known cancellation covers the summed Feynman-gauge mass term in the metric-anisotropy family; the general background-field calculation also starts from metric tree weights with perturbative tuning. Neither identifies L297's covariance-removal tensor on the fixed unweighted transverse slice for an independent O(1) 12 weight. Continuum renormalizability at nonexceptional momenta is not a row-sum theorem for this object.
GAP: Establish existence and regulator independence of the exact full tensor and prove its vanishing or a rigorous nonzero component away from rho=1, retaining the transverse covariance, weighted Wilson cubic/quartic jets and unchanged full density. No gauge-equivalence or source-localization theorem is assumed.
REASON: Essential comparison is complete and no inaccessible source is needed for one direct Wilson-specific test of the unchanged target. EXPLORE approves only a future bounded attempt, subject to separate continuation approval; it proves no identity and does not certify originality. No lemmas or mathematical scripts were written.
LITERATURE_REASON: Constant anisotropic Wilson weights change the covariance and both action tensors, while leaving the slice density fixed; the required cancellation or obstruction is outside the ready isotropic assessment.
SCOPE: Prospective SU(2) infinite-lattice bulk calculation with Euclidean counting measure, raw-edge Wilson jets and the fixed transverse slice; no finite-box, source-gradient, boundary, continuum or mass conclusion is included.
COVERED_TARGET: Determine whether the complete constant-field Wilson/density bulk tensor exists and vanishes for every constant 12-plaquette weight rho in [1/2,3/2] on the same transverse slice.

## Exact proposed object and inputs

Retain L279/L280's all-link Wilson polynomials, Haar normalization
and nonlinear relative-Coulomb density convention. The proposed bulk
test weights every 12-plaquette by the same real rho in [1/2,3/2]
and every other orientation by 1, at every site. This is a frozen
constant-weight model, not a replacement for the actual separated
sources or for the finite relative cube.

For nonzero Brillouin momentum q, let C(q) be the full plaquette
incidence symbol and restrict C(q)* w_rho C(q) to ker B(q)*,
with w_rho equal to rho on orientation 12 and 1 otherwise. Let
G_rho(q) denote its inverse on this transverse subspace, extended
by zero on the gradient direction. The cubic and quartic tensors
T_rho,U_rho come from the same weighted Wilson action. D_infinity
is the unchanged full slice-density operator from L282, including
Haar and both determinant terms; no extra ghost, counterterm or
longitudinal Gaussian is silently added.

The proposed one-color constant-field tensor is the direction
row-sum matrix of

    D_infinity + E(T_rho,T_rho;G_rho,G_rho)/4
               - A(U_rho;G_rho)/4.

Contractions have exactly L297(6)--(7)'s conventions. Existence and
regulator independence of this complete row sum belong to the target,
not its assumptions. At rho=1 its value is already zero by
L282/L283/L289 and L298's audit; that special case is not new work.
Essential local inputs for a future attempt are L279 L280 L282 L283
L287 L289 L297 L298, with their upstream qualifications. No result
from another notebook is proposed.

## Why this target and what would decide it

The main gap remains the interacting continuum construction and
positive mass. L298 removes only the largest all-ground pole in
L297(24). Its remaining source/resolvent residues still have upper
bounds growing as N^(1/2) log(eN) and N^(1/4) log(eN).

A Wilson-specific cancellation for frozen local source weights is
a possible mechanism for suppressing the zero-spatial-derivative
part of the source-dependent operator. It might help improve those
residues after a separate variable-source localization argument.
That implication is not proved: source gradients, boundary layers,
resolvent mixing, high spectrum and the higher perturbative remainder
would all remain obligations. This is not the generic orbit-identity
route stopped in ATTEMPTS/049; exact Wilson locality, weighted jets,
projection and density would have to produce the cancellation.

After source approval, a bounded discriminating test would compare
the complete Fourier tensor at rho near 1, retaining every action
and density term. Its first rho derivative at 1 is a possible initial
obstruction test, not a sufficient proof for the interval. A rigorous
nonzero component would abandon the proposed vanishing mechanism;
zero only at rho=1 or in one selected diagram is insufficient.
A proved identity with controlled integrals could justify a later
source-gradient test. Divergence of an absolute bound alone would
not establish divergence of the signed tensor. No such calculation
has been performed in this audit turn.

## Completed primary comparison (step 538, 2026-10-28)

### Search, reuse and prior failures

Queries included `"anisotropic" "gluon self-energy" "cancellation"`,
`"lattice gauge" "self-energy" "zero momentum" anisotropic`,
`lattice gauge theory general anisotropy one loop renormalization
Giordano c mu nu`, `"Wilson" "plaquette weights" "one-loop"`,
`"lattice gauge" "six" "couplings" "one-loop" mass`, and
`"Wilson action" "arbitrary" "weights" "perturbation"`.
Search hits and abstracts served only to locate primary texts. The
inspected sources below support the decision; a failed query does
not establish absence from the literature.

The local screen found no duplicate beyond the already verified
rho=1 case. Reuse the finite Gaussian/Wilson conventions and the
isotropic readings in `2026-10-28-complementary-ground-compression-rate.md`;
their assumptions have not changed. ATTEMPTS/047 stops an unestimated
integration-by-parts rearrangement; /048 records an inadequate absolute
bound; /049 stops generic orbit identities alone; /050 refutes the
different bare heat-tail terminal bound. Those four files were read.
None tests the frozen, local, independently weighted Wilson tensor.
No source from a sibling notebook was used.

### Inspected anisotropic cancellation

G. Burgio, A. Feo, M. Peardon and S. M. Ryan, *Gauge Theories on a
2+2 Anisotropic Lattice*, Phys. Rev. D **67**, 114502 (2003),
[hep-lat/0303005v1, 6 March 2003](https://arxiv.org/pdf/hep-lat/0303005v1).
Inspected II.B (5)--(6), selected gauge/measure/ghost statements
in III.A--C (16)--(28), action/counterterm/BPHZ statements in
III.D--F (31),(33)--(36), and IV.A before (37): PDF pp. 6,
8--13 (printed footer numbering).
The setting is four-dimensional SU(Nc), with d coarse directions
and spacing ratio xi. The tree weights are metric anisotropies;
extra tuning enters at order g^2. The calculation keeps the Haar
vertex and both one- and two-gluon ghost vertices. It treats massive
and massless BPHZ cases separately, introducing an infrared mass in
the latter. IV.A reports exact cancellation of the summed
delta_mu_nu/a^2 and delta_mu_nu p_mu^2 terms for every d,xi,
independently of tuning, in its Feynman-gauge calculation. It is an
explicit perturbative computation, not a numbered theorem supplying
our kernel convergence. No verification of its full symbolic diagram
computation is imported here.

**Applicability:** SU(2) is included, and the source supports the
relevance of complete action-plus-measure cancellation. Its stated
weights, covariance and gauge are not the proposed ones. The opening
six-coefficient action (1) is broader than the tree weights actually
used in (5)--(6); the opening generality alone cannot import the
reported calculation for an independent finite 12-weight change.
The Haar-only reading in `2026-10-12-coordinate-haar-cubic-scale.md`
is thus extended, not repeated. No individual source diagram is
identified with either determinant term of L280 without a proof.

### General anisotropy and background-field comparison

M. Giordano, *Renormalisation of gauge theories on general anisotropic
lattices and high-energy scattering in QCD*, Phys. Rev. D **92**,
034514 (2015),
[1506.04529v2, 27 August 2015](https://arxiv.org/pdf/1506.04529v2).
Inspected selected ranges in sections 2--2.2.2, printed pp. 2--13:
(2.3),(2.6)--(2.8),(2.14)--(2.18),(2.26)--(2.31),
(2.49)--(2.54) and footnote 14. Its positive lattice spacings set
tree coefficients C_mu_nu=(lambda_mu lambda_nu)^2/product(lambda).
It parameterizes six couplings, but its one-loop expansion treats
departures from the common inverse coupling as perturbative tuning.
Its conclusion concerns the continuum background effective action,
with local curvature-square terms and finite nonlocal terms retained.
The proof uses background gauge invariance, discrete symmetries and
locality of divergences. The one-loop determinant and parity arguments
are in (2.31),(2.49)--(2.50); the Haar action first contributes at a
higher order in that background-field bookkeeping. Footnote 14
identifies a likely analytic misprint in the older 2+2 tuning formula;
that formula is not imported here.

**Applicability:** The source's complementary tree coefficients have
equal complementary products (all one in its normalization). The
proposed coefficients instead have products rho,1,1 for
(12,34),(13,24),(14,23). This elementary hypothesis comparison excludes
a direct tree-level metric specialization when rho differs from one,
even allowing a common scale. Arbitrary bare-coupling notation in
(2.5)--(2.8) is not evidence that the loop covariance was computed
for every independent O(1) coupling. This is a scope check, not a
new cancellation or obstruction for the proposed tensor. In addition,
the background field and fluctuation gauge are different objects from
L297's covariance slots; its Haar power count cannot delete our D.

M. Luescher and P. Weisz, *Background field technique and renormalization
in lattice gauge theory*, Nucl. Phys. B **452** (1995), 213--233,
[hep-lat/9504006v1, 11 April 1995](https://arxiv.org/pdf/hep-lat/9504006v1).
Reuse the full comparison in `2026-10-25-transverse-complete-coefficient-log-growth.md`.
Reopened (5.10)--(5.14), printed pp. 14--15, and
(6.24)--(7.1), pp. 18--19, including section 7(b): measure vertices are retained; BRS and
shift symmetry support background renormalizability with limits at
nonexceptional momenta. This does not identify a bare covariance-removal
coefficient with the self-energy or supply its zero-momentum row sum.
The cited earlier Reisz and diagram calculations remain
unread leads, not inputs required for this bounded direct test.

### Exact uncovered difference and permission for later work

L297(8) identifies W as the coefficient of removing a covariance
line from its scalar polynomial. It explicitly does not identify it
with a Wilsonian effective action. The sources above therefore do
not prove W_rho(0)=0 merely by absence of a gluon mass counterterm.
The necessary matching, zero-momentum integrability and regulator
passage cannot be hidden in the words gauge invariance. The local
slice density remains L282(6), with its Haar term, diagonal projection
term and product-of-gauge-kernels term, all independent of rho.

EXPLORE authorizes one later bounded proof test of the exact TARGET,
not a reproof of either source's cancellation. A useful first test is
the complete rho response near one, formed from all weighted Wilson
vertices and the derivative of the actual transverse covariance,
while retaining the full density. Establish the relevant convergence
before treating a formal integral as a row sum. A rigorously nonzero
complete component refutes interval-wide vanishing and stops this
mechanism. A vanishing first derivative is only a preliminary check;
without a justified full identity it does not complete the TARGET or
justify a variable-source estimate. A proof of the interval identity
with controlled limits would justify a separately assessed localization
step. Numerical agreement or a single cancelled diagram is insufficient.

The changed ready assessment receives separate continuation approval
before research is invoked. No new identity, derivative estimate,
lemma or mathematical script was produced in this literature turn.
Full matching Mathlib coverage is **not checked**; none is asserted.
The direct calculation is justified only for this exact coefficient
and changed hypotheses, not as an originality claim. The continuum,
boundary-transfer and higher-remainder gaps remain unchanged.
