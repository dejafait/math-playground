/-
Lemma 5: the Euler-product logarithm on its actual domain.

For Re(s) > 1, L(s) = ∑_p -log(1 - p^{-s}) converges, exp(L(s)) = ζ(s),
Re L(s) = log |ζ(s)|, and for real σ > 1 one has Re L(σ) = log ζ(σ).
-/
import Mathlib.NumberTheory.EulerProduct.DirichletLSeries
import Mathlib.NumberTheory.LSeries.Dirichlet

open Complex

noncomputable section

/-- The Euler-product logarithm `∑_p -log(1 - p^{-s})`. -/
def eulerLog (s : ℂ) : ℂ :=
  ∑' p : Nat.Primes, -log (1 - (p : ℂ) ^ (-s))

/-- `exp L(s) = ζ(s)` for `Re(s) > 1`. -/
theorem L005_exp {s : ℂ} (hs : 1 < s.re) : exp (eulerLog s) = riemannZeta s :=
  riemannZeta_eulerProduct_exp_log hs

/-- `Re L(s) = log |ζ(s)|` for `Re(s) > 1`. -/
theorem L005_re_log {s : ℂ} (hs : 1 < s.re) :
    (eulerLog s).re = Real.log ‖riemannZeta s‖ := by
  have hζ : riemannZeta s ≠ 0 := riemannZeta_ne_zero_of_one_lt_re hs
  have h := congrArg norm (L005_exp hs)
  rw [norm_exp] at h
  have hpos : 0 < ‖riemannZeta s‖ := norm_pos_iff.2 hζ
  apply Real.exp_injective
  rw [Real.exp_log hpos, h]

/-- For real `σ > 1`, `Re L(σ) = log ζ(σ)`. -/
theorem L005_real {σ : ℝ} (hσ : 1 < σ) :
    (eulerLog σ).re = Real.log (riemannZeta σ).re := by
  have hs : 1 < (σ : ℂ).re := by simpa using hσ
  rw [L005_re_log hs]
  have him := riemannZeta_im_eq_zero_of_one_lt hσ
  have hpos := riemannZeta_re_pos_of_one_lt hσ
  have : ‖riemannZeta σ‖ = (riemannZeta σ).re := by
    rw [Complex.norm_eq_sqrt_sq_add_sq, him]
    simp [zero_pow (by exact two_ne_zero), Real.sqrt_sq hpos.le]
  rw [this]

/-- Lemma 5: Euler-product logarithm, exponential identity, and real logarithm. -/
theorem L005 {s : ℂ} (hs : 1 < s.re) :
    exp (eulerLog s) = riemannZeta s ∧
    (eulerLog s).re = Real.log ‖riemannZeta s‖ :=
  ⟨L005_exp hs, L005_re_log hs⟩

end

-- Kernel-axiom audit. Expected: propext, Quot.sound, Classical.choice.
#print axioms L005
#print axioms L005_real
