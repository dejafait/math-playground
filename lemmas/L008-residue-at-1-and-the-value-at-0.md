# Lemma 8: residue at 1 and the value at 0

**Hypotheses.** ζ is the meromorphic continuation specified above; the pole at 1 is simple.

**Conclusion.** Res_{s=1} ζ(s)=1 and ζ(0)=-1/2.

**Proof.** For real h>0, the integral comparison for the decreasing function x^{-1-h} gives

1/h = ∫_1^∞ x^{-1-h} dx ≤ ζ(1+h) ≤ 1+∫_1^∞ x^{-1-h} dx = 1+1/h.

Thus hζ(1+h) tends to 1. By the assumed simple Laurent pole, this limit is its residue, so ζ(1-s)=-1/s+O(1) near s=0. In the functional equation, 2(2π)^{s-1}=1/π+O(s), sin(πs/2)=πs/2+O(s³), and Γ(1-s)=1+O(s), using Γ(1)=1 and its holomorphicity there. Multiplication gives ζ(s)=-1/2+O(s). Meromorphic continuation is holomorphic at 0, so ζ(0)=-1/2. ∎

**Mathlib.** The residue identity `(s-1)ζ(s) → 1` as `s → 1` is `riemannZeta_residue_one`:

https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/RiemannZeta.html#riemannZeta_residue_one

The special value `ζ(0) = -1/2` is `riemannZeta_zero`:

https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/RiemannZeta.html#riemannZeta_zero

**Lean proof status.** Validated. Lean 4.33.1, mathlib `v4.33.1`, `lake build Rh.L008` from `scripts/lean`. Kernel axioms: `propext`, `Classical.choice`, `Quot.sound`.

**Lean proof command.**

```
(cd scripts/lean && lake exe cache get && lake build Rh.L008)
```

**Lean proof code.**

```lean
/-
Lemma 8: residue at 1 and the value at 0.

The residue of ζ at s = 1 is 1, and ζ(0) = -1/2.
-/
import Mathlib.NumberTheory.LSeries.RiemannZeta

open Complex Filter
open scoped Topology

noncomputable section

/-- The residue of `ζ` at the simple pole `s = 1` is 1. -/
theorem L008_residue :
    Tendsto (fun s : ℂ => (s - 1) * riemannZeta s) (𝓝[≠] 1) (𝓝 1) :=
  riemannZeta_residue_one

/-- `ζ(0) = -1/2`. -/
theorem L008_zero : riemannZeta 0 = -1 / 2 :=
  riemannZeta_zero

/-- Lemma 8: residue 1 at s = 1, and ζ(0) = -1/2. -/
theorem L008 :
    Tendsto (fun s : ℂ => (s - 1) * riemannZeta s) (𝓝[≠] 1) (𝓝 1) ∧
      riemannZeta 0 = -1 / 2 :=
  ⟨L008_residue, L008_zero⟩

end

#print axioms L008
#print axioms L008_residue
#print axioms L008_zero
```
