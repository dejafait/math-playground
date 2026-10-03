# 017 — 2026-10-03 — Persistent-root puncturing bound

Completed one mathematical attempt on the exact SPECIALIZE target in
the [saved assessment](../drafts/literature/2026-10-03-persistent-root-puncturing.md).
No literature retrieval or parked four-block calculation was repeated.
The proof in [L011](../lemmas/L011-persistent-root-puncturing-bound.md)
bounds the original bad set by twelve when D is nonzero and a coordinate
locator vanishes identically. This improves the requested bound of fifteen
and covers one class excluded from L010.

The covered BCHKS proximity input gives the auxiliary length-15,
dimension-8 bound of twelve. The new transfer argument accounts for
singular parameters and for input failure lost at the removed coordinate:
one failed transfer makes the whole original pair a fixed four-coordinate
residual family, with at most four bad parameters. Otherwise all original
bad parameters transfer. Multiple persistent roots and arbitrary
extension-field words are allowed. The
[calculation record](../drafts/2026-10-03-persistent-root-calculation.md)
preserves the unfinished reasoning and completed checks without replacing
the canonical proof.

Outcome: ADVANCE; STEP_KIND: RESEARCH; STEP_CLASSIFICATION:
POTENTIALLY_NEW. The auxiliary bound is known/imported mathematics;
the full transfer/count is not matched by the checked statements, with
no certified originality claim. STATUS remains IN_PROGRESS. Global
10/q–69/q bounds are unchanged: nonpersistent sixteen-count equality,
D identically zero and the July ABF26 comparison still need treatment.
No complete challenge candidate appears.

The next direction selects the singular class and a determinant/distance
test, rather than extending the now-completed persistent-root mechanism.
Its [assessment](../drafts/literature/2026-10-03-identically-singular-distance-transfer.md)
is REVIEW_REQUIRED because the hypotheses changed; no calculation on
that class was performed. The historical orbit stop, blocked source
retrieval, and exhausted exploration sequence are preserved. This
successful first persistent-root calculation ends its uninformative
exploration count; no launcher or retry state was changed.

Validation: `PYTHONDONTWRITEBYTECODE=1 python3 scripts/persistent-root/check.py`
passes the fixed-support lost-failure case, a singular error omitting
the persistent coordinate, and a codeword translation. The common-code
description and quantitative BCHKS hypotheses are checked in the proof;
prime-field examples are not used as extension-field upper bounds.
The shared documentation checker and local whitespace check also pass.
