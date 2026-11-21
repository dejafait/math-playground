# Lemma 985: Vaughan bulk slow-phase and fixed-order envelope loss

## Hypotheses

Let n>=2 be an integer, Lambda the actual von Mangoldt function,
including all prime powers, and

    K_n(u)=(n-1)^(-1)*sum_(k=2)^n L_(k-1)^(1)(u),
    B_n=sum_(exp(n)<m<=exp(2*n)) Lambda(m)*K_n(log m)/m
                              -integral_n^(2*n) K_n(u)du.

Exclude the left endpoint and include the right endpoint fully.
Consider only this procedure: finite Laguerre connection, fixed-order
real Bessel asymptotics in the bulk, Tao's arbitrary-weight Vaughan
inequality, the first/second derivative tests below, and one Cauchy
expansion of Type II, estimating its correlations in absolute value.
Retain the continuum compensator and additive remainder, bounding
them separately when no signed comparison is supplied. Assume no RH,
zero simplicity, PNT error estimate, arbitrary-coefficient derivative
test, or differentiation of an asymptotic remainder.

## Conclusion

The leading phase has dyadic Type I scale T comparable to 1 and
Type II differenced scale T comparable to h/n, h=|log(s_2/s_1)|<=log 2.
The cited derivative bounds, capped by the trivial bound, give only
the summation length. In fact the undifferenced unweighted phases
lie in an arc of width at most log 2 and their sums have size
comparable to their number of terms. This says nothing about the
sign of the compensated Mangoldt sum.

The exact average has leading envelope exp(u/2)*O(n^(-3/2)).
Fixed M=1 gives additive error O(exp(u/2)*n^(-5/2)); its separately
estimated contribution to B_n is O(exp(n)*n^(-3/2)). A complete
elementary absolute bound is

    |B_n|<=C*(exp(n)*n^(-1/2)+n),       n>=2.             (1)

Vaughan with these derivative tests gives no exponential saving,
and its direct bound is weaker by polynomial factors. These
majorants have exponential rate 1; the required threshold allows
every positive rate epsilon. Thus this specified estimate chain
does not pay the target. There is no lower bound here for B_n or
its actual remainder, or impossibility claim about centered methods.

Step243, 10 November 2026: REPRODUCTION, an elementary specialization
and scoped negative loss test, not a new prime estimate beyond the
checked sources, payment of L984(H), or an RH candidate. L981/L982/L984
are context, not mathematical inputs to this calculation.

## Proof

### Imported tools and their applicability

Import [NIST DLMF18.18.18](https://dlmf.nist.gov/18.18.E18).
At degree n-1, alpha=1, beta=2, its coefficients (1)_j/j! equal 1.
Removing the degree-zero term gives the exact identity

    K_n(u)=[L_(n-1)^(2)(u)-1]/(n-1).                    (2)

Import [DLMF18.15.17-20](https://dlmf.nist.gov/18.15.E19), at
degree n-1, alpha=2 and fixed M=1, and the fixed-order real-positive
Bessel asymptotic [DLMF10.17.2-3](https://dlmf.nist.gov/10.17).
Their specialization, amplitude and errors are given below; no
general asymptotic theorem is reproved. We use fixed-order O bounds,
not the first-neglected-term assertion at a possibly inadmissible
truncation. If the sharper real bounds in 10.17(iii) are used instead,
their separate truncation conditions must also be imposed.

Import T. Tao, *Every odd number greater than 1 is the sum of at
most five primes*, [arXiv1201.6656v4, Lemma4.11, pp23-24](https://arxiv.org/pdf/1201.6656v4#page=23).
For F supported in (V,U*V^2), U,V>1, this states

    |sum_m Lambda(m)F(m)|<=T_I+T_II,
    T_I=sum_(d<=UV) |sum_s (log s+c_d log d)F(ds)|,
    T_II=|sum_(d>U,w>V) mu(d)g(w)F(dw)|,
    |c_d|<=1,  g(w)=sum_(b|w,b>V) Lambda(b)-(log w)/2,
    |g(w)|<=(log w)/2.                                 (3)

This is the arbitrary-weight inequality, not the source's separate
additive-frequency theorem. Import Tao,
[*254A Notes5*, 7 February2015, Proposition6](https://terrytao.wordpress.com/2015/02/07/254a-notes-5-bounding-exponential-sums-and-the-zeta-function/):
on an interval of length at most N>=1, bounds
T/(A*N^j)<=|f^(j)|<=A*T/N^j, j=1,2, A>=1, and
0<T<=N/(2A), give normalized unweighted sum O(A^3/T).
Finally import O. Robert,
[*On van der Corput's k-th derivative test for exponential sums*,
2015 author preprint, Theorem1, p5](https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf#page=5):
lambda<=|f''|<=a*lambda, lambda>0, a fixed, gives
O_a(M*sqrt(lambda)+lambda^(-1/2)) on M integer terms.
Here both tests use exp(2*pi*i*f). Translate integer intervals for
Robert; empty and one-term intervals use trivial bounds. Import
these tools without reproof. The work is the n-dependent phase,
coefficient and loss comparison, justified by the pre-existing
SPECIALIZE assessment review241, separately approved in step242.

### Exact bulk amplitude and additive error

Put

    nu=4*n+2, t=u/nu,
    xi(t)=[sqrt(t-t^2)+arcsin(sqrt(t))]/2,
    z=nu*xi(t), Phi(u)=z-5*pi/4,
    D(t)=4*t^(5/4)*(1-t)^(1/4).

For u in [n,2n] and n>=2, t belongs to [1/5,1/2]. This compact
range avoids 0 and the turning point 1, is covered by the source's
fixed-delta uniformity, and makes xi bounded above and below by
positive constants. Thus z>0 and z is comparable to n. Writing
b_0(t)=B_0(xi(t)), the cited M=1 formula becomes

    L_(n-1)^(2)(u)=exp(u/2)/D(t) *
      [sqrt(xi)*J_2(z)+b_0(t)/(nu*sqrt(xi))*J_3(z)
                           +sqrt(xi)*envJ_2(z)*O(nu^(-1))]. (4)

DLMF18.15.20 specializes explicitly to

    b_0(t)=-1/2 * [-15/8+xi(t)*sqrt((1-t)/t)*
                     (15/8+t/(4*(1-t))+5*t^2/(24*(1-t)^2))].

This and its derivatives are bounded on [1/5,1/2]. The fixed-order
Bessel estimates give envJ_2(z)=O(z^(-1/2)),
J_2(z)=sqrt(2/(pi*z))*(cos Phi+O(1/z)) and
J_3(z)=sqrt(2/(pi*z))*(sin Phi+O(1/z)). The J_3 phase is
Phi-pi/2, so this sine sign is positive. These are additive
estimates, including at cosine zeros. Define

    H_n(u)=exp(u/2)*sqrt(2/(pi*nu))/[(n-1)*D(t)],
    b(t)=b_0(t)/xi(t).

Equations (2)-(4) give

    K_n(u)=H_n(u)*[cos Phi(u)+b(t)/nu*sin Phi(u)]
                          -1/(n-1)+E_n(u),
    |E_n(u)|<=C*exp(u/2)*n^(-5/2).                     (5)

The explicit correction in (4) is retained. Other terms of the
same order are included in E_n: (5) claims neither a sharp
correction coefficient nor a relative error. H_n is comparable to
exp(u/2)*n^(-3/2). The asymptotic initially holds after a finite
onset. For each earlier n the difference defining E_n is continuous
on compact [n,2n]; enlarging C over this finite set proves (5) for
all n>=2. This is not an effective-onset claim.

After division by m=exp(u), the explicit oscillatory terms are
smooth amplitudes times exp(+-i*Phi(log m)). On X<=m<=2X within
the bulk their supremum plus total variation is
O(n^(-3/2)*X^(-1/2)), and the b/nu correction is smaller by O(1/n).
Indeed each amplitude is m^(-1/2)*a_n(log(m)/nu), with a_n and
its first t derivative O(n^(-3/2)). Its m derivative is therefore
O(n^(-3/2)*m^(-3/2)). Only explicit functions were differentiated.

### Type I: bounded phase scale

Write p=Phi', q=Phi'', r=Phi'''. Direct differentiation gives

    p(u)=sqrt(nu-u)/(2*sqrt(u)),
    q(u)=-nu/[4*u^(3/2)*sqrt(nu-u)],
    r(u)=nu*(3*nu-4*u)/[8*u^(5/2)*(nu-u)^(3/2)].        (6)

Throughout [n,2n], the loose uniform bounds are

    1/2<=p<=1, 1/(8n)<=-q<=1/n, 0<r<=4/n^2.           (7)

For p use 2<=nu/u<=4+2/n<=5. For q use 4n<=nu<=5n,
n<=u<=2n, 2n<=nu-u<=4n: its lower bound is at least
1/(2^(5/2)*n)>1/(8n), its upper at most 5/(4*sqrt(2)*n)<1/n.
For r, 3nu-4u>=4n+6>0; the same ranges bound it above by
55/(8*2^(3/2)*n^2)<4/n^2. These verify the signs as well as sizes.

For fixed d>0, s in [S,2S] and log(ds) in the bulk, set
f(s)=Phi(log(ds))/(2*pi). Then

    f'(s)=p(log(ds))/(2*pi*s),
    f''(s)=[q(log(ds))-p(log(ds))]/(2*pi*s^2).          (8)

Their magnitudes are comparable to 1/S and 1/S^2, with fixed
constants. Tao applies with N comparable to S, T comparable to 1
and fixed A for sufficiently large S, giving O(S). Robert uses
lambda comparable to S^(-2), giving O(1+S). Neither saves against
the trivial bound on a full dyadic interval. Short intervals and
bounded S can use the actual number of terms.

Moreover any interval J inside [S,2S] staying in the bulk has
phase range at most log 2, by p<=1. Rotating by the midpoint
phase makes every term's real part at least cos((log 2)/2)>0:

    |sum_(s integer in J) exp(i*Phi(log(ds)))|
                    >=cos((log 2)/2)*#(J intersect Z).  (9)

This rules out a power saving from these unweighted phases on
dyadic intervals. It does not rule out outer coefficient cancellation
or cancellation with the continuum density.

### Type II: coefficients and all correlation ranges

On a dyadic factor rectangle r in [R,2R], s in [S,2S], R,S>=1,
restrict products to (X,Y] within the bulk. Keep |a_r|<=1 and
|b_s|<=L and put

    T=sum_r a_r sum_s b_s*1_(X<rs<=Y)*exp(i*Phi(log(rs))).

Cauchy in r bounds |T|^2 by C*R times the nonnegative expression

    sum_(s_1,s_2) b_(s_1)*conj(b_(s_2)) *
      sum_(r in I_(s_1,s_2))
         exp(i*[Phi(log(r*s_1))-Phi(log(r*s_2))]),       (10)

where I intersects [R,2R] with both product intervals. It is an
interval, possibly empty, with the same full integer endpoints.
The specified procedure then bounds its pair terms in absolute
value. No unweighted test is applied directly to arbitrary a_r,b_s.

For s_2>s_1 set h=log(s_2/s_1) in (0,log 2], u=log(r*s_1),
Delta(r)=Phi(u)-Phi(u+h), Delta_p=p(u)-p(u+h), and
Delta_q=q(u)-q(u+h). Both arguments and the segment between
them stay in [n,2n] on I. Integrating (7) gives
h/(8n)<=Delta_p<=h/n and -4h/n^2<=Delta_q<0. Hence

    Delta'(r)=Delta_p/r,
    Delta''(r)=(Delta_q-Delta_p)/r^2,
    h/(8*n*r^2)<=|Delta''(r)|<=3*h/(n*r^2).            (11)

The curvature is nonzero of fixed sign; no sign-change hypothesis
is hidden. For Delta/(2*pi), Tao has T comparable to h/n,
N comparable to R and fixed A, giving O(R*n/h) whenever its size
hypothesis holds. It holds for sufficiently large R; otherwise
use the trivial bound rather than invoke the proposition. Robert gives

    O(sqrt(h/n)+R*sqrt(n/h)),                          (12)

whose inverse-curvature term exceeds R. Both therefore offer
only O(R) after capping trivially. Shortening the common interval
cannot remove this inverse-curvature cost; use its actual number
of terms instead. Diagonal pairs s_1=s_2 have identically zero
phase and inner sum equal to their term count. For s_2=s_1+j,
1<=j<=S, h is comparable to j/S; the cost in (12) is
R*sqrt(n*S/j), including the near diagonal explicitly.

Thus absolute estimation in (10) gives

    |T|^2<=C*R^2*sum_(s_1,s_2)|b_(s_1)*b_(s_2)|
           <=C*R^2*S^2*L^2,
    |T|<=C*R*S*L.                                    (13)

The diagonal alone costs at most C*R^2*S*L^2; the unpaid
off-diagonal mass causes the loss. Reversing Cauchy interchanges
R,S with the same problem. Also Delta'<=h/(n*r) bounds its phase
variation on [R,2R] by h*log(2)/n. This does not sign the
coefficient-weighted correlation sum before absolute values.

### Vaughan support, amplitudes and compensation

For n>=3 partition the block into consecutive (X,Y] with
e^n<=X<Y<=min(2X,e^(2n)). Every integer belongs to exactly one
interval. Choose U=V=(4X)^(1/3) separately on each. Then V<X,
U*V^2=4X>Y strictly, and UV=(4X)^(2/3)<X because X>=e^3>16.
Thus (3) includes the last integer and all prime powers. Its
Lambda_(<=V) term vanishes by support, not an estimate. The
single n=2 can be included by enlarging a finite constant.

First use F(m)=1_(X<m<=Z)*exp(+-i*Phi(log m)), X<=Z<=Y.
All Type I inner ranges may be split dyadically; (8) supplies
no improvement. Partial summation handles their logarithm factor.
Directly |log s+c_d log d|<=log(ds)<=log(2X), and
# {s:X<ds<=Z}<=X/d+1<=2X/d for d<X. Therefore

    T_I<=C*X*log(2X)*sum_(d<=UV)1/d
        <=C*X*(log(2X))^2.                            (14)

For Type II, d<=2X/V<X, |g(w)|<=log(2X)/2, and the same
counting/harmonic bound gives T_II<=C*X*(log(2X))^2.
The coefficient-aware (10)-(13) gives no exponential improvement.
These bounds hold for every partial endpoint Z. Finite partial
summation against (5)'s explicit amplitudes multiplies them by
at most C*n^(-3/2)*X^(-1/2). This gives O(sqrt(X)*n^(1/2))
per block, and O(e^n*n^(1/2)) after summing the geometric sequence
of sqrt(X). Boundary terms are included in supremum plus variation;
there is no derivative of a cutoff, omitted endpoint or half-weight.

A stronger polynomial factor is available just by the triangle
inequality. Define the linear compensated functional

    C_n[F]=sum_(e^n<m<=e^(2n)) Lambda(m)*F(log m)/m
                                       -integral_n^(2n) F(u)du.

Use 0<=Lambda(m)<=log m<=2n and the elementary integral
comparison sum_(m<=e^(2n)) m^(-1/2)<=C*e^n. Equation (5) yields

    |C_n[H_n*cos Phi+H_n*b/nu*sin Phi]|
                     <=C*(e^n*n^(-1/2)+e^n*n^(-3/2)),
    |C_n[E_n]|<=C*(e^n*n^(-3/2)+e^n*n^(-5/2)).         (15)

The integrals use integral_n^(2n) exp(u/2)du<=2e^n.
These are separate upper bounds, with no assertion of compensation
cancellation. The degree-zero correction is exactly

    C_n[-1/(n-1)]
       =-[sum_(e^n<m<=e^(2n)) Lambda(m)/m-n]/(n-1).

The harmonic sum gives sum Lambda(m)/m<=C*n^2, so this is O(n).
Together the three pieces prove (1), including the finite prefix,
all prime powers and the real endpoint conventions.

Near X comparable to exp(2n), amplitude times a trivial X-term
sum is sqrt(X) times a polynomial. Reaching exp(epsilon*n)
would require essentially an X^(-1/2)*exp(epsilon*n) relative
saving, up to powers of n; these derivative tests give no power
saving. Also (15)'s remainder majorant is exp(n) times a negative
power of n. At general fixed M, the cited Laguerre remainder,
after division by n-1, has envelope
O_M(exp(u/2)*n^(-2M-1/2)), whose separate contribution has
majorant O_M(exp(n)*n^(1/2-2M)). A sufficiently large fixed
Bessel truncation makes its error no larger. No derivative or
growing-order estimate for a remainder is being used.

For any fixed A and epsilon<1, exp(n)*n^(-A)/exp(epsilon*n)
tends to infinity. The available majorants cannot imply the
every-epsilon threshold. This proves insufficiency of this estimate
chain, not a lower bound for B_n or its error, or failure of the
desired inequality. The centered functional could have cancellations
discarded in (3), (10) and (15); exploiting them needs different input.

### Relevance and stopping scope

Only one interior range of L984(H) was tested. Its complementary
ranges and L030-L032/C032a actual-Xi positivity and L966/L968 forcing
remain open. Stop this uncentered first/second derivative mechanism.
Reopening needs a materially new signed compensation or arithmetic
correlation estimate addressing the displayed loss, not more fixed
asymptotic terms or repetitions of these derivative tests. Preserve
the independent automatic-average, lobe-sign and criterion-only
stops. No complete RH candidate is asserted.

## Mathlib

Full matching Mathlib coverage for this compensated n-dependent
block, coefficient-aware loss comparison and cited uniform
asymptotics is unchecked and unknown. Primary mathematical inputs
are cited above. Supporting finite summation or differentiation
theorems would not themselves supply the arithmetic estimate.
No formalization or absence-of-coverage claim is made.
