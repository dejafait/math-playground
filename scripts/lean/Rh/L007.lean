/-
Lemma 7: nonvanishing on Re(s) = 1.

For real t ≠ 0, ζ(1 + it) ≠ 0.
-/
import Mathlib.NumberTheory.LSeries.Nonvanishing

open Complex

noncomputable section

/-- `ζ` has no zeros on the line `Re(s) = 1` except the pole at `s = 1`. -/
theorem L007 {t : ℝ} (ht : t ≠ 0) : riemannZeta ((1 : ℂ) + t * I) ≠ 0 := by
  have : ((1 : ℂ) + t * I) ≠ 1 := by
    simp [add_eq_left, mul_eq_zero, I_ne_zero, ofReal_eq_zero, ht]
  exact riemannZeta_ne_zero_of_one_le_re (by simp [add_re, mul_re, I_re, I_im])

end

#print axioms L007
