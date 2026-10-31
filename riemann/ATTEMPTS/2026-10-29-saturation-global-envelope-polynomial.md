# Global-envelope saturation polynomial: length obstruction

The exact approved target was simultaneous uniform approximation to
error 1/8 on [0,B_T] of x/((log T)^A+x), for some fixed A>=0,
and J_T log(2J_T)=o(T) with J_T=M N^(3d_T). The full hypotheses,
classical source, proof and interpretation of this formal budget are
canonical in [L482](../lemmas/L482-global-envelope-saturation-polynomial-length-obstruction.md).

WHY IT FAILS: Markov's classical derivative inequality forces
d_T^2>=B_T/(9(log T)^A)>=N^3/(9(log T)^A), so the required degree
tends to infinity. With the specified N and M, already d_T>=4
gives J_T>=M N^12 asymptotic to T/sqrt(2pi); its logarithmic
length factor cannot be o(T). The budget allows only degrees
at most three eventually, including along arbitrary unbounded
sequences. This is a known-method specialization, not a new
approximation theorem or a disproof of the saturation correlation.

B_T bounds all amplitudes by the triangle inequality; the actual
range on [T,2T] need not fill the interval. Preserve that distinction
and all prior interpolation/termwise stops. Reopening requires a
materially changed implementation, such as a justified actual-height
weighted approximation, a different length argument or a different
class of functions. Such a changed target needs its own source
coverage; L482 supplies no signed correlation or weighted-tail bound.
