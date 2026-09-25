# First-order localization of the actual diagonal class

Date: 2026-09-25. Initial selection saved before the detailed source audit.

## Gap, intermediate target, and decision test

The universal gap is rank E(Q) = m(E) for analytic order at least two.
In L006's restricted setting the missing input is q(kappa) = 0 in
V_p Sha. The achieved bound is r <= 2; the required lower bound is
r >= 2. L009 makes ordinary first-order lifting automatic, while
leaving the strict derivative Delta_d(res_K(kappa)) in a local
anti-invariant line undetermined.

This step tests that derivative using the actual anticyclotomic
component of the diagonal family. Audit its local conditions at
both split primes, its Coleman image, and reduction modulo T^2.
The intermediate target is a justified value or vanishing criterion
for Delta_d, retaining the ordinary local component. A Coleman
calculation alone need not compute the full local cohomology class.

If the family supplies a strict first-order lift, determine whether
this makes the proposed condition automatic under existing Selmer
hypotheses. If only its singular local image is controlled, isolate
the missing ordinary component and do not claim a computed value.
A nonautomatic constraint could help test a later Kummer criterion;
that implication, nonvanishing from complex analytic rank, auxiliary
existence, and the universal rank comparison would still be missing.

This does not retry L007 or L008's excluded representation contractions.
L009 and ATTEMPTS/007 already rule out the ordinary Bockstein test,
but do not use the actual family's full local condition. The source
sections to check are Castella--Hsieh 3.4, 4.2, and 5.3--5.5; keep
their named hypotheses and distinguish local finite and zero conditions.
Exploration turns entering this step: 0 of 3 without an advance or
informative negative result. No complete BSD candidate is proposed.

## Saved source audit in this turn

Theorem 3.6 and Corollary 3.7 of Castella--Hsieh give a full zero
localization at the conjugate prime, but a Coleman image at the
chosen prime. The rank-four local filtration contains the entire V
factor at the chosen prime; it does not select an ordinary complement.
Proposition 4.3 expresses the Coleman value through pairing against
a finite local class. The PDF text drops the bars on prime labels;
check the publisher's mathematical HTML before fixing those labels.

The ordinary component of the first local derivative is consequently
the relevant unknown. Pending checks: augmentation nondegeneracy of
the Coleman functional, theta divisibility by T^2 under kappa != 0,
and the factor and conjugation sign in Delta after averaging the
actual family lift. These source data have not yet computed Delta.
