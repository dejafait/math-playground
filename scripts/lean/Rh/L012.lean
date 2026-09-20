/-
Lemma 12: alternating Dirichlet series on the right half-plane.
Full formalization: local uniform convergence of the original alternating
partial sums, holomorphicity, and identification with the holomorphic
filled zeta product throughout Re(s)>0, with value log 2 at s=1.
-/
import Mathlib.Analysis.Complex.RemovableSingularity
import Mathlib.Analysis.SpecialFunctions.Pow.Deriv
import Mathlib.Analysis.Complex.LocallyUniformLimit
import Mathlib.Analysis.PSeries
import Mathlib.Analysis.SpecialFunctions.Pow.Asymptotics
import Mathlib.NumberTheory.LSeries.RiemannZeta
import Mathlib.Tactic

open Complex Filter Finset
open scoped Topology

noncomputable section

/-- A Dirichlet term, expressed exponentially to keep its entire dependence on s explicit. -/
def L012_term (n : ℕ) (s : ℂ) : ℂ :=
  Complex.exp (-s * (Real.log (n + 1 : ℝ) : ℂ))

/-- Pair one positive and one negative term before summing. -/
def L012_pair (n : ℕ) (s : ℂ) : ℂ := L012_term (2 * n) s - L012_term (2 * n + 1) s

def L012_eta (s : ℂ) : ℂ := ∑' n : ℕ, L012_pair n s

lemma L012_log_step (a : ℝ) (ha : 1 ≤ a) :
    0 ≤ Real.log (a + 1) - Real.log a ∧
    Real.log (a + 1) - Real.log a ≤ 1 / a := by
  have ha0 : 0 < a := lt_of_lt_of_le zero_lt_one ha
  constructor
  · exact sub_nonneg.mpr (Real.log_le_log ha0 (by linarith))
  · have h := Real.log_le_sub_one_of_pos (div_pos (by linarith : 0 < a + 1) ha0)
    rw [Real.log_div (by linarith) ha0.ne'] at h
    have he : (a + 1) / a - 1 = 1 / a := by field_simp; ring
    rwa [he] at h

/-- Uniform cancellation bound for two consecutive Dirichlet terms. -/
lemma L012_exp_step_bound (a δ R : ℝ) (s : ℂ)
    (ha : 1 ≤ a) (_hδ : 0 < δ) (hs : δ ≤ s.re) (hR : ‖s‖ ≤ R) :
    ‖Complex.exp (-s * (Real.log a : ℂ)) -
      Complex.exp (-s * (Real.log (a + 1) : ℂ))‖ ≤
      (R * Real.exp R) * a ^ (-δ - 1) := by
  have ha0 : 0 < a := lt_of_lt_of_le zero_lt_one ha
  have hR0 : 0 ≤ R := (norm_nonneg s).trans hR
  let d := Real.log (a + 1) - Real.log a
  have hd0 : 0 ≤ d := (L012_log_step a ha).1
  have hd : d ≤ 1 / a := (L012_log_step a ha).2
  have hd1 : d ≤ 1 := hd.trans (by simpa using (one_div_le_one_div_of_le zero_lt_one ha))
  have heq : Complex.exp (-s * (Real.log (a + 1) : ℂ)) =
      Complex.exp (-s * (Real.log a : ℂ)) * Complex.exp (-s * (d : ℂ)) := by
    rw [← Complex.exp_add]
    congr 1
    dsimp [d]
    push_cast
    ring
  have hexp : ‖Complex.exp (-s * (d : ℂ)) - 1‖ ≤ ‖s‖ * d * Real.exp (‖s‖ * d) := by
    simpa [norm_mul, norm_neg, Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg hd0]
      using Complex.norm_exp_sub_sum_le_norm_mul_exp (-s * (d : ℂ)) 1
  have hsd : ‖s‖ * d ≤ R := (mul_le_mul_of_nonneg_left hd1 (norm_nonneg s)).trans (by simpa using hR)
  have hsmall : ‖Complex.exp (-s * (d : ℂ)) - 1‖ ≤ (R * Real.exp R) / a := by
    calc
      _ ≤ ‖s‖ * d * Real.exp (‖s‖ * d) := hexp
      _ ≤ (R * (1 / a)) * Real.exp R :=
        mul_le_mul (mul_le_mul hR hd hd0 hR0) (Real.exp_le_exp.mpr hsd)
          (Real.exp_nonneg _) (by positivity)
      _ = _ := by ring
  have hnorm : ‖Complex.exp (-s * (Real.log a : ℂ))‖ ≤ a ^ (-δ) := by
    rw [Complex.norm_exp, Real.rpow_def_of_pos ha0]
    apply Real.exp_le_exp.mpr
    simp only [Complex.mul_re, Complex.neg_re, Complex.neg_im,
      Complex.ofReal_re, Complex.ofReal_im, mul_zero, sub_zero]
    nlinarith [Real.log_nonneg ha]
  rw [heq, ← mul_one_sub, norm_mul, norm_sub_rev]
  calc
    _ ≤ a ^ (-δ) * ((R * Real.exp R) / a) :=
      mul_le_mul hnorm hsmall (norm_nonneg _) (Real.rpow_nonneg ha0.le _)
    _ = (R * Real.exp R) * a ^ (-δ - 1) := by
      rw [Real.rpow_sub ha0, Real.rpow_one]
      ring

/-- A summable majorant, uniform on closed bounded subsets of the half-plane. -/
lemma L012_pair_bound (δ R : ℝ) (hδ : 0 < δ) (n : ℕ) (s : ℂ)
    (hs : δ ≤ s.re) (hR : ‖s‖ ≤ R) :
    ‖L012_pair n s‖ ≤ (R * Real.exp R) * (n + 1 : ℝ) ^ (-δ - 1) := by
  have ha : (1 : ℝ) ≤ 2 * n + 1 := by nlinarith [Nat.cast_nonneg (α := ℝ) n]
  have h := L012_exp_step_bound (2 * n + 1) δ R s ha hδ hs hR
  have hbase : (n + 1 : ℝ) ≤ 2 * n + 1 := by nlinarith [Nat.cast_nonneg (α := ℝ) n]
  have hp : (2 * n + 1 : ℝ) ^ (-δ - 1) ≤ (n + 1 : ℝ) ^ (-δ - 1) :=
    Real.rpow_le_rpow_of_nonpos (by positivity) hbase (by linarith)
  have hR0 : 0 ≤ R := (norm_nonneg s).trans hR
  calc
    ‖L012_pair n s‖ ≤ (R * Real.exp R) * (2 * n + 1 : ℝ) ^ (-δ - 1) := by
      simpa [L012_pair, L012_term, Nat.cast_add, Nat.cast_mul, Nat.cast_ofNat,
        add_assoc] using h
    _ ≤ _ := mul_le_mul_of_nonneg_left hp (by positivity)

lemma L012_majorant_summable (δ R : ℝ) (hδ : 0 < δ) :
    Summable (fun n : ℕ => (R * Real.exp R) * (n + 1 : ℝ) ^ (-δ - 1)) := by
  have h : Summable (fun n : ℕ => (n : ℝ) ^ (-δ - 1)) :=
    Real.summable_nat_rpow.mpr (by linarith)
  have ht := (summable_nat_add_iff 1).mpr h
  simpa only [Nat.cast_add, Nat.cast_one] using ht.mul_left (R * Real.exp R)

/-- Absolute convergence of the paired series, including the conditional-convergence strip. -/
theorem L012_paired_summable (s : ℂ) (hs : 0 < s.re) :
    Summable (fun n => L012_pair n s) := by
  apply Summable.of_norm
  exact Summable.of_nonneg_of_le (fun _ => norm_nonneg _)
    (fun n => L012_pair_bound s.re ‖s‖ hs n s le_rfl le_rfl)
    (L012_majorant_summable s.re ‖s‖ hs)

/-- Uniform convergence of paired partial sums on each bounded truncated half-plane. -/
theorem L012_paired_uniform (δ R : ℝ) (hδ : 0 < δ) :
    TendstoUniformlyOn (fun N s => ∑ n ∈ range N, L012_pair n s) L012_eta atTop
      {s : ℂ | δ ≤ s.re ∧ ‖s‖ ≤ R} := by
  exact tendstoUniformlyOn_tsum_nat (L012_majorant_summable δ R hδ)
    (fun n s hs => L012_pair_bound δ R hδ n s hs.1 hs.2)

/-- Paired partial sums converge locally uniformly on the full right half-plane. -/
theorem L012_paired_locally_uniform :
    TendstoLocallyUniformlyOn (fun N s => ∑ n ∈ range N, L012_pair n s) L012_eta atTop
      {s : ℂ | 0 < s.re} := by
  apply tendstoLocallyUniformlyOn_of_forall_exists_nhds
  intro s hs
  have hδ : 0 < s.re / 2 := by change 0 < s.re at hs; linarith
  refine ⟨{z : ℂ | s.re / 2 ≤ z.re ∧ ‖z‖ ≤ ‖s‖ + 1}, ?_,
    L012_paired_uniform _ _ hδ⟩
  apply mem_nhdsWithin_of_mem_nhds
  exact (Complex.continuous_re.continuousAt.eventually
    (eventually_ge_nhds (by linarith : s.re / 2 < s.re))).and
    (continuous_norm.continuousAt.eventually
      (eventually_le_nhds (by linarith : ‖s‖ < ‖s‖ + 1)))

/-- The paired sum defines a holomorphic function on Re(s)>0. -/
theorem L012_holomorphic : DifferentiableOn ℂ L012_eta {s : ℂ | 0 < s.re} := by
  apply L012_paired_locally_uniform.differentiableOn
  · apply Filter.Eventually.of_forall
    intro N
    apply DifferentiableOn.fun_sum
    intro n hn
    unfold L012_pair L012_term
    fun_prop
  · exact isOpen_lt continuous_const Complex.continuous_re

/-- The original, unpaired alternating partial sums. -/
def L012_partial (N : ℕ) (s : ℂ) : ℂ :=
  ∑ n ∈ range N, (-1 : ℂ) ^ n * L012_term n s

lemma L012_partial_even (N : ℕ) (s : ℂ) :
    L012_partial (2 * N) s = ∑ n ∈ range N, L012_pair n s := by
  induction N with
  | zero => simp [L012_partial]
  | succ N ih =>
    rw [Nat.mul_succ, show 2 * N + 2 = (2 * N + 1) + 1 by omega]
    simp only [L012_partial, sum_range_succ] at ih ⊢
    rw [show (-1 : ℂ) ^ (2 * N) = 1 by simp [pow_mul],
      show (-1 : ℂ) ^ (2 * N + 1) = -1 by simp [pow_add, pow_mul]]
    rw [ih]
    simp [L012_pair]
    ring

lemma L012_partial_split (N : ℕ) (s : ℂ) :
    L012_partial N s = (∑ n ∈ range (N / 2), L012_pair n s) +
      if N % 2 = 0 then 0 else L012_term (2 * (N / 2)) s := by
  have hmod : N % 2 = 0 ∨ N % 2 = 1 := by omega
  rcases hmod with hm | hm
  · rw [if_pos hm, add_zero, ← L012_partial_even]
    congr 1
    omega
  · rw [if_neg (by omega)]
    have he : N = 2 * (N / 2) + 1 := by omega
    conv_lhs => rw [he]
    rw [L012_partial, sum_range_succ]
    change L012_partial (2 * (N / 2)) s + _ = _
    rw [L012_partial_even]
    simp [pow_mul]

lemma L012_term_bound (n : ℕ) (δ : ℝ) (s : ℂ) (hs : δ ≤ s.re) :
    ‖L012_term n s‖ ≤ (n + 1 : ℝ) ^ (-δ) := by
  rw [L012_term, Complex.norm_exp, Real.rpow_def_of_pos (by positivity)]
  apply Real.exp_le_exp.mpr
  simp only [Complex.mul_re, Complex.neg_re, Complex.neg_im,
    Complex.ofReal_re, Complex.ofReal_im, mul_zero, sub_zero]
  have hl : 0 ≤ Real.log (n + 1 : ℝ) := Real.log_nonneg (by have := Nat.cast_nonneg (α := ℝ) n; linarith)
  nlinarith

/-- Uniform convergence of all alternating partial sums, without discarding odd indices. -/
theorem L012_uniform (δ R : ℝ) (hδ : 0 < δ) :
    TendstoUniformlyOn L012_partial L012_eta atTop
      {s : ℂ | δ ≤ s.re ∧ ‖s‖ ≤ R} := by
  have hp := Metric.tendstoUniformlyOn_iff.mp (L012_paired_uniform δ R hδ)
  apply Metric.tendstoUniformlyOn_iff.mpr
  intro ε hε
  obtain ⟨K, hK⟩ := eventually_atTop.mp (hp (ε / 2) (by positivity))
  have hr : Tendsto (fun n : ℕ => (n + 1 : ℝ) ^ (-δ)) atTop (𝓝 0) :=
    (tendsto_rpow_neg_atTop hδ).comp
      (tendsto_natCast_atTop_atTop.atTop_add tendsto_const_nhds)
  obtain ⟨J, hJ⟩ := eventually_atTop.mp (hr.eventually (gt_mem_nhds (by positivity : 0 < ε / 2)))
  filter_upwards [eventually_ge_atTop (2 * max K J)] with N hN
  intro s hs
  have hNK : K ≤ N / 2 := by omega
  have hNJ : J ≤ N / 2 := by omega
  have hp' := hK (N / 2) hNK s hs
  have ht : ‖L012_term (2 * (N / 2)) s‖ < ε / 2 := by
    calc
      _ ≤ (2 * ((N / 2 : ℕ) : ℝ) + 1) ^ (-δ) := by
        simpa only [Nat.cast_mul, Nat.cast_ofNat] using L012_term_bound (2 * (N / 2)) δ s hs.1
      _ ≤ (((N / 2 : ℕ) : ℝ) + 1) ^ (-δ) := by
        apply Real.rpow_le_rpow_of_nonpos (by positivity) _ (by linarith)
        nlinarith [Nat.cast_nonneg (α := ℝ) (N / 2)]
      _ < ε / 2 := hJ (N / 2) hNJ
  rw [L012_partial_split]
  split_ifs with hm
  · simpa only [add_zero] using hp'.trans (by linarith : ε / 2 < ε)
  · calc
      _ ≤ dist (L012_eta s) (∑ n ∈ range (N / 2), L012_pair n s) +
          ‖L012_term (2 * (N / 2)) s‖ := by
            simpa only [dist_self_add_right] using
              dist_triangle (L012_eta s) (∑ n ∈ range (N / 2), L012_pair n s)
                ((∑ n ∈ range (N / 2), L012_pair n s) + L012_term (2 * (N / 2)) s)
      _ < ε := by linarith

/-- All original alternating partial sums converge locally uniformly on Re(s)>0. -/
theorem L012_locally_uniform :
    TendstoLocallyUniformlyOn L012_partial L012_eta atTop
      {s : ℂ | 0 < s.re} := by
  apply tendstoLocallyUniformlyOn_of_forall_exists_nhds
  intro s hs
  have hδ : 0 < s.re / 2 := by change 0 < s.re at hs; linarith
  refine ⟨{z : ℂ | s.re / 2 ≤ z.re ∧ ‖z‖ ≤ ‖s‖ + 1}, ?_,
    L012_uniform _ _ hδ⟩
  apply mem_nhdsWithin_of_mem_nhds
  exact (Complex.continuous_re.continuousAt.eventually
    (eventually_ge_nhds (by linarith : s.re / 2 < s.re))).and
    (continuous_norm.continuousAt.eventually
      (eventually_le_nhds (by linarith : ‖s‖ < ‖s‖ + 1)))

#print axioms L012_paired_summable
#print axioms L012_holomorphic
#print axioms L012_partial_even
#print axioms L012_uniform

#print axioms L012_locally_uniform

/-- Absolute convergence before separating odd and even indices. -/
lemma L012_term_summable (s : ℂ) (hs : 1 < s.re) :
    Summable (fun n => L012_term n s) := by
  apply Summable.of_norm
  apply Summable.of_nonneg_of_le (fun _ => norm_nonneg _)
    (fun n => L012_term_bound n s.re s le_rfl)
  have h := Real.summable_nat_rpow.mpr (show -s.re < -1 by linarith)
  simpa only [Nat.cast_add, Nat.cast_one] using (summable_nat_add_iff 1).mpr h

lemma L012_term_cpow (n : ℕ) (s : ℂ) :
    L012_term n s = 1 / (n + 1 : ℂ) ^ s := by
  have hn : (n + 1 : ℂ) ≠ 0 := by exact_mod_cast (show (n + 1 : ℝ) ≠ 0 by positivity)
  rw [Complex.cpow_def_of_ne_zero hn, one_div, ← Complex.exp_neg]
  have hl : Complex.log (n + 1 : ℂ) = (Real.log (n + 1 : ℝ) : ℂ) := by
    simpa using (Complex.ofReal_log (show 0 ≤ (n + 1 : ℝ) by positivity)).symm
  rw [hl, L012_term]
  congr 1
  ring

lemma L012_even_term (n : ℕ) (s : ℂ) :
    L012_term (2 * n + 1) s = (2 : ℂ) ^ (-s) * L012_term n s := by
  rw [L012_term, L012_term, Complex.cpow_def_of_ne_zero (by norm_num : (2 : ℂ) ≠ 0)]
  have hl : Complex.log 2 = (Real.log 2 : ℂ) := by
    exact (Complex.ofReal_log (show (0 : ℝ) ≤ 2 by positivity)).symm
  rw [hl, ← Complex.exp_add]
  have he : ((2 * n + 1 : ℕ) + 1 : ℝ) = 2 * (n + 1 : ℝ) := by push_cast; ring
  rw [he, Real.log_mul (by norm_num) (by positivity)]
  push_cast
  congr 1
  ring

/-- Identification with zeta in the region of absolute convergence. -/
theorem L012_zeta_identity_of_one_lt_re (s : ℂ) (hs : 1 < s.re) :
    L012_eta s = (1 - (2 : ℂ) ^ (1 - s)) * riemannZeta s := by
  have ht := L012_term_summable s hs
  have he : Summable (fun n => L012_term (2 * n) s) :=
    ht.comp_injective (i := fun n : ℕ => 2 * n) (by intro a b h; change 2 * a = 2 * b at h; omega)
  have ho : Summable (fun n => L012_term (2 * n + 1) s) :=
    ht.comp_injective (i := fun n : ℕ => 2 * n + 1) (by intro a b h; change 2 * a + 1 = 2 * b + 1 at h; omega)
  have hz : (∑' n, L012_term n s) = riemannZeta s := by
    simp_rw [L012_term_cpow]
    exact (zeta_eq_tsum_one_div_nat_add_one_cpow hs).symm
  have hsplit := tsum_even_add_odd (f := fun n => L012_term n s) he ho
  have hodd : (∑' n, L012_term (2 * n + 1) s) =
      (2 : ℂ) ^ (-s) * riemannZeta s := by
    simp_rw [L012_even_term]
    rw [tsum_mul_left, hz]
  rw [hz, hodd] at hsplit
  have hpow : (2 : ℂ) ^ (1 - s) = 2 * (2 : ℂ) ^ (-s) := by
    rw [sub_eq_add_neg, Complex.cpow_add _ _ (by norm_num), Complex.cpow_one]
  rw [L012_eta, show (fun n => L012_pair n s) =
    (fun n => L012_term (2 * n) s - L012_term (2 * n + 1) s) from rfl,
    he.tsum_sub ho, hodd, hpow]
  linear_combination hsplit

#print axioms L012_zeta_identity_of_one_lt_re

/-- The multiplier has the derivative that cancels the zeta pole. -/
lemma L012_multiplier_deriv (s : ℂ) :
    HasDerivAt (fun z : ℂ => 1 - (2 : ℂ) ^ (1 - z))
      ((2 : ℂ) ^ (1 - s) * Complex.log 2) s := by
  simpa using (((hasDerivAt_id s).const_sub 1).const_cpow
    (Or.inl (by norm_num : (2 : ℂ) ≠ 0))).const_sub 1

/-- The punctured product has removable value log 2. -/
theorem L012_product_limit :
    Tendsto (fun s : ℂ => (1 - (2 : ℂ) ^ (1 - s)) * riemannZeta s)
      (𝓝[≠] 1) (𝓝 (Complex.log 2)) := by
  have hd : HasDerivAt (fun z : ℂ => 1 - (2 : ℂ) ^ (1 - z)) (Complex.log 2) 1 := by
    simpa using L012_multiplier_deriv 1
  have hq : Tendsto (fun z : ℂ => (1 - (2 : ℂ) ^ (1 - z)) / (z - 1))
      (𝓝[≠] 1) (𝓝 (Complex.log 2)) := by
    have ht := hd.tendsto_slope
    change Tendsto (fun z => slope (fun w : ℂ => 1 - (2 : ℂ) ^ (1 - w)) 1 z) _ _ at ht
    simpa [slope_def_field] using ht
  have h := hq.mul riemannZeta_residue_one
  simp only [mul_one] at h
  apply h.congr'
  filter_upwards [self_mem_nhdsWithin] with z hz
  have hn : z - 1 ≠ 0 := sub_ne_zero.mpr hz
  field_simp

#print axioms L012_product_limit

/-- Fill the removable singularity with its residue-determined value. -/
def L012_product_extension : ℂ → ℂ :=
  Function.update (fun s => (1 - (2 : ℂ) ^ (1 - s)) * riemannZeta s) 1
    (Complex.log 2)

lemma L012_product_extension_off_one {s : ℂ} (hs : s ≠ 1) :
    L012_product_extension s = (1 - (2 : ℂ) ^ (1 - s)) * riemannZeta s := by
  exact Function.update_of_ne hs _ _

/-- The filled product is holomorphic, including at the former pole. -/
theorem L012_product_extension_holomorphic : Differentiable ℂ L012_product_extension := by
  have hoff : ∀ s : ℂ, s ≠ 1 → DifferentiableAt ℂ L012_product_extension s := by
    intro s hs
    apply (((L012_multiplier_deriv s).differentiableAt).mul
      (differentiableAt_riemannZeta hs)).congr_of_eventuallyEq
    filter_upwards [eventually_ne_nhds hs] with z hz
    exact L012_product_extension_off_one hz
  intro s
  by_cases hs : s = 1
  · subst s
    apply (Complex.analyticAt_of_differentiable_on_punctured_nhds_of_continuousAt
      ?_ ?_).differentiableAt
    · filter_upwards [self_mem_nhdsWithin] with z hz
      exact hoff z hz
    · exact continuousAt_update_same.mpr L012_product_limit
  · exact hoff s hs

theorem L012_product_extension_one : L012_product_extension 1 = (Real.log 2 : ℂ) := by
  simp only [L012_product_extension, Function.update_self]
  exact (Complex.ofReal_log (by norm_num : (0 : ℝ) ≤ 2)).symm

#print axioms L012_multiplier_deriv
#print axioms L012_product_extension_holomorphic
#print axioms L012_product_extension_one

/-- Continue the absolutely convergent identity across the connected right half-plane. -/
theorem L012_eta_eq_extension (s : ℂ) (hs : 0 < s.re) :
    L012_eta s = L012_product_extension s := by
  have hopen : IsOpen {z : ℂ | 0 < z.re} :=
    isOpen_lt continuous_const Complex.continuous_re
  have hconv : Convex ℝ {z : ℂ | 0 < z.re} :=
    convex_halfSpace_gt ⟨Complex.reLm.map_add, Complex.reLm.map_smul⟩ 0
  have heq : L012_eta =ᶠ[𝓝 (2 : ℂ)] L012_product_extension := by
    have hn : {z : ℂ | 1 < z.re} ∈ 𝓝 (2 : ℂ) :=
      (isOpen_lt continuous_const Complex.continuous_re).mem_nhds (by norm_num)
    filter_upwards [hn] with z hz
    have hz1 : z ≠ 1 := by
      intro he
      subst z
      norm_num at hz
    rw [L012_product_extension_off_one hz1]
    exact L012_zeta_identity_of_one_lt_re z hz
  exact (L012_holomorphic.analyticOnNhd hopen).eqOn_of_preconnected_of_eventuallyEq
    (L012_product_extension_holomorphic.differentiableOn.analyticOnNhd hopen)
    hconv.isPreconnected (by norm_num : (2 : ℂ) ∈ {z : ℂ | 0 < z.re}) heq hs

theorem L012_zeta_identity (s : ℂ) (hs : 0 < s.re) (hs1 : s ≠ 1) :
    L012_eta s = (1 - (2 : ℂ) ^ (1 - s)) * riemannZeta s := by
  rw [L012_eta_eq_extension s hs, L012_product_extension_off_one hs1]

theorem L012_eta_one : L012_eta 1 = (Real.log 2 : ℂ) := by
  rw [L012_eta_eq_extension 1 (by norm_num), L012_product_extension_one]

/-- The complete convergence, holomorphicity, and removable-product assertion of L012. -/
theorem L012 :
    TendstoLocallyUniformlyOn L012_partial L012_eta atTop {s : ℂ | 0 < s.re} ∧
    DifferentiableOn ℂ L012_eta {s : ℂ | 0 < s.re} ∧
    (∀ s : ℂ, 0 < s.re → L012_eta s = L012_product_extension s) ∧
    (∀ s : ℂ, 0 < s.re → s ≠ 1 →
      L012_eta s = (1 - (2 : ℂ) ^ (1 - s)) * riemannZeta s) ∧
    L012_eta 1 = (Real.log 2 : ℂ) :=
  ⟨L012_locally_uniform, L012_holomorphic, L012_eta_eq_extension,
    L012_zeta_identity, L012_eta_one⟩

#print axioms L012_eta_eq_extension
#print axioms L012_zeta_identity
#print axioms L012_eta_one
#print axioms L012
