# Corollary C028l: constant Appell finite-range identity counterexample

## Hypotheses

Use J. Fernando Barbero G., Jesús Salas and Eduardo J. S. Villaseñor,
*On the asymptotics of the rescaled Appell polynomials*,
[arXiv:1903.08540v3, 17 November 2019](https://arxiv.org/pdf/1903.08540v3),
(1.1)-(1.2), p.1, (2.3), p.3, Section 3, pp.5-9, especially
(3.3), (3.15)-(3.17), (3.20), and Theorem 3.1/(3.21), p.9.
Take exactly the admissible model g identically 1, n=1, x=1.
The defining generating function is exp(xz)/g(z), and pi_n(x)=p_n(nx).
The constant g is entire, g(0)=1, and has no zeros. No minimum zero
modulus is needed to choose the initial coefficient circle in this model.

The source's real-parameter branch theta has theta(0)=0,
theta'(0)=sqrt(2), positive real part in (0,pi) for tau>0, and

    exp(i theta(tau))-i theta(tau)=1-tau^2,
    theta(-tau)=-conjugate(theta(tau)).

No actual-Xi series, RH, actual-F contour deformation or zero-location
hypothesis is used. This is the single-model verification approved by
assessment1599, not a proof of a general corrected source theorem.

## Conclusion

The defining coefficient gives pi_1(1)=p_1(1)=1. With the stated branch,
the absolutely convergent full-line model expression in (3.20) satisfies

    I_infinity := (e/(2pi)) integral_R theta'(tau) exp(-tau^2) d tau = 1.

The printed finite-range model expression in (3.21) instead satisfies

    I_pi := (e/(2pi)) integral_(-pi)^pi theta'(tau) exp(-tau^2) d tau
          = 1-T,
    0 < T < exp(1-pi^2).

Thus I_pi is real and strictly less than 1. No residues or principal-value
terms exist in this model to supply T. The printed exact finite-range
identity (3.21) fails for this admissible model, while the full-line
identity survives this model's endpoint and orientation checks. This
identifies a range error in the printed model specialization; it does
not establish any source-wide corrected theorem, actual-F bound,
nonreal actual zero, or payment of C028b's H_d=o(d).

## Proof

### Independent coefficient and methods

Equation (1.1), with g=1, is the Taylor series of exp(xz); hence p_1(x)=x
and pi_1(1)=1, independently of either identity under audit. We use the
standard named Cauchy coefficient formula and Cauchy integral theorem
(the former is also the source's (1.2)). We verify the present model's
changes of variable and unbounded-contour limit explicitly because
Section 3 makes endpoint decay an additional proviso. We do not reprove
a general Appell representation or invoke the suspect (3.21).

### Identify the complete branch and its orientation

For -pi<X<pi set

    Y(X)=log(sin X/X),       Y(0)=0,
    h(X)=1-X cot X+log(X/sin X),       h(0)=0.

All logarithm arguments here are positive real numbers; the definitions
at zero are removable limits. Both functions are smooth and even. For
0<X<pi, direct differentiation gives

    Y'(X)=cot X-1/X<0,
    h'(X)=X csc^2 X+1/X-2 cot X
         =[(X-sin X cos X)^2+sin^4 X]/[X sin^2 X]>0.

For the first strict sign, sin X-X cos X has derivative X sin X>0
and limit zero at zero. Taylor expansions at zero give

    Y(X)=-X^2/6+O(X^4),
    h(X)=X^2/2+O(X^4).

In fact h/X^2 extends analytically near zero with positive value 1/2.
As X increases to pi, Y decreases to -infinity and h increases to
infinity: -X cot X and log(X/sin X) both tend to positive infinity.
Consequently

    tau(X)=sign(X)*sqrt(h(X)),       tau(0)=0

is a smooth, strictly increasing bijection from (-pi,pi) onto R, with
nonvanishing derivative, including tau'(0)=1/sqrt(2). Let X(tau) be its
inverse. In particular X'(tau)>0 for every real tau,
X(-tau)=-X(tau), and X(tau) tends to pi as tau tends to infinity.
Define theta(tau)=X(tau)+iY(X(tau)). Then

    exp(i theta)= (X/sin X)(cos X+i sin X),
    exp(i theta)-i theta=X cot X+Y=1-h(X)=1-tau^2.

The identities extend across zero by continuity. This is precisely the
source's positive branch and its negative conjugate branch: the imaginary
part equation at Re theta=X in (0,pi) forces Y=log(sin X/X), and the
strict increase of h gives uniqueness for each tau>0. At zero,
theta'(0)=sqrt(2). Hence increasing tau or X follows the source curve
from its left endpoint towards its right endpoint. Differentiating the
conjugation relation gives

    theta'(-tau)=conjugate(theta'(tau)).                 (1)

There is no orientation reversal or missing sign in this Jacobian.

### Coefficient circle and the complete deformation

Put f(theta)=exp(exp(i theta)-i theta), an entire, 2pi-periodic function
of theta. Fix eta>0. On the positively oriented circle |z|=exp(-eta),
the substitution z=exp(i theta), from theta=-pi+i eta to pi+i eta,
has dz=i z dtheta. Cauchy's coefficient formula therefore gives

    1=[z]exp(z)
     =(1/(2pi i)) contour_integral exp(z) dz/z^2
     =(1/(2pi)) integral_(-pi+i eta)^(pi+i eta) f(theta) dtheta. (2)

For R>0 let a_R in (0,pi) be the unique number with Y(a_R)=-R.
Let C_R be the graph theta=X+iY(X), -a_R<=X<=a_R, oriented from
left to right. Join its endpoints horizontally to -pi-iR and pi-iR,
and join those two points vertically to the endpoints of the top
segment in (2). The top segment runs left to right. Cauchy's theorem
on the finite region between the top and this lower curve gives

    integral_top f = integral_C_R f
                    + integral_(-pi-iR)^(-a_R-iR) f
                    + integral_(a_R-iR)^(pi-iR) f.      (3)

Indeed, the right vertical boundary runs down and the left runs up;
their integrals cancel exactly by 2pi-periodicity. The lower boundary
in the closed contour is traversed right to left, giving the signs in
(3). The integrand has no theta-plane singularities, and g=1 has no
zeros, so there are no residue terms. The coefficient pole at z=0
was already accounted for in (2); z=exp(i theta) never vanishes.

As R tends to infinity, a_R tends to pi. For large enough R, a_R>=pi/2.
On either horizontal connector, theta=u-iR with |u|>=a_R, and

    |f(u-iR)|=exp(exp(R) cos u-R)<=exp(-R).

Their combined length is at most 2pi, so the absolute value of their
combined contribution is at most 2pi exp(-R), tending to zero.
This verifies all the connector terms of this model's deformation.

### Absolute convergence at both full-curve endpoints

On the curve, f(theta)=exp(X cot X+Y(X)) is positive real. The
arc integral in absolute value is bounded by

    integral_(-pi)^pi exp(X cot X+Y(X))*(1+|Y'(X)|) dX.  (4)

There is no singularity at zero, by the displayed expansions. Near
the positive endpoint set delta=pi-X with 0<delta<=pi/4. Since
X>=pi/2, cos delta>=1/2, and sin delta<=delta, we have

    X cot X=-X cot delta<=-pi/(4delta).

Also exp(Y)=sin X/X<=1. Using sin delta>=2delta/pi and X>=pi/2,

    |Y'(X)|=cot delta+1/X<=pi/(2delta)+2/pi.

Thus the integrand in (4) is at most

    exp(-pi/(4delta))*(1+pi/(2delta)+2/pi),

which is integrable at delta=0 by the substitution u=1/delta.
Evenness gives the same estimate at the negative endpoint. This proves
absolute convergence of the entire curve integral, not just a finite
preview. Taking R to infinity in (2)-(3) is now justified and gives

    (1/(2pi)) integral_C f(theta) dtheta=1.             (5)

The increasing parameter tau covers all of C. On every finite segment
f(theta(tau))=e*exp(-tau^2). Equation (4) implies absolute convergence
after substitution as well, since
|dtheta|=|theta'(tau)| d tau. Hence (5) proves I_infinity=1, with the
orientation and complete endpoints required for (3.20) in this model.

### The complete omitted tails and strict discrepancy

Absolute convergence and (1) permit pairing the negative and positive
tails. Their combined imaginary part is zero, and their normalized sum is

    T=(e/(2pi)) integral_(|tau|>pi) theta'(tau) exp(-tau^2) d tau
     =(e/pi) integral_pi^infinity exp(-tau^2) X'(tau) d tau.    (6)

Every factor in the last integrand is strictly positive. In particular
its integral on any closed subinterval of positive length in (pi,infinity) is
strictly positive, proving T>0 for the complete tails. Writing a=X(pi),
where 0<a<pi, the fundamental theorem of calculus and X(tau)->pi give

    integral_pi^infinity X'(tau) d tau=pi-a.

Because exp(-tau^2)<exp(-pi^2) for every tau>pi, (6) gives

    0<T<(e/pi)*exp(-pi^2)*(pi-a)<exp(1-pi^2).           (7)

No omitted portion of the infinite tails has an uncontrolled sign or
size. Equivalently the exact complete tail can be written

    T=(1/pi) integral_a^pi exp(X cot X)*(sin X/X) dX>0,

with endpoint integrability already proved. Splitting the absolutely
convergent full integral at +/-pi yields I_pi=I_infinity-T=1-T.
There is no principal-value issue, since g=1 and theta is smooth.
There are no g-zero residues in (3.21). Thus its printed finite-range
right side is I_pi<1, contrary to its left side pi_1(1)/1!=1.

### Scope and research decision

This is a direct replay and obstruction test of a suspect cited identity,
not a new zero-location theorem. The special verification is necessary
because quoting the suspect finite range would invalidate a later
contour interface. Keep the original scope stop1599: actual F would
still require different hypotheses, its own full endpoint bounds and
an independent signed estimate controlling compact nonreal-root mass.
Nothing here provides those, or corrects the general residue formula.
The constant-model audit is complete; repeating identity-only tests is
not a continuation towards the actual height gap.

## Mathlib

Full matching coverage is not checked and remains unknown. No formal
verification or claim of absence is made. The proof uses the standard
named Cauchy coefficient formula, Cauchy integral theorem, inverse function
theorem, and elementary real estimates, with every model-specific
hypothesis and unbounded limit verified above. Source claims outside
this exact model are neither imported nor audited here.
