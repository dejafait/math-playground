# Lemma 17: split Mellin integral with entire remainder

**Hypotheses.** ψ is as in Lemma 16. For s∈C put

I(s)=∫_1^∞ψ(x)(x^{s/2}+x^{(1-s)/2})dx/x,

where all powers use the real logarithm of x.

**Conclusion.** I is entire, I(s)=I(1-s), and for Re(s)>1,

π^{-s/2}Γ(s/2)ζ(s)=1/(s-1)-1/s+I(s).

**Proof.** For σ=Re(s)>1, the integral of the absolute values of the summands in ∫_0^∞Σ_{n≥1}e^{-πn²x}x^{s/2-1}dx is

Σ_{n≥1}∫_0^∞e^{-πn²x}x^{σ/2-1}dx=π^{-σ/2}Γ(σ/2)Σ_{n≥1}n^{-σ}<∞.

Thus Fubini's theorem permits termwise integration. The substitution u=πn²x and Euler's gamma integral give the left side in the conclusion. Split the x-integral at 1. Lemma 16 gives ψ(x)=(x^{-1/2}-1)/2+x^{-1/2}ψ(1/x) for 0<x<1. The elementary part integrates, for σ>1, to 1/(s-1)-1/s. Substituting y=1/x in the remaining part yields ∫_1^∞ψ(y)y^{(1-s)/2}dy/y, completing the identity.

On a compact set of s, both Re(s)/2 and (1-Re(s))/2 are bounded above by some finite A. Lemma 16 bounds the integrand in absolute value by 2C_0e^{-πx}x^{A-1}. Its k-th complex s derivative has the same bound times (log x/2)^k, also integrable for each fixed k. Dominated differentiation proves that I is entire. Reflection just interchanges its two summands, proving I(s)=I(1-s). ∎

**Mathlib.** The source uses Mathlib's complex exponential and Bochner set integral to define the literal integral with powers expressed through the real logarithm. Reflection is proved by pointwise equality of its two integrands, using `sub_sub_cancel` and commutativity of addition. Relevant documentation:

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Complex/Log.html

https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/Bochner/Basic.html

L016 supplies the literal ψ series and exponential tails. `norm_log_power` identifies the norm of each real-logarithm power, and `splitIntegrand_norm_le` applies the order-zero tail bound. `splitIntegrand_uniform_bound` proves the stated majorant 2C₀ exp(-πx)x^(A-1) whenever A bounds both real exponents and x≥1. These are internal helpers for the existing informal proof. Mathlib's real-power identities and exponent monotonicity are documented at:

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Pow/Real.html

`splitIntegrand_continuousOn` obtains continuity on [1,∞) from L016's order-zero differentiable series and continuity of the logarithm. `splitIntegrand_integrable` proves absolute convergence for every s: choose A=max(1,max(Re(s/2),Re((1-s)/2))), restrict `integrableOn_rpow_mul_exp_neg_mul_rpow` (p=1, b=π) to [1,∞), and apply the checked majorant. This Mathlib theorem is in the root namespace, not `Real`:

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Gaussian/GaussianIntegral.html#integrableOn_rpow_mul_exp_neg_mul_rpow

`hasDerivAt_splitIntegrand` now proves the complex parameter derivative, represented by `splitIntegrandDeriv`, using the exponential chain rule and constant multiplication/division rules. Its formula has the difference of the two exponentials and the additional log(x)/2 factor. Relevant documentation:

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/ExpDeriv.html

`splitIntegrandDeriv_uniform_bound` bounds the derivative by C₀ exp(-πx)x^A whenever x≥1 and A bounds both real exponents. The proof uses the triangle inequality and `Real.log_le_self` to absorb log(x)/2. `splitIntegrandDeriv_majorant_integrable` proves integrability of this bound for A≥0 using the same Gaussian-integral theorem above. `splitIntegrandDeriv_locally_dominated` chooses A=max(0,max(Re(s₀/2),Re((1-s₀)/2)))+1 and uses continuity of both real exponents to obtain one integrable bound throughout a neighborhood of every s₀. The logarithm estimate is documented at:

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Log/Basic.html#Real.log_le_self

`splitIntegrandDeriv_continuousOn` proves continuity on [1,∞), supplying derivative measurability. `hasDerivAt_splitMellin` applies the parametric integral theorem to the restricted Lebesgue measure, using the checked local bound and integrability. `splitMellin_differentiable` therefore proves entireness of the literal integral. The complete gamma–zeta Mellin identity remains open. The differentiation theorem is documented at:

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/ParametricIntegral.html#hasDerivAt_integral_of_dominated_loc_of_deriv_le

`thetaTerm_mellin_integral` evaluates each positive-index theta term against x^(s/2-1), expressed with the real logarithm, for Re(s)>1. It uses `Complex.integral_cpow_mul_exp_neg_mul_Ioi` and explicitly identifies the positive-real complex power with the logarithmic exponential. This is an individual integral identity; the sum–integral interchange remains open. Relevant documentation:

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Gamma/Basic.html#Complex.integral_cpow_mul_exp_neg_mul_Ioi

`thetaTerm_norm_integral` evaluates the integral of the literal summand norm using `norm_log_power` and the real gamma integral. `thetaTerm_summable_integral_norm` factors the resulting sequence into a constant times (n+1)^(-Re(s)) and applies the real p-series theorem. These establish summability of the absolute integrals for Re(s)>1. Individual summand integrability and the sum–integral interchange are not yet separately assembled in this source. Relevant documentation:

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Gamma/Basic.html#Real.integral_rpow_mul_exp_neg_mul_Ioi

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/PSeries.html#Real.summable_nat_rpow

**Lean proof status.** Partial, not a validated proof of the full statement. On 2026-09-20, Lean 4.33.1 with mathlib `v4.33.1` checked the literal definitions and `splitMellin_reflection`, establishing I(s)=I(1-s). The source additionally checks the real-logarithm power norm and the pointwise and common-exponent majorants. It now also checks continuity of the integrand on [1,∞) and its integrability for every complex parameter. The complex parameter derivative, its common-exponent bound, integrability of that bound for A≥0, and local domination near every parameter are now also checked. Derivative continuity, differentiation under the integral, and `Differentiable ℂ splitMellin` are also checked. The individual theta-term gamma integral is also checked. The real absolute-integral evaluation and summability of those integrals are also checked. All seventeen audited theorems use only `propext`, `Classical.choice`, and `Quot.sound`. The gamma–zeta identity remains unproved. Convergence now has a separate integrability proof, independent of reflection of totalized Bochner integrals. L017 remains backlog; no hypotheses, conclusion, or informal proof were changed.

**Lean proof command.**

This command succeeded for the partial source and its axiom audits only; it does not validate the full lemma:

```
(cd scripts/lean && lake build Rh.L017)
```

**Lean proof code.**

```lean
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
```
