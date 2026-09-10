# Lemma 54: every comparison-base zero is real and outside the small rectangle

**Hypotheses.** G(z)=0 and Y=Y_z is the nontrivial solution in Lemma 53.

**Conclusion.** z is real and |z|>2sqrt(7)>4.

**Proof.** Y(0)=0. Its smoothness gives Y(x)=O(x) near zero; the decay in Lemma 53 makes Y,Y',e^xY square integrable on [0,∞), and makes Y'(x)conj(Y(x)) tend to zero at infinity. Multiply the differential equation by conj(Y), integrate on [0,R], and integrate the second derivative by parts. Letting R tend to infinity gives

∫_0^∞(|Y'|²+e^{2x}|Y|²)dx=(z²/4)∫_0^∞|Y|²dx.

The right-hand norm is strictly positive by nontriviality. The left side is real and positive, hence z²/4 is positive real, which forces z real and nonzero.

For the sharper lower bound, put b(x)=1/x-2x for x>0. On [ε,R], expansion and integration by parts give

∫|Y'-bY|²dx=∫[|Y'|²+(b²+b')|Y|²]dx-[b|Y|²]_{ε}^{R}.

Here b²+b'=4x²-6. At zero, Y=O(x) makes b|Y|²=O(x) tend to zero and makes Y'-bY bounded. At infinity the proved decay kills both the boundary and all polynomial weights. Taking ε to zero and R to infinity proves

∫_0^∞(|Y'|²+4x²|Y|²)dx≥6∫_0^∞|Y|²dx.

For x>0, the exponential series gives

e^{2x}≥1+2x+2x²+(4/3)x³>1+4x²,

because the difference after the constant and 4x² is 2x(1-x+(2/3)x²)>0; its quadratic factor has negative discriminant and positive leading coefficient. Therefore the first energy integral is strictly greater than 7∫|Y|². Strictness holds because Y is nonzero on some interval with x>0. Thus z²/4>7, proving the stated bound. ∎
