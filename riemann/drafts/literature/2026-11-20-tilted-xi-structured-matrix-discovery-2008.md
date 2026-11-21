# Actual tilted-Xi structured-matrix discovery: completed review2009

TARGET: Assess primary coverage for a generalized Jacobi or comrade-matrix certificate of one negative square for Kuznetsov's exact Jensen-weighted tilted-Xi polynomials, and nominate one bounded actual-coefficient test.
CHECKED: 2026-11-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Inspected primary comrade, generalized Jacobi, symmetrizer, Pontryagin and Schur-inertia hypotheses; reused exact-family review2001 and C029m. Scoped searches/failure comparisons below did not establish an actual-family metric theorem; no novelty inference.
SOURCE_EVIDENCE: Noferini–Robol–Vandebril arXiv:1912.04157v2 Definition2.1/Theorem2.2/full proof and Section2.2 equation(2.1), PDF pp3–5; Derevyagin MFAT12(2006),220–233, Definition2.1/Propositions2.2–2.5 pp222–223; Amiraslani–Corless–Lancaster SFU manuscript Section2.2/Proposition3 p7; Behrndt–Derkach–Hassi–de Snoo OAM5(2011),679–706, Sections2.2–2.3/Lemma2.2 and proof pp681–683; Page–Styan–Wang–Zhang Section2 equations(8)–(16), manuscript pp3–4. Direct links and qualifications below.
COMPARISON: Known results give a coefficient-dependent comrade and a conditional root count once a nonsingular low-index metric is supplied, not its existence for these coefficients. Generalized Jacobi representation and constant-recurrence symmetrizers have unpaid or mismatched premises. Select a boundary-supported metric only as an untested finite ansatz.
GAP: Construct an actual-coefficient nonsingular metric of index<=1 uniformly eventually; first test the specified ansatz at N=6, including actual degree, orientation and nonsingularity.
REASON: Essential source discovery now supports a bounded metric-feasibility attempt. This is EXPLORATION/source preparation, with no actual-family index estimate, new theorem or RH candidate.
LITERATURE_REASON: Startup scope2008 was REVIEW_REQUIRED; its essential matrix/metric sources were outside ready scope2007. The conditional RH implication was not reviewed again.
SCOPE: Literature comparison and selection only. No lemma or mathematical script writes; the new continuation in assessment2009 requires the supervisor's separate approval before invocation.

## Gap, inputs and test

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity. On this
branch C029m proves that an eventual Hermite negative index<=1 suffices
for RH. The intermediate target is a root-independent metric certificate.
Its downstream use requires all sufficiently large N; a finite test
cannot supply that uniformity.

Reuse C029m's exact full T_N, including odd coefficients and Jensen
weights, from Kuznetsov2008 (3)–(4)/(13), pp563/566 and pp568–569,
[DOI](https://doi.org/10.4153/CMB-2008-055-0). Review2001 supplies the
previously inspected exact formulas. The convergence input retains the
unnumbered-source-assertion and unaudited upstream[9] qualifications.
No new analytic input or reciprocal-series argument is proposed.

Nominate **N=6 only**: certify its actual degree, form its comrade in
descending basis order, and symmetrically scale the basis part. Call
this matrix A. Seek a real vector z satisfying the proposed equations

    G=I+e_1 z^T+z e_1^T,    A^T G=GA,

with G nonsingular and negative index at most one. The motivation is
the source's one-row coefficient correction and a metric whose bulk
block is fixed to the identity. This is a hypothesis to test, not a
metric already constructed. No compatibility conditions or coefficients
were calculated this turn.

Success requires exact identities and certified inertia; incompatibility
or only singular feasible metrics rejects this ansatz. Unseparated
numerical residuals are inconclusive. A pass could motivate a uniform
formula; a failure stops this boundary ansatz, not all metrics or RH.
Failure at N=6 alone does not exclude an eventual-only variant; reopening
would need a specific reason that its obstruction disappears. This is
a small linear compatibility problem that can begin on paper without
Arb, installation or runtime discovery, distinct from the parked T_24
Hermite calculation. An uncovered certification method requires a new
source gate, not an unsupported implementation.

## Primary statements and applicability

**Comrade.** V. Noferini, L. Robol and R. Vandebril, *Structured backward
errors in linearizations*, [arXiv:1912.04157v2, 12 May 2021](https://arxiv.org/pdf/1912.04157v2),
Definition2.1/Theorem2.2/full three-part proof, PDF pp3–4: a degree-graded
basis has leading coefficients nu_j!=0. With descending Phi, p=phi_n+c^T Phi,
chi=nu_n/nu_(n-1), their C satisfies
C Phi=x Phi-chi^(-1)p e_1, det(xI-C)=p/nu_n, and
C=H-chi^(-1)e_1 c^T. No simple-root hypothesis is imposed.
Section2.2, PDF pp4–5, gives diagonal scaling(2.1) of the tridiagonal H
using positive recurrence factors. Its opening orthonormality assumption
uses a closed real interval; for Pollaczek use the general theorem and
verify the displayed finite scaling algebra from the exact recurrence,
without assuming compact support or importing later Jacobi estimates.
Actual degree and normalization need checking first. No low-index metric
is supplied. A rank-one coefficient correction is not an index bound.

**Generalized Jacobi.** M. S. Derevyagin, *Borg-type theorems for
generalized Jacobi matrices and trace formulas*, MFAT12(3) (2006),220–233,
[journal PDF](https://mfat.imath.kiev.ua/article/2006/03/der.pdf),
Definition2.1/Propositions2.2–2.5, pp222–223: real monic p_j of degrees
k_j, signs epsilon_j=±1, b_j>0 and signed couplings
 epsilon_j epsilon_(j+1)b_j define the specified block matrix.
The metric is diag(epsilon_j E_(p_j)^(-1)); Proposition2.2 asserts
symmetry and Proposition2.3 identifies the characteristic polynomial.
These cite upstream[9], without proofs here. Read Proposition2.5's
no-common-zero proof: recurrence plus endpoint initialization, with no
assertion of simple roots of each polynomial. The actual T_N would need
a new block representation and a metric-inertia bound; neither follows
from its positive basis recurrence. This candidate supplies no direct
import of the needed index estimate.

**Narrower symmetrizer.** A. Amiraslani, R. M. Corless and P. Lancaster,
*Linearization of matrix polynomials expressed in polynomial bases*,
IMA J. Numer. Anal.29 (2009),141–157,
[DOI](https://doi.org/10.1093/imanum/drm051),
[SFU manuscript](https://www.cecm.sfu.ca/~pborwein/MITACS/papers/LinMatPol.pdf),
Section2.2/Proposition3 and surrounding qualifications, manuscript p7:
recurrence factors alpha_j=alpha!=0, beta_j=beta and gamma_j=gamma must
be constant; matrix coefficients are Hermitian and the leading one is
nonsingular. Right symmetrizer(22) gives a Hermitian pencil, without a
one-negative-square bound. Pollaczek's recurrence factors vary, so this
is not directly applicable. The proposition is stated as readily verified
without a separate proof. Right symmetrizers cannot be silently treated
as left metrics; invertibility and orientation matter. Singular-leading
work is referenced but uninspected and not needed for the actual-degree
test.

**Root-count interface.** J. Behrndt, V. A. Derkach, S. Hassi and
H. S. V. de Snoo, *A realization theorem for generalized Nevanlinna
families*, Operators and Matrices5(4) (2011),679–706,
[journal PDF](https://files.ele-math.com/articles/oam-05-49.pdf),
Sections2.2–2.3 pp681–682: a selfadjoint operator in a Pontryagin space
of negative index kappa has at most kappa eigenvalue locations in each
open half-plane. Read Lemma2.2 and its complete proof through p683:
distinct eigenvectors span a neutral space; the multivalued-relation
exception is explicit. For a finite real matrix the applicable premises
are a symmetric nonsingular G and A^T G=GA. No diagonalizability or
simple-root assumption is needed for distinct locations. The unnumbered
operator statement cites [1]/[16]; those books were not independently
audited. Singular G is not covered. Singular Newton-sum Hermite forms
are a different issue, already handled by C029l. Repeated roots do not
invalidate this distinct-location interface.

**Inertia.** C. Page, G. P. H. Styan, B.-Y. Wang and F. Zhang, *Hua's
matrix equality and Schur complements*,
[author manuscript](https://www.cs.mcgill.ca/~chris/pub/PaiSWZ08.pdf),
Section2, manuscript pp3–4, equations(8)–(16): Hermitian inertia adds
over an invertible principal block and its Schur complement, by displayed
congruence(10) and Sylvester's law(15). Read that congruence and the
invertible-block case. Singular-block generalizations have extra range
conditions and are unnecessary with the proposed identity bulk. This
is a known verification method; no metric or Schur value was evaluated.

These statements support a future finite applicability/feasibility proof,
not a theorem imported specifically for tilted Xi. The three candidate
mechanisms compared were block Jacobi realization, a general explicit
symmetrizer, and the boundary-supported metric ansatz. The last is
selected for its finite falsifiability; its compatibility remains unknown.

## Search scope, failures and access

Queries included `comrade matrix orthogonal polynomials symmetric
indefinite metric Bezoutian inertia`, `generalized Jacobi matrix
Pontryagin space polynomial negative squares theorem`, `comrade matrix
symmetrizer orthogonal polynomial Bezoutian Barnett pdf`, `comrade matrix
Jacobi rank one perturbation orthogonal polynomial pdf`, `comrade matrix
indefinite`, `Kuznetsov Meixner Jacobi matrix`, `comrade rank-two metric
polynomial`, and the exact Amiraslani paper title. Over-specific
Kuznetsov/comrade queries returned irrelevant political results;
these are failed searches, not absence or novelty evidence. Primary
hypotheses above, rather than snippets, support the comparison.

Local reads: C029m; review2001; L530/L955 hypothesis/conclusion ranges;
November20 tilted-family assessments, attempts and histories; the named
November5 common-Favard stop and post-Favard discovery review. Scoped
term searches found no matching boundary-metric test in those records.
L530/L955 refute generic preservation, not the actual-family bound.
The L796 common-positive-measure stop concerns another central sequence
and one common measure, not this degree-dependent indefinite metric.
No sibling notebook was read; no cross-notebook input is proposed.
Stops2002/2003 and summability park2005 remain preserved.

PDF screenshots returned references without image payloads; no visual
inspection is claimed. Indexed primary text supplied the hypotheses
and proof cases. A Bern-hosted Langer–Najman–Tretter PDF returned503;
that unread lead was replaced for the essential operator statement by
the accessible OAM text. Barnett's original work was not inspected;
the modern proved comrade theorem suffices here. No essential source
blocker remains for the finite ansatz test. Mathlib coverage unchecked.
