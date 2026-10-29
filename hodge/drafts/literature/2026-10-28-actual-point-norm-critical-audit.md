# Actual point norm — critical-audit source coverage ready

TARGET: Critically audit L178's trace-normalization bridge, prescribed point norm and nonvanishing k-line Gram test, including the conditional bound s<=781.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 599 compared the complete L178 proof, L169's trace conventions, L174's integral comparison, step 597's exact/stronger-result search and saved audit assessments; checked history/598 and ATTEMPTS/093,/095 against the retained /068,/092–095 screen. Focused primary-source retrieval below resolves the audit-specific scope without repeating broad discovery or claiming novelty.
SOURCE_EVIDENCE: Freshly read Cox alg-geom/9410017v1 Appendix A Proposition A.1 and complete proof, printed pp.19–20, and Proposition 6.1's connecting-map/cochain comparison, pp.14–15; Nayak–Sastry II 1903.01783v2 Section 5.1's setup, Section 5.2 and Proposition 5.2.3 with complete proof, pp.24–26, Proposition 5.3.1 with proof, p.26, plus (4.1.2),(4.1.5), pp.21–22; Stacks 0FVU Lemma 48.27.1(5),(7) and their proof cases, Remarks 48.27.2–3. Reuse the exact saved local-duality, uniform-weight, actual-point, residual-rank and joint-Atiyah audit coverage listed below.
COMPARISON: Cox supplies a global trace/Dolbeault theorem, beyond a projective-space computation; Nayak–Sastry fixes the projective normalization and comparison with supported/proper Verdier traces; Stacks supplies actual functorial evaluation. These cover the tools for auditing L178, but do not certify its identification of conventions, prescribed-vector norm or rank specialization.
GAP: No essential source gap identified for this exact audit. Mathematical obligations remain the global trace bridge, kappa=1, both coordinate factors in the bilinear norm, exact k-line sign, full eigenspace rank and empty-support case; s<=781 remains pending independent audit.
REASON: This separate literature-only comparison approves the unchanged TARGET as SPECIALIZE for a later RESEARCH/REPRODUCTION conceptual audit. Import the general trace/rank results and check their actual-family application; do not reprove general duality or treat source readiness as mathematical verification.
SCOPE: Exactly L178 under the unchanged identical marked K3/common forms/metric/connection/full character and actual arrows; reduced finite possibly empty Z, t<=46, and the prior s<=782. No section integrability, point rescaling, metric compatibility, radical-image vanishing or F existence.
LITERATURE_REASON: The invocation-start audit nomination was REVIEW_REQUIRED; step 599 compares its new global-trace and fixed-vector audit obligations with the ready parent coverage and primary passages. This is the required separate source gate, not extra browsing on the already ready norm calculation.

## Original nomination — step 598

The following records the pre-review audit specification. Step 599's
decision above now approves its source scope, not its mathematical result.

The canonical proof is `lemmas/L178-actual-atiyah-point-norm-and-k-line-gram.md`.
Essential local inputs are L108, L168, L169, L174, L175, L176 and
L177. The earlier source comparison is
`drafts/literature/2026-10-28-actual-atiyah-point-norm.md`.
No cross-notebook input is proposed.

The main gap is still uniform primitive cycle realization, with the
hypothetical F's existence unresolved. This audit could retain or repair
the conditional exclusion of s=782; it cannot settle those main gaps.
Check source scope first, reusing inspected theorem statements and
proof cases while hypotheses remain unchanged. Do not repeat broad
discovery merely to fill a literature turn.

The most delicate mathematical claim is
gamma=delta_B(2 pi i)^(-2). Compare the ordered projective generator
in both primary sources, the functorial normalization of their proper
traces on B, Cox's connecting-map Dolbeault convention, multiplication
by sigma_B and the even dualizing shift. A projective-space equality
without its global trace compatibility would not suffice. Retain
L169's previously audited internal-Hom/Koszul sign rather than applying
it twice. Compare the actual integral normalization of L108/L174 with
the reference defining kappa; distinguish the scalar gamma from the
sheaf isomorphism with that name.

After separate approval, an audit must also check
ell_z(w_k(z))=(2 pi i)^(-2), the two coordinate factors in the norm,
Tr(h_z^2)=2, chi_sigma's integral normalization, and the actual theta_z.
Verify c=gamma s/d as a complex bilinear scalar, then check the sign
of the rank-one subtraction using q(k,k)=-14 and audited Dk=4k.
Replay the exact root interval (39/56,6/7), all eigenspace blocks,
rank versus map rank, and s<=689+2t<=781. Empty Z uses U=0 and
the old rank-fifteen formula without a prescribed point vector.

Continue only if the actual convention bridge and every rank input
survive, or record a concrete correction and its effect on the bound.
Do not infer nonzero norm from nondegeneracy or replace a bilinear
square by an absolute square. No fifteenth point-free normal direction
or improved square capacity for the original quartic follows here.
Preserve ATTEMPTS/068,/092–095, actual section/radical data gaps and
all unfinished work. This audit is not a candidate-solution audit.

Next invocation first needs literature_comparison/standard/high for
this nomination's source gate. If approved, the mathematical audit
should use proof_audit/conceptual_audit, deep_research/xhigh: the
global trace identification and derived normalization are delicate,
even though the final integer inequality is elementary. An independent
creative bracket mechanism remains blocked by the lack of an evaluable
actual section image or geometric lower-square-length input; routine
normalization must not be relabelled creative.

## Completed source comparison — step 599, 2026-10-28

LITERATURE / literature_comparison / EXPLORATION / REPRODUCTION.
The exact target is unchanged. No lemma, mathematical script, DAG row
or PROOF paragraph was modified; no sign, norm or rank calculation was
performed. This is local source readiness, not a mathematical advance
or progress beyond the checked sources.

### Primary coverage and qualifications

Fresh inspection used the primary arXiv copies, retaining the parent
assessment's version qualifications. In Cox, *Toric Residues*,
[alg-geom/9410017v1](https://arxiv.org/pdf/alg-geom/9410017v1#page=19),
Proposition A.1, printed pp.19–20, covers compact orbifold varieties,
not only toric ones. It compares algebraic trace with integration of
the corresponding Dolbeault form. Its complete proof invokes the formal
trace properties and fixes the universal normalization by an ordered
projective generator and its integral. Proposition 6.1's relevant proof,
pp.14–15, specifies connecting maps and cochain signs; one cochain
identity is asserted without proof in the source. B is smooth projective
of dimension two, so it meets A.1's hypotheses. Import that theorem;
its global statement is essential. Equality of two functionals on a
projective-space generator alone is not an argument for equality on B.

Nayak–Sastry, *Grothendieck Duality and Transitivity II*,
[1903.01783v2](https://arxiv.org/pdf/1903.01783v2#page=24),
Section 5.2, printed pp.24–26, defines the ordered standard projective
generator. Proposition 5.2.3(i) identifies its Verdier trace with the
standard trace; its proof uses the section residue and (4.1.5).
The complete proof of (ii) and Proposition 5.3.1 relate completion and
regular-section normalization. The diagrams (4.1.2),(4.1.5), pp.21–22,
compare supported and proper traces for the same smooth structural map.
The reused author-PDF regular-section and oriented Ext comparisons
remain those recorded in the uniform-weight audit below; no identity
between the March arXiv and May author versions is asserted. For B/C,
proper smoothness applies; a reduced point is a section over C, not
a flat sheaf on B. These sources cover normalization and compatibility
tools, not the notebook's Dolbeault/dualizing-isomorphism comparison.

Freshly reread [Stacks 0FVU](https://stacks.math.columbia.edu/tag/0FVU),
Lemma 48.27.1(5),(7), their proof cases, and Remarks 48.27.2–3:
proper-field duality is functorial and shift-compatible, and the
pairing is composition followed by trace; bounded coherent inputs
give finite-dimensional perfect pairings. Smoothness gives the shifted
canonical bundle. This supports the actual counit application but does
not fix a numerical Dolbeault normalization by itself. B and the
retained coherent/perfect inputs satisfy this scope.

### Reuse, duplicates and remaining audit

Reuse these assessments in `drafts/literature/`, with their precise
primary versions, inspected proof cases and Mathlib qualifications:

- `2026-10-28-actual-atiyah-point-norm.md`: exact-statement and stronger-result
  discovery and the unchanged fixed-vector source comparison.
- `2026-10-25-point-quotient-serre-critical-audit.md`: shifted evaluation,
  finite trace composition and symbolic point coordinates (Stacks
  0AX4/0DV0/0G81/0G23/0FPC, as specified there).
- `2026-10-26-uniform-point-weights-critical-audit.md`: Nayak–Sastry I
  C.1–C.2/C.5 and II regular-section conventions, retaining the already
  audited internal-Hom sign and one global delta_B.
- `2026-10-27-first-factor-atiyah-point-critical-audit.md`: Kuhn's derived
  pullback/trace compatibility and the fixed actual top comparison.
- `2026-10-27-residual-atiyah-normal-rank-critical-audit.md`: actual
  duality, orthogonal decomposition and pinned Mathlib composition/rank
  declarations over C. No stronger equality of Gram and map ranks.
- `2026-10-28-joint-atiyah-square-bound-critical-audit.md`: the actual
  two-factor setup and fixed k-line marking; no point-free improvement
  follows from a normal direction with point projection.

The parent search found no exact theorem supplying this family's
prescribed-vector norm; L178 is now the local calculation to audit,
not a duplicate to derive again. ATTEMPTS/093 concerns adjustable
complementary lifts, while /095 lacks metric/Leray compatibility;
neither decides this fixed-vector question. The parent screen of
/068,/092–095 remains applicable. No stopped route is reopened.

The later audit must compare Cox's global theorem and connecting-map
convention with nu_B, chi_B, multiplication by sigma_B and the proper
counit, rather than rely solely on P^2. Then check the retained relative
normalization against kappa, both fixed-coordinate factors through
theta_z, the bilinear scalar square, L176's subtraction and all L174/L177
eigenspace blocks. Root bounds, rank direction, dimension comparison and
empty Z must be replayed without assuming the desired coefficient.
Do not double-count L169's internal-Hom sign, infer nonzero norm from
nondegeneracy, or assume that Gram-radical images vanish.

Continue by retaining or precisely repairing L178 only if those actual
comparisons hold. A failed convention bridge parks the scalar-dependent
strengthening and preserves the prior conditional bound and stop evidence.
No section quadric, lower square length, F existence, transport or uniform
primitive realization follows from source approval. Full matching Mathlib
coverage remains unchecked; supporting rank declarations are reused,
with no Lean build or absence claim. No cross-notebook input is used.

The next action stays exactly TARGET and is now source-ready. Route it
as proof_audit/conceptual_audit, deep_research/xhigh. No independently
evaluable actual section image or geometric lower-square-length input
yet supports a creative bracket target; do not manufacture one to meet
a scheduling preference or skip this essential audit.
