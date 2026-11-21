# Lemma 733: coherent power profile admitted by the increment envelope

## Hypotheses

Set F(0)=0 and F(x)=x+x^(9/10) for real x>0. For real x>=2 and
1<=h<=x, define

    I_F(x,h)=integral_0^x |F(y+h)-F(y)-h|^2 dy.

For each fixed real c>0 and x>e, define the entire comparison envelope

    V_c(x,h)=x h^2 [ (x^(1/6)/h)^(2/5)(log x)^c + E_c(x) ],
    E_c(x)=exp(-(log x)^(1/3)/(c(log log x)^(1/3))).

For integers N>=1 put

    J_N^F=inf_(a in C) sum_(j=1)^N |a j-F(j)|^2/[j(j+1)].

This is a declared smooth model, with no assertion of prime-power
support, an Euler product, a zeta interpretation, or compatibility with
the October external zero-free input. The functional is modeled on
L732's definition, but no conclusion of that lemma is assumed.

## Conclusion

For all x>=2 and 1<=h<=x,

    I_F(x,h) <= (81/80)h^2 x^(4/5)-(1/80)h^(14/5)
              <= (81/80)h^2 x^(4/5).                       (1)

For every fixed c>0,

    sup_(1<=h<=x) I_F(x,h)/V_c(x,h) -> 0  as x->infinity. (2)

In particular, for every fixed K>0, I_F(x,h)<=K V_c(x,h) uniformly
on this h-range beyond an onset depending only on c,K. This preserves
both positive terms of V_c, rather than asserting any cancellation.

The discrete complex-drift minimum is attained uniquely and obeys

    J_N^F=(5/324)N^(4/5)+O(1),  N->infinity.              (3)

Consequently J_N^F>=(5/648)N^(4/5) for all sufficiently large integers
N. Thus this increment envelope alone, even required uniformly over
all its indicated lengths with arbitrarily fixed positive constants,
does not force subpolynomial drift-optimized prefix energy for general
profiles. This is no impossibility theorem for arguments using more
arithmetic or analytic information, and no RH or actual-prime estimate.

## Proof

### Full integral, including its lower endpoint

Write b=9/10 and Delta(y,h)=(y+h)^b-y^b. This is nonnegative.
For fixed h>0, Delta is decreasing for y>0, because
b[(y+h)^(b-1)-y^(b-1)]<0. Its continuous value at y=0 is h^b.
It follows that Delta<=h^b on [0,h]. For y>=h, integration of
the decreasing derivative gives

    Delta(y,h)=integral_y^(y+h) b t^(b-1) dt
               <=b h y^(b-1).

Since h<=x, split the defining integral into [0,h] and [h,x]; the
second interval is empty when h=x. As F's linear part cancels exactly,

    I_F(x,h) <= h^(2b+1)+b^2 h^2 integral_h^x y^(2b-2)dy
              =h^(14/5)+(81/80)h^2(x^(4/5)-h^(4/5))
              =(81/80)h^2 x^(4/5)-(1/80)h^(14/5).

This proves (1) without an estimate that omits y near zero. The
increment at y=0 is finite; no singular derivative is used there.

### Comparison with the complete source envelope

Montgomery and Vaughan, *Multiplicative Number Theory III*, author-hosted
working PDF, Theorem 28.6, equation (28.36), printed p. 212, with proof
pp. 212--216 (PDF indices 219--223), states for actual psi, x>=2,h>=1,

    integral_0^x |psi(y+h)-psi(y)-h|^2 dy << V_c(x,h)

for an absolute c>0 and absolute implied constant:
https://personal.science.psu.edu/rcv4/Vol3/Vol3.pdf .
Only the sufficiently large x>e range of that displayed expression is
used here; E_c is not defined here for 2<=x<=e.
The statement and complete relevant proof were inspected in the prior
source assessment `drafts/literature/2026-11-03-prime-variance-prefix-multiscale-scope.md`.
This citation specifies the envelope being tested; it is not applied
as a theorem to F, and its prerequisite density estimates are not
mathematical inputs to this elementary model proof. The working PDF
is mutable; no claim about a pinned published edition is made.

Retain V_c exactly as defined. Both its terms are positive for x>e,
so (1) implies, uniformly in 1<=h<=x,

    I_F/V_c <= (81/80) x^(-1/5)/E_c(x).                 (4)

Put L=log x>1. If L^2 log L>=1000/c^3, then

    L^(1/3)/(c(log L)^(1/3)) <= L/10,
    x^(-1/5)/E_c(x) <= x^(-1/10).

The condition follows eventually for every fixed c>0, since
L^2 log L increases without bound for L>1. Formula (4) then proves
(2), including a uniform rate beyond this c-dependent onset. To get
the asserted bound with any K>0, also take x>=(81/(80K))^10.
All these onsets are independent of h. No term of V_c was removed
from the asserted comparison, and no estimate for actual psi follows
by replacing it with F. The proof uses the E_c summand to show that
even the full envelope permits this profile.

### Exact complex projection with the discrete weights

Let w_j=j/(j+1)>0 and t_j=j^(-1/10), both real. For a=1+z,

    |a j-F(j)|^2/[j(j+1)] = w_j |z-t_j|^2.

With the finite real sums

    A_N=sum_(j=1)^N w_j=N+1-H_(N+1),
    B_N=sum_(j=1)^N w_j t_j=sum_(j=1)^N j^(9/10)/(j+1),
    C_N=sum_(j=1)^N w_j t_j^2=sum_(j=1)^N j^(4/5)/(j+1),

where H_m=sum_(k=1)^m 1/k, expansion for arbitrary complex z gives

    sum w_j |z-t_j|^2
      = A_N |z-B_N/A_N|^2+C_N-B_N^2/A_N.                (5)

Indeed the cross term is -2B_N Re z, and A_N>0 for every N>=1.
Thus the unique complex minimizer is the real number
a_N=1+B_N/A_N, and the minimum is exactly C_N-B_N^2/A_N.
All finite endpoints, including j=1 and j=N, were retained. In
particular this is one drift for the full prefix, allowed to depend
on N, rather than separate drifts on separate blocks.

### The asymptotic coefficient survives that projection

For every fixed 0<p<1, monotonicity of t^(-p) gives

    integral_1^(N+1) t^(-p)dt <= sum_(j=1)^N j^(-p)
                              <=1+integral_1^N t^(-p)dt.

These imply sum_(j=1)^N j^(-p)=N^(1-p)/(1-p)+O(1): the
change between N^(1-p) and (N+1)^(1-p) is bounded. Also

    sum_(j=1)^N j^(-p)/(j+1) <= sum_(j>=1) j^(-1-p)<infinity,

with convergence by the integral test. Since w_j=1-1/(j+1), these
two facts, for p=1/10 and p=1/5 respectively, yield

    B_N=(10/9)N^(9/10)+O(1),
    C_N=(5/4)N^(4/5)+O(1).

Moreover A_N=N+O(log(N+1)) and N/2<=A_N<=N. Therefore

    1/A_N=1/N+O(log(N+1)/N^2),
    B_N^2/A_N=(100/81)N^(4/5)
               +O(N^(-1/10)+N^(-1/5)log(N+1))
              =(100/81)N^(4/5)+O(1).

Substitute into (5). The leading difference is positive:

    5/4-100/81=(405-400)/324=5/324.

This proves (3) and the eventual lower bound. There is no numerical
fit, interchange of infinite sums, or assumed choice a=1 in this
argument. The strictly positive coefficient measures precisely the
power-mode component left after the optimal scalar projection.

### Separate bounded audit (2026-11-03, step 244)

The preceding argument was replayed with all finite endpoints. For an
explicit check of its O(1) remainder, the displayed integral bounds give

    -1/(1-p) <= sum_(j=1)^N j^(-p)-N^(1-p)/(1-p) <= 0,
    0 <= sum_(j=1)^N j^(-p)/(j+1) <= 1+1/p.

The first upper bound follows from
1+integral_1^N t^(-p)dt=N^(1-p)/(1-p)-p/(1-p).
The second follows from the integral test for j^(-1-p).
Consequently, with B_0=(10/9)N^(9/10),

    0 <= B_0-B_N <= 109/9,
    |C_N-(5/4)N^(4/5)| <= 29/4.

Also N-A_N=H_(N+1)-1<=log(N+1), and A_N>=N/2 since
each w_j>=1/2. Hence the triangle inequality, B_N<=B_0 and
B_N>=0 give, for every integer N>=1,

    |B_N^2/A_N-B_0^2/N|
      <= (B_0^2-B_N^2)/A_N+B_0^2(1/A_N-1/N)
      <= (4360/81)N^(-1/10)
         +(200/81)N^(-1/5)log(N+1).

For N>=1, log(N+1)<=log N+log 2<=5N^(1/5)+1
<=6N^(1/5), using log u<=u for u>=1. Therefore

    |J_N^F-(5/324)N^(4/5)|
      <=29/4+4360/81+1200/81
       =24589/324 <76.                                  (6)

In particular the stated lower bound holds whenever
N^(4/5)>=49248/5, for example for every integer
N>=ceil((49248/5)^(5/4)).
This deliberately coarse effective onset is only a verification of
the existing asymptotic, not an actual-prime estimate. At N=1 the
unique drift gives J_1^F=0, as (5) requires; the lower bound was only
asserted eventually.

The c-dependent comparison onset was also checked independently:
cubing the nonnegative inequality
L^(1/3)/(c(log L)^(1/3))<=L/10, for L>1, is exactly
L^2 log L>=1000/c^3. Combining it with
x>=(81/(80K))^10, x>e, proves the uniform K comparison.
There is no uniform-in-c or uniform-in-K onset claim. The case h=x
has an empty second integral and the value at y=0 is h^(9/10),
so neither endpoint uses a singular derivative. The coefficient and
all claimed quantifiers survive the audit. No change to the empty
mathematical-input row in the DAG is needed: L732 remains functional
context, and the source citation only specifies the comparison.

### Qualification and relevance

The allowed polynomial N^(4/5) is far above an N^(o(1)) upper
threshold, but this statement is about F only. It does not assert
that the smooth model obeys the finite divisor identities defining
the actual triangular family, any zero theorem of L732, or the
registered October input. Nor does it control an actual-family
anchor, complementary tail, cross-scale covariance or Xi sign.
Additional conditions could exclude F. The diagnostic ends here;
reopening this envelope-only inference requires a specified stronger
input. Its local advance is an informative obstruction to that
inference, not progress beyond the cited zero-free results.

## Mathlib

Full matching diagnostic not checked; availability unknown. Finite
complex least squares, integral comparison and power integration are
supporting facts, proved in the form needed above. No matching theorem
name or absence claim is asserted. The cited prime-variance theorem
serves only to fix the comparison envelope, and is not formally
verified here.
