# Full-circle heat comparison1370 — working checkpoint

Approved target: assessment1368, unchanged. Research/development, not a
new literature assessment. Main gap remains actual-Xi all-degree
positivity; the proposed comparison leaves reference signs independent.

Using Ono v1 (2.9), put u=-exp(i theta)/q, -pi<=theta<=pi and
v=sqrt(d/2)*theta. With s0=1/2+iY and a=Y/sqrt(2d)=sqrt(t), the
normalized circle is exactly

    (1/sqrt(pi)) integral K_d(v)*xi(1/2+iY exp(i v/sqrt(2d)))/m(Y) dv,
    K_d(v)=exp(d*(exp(i sqrt(2/d)*v)-1-i sqrt(2/d)*v)),
    |v|<=pi*sqrt(d/2).

Polymath v2 (35), with v reversed, gives the proposed reference as
the same integral over R with K_d replaced by exp(-v^2) and xi's
argument by s0-a*v. Thus parity, factor8, time and prefactor agree.
No F or zeta division occurs. This is unfinished reasoning, not yet
a proved comparison or an obstruction.

Plan: local cutoff V=d^(1/8). On |v|<=V, Cauchy derivative estimates
from a radius 1/log(Y) disk and reflection plus Ono (4.8) should give
|xi|/m <= C*Y*exp(C|v|) and |xi'|/m <= C*Y*log(Y)*exp(C|v|).
The argument error is O(Y*v^2/d); kernel error is
O(|v|^3/sqrt(d))*exp(-v^2). Integrating would give
O(Y/sqrt(d)+Y^2*log(Y)/d)=O(1/log(d)).

Obligations still open at this checkpoint: prove those uniform local
bounds on every interpolation disk; pay the entire complementary
circle using reflection and sectorial Stirling; pay the unbounded heat
tail including shifts beyond fixed vertical strips. An unpaid tail is
inconclusive. No sign/count conclusion or use of a heat real-zero theorem.

Source and duplicate coverage reused from assessment1368; exact primary
formulas (2.9), (4.8), (35) were retrieved for specialization, not a new
source-review turn. Stops1345/1355/559 remain preserved. No scripts run.

Completed disposition: the local disks and both entire tails are paid
in [C019j](../../lemmas/C019j-actual-jensen-full-circle-heat-comparison.md),
with uniform error O(1/log d). That file is the canonical full proof;
the provisional reasoning above is retained as the pre-work checkpoint.
Independent critical audit is pending. No reference signs or roots
were derived. The nomination for that audit is REVIEW_REQUIRED.
