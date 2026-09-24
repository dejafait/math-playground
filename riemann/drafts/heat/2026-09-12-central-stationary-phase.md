# Central stationary-phase checkpoint — 2026-09-12

Existing L140 is complete. For N/2≤k≤2N put X=τ/(2πk), r=X/N. Substitution x=Xu gives I_k=X^(-1+iτ)∫ a_r(u)exp(iτ(log u−u))du, where a_r=u^(-2)exp(−log²(ru)). For large t, r lies in [1/4,2]. The phase has a unique fixed nondegenerate maximum at u=1.

Candidate: I_k=X^(-1)exp(iτ(log X−1)−iπ/4)sqrt(2π/τ)exp(−log² r)+O(X^(-1)τ^(-3/2)), uniformly in this range. Summing absolute errors should give O(t^(-3/2))=o(t^(-1)). Unproved at checkpoint. Resume by proving a compact Morse-coordinate Gaussian estimate with uniform Fourier moments and bounding the two nonstationary tails by two integrations by parts; check endpoints at zero and infinity. No lower bound for the mode sum is proposed.

Completed: L141 proves the candidate expansion and the absolute summed O(t^(-3/2)) remainder. The compact estimate follows from Fourier inversion with a uniform fourth-derivative bound; two integrations by parts handle the nonstationary tails. The canonical lemma supersedes the draft claims. No central-sum lower bound or estimate of modes outside the central range was proved.
