# Step 308 — exact polyhedral subsystem witness, 2026-10-18

Reused the prior SPECIALIZE approval for precisely the selected
equalities, full original plane-domain intersection and moment signs.
[L086](../lemmas/L086-zero-plane-sign-equality-subsystem-is-feasible.md)
records the finite rational witness and complete certificate method.
The one Phase I run reaches artificial objective zero after 230 pivots;
all 776 construction and 139 independent original/raw verification
checks pass. Exactly 82 domain factors and 27 free moments are positive;
every selected original/raw equality residual is zero. No second LP or
remaining-mode test was performed. Original lift/reverse and vanishing
quadratic coefficients were checked before iteration.

Outcome NEGATIVE / RESEARCH / REPRODUCTION / calculation: this is new
evidence parking sign-only exclusion, using known LP tools rather than
a discovery beyond the checked sources. Exploration since the last
informative result resets to 0/3; the previous 2/3 conic explorations
and all failure evidence remain preserved. The first inspector call
before the model was saved found no file, and an ancestral inspection
needed PYTHONINTMAXSTRDIGITS=0; neither was a failed mathematical run.
The independent verifier was rerun only to report the exact zero indices.

The [working record](../drafts/2026-10-18-affine-sign-phase-one-working.md)
and [diagnostic stop](../ATTEMPTS/069-zero-plane-sign-equality-exclusion.md)
record scope. PROOF.md now parks this subsystem; DAG adds only L086's
direct inputs. A separate critical audit of L086 is the sole next action,
with its [new assessment](../drafts/literature/2026-10-18-affine-sign-witness-critical-audit.md)
REVIEW_REQUIRED for separate approval. The other 53 modes and independent
global/RS gaps remain unresolved; STATUS stays IN_PROGRESS and bracket
955–957 is unchanged.
