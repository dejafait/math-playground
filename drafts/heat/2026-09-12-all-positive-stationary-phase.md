# All-positive stationary-phase checkpoint — 2026-09-12

Prior L140–L142 work is complete and preserved. Candidate: extend L141's leading term M_k to every k≥1, with sum |I_k−M_k|=O(t^(−3/2)). This is unproved at this checkpoint.

Put A=τ/(2πN), r_k=A/k, X_k=Nr_k. The key proposed bound is sum k exp(−log²(z/k))(1+|log(z/k)|^p)≤C_p z² for all z>0. It implies sum X_k^(−1)|a_{r_k}^(j)(u)|≤C_j(A/N)u^(−j). Reuse L141's compact Morse coordinate and Fourier estimate, now summing derivative norms. For the nonstationary part D=(q·)' with q=u/(1−u), check D²b=q²b''+3qq'b'+((q')²+qq'')b. Its weighted sum should be integrable: O(1) near zero and O(u^(−2)) at infinity. Resume by proving the lattice bound, checking those coefficients and endpoint terms per mode, then summing with Tonelli. No lower bound is proposed.

Completed: L143 proves the candidate for every positive integer k. The lattice estimate gives the summed derivative bound, and D² has the asserted integrable endpoint majorants. The absolute summed error is O(t^(−3/2)). The canonical lemma supersedes the draft claim; cancellation among leading terms remains unproved.
