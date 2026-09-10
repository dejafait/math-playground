# Lemma 22: positive smooth superexponential kernels do not force real zeros

**Hypotheses.** On R let g(u)=exp(-cosh(2u)), h(u)=2g(u)+(g(u-4)+g(u+4))/2, and F(z)=∫_R h(u)e^{izu}du.

**Conclusion.** h is smooth, strictly positive, and even. It decays at least as fast as C exp(-c e^{2|u|}) for some C,c>0. F is entire and even, has positive imaginary-axis values and alternating even Taylor coefficients from positive moments, but has a zero z_0 with 0<Im(z_0)<1/2.

**Proof.** Positivity and smoothness are immediate, and evenness follows from that of g and the paired shifts. Since cosh(2v)≥e^{2|v|}/2 and |u±4|≥|u|-4, each shifted term is bounded by exp(-e^{-8}e^{2|u|}/2); one may take C=3 and c=e^{-8}/2. This majorant times e^{R|u|}|u|^k is integrable for every fixed R,k, so F is entire by dominated differentiation. The same is true for G(z)=∫_R g(u)e^{izu}du.

Real substitutions in absolutely convergent integrals give

F(z)=[2+(e^{4iz}+e^{-4iz})/2]G(z)=(2+cos(4z))G(z).

Let b=log(2+√3)>0. Since (2+√3)^{-1}=2-√3, cosh b=2. Also cosh 2>1+2=3>2 by its power series, so b<2 by strict monotonicity of cosh on (0,∞). Put z_0=(π+ib)/4. Then cos(4z_0)=cos(π+ib)=-cosh b=-2, so F(z_0)=0, and 0<Im(z_0)=b/4<1/2.

Evenness of h gives F(z)=2∫_0^∞h(u)cos(zu)du. The same dominated-series and cosh arguments as in Lemma 21 give the stated moment signs and positive imaginary-axis values. F is not identically zero because F(0)>0. This is a counterexample to the listed sufficient-condition guesses, not to RH or to a theorem using further arithmetic properties of K. ∎
