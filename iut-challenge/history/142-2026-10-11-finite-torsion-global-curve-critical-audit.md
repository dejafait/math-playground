# 2026-10-11 — Finite-torsion global-curve audit

STEP_ID: 2026-10-11-142-finite-torsion-global-curve-critical-audit

The separate audit passes the unchanged existential statement in
[L044](../lemmas/L044-global-curve-preserving-local-finite-torsion.md),
where the full model, genus, pointed-Galois and fixing-kernel checks
are canonical. The primary theorem includes genus one and all torsion
orders; integer approximation retains the exact leading coefficient.
The result preserves the embedded field N via complete kernels, not
degree equality. This validates a local input from known sources;
it is neither a new constancy theorem nor an essential IUT flaw.

No error or new dependency was found. DAG and PROOF assembly stay
unchanged; all unfinished work and ATTEMPTS/022,025,026,027 are preserved.
No mathematical script or cross-notebook input was used. The remaining
global torsion/degree/selected-place and native/input/action/pilot/
essentiality bridges still separate this result from finite B>=A.

The next direction is a single torsion-adjunction bridge, changing the
global base field while asking to retain the local completions.
Its [coverage proposal](../drafts/literature/2026-10-11-global-torsion-adjunction-preserving-completion.md)
is REVIEW_REQUIRED. No result on that new target was derived or
approved during this audit; the next turn is literature comparison.
