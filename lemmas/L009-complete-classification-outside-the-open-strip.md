# Lemma 9: complete classification outside the open strip

**Hypotheses.** s is outside 0<Re(s)<1, and s≠1 (the pole).

**Conclusion.** ζ(s)=0 if and only if s=-2n for a positive integer n. Each such zero is simple.

**Proof.** Lemmas 1 and 7 exclude zeros for Re(s)≥1. For Re(s)<0, the factor ζ(1-s) is holomorphic and nonzero by Lemma 1; Γ(1-s) is holomorphic and nonzero because Re(1-s)>1. The exponential prefactor is also holomorphic and nonzero. Thus the functional equation says that a zero occurs exactly when sin(πs/2)=0, namely at the negative even integers in this region. These zeros are simple: the sine derivative there is (π/2)cos(-nπ)≠0 and all other factors are nonzero. If Re(s)=0 and s=it with real t≠0, Lemma 7 makes ζ(1-it) nonzero, while the other factors are again holomorphic and nonzero. Finally s=0 is nonzero by Lemma 8. ∎

**Mathlib.** That the negative even integers are zeros is `riemannZeta_neg_two_mul_nat_add_one`:

https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/RiemannZeta.html#riemannZeta_neg_two_mul_nat_add_one

Nonvanishing on `Re(s) ≥ 1` is `riemannZeta_ne_zero_of_one_le_re`. The functional equation used to classify zeros with `Re(s) ≤ 0` is `riemannZeta_one_sub`. The value `ζ(0) = -1/2` is `riemannZeta_zero`. The packaged classification (zeros outside the open strip, away from the pole, are exactly the negative even integers, each simple) is not a named Mathlib theorem.
