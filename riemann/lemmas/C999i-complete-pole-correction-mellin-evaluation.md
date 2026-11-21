# Corollary 999i: exact Mellin evaluation of the complete pole correction

## Hypotheses

Use C999h's normalization, its correction Q in definition(1), and
C999g's theta convention. Thus, for real w,t, put

    theta(q)=sum_(n in Z) exp(-pi*n^2*q),
    B(x)=log theta(exp(2x)), a=w/2, s=a+i*t,
    Q(w,t)=2*(a^2-t^2)/(a^2+t^2)^2
           +4 integral_0^infinity B(x)*cosh(a*x)*cos(t*x) dx.

Initially 1<=w<=3/2 and 40<=t<=45. No event, zero-free, sign,
curvature or RH hypothesis is made. Write Psi(z)=xi_Q(0,z) for the
zero-parameter slice of the source completion; this is different from
the positive-parameter family G(w,t)=xi_Q(w,w/2+i*t).

Import J. C. Lagarias and E. Rains, *On a Two-Variable Zeta Function
for Number Fields*, [arXiv:math/0104176v5, 7 July 2002](https://arxiv.org/pdf/math/0104176v5),
Theorem5.1/(5.1), printed p24, and its proof, pp26--27:

    Psi(z)=(z^2/2) integral_0^infinity
                         log theta(r^2)*r^z dr/r, Re(z)>0,
    Psi(z)=-(z^2/8)*(1-2^(1+z/2))*(1-2^(1-z/2))
                    *zetahat(z/2)*zetahat(-z/2),
    zetahat(v)=pi^(-v/2)*Gamma(v/2)*zeta(v).

The product has its source continuation at removable singularities.
Its derivation by a Dirichlet series requires Re(z)>2; only the
continued identity and the right-half-plane Mellin integral are used
here. The theorem is imported, not reproved. The specialization below
is needed to match both half-lines and the complete rational term of Q.

## Conclusion

Exactly, with s=w/2+i*t,

    Q(w,t)=4 Re(Psi(s)/s^2)                                      (1)
          =-(1/2) Re[(1-2^(1+s/2))*(1-2^(1-s/2))
                      *zetahat(s/2)*zetahat(-s/2)].              (2)

The defining correction and the Mellin matching are absolutely
convergent, locally uniformly on a real neighborhood of the stated
rectangle. The proof gives bounds on the larger compact rectangle
1/2<=w<=2, 39<=t<=46. Formula(2) evaluates Q independently of G,
G_tt and any prospective collision. It supplies no sign for Q or
for the combined nonlocal residual in C999h, and no RH result.
The identity, domains, convergence assertions and direct inputs passed
the separate conceptual audit in step441 (11 November 2026), recorded
below. This validates the existing specialization, not a sign theorem
or a result beyond the cited source scope.

## Proof

### Convergence before the half-line split

The real modular identity from C999g gives, for u>=0,

    B(-u)=u+B(u).

C999h's real theta bound gives, with epsilon(u)=exp(-2*exp(2u)),

    0<=B(u)<=6*epsilon(u), u>=0.

For a complex variable z with Re(z)>0 define

    I(z)=integral_R B(x)*exp(z*x) dx.

Fix any 0<delta<=A<infinity. For delta<=Re(z)<=A, the integrand's
absolute value on x=u>=0 is bounded by

    6*exp(A*u)*epsilon(u).

On x=-u<=0 it is bounded by

    u*exp(-delta*u)+6*exp(-delta*u)*epsilon(u).

Both are integrable on [0,infinity). The first decays faster than
any exponential. These bounds remain integrable after multiplication
by u^k for any fixed nonnegative integer k. They prove absolute and
compact-uniform convergence on Re(z)>0, and justify holomorphic
differentiation of I there. In particular the change of variable
r=exp(x), with dr/r=dx, in the imported Mellin integral is legitimate:

    I(z)=integral_0^infinity log theta(r^2)*r^z dr/r
        =2*Psi(z)/z^2.                                        (3)

No Dirichlet series is evaluated in this domain.

### The rational term is exactly the negative-half-line contribution

Absolute convergence permits splitting I at zero and using x=-u
on its negative half-line. The modular identity yields

    I(z)=integral_0^infinity B(u)*(exp(z*u)+exp(-z*u))du
          +integral_0^infinity u*exp(-z*u)du
        =2 integral_0^infinity B(u)*cosh(z*u)du+1/z^2.          (4)

For Re(z)>0 the last elementary integral equals 1/z^2, by integration
by parts (the boundary u*exp(-z*u) vanishes) and the convergent
Laplace integral. Every term in (4) converges separately. This
calculation concerns the already convergent logarithmic Mellin input;
it does not split C999h's nonintegrable raw pole subtractions.

Now z=s=a+i*t, with a>0 and t real. Direct algebra gives

    Re(1/s^2)=(a^2-t^2)/(a^2+t^2)^2,
    Re cosh((a+i*t)*u)=cosh(a*u)*cos(t*u).

Taking twice the real part of (4) therefore reproduces the entire
definition of Q, including its rational summand:

    2 Re I(s)=2*(a^2-t^2)/(a^2+t^2)^2
                +4 integral_0^infinity B(u)*cosh(a*u)*cos(t*u)du
             =Q(w,t).

Combining this with (3) proves (1). Substitution of the imported
Theorem5.1/(5.1) proves (2); its factor is 4*(-1/8)=-1/2.
On our rectangle, s/2 and -s/2 are nonreal and thus avoid the
completed zeta poles at 0 and 1. No division by zeta or by a
possibly vanishing G or curvature occurs.

### Uniformity and scope

On 1/2<=w<=2, 39<=t<=46, we have 1/4<=Re(s)<=1, so the I bounds
above apply with delta=1/4 and A=1. Also s!=0 throughout a surrounding
open neighborhood of the original rectangle. Independently the
absolute integrand in Q's integral, including its factor4, is at
most 24*exp(u)*epsilon(u), uniformly on this larger real rectangle.
Every fixed parameter derivative of that integrand is bounded by
the same expression times a power of u. The rational summand has
a^2+t^2>0 and is smooth there. Thus taking real parts, passing through
the integral and the stated local-uniform assertion are justified.

The required threshold was exact equality without an unpaid pole
term; equations(3)--(4) meet it. This is a local specialization of
known mathematics, with no claim of progress beyond the cited source.
An independently evaluable correction may later help retain its
cancellation with the far-jump term. The far-jump sign, relative
curvature control, event existence and nondegeneracy, multiplicities,
initialization, other heights and global transport remain unresolved.

### Independent conceptual audit — step441

The audit checked the whole local proof against C999h definition(1),
its real theta bound, C999g's modular relation and the primary source.
No mathematical correction or additional premise was needed.

The source is Lagarias–Rains arXiv:math/0104176v5, Theorem5.1/(5.1),
printed p24, with its complete proof on pp26--27. Its theta convention
(1.2), p2, agrees with ours. The source completion is xi_Q, not zeta
or the positive-parameter slice G. Its proof supplies the displayed
logarithmic Mellin formula for Re(z)>0. The subsequent series step
requires Re(z)>2; its final product is analytically continued. The
two powers of 2, the arguments z/2 and -z/2, and coefficient -z^2/8
in the local import match (5.1). No source series is used on our box,
and no source proof is being replaced by a local reproof.

For completeness, the domination check applies to every differentiation
actually asserted: after k derivatives of I, the positive half-line
has majorant 6*u^k*exp(A*u-2*exp(2u)); the negative half-line has
majorant (u^(k+1)+6*u^k*epsilon(u))*exp(-delta*u). The latter has
finite integral for delta>0. For the former, v=exp(2u) reduces its
tail to a constant times (log v)^k*v^(A/2-1)*exp(-2v), integrable
for every fixed A and k. At u=0 all majorants are bounded. These
bounds hold on a strip containing any compact subset of Re(z)>0;
they justify the holomorphic integral and its differentiated versions,
not merely pointwise convergence. Substitution r=exp(x) is therefore
valid as an absolutely convergent improper-integral change of variables.

On the negative half-line the real modular identity gives exactly
B(-u)=u+B(u), with no logarithm branch ambiguity because theta is
positive on the positive real axis. The boundary values in integration
by parts for integral u*exp(-z*u) are zero at both endpoints; the
remaining integral is (1/z)*integral exp(-z*u)=1/z^2. Hence (4)
retains the whole negative-half-line contribution. Taking twice its
real part gives both terms of C999h(1), with factors 2 and 4 as written.
Combining with (3) and then (5.1) gives respectively 4*Re(Psi(s)/s^2)
and the factor 4*(-1/8)=-1/2. In particular the rational term must
neither be removed before matching nor added a second time to (2).

On the larger real rectangle, a is in [1/4,1]. For any fixed integers
m,n>=0, the absolute value of

    partial_w^m partial_t^n [4*B(u)*cosh(w*u/2)*cos(t*u)]

is at most 24*2^(-m)*u^(m+n)*exp(u)*epsilon(u). Hyperbolic
sine or cosine is bounded by exp(u), and the real trigonometric
factors are bounded by 1. This integrable bound checks every stated
fixed real parameter derivative. Also a^2+t^2>=39^2, so the rational
term and all its fixed derivatives are continuous and bounded on
this compact rectangle. Its interior contains the original closed
rectangle, including its edges. Thus the claimed real neighborhood
and uniformity are covered. On the larger rectangle s/2 has imaginary
part in [39/2,23], and -s/2 has the opposite nonzero imaginary part;
the completed-zeta poles are avoided. Their gamma arguments s/4 and
-s/4 are nonreal as well. Zeta zeros cause no problem, since there
is no division by zeta, G, or curvature.

C999h supplies the exact definition and the real bound used here;
C999g supplies the theta convention and modular identity. These are
exactly the direct local inputs in the existing DAG row. L018/L019
fix the inherited normalization through them; no extra direct use
of their zero-correspondence or kernel conclusions occurs in this
calculation. C999h(3) is downstream motivation, and C999f is not a
premise. The audit does not import a positive-w semigroup or any event
sign. The exact-equality and uniformity test passes, leaving the signed
residual and all the previously listed transport obligations open.

## Mathlib

Full matching coverage is unchecked and unknown. No formal verification
is claimed. Change of variables in absolutely convergent integrals,
dominated convergence and the elementary Laplace integral are supporting
facts; neither these nor the imported zeta-product theorem are claimed
to establish a matching Mathlib theorem for the complete Q identity.
