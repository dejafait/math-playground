/-
Lemma 34: small zero arguments do not ensure a mixed determinant sign.
-/
import Mathlib.Analysis.Complex.Polynomial.Basic
import Mathlib.Tactic

open Complex
open scoped ComplexConjugate

noncomputable section

def L034_alpha : ℂ := 10 + I / 4

def L034_c : ℂ := (L034_alpha ^ 2)⁻¹

def L034_T (k : ℕ) : ℂ := L034_c ^ k + conj L034_c ^ k

def L034_P (z : ℂ) : ℂ :=
  (1 - z ^ 2 / L034_alpha ^ 2) * (1 - z ^ 2 / (conj L034_alpha) ^ 2)

lemma L034_c_value : L034_c = (25584 / 2563201 : ℝ) + (-1280 / 2563201 : ℝ) * I := by
  apply Complex.ext <;> norm_num [L034_c, L034_alpha, Complex.inv_re,
    Complex.inv_im, Complex.normSq, pow_two]

/-- All six scalar power sums are positive real numbers. -/
theorem L034_scalar (k : ℕ) (hk : 1 ≤ k ∧ k ≤ 6) :
    (L034_T k).im = 0 ∧ 0 < (L034_T k).re := by
  obtain ⟨hk1, hk6⟩ := hk
  simp only [L034_T, ← map_pow, Complex.add_re, Complex.add_im, Complex.conj_re, Complex.conj_im]
  interval_cases k <;>
    norm_num [L034_T, L034_c_value, Complex.mul_re, Complex.mul_im,
      pow_succ]

/-- The determinant identity for an arbitrary conjugate pair. -/
theorem L034_identity (c : ℂ) :
    (c ^ 2 + conj c ^ 2) * (c ^ 4 + conj c ^ 4) - (c ^ 3 + conj c ^ 3) ^ 2 =
      ((-4 * ‖c‖ ^ 4 * c.im ^ 2 : ℝ) : ℂ) := by
  have hn : ‖c‖ ^ 4 = (c.re ^ 2 + c.im ^ 2) ^ 2 := by
    rw [show (4 : ℕ) = 2 * 2 by rfl, pow_mul, Complex.sq_norm]
    simp [Complex.normSq, pow_two]
  rw [hn]
  apply Complex.ext <;>
    simp only [Complex.add_re, Complex.add_im, Complex.sub_re, Complex.sub_im,
      Complex.mul_re, Complex.mul_im, Complex.conj_re, Complex.conj_im,
      Complex.ofReal_re, Complex.ofReal_im, pow_succ, pow_zero,
      Complex.one_re, Complex.one_im] <;> ring

/-- The mixed determinant of the explicit nodes is strictly negative. -/
theorem L034_negative : (L034_T 2 * L034_T 4 - L034_T 3 ^ 2).re < 0 := by
  unfold L034_T
  rw [L034_identity]
  simp only [Complex.ofReal_re]
  have hi : L034_c.im ≠ 0 := by norm_num [L034_c_value]
  have hc : L034_c ≠ 0 := by
    intro h
    exact hi (by rw [h]; rfl)
  have hn := pow_pos (norm_pos_iff.mpr hc) 4
  have hi2 := sq_pos_of_ne_zero hi
  nlinarith

/-- The polynomial has exactly the four specified roots. -/
theorem L034_roots (z : ℂ) : L034_P z = 0 ↔
    z = L034_alpha ∨ z = -L034_alpha ∨
    z = conj L034_alpha ∨ z = -conj L034_alpha := by
  have ha : L034_alpha ≠ 0 := by
    intro h
    have := congrArg Complex.re h
    norm_num [L034_alpha] at this
  have hca : conj L034_alpha ≠ 0 := by simpa only [map_ne_zero] using ha
  have hfactor (a : ℂ) (ha : a ≠ 0) :
      1 - z ^ 2 / a ^ 2 = 0 ↔ z = a ∨ z = -a := by
    rw [sub_eq_zero, eq_comm, div_eq_one_iff_eq (pow_ne_zero 2 ha)]
    exact sq_eq_sq_iff_eq_or_eq_neg
  simp only [L034_P, mul_eq_zero, hfactor _ ha, hfactor _ hca]
  tauto

/-- Every root is beyond the zero-free rectangle and within the height strip. -/
theorem L034_location (z : ℂ) (hz : L034_P z = 0) :
    4 < |z.re| ∧ |z.im| < 1 / 2 := by
  rcases (L034_roots z).mp hz with rfl | rfl | rfl | rfl <;>
    norm_num only [Complex.neg_re, Complex.neg_im, Complex.conj_re, Complex.conj_im]
  all_goals norm_num [L034_alpha]

/-- The polynomial is even and respects complex conjugation. -/
theorem L034_symmetry (z : ℂ) :
    L034_P (-z) = L034_P z ∧ L034_P (conj z) = conj (L034_P z) := by
  constructor
  · simp [L034_P]
  · simp [L034_P, mul_comm]

end

#print axioms L034_scalar
#print axioms L034_identity
#print axioms L034_negative
#print axioms L034_roots
#print axioms L034_location
#print axioms L034_symmetry
