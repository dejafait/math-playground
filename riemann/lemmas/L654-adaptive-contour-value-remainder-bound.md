# Lemma 654: adaptive contours give a fixed-density joint bound

## Hypotheses

Retain the full family of L651 and L653. Namely n>=5, x=-d=-5/4,
R=11/8, U=R^2, eta=1/100 and t_j=j/n for 0<=j<n. The finite set
Z consists of distinct points with Re(a)=x, |a|<=R-eta and x in Z.
Original simple-pole residues r_a are positive integers, M=sum_a r_a
is at most n/3, and N=|Z|. Poles and residues are independent of the
angle |u|=1. There is no separation, symmetry or coefficient-integrality
assumption. Define

    B_u(z)=product_(j<n) R(z-t_j*u)/(U-t_j*z/u),
    b_u(zeta)=B_u(R*zeta),  W_a(u)=B_u(x)/B_u(a),
    L(z)=sum_a r_a/(z-a),  q_u(zeta)=sum_a r_a W_a(u)/(R*zeta-a).

F_u is the complete component determined by
b_u q_u=B_u(x)L(R*zeta)-F_u. Use normalized spatial and angular circle
means, and <f,g>=mean f conjugate(g), linear in its first variable.
Put

    D_u=sum_a r_a^2 |W_a(u)|^2/(U-|a|^2),
    D_single,n=mean_u D_u,
    D_(u,M)={P_+(b_u J s): deg s<M},
    J s=zeta^(-1)conjugate(s),
    J_n=mean_u ||Proj_(D_(u,M)) F_u||_2^2.

Retain L653's value-only interpolant, without repeated-jet conditions:

    f_u(z)=conjugate(B_u(x))/B_(conjugate(u))(2x-z),
    Q(z)=product_(a in Z)(z-a),
    deg H_u<N,  H_u(a)=f_u(a)=conjugate(W_a(u)),
    s_u(zeta)=H_u(R*zeta).

Finally define

    sigma=sqrt(137/5000),
    delta=log(26/19)-(log 2)/3,  tau_n=(M/sigma) exp(-delta*n),
    ell=sum_a 1/r_a,
    K_(n,N)=N exp(N) (22n/N)^(N-1),
    T_(n,N,M,ell)=sigma/[R K_(n,N) sqrt(M ell)],
    phi(q)=q[1+log(22/q)]   for 0<q<=1/3.

All logarithms are natural. Multiplicities are retained in the
response and the original r_a^2 diagonal even though Q has degree N.

## Conclusion

Uniformly over every permitted family and angle,

    ||s_u||_2 <= K_(n,N) sum_a |W_a(u)|,                    (1)
    ||Proj_D F_u||_2 >= max(0,T*sqrt(D_u)-tau_n),
    J_n >= max(0,T*sqrt(D_single,n)-tau_n)^2,              (2)
    1/T <= 9 n^2 exp(n phi(N/n)).                          (3)

Thus the value-interpolation amplitude cost has an exponential bound
for every N<=M<=n/3, independent of separations, in place of L653's
exp(O(N log n)) bound. In particular, if

    n>=8192,       N<=n/384,                              (4)

then the approved squared rate holds with uniform constants and onset:

    ||Proj_D F_u||_2^2 >= (1/4) exp(-n/16) D_u,
    J_n >= (1/4) exp(-n/16) D_single,n.                   (5)

This fixed positive density of distinct poles includes arbitrarily
close clouds and spread configurations, and allows total original mass
as large as floor(n/3). It improves the cardinality range of L653 for
large n; L653's stronger squared rate 1/20 on its smaller subfamily is
preserved. It does not settle N near n/3: there the exponent in (3)
is bounded by phi(1/3)=(1+log 66)/3, far above the needed amplitude
rate 1/32. An excessive upper cost estimate is not an obstruction to
the actual interpolant, the optimal joint space or its angular mean.
The unrestricted joint target, Xi realization, matching upper bounds,
all-degree signs and inherited audits remain open. This result is
separately unaudited and is not an RH candidate or certified novelty.

## Proof

### 1. Source scope and complete response

Reuse the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-joint-full-grid-polynomial-dual.md`.
Its scope includes the present finite residue/polynomial test of the
same joint target. The local comparison read L649--L653's relevant
normalizations, full response, Gram/correction and contour arguments,
C645y's full component, and the polewise and reflected-multiplicity
failure records. None supplies this adaptive-radius bound. No novelty
is inferred from that scoped comparison, and no new general
approximation theorem is invoked or reproved.

Import the residue theorem and simple-pole rule from R. W. Howell and
J. H. Mathews, *Complex Analysis*, online edition, front matter updated
22 August 2025, [Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html).
The Hardy projection convention is L. Baratchart, S. Chevillard and
T. Qian, *Minimax principle and lower bounds in H2-rational
approximation*, J. Approx. Theory 206 (2016), 17--47, preprint v2,
24 March 2015, [Section 4, (17)--(19)](https://arxiv.org/pdf/1501.01161v2),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004).
Fourier orthogonality and Parseval are A. Levitt, *Analyse de Fourier
et applications*, version retrieved 2 November 2026,
[Theorem 1.3/Exercise 1.2 and Theorem 1.11/Corollary 1.12,
printed pp.6,8](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf).
These named inputs were inspected in the reused assessment chain;
no new source retrieval or independent manuscript audit is claimed.
The elementary contour specialization below is necessary to control
growing N without a separation hypothesis and to compare the rate.

The possible finite poles of f_u have modulus greater than 3/2.
All B_u(a) and B_u(x) are nonzero. The reflection identity in the
hypotheses follows from 2x-a=conjugate(a), retaining the conjugated
denominator angle. The distinct-node interpolant is therefore unique,
and H_u(x)=1. In particular s_u is nonzero and deg s_u<N<=M.

With A_u=R^(-1)sum_a r_a |W_a(u)|^2, the exact polynomial response
and full correction in L653 (6)--(7), using L651's Gram bound, give

    ||Proj_D F_u||_2 >= max(0,A_u/||s_u||_2-tau_n).        (6)

This includes P_-(b_u J s_u), whose norm is at most
exp(-delta*n)||s_u||. No grid factor or negative-part correction is
discarded. The Gram lower bound ensures the corresponding dual is
nonzero. L651 also gives delta>1/16 and D_u>=64/21, the latter from
the anchor W_x=1 and r_x>=1.

### 2. A regularized residue kernel

For an auxiliary radius 0<r<=1/16, avoiding the finitely many disk
tangencies, let Omega be the union of open disks of radius r about
the nodes. Its positively oriented boundary is piecewise smooth.
Partition it into arcs belonging to the individual generating circles;
intersection points have zero length and do not affect integrals.
The total length of the arcs assigned to any one a is at most 2*pi*r.
Every boundary point satisfies |w-a|>=r for every node, so

    |Q(w)|>=r^N.                                         (7)

Moreover |w|<=R-eta+r<=571/400<3/2. Hence f_u is holomorphic on a
neighborhood of the closure of Omega. No pole of f_u lies inside.

Define the polynomial kernel

    K_Q(w,z)=(Q(w)-Q(z))/(w-z),                           (8)

where its polynomial extension is used at w=z. The residue theorem
gives, for every z,

    H_u(z)=1/(2*pi*i) integral_(boundary Omega)
                         f_u(w) K_Q(w,z)/Q(w) dw.        (9)

Indeed at a node a and z not in Z the residue is
f_u(a) Q(z)/[(z-a)Q'(a)], exactly its Lagrange summand.
There is no pole at w=z because (8) is a polynomial. Summing the
residues proves (9) off Z and then everywhere by polynomial
continuity. This is the same H_u, not a new interpolation condition.
In particular z may lie inside Omega or on its boundary; the
regularization removes L653's need for a gap between that boundary
and |z|=R.

For |z|=R and every node a, |z-a|<2R. The common vertical line also
gives |Im(a)|^2<=12029/40000<1. If w belongs to the boundary arc
assigned to a_0, then for every a

    |w-a|<=r+|a_0-a|<1/16+2=33/16<2R.                  (10)

To bound (8), order the nodes arbitrarily and subtract the two
products one factor at a time. Explicitly,

    K_Q(w,z)=sum_(k=1)^N
                 product_(i<k)(w-a_i) product_(i>k)(z-a_i).

Equations (10) and |z-a|<2R show

    |K_Q(w,z)|<=N(2R)^(N-1).                            (11)

The formula and bound include N=1, with empty products equal to one.
No Vandermonde inverse or minimum separation enters this estimate.

### 3. Adaptive radius and retained angular weights

On a boundary arc assigned to a, put h=w-a, so |h|=r. The product
ratio from L653's reflected function has, factor by factor, the bounds

    |U-t_j*u*conjugate(a)| >= U-|a| > 1/2,
    |conjugate(a)-t_j*conjugate(u)| >= d-t_j > 1/4.

Consequently

    |f_u(w)|/|f_u(a)| <= [(1+2r)/(1-4r)]^n
                        <=exp(8nr).                    (12)

For the last inequality, log(1+2r)<=2r and
-log(1-4r)<=4r/(1-4r)<=16r/3 for r<=1/16; their sum is less than
8r. These scalar inequalities follow by integration, so no branch
of the logarithm of f_u is needed.

Use (7), (11), (12) and each arc's length in (9), before summing
over generating nodes. Since |f_u(a)|=|W_a(u)|, this gives

    ||H_u(R*zeta)||_2
      <=N(2R/r)^(N-1) exp(8nr) sum_a |W_a(u)|.           (13)

The L2 bound follows from the pointwise bound on |z|=R and the
normalized spatial measure. The angular weights have not been
replaced by a single maximum or separate-column normalizations.

Now take r_0=N/(8n). The integer-mass condition implies
0<r_0<=1/24<1/16. There is a sequence of regular radii tending to
r_0, since only finitely many tangencies are excluded. Inequality
(13) holds for the same fixed polynomial H_u at each such radius.
Its scalar right side is continuous at r_0; taking its limit is
therefore valid without assuming convergence of any contour integral
or exchanging limits with an angular mean. Since 2R/r_0=22n/N and
8nr_0=N, (13) proves (1).

### 4. The original diagonal and full angular mean

Weighted Cauchy--Schwarz and the original positive integer residues give

    (sum_a |W_a|)^2 <= (sum_a 1/r_a)(sum_a r_a |W_a|^2)
                     =ell R A_u,
    D_u <=sigma^(-2)sum_a r_a^2 |W_a|^2
         <=(MR/sigma^2) A_u.                            (14)

Thus (1) implies

    A_u/||s_u|| >= sqrt(A_u)/(K_(n,N) sqrt(ell R))
                  >=T sqrt(D_u).                       (15)

Equations (6) and (15) prove the pointwise part of (2). All
fixed-family functions involved are continuous in u; this follows
directly from the rational weights and Lagrange formula, and from
L651's uniformly invertible joint Gram matrix for the projection.
In particular they are integrable. The pointwise inequality
T sqrt(D_u)<=||Proj_D F_u||+tau_n and the triangle inequality in
normalized angular L2 give the integrated part of (2).

Here ell<=N<=n, M<=n, N<=n, and R/sigma<9. Also 22n/N>1. Hence

    K_(n,N)<=n exp(N[1+log(22n/N)]),
    1/T <=9 n^2 exp(N[1+log(22n/N)]),                   (16)

which is (3). No original squared residue was replaced by a unit
residue in D_u; (14) pays for unequal multiplicities explicitly.

### 5. Fixed positive density at the prescribed rate

Assume (4). Since phi'(q)=log(22/q)>0 for 0<q<=1/3,

    phi(N/n)<=phi(1/384)=(1+log 8448)/384<9/320.          (17)

For an exact verification of the last inequality, 8448<2^14 and
log 2<7/10, so its right numerator is less than 1+49/5=54/5.
The logarithm bound follows from
exp(7/10)>1+7/10+(7/10)^2/2+(7/10)^3/6=12013/6000>2.
Also log 9<3, for exp(3)>1+3+9/2+27/6=13>9.

At n=8192, log n=13 log 2<91/10, so

    3+2 log n <106/5<128/5=n/320.

The derivative of n/320-3-2 log n is positive for n>640.
Thus (16)--(17) give, for every n>=8192 under (4),

    log(1/T)<=3+2 log n+9n/320<=n/32,
    T>=exp(-n/32).                                      (18)

It remains to pay the full correction. Using the anchor lower bound,
M<=n/3, delta>1/16 and sqrt(21)/(24sigma)<2 gives

    tau_n/[exp(-n/32)*sqrt(D_u)]
      <=sqrt(21)/(24sigma) n exp(-(delta-1/32)n)
       <2n exp(-n/32)
       <=393216/n^2 <=3/512<1/2                         (19)

for n>=8192. The penultimate inequality is exp(v)>=v^3/6 with
v=n/32. The coefficient comparison follows by squaring:
21<2304sigma^2. All constants are exact; no numerical quadrature
or asymptotic onset is used.

Combining (6), (15), (18) and (19) yields
||Proj_D F_u||>=exp(-n/32)*sqrt(D_u)/2. Squaring and taking the
normalized angular mean proves (5). Bounds are uniform in n, the
angle, every separation and all permitted original residues.

### 6. Remaining scope

Unlike shrinking 1/n disks, the adaptive contour gives the rate
function phi(N/n) for arbitrary growing N. It covers both clusters
with arbitrarily small positive separation and spread families within
(4); it does not replace a distinct cloud by a repeated anchor.
The sharper single-anchor result of L653 is unaffected.

For the dense unit-residue endpoint N=M=floor(n/3), (16) allows an
amplitude cost approaching exp(n(1+log 66)/3) up to polynomial factors.
This bound is too large to infer the desired rate, and (2) may reduce
to zero once its correction is subtracted. It is an upper envelope,
not evidence of actual exponential cost or a joint countersequence.
No lower bound at the required rate is proved on the remaining dense
families. Angular correlations and more economical joint choices are
not excluded. No source manuscript or inherited lemma has received
an independent audit here; the new proof also awaits a separate audit.

The exact arithmetic check
`python3 scripts/one-sided-hankel/adaptive-contour-constants.py`
writes `scripts/one-sided-hankel/adaptive-contour-constants.json`.
All 21 rational comparisons passed; the full selected `checks` array,
including every actual and required bound, was inspected with the
shared JSON inspector. They check the geometric constants, logarithm
witnesses, onset, exponent and correction budget. The contour identity,
radius limit and uniform family conclusion are proved above, not by
these arithmetic checks. Existing full-grid normalization certificates
were not rerun because their identities were unchanged.

## Mathlib

Full matching coverage for this finite grid, adaptive value-interpolation
cost and fixed-density relative joint bound has not been checked.
The supporting residue, Fourier/Parseval and projection inputs are
the precise named imports above. Unknown availability is not evidence
of absence. No formal theorem asserting the unrestricted joint target
or actual-Xi mixed positivity is assumed.
