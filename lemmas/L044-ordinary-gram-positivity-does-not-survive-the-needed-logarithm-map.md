# Lemma 44: ordinary Gram positivity does not survive the needed logarithm map

**Hypotheses.** On R set g(u)=exp(-cosh(2u)), h(u)=(9/10)g(u)+(g(u-8)+g(u+8))/20, and F(z)=∫_R h(u)e^{izu}du. Define normalized even moments μ_{2n}=∫_R u^{2n}h(u)du/∫_R h(u)du. Near z=0 define T_2 by

log(F(z)/F(0))=-(μ_2/2)z²-(T_2/2)z⁴+O(z⁶).

**Conclusion.** h is smooth, strictly positive, even, and superexponentially decaying; its ordinary even-moment Gram matrices are all positive definite. Nevertheless T_2<0, so the analogous 1-by-1 logarithmic Hankel matrix is already negative.

**Proof.** The regularity, decay, and all moment/entire-transform properties follow exactly as in Lemma 22, now with shifts 8 and positive weights summing to 1. Ordinary Gram positivity follows from the proof of Lemma 43 applied to this positive density. Write ν_2 and ν_4 for the normalized moments of g. Symmetry and real substitutions in the shifted integrals give

μ_2=ν_2+8²/10,

μ_4=ν_4+(6·8²/10)ν_2+8⁴/10.

It follows that μ_4-3μ_2²=(ν_4-3ν_2²)+(7/100)8⁴.

To bound ν_2, use cosh(2u)≥1+2u², so ∫_R u²g(u)du≤e^{-1}√π/(4√2) by the Gaussian second moment. On [-1/2,1/2], cosh(2u)≤cosh 1<2, so ∫_R g(u)du>e^{-2}. Here cosh 1<2 follows from e<3 and e^{-1}<1, and e<3 follows by comparing Σ_{n≥2}1/n! with Σ_{n≥2}2^{-(n-1)}, strictly at n≥3. Therefore ν_2<e√π/(4√2)<3/2, using π<4. As ν_4≥0,

μ_4-3μ_2² > -27/4+(7/100)4096=27997/100>0.

Expanding the local logarithm of 1-(μ_2/2)z²+(μ_4/24)z⁴+O(z⁶) gives T_2=(3μ_2²-μ_4)/12<0. This proves the failed preservation directly. Also the real shift formula gives F(z)=[9+cos(8z)]G(z)/10 for the entire transform G of g, so it has explicit nonreal zeros at (π+i log(9+√80))/8 and its symmetric images. No positivity of reciprocal-zero forms can be inferred merely from the ordinary moment Gram property. ∎
