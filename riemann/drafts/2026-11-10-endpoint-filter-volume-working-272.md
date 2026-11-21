# Exact inverse stability: division-free volume test, step272

10 November 2026. One mathematical attempt under the unchanged, prior
EXPLORE assessment `literature/2026-11-10-endpoint-filter-inverse-stability-review-267.md`.
The exact E-to-S target is unchanged. Reuse its source comparison and
the audited L990/C990a contracts. Preserve the fixed anchor and complete
finite evidence in working271; do not enlarge the numerical horizon.

Main gap: L030-L032/C032a actual-Xi positivity and L966/L968 signed
forcing. The intermediate aim remains a homogeneous exact sequence
with finite positive exponential growth. It would obstruct unrestricted
recovery from one filtered observable, while leaving actual B_n,
arithmetic identification, shifted intervals, all prime powers, other
zeros, both complements and L984(H) unresolved.

## Saved analytic attempt

Test a block-volume route to the uniform finite-section problem. For
two solutions x,y retain the division-free discrete determinant
W_n=x_n*y_(n+1)-x_(n+1)*y_n. Subtraction of the exact homogeneous
rows gives c_(n,2)*W_(n+1)=c_(n,0)*W_n, including singular rows.
Only on an interval where the relevant pivots are nonzero may this
be written as a determinant product. A positive asymptotic lower
bound for that product could force an expanding direction in the
two-dimensional family; a separate upper bound and continuation
through singular rows would still be needed. It would not by itself
select the anchor x_32=1,x_33=0.

First discriminating test: evaluate the mean logarithmic determinant
of L990's leading coefficients with a fixed positive cutoff, retaining
every phase, and justify passage to the exact coefficients at that
fixed cutoff. Only subsequently consider removing the cutoff. Seek
a strictly positive lower rate; a zero rate abandons this particular
phase-averaged volume certificate, not all matrix-product mechanisms.
Do not exchange the cutoff and infinite-index limits, assert pointwise
logarithmic control from equidistribution, or divide through a singular
row. A useful bound must be uniform in section length; more finite
growth samples are not the test.

The leading reflection candidate is
R(phi,psi)=(-phi-2*pi/3,-psi). With
D=cos(phi+pi/3), C=cos(phi), E=cos(psi), T=sin(psi),
h=(-D*E+(D-C)*T,D*E,-C*T-D*E), this reflection exchanges
h_0 and h_2 and preserves h_1. Thus its l1 norm is preserved.
The leading row vanishes only at the finitely many phase pairs
D=T=0. These observations suggest a zero regularized mean, but the
exact-index transfer and all qualifications must be completed before
claiming an outcome. No new source theorem or cross-notebook input
is proposed. Full matching Mathlib coverage is unchecked.

## Completed test

NEGATIVE for the proposed positive fixed-cutoff volume certificate.
The exact all-index mean is zero for every fixed delta in (0,1),
below the strictly positive rate sought. The complete proof and
qualifications are canonical in
[L992](../lemmas/L992-endpoint-filter-zero-regularized-volume-rate.md).
Its exact-index proof bounds every collision-neighborhood contribution
at fixed cutoff; it does not use an unproved pivot, a shrinking-target
frequency or an interchange of cutoff and horizon limits.

The uncut logarithmic tails and the singular-row compatibility of a
prescribed anchor remain unresolved. Zero volume rate would not exclude
expansion in one direction even if an uncut limit were established.
The finite certificate of step271 is not extended, and the inverse
implication remains open. Stop this certificate and obtain a separate
conceptual audit before relying on the new obstruction. No numerical
or mathematical script was needed.
