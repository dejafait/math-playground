# C020k — The original full Gallagher energy exceeds its sufficient scale

## Hypotheses

Use exactly C020i's original integer-d witness, complete coefficients,
support N=Z_*, frozen heat factors, intervals and energy E(Y0).
In particular d tends through positive integers, T>2pi e solves

\[
d=\frac{T}{2\pi}(\log(T/(2\pi))-1),\quad
X=T/\sqrt{2d},\quad q=\log X,\quad
L=\lfloor X^{1/1000}\rfloor,\quad\ell=\log L,
\]
\[
h=3\pi/q,\quad B=(\sqrt2-1)X,\quad
D=[X,\sqrt2X-h],\quad U=(B-h)/2,\quad Y_c=\operatorname{midpoint}(D).
\]

The real coefficients alpha(n) are those of the Euler-product branch
of zeta(s)^(-1/2) on Re(s)>1, positively normalized on real s>1.
Retain the original taper and both shifted factors:

\[
M(t)=\sum_{n\le L}\alpha(n)\frac{\log(L/n)}{\ell}n^{-1/2-it},
\quad M(t)^2M(t+h)^2=\sum_{s\le L^4}c_s s^{-1/2-it}.
\]

For every unordered distinct witness-prime pair p<r in
[sqrt(X)/10,sqrt(X)/5], v=pr and J_(vs)(Y0)=a_v(Y0)c_s
with exactly the a_v of C020i (2); all other entries are zero.
The heat times are Y0 and Y0+h. No coefficient is replaced or omitted.
Thus the energy and low-height integral are precisely

\[
E(Y_0)=\int_0^\infty
 \left|\sum_{y<k\le ye^{1/U}}J_k(Y_0)k^{-1/2-iY_c}\right|^2\frac{dy}{y},
\qquad H_L=\int_{-1/10}^{1/10}|M(t)M(t+h)|^4dt.
\]

Use C020i and C020j, as retained by their conceptual audits1446.
All assertions are asymptotic with absolute constants and one
existential integer-d onset. No RH, critical-line reciprocal-series
continuation, actual-P estimate or moving-coefficient transfer is assumed.

## Conclusion

Put c0=25/(29sqrt(pi)). For every sufficiently large prescribed integer d,

\[
H_L\ge\frac{c_0^8}{5}\frac{L^4}{\ell^{20}},\qquad
\frac{H_L}{q^6}\ge\frac{c_0^8}{5}\frac{L^4}{q^6\ell^{20}}
 \longrightarrow\infty.                                      \tag{1}
\]

There are absolute c,c'>0 such that, uniformly for all Y0 in D,

\[
E(Y_0)\ge c\frac{L^4}{Xq^4\ell^{20}},\qquad
\frac{E(Y_0)}{Bq^2/U^2}\ge c'\frac{L^4}{q^6\ell^{20}}
 \longrightarrow\infty.                                      \tag{2}
\]

Consequently the sufficient uniform O(Bq^2/U^2) whole-energy estimate
proposed in source-review1440 is false for this exact witness.
The result is local negative evidence about that sufficient estimate,
not a new discovery beyond the checked sources or a disproof of RH.
The full high-height frozen norm, moving real denominator, signed
numerator, E_P and actual-Xi transfer remain unresolved. The application
is REPRODUCTION under unchanged SPECIALIZE coverage1445; it has not
received a later independent audit.

## Proof

### One common integer-d onset and both shifted arguments

C020i's audited scale calculation gives q->infinity along all of
the stipulated integers d. Write Q=exp(q/1000)=X^(1/1000).
For Q>=2 the exact floor satisfies Q/2<=L<=Q. In particular
L tends to infinity and

\[
q/1000-\log2\le\ell\le q/1000.                            \tag{3}
\]

Let L0 be the single integer onset in C020j (2). Choose d large
enough that L>=L0 and q>=30pi. Then 0<h<=1/10, so every
t in [-1/10,1/10] has both t and t+h in [-1/5,1/5]. C020j
applies simultaneously to both factors of the same finite mollifier:

\[
|M(t)|\ge c_0\sqrt L\,\ell^{-5/2},\qquad
|M(t+h)|\ge c_0\sqrt L\,\ell^{-5/2}.                       \tag{4}
\]

The lower bound is uniform in t, h in the indicated range, and L
above L0. No moving heat parameter is involved in (4); the heat
factors remain in J and are paid uniformly by C020i. Taking the
maximum with C020i's onset makes all assertions hold for every Y0
in D and every integer d thereafter.

### Power comparison and the sufficient-energy stop

The product in (4) has modulus at least c0^2 L ell^(-5).
Raise to the fourth power and integrate over an interval of length
1/5. This proves the first inequality in (1), with exponent ell^(-20),
retaining all four original tapers. From (3), for all sufficiently
large q with ell>0,

\[
\frac{L^4}{q^6\ell^{20}}
 \ge\frac{1000^{20}}{16}\,
       \frac{\exp(q/250)}{q^{26}}\longrightarrow\infty.    \tag{5}
\]

For example the logarithm of the variable factor on the right is
q/250-26 log q, which tends to infinity. Thus this is divergence
along all sufficiently large prescribed integers, not a selected
continuous sequence or a numerical observation.

C020i (4) gives E(Y0)>=c H_L/(Xq^4) and
E(Y0)/(Bq^2/U^2)>=c' H_L/q^6 uniformly in Y0. Substituting (1)
proves (2). More explicitly, for every proposed absolute constant C,
(5) eventually makes E(Y0)>C Bq^2/U^2 for every Y0 in D.
This contradicts the proposed uniform sufficient bound.

The imported analytic inputs are precisely the compact-window
Plancherel theorem cited in C020i and the fixed rho=-1/2,H=0
Selberg--Delange expansion cited in C020j. Their specializations
were checked there; no stronger source estimate or reproof is used.
The present application only checks the shifted intervals, common
onset and comparison of growth rates.

### Scope of the failure

In C020i (6), all the mass used in (1) is at heights |t|<=1/10,
outside D for large d. Its translated sinc multiplier is nonzero
there. The whole energy therefore includes a contribution irrelevant
to the desired high-height integral. Gallagher provides an upper
bound of that integral by a constant times U^2 E; its direction
cannot be reversed. No lower bound or contradiction for the original
high-height norm, the real denominator or RH follows from (2).
Stops1407/1408/1437 and the exhausted completion1431 retain their
different scopes; this result closes only the hard-window whole-energy
estimate from1440.

## Mathlib

Full matching coverage for (1)--(2) has not been checked. Supporting
finite-sum, integral and elementary growth facts are not a verified
matching theorem for this witness. The two precise analytic imports
and their qualifications remain in C020i/C020j. No absence claim or
Lean verification is asserted, and no numerical certificate is needed.
