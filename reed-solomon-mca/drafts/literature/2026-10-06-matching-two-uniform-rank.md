# Source review for a matching-two uniform rank obstruction

TARGET: Review known results and local obstructions for a uniform rank-28 theorem for all sixteen-edge, four-uniform, four-regular support families of matching number two on sixteen vertices over the fixed H.
CHECKED: 2026-10-06
DECISION: EXPLORE
SEARCH_EVIDENCE: October 6 bounded searches for fixed-evaluation exterior rank, four-regular four-uniform matching-two families and exterior hypergraph bounds found no inspected theorem deciding the universal target; queries and screened leads below.
SOURCE_EVIDENCE: Reused the inspected Conrad, Lovett, BGM, BDG, Gandini, Boito–Ruatta and regular-hypergraph assessments; read Scott–Wilmer's May 11, 2021 author PDF, Theorem 2.3 and proof, Lemma 3.4 and proof, and Corollary 3.5 and proof; inspected the essential local statements and arguments listed below.
COMPARISON: The sources supply exterior machinery, generic or selectable-evaluation theorems, and intersection/projection bounds, but no fixed-H simultaneous rank theorem; L024 excludes equality without stating a full-matrix rank, and L027/L029 cover only their specific patterns.
GAP: Universal rank 28 remains unproved; no certified rank-deficient admissible family is known from the inspected evidence, and rank deficiency would not itself realize equality.
REASON: Essential comparison is adequate for a bounded exact falsification test, without a theorem import or novelty claim; the newly completed continuation requires separate next-turn approval before invocation.
SCOPE: All simple sixteen-edge four-uniform four-regular families of matching number two on sixteen vertices, labeled bijectively by fixed H; only the bounded test specified below is preassessed, not an arbitrary-family classification or a generic-to-fixed specialization.
COVERED_TARGET: Test the proposed matching-two rank-28 obstruction by an exact search of at most 256 admissible support-family/H-labeling pairs, including the two-block case.

## Exact proposed mathematical scope

Let F range over finite extensions of F_97 and let H be its fixed
order-sixteen prime-subfield subgroup. A candidate family consists of
sixteen distinct four-element subsets of a sixteen-element vertex set,
with every vertex in exactly four subsets and maximum disjoint
subfamily size exactly two. For every bijection from its vertices to H,
form the annihilator rows and six-by-28 alternating block for each
support exactly as in L029. The question for source comparison is
whether the full stack always has rank 28. This is a proposed sufficient
obstruction, not a necessary condition for excluding equality and not
an assertion that the proposed theorem is true.

Reuse the existing exterior-algebra source assessment and generic-
versus-fixed-evaluation comparisons before seeking essential new
coverage. Compare the exact universal statement, stronger applicable
results and known counterexamples. Essential local comparisons are
L010's equality incidence conditions, L023/L024's two-block example,
L025/L027's matching-two family and L029/L030's 0135 family.
Those results must be read in their canonical files as needed;
no inference about their full matrix ranks is made in this checkpoint.
ATTEMPTS/019 stops the old seven-block containment search and must be
preserved. This proposed uniform mechanism does not repeat that search
or assume that a finite cyclic list exhausts the families.

The main bottleneck remains sixteen-count equality versus allowable
fifteen in the frozen four-omission cell. A justified uniform rank
attempt could address the matching-two branch beyond individual cyclic
families, using the already audited syndrome mechanism. Families with
larger matching number, arbitrary disjoint triples, realizability with
full weights and distinct parameters when rank fails, and ABF26
identification remain independent issues. No result from another
notebook or uncertified source is assumed.

The comparison below selects a bounded mathematical test, rather than
an import. Failure of full rank must not be called an MCA equality
witness. No proof or calculation of the universal assertion was
performed in this literature-only step. Full Mathlib matching coverage
is not checked.

## Reused source hypotheses and scope differences

Reuse [the 0135 assessment](2026-10-06-cyclic-0135-full-rank.md)
and [the arbitrary-label assessment](2026-10-05-cyclic-0125-arbitrary-label-rank.md)
for the following inspected primary statements. Their machinery and
scope comparisons persist when the support family changes; their
family-specific approvals do not transfer.

- Keith Conrad, [Exterior Powers](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf),
  undated author PDF retrieved October 6: Theorem 4.2, p. 11;
  Theorems 5.1/5.4, pp. 15–17; Corollary 5.9, p. 18.
  Exterior bases, functoriality and preservation of injections over
  fields support the existing annihilator convention. These apply to
  finite-dimensional spaces over F_97 and its extensions but give no
  bound for the intersection of the sixteen kernels.
- Lovett, MDS Matrices over Small Fields, FOCS 2018, Theorem 1.2,
  pp. 194–195 ([primary PDF](https://ieee-focs.org/FOCS-2018-Papers/pdfs/59f194.pdf));
  Brakensiek–Gopi–Makam, [arXiv:2206.05256v4](https://arxiv.org/html/2206.05256v4),
  Definitions 1.4/1.8, Theorem 1.12 and Corollary 1.15;
  Brakensiek–Dhar–Gopi, [arXiv:2310.12888v3](https://arxiv.org/html/2310.12888v3),
  Definitions 1.2/1.3/6.1, Theorems 4.1/6.4.
  Selectable or algebraically independent evaluation points and
  column-span intersection conclusions do not assert this exterior
  rank at prescribed H. The BDG Case 3 and full power-series proof
  remain unread and are not used. No generic specialization is made.
- [The overlap-factor assessment](2026-10-05-overlap-factor-universal-rank.md)
  records Gandini, arXiv:1810.11694v3, Theorem 1.1, Proposition 6.1,
  Theorems 7.3/7.5, and Boito–Ruatta, Extended companion matrix for
  approximate GCD, SNC 2011, section 3.2 Proposition 2/Corollary 1,
  p. 76. Characteristic-zero regularity and a single multiplication
  quotient's corank do not supply the required degree-two span over
  F_97. The optional Busé–Khalil–Mourrain lead remains unread and
  nonessential; no access retry is needed for this independent test.
- [The balanced-support assessment](2026-10-04-balanced-support-disjoint-triple.md)
  records Ihringer–Kupavskii, arXiv:1709.10462v3, Theorem 7 and proof,
  pp. 3/9; Füredi, J. Austral. Math. Soc. A 50 (1991), equation (2.1)
  and Theorems 3.3/4.3; and Ellis–Kalai–Narayanan,
  arXiv:1702.02607v8, section 4, p. 12, Lemma 4.1 and proof.
  These already distinguish regular intersection, fractional matching
  bounds and the translate construction from a forced disjoint triple.
  None supplies alternating rank or a classification of this family
  class. L023 already supplies the exact two-block specialization;
  it needs no reproof.

Hall's GRS distance input is already incorporated in L010's moment
independence and the two-block assessment. No distance or exterior
theorem is reproved. The previously reviewed graph/transversal method
still requires direct sums and graph isomorphisms not guaranteed by
these supports. Unread ABF26 definitions remain a separate main-goal
gap, rather than an essential prerequisite to testing the frozen matrix.

## Changed-scope searches and additional primary comparison

Queries issued October 6, 2026:

- `"exterior" "MDS" "hypergraph" rank`
- `"Reed Solomon" "exterior" "rank"`
- `"regular" "intersecting" "hypergraphs" "matching number" four`
- `"exterior algebra" "subspace arrangements" rank degree two`
- `"higher order MDS" "roots of unity"`
- `"regular" "4-uniform" "matching number" "2"`
- `"Vandermonde" "alternating" "subspaces"`
- `"exterior square" "hypergraph" rank matching`
- `"four-uniform" "four-regular" matching`
- `"4-uniform" "4-regular" "matching"`
- `"rational normal curve" "secant" "transversal" lines subspaces`
- `regular uniform hypergraphs small matching number fractional matching Furedi theorem`
- `"hypergraph" "exterior" "Lovasz" subspaces`
- `"four-uniform" "matching number two"`
- `"Regular Intersecting Families" arxiv Ihringer Kupavskii`
- `"Not-all-equal 3-SAT and 2-colorings" pdf Henning Yeo`
- `"exterior" "matching" "subspaces" Lovasz theorem`

Primary additional comparison (not imported): Alex Scott and Elizabeth
Wilmer, [Combinatorics in the exterior algebra and the Bollobás Two Families Theorem](https://people.maths.ox.ac.uk/scott/Papers/twofamilies.pdf),
author PDF dated May 11, 2021. Read the characteristic-zero scope on
p. 2; Theorem 2.3 and its initial-monomial proof, pp. 4–5; Lemma 3.4
and proof, pp. 16–17; Corollary 3.5 and proof, p. 17.
Theorem 2.3 bounds a self-annihilating homogeneous subspace by
binomial(n-1,r-1) for r<=n/2. Self-annihilation of the proposed kernel
is unproved. Lemma 3.4 bounds the maximum dimension fraction among
coordinate projections of a subspace in exterior degree r, with
0<r<=n-d. Corollary 3.5 obtains a projection bound on a nonempty
Zariski-open set of bases, using constant generic projection dimensions.
These conclusions do not prove injectivity of our prescribed stack.
The real/characteristic-zero scope also fails for F_97; no finite-field
extension of these theorems is asserted or needed here.

Other hits were screened as leads, not theorem evidence: Henning–Yeo's
four-regular four-uniform paper concerns two-colorability; perfect-matching
papers concern degree thresholds or fractional matchings; multipartite
Ryser results require additional partite structure and concern covers.
Those primary theorem statements were not inspected or imported. The
new regular-intersecting hit duplicates the saved Ihringer–Kupavskii
assessment. Secondary roots-of-unity claims, research-portal summaries
and rational-normal-curve existence snippets were not used as facts.
No essential matching rank theorem was identified behind those leads.
This bounded search neither proves novelty nor proves the proposed
universal statement false.

## Local duplicates and obstruction review

Read L010's hypotheses/conclusion, moment-kernel and eight-column
argument, and equality-incidence proof. Read L023/L024 in full;
L025's hypotheses, edge table, degree and matching proof; L027's
hypotheses/conclusion and quotient-map equivalence; L029's hypotheses,
matrix convention and quotient equivalence; L030's actual-moment bridge,
alternating expansion and completed audit cases. Reuse their ready
proof audits; no new critical audit or rank calculation is claimed.

L010 supplies the exact incidence conditions of equality, not matching
number two for every equality family. L023 meets the proposed incidence
and matching hypotheses on two eight-vertex blocks. L024 excludes that
family's affine-moment realization by coordinate root counting; it
does not state the full alternating stack's rank. Thus L024's conclusion
cannot be imported as the missing rank claim or as a rank-defect witness.
L027 and L029 establish rank 28 only for their displayed support patterns,
uniformly in labels. L030 separately checks actual full-weight errors,
finite parameters and every syndrome dimension for its application.
Neither new family coverage nor a universal theorem follows from them.

Read ATTEMPTS/016 and ATTEMPTS/017: balanced incidence does not force a
disjoint triple, and matching two does not force six edges on eight
vertices. Read ATTEMPTS/019 and L028's hypotheses, conclusions and
independent reconstruction passage. The saved 62 cyclic entries are
translation-orbit representatives, not pairwise nonisomorphic families
or an exhaustive list of arbitrary families. The exhausted seven-block
containment test adds no family and must not be repeated. A full-matrix
rank falsification test is a different mechanism; known 0125/0135
rank results are controls, not new advances. No certificate preview was
used as mathematical evidence and no cross-notebook input was read.

## One bounded continuation and decision test

The COVERED_TARGET above is ready for separate next-turn approval.
It tests the proposed universal assertion, retaining its fixed-H,
all-family and all-labeling quantifiers as the goal, without treating
finite positive tests as that assertion's proof. Use L010 and L029's
full six-by-28 convention for each support, and independent moment
nullspaces to validate any rank defect. L023/L024, L025/L027,
L028 and L029/L030 are essential examples, controls and scope limits.

In that later mathematical step, explicitly specify at most 256 distinct
admissible family/labeling pairs before testing. Include L023's two-block
family with labels on all sixteen vertices, and the proved 0125/0135
patterns as controls. Additional pairs may use the saved cyclic entries
or degree-preserving changes of supplied families, but check sixteen
distinct four-sets, sixteen vertex degrees four, a disjoint pair and
absence of every disjoint triple for each proposed family. Record
rejected candidate families and failed controls; do not quietly replace
the target by only cyclic families or promise an unavailable arbitrary-family
classification. No noncyclicity claim about the two-block example is
needed or certified by this review. Record complete labels, actual coverage and all tested
results. No family generation or mathematical script was run here.

Stop at a rank below 28. Independently reconstruct the full 96-by-28
matrix, verify all its entries and rank, and verify a saved nonzero
kernel vector against every row. A certified defect is an informative
negative result for the universal-rank mechanism and requires abandoning
that universal criterion, not declaring MCA equality or a disproof.
For rank-28 tests save exact rank certificates and the complete tested
input list. All positive tests leave the general theorem open; report
EXPLORATION and retain a concrete residual question instead of upgrading
samples to a lemma. A failed control stops the implementation inference.

Possible downstream use remains exclusion of the matching-two equality
branch through the audited alternating mechanism, conditional on a
future universal proof and a separate applicability check. Rank-defect
realization would still need decomposability, full weights, distinct
parameters and actual locator hypotheses. Larger-match families,
arbitrary disjoint triples, the global fifteen bound and ABF26
identification stay unresolved. No Mathlib matching coverage is claimed.
No new mathematical result, lemma or mathematical script was produced;
this literature step spends no mathematical exploration turn.
