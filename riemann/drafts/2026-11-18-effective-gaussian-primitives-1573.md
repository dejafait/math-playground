# Effective Gaussian primitives — work checkpoint1573

Approved target: the exact TARGET in assessment1572, reused unchanged.
One analytic specialization, not another dictionary solve. Main gap:
L030-L032/C032a actual-Xi all-degree positivity. The downstream test is
the unchanged dictionary1570 residual below 1/2; stop1571 remains valid.

Initial reasoning checkpoint: use the even test (G_sigma(z-r)+G_sigma(z+r))/2 in the
imported explicit formula. The prospective profile representation is
the pole term minus c/(4*pi), the subtracted archimedean integral
of [exp(-sigma*t^2)*cos(z*t)-exp(-t/2)]*B(t)/(2*pi), and the full
prime-power sum exp(-sigma*log(n)^2)*cos(z*log(n))*Lambda(n)/sqrt(n)
divided by 2*pi. Normalization and error propagation still need checks.

Proposed way to pay the noncompact primitive: prove an explicit
uniform bound |p_sigma(x)| <= C*(1+log(1+x)) for real x>=0 directly
from the subtracted formula. This would give a computable O(log(T)/T)
spatial tail, independently of unprovided zero coordinates. On the
compact part retain C032m's h(z^2) removable quotient, including the
origin; use Cauchy integrals to propagate disk errors without division
by x^2+w^2. No sign, residual or numerical practicality is established.

Continuation test: explicit uniform prime, archimedean, spatial and
finite-approximation errors must all tend to zero in an ordered cutoff
scheme. Otherwise record the precise failed obligation and stop.
Inputs: C032m/q and the inspected primary formulas recorded in
notes1572/1555. All inherited divisor/multiplicity, zero-ordinate,
strip/counting, finite-zero, heat and fixed-v1 qualifications remain;
no global p sign, density, moments or individual zero coordinates.

## Completed attempt

The complete derivation and all constants are now canonical in
[C032w](../lemmas/C032w-effective-shifted-gaussian-primitive-evaluation.md).
The method passes the analytic continuation test: the finite entire
profile approximation, logarithmic spatial-tail bound and polynomial
removable primitives have explicit uniform absolute errors converging
to zero in an ordered cutoff scheme. It awaits an independent audit.
No mathematical script or residual computation was performed.

This is local progress by specialization of an imported formula, not a
claim of mathematics beyond the sources checked. The initial uncertainty
above is preserved as work history, not as an outstanding formula claim.
Numerical practicality and the variation2 threshold remain unresolved;
stop1571 is unchanged. No justified covered central creative mechanism
has emerged from this evaluation result. Its noncompact tail and error
propagation require a conceptual audit before implementation or reuse.
