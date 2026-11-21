# Interior-zero compression of the actual Fredholm correction — source comparison

TARGET: Review whether separating G's r-1 enclosed zeros yields an exact finite-dimensional singular-value certificate for L776's ||A_(r,R)||<1, including repeated zeros and a certified bound for the remaining zero-free factor, without assuming real zeros or minor signs.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step426 searched rational finite-rank Hankel, multiple-pole/confluent, finite singular-value and Gram-metric terms; inspected Peller Section4, Perfekt–Pushnitski Section6.2, Yafaev Section5.1 and Gragg–Reichel Section1/Remark1.1. Reused step423's exact Toeplitz/minor comparison and the local Fredholm failure records; exact queries and read limits below.
SOURCE_EVIDENCE: Peller MSRI33 (1998) Theorem4.1/Corollaries4.2–4.3 pp.76–77; Perfekt–Pushnitski 1611.03772v2 Theorem6.1 PDF pp.18–19; Yafaev 1304.2677v1 (5.2),(5.6)–(5.7) PDF pp.22–23; Gragg–Reichel NPS-53-89-003 Section1 Proposition1.1,(1.11)–(1.17),Remark1.1 printed pp.1–5; Shapiro MAT520 (2024) Theorem9.25/proof pp.90–91. Direct primary URLs and qualifications below; reuse L776's Böttcher–Widom/Bornemann coverage.
COMPARISON: Known rational-Hankel theory covers repeated complex poles and a finite metric-correct singular-value reduction; it does not directly cover L776's generally nonselfadjoint compressed product or bound its norm. Conditional specialization must identify the correct one-sided rational factor, retain both Gram metrics and bound analytic-factor approximation in the original l2 norm. Existence of optimal rational approximation or fixed-symbol asymptotics supplies no effective actual-G budget.
GAP: Actual-G factor identification, multiplicity/normalization checks, full-product finite matrix and explicit conditional error certificate remain unwritten application work. No actual norm<1, certified zero data, universal radius or growing-r estimate is established. The narrow specialization below is covered; an unconditional bound is outside scope.
REASON: New primary coverage removes the repeated-pole and metric-reduction source gaps and makes one conditional known-theorem specialization independently testable. Continue to mathematics on this unchanged target; do not infer smallness from finite rank.
LITERATURE_REASON: The target changes from sign sufficiency to an explicit finite-dimensional actual norm certificate; rational-Hankel, repeated-zero and enclosure-error inputs were outside the approved specialization scope.
SCOPE: L018/L021/L776; r>=2, R>0, contour nonvanishing and exactly r-1 interior zeros with multiplicity. Permit arbitrary complex zeros and repeated zeros; explicit circle suprema, reciprocal-factor lower bounds and approximation enclosures are conditional inputs, never free constants or signs. Approve only a conditional representation/error theorem, not an actual numerical test, uniform norm bound or creative estimate. The pending nomination below is preserved as history; the completed comparison supersedes its unread-source statements.

## Proposed comparison and bounded decision

Main gap: actual-Xi all-degree mixed positivity. The intermediate question
is whether the specific A_(r,R) of L776 can be represented and bounded by
a finite singular-value problem using the enclosed zeros and the remaining
analytic factor. A later successful bound below 1 would pay the norm
hypothesis for an admissible pair, while other r, available radii, other
minor indices and the all-degree assembly remain independent gaps.

Essential local inputs are L018/L021 and the newly written, independently
unaudited L776. Keep R>0, contour nonvanishing and exactly r-1 enclosed
zeros counted with multiplicity. Certified complex zero enclosures may
be permitted; neither reality nor simplicity of those zeros is assumed.
Do not infer these enclosures from coefficient-minor signs. The source
review must distinguish an operator-norm certificate from a finite
determinant with an unpaid sign or an ill-conditioned change of basis.

Inspect primary finite-rank Hankel/rational-symbol results, then only the
essential repeated-pole and compression cases. Kronecker's finite-rank
Hankel theorem is an unread search lead here, not an imported theorem or
a sufficient quantitative certificate. Compare the source hypotheses
with L776's precise one-sided Fourier factors, projections and l2 norm.
Keep scalar normalization and the full remainder/error contribution.
No factorization, rank assertion or numerical experiment is derived in
this nomination.

Continue only if the source comparison identifies an exact operator
representation with a checkable bound of the form U+error<1, where all
inputs can in principle be certified from G and zero enclosures without
RH or desired minor signs. State the precise matrix, norm equivalence,
error quantities and applicability before approving a mathematical test.
If only an unpaid boundary sign or an unbounded inverse remains, record
that defect and park this compression proposal. A generic finite-rank
identity alone is not evidence that the actual norm is small.

The shifted-minor boundary stop and L775's core/full-complement modulus
stop remain preserved. This proposal concerns an exact operator norm,
not another scalar angular-complement budget. There is no novelty claim.
An eventual growing-r cancellation estimate could warrant a creative
attempt, but no such estimate with a concrete independent budget is ready
yet. Do not label routine rational-Hankel specialization creative; the
missing representation and budget block that nomination for now.

Primary identities already used:
[Böttcher–Widom v1](https://arxiv.org/pdf/math/0604009v1),
[Bornemann v2](https://arxiv.org/pdf/0804.2543v2).
Mathlib coverage is unchecked. No cross-notebook input is proposed.

## Completed source comparison — step426

One literature-only step: no new operator identity was derived, no lemma
or mathematical script was modified, and L776 was read for applicability
rather than critically audited. The progress here is source coverage of
known mathematics, not progress beyond the sources checked.

### Searches, duplicates and primary read limits

Queries included `finite rank Hankel operator rational symbol multiple
poles singular values Gram matrix Kronecker theorem`, `Hankel operator
analytic symbol finite section norm error Fourier coefficients Hilbert
Schmidt`, `finite rank Hankel Gram matrices`, `Yafaev On finite rank Hankel
operators arxiv`, and `On singular values of Hankel operators of finite
rank Gragg Lindquist pdf` (the latter located Gragg–Reichel, not Lindquist).
Search hits for controls, optimal rational approximation and selfadjoint
inertia were compared with the actual product, not silently imported.
Targeted local searches used only the Fredholm assessments/working notes,
step425 history and the shifted-boundary ATTEMPTS record. The prior
boundary-sign and L775 scalar-modulus stops remain; neither establishes a
stop for this independent norm mechanism. No matching local certificate
was found in those searched records; this does not establish novelty.

V. V. Peller, *An excursion into the theory of Hankel operators*,
Holomorphic Spaces, MSRI Publications33 (1998), pp.65–120,
[publisher-hosted chapter](https://library.slmath.org/books/Book33/files/peller.pdf).
Read Section4, Theorem4.1 and its complete recurrence proof, printed
pp.76–77 (PDF pp.12–13), and Corollaries4.2–4.3. For the matrix indexed
from zero with entries alpha_(i+j), finite rank is equivalent to a rational
generating function; the rank is deg(z alpha(z)). For the Hardy-space
convention, the rational object is the negative-frequency part of the
symbol. This indexing distinction must be checked against L776's
H(f)_(i,j)=f_(i+j-1), i,j>=1. The theorem needs no pole simplicity.
Also read Section6 Theorems6.1–6.2 and surrounding hypotheses, p.81:
optimal finite-rank/rational approximation is an existence result, not
an explicit effective error for our symbol. Its proof was not imported.

K.-M. Perfekt and A. Pushnitski, *On Helson matrices: moment problems,
non-negativity, boundedness, and finite rank*,
[arXiv:1611.03772v2](https://arxiv.org/pdf/1611.03772v2), 30 August2017,
Section6.2 Theorem6.1, PDF pp.18–19. Read the full classical-Hankel
statement and boundedness qualification. The form is a finite sum of
c_j(h) times the h-th derivative of fg at distinct complex nodes lambda_j,
0<=h<=k_j, with top coefficient nonzero. Rank is sum(k_j+1); boundedness
on l2 is equivalent to all nodes lying strictly in the unit disk.
The generating kernels are derivatives of (1-w lambda)^(-1), with no
conjugate in that bilinear formula. Thus multiplicity is covered, but
the bilinear transpose cannot be replaced by a Hilbert adjoint without
tracking conjugation. This recalled classical theorem has no proof in
that section; Peller supplies the rational/recurrence proof input. No
multivariate Helson assertion is used.

D. R. Yafaev, *On finite rank Hankel operators*,
[arXiv:1304.2677v1](https://arxiv.org/pdf/1304.2677v1), 9 April2013,
Section5.1 (5.2),(5.6)–(5.7), PDF pp.22–23. Read the arbitrary-pole-order
representations and polynomial-exponential coefficient relation. This
corroborates the confluent case in sequence coordinates. The adjacent
selfadjoint hypotheses and Theorem5.3's inertia conclusion were inspected
to exclude a false norm-to-sign import: our product is not assumed
selfadjoint and inertia counts do not bound its largest singular value.
The separate real-line representation and its proof are not imported.

W. B. Gragg and L. Reichel, *On singular values of Hankel operators of
finite rank*, NPS-53-89-003, November1988,
[primary technical report](https://calhoun.nps.edu/server/api/core/bitstreams/e5e56899-62e6-4986-a73b-d8ee92dba669/content),
Section1, printed pp.1–5: read coprimality and initial distinct-pole
hypotheses, Proposition1.1, the QR reduction (1.11)–(1.17), and complete
Remark1.1. A rational symbol uses poles strictly inside the disk in this
report's convention. QR orthonormalizes the infinite column map before
taking singular values of a finite matrix. Remark1.1 replaces diagonal
pole data by Jordan blocks and confluent Vandermonde data and states the
reduction survives; the general multiplicity details are expressly omitted
by the authors. Therefore future local application must supply its
confluent factorization, not cite a nonexistent detailed proof. Do not
use the OCR-damaged repeated-pole formula or the report's inverse-Gram
algorithm as a black box. Sections2–5's computational algorithms and the
1989 journal version were not read or imported. The report covers the
Hankel factor, not the full compressed product.

J. Shapiro, *Functional Analysis*, Princeton MAT520 Fall2024,
last typeset 25 December2024,
[author notes](https://web.math.princeton.edu/~js129/PDFs/teaching/MAT520_fall_2024/MAT520_Lecture_Notes.pdf),
Section9.4 Theorem9.25 and its proof, pp.90–91. Read the partial-isometry
norm identity and extension on the orthogonal complement. Use only the
standard polar decomposition theorem for finite-rank maps (closed ranges);
no inverse of a possibly singular Gram matrix is justified. The notes'
unrelated TODO in Claim9.27 is not an input. Standard Cauchy coefficient
estimates, triangle inequality and operator-norm submultiplicativity,
already used in L776, suffice for conditional approximation errors; an
optimal rational-approximation theorem is unnecessary.

### Exact application obligations and bounded mathematical continuation

This is SPECIALIZE, because the sources cover the general mechanism but
not its actual-G application. The following objects specify the next
proof obligations; they are not asserted new identities or an actual
norm certificate established by this literature turn.

1. With the r-1 interior zeros named alpha_j=w_j/R and multiplicities
   m_j, define the monic interior polynomial P and the quotient
   F(z)=G(Rz)/P(z). Check removable zeros, F's zero-free neighborhood of
   the closed disk, and the scalar normalization against L776's exact
   logarithmic factors. Show which negative-frequency principal parts
   of c supply H(tilde c). The entire b is not asserted rational.
   Account for every repeated pole by derivatives/principal parts and
   check that the source's zero-based sequence is c_(-(n+1)). No real-
   zero, simple-zero or coefficient-minor sign assumption is permitted.

2. Obtain a finite column factorization B=V C W* for B=H(tilde c),
   including the complex-bilinear-to-adjoint conversion. Define
   U=Q_r H(b)V and Y=Q_r W. The finite matrix to justify is

       K=(U*U)^(1/2) C (Y*Y)^(1/2).

   The required norm equivalence is ||A_(r,R)||=||K||_2, with ||.||_2
   here the finite matrix spectral norm, not L776's Schatten2 notation.
   Prove the metric equivalence using polar decomposition on the supports;
   allow rank deficiency and avoid an unpaid inverse. Eigenvalues of
   C, a raw nonorthogonal matrix or the finite Hankel factor alone do not
   give the required norm. This is elementary application of the cited
   finite-rank/QR/polar results, not a new rational-Hankel theorem.

3. Supply a conditional computable enclosure. Retain explicit radii
   rho<1<sigma, analytic-factor supremum bounds, a strictly positive
   lower bound wherever F is inverted, zero-data/derivative errors and
   a truncation order. L776's annular coefficient estimates supply the
   source of geometric tails, but their constants must be displayed.
   Error quantities must include delta_b=||H(b)-H(b_hat)|| and
   delta_B=||B-B_hat||, not just coefficient residuals. For the
   finite approximation A_hat, the proof must pay the full product
   error using the norm triangle/product inequalities, including the
   cross error, and the finite singular-value enclosure error. A
   certified upper bound U_fin plus this total error must be <1.
   If a factor is exact, its delta may be zero only after proving that
   fact. No determinant error or Euclidean coefficient norm substitutes
   for this operator error. No actual zero-enclosure computation is
   approved by this conditional theorem scope.

The representation and conditional budget are a concrete intermediate
target, not a prediction of smallness. All quantities may depend on the
fixed admissible (r,R); no uniform inverse bound, zero separation or
growing-r saving is inferred. A finite matrix still depends on G through
F and its reciprocal. Omitting that dependence would fail the test.

Continue only if these obligations yield an exact original-norm
representation and a finite, fully specified conditional error budget
with no unpaid sign or inverse. Record a failure or park the proposal
if this cannot be done in one bounded application attempt. An eventual
actual norm >=1 stops that sufficient test at that pair, not RH. An
actual U_fin+error<1 would pay L776 only for that pair. Admissible radii
for all orders (tied moduli can skip counts), remaining indices and
all-degree mixed positivity stay open. L776 remains independently
unaudited; a conditional norm interface does not validate it.

No justified creative estimate is ready yet: the missing local product
representation and actual quantitative budget are precise blockers.
Once supplied, a different growing-order mechanism would need its own
bounded test and source scope. This routine specialization is not
relabeled creative to meet a scheduling preference. The exact TARGET
at the top is unchanged, so this completed review covers the next
mathematical invocation on that same target; no newly named continuation
is being self-approved. Full matching Mathlib coverage is unchecked.
