# 2026-10-04 — Pinned forest nonlinear Ward specialization

Reused the saved SPECIALIZE assessment for the exact target, with no
additional literature work. Preserved existing changes and all stopped
branches. [L016](../lemmas/L016-forest-compensated-nonlinear-ward-identity.md)
gives the unique pinned compensator, retains its path derivatives, and
proves that the reduced-Haar divergence equals the full-link divergence
pointwise on the slice. The compensator divergence restores the omitted
tree-link contribution. Both existing nonlinear Wilson-flow probes
therefore have the same full and reduced Ward insertion.

The [working record](../drafts/2026-10-04-forest-compensated-ward-calculation.md)
was saved before the algebra check. The exact rational check
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/forest-ward/check.py` passes for
two N=4 forests, including reversed paths, nontrivial gauge coordinates,
the differentiated retraction, action derivative and plaquette divergence.
Both compensator terms are nonzero, so the test detects discarded path
derivatives. These samples support the all-mesh proof; they do not compute
Wilson expectations or a continuum limit.

Outcome: **ADVANCE / RESEARCH / REPRODUCTION**, a completed finite
representation input using the assessed known mechanism. No new discovery
beyond the checked literature or improvement of the reflected-error bound
<= c_box/2 is claimed. Physical-boundary subtraction, finite interacting
matching/remainders, continuum construction and finite positive mass
remain unresolved. STATUS stays IN_PROGRESS, with no complete candidate.

The exact nonlinear comparison needs no further audit. The next covered
subcase tests its free linearization against the existing gauge-quotient
Ward calculation, to make the induced forest operator usable with L011's
Hessian. This is preapproved in the unchanged assessment, so no new source
review is needed. No inconclusive mathematical exploration turn is spent;
the earlier exhausted bulk-locality branch remains preserved.

Validation: the shared documentation checker with --problem yang-mills
passes (16 nodes, 27 unique edges). Whitespace, unique checkpoint fields
and exact ready COVERED_TARGET matching pass. The direct mathematical
inputs in the new DAG row were reviewed; no earlier lemma, script or
literature assessment was changed.
