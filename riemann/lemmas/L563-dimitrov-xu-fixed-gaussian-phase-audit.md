# Lemma 563: fixed-Gaussian audit of the printed Fourier/correlation interface

## Hypotheses

Use the convention

    Ff(x)=integral_R f(u) exp(-ixu) du,
    W(h)(x)=h(x)h''(x)-h'(x)^2.

Fix K(u)=exp(-u^2) and y=1. Define

    V(z)=integral_R K(u) exp(-izu) du,
    phi(x)=Re V(x+i),  psi(x)=Im V(x+i),
    c(u)=cosh(u)K(u),  s(u)=sinh(u)K(u),
    nu_f(t)=integral_R (t-2u)^2 f(t-u)f(u) du,
    P(t)=cosh(t)nu_K(t).

All integrals here use ordinary one-dimensional Lebesgue measure; no
factor is hidden in nu_f. The letter s in this file denotes the odd
function above when it occurs as a subscript, not a complex coordinate.

The audited source is Dimitar K. Dimitrov and Yuan Xu, *Wronskians of
Fourier and Laplace transforms*,
[arXiv:1606.05011v1](https://arxiv.org/pdf/1606.05011v1), Fourier/Wronskian
definitions p. 3, (3.3) p. 10, (3.7) p. 11, Lemma 3.3 p. 12 and
Section 3.1 pp. 13–14. The explicit n=2 correlation integral appears
also on p. 7. The comparison is with this version only.

Import the classical Gaussian Fourier transform in the normalization
used in L233:

    F(exp(-a u^2))(x)=sqrt(pi/a) exp(-x^2/(4a)),  a>0.

This is a known input, not a new Gaussian-transform result. The
calculation below is necessary to check the suspect phases and the
normalization rather than assume the source identity being audited.

## Conclusion

For every real x, put A(x)=sqrt(pi) exp((1-x^2)/4)>0. Then

    phi(x)=A(x)cos(x/2),  psi(x)=-A(x)sin(x/2),
    Fc(x)=phi(x),         Fs(x)=i psi(x),                 (1)
    W(phi)(x)+W(psi)(x)=-A(x)^2,                        (2)
    nu_K(t)=sqrt(pi/2)exp(-t^2/2),
    FP(x)=A(x)^2 cos(x).                               (3)

Thus Lemma 3.3's identification psi=Fs fails, as does the positive
sine expression for Im V following (3.7). Section 3.1's printed
combination W(phi)+W(psi)=-FP also fails. At x=pi the actual sum
is -A(pi)^2<0 and the proposed right side is +A(pi)^2>0.

The corrected combination for this fixed Gaussian calculation is

    W(phi)+W(psi)=-(1/2)FJ,
    J(t)=nu_c(t)-nu_s(t)
        =integral_R (t-2u)^2 cosh(t-2u)K(t-u)K(u) du
        =2 exp(1/2)sqrt(pi/2)exp(-t^2/2).               (4)

The spatial identity nu_c+nu_s=P is valid, but it is the wrong
combination for (2). Both the phase and the factor 1/2 matter.

K is even, positive and Schwartz; V is entire, zero-free, and fits
Theorem A's Gaussian-factor allowance. However V fails the displayed
product hypothesis (3.8) of Theorem 3.2. This is consequently an exact
failure of the tested intermediate identities, not a counterexample
satisfying all hypotheses of Theorem 3.2. No actual-theta sign,
translate-approximation error or conclusion about RH follows.

## Proof

### Convergence and the complex Gaussian transform

For each nonnegative integer m and each fixed M>0,

    |u|^m exp(-u^2+M|u|)
        <= exp(M^2/2)|u|^m exp(-u^2/2)

is integrable. On every compact set of complex z this bounds the
integrands for V and all its complex derivatives. Dominated
differentiation therefore makes V entire. The classical real-axis
Gaussian transform and the identity theorem give

    V(z)=sqrt(pi)exp(-z^2/4),  z in C.                  (5)

There is no unproved contour shift. The same moment bounds justify
the transform derivatives of c and s used below. After writing
t=u+v, every double integral used here is bounded in absolute value
by an integrable polynomial times
exp(-u^2-v^2+|u|+|v|). This covers Fubini and the weighted
correlations, including their transforms. It also gives all weighted
integrability needed for the following computations.

Substitute z=x+i in (5). Since (x+i)^2=x^2-1+2ix,

    V(x+i)=A(x)[cos(x/2)-i sin(x/2)].

Expanding cosh and sinh before integration, with absolute convergence,
gives

    Fc(x)=[V(x+i)+V(x-i)]/2=A(x)cos(x/2),
    Fs(x)=[V(x+i)-V(x-i)]/2=-i A(x)sin(x/2).

This proves (1). Equivalently, parity gives

    psi(x)=-integral_R sinh(u)K(u)sin(xu)du,
    Fs(x)=-i integral_R sinh(u)K(u)sin(xu)du=i psi(x).

At x=pi the real number psi(pi)=-A(pi) differs from Fs(pi)=-i A(pi);
the printed positive sine integral instead equals +A(pi). This is
an exact nonzero-frequency witness, not a numerical approximation.

### Direct Wronskian evaluation

For any twice differentiable q, product differentiation gives

    W(Aq)=A^2 W(q)+(AA''-A'^2)q^2
         =A^2[W(q)-q^2/2],                            (6)

because (log A)''=-1/2. The Wronskians of cos(x/2) and sin(x/2)
both equal -1/4. Changing a function's sign leaves W unchanged.
Thus

    W(phi)=-A^2[1/4+cos(x/2)^2/2],
    W(psi)=-A^2[1/4+sin(x/2)^2/2].

Their sum is -A^2, proving (2) at all real x, including zeros of
either component. No logarithm of a vanishing component is used.

### Independent correlation evaluation and exact disagreement

In nu_K set r=u-t/2. Then

    (t-2u)^2=4r^2,
    K(t-u)K(u)=exp(-t^2/2)exp(-2r^2).

The classical Gaussian second moment gives

    integral_R 4r^2 exp(-2r^2)dr=sqrt(pi/2),

so nu_K has the value in (3). Its cosh(t)-weighted transform is
computed from the Gaussian transform with a=1/2, extended to complex
arguments by the same domination/identity-theorem argument as (5):

    FP(x)=(pi/2)[exp(-(x+i)^2/2)+exp(-(x-i)^2/2)]
         =pi exp((1-x^2)/2)cos(x)=A(x)^2 cos(x).

Consequently, the difference between the actual Wronskian sum and
the proposed value -FP is A(x)^2[cos(x)-1]. At x=pi it equals
-2pi exp((1-pi^2)/2), strictly negative, while the two sides have
opposite signs. A constant normalization change cannot eliminate
the varying cos(x). Agreement at x=0 would miss this failure.

### Locating the phase, weight and normalization corrections

For f equal to K, c or s, let H=Ff. Fubini with the bounds above and
the substitution t=u+v give directly, without using Theorem 2.5,

    Fnu_f(x)=integral_R^2 (u-v)^2 f(u)f(v)
                         exp(-ix(u+v))du dv
             =-2H(x)H''(x)+2H'(x)^2=-2W(H)(x).        (7)

Indeed integral u f(u)exp(-ixu)du=iH'(x) and the second moment
transform is -H''(x); expanding (u-v)^2 gives precisely (7).
This proves the factor 1/2 for the explicit integral normalization
used here. It makes no claim about all n or other correlation
measure conventions in the source.

The Wronskian is quadratic under scalar multiplication:
W(i psi)=-W(psi). Hence (1) and (7) imply

    W(phi)=-(1/2)Fnu_c,
    W(psi)= +(1/2)Fnu_s.

The hyperbolic addition identities yield, inside the absolutely
convergent integrals,

    nu_c(t)+nu_s(t)=cosh(t)nu_K(t),
    nu_c(t)-nu_s(t)=integral_R (t-2u)^2 cosh(t-2u)
                                      K(t-u)K(u)du.

The first identity survives the audit; the second is the combination
required by the real/imaginary Wronskians. To evaluate the latter,
the same substitution r=u-t/2 gives

    J(t)=exp(-t^2/2) integral_R 4r^2 cosh(2r)exp(-2r^2)dr.

For real b, completing the square in the Gaussian integral gives

    integral_R exp(-2r^2+br)dr=sqrt(pi/2)exp(b^2/8).

Twice differentiating in b is justified on compact b intervals by
the Gaussian moment bound. At b=2 or b=-2 the second derivative is
(1/2)sqrt(pi/2)exp(1/2). Averaging these values and multiplying
by 4 proves the value of J in (4). Therefore FJ=2A^2 and
-(1/2)FJ=-A^2, in exact agreement with the direct computation.
Every square in (6)–(7) is algebraic; no modulus square has been
substituted for the transform of the odd kernel.

### Scope relative to the product hypothesis

Formula (5) is nonzero everywhere, so its zeros lie in any prescribed
open horizontal strip vacuously. K is an even Schwartz kernel, and
V(z)=exp(-z^2/4)V_1(z) with the nonzero constant V_1=sqrt(pi)
of genus zero. Thus the Fourier representation (3.7) and the
Gaussian-factor setting of Theorem A present no obstacle to this
diagnostic.

In contrast, (3.8) requires V to be V(0) times a product over its
zeros, without a nonconstant zero-free Gaussian factor. Here there
are no zeros; that product is empty and equals 1. It would make V
constant, contradicting (5). Theorem 3.2 therefore cannot be applied
to this example. If Lemma 3.3 is read as inheriting that narrower
ambient hypothesis, this example proves inconsistency of the
displayed identities in the broader (3.7) setting, rather than a
counterexample within the narrowed class. No product-admissible
counterexample or theorem-wide verdict is asserted.

The calculation supplies new local evidence about the checked source
interface. It reproduces elementary Gaussian/Fourier algebra and is
not claimed as mathematics beyond the sources checked. The actual-Xi
signed remainder, all higher signs and any constructive approximation
remain unresolved.

## Mathlib

The full fixed-Gaussian source audit and its supporting Gaussian/Fourier
identities have not been checked in Mathlib. Availability is unknown;
no absence or formal verification is claimed. The standard Gaussian
transform is imported as stated above, and the relevant calculations
are proved here. [Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
