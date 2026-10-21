# Exact Fourier quadrature — bounded working record

STEP_ID: YM-20261006-051-exact-fourier-quadrature

The main gap is the complete interacting Ward coefficient and ultimately
the reflected error <=c_box/2. The gate-approved combined-response
SPECIALIZE assessment is reused. This attempt tests only its numerical
specialization: exact 144-point Gauss–Legendre quadrature on the four
panels [-3,-5/2], [-5/2,0], [0,5/2], [5/2,3] for
F_h(n)=integral x^h rho(x) exp(i(pi/8)n x) dx.
The threshold is 1e-12 H_h uniformly for h=0,1 and |n|<=224.
Passing supplies only the quadrature part of L035's coefficient-input
hypothesis; failing a sufficient estimate does not prove the rule inaccurate.

Inputs: L008's exact rho, L034–L035 and the Integrals class in
scripts/combined-ward-response/check_continuum_pure_sectors.py.
The supplied overview/DAG and targeted records show no existing certified
quadrature bound. ATTEMPTS/016 concerns propagation, not this input bound.
The general flow/matching theorems remain imported by the precise citations
in drafts/literature/2026-09-26-current-target.md; none bounds this rule.
Elementary quadrature analysis is needed for this particular cutoff.
No claim of novelty is made.

The transition panels have smooth nonanalytic endpoints. A direct
analytic-ellipse theorem is therefore insufficient. Exact Gauss polynomial
integration and positivity can instead reduce the problem to uniform
polynomial approximation, retaining endpoint effects. Refinement will be
used only as a diagnostic. Stored-node/phase/transform rounding, weights,
tensor arithmetic, L019 compensation and other Ward terms remain open.

## Completed attempt: ADVANCE / REPRODUCTION

Propose a degree-200 Chebyshev polynomial p on [5/2,3]. Its
coefficients are exact dyadics from a NumPy proposal, not assumed accurate.
Verify rho-p separately with 80-decimal-place outward integer arithmetic:
full polynomial Taylor jets, order-24 rho jets and analytic remainders.
In the disk of radius r=min(c-5/2,3-c)/16, write u=9-z^2,
v=z^2-25/4. Their perturbations obey D=6r+r^2<=min(u(c),v(c))/8.
If the smaller real value s<=1/2, the smaller exponential is dominated
by the larger with ratio <1/2. Otherwise the phases of both exponentials
are <16/49 radians. Both cases give a nonzero denominator and |rho|<=2.
Cauchy therefore bounds the order-24 Taylor remainder on a cell of
halfwidth l by 2(l/r)^25/(1-l/r). Endpoint collars of width 1/256
instead use |rho-1| or |rho|<=e^-41/(1-e^-41).

If the full cell certificate proves epsilon=sup|rho-p|<=1e-12, a
degree-86 polynomial for the phase suffices on each transition panel:
degree 200+86+h<=287. On the core use phase degree 286, so the
extra factor x for h=1 still stays within Gauss exactness.
The Bernstein ellipse parameter 4 bounds the phase errors by
2*3^42/(3*4^86) and 2*3^207/(3*4^286), respectively.
Positivity and exactness of the degree-144 Gauss rule then bound the
four-panel errors by 2 epsilon+2(1+epsilon) delta+10 delta_core
and 6 epsilon+6(1+epsilon) delta+25 delta_core.
The canonical proof, qualifications and reproduction commands are in
[L036](../lemmas/L036-exact-fourier-quadrature-bound.md). All 565 cell
bounds, coverage, analytic disk conditions, coefficient degrees and final
rational inequalities pass. The maximum rho residual is below 3.48e-14;
the exact quadrature errors are below 7e-14 and 2.1e-13, against 6e-12
and 9e-12. All relevant certificate fields and the all-cell audit were
inspected. The audit checks every saved cell but does not independently
recompute Taylor jets; their justification is the canonical interval
arithmetic proof and complete generating script.

Two initial runs stopped on rational serialization/type errors. Both were
repaired; analytic remainders are rounded outward to the fixed scale for
storage, and integer strings are explicitly parsed. The completed run has
no failed cells. Neither repair changes the mathematical upper-bound logic.
This establishes one exact numerical input using standard methods, with
no claim beyond the checked literature. Stored-transform errors remain
unbounded. Continue under the unchanged response assessment by enclosing
those errors within 5.93e-12 and 8.79e-12; together with L036 this would
supply L035's normalized coefficient hypothesis. Essential inputs are
L008, L034–L036 and the Integrals implementation. All earlier unresolved
assumptions and preserved stopped routes remain as stated above.
