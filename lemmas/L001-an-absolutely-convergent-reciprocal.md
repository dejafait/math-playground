# Lemma 1: an absolutely convergent reciprocal

**Hypotheses.** Re(s)=σ>1. Define μ(1)=1, μ(n)=0 if a prime square divides n, and μ(n)=(-1)^k if n is a product of k distinct primes.

**Conclusion.** M(s)=Σ_{n≥1} μ(n)n^{-s} converges absolutely and ζ(s)M(s)=1. In particular ζ(s)≠0.

**Proof.** Since |μ(n)|≤1, both series are dominated by Σ n^{-σ}<∞, whose convergence follows from the integral test. The double series for their product has sum of absolute values at most (Σ n^{-σ})². It can therefore be grouped by the product of the indices, giving

ζ(s)M(s)=Σ_{k≥1} k^{-s} Σ_{d|k} μ(d).

For k>1 with r distinct prime factors, the inner sum is Σ_{j=0}^r binom(r,j)(-1)^j=(1-1)^r=0. For k=1 it is 1. This proves the claim. No continuation of this reciprocal series to σ≤1 is asserted. ∎

**Mathlib.** The identity is in mathlib as `ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius` (`L ↗ζ s * L ↗μ s = 1` for `1 < s.re`):

https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius

Absolute convergence of the Möbius series is `ArithmeticFunction.LSeriesSummable_moebius_iff`:

https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeriesSummable_moebius_iff

Nonvanishing of `ζ` for `Re(s) > 1` is `riemannZeta_ne_zero_of_one_lt_re`:

https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#riemannZeta_ne_zero_of_one_lt_re

**Lean proof status.** Validated. Lean 4.33.1, mathlib `v4.33.1`, `lake build Rh.L001` from `scripts/lean`. Kernel axioms: `propext`, `Classical.choice`, `Quot.sound`.

**Lean proof command.**

```
(cd scripts/lean && lake exe cache get && lake build Rh.L001)
```

**Lean proof code.**

```lean
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
```
