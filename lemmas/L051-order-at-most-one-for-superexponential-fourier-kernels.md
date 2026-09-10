# Lemma 51: order at most one for superexponential Fourier kernels

**Hypotheses.** A real even measurable function h satisfies |h(u)|≤C exp(-c e^{2|u|}) for some C,c>0. Define F(z)=∫_R h(u)e^{izu}du.

**Conclusion.** F is entire and obeys log max_{|z|≤R}|F(z)|=O((R+1)log(R+2)) as an upper bound; in particular, if F is nonzero, its entire order is at most 1. This applies to g and all the finite positive shifts used above.

**Proof.** For every fixed derivative order k and compact |z|≤R, the absolute integrand after k derivatives is at most C|u|^k exp(R|u|-c e^{2|u|}), integrable. Hence dominated differentiation makes F entire. For R≥1,

max_{|z|≤R}|F(z)|≤2C∫_0^∞exp(Ru-c e^{2u})du=C∫_1^∞X^{R/2-1}e^{-cX}dX.

With m=ceil(R/2), bound X^{R/2-1}≤X^m and extend the integral to (0,∞), obtaining C m! c^{-(m+1)}. Taking logarithms and using m!≤m^m gives the asserted upper bound. A finite shift changes only C,c: e^{2|u-t|}≥e^{-2|t|}e^{2|u|}. No zero-location theorem is used. ∎
