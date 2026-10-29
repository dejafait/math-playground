# Moving-anchor cutoff attempt — 2026-10-26

Approved target: assess whether L461 admits one C with negative-witness
index at most ceil((3/16+C/sqrt(log log T))log T), T=2+|a| large.
The saved SPECIALIZE assessment is
`literature/2026-10-26-moving-anchor-explicit-rate-coverage.md`.
This is one REPRODUCTION attempt, not an initial-sign argument.

Main gap: actual-Xi initial signs at unbounded heights and global mixed
positivity. A uniform shrinking witness range could specify a sharper
initial interval for a later sign estimate; that estimate and effective
height overlap remain independent missing inputs.

Working setup (not yet a proved bound): put d=1/sqrt(log log T),
eta=3/8+d and R=3/8+2d. Normalize log zeta at 2+ih by L005.
Use r0=1/2, r1=9/8-d, r2=9/8-d/2, r3=9/8-d/4.
Borel–Caratheodory costs O(d^-1); the three-circles exponent satisfies
1-theta >= kappa*d for an absolute kappa>0. This suggests a uniform
logarithm loss O(d^-1 exp(-kappa*d*log log T) log T) for heights
comparable to T, which is eventually smaller than d^2 log T.

Unresolved application: propagate the boundary estimate through a
rectangle with heights |a|/2 and 3|a|/2, with d fixed during that
application. A holomorphic damping factor centered at i|a| should
suppress the polynomial horizontal bounds. Check its vertical cost
and its inverse on both circle heights |a|+/-Im(y). Retain uniform
Stirling constants, the positive anchor and all geometric prefactors.

Continuation/abandonment test: prove the complete L266 comparison
quotient <= (3/16+C*d)log T with one constant and one onset,
independently of b and central multiplicity, or preserve the failed
threshold and park this implementation. L461's external 7/8 premise
and manuscript/import-closure qualification are unchanged. L462's
fixed-anchor stop is preserved and does not cover this moving family.

L005 normalizes the logarithm, L018 supplies the completion identities,
L266 supplies the witness comparison, and L320 supplies elementary
growth. The exact external premise retained in L461/L452 is unchanged.
No fixed-parameter big-O or all-height compact minimum is assumed
uniform. No scripts or numerical evidence establish these bounds.

Working resolution before canonical write-up: the full logarithm bound
is at most d^2 log T eventually, since its ratio to that quantity is
O((log log T)^(3/2) exp(-kappa*sqrt(log log T))). For t=|a|,
normalize G(s)=xi(s)exp(-i*pi*s/4)(s+2)^(-q), q=7/4+R/2,
on 1/2-R<=Re(s)<=1/2+R, t/2<=Im(s)<=3t/2.
Its vertical bound is O(T^(d^2)); its preliminary full bound is O(T).
Multiply by exp(tau*(s-1/2-it)^2), tau=8log(T)/t^2. The horizontal
bound loses T^2; undoing damping at |Im(s)-t|<=R costs only a bounded
factor. This avoids all bounded-height zeta minima.

The resulting full circle/anchor ratio is at most
C0*T^(d+4d^2). L266 then retains the extra term
log(2C0/(1-p))/(2log(R/eta)). Using log(R/eta)>=d/R and
1-p>=2d, that term is at most d*log T eventually. The leading
coefficient is at most R(1+4d)/2 <= 3/16+(15/8)d for d<=1/32.
Thus the full quotient is below (3/16+3d)log T. The completed proof
is now canonical in
[L468](../lemmas/L468-moving-anchor-uniform-witness-cutoff.md).
Its separate critical audit is pending. It establishes no initial
signs or effective onset; the working notes above are preserved.
