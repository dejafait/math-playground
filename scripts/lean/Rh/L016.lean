import Mathlib.Analysis.SpecialFunctions.Gaussian.PoissonSummation
import Mathlib.Analysis.Calculus.SmoothSeries
import Mathlib.Analysis.Calculus.IteratedDeriv.Defs
import Mathlib.Tactic

/-! Full formalization of L016: the literal theta transformation and
uniform exponential tails for every iterated derivative of psi. -/

namespace Rh.L016

noncomputable def theta (x : ℝ) : ℝ :=
  ∑' n : ℤ, Real.exp (-Real.pi * (n : ℝ) ^ 2 * x)

noncomputable def psi (x : ℝ) : ℝ :=
  ∑' n : ℕ, Real.exp (-Real.pi * ((n : ℝ) + 1) ^ 2 * x)

/-- The theta transformation, with exactly the series in the notebook. -/
theorem theta_transformation {x : ℝ} (hx : 0 < x) :
    theta x = x ^ (-(1 / 2 : ℝ)) * theta (1 / x) := by
  have h := Real.tsum_exp_neg_mul_int_sq hx
  have hleft : (fun n : ℤ => Real.exp (-Real.pi * x * (n : ℝ) ^ 2)) =
      (fun n : ℤ => Real.exp (-Real.pi * (n : ℝ) ^ 2 * x)) := by
    funext n
    congr 1
    ring
  have hright : (fun n : ℤ => Real.exp (-Real.pi / x * (n : ℝ) ^ 2)) =
      (fun n : ℤ => Real.exp (-Real.pi * (n : ℝ) ^ 2 * (1 / x))) := by
    funext n
    congr 1
    ring
  rw [hleft, hright] at h
  simpa [theta, Real.rpow_neg hx.le, one_div] using h

lemma term_le_geometric {x : ℝ} (hx : 0 < x) (n : ℕ) :
    Real.exp (-Real.pi * ((n : ℝ) + 1) ^ 2 * x) ≤
      Real.exp (-Real.pi * x) ^ (n + 1) := by
  rw [← Real.exp_nat_mul]
  apply Real.exp_le_exp.mpr
  have hn : (0 : ℝ) ≤ n := Nat.cast_nonneg n
  have hp := Real.pi_pos
  have hs : (n : ℝ) + 1 ≤ ((n : ℝ) + 1) ^ 2 := by nlinarith
  push_cast
  nlinarith [mul_nonneg (mul_pos hp hx).le (sub_nonneg.mpr hs)]

lemma geometric_summable {x : ℝ} (hx : 0 < x) :
    Summable (fun n : ℕ => Real.exp (-Real.pi * x) ^ (n + 1)) := by
  have hq : Real.exp (-Real.pi * x) < 1 :=
    Real.exp_lt_one_iff.mpr (by nlinarith [Real.pi_pos])
  simpa [pow_succ] using
    (summable_geometric_of_lt_one (Real.exp_pos _).le hq).mul_right
      (Real.exp (-Real.pi * x))

/-- Absolute convergence of the positive-index series for every positive x. -/
theorem psi_summable {x : ℝ} (hx : 0 < x) :
    Summable (fun n : ℕ => Real.exp (-Real.pi * ((n : ℝ) + 1) ^ 2 * x)) :=
  Summable.of_nonneg_of_le (fun _ => (Real.exp_pos _).le)
    (term_le_geometric hx) (geometric_summable hx)

/-- Include the zero term in the positive half of the Gaussian series. -/
lemma gaussian_nat_summable {x : ℝ} (hx : 0 < x) :
    Summable (fun n : ℕ => Real.exp (-Real.pi * (n : ℝ) ^ 2 * x)) := by
  apply (summable_nat_add_iff 1).mp
  simpa only [Nat.cast_add, Nat.cast_one] using psi_summable hx

/-- The integer-index Gaussian series converges absolutely. -/
theorem theta_summable {x : ℝ} (hx : 0 < x) :
    Summable (fun n : ℤ => Real.exp (-Real.pi * (n : ℝ) ^ 2 * x)) := by
  apply Summable.of_nat_of_neg_add_one
  · simpa using gaussian_nat_summable hx
  · simpa only [Int.cast_neg, Int.cast_add, Int.cast_natCast, Int.cast_one, neg_sq] using psi_summable hx

set_option maxHeartbeats 800000 in
/-- The literal integer series is the zero term plus twice its positive half. -/
theorem theta_eq_one_add_two_psi {x : ℝ} (hx : 0 < x) :
    theta x = 1 + 2 * psi x := by
  have hp : Summable (fun n : ℕ =>
      Real.exp (-Real.pi * ((n : ℤ) : ℝ) ^ 2 * x)) := by
    simpa using gaussian_nat_summable hx
  have hn : Summable (fun n : ℕ =>
      Real.exp (-Real.pi * ((-(n + 1) : ℤ) : ℝ) ^ 2 * x)) := by
    simpa only [Int.cast_neg, Int.cast_add, Int.cast_natCast, Int.cast_one, neg_sq] using psi_summable hx
  rw [theta, tsum_of_nat_of_neg_add_one hp hn]
  simp only [Int.cast_natCast, Int.cast_neg, Int.cast_add, Int.cast_one, neg_sq]
  rw [(gaussian_nat_summable hx).tsum_eq_zero_add]
  simp only [Nat.cast_zero, zero_pow (by decide : 2 ≠ 0), mul_zero, zero_mul, Real.exp_zero,
    Nat.cast_add, Nat.cast_one]
  change 1 + psi x + psi x = 1 + 2 * psi x
  ring

/-- Factor out the first Gaussian decay, uniformly for x ≥ 1. -/
lemma term_le_fixed_tail {x : ℝ} (hx : 1 ≤ x) (n : ℕ) :
    Real.exp (-Real.pi * ((n : ℝ) + 1) ^ 2 * x) ≤
      Real.exp (-Real.pi * ((n : ℝ) + 1) ^ 2) *
        Real.exp Real.pi * Real.exp (-Real.pi * x) := by
  rw [← Real.exp_add, ← Real.exp_add]
  apply Real.exp_le_exp.mpr
  have hn : 0 ≤ (n : ℝ) := Nat.cast_nonneg n
  have hs : 0 ≤ ((n : ℝ) + 1) ^ 2 - 1 := by nlinarith
  have h := mul_nonneg (mul_nonneg Real.pi_pos.le hs) (sub_nonneg.mpr hx)
  nlinarith

/-- The j = 0 case of the stated exponential tail bound, with a fixed finite constant. -/
theorem psi_tail_bound {x : ℝ} (hx : 1 ≤ x) :
    |psi x| ≤ (psi 1 * Real.exp Real.pi) * Real.exp (-Real.pi * x) := by
  have hxpos : 0 < x := lt_of_lt_of_le zero_lt_one hx
  have hnonneg : 0 ≤ psi x := tsum_nonneg (fun _ => (Real.exp_pos _).le)
  rw [abs_of_nonneg hnonneg]
  have hsum := ((psi_summable (by norm_num : (0 : ℝ) < 1)).mul_right
    (Real.exp Real.pi)).mul_right (Real.exp (-Real.pi * x))
  simp only [mul_one] at hsum
  have h := (psi_summable hxpos).tsum_le_tsum (term_le_fixed_tail hx) hsum
  simpa only [mul_one, tsum_mul_right, psi] using h

/-- Explicit existential form of the order-zero estimate in L016. -/
theorem exists_psi_tail_constant :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ x : ℝ, 1 ≤ x → |psi x| ≤ C * Real.exp (-Real.pi * x) := by
  refine ⟨psi 1 * Real.exp Real.pi, mul_nonneg ?_ (Real.exp_pos _).le, ?_⟩
  · exact tsum_nonneg (fun _ => (Real.exp_pos _).le)
  · intro x hx
    exact psi_tail_bound hx

/-- Polynomial-Gaussian majorants for every derivative order are summable. -/
theorem derivative_majorant_summable (j : ℕ) {a : ℝ} (ha : 0 < a) :
    Summable (fun n : ℕ => (Real.pi * ((n : ℝ) + 1) ^ 2) ^ j *
      Real.exp (-Real.pi * ((n : ℝ) + 1) ^ 2 * a)) := by
  have hq : ‖Real.exp (-Real.pi * a)‖ < 1 := by
    rw [Real.norm_eq_abs, abs_of_pos (Real.exp_pos _), Real.exp_lt_one_iff]
    nlinarith [Real.pi_pos]
  have hs : Summable (fun n : ℕ => ((n + 1 : ℕ) : ℝ) ^ (2 * j) *
      Real.exp (-Real.pi * a) ^ (n + 1)) :=
    (summable_nat_add_iff (f := fun n : ℕ =>
      (n : ℝ) ^ (2 * j) * Real.exp (-Real.pi * a) ^ n) 1).mpr
      (summable_pow_mul_geometric_of_norm_lt_one (2 * j) hq)
  have hmajor := hs.mul_left (Real.pi ^ j)
  apply Summable.of_nonneg_of_le (fun n => by positivity) _ hmajor
  intro n
  have h := mul_le_mul_of_nonneg_left (term_le_geometric ha n)
    (show 0 ≤ (Real.pi * ((n : ℝ) + 1) ^ 2) ^ j by positivity)
  simpa only [Nat.cast_add, Nat.cast_one, mul_pow, ← pow_mul, mul_assoc] using h

/-- A single summable majorant controls derivative terms on every x ≥ a > 0. -/
theorem derivative_term_norm_le (j : ℕ) {a x : ℝ} (hx : a ≤ x) (n : ℕ) :
    ‖(-Real.pi * ((n : ℝ) + 1) ^ 2) ^ j *
      Real.exp (-Real.pi * ((n : ℝ) + 1) ^ 2 * x)‖ ≤
    (Real.pi * ((n : ℝ) + 1) ^ 2) ^ j *
      Real.exp (-Real.pi * ((n : ℝ) + 1) ^ 2 * a) := by
  rw [norm_mul, norm_pow, Real.norm_eq_abs, abs_mul, abs_neg,
    abs_of_pos Real.pi_pos, abs_of_nonneg (sq_nonneg _),
    Real.norm_eq_abs, abs_of_pos (Real.exp_pos _)]
  apply mul_le_mul_of_nonneg_left _ (by positivity)
  apply Real.exp_le_exp.mpr
  exact mul_le_mul_of_nonpos_left hx
    (mul_nonpos_of_nonpos_of_nonneg (neg_nonpos.mpr Real.pi_pos.le) (sq_nonneg _))

/-- The formal order-j Gaussian series converges at every positive point. -/
theorem derivative_series_summable (j : ℕ) {x : ℝ} (hx : 0 < x) :
    Summable (fun n : ℕ => (-Real.pi * ((n : ℝ) + 1) ^ 2) ^ j *
      Real.exp (-Real.pi * ((n : ℝ) + 1) ^ 2 * x)) :=
  Summable.of_norm_bounded (derivative_majorant_summable j hx)
    (derivative_term_norm_le j le_rfl)

/-- Termwise differentiation connects successive formal derivative series. -/
theorem hasDerivAt_derivative_series (j : ℕ) {x : ℝ} (hx : 0 < x) :
    HasDerivAt
      (fun y : ℝ => ∑' n : ℕ, (-Real.pi * ((n : ℝ) + 1) ^ 2) ^ j *
        Real.exp (-Real.pi * ((n : ℝ) + 1) ^ 2 * y))
      (∑' n : ℕ, (-Real.pi * ((n : ℝ) + 1) ^ 2) ^ (j + 1) *
        Real.exp (-Real.pi * ((n : ℝ) + 1) ^ 2 * x)) x := by
  have ha : 0 < x / 2 := by linarith
  have hmem : x ∈ Set.Ioi (x / 2) := by simp only [Set.mem_Ioi]; linarith
  apply hasDerivAt_tsum_of_isPreconnected
    (g := fun (n : ℕ) (y : ℝ) => (-Real.pi * ((n : ℝ) + 1) ^ 2) ^ j *
      Real.exp (-Real.pi * ((n : ℝ) + 1) ^ 2 * y))
    (g' := fun (n : ℕ) (y : ℝ) => (-Real.pi * ((n : ℝ) + 1) ^ 2) ^ (j + 1) *
      Real.exp (-Real.pi * ((n : ℝ) + 1) ^ 2 * y))
    (derivative_majorant_summable (j + 1) ha) isOpen_Ioi
    (convex_Ioi (x / 2)).isPreconnected _ _ hmem
    (derivative_series_summable j hx) hmem
  · intro n y _
    have h := (((hasDerivAt_id y).const_mul
      (-Real.pi * ((n : ℝ) + 1) ^ 2)).exp).const_mul
      ((-Real.pi * ((n : ℝ) + 1) ^ 2) ^ j)
    convert h using 1
    · rfl
    · rfl
    · simp only [pow_succ, mul_one, id_eq]
      ring
  · intro n y hy
    exact derivative_term_norm_le (j + 1) (le_of_lt hy) n

/-- Every iterated derivative of ψ is the corresponding Gaussian series on x > 0. -/
theorem iteratedDeriv_psi (j : ℕ) {x : ℝ} (hx : 0 < x) :
    iteratedDeriv j psi x =
      ∑' n : ℕ, (-Real.pi * ((n : ℝ) + 1) ^ 2) ^ j *
        Real.exp (-Real.pi * ((n : ℝ) + 1) ^ 2 * x) := by
  induction j generalizing x with
  | zero => simp [psi]
  | succ j ih =>
    rw [iteratedDeriv_succ]
    apply HasDerivAt.deriv
    apply (hasDerivAt_derivative_series j hx).congr_of_eventuallyEq
    filter_upwards [isOpen_Ioi.mem_nhds hx] with y hy
    exact ih hy

/-- A finite constant independent of x controls each derivative on x ≥ 1. -/
theorem exists_derivative_tail_constant (j : ℕ) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ x : ℝ, 1 ≤ x →
      |iteratedDeriv j psi x| ≤ C * Real.exp (-Real.pi * x) := by
  let b : ℕ → ℝ := fun n => (Real.pi * ((n : ℝ) + 1) ^ 2) ^ j *
    Real.exp (-Real.pi * ((n : ℝ) + 1) ^ 2)
  have hb : Summable b := by
    simpa only [mul_one] using derivative_majorant_summable j (by norm_num : (0 : ℝ) < 1)
  refine ⟨(∑' n, b n) * Real.exp Real.pi,
    mul_nonneg (tsum_nonneg (fun n => by dsimp [b]; positivity)) (Real.exp_pos _).le, ?_⟩
  intro x hx
  have hxpos : 0 < x := lt_of_lt_of_le zero_lt_one hx
  rw [iteratedDeriv_psi j hxpos, ← Real.norm_eq_abs]
  calc
    ‖∑' n : ℕ, (-Real.pi * ((n : ℝ) + 1) ^ 2) ^ j *
        Real.exp (-Real.pi * ((n : ℝ) + 1) ^ 2 * x)‖ ≤
        ∑' n : ℕ, ‖(-Real.pi * ((n : ℝ) + 1) ^ 2) ^ j *
          Real.exp (-Real.pi * ((n : ℝ) + 1) ^ 2 * x)‖ :=
      norm_tsum_le_tsum_norm (derivative_series_summable j hxpos).norm
    _ ≤ ∑' n : ℕ, b n * Real.exp Real.pi * Real.exp (-Real.pi * x) := by
      apply (derivative_series_summable j hxpos).norm.tsum_le_tsum _
        ((hb.mul_right (Real.exp Real.pi)).mul_right (Real.exp (-Real.pi * x)))
      intro n
      rw [norm_mul, norm_pow, Real.norm_eq_abs, abs_mul, abs_neg,
        abs_of_pos Real.pi_pos, abs_of_nonneg (sq_nonneg _),
        Real.norm_eq_abs, abs_of_pos (Real.exp_pos _)]
      simpa only [b, mul_assoc] using
        mul_le_mul_of_nonneg_left (term_le_fixed_tail hx n)
          (show 0 ≤ (Real.pi * ((n : ℝ) + 1) ^ 2) ^ j by positivity)
    _ = _ := by rw [tsum_mul_right, tsum_mul_right]

/-- The full transformation and all-orders tail conclusion of L016. -/
theorem L016 :
    (∀ x : ℝ, 0 < x → theta x = x ^ (-(1 / 2 : ℝ)) * theta (1 / x)) ∧
    (∀ j : ℕ, ∃ C : ℝ, 0 ≤ C ∧ ∀ x : ℝ, 1 ≤ x →
      |iteratedDeriv j psi x| ≤ C * Real.exp (-Real.pi * x)) :=
  ⟨fun _ hx => theta_transformation hx, exists_derivative_tail_constant⟩

end Rh.L016

#print axioms Rh.L016.theta_transformation
#print axioms Rh.L016.term_le_geometric
#print axioms Rh.L016.geometric_summable
#print axioms Rh.L016.psi_summable

#print axioms Rh.L016.gaussian_nat_summable
#print axioms Rh.L016.theta_summable
#print axioms Rh.L016.theta_eq_one_add_two_psi

#print axioms Rh.L016.term_le_fixed_tail
#print axioms Rh.L016.psi_tail_bound
#print axioms Rh.L016.exists_psi_tail_constant

#print axioms Rh.L016.derivative_majorant_summable
#print axioms Rh.L016.derivative_term_norm_le

#print axioms Rh.L016.derivative_series_summable
#print axioms Rh.L016.hasDerivAt_derivative_series

#print axioms Rh.L016.iteratedDeriv_psi

#print axioms Rh.L016.exists_derivative_tail_constant
#print axioms Rh.L016.L016
