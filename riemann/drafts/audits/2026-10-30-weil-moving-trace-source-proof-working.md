# L519 moving-trace source-proof audit — working record

2026-10-30. Gate: the supplied SPECIALIZE assessment
`drafts/literature/2026-10-30-weil-moving-trace-source-proof-audit-coverage.md`.
One conceptual proof audit; classification REPRODUCTION. The earlier
import/application check is preserved and is not being repeated as a
new result.

Main gap: actual-Xi all-degree positivity, with eigenvalue-relative
arithmetic flux cancellation still missing in the L516 route.
Intermediate target: verify L519's two physical trace limits under
exactly its assumed nullvector and dilated strong L2 convergence.
Use: a justified limiting boundary functional for a later arithmetic
test; neither vanishing nor a rate follows. Continue only if bounded
data, moving forcing and both entire signed integrals suffice without
new hypotheses. Otherwise record the missing condition.

Read paper 67 v1 (27 October 2026), Section 7 (7.1)–(7.6), especially
the paragraphs after (7.5) and (7.6), at
https://rstation.ai/problems/riemann_hypothesis/papers/67. Reused the
existing moving-interval assessment's duplicate/failure comparison
and L513/L515's audited fixed-model statements. No new source hunt.

Checkpoint before full write-up: use s=ell/ell_* and fixed interval
(0,ell_*). Compressed convolution becomes the integral of translations
by t/s against the SAME finite signed measure. Strong continuity of
translations and total variation domination give forcing convergence
from the eigen-equation, without comparing unbounded generators.
The interior pairing has weight sqrt(s)v(sx); its near-zero integral
is bounded by H V(s epsilon), using actual physical h bounded by H.
For the exterior pairing use r=ell_*-x and weight
sqrt(s) integral_0^infinity v(s ell_*+t)n(t+sr)dt. Check its entire
tail, uniform logarithmic L2 bound, pointwise convergence and reflection.
These were pending proof checks at the initial checkpoint.

Completed: the full independent argument is in
[L519](../../lemmas/L519-moving-interval-eigenvector-trace-convergence-import.md),
under “Separate source-proof audit, 2026-10-30.” Both physical trace
limits pass under the existing assumptions. The common measure is
unchanged, the near-zero error is at most 2H V(L epsilon), and the
whole exterior weight has an L2 majorant proportional to
1+|log x|. The forcing limit uses the bounded eigen-equation and
strong translation continuity, not a moving unbounded-operator limit.
No extra premise, new lemma ID, mathematical script or DAG edge is
needed. This is local validation of the inspected source assertion.

For selecting a distinct continuation only, read L516's remaining
signed criterion, L518's raw residual conclusion, and the recorded
generic-pole and automatic-support stops. A narrow search for cusp,
microlocal, parametrix and translated-singularity terminology in
Weil assessments/stops and L512–L519 found no match. This does not
establish novelty or source coverage. A proposed interior cusp
transport test is REVIEW_REQUIRED, with no derivation attempted here.
