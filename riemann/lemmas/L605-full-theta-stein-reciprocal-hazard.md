# Lemma 605: the full theta Stein kernel is a scaled reciprocal hazard

## Hypotheses

Use exactly L019's kernel K on [0,infinity), its even extension
k(u)=K(|u|) on R, and the normalized full-line density

\[
 Z=\int_{\mathbb R}k(u)\,du,\qquad p(u)=k(u)/Z.
\]

Define the centered Stein ratio by

\[
 h(u)=\int_u^\infty v p(v)\,dv,\qquad \tau(u)=h(u)/p(u).
\]

The named external inputs are imported as stated:

1. George Csordas, *Fourier transforms of positive definite kernels and
   the Riemann xi-function*, [arXiv:1309.0055v2, 21 February 2014](https://arxiv.org/pdf/1309.0055v2),
   equation (4.2), Theorem 4.1(i)-(iv), p. 10, and Theorem 4.2(b), p. 11.
   For the function Phi defined in (4.2), these give positivity on
   [0,infinity), even analyticity, superexponential derivative decay,
   and strict concavity of log Phi(sqrt(s)) for s>0.
2. Mark Bagnoli and Theodore C. Bergstrom, *Log-Concave Probability and
   Its Applications*, [4 March 2004 manuscript](https://escholarship.org/content/qt0xt8k6sd/qt0xt8k6sd_noSplash_d3b995fc634e40551bbd3dc90a1b0e43.pdf),
   Theorem 3 and Corollary 2, p. 4: a positive C1 log-concave probability
   density on an interval has nondecreasing hazard there.
3. Adrien Saumard, *Weighted Poincare inequalities, concentration
   inequalities and tail bounds related to Stein kernels in dimension
   one*, [arXiv:1804.03926v3, 23 November 2018](https://arxiv.org/pdf/1804.03926v3),
   Section 2 (5)-(6), printed pp. 3-4: for a density with connected
   support and finite absolute first moment, the centered tail ratio
   above is a version of its Stein kernel. The associated identity
   requires integrable terms and a vanishing endpoint product.

## Conclusion

The density p is strictly positive, even and smooth on R, has mean
zero, and every derivative decays faster than every exponential.
The ratio tau is strictly positive, even and smooth on R and is
nonincreasing on [0,infinity). In particular,

\[
 0<\tau(u)\le\tau(0)<\infty,\qquad \tau'(0)=0.
\]

More precisely, define the auxiliary probability density, survival
function and hazard on (0,infinity) by

\[
 q(s)=\Phi(\sqrt{s}),\quad J=\int_0^\infty q(s)\,ds,\quad
 f(s)=q(s)/J,\quad S(s)=\int_s^\infty f(t)\,dt,\quad
 r(s)=f(s)/S(s).
\]

Then

\[
 \boxed{\tau(u)=\frac{2}{r(u^2/4)}\quad(u>0)},\qquad
 \tau(0)=\frac{2J}{\Phi(0)}.                         \tag{1}
\]

This verifies only the full-theta monotonicity premise. It proves no
Fourier Laguerre sign, no bound on L604's integrated signed remainder,
and no all-degree positivity or RH assertion. Nonincrease is asserted
on the positive half-line with its zero endpoint, not on all of R.

## Proof

**Coordinates and full-line applicability.** Source equation (4.2) is

\[
 \Phi(t)=\sum_{n\ge1}\pi n^2(2\pi n^2e^{4t}-3)
                 \exp(5t-\pi n^2e^{4t}).
\]

For u>=0, multiplication of its summand at t=u/2 by 4 gives

\[
 [8\pi^2n^4e^{9u/2}-12\pi n^2e^{5u/2}]
                    e^{-\pi n^2e^{2u}},
\]

exactly L019's summand. Both series converge there, so
K(u)=4 Phi(u/2). Source Theorem 4.1's evenness then gives
k(u)=4 Phi(u/2) for every real u, including zero; it also establishes
smoothness across zero rather than assuming that an even extension
of a half-line function is smooth.

L019's positivity and integrable superexponential bound give
0<Z<infinity and every absolute moment. Explicitly, evenness and
u=2t give Z=16 integral_0^infinity Phi(t) dt. Source Theorem 4.1(iv),
with any fixed 0<epsilon<pi, gives for each j>=0 the derivative
decay of Phi^(j)(t) as t tends to infinity. Since e^(4t) dominates
every linear function, scaling and evenness show that for every B>0

\[
 |p^{(j)}(u)|\le C_{j,B}e^{-B|u|}\quad(u\in\mathbb R)
\]

for some finite C_(j,B); the compact remaining interval is bounded
by continuity. Thus p has connected positive support R, finite
absolute first moment and mean zero by evenness. These check the
hypotheses of Saumard's ratio formula. No integration-by-parts
identity or test function is used in this specialization.

For u>=0, h(u)>0. The integrable odd function v p(v) has integral
zero on [-u,u], hence h(-u)=h(u). The fundamental theorem of
calculus gives h'(u)=-u p(u), so h and tau=h/p are smooth and even,
and tau is positive on all of R. Also h(u) tends to zero as
u tends to either infinity, by the integrable first moment and
evenness. These tail facts do not assume a bound for tau.

**Auxiliary normalization and hazard hypotheses.** Near zero,
q(s)=Phi(sqrt(s)) extends continuously to q(0)=Phi(0)>0 and is
bounded. At infinity the substitution s=t^2 gives

\[
 J=2\int_0^\infty t\Phi(t)\,dt\in(0,\infty),           \tag{2}
\]

using the same positive integrable first-moment tail and scaling
as above. The substitution can first be made on bounded positive
intervals and then passed to both endpoints by positivity. Thus
f is a probability density, positive and C1 on the interval
(0,infinity). Source Theorem 4.2(b) gives log-concavity of q,
and normalization subtracts only the constant log J from its
logarithm. The auxiliary density is proportional to Phi(sqrt(s));
it is not the law of a squared variable with density p, whose
Jacobian would change this density.

For every s>0, 0<S(s)<infinity and f(s)>0, so r(s) is finite and
strictly positive. Bagnoli--Bergstrom Theorem 3/Corollary 2 applies
on this open interval and gives nondecreasing r. There is no
regularity assumption on a zero extension of f at its left endpoint.
Its right endpoint limit is f(infinity)=0. For every a>0,
q'(s)=Phi'(sqrt(s))/(2 sqrt(s)) and substitution t=sqrt(s) give

\[
 \int_a^\infty |f'(s)|\,ds
 =J^{-1}\int_{\sqrt a}^\infty |\Phi'(t)|\,dt<\infty.
\]

The last finiteness follows from source derivative decay. Thus the improper endpoint
integrals in the manuscript's Appendix 8.2 concave proof case
(Remark 4 and Lemma 4, p. 25) have their required limits here.

That proof's last concave-case line has the recorded sign/reference
typo: the preceding inequality implies f' S+f^2>=0, consistent
with Remark 4 and the stated corollary. The correctly stated named
theorem is imported; neither its proof nor the theta shape theorem
is reproved here. Csordas cites Csordas--Varga, *Constructive
Approximation* 4 (1988), 175-198, Theorem 2.1, for the latter;
the original 1988 proof has not been independently audited.

**Weighted-tail identity and zero endpoint.** Normalization cancels
from h/p, giving tau(u)=(integral_u^infinity v k(v) dv)/k(u).
For u>=0 put s=v^2/4, so v=2 sqrt(s) and v dv=2 ds. Consequently

\[
 \begin{split}
 \int_u^\infty v k(v)\,dv
 &=8\int_{u^2/4}^\infty \Phi(\sqrt{s})\,ds,\\
 k(u)&=4q(u^2/4),\\
 \tau(u)&=2\frac{\int_{u^2/4}^\infty q(s)\,ds}{q(u^2/4)}.
 \end{split}                                                \tag{3}
\]

The substitutions are justified by the finite positive tails already
checked, including at u=0 by taking the limit of the lower endpoint.
Since S/f=(integral q)/q, (3) proves (1) for u>0, with both Z and J
cancelled. At zero the separate normalizations give
h(0)=8J/Z and p(0)=4 Phi(0)/Z, so their ratio is again
2J/Phi(0); no identification of J with Z is made.
For 0<u<v, r(u^2/4)<=r(v^2/4); positivity of r reverses
this inequality on taking reciprocals. Hence tau(u)>=tau(v).

As u decreases to zero, q(u^2/4) tends to Phi(0)>0 and the numerator
integral in (3) tends to J. This proves continuity at zero and the
stated finite positive value tau(0), extending nonincrease to the
closed half-line. Smooth evenness gives tau'(0)=0; directly,
h'(0)=0 and p'(0)=0 give the same result by the quotient rule.
The zero endpoint is the argument u=0, not a zero value of tau.
No strict hazard or strict Stein monotonicity is needed or asserted.

**Later bounded audit, 31 October 2026.** Replayed all local identities
against the exact primary passages cited above, including the entire
concave hazard proof case. The factor 2, distinct normalizations,
centering, connected full-line support, smoothness through zero,
open-interval hazard hypotheses and both improper tails pass. The
explicit normalization and absolute-derivative integral above record
the audit's additional checks; no mathematical correction was needed.
This audits the specialization, not the original 1988 shape proof,
and establishes no Fourier-sign implication. The sole direct local
mathematical input remains L019; comparison countermodels and the
uncontrolled signed remainder are not premises.

## Mathlib

Full-result and supporting-result Mathlib coverage not checked.
No formal matching theorem or absence claim is made. This is a
specialization of the cited shape/hazard results with local coordinate,
normalization and endpoint checks, not a claimed new shape theorem.
