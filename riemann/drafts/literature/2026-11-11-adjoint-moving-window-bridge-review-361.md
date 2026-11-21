# Adjoint moving-window point bridge — source nomination

TARGET: Assess source coverage for an adjoint moving-window construction of C997c's point bridge, seeking band-dual measures with subexponential TV and a slope-uniform complete-kernel residual O(exp(-n/64)).
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Step362 searched moving-average adjoints, dilation-window inversion, approximate inverses and Volterra diagonal-zero results; read the primary contracts below and reused review322 for ambient continuation. No inspected theorem matches both original-TV and residual requirements; this bounded search establishes neither novelty nor impossibility.
SOURCE_EVIDENCE: Schuster–Quinto, SIAM J. Appl. Math.65(4)(2005), Section2 pp1371–1372, Definition2.1/(2.4)–(2.6)/Remark2.2; Schiefeneder–Haltmeier, arXiv:1606.03486v1, AppendixA.1 pp16–17, LemmaA.1/TheoremA.2 and its full uniqueness proof; Malone's Dublin thesis(2000), Sections1.2/1.5 pp1–4; Prouza, Kybernetika12(1976), Section2 pp103–104, screened for operator scope. C997c(1),(4)–(6) supplies the exact local kernel.
COMPARISON: Approximate-inverse reconstruction requires an appropriate solved adjoint equation; diagonal-zero Volterra uniqueness supplies neither range membership nor uniform inverse cost. Stationary refinement and discrete moving averages differ from the weighted finite windows. Prior scalar, spectral-tail and fixed-packet stops remain scoped and do not exclude an endpoint-chain test.
GAP: Construct or obstruct one zero-safe signed endpoint-chain adjoint with a finite complex band measure, slope-uniform residual O(exp(-n/64)) and subexponential original band-TV; boundary compatibility, representability and uniform constants remain unproved.
REASON: Essential source comparison is completed, with no persistent access blocker or matching theorem to import. It supports one bounded EXPLORE test, not existence or a universal obstruction. New continuation review362 receives separate approval before invocation; no mathematics was derived in this literature turn.
LITERATURE_REASON: Changed mechanism: adjoint moving-window/dilation construction on the exact response range, beyond the inspected saddle and ambient-Hardy contracts.
SCOPE: Integer n>=2; slope interval I=[7/4,9/4], data band E=[15/8,17/8], z_star=1+i/8; complete C997c(1) with both beta terms, both short intervals and K's -1. Arbitrary finite complex slope measures, original TV, fixed intervals; no actual-zero realization or selected-response identity is assumed.

## Exact proposed discriminator, not an established result

Write k_n(c,z)=H_n^+(z;delta_c), using the already defined C997c(1)
kernel, with delta_c the unit point mass at c. The proposed later
construction would seek complex Borel measures lambda_n supported on
the closed data band E such that, for all sufficiently large integers,

    ||lambda_n||_TV <= C_epsilon exp(epsilon*n) for every epsilon>0,
    sup_(c in I) |k_n(c,z_star)
           -integral_E k_n(c,gamma)dlambda_n(gamma)|
                                      <= C exp(-n/64).

The constants must be independent of n. This is a requested threshold,
not a claimed bound or a consequence of analytic uniqueness. The fixed
positive error exponent makes the proposal independently falsifiable;
an upper bound with an uncharged exponential coefficient cost does not
meet it. No candidate lambda_n, adjoint identity or new estimate was
derived during step361.

The suggested mechanism is to use the linked moving endpoints cn and
c(n+2) in the adjoint of the exact slope-to-response map, seeking a
signed telescoping construction across those windows. C997c(4) is the
starting identity; a later attempt must derive its own proposed adjoint
equation and boundary conditions. It must retain the complete lower
window and the weight g_n, including its zeros, without silently
dividing by g_n or replacing its sign by an absolute envelope. The
frequency-band restriction on lambda_n and its original variation are
part of the test, not consequences of a formal window inverse.

## Source-review work and acceptance test

Compare this exact operator question with primary work on adjoints of
moving averages, multiplicative/dilation window equations, and stable
band-limited reconstruction on an operator range. Retrieve precise
theorem hypotheses and relevant proof cases before importing a result.
Check whether the degree-dependent oscillatory weight, its zeros,
finite endpoint conditions and the simultaneous norm/rate requirements
are actually covered. Reuse adequate older coverage only within its
stated scope. A source giving injectivity or an uncontrolled inverse
is insufficient. An inaccessible nonessential lead is not a reason to
repeat a blocked source route.

Read only the directly relevant C997c kernel and specific comparisons.
C997a's original real-quartet dual problem differs from the proposed
one-sided point kernel; its (8) also warns that recovering this point
would not by itself recover the selected quartet. C997d records an
ambient-envelope loss, not a theorem excluding the exact operator
range. C997j/k only concern a fixed weighted polynomial space and
specific dual mechanisms. Those unaudited results are comparison
records here, not assumed mathematical inputs. The local screen is
not an exhaustive duplicate search; finish the comparison in the next
source turn before making a readiness decision.

Continue to one bounded creative proof attempt only if a specific
adjoint construction or precise quantitative obstruction test is
supported by adequate source coverage and differs from those recorded
failures. Otherwise report the actual overlap or source limitation and
nominate an independently testable mechanism. Do not broaden the
accepted C997p stop or repeat its saddle as discovery.

If the source comparison supports it, the intended later purpose is
proof_attempt/creative: the obstruction is simultaneous exponential
slope-residual decay and subexponential band-dual cost on the exact
response range. The bounded test is the displayed fixed-kernel pair of
bounds using one adjoint-window mechanism. This would address the point
bridge relevant to signed quartet selection, while C997a(8), the
selected/both-sign transfer, actual assay/reconstruction, L993,
signed recovery, complements, regulators and L984(H) remain independent
gaps. The main actual-Xi positivity gap L030-L032/C032a and L966/L968
forcing are unchanged. This is a nomination, not ready proof coverage
or a routing override for the next literature-only turn.

Mathlib matching coverage is unchecked and unknown. No cross-notebook
input is proposed. No complete RH candidate is involved.

## Completed source comparison — step362, 11 November 2026

The nomination above describes the state before this review. Its kernel,
intervals, point and simultaneous thresholds are unchanged. Outcome:
EXPLORATION / LITERATURE / NOVELTY_UNCHECKED. No construction, new adjoint
identity, specialization or impossibility theorem was derived. Source
extraction notes were checkpointed before finalizing this comparison.

### Primary contracts actually inspected

**Conditional adjoint reconstruction.** T. Schuster and E. T. Quinto,
*On a Regularization Scheme for Linear Operators in Distribution Spaces
with an Application to the Spherical Radon Transform*, SIAM J. Appl. Math.
65(4) (2005), 1369–1387, DOI 10.1137/S003613990343879X,
[author-hosted published text](https://sites.tufts.edu/tquinto/files/2021/01/srt.pdf),
Section2 pp1371–1372, Definition2.1, (2.4)–(2.6), Remark2.2.
For closed smooth-test-function subspaces V,W on open sets, continuous
injective A:V'->W', exact data g=Af, and a mollifier e_gamma in the stated
bidual pairing, a reconstruction kernel Psi_gamma satisfying
A*Psi_gamma=e_gamma gives f_gamma=<g,Psi_gamma>. Read the full pairing
argument and Remark2.2: a chosen mollifier need not have a solution in W.
The limit is weak distributional convergence. This conditional identity
supplies neither a prescribed reconstruction kernel nor a finite-measure
TV bound. Our space/range hypotheses have not been verified, so no
application is imported. A formal adjoint solution still needs an actual
band-measure representer with the requested estimates.

**Diagonal-zero uniqueness.** D. Schiefeneder and M. Haltmeier,
*The Radon Transform over Cones with Vertices on the Sphere and Orthogonal
Axes*, [arXiv:1606.03486v1](https://arxiv.org/pdf/1606.03486v1),
10 June2016, AppendixA.1 pp16–17, LemmaA.1 and TheoremA.2, including
its full proof. For Delta={a<=s<=u<=b}, real V in C^3(Delta), finitely
many simple zeros of V(s,s) in [a,b), and at each zero
(alpha1,alpha2)=grad V(s,s), alpha1+alpha2!=0,
1+alpha1/(alpha1+alpha2)>0, A.2 gives at most one continuous solution of
integral_a^u V(u,s)f(s)ds=g(u) for continuous g. The proof propagates
uniqueness between consecutive zeros and uses continuity at each zero.
The cited Volterra–Peres LemmaA.1 additionally requires a sole initial
simple zero, a linear Taylor part with continuous quadratic remainder
coefficients having continuous first u derivatives, and
g(s)=(s-a)^2 h(s), h in C^1, for existence and uniqueness.
No uniform stability bound is stated. Our complex band-adjoint problem
has not been reduced to this real triangular operator; its zero
multiplicities, gradient conditions and data compatibility are unverified.
This is a hypothesis warning, not an applicable inversion theorem.

**Dilation and moving-average terminology.** D. Malone,
*Solutions to Dilation Equations*, University of Dublin PhD (2000),
[author copy](https://www.maths.tcd.ie/~dwmalone/p/phd.pdf), declaration
dated 26 October2016, Sections1.2/1.5, printed pp1–4, treats refinement
g(x)=sum_k c_k g(2x-k) and its Fourier symbol. L. Prouza,
*On linear inversion of moving averages, discrete equalizers and
"whitening" filters, and the related difference equations and infinite
systems of linear equations*, Kybernetika12(2) (1976), 103–117,
[primary text](https://www.dml.cz/bitstream/handle/10338.dmlcz/124636/Kybernetika_12-1976-2_4.pdf),
Section2 pp103–104, sets up finite constant-coefficient discrete averages
of weakly stationary sequences and mean-square inversion. These setup
passages disambiguate scope. Neither is imported as a theorem about
weighted continuum windows, varying degree, complex band measures or TV.
Later classification/inversion theorems are not claimed as coverage.

### Exact comparison, duplicates and failures

C997c(1),(4)–(6) is the mathematical starting contract, including g_n and
the lower window. Its accepted finite-complex-measure Fubini representation
avoids a preliminary inverse. Endpoint cancellation must use it without
assuming a nonvanishing weight. None of the sources verifies that this
weight has only simple relevant zeros; no such claim is made here.

Reused review322's inspected Grabovsky–Hovsepyan Theorem2.7,
Trefethen Theorem5.2 and Demanet–Townsend Theorem2 assessments. Their
global Hardy/domain bounds and real-target hypotheses remain as recorded.
They do not supply a range-specific adjoint-window construction; no
redundant rereading or scalar-envelope calculation was performed.
C997d is a scope comparison, not a prohibition on the exact range.
C997a's interpolation and extra selected-response term,
ATTEMPTS/2026-11-10-adaptive-slope-dual-rate-unpaid-314.md,
C997j's scalar class and C997k's restricted polynomial spectral tail
were checked at their stated scopes. These unaudited comparisons are
not assumed theorems. C997p's accepted fixed-family stop is preserved;
no new packet regime or repeated saddle is nominated.

### Search and access record

Queries included `"moving average" "adjoint" inverse integral equation
variable kernel zeros`; `"dilation" "equation" "inverse" integral moving
average Mellin`; `Louis Maass approximate inverse method linear
functionals adjoint mollifier equation pdf`; `"Volterra" "first kind"
"vanishing" "diagonal" theorem integral equation`; `"moving average"
"inversion" integral equation deterministic theorem`; `"dilation"
integral equation "stability" inversion finite interval`; and exact-title
searches to locate primary copies. Local searches of named slope/point/
packet assessments and slope failures found no already inspected
endpoint-chain construction. This is bounded discovery, not novelty.

Saarbruecken preprint109 and Innsbruck PDF requests initially returned
502 errors. The Tufts published copy and arXiv v1, and later the indexed
Innsbruck preprint, supplied the relevant passages. No essential source
remains inaccessible. Louis–Maass (1990), Inverse Problems6, 427–440,
was located only at abstract level, an unread historical lead.
Rieder–Schuster's *Approximate Inverse in Action II* was located
bibliographically; its theorem/proof text was not read and the attempted
AMS PDF endpoint failed. It is nonessential to the direct endpoint-chain
test; no convergence/stability result from it is used. Other fractional,
Mellin and soft-extrapolation hits were discovery leads only. The first
notebook-local git status was overly verbose and truncated; it was used
only to observe pre-existing changes, not as mathematical evidence.
Subsequent claim/failure reads used named local paths.

### Decision and the single proposed continuation

EXPLORE: no adequate matching theorem or exact-range obstruction was
found in the bounded primary-source comparison. The remaining endpoint
compatibility, band representability and uniform estimates are proposed
mathematics, not missing essential access. The concrete proposal is one
finite signed endpoint chain linking the upper endpoints, retaining
every terminal and lower-window piece. It must pass the weight zeros
without uncontrolled division and produce an actual finite band measure.
Its quantitative discriminator is the unchanged pair of bounds above;
a failure of this ansatz has only that scope.

The new [test assessment](2026-11-11-adjoint-endpoint-chain-test-review-362.md)
requires separate approval next turn before mathematical invocation.
This review neither attempts nor approves a mathematical result. Weak
convergence, injectivity, an uncontrolled inverse, an L2 residual without
an original-TV conversion, or a numerical fit cannot pass the test.
No lemma, mathematical script or PROOF/DAG change was made. Mathlib full
matching coverage is unchecked/unknown. No cross-notebook input or RH
candidate is involved.
