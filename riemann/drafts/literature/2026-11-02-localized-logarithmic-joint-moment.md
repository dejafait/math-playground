# Localized logarithmic mean of the joint spatial moment polynomial

TARGET: Test whether, uniformly in L649's integer-mass family, some angular arc I with mu(I)>=n^(-2) obeys log mu(I)+2 mean_(I x T) log|G_n|>=log D_single,n-n/16-C for absolute C and onset, where G_n(u,zeta)=sum_(k<M)c_k(u)zeta^k.
CHECKED: 2026-11-02
DECISION: EXPLORE
SEARCH_EVIDENCE: On 2026-11-02 searched Mahler/Lp norm comparisons, rational Jensen zero/pole formulas, arc Remez/logarithmic estimates, and Mahler measure with positive residues or moment power sums. Read the primary sources specified below and the full C645p/C645x proofs plus relevant local failure records. No matching uniform integer-family arc theorem was identified; this bounded search does not establish novelty.
SOURCE_EVIDENCE: Inspected Defant--Mastylo arXiv:1508.05556v1 (2015-08-23), (1)--(5), Theorem 3.1 and proof pp.7--8, and Theorem 4.2 p.11; Issa--Lalin arXiv:1203.5379v1 (2012-03-24), Remark 3.8 and Theorem 4.1/proof p.7; Tao 246B Notes 1 (2020-12-23), Theorem 2 and proof; Brunault--Zudilin ISBN 9781108794459 excerpt, Proposition 1.4 pp.6--7 including boundary roots; Tikhonov--Yuditskii arXiv:1809.09726v2 (2018-10-20), Theorems 1.1--1.2 pp.2--3 and concluding proof pp.10--11. Mathlib's univariate MahlerMeasure documentation was inspected. Printed page numbers throughout.
COMPARISON: Sources provide integrability for nonzero complex polynomials, exact full-circle zero/pole accounting, sharp degree-dependent norm comparisons and a sharp measurable-set Remez bound. They do not compare this correlated rational moment polynomial with D_single,n or guarantee a connected arc of the required size at squared loss n/16. Generic norm losses and arithmetic coefficient hypotheses cannot be silently removed. No source or local obstruction inspected settles the criterion.
GAP: After explicit denominator clearing and nonzero-polynomial verification, control the complete spatial root contribution and angular zero/pole cost on one connected arc with mu(I)>=n^(-2), relative to the exact squared-residue diagonal, uniformly over n-dependent integer families. Fixed-polynomial integrability and a point estimate do not give that uniform bound.
REASON: Essential source comparison is now sufficient for one bounded creative attempt using the stated rational/polynomial formulas; it neither proves the target nor rules it out. The remaining task is family-specific zero/pole accounting and localization, not a reproof of Jensen, polynomial integrability or Remez. This changed assessment requires separate approval before research.
LITERATURE_REASON: At invocation, essential rational Jensen/logarithmic-mean source coverage was missing for this stronger sufficient criterion; this turn supplies that comparison. Repeated spatial Taylor or extra-cloud constant tuning would not address arbitrary dense spread support.
SCOPE: Exactly TARGET, including all original integer masses, full grid, conjugated angle, normalized means and connected arcs. A later attempt may specialize the cited identities, verify rational numerator nonvanishing and integrability, and bound all root/pole/localization costs, or exhibit an admissible asymptotic obstruction. No fractional relaxation, coefficient-integrality, separation, grid prefix or point-value substitute is covered.

## Exact proposed criterion, not a derived result

Keep n>=5, x=-5/4, R=11/8, eta=1/100, t_j=j/n, the common distinct
pole set Z on Re(a)=x with |a|<=R-eta and x in Z, and original
positive integer residues r_a of mass M<=n/3. Keep every rotated
grid factor, its conjugated denominator angle, and normalized spatial
and angular means. There is no separation, symmetry or integrality of
polynomial coefficients. Use L649's c_k(u) and exact D_single,n.

G_n is the finite polynomial in the TARGET field. The proposed test
allows a family-dependent connected angular arc I; mu(I) is its
normalized circle length, and mean_(I x T) is normalized on that
product. The full circle is permitted. A single constant C and one
onset must work for all families. The logarithmic integral's existence
and treatment of zeros must be justified; do not assume a nonvanishing
polynomial on the torus. No conclusion about that integral or the
criterion is established in the completed L656 turn.

The rationale is to seek a sufficient bound for L651's S_n through
logarithmic averaging after angular localization, paying log mu(I)
explicitly. Global averaging can lose angular concentration; point
evaluation alone does not pay the angular measure. The proposed
criterion must be assessed against both problems. Do not infer
arithmetic Mahler bounds from r_a being integers: the pole polynomial
and G_n generally have complex, nonintegral coefficients.

## Required comparison and bounded follow-up

Reuse the existing primary Fourier/projection assessment and exact
normalizations. Inspect primary Jensen/argument-principle hypotheses
and the essential zero/pole cases, and search stronger known rational
or polynomial norm comparisons. The necessary comparison must be
uniform in degree and this family, not a fixed-function nonvanishing
statement. Any needed denominator clearing must count all introduced
zeros and poles and its full angular logarithmic cost.

Contrast the local C645p angular evaluation and C645x universal
fractional-mixture stops before claiming a new mechanism; their full
proofs were read in the source review below. Preserve L647's
constant grouping stop, L649's exact-recovery stop, L650's separate
columns and C645y's grid prefix stop. The previous centered/shifted
Chebyshev screen and pole-location descent were inconclusive finite
tests of S_n, not tests or proofs of this logarithmic criterion.

If the source comparison makes the criterion ready, the proposed
later route is proof_attempt/creative at deep_research/max. The precise
obstruction is cancellation of the first-M spatial moment vector on
dense spread support while its diagonal concentrates in angle. A
logarithmic bound could preserve the complete polynomial's zero/pole
information instead of paying a global interpolation norm.

The bounded test would compute or bound all zero/pole contributions
to this localized mean and compare the full paid quantity with
log D_single,n-n/16. A uniform constant/onset, an admissible sequence
whose paid quantity fails for every allowed arc, or a quantitatively
isolated remaining term is decisive. A nonzero resultant, a finite
screen, an unevaluated supremum or a one-angle estimate is insufficient.
Failure would stop this sufficient criterion, not the joint target
or RH. This is a proposal for later work, not a second mathematical
attempt in the current turn.

Xi realization, matching upper bounds, all-degree signs, and audits of
L651/L654--L656 remain independent. The completed comparison below
changes source readiness only; separate approval precedes research.

## Completed source comparison — 2 November 2026

### Search and overlap

Representative queries were `Mahler measure polynomial Lp norm inequality
coefficient binomial Mignotte`, `rational function logarithmic integral
Jensen formula poles unit circle`, `polynomial Mahler measure arc Remez
inequality logarithmic integral`, `Mahler measure positive residues
rational polynomial`, and `Mahler measure polynomial moments power sums
positive weights complex`. General summaries and search snippets were
discovery aids only. No exact match emerged from these bounded searches.

Read L649's definitions, hypotheses and convergence argument and L651
through its complete joint-response reduction; reused the ready
`2026-11-02-joint-full-grid-polynomial-dual.md` source comparison. Read
all of C645p and C645x, including their qualifications and C645x's audit.
C645p's ambient continuation extremizer is not an admissible family.
C645x's auxiliary fractional lattice has too many distinct poles and
noninteger masses; its obstruction concerns one universal linear dual.
Neither establishes a counterexample to this family-dependent nonlinear
criterion. Their proofs supply reasons to keep every pole cost and the
integer census, rather than reasons to declare the proposal impossible.

Read the zero-evaluation, joint-angular-moment and full-angular-Chebyshev
ATTEMPTS records dated 2 November. The latter two are inconclusive finite
screens, not asymptotic countersequences; they do not test this logarithmic
criterion. No new screen or mathematical derivation was performed here.

### Primary inputs and exact qualifications

**Rational Jensen.** T. Tao, *246B, Notes 1: Zeroes, poles, and
factorisation of meromorphic functions*, 23 December 2020,
[Theorem 2, (1), (3)--(5) and proof](https://terrytao.wordpress.com/2020/12/23/246b-notes-1-zeroes-poles-and-factorisation-of-meromorphic-functions/).
For a meromorphic function on a neighborhood of the closed radius-r disk,
with removable singularities removed and center neither zero nor pole,
its center logarithm equals the boundary mean plus the sum of
log(distance/r) over zeros, minus that sum over poles, with multiplicity.
Boundary terms have zero weight. The proof removes interior divisors by
Blaschke factors and then uses a holomorphic logarithm. This is a
full-circle identity, not an unweighted-arc mean theorem. Center zeros
or poles must first be factored out; their values cannot be inserted as
finite logarithms. Formula (1) gives the finite rational divisor identity.
All cancellations must be resolved or counted with both signs.

**Boundary roots.** F. Brunault and W. Zudilin, *Many Variations of Mahler
Measures*, ISBN 9781108794459,
[publisher excerpt, Proposition 1.4, pp.6--7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf),
retrieved 2 November 2026. For every complex alpha, the normalized
circle integral of log|e^(2pi it)-alpha| is log max(1,|alpha|).
Read all three modulus cases: the unit-modulus case uses an indented
contour with error tending to zero, not continuity of a bounded
integrand. Thus torus zeros are not excluded by the cited one-variable
identity. Use this result by citation; no general Jensen reproof is
needed. An arc contribution remains an arc integral, not log-plus of
the modulus. The excerpt's alternative Riemann-sum proof is not used
at boundary roots.

**Logarithmic integrability.** Z. Issa and M. Lalin, *A generalization of a
theorem of Boyd and Lawton*,
[arXiv:1203.5379v1, Remark 3.8 and Theorem 4.1/proof, p.7](https://arxiv.org/pdf/1203.5379v1).
The theorem concerns nonzero polynomials over C in any finite number
of variables; generalized and multiple logarithmic Mahler integrals
converge. Its s=1 case supplies ordinary logarithmic integrability,
including zeros on the torus. Read the proof's small-value/complement
split and its fixed-multivariate-polynomial qualification. It supplies
no constants uniform in growing degree or this changing family.
Applicability still requires constructing the actual polynomial after
clearing angular denominators, verifying it is nonzero, and accounting
for the denominator logarithm. Rationality alone is not that verification.
No Boyd--Lawton limit or uniform small-value theorem is invoked here.

**Sharp norm and subset comparisons.** A. Defant and M. Mastylo,
*Lp-norms and Mahler's measure of polynomials on the n-dimensional
torus*,
[arXiv:1508.05556v1, (4)--(5), Theorem 3.1/proof pp.7--8; Theorem 4.2 p.11](https://arxiv.org/pdf/1508.05556v1).
For a complex polynomial H, normalized torus measure and p>0,
||H||_p <= product_j Lambda(p,d_j) M(H), where d_j are the separate
variable degrees and Lambda(p,d)=||(1+z)^d||_p. The constant is sharp,
with product extremizers. In particular Lambda(2,d)=sqrt(binomial(2d,d)),
as stated on p.11. Read the induction using Fubini, Fatou and Minkowski
and its sharpness case. The spatial degree alone may grow nearly as
n/3; its generic squared-norm loss is therefore not the desired n/16
loss. This comparison also begins with a norm of the whole polynomial,
not D_single,n. Theorem 4.2 controls norms using a measurable subset,
degree factors and the global L1 norm; it does not select a connected
arc. These are tools to cite, not a matching solution or an admissible
counterexample: the sharp product extremizer has not been realized here.

**Sharp arc-related Remez bound.** S. Tikhonov and P. Yuditskii,
*Sharp Remez inequality*,
[arXiv:1809.09726v2, Theorem 1.2 p.3; concluding proof pp.10--11](https://arxiv.org/pdf/1809.09726v2).
For a complex polynomial of degree d bounded by one on E in the unit
circle, with angular length |E|>=2pi-s and 0<s<2pi, the full-circle
supremum is at most T_d(sec(s/4)). Here T_d is the Chebyshev polynomial;
angular length is not normalized probability. Theorem 1.1 gives the
trigonometric version with degree 2d in the constant. Read the general
complex-polynomial statement, equality form and proof's single-gap
extremal reduction. This is a sup comparison for a supplied measurable
set, not a logarithmic lower mean on a selected arc. It contains no
pole correction and no reference to our diagonal. A sharp extremal
configuration for that theorem is not an admissible obstruction here.
Applying it after denominator clearing requires keeping the denominator
and actual degree; no favorable n/16 rate follows from its statement.

### Mathematical difference left for a later attempt

The source gap is sufficiently covered to test the mechanism, but the
mathematical gap is unchanged. The attempt must verify the actual
nonzero numerator (including exceptional identically-zero slices),
clear the angular rational denominators with all cancellations, and
justify product/arc integrability using the cited polynomial theorem.
It must keep all spatial roots, degree drops, leading factors and
angular poles when evaluating any Jensen expression. C645p identifies
interior angular poles p_j=t_j*x/U and possible exterior poles a/t_j;
none may be discarded merely because W_x=1 or an individual factor
cancels. Original positive integer r_a do not make the numerator's
complex coefficients integral, and a squared-residue diagonal is not
the Mahler measure of the sum.

The bounded test is the original TARGET: produce a uniform absolute
constant/onset, an admissible n-dependent sequence failing for every
allowed connected arc, or an explicitly quantitatively bounded remaining
term in the fully accounted logarithmic expression. Merely defining
the supremum over arcs, establishing integrability, bounding one value,
or giving a generic degree-loss inequality does not pass. If the
criterion fails, park this sufficient logarithmic route while preserving
the joint-projection target. Independent Xi and sign gaps stay open.

### Mathlib and review status

Inspected the official
[Mathlib.Analysis.Polynomial.MahlerMeasure documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html).
Supporting univariate results include
`Polynomial.intervalIntegrable_mahlerMeasure`,
`Polynomial.mahlerMeasure_mul`,
`Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`,
`Polynomial.mahlerMeasure_le_sqrt_sum_sq_norm_coeff`, and
`Polynomial.norm_coeff_le_choose_mul_mahlerMeasure`.
The first uses Lean's totalized real logarithm, so its zero-polynomial
instance does not prove finite analytic log|0| integrability. Nonzero
hypotheses and almost-everywhere interpretation remain essential.
No matching theorem for this rational two-variable localized criterion
was found in this module; wider multivariate coverage was not checked.

This is LITERATURE/EXPLORATION, NOVELTY_UNCHECKED, not a new lemma or a
mathematical proof of applicability. EXPLORE records a bounded comparison
with no adequate match, not originality. A newly ready continuation
requires separate approval next turn. The appropriate later task is
proof_attempt/creative: the discriminating test is family-specific
divisor/localization accounting against the squared rate 1/16, without
repeating point continuation or a universal fractional-mass dual.

