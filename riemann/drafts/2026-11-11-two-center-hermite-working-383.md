# Two-center Hermite attempt — step383, saved working note

Approved target: test the degree-n Hermite interpolant at the images of
t=n+1 and t=2(n+1), with balanced multiplicities, for the uncapped
complete residual O(exp(-n/64)) on both spectral windows. The unchanged
pre-invocation assessment is
`literature/2026-11-11-two-center-hermite-residual-test-review-382.md`.

Main gap: L030–L032/C032a actual-Xi positivity, L966/L968 signed forcing,
and unpaid L984(H). Plausible use: a uniform approximation would bound
the target action of exact band-null unit-TV measures. It would not
control C997s's capped objective or pay the independent transfer gaps.

Reused contracts: C997c(1),(4)–(6), C997s's complete kernel and step373
complex pairing audit. Parent review381/step382 supplies the precise
Calvi Theorems1.9/1.17/1.18 repeated-node contour formula and the scoped
duplicate/failure assessment. C997r/t/u remain contrasts, not premises.
No source refresh or cross-notebook input is needed.

Working setup: y=exp(it/(4n)), exponent alpha_n=(-7/2+i/2)n,
f_n(y)=exp(alpha_n Log y). The intended branch identity is
exp(15it/8)f_n(y)=exp(i(1+i/8)t). Nodes are
a_n=exp(i(n+1)/(4n)), b_n=exp(i(n+1)/(2n)); multiplicities
m=floor((n+1)/2), ell=n+1-m. The degree-n remainder has node product
(y-a_n)^m(y-b_n)^ell. Branch, enclosing contour, distances and all
n-dependent factors still require proof.

The audited complete-kernel variation costs are
18 exp(27/16)(n+2)exp(9n/32) on the upper window and
8 exp(3/4)(n+2)exp(-n/16) on the lower window. Thus a crude global
upper-window spectral error estimate must beat exponent 19/64, with
strict slack to absorb polynomial factors. A merely insufficient upper
envelope proves no lower obstruction.

Bounded decision: establish the complete uniform rate or a rigorous
obstruction specific to this interpolant. If neither is obtained in
this attempt, preserve the partial calculation and park the recipe
pending a materially different input or refined mechanism. Both beta
terms/windows, all zeros/endpoints and K's -1 must be retained.

Completed checkpoint: the canonical partial calculation and all proofs
are now in C997v. The lower window is paid; the chosen absolute upper
envelope has a proved positive rate even when its contour maximum is
left exact. This does not bound the actual residual from below. The
balanced target is parked as inconclusive. The proposed sublinear
allocation is separately marked REVIEW_REQUIRED; no estimate for it
was derived in this turn.
