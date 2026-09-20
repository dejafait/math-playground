import Rh.L016
import Mathlib.Analysis.SpecialFunctions.Gamma.Basic
import Mathlib.Analysis.Calculus.ParametricIntegral
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.Analysis.SpecialFunctions.Gaussian.GaussianIntegral

/-! Partial formalization of L017. The literal integral and reflection are
proved here, together with absolute convergence and entireness. The full Mellin
identity remains open. -/

open MeasureTheory
open scoped Topology

namespace Rh.L017

/-- Powers on the positive real axis use the real logarithm, as in L017. -/
noncomputable def splitIntegrand (s : ℂ) (x : ℝ) : ℂ :=
  (L016.psi x : ℂ) *
    (Complex.exp (s / 2 * (Real.log x : ℂ)) +
      Complex.exp ((1 - s) / 2 * (Real.log x : ℂ))) / (x : ℂ)

/-- The literal split Mellin integral; convergence is established below. -/
noncomputable def splitMellin (s : ℂ) : ℂ :=
  ∫ x in Set.Ici (1 : ℝ), splitIntegrand s x

lemma splitIntegrand_reflection (s : ℂ) (x : ℝ) :
    splitIntegrand s x = splitIntegrand (1 - s) x := by
  unfold splitIntegrand
  rw [sub_sub_cancel]
  rw [add_comm (Complex.exp (s / 2 * (Real.log x : ℂ)))]

/-- Reflection follows from pointwise equality, independently of convergence.
This theorem alone does not establish the full statement of L017. -/
theorem splitMellin_reflection (s : ℂ) :
    splitMellin s = splitMellin (1 - s) := by
  unfold splitMellin
  congr 1
  funext x
  exact splitIntegrand_reflection s x

/-- The real-logarithm power has the expected real-power norm. -/
lemma norm_log_power (z : ℂ) {x : ℝ} (hx : 0 < x) :
    ‖Complex.exp (z * (Real.log x : ℂ))‖ = x ^ z.re := by
  rw [Complex.norm_exp, Real.rpow_def_of_pos hx]
  simp [Complex.mul_re, mul_comm]

/-- The exponential tail in L016 controls the literal split integrand. -/
lemma splitIntegrand_norm_le (s : ℂ) {x : ℝ} (hx : 1 ≤ x) :
    ‖splitIntegrand s x‖ ≤
      (L016.psi 1 * Real.exp Real.pi) * Real.exp (-Real.pi * x) *
        (x ^ (s / 2).re + x ^ ((1 - s) / 2).re) / x := by
  have hp : 0 < x := lt_of_lt_of_le zero_lt_one hx
  unfold splitIntegrand
  rw [norm_div, norm_mul, Complex.norm_real, Real.norm_eq_abs,
    Complex.norm_real, Real.norm_eq_abs, abs_of_pos hp]
  apply div_le_div_of_nonneg_right _ hp.le
  apply mul_le_mul (L016.psi_tail_bound hx) _ (norm_nonneg _) _
  · exact (norm_add_le _ _).trans_eq (by rw [norm_log_power _ hp, norm_log_power _ hp])
  · exact le_trans (abs_nonneg _) (L016.psi_tail_bound hx)

/-- A common exponent gives the compact-parameter majorant used in the proof. -/
lemma splitIntegrand_uniform_bound (s : ℂ) {A x : ℝ} (hx : 1 ≤ x)
    (hleft : (s / 2).re ≤ A) (hright : ((1 - s) / 2).re ≤ A) :
    ‖splitIntegrand s x‖ ≤
      2 * (L016.psi 1 * Real.exp Real.pi) * Real.exp (-Real.pi * x) * x ^ (A - 1) := by
  have hp : 0 < x := lt_of_lt_of_le zero_lt_one hx
  have hc : 0 ≤ L016.psi 1 * Real.exp Real.pi :=
    mul_nonneg (tsum_nonneg (fun _ => (Real.exp_pos _).le)) (Real.exp_pos _).le
  calc
    ‖splitIntegrand s x‖ ≤
        (L016.psi 1 * Real.exp Real.pi) * Real.exp (-Real.pi * x) *
          (x ^ (s / 2).re + x ^ ((1 - s) / 2).re) / x := splitIntegrand_norm_le s hx
    _ ≤ (L016.psi 1 * Real.exp Real.pi) * Real.exp (-Real.pi * x) *
          (x ^ A + x ^ A) / x := by
      apply div_le_div_of_nonneg_right _ hp.le
      exact mul_le_mul_of_nonneg_left
        (add_le_add (Real.rpow_le_rpow_of_exponent_le hx hleft)
          (Real.rpow_le_rpow_of_exponent_le hx hright))
        (mul_nonneg hc (Real.exp_pos _).le)
    _ = _ := by rw [Real.rpow_sub hp, Real.rpow_one]; ring

/-- The literal integrand is continuous on the integration domain. -/
lemma splitIntegrand_continuousOn (s : ℂ) :
    ContinuousOn (splitIntegrand s) (Set.Ici 1) := by
  intro x hx
  have hp : 0 < x := lt_of_lt_of_le zero_lt_one hx
  have hpsi : ContinuousAt L016.psi x := by
    unfold L016.psi
    simpa only [pow_zero, one_mul] using (L016.hasDerivAt_derivative_series 0 hp).continuousAt
  have hlog : ContinuousAt (fun y : ℝ => (Real.log y : ℂ)) x :=
    Complex.continuous_ofReal.continuousAt.comp (Real.continuousAt_log hp.ne')
  exact ((Complex.continuous_ofReal.continuousAt.comp hpsi).mul
    (((continuousAt_const.mul hlog).cexp).add
      ((continuousAt_const.mul hlog).cexp))).div
        Complex.continuous_ofReal.continuousAt
        (by exact_mod_cast hp.ne') |>.continuousWithinAt

/-- Absolute convergence of the split Mellin integral for every complex parameter. -/
theorem splitIntegrand_integrable (s : ℂ) :
    IntegrableOn (splitIntegrand s) (Set.Ici 1) := by
  let A : ℝ := max 1 (max (s / 2).re ((1 - s) / 2).re)
  have hA : 1 ≤ A := le_max_left _ _
  have hbase := integrableOn_rpow_mul_exp_neg_mul_rpow
    (s := A - 1) (p := 1) (b := Real.pi) (by linarith) zero_lt_one Real.pi_pos
  have hmajor : IntegrableOn
      (fun x : ℝ => 2 * (L016.psi 1 * Real.exp Real.pi) *
        Real.exp (-Real.pi * x) * x ^ (A - 1)) (Set.Ici 1) := by
    have h := (hbase.mono_set (show Set.Ici (1 : ℝ) ⊆ Set.Ioi 0 from
      by
        intro x hx
        exact lt_of_lt_of_le (show (0 : ℝ) < 1 by norm_num) hx)).const_mul
        (2 * (L016.psi 1 * Real.exp Real.pi))
    simpa only [IntegrableOn, Real.rpow_one, mul_left_comm, mul_comm, mul_assoc] using h
  apply hmajor.mono' ((splitIntegrand_continuousOn s).aestronglyMeasurable measurableSet_Ici)
  filter_upwards [ae_restrict_mem measurableSet_Ici] with x hx
  exact splitIntegrand_uniform_bound s hx
    ((le_max_left _ _).trans (le_max_right _ _))
    ((le_max_right _ _).trans (le_max_right _ _))

/-- The parameter derivative required for dominated differentiation. -/
noncomputable def splitIntegrandDeriv (s : ℂ) (x : ℝ) : ℂ :=
  (L016.psi x : ℂ) *
    (Complex.exp (s / 2 * (Real.log x : ℂ)) -
      Complex.exp ((1 - s) / 2 * (Real.log x : ℂ))) *
        (Real.log x : ℂ) / 2 / (x : ℂ)

lemma hasDerivAt_splitIntegrand (s : ℂ) (x : ℝ) :
    HasDerivAt (fun z => splitIntegrand z x) (splitIntegrandDeriv s x) s := by
  have hl := (((hasDerivAt_id s).div_const 2).mul_const
    (Real.log x : ℂ)).cexp
  have hr := ((((hasDerivAt_const s (1 : ℂ)).sub (hasDerivAt_id s)).div_const 2).mul_const
    (Real.log x : ℂ)).cexp
  convert (((hl.add hr).const_mul (L016.psi x : ℂ)).div_const (x : ℂ)) using 1 <;>
    first | rfl | (dsimp [splitIntegrandDeriv]; ring)

/-- The logarithmic derivative factor can be absorbed by one power of x. -/
lemma splitIntegrandDeriv_uniform_bound (s : ℂ) {A x : ℝ} (hx : 1 ≤ x)
    (hleft : (s / 2).re ≤ A) (hright : ((1 - s) / 2).re ≤ A) :
    ‖splitIntegrandDeriv s x‖ ≤
      (L016.psi 1 * Real.exp Real.pi) * Real.exp (-Real.pi * x) * x ^ A := by
  have hp : 0 < x := lt_of_lt_of_le zero_lt_one hx
  have hlog : 0 ≤ Real.log x := Real.log_nonneg hx
  have hc : 0 ≤ L016.psi 1 * Real.exp Real.pi :=
    mul_nonneg (tsum_nonneg (fun _ => (Real.exp_pos _).le)) (Real.exp_pos _).le
  have he : 0 ≤ (L016.psi 1 * Real.exp Real.pi) * Real.exp (-Real.pi * x) :=
    mul_nonneg hc (Real.exp_pos _).le
  have hdiff :
      ‖Complex.exp (s / 2 * (Real.log x : ℂ)) -
        Complex.exp ((1 - s) / 2 * (Real.log x : ℂ))‖ ≤ 2 * x ^ A := by
    calc
      _ ≤ ‖Complex.exp (s / 2 * (Real.log x : ℂ))‖ +
          ‖Complex.exp ((1 - s) / 2 * (Real.log x : ℂ))‖ := norm_sub_le _ _
      _ = x ^ (s / 2).re + x ^ ((1 - s) / 2).re := by
        rw [norm_log_power _ hp, norm_log_power _ hp]
      _ ≤ x ^ A + x ^ A := add_le_add
        (Real.rpow_le_rpow_of_exponent_le hx hleft)
        (Real.rpow_le_rpow_of_exponent_le hx hright)
      _ = _ := by ring
  have hproduct := mul_le_mul (L016.psi_tail_bound hx) hdiff (norm_nonneg _) he
  unfold splitIntegrandDeriv
  simp only [norm_div, norm_mul, Complex.norm_real, Real.norm_eq_abs,
    abs_of_pos hp, abs_of_nonneg hlog, Complex.norm_ofNat]
  calc
    _ ≤ ((L016.psi 1 * Real.exp Real.pi) * Real.exp (-Real.pi * x) *
        (2 * x ^ A)) * Real.log x / 2 / x := by
      exact div_le_div_of_nonneg_right
        (div_le_div_of_nonneg_right (mul_le_mul_of_nonneg_right hproduct hlog)
          (by norm_num)) hp.le
    _ ≤ ((L016.psi 1 * Real.exp Real.pi) * Real.exp (-Real.pi * x) *
        (2 * x ^ A)) * x / 2 / x := by
      apply div_le_div_of_nonneg_right _ hp.le
      apply div_le_div_of_nonneg_right _ (by norm_num)
      exact mul_le_mul_of_nonneg_left (Real.log_le_self hp.le)
        (mul_nonneg he (mul_nonneg (by norm_num) (Real.rpow_nonneg hp.le _)))
    _ = _ := by field_simp

/-- The derivative majorant is integrable, uniformly for bounded real exponents. -/
lemma splitIntegrandDeriv_majorant_integrable {A : ℝ} (hA : 0 ≤ A) :
    IntegrableOn (fun x : ℝ =>
      (L016.psi 1 * Real.exp Real.pi) * Real.exp (-Real.pi * x) * x ^ A)
      (Set.Ici 1) := by
  have hbase := integrableOn_rpow_mul_exp_neg_mul_rpow
    (s := A) (p := 1) (b := Real.pi) (by linarith) zero_lt_one Real.pi_pos
  have h := (hbase.mono_set (show Set.Ici (1 : ℝ) ⊆ Set.Ioi 0 from
    by
      intro x hx
      exact lt_of_lt_of_le (show (0 : ℝ) < 1 by norm_num) hx)).const_mul
        (L016.psi 1 * Real.exp Real.pi)
  simpa only [IntegrableOn, Real.rpow_one, mul_left_comm, mul_comm, mul_assoc] using h

/-- Every parameter has a neighborhood with one integrable derivative bound. -/
theorem splitIntegrandDeriv_locally_dominated (s₀ : ℂ) :
    ∃ bound : ℝ → ℝ, IntegrableOn bound (Set.Ici 1) ∧
      ∀ᶠ s in 𝓝 s₀, ∀ x : ℝ, 1 ≤ x → ‖splitIntegrandDeriv s x‖ ≤ bound x := by
  let A : ℝ := max 0 (max (s₀ / 2).re ((1 - s₀) / 2).re) + 1
  have hA : 0 ≤ A := by
    dsimp [A]
    linarith [le_max_left (0 : ℝ) (max (s₀ / 2).re ((1 - s₀) / 2).re)]
  have hlA : (s₀ / 2).re < A :=
    lt_of_le_of_lt ((le_max_left _ _).trans (le_max_right _ _)) (lt_add_one _)
  have hrA : ((1 - s₀) / 2).re < A :=
    lt_of_le_of_lt ((le_max_right _ _).trans (le_max_right _ _)) (lt_add_one _)
  have hlc : Continuous (fun s : ℂ => (s / 2).re) := by fun_prop
  have hrc : Continuous (fun s : ℂ => ((1 - s) / 2).re) := by fun_prop
  have hl : ∀ᶠ s in 𝓝 s₀, (s / 2).re < A :=
    hlc.continuousAt.eventually_lt continuousAt_const hlA
  have hr : ∀ᶠ s in 𝓝 s₀, ((1 - s) / 2).re < A :=
    hrc.continuousAt.eventually_lt continuousAt_const hrA
  refine ⟨_, splitIntegrandDeriv_majorant_integrable hA, ?_⟩
  filter_upwards [hl, hr] with s hleft hright
  intro x hx
  exact splitIntegrandDeriv_uniform_bound s hx hleft.le hright.le

/-- Continuity in the integration variable supplies derivative measurability. -/
lemma splitIntegrandDeriv_continuousOn (s : ℂ) :
    ContinuousOn (splitIntegrandDeriv s) (Set.Ici 1) := by
  intro x hx
  have hp : 0 < x := lt_of_lt_of_le zero_lt_one hx
  have hpsi : ContinuousAt L016.psi x := by
    unfold L016.psi
    simpa only [pow_zero, one_mul] using (L016.hasDerivAt_derivative_series 0 hp).continuousAt
  have hlog : ContinuousAt (fun y : ℝ => (Real.log y : ℂ)) x :=
    Complex.continuous_ofReal.continuousAt.comp (Real.continuousAt_log hp.ne')
  exact ((((Complex.continuous_ofReal.continuousAt.comp hpsi).mul
    (((continuousAt_const.mul hlog).cexp).sub
      ((continuousAt_const.mul hlog).cexp))).mul hlog).div_const 2).div
        Complex.continuous_ofReal.continuousAt
        (by exact_mod_cast hp.ne') |>.continuousWithinAt

/-- Dominated differentiation of the literal split Mellin integral. -/
theorem hasDerivAt_splitMellin (s₀ : ℂ) :
    HasDerivAt splitMellin
      (∫ x in Set.Ici (1 : ℝ), splitIntegrandDeriv s₀ x) s₀ := by
  obtain ⟨bound, hint, hloc⟩ := splitIntegrandDeriv_locally_dominated s₀
  let U : Set ℂ := {s | ∀ x : ℝ, 1 ≤ x → ‖splitIntegrandDeriv s x‖ ≤ bound x}
  have hU : U ∈ 𝓝 s₀ := hloc
  have hbound : ∀ᵐ x ∂(volume.restrict (Set.Ici (1 : ℝ))),
      ∀ s ∈ U, ‖splitIntegrandDeriv s x‖ ≤ bound x := by
    filter_upwards [ae_restrict_mem measurableSet_Ici] with x hx
    intro s hs
    exact hs x hx
  have hdiff : ∀ᵐ x ∂(volume.restrict (Set.Ici (1 : ℝ))),
      ∀ s ∈ U, HasDerivAt (fun z => splitIntegrand z x) (splitIntegrandDeriv s x) s :=
    Filter.Eventually.of_forall (fun x s _ => hasDerivAt_splitIntegrand s x)
  exact (hasDerivAt_integral_of_dominated_loc_of_deriv_le hU
    (Filter.Eventually.of_forall (fun s => (splitIntegrand_integrable s).aestronglyMeasurable))
    (splitIntegrand_integrable s₀)
    ((splitIntegrandDeriv_continuousOn s₀).aestronglyMeasurable measurableSet_Ici)
    hbound hint hdiff).2

/-- The split remainder is entire. -/
theorem splitMellin_differentiable : Differentiable ℂ splitMellin :=
  fun s => (hasDerivAt_splitMellin s).differentiableAt

/-- Euler's gamma integral for one literal theta-series summand, with real-log powers. -/
lemma thetaTerm_mellin_integral {s : ℂ} (hs : 1 < s.re) (n : ℕ) :
    (∫ x in Set.Ioi (0 : ℝ),
      (Real.exp (-Real.pi * ((n + 1 : ℕ) : ℝ) ^ 2 * x) : ℂ) *
        Complex.exp ((s / 2 - 1) * (Real.log x : ℂ))) =
      (1 / (Real.pi * ((n + 1 : ℕ) : ℝ) ^ 2) : ℂ) ^ (s / 2) *
        Complex.Gamma (s / 2) := by
  have ha : 0 < (s / 2).re := by
    simp only [Complex.div_ofNat_re]
    linarith
  have hr : 0 < Real.pi * ((n + 1 : ℕ) : ℝ) ^ 2 :=
    mul_pos Real.pi_pos (sq_pos_of_pos (by positivity))
  have hgamma := Complex.integral_cpow_mul_exp_neg_mul_Ioi ha hr
  push_cast at hgamma ⊢
  rw [← hgamma]
  apply setIntegral_congr_fun measurableSet_Ioi
  intro x hx
  have hx' : (x : ℂ) ≠ 0 := by exact_mod_cast (ne_of_gt hx)
  dsimp only
  rw [Complex.cpow_def_of_ne_zero hx', ← Complex.ofReal_log (le_of_lt hx)]
  rw [mul_comm (Real.log x : ℂ) (s / 2 - 1)]
  rw [mul_comm]
  congr 1
  congr 1
  ring

/-- The absolute integral of one theta term is a real gamma integral. -/
lemma thetaTerm_norm_integral {s : ℂ} (hs : 1 < s.re) (n : ℕ) :
    (∫ x in Set.Ioi (0 : ℝ),
      ‖(Real.exp (-Real.pi * ((n + 1 : ℕ) : ℝ) ^ 2 * x) : ℂ) *
        Complex.exp ((s / 2 - 1) * (Real.log x : ℂ))‖) =
      (1 / (Real.pi * ((n + 1 : ℕ) : ℝ) ^ 2)) ^ (s.re / 2) *
        Real.Gamma (s.re / 2) := by
  have hr : 0 < Real.pi * ((n + 1 : ℕ) : ℝ) ^ 2 := by positivity
  rw [← Real.integral_rpow_mul_exp_neg_mul_Ioi (by linarith : 0 < s.re / 2) hr]
  apply setIntegral_congr_fun measurableSet_Ioi
  intro x hx
  dsimp only
  rw [norm_mul, Complex.norm_real, Real.norm_eq_abs, Real.abs_exp, norm_log_power _ hx]
  simp only [Complex.sub_re, Complex.div_ofNat_re, Complex.one_re]
  rw [mul_comm]
  congr 2
  ring

/-- The absolute integrals form a convergent p-series for Re(s)>1. -/
lemma thetaTerm_summable_integral_norm {s : ℂ} (hs : 1 < s.re) :
    Summable (fun n : ℕ => ∫ x in Set.Ioi (0 : ℝ),
      ‖(Real.exp (-Real.pi * ((n + 1 : ℕ) : ℝ) ^ 2 * x) : ℂ) *
        Complex.exp ((s / 2 - 1) * (Real.log x : ℂ))‖) := by
  have hp : Summable (fun n : ℕ => ((n + 1 : ℕ) : ℝ) ^ (-s.re)) :=
    (summable_nat_add_iff 1).mpr (Real.summable_nat_rpow.mpr (by linarith))
  have h := (hp.mul_left ((1 / Real.pi) ^ (s.re / 2))).mul_right
    (Real.Gamma (s.re / 2))
  apply h.congr
  intro n
  symm
  rw [thetaTerm_norm_integral hs]
  have hn : 0 ≤ ((n + 1 : ℕ) : ℝ) := by positivity
  rw [one_div, Real.inv_rpow (by positivity), Real.mul_rpow Real.pi_pos.le (sq_nonneg _),
    mul_inv_rev, one_div, Real.inv_rpow Real.pi_pos.le,
    ← Real.rpow_natCast_mul hn]
  norm_num only [Nat.cast_ofNat]
  rw [show (2 : ℝ) * (s.re / 2) = s.re by ring, Real.rpow_neg hn]
  ring

end Rh.L017

#print axioms Rh.L017.splitIntegrand_reflection
#print axioms Rh.L017.splitMellin_reflection

#print axioms Rh.L017.norm_log_power
#print axioms Rh.L017.splitIntegrand_norm_le

#print axioms Rh.L017.splitIntegrand_uniform_bound

#print axioms Rh.L017.splitIntegrand_continuousOn
#print axioms Rh.L017.splitIntegrand_integrable

#print axioms Rh.L017.hasDerivAt_splitIntegrand

#print axioms Rh.L017.splitIntegrandDeriv_uniform_bound
#print axioms Rh.L017.splitIntegrandDeriv_majorant_integrable
#print axioms Rh.L017.splitIntegrandDeriv_locally_dominated

#print axioms Rh.L017.splitIntegrandDeriv_continuousOn
#print axioms Rh.L017.hasDerivAt_splitMellin
#print axioms Rh.L017.splitMellin_differentiable

#print axioms Rh.L017.thetaTerm_mellin_integral

#print axioms Rh.L017.thetaTerm_norm_integral
#print axioms Rh.L017.thetaTerm_summable_integral_norm
