# First-moment transfer1391 — working checkpoint

The unchanged target is approved by assessment1389, source review1390
(SPECIALIZE). Main gap: actual-Xi all-degree positivity. This attempt
tests only the sufficient C019n remainder budget, not (N) or RH.

Proposed transfer: replace the deformed floor by the ordinary floor
with at most one term of size O(X^(-1/4)). For xi=v_n(Y)/q use a fixed
smooth even cutoff equal to one on [-1,1] and the multiplier
exp(t*q^2*xi^2/4-pi^2*t/64+i*pi*t*q*xi/8). Its inverse Fourier
kernels have a common Schwartz envelope because t*q^2 is bounded.
Retain both conjugate branches. Truncate the translation parameter at
U=X^(1/8); all larger parameters act only on the finite frozen sum.
Within the truncation, the ordinary floors differ by at most one term,
and the elementary phase curvature costs O(u^2/(q^2*X^(3/4))).
The resulting candidate representation is a truncated kernel average
of ordinary real Hardy Z plus O(X^(-1/4)), uniformly in Y in J.
HRS Theorem1 at k=1/2 would then give integral_J |V|=O(B*q^(1/4)).

Candidate consequence to check in full: Markov applied to sqrt(E)
puts a fixed positive fraction of D below E=O(sqrt(q)). C019n's
pointwise H<=-kappa*q then gives -I_H>=c*B*sqrt(q). Since |I_V|<=B/2,
the exact identity forces R>=c*B*sqrt(q)-B/2. This would rule out
R<=c_D*B/2 while leaving the sign of I_V and (N) unresolved.

Unfinished checks at this checkpoint: Fourier convention and both
branches; common kernel majorant; all three floors including equality;
complete finite-sum tail; ordinary phase and AFE errors; dyadic moment
covering; constants and inequality directions in the R comparison.
No numerical computation, effective onset, probabilistic law or RH
assumption is involved. Full proof will be canonical if completed.

Completion1391: the listed checks are addressed in the canonical
[C019o proof](../../lemmas/C019o-moving-first-absolute-moment-and-remainder-obstruction.md).
The transfer and remainder obstruction are derived, pending separate
conceptual audit. This checkpoint preserves the initial reasoning;
the canonical proof supersedes its provisional status and is the sole
full derivation. The result stops the sufficient small-R closure only.
