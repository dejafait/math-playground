# Lemma 706: bounded spatial Jensen defect on a fixed inner angular arc

## Hypotheses

Fix one actual L703 profile e before n varies. Use L666's complete
unit-residue family, L657's K,Q and rational continuation, and write

    n=12q+3, q>=1, M=n/3, J=n-1, A=27/10,
    d=5/4, x=-d, R=11/8, U=121/64, Y=9/20=A/6,
    a(y)=x+i*y, y_m=A*(m+1/2+e_m)/n, -2q<=m<2q,
    t_j=j/n, T_M(v)=sum_(k=0)^(M-1) v^k,
    G_n(u,z)=R^(-1)*[T_M(x*z/R)
                         +sum_m W_(a(y_m))(u)*T_M(a(y_m)*z/R)].

The profile properties needed here are |e_m|<=1/8 and e_m->0 at
both ends, supplied by L703. The same profile is used for every n,u,z.
Keep the anchor, j=0 factor, inverse angular variable, both endpoints
and all M moments. No reflection of e is assumed. On |u|=1/2 put

    S_n(u)=max_(|z|=1)|G_n(u,z)|,
    m_n(u)=mean_(|z|=1) log|G_n(u,z)|,
    Delta_n(u)=log S_n(u)-m_n(u),
    J_sp(n)=integral_(|u|=1/2) Delta_n(u) dmu(u),

where all circle measures are normalized and logarithms are natural.
An integral over a subarc uses this full-circle measure, without
renormalizing that subarc. These definitions do not replace original D.

## Conclusion

Every spatial slice on |u|=1/2 is a nonzero polynomial; the displayed
means and J_sp(n) are finite. If nu_n(u) is its actual degree, then

    0<=Delta_n(u)<=nu_n(u)*log 2<=(M-1)*log 2.               (1)

There are a fixed proper closed arc I of |u|=1/2 centered at -1/2,
with 0<mu(I)<1, and finite C,N such that, for every allowed n>=N,

    sup_(u in I) Delta_n(u)<=C.                            (2)

The onset may depend on the fixed profile. No numerical arc width or
effective onset is asserted. In particular,

    integral_I Delta_n dmu=O(1),
    limsup_(n=12q+3 -> infinity) J_sp(n)/n
                              <=(1-mu(I))*log(2)/3.        (3)

For this same fixed profile, J_sp(n)=o(n) is therefore equivalent to
integral_(I^c) Delta_n dmu=o(n). That complementary estimate is NOT
proved. The required global threshold is zero; (3) still permits
positive linear loss. This is a paid intermediate contribution to
the approved defect target, not a full angular amplitude bound,
inner-charge compensation, H/support estimate or Xi realization.
The separate conceptual audit in Section 6 accepts (1)--(3) with
exactly these qualifications. It establishes no stronger estimate or
claim of originality beyond the inspected sources.

## Proof

### 1. Source scope, imports and the radius-1/2 interfaces

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-03-fixed-profile-spatial-jensen-defect.md`.
The bounded attempt concerns its exact J_sp target. L705 supplies the
strict negative-real endpoint modulus gap and endpoint-band derivative;
the work below extends the normalized signed shape to a positive-measure
arc and pays its spatial logarithm. It does not extrapolate an endpoint
expansion to the whole angular circle. L669's n-dependent profiles,
L683's generic degree cost, L698's different-radius amplitude bound and
the block-dual/clearing stops remain contrasts, not premises.

Import the polynomial root formula and coefficient bound from
F. Brunault and W. Zudilin, *Many Variations of Mahler Measures*,
ISBN 9781108794459,
[Propositions 1.4-1.5 and Lemma 1.6, pp.6-8](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf).
They use actual degree and leading coefficient and include zero and
circle roots. For absolute product-logarithm integrability import
Z. Issa and M. Lalin, *A generalization of a theorem of Boyd and Lawton*,
[arXiv:1203.5379v1, Remark 3.8 and Theorem 4.1/proof, p.7, s=1](https://arxiv.org/pdf/1203.5379v1).
For the boundary Poisson--Jensen inequality import
R. B. Ash and W. P. Novinger, *Complex Variables*,
[Theorem 4.8.3 and Lemma 4.8.4, printed pp.33-36](https://people.math.sc.edu/girardi/m7034/book/AshComplexVariablesWithHyperlinks.pdf#page=94),
with the kernel normalization in Corollary 4.7.4, printed p.27.
The ready assessment inspected the relevant boundary-zero cases.
These general theorems are not reproved. The usual maximum-modulus
principle, uniform Riemann integration of continuous functions on
compact parameter sets, and dominated convergence are used below.

L666's only possible finite angular poles are p_j=x*j/(U*n)
and a(y_m)/t_j. The second set has modulus at least d>1/2.
The first meets |u|=1/2 only if j=121n/160, impossible for odd n.
Thus every W_a and every coefficient of G_n is finite and continuous
on this angular circle. Some nonanchor W_a may be zero there; no
nonvanishing assertion about those individual weights is needed.

There are exactly M distinct spatial nodes. If every spatial
coefficient of a slice vanished, its M moment equations, tested
against the degree-(M-1) Lagrange polynomial equal to one at x/R
and zero at every other node, would give W_x=0. But W_x=1.
This proves nonzero slices even when some other W_a vanish, and
allows actual spatial degree drops.

The polynomial K_n(v/2,z) is nonzero, since Q_n(v/2)G_n(v/2,z)
is nonzero at every |v|=1 as a spatial polynomial. Its logarithm
is absolutely integrable on the product torus by the cited theorem.
Q_n(v/2) has no zeros there, so log|G_n| is absolutely integrable
as well. Fubini is applicable. For each n, S_n is continuous and
strictly positive on the compact angular circle, hence log S_n is
bounded. This proves all the stated finiteness claims. The root
formula also gives (1): each root factor satisfies
|z-alpha|<=2*max(1,|alpha|) on |z|=1; multiply using the actual
leading coefficient. The lower bound is the mean-versus-maximum
inequality. No growing-degree small-value theorem is assumed.

### 2. Remove the common angular factor before taking a neighborhood

Let u_0=-1/2 and define

    F_n(u,y)=a(y)^(-1)*product_(j=1)^J
                             (U*u-t_j*a(y))/(a(y)-t_j*u),
    C_n(u)=x*product_(j=1)^J(x-t_j*u)/(U*u-t_j*x).

L666's exact rational continuation reads

    W_(a(y))(u)=C_n(u)*F_n(u,y).                            (4)

In particular C_n(u)F_n(u,0)=1. The factor x/a(y) coming from
j=0 is retained. C_n can have dense moving poles in a neighborhood
of u_0 as n varies. We make no uniform estimate for it there.
Instead F_n has no denominator zeros for |u|<=3/5, |y|<=Y,
since |a(y)-t*u|>=d-3/5>0. At u_0 the numerators
U*u_0-t*a(y) are nonzero on the two closed bands
Y/2<=|y|<=Y, 0<=t<=1. Compactness therefore gives a fixed closed
disk V about u_0, contained in |u|<3/5, on which they stay uniformly
away from zero on these bands.

On the bands define the continuous function

    L(u,y)=integral_0^1 [-i*t/(U*u-t*a(y))
                                    -i/(a(y)-t*u)]dt.

Uniform Riemann comparison of the logarithmic derivative gives

    F'_n(u,y)/(n*F_n(u,y))=L(u,y)+O(1/n).                 (5)

Here the prime denotes y differentiation. The omitted j=0 term is
-i/(n*a(y)); the t derivatives of the two integrands are uniformly
bounded on the specified compact sets. This verifies the stated
uniform error without choosing a logarithm across a zero.

For r=1/2, L705 (8)--(13) give

    Re L(u_0,y)>1/6       for Y/2<=y<=Y,
    Re L(u_0,y)<-1/6      for -Y<=y<=-Y/2.                 (6)

The second statement follows from the even modulus at this real
u_0, not from any symmetry of the displacement profile. Shrink V
so that the limiting bounds are respectively >=1/8 and <=-1/8.
Then (5), for all sufficiently large n, gives respectively

    partial_y log|F_n(u,y)|>=n/12,
    partial_y log|F_n(u,y)|<=-n/12.                       (7)

All constants here are uniform in u in V.

### 3. A uniform signed-interior error, including numerator zeros

An estimate only on the two bands would not justify omitting their
complement. Put c=U/2 and g=Y/12. L705 (11), including continuity
at zero, implies for |y|<=Y/2 and sigma in {+1,-1},

    integral_0^1 f(u_0,y,t)dt
       -integral_0^1 f(u_0,sigma*Y,t)dt <=-g,
    f(u,y,t)=log|U*u-t*a(y)|-log|a(y)-t*u|.                (8)

Indeed the difference is Phi_(1/2)(|y|)-Phi_(1/2)(Y),
and Phi_(1/2)(Y)-Phi_(1/2)(|y|)>=(Y-|y|)/6. At y=0
the numerator has one integrable logarithmic zero in t.

To extend the upper bound uniformly, rather than differentiate near
that zero, use

    f_epsilon(u,y,t)=log(|U*u-t*a(y)|+epsilon)
                                             -log|a(y)-t*u|.

At u_0, |U*u_0-t*a(y)|>=|d*t-c|, so almost everywhere in t

    0<=f_epsilon(u_0,y,t)-f(u_0,y,t)
                                 <=log(1+epsilon/|d*t-c|).

The last function has integral tending to zero with epsilon. For
0<epsilon<=1 it is dominated by the integrable logarithm with
epsilon=1, so dominated convergence applies uniformly in y.
Choose a fixed epsilon>0 making this integral at most g/8.
Continuity on compact parameter sets, and a further shrinking of V,
then give, for all u in V, |y|<=Y/2 and both sigma,

    integral f_epsilon(u,y,t)dt
              -integral f(u,sigma*Y,t)dt <=-3*g/4.        (9)

The regularized integrand is continuous on the entire compact set;
the endpoint integrands are continuous because their numerators do
not vanish. Their Riemann sums converge uniformly. The prefactors
1/a(y) in F_n contribute bounded logarithms divided by n. As
f<=f_epsilon, (9) therefore implies, eventually and uniformly,

    |F_n(u,y)|/|F_n(u,sigma*Y)|<=exp(-g*n/2),
                       u in V, |y|<=Y/2.                 (10)

If a sampled numerator is zero, the left side is zero and the bound
still holds. Thus neither a transition through such a zero nor the
anchor is discarded. The common poles of C_n played no part in
this uniform comparison.

### 4. Both endpoint sums and all spatial moments

Set a_+=x+iY, a_-=x-iY, p_+=a_+/R, p_-=a_-/R and

    lambda_+(u)=L(u,Y), lambda_-(u)=-L(u,-Y),
    zeta_sigma(u)=exp(-A*lambda_sigma(u)),
    b_sigma(u)=zeta_sigma(u)/(1-zeta_sigma(u)).

Their real derivative bounds imply |zeta_sigma|<=exp(-A/8)<1.
On the compact disk V each b_sigma is continuous, bounded and
bounded away from zero: its exponential numerator never vanishes,
and its denominator never vanishes.

Index the positive and negative nodes from their respective outer
endpoints. Their positive magnitudes are exactly

    y_(n,k)^+=Y-A*(k+1)/n+A*e_(2q-1-k)/n,
    y_(n,k)^-=Y-A*(k+1)/n-A*e_(-2q+k)/n,
                                          0<=k<2q.        (11)

For every fixed k the profile hypothesis gives
n*(y_(n,k)^sigma-Y)->-A*(k+1). Integrating (5) along the
endpoint segment proves, uniformly in u in V,

    F_n(u,y_(n,k)^+)/F_n(u,Y)->zeta_+(u)^(k+1),
    F_n(u,-y_(n,k)^-)/F_n(u,-Y)->zeta_-(u)^(k+1).         (12)

These are separate limits; no conjugacy between the two finite sums
is imposed. Wherever y_(n,k)^sigma>=Y/2, (7) and |e_m|<=1/8 give

    |F_n(u,sigma*y_(n,k)^sigma)|/|F_n(u,sigma*Y)|
                                  <=exp[-A*(k+7/8)/12]. (13)

For the remaining nodes use (10). Their total normalized modulus
is at most n*exp(-g*n/2). Equations (12)--(13) justify summing a
fixed initial block, uniformly bounding its remaining geometric tail,
then letting the block size tend to infinity. No unbounded signed
sum or limiting profile has been substituted for the finite family.

All nodes, including the two virtual endpoints, obey

    |a|/R<=rho_*:=sqrt(d^2+Y^2)/R<1.

Consequently T_M(a*z/R) is bounded by 1/(1-rho_*) on |z|<=1.
For each fixed k in (11), it converges there uniformly to
(1-p_sigma*z)^(-1), because the exact geometric remainder is at
most rho_*^M/(1-rho_*) and the endpoint nodes converge. The same
summation argument, now with these spatial factors retained, gives

    sum_(k=0)^(2q-1) F_n(u,sigma*y_(n,k)^sigma)
                         *T_M(a(sigma*y_(n,k)^sigma)*z/R)
       =F_n(u,sigma*Y)*[b_sigma(u)/(1-p_sigma*z)+o(1)],   (14)

uniformly for u in V and |z|<=1. The two o(1) errors are absolute
after their respective endpoint normalizations. The anchor term is
also bounded by (10) after either endpoint normalization.

Let E_n(u)=max{|F_n(u,Y)|,|F_n(u,-Y)|}>0. On V where C_n is
finite and nonzero, (4) and (14) yield the exact-family asymptotic

    Gtilde_n(u,z):=R*G_n(u,z)/(C_n(u)*E_n(u))
       =v_(+,n)(u)/(1-p_+*z)+v_(-,n)(u)/(1-p_-*z)+o(1),
    v_(sigma,n)(u)=b_sigma(u)*F_n(u,sigma*Y)/E_n(u).       (15)

The error is uniform on the specified sets. Both coefficients are
uniformly bounded and at least one has modulus bounded below by
min_(u in V,sigma)|b_sigma(u)|>0. In particular this is a signed
two-term normalized shape, not a sum of separate absolute weights.
At all points of |u|=1/2, C_n is finite and nonzero by Section 1.

### 5. Pay the spatial logarithm uniformly on an angular arc

The two spatial functions in (15) are linearly independent. In fact
their values at z=0 and z=1/2 give the fixed invertible matrix

    [ 1                     1                    ]
    [ (1-p_+/2)^(-1)        (1-p_-/2)^(-1)        ].

Its determinant is nonzero since p_+!=p_-. Boundedness and the
coefficient lower bound in (15) therefore provide constants
0<c_0<=1<=C_0<infinity such that, for all sufficiently large n,

    sup_(|z|<=1)|Gtilde_n(u,z)|<=C_0,
    max{|Gtilde_n(u,0)|,|Gtilde_n(u,1/2)|}>=c_0,          (16)

uniformly for u in V on |u|=1/2. The o(1) error has been absorbed
by reducing c_0 and enlarging C_0. In particular these normalized
polynomials are nonzero. They are analytic on a neighborhood of the
closed spatial disk, so the cited Poisson--Jensen theorem applies.

If |Gtilde_n(u,0)|>=c_0, Jensen gives its spatial log mean at least
log c_0. Otherwise use the nonzero value at 1/2. The unit-disk
Poisson kernel there has mass one and minimum 1/3. Subtracting that
minimum and using log|Gtilde_n|<=log C_0 on the boundary gives

    log|Gtilde_n(u,1/2)|
       <=(1/3)*mean_z log|Gtilde_n(u,z)|+(2/3)*log C_0.

Hence in both cases, since c_0<=C_0,

    mean_z log|Gtilde_n(u,z)|>=3*log c_0-2*log C_0,
    log max_(|z|=1)|Gtilde_n(u,z)|-mean_z log|Gtilde_n(u,z)|
                                            <=3*log(C_0/c_0). (17)

Boundary zeros are included. No phase choice, exceptional spatial
set or continuity of Mahler measure in growing degree is used.

Choose any fixed proper closed arc I centered at u_0 and contained
in V on |u|=1/2, with positive angular length. The scalar normalizing
factor C_n(u)E_n(u)/R in (15) cancels exactly in the defect. Thus
(17) proves (2) for every u in I, including u_0. Integrate it over
I and use (1) on the complement to obtain

    0<=J_sp(n)<=mu(I)*C+(1-mu(I))*(n/3-1)*log 2.

This proves (3). Nonnegativity and the O(1) contribution on I prove
the stated equivalence with the complementary o(n) estimate.
They do not establish that remaining estimate or a positive lower
limit. No mathematical script or numerical evidence is used.

### 6. Separate conceptual audit — 3 November 2026, step 157

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-03-spatial-jensen-defect-arc-audit-scope.md`,
separately source-approved in step 156. This audit accepts (1)--(3).
No substantive error was found; the details below make explicit the
uniform bounds and the scope of this acceptance. This is verification
of the existing quantitative specialization, not a new source theorem
or a stronger mathematical result. The primary imports in Section 1
are reused with their previously inspected hypotheses and proof cases.

**Exact family and finite-n interfaces.** Direct division of L666's
products gives (4), including x/a from j=0. The numerator zeros of C_n
are x/t_j and have modulus greater than d; its possible poles on the
new angular circle would require j=121n/160. Since 121 and 160 are
coprime and n is odd, this is impossible. The denominators of F_n
are also nonzero there. Thus C_n is finite and nonzero at every
point used for the defect, without an n-uniform bound on C_n.
The positive and negative node sets are disjoint from the anchor:
their nearest possible ordinates have magnitude at least 3A/(8n).
Successive nonanchor ordinates are separated by at least 3A/(4n).
There are exactly 4q+1=M distinct nodes and exactly M available
moment equations. Anchor isolation by their Lagrange polynomial is
therefore valid. The nonzero rescaled K and nonvanishing Q on the
torus justify finite-n absolute integrability and Fubini. No uniform
integrability as n grows is inferred. The root bound uses actual
degree and leading coefficient, including degree drops and circle roots.

**Uniform neighborhood and numerator zeros.** The two closed y-bands
have no numerator zero at u_0, even at t=0. A single compact disk V
therefore works for both bands. Differentiation of F_n gives exactly
the two integrands of (5) and the additional term -i/(n*a(y)).
L705's radius-1/2 margin is 56497/300000>1/6. The negative-band
sign follows from evenness of the modulus at real u_0, independently
of any profile symmetry. Compact continuity and the uniform O(1/n)
Riemann error justify (6)--(7).

For the interior, the integral of log(1+epsilon/|dt-U/2|) tends to
zero and dominates the regularization error for every real y in the
required interval. Its single infinite point is a null set and its
logarithmic singularity is integrable. The order of choices matters:
first fix epsilon using that bound at u_0, then shrink V, then choose
n for the two uniform Riemann estimates. The unregularized endpoint
integrands have no zeros on this compact set. Consequently (9)--(10)
are upper estimates even at sampled interior numerator zeros; neither
a logarithmic derivative there nor a uniform bound on C_n is used.

**Both growing sums, including every spatial term.** The identity
n/6=2q+1/2 verifies both indexings in (11). The two instances of
e_m tending to zero give (12) separately, with first limiting weight
zeta_sigma, not 1. Integrating the logarithmic derivative on each
zero-free endpoint segment justifies the complex ratio, without a
global logarithm or a conjugacy assertion for the finite profile.
For a tail starting at any fixed integer K>=0, (10) and (13) give
the explicit uniform bound

    sum_(k=K)^(2q-1) |F_n(u,sigma*y_(n,k)^sigma)
                       *T_M(a(sigma*y_(n,k)^sigma)*z/R)
                       /F_n(u,sigma*Y)|
       <= [exp(-A*(K+7/8)/12)/(1-exp(-A/12))
                                  +n*exp(-g*n/2)]/(1-rho_*),

for all sufficiently large allowed n, |z|<=1 and u in V, with an
empty sum understood as zero.
For each fixed initial block, the exact remainder
rho_*^M/(1-rho_*) tends to zero and its spatial nodes tend to their
respective endpoint. Taking n to infinity first and then K to
infinity proves the uniform statement (14). The anchor has the
same exponentially small normalized bound by (10) at y=0.
This pays the entire signed interior and every finite geometric sum;
it is not an interchange justified merely by termwise convergence.

Dividing each endpoint error by E_n can only decrease it, since
|F_n(u,sigma*Y)|/E_n<=1. At least one ratio is exactly one in
modulus. Hence the coefficient lower bound in (15) persists even
when the relative endpoint magnitudes or phases have no limit.
Equivalently the normalized polynomial can be formed from
F_n(u,0)T_M(xz/R)+sum_m F_n(u,y_m)T_M(a(y_m)z/R), divided
by E_n. This pole-free expression explains why moving poles of C_n
do not affect the error estimate. Its identification with Gtilde_n
is needed only where C_n is finite and nonzero, in particular on I.

**Noncancellation, boundary logarithms and the global qualification.**
If B is the two-by-two evaluation matrix in Section 5 and
b_min=min_(u in V,sigma)|b_sigma(u)|>0, then
max{|(Bv)_1|,|(Bv)_2|}>=b_min/||B^(-1)||_infinity,
where the matrix norm is induced by the vector maximum norm.
The uniform error in (15) can be made smaller than half this bound.
The upper bound follows from |p_sigma|=rho_*<1 and bounded b_sigma.
Thus one of the two interior evaluations of each normalized spatial
polynomial is nonzero with a uniform lower bound. Boundary zeros
do not violate the imported boundary Poisson--Jensen theorem.
At 1/2 the kernel has minimum 1/3 and integral one; its remainder
after subtracting 1/3 is nonnegative and has integral 2/3.
Multiplying that remainder by the boundary upper bound log C_0
has exactly the inequality direction in Section 5. This proves (17)
without assuming a lower boundary bound or fixed spatial degree.

Finally the scalar C_n E_n/R cancels from the defect pointwise.
Integrating over I uses full-circle measure, so the complementary
coefficient is exactly (1-mu(I))*log(2)/3, which is positive.
The audit accepts only the O(1) contribution on I and the equivalence
with the still-unproved complementary o(n) estimate. It does not pay
angular amplitude, full charge, H/support or Xi realization. The
existing direct inputs recorded in the DAG remain sufficient and
unchanged. No mathematical script or numerical evidence is needed.

## Mathlib

Full matching coverage for this fixed-profile arc asymptotic is not
checked. The ready assessment records supporting results in the
[MahlerMeasure module](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html),
including `Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`
and `Polynomial.norm_coeff_le_choose_mul_mahlerMeasure`. These support
the finite-polynomial interface; they are not a formalization of the
uniform signed endpoint sums or (2). No new Mathlib audit is claimed.
