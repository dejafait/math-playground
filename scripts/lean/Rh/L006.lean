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
