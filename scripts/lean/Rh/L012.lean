/-
Lemma 12: alternating Dirichlet series on the right half-plane.
Work in progress: paired-term convergence and the holomorphic sum.
-/
import Mathlib.Analysis.Complex.LocallyUniformLimit
import Mathlib.Analysis.PSeries
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
  have hl : 0 ≤ Real.log (n + 1 : ℝ) := Real.log_nonneg (by positivity)
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
    (Real.tendsto_rpow_neg_atTop hδ).comp
      (tendsto_natCast_atTop_atTop.atTop_add tendsto_const_nhds)
  obtain ⟨J, hJ⟩ := eventually_atTop.mp (hr.eventually (gt_mem_nhds (by positivity : 0 < ε / 2)))
  filter_upwards [eventually_ge_atTop (2 * max K J)] with N hN
  intro s hs
  have hNK : K ≤ N / 2 := by omega
  have hNJ : J ≤ N / 2 := by omega
  have hp' := hK (N / 2) hNK s hs
  have ht : ‖L012_term (2 * (N / 2)) s‖ < ε / 2 := by
    calc
      _ ≤ (2 * (N / 2) + 1 : ℝ) ^ (-δ) := by
        simpa only [Nat.cast_mul, Nat.cast_ofNat] using L012_term_bound (2 * (N / 2)) δ s hs.1
      _ ≤ (N / 2 + 1 : ℝ) ^ (-δ) := by
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

#print axioms L012_paired_summable
#print axioms L012_holomorphic
#print axioms L012_partial_even
#print axioms L012_uniform
