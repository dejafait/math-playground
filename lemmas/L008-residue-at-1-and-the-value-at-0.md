# Lemma 8: residue at 1 and the value at 0

**Hypotheses.** ζ is the meromorphic continuation specified above; the pole at 1 is simple.

**Conclusion.** Res_{s=1} ζ(s)=1 and ζ(0)=-1/2.

**Proof.** For real h>0, the integral comparison for the decreasing function x^{-1-h} gives

1/h = ∫_1^∞ x^{-1-h} dx ≤ ζ(1+h) ≤ 1+∫_1^∞ x^{-1-h} dx = 1+1/h.

Thus hζ(1+h) tends to 1. By the assumed simple Laurent pole, this limit is its residue, so ζ(1-s)=-1/s+O(1) near s=0. In the functional equation, 2(2π)^{s-1}=1/π+O(s), sin(πs/2)=πs/2+O(s³), and Γ(1-s)=1+O(s), using Γ(1)=1 and its holomorphicity there. Multiplication gives ζ(s)=-1/2+O(s). Meromorphic continuation is holomorphic at 0, so ζ(0)=-1/2. ∎
