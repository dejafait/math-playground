# Approved quartic branch-field test — working record

The active target and prior SPECIALIZE gate are in
[the assessment](literature/2026-10-25-pair-quartic-field-tower.md).
Use L110's exact Q4 and L132's irreducibility. No cross-notebook input.
The main gap remains quotient ranks and point control. The intermediate
test is an exact quadratic-tower simplification of the quartic branch
field, potentially useful for the global arithmetic of two-descent.
Continue only with the assessment's certified maps and coefficient
improvement; an irreducible resolvent instead closes this shortcut.
Neither outcome supplies a Selmer bound or a Beal solution.

## Preparation saved before execution

The monic normalization has coefficients a=64/25, b=6/25,
c=-52/25, d=-7/25. The prospective scaled resolvent is
H(Y)=Y^3-6Y^2-2628Y-43128 with Y=25r.
This handwritten arithmetic is not yet verified. The planned producer
will reconstruct the formula, exhaust integer divisors of 43128, and
save every exact evaluation. An independent replay will check the full
evidence and all seven residues modulo 7. An integral defining polynomial
via alpha=25theta will have both field maps and basis checked exactly.
All computation is subject to the prior caps, including preparation,
divisor generation, rejected candidates and replay. No backend probe,
rank calculation, unit or class-group completeness is attempted.

Existing work is preserved, including unfinished L108 and ATTEMPTS/050–057.
The old Stoll assessment is reused only as downstream context. The
duplicate/failure search found no previous calculation of this field's
resolvent or tower. L126 concerns a different, octic field; it is not an
input to this calculation. The ready Conrad sources are reused without
additional browsing or a new general-theory proof.

## Result

The initial producer stopped before root enumeration: its accounting
observer accepted scalars but not a list-valued equality check. The
initial ledger is retained in `quartic-field-initial-observer-failure.json`;
recursive equality/observation repairs this instrumentation error.
The producer is resumed explicitly with cumulative charges, without
discarding the failed preparation. This is not a mathematical failure.
The completed proof and qualifications are canonical in
[L133](../lemmas/L133-pair-quartic-field-no-quadratic-tower.md).
All 48 signed divisor trials and the independent seven-residue test
certify irreducibility. There are no rational resolvent-root branches,
so no exceptional relative-factor case is deferred. The integral model
has inverse field maps and determinant 244140625, but height 109375
versus 64. All 164 replay checks pass with no cap hit. Cumulative charges
are 517 root/divisor trials, 5458 instrumented scalar operations, maximum
degree four and bits 47. Full artifacts are under
`scripts/pair-genus-two/quartic-field-*`.

This informative NEGATIVE result for the tower shortcut makes no
originality claim beyond the inspected sources. ATTEMPTS/058 preserves
the stop. A direct maximal-order/field-discriminant certificate is the
proposed distinct target, with a separate REVIEW_REQUIRED assessment;
it was not investigated mathematically here.
