# Lemma 7: nonvanishing on Re(s)=1

**Hypotheses.** t∈R and t≠0.

**Conclusion.** ζ(1+it)≠0.

**Proof.** Suppose ζ has a zero of order m≥1 at 1+it. Such an order is finite: ζ is holomorphic there, is not identically zero by Lemma 1, and the identity theorem applies. Put h=σ-1>0. The simple pole at 1 gives |ζ(1+h)|≤C_0/h for sufficiently small h. The Taylor factorization at 1+it gives |ζ(1+h+it)|≤C_1 h^m. Since t≠0 implies 1+2it≠1, holomorphicity at 1+2it gives |ζ(1+h+2it)|≤C_2. Choose a common sufficiently small interval of h on which all three bounds hold. Lemma 6 then yields

1 ≤ ζ(1+h)³|ζ(1+h+it)|⁴|ζ(1+h+2it)| ≤ C_0³C_1⁴C_2 h^{4m-3}.

The right side tends to zero, since 4m-3≥1, a contradiction. No boundary limit of the prime sum was taken: only the already-proved inequality for h>0 and finite local Taylor/Laurent estimates were used. ∎

**Mathlib.** Nonvanishing of `ζ` on the closed half-plane `Re(s) ≥ 1` is `riemannZeta_ne_zero_of_one_le_re`:

https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Nonvanishing.html#riemannZeta_ne_zero_of_one_le_re

The line `Re(s) = 1`, `s ≠ 1`, is the special case used here. The 3-4-1 product that drives the argument is `DirichletCharacter.norm_LFunction_product_ge_one`.

**Lean proof status.** Validated. Lean 4.33.1, mathlib `v4.33.1`, `lake build Rh.L007` from `scripts/lean`. Kernel axioms: `propext`, `Classical.choice`, `Quot.sound`.

**Lean proof command.**

```
(cd scripts/lean && lake exe cache get && lake build Rh.L007)
```

**Lean proof code.**

```lean
/-
Lemma 7: nonvanishing on Re(s) = 1.

For real t ≠ 0, ζ(1 + it) ≠ 0.
-/
import Mathlib.NumberTheory.LSeries.Nonvanishing

open Complex

noncomputable section

/-- `ζ` has no zeros on the line `Re(s) = 1` except the pole at `s = 1`. -/
theorem L007 {t : ℝ} (ht : t ≠ 0) : riemannZeta ((1 : ℂ) + t * I) ≠ 0 := by
  have : ((1 : ℂ) + t * I) ≠ 1 := by
    simp [add_eq_left, mul_eq_zero, I_ne_zero, ofReal_eq_zero, ht]
  exact riemannZeta_ne_zero_of_one_le_re (by simp [add_re, mul_re, I_re, I_im])

end

#print axioms L007
```
