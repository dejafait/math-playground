# C019z — The full resonant numerator of the fixed real prime witness is negative

## Hypotheses

Use exactly C019y's fixed witness and definitions, with positive integers
d tending to infinity. In particular
\[
 d=\frac{T}{2\pi}(\log(T/(2\pi))-1),\quad T>2\pi e,
 \quad X=T/\sqrt{2d},\quad q=\log X,\quad B=(\sqrt2-1)X,
 \quad h=3\pi/q,
\]
\[
 J=[X,\sqrt2X],\quad D=[X,\sqrt2X-h],\quad
 L=\lfloor X^{1/1000}\rfloor,\quad \ell=\log L,\quad R=L^4.
\]
The real multiplicative coefficients alpha are those of the Euler-product
branch of zeta(s)^(-1/2) on Re(s)>1. Extend the original taper by
\(w(n)=(1-\log n/\ell)_+\) for all positive integers n; this does not
change any finite polynomial. Extend c by zero beyond R, where
\[
 c_s=\sum_{a_1a_2a_3a_4=s}
       \prod_{j=1}^4\alpha(a_j)w(a_j)\,(a_2a_4)^{-ih}.
                                                               \tag{1}
\]
This is the coefficient of H(Y)^2 with H=M(Y)M(Y+h), W=|H|^2.
Keep the original heat factors, at their own arguments,
\[
 t(Z)=Z^2/(2d),\quad u(Z)=\tfrac12\log(Z/(2\pi)),\quad
 N(Z)=\lfloor\sqrt{Z/(2\pi)+Z^2/(32d)}\rfloor,
\]
\[
 E_n(Z)=\exp\{t(Z)((u(Z)-\log n)^2-\pi^2/16)/4
                       +i\pi t(Z)(u(Z)-\log n)/8\}.
\]
Let \(\mathcal P=[\sqrt X/10,\sqrt X/5]\cap\{\text{primes}\}\).
For each unordered distinct pair p1<p2 in this set, write v=p1*p2 and
\[
 a_v(Y)=p_2^{-ih}E_{p_1}(Y)E_{p_2}(Y+h)
              +p_1^{-ih}E_{p_2}(Y)E_{p_1}(Y+h).
\]
Use C019y's grouped coefficients G and J, where J_(vs)=a_v*c_s
and other J entries vanish. All assertions below hold beyond one
absolute existential integer onset. The two resonant quantities are
\[
 \mathcal D_0=2\int_D\sum_k|J_k(Y)|^2/k\,dY,\qquad
 \mathcal N_0=2\operatorname{Re}\int_D
                       \sum_kG_k(Y)\overline{J_k(Y)}/k\,dY.
                                                               \tag{2}
\]
Neither is a replacement for its complete time integral. No assumption
on actual P, RH, nonvanishing, random laws or an ordinary-to-heat transfer
is added.

## Conclusion

Put \(K_1=\sum_{n\ge1}|c_n|^2/n\). Then K1 is comparable to ell^4,
and hence to q^4. There is an explicit absolute scalar I such that
\[
 \mathcal N_0=\frac{16K_1X}{q^2}(I+o(1)),\qquad
 \mathcal D_0=\frac{16K_1X}{q^2}
                  ((\sqrt2-1)(\log2)^2+o(1)),
 \qquad I<-\frac{19}{10000}.                              \tag{3}
\]
In particular, for absolute positive c,C,
\[
 -CBq^2\le\mathcal N_0\le-cBq^2,\qquad
 cBq^2\le\mathcal D_0\le CBq^2.                            \tag{4}
\]
This evaluates the entire zero-rational-frequency numerator, including
C019y (16), rather than another slice. C019y's selected dyadic slice
still has only O(Bq) numerator: its cancellation does not extend to the
whole resonant form.

The full fixed-witness quotient (N1) is still unresolved. Its signed
unequal-index terms, nonconjugate and mixed channels, full denominator
and actual-P residual remain exactly as in C019y (5). Neither a
cBq^2 lower bound nor an O(B) upper bound for (N1) follows from (3).
Independent conceptual audit1433 below retains (6)--(12) and the K1
norm order. Audit1435 below retains (13)--(21), including the original
moving floors and shifts, and the strict scalar bound in (3). Together
they validate (3)--(4) for the resonant quantities only.
POTENTIALLY_NEW denotes only lack of a matching theorem in the reused
assessment1409, not certified originality or a claimed RH advance.

## Proof

### 1. All source assignments on the witness support

The defining scales give d comparable to X^2*q^2 and ell asymptotic
to q/1000. For completeness, writing lambda=log(T/(2*pi)) gives
X^2=2*pi^2*exp(lambda)/(lambda-1), q~lambda/2, and
d/X^2=(lambda-1)^2/(2*pi^2). Thus t(Z)=O(q^(-2)) uniformly on J.
Writing N_*=N(sqrt(2)X), we have
\[
 N_*^2\le\frac{\sqrt2 X}{2\pi}+O(q^{-2})<X/4
                                                               \tag{5}
\]
eventually, since 2*sqrt(2)<pi. Also every witness prime exceeds R,
lies below N(X), and each v exceeds N_*, by the same strict scale
gaps as in C019x. In a factorization m*n*r=v*s with s<=R and r<=R,
neither large prime can enter r or s, and the two large primes cannot
enter the same source. They must therefore occupy distinct sources.
Each source is a witness prime times a positive integer less than 5,
by (5) and p>=sqrt(X)/10. Consequently every assignment is of one
of the following two forms, with a,b in {1,2,3,4} and ab dividing s:
\[
 (m,n,r)=(ap_1,bp_2,s/(ab)),\quad(ap_2,bp_1,s/(ab)).
\]
There are no other assignments, including for nonsquarefree s.

Set i_(a,p)(Z)=1 if ap<=N(Z), and zero otherwise, and define
\[
 T_{ab}(v,Y)=(bp_2)^{-ih}E_{ap_1}(Y)E_{bp_2}(Y+h)
                   i_{a,p_1}(Y)i_{b,p_2}(Y+h)
\]
\[
 \hspace{22mm}+(bp_1)^{-ih}E_{ap_2}(Y)E_{bp_1}(Y+h)
                   i_{a,p_2}(Y)i_{b,p_1}(Y+h).
\]
These indicators retain the true floors, including endpoint entries.
For each positive integer j put
\[
 K_j=\sum_{r\ge1}\frac{c_r\overline{c_{jr}}}{jr}.
                                                               \tag{6}
\]
All sums in (6) are finite by zero extension. The complete grouping is
\[
 G_{vs}=\sum_{a,b\le4;\ ab\mid s}c_{s/(ab)}T_{ab}(v,Y),
\]
\[
 \mathcal N_0=2\operatorname{Re}\int_D
       \sum_v\frac{\overline{a_v(Y)}}v
                    \sum_{a,b\le4}T_{ab}(v,Y)K_{ab}\,dY.
                                                               \tag{7}
\]
Uniqueness of v*s on the witness support follows from the two large
primes exceeding R. The only j needed are 1,2,3,4,6,8,9,12,16.
Equation (7) retains all of (2), not merely the r used by C019y.

### 2. Remove primes 2 and 3 with a paid taper error

C019p proves (|alpha|*|alpha|)(n)<=1; its fourfold version is
therefore bounded by tau(n). In particular |c_n|<=tau(n). Also
tau(n)^2<=d4(n): on a prime power of exponent e the difference between
binomial(e+3,3) and (e+1)^2 is (e+1)e(e-1)/6>=0. Expanding four
finite harmonic sums gives
\[
 \sum_{n\le R}\frac{\tau(n)^2}{n}
 \le\sum_{n\le R}\frac{d_4(n)}n\le(1+\log R)^4=O(\ell^4).
                                                               \tag{8}
\]
C019x (9), using squarefree integers with primes >11 and at most
sqrt(L), supplies the matching positive lower bound for K1.
Thus K1 is comparable to ell^4. These are finite coefficient facts;
no reciprocal on the critical line is used.

Write n=2^e*3^f*r, with gcd(r,6)=1. Put w_p=p^(-ih) and let
lambda_(p,j) be the coefficients of
\[
 (1-z)(1-w_pz):\qquad
 \lambda_{p,0}=1,\quad\lambda_{p,1}=-(1+w_p),\quad
 \lambda_{p,2}=w_p,\quad\lambda_{p,j}=0\ (j>2).
\]
Define an auxiliary finitely supported array, on all positive integers,
\[
 \widetilde c_{2^e3^fr}=\lambda_{2,e}\lambda_{3,f}c_r
                      \quad((r,6)=1).
\]
Its support can extend to 36R; no boundary entries are deleted. We claim
\[
 \sum_{n\ge1}|c_n-\widetilde c_n|^2/n=O(\ell^2).           \tag{9}
\]

To see this directly, expand (1), separating each factor into its
2-power, 3-power and coprime-to-6 part. Replace just the four tapers
w(2^(e_j)3^(f_j)r_j) by w(r_j). The resulting sum is exactly
tilde(c): the local coefficient series for the two unshifted and two
shifted alpha factors is
(1-z)^(1/2)*(1-z)^(1/2)*(1-w_p z)^(1/2)*(1-w_p z)^(1/2)
=(1-z)(1-w_p z), as a coefficient identity. This uses the same
binomial expansion as C019p, not an infinite evaluated mollifier.

All taper values are in [0,1]. Their positive-part definition is
Lipschitz in log(n), so telescoping the four products bounds their
difference by (e*log2+f*log3)/ell. If any r_j>L, both products vanish;
only r<=R needs consideration. Taking absolute coefficient sums, the
fourfold alpha convolution at 2^e is at most e+1, at 3^f at most f+1,
and at r at most tau(r). Hence
\[
 |c_{2^e3^fr}-\widetilde c_{2^e3^fr}|
 \le\frac{e\log2+f\log3}{\ell}(e+1)(f+1)\tau(r)
                         \mathbf1_{r\le R}.              \tag{10}
\]
Squaring (10), dividing by 2^e*3^f*r, and using (8) proves (9):
the remaining double series of a fixed polynomial in e,f against
2^(-e)3^(-f) converges. This also pays terms with n>R where c_n=0.
The coefficient series invoked for a fixed exponent are finite;
the positive majorant series just used is absolutely convergent.

For any two arrays x,y in the weighted norm ||x||^2=sum|x_n|^2/n,
Cauchy–Schwarz gives
\[
 \left|\sum_nx_n\overline{y_{jn}}/(jn)\right|
                       \le j^{-1/2}\|x\|\|y\|.
\]
Together with (8),(9) and the triangle inequality, this shows that
replacing both c's in any fixed K_j by tilde(c) costs O(ell^3).
Thus the upper boundary r<=R/j in the original correlation is paid,
even though the comparison array has a different finite support.

For j=2^a*3^b, the comparison correlation factorizes exactly as
\[
 \widetilde K_j=H_*U_a(2,h)U_b(3,h),\quad
 H_*=\sum_{(r,6)=1}|c_r|^2/r,
\]
\[
 U_a(p,h)=\sum_{e\ge0}\lambda_{p,e}
                          \overline{\lambda_{p,e+a}}/p^{e+a}.
\]
In particular
\[
 U_0=1+|1+w_p|^2/p+1/p^2,\quad
 U_1=-(1+\overline w_p)(p^{-1}+p^{-2}),\quad
 U_2=\overline w_p/p^2,\quad U_a=0\ (a>2).                \tag{11}
\]
Since U0>=1, the replacement error for K1 also permits normalizing
by U0(2,h)U0(3,h). Here h=O(ell^(-1)), so replacing the fixed local
factors in (11) by their h=0 values costs O(h*K1)=O(ell^3).
It follows that, simultaneously for the nine required j,
\[
 K_j=\rho(j)K_1+O(\ell^3),                               \tag{12}
\]
with an absolute complex error. The real constants rho are multiplicative
on the 2- and 3-parts, and their values on the needed indices are
\[
\begin{array}{c|rrrrrrrrr}
j&1&2&3&4&6&8&9&12&16\\ \hline
\rho(j)&1&-6/13&-4/11&1/13&24/143&0&1/22&-4/143&0.
\end{array}
\]
For example U0(2,0)=13/4 and U0(3,0)=22/9, which verify the
fractions directly. The original taper and shift have been estimated,
not silently replaced by an Euler product.

### 3. Keep the entries and integrate the source-prime masses

Uniformly for p in P, a<=4, and Z in J, ap/sqrt(X) lies in [1/10,4/5].
Thus u(Z)-log(ap)=O(1), E_(ap)(Z)=1+O(q^(-2)), and
(ap)^(-ih)=i+O(q^(-1)). These estimates remain valid before entry;
all entry indicators in (7) are retained. They give
a_v=2i+O(q^(-1)) and
T_ab=i*(i_(a,p1)(Y)i_(b,p2)(Y+h)+i_(a,p2)(Y)i_(b,p1)(Y+h))
plus O(q^(-1)) times the same nonnegative indicator sum.

Put
\[
 P_a(Z)=\sum_{p\in\mathcal P;\ ap\le N(Z)}1/p.
\]
We use only the same prime number theorem already assessed and used
in C019x/y: pi(t)~t/log(t), Hadamard and de la Vallee Poussin (1896),
as precisely stated in [NIST DLMF 27.12.4](https://dlmf.nist.gov/27.12.E4).
Partial summation on fixed proportional intervals of sqrt(X) gives
P1=O(1/q). All estimates here use this standard qualitative PNT;
no short-interval, arithmetic-progression or RH-strength error is needed.
The sum of 1/p^2 over P is O(X^(-1/2)/q).

For each a,b, summing the two orientations over p1<p2 gives exactly
P_a(Y)P_b(Y+h) minus the same-prime terms. Those omitted terms have
total O(X^(-1/2)/q), uniformly. Using (12) and the preceding heat/phase
bounds in (7) therefore yields
\[
 \mathcal N_0=4K_1\int_D\sum_{a,b\le4}
                  \rho(ab)P_a(Y)P_b(Y+h)\,dY+O(Bq).
                                                               \tag{13}
\]
Indeed the heat/phase replacement costs at most
O(B*K1/q^3)=O(Bq), the correlation replacement costs
O(B*ell^3/q^2)=O(Bq), and the removed same-prime terms cost
O(B*K1/(sqrt(X)*q))=o(Bq). The finite number of a,b values is
absorbed in the constants. No positivity of N0 was assumed.
Similarly the exact denominator resonance in (2) satisfies
\[
 \mathcal D_0=4K_1|D|P_1^2+O(Bq),                         \tag{14}
\]
because all original witness primes have entered at both times.

To specialize PNT with the true floors, set x=Y/X and
kappa(x)=sqrt(x/(2*pi)). Uniformly for x in [1,sqrt(2)],
N(Y)/sqrt(X)=kappa(x)+o(1), and the same holds for N(Y+h)/sqrt(X).
This follows directly from the formula for N: the floor changes its
ratio by at most X^(-1/2), and Y^2/(32dX)=O(1/(Xq^2)). PNT and
partial summation, uniformly over the compact range of endpoints,
then give
\[
 P_a(Y)=\frac2q u_a(x)+o(q^{-1}),\quad
 P_a(Y+h)=\frac2q u_a(x)+o(q^{-1}),
\]
\[
 u_a(x)=\bigl[\log(\min(2,10\kappa(x)/a))\bigr]_+.
                                                               \tag{15}
\]
To justify the uniformity explicitly, pi(t)/(t/log(t)) tends uniformly
to one for t in any fixed positive compact multiple of sqrt(X).
In the partial-summation formula for sum 1/p this gives a uniform
o(1/q) error; log(t)=q/2+O(1) gives the displayed leading logarithm.
Clipping an endpoint to the source interval and changing open to closed
endpoints costs at most O(X^(-1/2)). The uniform o(1) cutoff error
changes the continuous clipped logarithm by o(1). This covers both
multiplier-entry transitions and the shifted floor without differentiating
or deleting either floor.

Now u1=log2 throughout this interval. Define
\[
 f(x)=\sum_{a,b\le4}\rho(ab)u_a(x)u_b(x),\qquad
 I=\int_1^{\sqrt2}f(x)\,dx.                              \tag{16}
\]
Substitution of (15) in (13),(14), and |D|/X tending to sqrt(2)-1,
proves the two asymptotic formulas in (3). The last endpoint segment
has length h/X tending to zero and bounded f. Uniform errors are
sufficient; no exchange with an uncontrolled infinite sum occurs.

### 4. A rigorous negative sign for the scalar integral

Here is an elementary interval proof, including reproducible exact
arithmetic. Set A=log2, delta=log(4/3), x0=8*pi/25, and
epsilon=(1/2)log(x/x0). One has 1<x0<101/100. For 1<=x<=x0,
u1=A, u2=A+epsilon, u3=delta+epsilon, u4=0, and
epsilon lies in [-1/200,0], since log(x0)<x0-1<1/100.
The table in (12) gives exactly
\[
 f(x)=f_0+\epsilon\frac{-166A+61\delta}{143}
                    +\frac{131}{286}\epsilon^2,
 \quad f_0=\frac2{13}A^2-\frac{56}{143}A\delta
                                  +\frac1{22}\delta^2.    \tag{17}
\]
For x>=x0, put b=delta+epsilon; then u2=A, u3=b, u4=b-delta, and
\[
 f(x)=\frac2{13}A(A-\delta)
             +\frac{-68A+16\delta}{286}b-\frac3{286}b^2.
                                                               \tag{18}
\]
The following rational inequalities suffice:
\[
 f_0<0,\quad -68A+16\delta<0,\quad
 \sup_{-1/200\le e\le0}
       \{f_0+e(-166A+61\delta)/143+131e^2/286\}<1/100,
\]
\[
 f(6/5)<-1/100.                                           \tag{19}
\]
For transparency they can be checked from the enclosures
\[
 0.693147180559\le A\le0.693147180560,\qquad
 0.287682072451\le\delta\le0.287682072452,
\]
\[
 3.141592653589\le\pi\le3.141592653590,
\quad
 0.376195049517\le b(6/5)\le0.376195049519.
                                                               \tag{20}
\]
All decimals in (20) are exact rationals, not floating-point premises.
For a reproducible derivation, use Machin's identity
pi=16*arctan(1/5)-4*arctan(1/239). It follows from the tangent
addition formula and the angle in (0,pi/2), so the branch is fixed.
Twenty terms of each alternating arctangent series enclose the value
between the partial sum and the partial sum plus its next term.
For any rational z>=1, set v=(z-1)/(z+1). The identity
\[
 \log z=2\sum_{k=0}^{31}\frac{v^{2k+1}}{2k+1}+E,
 \quad 0\le E\le\frac{2v^{65}}{65(1-v^2)}               \tag{21}
\]
follows by integrating the geometric series, with its positive tail
bounded termwise. Apply it to 2, 4/3, and the enclosing rational
endpoints of 15/(4*pi); b(6/5)=delta+(1/2)log(15/(4*pi)). Outward
rounding to the grid 10^(-12) yields (20).

The exact Fraction script
`python3 scripts/jensen-pair-moment/resonant-scalar-sign-1413.py`
implements only these series, outward rational rounding and interval
arithmetic. Its complete selected enclosures and eight Boolean checks
are saved in
`scripts/jensen-pair-moment/resonant-scalar-sign-certificate-1413.json`.
They were inspected in full, not inferred from a preview. In particular
its upper enclosures give f0<-0.0004113, the early supremum<0.003010,
and f(6/5)<-0.0141905; these looser decimal inequalities are also exact
rational comparisons. No zeta sampling enters the certificate.

The derivative of (18) with respect to b is negative for b>=delta>0
by (19), and b increases with x. Thus f<0 on [x0,sqrt(2)], and
f<-1/100 on [6/5,sqrt(2)]. On [1,x0] use f<1/100. Since x0-1<1/100
and sqrt(2)>7/5, integration gives
\[
 I<\frac1{10000}-\frac1{100}\frac15=-\frac{19}{10000}.
\]
This proves (3),(4). The constants are absolute and independent of d.

### 5. What this does and does not pay

C019y (5) remains the exact continuation:
\[
 \mathcal N_P=\mathcal N_0+\mathcal O(G,J)
       +2\operatorname{Re}\int_DW^2(UA+CA+C\overline A)+\mathcal E_P,
\]
\[
 \mathcal D=\mathcal D_0+\mathcal O(J,J)
                              +2\operatorname{Re}\int_DW^2A^2.
\]
The objects U,C,A and the residual E_P have precisely their definitions
there. Equations (3),(4) give no sign or size estimate for these other
terms. The resonant numerator's negative sign is relevant because the
full numerator is squared in (N1), but it cannot survive an unpaid
signed remainder by assertion. In particular D>=D0 is not assumed.
The actual-P transfer from C019t remains unaudited and, if invoked,
retains all its C019j/k/l/s, L320 and L018/L021 contracts. It is not
used here. No all-degree positivity, M2 obstruction or RH conclusion
has been established.

This bounded attempt uses the unchanged assessed finite-sum target.
The explicit taper-error argument is necessary because an untapered
Euler-product correlation does not justify (12) for the four original
truncations. The fixed-interval PNT specialization is justified above;
it is an import, not a new number-theoretic discovery. The scalar
certificate proves only the sign of the displayed limiting integral.

### Independent conceptual audit1433 — 18 November 2026

Under unchanged SPECIALIZE coverage1431/1432, this audit retains
(6)--(12), including the norm order and all nine correlation constants.
It finds no mathematical error requiring repair in that reduction.
This is a local correctness audit/reproduction, not a stronger bound
or a novelty claim. It does not validate Sections 3--5, the scalar
certificate, or any full time-integral consequence.

**Identical definitions and scales.** C019y (1), C019x (7), and (1)
here have the same four ordered factors, the same two shifted factors,
and the same taper. Positive-part extension adds only zero terms;
in particular w(L)=0. Writing lambda=log(T/(2*pi)) gives
d=e^lambda(lambda-1) and X^2=2*pi^2*e^lambda/(lambda-1).
Thus X tends to infinity along the prescribed positive integers d,
ell~q/1000, and ell<=q/1000. Eventually ell>=1, and
h=3*pi/q<=3*pi/(1000*ell). No assertion is uniform in a variable
taper exponent: 1/1000 remains fixed.

The lower norm input is precisely audited C019x (9), in the explicit
form C019x (15). Its squarefree r<=floor(sqrt L) have primes >11,
so they are included both in K1 and in H_*. Its common-sector bound
uses h*log r<=3*pi/2000 and all four tapers at least 1/2, which
hold unchanged here. It yields
K1>=c_0*ell^4/(1024*81), with the fixed c_0>0 of C019x (3).
Only that coefficient result is used, not C019x's heat/source-prime
lower bound or its PNT input.

For the upper norm, put A=|alpha| and g=A*A, with Dirichlet
convolution. C019p's audited finite coefficient argument gives
0<=g(n)<=1. Hence A*A*A*A=g*g<=1*1=tau pointwise. The unit phases
and tapers in [0,1] imply |c_n|<=tau(n). Multiplicativity and
(e+1)^2<=binomial(e+3,3) give tau(n)^2<=d_4(n).
For R=L^4, expanding the fourfold convolution and then dropping its
product cutoff gives sum_(n<=R) d_4(n)/n<=H_R^4<= (1+4ell)^4.
This verifies (8) and K1 comparable to ell^4, hence to q^4, without
an untapered reciprocal or an infinite Euler product at s=1.

**Exact grouping (6)--(7).** The scale calculation preceding (5)
gives N_*<sqrt X/2 eventually. Every witness prime is >R and
<=N(X), while v>=X/100>N_*. In m*n*r=v*s with r,s<=R, each large
prime must divide a source and cannot divide r or s. Both cannot
divide the same source. Thus m,n are ap1,bp2 or ap2,bp1 with
a,b<5, and a*b*r=s. These exhaust all assignments even when s is
not squarefree. Their exact own-time indicators and phases are
exactly T_ab. Also v*s determines v and s uniquely because the
witness primes exceed R. In the finite numerator (2), substitute
J_vs=a_v*c_s and then set s=ab*r. The factor 1/(v*s) becomes
1/(v*ab*r), yielding exactly K_ab as defined in (6), with the
conjugation on c_(ab*r). This proves (7) without an infinite-sum
interchange or a replacement of the original upper boundary.

**Prime extraction on the whole support.** For a fixed n=2^e3^f r
with (r,6)=1, each ordered factor has a unique decomposition
a_i=2^(e_i)3^(f_i)r_i. Multiplicativity separates the alpha factors;
the shifted phases separate as
2^(-ih(e_2+e_4))*3^(-ih(f_2+f_4))*(r_2*r_4)^(-ih).
After replacing only w(a_i) by w(r_i), summing the finite exponent
compositions at each prime gives lambda_(2,e)lambda_(3,f)c_r.
The binomial identity used here is the standard generalized binomial
series, NIST DLMF [4.6.7](https://dlmf.nist.gov/4.6.E7), |z|<1;
the zeta Euler product on Re(s)>1 is
[27.4.3](https://dlmf.nist.gov/27.4.E3). These supporting identities
were inspected in source review1432 and are imported without reproof.
Equality of their coefficients is sufficient: each selected coefficient
uses only finitely many terms. Neither identity is evaluated at a
critical-line reciprocal. The remaining coprime coefficient is the
original c_r because each divisor of r is coprime to 6.

Both taper products vanish if some r_i>L. Otherwise their difference
is bounded by the sum of their four individual differences, since
every factor lies in [0,1]. The map x -> (1-x/ell)_+ is 1/ell-Lipschitz
on x>=0, giving precisely (e*log2+f*log3)/ell. If r>R, every
factorization r=r_1*r_2*r_3*r_4 has an r_i>L, so its difference
vanishes. Applying the absolute fourfold convolution bound separately
to 2^e, 3^f and r gives (10) for every e,f>=0 and every coprime r.
No restriction n<=R has been imposed in this argument.

In particular, writing
\[
 S=\sum_{e,f\ge0}
 (e\log2+f\log3)^2(e+1)^2(f+1)^2\,2^{-e}3^{-f},
\]
we obtain the complete bound
\[
 \|c-\widetilde c\|^2
 \le S\ell^{-2}(1+4\ell)^4\le625S\ell^2
 \quad(\ell\ge1),\qquad \|x\|^2=\sum_{n\ge1}|x_n|^2/n.
\]
S is finite: expand the squared linear factor into three terms;
each separates into products of sums of nonnegative polynomial
coefficients times 2^(-e) or 3^(-f), converging by the ratio test.
This proves (9), including all n>R. The comparison has no entries
beyond 36R because its local coefficients vanish for e>2 or f>2;
its potentially nonzero entries in (R,36R] remain in this norm.

**Two-array replacement and normalization.** For
B_j(x,y)=sum_n x_n*conjugate(y_(jn))/(jn), finite Cauchy--Schwarz
gives |B_j(x,y)|<=j^(-1/2)||x||||y||: the first squared sum is
||x||^2/j and the second is a sub-sum of ||y||^2. Consequently
\[
 |B_j(c,c)-B_j(\widetilde c,\widetilde c)|
 \le j^{-1/2}\|c-\widetilde c\|(\|c\|+\|\widetilde c\|)
 =O(\ell^3).
\]
Here ||c||=O(ell^2), ||c-tilde(c)||=O(ell), and the triangle
inequality bounds ||tilde(c)||. The full array is used on both
sides; hence this estimate pays the original r<=R/j boundary and
the extra comparison support simultaneously. It is uniform over
the nine required fixed j (indeed the displayed bound has j^(-1/2)).

For j=2^a3^b, unique factorization now gives exactly
tilde(K)_j=H_*U_a(2,h)U_b(3,h). Direct multiplication of the
three local coefficients yields (11); in particular
lambda_1*conjugate(lambda_2)=-(1+conjugate(w_p)), which checks
the phase in the second contribution to U_1. Put
D_h=U_0(2,h)U_0(3,h)>=1. Applying the same replacement at j=1
gives H_*=(K1+O(ell^3))/D_h. Since all relevant U_a are bounded
by absolute constants for real h, it follows that
\[
 K_j=K1\frac{U_a(2,h)U_b(3,h)}{D_h}+O(\ell^3).
\]
Each numerator and denominator is a fixed polynomial in p^(ih)
and p^(-ih), for p=2,3. Its derivative in real h is bounded;
D_h>=1 also bounds the derivative of its reciprocal. Thus the
ratio differs from its h=0 value by O(|h|). Multiplication by
K1=O(ell^4), with h=O(ell^(-1)), costs O(ell^3) as claimed.
No unproved lower bound for a signed correlation is used to divide.

At h=0 the local triples (U_0,U_1,U_2) are
(13/4,-3/2,1/4) at 2 and (22/9,-8/9,1/9) at 3. Dividing gives
(1,-6/13,1/13) and (1,-4/11,1/22), respectively; higher entries
vanish. Their products give, in the order j=1,2,3,4,6,8,9,12,16,
exactly (1,-6/13,-4/11,1/13,24/143,0,1/22,-4/143,0).
In particular the vanishing leading terms at 8 and 16 mean
K_j=O(ell^3), not exact vanishing of the original tapered correlations.
This completes the audit of (12) for every required j, with an
absolute complex error and a common existential integer onset.

The audit validates an input to the resonant numerator calculation,
not its subsequent prime-mass limit or negative sign. The other
channels, full denominator, actual-P error and Xi transfer remain
unresolved. The exhausted joint-completion route is not reopened.

### Independent conceptual audit1435 — 18 November 2026

This audit uses the unchanged integer-d hypotheses, the coefficient
identities and bounds retained by audit1433, and the precise supporting
sources assessed in nomination1433/source-notes1434. It reproduces the
local specialization in (13)--(21); it supplies neither a stronger PNT
nor an estimate for a full time integral. No repair to these formulas
is required. The details below also explain why the saved certificate's
weaker final comparison does not by itself prove the strict bound.

**Scales, heat factors and phases.** Write lambda=log(T/(2pi)). The
exact identities preceding (5) give

    q=lambda/2-(1/2)log(lambda-1)+(1/2)log(2pi^2),
    d/X^2=(lambda-1)^2/(2pi^2),   ell~q/1000.

Thus q tends to infinity along the stipulated integers d, and
t(Z)=O(q^-2) on J. For each of the finitely many a<=4 and each
witness prime p, log(ap)=q/2+log(ap/sqrt X), with the second term
bounded uniformly. Also u(Z)=q/2+(1/2)log((Z/X)/(2pi)). Therefore the
entire complex exponent defining E_(ap)(Z) is O(q^-2), whether or not
ap has entered. The elementary bound |exp(z)-1|<=|z|exp(|z|) gives
E_(ap)(Z)=1+O(q^-2) in modulus. Since h=3pi/q,

    (ap)^(-ih)=exp(-3pi i/2)exp(-ih log(ap/sqrt X))
              =i+O(q^-1).

Both own heat times are retained, since Y,Y+h belong to J for Y in D.
The expansions for a_v and T_ab before (13) follow, with the latter's
error bounded by C/q times its indicator sum. In particular an absent
orientation contributes exactly zero, including at each floor jump.

**Pair counting and error scales.** Put

    S_ab(Y)=sum_(p<r in P) [i_(a,p)(Y)i_(b,r)(Y+h)
                           +i_(a,r)(Y)i_(b,p)(Y+h)]/(pr),
    Q_ab(Y)=sum_(p in P) i_(a,p)(Y)i_(b,p)(Y+h)/p^2.

Every ordered unequal prime pair occurs exactly once in S_ab, so
S_ab=P_a(Y)P_b(Y+h)-Q_ab, also for a=b. PNT on this fixed proportional
interval gives P_1=O(q^-1) and #P=O(sqrt X/q). Consequently
0<=Q_ab<=sum_P p^-2=O(1/(sqrt X q)) and S_ab=O(q^-2).
The product conjugate(a_v)T_ab is twice its indicator sum with complex
error O(q^-1) times that sum. Taking 2Re in (7), and then using (12),
gives the coefficient 4 in (13). Absolute errors, without any presumed
sign cancellation, are bounded by constants times

    B K1/q^3,   B ell^3/q^2,   B K1/(sqrt X q).

The first two are O(Bq); the third divided by Bq is O(q^2/sqrt X),
which tends to zero. This also pays a possibly complex error in K_ab.
All constants are uniform in a,b and in the stipulated integers d.

For the denominator, uniqueness of the v*s representation, already
checked in audit1433, gives exactly

    D0=2K1 integral_D sum_(p<r) |a_(pr)(Y)|^2/(pr) dY.

Here |a_v|^2=4+O(q^-1), and
sum_(p<r)1/(pr)=(P_1^2-sum_P p^-2)/2. Every witness prime is at most
sqrt X/5, while N(X)/sqrt X tends to 1/sqrt(2pi)>1/5. Hence every
witness prime has entered at both times for all sufficiently large d;
P_1 is constant in Y in this paragraph. The same three bounds above
(with no correlation replacement needed) give exactly (14), including
the removed diagonal p=r. No inequality D>=D0 has been used.

**Uniform clipped prime masses.** Import the ordinary unconditional
prime number theorem pi(t)~t/log t in NIST DLMF 27.12.4,
https://dlmf.nist.gov/27.12.E4 . Import real-endpoint Abel partial
summation in Granville--Soundararajan, *Multiplicative number theory:
The pretentious approach*, author-hosted 2014 draft, Section 1.1.1,
(1.1.4)--(1.1.5), printed pp. 3--4,
https://dms.umontreal.ca/~andrew/PDF/Book.To2.5.pdf . The source formula
uses l<p<=y; an included lower endpoint is paid explicitly below.
The following is the needed specialization, not a reproof of either
named input.

Let H=sqrt X, l=H/10 and u=H/5, and let

    eta_X=sup_(l<=t<=u) |pi(t)log(t)/t-1|.

PNT implies eta_X tends to zero: its defining tail estimate holds
simultaneously for all t>=l. Uniformly for real l<=y<=u, Abel summation
with weight 1/t reads

    sum_(l<p<=y)1/p=pi(y)/y-pi(l)/l+integral_l^y pi(t)/t^2 dt.

Substitute pi(t)=t/log(t)*(1+O(eta_X)). Since log(t)=q/2+O(1),
the two main boundary terms differ by O(q^-2), their errors are
O(eta_X/q), and the integral is
(2/q)log(y/l)+O(q^-2+eta_X/q). These bounds are absolute and uniform
even when y-l tends to zero. Closing the lower endpoint adds at most
1/l=10/H. Thus the total uniform error is

    O(eta_X/q+q^-2+H^-1)=o(q^-1).

For any real cutoff c, clip it to [l,u]. If c<l, the clipped formula
can differ from the empty prime sum only by the possible atom at l;
if c>u it gives the full sum. Therefore the same absolute bound applies
uniformly through empty and saturated cases. There is no relative
short-interval estimate in this argument.

For Y=Xx in D, the exact floor formula gives

    N(Y)/H=kappa(x)+O(H^-1+(Xq^2)^-1).

The floor term is at most H^-1. The heat correction inside the normalized
square root is Y^2/(32dX)=O((Xq^2)^-1); the square root is Lipschitz
on this positive compact range. At Y+h the additional normalized
argument change is O(h/X), uniformly, so the same limit holds with
an additional O(h/X). Dividing by fixed a and clipping are Lipschitz
operations. The logarithm of the clipped ratio to 1/10 is also Lipschitz
on [1/10,1/5]. Substituting c=N(Y)/a and c=N(Y+h)/a in the preceding
prime-mass estimate proves both formulas (15), with a uniform absolute
o(q^-1). It retains the exact original floors and both shifts until
their errors have been bounded. In particular no differentiability of
an entry indicator is required at either transition.

Each product P_a(Y)P_b(Y+h) is now
4u_a(x)u_b(x)/q^2+o(q^-2), uniformly. Dividing the O(Bq) in (13),(14)
by K1 X/q^2 leaves O(q^-1), since K1 is comparable to q^4 and B/X is
constant. Also |D|=B-h exactly. The omitted scalar interval at the
right end has length h/X and a bounded integrand; its error after
normalization is O(h/X)=o(1). These facts prove the two asymptotic
identities in (3), with I as defined in (16). This is a finite sum of
uniform estimates, with no unproved interchange of limiting measures.

**Piecewise scalar algebra.** The threshold for u2 to saturate and
for u4 to become nonzero is the same x0=8pi/25. On [1,sqrt2], u1=A
and 0<u3<A: the needed endpoint comparisons follow already from
3<pi<22/7 and sqrt2<3/2 (in particular 10kappa/3 stays strictly
between 1 and 2). Thus the two lists of u-values used in (17),(18)
exhaust the interval. Expanding the nine rho values, with symmetric
off-diagonal terms counted twice, gives exactly

    f=A^2-(12/13)A u2-(8/11)A u3+(2/13)A u4
        +(1/13)u2^2+(48/143)u2 u3+(1/22)u3^2-(8/143)u3 u4.

Substitution of (u2,u3,u4)=(A+epsilon,delta+epsilon,0) gives (17);
substitution of (A,b,b-delta) gives (18). The formulas agree at
epsilon=0, b=delta, where their value is f0. They therefore describe
a continuous scalar function at the common transition.

**Exact enclosure method and replay.** The primary supporting formulas
are DLMF 4.24.3 (arctangent series), https://dlmf.nist.gov/4.24.E3 ,
and 4.6.4 (logarithm series), https://dlmf.nist.gov/4.6.E4 . The named
Machin identity with principal real arctangents is also recorded in
Rycroft, Harvard AM205 Unit 0, slide 13,
https://people.math.wisc.edu/~chr/am205/slides/am205_unit0.pdf .
Alternating next-term bounds are OpenStax, *Calculus Volume 2*,
Section 5.5, Theorems 5.13--5.14,
https://openstax.org/books/calculus-volume-2/pages/5-5-alternating-series .
These standard inputs are reused, not claimed as discoveries.

At 1/5 and 1/239 the arctangent term magnitudes decrease to zero.
The 20-term sum ends with a negative term; the next term is positive.
Thus the script correctly brackets each arctangent by that sum and
the sum plus its next term. Interval multiplication by -4 reverses
the second bracket before the Machin combination. For z>=1, v lies
in [0,1), and the omitted log series starts with exponent 65 and
denominator 65. Bounding all later denominators below by 65 gives
precisely the geometric remainder in (21), including v=0. The
arguments 2,4/3 and both endpoints of 15/(4pi) satisfy z>=1; the
last assertion follows from pi<15/4 in its rational enclosure.
Monotonicity of log and reversal of the positive reciprocal justify
using log(15/(4*pi.hi)).lo and log(15/(4*pi.lo)).hi. This gives the
stated interval for b(6/5), with delta's full interval added.

The script constructs all values from integer fractions. Its outward
rounding uses floor at the lower endpoint and ceiling at the upper
endpoint on the 10^-12 grid; the signed integer-division formulas
remain valid for negative arguments. Addition, negation and the
minimum/maximum of all four endpoint products preserve inclusion.
Occurrences of A,delta,b are allowed to vary independently in these
operations, enlarging rather than shrinking the enclosure. The early
epsilon^2 interval is [0,1/40000]; it is not a signed product bound
mistaken for a square.

Audit1435 executed the unchanged original script with only __file__
redirected to the separate directory scripts/jensen-pair-moment/audit-1435.
The replay certificate there is byte-identical to the original
resonant-scalar-sign-certificate-1413.json. All ten rational intervals
and all eight original checks were inspected in full. The full replay,
hashes, twelve additional/replay checks and exact thresholds are in
scripts/jensen-pair-moment/audit-1435/audit-checks-1435.json and the
adjacent replay certificate. The decisive exact upper endpoints are

    f0 <= -334229164038691247653/812500000000000000000000 < 0,
    early <= 26898893431027208775817/8937500000000000000000000 < 1/100,
    f(6/5) <= -4058487734011779843343367/286000000000000000000000000
            < -1/100,
    -68A+16delta <= -2126554755939/50000000000 < 0.

The same replay verifies 1<x0<101/100 and the looser decimal bounds
printed in the original proof. These are exact rational comparisons;
the script's floating-point displays are not premises.

**Strict integration and conclusion.** On [1,x0],
epsilon=(1/2)log(x/x0) lies in [-1/200,0], since log x0<x0-1<1/100.
The early interval bound proves f<1/100 there. On [x0,sqrt2], b>=delta>0
and d f/d b=(-68A+16delta-6b)/286<0, while d b/d x=1/(2x)>0.
Since f(x0)=f0<0, f<0 on this entire interval. At and after 6/5
the verified bound and monotonicity give f<-1/100. The exact partition
1<x0<6/5<7/5<sqrt2 therefore yields

    I < (x0-1)/100 - (sqrt2-6/5)/100
      < 1/10000 - (1/5)/100 = -19/10000.

The first strict inequality follows from integrating continuous strict
bounds on intervals of positive length, with the middle interval
having a strictly negative integral. The second also uses strict
x0-1<1/100 and sqrt2>7/5, the latter certified by (7/5)^2<2.
This supplies the strictness missing from the certificate's mere
comparison -19/10000<-1/1000. It proves the requested scalar assertion,
not just the weaker certificate threshold.

The scalar integral is finite, the denominator's limiting constant
(sqrt2-1)(log2)^2 is positive, and K1 is comparable to q^4. The
asymptotics consequently imply both two-sided order bounds (4) beyond
one absolute existential integer onset. This closes the independent
audit of the resonant claim only. Unequal-frequency and other channels,
the full denominator, E_P and actual-Xi transfer remain unbounded by
this audit; the exhausted joint-completion stop1431 remains in force.

## Mathlib

Full matching coverage is not checked; no absence assertion is made.
Unique factorization, finite Dirichlet convolution, Cauchy–Schwarz,
binomial coefficient algebra and elementary log/arctangent series are
supporting ingredients, not a verified formal theorem for this witness.
PNT is imported by the precise DLMF statement cited above, under its
ordinary unconditional hypotheses. Neither that theorem nor the rational
certificate formalizes the moving-floor and tapered-coefficient proof.
Audit1433 does not change that coverage status: it checks the finite
coefficient argument informally and performs no Mathlib lookup or
formal verification.
Audit1435 likewise performs no Mathlib lookup or formal verification.
Its PNT/Abel specialization and exact scalar audit establish informal
coverage of (13)--(21), not a full matching Mathlib theorem.
