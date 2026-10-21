# Source assessment for the seven-block pattern search

TARGET: Determine exactly which of the 62 full-orbit matching-number-two cyclic families recorded in L025's certificate contain a vertex-relabeled copy of L027's first seven supports.
CHECKED: 2026-10-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Targeted local duplicate searches and October 5 exact-pattern, cyclic matching-two and hypergraph-subgraph searches found no inspected result answering the saved 62-family containment question; queries and primary algorithm documentation read are recorded below.
SOURCE_EVIDENCE: Read L025's enumeration qualifications, L027's hypotheses and support-exclusion argument, the cyclic-orbit generator, NetworkX 3.7 VF2 documentation (Introduction, Subgraph Isomorphism, Graph Matcher), and igraph C manual Chapter 21 sections 1.1–1.2; reuse the saved arbitrary-label and critical-audit assessments for the moment obstruction.
COMPARISON: Known graph-matching methods supply finite search machinery, not the answers for these notebook-specific families; L027 supplies the audited obstruction while L025 supplies a translation-orbit list, with neither establishing containment or nonisomorphism.
GAP: Exact containment results, independent enumeration verification and the local seven-block applicability argument remain to be established in the mathematical step; no inspected source gives the desired family-by-family certificate.
REASON: Essential coverage now supports one bounded exact containment attempt; the question is finite and local, and no external uninspected theorem is an essential premise. Failed searches do not certify novelty.
SCOPE: Only injective seven-edge containment in the recorded full-orbit matching-two cyclic families, verification of that list and applicability of audited L027; no new support obstruction, arbitrary-family classification or H-label sampling.

## Bounded target and verification requirements

Essential inputs are L025's recorded family construction in
`scripts/small-union/cyclic-orbits-result.json` and the first seven
supports of L027. Read only the relevant complete family data when this
mathematical step starts. The number 62 is taken from L025's report; this
continuation has not independently revalidated that enumeration or
asserted that the recorded entries are pairwise nonisomorphic.

A copy means one injective assignment of the pattern's vertices to the
sixteen family vertices carrying each of its seven four-element edges
onto an edge of that family. It is not seven unrelated edge matches or
a symmetry reduction on H. A verified copy would allow the audited
obstruction to exclude the containing family under every H-labeling.
This implication requires a local applicability argument at that stage,
including full-weight syndromes and the disjoint pair; it is not a new
lemma established in the present audit.

The discriminating test is exact containment for each recorded family,
with explicit injective maps for positive cases and a complete, checkable
finite exclusion for negative cases. Continue this mechanism if it
certifiably excludes an additional abstract family. If it reaches only
families already isomorphic to L025's, retain that coverage limit and
choose a different support pattern or obstruction. Do not repeat H-label
sampling. The failed universal six-edge/eight-vertex criterion in
ATTEMPTS/017 is not being reinstated.

Remaining assumptions are exactness of the saved enumeration, correctness
of the containment evidence and applicability of L027 to a containing
family. No claim is made that the cyclic list exhausts arbitrary balanced
families. Other equality configurations, the global fifteen-count bound,
and ABF26 identification remain unresolved. The unchanged exact target is ready for a subsequent mathematical attempt;
this literature turn has performed no containment calculation.


## Changed-scope source and duplicate comparison

This is a literature-only review because the previous turn explicitly
left the new target uncovered. The balance exception is essential
changed-scope coverage, not another audit of the ready fixed-family theorem.
No lemma, mathematical script, or numerical certificate was written or run.

Local searches covered L025 and L027, the seven-block assessments,
`scripts/small-union/`, ATTEMPTS/017 and the directly relevant histories.
The generator records translation representatives and qualifying edge sets;
it has no seven-edge containment or hypergraph-isomorphism test. This is
source inspection, not independent verification of its counts. The complete
family data remain for the mathematical turn; 62 is still a reported count.
The prior arbitrary-label assessment is reused for its generic-MDS versus
fixed-H comparison, and the critical-audit assessment for L027. No renewed
MCA/ABF26 source search is needed for this finite combinatorial question.
ATTEMPTS/017 stops the universal small-union criterion, not this test.

Queries on 2026-10-05 were:

- `hypergraph subgraph isomorphism incidence graph edge vertex colors monomorphism VF2`
- `"cyclic" "16" "matching number" "four" hypergraph`
- `"Reed Solomon" "seven" "supports" exterior algebra`
- `"hypergraph" "0,1,2,5" "16"`
- `"cyclic" "4-uniform" "matching number two"`

No inspected hit answered the exact local family question. Matching/cover
and generic RS leads do not supply this list-specific containment output.
No novelty follows from those search results.

The primary [NetworkX 3.7 VF2 documentation](https://networkx.org/documentation/stable/reference/algorithms/isomorphism.vf2.html),
read on October 5, distinguishes node-induced subgraph isomorphism from
non-induced monomorphism. GraphMatcher takes the host first and pattern
second, and exposes mapping iterators and semantic matching. Its default
semantic check imposes no colors; an implementation must enforce the
vertex/edge-node types if using incidence graphs. It cites Cordella,
Foggia, Sansone and Vento, *A (Sub)Graph Isomorphism Algorithm for Matching
Large Graphs*, IEEE TPAMI 26(10), 1367–1372 (2004); that paper was not read
and is not imported as a correctness theorem. These are interface facts,
not certification of a future computation.

The primary [igraph C Reference Manual, Chapter 21, sections 1.1–1.2](https://igraph.org/c/html/latest/igraph-Isomorphism.html),
read on October 5, defines graph isomorphism by a one-to-one vertex mapping
and documents subisomorphism with the larger graph first, equal directedness
and simple-graph restriction, with exponential complexity. This confirms
availability of standard exact matching machinery; it provides neither the
62-family output nor an RS theorem. No installed library version was checked.
The nauty 2.9 guide and Boost documentation open attempts failed; these
optional algorithm leads are not essential sources or mathematical inputs.

A future incidence-graph implementation must justify that its chosen
matching semantics are equivalent to the exact injective hyperedge test;
that reduction is a verification obligation, not a new result proved here.
A direct complete assignment search is also within scope. For positives,
store the map and independently check all seven image edges. For negatives,
retain a complete reproducible exhaustive certificate, not a timeout or
absence of sampled matches. Independently reconstruct the qualifying
translation orbits and verify their matching categories before relying on
coverage of all reported 62 entries. Translation representatives are not
claimed to be hypergraph-isomorphism representatives.

The downstream implication also requires a local proof: inspect L027's
seven-block argument, account for its original full-family hypotheses,
extend any partial injective labeling to the sixteen labels, and verify
that the rank and dependent-direction exclusion use only the selected
seven blocks with full-weight errors. This implication is proposed, not
derived during review. Any newly proposed obstruction outside this scope
requires another assessment. Mathlib coverage of exact containment is not
checked; no Mathlib theorem is needed as a premise for this source review.
