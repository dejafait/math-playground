# Single first-prime Green correction: working record

2026-10-30. One research attempt under the unchanged EXPLORE assessment
`literature/2026-10-30-weil-first-prime-adjoint-correction-coverage.md`.
No result is asserted by this checkpoint.

Main gap: actual-Xi all-degree positivity; this branch also lacks the
signed endpoint flux bound. Intermediate test: remove the leading
interior cusp at d=log(2) from L518's adjoint residual while keeping
coefficient one on tau_L. A successful local correction might make a
later nullvector-specific signed pairing more informative. It will not
itself settle the endpoint scalar residual, other primes or flux signs.

Retain exactly L513--L516's fixed model and normalization and L518's
full residual, exterior tail and raw cutoff identity. Scoped duplicate
and failure checks: L518; raw-adjoint, generic-pole and nullvector-
multiplier ATTEMPTS records; prior source working record. No matching
correction was found there. Existing uncommitted work is preserved.

Proposed construction, still to justify: select a nonnegative smooth
localizer eta supported strictly inside I around d, away from other
prime cusp locations, eta=1 near d. Put q(x)=w_2 eta(x)v(x-d) for
x>d and q=0 otherwise. Let q_m=min(q,m), z_m=G_I^(-1)q_m using only
the positive killed reference, and take a monotone L1 limit z.
The proposed corrected weight is f_L+z, residual R_L+q-Bz.

Obligations: finite reference exit bound and symmetric Green kernel
give L1 convergence and admissible transposition; prove Gz=q in
distributions. Use the assessed diagonal/half-line Green estimates
to show z(d+s)=o(v(s)) and control all translated z values in Bz.
For the weak identity first take the raw cutoff epsilon to zero at
fixed m, then m to infinity; do not treat f_L+z as an operator test.
The coefficient one must follow from the exact limiting pairing,
not from a presumed zero normalized V-trace of z.

Continue only if all three obligations hold with the full signed
arithmetic residual. Stop this single correction if a leading cusp
survives or it needs a full A_I inverse or trace vanishing. No correction
iteration, new boundary theorem, H1 assumption, nullvector existence,
positivity or Xi realization is approved. Only the already assessed
GR reference inputs are to be used; their original proofs remain
imports. Full Mathlib coverage is unchecked.

## Completed disposition

The single construction is written in canonical L525. The L1 potential
limit, full first-cusp o(v(s)) bound and coefficient-one pairing pass
the local derivation; they await independent conceptual audit. The
scalar endpoint obstruction survives, and the paired correction is
zero against any assumed bounded nullvector. No iteration or trace
annihilation follows. Only the already assessed source statements and
essential kernel cases were retrieved for exact application; no new
literature discovery or mathematical script was performed. The initial
obligations above are preserved as a record, not unresolved duplicate
proof notes. The new audit continuation needs separate approval.
