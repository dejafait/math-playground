# Distinct-input collision attempt1477 — working note

The unchanged EXPLORE assessment1468/review1469 covers the fixed sextic
(2,4) test. The main gap is actual-Xi all-degree positivity and the
unpaid exceptional-root deficit. This attempt uses only T=1+D+tD^2,
1/4<=t<=5/18, R=(y^2-1)(y^2-4), Q=y^2+b y+c, c>b^2/4.
It does not assume any extremal reduction or transfer C020r/s's root
locations to R. C020q is an algebraic comparison; C020p supplies the
already justified Walsh normalization. No new literature is needed.

Bounded test: solve F(d)=F'(d)=0, F=T(RQ), retaining singular systems,
and examine the quartic residual by exact arithmetic. A root-free
residual would supply the output count four; a residual with two real
roots requires an independently certified pair-removing perturbation.
Four real residual roots do not give a witness. Search failure is not
whole-class impossibility. Stop after this one family calculation;
record any useful exact elimination and the remaining count gap.

Partial setup: define A=T(yR), B=TR, C=T(y^2R), so F=C+bA+cB.
At d the collision system is A b+B c=-C,
A' b+B' c=-C'. Its determinant is Delta=A B'-A' B.
Cramer's numerators are N_b=B C'-C B' and N_c=C A'-A C'.
The nonsingular admissibility margin is 4 N_c Delta-N_b^2>0.
All these are polynomials in d,t; no sampled root count is a proof.

Essential inputs/unresolved assumptions: C020p's preservation interface,
assessment1468/review1469, and exact polynomial/Sturm arithmetic below.
C020r/s exclude only two-double inputs. No general deformation,
composition law, actual-factor correspondence, exceptional-divisor
payment, all-degree control, initialization or overlap is available.

Completed result: C020t gives the exact regular collision parametrization
and the uniform fixed-family exclusion. The shifted Cramer numerator is
<=-3213/320, so every singular system is inconsistent. Thirty-two
rational parameter cells certify four simple reference roots and a
strict threshold order throughout the closed interval; the quartic
collision residual consequently has four simple real roots. All 340
exact checks pass. The full certificate is
`scripts/quartic-differential/sector-sextic-distinct-collision-1477.json`.
Floating roots only proposed brackets; their acceptance uses full-box
rational checks. Independent critical audit remains the next step.
No more fixed-spacing examples are justified by this result alone.
