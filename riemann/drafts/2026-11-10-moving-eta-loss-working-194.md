# Step194 — fixed-index moving-eta attempt

Target: the exact SPECIALIZE target in
`drafts/literature/2026-11-10-prescribed-q-moving-eta-loss-review-192.md`.
Main gap remains actual-Xi all-degree mixed positivity. Only the
parameter movement at fixed a_n is being tested.

Working calculation, before canonical write-up: set s=eta_n,
t=eta_(n+1)=s/9, delta=s-t, h_n(z)=a_n(z)^2 and
W(z)=z^2/((z+s)(z+t)). Direct subtraction gives
Delta Q=delta sum_j W(beta_j)h_n(beta_j).
L026 implies |Im beta|<Re beta, hence Re(beta^2)>0. Consequently
Re W has numerator |z|^4+(s+t)|z|^2 Re z+st Re(z^2)>0.
Keep h_n(0)=n^2 as a nonnegative real-part contribution. L964(10)
gives |h_n(z)-n^2|<=8*9^n |z| at every node, while |W|<=1.
The remainder is bounded by delta*8*9^n*A=A/9.

Write-up checks identified before completion: both off-diagonal sums and both separated
series must be absolute; conjugation must give realness; the Cauchy
bound must be invoked without L964's negative-margin hypothesis.
No theta partial fractions are needed, so no h-resolvent is deleted.
No index change inside a_n, zero data, RH or positive measure is used.
Completed these checks in the canonical L972 proof. A separate critical
audit is still required. Signed index forcing, initialization and
accumulated margins remain independent gaps.
