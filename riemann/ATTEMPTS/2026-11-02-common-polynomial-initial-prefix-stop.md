# Common multiplicity polynomial: initial-prefix restriction

The full residue decomposition and finite orthogonal grid energy are
canonical in [C645y](../lemmas/C645y-common-polynomial-retained-grid-energy.md).
The common polynomial P has its genuine integer degree M, and every
rotated-grid residue, including zero, is present in the full identity.
The new specialization has not received a separate conceptual audit.

WHY IT FAILS: Retaining only the first M grid coefficients does not
make their energy large merely because deg P=M. The exact nesting
identity identifies these coefficients with partial inner-input
responses. On C645t's already audited admissible family, every initial
prefix through ceil(n/2) has full response at most
22000*m*exp(-7*n/200), even with angle-dependent prefix selection.
The rate is strictly too small for exp(-n/32). Raw grid sample sizes
also retain the insufficient anchor rate; the inverse Gram factor
cannot be omitted. This stops the initial-prefix simplification,
not the full common-polynomial mechanism, the angular operator target,
or RH. The later grid coefficients and their shared degree constraint
are a materially refined, still unproved test. No separation or
coefficient-integrality assumption may replace that missing estimate.
