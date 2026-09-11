# Selected-subset crowding checkpoint — 2026-09-11

Unproved draft pending audit. For nonempty F_N contained in B_N, replace
M,A,C in Lemma 94 by the subset cardinality, minimum normalized coordinate,
and harmonic crowding. The same finite expansion should give average Q
at most 32 W_N D_N and the same two selection criteria.

Candidate construction: U=2^(4k²), d=sqrt(U), with a left consecutive
packet [U,U+d), central grid U+2d+j*d for 0<=j<d/2, and right
consecutive packet [U+U/2+2d,U+U/2+3d). Start k>=2 and add index 1.
All lie in [U,2U). Select just the central grid; its size d/2 and
crowding <=2 give W<=4. Full blocks: a block that meets the central
grid contains a whole endpoint packet (left if N<=U, right if N>U).
Then C>=H_d and M<=5d/2, giving V at least constant*log d.
A block meeting no grid meets only a consecutive packet, or possibly
both packets (which would force meeting the grid); use C>=H_M,
M<=d and N comparable to U to prove V grows uniformly. Audit clipping
and dyadic ratios before promoting. Interpolate x_s=s^(3/4) as in L095.

Resume here: check endpoints and uniform lower bounds; then store the
subset criterion and its construction as separate lemmas and validate.

Completed: all claims above were audited and stored in
`lemmas/L096-selected-subset-crowding-selection.md` and
`lemmas/L097-endpoint-packets-realize-subset-selection.md`.
The uniform full-block lower bound is H_d/(5sqrt(2)). No unfinished
claim from this draft is promoted beyond those proved statements.
