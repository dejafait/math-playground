# Gaussian constructor728: mandatory root-bisection work stop729

Canonical proof: [C998v Section5](../lemmas/C998v-zero-inclusive-dyadic-gaussian-kernel-compression.md).
Full evidence: `scripts/separation-seven/spectral-block-compression-audit-729.json`.

WHY IT FAILS: The saved Python constructor performs at least111 certified
bisections for each of1139 roots, with17 interval Horner steps per
bisection. Counting only scalar arithmetic/comparisons, explicit stores
and successful loop advances gives113,912,529 source operations>10^8.
All other costs are assigned favorable zero. This stops this specific
implementation under the stated all-work convention; it is neither an
arithmetic-only count nor a universal compression lower bound. Independent
moment/recurrence regeneration and the exact root/weight replay uphold
the positive1171-term approximation and its7.353e-9 weighted error bound.
Those approximation results are retained. Storage, density, the local
term, full scalar, signed S3,H2 and Xi/global transfer remain unpaid.
A different algorithm needs its own preparation/validation ledger and
source gate; the historical stops and100-digit failure are preserved.
