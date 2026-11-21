# C019y — Dyadic resonance cancellation in the fixed real prime witness

## Hypotheses

Use the unchanged C019p/u/x setup, with positive integers d tending
to infinity and
\[
 d=\frac{T}{2\pi}(\log(T/(2\pi))-1),\quad T>2\pi e,\quad
 X=T/\sqrt{2d},\quad q=\log X,\quad B=(\sqrt2-1)X,\quad h=3\pi/q,
\]
\[
 J=[X,\sqrt2X],\quad D=[X,\sqrt2X-h],\quad
 L=\lfloor X^{1/1000}\rfloor,\quad \ell=\log L,\quad R=L^4.
\]
All claims are beyond one absolute existential integer onset. Keep
the real multiplicative coefficients alpha of the Euler-product
branch of zeta(s)^(-1/2) on Re(s)>1, and precisely the linear taper
omega(n)=1-log(n)/ell for n<=L. Define
\[
 M(Y)=\sum_{n\le L}\alpha(n)\omega(n)n^{-1/2-iY},\quad
 H(Y)=M(Y)M(Y+h),\quad W(Y)=|H(Y)|^2,
 \quad H(Y)^2=\sum_{s\le R}c_s s^{-1/2-iY}.
\]
Thus the exact four-factor coefficient is
\[
 c_s=\sum_{a_1a_2a_3a_4=s;\ a_j\le L}
       \left(\prod_{j=1}^4\alpha(a_j)\omega(a_j)\right)(a_2a_4)^{-ih}.
                                                               \tag{1}
\]
Retain each own heat time and true floor:
\[
 t(Z)=Z^2/(2d),\quad u(Z)=\tfrac12\log(Z/(2\pi)),\quad
 N(Z)=\left\lfloor\sqrt{Z/(2\pi)+Z^2/(32d)}\right\rfloor,
\]
\[
 E_n(Z)=\exp\{\tfrac14t(Z)((u(Z)-\log n)^2-\pi^2/16)
                   +i(\pi/8)t(Z)(u(Z)-\log n)\},
\]
\[
 \theta(Z)=\tfrac Z2\log(Z/(2\pi))-\tfrac Z2-\pi/8,
 \qquad F(Z)=e^{i\theta(Z)}\sum_{n\le N(Z)}E_n(Z)n^{-1/2-iZ},
 \qquad V=F+\overline F.
\]
The real normalized actual-Jensen value P is exactly C019p's P,
with its original positive normalization. No estimate for P is an
input to the finite cancellation below.

Let \(\mathcal P=[\sqrt X/10,\sqrt X/5]\cap\{\text{primes}\}\).
Index unordered distinct pairs by their product v=p1*p2, p1<p2;
unique factorization makes the pair recoverable from v. Write
\[
 a_{m,n}(Y)=n^{-ih}E_m(Y)E_n(Y+h)
                   +m^{-ih}E_n(Y)E_m(Y+h),\quad a_v=a_{p_1,p_2},
\]
\[
 \Theta(Y)=\theta(Y)+\theta(Y+h),\qquad
 A(Y)=e^{i\Theta(Y)}\sum_{p_1<p_2\in\mathcal P}
                        a_v(Y)v^{-1/2-iY},
\]
\[
 S(Y)=W(Y)(A(Y)+\overline{A(Y)}),\quad
 Q_P(Y)=P(Y)P(Y+h)W(Y),\quad
 \mathcal D=\int_D S^2,\quad \mathcal N_P=\int_D Q_P S.
\]
This is precisely assessment1409's prescribed witness, without
adjustable coefficients or deletion of its other prime pairs.
The quotient is \(\mathcal N_P^2/\mathcal D\) when \(\mathcal D>0\),
and zero when \(\mathcal D=0\). No nonvanishing assumption is made.

## Conclusion

Equations (3)–(5) below give a complete finite decomposition of both
integrals, including all conjugate channels and the actual-P residual.
One explicit zero-rational-frequency slice has a positive self term
\(\mathcal D_2\) and a full matching numerator term \(\mathcal N_2\)
satisfying
\[
 cBq^2\le\mathcal D_2\le CBq^2,\qquad
 |\mathcal N_2|\le CBq,\qquad
 \mathcal E_2:=\mathcal N_2-\mathcal D_2
                    =-\mathcal D_2+O(Bq).                    \tag{2}
\]
In particular the doubled-source complement \(\mathcal E_2\) is
negative of order Bq^2. Its zero frequency prevents treating it as
an oscillatory error. All constants are absolute.

These are slice statements, not bounds on the full numerator,
denominator or quotient. They establish neither the proposed cBq^2
quotient lower bound nor an O(B) quotient upper bound. The remaining
zero-frequency sum, unequal frequencies, nonconjugate channels and
actual-P residual are still present in (5). No M2, sign-density,
Jensen-root or RH conclusion follows. This finite-sum development
uses unchanged EXPLORE coverage1409. Its selected-slice estimates
remain unaudited; audit1421 below checks only the finite identities
(1),(3)--(5). No originality beyond the assessed sources is asserted.

## Proof

### Complete expansion before selecting the slice

Put \(N_*=N(\sqrt2X)\), \(Z_*=N_*^2R\), and, exactly as in C019u,
\[
 G_k(Y)=\sum_{mnr=k;\ m,n\le N_*,\ r\le R}
 c_r n^{-ih}E_m(Y)E_n(Y+h)
             \mathbf1_{\{m\le N(Y),\ n\le N(Y+h)\}}.
\]
Every p in the witness is inside both floors on D, by C019x's
audited cutoff check. Also p>R eventually. Therefore an equality
v*s=v'*s' with witness prime products v,v' and s,s'<=R forces
v=v' and s=s': none of the two large primes can divide s or s'.
Define J_(vs)=a_v*c_s, and J_k=0 at the other indices. The two exact
identities are
\[
 U(Y)H(Y)^2=e^{i\Theta(Y)}\sum_{k\le Z_*}G_k(Y)k^{-1/2-iY},
 \quad A(Y)H(Y)^2=e^{i\Theta(Y)}\sum_{k\le Z_*}J_k(Y)k^{-1/2-iY},
 \quad U(Y)=F(Y)F(Y+h).                                    \tag{3}
\]
For two coefficient arrays define the real signed off-diagonal
\[
 \mathcal O(K,J)=2\operatorname{Re}\int_D
 \sum_{k\ne l}\frac{K_k(Y)\overline{J_l(Y)}}{\sqrt{kl}}
                         e^{iY\log(l/k)}\,dY,
\]
and put
\[
 \mathcal D_0=2\int_D\sum_k|J_k|^2/k,\quad
 \mathcal N_0=2\operatorname{Re}\int_D\sum_kG_k\overline{J_k}/k,
 \quad C(Y)=F(Y)\overline{F(Y+h)},
\]
\[
 \mathcal E_P=\int_D(P(Y)P(Y+h)-V(Y)V(Y+h))W^2(A+\overline A).
                                                               \tag{4}
\]
Expanding V(Y)V(Y+h)=U+conjugate(U)+C+conjugate(C) gives
\[
 \mathcal D=\mathcal D_0+\mathcal O(J,J)
                      +2\operatorname{Re}\int_D W^2 A^2,
\]
\[
 \mathcal N_P=\mathcal N_0+\mathcal O(G,J)
    +2\operatorname{Re}\int_D W^2(UA+CA+C\overline A)
    +\mathcal E_P.                                           \tag{5}
\]
These are finite identities with the full W, rather than a formal
orthogonal projection. In particular \(\mathcal D\ge\mathcal D_0\)
is not asserted. The remaining three complex products in (5)
include every nonconjugate and mixed real-pair channel.

Cauchy–Schwarz gives the exact residual estimate
\[
 |\mathcal E_P|\le
 \|(PP_h-VV_h)W\|_{L^2(D)}\sqrt{\mathcal D}.                  \tag{6}
\]
If the denominator vanishes, S=0 almost everywhere and both actual
and reference numerators vanish. Thus (6) needs no division by a
possibly zero norm. No numerical order for its first factor is
claimed here. Using C019t's stronger but still-unaudited contract
would retain its C019j/k/l/s, L320 and L018/L021 qualifications;
that contract is not used to prove (2).

### Audit1421 of the finite identities only

18 November 2026. This scoped audit verifies (1),(3)--(5) for use
in C019/C020c/C020d. It does not audit (2), the selected-slice
estimates below, or the actual-P approximation contracts.

The coefficient expansion (1) is the product of the four finite
mollifiers with exactly two shifted factors. Every witness prime
exceeds R eventually and is below N(X), by the scale relation and
the strict gap 1/5<1/sqrt(2*pi). If v*s=v'*s', every prime in v
must therefore divide v'; unique factorization gives v=v', s=s'.
Also v*s<=N*^2*R, so the definition of J loses no index. Expanding
the finite products now gives (3) with both source indicators.

Since W^2=|H^2|^2,
W^2*U*conjugate(A)=(U H^2)*conjugate(A H^2). Its equal and
unequal integer frequencies give exactly N0 and O(G,J) after
taking twice the real part. Similarly 2*W^2*|A|^2 gives
D0+O(J,J). The remaining term in S^2 is 2 Re(W^2 A^2).
Finally the eight terms of
(U+conjugate(U)+C+conjugate(C))*(A+conjugate(A)) pair into
twice the real parts of U*conjugate(A), U*A, C*A and
C*conjugate(A). Subtracting the reference product from the actual
one is precisely E_P in (4). This proves (5), including all
conjugates and the original W^2. All sums are finite for fixed d;
source jumps are inside their indicators and are integrable.
No orthogonality, sign assertion, nonvanishing, or interchange of
an infinite sum and an integral enters these identities.

### Six exact source assignments in the selected slice

Let
\[
 \mathcal P_0=[\sqrt X/10,\sqrt X/6]\cap\{\text{primes}\},
 \quad U_L=\lfloor\sqrt L/2\rfloor,
 \quad\mathcal R_0=\{r\le U_L:r\text{ squarefree},\ p\mid r\Rightarrow p>11\}.
\]
For v=p1*p2 with p1<p2 in P0 and r in R0, select k=2vr in (4).
The indices are distinct: the two primes exceed R, and 2r<=sqrt(L)
is recovered after removing them. C019x gives N_*<sqrt(X) and
t(Z)=O(q^(-2)), uniformly on J. Since
\[
 2p_j\le\sqrt X/3<\sqrt{X/(2\pi)}-1\le N(X)
\]
eventually, all of p_j and 2p_j are present throughout D at their
own arguments. The strict constant gap pays the integer floor.

In a factorization m*n*a=2p1*p2*r with a<=R, neither large prime
can divide a, and p1*p2>N_* prevents both from occupying one source.
Any prime factor of r is at least 13, and 13*p_j>sqrt(X)>N_*;
none can enter either source. The only remaining choice is whether
the factor 2 goes into a, m or n. Hence exactly six source
assignments occur, with no other coefficient that could be hidden
in this selected G_k. Put
\[
 b_v(Y)=a_{2p_1,p_2}(Y)+a_{p_1,2p_2}(Y).
\]
The exact identity is
\[
 G_{2vr}=c_{2r}a_v+c_r b_v,\qquad J_{2vr}=c_{2r}a_v.          \tag{7}
\]
The first summand has the two original source assignments; the
second has the four doubled-source assignments, all with their
original heat times and entry indicators equal to one.

### Insert the prime 2 in the four original linear tapers

Write w=2^(-ih) and delta=log(2)/ell. For an ordered factorization
\(\mathbf a=(a_1,a_2,a_3,a_4)\) of r, put
\[
 t_{\mathbf a}=\left(\prod_j\alpha(a_j)\omega(a_j)\right)(a_2a_4)^{-ih}.
\]
All a_j are odd and at most r. Every factorization of 2r is obtained
uniquely by inserting 2 into one of the four positions. All four
resulting factors are <=2r<=sqrt(L), so no truncation is changed.
Multiplicativity gives alpha(2a_j)=-alpha(a_j)/2; the linear taper
gives omega(2a_j)=omega(a_j)-delta. With epsilon_j=1 at positions
2,4 and zero at positions 1,3, equation (1) therefore gives exactly
\[
 c_{2r}=-(1+w)c_r+\delta e_r,\qquad
 e_r=\frac12\sum_{\mathbf a}t_{\mathbf a}
                         \sum_{j=1}^4\frac{w^{\epsilon_j}}{\omega(a_j)}.
                                                               \tag{8}
\]
There are 4^nu(r) ordered assignments, each alpha product has
absolute value 2^(-nu(r)), and all taper values are in [1/2,1].
Consequently
\[
 |c_r|\le2^{\nu(r)},\quad |c_{2r}|\le2^{\nu(r)+1},\quad
 |e_r|\le4\,2^{\nu(r)}.                                    \tag{9}
\]
C019x (8), which applies to every squarefree integer <=sqrt(L),
not only integers without small prime factors, also gives
\[
 |c_{2r}|\ge2^{\nu(r)+1}/32.                               \tag{10}
\]
Its sector check uses h*log(2r)<=3*pi/2000 and retains every taper.
Thus (8) is not a replacement of the finite mollifier by zeta^(-2).

### Own-time heat comparison and cancellation

For n=p_j or 2p_j, n/sqrt(X) stays in the fixed interval [1/10,1/3].
Thus u(Z)-log(n) is bounded uniformly for Z in J. The exact heat
definition and t(Z)=O(q^(-2)) imply E_n(Z)=1+O(q^(-2)) uniformly.
Every E factor is evaluated at its own argument in these estimates.
With z_j=p_j^(-ih), direct expansion of the two orientations gives
\[
 a_v=z_1+z_2+O(q^{-2}),\quad
 b_v=(1+w)(z_1+z_2)+O(q^{-2})=(1+w)a_v+O(q^{-2}).            \tag{11}
\]
Since log(p_j)=q/2+O(1), z_j=i+O(q^(-1)); in particular
1<=|a_v|<=3 beyond one common onset. Combining (7)–(11), with
delta=O(ell^(-1)) and ell asymptotic to q/1000, proves
\[
 G_{2vr}=\delta e_r a_v+c_r\{b_v-(1+w)a_v\},\qquad
 |G_{2vr}|\le C\,2^{\nu(r)}/\ell.                          \tag{12}
\]
The O(q^(-2)) heat errors and the O(ell^(-1)) taper errors have
both been retained. No pointwise positivity of the full pair has
entered this identity or bound.

### Sum only this slice, then retain the remainder

Define the terms selected from (4) by
\[
 \mathcal D_2=\int_D\sum_{p_1<p_2\in\mathcal P_0,\ r\in\mathcal R_0}
                         \frac{|c_{2r}a_v|^2}{vr},
\]
\[
 \mathcal N_2=\operatorname{Re}\int_D
       \sum_{p_1<p_2\in\mathcal P_0,\ r\in\mathcal R_0}
                         \frac{G_{2vr}\overline{c_{2r}a_v}}{vr}.
                                                               \tag{13}
\]
The factors in (13) are 2/(2vr), as required by (4); no factor of
two has been omitted. Equation (7) makes E2=N2-D2 exactly the
doubled-source contribution c_r*b_v, with its real part.

For the source-prime count use only the same standard PNT as C019x:
pi(x)~x/log(x), Hadamard and de la Vallee Poussin (1896), precisely
[NIST DLMF 27.12.4](https://dlmf.nist.gov/27.12.E4).
It is an already assessed input, not a new source assumption.
Subtracting at the fixed endpoints sqrt(X)/6 and sqrt(X)/10 gives
|P0| asymptotic to 2*sqrt(X)/(15q). Each pair weight lies between
36/X and 100/X. It follows, including the distinct-pair restriction,
that
\[
 \sum_{p_1<p_2\in\mathcal P_0}\frac1{p_1p_2}\asymp q^{-2}.
                                                               \tag{14}
\]
No short-interval or progression theorem is used.

C019x (3)'s finite squarefree harmonic estimate gives the lower
bound in
\[
 \sum_{r\in\mathcal R_0}\frac{4^{\nu(r)}}r\asymp\ell^4.    \tag{15}
\]
Indeed log(U_L) is asymptotic to ell/2. For the upper bound, on
squarefree r one has 4^nu(r)=d_4(r); hence the sum is at most
\(\sum_{n\le U_L}d_4(n)/n\le(1+\log U_L)^4\), by expanding
four finite harmonic sums and enlarging the product-restricted set.
This also treats r=1, for which nu(1)=0.

Using |D| asymptotic to B, (9),(10),(11),(14),(15) in D2 gives
\[
 \mathcal D_2\asymp B\ell^4/q^2\asymp Bq^2.
\]
Using instead (9),(11),(12),(14),(15) in N2 gives
\[
 |\mathcal N_2|\le CB\ell^3/q^2=O(Bq).
\]
This proves (2), including E2<=-cBq^2 eventually. All source and
coefficient sums here are finite, and all estimates were uniform
over their indices and the closed D, so finitely many absolute
onset requirements can be combined for every sufficiently large d.

The selected indices are only part of the zero-frequency sums.
The first unpaid expression in the numerator is
\[
 \mathcal N_0-\mathcal N_2
 =2\operatorname{Re}\int_D\sum_{k\ \text{not selected}}
                                  G_k\overline{J_k}/k.        \tag{16}
\]
It has no proved sign or O(B) bound. Even evaluating (16) would
leave O(G,J), O(J,J), the nonconjugate terms and E_P in (5).
In particular (2) cannot be extrapolated to cancellation of the
entire numerator or used to replace the full denominator by D2.
C019x's separate positive diagonal, whose chosen r has no small
prime factors, remains valid and is not contradicted by (12).

The new information is an exact cancellation mechanism within
the approved witness test, beyond the prior warning that a signed
complement could cancel. It justifies continuing, if pursued, by
grouping the complete resonant form rather than treating all
complement terms as oscillatory. It does not settle either of the
approved quotient thresholds or certify progress beyond the
literature checked.

## Mathlib

Full matching coverage is unchecked. Finite Dirichlet convolution,
unique prime factorization, Cauchy–Schwarz, and elementary estimates
for exponentials are supporting ingredients, not a verified formal
theorem for this moving-heat real-prime witness. No absence claim is
made. The PNT is imported by the precise primary reference above;
its fixed-interval specialization and all finite taper/heat changes
needed here are justified explicitly.
