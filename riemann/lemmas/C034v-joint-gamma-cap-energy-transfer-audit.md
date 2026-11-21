# C034v: joint gamma cap and absolute energy transfer, reproduced audit

## Hypotheses

Use C034r's actual theta kernel \(\Phi\), space
\(E=L^2(\mathbb R,e^{-y/2}dy)\), translations
\(T_rf(y)=f(y+r)\), and convolution convention. Fix \(q=2\) and
\(Q=\log2\). All arithmetic indices are positive integers. For real
\(X\ge2\), put \(I_X=(X/2,X]\) and define
\[
 A(y)=(4\pi^2e^{9y/2}-6\pi e^{5y/2})e^{-\pi e^{2y}},\qquad
 B(y)=-2\pi e^{5y/2}e^{-\pi e^{2y}}.
\]
For \(j=0,1\), set
\[
 \nu_0(d)=\mu(d),\quad \nu_1(d)=\mu(d)\log(X/d),\quad
 a_j(k)=\sum_{d\mid k,\ d\in I_X}\nu_j(d),
\]
\[
 \kappa_j=\sum_{d\in I_X}\nu_j(d)/d,\quad
 m_j=\sum_{d\in I_X}\nu_j(d),\quad
 D_j^c(u)=-\sum_{d\in I_X}\nu_j(d)(\{u/d\}-1/2).
                                                               \tag{1}
\]
The fractional part is zero at integers: these are right-hand,
after-jump values. For integer \(M\ge X\), define
\[
 \begin{split}
 G_{j,X,M}h&=\sum_{k\le M}a_j(k)k^{-1/2}
                          T_{\log(k/X)}(A*h),\\
 B_{j,X,M}h&=\kappa_j\sqrt M\,T_{\log(M/X)}(B*h),\\
 C_{j,X,M}&=G_{j,X,M}-B_{j,X,M},\\
 U_X^{(j)}h&=\sum_{d\in I_X}\nu_j(d)d^{-1/2}
                          T_{\log(d/X)}C_\Phi h .
 \end{split}                                                    \tag{2}
\]
In particular \(U_X^{(1)}=U_X\) from C034r. No divisor column or
prime power is removed from \(G\). For integer \(T\ge\lceil X\rceil\),
let \(M_*(X,T)\) be the least integer minimizing
\[
 |D_0^c(k)|^2+Q^{-2}|D_1^c(k)|^2,\qquad T\le k<2T.                \tag{3}
\]
The finite nonempty set and tie rule specify one cap without reference
to \(h\). The operator estimates below hold on \(E\); their notebook
application is exactly C034r's fixed compact smooth
\(h=-g''+g/4\), \(g=e^{-1/(1-y^2)}1_{|y|<1}\).

## Conclusion

There are constants \(C,c_\mu>0\) and \(X_0\ge2\), independent of
\(X,T,h\), such that for \(j=0,1\) and the cap (3),
\[
 \|C_{j,X,M_*}-U_X^{(j)}\|_{E\to E}
 \le C\{X^{1/4}T^{-1/4}+X^{5/4}T^{-3/4}\}.                      \tag{4}
\]
For \(T=\lceil X^3\rceil\) and \(X\ge X_0\),
\[
 \left|\|C_{1,X,M_*}h\|_E^2-\|U_Xh\|_E^2\right|
 \le C\{e^{-c_\mu f_0(\log X)}+X^{-1}\}\|h\|_E^2,
 \quad f_0(L)=L^{3/5}(\log L)^{-1/5}.                            \tag{5}
\]
Thus the right side is \(o(1)\) for the fixed input. This supplies
C034u(5)'s separate premise with \(V_X=C_{1,X,M_*}h\); its conclusion
(6) therefore applies to that vector without an additional GC6
assumption. The completed energy is always
\[
 \|G-B\|^2=\|G\|^2-2\Re\langle G,B\rangle+\|B\|^2.             \tag{6}
\]
No bound for either signed primitive sector, subpower source-energy
bound, cumulative-energy upper, or actual-Xi mixed positivity follows.
The onset \(X_0\) is existential here, not a certified decimal cutoff.

## Proof

### 1. Sources, scope and reason for reproduction

This audits the assertion already made by Leonard van Hemert,
*Exact Zero Detection and Compact Arithmetic Realizations for the
Riemann Xi Function*, v1.0.0, 11 October 2026,
DOI 10.5281/zenodo.23295277,
[tagged primary TeX](https://raw.githubusercontent.com/LeonardSEO/riemann-xi-zero-detection/refs/tags/v1.0.0/paper/paper.tex),
subsection `sec:integer-gamma-completion`, theorem
`thm:joint-integer-gamma-completion`, GC1-GC11, lines11382-11600.
The complete setup, theorem and proof were retrieved for this audit.
The manuscript is not treated as a reviewed proof of its other claims.
The prior SPECIALIZE assessment2092/source-notes2093 covers precisely
this reproduction. Its purpose is to verify the compressed cap,
weighted-space and endpoint arguments before using the energy premise.
There is no claim of a bound beyond that source.

The sole analytic-number-theory theorem imported below is Ethan
Simpson Lee and Nicol Leong, *New explicit bounds for Mertens function
and the reciprocal of the Riemann zeta function*,
[arXiv:2208.06141v5](https://arxiv.org/html/2208.06141v5),
9 September 2026, Theorem2.2(20),(23), Table1 third block and Section5.4.
We fix its row \(W=54,\mathcal R_3=5223,x_3(54)\).
The theorem and row qualifications were inspected; its computational
certificates and general analytic proof are imported, not replayed.
The other named inputs are periodic Parseval, the Fourier transform
of squared sinc, Young's inequality, finite Abel summation,
Cauchy-Schwarz and density of compact smooth functions in weighted
\(L^2\). The applications and convergence issues are checked below.
C034r supplies the theta normalization and bounded derivative
convolution; C034u is used only for the final finite-sector interface.

### 2. Uniform arithmetic variance

For \(r\ge1,Y>0\), write
\(b_r(Y)=\sum_{n\le Y,(n,r)=1}\mu(n)/n\).
When \(Y\ge1\), interchanging finite divisor sums shows that
\[
 S_r(Y)=\sum_{n\le Y,(n,r)=1}\mu(n)\lfloor Y/n\rfloor
\]
counts integers at most \(Y\) all of whose prime factors divide \(r\).
Indeed the divisor sum at an integer is
\(\prod_{p\mid k,\ p\nmid r}(1-1)\). Hence
\(0\le S_r(Y)\le Y\), while
\(|Yb_r(Y)-S_r(Y)|\le\lfloor Y\rfloor\le Y\).
Thus \(-1\le b_r(Y)\le2\). For \(0<Y<1\), \(b_r(Y)=0\),
so the same bound holds.

Let \(A_r^{(j)}=\sum_{d\in I_X,r\mid d}\nu_j(d)/d\).
It vanishes for nonsquarefree \(r\). If \(r\) is squarefree,
\(\mu(rn)=\mu(r)\mu(n)1_{(n,r)=1}\), including nonsquarefree \(n\).
With \(Y=X/r\), finite Abel summation gives
\[
 A_r^{(0)}=\frac{\mu(r)}r[b_r(Y)-b_r(Y/2)],\qquad
 A_r^{(1)}=\frac{\mu(r)}r\int_{Y/2}^Y
                           [b_r(t)-b_r(Y/2)]\frac{dt}{t}.        \tag{7}
\]
For the second identity, each atom \(n\in(Y/2,Y]\) contributes
\(\int_n^Ydt/t=\log(Y/n)\); an atom at \(Y/2\) is subtracted.
This includes real/integer endpoints and empty windows. Consequently
\[
 |A_r^{(0)}|\le3/r,\qquad |A_r^{(1)}|\le3Q/r.                    \tag{8}
\]

Use cycles-frequency \(e^{2\pi i\lambda u}\) only in this periodic
calculation. The function \(s(u)=\{u\}-1/2\) has mean zero and
nonzero Fourier coefficient \(-1/(2\pi i k)\). Its values at jumps
do not affect integrals. On a common period of \(s(u/d),s(u/e)\),
Parseval pairs their common frequencies \(\ell/(d,e)\), giving
\[
 \langle s(\cdot/d),s(\cdot/e)\rangle_{
 \mathrm{period}}=\frac{(d,e)^2}{4\pi^2de}
                    \sum_{\ell\ne0}\ell^{-2}
                  =\frac{(d,e)^2}{12de}.                       \tag{9}
\]
The bracket denotes normalized period integration. Let
\(P=\operatorname{lcm}(1,\ldots,\lfloor X\rfloor)\).
The identity \((d,e)^2=\sum_{r\mid d,r\mid e}J_2(r)\),
\(J_2(r)=r^2\prod_{p\mid r}(1-p^{-2})\), follows prime by prime
by telescoping. Since all \(\nu_j\) are real, (9) yields exactly
\[
 V_j=P^{-1}\int_0^P|D_j^c(u)|^2du
     =\frac1{12}\sum_{r\le X}J_2(r)|A_r^{(j)}|^2,
 \quad V_0\le3X/4,\quad V_1\le3Q^2X/4.                         \tag{10}
\]
Here \(J_2(r)\le r^2\) and (8) pay each term.

All nonzero Fourier frequencies of \(D_j^c\) are reduced fractions
\(a/b\), \(a\ne0,b\le X\), with coefficient
\(A_b^{(j)}/(2\pi i(a/b))\): the contributing \(d\)'s are exactly
the multiples of \(b\), and their original Fourier index is \(ad/b\).
For distinct such fractions the nonzero integer cross-determinant
gives separation at least \(1/(bb')\ge X^{-2}\).

### 3. Interval estimate and a single integer cap

For any bounded interval \(I\) of length \(\ell\), put
\(\eta=(2X^2)^{-1}\),
\[
 K_\eta(u)=\eta\left(\frac{\sin(\pi\eta u)}{\pi\eta u}\right)^2,
 \qquad W_I=\frac{\pi^2}{4}1_{I^+}*K_\eta,
\]
where \(I^+\) extends \(I\) by \(1/\eta\) at each end.
The squared-sinc transform gives \(\int K_\eta=1\) and Fourier
support \([-\eta,\eta]\). For \(u\in I\), the convolution includes
\(|v|\le1/(2\eta)\); on this subinterval
\(K_\eta(v)\ge4\eta/\pi^2\). Hence \(W_I(u)\ge1\), while
\[
 \int W_I=\frac{\pi^2}{4}(\ell+4X^2),\qquad
 \operatorname{supp}\widehat W_I\subset[-\eta,\eta].
\]
Take a finite symmetric truncation of the ordinary \(P\)-periodic
Fourier series of \(D_j^c\). Its nonzero frequencies have the
separation just proved. In the integral of its squared modulus
against \(W_I\), every off-diagonal frequency is therefore annihilated.
The result is \((\int W_I)\) times its coefficient square sum,
which is at most \((\int W_I)V_j\). These truncations converge in
\(L^2([0,P])\), and therefore in \(L^2(I)\) by periodicity and a
finite covering. Passing only the unweighted \(I\)-integral to the
limit proves
\[
 \int_I|D_j^c|^2\le\frac{\pi^2}{4}(\ell+4X^2)V_j.               \tag{11}
\]
No weighted whole-line convergence or Fourier value at a jump is used.

For integer \(k\) and \(0\le s<1\), every jump of
\(\{u/d\}\) occurs at an integer, so exactly
\(D_j^c(k+s)=D_j^c(k)-\kappa_js\).
Using \(|a+b|^2\le2|a|^2+2|b|^2\) and integrating in \(s\) gives
\[
 |D_j^c(k)|^2\le2\int_k^{k+1}|D_j^c(u)|^2du
                                      +\frac23|\kappa_j|^2.    \tag{12}
\]
By (8) at \(r=1\), \(|\kappa_0|\le3\) and
\(|\kappa_1|\le3Q\). Sum (12) over precisely the \(T\) integers
\(T\le k<2T\), combine the two \(j\)'s with weights \(1,Q^{-2}\),
and apply (10)-(11) to \([T,2T]\). The average score is at most
\[
 \frac{3\pi^2}{4}X(1+4X^2/T)+12
 \le(3\pi^2+6)(X+X^3/T),                                      \tag{13}
\]
where \(X\ge2\) pays the last constant. A minimum is at most its
average, so the same cap (3) satisfies, for both \(j\),
\[
 |D_j^c(M_*)|\le C(\sqrt X+X^{3/2}T^{-1/2}).                    \tag{14}
\]
This includes \(T=\lceil X\rceil\) and all ties. No input-dependent
cap has been selected.

### 4. Pointwise mean boundary and the weighted-space remainder

Direct differentiation gives \(A=B'+B/2\). For \(y\to-\infty\),
\(A,B,A',B'\) are \(O(e^{5y/2})\). At \(+\infty\) each is a
polynomial in \(e^{y/2}\) times \(e^{-\pi e^{2y}}\).
Thus their products with \(e^{-y/4}\) are in \(L^1\).
Weighted Young and C034r's translation formula give bounded
convolutions, \(\|T_r\|=e^{r/4}\), and differentiation after
convolution in operator norm. For \(u>0\), define the operator
\[
 F_X(u)=u^{-1/2}T_{\log(u/X)}C_A.
\]
Then
\[
 F_X'(u)=u^{-3/2}T_{\log(u/X)}(C_{A'}-C_A/2),
\]
\[
 \|F_X(u)\|\le C X^{-1/4}u^{-1/4},\qquad
 \|F_X'(u)\|\le C X^{-1/4}u^{-5/4}.                            \tag{15}
\]
For example, differentiability follows by conjugating with
\(Jf=e^{-y/4}f\) and applying translation continuity in \(L^1\)
to the weighted derivative kernel. It does not differentiate \(h\).

First let \(h\in C_c^\infty\). C034r's theta normalization also gives
on the full real axis
\[
 \Phi(y)=\sum_{n\ge1}n^{-1/2}A(y+\log n).                       \tag{16}
\]
Indeed for \(p(y)=e^{y/2}\sum_{n\ge1}e^{-\pi n^2e^{2y}}\),
\(p''-p/4\) is the series on the right, and C034r's Poisson relation
makes it even with value \(\Phi\) for \(y\ge0\). The series and
its derivatives converge absolutely uniformly on every compact
\(y\)-set. Compact support of \(h\) allows convolution and the
finite \(d\)-sum to pass through it. Grouping by \(k=dn\) gives
pointwise, normally on compact sets,
\[
 U_X^{(j)}h=\sum_{k\ge1}a_j(k)F_X(k)h.                          \tag{17}
\]
This is not claimed to be an absolutely convergent series in \(E\).

The right-continuous summatory function is exactly
\[
 \sum_{k\le u}a_j(k)=\sum_{d\in I_X}\nu_j(d)\lfloor u/d\rfloor
                   =\kappa_j u+D_j(u),\quad
 D_j=D_j^c-m_j/2.                                              \tag{18}
\]
Finite Abel summation on \((M,N]\), with integer endpoints, gives
\[
 \sum_{M<k\le N}a_j(k)F_X(k)h
 =\kappa_j\int_M^N F_X(u)h\,du
  +D_j(N)F_X(N)h-D_j(M)F_X(M)h
  -\int_M^N D_j(u)F_X'(u)h\,du.                               \tag{19}
\]
The head includes its atom at \(M\); this is why the tail is strict.
For compact inputs, the primitive of the mean integrand is pointwise
\(\sqrt u\,T_{\log(u/X)}(B*h)\), by \(A=B'+B/2\).
For fixed \(y\), its value tends to zero at infinity by the gamma
tail, uniformly over the compact support integrated against \(h\).
Therefore
\[
 \int_M^\infty F_X(u)h\,du
       =-\sqrt M\,T_{\log(M/X)}(B*h)                            \tag{20}
\]
pointwise. No absolute Bochner integral for (20) is asserted.

For fixed \(X\), both \(D_j,D_j^c\) are bounded functions of \(u\).
By (15), \(F_X(u)\to0\) in operator norm and
\(\int_M^\infty\|F_X'(u)\|du<\infty\). Thus the remaining
integrals in (19) converge absolutely in operator norm. Their action
on a compact input agrees almost everywhere with the pointwise
integral: weighted \(L^2\) embeds continuously into \(L^1\) on
bounded physical intervals, so Bochner convergence and Fubini there
identify the two limits. Taking \(N\to\infty\) in (19), using
(17),(20), proves in \(E\)
\[
 U_X^{(j)}h=C_{j,X,M}h+R_{j,X,M}h,\qquad
 R_{j,X,M}=-D_j^c(M)F_X(M)-\int_M^\infty D_j^c(u)F_X'(u)du.       \tag{21}
\]
To obtain the centered formula, the contribution of the constant
\(-m_j/2\) in (18) is exactly
\((m_j/2)[F_X(M)+\int_M^\infty F_X'(u)du]=0\).
This cancellation is justified in operator norm by (15), separately
from the pointwise mean calculation.

For \(Y\ge M\), (10)-(11) and Cauchy-Schwarz show
\[
 \begin{split}
 \int_Y^{2Y}|D_j^c(u)|u^{-5/4}du
 &\le Y^{-5/4}Y^{1/2}
                   \left(\int_Y^{2Y}|D_j^c(u)|^2du\right)^{1/2}\\
 &\le C\{\sqrt X\,Y^{-1/4}+X^{3/2}Y^{-3/4}\}.                 \tag{22}
 \end{split}
\]
Sum over \(Y=2^\ell M\), \(\ell\ge0\). The two geometric ratios
are \(2^{-1/4}\) and \(2^{-3/4}\), strictly below one.
Multiplying by \(X^{-1/4}\) from (15), and using (14) for the
endpoint in (21), bounds its remainder by
\(C(X^{1/4}T^{-1/4}+X^{5/4}T^{-3/4})\), since \(M\ge T\).
Every finite operator in (2) is bounded. Density of \(C_c^\infty\)
in \(E\) therefore extends (21) and the bound to every input.
This proves (4) with constants uniform in \(X,T,h\).

### 5. Lee-Leong reduction and operator Abel endpoints

Use the fixed third-block row of the cited Theorem2.2. Its parameter
\(W=54\) is allowed by Section5.4 and exceeds \(Z_3=53.989\).
Keep its paired \(\mathcal R_3=5223\) and exact threshold \(x_3(54)\).
In its (20), \(\mathcal H=3000175332800\) is fixed and
\(c_3(x)\le c_3(x_3(54))<\infty\) on the required range.
The tabulated decimals \(\log\log x_3=10.01\), \(c_3=22.19\)
are not used as independently rounded bounds. The source's finite
zero verification is part of its unconditional theorem, not global RH.

Put \(a=(5/(3\cdot54^3))^{1/5}>0\). For sufficiently large \(x\)
above that exact threshold, the exponential coefficient in (23) is
at least \(a\), since \(0<1-\log54/\log\log x<1\).
Writing \(L=\log x\), the theorem consequently bounds the Mertens
function \(\mathfrak M(x)=\sum_{n\le x}\mu(n)\) by
\(C xL e^{-a f_0(L)}\).
Now \(\log L/f_0(L)=L^{-3/5}(\log L)^{6/5}\to0\), so after
enlarging the threshold,
\[
 |\mathfrak M(x)|\le Cx e^{-c_0 f_0(\log x)},\qquad c_0=a/2>0.   \tag{23}
\]
Only weakening of the cited bound has occurred.
The derivative
\[
 f_0'(L)=\tfrac15L^{-2/5}(\log L)^{-1/5}(3-1/\log L)
\]
is eventually positive and at most one. Choose \(X_0\) so that
\(X/2\) is above all preceding thresholds and \(L-Q\) is in this
derivative range whenever \(X\ge X_0\). Then for every
\(u\in[X/2,X]\),
\(f_0(\log u)\ge f_0(\log X)-Q\).
Absorbing \(e^{c_0Q}\) into the constant makes (23) uniform on the
entire closed window with exponent \(c_\mu=c_0\).

Let
\[
 K_X(u)=\log(X/u)u^{-1/2}T_{\log(u/X)}C_\Phi,
                         \qquad X/2\le u\le X.
\]
C034r proves boundedness of \(C_\Phi,C_{\Phi'}\) and the necessary
weighted kernel differentiation. Thus in operator norm
\[
 K_X'(u)=u^{-3/2}T_{\log(u/X)}
       [-(1+\tfrac12\log(X/u))C_\Phi+\log(X/u)C_{\Phi'}],
\]
\[
 \|K_X(u)\|\le C u^{-1/2},\qquad
 \|K_X'(u)\|\le C u^{-3/2}.                                   \tag{24}
\]
These use \(0\le\log(X/u)\le Q\) and
\(\|T_{\log(u/X)}\|=(u/X)^{1/4}\le1\).
Finite Abel summation, valid also for integer endpoints, is
\[
 U_X=\mathfrak M(X)K_X(X)-\mathfrak M(X/2)K_X(X/2)
                        -\int_{X/2}^X\mathfrak M(u)K_X'(u)du.  \tag{25}
\]
The lower count includes its endpoint, thereby excluding that atom
from \((X/2,X]\). The upper term vanishes because \(K_X(X)=0\),
even when \(X\) is an integer. The lower boundary is retained.
Combining (23)-(25), its bound is \(C\sqrt{X/2}e^{-c_\mu f_0(\log X)}\),
and the integral costs at most
\(Ce^{-c_\mu f_0(\log X)}\int_{X/2}^X u^{-1/2}du\).
Consequently
\[
 \|U_X\|_{E\to E}\le C\sqrt X e^{-c_\mu f_0(\log X)}.           \tag{26}
\]
No derivative or smoothness of an arbitrary \(E\)-input was assumed.

### 6. Absolute energy and its limited downstream consequence

For \(T=\lceil X^3\rceil\), the two terms of (4) are bounded by
\(X^{-1/2}\) and \(X^{-1}\). In (21) put \(U=U_Xh\) and
\(r=R_{1,X,M_*}h\), so \(C_{1,X,M_*}h=U-r\).
The exact Hilbert-space expansion and Cauchy-Schwarz give
\[
 \big|\|U-r\|^2-\|U\|^2\big|\le2\|U\|\|r\|+\|r\|^2.
\]
Here (26) bounds the cross product by
\(Ce^{-c_\mu f_0(\log X)}\|h\|^2\), while the remainder square
is at most \(CX^{-1}\|h\|^2\). This proves (5).
All estimates used the completed vector, so (6)'s boundary square
and cross term are retained rather than silently dropped.

Applying C034u's already proved conditional inequality with this
verified error gives precisely the stated interface consequence.
It still contains its full signed main term and high primitive
complement. Neither is bounded here. No cumulative integration,
growing input, zero selection, rightmost zero, positivity assumption
or RH-equivalent estimate was used. This is a successful local
reproduction of GC5/GC6; it supplies no new result beyond those claims.

## Mathlib

Full matching coverage for the joint cap, completed gamma transfer
and Lee-Leong input has not been checked. The proof uses standard
Parseval, Young, finite Abel summation, weighted \(L^2\) translations,
Bochner integration, Cauchy-Schwarz and density as stated above.
No full formal theorem, absence from Mathlib, or machine verification
is claimed. The external computational theorem remains a cited input.
