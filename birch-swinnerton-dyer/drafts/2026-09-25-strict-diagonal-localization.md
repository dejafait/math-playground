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

## Resumed audit: first-order reduction

The publisher's mathematical HTML confirms the prime labels: the
full localization at overline{mathfrak p} is zero, while the Coleman
map is applied at mathfrak p. Section 5.5, (5.9)--(5.11), together
with its displayed characteristic divisibility forces
ord_T Theta = 2 r_1 >= 2 when kappa != 0: its proof gives t = 1 and
d_1 = 2, and both bounds then agree. This is an anticyclotomic order,
not the complex order or the rational rank.

Write Z for the diagonal Iwasawa class, normalized at T = 0 to
x = res_K(kappa), and let U = Loc_mathfrak_p(Z). Since x is strict,
U is divisible by T in the local module. The scalar reciprocity law
and Theta in (T^2) imply that the augmentation Coleman functional
annihilates u = (U/T)|_(T=0). The finite local line is the expected
kernel, so this gives u finite, not u = 0. Modulo T^2 the family
then has localizations (epsilon u, 0); averaging under the semilinear
tau-action gives Delta_d(x) = (u, -tau u)/2. This formula is pending
the exact local specialization and augmentation-kernel checks.

The new discriminating threshold is full U in T^2, whereas the
checked scalar law gives only Col(U) in T^2. An abstract local
deformation model can distinguish these two conditions without
claiming an arithmetic counterexample. No numerical value of the
ordinary derivative, Kummer membership, or new rank bound is saved
as established at this point.

## Completed assessment

[L010](../lemmas/L010-diagonal-local-derivative-and-coleman-kernel.md)
completes the local specialization, nonzero augmentation factor,
ordinary-kernel, and conjugation-sign checks. It proves the displayed
Delta formula and the exact full-localization divisibility criterion.
The prescribed full scalar series still permits arbitrary ordinary
first derivative in the local module; an explicit first-order diagram
also preserves the one zero localization and conjugation. Neither
construction claims a global arithmetic realization.

The informative negative is specific: the actual family's scalar
reciprocity law does not determine this stricter obstruction. Its
actual value remains unresolved. Before seeking another family
formula, the reason to change mechanism is that rational Kummer
classes have not even been shown to satisfy the proposed strict
lifting test. The bound remains r <= 2, short of r >= 2. This step
uses no exploration turn without an advance or informative negative.
