/-
Lemma 3: reflection orbits in the open critical strip.

If ζ(ρ) = 0 and 0 < Re(ρ) < 1, then ρ, conj ρ, 1-ρ and 1-conj ρ are zeros of
equal meromorphic order. Some of these points may coincide.
-/
import Mathlib.Analysis.Analytic.Order
import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.Analysis.Complex.CauchyIntegral
import Mathlib.Analysis.Meromorphic.Order
import Mathlib.Analysis.SpecialFunctions.Complex.Analytic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.SpecialFunctions.Gamma.Beta
import Mathlib.Analysis.SpecialFunctions.Gamma.Deriv
import Mathlib.NumberTheory.Harmonic.ZetaAsymp
import Mathlib.NumberTheory.LSeries.RiemannZeta

open Complex Filter
open scoped ComplexConjugate Topology Real

noncomputable section

/-- The open critical strip `{s | 0 < re s < 1}`. -/
def openCriticalStrip : Set ℂ := {s | 0 < s.re ∧ s.re < 1}

lemma mem_openCriticalStrip {s : ℂ} :
    s ∈ openCriticalStrip ↔ 0 < s.re ∧ s.re < 1 :=
  Iff.rfl

lemma isOpen_openCriticalStrip : IsOpen openCriticalStrip :=
  (isOpen_lt continuous_const continuous_re).inter (isOpen_lt continuous_re continuous_const)

lemma openCriticalStrip_conj {s : ℂ} (hs : s ∈ openCriticalStrip) :
    conj s ∈ openCriticalStrip := by
  simpa [openCriticalStrip, conj_re] using hs

lemma openCriticalStrip_one_sub {s : ℂ} (hs : s ∈ openCriticalStrip) :
    1 - s ∈ openCriticalStrip := by
  rcases hs with ⟨h₀, h₁⟩
  refine ⟨?_, ?_⟩ <;> simp [sub_re] <;> linarith

lemma not_neg_nat_of_mem_openCriticalStrip {s : ℂ} (hs : s ∈ openCriticalStrip) (n : ℕ) :
    s ≠ -n := by
  intro h
  have hre : s.re ≤ 0 := by simp [h]
  exact (not_le.mpr hs.1) hre

lemma ne_one_of_mem_openCriticalStrip {s : ℂ} (hs : s ∈ openCriticalStrip) : s ≠ 1 := by
  intro h
  have : (1 : ℝ) < 1 := by simpa [h] using hs.2
  exact this.false

/-- Mathlib's functional-equation prefactor `2 * (2π)^(-s) * Γ(s) * cos(π s / 2)`. -/
def zetaFEPrefactor (s : ℂ) : ℂ :=
  2 * (2 * π : ℂ) ^ (-s) * Gamma s * cos (π * s / 2)

lemma zetaFEPrefactor_ne_zero {s : ℂ} (hs : s ∈ openCriticalStrip) :
    zetaFEPrefactor s ≠ 0 := by
  refine mul_ne_zero (mul_ne_zero (mul_ne_zero two_ne_zero ?_) ?_) ?_
  · intro h
    exact (mul_ne_zero two_ne_zero (ofReal_ne_zero.mpr Real.pi_ne_zero))
      ((cpow_eq_zero_iff _ _).1 h).1
  · exact Gamma_ne_zero_of_re_pos hs.1
  · intro hc
    obtain ⟨k, hk⟩ := (cos_eq_zero_iff).1 hc
    have hπ : (π : ℂ) ≠ 0 := ofReal_ne_zero.mpr Real.pi_ne_zero
    have hs_odd : s = (2 * k + 1 : ℂ) := by
      have hmul : π * s = (2 * k + 1) * π := by
        have := congr_arg (fun z : ℂ => z * 2) hk
        simpa [mul_div_cancel₀ _ (two_ne_zero' ℂ)] using this
      have : π * s = π * (2 * k + 1) := by
        simpa [mul_comm] using hmul
      exact mul_left_cancel₀ hπ this
    have hre : s.re = (2 * (k : ℝ) + 1) := by simp [hs_odd]
    have : (0 : ℤ) < 2 * k + 1 ∧ 2 * k + 1 < 1 := by
      constructor
      · exact_mod_cast (hre ▸ hs.1)
      · exact_mod_cast (hre ▸ hs.2)
    omega

lemma riemannZeta_one_sub_eq_prefactor_mul {s : ℂ} (hs : s ∈ openCriticalStrip) :
    riemannZeta (1 - s) = zetaFEPrefactor s * riemannZeta s :=
  riemannZeta_one_sub (fun n => not_neg_nat_of_mem_openCriticalStrip hs n)
    (ne_one_of_mem_openCriticalStrip hs)

lemma analyticAt_zetaFEPrefactor {s : ℂ} (hs : s ∈ openCriticalStrip) :
    AnalyticAt ℂ zetaFEPrefactor s := by
  have hU : IsOpen {z : ℂ | 0 < z.re} := isOpen_lt continuous_const continuous_re
  have hG : AnalyticAt ℂ Gamma s := by
    have hd : DifferentiableOn ℂ Gamma {z | 0 < z.re} := by
      intro z hz
      have hpos : 0 < z.re := hz
      have hz' : DifferentiableAt ℂ Gamma z :=
        differentiableAt_Gamma z fun n hn => by
          have : z.re ≤ 0 := by simp [hn]
          linarith
      exact hz'.differentiableWithinAt
    exact hd.analyticAt (hU.mem_nhds hs.1)
  have hbase : (2 * π : ℂ) ∈ slitPlane :=
    Or.inl (by
      have : 0 < (2 * π : ℝ) := mul_pos two_pos Real.pi_pos
      simpa [mul_re])
  have hid : AnalyticAt ℂ (id : ℂ → ℂ) s := analyticAt_id
  have hneg : AnalyticAt ℂ (fun z : ℂ => -z) s := AnalyticAt.neg hid
  have hpow : AnalyticAt ℂ (fun z : ℂ => (2 * π : ℂ) ^ (-z)) s :=
    AnalyticAt.cpow analyticAt_const hneg hbase
  have hconstπ : AnalyticAt ℂ (fun _ : ℂ => (π : ℂ)) s := analyticAt_const
  have hlin : AnalyticAt ℂ (fun z : ℂ => π * z / 2) s :=
    (AnalyticAt.mul hconstπ hid).div_const
  have hcos : AnalyticAt ℂ (fun z : ℂ => cos (π * z / 2)) s :=
    (differentiable_cos.analyticAt _).comp hlin
  exact AnalyticAt.mul (AnalyticAt.mul (AnalyticAt.mul analyticAt_const hpow) hG) hcos

lemma analyticAt_one_sub (s : ℂ) : AnalyticAt ℂ (fun z : ℂ => 1 - z) s := by
  fun_prop

lemma deriv_one_sub (s : ℂ) : deriv (fun z : ℂ => 1 - z) s = -1 := by
  simp

lemma meromorphicOrderAt_riemannZeta_one_sub {ρ : ℂ} (hs : ρ ∈ openCriticalStrip) :
    meromorphicOrderAt riemannZeta (1 - ρ) = meromorphicOrderAt riemannZeta ρ := by
  have hg : AnalyticAt ℂ (fun z : ℂ => 1 - z) ρ := analyticAt_one_sub ρ
  have hg' : deriv (fun z : ℂ => 1 - z) ρ ≠ 0 := by simp [deriv_one_sub]
  have hcomp :
      meromorphicOrderAt (riemannZeta ∘ fun z : ℂ => 1 - z) ρ =
        meromorphicOrderAt riemannZeta (1 - ρ) :=
    meromorphicOrderAt_comp_of_deriv_ne_zero hg hg'
  have heq :
      (riemannZeta ∘ fun z : ℂ => 1 - z) =ᶠ[𝓝[≠] ρ] (zetaFEPrefactor * riemannZeta) := by
    have : ∀ᶠ z in 𝓝 ρ, z ∈ openCriticalStrip := isOpen_openCriticalStrip.mem_nhds hs
    filter_upwards [this.filter_mono nhdsWithin_le_nhds] with z hz
    simpa [Function.comp_apply, Pi.mul_apply] using
      riemannZeta_one_sub_eq_prefactor_mul hz
  have hmul :
      meromorphicOrderAt (zetaFEPrefactor * riemannZeta) ρ =
        meromorphicOrderAt riemannZeta ρ :=
    meromorphicOrderAt_mul_of_ne_zero (analyticAt_zetaFEPrefactor hs)
      (zetaFEPrefactor_ne_zero hs)
  rw [← hcomp, meromorphicOrderAt_congr heq, hmul]

/-- `conj ∘ f ∘ conj` is complex-differentiable whenever `f` is. -/
lemma hasDerivAt_conj_comp_conj {f : ℂ → ℂ} {f' z : ℂ}
    (hf : HasDerivAt f f' (conj z)) :
    HasDerivAt (fun w : ℂ => conj (f (conj w))) (conj f') z := by
  rw [hasDerivAt_iff_tendsto] at hf ⊢
  have hcomp := hf.comp (continuous_star.tendsto z)
  convert hcomp using 1
  ext w
  simp only [Function.comp_apply, smul_eq_mul]
  have h1 : ‖w - z‖ = ‖conj w - conj z‖ := by
    rw [← map_sub, norm_conj]
  have h2 :
      ‖conj (f (conj w)) - conj (f (conj z)) - (w - z) * conj f'‖ =
        ‖f (conj w) - f (conj z) - (conj w - conj z) * f'‖ := by
    have hrem :
        conj (f (conj w)) - conj (f (conj z)) - (w - z) * conj f' =
          conj (f (conj w) - f (conj z) - (conj w - conj z) * f') := by
      rw [map_sub, map_sub, map_mul, map_sub, conj_conj, conj_conj]
    rw [hrem, norm_conj]
  rw [h1, h2]
  rfl

lemma differentiableAt_conj_comp_conj {f : ℂ → ℂ} {z : ℂ}
    (hf : DifferentiableAt ℂ f (conj z)) :
    DifferentiableAt ℂ (fun w : ℂ => conj (f (conj w))) z :=
  (hasDerivAt_conj_comp_conj hf.hasDerivAt).differentiableAt

lemma analyticAt_conj_comp_conj {f : ℂ → ℂ} {z : ℂ}
    (hf : AnalyticAt ℂ f (conj z)) :
    AnalyticAt ℂ (fun w : ℂ => conj (f (conj w))) z := by
  rw [Complex.analyticAt_iff_eventually_differentiableAt] at hf ⊢
  have hmap : Tendsto conj (𝓝 z) (𝓝 (conj z)) := continuous_star.tendsto z
  filter_upwards [hmap.eventually hf] with w hw
  exact differentiableAt_conj_comp_conj hw

lemma map_conj_nhdsNE (x : ℂ) :
    Filter.map conj (𝓝[≠] x) = 𝓝[≠] (conj x) := by
  have hfun : ⇑conjCLE.toHomeomorph = conj := by
    ext y; exact conjCLE_apply y
  rw [← hfun, Homeomorph.map_punctured_nhds_eq, hfun]

lemma meromorphicAt_riemannZeta_of_ne_one {s : ℂ} (hs : s ≠ 1) :
    MeromorphicAt riemannZeta s :=
  (analyticOn_riemannZeta s (by simp [hs])).meromorphicAt

/-- Conjugation preserves the meromorphic order of `ζ`. -/
lemma meromorphicOrderAt_riemannZeta_conj (s : ℂ) :
    meromorphicOrderAt riemannZeta (conj s) = meromorphicOrderAt riemannZeta s := by
  by_cases hs : s = 1
  · subst s; simp
  have hs' : conj s ≠ 1 := by
    intro h
    exact hs (by simpa using congr_arg conj h)
  have hmero : MeromorphicAt riemannZeta s := meromorphicAt_riemannZeta_of_ne_one hs
  have hmero' : MeromorphicAt riemannZeta (conj s) := meromorphicAt_riemannZeta_of_ne_one hs'
  cases hord : meromorphicOrderAt riemannZeta s with
  | top =>
    rw [meromorphicOrderAt_eq_top_iff] at hord ⊢
    have : (∀ᶠ z in 𝓝[≠] (conj s), riemannZeta z = 0) ↔
        ∀ᶠ z in 𝓝[≠] s, riemannZeta (conj z) = 0 := by
      rw [← map_conj_nhdsNE s]
      exact Filter.eventually_map
    simpa [this, riemannZeta_conj, map_eq_zero] using hord
  | coe n =>
    obtain ⟨g, hg_an, hg_ne, hg_eq⟩ := (meromorphicOrderAt_eq_int_iff hmero).1 hord
    refine (meromorphicOrderAt_eq_int_iff hmero').2 ?_
    refine ⟨fun w => conj (g (conj w)), analyticAt_conj_comp_conj (by simpa using hg_an), ?_, ?_⟩
    · simpa using (map_ne_zero_iff (starRingEnd ℂ) star_injective).2 hg_ne
    · have hg_eq' :
          ∀ᶠ w in 𝓝[≠] (conj s), riemannZeta (conj w) = (conj w - s) ^ n • g (conj w) := by
        rw [← map_conj_nhdsNE s, eventually_map]
        simpa [conj_conj] using hg_eq
      filter_upwards [hg_eq'] with w hw
      have hzw : riemannZeta w = conj (riemannZeta (conj w)) := by
        rw [riemannZeta_conj, conj_conj]
      rw [hzw, hw]
      simp_rw [smul_eq_mul, map_mul, map_zpow₀, map_sub, conj_conj]

/-- Lemma 3: zeros in the open strip form conjugation/reflection orbits of equal multiplicity. -/
theorem L003 {ρ : ℂ} (hζ : riemannZeta ρ = 0) (h₀ : 0 < ρ.re) (h₁ : ρ.re < 1) :
    riemannZeta (conj ρ) = 0 ∧
    riemannZeta (1 - ρ) = 0 ∧
    riemannZeta (1 - conj ρ) = 0 ∧
    meromorphicOrderAt riemannZeta (conj ρ) = meromorphicOrderAt riemannZeta ρ ∧
    meromorphicOrderAt riemannZeta (1 - ρ) = meromorphicOrderAt riemannZeta ρ ∧
    meromorphicOrderAt riemannZeta (1 - conj ρ) = meromorphicOrderAt riemannZeta ρ := by
  have hs : ρ ∈ openCriticalStrip := ⟨h₀, h₁⟩
  have hconj0 : riemannZeta (conj ρ) = 0 := by
    rw [riemannZeta_conj, hζ, map_zero]
  have hone0 : riemannZeta (1 - ρ) = 0 := by
    rw [riemannZeta_one_sub_eq_prefactor_mul hs, hζ, mul_zero]
  have honeconj0 : riemannZeta (1 - conj ρ) = 0 := by
    have : 1 - conj ρ = conj (1 - ρ) := by simp
    rw [this, riemannZeta_conj, hone0, map_zero]
  refine ⟨hconj0, hone0, honeconj0, meromorphicOrderAt_riemannZeta_conj ρ,
    meromorphicOrderAt_riemannZeta_one_sub hs, ?_⟩
  rw [show 1 - conj ρ = conj (1 - ρ) by simp, meromorphicOrderAt_riemannZeta_conj]
  exact meromorphicOrderAt_riemannZeta_one_sub hs

end

-- Kernel-axiom audit. Expected: propext, Quot.sound, Classical.choice.
#print axioms L003
