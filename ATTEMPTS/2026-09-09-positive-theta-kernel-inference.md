# Attempt: positive even superexponential Fourier kernels force real zeros

Date: 2026-09-09

Outcome: failed sufficient-condition guess; the actual theta representation is retained in PROOF.md, Lemmas 16–22.

The theta calculation gives Ξ(z)=∫_0^∞K(u)cos(zu)du with K strictly positive and superexponentially decaying, yielding alternating even Taylor coefficients and Ξ(iy)>0. The attempted inference was that these properties, together with evenness and smoothness, force every zero of Ξ to be real.

For g(u)=exp(-cosh(2u)), set h(u)=2g(u)+(g(u-4)+g(u+4))/2. This is strictly positive, smooth, even, and bounded by 3exp(-e^{-8}e^{2|u|}/2). Its entire Fourier transform equals (2+cos(4z))G(z), where G is the entire Fourier transform of g. Consequently it has an off-real zero at (π+i log(2+√3))/4, within |Im(z)|<1/2, while retaining the same positive-moment and imaginary-axis-positivity properties.

**WHY IT FAILS.** Fourier kernel positivity, even when supplemented by smoothness and superexponential decay, does not force real zeros: positive translates of an even kernel multiply its transform by a factor with explicit nonreal zeros. The construction even places one such zero in the same horizontal strip that contains all Ξ zeros. It does not assert that every zero of this counterexample lies in that strip, nor that it shares the arithmetic theta coefficients of Ξ. A successful theorem would have to use additional specific properties; none has been proved here.

Next lemma: derive an unconditional growth bound and paired Hadamard product for Ξ, preserving the possibility of complex zeros, then inspect moment/zero identities.
