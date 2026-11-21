# Finite-taper specialization work1444

Approved target: the exact uniform M lower bound in assessment1443;
no energy application or C020i audit is part of this attempt.

Let ell=log L, s=1/2+it, z=1-s. Import (3.8) of de la
Breteche--Tenenbaum2021 at rho=-1/2, H=0:
A(x)=a0*x*(log x)^(-3/2)+O(x*(log x)^(-5/2)),
a0=1/Gamma(-1/2)=-1/(2 sqrt(pi)).

Exact Abel summation, including n=1 and the vanishing n=L weight,
gives M=ell^(-1) integral_1^L A(x)x^(-s-1)
*(1+s log(L/x)) dx. Split at sqrt(L). Since |alpha(n)|<=1,
the first integral is O(L^(1/4)) uniformly for |t|<=1/5.
In the second integral put v=log(L/x). Its main term is
a0 L^z/ell integral_0^(ell/2) exp(-zv)(ell-v)^(-3/2)(1+sv) dv.
Replace (ell-v)^(-3/2) by ell^(-3/2), with error
O(v ell^(-5/2)); the imported remainder costs
O(sqrt(L) ell^(-7/2)). Extend the resulting exponential integral
to infinity, incurring O(L^(1/4) ell^(-3/2)).
The integral equals 1/z+s/z^2=1/z^2.

Thus the candidate uniform asymptotic is
M(t)=L^(1/2-it) ell^(-5/2)
*[1/(Gamma(-1/2)(1/2-it)^2)+O(1/ell)].
The minimum main coefficient modulus is 50/(29 sqrt(pi));
half of it supplies a candidate absolute lower-bound constant.
Before promoting: write the complete coefficient bound, Abel endpoint
argument, uniform integral errors and existential onset in C020j.
No new arithmetic or reciprocal-series continuation is being assumed.

Completed: C020j contains the full proof of (1)--(2), including the
coefficient bound, exact Abel formula, uniform errors and one onset.
The target succeeded. No H_L bound or energy-stop application was
performed. The imported H=0 summatory expansion suffices; a higher
fixed expansion order is unnecessary for this finite-taper target.
