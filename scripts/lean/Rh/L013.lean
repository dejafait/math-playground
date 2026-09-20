import Rh.L012
import Rh.L009

open Complex
noncomputable section

lemma L013_term_real (n : ℕ) (σ : ℝ) :
    L012_term n (σ : ℂ) = (Real.exp (-σ * Real.log (n + 1 : ℝ)) : ℂ) := by
  simp [L012_term, Complex.ofReal_exp]

lemma L013_pair_pos (n : ℕ) {σ : ℝ} (hσ : 0 < σ) :
    0 < (L012_pair n (σ : ℂ)).re := by
  simp only [L012_pair, L013_term_real, sub_re, ofReal_re]
  apply sub_pos.mpr
  apply Real.exp_lt_exp.mpr
  have hlog : Real.log ((2 * n : ℕ) + 1 : ℝ) <
      Real.log ((2 * n + 1 : ℕ) + 1 : ℝ) :=
    Real.log_lt_log (by positivity) (by push_cast; linarith)
  nlinarith

/-- Positivity and reality of the alternating series on the positive real axis. -/
theorem L013_eta {σ : ℝ} (hσ : 0 < σ) :
    0 < (L012_eta (σ : ℂ)).re ∧ (L012_eta (σ : ℂ)).im = 0 := by
  have hs := L012_paired_summable (σ : ℂ) (by simpa using hσ)
  constructor
  · rw [L012_eta, Complex.re_tsum hs]
    exact (L013_pair_pos 0 hσ).trans_le ((Complex.hasSum_re hs.hasSum).summable.le_tsum 0 (fun n _ => (L013_pair_pos n hσ).le))
  · rw [L012_eta, Complex.im_tsum hs]
    simp only [L012_pair, L013_term_real, sub_im, ofReal_im, sub_self, tsum_zero]

/-- The full sign assertion, with reality explicit for both complex values. -/
theorem L013 {σ : ℝ} (hσ : 0 < σ) (hσ1 : σ < 1) :
    0 < (L012_eta (σ : ℂ)).re ∧ (L012_eta (σ : ℂ)).im = 0 ∧
    (riemannZeta (σ : ℂ)).re < 0 ∧ (riemannZeta (σ : ℂ)).im = 0 := by
  have hη := L013_eta hσ
  have hone : (σ : ℂ) ≠ 1 := by
    intro h
    have := congrArg Complex.re h
    simp only [ofReal_re, one_re] at this
    linarith
  have hid := L012_zeta_identity (σ : ℂ) (by simpa using hσ) hone
  have hp : (2 : ℂ) ^ (1 - (σ : ℂ)) = (((2 : ℝ) ^ (1 - σ) : ℝ) : ℂ) := by
    rw [show (1 - (σ : ℂ)) = ((1 - σ : ℝ) : ℂ) by push_cast; rfl]
    exact (Complex.ofReal_cpow (by norm_num : (0 : ℝ) ≤ 2) _).symm
  rw [hp] at hid
  have hneg : 1 - (2 : ℝ) ^ (1 - σ) < 0 :=
    sub_neg.mpr (Real.one_lt_rpow (by norm_num) (by linarith))
  have hre := congrArg Complex.re hid
  have him := congrArg Complex.im hid
  simp only [mul_re, mul_im, sub_re, sub_im, one_re, one_im,
    ofReal_re, ofReal_im, sub_zero, zero_mul, add_zero] at hre him
  refine ⟨hη.1, hη.2, ?_, ?_⟩
  · nlinarith [hη.1]
  · rw [hη.2] at him
    exact (mul_eq_zero.mp him.symm).resolve_left (ne_of_lt hneg)

/-- Every zero other than a negative even integer has nonzero imaginary part. -/
theorem L013_nontrivial_zero {s : ℂ} (hz : riemannZeta s = 0)
    (htrivial : ¬ ∃ n : ℕ, 0 < n ∧ s = -2 * (n : ℂ)) : s.im ≠ 0 := by
  have hone : s ≠ 1 := by
    intro h
    subst s
    exact riemannZeta_ne_zero_of_one_le_re (by simp) hz
  have hstrip : s ∈ openCriticalStrip := by
    by_contra h
    exact htrivial ((L009 h hone).mp hz)
  have hs : 0 < s.re ∧ s.re < 1 := hstrip
  intro him
  have heq : (s.re : ℂ) = s := by apply Complex.ext <;> simp [him]
  have hneg := (L013 hs.1 hs.2).2.2.1
  rw [heq, hz] at hneg
  simp at hneg

#print axioms L013_eta
#print axioms L013
#print axioms L013_nontrivial_zero
