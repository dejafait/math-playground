# Coverage: all fixed log-2 cubic harmonics

TARGET: Test whether the normalized actual coefficients of all fixed log-2 cubic harmonics admit a positive circle measure, using a finite Toeplitz minor as the obstruction test.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 221 searched notebook-local trigonometric-moment/Toeplitz references and the exact weighted-cubic scope, reused steps 213/215/217 and audited L409/L430/L431, and inspected the primary moment statements below. No inspected source decides this arithmetic sequence; no novelty inference follows.
SOURCE_EVIDENCE: Helton--Putinar, Positive Polynomials in Scalar and Matrix Variables, the Spectral Theorem, and Optimization (2007), section 3.1, Theorem 3.3 and proof, pp. 245--246; Yang--Xie 1605.02431v3 (21 July 2017), section 1.2 and section 2, Theorem 1 and both rank cases (5)--(15); reused Milinovich--Ng Lemma 6.1 p. 9, Gonek section 3 Lemma 2 p. 130, Fazzari 2306.15553v1 (3.5), and DLMF 25.11(i)/25.11.5 through the inspected step-213 comparison and L408--L430 interfaces. Details and direct links below.
COMPARISON: Herglotz covers all finite Toeplitz sections of a conjugate-symmetric sequence; finite Vandermonde decomposition covers a single PSD prefix. Neither theorem supplies the actual higher-harmonic cubic coefficients or signs their minors. The fixed-rational-character sources cover the required fixed powers, with coefficient identification, denominator-grid bookkeeping and complete-tail transfer left to research.
GAP: Establish the actual coefficients needed through harmonic 4, with the full physical/response errors controlled, and test every principal minor of the 5-by-5 normalized Toeplitz section exactly. No higher coefficient, minor, positive measure or redesigned law is established here.
REASON: Essential source coverage is ready for one bounded SPECIALIZE mathematical attempt after separate supervisor approval; import the moment theorems and derive only the stated arithmetic specialization. This literature-only review performs no coefficient evaluation, minor test or new lemma proof.
LITERATURE_REASON: Changed scope from one cosine coefficient to simultaneous fixed-power harmonics; essential positive-measure moment coverage and the exact higher-harmonic actual coefficient interface are not yet assessed.
SCOPE: Only the intermediate nonnegative-mass mechanism with L431's high component and O(ell) signed bulk contribution; fixed harmonics before the height limit. No growing-frequency theorem, actual conditional law or RH consequence.

The main gap is global mixed positivity. This intermediate target asks
whether the same mechanism can survive an entire arithmetic family of
constraints, rather than adding one more calibrated frequency. A strict
negative finite Toeplitz minor would rule out even a positive measure
with those moments. Nonnegative minors in a bounded test would not prove
positivity of the infinite sequence, a bounded density, preservation of
the full law, or any actual clipping assertion.

The step-220 proposal required a literature-only review. Step 221 completes
that review below. A later mathematical invocation, after its separate
approval, may perform only the bounded test specified here.

Essential inputs: L409, L430 and audited L431, with L421/L429 for the
unchanged high contribution and complete signed bulk bound. The zeroth
coefficient must be the actual beta and the first must agree with L431's
verified ratio. No higher coefficient, minor or positivity result is
derived here. Full matching Mathlib coverage is unchecked.

Continue to one bounded mathematical test only after essential coverage
is ready and the exact sequence and finite test are specified. A strict
negative minor is informative for this mechanism; finite nonnegative
minors are inconclusive and do not justify unbounded searching. Import
any known result deciding the sequence rather than reproducing it.
Finite Fourier support of L431's particular polynomial is not the sought
obstruction: the proposed class includes all finite positive circle
measures. No new law implementation is part of this target.

Actual/global realization, actual clipping, capped nondegeneracy, L413's
full-error margin and global mixed positivity remain unresolved. Preserve
L427/L428/L430's narrower stops, L431's one-harmonic construction and
the parked core/tail route. No cross-notebook input is proposed.

## Completed source comparison — 2026-10-18, step 221

This LITERATURE / NOVELTY_UNCHECKED review is EXPLORATION: it adds
essential source-scope coverage and a bounded test, without establishing
a mathematical input or an obstruction. No lemma or mathematical script
is written. PROOF.md and DAG.md are unchanged. Mathematical exploration
usage remains 0 of 3.

### Discovery, reuse and recorded failures

Local searches used `Herglotz`, `Toeplitz`, `positive circle measure`,
`trigonometric moment`, `prime.power` and `harmonic` in the active
notebook's literature/failure paths and relevant October-18 histories.
The one-harmonic Fejer assessment contains factorization and polynomial
coefficient tools, not an assessment deciding the infinite arithmetic
moment sequence. Read L430's character, arbitrary-rational pole,
complete-tail, zero-carrier and complete-law sections; L408's rational
interface; L409's coefficient/quantifiers; and L431's prime-2 reduction.
Reuse the completed step-213 source comparison and step-215 approval
for the analytic tools rather than reopening that discovery search.

External locator queries included `Herglotz theorem trigonometric moment
positive semidefinite Toeplitz Simon OPUC theorem 1.3.1`, `"zeta"
"signed cubic" "prime" "harmonics"`, `"zeta" "twisted" "cubic"
"trigonometric moment"`, and `"twisted third moment" "zeta" rational
Hardy`. The inspected matches below cover the general moment problem;
no inspected theorem supplies or decides this complete physical cubic
sequence. Search snippets and unrelated logarithmic-zeta moments are
not imported. The previously recorded unproved Bui theorem remains
excluded. No novelty or exhaustive-absence claim is made.

Read the canonical L427 failure record and step-205 L428 decision, and
reuse L430/L431's audited qualifications. A fixed mixture's mismatch,
a uniformly bounded bulk obstruction and the unchanged law's first
cubic mismatch do not prohibit a different positive measure. L431
already defeats the first-harmonic obstruction. Its polynomial's finite
Fourier support is not evidence against the unrestricted measure class.
C426c/core-tail stays parked. There is no cross-notebook input.

### Inspected moment theorems; import, do not reprove

J. William Helton and Mihai Putinar, *Positive Polynomials in Scalar and
Matrix Variables, the Spectral Theorem, and Optimization*, in *Operator
Theory, Structured Matrices, and Dilations* (2007), pp. 229--306,
[section 3.1, Theorem 3.3 and proof, pp. 245--246](https://mathweb.ucsd.edu/~toal/READ07/hpSurvey07.pdf#page=17).
For c_0>0 and c_(-n)=conjugate(c_n), existence of a unique positive
circle measure with moments c_n is equivalent to positive
semidefiniteness of the infinite Toeplitz matrix. This means every finite
section, not one determinant. The proof uses Fejer--Riesz and positive
functional representation; compactness and Stone--Weierstrass give
uniqueness. The measure's mass is c_0. No density, boundedness or finite
support is required. The complete theorem and relevant proof were read
in the author-hosted 78-page publication. Import this classical
Herglotz/trigonometric moment theorem; no general reproof is needed.

The web PDF text was accessible. The screenshot/local-download attempts
did not provide usable evidence (one screenshot timeout; local DNS
failure); they are not treated as verification. The finite theorem and
proof below were accessible in full HTML, so no essential source is
parked as inaccessible.

Zai Yang and Lihua Xie, *Frequency-Selective Vandermonde Decomposition
of Toeplitz Matrices with Applications*,
[arXiv:1605.02431v3, 21 July 2017, section 2, Theorem 1](https://arxiv.org/html/1605.02431v3#S2).
A finite Hermitian Toeplitz matrix is PSD exactly when it has a positive
atomic Vandermonde representation; the number of atoms is its rank.
Read section 1.2's sign conventions, (5)--(15), including the
rank-deficient unitary-shift proof and full-rank rank-one subtraction.
Uniqueness is asserted in the rank-deficient case, not in full rank.
The convention uses exp(-2pi i j f), with theta=2pi f; conjugation
changes the Fourier sign. This supplies finite-prefix compatibility,
not compatibility with unspecified higher moments. Restricted-support
Theorem 2 is unnecessary. No general factorization is to be reproved.

For the proposed application use mass one, real c_j and c_(-j)=c_j.
The research argument must explicitly justify the cosine-to-symmetric-
measure specialization by reflection/symmetrization. Do not assume that
the actual sine-weighted coefficients vanish, or that a hypothetical
measure must initially be even. PSD is the required condition;
strictly positive determinants are not necessary, and testing only
leading determinants is inadequate in the semidefinite case.

### Fixed-character source applicability, with unproved obligations

The primary analytic hypotheses/proof cases already inspected in the
[step-213 comparison](2026-10-18-prime-twisted-cubic-counterlaw-comparison.md)
are reused. Milinovich--Ng,
[Lemma 6.1, p. 9](https://home.olemiss.edu/~mbmilino/Lower_Bounds.pdf#page=9),
was also reinspected this turn: its chi kernel permits every positive
argument and fixed abscissa in [kappa_0,2], with the endpoint-transition
denominator retained. Its later GRH application is not used. Gonek,
[section 3, Lemma 2, p. 130](https://www.sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf#page=8),
supplies the already inspected saddle, endpoint and exterior cases.
Fazzari [2306.15553v1, (3.5)](https://arxiv.org/html/2306.15553v1#S3)
allows reduced rational additive phases and complete residue classes;
[DLMF 25.11(i)](https://dlmf.nist.gov/25.11#i) and
[25.11.5](https://dlmf.nist.gov/25.11.E5) supply the pole/continuation
under the previously recorded positive-parameter hypotheses. Use L408's
smooth-first sharp transfer, not a sharp indicator in the Schwartz
theorem or the previously excluded expanded polar display.

The relevant source parameters for harmonic j are the two fixed
single-carrier twists 2^j mn/k and 2^(-j) mn/k and zero-carrier twists
2^j mnk and 2^(-j) mnk. Each j is fixed before H tends to infinity.
These lie within the positive-rational source domain. L408's (12),
recalled in L430 (6), is the ready arbitrary-rational coefficient
interface, not just an integer-twist formula. Constants may depend on
j. No theorem uniform for j growing with H is imported or needed.

In the research turn verify, rather than assume, the full response
passage with L430's frequency majorants for these fixed scalings.
Retain every connector, both sharp endpoints, both real characters and
the H-first/head-second order. On the zero carrier, explicitly replace
the half-integer analysis by the fixed denominator-2^j grid, keeping
all integer resonances and all nonresonant near terms. L406's absolute
physical transfer can be multiplied by bounded cosine; an already
integrated signed tail cannot. The sources cover these fixed
parameters, but do not prove this changed application for us.

### Exact proposed sequence and one bounded test

Here are quantities to establish in research, not new asserted limits.
For j>=0 let g_j denote the prospective leading coefficient of

    E_H[Delta Bcal cos(j t log 2)]/(log H)^2.

The explicit candidate to verify from the cited rational interface is

    ghat_j=(kappa/2) sum_(m,n,k>=1) (mn)^(-2) k^(-3)
       [2^(j/2) A_num(2^j mn/k)
                  +2^(-j/2) A_num(mn/(2^j k))],
    kappa=17c^3/20160, c=1/(4pi),
    A_u=u^(-2) sum_(a=1)^u gcd(a,u).

This is a specified candidate coefficient formula for the test, not a
proved higher-harmonic theorem. The research proof must establish
g_j=ghat_j for every coefficient used. Its normalization must reproduce
g_0=beta from L409 and g_1=gamma_2 from L430, and hence the audited
L431 value c_1=g_1/beta=1161 sqrt(2)/1786. Define c_0=1 and
c_j=g_j/beta only after that identification; use c_(-j)=c_j for the
cosine moment problem. L431's existing prime-2 factorization and exact
A_(2^d) formula are available inputs, not a need to recompute odd
Euler factors numerically.

The bounded attempt is j=0,1,2,3,4 only. Establish those fixed
coefficients, form T_4=(c_(a-b))_(0<=a,b<=4), and inspect all its
nonempty principal minors, stopping at the first strictly negative
one. Use exact arithmetic in Q(sqrt(2)), or rigorous enclosures with
complete convergent tails. If a certificate script is useful in that
later research turn, save its full values, index sets and sign margins
under scripts/discriminant/; a decimal eigenvalue is only a locator.
No coefficients or minors have been calculated in this review.

A strict negative minor would obstruct every positive circle measure
with these cosine moments and therefore the intermediate positive-mass
mechanism, while its unchanged high and complete signed bulk remain
lower order. The application must cite L421's high absolute-cubic bound
and L430's full translated conditional-bulk bound; do not replace the
latter by an unproved bound on the expectation of the absolute cubic.
This excludes only the stated mechanism, not all counterlaws or RH.

If all principal minors through T_4 are nonnegative, report only
finite-prefix compatibility/inconclusiveness and stop this bounded
search. Do not increase the harmonic cutoff automatically, infer an
infinite positive sequence, bounded density, or implement a new law.
An unresolved zero sign or uncontrolled coefficient error is also an
honest incomplete test. Changed mechanisms need separate coverage.

Actual/global realization, actual clipping, capped nondegeneracy,
L413's full-error margin and global mixed positivity remain independent
gaps. Full matching Mathlib coverage is unchecked, not known absent.
Essential local inputs remain L409/L430/L431 and L421/L429, with
L406--L408 supplying the cited analytic interfaces. The later canonical
result must carry the imported theorem citations and its complete
specialization; this assessment is source coverage, not a new lemma.
