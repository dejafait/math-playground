# 30 October 2026 — restricted local-density source replay

Completed the gate-approved k=2,c=1/4 audit as mathematical research.
[L485](../lemmas/L485-maples-rodgers-restricted-local-density-second-moment.md)
recovers exactly the known uniform indicator bound, with multiplicities
and strict source endpoints. It fixes the displacement and indicator
normalizations, bypasses general-weight (19), and replaces the false
far-tail convergence assertion by the estimate actually needed. The
complete proof and source qualifications are canonical there. This is
local progress by reproduction/repair, not a new density theorem.

No kernel estimate or mass saving was derived. The source arithmetic
inputs and Mathlib matching remain unaudited/unchecked. The new count
input warrants a separately reviewed comparison with L483's overlap
step; its variable widths, padding and endpoint conventions are outside
the completed audit's scope. The next assessment is REVIEW_REQUIRED.
The weighted-correlation gap still prevents a justified source-ready
creative target. Existing unfinished work and all prior stop evidence
are preserved. No mathematical scripts or cross-notebook inputs were used.

For the overview byte budget, the previous affected PROOF.md paragraph
is preserved here before its compact replacement and L485 addition:

> The regulator/response and selected-law results lack global realization and regulator-uniform signs. Unaudited L469 obstructs U'+CU>=0 for U=wD_1 with positive C^1 w and continuous C at multiple real zeros; simple zeros remain compatible. Unaudited L470 excludes finite homogeneous polynomial-coefficient linear ODEs for Xi. L471 gives a zero-safe majorant and only N(T)=O(T(log T)^3). L483 and C483a use cited density, shells and fourth moments to give B_{>=delta(T)}(T)=o(T(log T)^3), with delta(T)=100 log log T/log T and both density remainders retained. C483a and L483's shared kernel pass local audit; sources remain unaudited and the complementary sector open. L474 gives B_epsilon(T)<=C epsilon^3 T(log T)^3 (0<epsilon<=1). L476's h=(log T)^(-1/4) truncation error is O(T(log T)^(5/2)). Both retain multiplicities/endpoints and await audit; complementary and retained masses remain uncontrolled.
