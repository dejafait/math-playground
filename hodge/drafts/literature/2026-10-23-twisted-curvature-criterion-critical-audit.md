# Twisted curvature criterion — proposed critical audit

TARGET: Critically audit L149's equivalence between bounded twisted Chern curvature and vanishing of its central Hermitian cross block.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the October 16 and October 23 Chern/quotient and twisted spectral assessments; inspected L149's statement and full criterion proof through (12), L148's exact least-norm identity, ATTEMPTS/086 and the relevant recorded audit boundaries. No new external search, primary retrieval or independent mathematical audit is claimed.
SOURCE_EVIDENCE: Reuse the recorded coordinate and block-connection proof inspection in Demailly CADG (21 June 2012), V.12 (12.2)-(12.3)/Theorem 12.4, pp. 268-269, and V.14 Theorems 14.3/14.5 and (14.6)-(14.7), pp. 273-275; reuse BGS III Section 1(b)-(c), pp. 304-305, Theorem 3.5/Lemmas 3.6-3.8, pp. 342-345, and p. 350 Hodge decomposition through the twisted spectral assessment and audited L148.
COMPARISON: The recorded sources give Chern and quotient formulas on the puncture, not L149's full central-block equivalence; L150 evaluates the preferred metric's block but does not audit the curvature calculation.
GAP: Independently check both directions of the criterion, its full matrix leading coefficient and error control, retaining the natural quotient metric and every smooth higher term.
REASON: Separate scope approval now complete for exactly TARGET as a later REPRODUCTION audit of known-tool specialization; unchanged source hypotheses cover the required formulas, with no essential unread result. No audit verdict or new mathematical consequence is established.
LITERATURE_REASON: The saved gate requires separate approval of the newly proposed L149 critical audit; reuse existing coverage to check its scope, rather than repeat discovery for an already assessed coefficient.
SCOPE: Conditional L146/L148/L149 equality-family complex, integral c_1=0, ch_2=-14e_1-21e_2-tau_D, identical marked K3 factors/common metric, k=(-4,-2,1,2), one fixed smooth positive twisting-line metric and finite possibly empty Z.

The universal primitive Hodge gap and equality-kernel existence remain
open. This intermediate target checks the analytic criterion needed
before applying L150's now separately audited preferred-metric
cancellation. A successful audit could support a later bounded-curvature
application; extension and positivity require additional work.

Reuse `2026-10-23-twisted-harmonic-metric-curvature.md` for the precise
Demailly source links, inspected proof cases and exclusions of stronger
direct-image results. Reuse L148's recorded natural spectral comparison.
The essential mathematical inputs are L146's entire Koszul splitting,
L148's exact quotient identity and positive norm bounds, and L149's
full calculation. L150 is motivation and a later application input,
not a premise proving the criterion. L071 and the actual-family
assumptions remain retained through these inputs. No cross-notebook
input is proposed; full matching Mathlib coverage is not checked.

Continue if both the zero-block derivative bounds on a full punctured
ball and the nonzero-block curvature obstruction survive independent
verification. Check the first-slot anti-linear convention, constant
normalizations, all derivative and inverse-metric terms, the singular
value cases including equal values, and the claimed O(r^(-1)) remainder
against a nonzero r^(-2) coefficient. A precise failure requires repair
or narrowing L149, preserving the canonical calculation. This proposal
performs neither that audit nor a curvature application.

ATTEMPTS/086 parks evaluation for an arbitrary retained metric and its
unresolved scalar-variation route. Auditing the existing criterion is
a different, independently testable obligation, not another attempt to
evaluate that arbitrary metric. Empty Z is vacuous; F and nonempty Z,
extension, positivity, split-set control, reconstruction, transport and
universal primitive Hodge realization remain unresolved. This assessment
was REVIEW_REQUIRED at invocation start and was not approved during the
L150 audit. The separate source comparison below now approves its scope.


## Separate source-scope approval, step 483

The unchanged exact TARGET is ready for one mathematical audit. This
literature-only step is STALLED / NOVELTY_UNCHECKED: it supplies a valid
process approval using existing evidence, without new mathematical or
source evidence, and resets no mathematical exploration counter.

**Precise reusable inputs.** The recorded primary proof-case inspection
in `2026-10-16-split-harmonic-metric-curvature-energy.md` covers
Demailly, *Complex Analytic and Differential Geometry*, 21 June 2012,
Chapter V, sections 12 and 14, at the equation/theorem/page locations
in SOURCE_EVIDENCE ([text mirror](https://www.ime.usp.br/~cordaro/wp-content/uploads/2022/03/Jean-Pierre-Demailly-Complex-Analytic-and-Differential-Geometry-1.pdf#page=269)).
The Chern formula requires a smooth positive Hermitian matrix in a
holomorphic frame. The induced quotient formulas require constant rank
on the open set of application. L149 uses them only on the punctured
ball, where the boundary column is nonzero and its rank is one. They
supply no assertion across its zero at the center. The October 23
`2026-10-23-twisted-harmonic-metric-curvature.md` already compares this
changed coefficient with those hypotheses; the audit does not change
the coefficient, line metric, frame, connection or parameter domain.
Its recorded searches and exclusions remain adequate for this scope.
No repeated discovery or fresh PDF inspection is claimed here.

For the metric identification reuse
`2026-10-23-twisted-harmonic-metric-two-sided-bounds.md`: Bismut,
Gillet and Soulé, *Analytic torsion and holomorphic determinant bundles
III. Quillen metrics on holomorphic determinants*, Comm. Math. Phys.
115 (1988), 301-351, DOI 10.1007/BF01466774
([author scan](https://www.imo.universite-paris-saclay.fr/~bismut/Bismut/1988b.pdf)),
at the sections and pages in SOURCE_EVIDENCE. The arbitrary smooth
holomorphic Hermitian coefficient and smooth proper product projection
are within its assessed scope. Neither scalar self-duality nor curvature
positivity is required. The recorded natural projective-complex bridge
is Stacks Lemma 13.19.8, [tag 064B](https://stacks.math.columbia.edu/tag/064B),
used at the analytic stalk with finite free source, not as a global
projectivity assertion. L148's exact least-norm identity and uniform
positive bounds are the established local inputs; the general spectral
reduction is not to be reproved. These citations give no curvature
estimate at the jump.

**Difference still requiring audit.** L149 specializes these formulas
to the full L146 Koszul splitting. The central subspace identification,
zero-block full-ball derivative estimates, constant normalizations,
nonzero-block matrix coefficient and complete remainder bound are the
objects of the later audit, not source imports or results of this
review. Both directions must retain the anti-linear first slot,
inverse-metric terms, all smooth higher coefficients and actual metric
norms. Trace cancellation alone is insufficient; rank-one and equal
singular-value cases must be checked in the full matrix. A precise
failure requires repair or narrowing of L149, preserving its original
calculation. A source citation alone cannot settle these checks because
the inspected sources do not state this exact shrinking-boundary
criterion. Checking this specialization is justified; rederiving their
general Chern or spectral theory is not.

L150 is a later preferred-metric application, not a premise of the
criterion. Its completed audit does not verify L149. Conversely this
audit does not reopen the exhausted arbitrary-metric evaluation or the
parked scalar-variation mechanism in ATTEMPTS/086. The actual-family
inputs L146 and L148 retain L071; F and nonempty Z remain assumptions,
not existence conclusions. Empty Z is vacuous. Extension, positivity,
split-set control, reconstruction, transport and universal primitive
Hodge realization remain independent gaps. No new lemma, mathematical
script, argument overview or DAG change is warranted. Full matching
Mathlib coverage remains not checked; no cross-notebook theorem is used.
