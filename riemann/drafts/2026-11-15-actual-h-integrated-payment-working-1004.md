# Actual-h capped integrated payment — working1004

Invocation-start ready1003 (EXPLORE), explicitly approved by this turn's
gate, covers exactly the prescribed capped integrated test. Supplied
orientation was used directly; prior unfinished changes are preserved.
The bounded duplicate/source comparisons in review1003 are reused.

Main gap: L030-L032/C032a actual-Xi all-degree algebraic-square positivity.
Intermediate target: construct or rule out nomination1002's exact smooth
capped integrated test through T_0. A construction would pay one local
initial-cycle comparison; global assembly, interfaces, all degrees and
Xi transfer would remain open. The decisive test is every cap, support,
initial-value, regularity and full-flux condition, or an incompatibility
for all admissible tests. An ansatz failure is not such an obstruction.

Inputs read: C467b hypotheses and (5)-(11), C467a hypotheses/balance,
C466 survivor-cone hypotheses, C466z actual chart, C466y first lifetime;
review1003, audit1002 working record and stop1000. No global real velocity,
lifetime regularity, stopped-set inverse or raw terminal slice is assumed.

Current construction idea, not yet a result: find a smooth compactly
supported nonnegative psi<=1 whose entire support survives past T_0 and
whose tested real mass g(t) has min g(t)>M_0. The normalized test
c psi/g(t), with M_0<c<min g, would have constant mass and satisfy the cap.
Transfer rapidly from eta_0 to this test by a smooth scalar convex
combination. C467b's Lipschitz balance bounds any loss during the short
transfer; no differentiability of the initial-bump raw mass is presumed.
The load-bearing unresolved estimate is enough uniformly surviving
reserve mass for the actual g=B'(1+z)-B'(1), not the unperturbed model.
If that estimate fails, retain the exact residual without claiming
nonexistence. No new source or different target has been invoked.

Partial derivation before the exact calculation: for ordered imaginary
coordinates, set r=(q_3-q_1)/2 and v=(q_3-2q_2+q_1)/2. C466 gives all
secant slopes <=1/47, so h=1/2209 bounds their squares. With C=41 the
background imaginary differences are C-Lipschitz in q. On survivors,
R=r^2 obeys R'>=-4R/(R-v^2)-2-82R and R'<=-567/100, while
d|v|/dt<=6(|v|+h sqrt(R))/(R-v^2)+41 sqrt(R). The second R inequality
uses R<=a^2, proved by first crossing. Positive lower bounds on
sqrt(R)-|v| would imply survival by the existing strict buffer and
compact ODE continuation, with no lifetime regularity assumption.

For the full Jacobian J=(Z+iI)Q, the candidate lower comparison is
(log(det Q Delta(q)))'>=-27h P_q-246, where
P_q=sum_(i<j)(q_j-q_i)^(-2). The singular log-Delta error is bounded by
7h P_q and the determinant error by 20h P_q; all background terms are
retained. Together with ||X||<=||u||, |H(X)-H_0|<=15/64 and C466's
phase cone, this would give a lower density proportional to
Delta(u) Delta(q), including the actual full Jacobian.

The floating diagnostic in scripts/adjoint-flux/integrated-reserve-
diagnostic-1004.py/.json suggests a factor about 10.87 over the initial
mass, but is explicitly nonrigorous and cannot establish existence.
The next calculation is an exact rational barrier certificate for
finitely many compact initial boxes, plus a rational initial-mass
upper bound. Every comparison and the smoothing/transfer argument
remain to be written and checked before claiming the construction.

Completed1004: the full argument is now canonical in C467c. The exact
certificate accepts 100 boxes and replays 25,600 rational time tubes;
164 uncertified boxes contribute nothing and remain recorded. The
reserve lower bound is >4e-16 exp(-H_0), while the prescribed initial
mass is <8e-17 exp(-H_0). A smooth normalized reserve test has constant
mass 2e-16 exp(-H_0); a rapid smooth convex transfer from eta_0 pays
the complete integrated flux without requiring differentiability of
the initial-bump representative. All cap, common-support and endpoint
qualifications are proved in C467c, pending independent conceptual
audit. The exact script replay passed with no verification failures.
The earlier floating evidence and tentative reasoning remain preserved;
neither replaces the canonical proof or the exact certificate.
