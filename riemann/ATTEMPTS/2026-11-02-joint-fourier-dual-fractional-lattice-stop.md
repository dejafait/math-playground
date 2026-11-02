# Uniform unit-pole joint Fourier dual: fractional-lattice obstruction

The bounded test nominated after the oblique saddle audit is obstructed
by [C645x](../lemmas/C645x-joint-fourier-dual-fractional-lattice-obstruction.md).
Its uniform contour proof forces dual norm at least
exp(251*n/8000)/(8*n*sqrt(2n+1)), exceeding C exp(n/32) for every fixed
C eventually. All 20 exact constant/rounding checks pass in
`scripts/one-sided-hankel/joint-dual-contour-certificate.json`.
The separate conceptual audit on 2 November 2026 passed without a
mathematical correction; its full record is canonical in C645x.

WHY IT FAILS: A test requiring anchor response >=1 and each other
unit-pole response >=-3/(2n) also controls positive fractional mixtures.
C645x constructs such a mixture with central weight one, total mass
<=n/3 and exponentially small spatial projection through degree 2n.
Thus the unit-pole constraints have discarded the distinct-pole and
integer-residue information needed to exclude this mixture. The
obstruction holds with arbitrary angular modes at this spatial cutoff;
enlarging only the angular rectangle cannot evade it. The mixture has
more than n/3 distinct poles and noninteger residues, and no full-symbol
or operator upper bound is proved. It does not refute the approved
angular target or RH.

Keep this specific dual parked after the completed audit of C645x.
Further work on the angular target needs a materially
different test using the joint integer/census constraints, or another
independently testable mechanism. Earlier entrywise-positivity and
zero-continuation stops are preserved and are not global bans.
