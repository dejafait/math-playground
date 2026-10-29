# Complete cubic asymptotic: one bounded mathematical attempt

Started 2026-10-26 under the supplied prior EXPLORE assessment
`literature/2026-10-26-complete-cubic-quadratic-asymptotic.md`.
The exact registered target is the complete N^2 cubic asymptotic and
comparison with L285(4). Existing unfinished files are preserved.

Main gap: construction of the interacting continuum theory and a finite
positive mass. Intermediate target: all five terms of L280(20), with a
full o(N^2) remainder or a rigorous scale obstruction. Downstream use:
compare the missing cubic contribution with the audited quartic/density
coefficient; subleading control and uniform higher remainders remain
independent gaps. Continue only with a controlled complete subfamily or
summed error; no bulk fit or unestimated internal tail proves the limit.

Inputs inspected: L279's all-link jets through L280, L280(18)–(23),
L003's exact relative modes and time Green kernel, L281's tail scope,
L284's separated edge-to-12-plaquette kernel, and L285(4), (7)–(12).
Reused the completed source comparison and its exclusions; checked
ATTEMPTS/047–049 and the selected recent cubic/quartic work notes.
The old Ward observable and generic gauge-identity mechanisms are not
inputs. No additional primary theorem or mathematical script is needed.

Work in progress: the insertion–insertion term has two separated 12
vertices. The cubic Wilson polynomial factors as a linear curl times a
local quadratic commutator. Its fully crossing Gaussian pairings should
then contain either a curl–curl line and two edge lines, or two curl–edge
lines and one edge line. Seek uniform bounds O(a^4), O(a^3), O(a^2),
respectively, giving O(a^8) per vertex pair and O(1) after the complete
O(a^-8) source-pair sum. The transverse edge bound needs the longitudinal
B Delta^-2 B* subtraction explicitly; scalar replacement is not valid.
This paragraph is a plan, not a proved estimate. The other four cubic
groups have unrestricted action vertices and are not covered by source
separation. No N^2 scale or compensation is assumed for them.

## Completed result and unfinished remainder

The estimate proposed above is now proved in
[L286](../lemmas/L286-cubic-insertion-pair-separated-bound.md).
It controls the entire insertion–insertion group by O_f(1), so its
N^-2 contribution is zero. The proof retains the longitudinal
B Delta^-2 B* correction using a differentiated exact time resolvent;
all spatial modes have a uniform summable separated majorant. Each
Wilson cubic vertex supplies an exact curl, yielding O(a^8) per pair
before the full O(a^-8) source-pair sum. This is an analytic estimate;
no numerical certificate or finite-data extrapolation was used.

The complete target is unfinished. L286(2) records the exact four
remaining groups and L286(3) their comparison with L285(4). The local
polynomial approximations available for quartic contractions do not
supply a pair-summable error here. For any fixed lattice-distance
cutoff, the insertion pair lies wholly in the distant tail for large
N; L286 controls that tail directly. No estimate of the other four
internal tails or their boundary sums is asserted. No compensation
or N^2 scale for the remaining response is presumed.

Continue the same already approved target with derivative-weighted
vertex-pair estimates for the remaining mixed and action groups.
Do not repeat bare uniform-entry replacement or global norm estimates.
The discriminating threshold remains a complete o(N^2) discarded-pair
error (or an informative rigorous scale obstruction). A further complete
subfamily bound is partial progress only. L286 has no separate critical
audit yet; its new normalizations and all dependencies remain explicit.
This is one mathematical attempt and a local ADVANCE, not a claimed
advance beyond all published results or a continuum candidate.

Verification: checked the cubic trace coefficient against the ordered
Wilson expansion, the 6/36 crossing multiplicity, the counting/physical
measure factors in both terms of the transverse kernel, and the complete
a^8(N+1)^8 source-pair count. Reviewed the five direct mathematical inputs
of the new DAG row; L285 is used only for the final comparison. The scoped
documentation checker passes (297 nodes, 1760 edges), and scoped diff
whitespace checking reports no errors. These checks are not a separate
critical mathematical audit. No mathematical script was run.
