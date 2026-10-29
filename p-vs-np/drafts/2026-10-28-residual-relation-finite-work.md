# Step 542 — finite residual-relation attempt

The supplied overview/DAG and ready EXPLORE assessment were read before
this research step. Preserve all earlier notebook changes. The target is
the assessment's exact joint generator/shift/occurrence/boundary target.
No external source refresh or cross-notebook input is needed.

Main gap: uniform P versus NP remains open. Intermediate target: the full
original-coordinate relation E_N on the dyadic path family, beginning at
N=4. A joint linear bound could help the unary fourth comparison; it
would leave all independent reception and complexity gaps unresolved.

Bounded test: enumerate the entire 15-dimensional candidate relation at
N=4 after checking its rank, select a minimum-total-support basis, and
check every shift and boundary coordinate. Test whether its literal
shift digraph is acyclic. If necessary, charge an explicit finite
nilpotent-orbit realization instead of treating a nilpotent matrix as an
acyclic graph. This fallback would establish finite feasibility only.
Continue toward a uniform claim only with a concrete scaling mechanism;
reject any failed map equation or claimed linear construction with a
proved superlinear cost. Finite search failure is not a universal stop.

Local inputs read: L110 §4; L122 hypotheses and §§2,4–5; L123 hypotheses
and §§4–5; Attempts 056/057. They stop their specified lifts, not freely
chosen relation bases. Existing graph/matrix helpers will reconstruct
the original endpoints, retaining every zero-residual and final coordinate.
This paragraph was saved before calculation; completed results follow.

## Completed finite result

The canonical proof is L124. Its full explicit table gives a basis of
the whole E₄, not merely paired reachable rows. All original zero-residual
directions and final coordinates remain present. Exhaustion of 32768
vectors proves finite minimum total basis support 37. The complete shift
has 24 entries and its literal digraph is acyclic. Both original initial
rows have common coordinates c=e0+e1+e3+e14; the common final functional
is d=e7. Adding the actual constant boundary edges requires removing the
two internal final entries from the endpoint maps and adding the two
fresh terminal entries. The full maps still span E₄ and have support 37.

The first receipt used a valid but unnecessarily large orbit-unrolled
graph (137 vertices/140 occurrences/maps 163), preserved at
`scripts/batched-incidence/output-542/residual-relation.json`.
The acyclic shift permits the direct graph instead: 17 vertices,
29 occurrences, g(Q)=75, 2g(Q)=150, endpoint supports 24+13=37, S=84.
Its complete certificate is
`scripts/batched-incidence/output-542-direct/residual-relation.json`.
The separately implemented audit reconstructs closures via matrix powers
rather than the generator's occurrence sweeps, checks every vector and
all map equations/boundaries, and writes
`scripts/batched-incidence/output-542-direct/audit.json`. No failures.

This is a local finite advance. The minimum applies only to E₄ generator
support, not to optimal realizations or all dyadic N. The literature
assessment found no exact joint match; this does not certify originality.
The qualitative common-source theorem is imported by precise citation
in L124; no general existence theorem is reproved. Mathlib matching
coverage is not checked.

No uniform mechanism has been proved. A prospective mechanism is dyadic
Pascal-block gluing of the full generators, with the actual N=8 equations
as the next discriminant. Expanded generator entries, shift edges and
boundary additions must all be charged: an O(N) new charge at every
doubling does not by itself give O(N) total support. Failure of a proposed
recursion rejects that proposal, not the exact target. The sole current
next action and routing remain in PROGRESS.md.
