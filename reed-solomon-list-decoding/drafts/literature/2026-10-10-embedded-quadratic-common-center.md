# Embedded quadratic packing — completed source comparison

TARGET: Assess a bounded search for a nonrealizable subfamily of at most eight L030 quadratic graphs under the specified consecutive-power embedding into H.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the RS-support/four-support and BGM assessments; searched prescribed agreement supports, common-center quadratic graphs, fixed-subgroup agreement hypergraphs and nonrealizable supports; scoped local searches found no completed test of this embedding. Queries, actual readings and unread leads are recorded below.
SOURCE_EVIDENCE: Alrabiah–Guruswami–Li, https://arxiv.org/pdf/2304.09445v3 (26 July 2023), Definition 2.5 and Lemma 2.7 with complete proof, printed pp. 7–8; inspected Theorem 2.9/Remark 2.10, p. 9, and Lemma 3.1, p. 10. Reused Shangguan–Tamo v1 Lemma 4.3 and BGM v4 coverage from the named prior assessments; precise citations below.
COMPARISON: The signed matrix framework covers finite fields and necessary scalar agreement constraints. It does not decide this fixed embedding or all pairwise tuple distinctions; generic/random rank guarantees are inapplicable as fixed-label certificates. L030 proves local independence, not one RS center. No exact-match theorem or novelty claim was established.
GAP: Later specialize the known matrix/common-root framework to arbitrary higher overlaps in the embedded subfamilies, justify row-wise tuple necessity, and compute exact actual-label pair-equality certificates; no new criterion or rank is proved in this review.
REASON: Essential source coverage is available for a bounded independent common-center diagnostic beyond the exhausted local edge system; existing generic results cannot replace its finite certificate.
SCOPE: Source review of the saved target and preparation of the precise 512-candidate continuation below; no mathematical script, lemma, rank calculation, quantitative cap or safety conclusion is produced here.

LITERATURE_REASON: The proposed embedding/common-center target lay outside the ready mixed-moment audit and local-independence assessments; its essential selected-support and tuple scope needed comparison.

## Pinned instance and proposed mathematical test

Use C001a/C012a's n=1024, k=64, E=F_65537, F=F_(65537^28),
and H of order 1024. Pin g=3^64 mod 65537=19139, with its order already
certified in C012a and used in L020/L031. Recheck that order in any later
finite certificate. Set C={g^j: 0<=j<=60}. In increasing order write L030's
T={16,64,70,102,112,118,121} as t_0,...,t_6 in F_137.
The proposed injection sends the auxiliary point (t_i,y) to
g^(61+137*i+y), with y represented by its integer in {0,...,136}.
The unused exponents are 1020,...,1023. This is a set labeling, not
a field embedding. For each polynomial f of degree at most two over
F_137, propose the selected support
C union {g^(61+137*i+rep(f(t_i))): 0<=i<=6}.

The proposed later diagnostic is to search for a subfamily of at most
eight distinct such supports that cannot belong to pairwise distinct
degree-less-than-64 messages agreeing with one received word on those
supports, for every tuple width m>=1. The source review should fix a
bounded candidate-selection procedure and stopping budget before
mathematics; no exhaustive family search is implied. A successful
negative certificate must identify all auxiliary polynomials, every
actual support/intersection and an exact linear-algebra obstruction
forcing a pair of messages equal in every tuple row. A singular matrix
alone is not a realization proof. Allow extra agreements and keep the
distinctions between scalar sufficiency and arbitrary-tuple necessity.

## Primary statements and comparison

Omar Alrabiah, Venkatesan Guruswami and Ray Li, *Randomly punctured
Reed–Solomon codes achieve list-decoding capacity over linear-sized
fields*, [arXiv:2304.09445v3](https://arxiv.org/pdf/2304.09445v3),
26 July 2023: Definition 2.5, printed p. 7, specifies signed Vandermonde
blocks, one star of equality constraints per labeled hyperedge, over
any finite field. Lemma 2.7 and its complete proof, p. 8, give a
specialized nonzero kernel from coefficient differences relative to
the last codeword. The theorem concerns distinct scalar codewords
and their actual agreement hypergraph. Selected supports and arbitrary
tuple rows need their own applicability argument; extra agreements
must remain permitted.

Theorem 2.9 and Remark 2.10, p. 9, concern symbolic rank for weakly
partition-connected hypergraphs. Lemma 3.1, p. 10, assumes uniformly
random distinct evaluation points. Neither certifies a prescribed
subgroup specialization. This is a method import, not an imported
answer to the finite diagnostic. No generic-rank theorem is reproved.

Reuse the adequate comparison in
[the four-support assessment](2026-10-07-four-support-realizability.md)
and [the RS-support assessment](2026-10-05-rs-support-realizability.md).
The former records Chong Shangguan and Itzhak Tamo,
*Combinatorial list-decoding of Reed–Solomon codes beyond the Johnson
radius*, [arXiv:1911.01502v1](https://arxiv.org/pdf/1911.01502v1),
4 November 2019, Lemma 4.3, printed pp. 11–12, for common-root removal;
its Section 5 unsigned matrices assume characteristic two and cannot
be used unchanged here. These passages were not retrieved again.
L020's degree-61 division and L031's rank/pair-distinction proof were
read locally. Neither local result is silently asserted for arbitrary
higher overlaps: that extension remains a later specialization obligation.

Reuse the “New primary readings” comparison in
[the BGM assessment](2026-09-26-current-target.md): Joshua Brakensiek,
Sivakanth Gopi and Visu Makam, *Generic Reed-Solomon Codes Achieve
List-decoding Capacity*,
[arXiv:2206.05256v4](https://arxiv.org/html/2206.05256v4),
28 August 2024, Theorem 1.13, Corollary 1.15 and Proposition 4.5.
Its generic/random-domain qualification is unchanged, so no repeated
retrieval was needed. Gouveia–Parrilo–Thomas's Boolean moment coverage
in foundations/08-boolean-moment-source.md is also reused only as a
contrast: it does not imply RS common-center realization.

## Bounded search and duplicate evidence

Queries executed on 2026-10-10:

- `Reed Solomon prescribed agreement supports realizability common received word higher order MDS intersection Vandermonde`
- `Reed Solomon common center agreement patterns GM MDS higher order MDS BGM theorem`
- `"Reed Solomon" "quadratic" "common center" supports`
- `"Reed Solomon" "prescribed" "agreement" "intersection matrix"`
- `"137" "Reed-Solomon" "quadratic" agreement`
- `"Reed-Solomon" "agreement hypergraph" "fixed" "subgroup"`
- `"Reed-Solomon" "nonrealizable" supports`

Search results did not establish a matching inspected theorem. This is
not an exhaustive search or evidence of originality. The primary AGL
definition, necessary-kernel proof and relevant theorem hypotheses were
read before further comparison. Narrow local searches in assessments,
foundations, histories and ATTEMPTS for embedded quadratic/common-center,
consecutive-power and reduced-intersection terms found the proposal and
the earlier pattern-specific tests, rather than a completed embedding test.
Relevant full passages of L030, L020 and L031 were read, together with
C001a/C012a's instance/generator and ATTEMPTS/021,022,030. Their stops stay
intact. L020's forbidden disjoint-pair triple cannot simply be sought as
L030's forbidden incidence pattern; L030 already excludes that antecedent.
L031's different core/pair hypotheses likewise do not cover this family.

A search lead advertised *MDS Paving Bounds for Reed–Solomon MCA*,
ePrint 2026/1463. The actual
[primary landing page](https://eprint.iacr.org/2026/1463), checked
2026-10-10, instead gives Przemek Chojecki, *Shortening Bounds for
Reed-Solomon MCA*, received 17 July/approved 21 July 2026. Only its
abstract and metadata were inspected. Its theorem text remains unread,
so no bound, applicability or overlap is imported from it. It is an
optional MCA lead, not essential coverage for the signed finite diagnostic.
Generalized GM-MDS and later merged/journal AGL statements remain unread
leads; the readable pinned version supplies the needed framework.

## Exact later prescription; no execution in this turn

The separately saved
[research assessment](2026-10-10-embedded-quadratic-bounded-search.md)
has the exact mathematical Next action. Its new ready scope receives
separate supervisor approval before research; this literature turn performs
no derivation or candidate-generation arithmetic.

Use only the following pool Q of auxiliary quadratics over F_137:
all a+bZ+cZ^2 with a,b,c in {0,1,136}, together with
a+lambda*(Z-u)*(Z-v) for a in {0,1,2,3}, lambda in {1,2,3,4}
and u<v in the pinned T. Normalize coefficients modulo 137, deduplicate,
and sort coefficient triples (constant,linear,quadratic) lexicographically
by representatives in 0,...,136. This is a finite search prescription,
not an asserted representative of all L030 graphs.

Generate exactly 512 trials b=0,...,511, stopping early only on a verified
obstruction. Trial size is d=2+(b mod 7). Use one continuous 32-bit LCG,
initial state 137061 and update s=(1664525*s+1013904223) mod 2^32.
Every draw first updates s. Choose the initial graph using s mod |Q|.
Grow the candidate by adding an unselected pool graph maximizing the
increase in w=sum_x max(|I_x|-1,0), where x ranges over auxiliary
graph points and I_x is its set of incident selected graphs. Break each
tie by a new draw modulo the lexicographically ordered tied list.
Use a tie draw also for singleton ties. Repeated completed candidates
consume a trial; record them without replacing them. Save the full pool,
draw transcript and candidate order. Auxiliary incidence is only a
selection heuristic; all ranks use the embedded E labels. Do not identify
coefficient translates or auxiliary symmetries as actual-label symmetries.

For each tested candidate, record all polynomials, every actual label
and support, and all higher intersections. Import AGL's signed equality
rows for each shared point, keeping characteristic-65537 minus signs.
A reduced degree-two matrix after removal of C may be used only with
a written common-root/degree argument covering every tuple row and every
higher overlap. The remaining common intersection may be larger than C;
do not assume pair-only incidence or exactly C as full common intersection.

The discriminating certificate sought is a pair whose coefficient
difference map vanishes on the complete equality kernel, with an exact
row-space identity, or a full-column-rank certificate as a special case.
The later proof must transfer its equality conclusion to every F-valued
tuple row, without descent or a projection preserving distinctions.
For a nonobstructed candidate, report every pair-map augmented rank;
singularity alone is not a positive realization certificate. Any positive
realization claim also needs a compatible center and distinct messages,
using or specializing L031's proper-subspace argument with its field-size
hypothesis. Store full exact matrices, row operations/identities and
failures on disk; print concise counts, bounds and certificate paths.

Stop at the first verified obstruction or at 512 trials. A certificate
allows a separately assessed restriction/cap target. No obstruction in
the prescribed trials parks this particular search prescription, without
asserting full-family realization or exhaustion of other embeddings or
mechanisms. A failed proof/certificate check is unfinished work to save,
not a mathematical negative conclusion. No list threshold is established
by a subfamily of size at most eight.

## Relevance, competing mechanisms and stop test

The main gap remains 67/68-agreement safety. L030's family defeats
the old local independence cap, yet has never been shown to be one
RS list. A forbidden subfamily would identify a concrete additional
RS restriction even within this old obstruction, potentially informing
a stronger local cap. It would not itself bound all realizable families
or imply safety. Quantification over other embeddings, cross-core
consistency, effective caps and common-center list sizes remain open.

The alternatives screened were extending L019 rational-center witnesses
to 67 agreements (outside that assessment's explicitly limited scope,
with no new quantitative mechanism identified), and the global moment
slice in ATTEMPTS/022 (historically process-parked, not mathematically
refuted). The selected diagnostic has explicit actual labels and a
finite checkable obstruction criterion. It does not revisit the failed
L046 map, add orders to L030's unchanged hierarchy, or assume that
auxiliary-field operations preserve actual subgroup ranks.

The primary-source comparison is complete for this bounded specialization;
its newly saved continuation still awaits separate supervisor approval.
A certified nonrealizable subfamily
would justify considering the added restriction in a later target;
an unsuccessful bounded search would justify only a diagnostic stop,
not full-family realization or a cap. If sources identify an applicable
theorem, import it with its precise hypotheses instead of reproving it.

Essential inputs for continuation: C001a/C012a for the actual instance,
L030 for the graph family, and L020/L031 for prior selected-support
rank-test comparisons. These are proposed inputs, not a new DAG node.
The old local obstruction in ATTEMPTS/021 and fixed-map obstruction in
ATTEMPTS/030 remain intact. This review supplies method coverage and a
concrete test, not new mathematics, finite rank evidence or progress beyond
the sources checked. Mathlib full matching and supporting coverage has
not been checked; unknown availability is not absence.
