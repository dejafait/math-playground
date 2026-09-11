# Logarithmic-buffer sharpness checkpoint — 2026-09-11

Fix c>0, A_n=4^n, d_n=c log A_n, K_n=floor(d_n), M_n=floor(log A_n). For sufficiently large n, put multiplicity M_n at ±(A_n+2d_n+k)±i for 0≤k<K_n, and simple targets ±A_n±i/2.

Candidate conclusion, unproved at checkpoint: the full unit-interval count is at most 4 log(2+|x|), and the exterior upward interaction at A_n+i/2 with cutoff A_n+d_n tends to 1/(6c). The positive same-level sum should be a Riemann sum over [2,3]; reflected and future blocks should vanish by O(n²/16^n) bounds.

Resume by checking arbitrary half-open unit intervals, block separation, strict cutoffs, and the Riemann-sum normalization. Do not use this candidate as a proved DAG input until those checks are complete.
