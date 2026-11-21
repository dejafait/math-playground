# C020a — A positive coherent saddle subfamily outweighs the negative resonance

## Hypotheses

Use exactly C019y's fixed real witness, actual target and notation,
with positive integers d tending to infinity. In particular
\[
 d=\frac{T}{2\pi}(\log(T/(2\pi))-1),\quad T>2\pi e,\quad
 X=T/\sqrt{2d},\quad q=\log X,\quad B=(\sqrt2-1)X,\quad h=3\pi/q,
\]
\[
 D=[X,\sqrt2X-h],\quad L=\lfloor X^{1/1000}\rfloor,\quad R=L^4,
 \quad H=M(Y)M(Y+h),\quad W=|H|^2,
 \quad H^2=\sum_{s\le R}c_s s^{-1/2-iY}.
\]
M retains the real Euler-product coefficients of zeta(s)^(-1/2)
on Re(s)>1 and the four original linear tapers in H^2. Extend c by
zero beyond R. Keep the exact own-time factors and floors
\[
 t(Z)=Z^2/(2d),\quad u(Z)=\tfrac12\log(Z/(2\pi)),\quad
 E_n(Z)=\exp\{t(Z)((u(Z)-\log n)^2-\pi^2/16)/4
                   +i\pi t(Z)(u(Z)-\log n)/8\},
\]
\[
 N(Z)=\left\lfloor\sqrt{Z/(2\pi)+Z^2/(32d)}\right\rfloor,
 \quad N_*=N(\sqrt2X),\quad
 \theta(Z)=\tfrac Z2\log(Z/(2\pi))-\tfrac Z2-\pi/8.
\]
Let \(\mathcal P=[\sqrt X/10,\sqrt X/5]\cap\{\text{primes}\}\).
For distinct p,b in P set
\[
 a_{pb}(Y)=b^{-ih}E_p(Y)E_b(Y+h)
                      +p^{-ih}E_b(Y)E_p(Y+h),
\]
\[
 A=e^{i(\theta(Y)+\theta(Y+h))}
             \sum_{p<b\in\mathcal P}a_{pb}(Y)(pb)^{-1/2-iY}.
\]
As in C019y, F is the true finite source sum, V=F+conjugate(F),
U=F(Y)F(Y+h), C=F(Y)conjugate(F(Y+h)), and S=W(A+conjugate(A)).
Write K1=sum |c_s|^2/s and K4=sum c_s conjugate(c_(4s))/(4s).
C019z supplies K1 comparable to q^4 and K4=K1/13+O(q^3), together
with its complete resonance N0=(16K1X/q^2)(I+o(1)), I<0.
These local inputs, and C019's reduction, remain subject to independent
conceptual review. No actual-P comparison is assumed here.

## Conclusion

Inside the exact complex channel integral_D W^2 CA, select all terms
whose conjugated source is one witness prime and whose mollifier
indices obey r=4s. Define their complete sum, without an interior
cutoff, by
\[
 \mathcal T_4=\sum_{\substack{p,b\in\mathcal P\\p\ne b}}
 \sum_{s\le R/4}\sum_{m\le N_*}
 \frac{c_{4s}\overline{c_s}\,p^{ih}}{2s p\sqrt{mb}}
 \int_{I_m}E_m(Y)\overline{E_p(Y+h)}a_{pb}(Y)
       e^{i\phi_{m,b}(Y)}\,dY,                              \tag{1}
\]
where rho_m is the positive solution of
rho_m/(2*pi)+rho_m^2/(32d)=m^2,
\[
 I_m=[\max(X,\rho_m),\sqrt2X-h],\qquad
 \phi_{m,b}(Y)=2\theta(Y)-Y\log(4mb),                     \tag{2}
\]
and an empty or singleton interval has integral zero. Ordered pairs
in (1) mean the two distinct possible conjugated sources for each
unordered witness pair; they do not duplicate the same expansion term.

For the explicit positive constant
\[
 J_4=\int_{1/10}^{1/5}
 \left[\min\left(\frac{\sqrt2}{8\pi t},4t\right)
                         -\frac1{8\pi t}\right]_+dt,
 \qquad C_4=\frac{8\pi\log2}{13}J_4,
\]
one has, uniformly for every sufficiently large integer d,
\[
 2\operatorname{Re}\mathcal T_4
             =\frac{16K_1X}{q^2}(C_4+o(1)),\qquad
 C_4>\frac{13}{1000},\qquad I+C_4>\frac1{1000}.           \tag{3}
\]
Consequently N0+2Re(T4) is positive of order Bq^2, although N0
alone is negative of that order. This selected part of the signed
remainder cannot be discarded as o(Bq^2). The *total* remainder
could still cancel within itself; (3) is no lower bound for it.

Neither threshold for the full quotient (N1) follows. The rest of
CA, the other channels, unequal-index terms, denominator and actual-P
residual are unpaid. This is local negative evidence against a
resonance-only sign inference, not an M2 or RH obstruction. It does
not replace the witness by the selected sum. POTENTIALLY_NEW means
only that assessment1409 found no matching full evaluation; no
originality beyond the inspected sources is certified.

## Proof

### 1. Exact selection and available coefficient control

In the CA expansion in C019 (8), put v=pb, n=p, r=4s. The rational
phase parameter mvr/(ns) becomes the integer 4mb. Its outer
denominator sqrt(mnvrs) is exactly 2sp sqrt(mb). Every p in P has
entered at both arguments throughout D, by C019y's retained cutoff
fact. Thus the source interval is exactly I_m in (2), including its
true entry endpoint. This proves that (1) is an exact subfamily of
the original complex integral, before any approximation.

Cauchy--Schwarz and zero extension give
\[
 \sum_s\frac{|c_{4s}c_s|}{s}\le2K_1,\qquad
 \sum_s\frac{c_{4s}\overline{c_s}}s=4\overline{K_4}.
                                                               \tag{4}
\]
Indeed sum |c_(4s)|^2/s <=4K1. In particular no untapered local
Euler product is substituted: the needed K4 asymptotic is precisely
C019z (9)--(12), whose error pays all four original taper boundaries.

We reuse the ordinary prime number theorem, Hadamard and de la Vallee
Poussin (1896), as stated in [NIST DLMF 27.12.4](https://dlmf.nist.gov/27.12.E4),
with the fixed-proportional-interval partial summation justified in
C019z. In particular
\[
 \sum_{p\in\mathcal P}1/p=\frac{2\log2}{q}+o(q^{-1}),\quad
 \#\mathcal P=O(\sqrt X/q),\quad
 \sum_{b\in\mathcal P}b^{-1/2}=O(X^{1/4}/q).             \tag{5}
\]
No primes in short intervals or progressions are required. Combining
(4),(5) and sum_(m<=N*) m^(-1/2)=O(X^(1/4)), the total absolute
outer coefficient mass in (1) is
\[
 O(K_1\sqrt X/q^2).                                      \tag{6}
\]

### 2. Pay source-entry and band-endpoint saddle transitions

The stationary center for (2) is x=8*pi*m*b. It is an integer
multiple of 2*pi, and
\[
 \phi'(Y)=\log(Y/x),\quad\phi''(Y)=1/Y,\quad
 \phi(x)=-x-\pi/4.                                      \tag{7}
\]
C019 (5),(6),(9)--(13) apply with the amplitude
beta(Y)=E_m(Y)conjugate(E_p(Y+h))a_(pb)(Y), uniformly in all
indices. Its smooth extension has bounded supremum and bounded
scaled derivatives on [X/2,2X]. Put Delta=X^(3/4). This is a proof
partition only; no selected expansion term is deleted.

For centers x in [X/2,2X] at distance at least Delta from each
endpoint of a nonempty I_m, the C019 quadratic coordinate satisfies
|z(endpoint)|>=c Delta/sqrt(X). Its endpoint correction r(z) is
O(1), uniformly. Integrating e^(iz^2) by parts gives tails O(1/|z|).
Thus C019 (9),(13) imply
\[
 \int_{I_m}\beta(Y)e^{i\phi(Y)}dY
 =\mathbf1_{\{x\in\operatorname{int}I_m\}}
       \beta(x)\sqrt{2\pi x}\,e^{-ix}+O(X/\Delta).       \tag{8}
\]
The same error bound with no main term holds for centers outside
[X/2,2X], by C019 (12),(13). If the center is outside I_m but in
the extended range, both transformed endpoints have the same sign;
their tails still give the stated bound. Empty intervals contribute
zero throughout.

For clarity, the full Fresnel value used in (8) is
integral_R exp(iz^2)dz=sqrt(pi)exp(i*pi/4). This follows from the
standard named Gaussian integral (a starting input in
foundations/notation-and-inputs.md), continued to the parameter
epsilon-i with epsilon>0. Integration by parts on [A,infinity)
bounds its damped tails uniformly by C/A for 0<epsilon<=1, since
|epsilon-i|>=1. The same holds on the negative half-line. Dominated
convergence on a fixed compact interval, followed by this uniform
tail bound, justifies the limit epsilon down to zero. The branch
is the continuation of the positive square root. The phase -pi/4
in (7) cancels the Fresnel phase +pi/4, yielding (8).

It remains to pay every excluded transition. If x lies within Delta
of a band endpoint or of rho_m while x is in the band enlarged by
Delta, then m is comparable to sqrt(X). For m<=N*, uniformly,
\[
 \rho_m=2\pi m^2+O(q^{-2}),\qquad
 x-\rho_m=2\pi m(4b-m)+O(q^{-2}).                        \tag{9}
\]
The first estimate follows from the defining equation for rho_m,
rho_m=O(X), and d comparable to X^2q^2. For each fixed b, band
transitions therefore contain O(Delta/sqrt(X)+1) possible integers
m. So do the source transitions, since the second formula in (9)
forces |m-4b|<=C Delta/sqrt(X). These bounds are uniform in p,s.
They include exact stationary endpoints and m=4b, even if equality
occurs for many prime pairs.

The second-derivative bound gives O(sqrt(X)) for each transition
integral with its smooth amplitude; it is the bound already imported
in C019 from Kösters, arXiv:0803.1141v2, Appendix A, Lemma A.2
(Titchmarsh, second edition, Lemma 4.4),
https://arxiv.org/html/0803.1141v2#A . Its hypotheses hold by (7),
and amplitude variation is bounded. The leading term proposed in
(8) has the same upper bound. Since m,b are comparable to sqrt(X),
their combined transition contribution is at most
\[
 C K_1\left(\sum_{p\in\mathcal P}1/p\right)
          \#\mathcal P\, (\Delta/\sqrt X+1)
 =O(K_1(\Delta+\sqrt X)/q^2).                            \tag{10}
\]
Off the transition set, (6),(8) cost at most
O(K1 X^(3/2)/(Delta q^2)). With Delta=X^(3/4), both errors are
O(K1 X^(3/4)/q^2)=o(K1 X/q^2). This pays endpoints and true floors
in aggregate, rather than assigning a full saddle to every endpoint.

### 3. Coherent phase and the exact surviving count

At an interior saddle, m,p,b are fixed positive compact multiples
of sqrt(X), and x is a compact multiple of X. Hence
u(x)-log m and the corresponding p,b differences are O(1).
The own-time heat factors are 1+O(q^(-2)), and
p^(ih)=-i+O(q^(-1)), while a_(pb)(x)=2i+O(q^(-1)). Uniformly,
\[
 p^{ih}\beta(x)=2+O(q^{-1}),\quad e^{-ix}=1,\quad
 \sqrt{2\pi x}=4\pi\sqrt{mb}.                           \tag{11}
\]
All shifted factors in (11) are still evaluated at x+h. Their
replacement errors are estimated at their own arguments, not by
setting the heat time or shift to zero in (1).

Multiplying (8),(11) by the outer coefficient in (1) gives the
main term 4*pi*c_(4s)conjugate(c_s)/(s*p) per interior m.
Its absolute total is O(K1X/q^2), by (4),(5) and the O(sqrt(X))
possible m for each b. Thus the O(q^(-1)) relative error in (11)
costs O(K1X/q^3). Including (10) gives
\[
 \mathcal T_4=16\pi\overline{K_4}\,F_X
                       +o(K_1X/q^2),                    \tag{12}
\]
where, to an O(1) error in the count for each b,
\[
 F_X=\sum_{p\ne b\in\mathcal P}\frac{M_X(b)}p,\qquad
 M_X(b)=\#\left\{m\in\mathbb N:
 \frac{X}{8\pi b}\le m\le
       \min\left(\frac{\sqrt2X}{8\pi b},4b\right)\right\}.
                                                               \tag{13}
\]
Indeed x>=rho_m is equivalent, away from the paid transition, to
m<=4b by (9). Moving the upper band endpoint by h costs O(1) in
this count, as does endpoint inclusion. The approximate conditions
in (13) imply m^2<=sqrt(2)X/(2*pi), so the original constraint
m<=N* adds no interior restriction. The O(1) count errors cost
O(K1 sqrt(X)/q^2), already negligible. No prime distribution
assumption was used to count these integers m.

Define the continuous piecewise smooth function
\[
 H_4(t)=\left[\min\left(\frac{\sqrt2}{8\pi t},4t\right)
                                      -\frac1{8\pi t}\right]_+.
\]
Then M_X(b)=sqrt(X) H4(b/sqrt(X))+O(1), uniformly on P. PNT
and partial summation against this bounded-variation function on
[1/10,1/5] give
\[
 \sum_{b\in\mathcal P}M_X(b)=\frac{2X}{q}J_4+o(X/q).
\]
This is the same fixed-interval PNT specialization as (5); the
single switch in H4 causes no difficulty. The removed p=b terms
sum to O(sqrt(X)/q), since M_X(b)/b=O(1). Consequently
\[
 F_X=\frac{4X\log2}{q^2}J_4+o(X/q^2).                  \tag{14}
\]
Equations (12),(14) and K4=K1/13+O(q^3), K1 comparable to q^4,
give the asymptotic formula (3), including its factor of two for
the real numerator. All errors tend to zero along every integer d
beyond one existential onset; no special subsequence is used.

### 4. Rigorous comparison with the full negative resonance

Put A0=log2, delta=log(4/3), x0=8*pi/25 and
t0=sqrt(sqrt(2)/(32*pi)). One has 1/10<t0<1/5 and
1/(32*pi)<1/100. Thus H4 is 4t-1/(8*pi*t) up to t0 and
(sqrt(2)-1)/(8*pi*t) thereafter. Direct integration gives
\[
 C_4=\frac{A_0}{13}\left\{
 \frac{\sqrt2}{2}-\frac{4\pi}{25}+(\sqrt2-1)A_0
             -\frac{\sqrt2}{2}\log\frac{25\sqrt2}{8\pi}\right\}.
                                                               \tag{15}
\]
C019z (17),(18) express its integrand f for I as
\[
 f=f_0+e(-166A_0+61\delta)/143+131e^2/286\quad(1\le x\le x_0),
\]
\[
 f=\frac2{13}A_0(A_0-\delta)
       +\frac{-68A_0+16\delta}{286}b-\frac3{286}b^2
                                      \quad(x_0\le x\le\sqrt2),
\]
where e=(1/2)log(x/x0)<=0, b=delta+(1/2)log(x/x0), and
f0=(2/13)A0^2-(56/143)A0*delta+delta^2/22. The early linear
coefficient is negative, so early f>=f0. The later polynomial is
decreasing for b>=delta, so later f>=f(sqrt(2)). The explicit
rational enclosures below establish
\[
 f_0>-7/250,\quad f(\sqrt2)>-7/250,\quad C_4>13/1000,
 \quad C_4-\frac7{250}(\sqrt2-1)>1/1000.                 \tag{16}
\]
It follows that I>-(7/250)(sqrt(2)-1), proving I+C4>1/1000.

For a reproducible exact check of (16), use the same elementary
series as C019z: Machin's identity with 20 alternating arctangent
terms, and for rational z>=1 the logarithm formula with
v=(z-1)/(z+1),
\[
 \log z=2\sum_{k=0}^{31}\frac{v^{2k+1}}{2k+1}+E,
 \qquad 0\le E\le\frac{2v^{65}}{65(1-v^2)}.
\]
Bracket sqrt(2) between 1414213562373/10^12 and
1414213562374/10^12 by squaring. Monotonicity of log and outward
rational arithmetic then enclose every expression in (15),(16).
The script
`python3 scripts/jensen-pair-moment/coherent-saddle-sign-1415.py`
writes its complete certificate to
`scripts/jensen-pair-moment/coherent-saddle-sign-certificate-1415.json`.
In particular its exact rational intervals imply
\[
 -0.027123<f(\sqrt2)<-0.027122,\quad
 0.0133427<C_4<0.0133428,
\]
\[
 0.0017447<C_4-\frac7{250}(\sqrt2-1)<0.0017448.
\]
These terminating decimals denote rationals. All selected scalar
enclosures and all eleven Boolean checks were inspected in full.
The certificate establishes scalar comparisons only; the asymptotic
and source-entry argument is the proof above, not numerical sampling.

### 5. The remaining full observable

The exact numerator is still
\[
 \mathcal N_P=(\mathcal N_0+2\operatorname{Re}\mathcal T_4)
 +\mathcal O(G,J)+2\operatorname{Re}\left\{
 \int_D W^2UA+\left(\int_D W^2CA-\mathcal T_4\right)
                   +\int_D W^2C\overline A\right\}+\mathcal E_P.
                                                               \tag{17}
\]
No sign or size has been proved for the second line of contributions.
Likewise D0+O(J,J)+2Re integral W^2 A^2 remains the complete
denominator, not a quantity bounded below by its diagonal. Actual-P
transfer is not invoked; later use of C019t retains its unaudited
C019j/k/l/s, L320 and L018/L021 contracts. C019z's negative N0 and
the positive partial sum (3) are both compatible with either sign
or substantial cancellation in (17). Neither full-quotient threshold
has been decided, and independent density/root/global-Xi gaps remain.

## Mathlib

Full matching coverage for this fixed moving-heat saddle subfamily
has not been checked. Supporting finite-sum, Gaussian-integral,
calculus, Cauchy--Schwarz or prime-number results would not alone
formalize (3). PNT and the derivative estimates are the precisely
cited known inputs above; no new general stationary-phase theorem,
new prime-distribution estimate or Mathlib formalization is claimed.
