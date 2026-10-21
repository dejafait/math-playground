# Critical audit of the fixed cyclic 0125 exclusion

The approved target and assessment are unchanged. This turn audits L026,
using only L010's moment columns and L025's prescribed supports and disjoint
pair. The unresolved main gap is arbitrary sixteen-count equality supports;
the intermediate target is a verified fixed-family obstruction. Its downstream
use is to eliminate the canonical cyclic labeling without conflating it with
arbitrary labelings or a global fifteen bound.

Initial proof inspection: the annihilating rows have the correct one-index
moment offset; expanding their two-by-two products gives L026 (1). Dividing
by the row-dependent nonzero scalar leaves powers indexed by j+k, from one
through thirteen. Sixteen distinct subgroup elements therefore separate all
blocks over any extension. The dependent-direction case uses nonzero sparse
syndromes and the disjoint pair, including the zero-direction case.

Bounded test: independently reconstruct all 104 small minors and
check both printed tables against the saved certificate. Rebuild annihilators
as nullspaces of the actual four moment columns, without importing the
generator script; their alternating constraints must again have rank 28 for
each of eight generators. Inspect extension-field and equality applicability
separately. Retain L026 if all checks pass; correct or withdraw its exclusion
if a load-bearing equation, table value, field passage or case fails. No
new support family or labeling is tested during this audit.

Completed: all checks passed. The canonical audit discussion and its
qualifications are in L026; the full independent certificate is
`scripts/cyclic-0125/alternating-obstruction-audit.json`. It reports all
104 nonzero minors, ranks 28 for all eight independent nullspace
constructions, and no failures among 743 checks. No error repair, new
lemma, stronger bound or certified originality is claimed. This is a
REPRODUCTION audit, recorded conservatively as EXPLORATION because it
adds an independent check without a new mathematical conclusion.

The fixed-label route is audited and complete. A separate proposed
continuation asks whether the same full-rank criterion holds under every
bijection of the abstract vertices with H. That universal rank claim is
not established here; a single deficient labeling would refute the
criterion without establishing a realizable equality pencil. It lies
outside the saved cyclic-label scope and requires literature review.
