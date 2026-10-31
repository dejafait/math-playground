# Corollary C055a: second-level shape with nonreal Fourier zeros

## Hypotheses

Use exactly L055's family

\[
g(u)=e^{-\cosh(2u)},\qquad c_a=\cosh(a/10),\qquad
h_a(u)=\frac{c_ag(u)+(g(u-a)+g(u+a))/2}{c_a+1}.
\]

Define the positive integer constants

\[
M_r=2^r\{2(r-1)^{r-1}+2^r\}\quad(2\le r\le8),\qquad
B_8=8^{16}\,7!\,M_8,
\]

and put

\[
a_0=\min\{1/500,1/(192B_8)\}>0.
\]

Let \(0<a\le a_0\), \(s_a(t)=h_a(\sqrt t)\) for \(t\ge0\), and
\(f_a=s_a'^2-s_as_a''\), with primes denoting derivatives in \(t\).
At zero use the removable real-analytic extensions.

The external mathematical input is Scott Schubr, *Admissible kernel lifts
with positive endpoint forms and nonreal Fourier zeros*, public Edition 2
(27 October 2026; manuscript dated 24 October), Section 2 equations (1)-(3)
and Section 3 equation (9), Theorem 3, printed pp. 3-6:
[primary PDF](https://research.luminaryoddities.com/admissible-kernel-lifts-positive-endpoint-forms-nonreal-fourier-zeros/v/2/files/Paper.pdf).
The archive advertises PDF SHA-256
`b204ae62af502437122e482681c6a8048e83789cac4475623a134d9bafe8fcfb`.
This is an author preprint. The load-bearing proof for this fixed-scale
application was independently reproduced below on 30 October 2026.
That audit covers the necessary Theorem 2 estimates, Lemma 4 and Theorem 3,
not the remaining manuscript or its computational package. The advertised
hash has not been independently checked against downloaded bytes.

## Conclusion

For every \(0<a\le a_0\) and every \(t\ge0\),

\[
f_a(t)>0,\qquad (\log f_a)''(t)<-\frac85<0.
\]

Thus the existence alternative of the approved target holds, with the
source argument audited at the stated scope. Nevertheless the Fourier transform of each
\(h_a\) has nonreal zeros at
\((2k+1)\pi/a\pm i/10\), for every integer \(k\), by L055.
Second-level shape therefore does not force real Fourier zeros for this
comparison family. This is a known-result application, not a new general
shape theorem or a statement about the actual theta kernel.

## Proof

Schubr's notation for a nonzero positive even finite atomic measure is
\(\mu=\sum_{j=1}^n w_j\delta_{b_j}\), with distinct positions and positive
weights. Write

\[
q=\frac{\max_jw_j}{\min_jw_j},\quad
D=\max_jb_j-\min_jb_j,\quad T=\binom n2q,\quad
\Delta=D/L,\quad
C_L=\frac{T}{e}(e^\Delta-1)+2\sinh^2(\Delta/2).
\]

Theorem 3 has the primary hypotheses

\[
L>0,\qquad \Delta\le1/125,\qquad C_L<1/10,\qquad
B_8T\Delta\le1/4.
\]

For \(\phi_L(u)=\sum_j w_j e^{-\cosh((u-b_j)/L)}\), set
\(S_L(t)=\phi_L(\sqrt t)\) and \(T_L=S_L'^2-S_LS_L''\).
The cited theorem asserts \(T_L>0\) and
\((\log T_L)''<-1/(10L^4)\) for every \(t\ge0\), including its analytic
endpoint. Its optional sufficient scale in equation (11), which includes
\(L\ge1\), is not a primary hypothesis and is not used here.

Take \(L=1/2\), positions \(-a,0,a\), and respective weights
\(1/2,c_a,1/2\). For each \(a>0\) they are distinct; the measure is positive
and even. Moreover \(a\le a_0\le1/500<1/100\), so
\(1\le c_a\le e^{1/1000}\le1000/999<2\). The middle inequality follows
by comparing the exponential series to the geometric series. Hence,
uniformly throughout this parameter interval,

\[
n=3,\quad D=2a,\quad q=2c_a<4,\quad T=3q<12,\quad
\Delta=4a\le1/125.
\]

For \(0\le\Delta\le1/4\), the elementary bounds
\(e^\Delta-1\le2\Delta\), \(2/e<1\), and
\(2\sinh^2(\Delta/2)\le\Delta^2\) give
\(C_L<T\Delta+\Delta^2\) when \(\Delta>0\).
These are also the bounds used in the proof of Theorem 2, printed p. 4.
For completeness the last follows from
\(\sinh v\le v/(1-v^2)\), \(0\le v\le1/8\), by its positive power
series, and \(2(1-v^2)^2\ge2(63/64)^2>1\).
Consequently

\[
C_L<T\Delta+\Delta^2
 <\frac{12}{125}+\frac1{15625}
 =\frac{1501}{15625}<\frac1{10}.
\]

The derivative budget is paid by the other part of the definition of
\(a_0\):

\[
B_8T\Delta<48B_8a\le\frac14.
\]

All three primary budgets thus hold for every \(0<a\le a_0\), with the
same \(a_0\), although the atomic measure varies with \(a\). This is not
an appeal to uniform convergence on an unbounded interval.

The fixed scale matches exactly:

\[
\phi_{1/2}(u)=c_ag(u)+\tfrac12g(u-a)+\tfrac12g(u+a)
             =(c_a+1)h_a(u).
\]

Here \(c_a+1>0\) is constant in the coordinate being differentiated.
Therefore \(S_{1/2}=(c_a+1)s_a\),
\(T_{1/2}=(c_a+1)^2f_a\), and the source conclusion yields

\[
f_a>0,\qquad
(\log f_a)''=(\log T_{1/2})''
 <-\frac1{10(1/2)^4}=-\frac85.
\]

The finite mixture is even and entire in \(u\), so its even power series
defines \(s_a(t)\) analytically at zero. Positive normalization respects
this extension. The theorem's strict endpoint signs ensure that
\(\log f_a\) also has its local real-analytic value there. No division
by \(\sqrt t\) at zero or global complex logarithm is assumed. No claim
about distinctness at the excluded parameter \(a=0\) is needed.

Finally \(a_0\le1/100\), so L055 applies to every parameter here and gives
the displayed nonreal Fourier zeros. No finite mixed-form claim from
L057 is used. The original applicability proof above imported the source
estimates; the following audit discharges that specific qualification.

### Independent audit of the load-bearing source proof

This is a reproduction of the cited Edition 2 argument, not a new shape
theorem. It is included because the original application explicitly left
these analytic estimates unverified. Keep the atomic data and the three
budgets above, ultimately at \(L=1/2\). Write the dimensionless variable
as \(x\), to distinguish it from the squared physical coordinate \(u\):

\[
d_j=b_j/L,\quad A_j(x)=\cosh(x-d_j),\quad B_j(x)=\sinh(x-d_j),
\quad p_j(x)=\frac{w_je^{-A_j(x)}}{\sum_iw_ie^{-A_i(x)}},
\quad \ell(x)=\log\phi_L(Lx).
\]

All expectations below are over the finite probability vector \(p(x)\)
at the specified real \(x\). All quantities are finite there; the bounds,
rather than the probabilities, are uniform over the real line.

**Pair suppression and centered moments (printed pp. 3-5).** Put
\(A_*=\min_j A_j\ge1\), \(u_{ij}=|A_i-A_j|\), and
\(v=2\sinh(\Delta/2)\). The addition formula and
\(|\sinh y|\le\cosh y\) imply
\(\cosh(y+h)\le e^{|h|}\cosh y\). Therefore

\[
A_j\le e^\Delta A_*,\qquad
u_{ij}\le(e^\Delta-1)A_*,\qquad
p_ip_j\le q e^{-u_{ij}}.
\]

For the last inequality, if \(A_i\ge A_j\), bound the denominator of
\(p_ip_j\) below by \(w_j^2e^{-2A_j}\); the other order interchanges
the indices. Direct hyperbolic algebra gives

\[
(B_i-B_j)^2=(A_i-A_j)^2+4\sinh^2((d_i-d_j)/2),
\qquad |B_i-B_j|\le u_{ij}+v.
\]

The differentiated finite sum gives
\(\ell''=-\mathbb EA+\operatorname{Var}B\), with
\(\operatorname{Var}B=\sum_{i<j}p_ip_j(B_i-B_j)^2\).
Since \(u^2e^{-u}\le u/e\) and \(\sum_{i<j}p_ip_j\le1/2\),

\[
\operatorname{Var}B
\le \frac{T}{e}(e^\Delta-1)A_*+2\sinh^2(\Delta/2)
\le C_L\mathbb EA.
\]

Thus the cited ordinary curvature estimate is valid. The stronger
derivative bounds use the following moments, not powers of this variance.
For an independent copy \(X'\) of a component variable \(X\), conditional
Jensen gives
\(\mathbb E|X-\mathbb EX|^r\le\mathbb E|X-X'|^r\).
For each integer \(2\le r\le8\), use

\[
u^re^{-u}\le(r-1)^{r-1}u\quad(u\ge0),\qquad
(u+v)^r\le2^{r-1}(u^r+v^r).
\]

Counting the two orders of every distinct pair yields

\[
\begin{aligned}
\mathbb E|A-\mathbb EA|^r
 &\le 2T(r-1)^{r-1}(e^\Delta-1)A_*
 \le4T(r-1)^{r-1}\Delta\mathbb EA,\\
\mathbb E|B-\mathbb EB|^r
 &\le2^rT\big((r-1)^{r-1}(e^\Delta-1)A_*+v^r\big)
 \le M_rT\Delta\mathbb EA.
\end{aligned}
\]

Here \(e^\Delta-1\le2\Delta\), \(v\le2\Delta\),
\(\Delta^r\le\Delta\), and \(\mathbb EA\ge A_*\ge1\), since
\(0\le\Delta\le1/4\). For example the bound for \(v\) follows
from \(\sinh y\le y/(1-y^2)\) for \(0\le y\le1/8\).
The displayed \(A\)-bound is also at most \(M_rT\Delta\mathbb EA\).
Signed choices of \(A\) or \(B\) have the same absolute centered bounds.

**Mixed cumulants and the finite derivative budget (printed p. 5).**
For \(2\le r\le8\), let \(X_1,\ldots,X_r\) be any signed component choices,
\(Y_i=X_i-\mathbb EX_i\), and \(H_r=M_rT\Delta\mathbb EA\).
For a block \(C\) of size \(m\le r\), generalized Hölder gives

\[
\left|\mathbb E\prod_{i\in C}Y_i\right|
\le\prod_{i\in C}(\mathbb E|Y_i|^r)^{1/r}
\le H_r^{m/r}.
\]

When \(m<r\), include the constant function 1 with exponent
\(r/(r-m)\); its norm is one. Thus no assumption \(H_r\ge1\) is
hidden. Multiplying over a partition of all \(r\) indices gives a bound
of exactly \(H_r\), including when \(0<H_r<1\). If \(H_r=0\), all
centered variables vanish and the same conclusion holds directly.

For clarity, the cumulant used here is the coefficient obtained by
differentiating \(\log\mathbb E\exp(\sum z_iX_i)\) once in each
variable at zero. Expanding \(\log(1+w)\) to total degree \(r\) gives
the finite partition formula

\[
\operatorname{cum}_r(X_1,\ldots,X_r)
=\sum_{\pi}(-1)^{|\pi|-1}(|\pi|-1)!
  \prod_{C\in\pi}\mathbb E\prod_{i\in C}X_i.
\]

Replacing each \(X_i\) by \(Y_i\) changes this logarithm only by a
linear function, so leaves every cumulant of order at least two unchanged.
There are at most \(r^r\) partitions (encode each block by its least
element), and every coefficient has magnitude at most \((r-1)!\).
Consequently

\[
|\operatorname{cum}_r(X_1,\ldots,X_r)|
\le r^r(r-1)!M_rT\Delta\mathbb EA.
\]

At fixed real \(x\), put \(h_j=-A_j\). The exact local identity is

\[
\ell(x+z)-\ell(x)
=\log\mathbb E_x\exp\big(h_j(x+z)-h_j(x)\big).
\]

The function inside this logarithm equals 1 at \(z=0\), so a local
analytic branch exists. Only coefficients up to degree eight are used.
Expansion by the preceding definition of cumulants gives

\[
\ell^{(k)}(x)=\sum_{\pi\in\Pi_k}
 \operatorname{cum}_{|\pi|}
 \big(h^{(|C_1|)},\ldots,h^{(|C_{|\pi|}|)}\big).
\]

Indeed, ordered block sizes from the exponential expansion become labeled
set partitions after multiplying the coefficient of \(z^k\) by \(k!\);
the factor \(1/|\pi|!\) removes the order of the blocks. This expansion
accounts for derivatives of the varying tilted probabilities. It assumes
neither a global logarithm nor an infinite cumulant expansion away from
the fixed center.

Each component derivative is \(-A\) in even order and \(-B\) in odd
order. For even \(k\), the one-block term is \(-\mathbb EA\).
For \(k=4,8\), each remaining term has \(2\le r\le8\) blocks.
The sequence \(M_r\) is increasing on these integers, and
\(|\Pi_k|\le8^8\), \(r^r\le8^8\), \((r-1)!\le7!\).
It follows, with both partition counts included, that

\[
|\ell^{(k)}+\mathbb EA|\le8^{16}7!M_8T\Delta\mathbb EA
=B_8T\Delta\mathbb EA\le\tfrac14\mathbb EA,
\qquad k=4,8.
\]

**Coordinate identity and its boundaries (printed p. 6, equation (14)).**
Set \(u=L^2x^2\), \(x>0\). For an even smooth \(\ell\),

\[
\frac{d^j}{du^j}\ell(\sqrt u/L)
=\frac{1}{L^{2j}2^{2j-1}(j-1)!}
 \int_0^1(1-v^2)^{j-1}\ell^{(2j)}(vx)\,dv.
\]

For \(j=1\), integrate \(\ell''\) and use \(\ell'(0)=0\).
For the induction, differentiation of the integral is allowed on the
compact \(v\)-interval, locally uniformly in \(x>0\). If its coefficient
is \(c_j\), the resulting expression is

\[
\frac{c_j}{2L^2x}\int_0^1v(1-v^2)^{j-1}
                  \ell^{(2j+1)}(vx)\,dv
=\frac{c_j}{4jL^2}\int_0^1(1-v^2)^j
                  \ell^{(2j+2)}(vx)\,dv.
\]

Integration by parts uses
\(((1-v^2)^j)'=-2jv(1-v^2)^{j-1}\). At \(v=1\) the
weight is zero; at \(v=0\) the odd derivative
\(\ell^{(2j+1)}(0)\) is zero. These are both boundary terms.
The new coefficient is \(c_j/(4jL^2)\), as required.

For this finite mixture, \(\phi_L\) is even entire and strictly positive
on the real axis. Its logarithm is even and real analytic near zero.
Consequently its local even series gives

\[
G_L^{(j)}(0)=\frac{j!}{(2j)!L^{2j}}\ell^{(2j)}(0),
\qquad G_L(u)=\ell(\sqrt u/L).
\]

The integral identity has this same limit by continuity on a compact
interval. No division by zero is used. The later bounds are pointwise
for every finite \(x\); there is no integration boundary at infinity
and no interchange of an infinite-height limit with these integrals.

**Comparison and strict margin (printed p. 6, equation (15)).**
Evenness of the atomic support gives \(|d_j|\le d=\Delta/2\le1/250\).
Applying the cosh ratio bound in both directions gives

\[
e^{-d}\cosh x\le\mathbb EA(x)\le e^d\cosh x.
\]

The previous derivative estimates imply that \(\ell^{(4)}\) and
\(\ell^{(8)}\) are negative, with magnitudes between
\((3/4)\mathbb EA\) and \((5/4)\mathbb EA\).
The coordinate integrals have nonnegative weights. Comparing them with
\(H(u)=-\cosh(\sqrt u/L)\), at \(j=2,4\), proves

\[
G_L'',G_L''''<0,\qquad
|G_L''|\ge\tfrac34e^{-d}|H''|,\qquad
|G_L''''|\le\tfrac54e^d|H''''|.
\]

These inequalities hold at \(u=0\) as well: the coordinate formula there
has a positive factor and the same strict derivative signs.
Let \((b)_m=b(b+1)\cdots(b+m-1)\), with \((b)_0=1\), and set
\(F_b(z)=\sum_{m\ge0}z^m/(m!(b)_m)\). The convergent cosh series
can be differentiated at every finite \(u\) and gives

\[
H''=-\frac{F_{5/2}(z)}{12L^4},\qquad
H''''=-\frac{F_{9/2}(z)}{1680L^8},\qquad z=\frac{u}{4L^2}.
\]

For instance the coefficient ratio in the \(j\)-th differentiated
series is \(1/[4L^2(m+1)(m+j+1/2)]\), with constant coefficient
\(-j!/((2j)!L^{2j})\); this verifies both normalizations.
For \(z\ge0\), termwise positive comparison gives
\(1\le F_{5/2}(z)\) and \(F_{9/2}(z)\le F_{5/2}(z)\).
Hence

\[
\frac{|H''''|}{2|H''|^2}\le\frac{12^2}{2\cdot1680}=\frac3{70},
\qquad
\frac{|G_L''''|}{2|G_L''|^2}
\le\frac{20}{9}e^{3d}\frac3{70}
\le\frac{500}{5187}<\frac1{10}.
\]

Here \(e^{3d}\le e^{3/250}\le250/247\), by comparison with the
geometric series; strictness of the last comparison follows from
\(5000<5187\). Also \(e^{-d}\ge1-d\ge249/250\), so

\[
|G_L''|\ge\frac34\frac{249}{250}\frac1{12L^4}
=\frac{249}{4000L^4}.
\]

Since \(S_L>0\), \(T_L=-S_L^2G_L''>0\). Its real logarithm exists,
including in a neighborhood of the removable endpoint. Exact real
differentiation gives

\[
(\log T_L)''
=2G_L''+\frac{G_L''''}{G_L''}
       -\left(\frac{G_L'''}{G_L''}\right)^2
<-\frac95|G_L''|
\le-\frac{2241}{20000L^4}<-\frac1{10L^4}.
\]

The strict inequality uses the rational ratio bound, not strictness of
the discarded square or a limiting strict inequality. It therefore also
holds at \(u=0\). The budgets and normalization already checked above
apply for every \(0<a\le a_0\), including \(a=a_0\); no positive lower
bound on \(a\) was required. Taking \(L=1/2\) proves the stated
\(-8/5\) margin for \(f_a\).

This discharges the source-proof qualification of C055a at exactly the
claimed scope. It does not audit other source theorems, use its optional
\(L\ge1\) sufficient scale, or assert realization by actual theta.
No source program or finite numerical sign grid enters this proof.

## Mathlib

Not checked. Availability of a full matching theorem, including the
uniform atomic application and endpoint curvature, is unknown; this is
not evidence of absence. No formalization or Mathlib verification is
claimed. [Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
