# Charge-seven family-form critical audit — source coverage ready

TARGET: Audit L062's Chern--Weil/Yoneda normalization and pointwise injectivity using the primary family-form conventions.
CHECKED: 2026-10-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the prior family-form assessment; searched Huybrechts--Lehn 10.3.3/factor/errata, Mukai family-form Chern normalization and Kodaira--Spencer curvature terminology; inspected the exact cited passages and a primary curvature-character formula. No inspected source certifies L062's particular coefficient.
SOURCE_EVIDENCE: Kuznetsov--Markushevich math/0703264v2, Section 2, Theorem 2.2 and (12)--(14), complete relevant family proof pp. 9--10 and analytic scope p. 8; Huybrechts--Lehn 1997, 10.1.6--8, Example 10.1.9, Definition 10.3.1, Lemma 10.3.3 and Proposition 10.4.1 with proof; Bismut, Index Theorem and the Heat Equation, ICM 1986 proceedings (1987), p. 492, equation (0.2).
COMPARISON: Primary inputs cover family KS/Yoneda/trace, Newton factorial and the ordinary curvature-character convention; their abstract Hodge/Serre identifications do not explicitly fix L062's ordered integral normalization. The coefficient and pointwise inference require an independent proof audit, not another existence theorem or a new family-form derivation.
GAP: Audit L062 (2),(4)--(6), retaining exterior order, both mixed terms, factorial, simultaneous KS sign and holomorphicity; distinguish the explicit integral from the printed Serre-duality form before deciding which scalar assertions and differential conclusions are justified.
REASON: Newly inspected primary curvature normalization completes coverage for the proposed critical audit; it does not certify the audited identity or construct F. Reuse these inputs in a mathematical audit next turn.
SCOPE: Only L062's conditional family at the unchanged marked S,h,tau_D, with L044/L052/L060 retained. No global algebraic moduli placement, injectivity on points, embedding, metric equality, normal bundle, inverse transform or transport.
COVERED_TARGET: Audit L062's Chern--Weil/Yoneda normalization and pointwise injectivity using the primary family-form conventions.

## Relevance and source-review boundary

The main gap is algebraicity of every primitive rational Hodge class,
already unresolved on arbitrary fourfolds. This route also lacks global
F and transverse transport. The intermediate target is an independent
audit of L062's conditional family-form identity and differential.
Its downstream use is deciding whether this local constraint may serve
as an input to a future moduli construction. It supplies no such
construction and no new algebraic class.

This literature-only turn approves the audit's coverage. It does not
perform the representative calculation, certify the coefficient,
repair L062 or independently verify injectivity. Those are the
next research task. Keep the completed L062 attempt and its evidence.

## Inspected conventions

Reuse [the earlier assessment](2026-10-06-charge-seven-classifying-symplectic-pullback.md)
for family hypotheses and local simple-sheaf scope. Targeted inspection
of [Kuznetsov--Markushevich, arXiv:math/0703264v2,
19 October 2007, Section 2, pp. 8--10](https://arxiv.org/pdf/math/0703264v2#page=9)
confirms the smooth-projective hypotheses, the simple-sheaf and analytic
scope, and the KS/Yoneda/trace pullback formula. The proof's final
Kunneth comparison uses a binomial coefficient for the traced total
Atiyah power. Its exterior-form notation is not an explicit evaluation
rule for L062's Dolbeault representatives. It cannot certify that
coefficient just by citing the displayed family formula.

[Huybrechts--Lehn, *The Geometry of Moduli Spaces of Sheaves*,
1997 text, printed pp. 219--221, 223--224 and 227--228](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=231)
defines Newton classes as traced Atiyah powers with an i! factor
relative to character components. Section 10.1.7 gives relative trace
and graded cyclicity; Section 10.1.8 and Example 10.1.9 identify KS
through the parameter Atiyah component. Definition 10.3.1 uses the
Newton component and Serre duality, while Lemma 10.3.3 describes the
ordered family pairing. Their displayed identifications do not explain
the analytic integral's numerical trace prefactor. Proposition 10.4.1's
full proof compares composition/trace to perfect Serre duality. This
is the relevant nondegeneracy input, not a proof of a particular
family's pullback or injectivity.

The relation between the Newton component and the ordered evaluation
must therefore remain a question for the audit. This review neither
asserts a textbook error nor resolves the exterior convention by
silently inserting a factor. No relevant erratum was located in the
bounded searches; that is not proof that none exists.

The additional primary passage is [Jean-Michel Bismut,
*Index Theorem and the Heat Equation*, Proceedings of the ICM,
Berkeley 1986, published 1987, pp. 491--504, p. 492,
equation (0.2)](https://www.imo.universite-paris-saclay.fr/~jean-michel.bismut/Bismut/1987c.pdf#page=2).
It states the ordinary Chern--Weil representation
ch(E)=Tr exp(-nabla^2/(2pi i)) for a bundle with connection and
curvature nabla^2. This directly specifies the character convention
needed to inspect L062 (4). Import the named Chern--Weil formula;
no index theorem, heat-kernel argument or superconnection generalization
is needed. The source supplies no family KS comparison or coefficient
for this F.

## Approved audit and discriminating test

Inputs: L044's marked S, exact h, full self-adjoint D and its sigma
eigenvalue; L052's connection; L060's conditional locally free F
and every stable charge-seven fibre; and the complete L062 proof.
The scoped source comparison does not reopen these mathematical inputs
or infer a bundle from its characters. No rational-polarization
substitution or global universal sheaf is needed for the direct family
audit. Any local moduli interpretation must retain simplicity and the
trace-free obstruction check already written in L062.

Audit the existing proof in this order:

1. Match the ordinary curvature character with L062 (4); establish
   the mixed-curvature KS representative, including its possible
   simultaneous sign and invariance under differentiable trivialization.
2. Check the full exterior evaluation (5), trace order, 2! and fibre
   orientation. Keep matrix multiplication order and the explicit
   prefactor in (2). Do not identify the printed Newton or Serre form
   with (2) without stating the comparison used. An exact numerical
   source-to-integral trace conversion is unnecessary unless asserted;
   the direct explicitly defined integral can be audited independently.
3. Check the transpose/full mixed-tensor contraction, passage to a
   holomorphic form, everywhere nonvanishing, and the claimed KS-kernel
   implication. Cohomological nonzero alone does not establish the
   pointwise claim without those passages.

Continue downstream only if this audit establishes a nonzero
holomorphic family pairing at every point. If only a nonzero scalar
convention changes, record it precisely and assess the surviving
conclusion separately. If representatives, holomorphicity or a
load-bearing implication fail, repair the argument before use; if no
repair is justified, park that input. No stronger geometric target is
approved. Any repair and its proof belong in L062 next research turn,
with PROOF updated only if the argument changes.

## Duplicates, failures and access

L062 already performs the calculation; reproducing it without critical
checks would add nothing. Histories 118--119 separate coverage from
the completed attempt. ATTEMPTS/044--045 stop the projection/cohomology
and spin/projective-index mechanisms; they do not settle this
normalization. The flat-source blocker stays parked.

Queries included `Huybrechts Lehn errata "10.3.3"`, `"10.3.3"
"factor" Huybrechts`, `"Mukai" "symplectic" "Chern" "factor"
two form`, and `"Kodaira-Spencer" "curvature" "Chern character"`.
An additional curvature-reference search led to the inspected Bismut
passage. Search snippets and unrelated results are not theorem evidence;
the searches establish no novelty or absence of stronger literature.

The Kobayashi--Nomizu II scan was opened but had no extracted body
text; screenshots were unreadable in this interface and shell retrieval
failed DNS. It remains an unread optional lead. The readable Bismut
passage suffices for the needed ordinary curvature formula, so this
access failure does not block the approved direct audit. No claim is
made to have settled other recorded source blockers.

## Mathlib

Full family-form, analytic simple-sheaf and normalization coverage:
**not checked**. No matching declaration or absence is asserted.
This is source-coverage progress using known inputs; correctness of
the local specialization awaits the mathematical audit. No new lemma,
script, bundle, moduli construction or Hodge-conjecture candidate is
supplied.
