# C020b — Matched integer saddles reinforce each other in the fixed witness

## Hypotheses

Use exactly C019y's fixed witness and C020a's notation, with positive
integers d tending to infinity. In particular
\[
 d=\frac{T}{2\pi}(\log(T/(2\pi))-1),\quad T>2\pi e,
 \quad X=T/\sqrt{2d},\quad q=\log X,\quad B=(\sqrt2-1)X,
 \quad h=3\pi/q,
\]
\[
 D=[X,\sqrt2X-h],\quad L=\lfloor X^{1/1000}\rfloor,
 \quad R=L^4,\quad W=|M(Y)M(Y+h)|^2,
 \quad M(Y)^2M(Y+h)^2=\sum_{s\le R}c_s s^{-1/2-iY}.
\]
Here M and c retain all four original linear tapers and the real
Euler-product coefficients of zeta(s)^(-1/2) on Re(s)>1. Extend c
by zero beyond R. Retain the exact own-time heat factors and floors
\[
 t(Z)=Z^2/(2d),\quad u(Z)=\tfrac12\log(Z/(2\pi)),
\]
\[
 E_n(Z)=\exp\{t(Z)((u(Z)-\log n)^2-\pi^2/16)/4
                        +i\pi t(Z)(u(Z)-\log n)/8\},
 \quad N(Z)=\left\lfloor\sqrt{Z/(2\pi)+Z^2/(32d)}\right\rfloor,
\]
\[
 N_*=N(\sqrt2X),\quad
 \theta(Z)=\tfrac Z2\log(Z/(2\pi))-\tfrac Z2-\pi/8,
 \quad F(Z)=e^{i\theta(Z)}\sum_{n\le N(Z)}E_n(Z)n^{-1/2-iZ}.
\]
Let P be the original positively normalized actual-Jensen value in
C019m/p/r. No estimate for P is assumed in this result. Put
\(\mathcal P=[\sqrt X/10,\sqrt X/5]\cap\{\text{primes}\}\) and
\[
 a_{pb}(Y)=b^{-ih}E_p(Y)E_b(Y+h)+p^{-ih}E_b(Y)E_p(Y+h),
\]
\[
 A=e^{i(\theta(Y)+\theta(Y+h))}
       \sum_{p<b\in\mathcal P}a_{pb}(Y)(pb)^{-1/2-iY},
 \quad C=F(Y)\overline{F(Y+h)},\quad U=F(Y)F(Y+h).
\]
The fixed witness is S=W(A+conjugate(A)), and the actual target is
Q_P=P(Y)P(Y+h)W. For a=1,2,3,4 use C019z's retained correlations
\[
 K_a=\sum_s\frac{c_s\overline{c_{as}}}{as},\qquad
 K_1\asymp q^4,\qquad K_a=\rho(a)K_1+O(q^3),
 \quad(\rho(1),\rho(2),\rho(3),\rho(4))
       =(1,-6/13,-4/11,1/13).                         \tag{1}
\]
These are finite tapered-coefficient statements; no critical-line
reciprocal, RH, random law or nonvanishing assumption is introduced.
C019/C019y/z and C020a remain subject to independent conceptual
review; the calculation here is not that review.

## Conclusion

For each a in {1,2,3,4}, define the complete selected families
\(\mathcal T_a^+\) of CA and \(\mathcal T_a^-\) of C conjugate(A)
by (4) below. In the first family the conjugated source is a witness
prime and r=a*s; in the second the unconjugated source is a witness
prime and s=a*r. There is no additional interior cutoff. Put
\[
 J_a=\int_{1/10}^{1/5}
 \left[\min\left(\frac{\sqrt2}{2\pi a t},at\right)
                            -\frac1{2\pi a t}\right]_+dt,
 \qquad C_a=2\pi a\rho(a)\log(2)J_a.
\]
Then, for every sufficiently large integer d,
\[
 \mathcal T_a^- -\overline{\mathcal T_a^+}
       =O\left(\frac{K_1X}{q^3}+\frac{K_1X^{3/4}}{q^2}\right),
\]
\[
 2\operatorname{Re}(\mathcal T_a^++\mathcal T_a^-)
        =\frac{16K_1X}{q^2}(2C_a+o(1)).                 \tag{2}
\]
Thus the matched family reinforces, rather than cancels, C020a's
positive a=4 term. However the entire selected set a=1,2,3,4 has
\[
 C_1=0,\qquad C_2+C_3+C_4<-19/1000.
\]
Writing N0=(16K1X/q^2)(I+o(1)) as in C019z, one obtains
\[
 \mathcal N_0+2\operatorname{Re}\sum_{a=1}^4
       (\mathcal T_a^++\mathcal T_a^-)
   =\frac{16K_1X}{q^2}\left(I+2\sum_{a=1}^4 C_a+o(1)\right),
 \qquad I+2\sum_{a=1}^4C_a<-39/1000.                    \tag{3}
\]
This is a signed partial numerator, not a bound for the full one.
It includes all terms in these eight selected families, but neither
all integer saddles nor all rational twists. The complement (12),
the full denominator and actual-P residual are unpaid. Neither a
cBq^2 lower bound nor an O(B) upper bound for (N1) follows. The
matched-cancellation test supplies a local input toward the fixed
quotient, with no claimed originality beyond the sources checked
and no resolution of the independent Jensen-density or RH gaps.

## Proof

### 1. Exact matching of the two channels

Let rho_m solve rho_m/(2*pi)+rho_m^2/(32d)=m^2, and define
\[
 I_m^+=[\max(X,\rho_m),\sqrt2X-h],\qquad
 I_m^-=[\max(X,\rho_m-h),\sqrt2X-h].
\]
Intervals with left endpoint at least the right endpoint have zero
integral. All witness primes have entered at both arguments on D,
as retained in C019y. With
\(\phi^0_\kappa(Y)=2\theta(Y)-Y\log\kappa\) and
\(\phi^h_\kappa(Y)=2\theta(Y+h)-Y\log\kappa\), put
\[
 \mathcal T_a^+=\sum_{\substack{p,b\in\mathcal P\\p\ne b}}
 \sum_{s\le R/a}\sum_{m\le N_*}
 \frac{c_{as}\overline{c_s}\,p^{ih}}{\sqrt a\,s p\sqrt{mb}}
 \int_{I_m^+}E_m(Y)\overline{E_p(Y+h)}a_{pb}(Y)
                  e^{i\phi^0_{amb}(Y)}\,dY,
\]
\[
 \mathcal T_a^-=\sum_{\substack{p,b\in\mathcal P\\p\ne b}}
 \sum_{s\le R/a}\sum_{m\le N_*}
 \frac{c_s\overline{c_{as}}\,m^{ih}}{\sqrt a\,s p\sqrt{mb}}
 \int_{I_m^-}E_p(Y)\overline{E_m(Y+h)}\overline{a_{pb}(Y)}
                  e^{-i\phi^h_{amb}(Y)}\,dY.             \tag{4}
\]
In C019 (8), the first selection is n=p, v=pb, r=a*s.
For the second selection, its original m=p, original n equals
the summation index m in (4), original r=s and original s=a*s.
The rational phase n*v*s/(m*r) is then a*m*b. This also verifies
the outer denominator and shifted factor in each line of (4).
Ordered p,b represent the two distinct choices of the selected
source for each unordered witness pair. They do not count the
same expansion term twice. Different a give different mollifier
ratios within either channel. In particular T_4^+ is precisely
C020a's T4. No real or conjugate channel has been silently dropped.

### 2. Stationary phases and complete transition payment

Set x=2*pi*a*m*b. The positive phase has center x, and the negative
phase has center x-h. Direct substitution gives
\[
 \phi^0_{amb}(x)=-x-\pi/4,\qquad
 -\phi^h_{amb}(x-h)=x+\pi/4-h\log(amb).                 \tag{5}
\]
Their second derivatives have respective signs plus and minus, with
magnitude 1/x at their centers. The full Gaussian factors therefore
give the two leading expressions
\[
 \sqrt{2\pi x}\,e^{-ix},\qquad
 \sqrt{2\pi x}\,e^{ix-ih\log(amb)}.                    \tag{6}
\]
The Fresnel phases cancel the constants in (5). Since amb is an
integer, exp(ix)=exp(-ix)=1. The remaining shifted phase in (6)
is essential; conjugating the Fresnel constant alone would give
the wrong source factor.

Here is the full boundary and source-entry justification for (6).
C019 (5),(6),(9)--(13) give bounded scaled derivatives of the
smooth amplitudes in (4) and an endpoint-corrected quadratic
coordinate, including negative phases by conjugation. The only
known oscillatory bound used is Kösters, *On the Occurrence of the
Sine Kernel in Connection with the Shifted Moments of the Riemann
zeta function*, arXiv:0803.1141v2, Appendix A, Lemma A.2
(Titchmarsh, second edition, Lemma 4.4),
https://arxiv.org/html/0803.1141v2#A . Its twice-differentiable real
phase has a second derivative of one sign bounded away from zero;
here the magnitude is at least c/X on every relevant subinterval.
Partial summation against the smooth amplitude gives O(sqrt(X)).
The precise source and relevant proof cases are already covered by
assessment1409/source-notes1410. This is an applicability argument,
not a new general oscillatory theorem or a new source import.

Use Delta=X^(3/4), as in C020a. Away from Delta-neighborhoods of
the actual endpoints, C019's quadratic coordinate and the elementary
Fresnel tail bound give (6) times the center amplitude when the
center is inside the interval, and zero otherwise, with error
O(X/Delta). The endpoint correction is O(1). Remote centers are
nonstationary and obey the same error bound. A full Gaussian is
never assigned to a stationary endpoint without paying its error.

For n<=N*, uniformly rho_n=2*pi*n^2+O(q^(-2)). Thus
\[
 x-\rho_m=2\pi m(ab-m)+O(q^{-2}).                        \tag{7}
\]
For the minus family, (x-h)-(rho_m-h)=x-rho_m exactly. Its
source transition therefore has exactly the same comparison (7).
Its band endpoints translate to x=X+h and x=sqrt(2)X;
the plus family has x=X and x=sqrt(2)X-h. For fixed b and a<=4,
each band transition includes O(Delta/sqrt(X)+1) integers m.
For a source transition whose center is in the enlarged band,
m is comparable to sqrt(X), and (7) implies
|m-ab|<=C Delta/sqrt(X). It gives the same count. Empty intervals,
exact endpoints and equality m=ab are included in this accounting.

Cauchy--Schwarz and zero extension give
\[
 \sum_s|c_{as}c_s|/s\le\sqrt a K_1,
 \quad \sum_s c_{as}\overline{c_s}/s=a\overline{K_a}.
                                                               \tag{8}
\]
The fixed-interval PNT consequences retained in C020a are
sum_(p in P)1/p=O(1/q), #P=O(sqrt(X)/q), and
sum_(b in P)b^(-1/2)=O(X^(1/4)/q). Together with
sum_(m<=N*)m^(-1/2)=O(X^(1/4)), (8) bounds the total absolute
outer coefficient mass in either line of (4) by
O(K1 sqrt(X)/q^2). The off-transition error is therefore
O(K1 X^(3/2)/(Delta q^2)). On transitions m,b are comparable
to sqrt(X), so the O(sqrt(X)) integral bound and (8) give total
O(K1(Delta+sqrt(X))/q^2). With the chosen Delta both are
O(K1 X^(3/4)/q^2). All constants are uniform for this finite set
of a; no assertion uniform in a growing with X is made.

### 3. The leading amplitudes and common integer count

At an interior center, m,p,b are compact positive multiples of
sqrt(X). At their own arguments the heat factors equal 1+O(q^(-2)).
Also p^(ih)=-i+O(q^(-1)) and a_pb=2i+O(q^(-1)). In the plus
family the full source multiplier in the main term is consequently
2+O(q^(-1)). In the minus family combine (6) with m^(ih) first:
\[
 m^{ih}e^{-ih\log(amb)}=(ab)^{-ih}=i+O(q^{-1}),\qquad
 \overline{a_{pb}(x-h)}=-2i+O(q^{-1}).
\]
The full multiplier is again 2+O(q^(-1)), including the heat
factors at x-h and x. This pays their actual arguments rather
than changing either heat time or the fixed shift in (4).
Since sqrt(2*pi*x)=2*pi*sqrt(a*m*b), the leading term per m
is 4*pi*c_(as)conjugate(c_s)/(s*p) in the plus family and
4*pi*c_s conjugate(c_(as))/(s*p) in the minus family.

Up to O(1) errors per b and the already paid transitions, both
families have the same count
\[
 M_a(b)=\#\left\{m\in\mathbb N:
 \frac{X}{2\pi ab}\le m\le
           \min\left(\frac{\sqrt2X}{2\pi ab},ab\right)\right\},
 \qquad F_a=\sum_{p\ne b\in\mathcal P}\frac{M_a(b)}p.     \tag{9}
\]
Indeed (7) gives m<=ab outside the source transition. Moving the
band endpoints by h changes each count by O(1). The conditions
m<=ab and 2*pi*a*m*b<=sqrt(2)X imply
m^2<=sqrt(2)X/(2*pi), so m<=N* imposes no further restriction.
Count errors cost O(K1 sqrt(X)/q^2). The leading absolute mass
is O(K1 X/q^2), hence the source replacement costs O(K1 X/q^3).
Consequently, writing epsilon_X=K1 X/q^3+K1 X^(3/4)/q^2,
\[
 \mathcal T_a^+=4\pi a\overline{K_a}F_a+O(\epsilon_X),
 \qquad \mathcal T_a^-=4\pi aK_aF_a+O(\epsilon_X).        \tag{10}
\]
The first assertion of (2) follows since F_a is real. In
particular matching does not reverse the real leading sign.

For completeness, M_a(b)=sqrt(X)H_a(b/sqrt(X))+O(1), where H_a
is the integrand defining J_a. This is a fixed continuous,
piecewise smooth function. The ordinary prime number theorem
(Hadamard and de la Vallee Poussin, 1896), in the precise form
[NIST DLMF 27.12.4](https://dlmf.nist.gov/27.12.E4), gives by
partial summation on [sqrt(X)/10,sqrt(X)/5]
\[
 \sum_b M_a(b)=2XJ_a/q+o(X/q),\qquad
 \sum_p1/p=2\log(2)/q+o(q^{-1}).
\]
This uses the uniform qualitative PNT on fixed positive compact
multiples of sqrt(X), as justified in C019z. No short intervals,
progressions or RH-strength error are invoked. The deleted p=b
terms cost O(sqrt(X)/q), because M_a(b)/b=O(1). Thus
F_a=4X log(2) J_a/q^2+o(X/q^2), additively also when J_a=0.
Combining this with (1),(10) proves the second assertion of (2).

### 4. Complete scalar comparison for these four ratios

The integrand H_a becomes positive at
t_a=1/(a sqrt(2*pi)) and switches its upper branch at
v_a=sqrt(sqrt(2)/(2*pi))/a. For a=1, t_a>1/5 and J1=0.
For a=2, 1/10<t_a<1/5<v_a. For a=3, both thresholds lie
strictly between 1/10 and 1/5. For a=4, t_a<1/10<v_a<1/5.
These strict comparisons are verified by squaring using the
rational enclosures below. Integrating a*t and 1/(2*pi*a*t)
on the indicated intervals gives, with A0=log(2), z=8*pi/25,
\[
 C_2=-\frac{3A_0}{13}(z-1-\log z),
\]
\[
 C_3=-\frac{2A_0}{11}
 \left(\sqrt2-1-\frac{A_0}{2}
              +(\sqrt2-1)\log\frac{18\pi}{25\sqrt2}\right),
\]
\[
 C_4=\frac{A_0}{13}\left(
 \frac{\sqrt2}{2}-\frac{4\pi}{25}+(\sqrt2-1)A_0
              -\frac{\sqrt2}{2}\log\frac{25\sqrt2}{8\pi}\right).
                                                               \tag{11}
\]
The last expression agrees with C020a (15). For example the a=3
integral is [sqrt(2)-1-A0/2+(sqrt(2)-1)log(18*pi/(25*sqrt(2)))]
divided by 12*pi; multiplying by 2*pi*3*rho(3)*A0 gives (11).

Use the same elementary exact enclosures as C020a: bracket sqrt(2)
between 1414213562373/10^12 and 1414213562374/10^12 by squaring;
apply twenty alternating arctangent terms in Machin's identity
pi=16 arctan(1/5)-4 arctan(1/239); and use, for rational z>=1,
log z=2 sum_(k=0)^31 v^(2k+1)/(2k+1)+E, v=(z-1)/(z+1),
with 0<=E<=2v^65/(65(1-v^2)). Monotonicity encloses logarithms
of interval arguments. Rational outward arithmetic then gives
\[
 -0.000002247<C_2<-0.000002246,\qquad
 -0.033041230<C_3<-0.033041229,
\]
\[
 0.013342706<C_4<0.013342707,\qquad
 -0.019700770<C_2+C_3+C_4<-0.019700769.
\]
These terminating decimals are rational comparisons. Generate the
full certificate, including all branch comparisons, with

    python3 scripts/jensen-pair-moment/matched-saddle-sign-1416.py

Its path is
scripts/jensen-pair-moment/matched-saddle-sign-certificate-1416.json.
It records exact intervals, thresholds and failures. This verifies
scalar inequalities only; the asymptotic argument is (4)--(10).
All five conclusion intervals and all thirteen checks were inspected
in full; the failures array is empty.
Using C019z's I<-19/10000 yields (3). No numerical prime, zeta,
or witness sampling is used as proof.

### 5. The unchanged full numerator and denominator

Let R_+=integral_D W^2 CA-sum_(a=1)^4 T_a^+ and
R_-=integral_D W^2 C conjugate(A)-sum_(a=1)^4 T_a^-.
C019y (5) gives exactly
\[
 \mathcal N_P=
 \left\{\mathcal N_0+2\operatorname{Re}\sum_{a=1}^4
                  (\mathcal T_a^++\mathcal T_a^-)\right\}
 +\mathcal O(G,J)
 +2\operatorname{Re}\left\{\int_D W^2UA+R_++R_-\right\}
 +\mathcal E_P.                                           \tag{12}
\]
No sign or size is assigned to the last three terms. In particular,
fixed ratios beyond four, other source assignments and noninteger
rational twists are still in R_+,R_-. C020a's positive partial sum
and (3)'s negative larger partial sum are compatible; neither is
a signed bound for (12). They show why selecting favorable terms
cannot establish the full numerator's sign.

The denominator remains D0+O(J,J)+2 Re integral_D W^2 A^2;
neither diagonal dominance nor nonvanishing is supplied. The
original convention at zero denominator is retained. No estimate
from C019t is used. Any later actual-P transfer retains its
unaudited C019j/k/l/s, L320 and L018/L021 contracts. Density,
ordered intervals, reciprocal root mapping, bulk separation and
all-degree Xi positivity remain independent unresolved steps.

## Mathlib

Full matching coverage for this fixed witness and its matched
moving-heat saddle families has not been checked. Supporting
finite-sum, Gaussian-integral, PNT, calculus or Cauchy--Schwarz
results would not by themselves formalize (2)--(3). The precise
known inputs are cited above and reused from ready assessment1409;
no new prime-distribution theorem or Mathlib formalization is claimed.
