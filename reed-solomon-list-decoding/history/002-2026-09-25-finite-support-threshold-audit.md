# 2026-09-25 — Finite-support threshold audit

The required shared and local overviews, existing changes, empty DAG, and
previous failed transfer were inspected and preserved. Renewed ABF retrieval
failed. A source locator in the adjacent MCA notebook led to direct inspection
of pinned primary ArkLib files; no lemma was imported across notebooks. The
[model freeze](../foundations/02-pinned-list-model.md) now records smoothness,
interleaving, closed lists, the base-field threshold, and grid boundaries,
without claiming recovery of the July PDF.

The one bounded mathematical test produced
[L001](../lemmas/L001-common-support-list-bound.md): common-support counting
gives an explicit bound independent of q and m, and a q^m-word witness excludes
the next point after n-k errors. It determines the grid boundary only under an
additional exponential field-size condition. The
[assessment](../drafts/2026-09-25-finite-support-threshold-audit.md) compares that
condition with the actual threshold and records the real-radius qualification.

This is ADVANCE, a partial mathematical input, with exploration turns 0/3;
STATUS remains IN_PROGRESS and no complete candidate appeared. The reason for
the next direction is quantitative: sharper field-independent bounds are
needed below the binomial field-size regime, so the claimed geometric
improvement is more relevant than repeating PDF failures or the rejected
q-polynomial transfer. The original route and evidence remain intact.

Validation: the symbolic proof was checked for support uniqueness, all witness
tuples, arbitrary characteristic, and endpoint inequalities. Seven exact toy
enumerations passed using `python3 scripts/finite-support/verify.py`; their
[output](../scripts/finite-support/results.json) is saved. The shared checker
was run with `--problem reed-solomon-list-decoding`. The DAG adds L001 with no
local lemma inputs; structural checking does not verify its mathematics.
