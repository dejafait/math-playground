# Lemma 28: a degree-two Jensen polynomial is real-rooted

**Hypotheses.** Define γ_n=n!M_{2n}/(2n)! for n≥0 and J_2(X)=γ_0+2γ_1X+γ_2X². This definition is the degree-two Jensen polynomial of the entire series Σ_nγ_n X^n/n!=Σ_nM_{2n}X^n/(2n)!.

**Conclusion.** J_2 has two distinct negative real roots.

**Proof.** γ_0=M_0>0, γ_1=M_2/2>0, and γ_2=M_4/12>0. Its discriminant is

(2γ_1)²-4γ_0γ_2=M_2²-M_0M_4/3>0

by Lemma 27. Thus both roots are real and distinct. Their sum is -2γ_1/γ_2<0 and their product γ_0/γ_2>0, so both are negative. No assertion about any higher degree or shifted Jensen polynomial is made. ∎

**Mathlib.** The quadratic-root argument is proved below using `Real.sq_sqrt` and `Real.sqrt_pos`, rather than a prepackaged theorem about these Jensen polynomials:

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Sqrt.html#Real.sq_sqrt

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Sqrt.html#Real.sqrt_pos

**Lean proof status.** Validated conditional proof. The theorem takes positivity of M_0, M_2, M_4 and M_0 M_4 < 3 M_2² as explicit hypotheses. These are the inputs supplied by the informal Lemma 27; their derivation for the actual theta-kernel moments is not yet formalized. This is not yet an end-to-end Lean proof for the actual Ξ moments. Lean 4.33.1, mathlib `v4.33.1`, `lake build Rh.L028` from `scripts/lean`. Kernel axioms: `propext`, `Classical.choice`, `Quot.sound`.

**Lean proof command.**

```
(cd scripts/lean && lake exe cache get && lake build Rh.L028)
```

**Lean proof code.**

```lean
/-
Lemma 28: degree-two Jensen polynomial, conditional on the moment
positivity and strict inequality supplied by the informal Lemma 27.
This file does not prove those facts for the theta-kernel moments.
-/
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic

noncomputable section

/-- With the moment inequalities from Lemma 27, the degree-two Jensen
polynomial has exactly two distinct roots, both strictly negative. -/
theorem L028 (M0 M2 M4 : ℝ)
    (h0 : 0 < M0) (h2 : 0 < M2) (h4 : 0 < M4)
    (hdisc : M0 * M4 < 3 * M2 ^ 2) :
    ∃ r₁ r₂ : ℝ, r₁ < r₂ ∧ r₂ < 0 ∧
      ∀ x : ℝ, M0 + 2 * (M2 / 2) * x + (M4 / 12) * x ^ 2 = 0 ↔
        x = r₁ ∨ x = r₂ := by
  let D := M2 ^ 2 - M0 * M4 / 3
  have hD : 0 < D := by dsimp [D]; linarith
  have hs : 0 < Real.sqrt D := Real.sqrt_pos.mpr hD
  have hs2 : Real.sqrt D ^ 2 = D := Real.sq_sqrt hD.le
  have hsM : Real.sqrt D < M2 := by
    have hprod := mul_pos h0 h4
    dsimp [D] at hs2
    nlinarith
  let a := M4 / 12
  have ha : 0 < a := by dsimp [a]; positivity
  let r₁ := (-M2 - Real.sqrt D) / (2 * a)
  let r₂ := (-M2 + Real.sqrt D) / (2 * a)
  have hr : r₁ < r₂ := by
    dsimp [r₁, r₂]
    exact (div_lt_div_iff_of_pos_right (by positivity)).mpr (by linarith)
  have hr₂ : r₂ < 0 := div_neg_of_neg_of_pos (by linarith) (by positivity)
  refine ⟨r₁, r₂, hr, hr₂, ?_⟩
  intro x
  have factor : M0 + 2 * (M2 / 2) * x + (M4 / 12) * x ^ 2 =
      a * (x - r₁) * (x - r₂) := by
    dsimp [r₁, r₂]
    field_simp
    dsimp [a, D] at *
    nlinarith
  rw [factor, mul_eq_zero, mul_eq_zero]
  simp only [ne_of_gt ha, false_or, sub_eq_zero]

end

#print axioms L028
```
