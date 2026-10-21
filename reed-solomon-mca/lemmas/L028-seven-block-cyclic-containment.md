# L028 — Exact seven-block containment in the saved cyclic families

## Hypotheses

Let V=Z/16Z. For a four-subset A of V put
F_A={A+t:t in V}. Consider only families with sixteen distinct edges and
matching number exactly two. Choose one seed per translation orbit by
minimizing the integer mask sum_(v in A) 2^v. This is a representative of
seeds under translation, not a representative under arbitrary vertex
isomorphism. These are exactly the 62 entries of L025's certificate
`scripts/small-union/cyclic-orbits-result.json`, as independently checked
below. Let I_t={t,t+1,t+2,t+5}, for 0<=t<=6, be L027's first seven
supports; their union is {0,...,11}.

A copy means one injective map f:{0,...,11}->V for which every f(I_t)
is an edge of F_A. Edge images must be exact four-element edges, rather
than arbitrary intersections or independent choices of vertex maps.

For the syndrome consequence, let F be any extension of F_97, let H be
the order-sixteen subgroup of its prime subfield, label all sixteen
vertices bijectively by H, and use L027's moment map. Every prescribed
error has all four support weights nonzero.

## Conclusion

Exactly eight of the 62 recorded families contain a copy. Their canonical
seeds and explicit witnesses are the following; f(i)=a i+b modulo sixteen
on 0<=i<=11. The map g(i)=a i on all sixteen vertices is a full
isomorphism from L025's family F_{0125} to the indicated host.

| Seed mask | Canonical seed A | a | b |
| --- | --- | --- | --- |
| 39 | {0,1,2,5} | 1 | 0 |
| 57 | {0,3,4,5} | 15 | 5 |
| 147 | {0,1,4,7} | 3 | 1 |
| 201 | {0,3,6,7} | 13 | 6 |
| 549 | {0,2,5,9} | 7 | 2 |
| 657 | {0,4,7,9} | 9 | 7 |
| 1059 | {0,1,5,10} | 11 | 10 |
| 1569 | {0,5,9,10} | 5 | 0 |

The other 54 families contain no copy. The negative assertion uses the
complete exact finite certificates and algorithms below. All eight
positive entries therefore represent the already excluded abstract
family, rather than eight distinct isomorphism classes or an additional
RS exclusion. No pairwise nonisomorphism assertion is made about the
remaining entries.

More generally, any sixteen-vertex family containing these seven blocks
cannot support full-weight errors with syndromes on a single affine
pencil, under any bijective labeling by H. This applicability statement
imports L027's proved seven-block obstruction. In this finite test it
excludes only the eight positives, which were already covered up to
isomorphism. The 11/q–16/q interval and the global fifteen-count gap are
unchanged; cyclic families are not assumed exhaustive among equality
families, and ABF26 correspondence remains unresolved.

## Proof

### Independent reconstruction of the input scope

The verifier starts from all binomial(16,4)=1820 four-subsets as actual
sets. For each remaining seed it constructs all sixteen translates by
set addition modulo sixteen, removes that entire orbit, and repeats.
Two translation orbits are either disjoint or equal, so this partitions
the seeds exhaustively. Within each orbit the minimum integer mask is
chosen and all edges are sorted by mask. The independent reconstruction
gives 116 translation orbits: one of size four, three of size eight,
and 112 of size sixteen. It compares every reconstructed orbit record
with the saved record, including every full-orbit degree and the counts
of disjoint pairs and triples. For every full orbit each vertex has
degree four, also following directly because precisely the four shifts
v-a, a in A, contain vertex v.

For each full orbit all 120 pairs and all 560 triples are inspected by
set disjointness. Having a disjoint pair and no disjoint triple is
equivalent to matching number two: any matching of size at least three
contains a disjoint triple. Exactly 62 full orbits meet this condition;
the other 50 contain a disjoint triple. Every one of the 62 saved seed,
edge-mask, complete edge-list, degree, pair/triple-count and disjoint-pair
witness fields is compared with this reconstruction. All comparisons
pass. The unrelated six-edge union histograms and minima are not inputs
to this theorem and are not asserted independently verified here.

### Exhaustive containment certificate

Number the sixteen host edges 0,...,15 in mask order. A vertex injection
would send distinct pattern edges to distinct host edges. Since host
translations act transitively on its edges, composing any such injection
with a translation normalizes its I_0 image to host edge zero. This is
solely an abstract combinatorial automorphism, with no symmetry
assumption on H-labelings or error weights.

For an ordered k-tuple of distinct selected host edges, compare the
cardinality of every nonempty intersection with the same intersection
among I_0,...,I_(k-1). Equal edge images under an injection force these
equalities. They are also sufficient for partial incidence equivalence.
Indeed for each nonempty S subset {0,...,k-1}, the number of vertices
lying in exactly the edges indexed by S is

\[
 n_S=\sum_{T\supseteq S}(-1)^{|T\setminus S|}
             \left|\bigcap_{t\in T}E_t\right|.
\]

This follows by summing, for each vertex belonging to all S, the
indicator product over the remaining edges that it does not belong
to them. The empty incidence class has size sixteen minus the sum of
the nonempty class sizes. Consequently matching all nonempty
intersection cardinalities gives identical incidence class sizes on
the two sixteen-vertex universes. Bijections within corresponding
classes then send every selected pattern edge to its selected host
edge. At depth seven, restriction to the twelve vertices in the pattern
union is exactly the required injection.

The search starts with the complete normalized prefix list [[0]]. At
each subsequent depth it tries every host edge index not already in
the prefix. Previous intersection constraints have already been checked,
so it checks all subsets containing the new edge. The list retained is
exactly the prefixes satisfying all intersection constraints. Induction
on depth proves exhaustiveness: every normalized embedding restricts to
a retained prefix, and every possible extension of every retained
prefix is tried. The certificate stores every retained prefix at all
seven depths for each family, even after a list becomes empty.

The independent verifier neither imports this search nor uses its
intersection routine. At every proposed extension it directly computes
the incidence signature of every one of the sixteen vertices: a bit
records membership in each selected edge. It compares the complete
signature-count histogram with that of the corresponding pattern
prefix, including signature zero. It tries every available index at
every independently retained prefix, stores every trial, and for each
rejection records a signature whose actual and required counts differ.
Its complete retained-prefix lists equal the search lists for every
family and depth. Thus a final empty list certifies noncontainment;
the computation involves no timeout, heuristic, or sampled mappings.

The combined counts of retained prefixes at depths one through seven
are 62,114,104,16,8,8,8. There are 4300 candidate checks including the
62 normalized roots. Eight families have one final prefix each, and
the other 54 have none. The exact eight seeds are displayed above.
For each positive the search matches vertices within equal incidence
classes; the independent verifier checks the twelve-element domain,
injectivity, and all seven complete edge images. The stored maps are
precisely the f displayed in the table. It additionally verifies the
full bijection g and equality of all sixteen image edges with the host
edge set. These full witnesses, rather than the absence of a map in
any restricted isomorphism search, prove all eight hosts isomorphic
to F_{0125}. Odd a makes each displayed affine map injective modulo
sixteen; the edge-set equality is checked explicitly for g, and the
host's translation invariance also preserves it upon adding b.

Reproduction commands from the active notebook root are
`python3 scripts/small-union/seven_block_containment.py` followed by
`python3 scripts/small-union/verify_seven_block_containment.py`.
The first writes `scripts/small-union/seven-block-containment-result.json`;
the second writes
`scripts/small-union/seven-block-containment-verification.json`.
The latter contains the entire independently reconstructed orbit record
list, every qualifying edge set, every prefix list and extension audit,
all positive maps and all full-isomorphism witnesses. Its summary reports
62/62 required families verified, eight positives, 54 exhaustive
negatives and no failures. The complete positive-witness field and
summary were inspected; every trial and source edge list is checked by
the independent verifier. The correctness argument above explains why
the finite algorithms certify the claimed scope; this remains an exact
computational proof with the stated reproducibility dependency, not a
Lean-formalized certificate or a theorem about arbitrary support families.

### Applicability of the seven-block obstruction

Let f be any copy in any sixteen-vertex host with labeling lambda_host.
On {0,...,11} put lambda(i)=lambda_host(f(i)). This is injective into H.
Extend it to a bijection from all sixteen pattern vertices to H by
assigning the four unused elements to the four remaining vertices.
The extension choices do not change the seven selected blocks.

L027 proves that those first seven blocks alone have rank 28 for every
such labeling, using only independence of eight distinct moment
columns. Its proof does not use supports eight through sixteen. For
actual errors on the selected blocks, pi_t(u)+gamma_t pi_t(v)=0 makes
u wedge v vanish in all seven quotients; rank 28 forces u and v
dependent. Each full-weight four-coordinate error has nonzero syndrome
by independence of its four moment columns. Thus a nonzero
one-dimensional span{u,v} would be contained in every selected support
span; a zero-dimensional span is already impossible. I_0 and I_6 are
disjoint, and their eight independent moment columns make their spans
intersect trivially. This excludes the dependent case as well.

This is the necessary restriction of L027's audited argument, rather
than an assumption that the remaining nine host edges are L025's edges.
It requires neither distinct gamma_t nor locator nonpersistence. In
particular L010 equality supplies the full-weight errors and common
affine syndromes needed for this obstruction, as verified in L027's
audit. No label automorphism, cyclic weight shift, or extension-field
sampling is used. The finite outcome here reaches only the already
excluded isomorphism class, so further testing this same pattern on the
same 62 entries has no remaining discriminating target.

### Source qualification

The pre-invocation EXPLORE assessment
`drafts/literature/2026-10-05-seven-block-pattern-coverage.md` covers
exactly this containment test, independent enumeration checks and the
seven-block applicability argument. Its inspected graph-matching
documentation supplies possible machinery, not these list-specific
answers. No external graph-matching theorem or library is imported or
reproved: the elementary exhaustive algorithms are justified above.
L025 supplies the recorded scope, and L027 the already audited moment
obstruction. The containment answer is local information beyond the
inspected source conclusions, without a certified originality claim or
additional progress on the sharp global error bound.

## Mathlib

Coverage of this exact finite containment characterization is **not
checked** in Mathlib. No matching theorem, absence claim or Lean
verification is asserted. Supporting moment and exterior-algebra
coverage retains the qualifications in L027; no new library theorem is
an essential premise of the computation.
