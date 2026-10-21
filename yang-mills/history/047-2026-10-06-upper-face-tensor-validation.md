# 2026-10-06 — Validate the separable finite-mode implementation

STEP_ID: YM-20261006-047-upper-face-tensor-validation

EXPLORATION / RESEARCH / REPRODUCTION; actual task implementation,
under the unchanged SPECIALIZE combined-response assessment.
Applied [L033](../lemmas/L033-upper-face-separable-heat-moment-tail.md)
with L008 and L030–L032 to implement the tensor/Laplace contraction.
All second-index components and pure-sector axial parts are retained.
The [working record](../drafts/2026-10-06-upper-face-tensor-validation.md)
and `scripts/combined-ward-response/continuum-tensor-certificate.json`
contain the full evidence and limitations. At M=4, the pointwise heat
contraction agrees with dense assembly to scaled error 8.25e-15; at M=12,
all retained sector parts reproduce the existing values within 4.55e-13.
No failed checks were recorded. This reproduces finite-cutoff diagnostics;
no new mathematical theorem, certified sign or full coefficient is claimed.

Continue with a bounded cutoff-112 tensor diagnostic within the same
approved target, checking coefficient/time refinement there. Small-cutoff
agreement is not an integration enclosure. L019 compensation, the other
jets, the complete logarithm and reflected error <= c_box/2 remain open.
Preserve the exhausted mechanisms and unfinished work. Mathematical
exploration usage is 1 of 3 after L033; no supervisor state was edited.
