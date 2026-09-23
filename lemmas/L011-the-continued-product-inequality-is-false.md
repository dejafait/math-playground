# Lemma 11: the continued product inequality is false

**Hypotheses.** Define F(σ,t)=|ζ(σ)|³|ζ(σ+it)|⁴|ζ(σ+2it)| for real σ,t sufficiently close to 0.

**Conclusion.** There is ε>0 such that F(σ,t)<1 whenever |σ|<ε and |t|<ε. In particular the absolute-value version of Lemma 6 fails at points with 0<σ<1 and t≠0. The original version with ζ(σ)³ also fails there for sufficiently small σ,t.

**Proof.** ζ is holomorphic near 0. Thus F is continuous near (0,0), and by Lemma 8, F(0,0)=(1/2)^8=1/256<1. Continuity gives the claimed neighborhood, which can be shrunk to ε<1. Also ζ(σ) is real for real σ by Lemma 2 and is negative near 0 since ζ(0)=-1/2. Replacing |ζ(σ)|³ by ζ(σ)³ therefore makes the original product nonpositive there, so it cannot be ≥1. ∎

**Mathlib.** The neighborhood counterexample is not a separately named theorem in the Mathlib sources used here. The proof above combines continuity with the following Mathlib results.

Differentiability of `ζ` away from `s = 1` is `differentiableAt_riemannZeta`:

https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/RiemannZeta.html#differentiableAt_riemannZeta

The value `ζ(0) = -1/2` is `riemannZeta_zero`:

https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/RiemannZeta.html#riemannZeta_zero

The conjugation identity, which implies that `ζ` is real on the real axis, is `riemannZeta_conj`:

https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Harmonic/ZetaAsymp.html#riemannZeta_conj
