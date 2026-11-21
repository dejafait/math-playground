# 2026-11-05 — step480, central signed residual calculation

Used the preexisting SPECIALIZE gate for exactly the saved fixed n=0,d=5
target. [L792](../lemmas/L792-central-index-five-signed-collision-margin.md)
records the known-method specialization, signed residual about
+2.943474175e-10 and two exact collision distances exceeding4.5e-9,
with the complete original parameter box and analytic coefficient error.
The full certificate is
`scripts/central-jacobi/signed-residual-certificate-480.json`:
CERTIFIED_STRICT_INTERIOR, 140 checks, no failures. All four critical
brackets and values were inspected in full. No degree or D change,
model rescue, external source refresh or cross-notebook import occurred.

The preserved first-pass certificate failed only an unjustified harness
expectation that the signed residual be negative; both collision checks
passed. The final check records the actual nonzero sign. Input data and
residual formulas are unchanged. This is a local quantitative advance
using known methods; root reality alone is covered by the cited stronger
Jensen literature, and there is no new all-degree result or RH candidate.

The DAG adds L792's directly used normalization, evaluator and fixed-model
inputs. PROOF.md is unchanged because the main assembly and its unresolved
gap are unchanged; it remains a short selective overview rather than a
catalog of every finite diagnostic. Existing unfinished work is preserved.

The [separate audit nomination](../drafts/literature/2026-11-05-central-signed-residual-audit.md)
has REVIEW_REQUIRED coverage pending next-turn approval. It targets the
new normalization/critical-value evidence, not another L791 audit.
A central creative nomination is still blocked by the absence of a
concrete signed growing-degree mechanism; this successful finite test
does not supply one. No exploration budget is reset by relabeling work.
