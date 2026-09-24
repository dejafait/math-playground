# Power-coordinate averaging checkpoint — 2026-09-11

Candidate, unproved at this checkpoint: for x_n=n^(2/3) and arbitrary increasing positive b_n tending to finite H, the block average of the full upward contribution over N<=n<2N tends to zero. For n in that block split successors at 4N. For j<=4N, the mean value theorem gives x_j-x_n >= (2/3)(4N)^(-1/3)(j-n). Expand b_j-b_n into increments Delta_r. For a fixed r and separation k=j-n, at most k pairs cross r, so the total coefficient is bounded by the harmonic sum through 4N. The resulting block average is O(H N^(-1/3) log N). For j>4N, x_j-x_n >= (1-2^(-2/3))j^(2/3), giving O(H N^(-1/3)) uniformly. The reflected sum is controlled by Lemma 74.

Resume by checking finite pair counting, constants, endpoints, and the infinite p-series bound before promoting this to a lemma. No height-tail rate is used. Existing work through Lemma 77 is complete and preserved.

Completed: the candidate and all constants are proved in Lemma 78. The finite crossing count and uniform infinite-tail bound establish vanishing block averages without any height-tail rate. No unfinished claim from this checkpoint is used as a proved input.
