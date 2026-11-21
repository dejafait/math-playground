# Corollary 919p: all real-zero prefixes have positive inverses in an order-two countermodel

## Hypotheses

Use the angular Fourier convention T(f)(z)=integral_R f(u)exp(izu)du.
Fix the single function

    F(z)=exp(-z^2) (2+cos z) sin z/(3z),  F(0)=1.

For each integer n>=0 put

    P_n(z)=product_(k=1)^n (1-z^2/(k*pi)^2),  P_0(z)=1,
    F_n(z)=F(z)/P_n(z)

initially away from the zeros of P_n. Empty products and sums have their
usual values. No hypothesis about zeta, Xi, or a numerical backend is used.
Import the standard identities cited below. This is the fixed-model
specialization authorized by assessment2239, not a change of parameters.

## Conclusion

For every n>=0 all apparent poles of F_n are removable and F_n is the
entire transform of a smooth, even, strictly positive probability density
f_n on R. More explicitly, with convolution on R,

    g(u)=exp(-u^2/4)/(2 sqrt(pi)),
    mu=(2/3)delta_0+(1/6)delta_-1+(1/6)delta_1,
    c_n=4^n (n!)^2/(2(2n)!),
    h_n(u)=c_n cos(pi u/2)^(2n) for |u|<1, and 0 otherwise,
    f_n=g*mu*h_n.                                             (1)

In particular h_0 is the uniform probability density on (-1,1); no
endpoint value of 0^0 is used. For every integer m,p>=0 and real B>=0,

    integral_R (1+|u|)^p exp(B|u|)|f_n^(m)(u)|du < infinity,
    exp(B|u|)f_n^(m)(u) -> 0 as |u| -> infinity.                (2)

The exact transform and inverse are

    F_n(z)=exp(-z^2)(2+cos z)/3
           * (n!)^2/[Gamma(n+1+z/pi)Gamma(n+1-z/pi)],           (3)
    f_n(u)=(1/(2pi)) integral_R F_n(x)exp(-ixu)dx.              (4)

Reciprocal-gamma factors in (3) are evaluated by their entire extension.
The second moments obey the explicit uniform bound

    integral_R u^2 f_n(u)du
       =8/3-(2/pi^2)sum_(k=1)^n 1/k^2 <=8/3.                 (5)

The complete real-zero set of F is {+/-k*pi:k>=1}, all simple; hence
P_n removes exactly its first n positive real zeros and their negatives.
The complete real-zero set of F_n is {+/-k*pi:k>n}, again simple. The
fixed simple nonreal zero

    z_*=pi+i log(2+sqrt(3))                                   (6)

belongs to every F_n. Every F_n has order exactly two (indeed type one
at order two).

Thus, in a class allowing order two, even all these finite-prefix
positive-inverse, tail and uniform-moment properties do not force real
zeros. This is a source-covered REPRODUCTION specialization, accepted
in the separate conceptual audit2243 below on 21 November2026. It is not
a counterexample to an order-one assertion, an actual-Xi theorem or RH.

## Proof

### Standard inputs and overlap

NIST DLMF [5.12.5](https://dlmf.nist.gov/5.12.E5) gives

    integral_0^(pi/2) cos(t)^(a-1)cos(bt)dt
      =pi/[2^a a B((a+b+1)/2,(a-b+1)/2)], Re(a)>0.

Use the beta-gamma identity [5.12.1](https://dlmf.nist.gov/5.12.E1)
first with both beta arguments of positive real part. Gamma recurrence
and reflection are [5.5.1 and 5.5.3](https://dlmf.nist.gov/5.5);
reciprocal gamma is entire, with simple zeros at the nonpositive
integers, by [5.2(i)](https://dlmf.nist.gov/5.2.i). These identities
are imported, not reproved. DLMF attributes the cosine-power identity
to Nielsen, *Handbuch der Theorie der Gammafunktion* (1906), section64;
that original proof is not claimed independently inspected.

For real-frequency convolution, Gaussian transformation and Schwartz
inversion use T. Tao, *245C, Notes2: The Fourier transform* (6 April2009),
[Exercises14,16,41 and formula(11)](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/).
Exercise41 with d=1 and r=2sqrt(pi), followed by xi=-x/(2pi), gives
T(g)(x)=exp(-x^2) in the present convention. Its hypotheses r>0 hold.
The finite measures used below have mass one and g,h_n are integrable.
We verify entire extension and the stronger derivative tails separately.
Complex sine and cosine use the exponential definitions in
[DLMF4.14.1-4.14.2](https://dlmf.nist.gov/4.14).

The base factor exp(-z^2)(2+cos z) already occurs in H. Arellano-Peña,
*Moment and Prime-Trace Criteria for the Riemann Hypothesis, with Spectral
Exclusions and Nonlocal Positivity*, author preprint, 6 September2026,
amended30 September2026, section5.3, printed p10, (5.12)-(5.13),
[DOI10.13140/RG.2.2.22856.07682](https://www.researchgate.net/publication/414031680_Moment_and_Prime-Trace_Criteria_for_the_Riemann_Hypothesis_with_Spectral_Exclusions_and_Nonlocal_Positivity).
Source review2239 inspected that subsection; no other claims of that
preprint are imported. There is no originality claim for the base
factor, nor a claim that the bounded review establishes novelty of
the combined model. The proof below supplies the all-n assembly that
is not imported from this overlap.

### Normalized compact inverse and every removable point

Fix an arbitrary n>=0 and write w=z/pi. On the strip
|Re(w)|<n+1, the substitution a=2n+1, b=2w in DLMF5.12.5 satisfies
Re(a)>0 and Re(n+1+w),Re(n+1-w)>0. Evenness and t=pi*u/2 give

    J_n(z):=integral_-1^1 cos(pi*u/2)^(2n)exp(izu)du
      =(4/pi) integral_0^(pi/2) cos(t)^(2n)cos(2wt)dt
      =2(2n)!/[4^n Gamma(n+1+w)Gamma(n+1-w)].                (7)

Here the beta arguments sum to 2n+2, and
Gamma(2n+2)/(2n+1)=(2n)!; this accounts for the normalization.
At z=0, (7) yields J_n(0)=2(2n)!/[4^n(n!)^2]=1/c_n.
Thus h_n>=0 has integral one and is even, with support in [-1,1].
Its transform is

    H_n(z):=T(h_n)(z)
      =(n!)^2/[Gamma(n+1+w)Gamma(n+1-w)].                   (8)

The integral defining J_n is entire: on |z|<=R its jth differentiated
integrand is bounded by |u|^j exp(R) on [-1,1], an integrable bound
for every j. The right side of (7), interpreted as a product of
reciprocal gamma functions, is entire too. Equality on the displayed
strip therefore proves (7)-(8) on C by the identity theorem. This
does not evaluate a beta integral outside its convergence domain.

For noninteger w away from poles, the cited recurrence and reflection
give

    Gamma(n+1+w)Gamma(n+1-w)
      =Gamma(1+w)Gamma(1-w) product_(k=1)^n(k^2-w^2),
    1/[Gamma(1+w)Gamma(1-w)]=sin(pi*w)/(pi*w).

Since product_(k=1)^n(k^2-w^2)=(n!)^2 P_n(z), this proves

    P_n(z) H_n(z)=sin z/z.                                 (9)

Both sides in (9) are entire, with the sinc value one at zero, so
the identity theorem extends this equality to every z. Consequently
H_n is the removable extension of sin(z)/(z P_n(z)), including n=0.
For every integer 0<=k<=n, (8) gives the explicit nonzero values

    H_n(+/-k*pi)=(n!)^2/[(n+k)!(n-k)!].                    (10)

This handles every removed pair, rather than leaving its extension
implicit. In particular H_n(0)=1.

### Strict positive inverses, complete tails and inversion

Let nu_n=mu*(h_n(u)du). This is an even probability measure supported
in [-2,2]. Define

    f_n(u)=integral_[-2,2] g(u-v)dnu_n(v).                 (11)

For fixed u, the continuous function g(u-v) has a strictly positive
minimum on [-2,2]; hence f_n(u)>0. Tonelli's theorem for the nonnegative
integrand and translation invariance give integral_R f_n=1.
Evenness follows from evenness of g and nu_n.

For every m>=0, differentiation of the explicit Gaussian gives

    g^(m)(s)=q_m(s)g(s),
    q_0=1, q_(m+1)=q_m'-(s/2)q_m,

where q_m is a polynomial of degree m. Choose a finite A_m such that
|q_m(s)|<=A_m(1+|s|)^m for all real s; the sum of the absolute
coefficients suffices. Derivatives of g(u-v) are bounded on any
compact u interval times [-2,2]. Differentiation under the finite
measure integral is therefore justified successively by dominated
convergence, and

    f_n^(m)(u)=integral g^(m)(u-v)dnu_n(v),
    |f_n^(m)(u)| <= A_m/(2sqrt(pi)) (3+|u|)^m
                    *exp(-((|u|-2)_+)^2/4),              (12)

where r_+=max(r,0). Indeed |u-v|<=|u|+2 and
|u-v|>=(|u|-2)_+ on the support. The bound is independent of n
because nu_n has mass one; no derivative of h_n, nor any uniform
bound on c_n, is assumed. For |u|>=2 the exponent after multiplication
by exp(B|u|) is -|u|^2/4+(B+1)|u|-1. Its negative quadratic term
dominates every polynomial. This proves both assertions (2), for
every m,p,B, and proves f_n is Schwartz.

The finite-measure convolution identity and the cited Gaussian
transform now give, for real x,

    T(f_n)(x)=exp(-x^2)[(2/3)+(exp(ix)+exp(-ix))/6]H_n(x)
             =exp(-x^2)(2+cos x)H_n(x)/3.                 (13)

For each R and j, |u|^j exp(R|u|)f_n(u) is integrable by (12).
Thus the left side has an entire extension with all z derivatives
obtained under the integral, locally uniformly. The right side is
entire by (8). Equality on R implies equality on C. Combining (9)
and (13) gives P_n T(f_n)=F and proves (3) and the claimed removable
extension of F_n. At a removed root its value is explicitly

    F_n(+/-k*pi)=exp(-(k*pi)^2)(2+(-1)^k)/3
                * (n!)^2/[(n+k)!(n-k)!] >0, 1<=k<=n.    (14)

For real x the probability transform bound gives |H_n(x)|<=1;
also |(2+cos x)/3|<=1. Therefore |F_n(x)|<=exp(-x^2), so its
inverse integral is absolutely convergent. Schwartz inversion (11)
of Tao, with xi=-x/(2pi), yields exactly (4), including its factor
1/(2pi) and its negative exponential sign. This completes both
the positive-transform representation and the inverse assertion.

### A uniform second moment

Every measure used above is even and has finite second moment.
The Gaussian transform differentiated twice at zero gives
integral u^2 g(u)du=2; dominated differentiation is justified by its
Gaussian tail. The atomic measure mu has second moment 1/3.

For each fixed n, the finite product and the Taylor expansion of sinc
at zero give

    P_n(z)=1-S_n z^2+O_n(z^4),
    sin z/z=1-z^2/6+O(z^4),
    H_n(z)=1+(S_n-1/6)z^2+O_n(z^4),
    S_n=sum_(k=1)^n 1/(k*pi)^2.                            (15)

Since h_n is compactly supported, differentiation of its transform
twice is justified directly; hence

    integral u^2 h_n(u)du=-H_n''(0)=1/3-2S_n.              (16)

This is nonnegative because it is the second moment of the positive
density already constructed. No value of an infinite sum is needed.
Applying Fubini to the convolution moment, or expanding
(s+a+t)^2 against g(s)ds, mu(da), h_n(t)dt, yields the sum of the
three second moments: mixed terms vanish by evenness and absolute
integrability. Equations (16) and the two preceding values give (5).
The bound8/3 holds for all n because S_n>=0, with equality at n=0.
This is an exact bound, not a numerical or finite-prefix sample, and
no interchange of n->infinity with a derivative or integral occurs.

### Complete real-zero inventory and a retained nonreal zero

On R the factors exp(-x^2) and 2+cos x are nonzero. The exponential
definition of sine shows sin x=0 exactly at integer multiples of pi;
its derivative there is (-1)^k. The sinc factor equals one at zero
and has a simple zero at every nonzero k*pi, since its derivative
there is (-1)^k/(k*pi). This proves the exhaustive real-zero and
multiplicity assertions for F. Each root of P_n is simple. Formula
(14) excludes any residual zero at a removed point, and away from
those points division by a nonzero polynomial changes neither zeros
nor their multiplicities. The real-zero assertions for F_n follow.

Put a=log(2+sqrt(3))>0. As exp(-a)=2-sqrt(3),
cosh a=2 and sinh a=sqrt(3). Thus

    cos(pi+ia)=-2,  sin(pi+ia)=-i sqrt(3).

At z_* the factor 2+cos z has derivative -sin z_*=i sqrt(3),
while exp(-z_*^2), sin(z_*)/z_* and every P_n(z_*) are nonzero.
Therefore z_* is a simple zero of F and every F_n. It was never
among the real factors removed.

### Exact growth and the limitation of the obstruction

Let M_n(r)=max_(|z|=r)|F_n(z)|. The probability supports give
|H_n(z)|<=exp(|Im z|) and |T(mu)(z)|<=exp(|Im z|). From (13),

    M_n(r)<=exp(r^2+2r).                                   (17)

For real r>0 the exact quotient has the positive value

    F_n(ir)=exp(r^2)(2+cosh r)sinh r
             /[3r product_(k=1)^n(1+r^2/(k*pi)^2)].         (18)

For each fixed n, the finite product equals
r^(2n)/[pi^(2n)(n!)^2] times (1+O_n(r^(-2))) as r tends to
infinity. The exponential definitions give
(2+cosh r)sinh r=(exp(2r)/4)(1+O(exp(-r))). Consequently

    log F_n(ir)=r^2+2r-(2n+1)log r
                 +log(pi^(2n)(n!)^2/12)+o_n(1).           (19)

This includes n=0. Since M_n(r)>=F_n(ir), (17)-(19) imply
lim_(r->infinity) log M_n(r)/r^2=1. In particular the usual order
limsup log log M_n(r)/log r is exactly two and its order-two type
is one. This statement is for each finite n; the lower asymptotic
does not assert uniformity as n grows with r.

For comparison, G. Csordas, *Fourier transforms of positive definite
kernels and the Riemann xi-function*, arXiv:1309.0055v2 (21 February2014),
[printed p10, (4.1) and the following order statement](https://arxiv.org/pdf/1309.0055v2),
states that the Xi transform has order one. His H(x)=xi(x/2)/8
differs from the spectral Xi convention by fixed nonzero amplitude
and frequency scalings; such scalings replace M(r) by a constant
times M(c*r), c>0, and preserve order. The order-two model therefore
does not test an implication restricted to order one. Csordas's
Theorem3.7, printed p8, concerns positive definiteness of every
weighted correlation kernel under its stated admissibility and
strict-log-concavity assumptions. No identification of that family
with the densities f_n is asserted.

The finite actual-Xi results C919m/C919o, and L018/L019/L058, are
scope comparisons only, not premises of this explicit model. Their
root-existence, further-removal and signed-positivity gaps remain.
L262's finite Laguerre-level example does not supply the every-prefix
quantifier proved here. Nor is this a limit of changing finite-block
countermodels or a deletion of the detecting nonreal pair. No
arithmetic, modular, mixed-positivity or theta tail identity for F
has been established. These distinctions delimit the generic
obstruction and prevent it from being read as an RH disproof.

### Critical audit2243: accepted within the stated scope

The independent audit used the complete written proof, the unchanged
SPECIALIZE assessment2241 and source notes2239. It found no mathematical
correction necessary. This accepts the previously pending obstruction;
it does not extend its statement or establish a new result beyond the
source-covered specialization. The following are the load-bearing checks.

1. In (7), evenness and u=2t/pi give4/pi, while a=2n+1 gives
   2^a=2*4^n. The beta arguments are n+1+w and n+1-w, and their
   positive-real-part conditions hold exactly on the strip used.
   Combining Gamma(2n+2)/(2n+1)=(2n)! gives the stated J_n and c_n,
   including c_0=1/2. Both sides are entire before extension outside
   that strip. The recurrence multiplies by (n!)^2 P_n, not by P_n
   alone; this cancels the numerator in (8) to give (9). For every
   0<=k<=n the arguments n+1+/-k are positive integers, so (10) and
   (14) verify all removed values without an unresolved gamma pole.

2. The probability measure nu_n has support[-2,2] for every n, even
   though h_n need not be smooth at its endpoints. All differentiations
   fall on g in (11). Its polynomial recurrence and compact-interval
   domination justify every derivative, and (12) uses only mass1.
   To check the precise tail strength, write r=|u|. For
   r>=8(B+1), the weighted exponent is

       -r^2/4+(B+1)r-1 <= -r^2/8-1.

   Thus (12), including its polynomial factor, gives both the weighted
   integrability and the pointwise limit in (2) for every m,p,B.
   The same bound supplies locally uniform complex-transform derivative
   domination. No derivative estimate for h_n or limit in n is used.

3. A narrow primary-source replay of Tao Exercise41 and inversion(11)
   checked the scale and Fourier signs. In dimension1 the source pair
   is r^(-1)exp(-pi*u^2/r^2) and exp(-pi*r^2*xi^2), for r>0.
   Setting r=2sqrt(pi) gives precisely g.
   Substitution xi=-x/(2pi) gives exp(-x^2); the inverse exponential
   becomes exp(-ixu), and reversing integration limits leaves the
   positive factor1/(2pi). Hence the convention in (3)-(4) is correct.
   Schwartz inversion applies to the already proved Schwartz f_n;
   the separate real-axis bound exp(-x^2) also proves absolute
   convergence of its inverse integral.

4. For a fixed finite n, 1/P_n=1+S_n z^2+O_n(z^4). Multiplying by
   sinc gives H_n''(0)=2S_n-1/3. Compact support permits the two
   transform derivatives. The convolution moment is consequently
   2+1/3+(1/3-2S_n)=8/3-2S_n; absolute integrability of all cross
   terms follows from finite second moments. This proves the claimed
   uniform upper bound, with equality at n=0, without a Basel-sum
   evaluation or an interchange of a derivative and an infinite product.

5. On the real axis 2+cos x>=1. The sinc zeros are therefore the
   entire real-zero inventory of F, and their derivatives are nonzero.
   Division preserves each remaining multiplicity and (14) excludes
   new or surviving zeros at a removed point. At z_* both sin z_*
   and z_* are nonzero, -sin z_*=i sqrt(3), and the polynomial P_n
   has only real roots. Thus its zero remains simple in every F_n.

6. The two compact probability factors each contribute at most
   exp(|Im z|), and |exp(-z^2)|<=exp(|z|^2), proving (17).
   On the imaginary axis all factors in (18) are positive. For fixed
   n its denominator has leading term
   3r^(2n+1)/(pi^(2n)(n!)^2), whereas the numerator has leading
   term exp(r^2+2r)/4. This gives (19), with its factor12 and
   n=0 case, and squeezes log M_n(r)/r^2 to1. The resulting order
   is exactly2 and the type exactly1. The proof makes no claim that
   the lower asymptotic is uniform when n grows with r.

7. All prefixes belong to one fixed F and remove only its first n
   real pairs. The nonreal pair is retained; positivity of these
   direct inverses is not positivity of Csordas's correlation family.
   The exact growth mismatch excludes any order-one or actual-Xi
   inference. No local lemma is a hidden premise: the named local
   results are comparisons, so the empty C919p DAG row is correct.

The generic sufficiency route is therefore stopped only in the
growth class stated above. Order-one sufficiency, actual-root existence,
arbitrary actual-Xi removal and the all-degree mixed signs stay open.
No numerical replay or mathematical script is needed for these exact
analytic checks, and none was used.

## Mathlib

Full matching coverage and supporting theorem names have not been
checked. No absence claim or Lean verification is made. The cited
classical identities and the complete analytic specialization above
are the informal proof inputs; no numerical certificate is used.
