# Lemma 10: the positive prime-logarithm representation diverges at and left of 1

**Hypotheses.** 0<σ≤1 is real.

**Conclusion.** Σ_p1/p=∞, and Σ_pΣ_{k≥1}p^{-kσ}/k=∞. For complex s with 0<Re(s)≤1, the corresponding double series is not absolutely convergent.

**Proof.** Suppose Σ_p1/p were finite. For each prime p,

Σ_{k≥1}p^{-k}/k ≤ 1/(p-1) ≤ 2/p.

Hence the finite products Π_{p≤X}(1-1/p)^{-1} would be bounded independently of X by exp(2Σ_p1/p). Expanding each finite product as convergent geometric series shows it is at least Σ_{1≤n≤X}1/n: every such integer has all its prime factors ≤X. The harmonic sums are unbounded (by integral comparison), a contradiction. For 0<σ≤1 the k=1 terms satisfy p^{-σ}≥1/p, proving divergence of the nonnegative double sum. Absolute values of p^{-ks}/k equal p^{-k Re(s)}/k, proving the complex assertion. This makes no claim about conditional convergence at individual nonreal points. ∎

**Mathlib.** Divergence of `∑_p 1/p` is `Nat.Primes.not_summable_one_div` (also `not_summable_one_div_on_primes`):

https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/SumPrimeReciprocals.html#Nat.Primes.not_summable_one_div

The comparison `∑_p p^r` converges iff `r < -1` is `Nat.Primes.summable_rpow`. The packaged double-series statement for `0 < σ ≤ 1` is not a separately named Mathlib theorem.

**Lean proof status.** Validated. Lean 4.33.1, mathlib `v4.33.1`, `lake build Rh.L010` from `scripts/lean`. Kernel axioms: `propext`, `Classical.choice`, `Quot.sound`.

**Lean proof command.**

```
(cd scripts/lean && lake exe cache get && lake build Rh.L010)
```

**Lean proof code.**

```lean
/-
Lemma 10: the positive prime-logarithm representation diverges at and left of 1.

For 0 < σ ≤ 1 real, ∑_p 1/p and ∑_p ∑_{k≥1} p^{-kσ}/k diverge. For complex s
with 0 < Re(s) ≤ 1 the corresponding double series is not absolutely convergent.
-/
import Mathlib.NumberTheory.SumPrimeReciprocals
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Pow.Complex

open Complex

noncomputable section

/-- The prime harmonic series diverges. -/
theorem L010_primes : ¬ Summable (fun p : Nat.Primes => (1 / p.1 : ℝ)) :=
  Nat.Primes.not_summable_one_div

/-- For `0 < σ ≤ 1`, the series `∑_p p^{-σ}` diverges. -/
theorem L010_rpow {σ : ℝ} (_hσ0 : 0 < σ) (hσ1 : σ ≤ 1) :
    ¬ Summable (fun p : Nat.Primes => (p.1 : ℝ) ^ (-σ)) := by
  simpa using (Nat.Primes.summable_rpow (r := -σ)).not.mpr (by linarith)

/-- The double series `∑_p ∑_{k≥1} p^{-kσ}/k` of nonnegative terms diverges. -/
theorem L010_double {σ : ℝ} (hσ0 : 0 < σ) (hσ1 : σ ≤ 1) :
    ¬ Summable (fun pk : Nat.Primes × ℕ =>
        (pk.1.1 : ℝ) ^ (-((pk.2 + 1 : ℕ) : ℝ) * σ) / (pk.2 + 1 : ℝ)) := by
  intro h
  have hinj : Function.Injective (fun p : Nat.Primes => (p, (0 : ℕ))) :=
    fun _ _ hab => (Prod.mk.inj hab).1
  have hslice := h.comp_injective hinj
  have : Summable (fun p : Nat.Primes => (p.1 : ℝ) ^ (-σ)) := by
    refine hslice.congr fun p => ?_
    simp
  exact L010_rpow hσ0 hσ1 this

/-- Absolute values of Euler-product logarithm terms. -/
lemma abs_prime_log_term (p : Nat.Primes) (k : ℕ) (s : ℂ) :
    ‖((p.1 : ℝ) : ℂ) ^ (-((k + 1 : ℕ) : ℂ) * s) / (k + 1 : ℂ)‖ =
      (p.1 : ℝ) ^ (-((k + 1 : ℕ) : ℝ) * s.re) / (k + 1 : ℝ) := by
  have hppos : 0 < (p.1 : ℝ) := Nat.cast_pos.2 p.prop.pos
  rw [norm_div, norm_cpow_eq_rpow_re_of_pos hppos]
  have hre : (-((k + 1 : ℕ) : ℂ) * s).re = -((k + 1 : ℕ) : ℝ) * s.re := by
    simp [neg_re, mul_re]
  have hden : ‖(k + 1 : ℂ)‖ = (k + 1 : ℝ) := by
    rw [← Nat.cast_succ k, Complex.norm_natCast, Nat.cast_succ]
  rw [hre, hden]

/-- For `0 < Re(s) ≤ 1`, the Euler-product logarithm series is not absolutely convergent. -/
theorem L010_abs {s : ℂ} (hs0 : 0 < s.re) (hs1 : s.re ≤ 1) :
    ¬ Summable (fun pk : Nat.Primes × ℕ =>
        ‖((pk.1.1 : ℝ) : ℂ) ^ (-((pk.2 + 1 : ℕ) : ℂ) * s) / (pk.2 + 1 : ℂ)‖) := by
  intro h
  have hreal :
      Summable (fun pk : Nat.Primes × ℕ =>
        (pk.1.1 : ℝ) ^ (-((pk.2 + 1 : ℕ) : ℝ) * s.re) / (pk.2 + 1 : ℝ)) :=
    h.congr fun pk => abs_prime_log_term pk.1 pk.2 s
  exact L010_double hs0 hs1 hreal

/-- Lemma 10: prime harmonic divergence and real double-series divergence
for `0 < σ ≤ 1`. -/
theorem L010 {σ : ℝ} (hσ0 : 0 < σ) (hσ1 : σ ≤ 1) :
    ¬ Summable (fun p : Nat.Primes => (1 / p.1 : ℝ)) ∧
      ¬ Summable (fun pk : Nat.Primes × ℕ =>
          (pk.1.1 : ℝ) ^ (-((pk.2 + 1 : ℕ) : ℝ) * σ) / (pk.2 + 1 : ℝ)) :=
  ⟨L010_primes, L010_double hσ0 hσ1⟩

end

#print axioms L010
#print axioms L010_primes
#print axioms L010_double
#print axioms L010_abs
```
