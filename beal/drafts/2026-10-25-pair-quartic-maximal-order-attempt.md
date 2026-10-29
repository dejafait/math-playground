# Direct quartic maximal-order attempt

Approved target: Determine a certified maximal order and field discriminant
for the quartic branch field of L110.

Main gap: primitive Beal signatures remain unexcluded. Locally the quotient
route lacks ranks and points. Intermediate target: compute the integer ring
of L133's integral quartic, enabling meaningful later ideal arithmetic.
Inputs are L110's branch polynomial, L132's irreducibility and L133's inverse
field maps. No cross-notebook theorem is used. The existing octic arithmetic
implementation is a local implementation reference, not a theorem input.

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-25-pair-quartic-maximal-order.md`.
The attempted mechanism uses the cited Stevenhagen Section 9 radical and
multiplier-order theorem, with exact rational/finite-field linear algebra.
Every square-dividing discriminant prime must be covered, including small
and ramified primes. No monogenic maximal-order assumption is made.

Before execution the cumulative caps are fixed at 250000 factor/divisor
trials, 128 strict enlargements, 2000000 instrumented scalar operations,
field dimension four and 4096 numerator/denominator bits. Both generation
and independent replay, including failed executions, share one ledger.
Completion requires full factorization, every terminal multiplier equality,
integrality of every multiplication table and 1, independent lattice replay
and the trace/determinant/index-square discriminant identity. A failure or
cap hit preserves partial evidence and ends this bounded target without
claiming maximality. Class/unit completeness, Selmer/rank, rational points,
marked lifts, degree-nine recovery, both L095 systems and other signatures
remain independent gaps.

## Completed calculation

The exact basis, full product table, trace matrix and terminal Frobenius,
radical and multiplier-minor certificates are canonical in
[L134](../lemmas/L134-pair-quartic-maximal-order.md). The certified field
discriminant is 2874960; the power-order index is 937500. This is local
arithmetic progress by specialization of known methods, not a new general
result or a rank/point/Beal conclusion. The quadratic-tower failure in
ATTEMPTS/058 remains intact.

`scripts/pair-genus-two/quartic_order.py` adapts the existing notebook's
octic radical/multiplier implementation to the exact monic degree-four
field. Its standalone arithmetic is instrumented through
`quartic_order_budget.py`. A mechanical AST transformation expanded numeric
operations, comparisons, sums and modular powers to the accounting API;
the final expanded source is saved, with no runtime AST transformation.
The producer performs eight strict enlargements (two at 2, one at 3,
five at 5), twelve sequential tests and four final-order tests.

The independent `verify_quartic_order.py` imports only accounting. Its
Horner field products, subset determinants and column ranks independently
check every full saved table, lattice, kernel and inclusion. The first
replay passed 959 checks. A code review found eleven primality-divisor
trials had been charged as scalar arithmetic but omitted from the
factor/divisor counter: seven at p=5 and four at p=11 across the sixteen
step records. Those eleven charges were added to the persistent ledger,
and the primality helper was corrected. No mathematical evidence changed.
The second replay adds explicit terminal invertible minors; all 967
checks pass with no failures. It preserves all earlier cumulative work
in the ledger; no counters were reset. Producer failure serialization was
also made independent of the arithmetic budget, and future interrupted
factorization retains its partial trial chain. No cap failure occurred.

Full evidence paths:

- `scripts/pair-genus-two/quartic-order-certificate.json`;
- `scripts/pair-genus-two/quartic-order-verification.json`;
- `scripts/pair-genus-two/quartic-order-ledger.json`.

Actual/caps, including generation and both replays: factor/divisor trials
94/250000; strict enlargements 8/128; scalar operations 591967/2000000;
field dimension 4/4; numerator/denominator bits 78/4096. The scalar count
includes arithmetic and numeric comparisons, including extra index and
mask arithmetic. Container/control bookkeeping, serialization, Fraction
normalization and internal bit operations are excluded. No failed
mathematical run or restart occurred. This count is not a bit complexity
or runtime claim.

The continuation is a separate critical audit of L134, with a newly
recorded REVIEW_REQUIRED assessment. It must check the theorem's exact
scope, final lattice integrality, radical equality, I_p/pI_p action,
complete prime coverage and the field map; it must not infer ranks,
points or Beal exclusions. The original main-target gaps listed above
remain unresolved.
