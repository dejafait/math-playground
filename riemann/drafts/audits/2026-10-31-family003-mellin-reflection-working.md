# Full-frequency Mellin reflection — application audit

Work in progress, 2026-10-31. Approved target and SPECIALIZE scope are
the unchanged Mellin-reflection normalization assessment. This is a
RESEARCH / REPRODUCTION conceptual audit, not new source discovery.

Main gap: actual-Xi all-degree positivity. Intermediate target: check
the fixed-data analytic reflection underlying L541 Hypothesis 1 using
L547's cusp construction and the retained coefficient/Gauss bounds.
Downstream use: remove this one conditional analytic premise, without
claiming arithmetic uniformity, marked expansion, global closure or signs.

Test: check the horizontal chain rule and zero mode, direct/reflected
Mellin convergence and scalars, endpoint derivatives, continuation/strip
growth and contour shift. A failed interchange, surviving constant or
scalar mismatch stops the claimed implication at that point. L547's
independent review remains open. No cross-notebook input.

The ready source comparison and prior finite-cusp/phase work are reused.
No completed duplicate analytic audit was recorded in those sources.
Existing notebook changes are preserved; no mathematical script is needed.

## Checked reasoning before canonical write-up

For a fixed reduced cusp, write Q=q_c and u=1/(Qv). Substitution
in DR (5.1) gives z'=-delta/c-bar(z)/(c^2(v^2+|z|^2)) and
v'=v/(Q(v^2+|z|^2)). At z=0 their bar-z derivatives are
-1/(c^2v^2), zero for bar(z'), and zero for v'. Thus the constant
term contributes zero even after the coordinate change. The differentiated
reflection has factor -bar(kappa)/(c^2v^2) times the z derivative
of the raw H-cusp expansion at (-delta/c,u).

The direct Bessel integral gives i/4 (2pi)^(-2s) times
Gamma(s+1/3)Gamma(s+2/3) and bar(alpha(mu))q_mu^(-s).
The reflected substitution gives -2pi i c^(-2)Q^(2-2s)mu times
the integral of u^(2-2s)K_(1/3)(4pi|mu|u). This yields the
source's reflected scalar and Gamma(4/3-s)Gamma(5/3-s).
At t=1/2-s the scalar quotient is -i/81, with K=(2pi)^4/27
and kernel argument q_mu X/Q^2. These are symbolic equalities.

Absolute Dirichlet majorants converge for exponent beta>1:
sum_n q_n^(-beta), sum_b q_b^(1/2-3beta), and
sum_(h>=-4) 3^(h(1/6-beta)). The full lattice has |mu|>=1/9.
Its coefficients have polynomial size, so all differentiated Bessel
series converge locally uniformly and have exponential decay at large
height. The cusp identity gives v^(-A_j)exp(-b_c/v) at zero,
with b_c>0 depending on the fixed cusp. This supplies every log-height
integration by parts. Arithmetic-uniform endpoint constants are excluded.

## Completed verdict

All six checks pass at fixed arithmetic data; the canonical proof is
L548. In particular it takes rectangle height to infinity before epsilon
to zero, with a boundary constant independent of epsilon. It interchanges
the reflected series only on Re(t)>1/2, then shifts each individual kernel
to zero and proves absolute summability using its representation on a
larger line. No dual Dirichlet interchange on Re(t)=0 is asserted.

This is a conditional reproduction, not progress beyond the source's
claimed theorem. L541 now cites that fixed-data result; no uniform
kernel seminorm, marked expansion, coefficient/Gauss bound, global closure
or Xi sign has been proved. L547 and L548 await independent critical review.
No mathematical script or numerical certificate was used. The shell
source download failed at DNS, but browser retrieval supplied every
required proof range; no source blocker remains.

The next independent check is L547's canonical construction, using the
unchanged ready canonical-cusp assessment. Its required input is the raw
DR automorphy/cusp and reciprocity formulas, not the downstream results
L546, L548 or L541 that depend on it. No justified new central-sign
mechanism was supplied by this analytic audit; absolute convergence and
fixed-data reflection do not produce the missing sign bridge.
