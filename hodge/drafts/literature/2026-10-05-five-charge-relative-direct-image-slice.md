# Five-charge coefficient slice — literature assessment

TARGET: Test whether relative direct-image finite-rank identities exclude every L052 survivor with a=-9 and arbitrary integer b.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded searches for rank-two K3 product families with c_2=5 and relative GRR found general tools and Maciocia's equivalence-kernel classification; scoped local searches found L054's fixed-pair test but no completed variable-slice test. Queries and inspected scopes appear below.
SOURCE_EVIDENCE: Reused the inspected Fulton second edition (1998), Theorem 15.2, pp. 286–287, Example 15.2.8, pp. 291–292, and assessed Verbitsky/Huybrechts surface inputs; inspected Stacks 0A1H, Lemma 36.31.3 in 0BDH with its full proof, 02UM and 02UO, and Maciocia's accepted manuscript Theorem 0.1, Proposition 1.1 and Theorem 2.5, printed pp. 2–5.
COMPARISON: General base-change and relative-GRR hypotheses do not fix the second pure coefficient; L052 already covers all-fibre restrictions throughout its region, and L048 supplies parameter-dependent forced characters. L054 evaluates only (-9,-10); Maciocia requires an equivalence or a specified product-line extension, absent from this target.
GAP: Separately apply the existing all-fibre stability/cohomology statements to the c_2=5 projection for every survivor, compute the full relative character as a function of b, and compare it with an actual line-bundle character without assuming stability of the other factor.
REASON: The changed quantified target required a separate comparison; the inspected general theorems and existing coefficient-independent local inputs cover its tools. Only their unevaluated variable-character specialization remains, with no general reproof needed and no novelty claim.
SCOPE: Exactly L044's fixed S, h and mixed tensor on S x S, rank-two locally free holomorphic F slope-polystable at p_1^*h+p_2^*h with c_1=0 and L048's character, a=-9 and integer b satisfying L052's survivor conditions, projecting by p_2. No other coefficient slice, bundle construction, arbitrary tensor or transverse transport.

## Gap, use and bounded test

The main gap remains universal algebraicity of primitive rational Hodge
classes, already unresolved on arbitrary fourfolds. Locally this route
lacks a compatible product bundle carrying the fixed mixed cubic action.
The intermediate target tests the entire surviving c_2=5 edge, rather
than another individual example. An exclusion would redirect prospective
constructions to larger factor charges. Compatible identities would
supply no bundle and would end this finite-rank obstruction on this slice.

Continue with one separate mathematical test if the existing all-fibre
input yields concentration for the chosen projection. Compare the full
relative character with the line identity for every allowed integer b,
including any exceptional value at which the character is compatible.
If concentration fails, park the dependent computation; if compatibility
occurs, retain that limitation rather than asserting existence. No
variable pushforward character, exceptional value or exclusion is
derived in this literature turn.

Continuation inputs: L044 fixes metric/tensor; L048 gives forced higher
characters and the full mixed square; L052 gives the coefficient-independent
all-fibre restriction passage, stable Euler test and zero-slope lattice;
L054 supplies the fixed-pair application and sign conventions. L053
supplies individual factors only and is not a premise for global existence.
Other corrections, compatible global realization, transverse transport
and universal primitive-Hodge algebraicity remain unresolved. In
particular, arbitrary b does not justify calling the other factor stable.

## Hypotheses and primary source coverage

L052's proof states that every factor restriction is locally free and
polystable for every pair in its hypotheses, using its coefficient-independent
hyperholomorphic curvature argument. Its stable/split alternatives and
equation (4) explicitly include the factor value five. Reusing these
statements is within their scope; this review does not prove a wider
restriction theorem. L048's hypotheses already cover variable a,b in
the weaker necessary region, and its conclusion records the forced
character in terms of p=4+a and t=4+b. The mathematical turn must retain
the complete mixed-square contribution, not just its divisor portion.

Reuse the [fixed-pair assessment](2026-10-05-minimum-pair-relative-cohomology.md)
for Fulton, *Intersection Theory*, second edition (1998),
[Theorem 15.2, pp. 286–287, and Example 15.2.8, pp. 291–292](https://djvu.online/file/87GFN2nbfbdF7).
Its proper morphism between nonsingular quasi-projective varieties covers
this projective projection for every b. Use the alternating coherent
pushforward, the relative tangent bundle and rational cycle-class map;
no coefficient restriction enters that theorem. The earlier scan/version
qualification is retained; no new Fulton passage was needed.

[Stacks Lemma 36.30.1, Tag 0A1H](https://stacks.math.columbia.edu/tag/0A1H)
requires finite presentation, a perfect input and a bounded finitely
presented base-flat complex with proper support. With O_X and F[0],
smooth projectivity and local freeness discharge these conditions.
It gives perfect derived pushforward and arbitrary base change. Its
proof's Noetherian case applies here; no approximation case is needed.

[Stacks Lemma 36.31.3 in Tag 0BDH](https://stacks.math.columbia.edu/tag/0BDH)
requires a perfect complex and specifies the open locus where it is a
rank-r locally free module in degree i, characterized by derived pullback.
The full proof uses vanishing of the other fibre Betti numbers, the
finite-free complex criterion and open rank loci. For the future
application every closed fibre must lie in the required locus; a virtual
rank alone is insufficient. The finite-type complex base then permits
checking that its closed complement is empty.

[Stacks Section 42.66, Tag 02UO](https://stacks.math.columbia.edu/tag/02UO)
states smooth proper relative GRR for finite locally free input and
finite locally free higher direct images, with alternating signs and
relative Todd class. Its general proof is deferred, so Fulton remains
the theorem citation. [Section 42.45, Tag 02UM](https://stacks.math.columbia.edu/tag/02UM)
defines the character through Chern roots and gives its polynomial
expansion; this covers the finite-rank comparison. These stable-tag
statements and relevant proof case were inspected online on CHECKED.

Reuse the [factor-source assessment](2026-10-04-corrected-rank-two-factor-restrictions.md):
Verbitsky, arXiv:math/0107182v10, Theorem 3.9, Proposition 3.7 and
Lemma 3.8, pp. 12–14; Huybrechts, *Lectures on K3 Surfaces*, author-hosted
draft, Chapter 1 equations (2.5)–(2.6), Proposition 2.4, pp. 11–13,
Chapter 9 Section 3.1, pp. 175–176, Theorem 4.9, p. 182. The stable
criterion is used after excluding product line splitting; total invariance
is not assigned to arbitrary summands. Real-class slope stability is
retained. Changing pure point coefficients does not change these source
hypotheses; L052 already makes that local specialization explicit.

## Nearby results, duplicates and failures

Read/reused Maciocia, *Rank Two Fourier–Mukai Transforms for K3 Surfaces*,
J. Geom. Phys. 118 (2017), 192–201,
[accepted manuscript](https://www.pure.ed.ac.uk/ws/portalfiles/portal/30370169/Rank_Two_Fourier_Mukai_Transforms_for_K3_Surfaces.pdf),
Theorem 0.1, printed p. 2; Proposition 1.1 and its proof, pp. 3–4;
Theorem 2.5, p. 5. Theorem 0.1 classifies equivalence kernels in its
specified twisted-determinant range with a generically special line
subsheaf. Theorem 2.5 treats a locally free extension by a product-line
twist of the diagonal ideal and requires acyclicity of the line ratio
and equality of the two line products. Proposition 1.1 computes the
transform character in that ansatz. None supplies a classification for
an arbitrary product bundle under this target's hypotheses. No equivalence,
strong simplicity, complete moduli parametrization or diagonal-extension
presentation is assumed here; no such assumption may be inserted to use
that stronger classification.

Scoped searches in the relevant 2026-10-05 assessments, histories,
ATTEMPTS and L048/L052/L054 found only the fixed (-9,-10) calculation.
History 102 proposes the slice but does not solve it. The canonical
L054 proof explicitly limits its evaluation to that pair; its method is
a reusable tool rather than a duplicate variable result.
[The fixed-pair stop](../../ATTEMPTS/039-minimum-pair-relative-direct-image.md)
is preserved. L048–L049 indices, L050 topology, L051–L052 factor
necessity and L053 individual existence do not give product compatibility.
Older symmetric, boundary and presentation stops keep their exact scopes;
this bounded target adds a quantifier, not a new construction mechanism.

New exact external queries on CHECKED:

- "K3" "rank two" "c_2=5" family bundle direct image
- "K3" "rank two" "product" "Grothendieck" Riemann Roch
- "rank two" "Fourier-Mukai" "Maciocia" K3

The search retrieved Maciocia and nearby derived-equivalence/moduli work,
not an inspected theorem deciding this fixed-tensor variable slice.
Nonprimary summaries and snippets were not theorem evidence. The stronger
known tools are sufficient for this bounded specialization; failed
searches imply no novelty, and no essential source is blocked. Further
unread moduli/Nahm leads are not required to perform the approved test.

## Outcome and Mathlib

Completed LITERATURE / EXPLORATION / NOVELTY_UNCHECKED, actual task type
literature_comparison. The new theorem-level scope comparison changes
REVIEW_REQUIRED to SPECIALIZE for the exact unchanged TARGET. It approves
a separate REPRODUCTION attempt, not the mathematical conclusion.
No lemma, mathematical script, DAG or PROOF change is made. Mathematical
exploration usage remains zero. No new class, transverse direction or
candidate resolution is supplied.

Mathlib coverage of a matching full slice exclusion and of supporting
coherent base change/relative GRR: not checked. No absence is asserted.
Full proofs of the existing local inputs remain canonical in lemmas/;
the general results are imported by the citations above, with no reproof.
