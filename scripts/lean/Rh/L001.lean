/-
Lemma 1: an absolutely convergent reciprocal.

For `Re(s) > 1`, `M(s) = ∑ μ(n) n^{-s}` converges absolutely and
`ζ(s) M(s) = 1`. In particular `ζ(s) ≠ 0`.

This is mathlib's `ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius`
together with `ArithmeticFunction.LSeriesSummable_moebius_iff` and
`riemannZeta_ne_zero_of_one_lt_re`.
-/
import Mathlib.NumberTheory.LSeries.Dirichlet

open scoped LSeries.notation ArithmeticFunction.Moebius ArithmeticFunction.zeta

noncomputable section

/-- Absolute convergence of `∑ μ(n) n^{-s}` iff `Re(s) > 1`. -/
theorem L001_summable_iff {s : ℂ} :
    LSeriesSummable (fun n => (μ n : ℂ)) s ↔ 1 < s.re :=
  ArithmeticFunction.LSeriesSummable_moebius_iff

/-- Absolute convergence of `∑ μ(n) n^{-s}` for `Re(s) > 1`. -/
theorem L001_summable {s : ℂ} (hs : 1 < s.re) :
    LSeriesSummable (fun n => (μ n : ℂ)) s :=
  L001_summable_iff.mpr hs

/--
The Dirichlet series of `ζ` and of `μ` are multiplicative inverses for `Re(s) > 1`.

This is the exact mathlib identity `L ↗ζ s * L ↗μ s = 1`. The proof is the
standard one: both series converge absolutely, so the product is the L-series of
the Dirichlet convolution; `ζ * μ = 1` as arithmetic functions, hence the
convolution is `δ`, and `L δ = 1`.
-/
theorem L001_LSeries {s : ℂ} (hs : 1 < s.re) :
    LSeries (fun n => (ArithmeticFunction.zeta n : ℂ)) s *
      LSeries (fun n => (μ n : ℂ)) s = 1 := by
  have hζ : LSeriesSummable (fun n => (ArithmeticFunction.zeta n : ℂ)) s :=
    ArithmeticFunction.LSeriesSummable_zeta_iff.mpr hs
  have hμ : LSeriesSummable (fun n => (μ n : ℂ)) s := L001_summable hs
  -- `L(f ⍟ g) = L f * L g` under absolute convergence.
  rw [← LSeries_convolution' hζ hμ]
  -- `ζ * μ = 1` as arithmetic functions, so `↗ζ ⍟ ↗μ = δ`, and `L δ = 1`.
  simp [← ArithmeticFunction.natCoe_apply, ← ArithmeticFunction.intCoe_apply,
    ArithmeticFunction.coe_mul, ArithmeticFunction.one_eq_delta, LSeries_delta,
    -ArithmeticFunction.zeta_apply]

/-- Lemma 1: `ζ(s) * ∑ μ(n) n^{-s} = 1` for `Re(s) > 1`. -/
theorem L001 {s : ℂ} (hs : 1 < s.re) :
    riemannZeta s * LSeries (fun n => (μ n : ℂ)) s = 1 := by
  rw [← ArithmeticFunction.LSeries_zeta_eq_riemannZeta hs]
  exact L001_LSeries hs

/-- Immediate corollary: `ζ` has no zeros in `Re(s) > 1`. -/
theorem L001_ne_zero {s : ℂ} (hs : 1 < s.re) : riemannZeta s ≠ 0 := by
  intro h
  have := L001 hs
  simp [h] at this

end

-- Kernel-axiom audit. Expected: propext, Quot.sound, Classical.choice.
#print axioms L001
#print axioms L001_ne_zero
