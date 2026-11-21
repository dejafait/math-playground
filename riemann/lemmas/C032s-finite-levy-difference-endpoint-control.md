# Corollary C032s: finite Levy-difference mass and endpoint signs

## Hypotheses

Use exactly C032j's actual-zero normalization and fixed-v1 preprint
qualifications. In particular Z+ counts positive-ordinate nontrivial
zeta zeros with multiplicity, z_rho=gamma_rho-i*delta_rho,
|delta_rho|<1/2, and

    H(u)=sum_(rho in Z+) exp(-u*z_rho^2),
    H_sigma(t)=H(t/(1+4*sigma*t))/sqrt(1+4*sigma*t),
    ell_sigma(t)=H_sigma(t)/t.

The fixed half-variances are sigma=1,2. Retain the cited counting,
finite-zero and heat inputs: every zero through height 100 is real in
the z coordinate, the first ordinate lies in (14,15), and
sum_(gamma>100) gamma^(-2)<1. Use the separately controlled j=0,1
heat-sum errors in the proof of Proposition B.1 cited below. These
are external preprint inputs, including the cited finite verification;
their source-wide correctness and zero data are not independently
verified here. RH and positivity of p_sigma are not hypotheses.

Set

    D(t)=ell_2(t)-ell_1(t),
    K(u)=sqrt(u)*H(u),
    u_sigma(t)=t/(1+4*sigma*t).

## Conclusion

D is a real continuous function on (0,infinity), with

    D(t)=t^(-1/2)/(2*sqrt(pi))+O(log(1/t))  as t decreases to 0,
    integral_0^infinity |D(t)| dt < infinity.

D(t)>0 for 0<t<=1/9996 and for every t>=1/192. Consequently
ell_1-ell_2 is not globally nonnegative and cannot be the proposed
positive Levy difference. More precisely, the effective small-time
estimate is

    K'(u)<-381/(40000*u),             0<u<=1/10000,
    D(t)>(381/40000)*t^(-3/2)*log((1+8*t)/(1+4*t))>0,
                                      0<t<=1/9996.

Thus the only remaining t interval for the global sign is
(1/9996,1/192). The explicit absolute counting-error estimate used
below does not close this interval; that failure is not a negative
value of D. This endpoint proof alone leaves the sign incomplete.

Finite absolute mass is settled for the actual difference, but
the forward direction still requires a global sign proof. No
compound-Poisson comparison, signed positive output, full cancellation
in C032q, unsmoothed realization or actual-Xi all-degree positivity
is concluded. If D is later proved nonnegative everywhere, its total
mass will be strictly positive and finite by the conclusions above.

## Proof

### Imported estimates and the precise specialization

C032j supplies the exact Gaussian transform, using Suvrit Sra,
*Some positivity properties of Riemann Xi under smoothing*,
[2611.00345v1, 11 November 2026](https://hexagonmath.org/pdf/2611.00345v1),
Proposition 3.1, printed pp.5-6, proof in C.1, p.21. Its variance
is 2*sigma. We use that identity without rederiving Gaussian smoothing.

For the heat estimates use Sra, *On some positivity properties of
the Riemann Xi function*,
[2610.00584v1, 20 October 2026](https://hexagonmath.org/pdf/2610.00584v1),
Proposition B.1 and its complete proof, printed p.17. Put

    A=1/(8*sqrt(pi)), c=gamma_E+2*log(4*pi),
    I(u)=(1/(2*pi))*integral_0^infinity
                     exp(-u*y^2)*log(y/(2*pi)) dy
        =A*u^(-1/2)*(log(1/u)-c).

The source proof bounds the counting error for derivative order j by
O(u^(-j)*log(1/u)), and the complex-displacement error by
O(u^(1/2-j)*log(1/u)). For j=0,1 this means, with L(u)=log(1/u)
and u sufficiently small,

    H(u)=I(u)+r_0(u),       |r_0(u)|<=C_0*L(u),
    H'(u)=I'(u)+r_1(u),     |r_1(u)|<=C_1*u^(-1)*L(u).       (1)

These are separate estimates from the source proof. In particular
(1) does not arise by differentiating an O remainder. The j=1 main
integral is I' because differentiation of the Gaussian integral is
dominated on every compact positive u interval, including at y=0
where the logarithm is integrable. The published derivative equivalents
alone would not suffice for the cancellation below.

For the counting and tail bounds use the same preprint, Section 2.1,
(2.1)-(2.3),
printed p.3: the reciprocal-square sum and finite-zero inputs stated
above. Lemma 2.1, printed pp.3-4, supplies local absolute convergence
of H and its derivatives. Conjugate symmetry makes H real. The
source results are imported; only the missing two-width comparison
and its endpoint control are derived here. Assessment1552 covers
these inputs and this specialization; no originality is certified.

### Cancellation at zero and rejection of the reverse ordering

By differentiating sqrt(u)*I(u) exactly and using both errors in (1),

    K'(u)=H(u)/(2*sqrt(u))+sqrt(u)*H'(u)
         =-A/u+R(u),
    |R(u)|<=C*u^(-1/2)*log(1/u)                              (2)

for sufficiently small u. Since sqrt(u)*log(1/u) tends to zero,
the leading term in (2) has a strict negative sign near zero.

The Gaussian identity gives exactly

    ell_sigma(t)=t^(-3/2)*K(u_sigma(t)),
    D(t)=t^(-3/2)*integral_(u_2(t))^(u_1(t)) -K'(u) du.       (3)

Here 0<u_2<u_1 and

    u_1-u_2=4*t^2/((1+4*t)*(1+8*t)),
    log(u_1/u_2)=log((1+8*t)/(1+4*t)).

For small t, throughout the interval in (3), t/2<=u<=t;
thus u^(-1/2)*log(1/u)<=C'*t^(-1/2)*log(1/t), with an
absolute constant C'. Its length is at most 4*t^2. Integration
of (2), with this common bound for its error, therefore yields

    D(t)=A*t^(-3/2)*log((1+8*t)/(1+4*t))+O(log(1/t))
        =4*A*t^(-1/2)+O(log(1/t)).                           (4)

The last step uses log((1+8*t)/(1+4*t))=4*t+O(t^2);
the resulting O(t^(1/2)) is absorbed by the displayed error.
Since 4*A=1/(2*sqrt(pi)) and sqrt(t)*log(1/t) tends to zero,
(4) proves the claimed strict sign near zero. It also supplies
an integrable majorant C''*(t^(-1/2)+log(1/t)) there. This
proves zero-endpoint absolute integrability without subtracting
two uncontrolled heat-sum remainders. The reverse difference is
strictly negative on this interval, which stops that ordering.

### Effective small-time sign from the assessed counting input

This makes the existential small-time threshold explicit under the
same inputs; it neither assumes the
remaining sign nor independently verifies the preprint. Its counting
inequality is imported from the cited fixed-v1 source (2.1), printed
p.3, with the source's explanation in Appendix B.1, printed p.17:

    |N(y)-M(y)|<=E(y):=4+log(y+2)/8, y>=0,
    M(y)=y/(2*pi)*(log(y/(2*pi))-1), M(0)=0.

Here N counts all positive-ordinate zeros with multiplicity. The source
uses Bellotti and Wong (2025), Theorem 1.1, as published. We import
this already assessed consequence, without reproving that counting
theorem. Its (2.2) also gives

    sum_(gamma>100) gamma^(-2)
        <=2*(log(100)+1)/100<3/25.                         (8)

The last elementary inequality uses log(100)<5. For example,
e>8/3 follows from its power series, and (8/3)^5>100.

For 0<u<=1 put L=log(1/u) and define the entire function

    f_u(z)=(1/2-u*z^2)*exp(-u*z^2),
    S(u)=sqrt(u)*K'(u)=sum_rho Re(f_u(z_rho)),
    S_0(u)=sum_rho f_u(gamma_rho).

Absolute local convergence justifies these equalities and the
separations below. The counting main integral is

    integral_0^infinity f_u(y) dM(y)=I(u)/2+u*I'(u)
                                  =-A/sqrt(u).

Stieltjes integration by parts gives

    |S_0(u)+A/sqrt(u)|
       <=integral_0^infinity |f_u'(y)|*E(y) dy.             (9)

The endpoint terms vanish: N(0)=M(0)=0, while at infinity the
Gaussian times N-M tends to zero. Put x=sqrt(u)*y. Then

    |f_u'(y)| dy=w(x) dx,
    w(x)=2*x*|x^2-3/2|*exp(-x^2),
    log(y+2)<=L/2+log(x+2)<L/2+1+x/2.

The last bound uses u<=1 and
log(x+2)=log(2)+log(1+x/2)<=log(2)+x/2<1+x/2. The real function
(1/2-x^2)*exp(-x^2) decreases from 1/2 to -exp(-3/2), then
increases to zero. Thus

    integral_0^infinity w(x) dx=1/2+2*exp(-3/2)<1,
    integral_0^infinity x*w(x) dx
      <=integral_0^infinity (3*x^2+2*x^4)*exp(-x^2) dx
       =3*sqrt(pi)/2<3.

Here e^3>(8/3)^3>16 proves exp(-3/2)<1/4; pi<4 gives the
second strict bound. Applying these to (9) yields

    |S_0(u)+A/sqrt(u)|<69/16+L/16.                        (10)

We next bound the actual complex-displacement error separately.
All terms with gamma<=100 have delta=0. For gamma>100, the segment
z=gamma-i*v, |v|<=1/2, satisfies |z|^2<=(101/100)*gamma^2.
Direct differentiation, with primes now denoting z derivatives, gives

    f_u''(z)=u*(-3+12*u*z^2-4*u^2*z^4)*exp(-u*z^2).

Writing x=u*gamma^2, throughout that segment

    |f_u''(z)|<=u*exp(u/4)*exp(-x)*(3+13*x+5*x^2).

Since f_u'(gamma) is real, the first-order Taylor term
-i*delta*f_u'(gamma) has zero real part. The integral Taylor remainder
therefore gives

    |Re(f_u(gamma-i*delta))-f_u(gamma)|
      <=(u/8)*exp(u/4)*exp(-x)*(3+13*x+5*x^2).             (11)

This estimate uses |delta|^2/2<=1/8, not differentiation of a big-O
term. For n=1,2,3 the maximum of x^n*exp(-x) on x>=0 is
n^n*exp(-n), by its derivative. Using e>8/3 and exp(u/4)<4/3,
multiplication of (11) by gamma^2=x/u gives the uniform bound

    gamma^2*|Re(f_u(gamma-i*delta))-f_u(gamma)|
      <(1/6)*(9/8+117/16+3645/512)
       =7965/3072<3.

The exponential bound follows from exp(v)<1/(1-v) for 0<v<1,
applied at v=1/4. Summation with (8) now proves

    |S(u)-S_0(u)|<9/25, 0<u<=1.                          (12)

Combining (10) and (12), with C=1869/400=69/16+9/25, gives

    S(u)<-A/sqrt(u)+C+log(1/u)/16, 0<u<=1.               (13)

The function sqrt(u)*(C+log(1/u)/16) is increasing on (0,1],
since its derivative is
u^(-1/2)*((C+log(1/u)/16)/2-1/16)>0. Consequently, for
0<u<=1/10000, log(10000)<10 and A>1/16 imply

    u*K'(u)<-A+sqrt(u)*(C+log(1/u)/16)
       <-1/16+(1/100)*(79/16+9/25)
        =-381/40000.                                    (14)

If 0<t<=1/9996, then u_1(t)<=1/10000 and 0<u_2(t)<u_1(t).
Integrate the strict bound -K'(u)>381/(40000*u) in (3). This
proves the explicit positive lower bound for D in the conclusion.

For clarity, (13) cannot finish the intermediate sign test. On
[1/1008,1/1004], its right side is positive: these u are greater
than 1/1024, so A/sqrt(u)<4 (using pi>1), whereas C>4 and
log(1/u)>0. For t=1/1000 the integration interval in (3) is
exactly [1/1008,1/1004]. Thus this upper bound on K' gives a
negative lower bound on D there, not the required nonnegative one.
This proves only nonclosure of this absolute-error estimate; it is
neither a counterexample to K'<0 nor a wrong sign of the actual D.
No failure of all possible counting arguments is claimed.

### Finite absolute mass at infinity

For t>=1 and sigma=1,2, u_sigma(t) belongs to [1/9,1/4].
Local convergence makes K continuous and bounded on this compact
interval. If M_K is its finite maximum absolute value, (3) or the
preceding exact difference identity gives

    |D(t)|<=2*M_K*t^(-3/2), t>=1.

This bound is integrable. Continuity controls every remaining
compact t interval away from zero; together with (4) it proves
integral |D|<infinity. No unsmoothed large-time asymptotic is used
at u_sigma(t), which tends to a finite positive time.

### Positive sign for t>=1/192

It suffices to prove K'(u)<0 on [1/200,1/4]. Let q be the square
of the first ordinate, so 196<q<225, and write

    lambda_rho=z_rho^2,
    sqrt(u)*K'(u)=H(u)/2+u*H'(u)
                =sum_rho (1/2-u*lambda_rho)*exp(-u*lambda_rho).

Every gamma<=100 has delta=0 and gamma>14. For u>=1/200,
each of these real summands is negative. Selecting one occurrence
of the first zero and discarding the others gives an upper bound

    -(u*q-1/2)*exp(-u*q)<=-(12/25)*exp(-u*q)                 (5)

for their sum. This works with any multiplicity.

For gamma>100, put a=Re(lambda)=gamma^2-delta^2. The strip and
q<225 imply

    a-q>=(3/4)*gamma^2,      |lambda|<=2*gamma^2.

Hence the absolute value of its summand, after division by exp(-u*q),
is at most

    (2*u*gamma^2+1/2)*exp(-(3/4)*u*gamma^2).                 (6)

Write x=u*gamma^2. Since u>=1/200 and gamma>100, x>50 and
gamma^2=x/u<=200*x. Multiplying (6) by gamma^2 therefore bounds it by

    200*x*(2*x+1/2)*exp(-3*x/4)
      <=500*x^2*exp(-3*x/4)
      <=1,250,000*exp(-75/2)<1/100.                         (7)

The middle inequality follows because x^2*exp(-3*x/4) decreases
for x>=50 (its logarithmic derivative is 2/x-3/4<0).
For the last inequality, e>2 gives exp(75/2)>2^37, and
2^37=137,438,953,472>125,000,000. These exact inequalities
require no floating-point calculation.

Sum (7) against gamma^(-2). The imported sum is less than one,
so the entire high-zero contribution has absolute value less than
(1/100)*exp(-u*q). Combining with (5), with absolute convergence
justifying this separation, yields

    sqrt(u)*K'(u)<-(47/100)*exp(-u*q)<0.

In particular this holds on the required u interval. If t>=1/192,
then u_2(t)>=1/200 and u_1(t)<1/4. The interval in (3) has positive
length and its integrand is strictly positive. Therefore D(t)>0.

The effective small-time section permits t_0=1/9996<1/192. This
proves all stated conclusions and leaves precisely the intervening
sign problem unresolved. Neither the sign of K' on
(1/10000,1/200) nor the remaining signs of its integrals in (3)
are asserted. A future failure of the sufficient pointwise K' test
would not by itself
refute the ordered-difference inequality. ∎

### Critical audit1558 — 18 November 2026

The complete endpoint proof passed a separate mathematical audit
under assessment1556, retaining all fixed-v1 and finite-zero
qualifications. The Gaussian identity in Proposition 3.1 and its
Appendix C.1 proof were checked directly: the two translates cancel
the factor 1/2, the variance is 2*sigma, and the resulting identity
is exactly (3). The counting conventions and bounds (2.1)-(2.3),
Appendix B.1, and the full Proposition B.1 proof were also checked
in the cited October v1. In particular that proof provides separate
errors for j=0 and j=1 relative to their Gaussian main integrals;
the derivative equivalent alone is not the input used here.

Substitution in K' cancels the logarithmic main terms and leaves
-A/u. The combined error is O(u^(-1/2)*log(1/u)). For t<=1/8,
the integration segment in (3) lies in [t/2,t] and has length at
most 4*t^2. Multiplication by t^(-3/2) therefore gives the stated
O(log(1/t)) error, rather than a nonintegrable error from subtracting
two separate heat remainders. The leading coefficient 4*A and the
integrable zero-endpoint majorant in (4) are correct.

The effective small-time calculation was checked independently:
the variation and first weighted variation bounds yield 69/16+L/16;
the complex Taylor remainder has the factor delta^2/2<=1/8.
The polynomial in its second derivative is exactly
u*(-3+12*u*z^2-4*u^2*z^4). Its three scalar maxima give
7965/3072<3 after multiplication by gamma^2. With the imported
tail below 3/25 this gives the error below 9/25. Thus (13)-(14),
including the strict margin 381/40000 and monotonicity down to
u=0, are valid. Stieltjes boundary terms vanish at both ends;
multiplicities and endpoint conventions do not change the estimates.
The nonclosure example t=1/1000 remains a failure of this bound,
not a negative value of D.

For the other endpoint, retaining one occurrence of the first zero
costs at least (12/25)*exp(-u*q). All other zeros through 100 give
nonpositive contributions. For gamma>100, the bound a-q>=3*gamma^2/4
and gamma^2<=200*x give (7), whose exact exponential comparison is
strictly below 1/100. Summation uses the reciprocal-square tail,
so the resulting margin 47/100 is valid with any multiplicities.
The conditions u_1<=1/10000 and u_2>=1/200 translate exactly to
t<=1/9996 and t>=1/192, respectively, including equality.

Finally, for t>=1 both transformed times lie in [1/9,1/4].
Uniform local absolute convergence makes K bounded there, giving
the integrable t^(-3/2) bound. No large-u asymptotic is applied at
the finite limiting transformed times. Thus continuity, finite
absolute mass, both endpoint signs and the recorded envelope stop
are accepted under the cited inputs. No new lemma, numerical
certificate or stronger source-wide verification is claimed.

## Mathlib

Full matching coverage has not been checked and remains unknown.
No Mathlib theorem is used as a substitute for the fixed-v1 heat,
counting or finite-zero inputs. Supporting integration and real
analysis APIs were not assessed for this informal specialization.
