# Step 492 — finite Selmer/height certificate attempt

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-25-selmer-height-finite-certificate.md`, with
its exact COVERED_TARGET matching the startup Next action. This is one
research attempt, not an additional source-comparison turn.

Main gap: rational rank versus arbitrary complex analytic order >=2.
Intermediate target: compose L001, L003 and audited L118 into a finite
certificate for V_2=0 at good ordinary p>=5. Intended use: remove the
Sha and augmentation defects for eligible finite inputs; uniform
arithmetic production and complex-order comparison remain unresolved.
Continue only if the full Selmer upper bound, torsion correction and
determinant enclosure imply all premises without assuming finite Sha
or nondegeneracy of the full rational height space. An unsharp bound
or a determinant enclosure containing zero is inconclusive.

Inputs inspected: L001/L002/L003; L118's filtration statement and
comparison, with its prior full audit retained; foundations/03/04.
Failure contrasts: L019 and ATTEMPTS/002/031. The existing source
assessment already checks duplication against L001/L003 and supplies
Milne, Harvey, Stein--Wuthrich and Ray coverage. No cross-notebook input.
All pre-existing unfinished changes are preserved.

Working proof plan (not yet a certified result): use the nonzero minor
to prove Q_p-independence, then the sharp Kummer bound to obtain
r=k and Sha[p]=0. A p-primary torsion group with no p-torsion is zero.
The points then span the rational space, giving the nonzero regulator
needed by L003; L118 converts delta=0 to V_2=0. The remaining finite
precision task is to scale an entrywise-certified matrix into Z_p,
prove a determinant error bound by multilinearity, and track all
polarization/normalization losses, including the empty case.

## Completed attempt

The composition is written in
[L119](../lemmas/L119-finite-selmer-height-vanishing-certificate.md),
with full hypotheses, proof, source qualifications and unchecked Mathlib
coverage. Classification: REPRODUCTION. This is a local conditional
certificate interface, not progress beyond the checked arithmetic sources.
The proof composes L001's Kummer bound, L003's height criterion and
L118's accounting, with their existing arithmetic scope retained.

The exact full Selmer threshold forces rank k and Sha[p]=0 after height
independence. Absence of p-torsion then forces all p-primary Sha to vanish.
The rational point lattice spans the rational space, with no saturation
claim; L003 and L118 apply only after these checks. The finite precision
proof gives det H in D_0+p^(N-ak) Z_p, where p^a scales both the entry
representatives and their errors into Z_p. Strict exclusion, k=0, k=1
and a nonintegral k=2 boundary case are handled explicitly.

Rechecked the already assessed Harvey Section 2.2 equation (3) and
Stein--Wuthrich Sections 4/4.1 equations for polarization and the ordinary
height. For the same equation/differential/canonical sigma, their quadratic
heights have scalar conversion -1. The numerical contract uses this
unnormalized height; logarithmic generator normalization is used only
for its exact nonzero scalar and does not silently preserve finite digits.
An explicit scalar-ball multiplication error rule is included for a
producer that actually changes normalization.

Meaningful mathematical checks were exact proof checks, not a numerical
preview: column telescoping proves the determinant bound for every k;
the k=2 diagonal example attains the nonintegral precision loss; the
Kummer equalities handle the torsion correction and empty case. No
mathematical script, unverified computation or new curve input is used.
The composed certificate still requires a separate critical audit.
No BSD candidate, general nondegeneracy theorem, uniform producer or
comparison with arbitrary complex order has been established.
