# L207 — Energy-weighted coefficient replacement in a polynomial prefix transition

## Hypotheses

Use L205–L206's polynomial and exact covariance-side prefix, with
epsilon=N^(-7/4), a=8/N, m=ceil(6 epsilon^(-1/2) log N), d=m-1,
and p=p_(m-1,epsilon). Keep the full joint-group setting and both
actual L010 probes of those inputs. This lemma estimates only the
short interior transition of one prefix. It changes no plateau,
projection, residual, boundary value or heat sum.

On the infinite transverse vertex grid let

    T=Delta_(T,infinity)+epsilon I,
    K_r(T)=(1/(2 pi)) integral_(-pi)^pi
                  exp(i r theta) p(T+(2-2cos theta)I) d theta.

Thus K_r is the transverse operator whose kernel is L206's k(r,z).
Define E_t(T) by L206(2), equivalently

    E_t(T)=-sum_(r=t)^d K_r(T)  (1<=t<=d),
    E_t(T)=-E_(1-t)(T),
    E_t(T)=0 outside 1-d<=t<=d.                       (1)

Let C_N(x) be a twice continuously differentiable map, in operator
norm, from an interval containing all x_j+a(t-1/2), 1-d<=t<=d,
to bounded operators on the transverse l2 space. Its derivatives
have bounds c_1= sup ||C_N'|| and c_2= sup ||C_N''||. Constants
in the estimates below are independent of N, j and C_N.
C_N need not commute with T. Smooth sampled multiplication
operators are included when their axial derivatives obey these
bounds; a rough Green or projection kernel is not thereby included.

## Conclusion

Put eta=2 rho_epsilon^m, with rho_epsilon as in L205. Then

    ||T^2 p'(T)+I|| <= eta(1+17m^2/8),               (2)
    sum_t (t-1/2)^2 ||E_t(T) T^2||
                         <= C[epsilon^(-1/2)+eta d^4]. (3)

In particular the same signed transition satisfies

    sum_t C_N(x_j+a(t-1/2)) E_t(T) T^2
                       =-a C_N'(x_j)+R_N,
    ||R_N|| <= a c_1 eta(1+17m^2/8)
                +C a^2 c_2[epsilon^(-1/2)+eta d^4]. (4)

For L205's actual degree schedule a sharper residual bound is
eta<=2N^(-11/4). Thus, for uniformly bounded c_1,c_2,

    ||R_N|| <= C[c_1 N^(-2)(log N)^2
                 +c_2{N^(-9/8)+N^(-5/4)(log N)^4}]
             =o(a).                                 (5)

This controls the growing-degree p' insertion and the weighted
absolute second transition moment, with a right T^2 energy weight.
It is not an unweighted trace error. Applying it to L206's actual
four covariance blocks still requires control of the other factors
after that right weight is supplied in their original order. No
factor T^(-2), prefix, coefficient or finite projection may be
commuted or discarded to infer such control. Both plateau/transition
cross terms, upper jumps and finite Green terms remain. There is
still no cubic limit or coefficient for either actual joint group.

This is a local application of standard spectral and Taylor methods,
not progress beyond the checked sources. Independent f_(i,2),r_0,
full compensation, finer asymptotics, matching, interacting reflected
error <=c_box/2, continuum axioms and infrared mass remain unresolved.

## Proof

### 1. Differentiate the actual finite polynomial

Write r(t)=T_m((8+epsilon-t)/8)/T_m(1+epsilon/8), using T_m
here only for the Chebyshev polynomial, distinguished from operator T.
L205 gives |r(t)|<=eta on [epsilon,16+epsilon]. The recurrence
identity T_m(cos theta)=cos(m theta) gives

    |T_m'(cos theta)|
          =m |sin(m theta)/sin theta|<=m^2.

For 0<theta<pi, the last inequality follows by writing the ratio
as a sum of m complex numbers of modulus one using the geometric
series for exp(2 i theta). Continuity gives the endpoint bound.
L205's denominator is at least rho_epsilon^(-m)/2. The chain rule
therefore gives |r'(t)|<=eta m^2/8 on the same interval.

Since p(t)=(1-r(t))/t, direct differentiation yields

    t^2 p'(t)+1=r(t)-t r'(t).

The transverse spectrum of T lies in [epsilon,12+epsilon], a subset
of [epsilon,17]. The spectral theorem proves (2). No derivative
convergence is inferred merely from a uniform approximation of p.

### 2. Compare complete axial Fourier coefficients before the moment sum

For a transverse spectral value mu in [epsilon,12+epsilon], define
the infinite one-dimensional resolvent coefficient

    g_r(mu)=q(mu)^|r|/sqrt(mu(mu+4)),
    q(mu)=(mu+2-sqrt(mu(mu+4)))/2=exp(-kappa(mu)),
    kappa(mu)=2 asinh(sqrt(mu)/2).                    (6)

Indeed 0<q<1 and q+q^(-1)=mu+2. Substitution gives
(mu+2)g_r-g_(r-1)-g_(r+1)=0 for r!=0, and its value at
r=0 is (q^(-1)-q)/sqrt(mu(mu+4))=1. The sequence is absolutely
summable. Taking its Fourier series proves that it is exactly the
kernel of (mu+2-2cos theta)^(-1), including its normalization.

L205's relative polynomial residual consequently gives, for every r,

    |K_r(mu)-g_r(mu)|
      <= eta/(2 pi) integral_(-pi)^pi
                          (mu+2-2cos theta)^(-1) d theta
       = eta g_0(mu).                                (7)

This uses the full axial spectrum. Multiplication by mu^2 and
mu<=13 show that mu^2 times the right side is at most C eta.
For |r|>d the polynomial coefficient K_r is exactly zero.

We need a summed operator bound rather than an interchange of
supremum and summation. For 0<mu<=13, the elementary inequality
asinh u>=u/sqrt(1+u^2), obtained by integrating its decreasing
derivative, gives

    kappa(mu)>=c sqrt(mu), c=2/sqrt(17),
    mu^2 g_r(mu)<= (mu^(3/2)/2) exp(-c |r| sqrt(mu)).

For r>=1, set v=r sqrt(mu). Boundedness of v^3 exp(-cv/2)
implies

    sup_(epsilon<=mu<=13) mu^2 g_r(mu)
       <=C r^(-3) exp(-c r sqrt(epsilon)/2).          (8)

Apply the spectral theorem separately to each K_r(T)T^2, then
sum (7)–(8). The geometric series is bounded by
2/[c sqrt(epsilon)], since exp(u)-1>=u. Thus

    sum_(r=1)^d r^3 ||K_r(T)T^2||
       <=C epsilon^(-1/2)+C eta sum_(r=1)^d r^3
       <=C[epsilon^(-1/2)+eta d^4].                  (9)

In particular no polynomial kernel positivity is assumed. Positivity
is used only for the explicit scalar resolvent in (6)–(8).

### 3. The signed transition and the operator Taylor remainder

L206's finite sums give sum_t E_t(T)=0 and
sum_t(t-1/2)E_t(T)=p'(T), with the same link midpoint.
They are identities of transverse operators. From (1), the triangle
inequality, reflection t -> 1-t, and

    sum_(t=1)^r(t-1/2)^2=r(4r^2-1)/12<=r^3/3,

we obtain

    sum_t(t-1/2)^2||E_t(T)T^2||
       <=(2/3)sum_(r=1)^d r^3||K_r(T)T^2||.

Equation (9) proves (3). All sums here are finite; their bound is
uniform before taking N to infinity.

Taylor's formula with integral remainder holds in the Banach space
of bounded operators and gives

    C_N(x_j+a(t-1/2))
      =C_N(x_j)+a(t-1/2)C_N'(x_j)+D_t,
    ||D_t||<=(a^2/2)(t-1/2)^2 c_2.

Multiply on the right by E_t(T)T^2 and sum. The constant term is
zero and the linear term is a C_N'(x_j)p'(T)T^2. Equations
(2)–(3) prove (4), keeping the coefficient on its original left
side. No commutation with C_N or its derivatives is used.

### 4. Check the chosen mass and degree without a fixed-degree limit

The exact rho in L205 obeys

    log(1/rho_epsilon)=2 asinh(sqrt(epsilon)/4)
       >=2 sqrt(epsilon)/sqrt(16+epsilon)
       >=(2/sqrt(17))sqrt(epsilon),

for 0<epsilon<=1. Hence m>=6 epsilon^(-1/2)log N gives

    eta<=2N^(-12/sqrt(17))<=2N^(-11/4).

The last comparison follows from 48>11 sqrt(17), or 2304>2057.
Together with m<=C N^(7/8)log N, this bounds

    a eta(1+17m^2/8)<=C N^(-2)(log N)^2,
    a^2 epsilon^(-1/2)=64N^(-9/8),
    a^2 eta d^4<=C N^(-5/4)(log N)^4.

These prove (5); all three terms are o(N^(-1)). The transition is
interior by L205–L206, so its coefficient interval crosses no upper
pin. This calculation has not approximated the long plateau or
the finite projection. Its remaining energy insertion is a real
restriction: ||T^(-2)||=epsilon^(-2), and unweighting (4) by that
generic bound would lose its useful smallness. The other trace
factors must instead supply the appropriate energy control.

All checks are analytic finite sums, scalar recurrences, norm
inequalities and exponent comparisons. No mathematical script or
numerical preview is used as proof.

## Mathlib

Full matching actual-probe coefficient replacement and cubic limit:
**not checked**. Supporting spectral calculus, Fourier series,
Chebyshev derivatives and Banach-valued Taylor coverage: **not
checked**; unknown availability is not absence. The spectral theorem
and Taylor's theorem are used in their standard bounded self-adjoint
and norm-C^2 forms. The elementary derivative and resolvent formulas
are proved here because their mass-uniform errors at this precise
growing degree are needed; no general approximation or flow theorem
is reproved. L205 supplies the polynomial, relative error and degree
schedule, and L206 the signed transition and lattice midpoint.
Reuse the unchanged [approved assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
within its exact joint-group target. No new literature or originality
claim is made.
