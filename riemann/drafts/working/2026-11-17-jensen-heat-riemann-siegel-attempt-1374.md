# Step1374 — uniform heat-sum reduction working checkpoint

Research target is exactly assessment1373's (B), whose SPECIALIZE gate
predates this turn. Main gap: actual-Xi every-degree positivity; this
attempt only exposes a finite arithmetic reference for later signed tests.
No new signed-moment assertion is being attempted.

Inputs inspected: C019j (including its exact scale formulas and gamma
normalization), the supplied full overview/DAG, assessment1373, and
Polymath arXiv:1904.12438v2 (5)--(24), Corollary6.5/(70)--(74),
Proposition6.6. The relevant local source comparisons preserve the
signed-block scope failures; there is no prior proof of this reduction.

Calculation in progress: at x=2Y,y=0, kappa=0 and gamma is the quotient
of conjugate M_t values, so multiplying the source sum by B_t gives
twice a real part. Check its factor16 against H_0=xi/8 and m(Y).
The scale t log^2 Y is uniformly bounded. Intended error bounds are
e_A+e_B=O(Y^(-3/4)) and e_C,0=O(Y^(-1/4)); conversion additionally
requires 8|M_t(1/2-iY)|/m(Y)=O(1). These bounds are not certified here.
Retain the exact floor at every cutoff threshold. Continue if all three
errors and the normalization prove (B), otherwise preserve the precise
obstruction. No numerical experiment or effective onset is required.

All source estimates are imports; only the coupled-scale specialization
is to be proved. Signed margins, sample order/count, bulk separation,
and RH remain independent gaps. Existing notebook work is preserved.

Completed: the proof of (B), including all three errors and cutoff
equality cases, is saved canonically in C019k. This working checkpoint
records the earlier unfinished state, not an additional proof. The source
specialization is a local input, with no claim beyond checked literature.
