# Negative Poisson modes checkpoint — 2026-09-12

Existing L140 and L141 are complete and preserved. For m≥1, substitute x=N exp(y) in I_{−m}. Shift y to y+iθ with θ=π/2. Candidate modulus bound:

|I_{−m}| ≤ N^(−1) exp(θ²−τθ) ∫ exp(−y²−y) exp(−2πmN exp(y) sin θ) dy.

Summing the positive majorants using 1/(exp(a)−1)≤1/a should give sqrt(π)e N^(−2) exp(π²/4−πτ/2)/(2π), exponentially small compared with t^(−1). This is unproved at checkpoint. Resume by checking both vertical contour sides, the shift sign and prefactor, Tonelli, and the Gaussian constant. No full-series lower bound is proposed.

Completed: L142 proves the candidate bound with the stated constant. Both vertical sides vanish by a Gaussian bound independent of m; Tonelli and the geometric-series majorant control the infinite absolute sum. The canonical lemma supersedes the draft claim. Positive-mode cancellation remains unproved.
