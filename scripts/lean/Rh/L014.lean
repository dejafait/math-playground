import Rh.L012
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals

open Complex Filter Finset
open scoped Topology Function
noncomputable section

/-- The integral over the nth occupied interval of the kernel in L014. -/
def L014_cell (n : ℕ) (s : ℂ) : ℂ :=
  ∫ x : ℝ in (2 * n + 1 : ℝ)..(2 * n + 2 : ℝ), (x : ℂ) ^ (-s - 1)

lemma L014_ne_zero (s : ℂ) (hs : 0 < s.re) : s ≠ 0 := by
  intro h
  simpa [h] using hs

/-- Integrating on one occupied interval recovers a paired Dirichlet term. -/
theorem L014_cell_identity (n : ℕ) (s : ℂ) (hs : 0 < s.re) :
    L014_cell n s = L012_pair n s / s := by
  have hne := L014_ne_zero s hs
  have hr : -s - 1 ≠ (-1 : ℂ) := by intro h; apply hne; linear_combination -h
  have hab : (0 : ℝ) ∉ Set.uIcc (2 * n + 1 : ℝ) (2 * n + 2 : ℝ) := by
    rw [Set.uIcc_of_le (by linarith)]
    intro h
    have := h.1
    nlinarith [Nat.cast_nonneg (α := ℝ) n]
  rw [L014_cell, integral_cpow (Or.inr ⟨hr, hab⟩)]
  have hexp : -s - 1 + 1 = -s := by ring
  rw [hexp]
  have hterm (k : ℕ) : L012_term k s = ((k + 1 : ℝ) : ℂ) ^ (-s) := by
    rw [L012_term, Complex.cpow_def_of_ne_zero (by exact_mod_cast (show (k + 1 : ℝ) ≠ 0 by positivity)),
      ← Complex.ofReal_log (by positivity)]
    congr 1
    ring
  simp only [L012_pair, hterm, Nat.cast_add, Nat.cast_mul, Nat.cast_ofNat, Nat.cast_one]
  push_cast
  field_simp
  ring

/-- The finite integral sum is the original even alternating partial sum divided by s. -/
theorem L014_finite (N : ℕ) (s : ℂ) (hs : 0 < s.re) :
    ∑ n ∈ range N, L014_cell n s = L012_partial (2 * N) s / s := by
  simp_rw [L014_cell_identity _ _ hs]
  rw [← Finset.sum_div, L012_partial_even]

/-- The cell integrals form an absolutely summable complex series. -/
theorem L014_cell_summable (s : ℂ) (hs : 0 < s.re) :
    Summable (fun n => L014_cell n s) := by
  simp_rw [L014_cell_identity _ _ hs]
  exact (L012_paired_summable s hs).div_const s

/-- Identification of the sum of cell integrals; not yet the improper integral. -/
theorem L014_cell_sum (s : ℂ) (hs : 0 < s.re) :
    ∑' n, L014_cell n s = L012_eta s / s := by
  simp_rw [L014_cell_identity _ _ hs]
  exact tsum_div_const

#print axioms L014_cell_identity
#print axioms L014_finite
#print axioms L014_cell_summable
#print axioms L014_cell_sum

open MeasureTheory Set

/-- The occupied half-open intervals, indexed from zero. -/
def L014_support : Set ℝ := ⋃ n : ℕ, Ico (2 * n + 1 : ℝ) (2 * n + 2 : ℝ)

def L014_weight (x : ℝ) : ℝ := L014_support.indicator (fun _ => 1) x

lemma L014_support_measurable : MeasurableSet L014_support :=
  MeasurableSet.iUnion (fun _ => measurableSet_Ico)

lemma L014_support_subset : L014_support ⊆ Ici (1 : ℝ) := by
  intro x hx
  obtain ⟨n, hn⟩ := mem_iUnion.mp hx
  have := hn.1
  have := Nat.cast_nonneg (α := ℝ) n
  change 1 ≤ x
  linarith

lemma L014_weight_bounds (x : ℝ) : 0 ≤ L014_weight x ∧ L014_weight x ≤ 1 := by
  classical
  by_cases hx : x ∈ L014_support <;> simp [L014_weight, hx]

lemma L014_weighted_eq (s : ℂ) :
    (fun x : ℝ => (L014_weight x : ℂ) * (x : ℂ) ^ (-s - 1)) =
      L014_support.indicator (fun x : ℝ => (x : ℂ) ^ (-s - 1)) := by
  classical
  funext x
  by_cases hx : x ∈ L014_support <;> simp [L014_weight, hx]

/-- Absolute integrability of the actual weighted integrand on [1,∞). -/
theorem L014_weighted_integrable (s : ℂ) (hs : 0 < s.re) :
    IntegrableOn (fun x : ℝ => (L014_weight x : ℂ) * (x : ℂ) ^ (-s - 1))
      (Ici 1) := by
  rw [L014_weighted_eq]
  have h : IntegrableOn (fun x : ℝ => (x : ℂ) ^ (-s - 1)) (Ici 1) := by
    apply (integrableOn_Ici_iff_integrableOn_Ioi (by finiteness)).mpr
    apply integrableOn_Ioi_cpow_of_lt _ (by norm_num)
    simp only [sub_re, neg_re, one_re]
    linarith
  exact h.indicator L014_support_measurable

#print axioms L014_weight_bounds
#print axioms L014_weighted_integrable

/-- The weighted improper integral is the sum of the occupied cell integrals. -/
theorem L014_integral_eq_sum (s : ℂ) (hs : 0 < s.re) :
    (∫ x : ℝ in Ici 1, (L014_weight x : ℂ) * (x : ℂ) ^ (-s - 1)) =
      ∑' n, L014_cell n s := by
  rw [L014_weighted_eq, integral_indicator L014_support_measurable,
    Measure.restrict_restrict L014_support_measurable,
    Set.inter_eq_left.mpr L014_support_subset]
  have hbase : IntegrableOn (fun x : ℝ => (x : ℂ) ^ (-s - 1)) (Ici 1) := by
    apply (integrableOn_Ici_iff_integrableOn_Ioi (by finiteness)).mpr
    apply integrableOn_Ioi_cpow_of_lt _ (by norm_num)
    simp only [sub_re, neg_re, one_re]
    linarith
  have hd : Pairwise (Disjoint on (fun n : ℕ =>
      Set.Ico (2 * n + 1 : ℝ) (2 * n + 2 : ℝ))) := by
    intro i j hij
    apply Set.disjoint_left.mpr
    intro x hi hj
    rcases lt_or_gt_of_ne hij with h | h
    · have hc : (i : ℝ) + 1 ≤ j := by exact_mod_cast h
      have := hi.2
      have := hj.1
      linarith
    · have hc : (j : ℝ) + 1 ≤ i := by exact_mod_cast h
      have := hj.2
      have := hi.1
      linarith
  rw [L014_support, integral_iUnion (fun _ => measurableSet_Ico) hd
    (hbase.mono_set L014_support_subset)]
  congr 1
  funext n
  rw [integral_Ico_eq_integral_Ioc, L014_cell,
    intervalIntegral.integral_of_le (by linarith)]

theorem L014_first_identity (s : ℂ) (hs : 0 < s.re) :
    (∫ x : ℝ in Ici 1, (L014_weight x : ℂ) * (x : ℂ) ^ (-s - 1)) =
      L012_eta s / s :=
  (L014_integral_eq_sum s hs).trans (L014_cell_sum s hs)

#print axioms L014_integral_eq_sum
#print axioms L014_first_identity

/-- The exponential Jacobian converts the weighted power to the Laplace kernel. -/
lemma L014_exp_integrand (s : ℂ) (u : ℝ) :
    Real.exp u • ((L014_weight (Real.exp u) : ℂ) *
      (Real.exp u : ℂ) ^ (-s - 1)) =
    (L014_weight (Real.exp u) : ℂ) * Complex.exp (-s * u) := by
  rw [Complex.cpow_def_of_ne_zero (by exact_mod_cast (Real.exp_ne_zero u)),
    ← Complex.ofReal_log (Real.exp_pos u).le, Real.log_exp,
    Complex.real_smul, Complex.ofReal_exp]
  calc
    Complex.exp (u : ℂ) * ((L014_weight (Real.exp u) : ℂ) *
        Complex.exp ((u : ℂ) * (-s - 1))) =
      (L014_weight (Real.exp u) : ℂ) *
        (Complex.exp (u : ℂ) * Complex.exp ((u : ℂ) * (-s - 1))) := by ring
    _ = _ := by rw [← Complex.exp_add]; congr 2; ring

/-- Absolute integrability of the transformed kernel on [0,∞). -/
theorem L014_laplace_integrable (s : ℂ) (hs : 0 < s.re) :
    IntegrableOn (fun u : ℝ => (L014_weight (Real.exp u) : ℂ) *
      Complex.exp (-s * u)) (Ici 0) := by
  apply (integrableOn_Ici_iff_integrableOn_Ioi (by finiteness)).mpr
  have h := (integrableOn_Ici_iff_integrableOn_Ioi (by finiteness)).mp
    (L014_weighted_integrable s hs)
  have he := (integrableOn_comp_exp_Ioi
    (fun x : ℝ => (L014_weight x : ℂ) * (x : ℂ) ^ (-s - 1)) 0).mpr
    (by simpa using h)
  simpa only [L014_exp_integrand] using he

/-- The exponential substitution identifies the two improper integrals. -/
theorem L014_substitution (s : ℂ) :
    (∫ u : ℝ in Ici 0, (L014_weight (Real.exp u) : ℂ) * Complex.exp (-s * u)) =
    (∫ x : ℝ in Ici 1, (L014_weight x : ℂ) * (x : ℂ) ^ (-s - 1)) := by
  rw [integral_Ici_eq_integral_Ioi, integral_Ici_eq_integral_Ioi]
  simpa only [L014_exp_integrand, Real.exp_zero] using
    integral_comp_exp_Ioi
      (fun x : ℝ => (L014_weight x : ℂ) * (x : ℂ) ^ (-s - 1)) 0

theorem L014_second_identity (s : ℂ) (hs : 0 < s.re) :
    (∫ u : ℝ in Ici 0, (L014_weight (Real.exp u) : ℂ) * Complex.exp (-s * u)) =
      L012_eta s / s :=
  (L014_substitution s).trans (L014_first_identity s hs)

#print axioms L014_exp_integrand
#print axioms L014_laplace_integrable
#print axioms L014_substitution
#print axioms L014_second_identity

/-- A common exponential majorant on every closed right half-plane. -/
lemma L014_laplace_majorant (s : ℂ) (δ u : ℝ) (hs : δ ≤ s.re) (hu : 0 ≤ u) :
    ‖(L014_weight (Real.exp u) : ℂ) * Complex.exp (-s * u)‖ ≤
      Real.exp (-δ * u) := by
  rw [norm_mul, Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg (L014_weight_bounds _).1, Complex.norm_exp]
  have hre : (-s * (u : ℂ)).re = -s.re * u := by simp
  rw [hre]
  calc
    L014_weight (Real.exp u) * Real.exp (-s.re * u) ≤
        1 * Real.exp (-s.re * u) :=
      mul_le_mul_of_nonneg_right (L014_weight_bounds _).2 (Real.exp_pos _).le
    _ ≤ Real.exp (-δ * u) := by
      rw [one_mul]
      exact Real.exp_le_exp.mpr (mul_le_mul_of_nonneg_right (neg_le_neg hs) hu)

/-- Uniform Laplace tail bound, independent of the imaginary part of s. -/
theorem L014_laplace_tail (s : ℂ) (δ T : ℝ) (hδ : 0 < δ)
    (hs : δ ≤ s.re) (hT : 0 ≤ T) :
    ‖∫ u : ℝ in Ici T, (L014_weight (Real.exp u) : ℂ) *
      Complex.exp (-s * u)‖ ≤ Real.exp (-δ * T) / δ := by
  rw [integral_Ici_eq_integral_Ioi]
  calc
    _ ≤ ∫ u : ℝ in Ioi T, Real.exp (-δ * u) := by
      apply norm_integral_le_of_norm_le (integrableOn_exp_mul_Ioi (neg_neg_of_pos hδ) T)
      filter_upwards [ae_restrict_mem measurableSet_Ioi] with u hu
      exact L014_laplace_majorant s δ u hs (hT.trans hu.le)
    _ = _ := by rw [integral_exp_mul_Ioi (neg_neg_of_pos hδ)]; simp

#print axioms L014_laplace_majorant
#print axioms L014_laplace_tail

/-- The same uniform tail bound in the original variable, with cutoff exp(T). -/
theorem L014_power_tail (s : ℂ) (δ T : ℝ) (hδ : 0 < δ)
    (hs : δ ≤ s.re) (hT : 0 ≤ T) :
    ‖∫ x : ℝ in Ici (Real.exp T), (L014_weight x : ℂ) *
      (x : ℂ) ^ (-s - 1)‖ ≤ Real.exp (-δ * T) / δ := by
  have he : (∫ u : ℝ in Ici T, (L014_weight (Real.exp u) : ℂ) *
      Complex.exp (-s * u)) =
      ∫ x : ℝ in Ici (Real.exp T), (L014_weight x : ℂ) * (x : ℂ) ^ (-s - 1) := by
    rw [integral_Ici_eq_integral_Ioi, integral_Ici_eq_integral_Ioi]
    simpa only [L014_exp_integrand] using
      integral_comp_exp_Ioi
        (fun x : ℝ => (L014_weight x : ℂ) * (x : ℂ) ^ (-s - 1)) T
  rw [← he]
  exact L014_laplace_tail s δ T hδ hs hT

#print axioms L014_power_tail

/-- The common tail majorant tends to zero. -/
lemma L014_tail_decay (δ : ℝ) (hδ : 0 < δ) :
    Tendsto (fun T : ℝ => Real.exp (-δ * T) / δ) atTop (𝓝 0) := by
  have h := Real.tendsto_exp_atBot.comp
    ((tendsto_const_mul_atBot_of_neg (neg_neg_of_pos hδ)).mpr tendsto_id)
  simpa using h.div_const δ

/-- Uniform convergence of finite Laplace integrals on closed right half-planes. -/
theorem L014_laplace_uniform (δ : ℝ) (hδ : 0 < δ) :
    TendstoUniformlyOn
      (fun T : ℝ => fun s : ℂ => ∫ u : ℝ in (0 : ℝ)..T,
        (L014_weight (Real.exp u) : ℂ) * Complex.exp (-s * u))
      (fun s => L012_eta s / s) atTop {s : ℂ | δ ≤ s.re} := by
  apply Metric.tendstoUniformlyOn_iff.mpr
  intro ε hε
  filter_upwards [(L014_tail_decay δ hδ).eventually (gt_mem_nhds hε),
    eventually_ge_atTop (0 : ℝ)] with T hεT hT
  intro s hs
  have hi := L014_laplace_integrable s (hδ.trans_le hs)
  have he := intervalIntegral.integral_Ici_sub_Ici' hi
    (hi.mono_set (Ici_subset_Ici.mpr hT))
  rw [L014_second_identity s (hδ.trans_le hs)] at he
  rw [dist_eq_norm, ← he]
  simp only [sub_sub_cancel]
  exact (L014_laplace_tail s δ T hδ hs hT).trans_lt hεT

#print axioms L014_tail_decay
#print axioms L014_laplace_uniform

/-- Uniform convergence with an arbitrary real cutoff in the power variable. -/
theorem L014_power_uniform (δ : ℝ) (hδ : 0 < δ) :
    TendstoUniformlyOn
      (fun X : ℝ => fun s : ℂ => ∫ x : ℝ in (1 : ℝ)..X,
        (L014_weight x : ℂ) * (x : ℂ) ^ (-s - 1))
      (fun s => L012_eta s / s) atTop {s : ℂ | δ ≤ s.re} := by
  apply Metric.tendstoUniformlyOn_iff.mpr
  intro ε hε
  have hd := (L014_tail_decay δ hδ).comp Real.tendsto_log_atTop
  filter_upwards [hd.eventually (gt_mem_nhds hε),
    eventually_ge_atTop (1 : ℝ)] with X hεX hX
  intro s hs
  have hi := L014_weighted_integrable s (hδ.trans_le hs)
  have he := intervalIntegral.integral_Ici_sub_Ici' hi
    (hi.mono_set (Ici_subset_Ici.mpr hX))
  rw [L014_first_identity s (hδ.trans_le hs)] at he
  rw [dist_eq_norm, ← he]
  simp only [sub_sub_cancel]
  have ht := L014_power_tail s δ (Real.log X) hδ hs (Real.log_nonneg hX)
  rw [Real.exp_log (by linarith : 0 < X)] at ht
  exact ht.trans_lt hεX

/-- Local uniform convergence of the Laplace integral throughout Re(s)>0. -/
theorem L014_laplace_locally_uniform :
    TendstoLocallyUniformlyOn
      (fun T : ℝ => fun s : ℂ => ∫ u : ℝ in (0 : ℝ)..T,
        (L014_weight (Real.exp u) : ℂ) * Complex.exp (-s * u))
      (fun s => L012_eta s / s) atTop {s : ℂ | 0 < s.re} := by
  apply tendstoLocallyUniformlyOn_of_forall_exists_nhds
  intro s hs
  have hδ : 0 < s.re / 2 := by change 0 < s.re at hs; linarith
  refine ⟨{z : ℂ | s.re / 2 ≤ z.re}, ?_, L014_laplace_uniform _ hδ⟩
  apply mem_nhdsWithin_of_mem_nhds
  exact Complex.continuous_re.continuousAt.eventually
    (eventually_ge_nhds (by linarith : s.re / 2 < s.re))

/-- Local uniform convergence of the power integral throughout Re(s)>0. -/
theorem L014_power_locally_uniform :
    TendstoLocallyUniformlyOn
      (fun X : ℝ => fun s : ℂ => ∫ x : ℝ in (1 : ℝ)..X,
        (L014_weight x : ℂ) * (x : ℂ) ^ (-s - 1))
      (fun s => L012_eta s / s) atTop {s : ℂ | 0 < s.re} := by
  apply tendstoLocallyUniformlyOn_of_forall_exists_nhds
  intro s hs
  have hδ : 0 < s.re / 2 := by change 0 < s.re at hs; linarith
  refine ⟨{z : ℂ | s.re / 2 ≤ z.re}, ?_, L014_power_uniform _ hδ⟩
  apply mem_nhdsWithin_of_mem_nhds
  exact Complex.continuous_re.continuousAt.eventually
    (eventually_ge_nhds (by linarith : s.re / 2 < s.re))

#print axioms L014_power_uniform
#print axioms L014_laplace_locally_uniform
#print axioms L014_power_locally_uniform
