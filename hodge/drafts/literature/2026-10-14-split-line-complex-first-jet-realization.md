# Split line — determinant-fixed complex first-jet specialization

TARGET: Test determinant-fixed two-parameter complex analytic realization of L094's I-complex plane with its prescribed first jet.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the immediately completed split-line analytic-integration comparison; its scoped searches and duplicate/failure checks cover this explicit partial integration target, without claiming novelty.
SOURCE_EVIDENCE: BMM 1907.10690v2 Theorems 5.1/2.3, pp. 15/5--6, https://arxiv.org/pdf/1907.10690v2; Buchdahl--Schumacher (2022) Proposition 2.6/(2.4), pp. 83--84, https://d-nb.info/1262812674/34; Artin (1968) Theorem (1.2), p. 277, via inspected Rond (2018) Theorem 2.1, p. 122, and proof reductions pp. 123--126, https://www.journalofsingularities.com/volume17/rond.pdf. Original Artin full proof was not newly retrieved.
COMPARISON: Known tools cover holomorphic formality, split-module transfer, a finite analytic slice and preservation of a multivariable first jet. The explicit determinant-fixed specialization and actual formal-map/jet comparison remain to be proved.
GAP: Verify trace-free formality and determinant compatibility, relate L094's necessary ASD quadratic vanishing to the complex Yoneda equation, produce a compatible formal two-parameter map, place it in the analytic slice and retain its first differential by approximation.
REASON: This independently testable complex prerequisite is distinct from the parked fixed-metric quaternionic integration claim and avoids uncontrolled Green/curvature values; a partial realization would close only one local holomorphic requirement.
SCOPE: Audited L094's actual E=L plus L^{-1}, S,g,h,k and explicit W; complex structure I is fixed. One attempt may realize the prescribed I-complex tangent plane by an actual determinant-trivial locally free holomorphic family near zero in C^2. No exact quaternionic chart, stable punctured family, actual equality F, nonempty reducible locus, prescribed global mixed action or transport is assumed.

Use the [completed comparison](2026-10-14-equality-split-line-analytic-integration.md)
for primary versions, theorem/page numbers, relevant proof cases, applicability
and limits. Import the general theorems by those precise citations; justify
only the listed specializations. This assessment was separately source-reviewed in step 267; direct URLs
now appear in SOURCE_EVIDENCE. Its SPECIALIZE scope and target are unchanged.
Supervisor validation precedes a research invocation.

Essential input is audited L094 with L071's marked S,h,k through L025/L044
and foundations/05. Use b=a^(0,1) from L094 when specifying the prescribed
complex differential; verify the chosen C^2 identification rather than
assuming a tangent-normalized formality map. L095's conditional derivative
and L096's possibly empty reducible set are contextual constraints, not
existence inputs. L081 and L082 provide assessed general tools and a
comparison recipe only, not the present realization.

The main gap is universal primitive rational Hodge realization. A complex
local family could supply one prerequisite for a split equality-kernel
construction and delimit which difficulty is specifically quaternionic.
Independent quaternionic integration, actual derivative identification,
punctured stability, global kernel construction, mixed action,
reconstruction, separation and transport remain unresolved.

One bounded proof attempt may verify the trace-free DG-module splitting
and reductive automorphisms, the holomorphic quadratic restriction, and
the formal-to-analytic family bridge. If it establishes only one useful
intermediate input, record that result and the remaining obligations.
Continue only with an actual family and precisely matched determinant and
first jet, or a rigorous intermediate bridge. Stop the recipe at a failed
hypothesis or incompatible jet. Finite-order approximation must not be
called convergence of a chosen formal series or a quaternionic map.
Do not compute or assume an exact unitary ASD normal form; no scalar or
metric prescription is part of this target.

Preserve ATTEMPTS/061 and histories/237--240, history/261 and ATTEMPTS/046,
and the parked Green-operator curvature mechanism. No new mathematics is
derived or approved by derivation in this source-review turn. Matching
Mathlib coverage is not checked. Any stronger germ/connection/stability
target outside SCOPE requires REVIEW_REQUIRED separately.


## Separate source approval — step 267

LITERATURE_REASON: Supervisor recovery identified missing direct source URLs in this ready assessment; recheck only the cited hypotheses and access, preserving the existing target and comparison.

Reopened the three direct PDFs above. BMM Theorem 5.1 and its complete
p. 15 proof retain projectivity, trivial canonical bundle and linearly
reductive automorphisms; Theorem 2.3 retains its injective cohomology map
criterion, with the split DG-module sufficient case. Buchdahl--Schumacher
Proposition 2.6 requires a small closed input in the stated Sobolev norm,
p>2 dim_C S, and a correction orthogonal to ker(bar-partial-star);
the residual estimate and (2.4) identify integrability with the complete
holomorphic obstruction zero locus. Rond Theorem 2.1 requires convergent
equations over a characteristic-zero valued field and a formal solution
vanishing at zero; the variables are multivariables. Its proof strategy
uses Jacobian reduction, Weierstrass division and induction on their number.
These rechecks support reuse; they add no theorem or local specialization.

The prior completed comparison and ATTEMPTS/061 were inspected narrowly.
No new duplicate or changed failure was identified. Determinant-fixed
transfer, the quadratic comparison, the prescribed differential and
formal-to-analytic family matching remain mathematical obligations.
No original Artin proof, quaternionic chart, punctured stability or new
Mathlib coverage is claimed. Outcome is STALLED: a valid source-link repair
with an unchanged ready continuation, not mathematical progress or a
reset of exploration usage. No lemma, mathematical script, DAG or argument
overview is changed.
