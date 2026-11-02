# Lemma 653: value interpolation controls families with few distinct poles

## Hypotheses

Retain L651's family: n>=5, x=-d=-5/4, R=11/8, U=R^2,
eta=1/100 and t_j=j/n. The common finite set Z consists of distinct
points with Re(a)=x, |a|<=R-eta and x in Z. Original simple-pole
residues r_a are positive integers, M=sum r_a<=n/3, and N=|Z|.
The family is independent of the angle |u|=1. There is no separation,
symmetry or coefficient-integrality assumption. Put

    B_u(z)=product_(j<n) R(z-t_j*u)/(U-t_j*z/u),
    b_u(zeta)=B_u(R*zeta),  W_a(u)=B_u(x)/B_u(a),
    L(z)=sum_a r_a/(z-a),  q_u(zeta)=sum_a r_a W_a(u)/(R*zeta-a).

F_u is the complete component specified in L650/L651 by
b_u q_u=B_u(x)L(R*zeta)-F_u. Use normalized circle means and
<f,g>=mean f conjugate(g), linear in the first variable. Set

    D_u=sum_a r_a^2 |W_a(u)|^2/(U-|a|^2),
    D_single,n=mean_u D_u,
    D_(u,M)={P_+(b_u J s):deg s<M},
    J s=zeta^(-1)conjugate(s),
    J_n=mean_u ||Proj_(D_(u,M)) F_u||_2^2.

Define the rational reflected weight and its value interpolant by

    f_u(z)=conjugate(B_u(x))/B_(conjugate(u))(2x-z),
    Q(z)=product_(a in Z)(z-a),
    deg H_u<N,  H_u(a)=f_u(a)=conjugate(W_a(u)),
    s_u(zeta)=H_u(R*zeta),
    e_u=P_-(b_u J s_u),  v_u=P_+(b_u J s_u).

This is the rational remainder modulo Q, not the multiplicity
polynomial of degree M. Original residues are retained in L, q and D_u.
Finally put

    sigma=sqrt(137/5000),
    delta=log(26/19)-(log 2)/3,  epsilon_n=exp(-delta*n),
    tau_n=(M/sigma)*epsilon_n,
    C_(n,N)=200 exp(16) (N/n) (2Rn)^N,
    T_(n,N,M)=sigma/[R sqrt(M) C_(n,N)].

All logarithms are natural.

## Conclusion

For every such family with n>=400, uniformly at every angle,

    ||s_u||_2 <= C_(n,N) max_a |W_a(u)|,                  (1)
    ||Proj_D F_u||_2 >= max(0,T_(n,N,M)*sqrt(D_u)-tau_n),
    J_n >= max(0,T_(n,N,M)*sqrt(D_single,n)-tau_n)^2.     (2)

Thus the interpolation cost has an explicit bound independent of
every pole separation. In particular, under the additional restriction

    n>=8192,    N<=n/[64 log(2Rn)],                       (3)

the joint target holds, with uniform constants and onset:

    ||Proj_D F_u||_2^2 >= (1/4) exp(-n/20) D_u,
    J_n >= (1/4) exp(-n/20) D_single,n
        >= (1/4) exp(-n/16) D_single,n.                 (4)

The mass M may still be as large as floor(n/3). Restriction (3) is on
the number of distinct poles, not their total multiplicity. It includes
arbitrarily close distinct clouds satisfying (3). For a single anchor
of any allowed residue, the interpolant is exactly 1 and the stronger
pointwise relative bound is 21/121.

This proves only the sparse-distinct subfamily of the approved joint
target. For N of order n, (1) costs exp(O(n log n)) and does not supply
the required rate. It neither disproves that rate nor bounds the actual
optimal joint response from above. Dense distinct families, Xi
realization, matching detector upper bounds, all-degree signs and
separate audits remain open. This local specialization has not had a
separate critical audit; no certified originality or RH candidate is
claimed.

## Proof

### 1. Source scope, remainder and complete response

The unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-joint-full-grid-polynomial-dual.md`
covers the exact joint target and finite Hardy/projection/residue/
polynomial algebra. Its inspected source comparison is reused. The
scoped local comparison checked L649--L652, C645y's full component,
the joint-angular failure record and the reflected-input stops. No
matching distinct-cardinality estimate was found there. L652's
single-angle multiplicity obstruction is a contrast, not a premise
for an angular stop. No novelty follows from that bounded comparison.

Import the residue theorem and simple-pole rule from R. W. Howell
and J. H. Mathews, *Complex Analysis*, online edition, front matter
updated 22 August 2025,
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html).
Import the Hardy projection convention from L. Baratchart, S. Chevillard
and T. Qian, *Minimax principle and lower bounds in H2-rational
approximation*, J. Approx. Theory 206 (2016), 17--47, preprint v2,
24 March 2015,
[Section 4, (17)--(19)](https://arxiv.org/pdf/1501.01161v2),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004).
Fourier orthogonality and Parseval are A. Levitt, *Analyse de Fourier
et applications*, version retrieved 2 November 2026,
[Theorem 1.3/Exercise 1.2 and Theorem 1.11/Corollary 1.12,
printed pp.6,8](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf).
These statements were inspected in the reused assessment chain; no new
source retrieval or independent source audit is claimed. No general
approximation theorem is reproved. The finite contour specialization
below is needed to obtain constants uniform over colliding nodes and
to compare its cost with the prescribed exponent.

The possible finite poles of f_u are 2x-t_j*conjugate(u), with
modulus at least 2d-t_j>3/2>R. Thus f_u is holomorphic near the closed
disk |z|<=R. At each node 2x-a=conjugate(a), so conjugating the
complete B product, including its denominator angle, gives
f_u(a)=conjugate(W_a(u)). The unique value interpolant is

    H_u(z)=sum_a f_u(a) Q(z)/[(z-a)Q'(a)].                (5)

Distinctness guarantees Q'(a)!=0. This formula is a definition for
fixed families, not a separation-dependent norm estimate. In particular
H_u(x)=1, and deg s_u<N<=M. By L651's Gram lower bound v_u!=0.

L650's arbitrary-polynomial response and L651's negative-part estimate
give, with A_u=R^(-1)sum_a r_a |W_a(u)|^2,

    <F_u,v_u>=B_u(x)<L(R*zeta),e_u>-A_u,
    ||v_u||^2=||s_u||^2-||e_u||^2,
    ||e_u||<=epsilon_n||s_u||,
    |B_u(x)<L(R*zeta),e_u>|<=tau_n||s_u||.              (6)

Here L651 uses all M spatial coordinates; s_u is padded with zeros
when N<M. All n grid factors remain. Hence Cauchy--Schwarz for the
projection, followed by ||v_u||<=||s_u||, gives

    ||Proj_D F_u|| >= |<F_u,v_u>|/||v_u||
                    >= max(0,A_u/||s_u||-tau_n).        (7)

This keeps the complete negative-part correction. It does not replace
the norm of a complex pairing by a sum of absolute residues without
paying the interpolant's norm.

### 2. A separation-independent contour bound

Assume n>=400. Choose r in [1/n,2/n] avoiding the finitely many radii
at which the circles of radius r around distinct nodes are tangent.
Let Omega be the union of the corresponding open disks. Its boundary,
oriented positively around each component, is a finite union of
piecewise smooth circle arcs; the centers lie on one line, so the
components have no holes. The following bounds also hold componentwise:

    length(boundary Omega)<=2*pi*r*N,
    |w-a|>=r for every a in Z and w in boundary Omega,
    |Q(w)|>=r^N,
    |w|<=R-eta+r<=R-eta/2.                              (8)

Each boundary point is at distance r from at least one node a. Write
h=w-a and use 2x-a=conjugate(a). Direct division of the rational
products gives

    f_u(w)/f_u(a)
      =product_j [(U-t_j*u*(conjugate(a)-h))/(U-t_j*u*conjugate(a))]
                   *[(conjugate(a)-t_j*conjugate(u))
                      /(conjugate(a)-h-t_j*conjugate(u))].

The original family has

    |U-t_j*u*conjugate(a)|>=U-|a|>=U-(R-eta)>1/2,
    |conjugate(a)-t_j*conjugate(u)|>=|a|-t_j>=d-t_j>1/4.

Consequently

    |f_u(w)/f_u(a)| <= [(1+2r)/(1-4r)]^n <=exp(8nr)
                    <=exp(16).                         (9)

For the logarithmic inequality in (9), r<=2/400<1/16, so
log(1+2r)<=2r and -log(1-4r)<=4r/(1-4r)<=16r/3;
their sum is less than 8r. These inequalities follow by integration
of 1/(1+t) and 1/(1-t), respectively. Thus no branch of a logarithm
of f is being chosen. The maximum of |f| on the contour is at most
exp(16) W_max, where W_max=max_a |W_a(u)|.

For |z|=R, z is outside Omega and |w-z|>=eta/2. Applying the
simple-pole residue rule at each node to (5) yields exactly

    H_u(z)=-Q(z)/(2*pi*i)
               *integral_(boundary Omega) f_u(w)/[Q(w)(w-z)] dw. (10)

There are no other poles inside: f is holomorphic there and z is
outside. Also |Q(z)|<=product_a(|z|+|a|)<=(2R)^N. Using (8)--(9),

    |H_u(z)| <= (2/eta) exp(16) N r (2R/r)^N W_max
              <=200 exp(16) (N/n) (2Rn)^N W_max.

The second inequality uses r^(1-N)<=n^(N-1), valid also for N=1.
The normalized boundary L2 norm is at most this supremum, proving (1).
The contour is auxiliary and independent of the angular estimate;
no lower bound on the separation or exchange of limits has entered.

### 3. Comparing with the original diagonal

The radial margin gives U-|a|^2>=sigma^2. Positivity and integrality
of the original residues imply r_a>=1 and r_a<=M. Therefore

    W_max^2 <=sum_a r_a |W_a|^2=R A_u,
    D_u <=sigma^(-2)sum_a r_a^2 |W_a|^2
         <=(M R/sigma^2) A_u.

Combining these two inequalities gives

    W_max*sqrt(D_u) <=(R sqrt(M)/sigma) A_u,
    A_u/||s_u|| >= T_(n,N,M) sqrt(D_u).                 (11)

This pays for unequal residues rather than silently replacing r_a^2
in D_u by r_a. Substituting (11) in (7) proves the pointwise part
of (2). All rational quantities and the interpolant are continuous
in u for a fixed family. The joint Gram matrix has the uniform lower
bound from L651, so its projection norm is continuous as well. From
T sqrt(D_u)<=||Proj_D F_u||+tau_n, the triangle inequality in the
normalized angular L2 space gives the integrated bound in (2).
This is a bound for the full angular mean, not a sampled quadrature.

### 4. Uniform constants for the sparse-distinct family

Assume (3). Since N/n<=1 and M<=n, equation (11)'s coefficient has

    log(1/T) <=16+log(200R/sigma)+(log n)/2+N log(2Rn).

Now R/sigma<9, so 16+log(200R/sigma)<16+log(1800)<27,
using 1800<2^11 and log 2<1. For n>=8192,

    27<=n/256,   log n<=n/256,   N log(2Rn)<=n/64.

For the middle inequality at 8192, log(8192)=13 log 2<13<32;
thereafter the derivative of n/256-log n is positive. It follows that

    log(1/T) <=11n/512<n/40,
    T>=exp(-n/40).                                      (12)

The anchor has W_x=1 and r_x>=1, hence D_u>=64/21 at every angle.
L651 proves delta>1/16. Therefore

    tau_n/[exp(-n/40)*sqrt(D_u)]
      <=sqrt(21)/(24 sigma)*n*exp(-(delta-1/40)n)
       <2n exp(-3n/80) <=1/2                            (13)

for n>=8192. The coefficient bound follows by squaring, since
21<2304 sigma^2. For the final bound, exp(v)>=v^3/6 gives
2n exp(-3n/80)<=6144000/(27n^2)<=1/2; the last inequality holds
already at 8192 and its left side decreases. All comparisons are exact.

Equations (7), (11)--(13) give
||Proj_D F_u||>=exp(-n/40)*sqrt(D_u)/2. Squaring and integrating
proves (4), including a uniform onset and a positive absolute constant.
Its squared loss 1/20 is strictly smaller than the permitted 1/16.
No limit over angle or family is required to obtain this conclusion.

### 5. Repeated anchors, distinct clouds and remaining scope

If Z={x} with arbitrary allowed r_x=M, equation (5) gives H_u=1.
Since b_u(0)=0, v_u=b_u/zeta has norm one and e_u=0. Equation (6)
gives <F_u,v_u>=-M/R. Dividing by D_u=M^2/(U-d^2) proves the
pointwise relative bound (U-d^2)/R^2=21/121. This removes L652's
unneeded repeated-jet conditions; it does not assert that its old
polynomial was inexpensive.

For a direct distinct-cloud test, take a_j=x+i*j*h for 0<=j<N,
all original residues one, and any h>0 with
(N-1)h<=sqrt((R-eta)^2-d^2). The proof and (4), when (3) holds,
are uniform as h decreases to zero. For fixed n,N the coefficients
in (5) have a removable confluent limit: write f=N_u/D_u^f with
polynomial denominator nonzero on the disk. Multiplication by D_u^f
on C[z]/(Q) is invertible even at Q=(z-x)^N. Its matrix entries
are continuous in Q and u, and its determinant is nonzero at all
angles. The adjugate formula and compactness of the angular circle
give uniform convergence to the degree<N Taylor polynomial at x.
This explains why the bound covers arbitrarily close nodes without
treating a distinct cloud as a single node. It gives no uniform
growing-N Taylor estimate stronger than (1).

At N=M=floor(n/3), the exponent of the proved cost is
N log(2Rn)+O(log n), not a bound below n/32. Thus this proof leaves
the dense regime unresolved. An expensive upper bound on a chosen
interpolant is not a lower bound on its actual cost and is not a
counterexample to the joint space. The preserved draft records the
unfinished all-angle Taylor-tail approach without asserting a result.

The companion exact check
`python3 scripts/one-sided-hankel/value-remainder-check.py`
writes `scripts/one-sided-hankel/value-remainder-check.json`.
It tests the value-only interpolation and its complete response/norm
against full-grid interpolation, at Gaussian-rational rotations with
unequal residues, a repeated anchor and distinct close clouds. It also
checks the rational constants used in (12)--(13). These finite checks
test normalization and conjugation only. The uniform inequalities are
the analytic proof above, and a separate critical audit remains due.
All 48 exact checks passed in four cases at n=9,12. The complete
verification objects, identity-error arrays, diagonal comparisons and
constant bounds were inspected with the shared JSON inspector. No
finite test was used to infer (3)--(4).

## Mathlib

Full matching coverage of this specified grid, value-interpolation cost
and sparse-distinct joint lower bound has not been checked. Supporting
residue, Fourier/Parseval and projection facts are the named imports
above. Unknown availability is not evidence of absence. No formal result
asserting the unrestricted joint bound or Xi positivity is assumed.
