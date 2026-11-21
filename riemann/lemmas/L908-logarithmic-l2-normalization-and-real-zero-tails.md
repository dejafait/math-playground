# L908: normalization and logarithmic L2 tails for real-zero images

## Hypotheses

Use the local completed function Xi of L018 and its kernel K of
L019-L020. Use exactly Hedenmalm's w(t)=Theta_00(i t^2), D and L,
as in L906, and the primitive u_alpha of L907. In logarithmic
coordinates set

\[
W(x)=w(e^x),\quad q(x)=W'(x)/W(x),\quad
U_\alpha(x)=u_\alpha(e^x),\quad
G_\alpha(x)=(Lu_\alpha)(e^x).
\]

The transform statement below holds for every complex alpha. For
the norm and tail statements assume alpha,beta are real and
Xi(alpha)=Xi(beta)=0. No existence, location, indexing, simplicity,
RH, symmetry, completion or orthogonality assumption is imposed.

## Conclusion

With the source's defining series unchanged, the exact normalization is

\[
\int_{\mathbb R}W(x)e^{i\alpha x}\,dx
=\int_0^\infty w(t)t^{i\alpha}\,\frac{dt}{t}
=\frac12\Xi(\alpha)\qquad(\alpha\in\mathbb C).                 \tag{1}
\]

Thus the printed coefficient in the source's (2.2.1) differs by a
factor of two from (1) when its (1.2.3) and (2.2.2) are retained.
Their zero sets nevertheless agree. For real zero alpha, put

\[
B=\frac{24\pi}{7},\qquad
A_\alpha=B|\alpha|+20\pi B+4\pi^2.
\]

For every real x, writing r=|x|,

\[
|q(x)|\le20\pi e^{2r},\quad
|U_\alpha(x)|\le B e^{5r/2-\pi e^{2r}},\quad
|G_\alpha(x)|\le A_\alpha e^{9r/2-\pi e^{2r}}.              \tag{2}
\]

In particular G_alpha is square integrable on R. The off-diagonal
Gram integral is absolutely convergent, and for every R>=0,

\[
\int_{|x|\ge R}|G_\alpha(x)\overline{G_\beta(x)}|\,dx
\le \frac{6A_\alpha A_\beta}{5\pi}
        e^{7R-2\pi e^{2R}}.                               \tag{3}
\]

This establishes prerequisites for the proposed first-two-zero Gram
test only. It computes no Gram entry and rejects no metric.

## Proof

**Source comparison.** The external definitions used are Hedenmalm,
*Spectral interpretation of Riemann zeta zeros*,
[arXiv:2606.17494v1](https://arxiv.org/html/2606.17494v1),
(1.2.3), (2.2.1)-(2.2.2), (3.2.1)-(3.2.2), and the primitive in
Theorem 3.3.1. The source's (2.2.2) defines precisely the completion
in L018. We do not import its printed (2.2.1) as an additional premise;
the following comparison with the local cosine transform is necessary
to reconcile that coefficient. No standard quadrature or zero-isolation
algorithm is reproved here.

Combining the two equal nonzero-index terms of the first series in
(1.2.3), as already justified in L906, gives, for x>=0,

\[
W(x)=e^{x/2}\sum_{n\ge1}(2v_n^2-3v_n)e^{-v_n},\qquad
v_n=\pi n^2e^{2x}.
\]

Comparison term by term with L019 gives W(x)=K(x)/4 on x>=0.
L906 inversion gives W(-x)=W(x). Its complete endpoint estimates
make W(x)e^{i alpha x} absolutely integrable for every fixed complex
alpha: the extra factor is at most e^{|Im alpha| |x|}, dominated by
the superexponential decay. Splitting the integral at zero and changing
x to -x on the negative half now gives

\[
\int_{\mathbb R}W(x)e^{i\alpha x}dx
=2\int_0^\infty W(x)\cos(\alpha x)dx
=\tfrac12\int_0^\infty K(x)\cos(\alpha x)dx
=\tfrac12\Xi(\alpha),
\]

using L020, including its complex-parameter convergence. The real
change of variables t=e^x proves (1). The scalar 1/2 is nonzero,
so the source's Xi definition and this full transform have exactly
the same zeros and multiplicities, despite the printed coefficient.

**A denominator bound for the logarithmic derivative.** For x>=0
put v=pi e^{2x}>3. All terms of W are positive. The n=1 term yields

\[
W(x)\ge e^{x/2}v^2e^{-v},                                \tag{4}
\]

because 2v^2-3v>=v^2 for v>=3. For m=4 or 6 define
S_m(v)=sum_(n>=1) n^m exp(-v(n^2-1)). We need its complete tail,
not a finite sum. For a_n=n^6 exp(-v(n^2-1)), n>=1,

\[
\frac{a_{n+1}}{a_n}
\le 2^6e^{-3(2n+1)}\le64e^{-9}<\frac1{125}.
\]

Here e^3>20 was proved by the finite exponential sum in L906, so
e^9>8000. Since a_1=1, the geometric bound gives
S_6(v)<=125/124<2, and S_4(v)<=S_6(v)<2. Consequently

\[
W(x)\le 2e^{x/2}v^2e^{-v}S_4(v)
\le4\pi^2e^{9x/2-\pi e^{2x}}.                           \tag{5}
\]

The differentiated series in L906 has polynomial
P_1(z)=-4z^3+15z^2-(15/2)z. For z>=3,

\[
|P_1(z)|\le4z^3+15z^2+(15/2)z
\le(4+5+5/6)z^3<10z^3.
\]

Termwise differentiation is justified by L906's compact derivative
majorants. Summing absolute values and using the full S_6 bound,

\[
|W'(x)|\le10e^{x/2}v^3e^{-v}S_6(v)
\le20e^{x/2}v^3e^{-v}.
\]

Dividing by the strictly positive lower bound (4) gives
|q(x)|<=20v=20pi e^{2x}. Differentiating the exact evenness of W
makes q odd. Thus this bound, and (5) with |x|, hold at both ends,
including x=0. In particular no reciprocal estimate is inferred merely
from rapid decay of W.

**Two primitive tails at an exact real zero.** The change of variables
in the definition of L907 gives

\[
U_\alpha(x)=e^{-i\alpha x}\int_{-\infty}^x e^{i\alpha s}W(s)ds.
\]

At an exact real zero (1) makes the full integral zero. Hence also

\[
U_\alpha(x)=-e^{-i\alpha x}\int_x^\infty e^{i\alpha s}W(s)ds. \tag{6}
\]

Use the first representation for x<=0 and the second for x>=0.
Since alpha is real, its exponential factors have modulus one.
Evenness of W gives

\[
|U_\alpha(x)|\le\int_r^\infty W(s)ds,\qquad r=|x|.
\]

From (5), putting v=pi e^{2r},

\[
\int_r^\infty W(s)ds
\le2\pi^{-1/4}\int_v^\infty y^{5/4}e^{-y}dy.
\]

For y>=v>=pi>3 the logarithmic derivative of y^(5/4)e^(-y) is
5/(4y)-1<=-7/12. Integrating this differential inequality from v
to y bounds the integrand by v^(5/4)e^(-v)e^(-7(y-v)/12).
Its full integral is at most (12/7)v^(5/4)e^(-v). This proves
the middle inequality in (2), with B=24pi/7. This use of (6) is
restricted to exact zeros. It is not valid at every point in a
numerical root enclosure.

**L-images and the full Gram tails.** L907 gives
U_alpha'=-i alpha U_alpha+W. In these coordinates

\[
G_\alpha=\frac1i(U_\alpha'-qU_\alpha)
=-\alpha U_\alpha-iW+iqU_\alpha.
\]

Combining the already proved bounds, and e^(5r/2)<=e^(9r/2),
gives the last inequality in (2) with the displayed A_alpha.
All functions are smooth at finite x, so there is no finite-point
integrability issue. For the product bound, each half of |x|>=R
is at most A_alpha A_beta times

\[
\begin{aligned}
\int_R^\infty e^{9r-2\pi e^{2r}}dr
&=\frac1{2(2\pi)^{9/2}}
       \int_{2\pi e^{2R}}^\infty y^{7/2}e^{-y}dy\\
&\le\frac{3}{5\pi}e^{7R-2\pi e^{2R}}.
\end{aligned}
\]

For the last inequality use y>=2pi>6, so the logarithmic derivative
7/(2y)-1<=-5/12, and integrate its exponential majorant exactly
as above. Adding the two halves proves (3). Taking beta=alpha
proves square integrability, including the complete integral by R=0.
The measure dx is exactly dt/t. No numerical tolerance or truncated
integral is used. This completes the stated specialization.

**Qualification of the bounded attempt (step150; historical).** These were local,
then-unaudited application bounds for the existing target, classified as
REPRODUCTION; no originality is inferred. The required indexed root
certificate was not obtained. The checked Python environments lacked
Arb/FLINT; bounded python-flint installation attempts under Python3.15
and Python3.12 returned no matching distribution. No 128-bit or 256-bit
Gram pass was run, and no midpoint or floating-point approximation was
substituted. Thus the first-two-zero Gram value, parameter-ball errors,
central quadrature and its analytic callback remain unresolved.

### Independent critical audit, 8 November 2026 (step152)

The audit passes for every claim (1)-(3), with the existing constants
and hypotheses unchanged. This validates local prerequisites, not a
Gram value, orthogonality or an advance beyond the assessed sources.
The step150 implementation stop above remains in effect. The following
checks supersede only its then-unaudited mathematical status.

**Normalization and complex convergence.** Rechecked the primary
version-1 [HTML, Section 1.2](https://arxiv.org/html/2606.17494v1#S1.SS2)
and [Section 2.2](https://arxiv.org/html/2606.17494v1#S2.SS2),
equations (1.2.1)-(1.2.3) and (2.2.1)-(2.2.2). The n=0 terms of
(1.2.3) vanish. Pairing n with -n gives coefficients 2 and -3 in
P_0; L019 has coefficients 8 and -12. Thus W=K/4 on x>=0.
The source's completion (2.2.2) agrees with L018, while (2.2.1)
prints Xi, not Xi/2. No alternate definition of Xi is used to remove
that discrepancy. The exact inversion in L906 supplies evenness of W.

For each compact set of parameters |Im alpha|<=M, the full integrand
is bounded by a constant times
exp((9/2+M)|x|-pi exp(2|x|)). This is integrable, as are its products
with any fixed power of |x|. Therefore both halves, their changes of
variables and complex-parameter differentiation are justified by
domination. The split full transform equals twice the half-line cosine
transform of W, hence Xi/2 by L020. The equality is between entire
functions and the multiplier is nonzero, so it preserves zeros and
their multiplicities. This verifies the coefficient correction; it
does not import the inconsistent printed equality as a premise.

**Positive denominator and complete series.** For x>=0, v=pi exp(2x)>3
and v_n=n^2v. Every summand is positive, and
2v^2-3v-v^2=v(v-3)>0 verifies (4), also at x=0. The complete-series
ratio is

\[
\frac{a_{n+1}}{a_n}=(1+1/n)^6e^{-v(2n+1)}
\le64e^{-9}<\frac1{125}\qquad(n\ge1).
\]

The last strict comparison follows from the L906 rational bound
sum_(j=0)^8 3^j/j!=89641/4480>20, since 89641>89600;
thus e^9>8000 and 64/8000=1/125. Starting with a_1=1 gives
S_6<=125/124<2; termwise n^4<=n^6 gives the asserted S_4 bound.
There is no omitted finite range or tail at n=1 or v=pi.

Independently applying the recurrence to P_0 gives
P_1=-4z^3+15z^2-(15/2)z. For z>=3 its absolute value is at most
(4+5+5/6)z^3=(59/6)z^3<10z^3. The summable compact derivative
majorants of L906 justify this use of the differentiated series.
Its sum is at most 20 exp(x/2)v^3 exp(-v); division by (4) yields
20v. The same full S_4 bound gives (5). Smooth positive even W
makes q smooth and odd, with q(0)=0, so both reflected estimates
hold at the joining point and on the negative half-line. No lower
bound uniform in x, or bounded reciprocal at infinity, is assumed.

**Exact-zero primitive and its constant.** L907's improper lower-end
integral is absolutely convergent, and at finite x the ordinary FTC
gives U_alpha'=-i alpha U_alpha+W. The audited full transform gives
zero total integral at Xi(alpha)=0. Splitting that absolutely
convergent integral proves (6) exactly. For real alpha, both factors
exp(i alpha s) and exp(-i alpha x) have modulus one. On x<=0,
substitution s=-h and evenness bound the lower primitive by
integral_(|x|)^infinity W(h)dh; on x>=0 use (6). These arguments
apply at x=0 without a limiting or half-weight convention.

In the primitive-tail substitution y=pi exp(2s), ds=dy/(2y).
Thus the coefficient is 4pi^2/(2pi^(9/4))=2pi^(-1/4) and the
power of y is 9/4-1=5/4. For y>=v>=pi>3, the logarithmic derivative
5/(4y)-1 is at most -7/12. Its integrated exponential majorant
has integral 12/7, so the prefactor becomes

\[
2\pi^{-1/4}\frac{12}{7}(\pi e^{2r})^{5/4}
=\frac{24\pi}{7}e^{5r/2}.
\]

This checks B without using asymptotic notation. Reality and exact
zero membership are separate hypotheses. The audit does not extend
(6) to all points of a root ball or use unit-modulus estimates at
nonreal parameters.

**Operator sign, both Gram tails and R=0.** Since phi(e^x)=-log W(x),
its x derivative is -q; the source's (3.2.1)-(3.2.2) therefore give
L=(1/i)(d/dx-q). Multiplying U_alpha'=-i alpha U_alpha+W by 1/i
gives the sign -alpha U_alpha-iW+iqU_alpha used above. The three
absolute contributions have constants |alpha|B, 4pi^2 and 20pi B.
Their powers are respectively 5r/2, 9r/2 and 9r/2. Because r>=0,
their sum is bounded by the stated A_alpha times the common last
exponential. No cancellation is required.

For one Gram half, let Y=2pi exp(2R). The substitution y=2pi exp(2r)
has coefficient 1/[2(2pi)^(9/2)] and remaining power y^(7/2).
For every R>=0, Y>=2pi>6, so 7/(2y)-1<=-5/12 throughout y>=Y.
The integrated majorant is (12/5)Y^(7/2)exp(-Y). Its coefficient
after substitution simplifies to

\[
\frac{12/5}{2(2\pi)^{9/2}}(2\pi)^{7/2}
=\frac{3}{5\pi}.
\]

The negative half satisfies the same absolute bound by the estimates
in r=|x|, without asserting equality of the two Gram integrands.
Adding them gives 6/(5pi), as in (3). At R=0 the possible overlap
is the singleton {0}, of measure zero; all functions there are smooth.
The finite bound (6A_alpha A_beta/(5pi))exp(-2pi) therefore controls
the full absolute integral. Taking beta=alpha establishes L2 on the
whole line, and t=exp(x) gives dx=dt/t exactly.

The theorem and its mathematical inputs are unchanged. Finite-span injectivity does not
supply symmetry, and these real-zero norms do not settle the all-zero
metric problem or actual-Xi mixed positivity. Indexed roots, parameter
uncertainty, central integration and any analytic callback are still
unverified. No mathematical script or numerical certificate was needed
for this analytic audit; its complete evidence is the checks above.

### Analytic Gram attempt, 8 November 2026 (step154; unaudited addition)

This addition uses only the hypotheses and canonical inputs above.
For the following identities additionally take distinct real zeros
alpha,beta with alpha<beta. The actual first two distinct positive real
zeros, if selected as in the approved test, are a special case. No
root-location, indexing or simplicity assertion is made here. The
step152 audit applies to (1)-(3), not to this subsequent addition.

Put A=partial_x-q and V=W''/W=q'+q^2. Here V is a scalar function,
unrelated to the enlarged vector space named V in L906. Define

\[
\Gamma_{\alpha\beta}=\int_{\mathbb R}
       G_\alpha(x)\overline{G_\beta(x)}\,dx.
\]

The precise conclusions of this attempt are the identities

\[
\Gamma_{\alpha\beta}\in\mathbb R,\qquad
(\beta-\alpha)\Gamma_{\alpha\beta}
=i\int_{\mathbb R}V'(x)U_\alpha(x)\overline{U_\beta(x)}\,dx
=-2\int_0^\infty V'(x)
             \operatorname{Im}(U_\alpha(x)\overline{U_\beta(x)})\,dx,
\tag{7}
\]

and, when alpha,beta are positive,

\[
\Gamma_{\alpha\beta}=
-\frac{2}{\beta-\alpha}\int_0^\infty\!\int_0^\infty\!\int_0^\infty
 V'(x)W(x+s)W(x+t)\sin(\alpha s-\beta t)\,dt\,ds\,dx.
\tag{8}
\]

All displayed integrals converge absolutely, including the triple
integral before any cancellation. These identities do not establish
zero or nonzero, or a sign, for the required Gram entry.

**Derivative bounds and boundary terms.** L906 gives, for every fixed
integer k>=0, with r=|x|,

\[
|W^{(k)}(x)|\le C_k e^{(2k+9/2)r-\pi e^{2r}}.
\]

The lower bound (4), reflected by evenness, gives on the whole line
W(x)>=pi^2 exp(9r/2-pi exp(2r)). Division therefore proves
|W^(k)/W|<=C_k' exp(2kr). In particular q=O(exp(2r)),
V=O(exp(4r)) and

\[
V'=W'''/W-(W''/W)(W'/W)=O(e^{6r}).
\]

These are bounds by finite constants, not claims about their signs.
For each fixed real zero alpha the ODE gives, for m>=1,

\[
U_\alpha^{(m)}=(-i\alpha)^m U_\alpha+
       \sum_{j=0}^{m-1}(-i\alpha)^{m-1-j}W^{(j)}.
\]

Induction by ordinary differentiation proves this finite identity.
Together with (2), it implies for every m>=0

\[
|U_\alpha^{(m)}(x)|\le C_{\alpha,m}
       e^{(2m+5/2)r-\pi e^{2r}}.
\tag{9}
\]

For m>=1 the largest derivative of W in the finite sum is m-1;
its exponent is 2m+5/2. The m=0 case is (2).
Thus all products used below, including those with q, V and V',
are absolutely integrable and tend to zero at both ends whenever
they occur as boundary terms. For example q f conjugate(g),
f' conjugate(g) and (Hf) conjugate(g) have such bounds for
f=U_alpha, g=U_beta, and also when f or g is replaced by its
first derivative; here H=-partial_x^2+V. Differentiating Hf
requires only f''' and V'f+Vf', already covered. A fixed exponential
exp(Cr) times exp(-c exp(2r)), c>0, is integrable and tends to zero.
This checks both ends separately, without a formal self-adjointness
or completed-domain assumption.

**Green calculation.** Use the integral pairing linear in its first
argument. On finite intervals integration by parts and expansion of A
give, after taking the independently justified endpoint limits,

\[
\langle Af,Ag\rangle
=\int_{\mathbb R}(f'\overline{g'}+(q'+q^2)f\overline g)\,dx
=\langle Hf,g\rangle.
\tag{10}
\]

The first boundary term is -[q f conjugate(g)] and the second is
[f' conjugate(g)], both zero by (9). Likewise
<h,Dg>=<Dh,g> for D=-i partial_x and h=Hf: its only boundary
term is i[h conjugate(g)], also zero. Because L=-iA, (10) yields

\[
\begin{aligned}
\langle LDf,Lg\rangle-\langle Lf,LDg\rangle
 &=\langle HDf,g\rangle-\langle Hf,Dg\rangle\\
 &=\langle(HD-DH)f,g\rangle
 =i\int_{\mathbb R}V'f\overline g\,dx.
\end{aligned}
\tag{11}
\]

The last equality is direct differentiation:
HDf=i f'''-iVf', while DHf=i f'''-iV'f-iVf'.
No commutation of unbounded operator realizations is asserted.
L907's ODE reads DU_alpha=-alpha U_alpha-iW and LW=0.
Consequently LDU_alpha=-alpha G_alpha. Substituting the two
real parameters in the left side of (11) gives exactly
(beta-alpha)Gamma_alpha,beta. This proves the first integral in (7).

**Reflection and the remaining phase.** Evenness of W and the
exact-zero upper-tail representation (6) give

\[
U_\alpha(-x)=e^{i\alpha x}\int_x^\infty e^{-i\alpha y}W(y)dy
           =-\overline{U_\alpha(x)}.
\]

Differentiation gives U_alpha'(-x)=conjugate(U_alpha'(x)).
Since q is real and odd, (AU_alpha)(-x)=conjugate(AU_alpha(x)),
and G_alpha(-x)=-conjugate(G_alpha(x)). The Gram integrand at
-x is therefore the conjugate of its value at x. Absolute convergence
proves that Gamma is real. Also V is real and even and V' is odd.
Writing P=U_alpha conjugate(U_beta), we have P(-x)=conjugate(P(x)),
so splitting the first integral in (7) at zero gives its second one
with the displayed minus sign.

For x>=0, (6) gives exactly

\[
U_\alpha(x)=-\int_0^\infty e^{i\alpha s}W(x+s)ds.
\]

The product of the two absolutely convergent tail integrals has
imaginary part

\[
\int_0^\infty\int_0^\infty
 W(x+s)W(x+t)\sin(\alpha s-\beta t)\,dt\,ds.
\]

To justify also interchanging x with these variables, put
T(x)=integral_x^infinity W(y)dy for x>=0. The proof of (2) gives
T(x)<=B exp(5x/2-pi exp(2x)). Therefore the absolute triple
integral is at most

\[
\int_0^\infty |V'(x)|T(x)^2dx
\le C B^2\int_0^\infty e^{11x-2\pi e^{2x}}dx<\infty.
\]

Fubini's theorem for absolutely integrable functions now applies and
proves (8). It does not discard an oscillatory tail.

**Outcome of the bounded test.** For any fixed x and t>0, the sine
factor has both signs on open s-intervals in (0,infinity), since
alpha>0; W(x+s)W(x+t)>0 throughout. Thus at every x with V'(x)!=0
the inner kernel is not pointwise of one sign. This observation does
not prove that its weighted integral changes sign, nor that some
stronger cancellation estimate is impossible. No such estimate has
been established here, and no sign of V' is presumed. Equations
(7)-(8) consequently leave the decisive relative-phase integral
uncontrolled. The approved first-two-zero test is inconclusive and
this integration-by-parts attempt stops. This is a local standard
calculation under the existing SPECIALIZE assessment, classified
REPRODUCTION, not a new metric obstruction or an RH result. It does
not remove the earlier numerical prerequisite stop.

## Mathlib

Full matching coverage for this normalization and metric-tail result is
unchecked, as is supporting interval integration coverage. No absence
claim is made. This proof relies on the specified canonical theta and
cosine-transform inputs, not on a Mathlib implementation.
Full matching and supporting formal coverage for the step154 Green
calculation and absolutely convergent Fubini specialization is unchecked.
