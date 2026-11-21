# Corollary C032o: the odd kernel fails direct compact-transform growth

## Hypotheses

Retain C032j/k/m's actual positive-ordinate divisor, multiplicities,
Gaussian convention, normalized entire lifts and fixed-v1 source
qualifications. In particular write z_rho=gamma_rho-i*delta_rho,
gamma_rho>14, |delta_rho|<1/2, N(T)=O(T log(T+2)), and

    H(t)=sum_rho exp(-t*z_rho^2)>0,                 t>0.

The strict heat positivity and the probability exponent below are
qualified preprint imports, not independent source-wide verifications.
Fix the admitted width sigma=1. Suppress this subscript and use

    p(z)=(1/2)*sum_rho [G(z-z_rho)+G(z+z_rho)],
    G(z)=(4*pi)^(-1/2)*exp(-z^2/4),
    O(w)=2*pi*integral_0^w p(i*t) dt,
    b(w)=E(w)+O(w),
    K(w)=exp(-E(w))*sinh(O(w)).

C032k supplies b(w)=B(w^2) for real w>0, with B the finite
nonnegative Bernstein exponent in C032j:

    B(s)=integral_0^infinity (1-exp(-s*t))*ell(t) dt,
    ell(t)=H_1(t)/t>=0.

No p>=0, RH, endpoint density, positive width mixture, or
signed-mixture uniqueness hypothesis is imposed.

## Conclusion

For every C>0 and integer N>=0 there is a real w>=0 such that

    |K(w)|>C*(1+w)^N.                              (1)

Consequently no finite C>0, A>=0 and integer N>=0 can satisfy

    |K_sigma(w)|<=C*(1+|w|)^N*exp(A*|Im(w)|)

simultaneously on C and 1<=sigma<=2: its restriction to sigma=1
and w>=0 already fails. In particular K_1 is not the direct
Fourier-Laplace transform in w of a compactly supported distribution
on R. This rules out the proposed uniformly bounded common compact
distribution interface. It says nothing about other coordinates,
noncompact transforms, or cancellation after signed width integration.
It proves no actual-Xi sign and does not resolve RH.

## Proof

### Source scope and the local difference

All divisor, lift and Bernstein inputs are those cited precisely in
C032j/k/m: Suvrit Sra, *Some positivity properties of Riemann Xi under
smoothing*, fixed [2611.00345v1, 11 November 2026](https://hexagonmath.org/pdf/2611.00345v1),
Section3.1, Proposition3.1, LemmaA.4, PropositionA.7 and the proof of
PropositionA.8; and *On some positivity properties of the Riemann Xi
function*, fixed [2610.00584v1, 20 October 2026](https://hexagonmath.org/pdf/2610.00584v1),
Theorem1.1 and Section2.1/Lemma2.1. The earlier local applicability
checks and qualifications are retained, without reproof of these inputs.

The transform implication is Lars Hormander, *Supports and singular
supports of convolutions*, Acta Math.110 (1963), Theorem2.1/(2.4),
printed pp281-282, [primary scan](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5966-11511_2006_Article_BF02391861.pdf).
For support in [-A,A] its necessary bound is exactly polynomial
growth times exp(A*|Im(w)|), with transform convention exp(-i*x*w).
The statement and printed proof were inspected in source-notes1535.
Only this necessary direction is used; it is not reproved here.

Holomorphic integration uses Friedrich Haslinger, *Complex Analysis*,
Section2.7, [Theorem2.39 and proof, pp67-68](https://www.mat.univie.ac.at/~has/scriptneu.pdf),
with the compact dominators checked below. Coverage1528/1532 is reused.
The elementary complex-parameter Gaussian integral is the standard
Gaussian integral, extended in its linear parameter by holomorphy.
The local work is the exact full-divisor transform and a positive
correction argument at its boundary. No matching nonlinear growth
theorem was found in assessment1535; no originality claim is made.

### 1. Full-divisor Gaussian domination and exact transform

Put a0=1/4 and S=sum_rho exp(-gamma_rho^2/4)<infinity.
Finiteness follows from the stated counting bound, with multiplicity.
For real v, both Gaussian translates satisfy

    |G(i*v +/- z_rho)|
       <=(4*pi)^(-1/2)*exp(-gamma_rho^2/4)
                         *exp(v^2/4+|v|/4+1/16).

Thus, for M=(4*pi)^(-1/2)*exp(1/16)*S,

    |p(i*v)|<=M*exp(v^2/4+|v|/4),
    |O(v)|<=2*pi*M*v*exp(v^2/4+v/4),              v>=0.       (2)

For every real a>a0, multiplying the first bound by exp(-a*v^2)
gives an integrable majorant on R for the sum of absolute values of
all summands. Multiplication by any fixed polynomial remains
integrable. This justifies exchanging the entire infinite divisor
sum with Gaussian integration; no finite truncation is substituted.

For d=a-a0>0, the exact algebraic expression is

    p(i*v)=(4*pi)^(-1/2)*exp(v^2/4)
              *sum_rho exp(-z_rho^2/4)*cos(z_rho*v/2).

The standard Gaussian integral gives, for every complex z,

    integral_R exp(-d*v^2)*cos(z*v/2) dv
       =sqrt(pi/d)*exp(-z^2/(16*d)).

Its extension from real z is legitimate: on each compact set of z,
the integrand is bounded by exp(-d*v^2+c*|v|), an integrable
dominator. Both sides are entire in z and agree on R, so the identity
theorem applies. This verifies the needed complex-shift specialization.
Evenness and the justified sum exchange therefore give

    integral_0^infinity exp(-a*v^2)*p(i*v) dv
      =H(a/(4*a-1))/(2*sqrt(4*a-1)).              (3)

Here 1/4+1/(16*d)=a/(4*a-1), so the argument of H is positive.
Evenness and real Taylor coefficients of p make p(i*v) real on R;
O is real there as well. No pointwise sign of p(i*v) was used.

Define q(x)=O(sqrt(x)) for x>=0 and

    L(a)=integral_0^infinity exp(-a*x)*q(x) dx,    a>a0.

Equation(2) makes this integral absolutely convergent, also after
multiplication by any fixed power of x, on every smaller half-plane
Re(a)>a'>a0. Thus it defines a holomorphic function on Re(a)>a0
with all its differentiated integrals justified. The substitution
x=v^2 and integration by parts, using O'=2*pi*p(i*v), give

    L(a)=2*integral_0^infinity v*exp(-a*v^2)*O(v) dv
        =(2*pi/a)*integral_0^infinity exp(-a*v^2)*p(i*v) dv
        =pi*H(a/(4*a-1))/(a*sqrt(4*a-1))>0.       (4)

At zero the boundary term vanishes because O(0)=0. At infinity it
vanishes by (2), since a>a0. Both integrals in the integration by
parts are absolutely convergent. The strict inequality in (4) is
exactly the retained H>0 input, not a numerical sign estimate.

### 2. Every right derivative is flat at a0

Write alpha_rho=Re(z_rho^2)=gamma_rho^2-delta_rho^2>195.
For each integer k>=0 the counting bound implies

    D_k=sum_rho |z_rho|^(2*k)*exp(-alpha_rho)<infinity.

Normal convergence on compact subsets of Re(t)>0 justifies
termwise differentiation of H there. Indeed for t=u+i*y in such a
compact set the absolute summands, including any fixed derivative,
are bounded by a polynomial in gamma times
exp(-epsilon*gamma^2+c*gamma+c'), which is summable by counting.
For real t>=1 this yields

    |H^(k)(t)|<=D_k*exp(-195*(t-1)).              (5)

As d=a-a0 decreases to zero,
t=a/(4*a-1)=1/4+1/(16*d). Differentiating (4) any fixed n times
produces finitely many terms: derivatives of 1/(a*sqrt(4*a-1)),
derivatives of t, and H^(k)(t) with k<=n. The rational and
square-root factors have at most power growth in d^(-1).
By (5), for some finite C_n and M_n and sufficiently small d>0,

    |L^(n)(a0+d)|
      <=C_n*d^(-M_n)*exp(-195/(16*d)) -> 0.       (6)

This holds for every n, including n=0. The constants need not be
uniform in n; the following argument uses each finite moment first.

### 3. A polynomial bound for K forces a nonnegative correction

Suppose, to obtain a contradiction, that |K(w)|<=C*(1+w)^N for all
real w>=0, with C>0 and integer N>=0. The Bernstein integral gives

    0<=B(s)<=B(1)*max(1,s),                      s>=0.       (7)

For s<=1 use monotonicity of 1-exp(-s*t); for s>=1 use
1-exp(-s*t)<=s*(1-exp(-t)), which follows because
(1-exp(-u))/u is decreasing for u>0. Integrating is legitimate
against ell(t)>=0 and B(1)<infinity. This is a bound for the already
imported exponent, not an assumption on an unknown signed law.

For real w>=0 the exact reflected-exponential identity is

    2*K(w)=exp(-b(w))*(exp(2*O(w))-1),
    exp(2*O(w))=1+2*K(w)*exp(B(w^2)).             (8)

The last quantity is strictly positive. Equations(7)-(8) imply

    2*O(w)<=B(w^2)+log(1+2*C*(1+w)^N).

Since log(1+2*C*(1+w)^N)<=log(1+2*C)+N*log(1+w), there is a
finite D>0 such that O(w)<=D*(1+w^2) for all w>=0. Thus

    h(x)=D*(1+x)-q(x)>=0,                       x>=0.       (9)

It is continuous. For a>a0 it and all its polynomially weighted
Laplace integrals converge absolutely by (2).

### 4. Positive moments contradict the exact flat transform

By (4) and (9),

    integral_0^infinity exp(-a*x)*h(x) dx
       =D*(1/a+1/a^2)-L(a),                     a>a0.

Differentiation n times is justified using the absolute domination
already established. Consequently

    integral_0^infinity x^n*exp(-a*x)*h(x) dx
      =D*(n!/a^(n+1)+(n+1)!/a^(n+2))-(-1)^n*L^(n)(a).

Let a decrease to a0. Monotone convergence applies to the
nonnegative integrands on the left, separately for each n. Equation(6)
therefore gives the finite, exact boundary moments

    integral_0^infinity x^n*exp(-a0*x)*h(x) dx
       =D*(n!/a0^(n+1)+(n+1)!/a0^(n+2)).          (10)

For 0<epsilon<a0, expand exp(epsilon*x) in its nonnegative
power series. Tonelli/monotone convergence and (10), with no
exchange of signed divergent moments, give

    integral_0^infinity exp(-(a0-epsilon)*x)*h(x) dx
       =D*(1/(a0-epsilon)+1/(a0-epsilon)^2)<infinity.       (11)

Choose epsilon=1/8, so a1=a0-epsilon=1/8. From
|q(x)|<=D*(1+x)+h(x) and (11),

    integral_0^infinity exp(-a1*x)*|q(x)| dx<infinity.

The integral defining L now extends holomorphically to Re(a)>a1.
Explicitly, on any compact subset choose b>a1 below its least real
part. The integrand is dominated by exp(-a1*x)*|q(x)|;
each n-th derivative is dominated by that same integrable function
times sup_(x>=0) x^n*exp(-(b-a1)*x)<infinity. These check the
holomorphic-integration theorem and all derivative interfaces.

In particular a0 is an interior point of this extension. Its
derivatives at a0 equal the right limits in (6), hence are all zero.
The Taylor series and identity theorem force L to vanish on the
connected half-plane Re(a)>a1. This contradicts L(a)>0 in (4).
The assumed polynomial bound is impossible, proving (1).

Any proposed global bound in the conclusion restricts on sigma=1,
w>=0 to the impossible polynomial bound. Hormander's necessary
compact-distribution estimate then gives the transform consequence.
Both nonlinear reflected exponentials and the complete actual divisor
were retained. Neither an oversized upper envelope nor growth of E
or O alone was substituted for growth of K.

This is the bounded growth decision only. J_eta identically zero
for a mass-one signed measure remains undecided, as do transformed
input identification, other transform coordinates, positive mixtures
and unsmoothed actual-Xi realization. The conceptual audit below
validates this qualified obstruction; it is not a complete-RH candidate.

### Conceptual audit1538, 18 November 2026

Equations (2)-(11) pass independent analytic replay under the stated
inputs. This is verification of the local obstruction, not a new
growth theorem or a source-wide verification of the fixed-v1 preprints.
The inspected source coverage in assessment1536, approved1537, is
reused. No additional theorem, RH assumption or numerical divisor
truncation is required.

For (2)-(4), the imaginary part of i*v +/- z_rho is v -/+ delta_rho.
Thus its squared contribution is bounded by v^2+|v|+1/4. Summing the
absolute values retains exactly S, including every multiplicity and
the factor 1/2 for the two translates. After multiplication by
exp(-a*v^2), the majorant is a constant times
exp(-(a-1/4)*v^2+|v|/4), also integrable with every fixed polynomial
factor. The full-line Gaussian factor is 1/(2*sqrt(d)); the half-line
factor is 1/(4*sqrt(d))=1/(2*sqrt(4*a-1)), so (3) and the integration
by parts factor 2*pi/a in (4) are correct. Reality uses conjugation
invariance of the positive-ordinate divisor, with multiplicities;
it does not require each z_rho to be real. Both endpoint terms and
both absolute integrals in the integration by parts are controlled
by (2).

For (5)-(6), on a complex t-compact set with Re(t)>=epsilon>0,
Re(t)<=V and |Im(t)|<=M, each differentiated heat summand is bounded
by |z_rho|^(2*k)*exp(-epsilon*gamma_rho^2+V/4+M*gamma_rho).
Counting makes this summable. On the real ray t>=1, splitting
exp(-t*alpha_rho) as exp(-alpha_rho)*exp(-(t-1)*alpha_rho)
gives exactly (5). For d>0, t^(j)(a)=(-1)^j*j!/(16*d^(j+1))
for j>=1. In the n-th derivative of (4), a term containing H^(k)
has at worst d^(-n-k-1/2), with k<=n. Thus M_n=2*n+1/2 is a
valid choice in (6), after enlarging C_n on a sufficiently small
right neighborhood. The exponential factor absorbs every such
fixed power. This checks all orders separately, without claiming
an n-uniform bound or analyticity at the boundary at this stage.

For (7)-(9), B>=0 and the reflected identity imply

    exp(2*O(w)) <= exp(B(w^2))*(1+2*C*(1+w)^N).

The left side is positive and real. Taking its real logarithm and
using log(1+w)<=w<=1+w^2 proves the proposed bound with, for example,

    D=1+(B(1)+log(1+2*C)+N)/2>0.

Only an upper bound for q follows; no lower bound or sign for q is
being silently used. It is h=D*(1+x)-q, and only h, that is
nonnegative in both applications of monotone convergence.

The differentiated transform in (10) has the correct sign (-1)^n.
Its n=0 case is included. Dividing the two boundary moment terms by
n! gives the series with coefficients a0^(-n-1) and
(n+1)*a0^(-n-2). Both converge for epsilon<a0 and sum exactly to
(11). In particular at a1=1/8 the h integral equals 72*D, while
the D*(1+x) integral also equals 72*D. Consequently

    integral_0^infinity exp(-x/8)*|q(x)| dx <= 144*D.

This is a full absolute integral bound, not a formal moment expansion.
It supplies a positive Lebesgue-measure dominator for Haslinger2.39
on each compact subset of Re(a)>1/8, with every fixed derivative
paid by the additional exponential margin there. Hence a0 is truly
interior to the extension, its derivatives are the right limits
already computed, and the Taylor/identity argument is valid. The
contradiction uses H>0 solely as the qualified input in (4).

The necessary compact-distribution bound then applies with exactly
the stated Fourier convention. No continuum signed-width conclusion
follows from the single-width failure. C032n is not an input, and
no probability-kernel measurability or mixture positivity is needed.

## Mathlib

Full matching coverage is unchecked and unknown. No Mathlib theorem
is used. Supporting Gaussian integration, holomorphic integration,
Laplace, monotone-convergence and Taylor/identity results may exist;
no full matching theorem or absence claim is asserted. This is a
qualified local consequence of the cited inputs and the displayed
argument, not a claim of progress beyond all existing literature.
