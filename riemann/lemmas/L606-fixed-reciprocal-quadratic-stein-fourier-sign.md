# Lemma 606: the fixed reciprocal-quadratic Stein model has nonnegative first Fourier sign

## Hypotheses

The prescription is exactly
\[
 \tau(u)=\frac1{1+u^2}\qquad(u\in\mathbb R).
\]
Seek a strictly positive even smooth probability density p on R, with
mean zero and, for every integer j>=0 and B>0,
\[
 |p^{(j)}(u)|\le C_{j,B}e^{-B|u|},
 \qquad
 \tau(u)=\frac{\int_u^\infty v p(v)\,dv}{p(u)}.
\]
Use the Fourier convention F(z)=integral_R p(u)exp(izu)du.

The external inputs, with the exact finite subclass and proof cases
covered in the prior source assessment, are:

1. Adrien Saumard, *Weighted Poincare inequalities, concentration
   inequalities and tail bounds related to Stein kernels in dimension
   one*, [arXiv:1804.03926v3, 23 November 2018](https://arxiv.org/pdf/1804.03926v3),
   Section 2 (5)-(6), pp. 3-4, and Proposition 5 (19), pp. 7-8.
   The representation requires an existing connected-support density
   with finite first moment. It is not an existence theorem for this
   prescription. Existence and the exact tail identity are checked below.
2. Charles M. Newman, *Fourier Transforms with Only Real Zeros*,
   Proc. Amer. Math. Soc. **61** (1976), 245-251,
   [primary article](https://sites.math.northwestern.edu/~auffing/papers/Newman.pdf),
   (1.5), Theorem 2 and its sufficiency proof, pp. 246-248.
   The finite subclass used here consists of measures
   \[
   d\rho(u)=K u^{2m}e^{-a u^4-\beta u^2}
       \prod_{j=1}^N(1+u^2/a_j^2)\,du,
   \]
   with K>0, m a nonnegative integer, a>0, beta real and a_j>0.
   For every b>0, the Fourier transform of exp(-b u^2)d rho(u)
   has only real zeros. The theorem's Laplace-transform statement
   uses imaginary zeros; the Fourier statement follows by z -> iz.
   No infinite compensated product or b=0 assertion is needed.
3. The standard named Hadamard factorization theorem for entire
   functions of finite order, and George Csordas, *Fourier transforms
   of positive definite kernels and the Riemann xi-function*,
   [arXiv:1309.0055v2, 21 February 2014](https://arxiv.org/pdf/1309.0055v2),
   Definition 1.1 and (2.1), pp. 2-3: real Laguerre--Pólya functions
   satisfy F'^2-FF''>=0 on R. Real zeros alone will not be used
   without the growth and product checks below.

## Conclusion

There is exactly one density with the required ratio. It is
\[
 Q(u)=\frac{u^2}{2}+\frac{u^4}{4},\qquad
 Z=\int_{\mathbb R}(1+u^2)e^{-Q(u)}\,du\in(0,\infty),\qquad
 p(u)=Z^{-1}(1+u^2)e^{-Q(u)}.                         \tag{1}
\]
It meets every stated density/decay hypothesis, and tau is strictly
decreasing on (0,infinity). Its entire Fourier transform has order
at most 4/3, only real zeros, and belongs to the Laguerre--Pólya class.
Consequently
\[
 F'(x)^2-F(x)F''(x)\ge0\qquad\hbox{for every real }x.    \tag{2}
\]

Thus this fixed model cannot supply a negative first-sign witness.
This is a specialization of known real-zero and Laguerre results,
not a proof or disproof of the generic monotone-Stein implication.
It gives no Xi sign or estimate for L604's integrated remainder.

## Proof

**Reconstruction and uniqueness.** If p meets the hypotheses, let
h(u)=integral_u^infinity v p(v)dv. Its finite first moment and
continuity give h'(u)=-u p(u). Since h=tau p, strict positivity gives
\[
 \frac{p'(u)}{p(u)}
 =-\frac{u}{\tau(u)}-\frac{\tau'(u)}{\tau(u)}
 =-u-u^3+\frac{2u}{1+u^2}.
\]
Integrating on the connected domain R yields
p(u)=C(1+u^2)exp(-Q(u)), with one constant C>0. The integral Z in
(1) is positive and finite, so probability normalization forces C=1/Z.
This is the elementary specialization of Saumard's reconstruction;
the local ODE and the following tail check are necessary because
the cited representation does not itself construct a law.

For the density in (1), Q'(v)=v(1+v^2) and exp(-Q(v)) tends to zero
at positive infinity. The absolutely convergent integral therefore is
\[
 h(u)=C\int_u^\infty v(1+v^2)e^{-Q(v)}\,dv
     =C e^{-Q(u)}                                      \tag{3}
\]
for every real u, including negative u. There is no deletion of the
negative part of the integrand: (3) follows from the same antiderivative
on every finite interval before taking its upper endpoint to infinity.
Dividing by p verifies the prescribed ratio at both tails and at zero.

The density is positive, even, smooth and has support R. Each
derivative is C P_j(u)exp(-Q(u)), where P_0=1+u^2 and
P_{j+1}=P_j'-(u+u^3)P_j is a polynomial. For every B>0,
|P_j(u)|exp(-Q(u)+B|u|) is bounded, since its limit at both infinities
is zero. This gives precisely the stated derivative bounds. Every
absolute moment is finite; evenness gives mean zero. Both p and h
tend to zero at both infinities, and h times any polynomial tends
to zero there. In particular Saumard's connected-support and
first-moment hypotheses hold; no unverified integration-by-parts
test is being used. Finally tau'(u)=-2u/(1+u^2)^2<0 for u>0.

**Positive-damping application of Newman.** Define the finite positive
even measure
\[
 d\rho(u)=C(1+u^2)e^{-u^4/4+u^2/2}\,du.
\]
Its total mass is finite, since a negative quartic dominates its
quadratic and polynomial factors at both ends. It is exactly the
finite subclass above with
\[
 K=C>0,\quad m=0,\quad a=1/4,\quad\beta=-1/2,
 \quad N=1,\quad a_1=1.
\]
Choose b=1>0. Then exp(-b u^2)d rho(u)=p(u)du exactly.
Newman's theorem therefore gives only real zeros for F. Negative
beta is allowed, the theorem does not require rho to be a probability
measure, and there is no undamped-limit interchange. If its Laplace
variable is w, its transform is L(w)=integral exp(wu-u^2)d rho(u),
so F(z)=L(iz); imaginary zeros of L correspond to real zeros of F.
These are the same integration coordinate and Fourier frequency as
in (1)-(2), with no scaling left implicit.

**Entire growth and the Laguerre step.** For any r>=0 and v>=0,
maximizing r v-v^4/8 gives
\[
 r v-v^4/8\le \frac34\,2^{1/3}r^{4/3}.
\]
Indeed for r>0 the maximum occurs at v=(2r)^{1/3}; r=0 follows
directly. Thus for |z|<=r,
\[
 |F(z)|\le A\exp\bigl((3/4)2^{1/3}r^{4/3}\bigr),\qquad
 A=C\int_{\mathbb R}(1+u^2)e^{-u^4/8-u^2/2}\,du<\infty. \tag{4}
\]
On each compact z-disk, the same bound with an additional |u|^j
is integrable for every fixed j: explicitly it is bounded by
C exp((3/4)2^{1/3}r^{4/3}) |u|^j(1+u^2) exp(-u^4/8-u^2/2).
Hence the integral defines an
entire function, all differentiations under it are justified,
and (4) gives order at most 4/3, strictly less than two.
Also F(0)=1, and evenness and realness on R follow from evenness
and reality of p.

Hadamard factorization now applies to this nonzero entire function.
All its zeros are real by the preceding application, none is zero,
and evenness pairs them as +/-r_k with r_k>0, counted with
multiplicity. Order less than two gives sum_k r_k^{-2}<infinity
and permits genus-one factors and an exponential of degree at most
one. Pairing those factors uses
E_1(z/r_k)E_1(-z/r_k)=1-z^2/r_k^2, so
\[
 F(z)=e^{Az+B}\prod_k(1-z^2/r_k^2).
\]
The paired product converges locally uniformly by that summability.
F(0)=1 gives exp(B)=1. Comparing z and -z near zero, where the
product is nonzero, gives exp(2Az)=1 and hence A=0. Empty or finite
zero sets are included in this argument. Thus
\[
 F(z)=\prod_k(1-z^2/r_k^2).                            \tag{5}
\]
Finite partial products in (5) are real polynomials with only real
zeros; their locally uniform limit is F. This verifies the
Laguerre--Pólya hypothesis of Csordas (2.1), which yields (2).
As a direct check on this application, off the real zeros the
convergent differentiated product gives
\[
 \frac{F'(x)^2-F(x)F''(x)}{F(x)^2}
   =\sum_k\frac{2(r_k^2+x^2)}{(r_k^2-x^2)^2}\ge0.
\]
The differentiated tails converge locally away from the zeros by
sum r_k^{-2}<infinity. At a real zero, the form equals F'(x)^2>=0,
covering simple and multiple zeros without division there.
No converse from the first inequality to all-real zeros is invoked.

The global known-class obstruction meets the approved abandonment
test: terminate the fixed model's negative-value search. Nothing in
this proof transfers its stronger real-zero property to an arbitrary
nonincreasing Stein ratio or to the theta density of L605. The
generic sign implication and actual-Xi signs remain unproved.

**Independent application audit, 1 November 2026.** The reconstruction,
normalization, negative-u tail antiderivative, all derivative bounds and
centering have been replayed under the stated hypotheses. The source
application was checked against Newman's (1.5), class definition and
Theorem 2 sufficiency, printed pp. 246-248: a positive quartic coefficient
allows the negative beta above, and b=1 gives exactly p, not a limiting
measure. Only the finite-product sufficiency case is used. The compact
majorant, exponent 4/3, nonzero value at zero, multiplicity pairing and
removal of the linear exponential were checked independently. In the
last displayed series, for |x|<=R and r_k>=2R the summand is bounded
by (40/9)r_k^{-2}; finitely many remaining terms are harmless on compact
sets avoiding zeros. This verifies the stated differentiated convergence.
At zeros the undivided form applies. Csordas Definition 1.1 and (2.1)
require the product-class check supplied here, not a decreasing density
or any admissible-kernel assertion. All application checks pass; no
mathematical correction or additional theorem is required. This validates
the fixed-model stop only, with no result beyond the cited known class.

## Mathlib

Full matching theorem and supporting-result coverage not checked.
No Mathlib absence claim or formal verification is made. Newman's
finite-class theorem and the named Hadamard/Laguerre inputs are
imported; the fixed reconstruction, hypotheses and coordinate/growth
checks above are the local specialization. Newman's theorem is not
reproved. No numerical Fourier samples are used.
