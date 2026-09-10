# Lemma 18: entire completion and exact zero correspondence

**Hypotheses.** I is as in Lemma 17. Define ξ(s)=1/2+s(s-1)I(s)/2 and Ξ(z)=ξ(1/2+iz).

**Conclusion.** ξ is entire, ξ(1-s)=ξ(s), ξ(conj(s))=conj(ξ(s)), and ξ(0)=ξ(1)=1/2. On Re(s)>0, away from s=1,

ξ(s)=s(s-1)π^{-s/2}Γ(s/2)ζ(s)/2.

The zeros of ξ are exactly the nontrivial zeros of ζ, with the same multiplicities. Ξ is entire, even, and real on the real axis. RH is exactly the still-unproved assertion that all zeros of Ξ are real.

**Proof.** Entirety and reflection follow from Lemma 17 and s(s-1)=(1-s)((1-s)-1); endpoint values follow by substitution. Since ψ is real, conjugating the absolutely convergent integral shows I(conj(s))=conj(I(s)), and then the same holds for ξ. Multiply the identity of Lemma 17 by s(s-1)/2; the rational terms give exactly 1/2. This proves the product expression for Re(s)>1. Its right side is holomorphic on Re(s)>0 after removing the singularity at 1: Γ(s/2) is holomorphic there and (s-1) cancels the only ζ pole. The identity theorem gives the asserted extension.

In the open strip every prefactor in this expression is holomorphic and nonzero, so zero multiplicities agree. For Re(s)≥1 away from 1 the expression and Lemmas 1 and 7 make ξ nonzero; at 1 its value is 1/2. For Re(s)≤0 reflect to Re(1-s)≥1. Thus ξ has no zeros outside the open strip. By Lemma 9 this proves the exact zero correspondence. Composition makes Ξ entire, and reflection gives Ξ(-z)=Ξ(z). Moreover conjugation gives conj(Ξ(z))=Ξ(-conj(z))=Ξ(conj(z)), hence reality on R. Finally if s=β+iγ, its corresponding variable is z=(s-1/2)/i=γ+i(1/2-β), real exactly when β=1/2. The change of variable has nonzero derivative and preserves multiplicity. ∎
