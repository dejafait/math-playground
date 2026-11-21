# Corollary 708a: bounded signed spatial growth on two inner angular arcs

## Hypotheses

Fix one actual L703 profile before n varies, with precisely its cutoff
and width choices. Retain the complete L666 family and rational angular
continuation, with

    n=12q+3, q>=1, M=n/3, d=5/4, x=-d, R=11/8,
    U=121/64, A=27/10, Y=9/20, t_j=j/n,
    a(y)=x+i*y, y_m=A*(m+1/2+e_m)/n, -2q<=m<2q,
    Z_n={x} union {a(y_m): -2q<=m<2q},
    W_a(u)=(x/a)*product_(j=1)^(n-1)
        [(x-t_j*u)/(a-t_j*u)]*[(U*u-t_j*a)/(U*u-t_j*x)],
    T_M(v)=sum_(k=0)^(M-1)v^k,
    G_n(u,z)=R^(-1)*sum_(a in Z_n) W_a(u)*T_M(a*z/R).

Keep all original unit masses, the anchor W_x=1, the j=0 factor,
inverse angular variable, both finite endpoints, the signed interior
and every one of the M moments. The profile is neither truncated nor
allowed to depend on n. In particular |e_m|<=1/8 and e_m->0 at both
ends. Use normalized full-circle angular measure mu and put

    s=65/64, r_out=33/32, rho=sqrt(2824/3025), v=s*rho,
    S_(n,r)(u)=max_(|z|<=r)|G_n(u,z)|,
    b_n(u)=log(S_(n,s)(u)/S_(n,1)(u)),
    B_sp(n)=integral_(|u|=1/2) b_n(u) dmu(u),
    H(z)=1/(R+d*z).

L706 gives finite continuous coefficients and nonzero slices on this
angular circle. Thus the positive maxima and finite-n logarithmic
ratios are well-defined, including degree drops. All logarithms are
natural. No cancellation budget relative to an absolute envelope is
assumed.

## Conclusion

There exist disjoint fixed proper closed arcs I_+, I_- of |u|=1/2,
centered respectively at 1/2 and -1/2, with positive measures and
mu(I_+ union I_-)<1, and constants c,C,C_-,N>0 such that, for all
allowed n>=N,

    sup_(u in I_+, |z|<=s)|G_n(u,z)-H(z)|<=C*exp(-c*n),  (1)
    b_n(u)=log(32/27)+O(exp(-c*n)),       u in I_+,       (2)
    0<=b_n(u)<=C_-,                      u in I_-.       (3)

The error in (2) is uniform. On I_+ the exact finite decomposition

    G_n=F_n-T_n,
    F_n(u,z)=sum_a W_a(u)/(R-a*z),
    T_n(u,z)=sum_a W_a(u)*(a*z/R)^M/(R-a*z)

has both F_n-H exponentially small on |z|<=s and an exponentially
small remainder relative to the actual S_(n,1). The constants, arcs
and onset are existential and may depend on the fixed profile.

Writing I=I_+ union I_-, the full-circle consequence is only

    integral_I b_n dmu=O(1),
    limsup_(n=12q+3 -> infinity) B_sp(n)/n
                               <=(1-mu(I))*log(s)/3.    (4)

Consequently the sublinear B_sp target is equivalent here to its
still-unproved complementary estimate integral_(I^c)b_n dmu=o(n).
The right side of (4) is strictly positive. No sublinear full-circle
bound or positive lower limiting obstruction is claimed. In
particular, L708's exponential absolute-envelope cancellation can hold
on a fixed tilted subarc of I_+ simultaneously with (2).

This is a local specialization of the established signed estimates
and standard analytic tools. It pays two arc contributions to the
approved target, without certified originality, a global Jensen
payment, or an RH candidate. Amplitude, full charge, H/support, Xi
realization and actual-Xi all-degree signs remain independent. This
corollary has not received a separate critical audit.

## Proof

### 1. Scope, source import and radius margins

Reuse the invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-spatial-doubling-growth-attempt-scope.md`,
approved in step 159, and its saved primary-source comparison. L707
already supplies the degree-independent growth-to-defect transfer.
This attempt estimates its actual signed growth observable locally;
it does not repeat the failed interpolation or absolute-envelope
budgets. The global target and the family have not changed.

Import Hadamard's three-circles theorem from K. Ramachandra,
*On the Mean-Value and Omega-Theorems for the Riemann Zeta-Function*,
TIFR Lectures 85 (1995),
[Theorem 1.5.2 and proof, printed p.27, PDF p.37](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr85.pdf#page=37).
For a function analytic near a closed annulus with radii r_1<r_2<r_3,
its maxima satisfy M_2<=M_1^theta*M_3^(1-theta), where
theta=log(r_3/r_2)/log(r_3/r_1). Zeros are permitted. The usual
maximum-modulus principle identifies circle and disk maxima here.
The identically zero case is immediate. No general theorem is reproved.
The changed spatial radius requires the explicit family bounds below;
the unit-disk statements of L706 and L708 alone do not state them.

For every retained node, |a|^2<353/200 and hence |a|/R<=rho.
Exact arithmetic gives

    (r_out*rho)^2=3177/3200<1,
    (s*rho)^2=59657/61952<1,
    R-d*r_out=11/128>0,       R-d*s=27/256>0.             (5)

Thus all resolvents in the hypotheses, and H, are analytic on a
neighborhood of the closed disk of radius r_out. Bounds for the
finite sums T_M on this disk are independent of M apart from their
weights. One must not just enlarge L708's earlier disk centered at
z=1/2: (s+1/2)^2=9409/4096 exceeds the limiting endpoint-pole
distance squared 6481/2824. The concentric disks in (5) avoid that
geometric issue entirely.

### 2. An arbitrarily small outer exponential rate near u=1/2

Audited L708 (3) supplies a fixed closed angular neighborhood V_0 of
u_0=1/2 and c_0,C_0>0, with

    max_(|z|<=1)|G_n(u,z)-H(z)|<=C_0*exp(-c_0*n),
                                                     u in V_0. (6)

Shrink V_0 if necessary so that Re u>0. Its exact factorization,
including j=0, is

    lambda_t=d+t*u, a_t=Re lambda_t,
    r_t=t*(d+t*u)/(U*u+d*t),
    Q_t(u,y)=r_t+(1-r_t)*lambda_t/(lambda_t-i*y),
    W_(a(y))(u)=product_(j=0)^(n-1) Q_(t_j)(u,y).         (7)

The notation a_t in (7) is a positive real number, not a spatial node.
All parameter denominators stay nonzero on a sufficiently small
fixed neighborhood of u_0, and a_t>=d. For real y, direct triangle
inequalities give

    |Q_t(u,y)|<=z_t(u):=|r_t|+|1-r_t|*|lambda_t|/a_t.    (8)

At u_0 the numbers lambda_t are positive real and 0<=r_t<1 for
0<=t<=1, so z_t(u_0)=1. Joint continuity in (u,t) and compactness
of [0,1] imply that for any fixed delta>0 there is a fixed closed
neighborhood V_+ within V_0 on which z_t(u)<=exp(delta) for all t.
In particular, on V_+ every actual weight satisfies

    |W_a(u)|<=exp(delta*n).                              (9)

This bound holds for the complete original finite family and does not
replace its signed sum. The same c_0 in (6) remains valid on V_+.
No rate is lost merely by shrinking the angular neighborhood.

Let tau_s=-log(s*rho)/3>0 and choose, before n,

    0<delta<=min(c_0/8,tau_s/4).                          (10)

With that single choice of V_+, (5), (9) and the exact M-term
geometric sum imply

    max_(|z|<=r_out)|G_n(u,z)|
       <=M*exp(delta*n)/[R*(1-r_out*rho)],
    max_(|z|<=r_out)|G_n(u,z)-H(z)|
       <=C_1*n*exp(delta*n).                             (11)

The H contribution is bounded by 128/11. The constants in (6) and
(11) are uniform in u in V_+ and all sufficiently large allowed n.
In particular (11) retains every moment rather than estimating a
chosen low-degree truncation.

### 3. Continue the signed limit and pay its relative finite remainder

For fixed n,u, apply the cited three-circles theorem to G_n-H at
spatial radii 1,s,r_out. It is analytic by (5). The interpolation
weight satisfies

    theta=log(66/65)/log(33/32)>1/3,

because (66/65)^3=287496/274625>33/32. Combining (6) and (11)
gives a bound C_2*n^(1-theta)*exp(-eta*n), where

    eta=theta*c_0-(1-theta)*delta
       >=c_0*(theta-(1-theta)/8)>c_0/4.

Absorb the fixed power of n by decreasing the rate to c_0/8.
This proves (1) uniformly on V_+, and hence on any fixed positive
closed arc I_+ around 1/2 contained in V_+. The zero-function case
of the comparison would give the assertion directly.

For completeness keep the exact F_n-T_n identity rather than treating
an absolute error as relative. From (5), (9), M=n/3 and (10),

    max_(|z|<=s)|T_n(u,z)|
       <=n/[3*R*(1-v)]*exp[-(tau_s-delta)*n]
       <=C_3*exp(-tau_s*n/2).                            (12)

The first inequality is for all n; the second absorbs its polynomial
factor at one uniform onset. Therefore F_n-H=(G_n-H)+T_n is also
exponentially small on this disk. Every signed endpoint and interior
term is still present in F_n, G_n and T_n.

For 0<=r<=s, max_(|z|<=r)|H(z)|=1/(R-d*r), attained at z=-r.
Uniform approximation in (1), using both directions of the triangle
inequality for maxima, yields

    S_(n,1)(u)=8+O(exp(-c*n)),
    S_(n,s)(u)=256/27+O(exp(-c*n)).                       (13)

In particular S_(n,1)>=4 eventually on the whole chosen arc. Division
of (12) by this actual lower bound proves the relative-remainder
claim. Taking logarithms in (13) is legitimate uniformly, since both
maxima stay bounded away from zero, and proves (2). This uses no lower
bound for A_n/S_(n,1), the absolute-weight quantity stopped by L708.

For the compatibility statement, L708 Section 7 has the strict
derivative d/dtheta Im Omega((1/2)exp(i*theta))>0 at theta=0.
Its construction therefore permits the positive tilt to be chosen
inside any sufficiently small neighborhood of 1/2, including the
interior of I_+. Reuse its ensuing fixed negative ordinate and
uniform finite-product estimate on a smaller closed tilted arc.
For A_n=R^(-1)*sum_a|W_a| this gives S_(n,1)<=A_n*exp(-epsilon*n)
there, with some epsilon>0 and one enlarged onset. The profile is
unchanged. This makes no assertion that an earlier preselected
obstruction arc must lie in the newly shrunken neighborhood.

### 4. Retain both signed endpoints on the opposite enlarged disk

Reuse L706's fixed neighborhood V_- of -1/2 and its factorization

    W_(a(y))(u)=C_n(u)*Fhat_n(u,y),
    Fhat_n(u,y)=a(y)^(-1)*product_(j=1)^(n-1)
                                  (U*u-t_j*a(y))/(a(y)-t_j*u),
    C_n(u)=x*product_(j=1)^(n-1)(x-t_j*u)/(U*u-t_j*x).

Here Fhat_n is an endpoint normalization, distinct from the spatial
resolvent F_n above. The endpoint derivative, interior gap, and fixed
block limits in L706 Sections 2--4 do not involve the spatial radius.
Write p_sigma=(x+sigma*iY)/R. The two coefficients used there are
b_sigma(u)=zeta_sigma(u)/(1-zeta_sigma(u)), with
|zeta_sigma|<=exp(-A/8)<1; each b_sigma is continuous, bounded, and
bounded away from zero on the chosen compact V_-.

Here is the needed change in the spatial part of that proof. On
|z|<=s, every geometric factor has modulus at most 1/(1-v), and

    |T_M(a*z/R)-(1-a*z/R)^(-1)|<=v^M/(1-v).              (14)

For any fixed endpoint block index k, the actual nodes tend to their
respective virtual endpoint because e_m->0 at both ends. Thus (14)
converges uniformly to the corresponding resolvent. L706's remaining
endpoint blocks are dominated by exp[-A*(k+7/8)/12], now times the
fixed factor 1/(1-v). Its complete interior and anchor errors are
bounded by a constant times n*exp(-g*n/2)/(1-v), where g=Y/12.
Consequently the same finite-block argument, with both tails and the
interior paid, gives the enlarged-disk version of its signed shape:

    G_n(u,z)/N_n(u)
      =v_(+,n)(u)/(1-p_+*z)+v_(-,n)(u)/(1-p_-*z)+o(1),  (15)
    E_n(u)=max{|Fhat_n(u,Y)|,|Fhat_n(u,-Y)|},
    N_n(u)=C_n(u)*E_n(u)/R,
    v_(sigma,n)(u)=b_sigma(u)*Fhat_n(u,sigma*Y)/E_n(u).

The error is uniform for |z|<=s and for u on a fixed closed angular
arc I_- about -1/2 within V_-. On this arc C_n is finite and nonzero:
the only relevant possible common poles require j=121n/160, which is
impossible for odd n. The endpoint factors and E_n are nonzero by
L706's endpoint-band construction. No uniform analytic assertion
about C_n across its nearby moving poles is made.

The two coefficients in (15) are bounded, and their maximum modulus
is bounded below by min_(u,sigma)|b_sigma(u)|>0. The fixed matrix
of the two functions (1-p_sigma*z)^(-1) at z=0,1/2 is invertible
because p_+!=p_-. Hence at least one of these two values of the
main term in (15) is bounded away from zero. Absorbing its uniform
o(1) error, and using 1-v>0 for the upper bound, gives fixed
0<c_-<=C_*<infinity such that

    S_(n,1)(u)/|N_n(u)|>=c_-,
    S_(n,s)(u)/|N_n(u)|<=C_*,                 u in I_-.

The normalizing scalar cancels from the ratio. This proves (3) with
C_-=log(C_*/c_-), increasing C_* if needed. It retains two signed
endpoint coefficients and all M finite moments, including possible
spatial boundary zeros and actual degree drops.

### 5. Full-circle accounting and the remaining test

Choose the two arcs small enough that they are disjoint, their union
is proper, and they avoid a fixed neighborhood of u=i/2. The degree
bound in L707 (3), whose reciprocal-
polynomial maximum-modulus argument also covers constants, gives

    0<=b_n(u)<=(M-1)*log(s)                               (16)

on the entire angular circle. Nonzero slices and continuity from L706
justify all finite-n integrals. Integrating (2), (3) and (16) gives

    B_sp(n)<=mu(I_+)*log(32/27)+O(exp(-c*n))
             +mu(I_-)*C_-+(1-mu(I))*(M-1)*log(s).

This proves (4). The bounded nonnegative contribution on I proves
the stated equivalence with the complementary sublinear estimate.
There is no passage from a fixed paid arc to an unproved global
endpoint or anchor expansion. In particular the positive constant
log(32/27) in (2) contributes zero after division by n, and cannot
serve as a positive linear obstruction.

L707's transfer would turn a future full-circle B_sp=o(n) estimate
into J_sp=o(n). The three-circles/Poisson specialization L707 (1) and
the degree comparison (16) were checked in their displayed forms
for this application; this is not an audit of the rest of L707.
The unpaid complement and the independent downstream hypotheses
prevent any stronger conclusion here.

The exact auxiliary comparisons in (5) and in the interpolation
weight were checked by
`python3 scripts/one-sided-hankel/spatial-growth-signed-arcs-165.py`.
Its full certificate is
`scripts/one-sided-hankel/spatial-growth-signed-arcs-165.json`.
All nine checks pass, with actual and required rational bounds printed.
This certificate verifies only arithmetic, not the analytic estimates,
the existence of the arcs, the profile construction, or the full target.

## Mathlib

Full matching Mathlib coverage for this fixed-family two-arc conclusion,
its uniform signed limit, and the averaged B_sp target has not been
checked. No absence or formal verification is claimed. The cited
three-circles theorem and the L706/L708 inputs are informal mathematical
inputs with their existing source qualifications. This specialization
has not received a separate critical audit.
