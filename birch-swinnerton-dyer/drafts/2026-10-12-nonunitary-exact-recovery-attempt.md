# BSD-172 — fixed nonunitary exact recovery attempt

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-12-nonunitary-exact-value-recovery.md`.
The only target is exact recovery of the oriented {1/6,infinity}
real integral divided by the total minimal period for y^2=x^3+1.
The main gap remains arbitrary analytic-order-at-least-two rank equality.
One exact symbol could supply a normalization test input, but leaves full
integral generation, coefficient production, rational directions, Sha
and complex-order comparison unresolved.

## Saved reasoning before finite work

Import Cai--Chen--Liu Section 3 p.3732's origin-preserving Q-isomorphism
(X_0(36),infinity)=E. Its Jacobian is E, and this is a degree-one optimal
parametrization. Apply Cesnavicius--Neururer--Saha Theorems 1.2/7.2:
8 and 27 do not divide 36, so its integral differential scalar divides
one, hence has absolute value one. Choose its sign to make c_0=1.
The source and target period ratios are one. No CM exclusion applies.

Wuthrich Proposition 1 and the audited L048 total-period convention
give an arbitrary-cusp lattice from good split-prime torsion reduction.
Here delta=6 and the cusp field is Q(zeta_6). Certify primes 7 and 13,
their good reduction, splitting and every affine point, then set T to
the gcd of their counts. Manin--Drinfeld and torsion injection give
T times each cusp image zero. With absolute differential scalar one,
T A_f({1/6,infinity}) belongs to the minimal period lattice. Its real
projection is (Omega(E)/2)Z, including this connected real locus.
Thus K=2T clears the desired rational value. Reversing Wuthrich's path
changes the sign only, not the lattice.

Use audited L051's exact outward interval as a named input; do not
produce a new analytic approximation or reuse an expected exact value.
Save every selected point-count entry and enumerate every reduced
rational with denominator at most K in that interval. Check also the
stronger K-scaled integer isolation. Continue only if applicability and
existence are justified and enumeration gives exactly one value;
otherwise preserve failure and stop this fixed attempt. L050 and
ATTEMPTS/025 concern a different, preserved representation failure.

## Completed fixed attempt

The canonical proof and precise source specialization are in
[L052](../lemmas/L052-nonunitary-cusp-exact-rational-recovery.md).
Both complete split-prime counts are 12, so K=24. Every denominator
1 through 24 was enumerated, and independent finite replay of all 20
x-entries, all actual y-lists and 624 numerator cases passes. The sole
reduced rational in L051's interval is -1/12; rational existence comes
from the independent lattice theorem. The certificate and report are
`scripts/nonunitary-cusp/exact_value_certificate.json` and
`scripts/nonunitary-cusp/exact_value_verification.json`.

This is ADVANCE in local known-method reproduction, not progress beyond
the sources checked or a BSD candidate. Separate critical audit of the
new applicability/isolation assembly remains pending; its coverage
proposal is REVIEW_REQUIRED for the next turn. The preexisting source
assessment and failed/audited analytic certificates were not changed.
