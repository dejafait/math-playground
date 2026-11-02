# Fixed mixed correlation — bounded calculation checkpoint

Approved target is exactly the saved SPECIALIZE assessment
`drafts/literature/2026-10-31-jacobi-mixed-correlation-admissibility.md`.
No change of Q, endpoint subtraction, identity or Xi-sign claim.

Essential inputs read: L019, L600 in full and the real-axis proof
in L239. L233 is downstream context only. Existing ordinary-L2 stop
does not decide this mixed term. No duplicate proof was found in the
scoped mixed-correlation records.

Working calculation to complete and check: set a=5/2,
R(u)=exp(a*u)Q(u). L600 gives R bounded, with endpoint limits
-12/pi at minus infinity and zero at plus infinity. With x=s+t,
exp(-5t)M(t)=integral k(x)exp(-a*x)R(x-2t) dx.
The weight k(x)exp(-a*x) is integrable and strictly positive by
L019 and the real-axis bound in L239. This supplies all fixed-shift
and compact-t domination. Dominated convergence should give the
positive-translation limit -(12/pi)integral k(x)exp(-a*x)dx,
and the opposite normalized endpoint zero. Complete the continuity
and signed translated-test proof before accepting non-temperedness;
pointwise growth alone is not the distributional test.

Main gap: actual-Xi all-degree signs at unbounded heights. This
admissibility prerequisite can park only the fixed uncorrected M as
an ordinary tempered Fourier component. Complete first-kernel identity,
independent residual bound and higher signs remain unresolved.

Continuation discriminator: use one fixed nonnegative smooth compact
bump and prove exponential signed pairing growth versus polynomial
Schwartz seminorm growth. If cancellation prevents that averaged
bound, leave temperedness unresolved. No numerical script is needed.

Completed: the full proof is canonical in
`lemmas/L601-jacobi-mixed-correlation-not-tempered.md`. It proves
every-shift convergence and continuity, both scaled endpoint limits,
and the noncancelling translated-bump obstruction. The unfinished
independent audit is the sole checkpointed continuation; this working
calculation is no longer a separate open task.
