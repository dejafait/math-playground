# Variable local count checkpoint — 2026-09-11

Scoped candidate (unproved at checkpoint): under Lemma 74, assume unit interval counts <= C(1+t)^alpha, 0<=alpha<1, and (H-b_n)(1+x_n)^(3alpha) -> 0. Infinitely many gaps should exceed c(1+x_n)^(-alpha), c=[2C(alpha+1)2^alpha]^-1. Compare cumulative counting with increments of (1+x)^(alpha+1). Shifted unit bins then give a convergent sum with tail k^(alpha-2) and U_n=O((H-b_n)(1+x_n)^(3alpha)) on this subsequence.

Resume by checking constants in transformed increments and the binwise infinite majorant; then test strict enlargement using x_n=n^p, 1/2<p<1, b_n=2-n^-q, q>3(1-p). This is conditional progress only; unrestricted counts/heights remain unproved.

Completed: the candidate is proved in Lemma 77 with the explicit constant above. The concrete example x_n=n^(2/3), b_n=2-n^(-2) verifies strict enlargement beyond bounded local counts. The count and height-tail hypotheses remain additional assumptions; no unrestricted assertion is promoted. Current next action is recorded only in PROGRESS.md.
