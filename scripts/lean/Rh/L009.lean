/-
Lemma 9: complete classification outside the open strip.

Outside 0 < Re(s) < 1, and away from the pole s = 1, the zeros of ζ are
exactly the negative even integers, each simple.
-/
import Mathlib.NumberTheory.LSeries.Nonvanishing
import Rh.L003

open Complex Filter
open scoped Topology Real

noncomputable section

lemma riemannZeta_neg_two_nat {n : ℕ} (hn : 0 < n) :
    riemannZeta (-2 * (n : ℂ)) = 0 := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_succ_of_ne_zero hn.ne'
  simpa [Nat.cast_succ] using riemannZeta_neg_two_mul_nat_add_one k

lemma riemannZeta_one_sub_of_one_le_re {s : ℂ} (hs : 1 ≤ s.re) (hs1 : s ≠ 1) :
    riemannZeta (1 - s) = zetaFEPrefactor s * riemannZeta s := by
  refine riemannZeta_one_sub (fun n hn => ?_) hs1
  have hre : s.re ≤ 0 := by simp [hn]
  linarith

lemma analyticAt_zetaFEPrefactor_of_re_pos {s : ℂ} (hs : 0 < s.re) :
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
    exact hd.analyticAt (hU.mem_nhds hs)
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

lemma zetaFEPrefactor_eq_zero_iff_cos {s : ℂ} (hs : 0 < s.re) :
    zetaFEPrefactor s = 0 ↔ cos (π * s / 2) = 0 := by
  unfold zetaFEPrefactor
  have hpow : (2 * π : ℂ) ^ (-s) ≠ 0 := by
    intro h
    exact (mul_ne_zero two_ne_zero (ofReal_ne_zero.mpr Real.pi_ne_zero))
      ((cpow_eq_zero_iff _ _).1 h).1
  have hG : Gamma s ≠ 0 := Gamma_ne_zero_of_re_pos hs
  simp [mul_eq_zero, hpow, hG]

lemma cos_pi_div_two_eq_zero_iff {s : ℂ} :
    cos (π * s / 2) = 0 ↔ ∃ k : ℤ, s = 2 * k + 1 := by
  rw [cos_eq_zero_iff]
  constructor
  · rintro ⟨k, hk⟩
    refine ⟨k, ?_⟩
    have hπ : (π : ℂ) ≠ 0 := ofReal_ne_zero.mpr Real.pi_ne_zero
    have hmul : π * s = (2 * k + 1) * π := by
      have := congr_arg (fun z : ℂ => z * 2) hk
      simpa [mul_div_cancel₀ _ (two_ne_zero' ℂ)] using this
    have : π * s = π * (2 * k + 1) := by simpa [mul_comm] using hmul
    exact mul_left_cancel₀ hπ this
  · rintro ⟨k, rfl⟩
    refine ⟨k, ?_⟩
    field_simp [two_ne_zero' ℂ]

lemma riemannZeta_zero_ne_zero : riemannZeta 0 ≠ 0 := by
  rw [riemannZeta_zero]
  norm_num

lemma exists_neg_even_of_zeta_zero_left {s : ℂ} (hle : s.re ≤ 0) (hz : riemannZeta s = 0) :
    ∃ n : ℕ, 0 < n ∧ s = -2 * (n : ℂ) := by
  have hs0 : s ≠ 0 := fun h => by
    subst h
    exact riemannZeta_zero_ne_zero hz
  have hu : 1 ≤ (1 - s).re := by
    simp [sub_re]
    linarith
  have hu1 : 1 - s ≠ 1 := by
    simpa using hs0
  have hFE := riemannZeta_one_sub_of_one_le_re hu hu1
  have hs' : 1 - (1 - s) = s := by ring
  have hζu : riemannZeta (1 - s) ≠ 0 := riemannZeta_ne_zero_of_one_le_re hu
  have hpre : zetaFEPrefactor (1 - s) = 0 := by
    have : zetaFEPrefactor (1 - s) * riemannZeta (1 - s) = 0 := by
      rw [← hFE, hs', hz]
    exact (mul_eq_zero.mp this).resolve_right hζu
  have hre_pos : 0 < (1 - s).re := by linarith
  have hcos : cos (π * (1 - s) / 2) = 0 :=
    (zetaFEPrefactor_eq_zero_iff_cos hre_pos).mp hpre
  obtain ⟨k, hk⟩ := cos_pi_div_two_eq_zero_iff.mp hcos
  have hre : (1 - s).re = 2 * (k : ℝ) + 1 := by
    simp [hk, add_re, mul_re]
  have hkpos : (0 : ℤ) < k := by
    have : (1 : ℝ) ≤ 2 * (k : ℝ) + 1 := hre ▸ hu
    have hk0 : (0 : ℤ) ≤ k := by exact_mod_cast (show (0 : ℝ) ≤ k from by linarith)
    have hkne : k ≠ 0 := by
      intro hkz
      have : 1 - s = 1 := by simp [hk, hkz]
      exact hu1 this
    exact lt_of_le_of_ne hk0 hkne.symm
  refine ⟨k.toNat, ?_, ?_⟩
  · have hcast : (k.toNat : ℤ) = k := Int.toNat_of_nonneg hkpos.le
    have : (0 : ℤ) < k.toNat := hcast.symm ▸ hkpos
    exact_mod_cast this
  · have hk' : (k : ℂ) = (k.toNat : ℂ) := by
      rw [← Int.cast_natCast, Int.toNat_of_nonneg hkpos.le]
    have hs : s = -2 * (k : ℂ) := by
      calc
        s = 1 - (1 - s) := by ring
        _ = 1 - (2 * k + 1) := by rw [hk]
        _ = -2 * k := by ring
    simpa [hk'] using hs

/-- Zeros of `ζ` outside the open critical strip, away from the pole, are the
negative even integers. -/
theorem L009 {s : ℂ} (hstrip : s ∉ openCriticalStrip) (hone : s ≠ 1) :
    riemannZeta s = 0 ↔ ∃ n : ℕ, 0 < n ∧ s = -2 * (n : ℂ) := by
  constructor
  · intro hz
    by_cases hge : 1 ≤ s.re
    · exact (riemannZeta_ne_zero_of_one_le_re hge hz).elim
    have hle : s.re ≤ 0 := by
      have hnot : ¬ (0 < s.re ∧ s.re < 1) := by
        simpa [openCriticalStrip] using hstrip
      by_cases hpos : 0 < s.re
      · exact (hge (le_of_not_gt (not_and.mp hnot hpos))).elim
      · exact le_of_not_gt hpos
    exact exists_neg_even_of_zeta_zero_left hle hz
  · rintro ⟨n, hn, rfl⟩
    exact riemannZeta_neg_two_nat hn

lemma analyticAt_cos_pi_div_two (s : ℂ) :
    AnalyticAt ℂ (fun z : ℂ => cos (π * z / 2)) s :=
  (differentiable_cos.analyticAt _).comp <|
    ((analyticAt_const).mul analyticAt_id).div_const

lemma deriv_cos_pi_div_two (s : ℂ) :
    deriv (fun z : ℂ => cos (π * z / 2)) s = -sin (π * s / 2) * (π / 2) := by
  have hlin : HasDerivAt (fun z : ℂ => π * z / 2) (π / 2) s := by
    simpa using ((hasDerivAt_id s).const_mul (π : ℂ)).div_const 2
  have hcos : HasDerivAt (fun z : ℂ => cos (π * z / 2)) (-sin (π * s / 2) * (π / 2)) s := by
    simpa [Function.comp_def] using (hasDerivAt_cos (π * s / 2)).comp s hlin
  exact hcos.deriv

lemma cos_int_mul_pi_complex (k : ℤ) : cos ((k : ℂ) * π) = (-1) ^ k := by
  have h : ((k : ℂ) * π) = ↑((k : ℝ) * π) := by
    simp [← ofReal_intCast, ← ofReal_mul]
  rw [h, ← ofReal_cos, Real.cos_int_mul_pi, ofReal_zpow, ofReal_neg, ofReal_one]

lemma meromorphicOrderAt_cos_pi_div_two_odd {k : ℤ} :
    meromorphicOrderAt (fun z : ℂ => cos (π * z / 2)) (2 * k + 1) = 1 := by
  have han := analyticAt_cos_pi_div_two (2 * k + 1 : ℂ)
  have hz0 : cos (π * (2 * k + 1 : ℂ) / 2) = 0 :=
    cos_pi_div_two_eq_zero_iff.mpr ⟨k, rfl⟩
  have hder : deriv (fun z : ℂ => cos (π * z / 2)) (2 * k + 1) ≠ 0 := by
    rw [deriv_cos_pi_div_two]
    have hπ : (π : ℂ) / 2 ≠ 0 :=
      div_ne_zero (ofReal_ne_zero.mpr Real.pi_ne_zero) two_ne_zero
    have hsin : sin (π * (2 * k + 1 : ℂ) / 2) ≠ 0 := by
      have harg : π * (2 * k + 1 : ℂ) / 2 = (k : ℂ) * π + π / 2 := by
        field_simp [two_ne_zero' ℂ]
      rw [harg, sin_add, sin_pi_div_two, cos_pi_div_two]
      simp [cos_int_mul_pi_complex]
      exact zpow_ne_zero k (by norm_num : (-1 : ℂ) ≠ 0)
    exact mul_ne_zero (neg_ne_zero.mpr hsin) hπ
  have hord := han.analyticOrderAt_eq_one_of_zero_deriv_ne_zero hz0 hder
  rw [han.meromorphicOrderAt_eq, hord]
  simp

lemma analyticAt_riemannZeta_of_ne_one {s : ℂ} (hs : s ≠ 1) :
    AnalyticAt ℂ riemannZeta s :=
  analyticOn_riemannZeta s (by simp [hs])

/-- Each trivial zero is simple. -/
theorem L009_simple {n : ℕ} (hn : 0 < n) :
    meromorphicOrderAt riemannZeta (-2 * (n : ℂ)) = 1 := by
  set s := -2 * (n : ℂ)
  set u := (1 : ℂ) + 2 * (n : ℂ)
  have hs : s = 1 - u := by
    simp [s, u]
  have hu_re : 1 < u.re := by
    simp [u, add_re, mul_re]
    have : (0 : ℝ) < n := Nat.cast_pos.mpr hn
    linarith
  have hu1 : u ≠ 1 := fun h => by
    have : u.re = 1 := by simp [h]
    linarith
  have hζu : riemannZeta u ≠ 0 :=
    riemannZeta_ne_zero_of_one_le_re hu_re.le
  have hg : AnalyticAt ℂ (fun z : ℂ => 1 - z) u := by fun_prop
  have hg' : deriv (fun z : ℂ => 1 - z) u ≠ 0 := by simp
  have hcomp :
      meromorphicOrderAt (riemannZeta ∘ fun z : ℂ => 1 - z) u =
        meromorphicOrderAt riemannZeta (1 - u) :=
    meromorphicOrderAt_comp_of_deriv_ne_zero hg hg'
  have heq :
      (riemannZeta ∘ fun z : ℂ => 1 - z) =ᶠ[𝓝[≠] u]
        (zetaFEPrefactor * riemannZeta) := by
    have : ∀ᶠ z in 𝓝 u, 1 < z.re :=
      (isOpen_lt continuous_const continuous_re).mem_nhds hu_re
    filter_upwards [this.filter_mono nhdsWithin_le_nhds] with z hz
    have hz1 : z ≠ 1 := fun h => by
      have : z.re = 1 := by simp [h]
      linarith
    simpa [Function.comp_apply, Pi.mul_apply] using
      riemannZeta_one_sub_of_one_le_re hz.le hz1
  have hanζ : AnalyticAt ℂ riemannZeta u := analyticAt_riemannZeta_of_ne_one hu1
  have hmul :
      meromorphicOrderAt (zetaFEPrefactor * riemannZeta) u =
        meromorphicOrderAt zetaFEPrefactor u := by
    have hcomm : zetaFEPrefactor * riemannZeta = riemannZeta * zetaFEPrefactor := mul_comm _ _
    rw [hcomm]
    exact meromorphicOrderAt_mul_of_ne_zero hanζ hζu
  have hpre_fac :
      meromorphicOrderAt zetaFEPrefactor u =
        meromorphicOrderAt (fun z : ℂ => cos (π * z / 2)) u := by
    have hpow : AnalyticAt ℂ (fun z : ℂ => (2 * π : ℂ) ^ (-z)) u := by
      have hbase : (2 * π : ℂ) ∈ slitPlane :=
        Or.inl (by
          have : 0 < (2 * π : ℝ) := mul_pos two_pos Real.pi_pos
          simpa [mul_re])
      exact AnalyticAt.cpow analyticAt_const (AnalyticAt.neg analyticAt_id) hbase
    have hG : AnalyticAt ℂ Gamma u := by
      have hU : IsOpen {z : ℂ | 0 < z.re} := isOpen_lt continuous_const continuous_re
      have hd : DifferentiableOn ℂ Gamma {z | 0 < z.re} := by
        intro z hz
        have hpos : 0 < z.re := hz
        exact (differentiableAt_Gamma z fun m hm => by
          have : z.re ≤ 0 := by simp [hm]
          linarith).differentiableWithinAt
      exact hd.analyticAt (hU.mem_nhds (lt_trans zero_lt_one hu_re))
    have h2n : (2 : ℂ) ≠ 0 := two_ne_zero
    have hpow0 : (2 * π : ℂ) ^ (-u) ≠ 0 := by
      intro h
      exact (mul_ne_zero two_ne_zero (ofReal_ne_zero.mpr Real.pi_ne_zero))
        ((cpow_eq_zero_iff _ _).1 h).1
    have hG0 : Gamma u ≠ 0 := Gamma_ne_zero_of_re_pos (lt_trans zero_lt_one hu_re)
    have hA : AnalyticAt ℂ (fun z => (2 : ℂ) * ((2 * π : ℂ) ^ (-z)) * Gamma z) u :=
      (analyticAt_const.mul hpow).mul hG
    have hA0 : (2 : ℂ) * ((2 * π : ℂ) ^ (-u)) * Gamma u ≠ 0 :=
      mul_ne_zero (mul_ne_zero h2n hpow0) hG0
    have hfun :
        (fun z => (2 : ℂ) * ((2 * π : ℂ) ^ (-z)) * Gamma z * cos (π * z / 2)) =
          (fun z => ((2 : ℂ) * ((2 * π : ℂ) ^ (-z)) * Gamma z) * cos (π * z / 2)) := by
      funext z
      ring
    rw [show zetaFEPrefactor = fun z =>
        (2 : ℂ) * ((2 * π : ℂ) ^ (-z)) * Gamma z * cos (π * z / 2) from rfl, hfun]
    exact meromorphicOrderAt_mul_of_ne_zero (f := fun z => cos (π * z / 2)) hA hA0
  have hcosord : meromorphicOrderAt (fun z : ℂ => cos (π * z / 2)) u = 1 := by
    have : u = (2 * (n : ℤ) + 1 : ℂ) := by
      simp [u]
      ring
    rw [this]
    simpa using meromorphicOrderAt_cos_pi_div_two_odd (k := n)
  rw [hs, ← hcomp, meromorphicOrderAt_congr heq, hmul, hpre_fac, hcosord]

end

#print axioms L009
#print axioms L009_simple
