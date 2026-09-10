/-
Lemma 4: a counterexample to the symmetry-only inference.

The polynomial with roots a, conj a, 1-a, 1-conj a for a = 1/4+I is
reflection- and conjugation-symmetric, positive on the real axis and on
the critical line, but has no zeros on the critical line.
-/
import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic

open Complex
open scoped ComplexConjugate

noncomputable section

def a : ℂ := ⟨1 / 4, 1⟩

def P (s : ℂ) : ℂ :=
  (s - a) * (s - conj a) * (s - (1 - a)) * (s - (1 - conj a))

lemma a_re : a.re = 1 / 4 := rfl
lemma a_im : a.im = 1 := rfl

lemma conj_a_val : conj a = ⟨1 / 4, -1⟩ := by
  apply Complex.ext <;> simp [a]

lemma P_one_sub (s : ℂ) : P (1 - s) = P s := by
  unfold P
  have h1 : 1 - s - a = -(s - (1 - a)) := by ring
  have h2 : 1 - s - conj a = -(s - (1 - conj a)) := by ring
  have h3 : 1 - s - (1 - a) = -(s - a) := by ring
  have h4 : 1 - s - (1 - conj a) = -(s - conj a) := by ring
  rw [h1, h2, h3, h4]
  ring

lemma P_conj (s : ℂ) : P (conj s) = conj (P s) := by
  unfold P
  simp [map_mul, map_sub, map_one]
  ring

lemma P_eval_a : P a = 0 := by simp [P]
lemma P_eval_conj_a : P (conj a) = 0 := by simp [P]
lemma P_eval_one_sub_a : P (1 - a) = 0 := by simp [P]
lemma P_eval_one_sub_conj_a : P (1 - conj a) = 0 := by simp [P]

lemma a_not_on_critical_line : a.re ≠ 1 / 2 := by
  rw [a_re]; norm_num

lemma conj_a_not_on_critical_line : (conj a).re ≠ 1 / 2 := by
  simp [a]

lemma one_sub_a_not_on_critical_line : (1 - a).re ≠ 1 / 2 := by
  simp [a]; norm_num

lemma one_sub_conj_a_not_on_critical_line : (1 - conj a).re ≠ 1 / 2 := by
  simp [a]; norm_num

lemma a_in_open_strip : 0 < a.re ∧ a.re < 1 := by
  rw [a_re]
  constructor <;> norm_num

lemma pair_a (z : ℂ) :
    (z - a) * (z - conj a) = (z - ⟨1 / 4, 0⟩) ^ 2 + 1 := by
  apply Complex.ext
  · simp [a, sq, mul_re, sub_re, sub_im, add_re]
    ring
  · simp [a, sq, mul_im, sub_re, sub_im, add_im]
    ring

lemma pair_one_sub_a (z : ℂ) :
    (z - (1 - a)) * (z - (1 - conj a)) = (z - ⟨3 / 4, 0⟩) ^ 2 + 1 := by
  apply Complex.ext
  · simp [a, sq, mul_re, sub_re, sub_im, add_re]
    ring
  · simp [a, sq, mul_im, sub_re, sub_im, add_im]
    ring

lemma P_as_real_pairs (z : ℂ) :
    P z = ((z - ⟨1 / 4, 0⟩) ^ 2 + 1) * ((z - ⟨3 / 4, 0⟩) ^ 2 + 1) := by
  unfold P
  rw [show (z - a) * (z - conj a) * (z - (1 - a)) * (z - (1 - conj a)) =
        ((z - a) * (z - conj a)) * ((z - (1 - a)) * (z - (1 - conj a))) by ring]
  rw [pair_a, pair_one_sub_a]

lemma ofReal_mk (x : ℝ) : (x : ℂ) = ⟨x, 0⟩ := rfl

lemma pair_ofReal (x c : ℝ) :
    ((x : ℂ) - ⟨c, 0⟩) ^ 2 + 1 = ⟨(x - c) ^ 2 + 1, 0⟩ := by
  apply Complex.ext
  · simp [ofReal_mk, sq, sub_re, mul_re, add_re]
  · simp [ofReal_mk, sq, sub_re, sub_im, mul_im, add_im]

lemma P_ofReal_eq_mk (x : ℝ) :
    P x = ⟨((x - 1 / 4) ^ 2 + 1) * ((x - 3 / 4) ^ 2 + 1), 0⟩ := by
  rw [P_as_real_pairs, pair_ofReal, pair_ofReal]
  apply Complex.ext
  · simp [mul_re]
  · simp [mul_im]

lemma P_ofReal_pos (x : ℝ) : 0 < (P x).re ∧ (P x).im = 0 := by
  rw [P_ofReal_eq_mk]
  constructor
  · simp
    nlinarith [sq_nonneg (x - (1 / 4 : ℝ)), sq_nonneg (x - (3 / 4 : ℝ))]
  · rfl

lemma P_critical_line_eq_mk (t : ℝ) :
    P ⟨1 / 2, t⟩ =
      ⟨((1 / 16 + 1 - t ^ 2) ^ 2 + (t / 2) ^ 2), 0⟩ := by
  rw [P_as_real_pairs]
  -- ⟨1/2, t⟩ - ⟨1/4, 0⟩ = ⟨1/4, t⟩, ⟨1/2, t⟩ - ⟨3/4, 0⟩ = ⟨-1/4, t⟩
  have h1 : (⟨1 / 2, t⟩ : ℂ) - ⟨1 / 4, 0⟩ = ⟨1 / 4, t⟩ := by
    apply Complex.ext <;> simp <;> ring
  have h2 : (⟨1 / 2, t⟩ : ℂ) - ⟨3 / 4, 0⟩ = ⟨-1 / 4, t⟩ := by
    apply Complex.ext <;> simp <;> ring
  rw [h1, h2]
  apply Complex.ext
  · simp [sq, mul_re, add_re]
    ring
  · simp [sq, mul_im, add_im]
    ring

lemma P_critical_line_pos (t : ℝ) :
    0 < (P ⟨1 / 2, t⟩).re ∧ (P ⟨1 / 2, t⟩).im = 0 := by
  rw [P_critical_line_eq_mk]
  constructor
  · simp
    nlinarith [sq_nonneg (1 / 16 + 1 - t ^ 2 : ℝ), sq_nonneg (t / 2 : ℝ)]
  · rfl

lemma differentiable_P : Differentiable ℂ P := by
  have h (c : ℂ) : Differentiable ℂ fun s : ℂ => s - c :=
    Differentiable.sub differentiable_id (differentiable_const c)
  unfold P
  exact (((h a).mul (h (conj a))).mul (h (1 - a))).mul (h (1 - conj a))

/-- Lemma 4: a conjugation- and reflection-symmetric polynomial that is
positive on the real axis and the critical line, with all zeros off that line
inside the open strip. -/
theorem L004 :
    (∀ s : ℂ, P (1 - s) = P s) ∧
    (∀ s : ℂ, P (conj s) = conj (P s)) ∧
    Differentiable ℂ P ∧
    (∀ x : ℝ, 0 < (P x).re ∧ (P x).im = 0) ∧
    (∀ t : ℝ, 0 < (P ⟨1 / 2, t⟩).re ∧ (P ⟨1 / 2, t⟩).im = 0) ∧
    P a = 0 ∧ P (conj a) = 0 ∧ P (1 - a) = 0 ∧ P (1 - conj a) = 0 ∧
    a.re ≠ 1 / 2 ∧ (conj a).re ≠ 1 / 2 ∧
    (1 - a).re ≠ 1 / 2 ∧ (1 - conj a).re ≠ 1 / 2 ∧
    0 < a.re ∧ a.re < 1 :=
  ⟨P_one_sub, P_conj, differentiable_P, P_ofReal_pos, P_critical_line_pos,
    P_eval_a, P_eval_conj_a, P_eval_one_sub_a, P_eval_one_sub_conj_a,
    a_not_on_critical_line, conj_a_not_on_critical_line,
    one_sub_a_not_on_critical_line, one_sub_conj_a_not_on_critical_line,
    a_in_open_strip.1, a_in_open_strip.2⟩

end

-- Kernel-axiom audit. Expected: propext, Quot.sound, Classical.choice.
#print axioms L004
