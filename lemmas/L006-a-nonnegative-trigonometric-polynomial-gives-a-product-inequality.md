# Lemma 6: a nonnegative trigonometric polynomial gives a product inequality

**Hypotheses.** σ>1 and t∈R.

**Conclusion.** ζ(σ)³|ζ(σ+it)|⁴|ζ(σ+2it)|≥1.

**Proof.** All quantities inside the real logarithms below are positive by Lemmas 1 and 5. Lemma 5 and absolute convergence give

3 log ζ(σ)+4 log|ζ(σ+it)|+log|ζ(σ+2it)|
=Σ_p Σ_{k≥1} p^{-kσ}[3+4cos(kt log p)+cos(2kt log p)]/k.

For every real θ, the bracket is 2(1+cos θ)²≥0. The sum is nonnegative, and exponentiating yields the claim. The equality is asserted only for σ>1. ∎

**Mathlib.** The 3-4-1 product inequality for Dirichlet L-functions is `DirichletCharacter.norm_LFunction_product_ge_one`:

https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Nonvanishing.html#DirichletCharacter.norm_LFunction_product_ge_one

The corresponding Euler-product form is `DirichletCharacter.norm_LSeries_product_ge_one`. Specializing either to the trivial character modulo 1 yields the zeta inequality. The zeta-only packaged statement is not a separately named Mathlib theorem.

**Lean proof status.** Validated. Lean 4.33.1, mathlib `v4.33.1`, `lake build Rh.L006` from `scripts/lean`. Kernel axioms: `propext`, `Classical.choice`, `Quot.sound`.

**Lean proof command.**

```
(cd scripts/lean && lake exe cache get && lake build Rh.L006)
```

**Lean proof code.**

```lean
/-
Lemma 6: a nonnegative trigonometric polynomial gives a product inequality.

For σ > 1 and t real, ζ(σ)³ |ζ(σ+it)|⁴ |ζ(σ+2it)| ≥ 1.
-/
import Mathlib.NumberTheory.LSeries.DirichletContinuation
import Mathlib.NumberTheory.LSeries.Nonvanishing

open Complex

noncomputable section

lemma riemannZeta_norm_eq_re_of_one_lt {σ : ℝ} (hσ : 1 < σ) :
    ‖riemannZeta σ‖ = (riemannZeta σ).re := by
  have hpos := riemannZeta_re_pos_of_one_lt hσ
  have him := riemannZeta_im_eq_zero_of_one_lt hσ
  rw [norm_eq_sqrt_sq_add_sq, him]
  simp [zero_pow (by exact two_ne_zero), Real.sqrt_sq hpos.le]

/--
The 3-4-1 Euler-product inequality for `σ > 1`. This is the specialization of
`DirichletCharacter.norm_LFunction_product_ge_one` to the trivial character mod 1,
together with positivity of real zeta values on `(1, ∞)`.
-/
theorem L006 {σ t : ℝ} (hσ : 1 < σ) :
    1 ≤ (riemannZeta σ).re ^ 3 *
      ‖riemannZeta ((σ : ℂ) + t * I)‖ ^ 4 *
      ‖riemannZeta ((σ : ℂ) + (2 : ℂ) * t * I)‖ := by
  have hx : 0 < σ - 1 := sub_pos.mpr hσ
  have hprod :=
    DirichletCharacter.norm_LFunction_product_ge_one (N := 1)
      (χ := (1 : DirichletCharacter ℂ 1)) hx t
  rw [DirichletCharacter.LFunctionTrivChar] at hprod
  simp only [DirichletCharacter.LFunction_modOne_eq] at hprod
  have h0 : (1 : ℂ) + (σ - 1 : ℝ) = (σ : ℂ) := by
    push_cast
    ring
  rw [h0] at hprod
  have h1 : (σ : ℂ) + I * t = (σ : ℂ) + t * I := by ring
  have h2 : (σ : ℂ) + 2 * I * t = (σ : ℂ) + (2 : ℂ) * t * I := by ring
  rw [h1, h2] at hprod
  rw [norm_mul, norm_mul, norm_pow, norm_pow, riemannZeta_norm_eq_re_of_one_lt hσ] at hprod
  exact hprod

end

#print axioms L006
```
