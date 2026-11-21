# Step1641 — 19 November 2026

Completed the approved mathematical reproduction of assessment1640.
[C048g](../lemmas/C048g-mellin-full-theta-right-ray-allowance.md)
proves absolute convergence of the complete full-theta right ray and
its exact A_+ L^(9/2)/r allowance on C048c's closed sector. The
negative-real-part phase case is explicit. This is local progress in
reproducing Kawano's source component, with no progress beyond the
checked source claim and no RH candidate.

The exact-rational scalar certificate
`scripts/mellin-horizontal-local/right_ray_constants_1641.json`
records 13 passing comparisons and no failures; its rigorous outward
coefficient interval is (0.096513538928204,0.096513538928205), below
0.096514. The full proof, source citations, qualifications and Mathlib
status are canonical in C048g. Working reasoning was saved before the
certificate and final proof in drafts/mellin-full-theta-right-ray-working-1641.md.

The new DAG row records only C048c and L799 as direct mathematical
inputs: the former supplies sector geometry and branches, the latter
the general strip-series identity. L801 was only an overlap contrast;
C048f's notation is explicitly defined, and its finite bound is unused.
No finite local estimate was assumed to extend to the ray.

Route decision: nominate the separate conceptual audit in
[assessment1641](../drafts/literature/2026-11-19-mellin-right-ray-conceptual-audit-1641.md).
It reuses ready coverage but is newly written, so separate next-turn
approval remains required. Left tails, global assembly, zero counts,
inversion and sufficient actual-Xi signs remain open. The global-import
stop is preserved. There is no concrete independent central sign test
to justify creative routing; the analytic audit takes priority.

Outcome ADVANCE means a relevant reproduced input, not a new theorem
beyond the inspected source. No mathematical EXPLORATION attempt was
spent. Existing unfinished notebook work was preserved; no shared or
runtime state, scheduler counters, credentials or commits were changed.

Scoped documentation validation first found PROOF.md 32 bytes over its
8192-byte limit after the new sentence. Shortened that sentence without
changing its claim; all mathematical details remain canonical in C048g.

Validation after the wording repair: the scoped structure checker passed
(1443 nodes, 3536 unique edges, acyclic, complete coverage and valid links);
scoped git whitespace checks passed. The Next action exactly matches the
new NEXT_REVIEW target. These process checks do not replace the pending
independent conceptual audit.
