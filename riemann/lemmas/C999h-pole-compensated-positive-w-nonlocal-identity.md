# Corollary 999h: a pole-compensated positive-w nonlocal identity

## Hypotheses

Use C999g's theta normalization and completed family

    theta(q)=sum_(n in Z) exp(-pi*n^2*q),
    xi_Q(w,s)=s*(s-w)*Z_Q(w,s)/(2w),
    G(w,t)=xi_Q(w,w/2+i*t).

In particular G(1,t)=Xi(t), with the normalization inherited from
L018/L019. Here w,t are real, initially 1<=w<=3/2 and 40<=t<=45.
Every parameter derivative holds t fixed, so s moves with w.
No zero, sign, nondegeneracy or RH assumption is imposed.

The external inputs are J. C. Lagarias and E. Rains, *On a Two-Variable
Zeta Function for Number Fields*, [arXiv:math/0104176v5, 7 July 2002](https://arxiv.org/pdf/math/0104176v5):
Theorem 2.1/(2.9), printed pp. 8--9; Theorem 2.2 case III/(2.12),(2.15)
and proof (2.17)--(2.22), pp. 10--11; Proposition 7.2/(7.12), p. 37;
and Theorem 7.4/(7.15)--(7.16) and proof, pp. 38--39. Import their
case-III transform and finite, even, nonnegative canonical density

    M(y)=xi_Q(0,i*y)/pi,     m=integral_R M(y)dy<infinity.

This measure is absolutely continuous, so has no atom at zero.
Its characteristic function is f(x)=theta(1)*exp(-x/2)/theta(exp(2x)).
Use the source's sine compensation in (7.12). These theorems are
imported, not reproved; only their positive-w specialization is derived.

Put, for real x and w>0,

    B(x)=log theta(exp(2x)), b(x)=x/2+B(x), b0=b(0),
    a=w/2, d_w(t)=t^2+w^2/4, c_w(t)=-d_w(t)/(2w),
    h_w(x)=exp(w*b(x))-exp(a*x)-exp(-a*x),
    H(w,t)=Z_Q(w,w/2+i*t), U(w,t)=G(w,t)/d_w(t).

The logarithm here is real. C999g's modular identity makes b and h_w
even. In c_w and h_w, the subscript labels the parameter; partial_w
below always denotes differentiation. Write nu(dy)=M(y)dy/y^2 for
y!=0. This is a jump measure, not the finite canonical measure itself.

## Conclusion

Define the explicit correction

    Q(w,t)=2*(a^2-t^2)/d_w(t)^2
           +4 integral_0^infinity B(x)*cosh(a*x)*cos(t*x) dx.       (1)

Then the completed parameter equation is

    partial_w G(w,t)
      =(b0+w/(2*d_w(t))-1/w)*G(w,t)
       +(d_w(t)/2) integral_R
          [2*U(w,t)-U(w,t+y)-U(w,t-y)] nu(dy)
       -(d_w(t)/(2w))*Q(w,t).                                 (2)

Both the paired nonlocal integral and the correction are absolutely
convergent, locally uniformly on a real neighborhood of the stated
rectangle. The proof supplies a common integrable majorant even though
the nonlocal integral uses all real ordinates t+y. Formula (2) holds
without a global sign hypothesis or a positive-w semigroup assertion.

At a **prospective** pair (w,t) satisfying G(w,t)=G_t(w,t)=0, the
residual is exactly

    partial_w G(w,t)
      =-(d_w(t)/2) integral_R
           [U(w,t+y)+U(w,t-y)] nu(dy)
       -(d_w(t)/(2w))*Q(w,t).                                 (3)

Each shifted term in (3) is individually absolutely integrable there.
No sign for (3), no actual event, and no sign for G_w*G_tt is asserted.
This is a local analytic input, not a solution of the positivity gap.
The identity, all stated convergence claims and the event specialization
passed the separate conceptual audit in step435 (11 November 2026).
That audit validates this specialization of the cited transforms; it
establishes no residual sign or result beyond the assessed source scope.

## Proof

### The two subtractions and a common majorant

Because 0<Re(s)=w/2<w, case III of the cited transform applies.
Multiplying its integrand by exp(w*x/2) gives exactly

    H(w,t)=integral_R h_w(x)*exp(i*t*x) dx, G(w,t)=c_w(t)*H(w,t).
                                                                    (4)

The subtractions 1 and exp(-w*x) have become exp(a*x) and exp(-a*x).
Neither is integrated separately. This is a direct use of the source
transform, not continuation of its negative-w semigroup.

Here are explicit bounds sufficient for every interchange below.
Work on the larger real parameter interval 1/2<=w<=2, and x>=0.
The half-strip theta-series bound used in C999g, restricted to the
real axis, gives, with epsilon(x)=exp(-2*exp(2x)),

    0<=B(x)<=6*epsilon(x)<1.

For clarity this restriction also follows from
theta(exp(2x))-1<=2*epsilon(x)/(1-exp(-6*exp(2x)))
<=3*epsilon(x), using pi>2 and n^2>=1+3(n-1).
The last coefficient uses exp(6)>3. The inequality log(1+u)<=u
suffices on the real axis, and 6*exp(-2)<1 follows from exp(2)>7.
Thus 0<=exp(w*B)-1<=2*B*exp(2B)<=108*epsilon, using exp(2)<9.
Writing h_w=exp(a*x)*(exp(w*B)-1)-exp(-a*x) yields

    |h_w(x)|<=E(x):=108*exp(x)*epsilon(x)+exp(-x/4),
    |partial_w h_w(x)|<=D(x)
       :=54*(x+1)*exp(x)*epsilon(x)+(x/2)*exp(-x/4).          (5)

The second bound follows by differentiating this last, convergent
expression: its three terms are (x/2)*exp(a*x)*(exp(wB)-1),
exp(a*x)*B*exp(wB), and (x/2)*exp(-a*x). The first two have
bounds 54*x*exp(x)*epsilon and 54*exp(x)*epsilon respectively.
Evenness gives the same bounds at negative x with x replaced by |x|.
All polynomial moments
of E and D are finite: the second terms decay exponentially and the
first terms decay faster than any exponential. In particular put

    A_j=integral_R |x|^j*E(|x|) dx<infinity, j=0,1,2.

Equation (4) can be differentiated in w by dominated convergence.
It also gives H twice continuously differentiable in t, with
|partial_t^j H(w,t)|<=A_j for every real t, uniformly in this larger
w interval. Differentiating in w at its interior points, or in a
smaller neighborhood of the target, is therefore legitimate.

Differentiating h_w without separating divergent integrals gives

    partial_w h_w(x)=b(x)*h_w(x)+r_w(x),
    r_w(x)=2*b(x)*cosh(a*x)-x*sinh(a*x).                    (6)

For x>=0 the complete correction simplifies to

    r_w(x)=x*exp(-a*x)+2*B(x)*cosh(a*x),
    |r_w(x)|<=x*exp(-x/4)+12*exp(x)*epsilon(x).             (7)

It is even. Also |b(x)*h_w(x)|<=(|x|/2+1)*E(|x|).
Thus both terms on the right of (6) are separately integrable,
uniformly in w. The cancellation in (7) is essential: the individual
terms 2*b*cosh and x*sinh in (6) need not be integrable.

### Canonical measure and the compensated operator

The source Theorem 7.4 proof fixes the normalization explicitly:
M(y)=(1/(2*pi))*integral_R gamma(0,x)*exp(-i*y*x)dx
=xi_Q(0,-i*y)/pi=xi_Q(0,i*y)/pi, where gamma(0,x)=B''(x)
in the source notation. Its finiteness and density
are part of that imported theorem; this is a normalization check,
not a new Fourier-inversion argument. The positive-w parameter w
does not enter this canonical measure.

The source characteristic function is positive and even on R, and
log f(x)=b0-b(x). Theorem 7.4 and Proposition 7.2 consequently give

    b(x)-b0=integral_R [1-cos(x*y)] nu(dy).                 (8)

Here is the compensation check for this specialization. In (7.12)
the combined imaginary integrand sin(x*y)-x*sin(y), divided by y^2,
is absolutely integrable against M(y)dy: for |y|<=1 its magnitude
is at most (|x|^3+|x|)*|y|/6, by subtracting the linear terms
inside each sine; for |y|>1 it is at most (1+|x|)/y^2.
It is odd, so its integral is zero. The remaining drift coefficient
must be zero because its contribution is purely imaginary and log f
is real, with its continuous branch fixed at x=0. The real integrand is bounded
by x^2*M(y)/2 near zero and 2*M(y)/y^2 away from zero. This proves
that (8) uses ordinary absolutely convergent integrals. No atom at
zero, and hence no Gaussian term from such an atom, was discarded.

For a bounded twice continuously differentiable function phi with
bounded first and second derivatives, define the extended integral

    D_op phi(t)=integral_R
        [phi(t)-(phi(t+y)+phi(t-y))/2] nu(dy).              (9)

This is the negative of the symmetric jump-generator expression.
Its integrand, including the density M(y)/y^2, is bounded by

    (||phi''||_infinity/2)*M(y),             0<|y|<=1,
    2*||phi||_infinity*M(y)/y^2,             |y|>1.        (10)

Taylor's formula with integral remainder proves the first bound:
the centered second difference equals
integral_0^|y| (|y|-v)*[phi''(t+v)+phi''(t-v)]dv.
Multiplication by -1/2 gives the integrand in (9), before nu.
The triangle inequality proves the second. Thus (9) is well-defined
on this stated class. To compare with sine compensation, first
integrate over delta<|y|<R and pair y and -y in

    phi(t+y)-phi(t)-phi'(t)*sin(y).

The paired value is -D_op phi. The unsymmetrized combined expression
is also absolutely integrable: near zero its absolute value divided
by y^2 is at most ||phi''||_infinity/2+||phi'||_infinity*|y|/6,
using the Taylor remainder and |y-sin(y)|<=|y|^3/6;
away from zero use boundedness of phi and phi'. Dominated convergence
removes delta and R. Replacing sin(y)
by y*1_(|y|<1) changes the result by an absolutely integrable odd
function and therefore by zero. We have not separately integrated
an uncompensated first-order term against the singular jump measure.

This proves precisely the extension of the integral that is used
here, including its Fourier identity below. No claim that the
positive-w family is a probability semigroup, and no abstract
generator-domain inclusion beyond these direct estimates, is needed.

For H from (4), absolute Fubini is licensed by the particularly
simple uniform bound

    integral_R integral_R |h_w(x)|*|1-cos(x*y)|
                             *M(y)/y^2 dy dx <= m*A_2/2.  (11)

Indeed |1-cos(x*y)|<=x^2*y^2/2 for all real x,y. Consequently,
using the Fourier convention in (4),

    integral_R b(x)*h_w(x)*exp(i*t*x)dx
       =b0*H(w,t)+D_op H(w,t).                            (12)

The cosine multiplier produces the average of H(w,t+y) and
H(w,t-y); there is no 2*pi factor in this multiplication identity.
The density normalization M=xi_Q(0,i*y)/pi was already fixed by
the imported source. Bounds (10) with A_0,A_2 are common integrable
majorants for the complete nonlocal expression, for all real t
and 1/2<=w<=2. They justify parameter continuity under that integral.

### Completion and the explicit residual

Let Q be the Fourier transform of the complete r_w in (7).
Evenness, (7), and the elementary integral

    integral_0^infinity x*exp(-a*x)*cos(t*x)dx
       =(a^2-t^2)/(a^2+t^2)^2, a>0,

give exactly (1). The elementary integral follows by differentiating
integral_0^infinity exp(-(a-i*t)*x)dx=1/(a-i*t) in a;
x*exp(-a*x) provides domination. The remaining integral in (1)
is dominated by 6*exp(x)*epsilon(x) before its factor 4.
Thus its convergence and local uniformity are included in (7).
Both original pole subtractions contribute to the even r_w; the
rational term in (1) is not a disposable boundary term.

Equations (6) and (12) now prove the uncompleted equation

    partial_w H=b0*H+D_op H+Q.                             (13)

This derivative follows the moving center. In particular the x/2
in b and the derivative of both exponentials in h_w are retained.
Since c_w=-t^2/(2w)-w/8, its derivative at fixed t is
t^2/(2w^2)-1/8. Direct division and substitution therefore give

    (partial_w c_w)/c_w=w/(2*d_w)-1/w,
    H=-2w*U,
    c_w*D_op H=(d_w/2)*integral_R [2U(t)-U(t+y)-U(t-y)]nu(dy).

The product rule for G=c_w*H proves (2), including the derivative
of the completion s(s-w)/(2w). The completion and its derivative
are bounded on the target and a surrounding compact real rectangle.
Moreover U=-H/(2w), so (10) supplies a common majorant for the
completed integral too, including every translated ordinate.
For example |U|<=A_0 and |U_tt|<=A_2 on 1/2<=w<=2; multiply
the resulting bound by the bounded d_w(t) on that rectangle.

Finally if G=G_t=0 at a proposed point, d_w(t)>0 implies U=U_t=0
there. Taylor's remainder gives |U(w,t+/-y)|<=A_2*y^2/2 for
|y|<=1; for |y|>1 use |U|<=A_0. In particular each individual
absolute integral is bounded by

    (A_2/2)*integral_(|y|<=1) M(y)dy
      +A_0*integral_(|y|>1) M(y)/y^2 dy <=(A_2/2+A_0)*m.

Each shifted term can therefore be integrated individually against
nu at that point. Both event equations are necessary for this bound:
U=0 removes the constant term and U_t=0 removes the linear term.
Setting the local G and U terms in (2) to zero proves (3). No event is assumed
to exist. The residual still involves off-event values of the
actual family and the signed Fourier correction Q, neither of
which has been signed in this argument. Curvature, nondegeneracy,
multiplicities, initialization and transport to other heights remain
independent gaps.

## Mathlib

Full matching coverage is unchecked and unknown. No formal verification
is claimed. Dominated convergence, Fubini, Taylor's integral remainder
and the elementary Laplace integral are the standard supporting tools.
For the conventional compensated generator on its test-function
domain, compare R. L. Schilling, *An Introduction to Levy and Feller
Processes*, [arXiv:1603.00251v2](https://arxiv.org/pdf/1603.00251v2),
Theorem 6.8/(6.8)--(6.10), pp. 39--41. The needed extension and all
interchanges here were proved directly in (5)--(12); no maximum
principle or positive-w semigroup was imported. This is a specialization
of known transforms, with no certified claim of originality.
