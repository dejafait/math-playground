# Corollary 466l: normalized third marginal and partial actual-law signs

## Hypotheses

Use C466k's actual function \(h(z)=\xi(1/2+\sqrt z)/c_0\),
\(c_0=\xi(1/2)>0\), and normalized density \(p=\theta_1\).
In particular, \(p\in C^\infty(\mathbb R)\) is zero on
\(( -\infty,0]\), positive on \((0,\infty)\), has mass one,
and has Laplace transform \(1/h(z)\) for \(\operatorname{Re}z>0\).
Retain all inherited C466a/L018 conventions and the external strip,
symmetry, paired-product, counting and verified-low-zero qualifications.
The imported density construction and those external inputs are not
independently verified here. No global PF, Gaussian-mixture assertion,
RH, simplicity or extra verified zeros are assumed.

Put \(B(s)=\log h(s)\), \(x=B'(1)>0\), \(S=3x\), and
\[
 q(u)=h(1)e^{-u}p(u),\qquad F(t)=A_x(1+it)
       =\frac{e^{x(1+it)}}{h(1+it)}.
\]
C466k establishes that \(q\) is a probability density of mean \(x\),
the complex asymptotic expansion used below, and every polynomially
weighted absolute-inversion bound on the original line.

## Conclusion

Define the absolutely convergent marginal and its opposed slice by
\[
 M(a,b)=\int_{\mathbb R}F(t+a)F(t+b)F(t-a-b)\,dt,
 \qquad K(r)=\operatorname{Re}M(r,0).
\]
With \(\mathcal D_3(p;x)=-\det[p^{(i+j)}(x)]_{i,j=0}^2\),
\[
 \mathcal D_3(p;x)=\frac1{2(2\pi)^3}
 \int_{\mathbb R^2}(a-b)^2(2a+b)^2(a+2b)^2
                   \operatorname{Re}M(a,b)\,da\,db.       \tag{1}
\]
The integral is absolutely convergent before taking its real part.
For \(\Theta=p/c_0\), multiply the right side by \(c_0^{-3}\).
The polynomial at \((a,b)=(r,0)\) is \(4r^6\), not zero when
\(r\ne0\).

At the specified total \(S\), the three full copies of \(q\) have a
continuous conditional version with positive normalizer
\(Z(S)=(q*q*q)(S)\). With respect to that version,
\[
 K(r)=\frac{2\pi e^{3x}}{h(1)^3}Z(S)
       \mathbb E[\cos(r(U_1-U_3))\mid U_1+U_2+U_3=S].      \tag{2}
\]
Equivalently, with \(T_S=\{(u,v):u>0,v>0,u+v<S\}\),
\[
 K(r)=2\pi\int_{T_S}p(u)p(v)p(S-u-v)
                  \cos(r(2u+v-S))\,du\,dv.               \tag{3}
\]
Consequently
\[
 K(r)>0\quad\left(|r|\le\frac{\pi}{2S}\right),\qquad
 K(r)|h(1+ir)|^2\longrightarrow 2\pi p(S)>0
                         \quad(|r|\longrightarrow\infty).\tag{4}
\]
The second conclusion gives strict positivity beyond an existential
finite onset. No effective onset or sign on the intervening bounded
frequency region is supplied. The all-real slice test is unresolved.
Even a positive entire slice would leave the full two-frequency sign,
all orders/all x and density-to-Xi transfer open. This is a local
partial result from attempt932, validated by the step934 audit below,
not a candidate proof of RH or a negative actual density minor.

## Proof

### The bilinear identity and its exact real-coordinate specialization

Import Andreief's complex bilinear integration identity from Giulio
Ruzza, *Introduction to Random Matrix Theory, Riemann-Hilbert problems,
and Universality*, 4 May 2022 notes,
[Lemma 3.1.1, pp.27-28](https://webpages.ciencias.ulisboa.pt/~gruzza/introRMT.pdf),
also Peter Forrester,
[arXiv:1806.10411v1, (1.7), Section 2.2](https://arxiv.org/pdf/1806.10411v1).
Every complex cross-product must be in \(L^1\); the identity contains
\(3!\) and no conjugation. Reuse the complete source inspections in
reviews925/930. Only its needed specialization is given here.

C466k(7) gives
\[
 p^{(j)}(x)=\frac1{2\pi}\int_{\mathbb R}(1+it)^jF(t)\,dt
 \quad(0\le j\le4).
\]
Take \(f_i(t)=(1+it)^i\),
\(g_j(t)=(1+it)^jF(t)/(2\pi)\), \(0\le i,j\le2\).
All nine cross-products have degree at most four and are absolutely
integrable by C466k(6). If
\(\Delta(t)=\prod_{i<j}(t_j-t_i)\), then
\(\Delta(1+it_1,1+it_2,1+it_3)=i^3\Delta(t)\).
Its algebraic square is \(-\Delta(t)^2\); this cancels the minus
in \(\mathcal D_3\). Thus
\[
 \mathcal D_3(p;x)=\frac1{6(2\pi)^3}
       \int_{\mathbb R^3}\Delta(t)^2\prod_{j=1}^3F(t_j)
                                  \,dt_1dt_2dt_3.          \tag{5}
\]
There is no replacement by a conjugate Gram determinant.

Absolute integrability also follows directly from
\[
 |\Delta(t)|^2\le 8\prod_{j=1}^3(1+t_j^2)^2,
 \qquad\int_{\mathbb R}(1+t^2)^2|F(t)|\,dt<\infty.
\]
Make the invertible real change of variables
\[
 t_1=t+a,\quad t_2=t+b,\quad t_3=t-a-b.
\]
Its matrix, with columns \((t,a,b)\), is
\(\left(\begin{smallmatrix}1&1&0\\1&0&1\\1&-1&-1\end{smallmatrix}\right)\)
and has determinant \(3\). The squared Vandermonde becomes
\((a-b)^2(2a+b)^2(a+2b)^2\), independent of \(t\).
The change-of-variables theorem and absolute Fubini therefore give
(1), including its factor \(3/6\).

The marginal is continuous in \((a,b)\). Indeed, on a compact set
of shifts the fixed-line decay bounds each shifted \(F\) by
\(C_N(1+|t|)^{-N}\), for every fixed \(N\), and the factors are
continuous. Dominated convergence applies. On the opposed slice,
conjugation followed by \(t\mapsto-t\) leaves the integral unchanged,
so \(M(r,0)\) is real and equals \(K(r)\). A negative value at a
nonzero \(r\), if found, would give a negative open patch in the
weighted marginal in (1), by continuity and \(4r^6>0\). This would
refute pointwise nonnegativity of that marginal, not the sign of its
full integral. No such value is established here.

### Complex convolution, the specified conditioning value and constants

Use angular Fourier convention
\(\widehat f(t)=\int e^{-itu}f(u)\,du\). Import the complex
\(L^1\) convolution theorem from Christopher Heil,
[*The Fourier Transform on L1(R)*, Fall 2009 convolution extract,
Theorem 1.23(a)-(d), pp.16-17](https://heil.math.gatech.edu/7338/fall09/convolution.pdf).
His \(2\pi\)-frequency convention is converted by evaluating his
transform at \(t/(2\pi)\). For pointwise inversion use David Jerison,
[*Fourier Integrals on L2(R) and L1(R)*, MIT18.103 Fall 2013,
Corollary 4 and Proposition 2 with Theorem 2, pp.2-4](https://math.mit.edu/~jerison/103/handouts/fourierint1.13.pdf).
These are imported results, not reproved identities. Review930 has
the full relevant proof inspections and their limitations.

Here \(\widehat q(t)=h(1)/h(1+it)\) is integrable and bounded by one.
C466k's inversion identifies \(q\) with its bounded uniformly
continuous inverse transform everywhere. In particular
\(q\in L^1\cap L^\infty\). For fixed real \(r\), put
\(q_+(u)=e^{-iru}q(u)\), \(q_-(u)=e^{iru}q(u)\), and
\(g_r=q_+*q*q_-\). All three factors are bounded uniformly
continuous \(L^1\) functions. Their iterated convolution is in
\(L^1\cap L^\infty\subset L^2\) and is continuous: for example,
translation continuity of the bounded uniformly continuous final
factor, dominated by the other two \(L^1\) factors, proves the last
assertion. The cited convolution theorem gives
\[
 \widehat g_r(t)=
 \frac{h(1)^3}{h(1+i(t+r))h(1+it)h(1+i(t-r))}.              \tag{6}
\]
This is in \(L^1\), since two characteristic-function factors are
bounded by one and the third is integrable; it is also in \(L^2\).
Jerison's inversion therefore agrees almost everywhere with its
absolutely convergent continuous inverse integral. Continuity of
\(g_r\) makes the equality hold at every real argument. In particular
\[
 M(r,0)=\frac{2\pi e^{3x}}{h(1)^3}g_r(S),\quad
 g_r(S)=\int_{T_S}q(u)q(v)q(S-u-v)e^{-ir(2u+v-S)}\,du\,dv.\tag{7}
\]
Both expressions retain their complex phases before using symmetry.
Absolute Fubini for the convolution is covered by the bounded last
factor and the two \(L^1\) factors. No delta-function argument is used.

For three independent copies with density \(q\), the map
\((u,v,w)\mapsto(u,v,y=u+v+w)\) has determinant one. Their joint
density in the new coordinates is \(q(u)q(v)q(y-u-v)\).
Its marginal \(Z(y)=(q*q*q)(y)\) is continuous and finite.
For every \(y>0\) it is strictly positive: a small neighborhood
of \((y/3,y/3)\) lies in \(T_y\), and its three continuous density
factors are strictly positive. Thus for every \(y>0\), not merely
almost every one, the conditional version is
\[
 d\mu_y(u,v)=\frac{q(u)q(v)q(y-u-v)}{Z(y)}\,du\,dv,
 \qquad (u,v)\in T_y,\quad U_3=y-u-v.                      \tag{8}
\]
This is a version of the conditional law because its product with
\(Z(y)dy\) gives the joint density just calculated. It is continuous
in \(y>0\) against bounded continuous test functions on the triple:
dominate the numerator by
\(\|q\|_\infty q(u)q(v)\) times the test bound, and apply dominated
convergence on \(\mathbb R^2\), then divide by continuous positive
\(Z(y)\). This pays evaluation at \(y=S\).

Exchange of the first and third coordinates preserves this law and
reverses the phase in (7), making that integral real. Equations
(7)-(8) give (2). On \(T_S\), the product of the three tilting
factors is exactly \(h(1)^3e^{-S}\). Since \(S=3x\), it cancels
the prefactor in (7), proving (3). In particular
\(K(0)=2\pi(p*p*p)(S)>0\), with all convolution values taken in
their continuous version on the positive axis.

The conditioning does not preserve independence, even in the weaker
form of a mixture of identically distributed independent pairs.
Under \(\mu_S\), each of \(U_1>S/2\) and \(U_3>S/2\) has strictly
positive probability, but their intersection is empty. A mixture
of iid pairs would instead have intersection probability
\(\mathbb E a^2\ge(\mathbb E a)^2>0\), where \(a\) is the component
tail probability. Thus the natural conditional-pair square argument
cannot be used. This does not exclude an unrelated factorization of
the difference law alone. The independent-difference formula in
Iksanov, [Xi'an 2019 notes, Proposition 117 and Corollary 119,
pp.65-66](https://do.csc.knu.ua/wp-content/uploads/2023/01/Char_funct_XIan2019.pdf),
has no application to the dependent pair without additional input.

Since \(|2u+v-S|<S\) on \(T_S\), the cosine in (3) is strictly
positive for \(|r|\le\pi/(2S)\). The positive density factors and
nonempty triangle prove the first claim in (4), including its endpoints.
This small-frequency argument does not extend to arbitrary \(r\).

### Large-frequency modulus and the normalized integral

The further sign argument uses the actual complex growth of \(h\),
not positivity or symmetry of a generic conditional density. Set
\(b(v)=\log|h(1+iv)|\). This is a finite continuous even function,
because the right half-plane is zero-free and \(h\) has conjugate
symmetry. C466k(4), inherited from C466a's sector estimate, states
\[
 B(z)=\frac{\sqrt z}{2}\left(\log\frac{\sqrt z}{2\pi}-1\right)
       +\frac78\log z+C+O(|z|^{-1/2})                       \tag{9}
\]
uniformly for large \(z\) in the closed right half-plane. This is
the specified analytic logarithm there, not a branch through a zero.

For \(v\to+\infty\),
\(\sqrt{1+iv}=\sqrt{v/2}(1+i)+O(v^{-1/2})\) and
\(\log\sqrt{1+iv}=\tfrac12\log v+i\pi/4+O(v^{-1})\).
Taking real parts in (9) gives
\[
 b(v)=\kappa\sqrt v\log v+\lambda\sqrt v+
                 \frac78\log v+C+O(\log v/\sqrt v),         \tag{10}
\]
where
\[
 \kappa=\frac1{4\sqrt2}>0,\qquad
 \lambda=-\frac{\log(2\pi)+1+\pi/4}{2\sqrt2}.
\]
For instance the adverse argument contribution is
\(-\sqrt{v/2}\,\pi/8\), which is included in \(\lambda\).
Only a modulus expansion is asserted here; no derivative of its
remainder will be assumed.

For \(r>0\), define
\[
 H_r(t)=\frac{e^{3ixt}}{h(1+it)}
       \frac{|h(1+ir)|^2}
            {h(1+i(t+r))h(1+i(t-r))}.
\]
The exact identity, before any limit, is
\[
 K(r)|h(1+ir)|^2=e^{3x}\int_{\mathbb R}H_r(t)\,dt.          \tag{11}
\]
For fixed \(t\), each of the two ratios of nearby \(h\)-values tends
to one. To justify this from (9), differentiate only its explicit
part, whose derivative is
\(\log(\sqrt z/(2\pi))/(4\sqrt z)+7/(8z)\).
It is \(O(\log r/\sqrt r)\) along the bounded vertical segment
from \(1\pm ir\) to \(1+i(\pm r+t)\). The difference of the two
remainders is \(O(r^{-1/2})\), using their values, not their
derivatives. Hence the difference of the logarithms tends to zero.
Conjugate symmetry gives \(|h(1+ir)|^2=h(1+ir)h(1-ir)\), so
\[
 H_r(t)\longrightarrow\frac{e^{3ixt}}{h(1+it)}.             \tag{12}
\]
Uniform absolute domination of (11), including \(t\) near \(\pm r\),
is essential. It is proved next.

### Three ranges giving uniform absolute domination

Write \(w(v)=\sqrt v\log v\) for \(v\ge e\) and
\[
 E_r(t)=b(t+r)+b(t-r)+b(t)-2b(r),\qquad |H_r(t)|=e^{-E_r(t)}.
\]
Evenness permits \(t\ge0\). We prove that, for some fixed
\(R,T,c,C_1>0\) and all \(r\ge R\),
\[
 |H_r(t)|\le C_1\quad(0\le t\le T),\qquad
 |H_r(t)|\le C_1e^{-c w(t)}\quad(t\ge T).                   \tag{13}
\]
This is an integrable bound on the full real axis.

First choose \(T\ge e\) sufficiently large that (10) holds above
\(T\), and
\[
 \tfrac9{10}\kappa w(v)\le b(v)\le\tfrac{11}{10}\kappa w(v)
 \quad(v\ge T).                                           \tag{14}
\]
Let \(g(v)\) denote the explicit four terms in (10). Its elementary
second derivative is \(O(\log v/v^{3/2})\). For \(r\) large and
\(0\le t\le r/2\), the symmetric second-difference estimate on
\([r/2,3r/2]\) and the value bound on the remainder in (10) give
\[
 b(r+t)+b(r-t)-2b(r)
       \ge -M\frac{t^2\log r}{r^{3/2}}-C_2\frac{\log r}{\sqrt r}.
                                                               \tag{15}
\]
Here \(M,C_2\) are fixed; the second remainder term is bounded
uniformly for large \(r\). No Cauchy disk crossing the boundary
of (9)'s sector, or unjustified differentiated remainder, is needed.

Choose \(0<\epsilon<1/2\) so small that
\[
 M\epsilon^{3/2}(1+\log(1/\epsilon))\le\kappa/4.            \tag{16}
\]
If \(T\le t\le\epsilon r\), put \(y=r/t\ge1/\epsilon\).
Since \(\log t\ge1\) and
\(y^{-3/2}(1+\log y)\) decreases for \(y\ge1\),
\[
 \frac{t^2\log r/r^{3/2}}{w(t)}
 =y^{-3/2}\frac{\log r}{\log t}
 \le\epsilon^{3/2}(1+\log(1/\epsilon)).                    \tag{17}
\]
Equations (14)-(17), using also \(b(t)\ge\kappa w(t)/2\),
show \(E_r(t)\ge b(t)/2-C_3\ge\kappa w(t)/4-C_3\).
For \(0\le t\le T\), enlarge \(R\) so that \(T\le\epsilon R\).
The same (15) bounds the deficit by a fixed constant, and \(b(t)\)
is bounded below on the compact interval. This proves (13) in the
small range, including its compact beginning.

For the comparable range \(\epsilon r\le t\le2r\), (10) implies
the uniform assertion
\[
 \sup_{0\le a\le3}
 \left|\frac{b(ar)}{\kappa\sqrt r\log r}-\sqrt a\right|
          \longrightarrow0.                              \tag{18}
\]
Here it is important that \(a=0\) is included. For \(ar\ge T\),
the leading-term discrepancy is
\(\kappa\sqrt r\sqrt a\log a\), uniformly \(O(\sqrt r)\)
because \(\sqrt a\log a\) extends continuously at zero. The
\(\lambda\)-term is also \(O(\sqrt r)\); the logarithmic term is
\(O(\log r)\), and the remainder is bounded for \(ar\ge T\).
For \(ar<T\), \(b(ar)\) is bounded on \([0,T]\), while the
proposed leading term is at most \(\kappa\sqrt T\log r\).
Dividing these estimates by \(\kappa\sqrt r\log r\) proves (18).

With \(s=t/r\), (18) gives, uniformly on \([\epsilon,2]\),
\[
 \frac{E_r(t)}{\kappa\sqrt r\log r}
 \longrightarrow f(s):=\sqrt{1+s}+\sqrt{|1-s|}+\sqrt s-2.
                                                               \tag{19}
\]
This continuous function is strictly positive for every \(s>0\).
For \(0<s<1\), use \(\sqrt{1+s}\ge1\) and
\(\sqrt{1-s}\ge1-s\) to obtain \(f(s)\ge\sqrt s-s>0\).
At \(s=1\) its value is \(\sqrt2-1>0\); for \(s\ge1\),
\(\sqrt{1+s}\ge\sqrt2\) and \(\sqrt s\ge1\) give the same
strict lower bound. Let \(m=\min_{[\epsilon,2]}f>0\).
For large \(r\), (19) is at least \(m/2\). Since
\(w(t)\le2\sqrt2\sqrt r\log r\) when \(t\le2r\) and \(r\ge2\),
\[
 E_r(t)\ge\frac{\kappa m}{4\sqrt2}w(t)
          \quad(\epsilon r\le t\le2r).                    \tag{20}
\]
This range explicitly covers \(t=r\), where one frequency is zero.

Finally let \(t\ge2r\), with \(r\ge T\). By (14),
\(b(t-r)\ge0\), \(w(t+r)\ge w(t)\), and
\(w(r)\le w(t)/\sqrt2\). Hence
\[
 E_r(t)\ge\kappa\left(\frac95-\frac{11}{5\sqrt2}\right)w(t).
                                                               \tag{21}
\]
The displayed coefficient is positive. This proof uses monotonicity
only of the explicit function \(w\), not an unproved monotonicity
of \(b\). Taking the smallest positive coefficient from the three
ranges and enlarging the constants proves (13). Integrability follows,
for example, from \(w(t)\ge\sqrt t\) for \(t\ge e\).

### The resulting partial sign and its limits

Apply dominated convergence in (11), using (12)-(13), and then
C466k(7) at the real argument \(S\):
\[
 \lim_{r\to\infty}K(r)|h(1+ir)|^2
 =e^{3x}\int_{\mathbb R}\frac{e^{iSt}}{h(1+it)}\,dt
 =2\pi e^{3x-S}p(S)=2\pi p(S)>0.                           \tag{22}
\]
Evenness of \(K\) and of \(|h(1+ir)|\) gives the negative-frequency
limit as well. Positivity of the limit and the nonzero denominator
give eventual strict positivity, proving (4).

The convolution and determinant formulas are routine applications of
the cited results. The actual-law normalized tail limit is the local
partial mathematical input obtained here; the approved bounded search
did not identify a matching source result, but this does not certify
originality. There is no effective tail threshold, numerical evidence,
contour deformation or finite-core approximation in the argument.
The compact region left between the proved local interval and the
existential tail remains unsigned. The common-product contour stop
C466k and the distinct chamber/conditional-core stops are preserved;
their failures do not refute cancellation on the original line.

### Critical audit, 14 November 2026, step934

The complete chain (1)-(22) passes this audit under the stated inherited
inputs. No conclusion is strengthened and no failed implication was
found. The representation steps specialize the already inspected
Andreief and Fourier theorems; their full statements and proof coverage
are reused from reviews925/930/933. This is a verification of the local
partial result, not an independent verification of the imported density,
the low-zero certificates, or the entire cited manuscript.

The normalization in (5) uses \(i^6=-1\), canceling exactly the sign
in \(\mathcal D_3\). The real determinant is \(+3\), giving
\(3/3!=1/2\) in (1); changing to \(\Theta\) contributes
\(c_0^{-3}\). Each variable has degree at most four in the absolute
Vandermonde bound, so C466k(6)-(7) pays every moment and Fubini use.
The convolutions in (6)-(7) retain the opposite modulations and the
angular-frequency factor \(2\pi\). The bounded continuous version
of \(q\), the bound \(\|q\|_\infty q(u)q(v)\), and positivity
on the open triangle justify (8) at the specified \(S>0\), as well
as its weak continuity. Independence is used before conditioning only.
The tilt factors cancel since \(S=3x\). Thus the distinct constants
\(K(0)=2\pi(p*p*p)(S)\) and the tail constant \(2\pi p(S)\)
have not been interchanged. The strict cosine argument includes the
endpoints \(|r|=\pi/(2S)\), since \(|U_1-U_3|<S\) throughout
the open triangle.

For the analytic step, taking real parts of (9) gives precisely the
\(\kappa\) and \(\lambda\) in (10), including
\(-\pi\sqrt{v/2}/8\). Fixed-\(t\) logarithm differences in
(12) use a bounded vertical segment in the large right-half-plane
region. The explicit derivative tends to zero there and the two
remainder values tend to zero; no derivative estimate for the error
or phase-discarding modulus substitution is needed.

Here is an explicit check of the quantifiers in the domination argument.
For the four-term function \(g\) in (15),
\[
 g''(v)=-\frac{\kappa\log v+\lambda}{4v^{3/2}}
         -\frac7{8v^2}.
\]
The symmetric-difference integral
\(\int_{-t}^{t}(t-|u|)g''(r+u)\,du\) has kernel mass \(t^2\).
For \(t\le r/2\) it is bounded below by the first deficit in
(15). If \(\rho=b-g\), then
\(\rho(r+t)+\rho(r-t)-2\rho(r)\) has absolute value at most
\(C_2\log r/\sqrt r\), solely from its three value bounds.
After fixing \(T\) and these constants, choose \(\epsilon\) by
(16), then take \(R\ge\max\{2T,T/\epsilon,2\}\), increasing
it to satisfy the finitely many asymptotic thresholds. This order
of choices is not circular. On \([T,\epsilon r]\), the deficit
is at most \(\kappa w(t)/4+C_3\le b(t)/2+C_3\); on
\([0,T]\) its bound and the compact minimum of \(b\) are uniform
in \(r\ge R\).

In (18), for \(ar\ge T\) the discrepancy divided by
\(\kappa\sqrt r\log r\) tends to zero uniformly because
\(\sqrt a\log a\) is bounded on \([0,3]\) after its continuous
extension. The lower-order terms have uniform bounds
\(O(\sqrt r)\), \(O(\log r)\), and \(O(1)\).
For \(ar<T\), the two terms to compare are bounded by a compact
bound for \(b\) and \(\kappa\sqrt T\log r\).
This proves the required uniformity even at \(a=0\); neither
(19) nor (20) applies a large-argument expansion at zero. The
continuous positive \(f\) has \(m>0\) on \([\epsilon,2]\).
In the far range the coefficient in (21) is positive since
\(9\sqrt2>11\), equivalently \(162>121\).

Consequently one may take any positive \(c\) no larger than
\[
 \min\left\{\frac\kappa4,
       \frac{\kappa m}{4\sqrt2},
       \kappa\left(\frac95-\frac{11}{5\sqrt2}\right)\right\}
\]
and enlarge \(C_1\) to cover the small-range constants. This gives
one integrable majorant for every \(r\ge R\); evenness covers
negative \(t\). Dominated convergence and C466k(7) then give (22)
with the exact cancellation \(e^{3x-S}=1\). Since \(p(S)>0\),
the eventual strict sign follows. These choices remain existential:
the audit supplies no numerical \(T,\epsilon,R\), positive lower
bound for \(p(S)\), or convergence rate. Intermediate frequencies,
the full marginal sign, all orders/all \(x\), and Xi transfer remain
open. This reproduction does not establish originality of the tail
argument beyond the source comparison already recorded.

## Mathlib

Full matching coverage has not been checked. The imported convolution,
Fourier inversion, change of variables, dominated convergence and
bilinear determinant identities are supporting mathematics, not a
formalization of (22) or an all-real sign theorem. No matching
declaration or absence claim is asserted. Unknown coverage is not
evidence of absence.
