# Step 261: bounded prime-2 covariance repair

The approved target is the exact TARGET in
`literature/2026-10-20-prime-two-occupation-covariance-repair.md`.
Its SPECIALIZE coverage is reused without new literature work. The main
gap remains global mixed positivity. The intermediate test asks whether
L440's separation survives a bounded change of only the bulk xy covariance;
success would distinguish a defect of its representative from a constraint
on all laws satisfying L438. It would not construct a trajectory.

Working construction, saved before the full preservation checks: with
omega=log 2, set d(t)=-omega sin(omega t)/sqrt(2),
bar_d=E_H(w d)/E_H w, and add (d-bar_d)(e1 e2^T+e2 e1^T)
to L438's centered bulk covariance. Keep all rare components, m, w, g_H
and the original cutoff. The integrated matrix addition is exactly zero;
the conditional x-second entry is unchanged. The proposed residual
increment is -omega/(30 sqrt(2))+o(1). These observations alone do not
discharge support or preservation of moments after reselecting the atoms.

Continue only after establishing boundedness, Borel realization, strict
translated negative support, exact six seconds and first B mean, the first
D tolerance, all original cubic and quartic tolerances and fixed-prime
limits, fixed envelopes and the same-family cap conclusion. A proved
conflict stops this restricted repair; an unchecked bound leaves it
unfinished. L440's separation and all older failure scopes are preserved.

Completed: the full proof and all preservation estimates are canonical in
L441. The candidate correction passes this bounded attempt and gives
residual o(1); no mathematical script or numerical certificate is needed.
Its separate critical audit remains pending. The continuation assessment
is marked REVIEW_REQUIRED rather than approved in the construction turn.
