# Lemma 604: a two-point Stein decomposition with an unavoidable signed remainder

## Hypotheses

Let p be a strictly positive even C-infinity probability density on R.
For each integer j>=0 and B>0 assume
|p^(j)(u)|<=C_(j,B) exp(-B|u|). Define

\[
h(u)=\int_u^\infty v p(v)\,dv,\qquad
\tau(u)=h(u)/p(u),\qquad
F(x)=\int_{\mathbb R}p(u)e^{ixu}\,du.
\]

Assume tau is nonincreasing on (0,infinity), and put c=tau(0).
The normalization and decay put p within L233's hypotheses.

The external identity used below is Adrien Saumard, *Weighted Poincare
inequalities, concentration inequalities and tail bounds related to
Stein kernels in dimension one*,
[arXiv:1804.03926v3, 23 November 2018](https://arxiv.org/pdf/1804.03926v3),
Section 2, equations (5)-(6), printed pp. 3-4:
E[X phi(X)]=E[tau(X) phi'(X)] for centered laws with connected density
support, finite absolute first moment, integrable terms, and vanishing
endpoint product h*phi. Each use is checked below. No variance or
Fourier-sign theorem is imported, and the Stein identity is not reproved.

## Conclusion

For s in (0,c), set

\[
H_s(x)=\int_{\{u:\tau(u)>s\}}p(u)e^{ixu}\,du,
\qquad M(x)=\int_0^c |H_s(x)|^2\,ds.
\]

For a>b>0 define Delta(a,b)=tau(b)-tau(a)>=0 and

\[
\begin{split}
K_x(a,b)={}&\cos(x(a+b))+\cos(x(a-b))\\
&+x(a-b)\sin(x(a+b))+x(a+b)\sin(x(a-b)),\\
R(x)={}&2\int_0^\infty\int_0^a
\Delta(a,b)p(a)p(b)K_x(a,b)\,db\,da.
\end{split}                                                    \tag{1}
\]

All these integrals converge, H_s is real, 0<=M(x)<=c, and

\[
F'(x)^2-F(x)F''(x)=M(x)+R(x)\qquad (x\in\mathbb R).       \tag{2}
\]

For every x!=0, K_x takes both signs in the open triangle a>b>0:

\[
K_x(2\pi/|x|,\pi/|x|)=-2,\qquad
K_x(4\pi/|x|,2\pi/|x|)=2.                                \tag{3}
\]

More specifically, if tau is nonconstant, there exists x_*>0 such
that the integrand defining R(x_*) is strictly negative on a nonempty
open subset of that triangle. Thus nonincrease does not make this
representation's remainder pointwise nonnegative. If tau is constant,
R=0 and (2) becomes D(x)=c F(x)^2, where D=F'^2-FF''.

This does **not** assert that R(x_*)<0 or that D(x_*)<0. In particular,
this identity is not itself a counterexample to the monotone-Stein
first-sign criterion. The later, independently audited L607 refutes
that generic criterion; it is a contrast, not an input here. If R_+
and R_- denote the integrals in (1) with K replaced
by its positive and negative parts, respectively, the remaining
requirement is R_-(x)<=M(x)+R_+(x) for every x. No such integrated
estimate is proved here. This lemma does not establish the actual-theta
premise or any higher Xi sign. This is one representation-specific obstruction,
not an impossibility theorem for other uses of Stein monotonicity.

## Proof

**Applicability and convergence.** Evenness and the finite first
moment give mean zero. For u>=0, h(u)>0. Changing variables in the
negative tail and using the zero mean gives h(-u)=h(u). Thus tau is
positive, even and smooth, and its assumed nonincrease implies
0<tau(u)<=c for every u. The density support is the connected interval
R. Every absolute moment exists. Differentiation of F to any fixed
order is justified by domination with the corresponding moment;
in particular F, F', F'' are real on the real axis.

In each Stein use below, for fixed v and x the test is

\[
\phi_v(u)=(u-v)\cos(x(u+v)),\qquad
\phi_v'(u)=\cos(x(u+v))-x(u-v)\sin(x(u+v)).
\]

Both sides of the identity are absolutely integrable: they are
bounded by a constant depending on x,v times (1+u^2)p(u) and
(1+|u|)h(u), respectively. Since h<=c p and p has the stated decay,
h(u) phi_v(u) tends to zero at both ends. Integrating also against
p(v) preserves absolute convergence by the first two moments.
For the v term the test is explicitly
psi_u(v)=(v-u)cos(x(u+v)), whose derivative is
cos(x(u+v))+x(u-v)sin(x(u+v)). The same checks apply.
Writing m_j=integral |u|^j p(u) du, the absolute double integral
of each pre-Stein term is at most m_2+m_1^2. The absolute double
integral of each post-Stein term is at most c(1+2|x|m_1).
Thus the fixed-parameter identities may indeed be integrated in the
other variable, without an unproved interchange of boundary limits.
No estimate on tau'
and no growth assertion about tau independent of its definition is
used. These verify all hypotheses of the cited identity.

**The complete two-point identity.** L233's absolutely convergent
double-integral identity, with k=p and v replaced by -v, gives

\[
D(x)=\tfrac12\iint (u-v)^2p(u)p(v)\cos(x(u+v))\,du\,dv.    \tag{4}
\]

In detail, L233 gives D=4*hat A(2x) and
hat A(2x)=(1/8) integral integral (u+v)^2 p(u)p(v)
exp(ix(u-v)) du dv. Their product supplies the factor 1/2;
reflection v to -v uses evenness of p. Taking real parts gives (4).
This use needs neither L233's comparison example nor its theta inputs.

Write (u-v)^2=u(u-v)-v(u-v) and apply Stein in the corresponding
variable. The u term contributes
tau(u)[cos(x(u+v))-x(u-v)sin(x(u+v))]; the negative v term contributes
tau(v)[cos(x(u+v))+x(u-v)sin(x(u+v))]. Hence

\[
\begin{split}
D(x)={}&\tfrac12\iint (\tau(u)+\tau(v))p(u)p(v)
                      \cos(x(u+v))\,du\,dv\\
&-\tfrac x2\iint (\tau(u)-\tau(v))(u-v)p(u)p(v)
                      \sin(x(u+v))\,du\,dv.                \tag{5}
\end{split}
\]

All uses of Fubini in (4)-(5) follow from the bounds just given.
If G(x)=integral h(u) cos(xu) du, evenness and interchange of u,v
identify the first line of (5) as F(x)G(x). There is no claim that
this product is nonnegative.

**A nonnegative part without a sign assumption on F*G.** Evenness
also permits cos(x(u-v)) in that first line. The elementary layer
identity

\[
\min(\tau(u),\tau(v))
=\int_0^c {\bf1}_{\tau(u)>s}{\bf1}_{\tau(v)>s}\,ds
\]

and absolute Fubini give

\[
\iint \min(\tau(u),\tau(v))p(u)p(v)\cos(x(u-v))\,du\,dv
=\int_0^c |H_s(x)|^2\,ds=M(x).                            \tag{6}
\]

The total absolute triple integral is at most c. The conjugate in
the product of transforms in (6) is essential: this is a modulus
square, not an assumed sign of an algebraic Fourier product. Since
each superlevel set of the even function tau is even, H_s is real.
Also |H_s|<=1, giving 0<=M<=c. No Stein identity is applied to the
indicator functions. In particular no inverse of tau, derivative of
a superlevel boundary, or strict monotonicity is used. Flat portions
cause no exception: the indicator layer identity holds for every u,v,
with the endpoints in s irrelevant to its integral. If tau has a
positive limiting floor ell, all levels 0<s<ell give H_s=F and are
already included. The case tau identically c is included in the same
way, with every level 0<s<c contributing F.

Using (tau(u)+tau(v))/2=min(tau(u),tau(v))
+|tau(u)-tau(v)|/2, the difference F*G-M equals

\[
\tfrac12\iint|\tau(u)-\tau(v)|p(u)p(v)
                                  \cos(x(u-v))\,du\,dv
=4\int_{a>b>0}\Delta(a,b)p(a)p(b)\cos(xa)\cos(xb)\,da\,db.
                                                               \tag{7}
\]

For clarity, summing the four sign choices (u,v)=(+/-a,+/-b)
in the first integral gives 4 cos(xa) cos(xb); its factor 1/2 then
gives 2 on the positive quadrant. Symmetry between a,b gives the
factor 4 on the triangle. The diagonals have Lebesgue measure zero.

For the second line of (5), the same four sign choices yield

\[
2(\tau(a)-\tau(b))
\{(a-b)\sin(x(a+b))+(a+b)\sin(x(a-b))\}.
\]

The entire expression is symmetric in a,b. Multiplying by -x/2
and restricting to a>b therefore gives

\[
2x\int_{a>b>0}\Delta(a,b)p(a)p(b)
\{(a-b)\sin(x(a+b))+(a+b)\sin(x(a-b))\}\,da\,db.           \tag{8}
\]

Combining (7)-(8) and
2 cos(xa) cos(xb)=cos(x(a+b))+cos(x(a-b)) proves (1)-(2).
The bound |K_x(a,b)|<=2+2|x|a on this triangle and
0<=Delta<=c proves absolute convergence of R, R_+, and R_- using
only the first moment. It also justifies all quadrant rearrangements.

**Zero frequency and the degenerate cases.** There has been no division
by x. At x=0, F(0)=1, F'(0)=0 and -F''(0)=m_2, so D(0)=m_2.
Equation (6) gives M(0)=integral integral min(tau(u),tau(v))
p(u)p(v) du dv. Since K_0=2, (1) gives
R(0)=4 integral_(a>b>0) Delta(a,b)p(a)p(b) da db, exactly
the absolute-difference term (7) at zero. Consequently
M(0)+R(0)=integral tau(u)p(u) du=integral h(u) du=m_2.
The last equality is also checked directly by nonnegative Tonelli:

\[
\int_{\mathbb R}h(u)\,du
=2\int_0^\infty\int_u^\infty v p(v)\,dv\,du
=2\int_0^\infty v^2p(v)\,dv=m_2.
\]

The layer integrals are dominated by total mass c, and the R integrals
by the preceding bound uniformly on compact frequency intervals.
Thus their continuity at zero also follows by dominated convergence;
no zero-frequency limit of a divided Fourier identity is imported.
When tau is constant, (7)-(8) vanish, M=c|F|^2=cF^2 and R=0
for every real x, including zero. Flat portions were already covered
by (6), so none of these checks assumes tau'<0.

**The exact remaining sign obstruction.** The values in (3) follow
from cos(3pi)=cos(pi)=-1, cos(6pi)=cos(2pi)=1, and the vanishing of
the corresponding sines. K_x is even in x and continuous in a,b;
both signs therefore persist on open subsets of the triangle.

Suppose now that tau is nonconstant. By evenness and monotonicity,
there are 0<r<s with tau(r)>tau(s); continuity rules out variation
only at the origin. Choose an integer N>=1 with
2^N r>=s. Then

\[
\sum_{j=0}^{N-1}\{\tau(2^j r)-\tau(2^{j+1}r)\}
=\tau(r)-\tau(2^N r)>0.
\]

All summands are nonnegative, so some b_*=2^j r satisfies
tau(b_*)>tau(2b_*). At x_*=pi/b_*, take a_*=2b_*.
Equation (3) gives K_(x_*)(a_*,b_*)=-2, while Delta(a_*,b_*)>0
and p(a_*)p(b_*)>0. Continuity gives a small open rectangle around
(a_*,b_*) contained in a>b>0 on which the remainder integrand is
strictly negative. A smaller closed rectangle has negative integral;
thus R_-(x_*)>0. No inference about the sign of the full remainder
or D follows. If tau is constant, Delta=0 and (6) gives M=c F^2,
which proves the stated constant-kernel check.

The attempt therefore stops at the fully specified integrated
inequality following (3). Monotonicity supplies the sign of Delta;
it does not remove the negative contribution just proved. Additional
cancellation or quantitative comparison with M and R_+ would be
needed. Neither weighted Poincare positivity nor the original
negative-sign mixture of L233 is used to bypass that step; C233b
excludes that mixture from the present premise.

**Independent identity audit, 1 November 2026.** The complete L233
normalization, both Stein tests, their endpoints and joint absolute
bounds, conjugation and layer normalization, all four quadrant factors,
zero/constant/flat cases and the strict dyadic pointwise witness have
been replayed. The cited Saumard v3 (5)-(6), pp. 3-4, was checked
directly with its integrability and endpoint conditions. No sign,
factor or hypothesis mismatch was found; the displayed identity is
unchanged. The explicit estimates and special-case checks above make
the replay checkable without a numerical certificate. This validates
an existing representation, not an integrated compensation estimate
or a new result beyond the sources checked. L605 and L608 are not
premises. The direct local mathematical input remains L233 alone.

## Mathlib

Full-result and supporting-result coverage not checked. No matching
formal theorem is claimed. The Stein identity is imported by the
precise citation above; its two-point specialization, layer-of-squares
decomposition and pointwise sign obstruction are proved here under
the previously assessed scope. The literature assessment did not
establish coverage of this complete representation; that fact does
not certify originality. No actual-theta sign or new zeta estimate is
claimed.
