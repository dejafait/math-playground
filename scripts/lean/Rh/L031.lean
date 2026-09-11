/-
Lemma 31: a mixed test detects the finite counterexample.
An explicit rational polynomial replaces the Lagrange interpolation formula.
-/
import Rh.L034
import Mathlib.LinearAlgebra.Matrix.PosDef

open Complex Polynomial Matrix
open scoped ComplexConjugate

noncomputable section

def L031_b : ℝ := 1 / 25

def L031_T (k : ℕ) : ℝ := L031_b ^ k + (L034_c ^ k).re * 2

def L031_q : Polynomial ℝ :=
  C (4914140794001 / 1848321280) +
  C (-758169934387323 / 2274856960) * X +
  C (39452764147173995 / 5914628096) * X ^ 2

/-- The real power sums agree with the complex node sums. -/
theorem L031_T_eq (k : ℕ) : (L031_T k : ℂ) =
    (L031_b : ℂ) ^ k + L034_c ^ k + conj L034_c ^ k := by
  simp only [← map_pow]
  apply Complex.ext <;>
    simp only [L031_T, Complex.add_re, Complex.add_im, Complex.conj_re,
      Complex.conj_im, Complex.ofReal_re, Complex.ofReal_im,
      Complex.ofReal_add, Complex.ofReal_mul, Complex.ofReal_pow,
      Complex.mul_re, Complex.mul_im, Complex.ofReal_ofNat] <;> norm_num <;> ring

/-- The polynomial has degree at most two. -/
theorem L031_degree : L031_q.natDegree ≤ 2 := by
  unfold L031_q
  compute_degree

/-- The three interpolation values, proved using exact rational arithmetic. -/
theorem L031_values :
    L031_q.eval₂ Complex.ofRealHom (L031_b : ℂ) = 0 ∧
    L031_q.eval₂ Complex.ofRealHom L034_c = I / L034_c ∧
    L031_q.eval₂ Complex.ofRealHom (conj L034_c) = -I / conj L034_c := by
  have hcj : conj L034_c = (25584 / 2563201 : ℝ) + (1280 / 2563201 : ℝ) * I := by
    apply Complex.ext <;>
      simp only [Complex.conj_re, Complex.conj_im] <;>
      norm_num [L034_c_value]
  rw [hcj, L034_c_value]
  norm_num [L031_q, L031_b, Polynomial.eval₂_add, Polynomial.eval₂_mul,
    Polynomial.eval₂_pow, Complex.div_re, Complex.div_im, Complex.normSq,
    Complex.mul_re, Complex.mul_im, pow_two, Complex.ext_iff]

/-- The mixed form of this real polynomial is exactly minus two. -/
theorem L031_form :
    (L031_b : ℂ) ^ 2 * (L031_q.eval₂ Complex.ofRealHom (L031_b : ℂ)) ^ 2 +
    L034_c ^ 2 * (L031_q.eval₂ Complex.ofRealHom L034_c) ^ 2 +
    (conj L034_c) ^ 2 * (L031_q.eval₂ Complex.ofRealHom (conj L034_c)) ^ 2 = -2 := by
  rw [L031_values.1, L031_values.2.1, L031_values.2.2]
  have hc : L034_c ≠ 0 := by
    intro h
    have := congrArg Complex.im h
    norm_num [L034_c_value] at this
  have hcj : conj L034_c ≠ 0 := by simpa only [_root_.map_ne_zero] using hc
  field_simp
  simp [I_sq]
  ring

/-- Every scalar power sum remains strictly positive. -/
theorem L031_positive (k : ℕ) (hk : 1 ≤ k) : 0 < L031_T k := by
  have hn : ‖L034_c‖ < 1 / 100 := by
    have hs : ‖L034_c‖ ^ 2 = (256 / 2563201 : ℝ) := by
      rw [Complex.sq_norm, L034_c_value]
      norm_num [Complex.normSq]
    nlinarith [norm_nonneg L034_c]
  have hb : 0 < L031_b := by norm_num [L031_b]
  have hpow : ∀ n : ℕ, 1 ≤ n → 2 * ‖L034_c‖ ^ n < L031_b ^ n := by
    intro n
    induction n with
    | zero => omega
    | succ n ih =>
      intro hn1
      by_cases hn0 : n = 0
      · subst n
        norm_num only [pow_one]
        dsimp [L031_b]
        linarith
      · have hprev := ih (by omega)
        have hmul := mul_lt_mul_of_pos_right hprev hb
        have hrb : ‖L034_c‖ ≤ L031_b := by dsimp [L031_b]; linarith
        rw [pow_succ, pow_succ]
        calc
          2 * (‖L034_c‖ ^ n * ‖L034_c‖) ≤
              (2 * ‖L034_c‖ ^ n) * L031_b := by
                nlinarith [pow_nonneg (norm_nonneg L034_c) n]
          _ < L031_b ^ n * L031_b := hmul
  have hre := Complex.abs_re_le_norm (L034_c ^ k)
  rw [norm_pow] at hre
  have hlow := (abs_le.mp hre).1
  have hstrict := hpow k hk
  dsimp [L031_T]
  linarith

/-- The Hankel matrix formed from these scalar power sums. -/
def L031_H : Matrix (Fin 3) (Fin 3) ℝ := fun m n => L031_T (m.val + n.val + 2)

/-- An explicit coefficient vector witnesses failure of positive semidefiniteness. -/
theorem L031_not_posSemidef : ¬ L031_H.PosSemidef := by
  intro h
  let v : Fin 3 → ℝ := ![4914140794001 / 1848321280,
    -758169934387323 / 2274856960, 39452764147173995 / 5914628096]
  have hv := h.dotProduct_mulVec_nonneg v
  norm_num [v, dotProduct, mulVec, Fin.sum_univ_succ, L031_H, L031_T,
    L031_b, L034_c_value, Complex.mul_re, Complex.mul_im, pow_succ] at hv

end

#print axioms L031_T_eq
#print axioms L031_degree
#print axioms L031_values
#print axioms L031_form
#print axioms L031_positive
#print axioms L031_not_posSemidef
