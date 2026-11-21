# Corollary C030t: a conditional subdiagonal bound from real-scale comparison

## Hypotheses

Use C030r's finite conjugate-rate family: integers m>=1, n>=2m,
n>=4 and 2<=d<=floor(n/2); positive real a_l,r; real b_l; and

    A=sum_l |b_l|, M=sum_l b_l^2, x>0, x*A<=1/4.

All rates are fixed as the evaluation variable t varies. For
1<=i<d let beta_(i,b)(t) and beta_(i,0)(t) be C030r's positive
square-root determinant ratios, with the reference retaining all real
rates and setting every b_l=0. Include repeated real rates, zero phases,
n=2m, every real contrast and the closed phase boundary.

For the conditional form fix 0<c<=1 and impose the real-reference
condition at this rank and endpoint:

    beta_(i,0)(t)>=c*beta_(i,0)(x),
                         for every 3*x/4<=t<=x.       (H)

Audited C030u supplies (H) with c=1 throughout this family. The conditional
proof below retains c to identify its precise use. Condition (H) is a
relative comparison within one fixed real family, not a positive uniform
lower bound on beta_(i,0) across families.

Use C030q's already audited individual response estimate and floor,
with K=4224/961. These are uniform over the above finite family.

## Conclusion

Under the additional hypothesis (H),

    |beta_(i,b)(x)-beta_(i,0)(x)|
       <= [512*K/(31*sqrt(31)*c)]*x*M
       < (14/c)*x*M,                                 (1)

where the strict inequality is intended only when M>0. When M=0
both coefficients agree. Applying C030u with the same fixed real-rate
list gives the full finite phase comparison without an additional
unproved hypothesis:

    |beta_(i,b)(x)-beta_(i,0)(x)|
       <= [512*K/(31*sqrt(31))]*x*M < 14*x*M, M>0.    (1a)

Attempt1232 supplied the conditional reduction. Independent conceptual
audit1238, under unchanged assessment1236/review1237, passes (2)-(9)
and the c=1 application. This is REPRODUCTION of the local argument
and assembly of the audited inputs, not a claim of originality or of
progress beyond the sources checked. A finite evolution norm, actual-Xi
supply, degree/time and signed-complement control, theta signing,
graph realization and all-degree positivity remain open. There is no
RH candidate here.

## Proof

### Known determinant identities and differentiation scope

Write D_(j,b) for C030r's signed derivative-Hankel determinant and
Z_(j,b) for its probability-Haar orbital integral. For 0<t<=x put

    F_j(t)=Z_(j,b)(t)/Z_(j,0)(t),
    u_j(t)=log F_j(t),
    v(t)=log(beta_(i,b)(t)/beta_(i,0)(t)).

The pair-swap symmetry in C030q gives F_j as a real cosine average
under its own positive real-reference law. Its floor and the elementary
upper bound cos<=1 imply

    31/32<=F_j(t)<=1,
    |u_j'(t)|=|G_(j,b)(t)-G_(j,0)(t)|<=K*t*M.        (2)

Each rank has its own normalizer. No common tilted law across ranks
is used. Compact domination of the finite orbital integrals and
C030r's positive determinants give all derivatives used here, including
at the closed endpoint by local continuation of strict positivity.

C030r(2) expresses D_(j,b)/D_(j,0) as a constant rate-product ratio
to power j, times F_j. The rate factors therefore cancel from the
adjacent determinant ratio, giving the exact equality

    v=(u_(i+1)+u_(i-1))/2-u_i.                      (3)

For completeness, the differential identity required below is the
standard Desnanot--Jacobi identity for a derivative-Hankel determinant.
If tau_j=det[f^(p+q)]_(0<=p,q<j) and tau_0=1, it says

    tau_i*tau_i''-(tau_i')^2=tau_(i+1)*tau_(i-1).

To check its specialization, differentiation by rows leaves only the
last row: all other terms have a repeated row. Differentiating that
minor by columns likewise leaves only its last column. The resulting
minors have respectively one or both last indices raised from i-1 to
i. Desnanot--Jacobi applied to the size i+1 Hankel matrix then gives
the displayed identity; for i=1 it is f*f''-(f')^2=tau_2 directly.
For D_j=(-1)^(j*(j-1)/2)*tau_j, the adjacent signs yield

    (log D_(i,b))''=-beta_(i,b)^2.

Subtracting the real-reference identity cancels the constant
rate-product factor and gives

    u_i''=-beta_(i,0)^2*(exp(2*v)-1).                (4)

This uses only algebraic differentiation and nonzero determinants.
It is not differentiation of the inequality in (2), and no variance
positivity for a complex law is asserted. The same identity is used
in C030s, but none of that corollary's bounds or multiplicity assumptions
is needed here.

The real-rate finite-convolution identity underlying C030r is imported
there from S. Sra, *On some positivity properties of the Riemann Xi
function*, [author-v3, 2 November 2026](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf),
Lemma C.6/(C.10), pp23-25; the derivative-Hankel framework and coefficient
identities are in C.5/(C.9), pp22-23, and C.9/(C.18)-(C.23), pp27-28.
Assessment1228 inspected those passages. Their real-rate theorem is
used through C030r's justified conjugate-rate specialization, not
assumed to supply (H). The short sign and differentiation check above
specifies the use of the standard identity, not a reproof of the source
theorem. C030q is the separate established response input; its full
source qualifications remain in its canonical proof.

### A short interval on which the response has one sign

If M=0 the phases all vanish and (1) follows immediately. Suppose M>0.
By (2)-(3),

    |v'(t)|<=2*K*t*M,
    |v(t)|<=log(32/31).                              (5)

For the second inequality, both sqrt(F_(i+1)*F_(i-1)) and F_i
belong to [31/32,1]. Also F_j(t) tends to 1 as t decreases to zero:
each finite orbital integrand tends uniformly to 1 with its fixed
rates. Equation (3) thus gives v(t)->0. Integrating the first inequality
in (5) from a positive lower endpoint and then letting that endpoint
decrease to zero gives

    |v(x)|<=K*x^2*M.                                 (6)

If v(x)=0 the coefficients at x agree. Otherwise put w=|v(x)|>0 and

    h=w/(4*K*x*M).

By (6), 0<h<=x/4. For x-h<=t<=x, (5) implies

    |v(t)-v(x)|<=2*K*x*M*h=w/2.

Consequently v has the same sign as v(x) on this entire interval
and |v(t)|>=w/2. If that sign is positive, exp(2*v(t))-1>=w.
If it is negative, then

    1-exp(2*v(t))>=1-exp(-w)
       =integral_0^w exp(-s)ds
       >=w*exp(-w)>=(31/32)*w,                       (7)

where (5) bounds w. Thus in both cases (4) has constant sign there
and, using (H),

    |u_i''(t)|>=(31/32)*c^2*beta_(i,0)(x)^2*w.       (8)

Only the real-reference comparison (H) is used for this lower bound.

### Integration pays the absolute coefficient difference

Because the sign in (8) is constant, there is no cancellation when
integrating it. Applying the first-derivative estimate (2) at both
endpoints gives

    (31/32)*c^2*beta_(i,0)(x)^2*w*h
       <=|u_i'(x)-u_i'(x-h)|
       <=K*M*(2*x-h)<=2*K*x*M.

Insert the value of h and take the nonnegative square root:

    beta_(i,0)(x)*w <= [16*K/(sqrt(31)*c)]*x*M.       (9)

Finally |exp(v(x))-1|<=exp(|v(x)|)*|v(x)|. Equations (5) and (9)
give the first inequality in (1). The constant is less than 14/c:
K<9/2, and 512/(31*sqrt(31))<3 because
512^2=262144<268119=9*31^3. Their product is less than 27/2<14.
This bound is deliberately not optimized.

All arguments are finite and pointwise. They preserve fixed rates
through the interval, use only t<=x within the allowed phase window,
and retain separate rank normalizers. Zero-phase cases, coincident
rates and n=2m require no limit of singular expressions. Rank i=1
uses F_0=1 and u_0=0; i+1<=d is within C030r's determinant range.
No positive lower bound on beta_(i,0)(x) is divided out in the estimate.

### Application of the real-reference input

C030u uses the convolution with the fixed list
(a_1,a_1,...,a_m,a_m,r,...,r), with exactly the same n, m and positive
real rates as the reference here. Its determinant signs and positive
square-root normalization agree with C030r's. Its audited conclusion
is beta_(i,0)(t)>=beta_(i,0)(x) for every 0<t<=x. It therefore supplies
(H) with the single constant c=1, including both endpoints, repeated
rates, n=2m and all real-rate contrasts. No reference lower floor across
families or uniform small/large-time onset is required. Substitution
in (1) proves (1a). C030u's monotonicity proof is used as an established
local input, not reproved here.

### Independent conceptual audit1238

17 November 2026. This audit verifies the local reduction and the
preceding application relative to the established C030q/r/u inputs.
It is not a new audit of their external source theorems. Reused source
coverage1236/review1237 and1228/1229; in particular Sra's Theorem C.9
norm conclusion, with its additional degree condition, is not an input.
The real determinant statement was refreshed there as arXiv2611.02944v1,
Lemma C.6/(C.10), pp23-24; the author-v3 citation above is retained.

For clarity write rho=R_b/R_0>0 for the rate-product ratio in C030r.
The exact determinant quotient is rho^j*F_j(t), since the factorial
and t-power factors agree for both lists. The exponent of rho in the
beta quotient is ((i+1)+(i-1))/2-i=0. The remaining logarithm is (3),
and log D_(i,b)-log D_(i,0)=i*log rho+u_i. All rates, including rho,
remain fixed under differentiation. C030q's cosine representation and
positive floor give (2) with each rank's own real normalizer. They also
give F_j(0)=1 by compact domination for this fixed family; no uniform
family limit is invoked.

Here is the full minor check behind (4). In the Hankel matrix with
indices 0,...,i, let S={0,...,i-2} (empty when i=1). The determinant
tau_i has row and column set S union {i-1}. Its derivative is the minor
with row set S union {i} and column set S union {i-1}: differentiation
of any earlier row gives a repeated row. Differentiating this expression
by columns gives tau_i'' with both sets S union {i}. Symmetry identifies
the other cross minor with tau_i'. Desnanot--Jacobi gives the displayed
identity, with the central minor tau_(i-1) and empty determinant 1.
The adjacent sign exponent is i*(i+1)/2+(i-1)*(i-2)/2=i*i-i+1,
which is odd. Division by the positive D_i^2 gives the minus sign in
(4). No second-derivative estimate is inferred from (2).

Equation (3) and the individual bounds in (2) give |v'|<=2*K*t*M.
Both its numerator sqrt(F_(i+1)*F_(i-1)) and denominator F_i lie in
[31/32,1], proving the logarithmic bound in (5). Integration down to
zero is valid because v tends to zero and the majorant is integrable;
it gives (6) with constant K, not 2*K. For M>0 and w>0 the stated h
therefore obeys 0<h<=x/4, so (H) applies on the whole selected interval.
Integrating |v'| between any t there and x gives at most w/2. Thus the
sign never changes or reaches zero. For positive v, exp(2v)-1>=w;
for negative v, 1-exp(2v)>=1-exp(-w)>=w*exp(-w)>=31*w/32.
This checks both branches of (7) and the noncancelling sign in (8).

The fundamental theorem of calculus now equates the absolute integral
of u_i'' with |u_i'(x)-u_i'(x-h)|. The endpoint upper bound is
K*M*(2*x-h). Substitution of h yields

    beta_(i,0)(x)^2*w^2 <= 256*K^2*x^2*M^2/(31*c^2).

Taking the positive square root proves (9). The conversion back to beta
costs at most exp(w)<=32/31, giving exactly (1). The arithmetic checks
are 2*4224=8448<8649=9*961 and
512^2=262144<268119=9*31^3. Thus its constant is less than 27/(2*c),
hence less than 14/c. This is an exact inequality, not a numerical test.

If M=0 the two rate lists and coefficients coincide. If M>0 but v(x)=0,
the coefficient difference is zero and no division by w is made.
Rank i=1 uses F_0=1, u_0=0 and the empty determinant. The largest used
rank i+1<=d<=floor(n/2) is available in C030r. Repeated rates never
produce a rate-difference denominator; n=2m simply removes the r entries.
At x*A=1/4 strict determinant positivity supplies local differentiability,
while every estimate is applied only at t<=x inside the phase window.
All constants are independent of m,n,d and the rates. Positivity of an
individual beta permits its logarithm but is never used as a uniform
lower bound. These checks complete the audit and justify (1a).

The full finite phase target is now established by this assembly. The
joint-moment route parked in1232 remains unpaid and is not an input;
C030s is not an input either. No evolution estimate or transfer to the
actual-Xi signed form follows without further work.

## Mathlib

Full matching coverage of (1), (1a), condition (H), and the supplied orbital
response bound is unchecked; no absence claim is made. Supporting
mathematics includes the Desnanot--Jacobi identity, differentiation of
finite determinants, the fundamental theorem of calculus and elementary
exponential inequalities. Exact supporting Mathlib theorem names were
not checked, and no formal verification is claimed.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
