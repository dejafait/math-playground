# Actual-theta order-five cell: completed source comparison

TARGET: Assess whether primary results already determine the sign of the actual Xi coefficient minor D_(5,4)=det[a_(4+j-i)]_(i,j=0)^4, with a_n=M_(2n)/(8*4^n*(2n)!), and identify its precise overlap with L772, L786 and C792a/b before proposing any theta-specific signed calculation.
CHECKED: 2026-11-05
DECISION: IMPORT
SEARCH_EVIDENCE: Step569 searched actual xi coefficient PF/order-five and Katkova finite-order terminology; inspected the primary finite-order statement and its complete short proof, and reused the named local assessments. No calculation or novelty inference.
SOURCE_EVIDENCE: Katkova math/0505174v1 definitions/(3)–(8) pp.2–4, Theorem B/Theorem1 and full proof pp.5–6; Michałowski 2607.16795v1 (1)–(3), Section1.2/Theorem1.1 for scope only. Nonnegativity is covered; strict positivity is not imported. Source-index qualification below.
COMPARISON: Finite-order coefficient positivity already excludes negative actual D_(5,4). L772 is another sequence; L786 is strict order three; L792/C792a/b concern Jensen polynomials and preserver obstructions, not this Toeplitz minor.
GAP: A strict positive margin is not established by the reviewed finite-order statement. All-degree mixed positivity and an independent uniform signed bridge remain open.
REASON: Primary overlap changes routing: abandon a calculation seeking an unknown nonnegative sign; record the known input by citation/applicability only, without claiming discovery.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED lacked essential exact finite-order coverage; the existing order-three/asymptotic assessments did not settle this source question.
SCOPE: Literature-only comparison; no lemma, mathematical script, determinant calculation, strictness proof or source reproof. Newly written import coverage requires separate next-turn approval.

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
resolve source coverage for one actual order-five cell at the order
where the recorded generic construction can fail. A known positive
result could be imported as a bounded actual-weighted input; a known
obstruction could redirect the proposed comparison. Neither finite-cell
positivity nor failure of a generic sufficient criterion resolves the
main gap or supplies an all-degree bridge.

Continuation test: find an inspected primary statement covering the
exact normalized actual cell (or a rigorously stronger family), or
specify an uncovered actual signed estimate with an independently
checkable threshold and downstream use. Import covered mathematics;
do not run a certificate merely to reproduce it. Abandon a proposed
calculation if its sign is already imported or its only new premise is
the desired minor sign itself. A failed search does not establish novelty.

Essential input IDs for the review: L019/L021 for the actual moments,
L776 for the coefficient and minor conventions, L772 as a generic
contrast, L786 and L792/C792a/C792b for local overlap. Retrieve only
their relevant statements and the specifically needed source evidence.
L812 is the route-decision evidence, not an input to a minor identity.
Do not infer positivity from L790's Taylor bound alone. No cross-notebook
input is proposed. Full matching Mathlib coverage is unchecked.

Unresolved obligations remain actual signed compensation, a sufficient
degree-uniform bridge, initial/edge and shifted/mixed regimes. No new
creative mechanism is ready: an independent sufficient functional and
signed margin are still unspecified. This source review may establish
that the cell is already known and should not be pursued. It must not
be presented as protected creative work merely to satisfy scheduling.

## Completed primary comparison — step569

The nomination above is preserved as the starting question. This section
supersedes its pending source status. The source test finds known
nonnegativity, not a strict sign or quantitative margin.

Olga M. Katkova, *Multiple positivity and the Riemann zeta-function*,
Comput. Methods Funct. Theory **7** (2007),13–31,
DOI [10.1007/BF03321628](https://doi.org/10.1007/BF03321628).
Numbering binds to [math/0505174v1](https://arxiv.org/pdf/math/0505174v1#page=5),
not an independently inspected journal copy. Read definitions/(3)–(8),
Theorem B, Theorem1 and its complete short proof, including the product
limit. Theorem1 states xi_1(z)=xi(1/2+sqrt(z)) belongs to PF44;
PF denotes nonnegative minors, not strict positivity. Its proof uses a
zero-free sector and genus-zero polynomial products converging compactly.

**Source qualification.** The printed sector is |arg z|<43*pi/44,
whereas Theorem B's PF_m threshold is m*pi/(m+1). The displayed maximal
PF44 inference therefore has an apparent one-order mismatch. Do not
import that endpoint. The order-five application is safely below the
printed threshold and is the only nominated application. No corrected
maximal-order theorem or strictness argument is proved here. The PDF
retains its v1 identifier despite a generated 2018 title-page date.

The [16 September2006 author revision](https://www.dcce.ibilce.unesp.br/~dimitrov/ProfRusev/Katkova/18.pdf)
was located and its opening definitions retrieved, but theorem-page
access timed out; shell retrieval failed DNS. Its finite-order theorem
and the journal text remain unread and are unused. These access failures
do not block the safely lower-order import. Schoenberg's original 1955
proof was not independently read; cite Katkova's primary result/proof.

Wojciech Michałowski, [arXiv:2607.16795v1](https://arxiv.org/html/2607.16795v1#S1.SS2),
18 July2026: read (1)–(3), Section1.2 and Theorem1.1 for comparison.
Its verified-height discussion describes a much larger finite-order
nonnegative region; its strict tail theorem requires k>=10^18*r^3 and
does not cover (5,4). No verified-height extension, strict sign or
ancillary certificate is imported. Reuse step385's proof-scope assessment.
Its tail-scope phrase about an open complementary region cannot override
its preceding finite-order coverage.

### Local overlap and future applicability

L776 fixes G(w)=xi(1/2+sqrt(w)/2)/8 with ordinary a_n. Katkova uses
xi_1(z)=xi(1/2+sqrt(z)) with ordinary b_n. The later canonical import
must explicitly check G(w)=xi_1(w/4)/8, retain all positive scale
factors, and identify increasing Toeplitz rows0,...,4 and columns4,...,8.
This is an applicability obligation, not a new derivation in this review.
No contour radius, zero count, Fredholm norm or theta quadrature is needed.
L019/L021/L776 and L786 already fix the actual moment normalization.

L772 has no actual-theta realization: its negative generic minor and
all-iterate Turan signs do not determine the actual cell. Reuse its
canonical audit coverage in `2026-11-04-positive-entire-countermodel-audit.md`;
no repeated audit. L786 imports Nuttall's strict order-three theorem and
does not imply order five. L792 instead concerns the central degree-five
Jensen polynomial, with gamma(j)=8*4^j*j!*a_j; its particular real-rooted
image and signed residual are not this Toeplitz determinant. C792a
excludes universal diagonal hyperbolicity preservation with the matched
prefix; C792b excludes same-mesh preservation. Neither contradicts known
finite-order coefficient nonnegativity. No C792b audit was performed.

Reuse `2026-11-04-actual-jensen-mechanism-discovery.md` (step385),
`2026-11-04-actual-toeplitz-signed-integral-review.md` (step389),
`2026-11-05-nuttall-order-three-import.md`, and the L772 audit assessment.
Queries included “Riemann xi coefficients Polya frequency PF 44 Katkova
determinant order 5”, “Riemann xi function Taylor coefficients total
positivity Michalowski 2025”, and exact Katkova/title/PF43 variants.
Secondary PF43 summaries were discovery leads only. Kernel PF failure,
infinite log-concavity and Jensen hyperbolicity are different statements.
No sibling notebook was read. Full matching Mathlib coverage is unchecked.

**Decision:** abandon the proposed unknown-nonnegative-sign calculation.
Strict positivity remains unimported, but no redundant determinant
certificate is nominated. The sole next action is the known import in
`2026-11-05-katkova-order-five-nonnegative-import.md`, after separate
next-turn approval. Stop on an actual scaling/scope mismatch and preserve
its evidence; do not silently upgrade >=0 to >0. Essential proof inputs
are L018/L019/L021 and L776 definitions only; the other named results
are comparisons. All-degree mixed positivity, actual signed compensation,
degree-uniform sufficiency and initial/edge/shifted regimes remain open.
No creative mechanism is ready: an independent sufficient signed
functional and uniform margin are still missing.
