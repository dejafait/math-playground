# Lemma 52: tuning the introduced zeros into the strip

**Hypotheses.** a=1/100, b=1/1000, c=cosh b, g(u)=exp(-cosh(2u)), and

h(u)=[c g(u)+(g(u-a)+g(u+a))/2]/(c+1).

Let G and F be the Fourier transforms of g and h.

**Conclusion.** h is positive, smooth, even, superexponentially decaying, and satisfies (log h)''<-cosh(2u)/4. F has order at most 1 and

F(z)=[c+cos(az)]G(z)/(c+1).

All zeros of the prefactor are exactly z=(2k+1)100π±i/10, k∈Z. Thus the introduced nonreal zeros satisfy |Re z|>4 and |Im z|<1/2. This lemma alone does not locate every zero of G.

**Proof.** Since 1<c<2, the ratio between any two of the three positive weights is at most 2c<4<18. The proof of Lemma 50 used the weights only through their positivity, normalization, and the ratio bound 18. The same curvature estimates therefore apply without change. The remaining kernel properties are immediate from the positive shifts, and Lemma 51 gives order at most 1.

The Fourier factorization follows by real substitution in absolutely convergent integrals. To solve cos(az)=-c, put w=e^{iaz}≠0. Then w²+2cw+1=0, whose roots are -e^b and -e^{-b} since c=cosh b. Taking all logarithms gives az=(2k+1)π±ib, exactly the listed zeros. There are no other prefactor zeros. Their real parts have absolute value at least 100π>4 and imaginary parts have absolute value 1/10<1/2. The product's other zeros are precisely zeros of G, which require a separate argument. ∎
