# Lemma 898: fixed cross-endpoint Xi-defect radii are bounded

## Hypotheses

Use the actual theta kernel K of L019 and the actual Xi of L020. Put
Phi(u)=K(|u|)/2 on the real line, p=u+v, q=u-v, and

\[
 W_y(u,v)=p^2\operatorname{sinhc}(yp)\Phi(u)\Phi(v),\quad
 C_y(z)=\iint_{\mathbb R^2}W_y(u,v)\cos(zq)\,du\,dv,
 \qquad 0\leq y\leq\tfrac12,
\]

where sinhc(t)=sinh(t)/t for t!=0 and sinhc(0)=1. Define

\[
 A_{2j}(y)=\iint W_y q^{2j},\quad m_{2j}(y)=A_{2j}(y)/A_0(y),
 \quad G_y(z)=C_y(iz).
\]

Fix one epsilon with 0<=epsilon<1/2. All bounds below may depend on it.
For integers m>=0 set

\[
 \widehat P_m(x)=1+
 \sum_{\substack{1\leq j\leq2m+1\\j\ {m even}}}
 \frac{A_{2j}(\varepsilon)}{A_0(1/2)}\frac{x^{2j}}{(2j)!}
 -\sum_{\substack{1\leq j\leq2m+1\\j\ {m odd}}}
 \frac{A_{2j}(1/2)}{A_0(\varepsilon)}\frac{x^{2j}}{(2j)!}.
\]

Let Rhat_m be the supremum of r>=0 for which P̂_m(x)>0 whenever
0<=x<r. This is an initial-interval radius, not the last positive point.

## Conclusion

For each such fixed epsilon,

\[
                         \sup_{m\geq0}\widehat R_m<\infty.
\]

This is the analytic obstruction claimed by Leonard van Hemert,
*Finite Positivity Certificates and a Cross-Endpoint Obstruction for a
Riemann Xi-Defect Kernel*, manuscript title date 20 July 2026,
[primary raw source](https://raw.githubusercontent.com/LeonardSEO/certified-riemann-xi-positivity/main/paper/main.tex),
retrieved 8 November 2026: Sections 2–3 and 8–10, especially
`lem:defect`, `lem:monotonicity`, `prop:exact-hierarchy`,
`prop:mixed-limit`, `lem:hyperbolic-growth`, `thm:obstruction`,
and `rem:endpoint`. The inspected raw version has 868 lines;
load-bearing ranges are 130–285 and 524–693 (browser numbering).
No immutable commit or peer-review status is verified. Its formulas and
hypotheses agree with the separately approved 7 November source assessment.

The audit below reproduces that source result and checks its local
applicability; it is not a claim beyond the checked source. Reproduction
is warranted because the newly located manuscript's normalization and
analytic proof had not been independently checked in this notebook.
No finite numerical certificate, zero census, RH assumption, simplicity
assumption, or assertion about reciprocal-node mixed forms is an input.

## Proof

### Normalization, domination and the defect sign

L019 gives exactly

\[
 \Phi(u)=\sum_{n\geq1}(4\pi^2n^4e^{9|u|/2}
                  -6\pi n^2e^{5|u|/2})e^{-\pi n^2e^{2|u|}},
\]

which is the source's full-line kernel, with no rescaling of u. Evenness
and L020 give

\[
 \int_{\mathbb R}\Phi(u)e^{izu}\,du
   =2\int_0^\infty\Phi(u)\cos(zu)\,du=\Xi(z).
\]

For |z|<=R and 0<=y<=1/2 the absolute integrand for C_y is bounded by

\[
 p^2 e^{|p|/2+R|q|}\Phi(u)\Phi(v).
 \tag{1}
\]

Indeed |cos(zq)|<=exp(R|q|) and sinhc(yp)<=exp(|p|/2).
Since |p|,|q|<=|u|+|v|, L019 makes (1), multiplied by any fixed
polynomial in |u|+|v|, integrable. For example its integral is bounded
by a finite sum of products of integrals of
(1+|u|)^k exp((R+1/2)|u|)Phi(u). This supplies absolute Fubini and
dominated differentiation at each required fixed order. It also supplies
continuity in y at zero; a formula divided by y is unnecessary there.

For real x,y, write P(x,y)=|Xi(x+iy)|^2. Multiplication of the two
Fourier integrals gives exp(ixq-yp). Swapping u,v removes the imaginary
part, and simultaneous sign reversal replaces exp(-yp) by cosh(yp).
Thus

\[
 P(x,y)=\iint\Phi(u)\Phi(v)\cosh(yp)\cos(xq),\qquad
 P_y(x,y)=y C_y(x).
 \tag{2}
\]

With f=Xi, E=f+if' and E#=f-if', direct expansion and holomorphic
differentiation give, at z=x+iy,

\[
 |E|^2-|E^\#|^2=-4\operatorname{Im}(f'\overline f)
                    =2P_y=2y C_y(x).
\]

The sign and factor therefore match the source. Differentiating (2) at
y=0 gives C_0=P_yy(x,0)=2(f'(x)^2-f(x)f''(x)). The zero-y defect
identity itself is 0=0; it does not imply this first-sign inequality.

### Strict moments and the lower-polynomial interpretation

Every A_{2j}(y) is finite and positive: its integrand is nonnegative and
positive outside p=0 and, for j>0, q=0. These are null lines. For
0<=y_1<y_2 and p!=0, the convergent series

\[
 \operatorname{sinhc}(yp)=\sum_{r\geq0}\frac{y^{2r}p^{2r}}{(2r+1)!}
\]

is strictly larger at y_2 than y_1 (already its r=1 term is larger).
Integrating proves strict raw-moment monotonicity, including y_1=0.
There is no inference of strictness from a nonzero derivative at zero.
In particular, with a=A_0(epsilon), b=A_0(1/2), we have 0<a<b.

For epsilon<=y<=1/2 and j>=1,

\[
 \frac{A_{2j}(\varepsilon)}b < m_{2j}(y)
                 < \frac{A_{2j}(1/2)}a.
 \tag{3}
\]

For the left inequality, increasing the numerator and decreasing the
denominator from opposite endpoints is weakly favorable; both could
be equalities only at y=epsilon=1/2, which is excluded. The same
argument with the endpoints reversed proves the right inequality.

Put S_m(y,x)=sum_{j=0}^{2m+1}(-1)^j m_{2j}(y)x^{2j}/(2j)!.
To check the source's minorant at every m, let T be the cosine Taylor
polynomial of degree 4m+2. The (4m+2)-nd derivative of cos(t)-T(t)
is 1-cos(t), and all lower derivatives vanish at zero. Repeated
integration makes the difference strictly positive at t>0; evenness
handles t<0. Averaging this pointwise inequality against W_y/A_0(y)
and then using (3) gives, for x!=0,

\[
              \widehat P_m(x)<S_m(y,x)<C_y(x)/A_0(y).
 \tag{4}
\]

All three quantities are one at x=0. The strict lower bound does not
allow a negative P̂_m value to be promoted to a negative C_y value.

### Entire convergence and the constant term

The sum of absolute cosine-series terms on |z|<=R is at most
cosh(Rq). Bound (1) therefore permits absolute interchange and
gives, uniformly on each fixed complex disk and over 0<=y<=1/2,

\[
 C_y(z)=\sum_{j\geq0}(-1)^j A_{2j}(y)\frac{z^{2j}}{(2j)!},
 \qquad G_y(z)=\sum_{j\geq0} A_{2j}(y)\frac{z^{2j}}{(2j)!}.
 \tag{5}
\]

More explicitly, the supremum of each integrated absolute remainder
is bounded by the integral of W_{1/2} times the tail of the nonnegative
cosh(Rq) series; that integral tends to zero by domination. This is
uniform convergence, rather than pointwise convergence asserted to
be uniform. Division by A_0(y)>=A_0(0)>0 preserves it for S_m.
Thus the exact hierarchy in the source is valid on each of its stated
compact rectangles. A positive continuous limit there has a positive
minimum, which all sufficiently late sections retain; (4) gives the
converse. No unbounded rectangle is included in this argument.

Separate even and odd j in (5). The even part is (G_y+C_y)/2; the
odd part is (G_y-C_y)/2. The even sum in P̂_m starts at j=2, whereas
the full even part includes j=0 with value a/b. Consequently

\[
 \widehat P_m(z)\longrightarrow
 F_\varepsilon(z)=1-\frac ab+
 \frac{G_\varepsilon(z)+C_\varepsilon(z)}{2b}
 -\frac{G_{1/2}(z)-C_{1/2}(z)}{2a}
 \tag{6}
\]

locally uniformly on C. In particular F_epsilon(0)=1. Omitting the
constant correction would change that value to a/b and would not be
the limit of the stated polynomials.

### Negative limit and every exceptional degree

For real x, positivity gives |C_y(x)|<=A_0(y). Pointwise monotonicity
of W_y and cosh(xq)>=0 give G_{1/2}(x)>=G_epsilon(x). Therefore (6)
implies

\[
 F_\varepsilon(x)\leq
 1-\frac ab+\frac{a}{2b}+\frac{b}{2a}
 -\frac{b-a}{2ab}G_\varepsilon(x).
 \tag{7}
\]

To check growth without assuming mass on a null line, take for example
the rectangle 2<=u<=3, 0<=v<=1/2. On it p>=2 and |q|>=3/2, and
W_epsilon is continuous and strictly positive, also when epsilon=0.
Its mass c is positive and finite. Restricting the hyperbolic integral
there gives G_epsilon(x)>=c cosh(3x/2) for x>=0. Since b-a>0,
(7) proves F_epsilon(x)->-infinity as x->+infinity.

Choose one finite X>0 with F_epsilon(X)<0. Convergence at that fixed
X supplies an integer M such that P̂_m(X)<0 for all m>=M. Hence
Rhat_m<=X for every such m. This statement alone would not cover all
degrees. For each of the finitely many 0<=m<M, P̂_m(0)=1 and its
leading coefficient, at degree 4m+2, is

\[
                 -\frac{A_{4m+2}(1/2)}{a(4m+2)!}<0.
\]

It tends to -infinity on the positive real axis. Continuity gives a
positive zero, and continuity at zero bounds the first positive zero
away from zero. A nonzero polynomial has finitely many zeros, so the
first one exists and is finite; it equals this initial positivity
radius. Thus max({X} union {Rhat_m:0<=m<M}) is finite, including when
M=0. It bounds every degree and proves the conclusion.

### Endpoint and scope audit

At epsilon=0 the density is p^2 Phi(u)Phi(v); its mass a is positive,
all domination bounds remain valid, and strict raw monotonicity gives
a<b. Thus no positive-epsilon premise was smuggled into the proof.
At epsilon=1/2 we instead have a=b, and (6) reduces to C_{1/2}/b.
The coefficient used in (7) then vanishes. No bound uniform as epsilon
approaches 1/2, no conclusion at the coincident endpoint, and no result
for a degree-dependent epsilon follows from this audit.

The result retires only the fixed cross-endpoint lower-polynomial
extension. The exact sections, changing cells, signed correlation
estimates, all-height defect positivity, and the L030–L032/C032a
mixed-form gap remain unresolved. The source's finite certificates and
its further RH-equivalence discussion are not verified here. ∎

## Mathlib

Full matching coverage was not checked; availability is unknown.
The audit uses ordinary dominated convergence, Fubini, convergent
power series and polynomial continuity, but no specific supporting
Mathlib theorem has been identified. The source is a mathematical
manuscript, not a formal proof certificate.
