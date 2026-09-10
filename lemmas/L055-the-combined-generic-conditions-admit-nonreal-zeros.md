# Lemma 55: the combined generic conditions admit nonreal zeros

**Hypotheses.** Let 0<a≤1/100, c_a=cosh(a/10), and

h_a(u)=[c_a g(u)+(g(u-a)+g(u+a))/2]/(c_a+1),  g(u)=exp(-cosh(2u)).

Let F_a be the Fourier transform of h_a.

**Conclusion.** Every F_a has all of the following properties: entire order at most 1; evenness and reality on R; a smooth strictly positive even kernel with superexponential decay and (log h_a)''<-cosh(2u)/4; strictly alternating nonzero even Taylor coefficients; positive values on the imaginary axis; and every zero in |Re z|>4, |Im z|<1/2. Nonetheless it has nonreal zeros at (2k+1)π/a±i/10 for every integer k.

**Proof.** The proof of Lemma 50 is uniform when 0<a≤1/100: the bounds e^{2a}<2 and sinh(2a)<1/40 only improve as a decreases. The three normalized weights here have maximum ratio 2c_a<4<18, so the identical curvature proof applies. Lemma 51 supplies the entire order. Positivity and evenness of the kernel give imaginary-axis positivity and nonzero alternating even coefficients by the same dominated cosine expansion as Lemma 21, applied to 2h_a on [0,∞).

The shift formula gives F_a(z)=[c_a+cos(az)]G(z)/(c_a+1). As in Lemma 52, every prefactor zero is exactly (2k+1)π/a±i/10. Its real part has absolute value ≥100π>4 and its imaginary part has absolute value 1/10. Lemma 54 places every zero of G on the real axis with absolute value >4. Products of entire functions have precisely the union of their zero sets, with added multiplicities, so these two lists locate all F_a zeros. All the stated properties hold simultaneously, but the displayed prefactor zeros are nonreal. ∎
