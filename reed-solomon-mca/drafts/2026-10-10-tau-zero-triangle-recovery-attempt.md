# Tau-zero triangle recovery — bounded working attempt

Started 2026-10-10 under the pre-existing SPECIALIZE assessment
`literature/2026-10-10-tau-zero-triangle-fourth-support.md`.

Main gap: arbitrary L010 sixteen-count equality; global interval
11/q–16/q. Exact approved intermediate target: additional-four-support
recovery for L041's tau=0 triangle, arbitrary original finite parameters
and extension-field weights, including initially zero fourth weights.
Downstream use: simultaneous recovery constraints for this other triple
pattern. Counting, extraction, other patterns and challenge-definition
coverage remain independent gaps. Continue if explicit prime-field label
tests and pair-weight equations lift every exceptional quotient case;
reassess if only generic membership or an unresolved lift is obtained.

Inputs: L010 and audited L041; imported DR2/DR6–DRC recurrence coverage
from the saved assessment. L016/L043 are method comparisons only, not
triangle theorems. ATTEMPTS/008–009,022–024 were checked and preserved.

Use A0={a,b,y1,y2}, A1={a,c,z1,z2}, A2={b,c,w1,w2}.
Pair weights on a,b,c are p,1-p; q,1-q; r,1-r respectively,
with p,q,r outside {0,1}. Put g=gamma1-gamma0,
rho=(gamma2-gamma0)/g, t=(T-gamma0)/g, and Y=sum c_y v_y,
Z=sum c_z v_z. L041 gives the normalized pencil

M(t)=(1-t)/(1-rho) [Y+c_a p v_a+c_b q v_b]
     +t/rho [Z+c_a(1-p)v_a+c_c r v_c].

For K let J={a,b,c} minus K, m=|J|. Nonzero recurrence
columns are independent by their first m rows. An explicit quotient
is obtained by multiplying the recurrence functional polynomials by
G_J(X)=product_(x in J)(X-x): projected coordinate j=0,...,3-m
is sum_(y in Y) c_y y f_K(y) G_J(y) y^j, and similarly for Z.
This avoids an unspecified quotient basis. If m<=2, injectivity on
at most eight moment columns makes the Y vector zero iff both Y
labels are in K, and similarly for Z; both-zero is thus possible
only for m=3. The m=3 case needs its own complete lift.

For nonzero proportional vectors z=mu*y, mu lies in F_97^*.
Exclude mu=-1 and E=rho-(1-rho)mu=0. Then t=rho/E and
E M(t)=N=Z-mu Y+c_a[1-(1+mu)p]v_a-mu c_b q v_b+c_c r v_c.
The missing-column solve C beta=-F_K(Z-mu Y), first m rows,
gives explicit rational required pair coefficients. Compare these
with the displayed a,b,c coefficients before any fourth-weight solve.

When both projected vectors vanish, recover betaY,betaZ from
C betaY=-F_K Y and C betaZ=-F_K Z. The actual pair gates are
three affine equations A_x+mu B_x=0 with
(A_a,B_a)=(c_a(1-p)-betaZ_a,-c_a p+betaY_a),
(A_b,B_b)=(-betaZ_b,-c_b q+betaY_b),
(A_c,B_c)=(c_c r-betaZ_c,betaY_c).
Need prove the all-zero A,B case impossible, retain all no-direction
and pivot cases, and recover all eight moments plus same-support
failure. No universal support classification or count is assumed.

This unfinished reasoning was saved before completing the case proof.

Completed result: [L057](../lemmas/L057-tau-zero-triangle-fourth-support-recovery.md)
contains the full necessary-and-sufficient criterion. Explicit quotient
rows are polynomial evaluations, and explicit Lagrange sums recover
each missing coefficient and each fourth weight. The both-zero case
has m=3 and a complete affine pivot test, with an entirely free lift
excluded by sparse-error uniqueness. All original finite exclusions,
all eight moments, zero recovered weights and same-support failure
are retained. The continuation test is met for local recovery, not
counting or extraction.

Three selected prime-field regression pencils independently compare
the criterion with full eight-moment Gaussian recovery on all 1817
nonbase four-supports at all 94 eligible prime-field parameters each.
Actual/required discrepancies are 0/0; both an isolated and a both-zero
full recovery are exercised. Full evidence is in
`../scripts/triangle-recovery/selected-regression.json`; reproduce with
`python3 scripts/triangle-recovery/check_selected.py` from the notebook.
The complete failures array and selected both-zero certificate row
were inspected. This regression is not a uniform field/count proof.

Classification: REPRODUCTION under the prior SPECIALIZE gate. This is
local progress using assessed recurrence machinery, with no claimed
advance beyond checked sources or on 11/q–16/q. L057 awaits a separate
critical audit; its newly proposed audit scope is REVIEW_REQUIRED.
