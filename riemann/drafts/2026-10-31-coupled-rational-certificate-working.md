# Coupled rational certificate: bounded mathematical attempt

The invocation-start SPECIALIZE assessment is
`literature/2026-10-31-coupled-rational-global-certificate-scope.md`.
Its exact TARGET is the sole target of this attempt. Existing changes
and the L590/L592/L593 stops are preserved; no new source review is needed.

Main gap: actual-Xi all-degree signs at unbounded heights. Intermediate
target: global clipping inequalities for V=P4/q, with the stipulated
positive-definite q and arbitrary real homogeneous quartic P4, at full
cost trace(HK)<1/288. A sufficient certificate would exclude periodic
bulk reaching that budget when K-C(h) is in the actual finite C_I.
Periodic fourth/probability assembly and nonlinear Xi transfer remain
independent gaps.

Inputs read: L592, L586 hypotheses and spectral generators; L590's
family/origin cases; L593's hypotheses, conclusion and separating
storage, and the two relevant ATTEMPTS stops. The supplied assessment
already compares the primary rational-divergence method (Chernyavsky
et al., arXiv:2110.03079v1, Remark 3.1) and its limitations. No inspected
source supplies this certificate or a whole-family lower bound.

Bounded test: specialize denominator clearing, retain w=0 and arbitrary
z,Z, and attempt a sufficient polynomial SOS certificate. An exact
global certificate at cost below 1/288 warrants continuation. A rigorous
whole-family lower bound at least 1/288 stops the family. Numerical
infeasibility, sampled failure, or failure of the SOS subclass does not.

Initial observations saved before computation: q>=|w|^2/2. Quotient
homogeneity should give a global C1 zero extension with quadratic
value growth and linear gradient growth. Off w=0, the cleared branch
is q^2(v^T H v-b(xz-y^2))-q DP4+P4 Dq, for b=0,1.
Continuity must restore the zero-set cases; the cleared values at w=0
alone cannot do so. The first global branch, integrated over each
single-frequency periodic generator in L586, should already imply
trace(H A(u))>=0 for every real u, including u=0. Thus no separate
frequency sampling can be used or is needed once that branch is proved.

The local Python environment has NumPy but no SciPy, CVXPY, Clarabel,
SCS, SymPy or mpmath. A bounded NumPy conic projection experiment is
possible; no solver claim or exact certificate follows from its residuals.

Completed bounded attempt: L594 contains the canonical C1/growth,
zero-set, cleared-branch and automatic-cone proofs, and the full exact
rejection of one rounded iterate. This is a specialization of the
known sufficient method, without a certificate at the requested cost.
The 35-coefficient quartic search used two 40-by-40 Gram matrices and
the stricter trial cost 1/300. A 12000-iteration projection and one
300000-iteration refinement leave residuals about 0.000939426 and
0.000925575 respectively. The refined affine Gram has a minimum
eigenvalue about -0.000690697. These are neither exact feasibility nor
infeasibility certificates; the stricter trial cannot decide costs
between 1/300 and 1/288.

The rounded refined iterate has exact cost in
(3440040029/10^12,3440040031/10^12), below 1/288, but its first global
branch is less than -1/200 at L594 Section 5's rational point. The
full exact candidate, point, intermediate evaluations and cost bounds
are in `../scripts/coupled-flux/rational_probe_candidate_violation.json`.
All selected exact inputs and load-bearing fractions were inspected;
the cleared identity and strict cost/residual comparisons pass. The
36 matrix entries and 35 coefficients in L594 match the certificate.
The random search only found a point; exact rational substitution
verifies its violation. Neither that point nor the slow numerical
residual proves a whole-family lower bound.

Outcome: EXPLORATION, one mathematical attempt. Preserve both full
probe artifacts and the failed candidate. This result does not justify
lengthening the same unpreconditioned projection. The unchanged ready
target remains suitable for a refined approach using acceleration-block
Schur conditions (including singular range cases) and covariance-scaled
variables, at the actual strict 1/288 threshold. No such reduction or
new certificate is derived here. Main signs and nonlinear Xi transfer
remain open; no new central-Xi creative mechanism is claimed.
