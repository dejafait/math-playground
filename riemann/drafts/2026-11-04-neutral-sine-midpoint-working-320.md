# Approved sine midpoint test, step 320

Completed: the proposed coefficient, domain and cutoff checks and the analytic negative bound are written in canonical L751. The remainder of this file preserves the saved pre-completion reasoning, not an additional theorem or current Next action.

Gate reused: `literature/2026-11-04-neutral-supersolution-certificate-coverage.md`, its exact COVERED_TARGET. No further source review or profile search.

In progress: use L744(6), L740's smooth domain, and the cited Frank–Seiringer p=2 identity. Write k(u)=2e^(-u/2)/(1-e^(-2u)), m0=psi(1/4)-log(pi), L=9log3, b=L/2, a=pi/L. The full multiplier should match m0+integral k(u)(1-cos(tu))du. At b the exact residual is m0+integral_0^b k(u)(1-cos(au))du+integral_b^infinity k(u)du minus the complete two-sided prime-power sum. Each surviving arithmetic term is nonnegative before subtraction; the others vanish by zero extension.

Candidate analytic certificate to check: k(u)<=e^(-u/2)(2+1/u), giving the first integral <=18a^2 and the exterior tail <=(4+2/b)e^(-b/2). Elementary log3>1, pi<4 and e^(-b/2)=3^(-9/4)<1/9 give total continuous increment <328/81. The sourced rational digamma value, gamma>=0, pi>3, log2>2/3 and log(pi)>1 give m0<-9/2. If all constants and coefficients check, R_h(b)<-73/162<0. This is only a rejection of this sine's sufficient pointwise test, not a negative neutral energy witness.

Still required before completion: establish the exact multiplier normalization, full killed ground-state specialization for complex compact tests, cutoff/domain finiteness and the explicit midpoint inequality. No numerical scripts needed if this analytic bound checks. Store the full argument canonically, preserve all old stops, then select one independently gated continuation.
