# Step500 working checkpoint — 11 November 2026

Authorized target and prior SPECIALIZE gate:
`drafts/literature/2026-11-11-growing-window-mixed-pairing-498.md`.
Only the uniform full Hermitian low/high pairing is being attempted.
Main gap: actual-Xi positivity L030-L032/C032a. Downstream use: pay
one interaction, conditional on an independent low-block margin.

Partial reasoning saved before the canonical write-up: use L744(6)
and complex polarization, retaining both pole products. Cell neutrality
of u and C744n's exact correction kill the global moments. For the
uncorrected carrier, set p(x)=1+x^2+x^4 and
r=max(|xi|,|xi-t|)>=|t|/2. The scalar envelope is at most
[A+log(2+r)]/r^2 after division by sqrt(p(xi)p(xi-t)); this expression
is decreasing for r>=1. Weighted Plancherel/Cauchy--Schwarz therefore
appears to give 4 M0 M1 [A+log(2+T/2)]/T^2, uniformly in support.
For every delay, the second derivative of the translated envelope
product has L1 norm <=4 M0 M1, so two integrations by parts appear
to give the uniform T^-2 rate. C744n(5),(7)-(8) pay the entire
correction and arithmetic mass, respectively. Need final checks of
adjoint orientation, complex polarization and all constants.

No low-block sign, unrestricted decomposition, or RH conclusion.
Continue only if these estimates give O(T^-2 log T) with no K factor,
both profiles varying and both signs; otherwise preserve the obstruction.

Completed in `lemmas/C744o-growing-window-uniform-mixed-energy-bound.md`:
the explicit bound (12) closes this test, including the whole correction
and prime-power sum. This working checkpoint preserves the intermediate
reasoning; the canonical proof supersedes its tentative wording.
Separate critical audit remains pending; no low-block sign is supplied.
