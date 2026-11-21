# Actual quartic pair and two-site reference: source comparison1924

20 November 2026. Literature only. This completes nomination1923's
source review; no actual invariant, image bound, parameter solution,
new lemma or mathematical script has been calculated. The proposed
finite test below requires separate approval before execution.

## Gap, intermediate target and use

The main gap is L030-L032/C032a actual-Xi all-degree positivity;
C028b's equivalent H_d=o(d) remains unpaid. The intermediate question
is actual degree-four coefficient matching by the positive two-site
reference of C028t, after real affine centering and variance scaling.
A successful match could eliminate the cubic and quartic residuals in
this one degree. It supplies no degree-uniform full-cost estimate.

C028t certifies a nonsingular reference Jacobian at (0,1), under the
stated L917/L037 contracts. It supplies no size for an image neighborhood.
The downstream question therefore needs the actual target and a
quantitative finite-domain test, rather than another rank computation.

## Reused construction and exact input scope

Reuse source-notes1908/1920's inspected primary statements and proofs:
Gautschi, *Orthogonal Polynomials: Computation and Approximation*,
OUP2004, Section2.1.1, Theorem2.1, (2.1.1)-(2.1.3), pp52-54;
Delgado--Fernandez--Perez--Pinar, SIGMA12(2016),090,
[arXiv:1601.07194v2, Section3 pp8-10, Theorem3.1](https://arxiv.org/pdf/1601.07194v2);
and [DLMF18.2(i)/(vi)](https://dlmf.nist.gov/18.2#vi).
No new modification theorem or real-zero theorem is needed. The positive
full-theta density of L019/L021, all finite moments and two positive
unit atoms meet their construction hypotheses. Division of the measure
by3 changes no monic orthogonal polynomial. Interior-site monotonicity
is neither assumed nor revived; the source objection recorded1920 remains.

Read C028t's hypotheses, construction, centering formulas, evidence and
limitations; C028q's actual cubic convention; C028d/C028h's actual
centered coefficients; C028a's moment normalization; and L917/L037's
containment/arithmetic statements. These specify the following inputs
without assuming that the actual roots are real.

- Actual Q_4 and its coefficients are exactly C028d's formula at d=4.
  Its formal centered root power sums count complex roots algebraically,
  divided by4, and are computable by the Newton identities already used
  in C028t. C028q supplies actual variance 3S_2>0 and actual standardized
  cubic gamma_4. Define k_actual to be the fourth formal centered root
  power sum divided by4 and then by (3S_2)^2. Its explicit coefficient
  expansion and numerical enclosure remain future work.
- Actual b_j are j!*I_(2j)/((2j)!*I_0), j=0,...,4. The quartic needs
  I_8, an additional input beyond C028t's I_0,I_2,I_4,I_6. L917's
  accepted coverage through order12 includes it on the same closed
  panel0 containing lambda=0. No new quadrature is required, but the
  complete selected I_8 endpoints and audit197 provenance must be
  inspected before use. No certificate endpoints were inspected today.
- Reference coefficients use probability moments I_(2j)/I_0 with no
  factorial conversion, through order6; odd base moments are exactly0.
  Mixed moments through7 and empirical division4 remain as in C028t.
  A common vector of actual raw moments generates both target and
  reference. Replacing their intervals by midpoints would change the
  problem. Independent interval overestimation is allowed; narrowing
  by an unproved correlation is not.
- Reflection reverses g and preserves k. Both affine orientations
  must be considered when excluding matching. Reference-root reality
  follows from its positive measure; actual-root reality is not an input.

These are definitions and source applicability/index checks, not a new
actual-quartic formula, sign claim or matching theorem. The inherited
Decimal-library correctness assumption remains explicit.

## Newly inspected quantitative theorem

Siegfried M. Rump, *Verification methods: Rigorous results using
floating-point arithmetic*, Acta Numerica19(2010),287-449,
[corrected author PDF](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf),
retrieved2026-11-20: Section13, Theorems13.1/13.3, (13.1)-(13.9),
PDF pp87-89; parameter paragraph after Algorithm13.4, PDF p90.
Read the full13.3 statement/proof, including the row-wise mean-value
enclosure, Brouwer existence and the cited nonsingularity step.
For C^1 f:D->R^n, a real matrix R, 0 in an interval box X and
x0+X contained in D, its sufficient condition is

    -R*f(x0)+(I-R*J_f(x0+X))*X contained in int(X).

Here J_f is an interval hull enclosing every Jacobian on the box,
not just its value at x0. The conclusion gives a unique root and
nonsingularity; no prior exact inverse for R is required. Read also
Section5 (5.16)-(5.17), PDF p28, for interval range inclusion.
Import these known tools without a reproof. Failure of their sufficient
conditions proves no nonexistence. Lemma10.5's separate proof was not
assessed; the imported authority is the stated nonlinear theorem.

Applicability is conditional on enclosing the complete finite reference
coefficient map and its derivatives on the chosen domain, including all
Gram and variance divisions. C028t proves smoothness for the actual
positive measure at distinct real sites, but its point certificate is
not a derivative enclosure over a collar. For fixed contained moments,
the target is constant with respect to the sites. Uniform interval
evaluation retains input uncertainty; a certificate for one midpoint
target would not certify the actual target. No matching statement for
this theta family is contained in Rump's general theorem.

## Stronger-looking finite hyperbolicity coverage

M. J. Griffin, K. Ono, L. Rolen, J. Thorner, Z. Tripp and I. Wagner,
*Jensen Polynomials for the Riemann Xi-Function*,
[author accepted manuscript](https://uva.theopenscholar.com/files/ken-ono/files/jensenadvmathaccepted.pdf),
retrieved2026-11-20: (1.1)-(1.2), Theorem1.2/Corollary1.3, pp1-2;
Section5, Lemmas5.1-5.2 and proof of1.2, pp12-13, inspected.
Theorem1.2 assumes finite-height RH_m(T) and concludes hyperbolicity
for d<=floor(T)^2, n>=m; Corollary1.3 states d<=9*10^24,n>=0.
The proof uses sector approximation, differentiation and a multiplier
theorem. Its upstream multiplier theorem and zero verification were not
audited here. This is a comparison source, not a new local theorem import
or authority for an actual-root assumption in the proposed calculation.

Its hyperbolicity conclusion neither fixes the positive measure to be
theta plus two unit atoms nor controls the image of its site map. The
fixed-degree Hermite asymptotic in the same paper changes derivative
index n; the present polynomial has fixed unshifted coefficients.
Neither conclusion pays this exact inverse problem. A finite-degree
match must therefore be reported as reference-family feasibility,
without presenting quartic hyperbolicity as new RH progress.

## Bounded search and overlap/failure checks

Queries actually issued included:

- Uvarov orthogonal polynomial prescribed zeros inverse problem two mass points coefficients range
- "Uvarov" "prescribed zeros"
- "Uvarov" "inverse problem" mass points
- "Uvarov" "skewness" "kurtosis"
- "Uvarov" "coefficient" "image" orthogonal polynomials
- "orthogonal polynomials" "prescribed" "mass points" zeros coefficients
- "Uvarov" "quartic" "range"
- Krawczyk theorem interval box existence uniqueness parameters interval nonlinear equations Rump 2010 verification
- Jensen polynomial Riemann xi degree four hyperbolic explicit coefficients

No exact image/membership theorem for this full-theta, two-unit-mass,
equally weighted zero-invariant problem was inspected or found by this
bounded search. This is not a novelty or nonexistence claim. Unit-circle
inverse problems, classical-weight perturbations, multivariate linear
relations and distribution-moment fitting hits were not imported.
No essential unread source remains for the finite test specified below.

Local comparison used C028q/r/s/t, C028a/d/h definitions, and C028c's
audited specified-family retained-cost stop. Read the named grid413,
signed-Fourier435, quartic-field98 and scalar-only1919 records. They
concern an atomic Turan grid, recursive Fourier enclosure growth, a fixed
quartic-field tail mismatch, and repetition of the paid cubic scalar
certificate, respectively. None settles the changed actual image.
C028c concerns d>=5 and a different Jacobi family; it does not exclude
this fixed quartic test. The narrowly located1797 Rump assessment covers
linear solves only and explicitly leaves later sections unassessed;
it cannot substitute for today's nonlinear theorem read. No cross-notebook
result is used. Supporting Mathlib coverage was not newly investigated;
full matching image/inclusion coverage remains unchecked.

## One nominated test, no execution or derived result

Choose once the collar

    B=[-1/4,1/4] x [3/4,5/4], x0=(0,1), X=[-1/4,1/4]^2.

It has separated sites and surrounds precisely the audited point. This
choice tests whether that rank input has a quantitative use for the
actual pair in this collar; it is not claimed to be an inverse-function
neighborhood, a promising numerical fit, or a bound on all matching sites.

Use f_e(a,b)=(e*g(a,b)-gamma_4, k(a,b)-k_actual), e=+1,-1.
Nominate one fixed-box interval range/Krawczyk test for these two
orientations. For each, take R_e as the exact rational inverse of the
midpoint of a rigorously recomputed point-Jacobian box, if that midpoint
is invertible. Keep this deterministic choice; no approximate nonlinear
solver, site sweep, subdivisions, radius changes, mass changes or moment
refinement is nominated. All general-site formulas/derivatives still
need to be implemented and justified in the later research step.

The decisive inclusion threshold is the strict componentwise containment
in Rump13.3, with every actual input radius retained and every divisor
certified. A residual-component range excluding0 excludes that orientation
on B by the inclusion principle. Exclusion of both orientations is a
collar-only obstruction. One successful inclusion establishes a parameter
solution under the input contracts; the research proof must also check
the Newton/affine coefficient equivalence. If a divisor cannot be paid,
the point midpoint is singular, or neither criterion decides, report the
specific failed inequality as inconclusive and stop this test. Do not
call failure of sufficient inclusion a mathematical obstruction.

The next test can inform whether to continue quantitative work near
(0,1). Outside-collar matching, other degrees, full residual costs and
H_d=o(d) remain open in every outcome. A changed domain or solver after
failure needs a materially motivated, separately assessed target, not
an automatic radius or parameter sequence. This is ordinary finite
specialization, not a creative central mechanism. The blocker to that
nomination remains a concrete, independently justified signed full-cost
estimate uniform in degree. No new such mechanism was found here.
