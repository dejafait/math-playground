# Inverse-parameter polynomial separator — completed bounded source comparison

TARGET: Test whether L666 admits real polynomials P_n of degree at most n with P_n(0)=0, P_n(1)=1, P_n(10/11)=0, Re P_n(x/(x+i*y))>=0 for all |y|<=9/20, and exact angular preimages A_n(a)=P_n(x/a) for |a|>(n-1)/n with ||psi_n||_2<=exp(n/100)*n^C for absolute C and onset.
CHECKED: 2026-11-02
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 49 searched proper-arc polynomial positivity, stronger trigonometric positivity/moment characterizations, Blaschke-product-ratio transforms and prescribed-pole inverse norms; exact queries and inspected versus unread sources are recorded below. Scoped local searches found the nomination but no completed test of this exact polynomial-action class; no novelty claim follows.
SOURCE_EVIDENCE: Yang--Xie, arXiv:1605.02431v3 (21 July 2017), Sections 3--4, Theorems 2--3, equations (17)--(23),(39)--(50), PDF pp.6--11, including the full-rank endpoint case and duality proof. Reuse the already inspected Douglas Theorem 1, Bal--Martin--Naderi Lemmas 3.1--3.2 and scalar Fourier/Parseval reading, with the limits below.
COMPARISON: A known exact closed-arc sign certificate is available once a circle parametrization and coefficient matching are justified. Neither it nor the reused transform/range theorems constructs this prescribed polynomial, establishes membership in the full W_a action range, or pays its normalized angular inverse at rate 1/100. The specified class remains undecided.
GAP: Prove or obstruct simultaneous polynomial feasibility, exact exterior-domain action membership and the complete exp(n/100)*n^C angular cost for the saved degree/zero-constrained class; the arc substitution, all parameter coefficients, normalization and uniform onset must be justified.
REASON: Essential source comparison is sufficient for one bounded family-specific test, with no source blocker. EXPLORE approves investigation of the identified difference, not a mathematical conclusion; the changed assessment is available for separate supervisor approval before research. L674 remains separately unaudited.
LITERATURE_REASON: L674's full parameter-circle attenuation motivates a new finite-polynomial action with a prescribed zero at -R. Primary coverage of this arc-positivity and exact inverse-range ansatz was not part of the completed positive-real representation comparison.
SCOPE: Exactly TARGET with the full L666 product, normalized angular L2 pairing and the entire closed ordinate segment. One analytic polynomial-action construction and its exact paid inverse, or a class-specific obstruction, is covered; elementary rational/Fourier coefficient analysis and a justified closed-arc specialization are permitted after approval. No finite-fit replay, exponential surrogate, assumed nonzero coefficient, norm equivalence or transform identification is covered.

## Preserved nomination and hypotheses

Keep q>=1 integer, n=12q+3, x=-5/4, U=121/64 and L666's
complete W_a, including j=0 and the denominator angle 1/u. Both
angular measures and norms are normalized. The action convention is
A_n(a)=mean conjugate(psi_n(u))*W_a(u). Polynomial coefficients are
real; exact action equality is required throughout the specified
exterior parameter domain, not only at fitted ordinates. The degree
bound and zero at 10/11 are deliberately restrictive choices to test.

Reuse the Herglotz source reading and general cone comparison when
applicable. The next review should inspect the primary hypotheses for
nonnegative real parts of polynomials on the relevant proper arc and
for exact rational angular-transform membership, rather than assuming
that abstract positivity or a chosen induced norm supplies the inverse.
At nomination no named arc-polynomial theorem had been inspected for
this target; the completed comparison below now supplies that coverage.
Record any discovered exact match, stronger result or obstruction;
otherwise limit approval to the identified family-specific difference.

Essential local input is L666's rational identity and L674's qualified
parameter-circle obstruction; the latter remains separately unaudited.
Compare C645o's interior-residue correction, C645p's continued-value
cost, the finite polar repair stop, L668 and L673 without replaying
unrelated calculations. The proposed action is a continuum identity,
not the previous finite-node Fourier fit. Finite fitting, a scalar mean,
an assumed nonzero Laurent coefficient, unproved norm equivalence,
or ignoring the rest of |a|=R cannot certify the target.

The continuation test, if coverage becomes ready, is one exact polynomial
action with continuum signs and its full rate-1/100 angular cost, or a
quantified obstruction for this degree/zero-constrained class. A failure
stops only this class. Independent original-residue, H, support, Xi
realization and all-degree sign gaps remain. No polynomial feasibility,
range identity, sign theorem, cost estimate or RH candidate is asserted
in this nomination. Full matching Mathlib coverage has not been checked.

## Completed comparison — 2 November 2026, step 49

### Primary arc theorem and proof cases inspected

Zai Yang and Lihua Xie, *Frequency-Selective Vandermonde Decomposition
of Toeplitz Matrices with Applications*,
[arXiv:1605.02431v3](https://arxiv.org/pdf/1605.02431v3),
21 July 2017; [HTML version](https://arxiv.org/html/1605.02431v3).
Read Sections 3--4, Theorems 2--3 and their proofs, PDF pp.6--11.
For a closed proper circle interval I with distinct endpoints, including
wrapping intervals, their degree-one g is nonnegative on I and negative
off I. For integer N>=2, Theorem 2 characterizes interval-supported Vandermonde
decomposition by T>=0 and T_g>=0. Theorem 3 gives, for Hermitian
h(f)=sum_(|j|<=N-1) gamma_j exp(2*pi*i*j*f),

    h>=0 on I iff gamma_(-j)=tr(Theta_j Q0)+tr(Theta_gj Q1),
    |j|<=N-1, Q0>=0 (N by N), Q1>=0 ((N-1) by (N-1)).

Here Theta_j and Theta_gj are exactly equations (40)--(42), using
g from (18)--(20); coefficient orientation is not interchangeable.
The reading includes the rank-deficient case, full-rank endpoint
subtraction, the converse, and the dual-cone/closedness argument.
Nonnegative endpoint values are allowed. This is an exact sign
characterization, with no angular inverse estimate.

For applicability, a later attempt must explicitly identify a circle
coordinate for x/(x+i*y), its closed oriented arc, the real-part
trigonometric coefficients and the degree. No such specialization
or new polynomial is derived in this literature turn. Real coefficients,
P_n(0)=0, P_n(1)=1 and P_n(10/11)=0 remain additional constraints;
the cited sign characterization does not establish their joint
feasibility. A positive semidefinite fit at sampled ordinates is not
the theorem's coefficient identity.

### Reused exact-range and norm coverage

Reuse the primary reading in
`drafts/literature/2026-11-02-positive-real-angular-separator.md`:
R. G. Douglas, *On majorization, factorization, and range inclusion
of operators on Hilbert space*, Proc. AMS 17 (1966), 413--415,
[Theorem 1 and proof, pp.413--414; distinct-domain extension, p.415](https://galaxy.agh.edu.pl/~rudol/Operat/DouglasFactorizationLemma.pdf),
DOI 10.1090/S0002-9939-1966-0203464-1. It supplies exact range
inclusion/factorization and its operator-majorization cost criterion.
It does not supply that inclusion or its constant for this W_a.

The same assessment inspected J. Bal, R. T. W. Martin and F. Naderi,
*A reproducing kernel approach to Lebesgue decomposition*, Canadian
J. Math. 77 (2025), 1570--1610, DOI 10.4153/S0008414X24000488,
[Section 2.1 and Lemmas 3.1--3.2, pp.1574,1583--1584](https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/D6C85487ABC9D29C3F79208BEED1F1B9/S0008414X24000488a.pdf/reproducing_kernel_approach_to_lebesgue_decomposition.pdf).
Its Cauchy-transform isometry has its own measure, kernel and induced
range norm. No identification of that transform with W_a has been
proved. Herglotz requires open-domain positivity; it is not needed
for a sign certificate confined to a proper arc.

Reuse the scalar Fourier coverage in
`drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md`:
A. Levitt, *Analyse de Fourier et applications*,
[author PDF](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf),
retrieved 2 November 2026, Theorem 1.3/Exercise 1.2 and Theorem 1.11/
Corollary 1.12, printed pp.6,8; completeness proof p.53.
This permits standard normalized L2 coefficient/norm arguments after
the measures and interchanges are justified. It supplies no nonzero
Laurent coefficient or lower singular-value bound for this product.

L666's already imported Danchenko--Semin quadrature measures rational
angular responses with a prescribed finite pole completion. Its
quadrature identity is not an inverse-action theorem for continuum
parameter data. No further reading of that unchanged source is needed.
No general representation, quadrature or Parseval theorem should be
reproved here; only the family-specific membership and paid cost are
uncovered. A future proof must distinguish equality of complete
analytic actions from matching finitely many parameter values.

### Duplicate and failure comparison

Read L666 Section 2's full rational identity, L674's statement and
proof, C645o's residue/Gram statement and normalization, C645p's
projection and sharp continued-zero cost, L668's statement/source
scope, and L673's audited conclusion. Checked the finite-polar stop
in `ATTEMPTS/2026-11-02-positive-cone-polar-finite-screen-inconclusive.md`.
The exact local search for the polynomial nomination found no earlier
completed derivation in the selected 2 November source, attempt and
history paths. This is a duplicate check, not evidence of originality.

L674's qualified attenuation on the entire |a|=R circle is a necessary
test for any small-norm action; its disk Herglotz obstruction applies
to a stronger positivity domain. The new prescribed zero is an ansatz,
not control of the rest of that circle. C645o forbids discarding
interior angular residues. C645p stops a specific continued-value
transfer; L668 stops different prescribed spatial inverse data.
Neither is a universal obstruction to this polynomial action class.
L673's rate 1/200 positive approximants do not decide the rate 1/100
lower target. Finite polar repairs remain uncertified at the continuum
and asymptotic levels. None of these failures licenses ignoring signs,
unpaid inversion, or the original unit-residue/H/Xi gaps.

### Search record, unread leads and decision

Queries included `positive trigonometric polynomial on arc sum of
squares Dumitrescu theorem interval`, `polynomials positive real part
circular arc rational interpolation minimum norm Hardy space`,
`frequency selective Vandermonde decomposition Yang Xie 2016 positive
trigonometric polynomial arc theorem pdf`, `Blaschke product ratio
transform polynomial`, `inverse Cauchy transform polynomial norm
Hilbert space`, `prescribed poles rational inverse orthogonal Malmquist
norm`, and `polynomial positive real part arc prescribed zero`.
The initial interval-positivity search led to the inspected Yang--Xie
primary manuscript rather than reliance on a snippet or book mirror.

Dumitrescu's 2006 *Trigonometric polynomials positive on frequency
domains and applications to 2-D FIR filter design* was a lead; the
university PDF URL failed. Yang--Xie provides the needed primary
closed-arc result, so that access failure is not an essential blocker.
Their references [30] Davidson--Luo--Sturm and [31] remain unread
alternative derivations; no stronger conclusion is attributed to them.
Search leads on prescribed-pole orthogonal rational bases and inverse
eigenvalue algorithms were not theorem-inspected or used. A basis
construction or discrete approximation, without an exact identification
and uniform inverse cost, cannot settle the saved target.

Decision: EXPLORE for exactly TARGET. The strongest inspected sign
result is imported as a tool, not as a solution to the simultaneous
polynomial/range/cost problem. Standard transform results are criteria,
not a computed bound for this family. No essential unread theorem is
being assumed. This bounded search does not certify novelty or absence
of a matching theorem elsewhere. Full matching Mathlib coverage of the
target and the arc specialization remains not checked.

After separate approval, the bounded test is one exact construction
with all three polynomial constraints, closed-segment signs, full
exterior action identity and rate-1/100 cost, or an obstruction for
this specified class. Exact infeasibility or an unavoidable rate above
1/100 parks this class only. If no decisive result is obtained, preserve
the full coefficient/inverse conditions and the first unresolved case;
do not replace the target by a finite fit. No new lemma or mathematical
script was produced, and the RH argument has not changed.
