# Corollary C030w: a compact signed-convolution determinant criterion

## Hypotheses

Fix integers m>=1, n>=max(4,2m) and 2<=d<=floor(n/2). Fix positive
real a_1,...,a_m,r and real b_1,...,b_m, and let the actual n rates be

    (q_1,...,q_n)=(a_1+i*b_1,a_1-i*b_1,...,
                   a_m+i*b_m,a_m-i*b_m,r,...,r).

When n=2m the list contains no r entries. Define

    A=sum_l |b_l|, M=sum_l b_l^2,
    q_max=max_(1<=j<=n) Re(q_j).

Fix t>0 and 0<s_*<=t, and assume exactly C030v's restrictions

    t*A<=1/4,
    (n-2*d+1)/2 >= sqrt((d-1)*(n-d+1)).                  (H)

All rates are fixed under differentiation. For Re(q)>0 let
e_q(y)=q*exp(-q*y) for y>0 and zero otherwise, and let
f_b=e_(q_1)*...*e_(q_n). Use C030r's real lower triangular d-by-d
coefficient matrix C_b(x), with positive leading coefficients and
signed derivative-functional norms (-1)^i. No positive derivative
functional is assumed.

Let nu be a real finite signed Borel measure supported on the fixed
interval [0,t-s_*], with total variation |nu|. It does not depend on
the differentiation variable x. Define, near x=t,

    g(x)=f_b(x)+integral_[0,t-s_*] f_b(x-u) dnu(u),
    B_t(u)=exp(q_max*u/2+(37/4)*M*(t^2-(t-u)^2)),
    epsilon=integral_[0,t-s_*] B_t(u)^2 d|nu|(u).

Assume the strict budget epsilon<1. Atoms at either endpoint, nu=0,
repeated rates, zero phases, all real-part contrasts, n=2m and the
closed phase boundary t*A=1/4 are allowed. Neither nu nor delta_0+nu
is required to be positive or to have prescribed total mass.

## Conclusion

The ordinary derivatives defining the following determinants exist, and

    D_k(g;t)=(-1)^(k*(k-1)/2)
                 *det[g^(i+j)(t)]_(0<=i,j<k)>0,
                                  every 1<=k<=d.       (1)

This is a source-based specialization under the prior SPECIALIZE
assessment1242/review1243, completed in attempt1244. Classification is
REPRODUCTION: the signed perturbation mechanism is already present in
the cited real-rate theorem. The conjugate-rate assembly below is local
progress, not a claimed new matrix principle or a proof of RH.
Independent conceptual audit1246, under the unchanged SPECIALIZE
assessment1244/review1245, passes (1) with the original hypotheses
and strict budget. Its checks are recorded below.

No assertion is made at epsilon=1 or s_*=0, beyond the phase window,
for infinite reference convolutions, or about global PF closure. No
actual-Xi representation or payment of this budget is established.

## Proof

### Imported mechanism and the required specialization

S. Sra, *On some positivity properties of the Riemann Xi function*,
[arXiv2611.02944v1, 2 November 2026](https://arxiv.org/pdf/2611.02944v1),
Theorem C.9/(C.18)-(C.20), printed pp27-28, proof p29, supplies the
signed-measure, shifted-congruence and leading-compression mechanism
for positive real rates. Its dimension m is our d, not our pair count.
Its rate hypothesis does not cover nonzero b_l, so that theorem is not
directly applied to this family. C030r supplies the real signed
normalization for these conjugate rates, and C030v supplies the
replacement bound B_t. The following proof checks those interfaces
and the compact signed integral. It does not reprove the source's
real-rate estimate or claim its later global conclusions.

We import the standard Hermitian eigenvalue perturbation bound in
N. J. Higham, [*Eigenvalue Inequalities for Hermitian Matrices*,
9 March 2021](https://nhigham.com/2021/03/09/eigenvalue-inequalities-for-hermitian-matrices/),
the Courant--Fischer consequence following equation (1): for Hermitian
U,V of equal size, with eigenvalues in nonincreasing order,

    |lambda_j(U+V)-lambda_j(U)|<=||V||_2, every j.       (2)

Neither U nor V needs to be positive definite, and eigenvalues need
not be simple. We use (2) on each real symmetric leading block. This
is a theorem application, not a reproof of the perturbation theorem.

### Local ordinary differentiation against the signed measure

C030r's finite-simplex formula gives a real analytic interior function
f_b on (0,infinity), with continuous derivatives of all orders. Put
delta=s_*/2. For x in [t-delta,t+delta] and u in [0,t-s_*],

    s_*/2 <= x-u <= t+s_*/2.                            (3)

This is a compact interval contained in (0,infinity). For each integer
0<=j<=2d-1, let

    K_j=max_(s_*/2<=y<=t+s_*/2) |f_b^(j)(y)|<infinity.

The constant function K_j is integrable against |nu| because |nu|
is finite. For 0<=j<=2d-2, on the open interval (t-delta,t+delta), each
difference quotient for f_b^(j)(x-u), at a fixed interior x and sufficiently
small increment, is bounded in absolute value by K_(j+1), uniformly
in u. This follows from the real mean value theorem and (3). The
Jordan decomposition of nu and dominated convergence therefore permit
successive differentiation under the integral. Continuity follows by
the same domination. In particular, for 0<=j<=2d-2,

    g^(j)(x)=f_b^(j)(x)
                    +integral_[0,t-s_*] f_b^(j)(x-u)dnu(u). (4)

The domain and measure in this integral are fixed. There is no moving
truncation, derivative of nu, or boundary term. All shifted arguments
stay strictly positive; no differentiability of the zero extension
at zero is required. The neighborhood may go beyond x*A<=1/4:
only analyticity is needed there. The sign and evolution estimates
below are used only at t and at t-u in [s_*,t].

### The shifted matrix and the strict perturbation budget

Write H_d(s)=[f_b^(i+j)(s)]_(0<=i,j<d) and
J_d=diag(1,-1,...,(-1)^(d-1)). C030r gives, for s in [s_*,t],

    C_b(s)*H_d(s)*C_b(s)^T=J_d.                         (5)

All these matrices are real, and C_b(s) is nonsingular. The conditions
s>0 and s*A<=t*A<=1/4 verify the normalization's domain, including
the closed phase endpoint. For each u in [0,t-s_*], set s=t-u and

    R(u)=C_b(t)*C_b(s)^(-1),
    F(u)=C_b(t)*H_d(s)*C_b(t)^T.

Solving (5) for H_d(s) proves the exact, ordered congruence

    F(u)=R(u)*J_d*R(u)^T.                               (6)

C030v applies with the same fixed n,m,d,rates,t and this positive s;
its degree inequality is precisely (H). Consequently

    ||R(u)||_2<=B_t(u),
    ||F(u)||_2<=||R(u)||_2^2*||J_d||_2<=B_t(u)^2.       (7)

Here ||J_d||_2=1, and the transpose has the same Euclidean operator
norm. No inverse-basis estimate apart from C030v's relative evolution
bound has been assumed.

The matrix F(u) is continuous on the support interval. Its entrywise
signed integral E=integral F(u)dnu(u) is real symmetric and satisfies

    ||E||_2 <= integral ||F(u)||_2 d|nu|(u)
             <=epsilon<1.                              (8)

For completeness, the first inequality uses total variation rather
than positivity: for any real unit vectors v,w,
|v^T E w|<=integral |v^T F(u)w|d|nu|(u)
<=integral ||F(u)||_2 d|nu|(u). Taking the supremum over v,w gives
the asserted operator-norm bound. Formula (7) ensures its integrability.

Let H_g=[g^(i+j)(t)]_(0<=i,j<d). By (4), (5) at t and entrywise
linearity of the finite integral,

    C_b(t)*H_g*C_b(t)^T=J_d+E.                          (9)

Thus the strict threshold in the target supplies a norm perturbation
of an indefinite signature matrix, without turning the derivative
functional or nu into a positive measure.

### Every leading determinant

Fix any 1<=k<=d, and let P_k be the k-by-d matrix selecting the first
k coordinates. Let C_k and H_g,k denote the leading k-by-k blocks of
C_b(t) and H_g, respectively, and put E_k=P_k E P_k^T. Since
C_b(t) is lower triangular, its first k rows have no entries in
columns k,...,d-1. Hence P_k C_b(t)=C_k P_k, and compressing (9) gives

    C_k*H_g,k*C_k^T=J_k+E_k,
    ||E_k||_2<=||E||_2<=epsilon<1,                      (10)

where J_k=diag(1,-1,...,(-1)^(k-1)). The norm inequality uses
||P_k||_2=||P_k^T||_2=1. In particular this is a statement about each
leading derivative block, not an inference from full-matrix inertia.

The matrix J_k has p=ceil(k/2) eigenvalues +1 and q=floor(k/2)
eigenvalues -1. Apply (2) to U=J_k, V=E_k. Its first p ordered
eigenvalues are at least 1-epsilon>0, and its last q are at most
-1+epsilon<0. There are no zero eigenvalues. Thus

    sign det(J_k+E_k)=(-1)^floor(k/2).                  (11)

Each C_k is real triangular and nonsingular, so (10) implies
det(H_g,k)=det(J_k+E_k)/(det C_k)^2. The denominator is strictly
positive. Finally k*(k-1)/2 and floor(k/2) have the same parity:
for k=2h or 2h+1 their difference is respectively 2h(h-1) or 2h^2.
Combining this fact with (11) proves the strict positivity in (1)
for the chosen k, and hence for every 1<=k<=d.

### Boundary cases and limitations

For k=1 the argument has one positive eigenvalue and no negative
ones, so it includes g(t)>0. If nu=0, E=0 and the result reduces to
C030r's signs. At u=0, R(0)=I_d and B_t(0)=1, so an atom there is
included without a limiting argument. At u=t-s_*, the shifted time
is exactly s_*>0, and (3)-(8) remain valid. If s_*=t, the support
is {0}; write nu=c*delta_0 with c real. Then epsilon=|c|<1 and
g=(1+c)f_b near t with 1+c>0, consistently with (1).

If M=0, all phases vanish and B_t(u)=exp(q_max*u/2); the squared
weight is the real-rate exp(q_max*u). Partial zero phases, repeated
rates and arbitrary real-part contrasts require no new limit or
nondegeneracy premise beyond the already strict pivots in C030r.
When n=2m, r is absent and does not enter q_max. At t*A=1/4 the
normalization and C030v's estimate include the endpoint; (3)-(4)
need only interior analyticity, not positivity beyond that endpoint.
The original degree inequality and 2<=d<=floor(n/2) are retained.

The proof establishes a finite sufficient budget. It neither constructs
such a reference and signed measure for actual Xi nor estimates the
actual weighted variation. Compatible degree/time choices, the global
complement, theta signing, graph realization and all-degree mixed
positivity remain independent open issues. In particular this does
not discharge L030-L032/C032a or reopen automatic finite-to-global
transfers stopped elsewhere in the notebook.

### Independent conceptual audit1246

17 November 2026. This audit reuses the approved source assessment
and the audited C030r/v interfaces; it does not independently recertify
all upstream orbital results or the source's global PF assertions.
The conclusion passes without changing a hypothesis or constant.

**Input matching.** C030w's n,m,d and fixed rates satisfy C030r's
normalization hypotheses. For every support point u, s=t-u lies in
[s_*,t], so s>0 and s*A<=1/4. C030r(5) is therefore exactly (5),
for the same ordinary derivative Hankel matrix and row coefficient
normalization. C030v(1) is exactly the ordered norm estimate in (7)
with its unchanged degree inequality (H). Its real maximum is over
the actual list; an unused r when n=2m cannot enter that estimate.
C030q/t and C030u are used only inside those audited inputs. C030s
and the parked joint-moment inequality are not premises. The two
direct mathematical inputs recorded for C030w in the DAG are correct.

**Signed differentiation.** With delta=s_*/2, the smallest possible
x-u is s_*/2 and the largest is t+s_*/2, even at either support
endpoint. This verifies the entire compact domination interval (3).
For a fixed interior x choose increments whose segments stay in
(t-delta,t+delta). The mean value bound by K_(j+1) then holds
simultaneously for all u. Since |nu| is finite, dominated convergence
applies separately to both Jordan parts at every differentiation
step. Derivatives through order 2d-2, the maximal Hankel entry order,
are continuous; K_(2d-1) supplies more than sufficient domination
for the last displayed difference-quotient check. Nothing varies in
nu or its integration interval. This verifies ordinary derivatives,
not merely distributional ones, and requires no assertion at zero.
Only interior analyticity is used on the neighborhood beyond the
closed phase boundary.

**Ordered normalization and budget.** Solving (5) gives
H_d(s)=C_b(s)^(-1) J_d C_b(s)^(-T). Substitution at t places the
two factors as R(u) and R(u)^T in (6); reversing their order would
not be this congruence. The norm bound must be squared because there
are two factors. In particular the actual weight is

    B_t(u)^2=exp(q_max*u+(37/2)*M*(2*t*u-u^2)).

This is the stated epsilon, with no missing factor two. Continuity
on the closed support interval makes all entries measurable. The
unit-vector total-variation argument in (8) controls their signed
matrix integral without a positive-functional or positive-nu premise.
The imported Hermitian bound applies because that integral and every
compression are real symmetric. Strict epsilon<1, not epsilon<=1,
is what keeps every relevant eigenvalue away from zero.

**Every ordinary leading block.** The coefficient rows of degree
less than k have zero entries in all monomial columns of degree at
least k. Thus P_k C_b(t)=C_k P_k holds for each k, and multiplication
on both sides gives exactly (10) with the first k ordinary derivative
rows and columns. The full matrix's inertia is not being used as a
surrogate. Apply the cited eigenvalue bound anew to each J_k+E_k:
its ceil(k/2) positive eigenvalues are at least 1-epsilon and its
floor(k/2) negative eigenvalues are at most -1+epsilon. The real
nonzero determinant of C_k enters squared. The parity differences
2h(h-1) and 2h^2 in the proof verify the sign for even and odd k.
For k=1 this uses the leading block of the already permitted d>=2
normalization; it does not invoke C030v at a forbidden d=1.

**Boundary checks and verdict.** At u=0 the congruence is J_d
and its bound is one. At u=t-s_* the normalization is evaluated at
the positive time s_*. Both atoms are already covered by the signed
integral. For s_*=t, nu=c delta_0, |c|<1 gives a positive factor
1+c, so every k-th determinant scales by (1+c)^k. For nu=0 the
perturbation vanishes. M=0 gives exactly the real-rate weight;
partial zero phases, repeated rates and all real-part contrasts are
already within C030r/v, without a distinct-rate limit. Both input
theorems include t*A=1/4 and n=2m; (H) remains required in those
cases. There is no claim at s_*=0, epsilon=1 or outside the phase
window. The audit identifies no load-bearing failure or added premise.

This is verification of an existing source-based specialization,
classified REPRODUCTION, not a new theorem beyond the sources checked.
It certifies only the finite sufficient budget in (1). Actual-Xi
representation and payment, degree/time compatibility, the global
complement, theta signing, realization and all-degree positivity remain
unresolved. No numerical or mathematical-script check was needed for
these exact analytic and finite-dimensional steps.

## Mathlib

Full matching coverage for this compact conjugate-rate signed-convolution
criterion has not been checked; no absence claim is made. The imported
finite Hermitian perturbation bound and dominated convergence are named
standard inputs, with the former precisely cited above. No Lean proof,
numerical certificate or computational verification is claimed.
