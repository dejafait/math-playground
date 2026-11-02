# Coupled rational family: second bounded attempt

The unchanged invocation-start SPECIALIZE assessment is
`literature/2026-10-31-coupled-rational-global-certificate-scope.md`.
Only its exact P4/q, full-K, both-global-branches target is being tested.
The main gap is all-degree actual-Xi positivity. A certificate of cost
less than 1/288 would bound periodic clipping under the finite-C_I
reserve; nonlinear Xi transfer remains independent and unresolved.

Preserve L594 and its failed rounded candidate, and the L590/L592/L593
stops. This attempt does not extend the failed projection. It uses
acceleration minimization and covariance-scaled variables. For the
reordered vector (w,a), a=(z,Z), partition H into E,B,C, so that
v^T H v=w^T E w+2a^T B w+a^T C a. Put
g=(V_y,V_Y), d=V_x*y+V_X*Y. The b-th branch is
a^T C a+2a^T l_b+r_b, with
l_b=Bw-g/2-b*(x,0)/2 and r_b=w^T E w-d+b*y^2.
The necessary-and-sufficient condition is C positive semidefinite,
l_b in range(C), and r_b>=l_b^T C^+ l_b for every w, b=0,1.
This follows by diagonalizing C and completing squares on its positive
eigenspaces; nonzero nullspace linear terms are unbounded below.
At w=0, L594 gives g=d=0, so C>=0 is exactly the remaining condition.
No positive-definiteness assumption may discard singular cases.

Planned bounded computation: a finite set of state directions gives
necessary 3-by-3 Schur matrix inequalities, with all acceleration
values included. Minimize full trace(HK) in a covariance-scaled basis.
A finite-state feasible answer is only a lower-relaxation probe, never
a global certificate. A dual lower bound must be recovered exactly
before excluding the family. If the value is below 1/288, global
positivity remains to be proved. Full artifacts will be saved.

Continuation/abandonment test: exact global feasibility below 1/288 or
an exact whole-family lower bound at least 1/288 is decisive. A second
unproductive attempt requires reassessing this family rather than a
third solver extension. No source refresh, new denominator, higher
degree or different witness family is authorized in this step.

Partial computation saved: 192 directions gave a floating relaxation
value below the threshold; 1536 directions gave a stable dual value
about .00918, but later low-barrier iterates lost reliability. Full
failed diagnostics are preserved. Only the stable iterate is a lead.
The next part of this same attempt is exact dual recovery: fix rational
state rays and rational Cholesky factors for all dual matrices; allow
small weight corrections to 46 selected positive matrices. There are
21 covariance equations and 25 essential quartic derivative equations.
Polynomial division by q eliminates the ten quadratic-storage gauges:
the remainder has degree in x at most one. Those quadratic derivatives
already have zero expectation under the exact K. Directed intervals
and a residual-certified approximate inverse can bound the correction
without treating a truncated K as the exact covariance. If positivity,
all equations or the strict lower bound fails, the dual is unproved.

Completed: L595 contains the canonical finite-dual proof. All 3072
rational PSD factors and 1536 state rays are preserved in
`../scripts/coupled-flux/rational_schur_dual_inputs.json`. The directed
90-digit verification bounds the weight correction by .011204 and
the corrected objective below by .00907642344528..., above both
9/1000 and the requested 1/288. A 120-digit replay passes the same
five rational inequalities. Both full certificates are retained.
This is a family-wide negative result, not numerical SOS infeasibility.
The lower-barrier numerical failures are retained separately and are
not used in the proof. No probability or path realization is asserted.

Outcome: NEGATIVE; two mathematical attempts in this family, of which
the first was EXPLORATION. Park further cheap-certificate searches and
independently audit L595's logic and complete certificate. The newly
written ready audit scope needs separate approval next turn; it is
not an audit or an approval of the new theorem. General storage,
periodic clipping and nonlinear Xi transfer remain open.
