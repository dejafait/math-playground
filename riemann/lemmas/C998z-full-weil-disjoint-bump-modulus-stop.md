# C998z: Complete-Weil disjoint-bump modulus obstruction

## Hypotheses

Use the complete smooth actual-zeta Weil form, with zero extension,

\[
 F_f(t)=\int_{\mathbb R}f(x)e^{-itx}\,dx,\qquad
 C_f(d)=\int_{\mathbb R}f(x+d)\overline{f(x)}\,dx,
\]
\[
 \begin{split}
 Q(f)={}&\int_{\mathbb R}
 [\Re\psi(1/4+it/2)-\log\pi]|F_f(t)|^2\frac{dt}{2\pi}\\
 &+2\Re\bigl(F_f(i/2)\overline{F_f(-i/2)}\bigr)
 -2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\Re C_f(\log n).
 \end{split}                                                   \tag{1}
\]

This is L744(6), equivalently the geometric form cited in C744m(3):
Vincent Liu, *Certified Weil Positivity Beyond the Unit Window:
Source-Exact Block-Schur and Tail-Compensation Bounds for the Riemann
Zeta Function*, manuscript 14 September 2026, Section 2 equation (1),
[primary manuscript](https://www.alphaxiv.org/abs/2609.weil-positivity-riemann-zeta-bounds.pdf).
Only the formula is used; the source's positivity theorem and its
unreplayed computer certificate are not premises. Its normalization
and smooth applicability were assessed in review492 and assessment788.

The kernel identities imported below are L741(7), (13), (16)-(18),
used at arbitrary fixed interval length by L744(5)-(6). Their analytic
source includes the digamma integral [NIST DLMF 5.9.13](https://dlmf.nist.gov/5.9.E13),
valid at the required argument with real part 1/4. We do not reprove
the explicit formula or use a positivity-preserving semigroup theorem.

Define

\[
 b(s)=\begin{cases}e^{-1/(1-s^2)},&|s|<1,\\0,&|s|\ge1,\end{cases}
 \quad u(x)=b(100(x+1/2)),\quad v(x)=b(100(x-1/2)),
 \quad A=\int_{\mathbb R}u=\int_{\mathbb R}v>0.
                                                               \tag{2}
\]

There is no neutrality, Fourier cutoff, norm cap or RH assumption.

## Conclusion

For exactly the pair (2),

\[
 \boxed{\Delta:=Q(u+v)-Q(u-v)>\frac83 A^2>0.}             \tag{3}
\]

Since |u-v|=u+v, the full-form modulus inequality
Q(|f|)<=Q(f) fails on C_c^infinity((-1,1)) at f=u-v.
This is an informative negative test of that proposed extension of the
limiting-form mechanism, classified REPRODUCTION. It is not a claim of
novelty beyond the sources checked. Neither Q(u-v)<0, a ground-state
sign, a semigroup conclusion, an off-line zero nor an RH resolution
follows. The separate audit below (13 November 2026, step791) accepts
the identity, arithmetic exclusions and strict bound for this exact
pair; it does not validate any external positivity certificate.

## Proof

### 1. Smoothness and the complete arithmetic contribution

The usual zero extension of b is smooth: every one-sided derivative
at |s|=1 is a finite sum of a rational function of s, with at most a
finite-order pole there, times e^{-1/(1-s^2)}. Each such term tends to
zero because t^N e^{-t}->0 as t->infinity for every fixed N. Induction
on derivative order therefore matches all derivatives to zero.
Consequently u,v and u+v,u-v are smooth compact tests in (-1,1).
Their supports are [-51/100,-49/100] and [49/100,51/100], respectively;
they are strictly positive on the interiors and disjoint. The integrals
in (2) are finite, equal by translation, and positive.

For d>0 set

\[
 H(d)=\int_{\mathbb R}u(x)v(x+d)\,dx\ge0.
\]

It vanishes unless 49/50<d<51/50. Self-correlations of either bump
vanish for d>=1/50. Orientation of the disjoint supports gives

\[
 C_{u+v}(d)-C_{u-v}(d)=2H(d),\qquad
 \|u+v\|_2^2-\|u-v\|_2^2=0,\qquad
 \int_0^\infty H(d)\,dd=A^2.                             \tag{4}
\]

The last identity is ordinary Fubini with y=x+d; all points with
u(x)v(y)>0 have y>x. All integrands have compact support.

Here are elementary exact logarithm bounds needed to check every
prime power. For 0<t<1 the exponential series gives e^t<1/(1-t).
Also

\[
 e^{1/50}<50/49<2,\qquad
 e^{49/50}>1+49/50+\tfrac12(49/50)^2>2.
\]

For n>=3 the factorial terms obey
1/n!<= (1/6)(1/4)^{n-3}, strictly for n>=5. Hence

\[
 e<1+1+\tfrac12+\frac{1/6}{1-1/4}=49/18,
 \qquad e^{51/50}=e\,e^{1/50}<25/9<3.
\]

Thus

\[
 1/50<\log2<49/50<51/50<\log3.                          \tag{5}
\]

For n=2 neither a self difference nor a cross difference can equal
log2. For every n>=3, including every power 2^j with j>=2 and every
other prime power, log n exceeds the entire support diameter 51/50.
Therefore C_{u+v}(log n)=C_{u-v}(log n)=0 for every n>=2. This
accounts for the full arithmetic sum in each form, not merely its
cross difference. No tail or favorable term is discarded.

### 2. Gamma term with its regularization retained

Write q_m for the first term of (1). To apply the causal identities,
translate both tests by +1 into (0,2). For g(x)=f(x-1) one has
F_g(z)=e^{-iz}F_f(z), C_g=C_f, and the pole factors acquire the
reciprocal real factors e^{1/2},e^{-1/2}; hence every term of Q is
unchanged. Differences and H are likewise unchanged.

On these translated smooth tests L744(5)-(6) express

\[
 q_m(f)=-\Re\langle(D+cI+R)f,f\rangle,\quad c=\log(2\pi),
\]
\[
 D_\epsilon f=\int_\epsilon^\infty\frac{e^{-d}}d
                    [f(\cdot-d)-f]\,dd,\quad
 D_\epsilon f\longrightarrow Df\text{ in }L^2,
\]
\[
 (Rf)(x)=\int_0^\infty r(d)f(x-d)\,dd,\quad
 r(d)=k(d)-e^{-d}/d,\quad
 k(d)=\frac{2e^{-d/2}}{1-e^{-2d}},\quad r\in L^1(0,\infty).
                                                               \tag{6}
\]

These are the imported truncated-generator and digamma identities of
L741, not a replacement of the gamma multiplier by log|t|. The
inner product is linear in its first argument. In the difference
between u+v and u-v, the scalar c term vanishes by (4). The subtraction
-f inside D_epsilon also cancels by that norm identity **before**
letting epsilon decrease. Using (4), for 0<epsilon<49/50 its remaining
contribution to the difference is exactly

\[
 -2\int_0^\infty\frac{e^{-d}}d H(d)\,dd.
\]

The R contribution is -2 integral r(d)H(d) dd. Both integrals are
absolutely convergent; H is supported away from zero and on a fixed
compact interval. The L2 convergence in (6) passes the pairings to
the limit. Consequently, with all regularizing scalars accounted for,

\[
 q_m(u+v)-q_m(u-v)=-2\int_0^\infty k(d)H(d)\,dd.        \tag{7}
\]

No separate divergent integral or distributional diagonal value has
been evaluated, and no closed-form-domain extension is required.

### 3. Both poles and the uniform sign

For any of our real compact tests, finite-square Fubini gives

\[
 2F_f(i/2)F_f(-i/2)
 =4\int_0^\infty\cosh(d/2)C_f(d)\,dd.
\]

Indeed the full-square integral with e^{(x-y)/2} symmetrizes to
cosh((x-y)/2); its two half-squares are equal. The diagonal has
Lebesgue measure zero. Thus by (4) the complete pole difference is
+8 integral cosh(d/2)H(d) dd. Combining this with (7) and the exactly
zero arithmetic contributions proves the identity

\[
 \Delta=2\int_{49/50}^{51/50}
             [4\cosh(d/2)-k(d)]H(d)\,dd.                \tag{8}
\]

For every d in the closed interval [49/50,51/50],

\[
 e^{2d}\ge e^{49/25}
 >1+49/25+\tfrac12(49/25)^2>4.
\]

Therefore 1-e^{-2d}>3/4, e^{-d/2}<1 and k(d)<8/3. Since
cosh(d/2)>=1, the bracket in (8) is strictly greater than 4/3
throughout this interval. Integrating the uniform bound and using
(4) proves (3); strictness follows also directly from A>0 and the
strict continuous kernel bound on this compact interval.

Finally, disjoint nonnegative supports imply |u-v|=u+v pointwise,
and both functions remain in the stated smooth domain. Equation (3)
therefore violates the proposed modulus comparison at its required
threshold zero. This stops only that comparison; positivity of Q
and all independent Xi/limit/ground-state gaps remain separate.

### 4. Separate fixed-pair audit, 13 November 2026, step791

The audit replays the complete calculation against L741(7),(13),
(16)-(18) and L744(5)-(6), using the unchanged SPECIALIZE coverage in
assessment789. It is REPRODUCTION: local verification of a standard
specialization, with no claim of progress beyond the sources checked.
The required comparison is Delta<=0; the verified lower bound has the
opposite strict sign. No numerical quadrature or mathematical script
is needed for this exact proof.

**Domain, orientation and translation.** Smoothness of the zero
extension follows at every derivative order from exponential decay
against any finite power; the two affine substitutions preserve this
property. Thus all four tests are in the stated smooth domain. The
translation by +1 places their supports in [49/100,51/100] and
[149/100,151/100], inside (0,2). Its real Fourier phase preserves the
gamma term, its two imaginary Fourier factors cancel in the pole
product, and correlations are unchanged. L744's arbitrary-fixed-L
smooth calculation therefore applies without importing the sign or
closed-domain conclusions for L741's different length log(3).

For d>0, expand the correlations before applying any kernel:

\[
 C_{u+v}(d)-C_{u-v}(d)
 =2\int [u(x+d)v(x)+v(x+d)u(x)]\,dx=2H(d).
\]

The first summand vanishes by support orientation. The only positive
cross separations are 49/50<d<51/50; endpoint intersections have
measure zero (and the bumps vanish there). Self separations are
strictly less than 1/50. Fubini applies to the compact nonnegative
integrand u(x)v(y), whose nonzero set satisfies y>x, and gives
integral H=A^2. Disjointness also gives exact equality of the two
squared norms and |u-v|=u+v, including the endpoints and their common
zero set. Hence taking the modulus does not leave the smooth domain.

**Every arithmetic delay.** The strict geometric-series estimate
e^t<1/(1-t) for 0<t<1 follows by coefficient comparison, with a
strict coefficient from degree2 onward. In particular e^(1/50)<50/49<2.
The lower polynomial at 49/50 equals 12301/5000>2. For the bound on e,
the ratio of successive factorial terms starting at degree3 is at
most 1/4, with strictness starting at degree 5, so the stated geometric
majorant gives e<49/18. Thus e^(51/50)<25/9<3, and all of (5) holds
strictly. The delay log2 lies between the self and cross separation
ranges. Each integer n>=3 has log n>=log3>51/50; this includes every
remaining prime power. Both entire correlations, not only their
difference, are zero at every arithmetic delay. All coefficients
Lambda(n)/sqrt(n) consequently multiply exact zeros.

**Scalar, cutoff and gamma sign.** Using L741's imported transform
at p=it, the sum of the D,cI,R multipliers is

\[
 -\log(1+it)+\log(2\pi)
 +\log(1+it)-\psi(1/4+it/2)-\log2
 =\log\pi-\psi(1/4+it/2).
\]

Taking minus the real pairing yields exactly the gamma symbol in
(1). The digamma argument has real part 1/4; the logarithms used in
the imported identity are in the right half-plane. No extra Euler
constant, pole term or diagonal scalar is to be added.

For completeness the cutoff limit here can be checked directly,
without a closed-domain extension. For smooth compact f,
||f(.-d)-f||_2<=d||f'||_2. The norm of the omitted integral from 0 to
epsilon in D_epsilon is therefore <=epsilon||f'||_2; the integral
for d>=1 converges in L2 by its exponential weight. This proves the
needed L2 convergence on these tests. At every fixed epsilon the
scalar c term and the -f subtraction contribute a multiple of
||u+v||_2^2-||u-v||_2^2=0, before taking that limit. The remaining
causal pairing difference is 2H(d). For epsilon<49/50 its support
lies entirely above epsilon. Thus minus the D pairing gives
-2 integral e^(-d)H(d)/d, minus the R pairing gives
-2 integral r(d)H(d), and their sum is exactly (7). Both integrals
are absolutely convergent on the compact separation interval. This
checks the gamma factor 2 and its negative sign independently of a
formal subtraction of divergent integrals.

**Both poles and the final strict bound.** For real f, the product
F_f(i/2)F_f(-i/2) is the finite-square integral with weight
exp((x-y)/2). Exchanging x and y replaces that weight by its inverse;
averaging gives cosh((x-y)/2). Its two half-squares have equal
integrals, so the coefficient 2 in (1) gives coefficient 4 on d>0.
The correlation difference 2H therefore produces coefficient 8 for
the pole difference. Together with the gamma factor -2 and zero
arithmetic terms, this is precisely (8), with no lost conjugation
or replacement of the signed pole product by a modulus square.

The lower exponential polynomial at 49/25 is 6101/1250>4. Hence on
the entire closed separation interval, 1-e^(-2d)>3/4 and
2e^(-d/2)<2, giving k(d)<8/3. Since cosh(d/2)>=1, the bracket in
(8) is >4/3 at every point of that interval. It is continuous there;
compactness even gives a uniform strictly positive margin above 4/3.
With H>=0 and integral H=A^2>0 this proves
Delta>2(4/3)A^2, including the strictness in (3).

All audit obligations pass without a mathematical repair. The result
rules out only Q(|f|)<=Q(f) on the stated full smooth domain. It
does not compute the sign of either individual energy, compare
lowest parity eigenvalues, establish a semigroup criterion, or
remove any Xi-realization, multiplicity or global-sign gap.

## Mathlib

Full matching Mathlib coverage of (1), its complete-Weil off-diagonal
specialization, or this fixed-pair obstruction has not been checked.
Elementary support, exponential and integration facts are supporting
standard inputs, not a formalization of the full result. No absence
claim or Lean verification is made.
