# Centered Taylor band construction — scoped stop367

The approved m_n=n equispaced grid was tested with the centered Taylor
rule (center t=2n), allowing every truncation order 0<=m<=n and padding
the unused grid coefficients with zeros. The full grid family is open.

WHY IT FAILS: [C997r](../lemmas/C997r-centered-taylor-band-norm-defect-obstruction.md)
proves an actual norm/defect dichotomy for this rule. At m>=n/24,
the exact original coefficient variation grows at a positive exponential
rate. At lower orders a uniform last-term and phase-separation argument,
combined with the already assessed real Laguerre bulk formula, forces
the complete weighted defect to grow at rate at least 1/64 up to a
polynomial. Thus no choice of truncation orders pays both requirements;
the retained boundary cannot repair that simultaneous failure. This
is not a lower bound for the point residual and not an all-grid or
all-measure obstruction. Step369 independently audited and accepted
this scope and both uniform branches, without changing the bounds.
Preserve stops314/315/364
and C997i/m/p; do not repeat this Taylor rule without materially new
input or a different construction.

Audit369 replayed all 21 exact scalar checks and verified the complete
coefficient, phase-projection, fixed-J bulk-peak and target-subtraction
argument in the canonical corollary. The existential onset and the
sufficient-only residual criterion remain qualifications. The different
continuation is source assessment of direct complete-residual minimax
approximation with free grid coefficients and budget exp(sqrt(n)); no
new residual bound or source approval is claimed.
