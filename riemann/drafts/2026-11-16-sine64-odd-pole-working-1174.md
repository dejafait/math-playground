# Odd-pole reserve working checkpoint1174

Approved target: test 2||Q sinh(x/2)||^2<1/8 on unchanged C750m QH.
Reused supplied assessment1173; C750m(2),(7) fixes complex normalization.
No changed support, projection, cutoff or full-loss retry.

In progress: for j=2k, direct integration gives
<s,phi_(2k)>=-2 alpha_k sinh(b/2)/(sqrt(b)(alpha_k^2+1/4)),
alpha_k=k*pi/b; odd-index coefficients vanish by parity.
Thus the required norm equals (8b sinh(b/2)^2/pi^2)
sum_(k>=33) k^2/(k^2+(b/(2pi))^2)^2 by Parseval.
Check the antiderivative, signs, complex rank-one norm and complete tail
in the canonical proof before reporting this as established.

Proposed exact bound: sum<sum_(k>=33)1/k^2<1/32,
b<7/3 from the degree8 positive exp(14/3) Taylor polynomial>101,
sinh(b/2)^2=(102/sqrt101-2)/4<41/20, pi>25/8.
The last inequality follows from 64 alternating arctan(1) terms,
using already assessed DLMF4.24.3 and the alternating-series remainder.
Exact rational certificate and final comparison remain to save.
No full signed multiplier, head/coupling, all-support or Xi sign follows.

Completed1174: canonical C750p proves the coefficient formula, complex
rank-one norm and complete k>=33 tail. Exact certificate at
scripts/sine64/odd-pole-reserve-1174.json passes all checks:
nu_odd<1148/9375=1/8-191/75000. Pending phrases above preserve the
pre-calculation checkpoint, not the final state. No parameter was retuned.
