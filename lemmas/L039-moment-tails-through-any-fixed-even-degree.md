# Lemma 39: moment tails through any fixed even degree

**Hypotheses.** m≥0 is an integer, p=m+2, and 0≤k≤2m is an even integer. Let B_k be the four-term integral on [0,2] in Lemma 35.

**Conclusion.** 0≤M_k-B_k≤E_m, where

E_m=128e^{-150}Σ_{j=0}^p [p!/(p-j)!]50^{p-j}/3^{j+1} + 80,000p!e^{-74}.

For moments through M_12, take m=6, p=8; the second coefficient is 3,225,600,000.

**Proof.** Repeat the bounds of Lemma 35 with u^k≤e^{2mu}. The substitution X=e^{2u} now gives the power X^{m+5/4}, bounded by X^{m+2}=X^p on X≥1. Thus the u≥2 tail is bounded by 128∫_{50}^∞X^p e^{-3X}dX, equal to the first displayed term by repeated integration by parts. The n≥5 bound becomes 64p!Σ_{n≥5}n⁴e^{-(3n²-1)}≤64p!·1250e^{-74}, equal to the second term. Both arguments are valid for each fixed m; the bound may become inefficient as m grows and no uniform-in-m sign conclusion is asserted. ∎
