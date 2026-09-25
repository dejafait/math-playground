# Finite Selmer tower rank inference

Date: 2026-09-24. Outcome: informative negative for the specified data-only
inference; the descent method itself is not abandoned.

The proposed arithmetic intermediate target was a rank certificate from a
finite initial p-power Selmer tower, its transition maps, rank parity, and
restricted alternating pairings. Such a certificate could be used in a
later analytic-order comparison, which was not assumed or established.

## WHY IT FAILS

[L001](../lemmas/L001-finite-selmer-tower-rank-ambiguity.md) constructs rank-zero
and rank-two exact-sequence models with identical observed data through any
fixed depth N. The rank-zero model has finite torsion of exponent p^M with
M >= 2N and a nondegenerate pairing on the whole group, while its observed
restrictions vanish. Thus even these strengthened hypotheses yield only
r <= 2, with a two-unit ambiguity if even parity is granted. The models
are not asserted to arise from elliptic curves, and the marked rational
Kummer images are not part of the matched data. This refutes a deduction
from the specified group structure alone, not BSD or arithmetic descent.

Independent rational points, effective information about Sha, or additional
arithmetic structure would change the test. Merely increasing a preset
observation depth or repeating the same restricted-pairing check would not.
