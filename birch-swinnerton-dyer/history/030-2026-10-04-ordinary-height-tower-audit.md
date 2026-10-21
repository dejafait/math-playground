# 2026-10-04 — Ordinary height radical does not force formal Sha surjectivity

Completed only the ready COVERED_TARGET in
[the prior assessment](../drafts/literature/2026-10-04-cyclotomic-selmer-height-radical.md),
without new browsing. The audit and full proof are saved in
[L019](../lemmas/L019-ordinary-height-radical-with-compatible-sha-tower.md);
the intermediate reasoning is preserved in
[the working note](../drafts/2026-10-04-ordinary-height-tower-audit.md).
The first ordinary Bockstein is an isomorphism, unlike the relaxed
global Bockstein, so its height has zero radical while the marked
Sha quotient remains one-dimensional. Coefficient specialization
of the same integral complex preserves the full compatible tower,
every prescribed depth-two basis, all local triangles and the
divisible Cassels--Tate kernel.

This new compatibility test stops inference of radical surjectivity
from the listed formal package. It does not refute arithmetic
surjectivity under L018's actual hypotheses or realize an elliptic
curve/full Kurihara family. The result specializes known height
formalism and is not claimed beyond the checked literature. The
arithmetic bound stays r <= 2; r >= 2, actual rational determinant
membership, production of the two-prime premise, analytic comparison
and higher ranks remain unproved. STATUS is IN_PROGRESS; no candidate
exists. The failure is preserved in
[ATTEMPTS/019](../ATTEMPTS/019-ordinary-height-radical-surjection.md).

The next direction adds an actual rank-two derived arithmetic class
and seeks a point-valued comparison; it does not build another generic
height model. Its changed domain/hypotheses require an exact source
comparison, so [its assessment](../drafts/literature/2026-10-04-arithmetic-rank-two-exterior-certificate.md)
is REVIEW_REQUIRED. The existing Sano determinant and Kim structure
coverage is reused; it is not coverage for this arithmetic point
formula. Original Nekovar and Jones source blockers stay parked.
No new literature was reviewed in this research step.

Step BSD-2026-10-04-030-ordinary-height-tower-audit has outcome NEGATIVE,
kind RESEARCH, classification REPRODUCTION and actual task type
proof_audit. Exploration turns used are 0 of 3. The recommended next
settings are literature_comparison, standard/high, for theorem-domain
and hypothesis comparison rather than a difficult proof attempt.

Validation: `python3 scripts/cyclotomic-determinant/check_model.py`
passes, including the new ordinary Bockstein/height identities.
`python3 ../scripts/docs/check_structure.py --problem birch-swinnerton-dyer`
passes with 20 nodes and 18 unique edges. L019 uses L013's complex
and maps; L018's tower is a comparison specification, not a premise
asserting arithmetic realization of the model. No other mathematical
tests were needed, and no shared infrastructure or other notebook
was edited. Prior unfinished changes were preserved.
