# Lemma 53: a differential equation for the comparison base transform

**Hypotheses.** Fix z∈C, set ν=z/2, and for real x≥0 define

Y_z(x)=∫_0^∞exp(-e^x cosh t)cos(νt)dt.

G(z)=∫_R exp(-cosh(2u))e^{izu}du as in Lemma 52.

**Conclusion.** Y_z is smooth, Y_z(0)=G(z), and

-Y_z''(x)+e^{2x}Y_z(x)=(z²/4)Y_z(x).

With r=e^x tending to infinity, Y_z(x)=O_z(e^{-r}), Y_z'(x)=O_z(e^{-r/2}), and sqrt(r)e^rY_z(x) tends to sqrt(π/2)>0. In particular Y_z is not identically zero.

**Proof.** Evenness of the g integral and t=2u give Y_z(0)=G(z). Any fixed x-derivative introduces only a polynomial in e^x cosh t, while the exponential exp(-e^x cosh t) dominates that polynomial times |cos(νt)|≤e^{|Im ν|t} on compact x-intervals. This justifies smooth differentiation. Write k(t)=e^{-r cosh t}. Direct differentiation gives

k_{xx}=(r²cosh²t-r cosh t)k,  k_{tt}=(r²sinh²t-r cosh t)k,

so k_{xx}-r²k=k_{tt}. Twice integrating k_{tt}cos(νt) by parts gives -ν²Y_z: at infinity the exponential dominates all boundary factors; at zero k_t(0)=0 and sin 0=0. This yields the stated equation.

Let B=|Im ν|. Since cosh t≥1+t²/2 and r≥1,

|Y_z(x)|≤e^{-r}∫_0^∞e^{-t²/2+Bt}dt=O_z(e^{-r}).

For the derivative use y e^{-y}≤2e^{-y/2}, y≥0, with y=r cosh t. The same Gaussian comparison bounds |Y_z'(x)| by a constant times e^{-r/2}. Finally set t=v/sqrt(r):

sqrt(r)e^rY_z(x)=∫_0^∞exp[-r(cosh(v/sqrt(r))-1)]cos(νv/sqrt(r))dv.

The integrand tends pointwise to e^{-v²/2} and has absolute value at most e^{-v²/2+Bv}, integrable and independent of r≥1. Dominated convergence gives the asserted nonzero limit, using the Gaussian integral. ∎
