# Step256 working calculation — preserve before final write-up

Approved target: review254 exact two-endpoint cutoff/jump cost, H=exp(n).
Inputs: L985 exact K connection; L988 finite E definition; Gorodetsky
2211.08973v6 Lemma5.2 s=1 in canonical foundation; DLMF18.14.8.

Let A(x)=sum_(m<=x) Lambda(m)/m with full endpoint, J(x) equal
Lambda(x)/(2x) at a prime power and zero otherwise, V(x)=sum_(k>=1)
x^(-2k-1)/(2k+1). Source gives G_H(x)=log x-gamma_E+V(x)-A(x)+J(x)+R(x,H),
where G_H=sum_(|gamma|<=H)x^(rho-1)/(rho-1). Thus upper K times this
expression minus lower K times it equals the finite E sum exactly.

Global Laguerre bound gives |K_n(u)|<=2n exp(u/2), n>=2,u>=0.
Nearest-other prime power x' satisfies x'>=x/2: choose the power of2
below x, except use x/2 if x itself is a power of2. This candidate
is different from x and within x/2; hence every nearest choice is
within x/2. No clearance needed. Source s=1 remainder <=C[2log(x)/x
+log^2(xH)/H*(2+1/(2log x))], with absolute C.

At x=e^n,e^(2n), H=e^n: weighted source remainder <=C[
4n^2 e^(-n/2)+8n^2 e^(-n)+18n^3 e^(-n/2)+(81/2)n^3].
Half-jump magnitude <= n^2 e^(-n/2)+2n^2 e^(-n).
Total O(n^3)=o(e^(n/2)n^(-3/2)). Recheck algebra and exact signs in
canonical file. This is REPRODUCTION, not a signed arithmetic estimate.
Retain gamma_E,V,both prefixes,both K values including -1,analytic
multiplicities and closed cutoff. No infinite sum exchange or B_n identity.
