# Step 422 — fixed-box complete upper capacities

Main gap: arbitrary-center safety at 67/68 agreements. Intermediate target:
Test L112's fixed enclosed root against all upper capacities x_i*x_j*x_h<=min(c_i,c_j,c_h) on the 28,215 actual permitted side classes.
The prior SPECIALIZE assessment is
`drafts/literature/2026-10-23-enclosed-root-all-upper-capacities.md`.
Its source review is reused unchanged. L112 covers only (5,5,5), while
L110/ATTEMPTS/093 concern a different sufficient allowance and
ATTEMPTS/082 concerns a stopped full-variable prescription.

Use L021,L098,L109,L110,L111,L112 and foundations/04,13,14. Reconstruct
canonical pairs and the original-coordinate endpoints from the full saved
L112 certificate, binding all inputs by SHA-256. No new nonlinear solve,
trajectory, box refinement or parameter scan. Enumerate original (i,j,t,s)
ranges and D, all six presentations, repetitions and null edges. Compare
the resulting classes with L110's saved enumeration and its independent
realizability criterion. A second script uses four fixed-edge occupancy
regions, independently reconstructs endpoints and all comparisons, and
checks complete coefficient agreement with the existing enclosure.

Every positive endpoint product is compared exactly with the minimum of
the three canonical capacities. Upper <= capacity passes that class;
lower > capacity rejects this enclosed root; otherwise the box is
inconclusive. Save all classes, exact fractions, class multiplicities,
representatives, extreme bounds, failures/straddles and input hashes.
Constructor and independent checker each have a 300-second budget and
preserve incomplete/failed reports. Only run this finite fixed-box test.

A complete pass would establish the upper-capacity part of this product
prescription. A violation parks this root; a straddle stops this box's
decision without refinement. Neither decides Boolean lower rows, the full
source lift, PSD, global positive-root uniqueness, packing, RS realization
or the 955–957 bracket. L112's dedicated critical audit remains pending.

Mathlib: full matching finite comparison application not checked.

Completed: every one of 28,215 actual permitted classes passes its upper
capacity, with zero rejections/straddles. The maximum upper ratio is at
(5,5,6), strictly between 107/10^13 and 108/10^13. The constructor and
independent checker pass 1,567,627 and 3,153,044 checks respectively, with
no failures, retaining the entire original source partition and every
endpoint comparison. Complete evidence, hypotheses and qualifications
are canonical in L113. This supplies one shared upper-capacitated
triangle weighting using L112's root input; stronger feasibility and
the dedicated critical audits remain pending. The new audit continuation
is REVIEW_REQUIRED, without retroactively changing this completed target.
