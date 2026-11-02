# Full-action Poisson transfer — working checkpoint, step 63

Approved target: the unchanged TARGET in
`drafts/literature/2026-11-02-full-action-half-plane-poisson-transfer.md`
(invocation-start EXPLORE). One mathematical attempt; no new source
coverage or stronger positivity hypothesis is assumed.

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
exclude L679-feasible full angular actions at the fixed rate 1/100.
Downstream use: decide this general segment-positive separator mechanism;
cone/H/support and Xi realization remain independent. Continue only if
the complete signed Poisson balance gives an asymptotic contradiction
for every fixed C; otherwise record the failed hypothesis or rate.

Inputs read: L666 (6), L674 Sections 1--2, audited L678 (1)/(14)
and its ray-bound proof/audit, and audited L679's statement and mass
normalization. The three exact domain/polynomial/pole stop records
confirm that this test removes their extra domain, degree and zero
conditions. Reuse ABR Theorem 7.5 from the ready assessment.

Unfinished calculation: put d=5/4, h=R-d=1/8, b=9/20 and
g(y)=Re A(x+i*y). For |a|>=d, each nonzero-index full-kernel factor
is at most (d+1)/(U-d) times (U+d)/(d-1)=1809/41<45;
the j=0 factor remains d/|a|. Thus the entire closed half-plane
is bounded for each fixed n and psi, and the action even decays
at infinity. Verify compact differentiation and boundary continuity
before applying the cited representation to A(x+i*z).

The candidate exact representation at -R is
Re A(-R)=integral_R h*g(y)/(pi*(h^2+y^2)) dy.
L679's normalized mass uses d*dy/(pi*(d^2+y^2)). Their density
ratio on [-b,b] has minimum
(h/d)*(d^2+b^2)/(h^2+b^2)=1412/1745>4/5.
Outside that segment L678 supplies an absolute bound
exp(B)*n^C*exp(-(gamma-1/100)*n), with
gamma=94502611/8000000000 and B=19680067/8000000.
L674's parameter-circle calculation appears valid and gives
|A(-R)|<=(10/11)*(66/67)^(n-1)*exp(n/100)*n^C.
Both terms are exponentially small against n^-3; the remaining
work is full applicability, exact arithmetic, quantifiers and scope.

Minor prerequisite arithmetic found: L679 Section 6 writes
U-d=21/64; the exact difference is 41/64. The weaker bound
21/64 used there remains valid, so its theorem is unaffected.
Correct only that identity while retaining the original estimate.

This is partial reasoning, not an independent audit or a completed
RH argument. No numerical evidence is needed for the proposed balance.

Completed later in this same step in
`lemmas/L680-full-action-signed-poisson-cost-obstruction.md`.
The original working reasoning above is retained; the complete proof,
qualifications and citation are canonical there. The continuation is
an independent conceptual audit under the unchanged ready target.
