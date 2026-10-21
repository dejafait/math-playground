# Retained adjacent-cusp specialization — critical-audit source scope ready

TARGET: Critically audit L059's actual Tate quotient normalization, valuation-one adjacency, common regular-model comparison and equivariant contraction yielding c(1)=plus-or-minus Q.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step 211's exact searches and duplicate/failure comparison under unchanged hypotheses; inspected full L059, L056's retained model statement, L057's ordered-component/deck-map ranges and completed audit, and ATTEMPTS/031. Targeted extraction located Conrad 5.5 and 4.7 as precise audit inputs; source versions, proof cases and access limits are in drafts/2026-10-14-retained-adjacent-cusp-audit-source-review.md.
SOURCE_EVIDENCE: Direct primary coverage: Tate Isogenies theorem/construction/full proof pp.16–17, https://people.math.harvard.edu/~ctm/home/text/others/tate/tate-unif/tate-unif.pdf ; Cremona introduction and section 2.1 theorem/full proof pp.1–3, https://johncremona.github.io/papers/component.pdf ; Liu 2006 Example 8.3.53 pp.365–367, Lemma 10.3.21 pp.513–514 and Corollary 10.3.25 p.515 with relevant charts/proofs, https://rexresearch1.com/GeometryLibrary/AlgebraicGeometryArithmeticCurvesLiu.pdf ; Conrad 2015 Definition 3.6, Proposition 3.7, Theorem 3.10/Remark 3.11, Corollary 4.7/full proof p.12, Theorems 5.4 and 5.5/full proof pp.14–15, Remark 3.14, https://math.stanford.edu/~conrad/BSDseminar/refs/minimalmodel.pdf ; reused Milne 2021 II.1.7 p.49, https://www.jmilne.org/math/Books/EC2.pdf , and audited L053,L056,L057 coverage.
COMPARISON: Known inputs cover the general algebraic isogenies, split-node resolution, minimal-model domination and contractions; Conrad 5.5 supplies the exact minimal-Weierstrass/Neron identity bridge, while 4.7 separately covers the W-side minimal-resolution criterion. They do not establish L059's actual-map label; component-count and first-blowup specializations still need an independent mathematical audit.
GAP: Audit W's minimality before using 5.5; distinguish Cremona's rational quotient from geometric components; test domination counting, the actual valuation-one first blowup, cyclic order and preserved component subset, and contraction/marking/log/deck-map compatibility over unchanged N. No audit verdict or global/numerical conclusion is imported.
REASON: Essential general source coverage now suffices for this single critical audit; the newly located identity bridge resolves a source-scope omission without deriving the actual specialization. Step 213 remains an unaudited known-method result, not retroactively uncovered or rejected.
SCOPE: Critical audit and necessary citation/applicability repairs of L059's stated retained component mechanism, using known inputs and REPRODUCTION only. Excludes the parked annular atlas, arbitrary generator relabeling, field changes, arbitrary finite-map extension, global selected/theta data and original finite B>=A.
COVERED_TARGET: Critically audit L059's actual Tate quotient normalization, valuation-one adjacency, common regular-model comparison and equivariant contraction yielding c(1)=plus-or-minus Q.

Step 214 completes source approval only. The detailed review is
`drafts/2026-10-14-retained-adjacent-cusp-audit-source-review.md`.
Full proof obligations below remain for the later mathematical audit.
No lemmas, mathematical scripts, PROOF or DAG were modified in this turn.

LITERATURE_REASON: The exact saved audit target entered as REVIEW_REQUIRED;
the explicit minimal-Weierstrass/Neron identity bridge and the new
component-count/first-blowup use needed source comparison. This is not
additional discovery on the unchanged ready specialization target.

Retain L059 and its actual inputs L053,L056,L057, with their inherited
L045,L048,L051,L054,L055 hypotheses. Keep E_0,F,K_glob,Omega,u,w,
H subset N, M>=max(M_tors,31), changed r=q_0 with v_3(r)=30,
fixed pointed Tate isomorphism, actual alpha,psi,gamma,0_B,Q,c.
L058's audited compatible splitting remains independent context.
Neither K_glob=N, r=3^30 nor the desired c-label is an audit premise.

The proof constructs lambda by factoring the algebraic Tate power
map through alpha and uses i=lambda gamma^(-1) for the model
comparison. It does not assert an unproved equality with a guessed
annular chart or extend the finite map b to regular models. Check
this exact normalization and the origin before comparing components.

For the minimality argument, verify the standard W's Weierstrass
minimality and use Conrad 5.5 to check the meaning of Cremona's E^0(N)
before counting Neron components. Conrad 4.7 is supplementary W-side
coverage, not an automatic result about D. Test the domination argument
from each m-component resolution and the passage from smooth components
to vertical components without assuming minimality of a resolution.
For adjacency, inspect the two first-blowup charts at the smooth
valuation-one point and at the intersection with the strict transform
of the original component. Check that subsequent split-node resolution
does not change either. Then check translation order, geometric cyclic
order, spacing n of the seven retained components, contraction
uniqueness, and the equality of actual marking sections and deck maps.

A pass validates only the local label; a failure must identify the
exact unsupported inference and preserve the rest. Full selected/theta
data, actual input/action/pilot/essentiality and original finite B>=A
remain unresolved. Full matching Mathlib coverage is not checked.
