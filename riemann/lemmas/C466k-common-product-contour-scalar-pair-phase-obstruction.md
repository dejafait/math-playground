# Corollary 466k: common product-contour scalar/pair phase obstruction

## Hypotheses

Use C466a's actual entire function
\(h(z)=\xi(1/2+\sqrt z)/c_0\), \(c_0=\xi(1/2)>0\),
and its normalized probability density \(p=\theta_1\). Thus
\(p\in C^\infty(\mathbb R)\), \(p=0\) on \(( -\infty,0]\),
\(p>0\) on \((0,\infty)\), and
\[
 \int_0^\infty e^{-zu}p(u)\,du=\frac1{h(z)}
 \qquad(\operatorname{Re}z>0).
\]
Retain C466a's L018 conventions and external strip, symmetry,
paired-product, counting and verified-low-zero qualifications. The
one-sided density assertion, including its full positive support,
is an imported input, not established independently here. No other
Gaussian-mixture assertion, RH, simplicity or global PF is assumed.

Put \(B(s)=\log h(s)\) for positive real \(s\), and fix
\(x=B'(1)\). Let \(\gamma:\mathbb R\to\{\operatorname{Re}z>0\}\)
be a regular injective \(C^2\) curve with \(\gamma(0)=1\) and
\(\gamma'(0)=i\). Define
\[
 A_x(z)=\frac{e^{xz}}{h(z)},\qquad
 w_\gamma(u)=A_x(\gamma(u))\frac{\gamma'(u)}i.
\]
The common Cartesian-product contour uses this same orientation in
both variables. No deformation or endpoint convergence is assumed.

For the separate **local coupled scope audit947** only, let \(G\) be
any symmetric holomorphic germ on \(\mathbb C^3\) at zero with
\(G(0)=g>0\). It need not arise from a density. The actual specialization
is \(G(w)=\prod_{j=1}^3 A_x(1+iw_j)\). No global hypotheses on this
generic germ are imposed.

## Conclusion

There is no such curve satisfying simultaneously
\[
 w_\gamma(u)\in(0,\infty)\quad(u\in\mathbb R),                 \tag{1}
\]
and
\[
 -\bigl(\gamma(v)-\gamma(u)\bigr)^2
       w_\gamma(u)w_\gamma(v)\in[0,\infty)
       \quad(u\ne v).                                       \tag{2}
\]
These are precisely the scalar and signed two-variable pointwise
conditions in test925, with its determinant convention. Already their
restriction to any open parameter interval about zero is impossible.

This stops that common product-contour mechanism even at the selected
single \(x\). It does not refute a density minor, rule out coupled
surfaces or cancellation arguments, imply failure of global PF, or
settle L030-L032/C032a. This specialization was recorded in step927
and passed the step929 critical audit below; it is not a candidate RH proof.

The coupled cubic-phase test has a different verdict: for every such
\(G\) there is a permutation-equivariant local holomorphic map
\(z(u)\), with \(z(0)=(1,1,1)\), \(Dz(0)=iI\), and
\(z_j-z_i=i(u_j-u_i)\), for which the full signed pullback, divided
by the real squared Vandermonde, is the constant \(g\). Its Taylor
truncation through degree four has divided coefficient \(g+O(\|u\|^4)\).
Thus the positive-constant/no-imaginary-terms-through-degree-three
condition is generic and cannot discriminate actual-density signs.
This local scope qualification parks test945; it supplies no global
deformation or determinant sign and does not weaken the product stop.

## Proof

### Exact inversion at s=1 and normalization

All moments of \(e^{-u}p(u)\,du\) are finite: for each nonnegative
integer \(r\), \(u^r e^{-u}\) is bounded on \([0,\infty)\), and
\(p\) has mass one. Differentiating the transform at \(s=1\),
with domination on a smaller positive real neighborhood, gives
\[
 h(1)\int_0^\infty u e^{-u}p(u)\,du=B'(1)=x.                 \tag{3}
\]
Thus \(q(u)=h(1)e^{-u}p(u)\) is a probability density with finite
strictly positive mean \(x\); its support is \([0,\infty)\), and
it is positive at every positive argument. Here \(h(1)>0\).

Weighted inversion at this fixed value of \(s\) needs a large-frequency
estimate, rather than C466a's large-s limit. Use C466a's complex
estimate (1), for large \(z\) in the closed right half-plane:
\[
 B(z)=\frac{\sqrt z}{2}
     \left(\log\frac{\sqrt z}{2\pi}-1\right)
        +\frac78\log z+C+O(|z|^{-1/2}).                       \tag{4}
\]
This is an analytic logarithm in the large region there specified;
no continuation through zeros is needed. At \(z=1+it\), write
\(\sqrt z=a+ib\). Then
\(a\ge |z|^{1/2}/\sqrt2\), \(|b|\le |z|^{1/2}\), and
\(|\arg\sqrt z|\le\pi/4\). In particular
\[
 \operatorname{Re}\left[\frac{\sqrt z}{2}
      \left(\log\frac{\sqrt z}{2\pi}-1\right)\right]
 =\frac a2\left(\frac12\log|z|-\log(2\pi)-1\right)
       -\frac b2\arg\sqrt z
 \ge \frac{|z|^{1/2}\log|z|}{4\sqrt2}-C_1|z|^{1/2}           \tag{5}
\]
once the parenthesis is positive. The real part of the remaining
logarithm in (4) is \((7/8)\log|z|\); the error is bounded.
Consequently there are constants \(c>0,T<\infty\) such that
\[
 |h(1+it)|^{-1}\le
       \exp[-c\sqrt{|t|}\log|t|]\quad(|t|\ge T).              \tag{6}
\]
The density transform ensures that \(h\) has no zeros in the right
half-plane; the integrand is bounded on compact parts of this line.
Thus every polynomially weighted reciprocal in (6) belongs to
\(L^1(\mathbb R)\).

Apply the weighted Fourier inversion theorem used in C466a to
\(e^{-y}p(y)\), whose Fourier transform with kernel \(e^{-ity}\)
is \(1/h(1+it)\). Absolute convergence of all polynomially weighted
transforms permits differentiation under the integral, at every real
\(y\). The continuous inverse agrees with the given smooth density,
not just an unspecified almost-everywhere representative. Leibniz's
rule after multiplication by \(e^y\) gives the exact formulas
\[
 p^{(r)}(y)=\frac1{2\pi}\int_{\mathbb R}
       (1+it)^r\frac{e^{y(1+it)}}{h(1+it)}\,dt,
       \qquad r\ge0.                                        \tag{7}
\]
Only \(r=0,1,2\) will be used for the determinant. The normalized
density is \(p\); C466a's \(\Theta=p/c_0\) has the determinant
\(\mathcal D_2(\Theta;x)=c_0^{-2}\mathcal D_2(p;x)\).

### Bilinear identity, sign and both Jacobians

Import Andreief's bilinear identity, in the precise complex-valued
form of Giulio Ruzza, *Introduction to Random Matrix Theory,
Riemann-Hilbert problems, and Universality*, notes updated 4 May 2022,
[Lemma 3.1.1, pp.27-28](https://webpages.ciencias.ulisboa.pt/~gruzza/introRMT.pdf).
Its hypothesis is that each cross-product \(f_i g_j\) is in \(L^1\);
it supplies no conjugation and no positivity. See also Peter Forrester,
*Meet Andreief, Bordeaux 1886, and Andreev, Kharkov 1882-83*,
[arXiv:1806.10411v1, (1.7), Section 2.2 and (2.4)](https://arxiv.org/pdf/1806.10411v1).
These known identities are imported, not reproved.

For any parametrized curve for which
\(\int(1+|\gamma|^2)|w_\gamma|\,du<\infty\), define
\(m_r=(2\pi)^{-1}\int\gamma(u)^r w_\gamma(u)\,du\),
\(0\le r\le2\). In the cited theorem take
\(f_i(u)=\gamma(u)^i\) and
\(g_j(u)=\gamma(u)^j w_\gamma(u)/(2\pi)\), \(i,j=0,1\).
The displayed absolute-moment hypothesis verifies every required
cross-product in \(L^1\). The two determinants in the integrand are
\(\gamma(v)-\gamma(u)\) and
\((\gamma(v)-\gamma(u))w_\gamma(u)w_\gamma(v)/(2\pi)^2\).
Therefore
\[
 -\det[m_{i+j}]_{i,j=0}^1
 =\frac1{2(2\pi)^2}\int_{\mathbb R^2}
   -\bigl(\gamma(v)-\gamma(u)\bigr)^2
      w_\gamma(u)w_\gamma(v)\,du\,dv.                        \tag{8}
\]
Absolute convergence of this double integral also follows directly
from \(|\gamma(v)-\gamma(u)|^2\le2(|\gamma(v)|^2+|\gamma(u)|^2)\).
Each weight contains its own factor \(\gamma'/i\). No conjugate
Vandermonde, reversal of one orientation or omitted factor of \(i\)
is permissible.

For the original Bromwich curve \(\gamma_0(u)=1+iu\), (6) verifies
the absolute-moment hypothesis, (7) identifies \(m_r=p^{(r)}(x)\),
and the left side is exactly
\(\mathcal D_2(p;x)=p'(x)^2-p(x)p''(x)\).
For a different curve (8) concerns its own moments. Identifying them
with (7) would require a justified deformation; none is asserted.
The algebraic pullback in (8) is defined pointwise even without
integrability, so its necessary phase conditions can be refuted
locally without constructing a deformation.

### The pair condition forces a vertical arc

Under (1), division in (2) by the strictly positive product of weights
gives \(-\bigl(\gamma(v)-\gamma(u)\bigr)^2\ge0\) real.
For a nonzero complex number \(a+ib\), its negative square is real
nonnegative only if \(a=0\): its imaginary part is \(-2ab\), and
\(b=0,a\ne0\) would give a negative real number. Injectivity excludes
zero secants. Taking \(v=0\) proves \(\operatorname{Re}\gamma(u)=1\).
The same argument works on any open interval about zero where (1)-(2)
hold. There write \(\gamma(u)=1+i\tau(u)\), with real \(C^2\)
function \(\tau\), \(\tau(0)=0\), \(\tau'(0)=1\).
On a smaller interval \(\tau'>0\), and its image contains an open
real interval \(J\) about zero. Since \(\gamma'/i=\tau'>0\), (1)
now implies
\[
 \frac{A_x(1+it)}{A_x(1)}
     =e^{ixt}\frac{h(1)}{h(1+it)}\in(0,\infty)
                   \qquad(t\in J).                          \tag{9}
\]
This uses the full scalar weight including its Jacobian; it never
assumes reality of the exponential factor alone.

### Analytic bridge, whole-axis symmetry and support contradiction

Let \(U\) have density \(q\) from (3), and \(Y=U-x\).
Its characteristic function is
\[
 \phi(t)=\mathbb E e^{itY}
         =e^{-ixt}\frac{h(1)}{h(1-it)}\quad(t\in\mathbb R).
                                                               \tag{10}
\]
The expectation extends holomorphically to
\(\operatorname{Im}t>-1\): on any compact subset, each differentiated
integrand is bounded by a constant times
\((1+u)^r e^{-\delta u}p(u)\), for some \(\delta>0\), including
the bounded factor from centering. This is integrable because \(p\)
has mass one. In particular \(\phi(t)-\phi(-t)\) is holomorphic on
the connected strip \(|\operatorname{Im}t|<1\).

For real \(t\), conjugate symmetry of a characteristic function gives
\(\phi(-t)=\overline{\phi(t)}\). Equation (9) says
\(\phi(-t)\) is real near zero. Hence
\(\phi(t)-\phi(-t)=0\) on a nontrivial real interval. The identity
theorem on the stated strip makes this equality hold on its entire
domain, in particular for every real \(t\). Thus \(\phi\) is real
and even on the whole real axis.

Now import Alexander Iksanov, *Characteristic functions and their
relatives in probability theory*, Xi'an 2019 lecture notes,
[Definition 139 and Lemma 141, pp.75-76](https://do.csc.knu.ua/wp-content/uploads/2023/01/Char_funct_XIan2019.pdf):
a law has a real even characteristic function on the whole real axis
exactly when it is symmetric about zero. Its uniqueness input is
Theorem 113, p.63. Remark 114 there explicitly warns that a finite
interval alone is insufficient; the holomorphic-strip argument above
supplies the missing hypothesis in this application. Consequently
\(Y\) and \(-Y\) have the same law.

But \(U\ge0\) almost surely, while its density is strictly positive
on every positive interval. Since \(x>0\),
\[
 \mathbb P(Y>x+1)=\mathbb P(U>2x+1)>0,
 \qquad
 \mathbb P(Y<-x-1)=\mathbb P(U<-1)=0.                         \tag{11}
\]
Symmetry makes these probabilities equal, a contradiction. This
establishes the stated local and hence global incompatibility.

### Scope and comparison with recorded stops

The only new notebook contribution is this actual-law application
of the cited determinant and symmetry inputs; no originality is
certified. Source coverage and duplicate/failure checks are reused
from review925/test925. C466g's growing-order boundary signs do not
imply a common contour; C466j's chamber-cone stop concerns another
mechanism and is neither a premise nor superseded here. A failure
of this sufficient pointwise mechanism supplies no negative actual
minor. Noncompact endpoints, admissible deformation, cancellations,
all-x/all-order signs and Xi transfer are not paid by (8)-(11).

### Independent critical audit — 14 November 2026, step929

The approved audit927 scope was replayed against the complete proof,
C466a's hypotheses and sector estimate, and review925/test925's inspected
source statements and proof cases. No failed inference was found. This
validates the existing scoped obstruction; it adds neither a stronger
theorem nor an originality claim. The external density construction and
its cited zero/counting inputs remain qualifications, not newly checked
certificates.

In (3), differentiating the Laplace transform gives
\(-\int u e^{-u}p(u)du=-h'(1)/h(1)^2\), so multiplication by
\(h(1)\) gives precisely \(x=B'(1)\), with no missing normalizing
constant. Positivity on positive intervals makes this finite mean
strictly positive. In (5), the leading coefficient is
\(1/(4\sqrt2)\), and the adverse argument term is only
\(O(\sqrt{|z|})\); it cannot cancel the leading
\(\sqrt{|z|}\log|z|\) growth. Thus (6) really holds along the
fixed line \(\operatorname{Re}z=1\). It is not an invocation of
C466a's large-real-s Gaussian limit. Polynomially weighted L1 bounds
give (7) and its derivatives locally uniformly in y. Smoothness of
the given density identifies the inverse at every y.

The four cross-products in the N=2 application have powers
\(0,1,1,2\), all covered by its absolute-moment hypothesis.
Both column weights stay in the second determinant, and each contains
\(\gamma'/i\). This confirms the factor \(1/(2(2\pi)^2)\),
the minus algebraic square in (8), and the scaling \(c_0^{-2}\).
Absolute double integrability follows from the stated secant bound.
The proof correctly distinguishes arbitrary contour moments from
density derivatives on the original Bromwich line.

For the local argument, division by the strictly positive weights is
legitimate. A nonzero secant with nonnegative negative square must be
purely imaginary; taking one endpoint at zero fixes real part 1.
The tangent condition implies \(\tau'>0\) on a smaller interval,
so the inverse function theorem supplies the open frequency interval
used in (9). Scalar reality follows only after retaining this Jacobian.

For completeness, on a compact set K in \(\operatorname{Im}t>-1\),
put \(\delta=\inf_{t\in K}(1+\operatorname{Im}t)>0\).
The absolute value of the r-th t derivative of the expectation
integrand is bounded by
\[
 C_{K,r}(1+u)^r e^{-\delta u}p(u).
\]
Its integral is finite because the polynomial times the exponential
is bounded and p has unit mass. This verifies holomorphy of phi on
that entire half-plane. Reflection gives the common connected strip
\(|\operatorname{Im}t|<1\), containing the whole real axis. The
real interval of zeros has an accumulation point inside that strip;
the identity theorem therefore applies before the whole-axis symmetry
criterion is used. No finite-interval uniqueness claim is made.
Finally q is positive on, for example, \((2x+1,2x+2)\), whereas
U has no mass below zero. The two probabilities in (11) are indeed
strictly positive and zero, respectively, contradicting symmetry.

No integration over a hypothetical new contour enters this last
contradiction. End connectors, homotopy and deformation estimates are
therefore unnecessary for this exclusion, but remain necessary for
any future positive representation. C466a remains the sole direct
local mathematical input; C466g/j are comparisons only. The audit
supports stopping the simultaneous scalar/pair product-contour route,
without extending the stop to coupled contours or cancellation methods.

### Coupled local scope audit — 14 November 2026, step947

This is the bounded specialization approved by nomination945/review946,
not a reproof of a normal-form theorem or an assertion of novelty.
Import the holomorphic implicit-function theorem from Jiří Lebl,
[*Tasty Bits of Several Complex Variables*, v4.4, 31 May 2026,
Theorem 1.3.8, printed p32](https://www.jirka.org/scv/scv.pdf), and its
locally absolutely convergent holomorphic power series from Theorem
1.2.1, pp20-21. Review946 inspected these statements. A singular-volume
normal-form theorem is unnecessary: the common shift below preserves
the entire collision factor exactly. The new verification concerns
the prescribed derivative, equivariance, signed Jacobian and truncation.

Write \(e=(1,1,1)\),
\[
 t=(u_1+u_2+u_3)/3,\qquad v=u-te=(a,b,-a-b).
\]
On a sufficiently small neighborhood in \(\mathbb C\times\{\sum v_j=0\}\),
define the parameter-dependent primitive
\[
 F(T,v)=\int_0^T G(v+se)\,ds
       =T\int_0^1 G(v+\tau Te)\,d\tau.                    \tag{12}
\]
Choose the neighborhood so all these segments stay in the domain of
\(G\). Local uniform absolute convergence of its power series permits
termwise integration on smaller polydisks, proving joint holomorphy
and \(F_T(T,v)=G(v+Te)\). In particular
\(F(0,v)=0\), \(F_T(0,0)=g\ne0\). The cited implicit theorem applied
to \(F(T,v)-gt=0\), with parameters \((t,a,b)\), supplies a unique
holomorphic germ \(T=T(t,v)\) satisfying
\[
 F(T(t,v),v)=gt,\quad T(0,0)=0,\quad
 T_t(0,0)=1,\quad D_vT(0,0)=0.                            \tag{13}
\]
The last two statements follow by differentiating the identity:
\(F_T=g\) at zero and \(D_vF(0,0)=0\). Hence \(T=t+O(\|u\|^2)\).

Symmetry of \(G\) gives \(F(T,\sigma v)=F(T,v)\) for every
permutation \(\sigma\). Implicit uniqueness then gives
\(T(t,\sigma v)=T(t,v)\) as germs. Shrinking to a common neighborhood
for the finitely many permutations makes these equalities simultaneous.
Set
\[
 w(u)=v+T(t,v)e,\qquad z(u)=e+iw(u).                       \tag{14}
\]
This is permutation equivariant, \(z(0)=e\), \(Dz(0)=iI\), and
\(z_j-z_i=i(v_j-v_i)=i(u_j-u_i)\) identically. In particular all
pair collisions and their intersection are preserved. The invertible
derivative also makes the map locally biholomorphic, by the same
implicit theorem; its restriction to a small real neighborhood is
a regular embedded cycle germ. No global injectivity is asserted.

Both coordinate Jacobians are required. The linear map
\((t,a,b)\mapsto u=(t+a,t+b,t-a-b)\) has matrix
\(\left(\begin{smallmatrix}1&1&0\\1&0&1\\1&-1&-1\end{smallmatrix}\right)\)
and determinant \(+3\). The map
\((t,a,b)\mapsto(T(t,a,b),a,b)\) has determinant \(T_t\), including
all dependence on the two difference variables. Consequently
\(\det(D_uw)=T_t\). In wedge notation, which retains orientation,
\[
 \bigwedge_{j=1}^3(dz_j/i)
 =3T_t\,dt\wedge da\wedge db
 =T_t\,du_1\wedge du_2\wedge du_3.                        \tag{15}
\]
The two factors \(+3\) cancel; there is no absolute complex
Jacobian or independent orientation reversal. With
\(\Delta(u)=\prod_{i<j}(u_j-u_i)\),
\(\Delta(z)=i^3\Delta(u)\) and hence
\(-\Delta(z)^2=\Delta(u)^2\). Thus the signed form
\[
 -\Delta(z)^2G((z-e)/i)\bigwedge_{j=1}^3(dz_j/i)
\]
pulls back to
\[
 \Delta(u)^2 G(v+T e)T_t\,du_1\wedge du_2\wedge du_3
 =g\Delta(u)^2\,du_1\wedge du_2\wedge du_3,               \tag{16}
\]
where the last equality is the t derivative of (13).
Division away from collisions therefore extends holomorphically over
every collision as the constant \(g\). This is an exact factorization,
not division of an uncontrolled remainder by a vanishing polynomial.

Let \(T_4\) be the Taylor polynomial of \(T\) through total degree
four in \((t,a,b)\), equivalently in \(u\). Holomorphic power series
give \(T-T_4=O(\|u\|^5)\) and
\(T_t-(T_4)_t=O(\|u\|^4)\). Permutations act linearly on these
coordinates, so each homogeneous part retains the invariance in (13).
Replacing T by \(T_4\) in (14) preserves equivariance, first derivative,
and the exact difference identity. Its corrections to \(e+iu\) have
precisely the allowed degrees two through four. Formula (15) still
holds with \((T_4)_t\). Since G and its first derivatives are bounded
on a smaller complex neighborhood,
\[
 G(v+T_4e)(T_4)_t-G(v+Te)T_t=O(\|u\|^4).                 \tag{17}
\]
Indeed the change of the G factor is \(O(\|u\|^5)\), its multiplier
is bounded, and the derivative change is \(O(\|u\|^4)\).
The Vandermonde remains an exact common factor before taking (17).
The divided coefficient is therefore \(g+O(\|u\|^4)\); every Taylor
term of degrees one, two and three vanishes, including its imaginary
part. Its real constant is strictly positive. No numerical preview or
finite fit is used in this conclusion.

For the actual form use \(G(w)=\prod_j A_x(1+iw_j)\). Because
\(h(1)>0\), h has no zeros on some neighborhood of 1;
\(A_x\) and G are holomorphic there, symmetric in the three variables,
and \(g=(e^x/h(1))^3>0\). This uses no Taylor coefficients of h,
no C466p sign, and no zero certificates beyond those retained when
interpreting the original density integral. The construction even
works for other real x wherever this local analytic condition holds.
It therefore cannot distinguish the selected actual mean or global
positivity. The full-form constant germ is stronger locally than the
requested finite jet, but provides no noncompact continuation,
endpoint control, integrability, Bromwich homology, all-order sign,
or transfer to L030-L032/C032a. Stops927/932/941 remain scoped to their
original mechanisms. Do not increase the jet order to reopen test945.

## Mathlib

Full matching coverage has not been checked. The supporting analytic
identity theorem, Fourier inversion and determinant integration inputs
are distinguished from this full actual-law contour exclusion; no
matching declaration or absence claim is asserted. Unknown coverage
is not evidence of absence.

Full matching coverage for audit947's equivariant collision-preserving
scope qualification is also unchecked. Holomorphic implicit functions,
power series and determinants are the supporting standard inputs;
no formalization or absence from Mathlib is claimed.
