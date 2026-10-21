# Small-union cyclic test — working record

Approved input assessment: drafts/literature/2026-10-05-matching-two-small-union-criterion.md (EXPLORE, unchanged target).

The main mathematical gap is L010's possible sixteen-count equality;
the current interval is 11/q–16/q and the allowable count is fifteen.
The intermediate target asks whether every simple sixteen-edge,
sixteen-vertex, four-uniform degree-four family of matching number two
has six distinct edges with union at most eight. Such a configuration
might support an affine-restriction argument analogous to L024, but that
implication is unproved and is outside this test. L023 already blocks an
incidence-only disjoint-triple reduction; L024 excludes its exact family,
not all matching-two families. Their full proofs and ATTEMPTS/016 were
checked before work. No existing small-union calculation was found in
the targeted notebook search.

Bounded attempt: enumerate all four-element seeds in Z/16Z, keep one
representative per translation orbit, and retain only full sixteen-edge
orbits. Verify all vertex degrees, every disjoint triple, and a disjoint
pair. For each qualifying family, examine all 8008 six-edge subsets and
record the complete union-size histogram and a minimum-union witness.
Preserve complete qualifying edge lists and counters in a disk certificate.
Independently verify the retained cases using set operations and all
six-edge subsets, and reconstruct the entire seed coverage.

Continuation/abandonment test: a fully verified family with minimum
six-edge union at least nine refutes the universal criterion. A complete
cyclic search without such a family exhausts this restricted search only;
the universal assertion and any RS application stay unresolved, and
further work requires a concrete noncyclic or structural target and its
separate assessment. No cyclic reduction is assumed. Essential downstream
inputs are L010, L023 and L024; the incidence calculation itself has no
local lemma input. Arbitrary-support and arbitrary-triple reductions,
affine-moment compatibility and ABF26 correspondence remain independent
unresolved assumptions.

Completed: the generator enumerated 1820 seeds and 116 translation
orbits, including 112 full orbits. Of 62 full orbits with matching number
two, 56 are counterexample candidates. The selected seed {0,1,2,5}
was independently verified using all 560 triples and all 8008 six-edge
subsets; its minimum union is eleven, exceeding the required nine.
The complete selected checks, edges, histogram and minimum witness were
inspected. Full certificates are in scripts/small-union/; the canonical
proof in L025 establishes the needed exclusion of unions at most eight
by elementary cyclic-gap counting, without computational dependence.

Decision: abandon the universal incidence criterion (NEGATIVE).
The original target is false; no RS pencil or global bound is obtained.
The next independent compatibility target is specified, with essential
inputs and unresolved qualifications, in
drafts/literature/2026-10-05-cyclic-0125-affine-compatibility.md and is
REVIEW_REQUIRED. No mathematics for that changed target was attempted.
