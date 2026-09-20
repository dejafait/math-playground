import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.Analysis.Calculus.ParametricIntervalIntegral
import Mathlib.Analysis.SpecialFunctions.Complex.Log
import Mathlib.Tactic

/-! Full formalization of L015: the indicator-kernel transform is entire,
positive on the real axis, and has a nonreal zero in the claimed strip. -/

open MeasureTheory

namespace Rh.L015

noncomputable def finiteTransform (s : ℂ) : ℂ :=
  (∫ u : ℝ in (0 : ℝ)..1, Complex.exp (-s * u)) +
    ∫ u : ℝ in (2 : ℝ)..4, Complex.exp (-s * u)

noncomputable def kernel (u : ℝ) : ℝ :=
  (Set.Icc (0 : ℝ) 1 ∪ Set.Icc 2 4).indicator (fun _ => 1) u

noncomputable def H (s : ℂ) : ℂ :=
  ∫ u : ℝ in Set.Ici (0 : ℝ), (kernel u : ℂ) * Complex.exp (-s * u)

theorem H_eq_finiteTransform (s : ℂ) : H s = finiteTransform s := by
  have hc : Continuous (fun u : ℝ => Complex.exp (-s * u)) := by fun_prop
  have hi : (fun u : ℝ => (kernel u : ℂ) * Complex.exp (-s * u)) =
      (Set.Icc (0 : ℝ) 1 ∪ Set.Icc 2 4).indicator
        (fun u : ℝ => Complex.exp (-s * u)) := by
    ext u
    by_cases hu : u ∈ Set.Icc (0 : ℝ) 1 ∪ Set.Icc 2 4 <;>
      simp [kernel, Set.indicator, hu]
  have hsub : Set.Icc (0 : ℝ) 1 ∪ Set.Icc 2 4 ⊆ Set.Ici 0 := by
    intro u hu
    rcases hu with hu | hu
    · exact hu.1
    · exact le_trans (by norm_num) hu.1
  have hd : Disjoint (Set.Icc (0 : ℝ) 1) (Set.Icc 2 4) := by
    apply Set.disjoint_left.mpr
    intro u hu hv
    linarith [hu.2, hv.1]
  unfold H
  rw [hi, setIntegral_indicator (measurableSet_Icc.union measurableSet_Icc),
    Set.inter_eq_right.mpr hsub,
    setIntegral_union hd measurableSet_Icc
      hc.continuousOn.integrableOn_Icc hc.continuousOn.integrableOn_Icc,
    integral_Icc_eq_integral_Ioc, integral_Icc_eq_integral_Ioc]
  unfold finiteTransform
  rw [intervalIntegral.integral_of_le (by norm_num : (0 : ℝ) ≤ 1),
    intervalIntegral.integral_of_le (by norm_num : (2 : ℝ) ≤ 4)]

/-- Compact parameter and integration domains give a uniform derivative bound. -/
lemma intervalTransform_differentiable (a b : ℝ) :
    Differentiable ℂ (fun s : ℂ => ∫ u : ℝ in a..b, Complex.exp (-s * u)) := by
  intro s
  have hc : Continuous (fun p : ℂ × ℝ =>
      Complex.exp (-p.1 * p.2) * (-(p.2 : ℂ))) := by fun_prop
  obtain ⟨C, hC⟩ := ((isCompact_closedBall s 1).prod (isCompact_uIcc (a := a) (b := b))).exists_bound_of_continuousOn hc.continuousOn
  apply (intervalIntegral.hasDerivAt_integral_of_dominated_loc_of_deriv_le
    (F' := fun z u => Complex.exp (-z * u) * (-(u : ℂ)))
    (bound := fun _ => C) (s := Metric.ball s 1)
    (Metric.ball_mem_nhds s (by norm_num)) ?_ ?_ ?_ ?_ ?_ ?_).2.differentiableAt
  · exact Filter.Eventually.of_forall (fun z =>
      (show Continuous (fun u : ℝ => Complex.exp (-z * u)) by fun_prop).aestronglyMeasurable)
  · exact (show Continuous (fun u : ℝ => Complex.exp (-s * u)) by fun_prop).intervalIntegrable a b
  · exact (show Continuous (fun u : ℝ =>
      Complex.exp (-s * u) * (-(u : ℂ))) by fun_prop).aestronglyMeasurable
  · exact Filter.Eventually.of_forall (fun u hu z hz =>
      hC (z, u) ⟨Metric.ball_subset_closedBall hz, Set.uIoc_subset_uIcc hu⟩)
  · exact intervalIntegrable_const
  · apply Filter.Eventually.of_forall
    intro u _ z _
    simpa using (((hasDerivAt_id z).neg.mul_const (u : ℂ)).cexp)

theorem H_entire : Differentiable ℂ H := by
  have heq : H = finiteTransform := funext H_eq_finiteTransform
  rw [heq]
  exact (intervalTransform_differentiable 0 1).add (intervalTransform_differentiable 2 4)

theorem finiteTransform_zero : finiteTransform 0 = 3 := by
  norm_num [finiteTransform]

theorem finiteTransform_formula (s : ℂ) (hs : s ≠ 0) :
    finiteTransform s =
      (1 - Complex.exp (-s)) *
        (1 + Complex.exp (-2 * s) + Complex.exp (-3 * s)) / s := by
  unfold finiteTransform
  rw [integral_exp_mul_complex (neg_ne_zero.mpr hs),
    integral_exp_mul_complex (neg_ne_zero.mpr hs)]
  norm_num
  have h2 : Complex.exp (-2 * s) = Complex.exp (-s) ^ 2 := by
    rw [show -2 * s = -s + -s by ring, Complex.exp_add]
    ring
  have h3 : Complex.exp (-3 * s) = Complex.exp (-s) ^ 3 := by
    rw [show -3 * s = -s + (-s + -s) by ring, Complex.exp_add,
      Complex.exp_add]
    ring
  have h4 : Complex.exp (-(s * 4)) = Complex.exp (-s) ^ 4 := by
    rw [show -(s * 4) = (-s + -s) + (-s + -s) by ring,
      Complex.exp_add, Complex.exp_add]
    ring
  have h2' : Complex.exp (-(s * 2)) = Complex.exp (-s) ^ 2 := by
    convert h2 using 1 <;> congr 1 <;> ring
  simp only [neg_mul] at h2 h3
  rw [h2, h3, h4, h2']
  field_simp
  <;> ring

theorem H_zero : H 0 = 3 := by
  rw [H_eq_finiteTransform, finiteTransform_zero]

theorem H_formula (s : ℂ) (hs : s ≠ 0) :
    H s = (1 - Complex.exp (-s)) *
      (1 + Complex.exp (-2 * s) + Complex.exp (-3 * s)) / s := by
  rw [H_eq_finiteTransform, finiteTransform_formula s hs]

theorem H_real_pos (σ : ℝ) : (H (σ : ℂ)).im = 0 ∧ 0 < (H (σ : ℂ)).re := by
  have he (u : ℝ) : Complex.exp (-(σ : ℂ) * u) =
      (Real.exp (-σ * u) : ℂ) := by
    rw [Complex.ofReal_exp]
    push_cast
    rfl
  have hc : Continuous (fun u : ℝ => Real.exp (-σ * u)) := by fun_prop
  have hp (a b : ℝ) (hab : a < b) :
      0 < ∫ u : ℝ in a..b, Real.exp (-σ * u) := by
    apply intervalIntegral.integral_pos hab hc.continuousOn
    · intro u _
      exact (Real.exp_pos _).le
    · exact ⟨a, ⟨le_rfl, hab.le⟩, Real.exp_pos _⟩
  rw [H_eq_finiteTransform]
  simp only [finiteTransform, he, intervalIntegral.integral_ofReal,
    Complex.add_im, Complex.ofReal_im, add_zero, Complex.add_re, Complex.ofReal_re]
  exact ⟨True.intro, add_pos (hp 0 1 (by norm_num)) (hp 2 4 (by norm_num))⟩


/-- The real cubic root used in the existing counterexample construction. -/
theorem cubic_real_root : ∃ r : ℝ, -2 < r ∧ r < -1 ∧ 1 + r ^ 2 + r ^ 3 = 0 := by
  have hc : Continuous (fun r : ℝ => 1 + r ^ 2 + r ^ 3) := by fun_prop
  obtain ⟨r, hr, he⟩ := intermediate_value_Icc (by norm_num : (-2 : ℝ) ≤ -1)
    hc.continuousOn (by norm_num : (0 : ℝ) ∈ Set.Icc
      (1 + (-2 : ℝ) ^ 2 + (-2 : ℝ) ^ 3) (1 + (-1 : ℝ) ^ 2 + (-1 : ℝ) ^ 3))
  refine ⟨r, ?_, ?_, he⟩
  · rcases eq_or_lt_of_le hr.1 with h | h
    · subst r
      norm_num at he
    · exact h
  · rcases eq_or_lt_of_le hr.2 with h | h
    · subst r
      norm_num at he
    · exact h

/-- A nonreal cubic root with the exact modulus bounds needed for the logarithm. -/
theorem cubic_nonreal_root : ∃ z : ℂ,
    z.im ≠ 0 ∧ 1 + z ^ 2 + z ^ 3 = 0 ∧ 1 / 2 < ‖z‖ ^ 2 ∧ ‖z‖ ^ 2 < 1 := by
  obtain ⟨r, hrlo, hrhi, hr⟩ := cubic_real_root
  let a : ℝ := -(1 + r) / 2
  let d : ℝ := r ^ 2 + r - a ^ 2
  have hd : 0 < d := by
    dsimp [d, a]
    nlinarith [sq_nonneg (r + 1)]
  let b : ℝ := Real.sqrt d
  have hb : 0 < b := Real.sqrt_pos.2 hd
  have hb2 : b ^ 2 = d := Real.sq_sqrt hd.le
  let z : ℂ := ⟨a, b⟩
  have hz : 1 + z ^ 2 + z ^ 3 = 0 := by
    apply Complex.ext <;> simp [z, Complex.mul_re, Complex.mul_im, pow_succ] <;>
      dsimp [d, a] at * <;> nlinarith
  have hn : ‖z‖ ^ 2 = r ^ 2 + r := by
    rw [Complex.sq_norm]
    simp [Complex.normSq, z]
    dsimp [d] at hb2
    nlinarith
  refine ⟨z, ne_of_gt hb, hz, ?_, ?_⟩ <;> rw [hn]
  · nlinarith
  · nlinarith

/-- The logarithmic construction places a nonreal zero in the claimed strip. -/
theorem H_nonreal_zero : ∃ s : ℂ, H s = 0 ∧ s.im ≠ 0 ∧
    0 < s.re ∧ s.re < Real.log 2 / 2 ∧ Real.log 2 / 2 < 1 := by
  obtain ⟨z, hzi, hz, hlo, hhi⟩ := cubic_nonreal_root
  have hz0 : z ≠ 0 := by
    intro h
    simp [h] at hzi
  let s := -Complex.log z
  have hexp : Complex.exp (-s) = z := by
    simpa [s] using Complex.exp_log hz0
  have hsim : s.im ≠ 0 := by
    intro h
    have hi := congrArg Complex.im hexp
    simp [Complex.exp_im, h] at hi
    exact hzi hi.symm
  have hs0 : s ≠ 0 := by
    intro h
    simp [h] at hsim
  have hn : 0 < ‖z‖ := norm_pos_iff.mpr hz0
  have hloghi : Real.log (‖z‖ ^ 2) < 0 := by
    simpa using Real.strictMonoOn_log (show (0 : ℝ) < ‖z‖ ^ 2 by positivity)
      (show (0 : ℝ) < 1 by norm_num) hhi
  have hloglo : -Real.log 2 < Real.log (‖z‖ ^ 2) := by
    have h := Real.strictMonoOn_log (show (0 : ℝ) < 1 / 2 by norm_num)
      (show (0 : ℝ) < ‖z‖ ^ 2 by positivity) hlo
    simpa [Real.log_div] using h
  have hre : s.re = -Real.log ‖z‖ := by simp [s, Complex.log_re]
  rw [Real.log_pow] at hloghi hloglo
  have h2 : Complex.exp (-2 * s) = z ^ 2 := by
    rw [show -2 * s = -s + -s by ring, Complex.exp_add, hexp]
    ring
  have h3 : Complex.exp (-3 * s) = z ^ 3 := by
    rw [show -3 * s = -s + (-s + -s) by ring, Complex.exp_add,
      Complex.exp_add, hexp]
    ring
  refine ⟨s, ?_, hsim, ?_, ?_, ?_⟩
  · rw [H_formula s hs0, h2, h3, hz]
    simp
  · rw [hre]
    norm_num at hloghi
    linarith
  · rw [hre]
    norm_num at hloglo
    linarith
  · have h := Real.log_lt_sub_one_of_pos (by norm_num : (0 : ℝ) < 2)
      (by norm_num : (2 : ℝ) ≠ 1)
    linarith

/-- All assertions of the existing L015 statement for its indicator kernel. -/
theorem L015 : Differentiable ℂ H ∧
    (∀ σ : ℝ, (H (σ : ℂ)).im = 0 ∧ 0 < (H (σ : ℂ)).re) ∧
    ∃ s : ℂ, H s = 0 ∧ s.im ≠ 0 ∧ 0 < s.re ∧
      s.re < Real.log 2 / 2 ∧ Real.log 2 / 2 < 1 :=
  ⟨H_entire, H_real_pos, H_nonreal_zero⟩

end Rh.L015

#print axioms Rh.L015.finiteTransform_zero
#print axioms Rh.L015.finiteTransform_formula

#print axioms Rh.L015.H_eq_finiteTransform

#print axioms Rh.L015.H_zero
#print axioms Rh.L015.H_formula

#print axioms Rh.L015.intervalTransform_differentiable
#print axioms Rh.L015.H_entire

#print axioms Rh.L015.H_real_pos

#print axioms Rh.L015.cubic_real_root
#print axioms Rh.L015.cubic_nonreal_root

#print axioms Rh.L015.H_nonreal_zero
#print axioms Rh.L015.L015
