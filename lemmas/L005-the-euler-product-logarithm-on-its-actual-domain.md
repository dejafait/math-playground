# Lemma 5: the Euler-product logarithm on its actual domain

**Hypotheses.** Re(s)>1. The index p runs over primes and k over positive integers.

**Conclusion.** L(s)=Σ_p Σ_{k≥1} p^{-ks}/k converges absolutely, locally uniformly on Re(s)>1, and exp(L(s))=ζ(s). Consequently Re L(s)=log|ζ(s)|. For real σ>1, L(σ)=log ζ(σ).

**Proof.** On Re(s)≥1+δ, δ>0, the absolute sum is at most

Σ_p p^{-(1+δ)}/(1-p^{-(1+δ)}) ≤ (1-2^{-(1+δ)})^{-1} Σ_{n≥2} n^{-(1+δ)} < ∞.

This is a uniform majorant. For a finite set of primes p≤X, the power-series identity exp(Σ_{k≥1} z^k/k)=(1-z)^{-1}, |z|<1, gives exp(L_X(s))=Π_{p≤X}(1-p^{-s})^{-1}. Expanding the finitely many absolutely convergent geometric series and applying unique factorization identifies this product with the sum of n^{-s} over integers all of whose prime factors are ≤X. The difference from ζ(s) has absolute value at most Σ_{n>X} n^{-Re(s)}, since any omitted integer has a prime factor >X and hence is >X. This tends to zero, uniformly on Re(s)≥1+δ. Taking the limit proves exp L=ζ. Taking absolute values gives exp(Re L)=|ζ| and thus the real-logarithm identity, with no choice of a complex logarithm required. For real σ the positive Dirichlet series makes the final identity immediate. ∎

**Mathlib.** The identity `exp(∑_p -log(1-p^{-s})) = ζ(s)` for `Re(s) > 1` is `riemannZeta_eulerProduct_exp_log`:

https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/EulerProduct/DirichletLSeries.html#riemannZeta_eulerProduct_exp_log

Nonvanishing on this half-plane is `riemannZeta_ne_zero_of_one_lt_re`. For real `σ > 1`, positivity and reality of `ζ(σ)` are `riemannZeta_re_pos_of_one_lt` and `riemannZeta_im_eq_zero_of_one_lt`.

**Lean proof status.** Validated. Lean 4.33.1, mathlib `v4.33.1`, `lake build Rh.L005` from `scripts/lean`. Kernel axioms: `propext`, `Classical.choice`, `Quot.sound`.

**Lean proof command.**

```
(cd scripts/lean && lake exe cache get && lake build Rh.L005)
```

**Lean proof code.**

```lean
/-
Lemma 5: the Euler-product logarithm on its actual domain.

For Re(s) > 1, L(s) = ∑_p -log(1 - p^{-s}) converges, exp(L(s)) = ζ(s),
Re L(s) = log |ζ(s)|, and for real σ > 1 one has Re L(σ) = log ζ(σ).
-/
import Mathlib.NumberTheory.EulerProduct.DirichletLSeries
import Mathlib.NumberTheory.LSeries.Dirichlet

open Complex

noncomputable section

/-- The Euler-product logarithm `∑_p -log(1 - p^{-s})`. -/
def eulerLog (s : ℂ) : ℂ :=
  ∑' p : Nat.Primes, -log (1 - (p : ℂ) ^ (-s))

/-- `exp L(s) = ζ(s)` for `Re(s) > 1`. -/
theorem L005_exp {s : ℂ} (hs : 1 < s.re) : exp (eulerLog s) = riemannZeta s :=
  riemannZeta_eulerProduct_exp_log hs

/-- `Re L(s) = log |ζ(s)|` for `Re(s) > 1`. -/
theorem L005_re_log {s : ℂ} (hs : 1 < s.re) :
    (eulerLog s).re = Real.log ‖riemannZeta s‖ := by
  have hζ : riemannZeta s ≠ 0 := riemannZeta_ne_zero_of_one_lt_re hs
  have h := congrArg norm (L005_exp hs)
  rw [norm_exp] at h
  have hpos : 0 < ‖riemannZeta s‖ := norm_pos_iff.2 hζ
  apply Real.exp_injective
  rw [Real.exp_log hpos, h]

/-- For real `σ > 1`, `Re L(σ) = log ζ(σ)`. -/
theorem L005_real {σ : ℝ} (hσ : 1 < σ) :
    (eulerLog σ).re = Real.log (riemannZeta σ).re := by
  have hs : 1 < (σ : ℂ).re := by simpa using hσ
  rw [L005_re_log hs]
  have him := riemannZeta_im_eq_zero_of_one_lt hσ
  have hpos := riemannZeta_re_pos_of_one_lt hσ
  have : ‖riemannZeta σ‖ = (riemannZeta σ).re := by
    rw [Complex.norm_eq_sqrt_sq_add_sq, him]
    simp [zero_pow (by exact two_ne_zero), Real.sqrt_sq hpos.le]
  rw [this]

/-- Lemma 5: Euler-product logarithm, exponential identity, and real logarithm. -/
theorem L005 {s : ℂ} (hs : 1 < s.re) :
    exp (eulerLog s) = riemannZeta s ∧
    (eulerLog s).re = Real.log ‖riemannZeta s‖ :=
  ⟨L005_exp hs, L005_re_log hs⟩

end

-- Kernel-axiom audit. Expected: propext, Quot.sound, Classical.choice.
#print axioms L005
#print axioms L005_real
```

