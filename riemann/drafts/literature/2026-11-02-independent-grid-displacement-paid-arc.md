# Independent perturbations of the two grids: source comparison

TARGET: Test whether L664's rate-1/16 paid-arc criterion holds uniformly after independent real displacements of every nonanchor ordinate by at most h/16, with delta=1/4 and all L649 admissibility hypotheses, original unit residues and full moments retained.
CHECKED: 2026-11-02
DECISION: EXPLORE
SEARCH_EVIDENCE: On 2026-11-02 searched perturbed trigonometric interpolation/quadrature, equal-weight perturbed trapezoidal sums, finite node-polynomial logarithmic derivatives, quantitative Mahler continuity, and Mahler measure with positive residues/moments; inspected the primary statements and proof portions below. Scoped local searches and the three relevant failure records found no prior independent-displacement resolution. No matching theorem was identified in this bounded comparison; no novelty claim follows.
SOURCE_EVIDENCE: Austin--Trefethen, SIAM J. Numer. Anal. 55(5) (2017), 2113--2122, DOI 10.1137/16M1107760, definitions (1)--(7), Theorems 1--2 pp.2115--2116, Theorem 1 proof p.2117, Section 5 outline pp.2119--2121 (https://people.maths.ox.ac.uk/trefethen/perturbed.pdf); Dimitrov--Habegger, arXiv:1909.06051v2, 24 March 2022, Section 2 norm p.9, Appendix A Lemmas A.3--A.5 pp.45--48, complete A.4/A.5 proofs (https://arxiv.org/pdf/1909.06051v2); rechecked Howell--Mathews Section 8.1 Theorems 8.1.5/8.1.7 (https://complexanalysis.org/web/sec_residue-thm.html). Reused the ready two-offset audit assessment's finite-endpoint and full-root Mahler source scope.
COMPARISON: Austin--Trefethen uses periodic interpolation and generally changes the quadrature weights; its analytic constants depend on the function. Dimitrov--Habegger requires relative coefficient control and retains dependence on the number of terms, with exponent 1/(8(k-1)). Neither imports a uniform bound for this n-dependent unit-residue finite family. The finite residue, full-root and localization inputs remain usable; the perturbed-kernel and paid comparison are unproved.
GAP: Establish a family-uniform finite-kernel/logarithmic response estimate against the exact squared-residue D, including all endpoint terms, all M moments and growing-degree constants; alternatively give an admissible countersequence controlling every allowed arc or a decisive proved perturbation cost. No calculation, robustness result or such obstruction is supplied by this review.
REASON: Essential source comparison is now adequate for one bounded mathematical attempt at the unchanged TARGET. EXPLORE permits testing the identified difference; it approves neither the criterion nor an inherited exact-grid alias identity. No essential source is blocked, and another literature turn is not the default.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED explicitly requested the missing independent-displacement comparison. The target changes the exact-grid sampling hypotheses, so the earlier L664 audit assessment alone was insufficient.
SCOPE: Exactly TARGET with n=12q+3, q>=1, h=27/(5n), delta=1/4, fixed anchor, independent real |epsilon_y|<=h/16, original unit residues, full grid, conjugated angle and all M=4q+1 moments; restrict to L649-admissible families. No symmetry, periodic extension, changed quadrature weights, general support or Xi signs are included as assumptions or conclusions.

## Exact later test

Start with L664's n=12q+3, h=27/(5n), delta=1/4 and the fixed
anchor x. For every nonanchor real ordinate y in its two signed
grids, replace y by y+epsilon_y, where epsilon_y is real and
|epsilon_y|<=h/16. The choices may be independent and n-dependent;
no conjugate-pair symmetry is assumed. Retain L649 admissibility,
all original unit residues, the conjugated denominator angle, the
complete grid and all M=4q+1 spatial moments. D remains its exact
squared-residue diagonal.

The requested conclusion is one absolute C and onset such that,
for every such family, a connected arc of normalized measure at
least n^(-2) satisfies

    log mu(I)+2 mean_(I x T) log|G| >= log D-n/16-C.

This is a robustness test for a less rigid dense-support family,
with a plausible downstream use toward arbitrary support. It is
not a general-support or Xi-sign assertion. L664's anchor approximation
cannot be assumed for the perturbed family. The proposed mechanism
to assess is the exact logarithmic derivative of the perturbed node
polynomial as a finite residue kernel, compared with the grid kernel,
while preserving all spatial roots and the angular localization cost.
No identity or estimate for that mechanism is proved in this file.

## What was compared

The main gap remains actual-Xi mixed positivity and unbounded-height
signs. This intermediate target tests robustness toward less rigid
dense support. Even a positive answer would leave arbitrary support,
Xi realization and sign transfer unresolved. A failure of the anchor
approximation would leave the paid-arc criterion undecided.

**Perturbed quadrature.** A. P. Austin and L. N. Trefethen,
*Trigonometric interpolation and quadrature in perturbed points*,
[published author PDF](https://people.maths.ox.ac.uk/trefethen/perturbed.pdf),
pp.2114--2117: the reference grid has 2N+1 periodic points with
spacing 2pi/(2N+1), each displaced by at most alpha times that spacing,
0<alpha<1/2. Quadrature integrates the degree-N interpolant;
the perturbed weights generally differ. Theorem 1 gives error
O(N^(4alpha-sigma)) for sigma>4alpha derivatives and exponential
convergence for periodic strip-analytic data. Theorem 2 bounds the
Lebesgue constant by C(N^(4alpha)-1)/(alpha(1-2alpha)), N>=2,
with the limiting logarithmic interpretation at alpha=0.
Read the projection/best-approximation reduction and analytic proof,
and Section 5's cardinal-product outline. Its full supplementary proof
was not read or imported. Our finite unit-residue sums are not that
quadrature; periodicity and uniform bounds for the changing integrand
are unestablished. Small displacement alone does not supply them.

**Logarithmic stability.** V. Dimitrov and P. Habegger,
*Galois orbits of torsion points near atoral sets*,
[arXiv:1909.06051v2](https://arxiv.org/pdf/1909.06051v2),
Lemma A.5, p.48, uses maximum coefficient norm |P|. For nonzero
P,Q in C[X_1,...,X_d], each with at most k terms, k>=2, and
rho=|P-Q|/|Q|<=1/2, it gives

    m(P)<=m(Q)+C(d,k)*rho^(1/(8(k-1))).

C(d,k) is effective. Read its complete normalization and small-value
split, including the constant-Q case, and A.4's dyadic logarithmic-tail
proof using A.3(i). This handles complex coefficients and torus zeros;
it does not assume algebraic coefficients or the main theorem's atoral
hypothesis. For this notebook, relative coefficient control and the
growing term-count dependence remain unverified. The displayed
inequality has the stated direction; a lower comparison would require
applying it in the other order with that order's hypotheses. It gives
no immediate uniform paid bound for rational angular slices.

**Finite kernels and endpoints.** Reuse
`2026-11-02-two-offset-anchor-audit.md` for Howell--Mathews,
Sections 6.2/8.1, and Brunault--Zudilin, Proposition 1.4 pp.6--7,
including boundary roots. Rechecked the primary
[residue and simple-pole statements](https://complexanalysis.org/web/sec_residue-thm.html).
They permit finitely many enclosed isolated poles with no boundary
singularities, on a positively oriented simple contour, once analyticity
elsewhere is checked. A node-polynomial logarithmic derivative is a
candidate finite residue kernel; its census, contour clearance and
uniform estimates remain later mathematical work. It must not be
identified with L664's infinite periodic alias kernel without accounting
for their difference. The reused Trefethen--Weideman Theorems 3.2,
5.1 and 10.2 comparison already distinguishes periodic, whole-line and
finite-interval hypotheses and preserves endpoint discrepancies.
No further reproof of those general results is justified.

**Search and overlap record.** Representative queries:
`Austin Trefethen trigonometric interpolation quadrature perturbed points
2017 theorem pdf`, `perturbed trapezoidal rule finite interval logarithmic
derivative node polynomial quadrature equal weights`, `Mahler measure
quantitative continuity coefficients degree polynomial perturbation roots
theorem`, `Mahler measure Holder polynomial coefficients`,
`logarithmic derivative perturbed nodes quadrature`, and `Mahler measure
positive residues moments`. Broader results were used only to locate
the primary texts above. Chern--Vaaler, *J. Reine Angew. Math.* 540
(2001), 1--47, Theorem 4 (DOI 10.1515/crll.2001.084), was an unread
lead: DOI retrieval failed; the secondary quotation is not an import.
It is not essential to the approved direct kernel test. The published
Dimitrov--Habegger MSP PDF was not readable through the tool; the
explicitly versioned primary arXiv text was accessible and inspected.

Local comparison used L649 definitions, L664's statement and exact
contour setup, L658's original-family hypotheses/localization and
L661's general envelope. The ready source assessments were reused.
The scoped records
`ATTEMPTS/2026-11-02-full-circle-root-compensation-stop.md`,
`ATTEMPTS/2026-11-02-lattice-endpoint-dominance-stop.md` and
`ATTEMPTS/2026-11-02-phase-census-absolute-contour-cost-stop.md`
stop particular averages or estimates, not this displaced family.
L664's common-delta result supplies the exact-grid baseline only.
No duplicate resolution was found in this bounded local comparison.

## Approved continuation and stopping test

One mathematical attempt at the exact TARGET is source-ready. Start
from L649, L664's audited baseline, L658 (including L657's inherited
nonzero/integrability and full-root scope), and L661's general envelope.
Compare the candidate perturbed finite kernel with its exact-grid
counterpart, paying the finite sides and all moments. This is a test
of an unproved estimate, not a request to reprove general quadrature.

The attempt must yield a uniform paid lower bound, an admissible
countersequence controlling every allowed arc, or a proved perturbation
cost that quantitatively decides this mechanism's budget. Retain the
rate n/16 and log mu(I) charge; L658 records distinct sufficient and
necessary H thresholds. Neither finite numerical evidence nor failure
at u=-1 refutes the criterion. If only that angle's estimate fails,
record a mechanism limitation and leave the all-arcs question open.
No symmetry or anchor approximation may be inherited after perturbation.
Preserve old stops and unfinished work. This review performs no new
mathematics, lemma write or mathematical-script execution.

**Mathlib.** Reuse the previously inspected univariate MahlerMeasure
coverage in the ready localized-logarithmic assessment, including
`Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`,
`Polynomial.intervalIntegrable_mahlerMeasure` and
`Polynomial.mahlerMeasure_mul`, with analytic nonzero qualifications.
Full matching coverage for perturbed kernels, the quantitative
continuity theorem and this paid criterion was not checked.

EXPLORE is source readiness for this bounded test, not a mathematical
advance or originality certification. Later work is
proof_attempt/development: difficult uniform development of the existing
finite-kernel route. Newly changed readiness remains subject to the
supervisor's separate next-turn approval; no same-turn attempt occurs.
