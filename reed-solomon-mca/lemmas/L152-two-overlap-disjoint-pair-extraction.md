# L152 — Disjoint-pair extraction for the two-plus-two incidence family

## Hypotheses

Let H={1,8,12,18,22,27,33,47,50,64,70,75,79,85,89,96} and
S={1,8,12,18,22,27,33}. Put J=H minus S. Let E be a family of
m distinct four-element subsets of H, where 12<=m<=14. Assume:

- Every A in E has |A intersection S|=|A intersection J|=2.
- For distinct A,B in E, |A intersection B|<=1 (linearity).
- Each label x has degree d(x)=|{A in E:x in A}|<=4.

Isolated labels are allowed. Regularity, four-partiteness and a plane
embedding are not hypotheses. This is a pure incidence statement; no
moment feasibility or particular numeric support pair is assumed.

## Conclusion

There are distinct A,B in E with A intersection B empty.

This closes the stated incidence extraction implication only. It does
not identify the pair with any fixed pair excluded elsewhere, transport
moment exclusions to other labels, or prove universal representation or
the challenge. The argument below is a local SPECIALIZE result under
the prior assessment
`drafts/literature/2026-10-24-two-overlap-disjoint-pair-extraction-review.md`.
Classification: REPRODUCTION; no originality or progress beyond the
checked literature is claimed. The separate critical audit of 2026-10-25
passed at precisely this incidence scope; see the audit record below.

## Proof

Suppose instead that E is intersecting. By linearity every two distinct
edges now meet in exactly one label. All degrees below are relative to
this same E, with no deletion of edges; isolated labels remain permitted
in the ambient set H.

### Imported general bound and its exception

Import Z. Füredi, *Maximum degree and fractional matchings in uniform
hypergraphs*, Combinatorica 1(2) (1981), 155–162, Corollary 3, p. 158
([published scan](https://www.renyi.hu/~furedi/PUBS3/furedi_007_cca1981_fractional_matchings.pdf),
[DOI](https://doi.org/10.1007/BF02579271)). In its intersecting
r-uniform form, either the hypergraph is a projective plane of order
r-1, or its maximum degree is at least |E|/(r-1). The plane parameters
are r^2-r+1 edges and degree r; see p. 157. This is the primary
statement inspected in the prior assessment, not a newly reproved
general degree theorem.

For the source application take the vertex set to be H_active, the union
of the edges, and apply the corollary with r=4 to the unchanged family E.
It is finite, intersecting and four-uniform, and its maximum degree is at
most four. In the non-plane case this gives m<=12. The exceptional
order-three plane has thirteen edges and every vertex of H_active has
degree four. Reinstating H minus H_active adds only degree-zero labels;
neither the edge count nor any active degree changes. Since every edge
has exactly two labels in S, double counting incidences with S in that
exception would give

    26 = 2m = sum_(x in S) d(x) = 4 |S_active|,

where S_active consists of the nonisolated labels of S. This is
impossible over the integers. Thus the exception cannot occur, m=13
and m=14 are excluded, and it remains to exclude m=12. Neither a
regularity assumption for that boundary case nor a plane embedding is
imported from the citation.

### Degree pattern at the twelve-edge boundary

Fix an edge A. Every other edge meets A once, so counting pairs
(x,B) with x in A, B different from A, and x in B yields

    sum_(x in A) (d(x)-1) = 11,
    sum_(x in A) d(x) = 15.

There are four summands, each at most four and each a positive integer.
Consequently their deficits from four sum to one: each edge contains
exactly three degree-four labels and one degree-three label. In
particular every nonisolated label has degree three or four.

Write V_3 and V_4 for these two sets of labels, and n_i=|V_i|.
Counting incidences first with V_3 and then with V_4 gives

    3 n_3 = 12,       4 n_4 = 36.

Thus n_3=4 and n_4=9. These are consequences, not assumptions about
the number of active labels. The remaining three labels of H may be
isolated.

Let a=|S intersection V_3| and b=|S intersection V_4|. Every edge
has two labels in S, hence

    3a + 4b = 24,       0<=a<=4.

Reducing modulo four forces a to be zero or four. Solving for b gives
exactly (a,b)=(0,6) or (4,3). In the first case J contains all four
degree-three labels and exactly three degree-four labels; in the second
case S does. Therefore one of the two parts, call it P, contains all
of V_3 and exactly three labels of V_4. Isolated labels in either part
do not enter any of these counts.

### Pair saturation contradicts the partition

Each edge contains three labels of V_4 and therefore accounts for
three unordered pairs in V_4. No such pair can occur in two different
edges, since that would violate linearity. The twelve edges thus
account for 12*3=36 different pairs. There are exactly
choose(9,2)=36 pairs in V_4. Hence every pair in V_4 occurs in an
edge of E, exactly once.

Choose two of the three labels in P intersection V_4. Their containing
edge also has its unique label in V_3, which belongs to P. This edge
therefore has at least three labels in P, contrary to the hypothesis
that every edge has exactly two labels in each part. This excludes
m=12 and completes the contradiction. A disjoint pair must exist.

### Scope and downstream qualification

The citation supplies the general degree bound and its exceptional
case; the proof supplies the partition-sensitive twelve-edge boundary
and the incidence obstruction to the exceptional partition. This is
the difference approved by the SPECIALIZE assessment, not a reproof
of the general theorem. The proof uses no numerical experiment or
classification of planes and does not assume that the boundary family
embeds in a plane. All 12–14 admissible edge counts have been addressed.

For prospective use on an equality pencil, L086 and L109 are context,
not premises of this abstract lemma: they supply necessary incidence
conditions and the 12–14 count only under their full coding hypotheses.
Those hypotheses and their finite-certificate qualifications must be
retained in any later application. No such application or uniform
pair-exclusion theorem is asserted here. The earlier stopped
disjoint-triple, small-union and useful-pair mechanisms in
ATTEMPTS/016,017,027 remain stopped for their stated implications.

### Independent critical audit, 2026-10-25

Verdict: **PASS for the stated abstract incidence implication only**.
The approved audit reused the primary inspection recorded in
`drafts/literature/2026-10-24-two-overlap-disjoint-pair-extraction-review.md`
and its separately approved critical-audit scope. No new general theorem
or source hypothesis was needed. The source application above was made
explicit on H_active; this is a clarification, not a changed hypothesis.

The audit checked that the non-plane and plane alternatives exhaust
m=12,13,14, with no lost isolated-label case; that the fixed-edge count
uses each other edge exactly once; that every active label must have
degree three or four; and that the two solutions for (a,b) exhaust the
integer equation with 0<=a<=4. Their active part sizes are respectively
6 and 7, or 7 and 6, and neither requires all ambient labels to be active.
Pair saturation uses injectivity from linearity as well as equal finite
cardinalities. The final edge contains three distinct labels of P: its
two chosen degree-four labels and its degree-three label. No case was
omitted and no substantive mathematical error was found.

All evidence needed for this verdict is the exact proof above and its
precise imported theorem; no numerical certificate or formal verification
is claimed. The audit neither applies the lemma to a coding family nor
transports a numeric-pair exclusion. No local lemma is a mathematical
input, so the existing empty L152 DAG row remains correct.

## Mathlib

Full matching coverage for this partition-sensitive implication and
Füredi's cited corollary: **not checked**. Supporting finite-incidence
and finite-set counting coverage: **not checked**. No library absence
or formal verification is claimed. The proof is an informal exact
counting argument with a precise imported general theorem.
