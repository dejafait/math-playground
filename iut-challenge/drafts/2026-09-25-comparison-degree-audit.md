# Comparison degree audit — 2026-09-25

One bounded comparison/normalization audit, completed as exploration turn 2 of 3. No candidate resolution was obtained. Intermediate reasoning was saved here before the source calculation and before the determinant proof.

## Target and discriminating test

Gap: establish or refute the input-volume membership inference in Corollary 3.12(xi-f) under the original hypotheses. With A and B as fixed in the [source record](../foundations/02-comparison-claim-and-sources.md), the required conclusion is finite B with B ≥ A.

Intermediate target: trace the composite cited in Remark 3.11.1(iii), retaining its object types and ring labels, and determine whether determinant normalization itself leaves an uncontrolled numerical factor. A normalization mismatch surviving the prescribed corrections would justify pursuing that objection. If the common factor cancels, this scalar test does not establish a flaw; the remaining test must concern represented output regions.

Plausible use: identify which numerical compatibility a faithful comparison must establish. The actual initial data, full image family, hull, and log-Kummer compatibility remain additional obligations. No complete downstream passage to the challenge target is assumed.

## Source identification and type check

The official announcement and current prize page were rechecked on 2026-09-25 and agree with the recorded [scope](../foundations/01-challenge-scope.md). The author-hosted IUT III still has 199 pages; printed pagination is used below.

In [IUT III, Remark 3.10.2, pp. 151–152](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf#page=152), label the lower and upper objects Xᵢ and Yᵢ, respectively, with i = 0,1,2,3 denoting env, gau, LGP, lgp. Their original labels are (n,m) and (n,◦). Let bᵢ and uᵢ be lower and upper horizontal arrows, and kᵢ the upward Kummer arrows. [Remark 3.11.1(iii), pp. 160–161](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf#page=161) specifies c = u₃u₂u₁k₀b₁⁻¹b₂⁻¹, from X₂ to Y₃. The subsequent representation involves (Ind1)–(Ind3).

[Proposition 3.9(i)–(iii), pp. 115–117](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf#page=115), supplies the volume conventions. [Remark 3.9.5(vii), (Ob3)–(Ob4), pp. 131–134](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf#page=132), uses weighted determinants, divides out the reference determinant, and compares with the same tensor power of the input.

These are source assertions under audit, not independently verified mathematical inputs for the full theory.

## Completed calculation and its precise limits

[L002](../lemmas/L002-comparison-composite-and-normalized-determinant.md) gives the full abstract path calculation and the conditional finite-packet volume calculation. For coherent commuting squares, c = u₃k₂ = k₃b₃. This equality has the type X₂ → Y₃; it is not an identity map on a specified represented lattice. It does not identify either labeled ring structure with the input theater's ring structure, and it cannot be applied to arbitrary independent representatives of poly-isomorphisms while dropping the commuting-square condition.

For a realization by finite tuples of linear maps Tᵣ between ℚ_p-vector spaces, with full reference lattices Oᵣ and Pᵣ, the exact result is

ν_P(TL) − ν_O(L) = ν_P(TO),

where ν_O(L) = Σᵣ (wᵣ/dᵣ) log(μᵣ(Lᵣ)/μᵣ(Oᵣ)), wᵣ > 0, Σᵣ wᵣ = 1, and dᵣ is the dimension of the r-th space. Thus even this additional linear realization requires control of the transported reference's normalized volume. Transporting the reference itself cancels that defect. Vanishing weighted defect is weaker than equality of every reference lattice.

The weighted relative determinant computes Dν_O(L), with D a positive common denominator satisfying Σᵣ eᵣdᵣ = D. For Lᵣ = pᵃOᵣ the determinant ideal is p^{aD}ℤ_p and the normalized value is −a log p. Comparing DA with DB has precisely the same strength as comparing A with B. D is the explicitly defined denominator in this lemma; it has not been identified with any particular global IUT tensor exponent. An unequal scaling of different objects would not be removed by this calculation.

This test eliminates an artificial discrepancy caused solely by forgetting the common normalization in this finite model. It does not show that the source composite is represented by the required Tᵣ, compute ν_P(TO) for IUT, or identify the full output with T applied to one input lattice. In particular, no estimate for the actual B is achieved. The required threshold remains B ≥ A (equivalently B/A ≤ 1 since A < 0, once B is finite).

## Redundancy and route assessment

L001 and [ATTEMPTS/001](../ATTEMPTS/001-bare-power-map-counterexample.md) already exclude the bare cyclic-monoid shortcut. Neither repeating it nor cancelling a common determinant power establishes a new IUT-specific obstruction. The abstract/concrete distinction is also present in [Scholze–Stix, §§2.1.8–2.2, pp. 8–10](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf). [Mochizuki's response, (C14), p. 4](https://www.kurims.kyoto-u.ac.jp/~motizuki/Cmt2018-08.pdf#page=4), distinguishes linear degree comparisons from geometry-dependent changes to region volumes. No side of that dispute is treated as a correctness certificate.

The scalar audit has now used two turns without an IUT-specific advance or informative negative result, so it should not be repeated under another name. Two possible continuations were compared: constructing and estimating the actual indeterminacy orbit, or testing the quotient step on which the membership inference relies. The former presently requires too much unchecked initial-data machinery for one discriminating test. The latter has a bounded source anchor in Remark 3.9.5(v)–(vi), (ix), and can distinguish an identity after a quotient from a justified lift to an input degree. It was selected at completion as a materially different mechanism. Its assessment must respect the remaining exploration budget; no budget reset is claimed.

The restricted objection based on an uncompensated determinant tensor power is stopped in [ATTEMPTS/002](../ATTEMPTS/002-uncompensated-determinant-power.md); the calculation is retained as a diagnostic. The already rejected direct power-map route also remains recorded. Existing unfinished work and identifiers were preserved. The sole current route decision and concrete next action are in PROGRESS.md.

## Checks and limits

The mathematical checks were the typed cancellation using the three commuting squares, the lattice-index proof of the determinant/Haar formula, and the exact common-scalar normalization check in L002. No numerical experiment was needed. L002 does not use L001 mathematically; their relationship is motivational only. The DAG therefore has no edge between them.

Mathlib: full comparison statement and supporting library coverage **not checked**. The proof of L002 uses the standard named Smith normal form and Haar-measure uniqueness theorems; it does not use the disputed IUT conclusion. No machine verification is claimed. The structural checker is recorded in the dated history after execution.
