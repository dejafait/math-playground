import Mathlib.NumberTheory.LSeries.RiemannZeta
import Mathlib.NumberTheory.Harmonic.ZetaAsymp
import Mathlib.Tactic

open Complex Filter
open scoped Topology

noncomputable section

/-- The absolute-value product in Lemma 11. -/
def L011_F (σ t : ℝ) : ℝ :=
  ‖riemannZeta (σ : ℂ)‖ ^ 3 * ‖riemannZeta ((σ : ℂ) + t * I)‖ ^ 4 *
    ‖riemannZeta ((σ : ℂ) + 2 * t * I)‖

/-- Both continued product inequalities fail throughout a neighborhood of zero.
The real part represents the real value of zeta on the real axis. -/
theorem L011 : ∃ ε : ℝ, 0 < ε ∧ ε < 1 ∧
    ∀ σ t : ℝ, |σ| < ε → |t| < ε →
      L011_F σ t < 1 ∧
      (riemannZeta (σ : ℂ)).re ^ 3 *
        ‖riemannZeta ((σ : ℂ) + t * I)‖ ^ 4 *
        ‖riemannZeta ((σ : ℂ) + 2 * t * I)‖ < 1 := by
  have hz : ContinuousAt riemannZeta (0 : ℂ) :=
    (differentiableAt_riemannZeta (by norm_num)).continuousAt
  have h₁ : ContinuousAt (fun p : ℝ × ℝ => riemannZeta (p.1 : ℂ)) (0, 0) :=
    hz.comp_of_eq (by fun_prop) (by simp)
  have h₂ : ContinuousAt (fun p : ℝ × ℝ =>
      riemannZeta ((p.1 : ℂ) + p.2 * I)) (0, 0) := by
    apply ContinuousAt.comp (g := riemannZeta) (f := fun p : ℝ × ℝ => (p.1 : ℂ) + p.2 * I)
    · simpa only [Complex.ofReal_zero, mul_zero, zero_mul, add_zero] using hz
    · fun_prop
  have h₃ : ContinuousAt (fun p : ℝ × ℝ =>
      riemannZeta ((p.1 : ℂ) + 2 * p.2 * I)) (0, 0) := by
    apply ContinuousAt.comp (g := riemannZeta) (f := fun p : ℝ × ℝ => (p.1 : ℂ) + 2 * p.2 * I)
    · simpa only [Complex.ofReal_zero, mul_zero, zero_mul, add_zero] using hz
    · fun_prop
  have hf : ContinuousAt (fun p : ℝ × ℝ => L011_F p.1 p.2) (0, 0) :=
    ((h₁.norm.pow 3).mul (h₂.norm.pow 4)).mul h₃.norm
  have hf0 : L011_F 0 0 < 1 := by
    norm_num [L011_F, riemannZeta_zero, norm_div]
  have hn0 : (riemannZeta (0 : ℂ)).re < 0 := by
    norm_num [riemannZeta_zero]
  have hev : ∀ᶠ p : ℝ × ℝ in 𝓝 (0, 0),
      L011_F p.1 p.2 < 1 ∧ (riemannZeta (p.1 : ℂ)).re < 0 :=
    (hf.eventually (gt_mem_nhds hf0)).and
      ((Complex.continuous_re.continuousAt.comp h₁).eventually (gt_mem_nhds hn0))
  obtain ⟨r, hr, hbound⟩ := Metric.eventually_nhds_iff.mp hev
  refine ⟨min (r / 2) (1 / 2), lt_min (by linarith) (by norm_num),
    lt_of_le_of_lt (min_le_right _ _) (by norm_num), ?_⟩
  intro σ t hσ ht
  have hd : dist (σ, t) (0, 0) < r := by
    rw [Prod.dist_eq, Real.dist_0_eq_abs, Real.dist_0_eq_abs]
    have hmin := min_le_left (r / 2) (1 / 2)
    exact max_lt (by linarith) (by linarith)
  obtain ⟨hf', hn⟩ := hbound hd
  refine ⟨hf', lt_of_le_of_lt ?_ zero_lt_one⟩
  exact mul_nonpos_of_nonpos_of_nonneg
    (mul_nonpos_of_nonpos_of_nonneg (show (riemannZeta (σ : ℂ)).re ^ 3 ≤ 0 by nlinarith [sq_nonneg (riemannZeta (σ : ℂ)).re]) (by positivity))
    (norm_nonneg _)

/-- Zeta on the real axis equals the real value used in the signed product. -/
theorem L011_real (σ : ℝ) :
    riemannZeta (σ : ℂ) = ((riemannZeta (σ : ℂ)).re : ℂ) := by
  have h := riemannZeta_conj (σ : ℂ)
  have hi := congrArg Complex.im h
  simp at hi
  apply Complex.ext
  · simp
  · simp only [Complex.ofReal_im]
    linarith

/-- In particular there is a counterexample inside the open critical strip
with nonzero imaginary coordinate. -/
theorem L011_counterexample : ∃ σ t : ℝ, 0 < σ ∧ σ < 1 ∧ t ≠ 0 ∧
    L011_F σ t < 1 ∧
    (riemannZeta (σ : ℂ)).re ^ 3 *
      ‖riemannZeta ((σ : ℂ) + t * I)‖ ^ 4 *
      ‖riemannZeta ((σ : ℂ) + 2 * t * I)‖ < 1 := by
  obtain ⟨ε, hε, hε1, h⟩ := L011
  have hpos : 0 < ε / 2 := by linarith
  refine ⟨ε / 2, ε / 2, hpos, by linarith, ne_of_gt hpos, ?_⟩
  exact h _ _ (by rw [abs_of_pos hpos]; linarith)
    (by rw [abs_of_pos hpos]; linarith)

#print axioms L011
#print axioms L011_real
#print axioms L011_counterexample
