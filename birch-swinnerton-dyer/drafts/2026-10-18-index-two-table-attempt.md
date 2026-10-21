# Step 321 — bounded index-two multiplier table

The main gap is arbitrary-curve rank equality at analytic order at least
two. The approved intermediate target is the complete table of L080's
entire multiplier order, in the original H field. A successful table
could support a later local maximality test; complete units/classes,
descent arithmetic and the general rank comparison remain independent.

Use the supplied SPECIALIZE assessment
`literature/2026-10-18-index-two-multiplier-table.md`, audited L067,
L077, L078 and L080. The exact known multiplier basis keeps m_0,...,m_46
and replaces m_47 by m_47/2. Existing L080 replay covers the old table,
not this new one. The scoped duplicate/failure comparison is already
recorded in step 320; ATTEMPTS/041 and 042 remain preserved.

Plan one producer using transported old structure constants, followed by
one independent verifier using full original-H polynomial remainders.
Retain all rational transports and inverses, actual identity, old-order
inclusion, index two and every integer product slot. Use scale 62=2*31
in the new integer polynomial representatives, retaining the original
scale 31 explicitly. Each stage includes validation and reporting and
has a strict external 180-second cap; combined artifacts have a
134217728-byte cap. Any failure or cap stops without retry or iteration.

The single execution passed both stages: production 0.684513 external
seconds, verification 0.971167, both below 180. Full independent replay
checks all 110592 coefficient slots and 2304 ordered products, all
transports/inverses, identity and exact index two. Zero rational fallback
steps were needed, but general Q[T] division is implemented. Both stage
failure lists are empty; all 435 originals are preserved. Full evidence
is in `scripts/seven-torsion/index-two-table-321/`; canonical reasoning
is in L084. Combined artifacts are below 4.8 MB against 134217728 bytes.
No retry, cap change or maximality test occurred. The construction is
known-method reproduction, with separate critical audit pending.
