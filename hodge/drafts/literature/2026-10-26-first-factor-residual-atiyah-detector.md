# First-factor Atiyah detector after removing the base tangent image

TARGET: Assess whether the first-factor trace–Atiyah map supplies an independent detector after removing L173's base-tangent image, using the actual two-factor Gram form.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 582 repeated the notebook-local first-factor/other-factor/two-factor Atiyah and Gram/Schur duplicate screen in drafts/literature and ATTEMPTS; inspected the primary contraction statement and its complete relevant proof, and Nesterov's product-family comparison. Queries, inspected scope and unread leads are recorded below; no matching completed local residual-rank test was found.
SOURCE_EVIDENCE: Freshly read Buchweitz–Flenner arXiv:math/9912245v1, Section 4 through Proposition 4.2 and Corollary 4.3, printed pp.28–29, https://arxiv.org/pdf/math/9912245v1#page=28; reuse Corollary 4.8 and L173/L165's actual Serre-transpose coverage. Read Nesterov, Quasimaps to moduli spaces of sheaves on a K3 surface, published online 17 May 2024, Sections 2.1–2.2 through the statement of Proposition 2.3 and the statement of Corollary 3.2, https://doi.org/10.1017/fms.2024.48.
COMPARISON: The primary formula explicitly covers H^1(T_X), and its coefficient contraction/trace rule covers the operations needed for all self and mixed blocks. It supplies neither the specialized two-factor Gram entries nor their residual rank. Nesterov's curve-base and enlarged HT^2 hypotheses do not supply the needed second rank-twenty H^1(T) detector on this surface-base product. No injectivity theorem is imported.
GAP: In a later research step specialize the inspected contraction/trace identities with both pulled-back H^1(T) inputs, normalize against L173's actual base block, retain the full prescribed mixed tensor, and test residual Gram rank. Independence, nonzero residual rank and extra bracket constraints remain unproved.
REASON: The essential source gap for this bounded rank test is now covered. Reuse the known identities rather than reprove them; the actual two-factor specialization and residual calculation are the remaining work. This literature turn derives no Gram formula, rank or lemma.
SCOPE: The same hypothetical locally free rank-two F on the identical marked K3 product, integral c_1=0, full prescribed ch, actual connection, fixed forms and actual j,r,a,Q; unknown s,t and possibly empty Z. No cross-notebook result, semiregularity injectivity, metric-star compatibility, arbitrary section integrability or F existence.
LITERATURE_REASON: The invocation-start assessment was REVIEW_REQUIRED specifically for the two-global-H^1 contraction and mixed-pairing scope; the ready base-only assessment did not cover that specialization.

## Covered test, not a mathematical result

The main gap remains primitive realization and existence of F. The
intermediate question is whether using the other factor's Atiyah
component adds an actual linear obstruction constraint after L173
has removed the base tangent component. It could tighten the allowed
normal-plus-point quadratic lift; it need not settle either remaining
operation or construct a cycle.

Let the first-factor Atiyah image mean the map from H^1(S_1,T_{S_1})
to H^2(X,End_0(F)) obtained by contraction with the trace-free
S_1-cotangent component of At(F), using the same first-order convention
as L173. This describes the map to be assessed, without assuming its
rank or any analogue of L116 for the other projection. The base image
already reviewed is i I H^1(B,T_B). Its Q-restriction is nondegenerate.

The bounded proposed mathematical test is to compute the self and
mixed Serre pairings of these two actual images from the applicable
contracted-Atiyah/Chern-character formula. Remove the component in
the fixed base image by its Q-orthogonal projection and inspect the
remaining Gram form (equivalently the corresponding Schur complement).
A proved positive rank would certify independent residual directions
and justify determining their extra obstruction constraint. A zero
Gram form would not by itself prove the residual map zero: a nonzero
complex isotropic image remains possible. If the Gram test has no
nonzero rank certificate or cannot be determined from the actual
inputs, park this particular rank test, preserve that limitation and
require a materially different evaluable input before repeating it.
No rank, Gram entry, inequality or resulting detector is derived here.

The source comparison below checks Corollary 4.3 for cohomological
tangent classes rather than only ordinary vector fields. The later
specialization must retain its factorials, signs and trace normalization.
Reuse Corollary 4.8's annihilation scope; do not re-prove it or assume
injectivity. L071's prescribed mixed tensor
must be retained in any later calculation; the needed normalization
passages of L108 and the current L173 are local inputs, not a license
to read unrelated branches.

This proposed mechanism differs from ATTEMPTS/093's unrestricted
scalar-isotropy lifts, /094's unweighted cyclicity and /095's missing
metric-star comparison. It requires a new actual two-factor rank
test, not repetition of their failed tests. Preserve those stops and
ATTEMPTS/004,/009,/068,/092. Essential input results are L071, L108,
L116, L165 and L173, with their retained hypotheses; no other-factor
Leray splitting or kernel existence is assumed. L166/L167 explain
the downstream quadratic-operation gap without evaluating it.

With this source coverage, the proposed mathematical purpose is
proof_attempt/creative, deep_research/max: the precise obstruction
is possible dependence of the first-factor Atiyah image on the
already detected base image; the decisive bounded evidence is the
rank of its actual residual Gram form. This routing is a proposal
for a later approved attempt, not permission to calculate during the
current literature-only turn. Full matching Mathlib coverage is unchecked.

## Completed primary comparison, step 582

In [Buchweitz–Flenner, v1, printed pp.28–29](https://arxiv.org/pdf/math/9912245v1#page=28),
Definition 4.1 uses Tr(exp(-At)) and includes the factors 1/k!.
Corollary 4.3 has domain H^{r-1}(X,T_X), so r=2 is explicitly
the global H^1 case. Its k=1 component compares semiregularity
of contraction with -At against contraction with ch_2. The
preceding construction makes contraction a derivation on the
shifted coefficient algebra, and trace commutes with coefficient
cup operations. The complete Proposition 4.2 proof uses precisely
that compatibility, the derivation rule and graded cyclic trace;
it does not restrict to vector fields. These are the inputs for
a second contraction; the two-input specialization is still to
be written. Corollary 4.8's commutator annihilation is reused from
the completed parent review, not reproved here. No simplicity,
stability or semiregularity injectivity is a hypothesis of these
identities for the locally free F in question.

The proposed application has smooth projective X and locally free F,
so perfectness is available. Both tangent inputs will be pulled back
to X, where the theorem applies before selecting factor components.
This avoids imposing any other-projection Leray concentration.
The trace-free comparison must retain the determinant component:
the source's degree-one character is Tr(-At)=c_1, which is zero
under the stated hypotheses. L173 also records why a scalar Atiyah
component pairs trivially with a trace-free obstruction input.
These facts authorize checking the projection, not replacing At
by c_1 or discarding its nonscalar component.

All four ordered self/mixed pairings are within the covered
coefficient-operation scope. The research step must show the
Yoneda order and tensor shifts explicitly; use the source's shifted
grading, not only the exterior degree. Fix the sign comparing its
-At convention to L173's first-order convention, and use L165's
matrix trace, product volume and common normalization throughout.
The calculated base/base block must agree with L173's nondegenerate
restriction. No entries, scalar ratios, cancellation or rank are
asserted by this review. No new theorem beyond these identities is
needed for a bounded computation of the remaining blocks.

## Stronger results, duplicates and limits

[D. Nesterov, Sections 2.1–2.2](https://doi.org/10.1017/fms.2024.48)
works with a K3 surface times a nodal curve and a sheaf flat over
that curve. Lemma 2.2 treats the contraction comparison, with
HT^2(S)=H^0(wedge^2 T_S) direct sum H^1(T_S) direct sum H^2(O_S).
Proposition 2.3 assumes ch(F)_f wedge ch(F)_d is nonzero and finds
an HT^2 direction with zero fibre contraction and nonzero degree
contraction. Its statement is not restricted to H^1(T_S).
Corollary 3.2 assumes nonzero quasimap degree beta and gives a
surjective semiregularity cosection. The surface base here and the
two fixed H^1 domains do not meet those precise product-family
hypotheses. Thus that stronger detector conclusion is not an
import for this target, and no reproof or extrapolation is proposed.

Local comparisons: L173 supplies the actual base image and its
transpose; L165 supplies Q and the orthogonal splitting. Neither
evaluates the first-factor map. ATTEMPTS/093 leaves the complement
unrestricted, /094 uses cyclicity alone, and /095 lacks a metric
comparison. The present test instead proposes a characteristic
pairing computation with two actual Atiyah inputs. The search also
returned earlier Schur-form positivity and Schur-block tests; they
do not contain this contraction comparison. Preserve all their
stop evidence. No exact residual Gram result was found in the
notebook paths searched; this does not certify originality.

Queries actually run: `"Atiyah" "two" "contraction" "Chern character"
Buchweitz Flenner`; `"K3" "product" "Atiyah" "semiregularity"`;
`"Atiyah" "Serre" "pairing" "Chern" "H^1"`;
`"K3 surfaces" "product" "semiregularity" Atiyah`;
`"Atiyah class" "Gram" K3`. Primary retrieval then focused on the
exact BF statement/proof and Nesterov's hypotheses. Search results
also included recent claimed K3-product/Hodge resolutions and
abelian secant-sheaf work; those manuscripts were not inspected,
are not inputs, and no correctness or theorem-level comparison
is claimed for them. No external result here replaces the local
main target with a known special case.

The reusable parent assessment is
`2026-10-26-trace-atiyah-semiregularity-actual-obstruction.md`;
its all-obstruction references are stronger in obstruction order,
not an asserted independent-factor rank result. L071's specified
D and full tau_D, L108's normalized KS inclusion, L116's actual
arrows, L165's trace and L173's audited base lift remain essential
local inputs. Full matching Mathlib coverage is unchecked; no
absence claim is made. There is no source-access blocker.

## Continuation and decision test

The exact TARGET is now covered with DECISION SPECIALIZE. A single
later attempt may compute the actual 40-dimensional two-factor
Gram form and its residual after projection to L173's base image,
with complete sign/normalization and determinant checks. This is
a specialization of the cited identities; the residual detector
mechanism has not been established in the sources checked. A
strictly positive residual rank is the continuation certificate.
If the Gram form is zero or the required entries remain unevaluable,
park this rank test; zero complex Gram does not imply zero map.
An independent isotropic image would need a materially different
test. A positive rank alone also does not identify its normal/point
placement, evaluate section brackets, prove F exists, or resolve
primitive Hodge realization. No calculations, new mathematical
claims or lemma changes were made in this literature-only turn.
