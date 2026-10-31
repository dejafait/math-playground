# 2026-10-31: effective actual-Xi Hermite derivative tails

STEP_ID: 2026-10-31-hermite-effective-tail-calculation-01

RESEARCH / REPRODUCTION / ADVANCE: the approved quantitative test
succeeds with C=16. Canonical proof:
[L564](../lemmas/L564-effective-hermite-derivative-tail.md).
It bounds the complete theta kernel, all coefficient indices and the
entire derivative tails, and gives error <=exp(-8T), stronger than
the required exp(-2pi T), for every T>=1. No numerical sampling or
unknown onset is used. This is local progress supplying explicit
dependence absent from the inspected source statements; no novelty
beyond those sources, sign result or RH resolution is claimed.

The new DAG row uses L018–L020 for actual-Xi normalization; Romik and
DLMF are external inputs stated precisely in the canonical proof.
L233/C233a provide downstream motivation, not positivity premises.
Existing unfinished work and historical route stops were preserved.

Next: separate coverage approval for the independent L564 audit,
as recorded in
[the pending assessment](../drafts/literature/2026-10-31-l564-effective-tail-audit.md).
Signed truncation margins, multiplicity-compatible transfer and all
higher signs remain unresolved. No justified central creative target
has yet been identified from this absolute error alone; inspect this
quantitative input before proposing a signed mechanism.

Scoped documentation validation passed:
`python3 ../scripts/docs/check_structure.py --problem riemann`.
The L564 edges were checked against its actual normalization uses;
structural validation is not an independent mathematical audit.
