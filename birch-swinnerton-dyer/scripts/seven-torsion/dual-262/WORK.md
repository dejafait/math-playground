# Approved bounded attempt — 2026-10-16, step 262

Target is the exact TARGET of drafts/literature/2026-10-16-explicit-dual-kernel-algebra.md (SPECIALIZE at invocation start). Main gap: arbitrary analytic-order-at-least-two rational rank equality. Intermediate target: explicit whole nonzero dual kernel over D, potentially usable as the affine-line algebra for L066. All descent arithmetic and rational membership remain independent gaps.

Inputs: audited L067/L068/L070/L071/L072, full direction and quotient certificates only. ATTEMPTS/035--036 are cost comparisons, not inputs; partial columns and L069 are excluded. Preserve all upstream bytes.

Selected algorithm: BMSS Theorem 2(2), fastElkies', with conservative S modulo x^52 and T(t)=S(x)/x for t=x^2 modulo t^26. Newton doubling solves the same linearized differential equation as pinned Sage 10.7 lines 3147--3188. Reconstruct numerator degree <=7 and denominator degree <=6 for normalized x map. Normalized codomain is (7^4 a,7^6 b); actual dual divides x by 49 and y by 343, differential scalar seven.

Production and independent replay each have one 180-second arithmetic stage, external watchdog 181 seconds; total new data <=128 MiB. Stop on first cap/failure. Success needs full maps, both composition coordinates, exact degree/projective kernel and etaleness for all eight fibers and both signs. A partial kernel is not success. Any different algorithm or narrower new target requires its own review. Full Mathlib coverage not checked.
