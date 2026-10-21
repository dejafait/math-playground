# L139 — The axial generator is a positive multiple of the physical divergence form

## Hypotheses

Import L098(2)'s established K_(i,ax), with exactly L097's real
physical columns V_k, plane paths z_v, C, P and Q=I-P. Use SU(2),
both actual L010 probes i=3,6, the direction-1 straight lower-rooted
forest, D=(-4,4)^4 with all-face relative fixed links, tau=1/16, and
bare small-coupling coefficients at fixed mesh before refinement.
This contracts a proved continuum functional; it takes no new mesh
limit. Retain both generator orientations already included in L098,
all relative exterior modes, both displacement sectors, the lower
prefix including its constant axial mode, and both axial derivatives.

Use L008's actual smooth compact divergence-free displacement u and
real symmetric c_(i;kl), and L132's exact physical form P_(i,D).
Any numerical bounds below import L133's full intervals for that
form, with its certified-input and L039 IEEE arithmetic qualifications.
They are not independent processor/BLAS verification. No outside
factor 3 or color factor is introduced here. L124 adds K_(i,ax)
with a plus sign before its single outside factor 3.

## Conclusion

With normalized torus measure, E=diag(eta_2,eta_3,eta_4), define

    t_ax=(4/3) integral Tr[(Q E^2 Q)^2].                   (1)

The integrand is bounded; its value at lambda=0 may be set to zero.
It need not have a direction-independent limit there. Then

    2/3<t_ax<3/2,
    K_(i,ax)=(t_ax/2)P_(i,D).                             (2)

Consequently L133's qualified complete intervals give

    786<K_(3,ax)<1770,   234<K_(6,ax)<528.                 (3)

The exact rectangular-cutoff reduction uses the same scalar and
L132's D form, and its complete omitted-spectrum error is bounded by

    |K_(i,ax)-(t_ax/2)P_(i,D)^[K]|
                        <(3/4) C_D N_i H(K).             (4)

At K=96 the right side is below 10^-12 for both probes. No new
retained spatial/time integral or torus quadrature is required for
(3). The reduction and analytic scalar bounds are unconditional
within the imported functional hypotheses; (3) retains L133's
computer-assisted arithmetic model.

This evaluates another selected coefficient in L124, not its complete
comparison. G,R and the triplet transverse-H sign remain unresolved.
No compensation K_(i,oo)=-4 gamma D_i, finer-scale bound, logarithm,
other-jet cancellation, finite interacting matching or reflected error
<=c_box/2 follows. Continuum field axioms, reflection positivity,
infrared control and finite positive mass remain independent gaps.
There is no Yang--Mills candidate or claim of certified novelty.

## Proof

### 1. Contract the complete axial filter before angle integration

Let Z be the real matrix with oriented plane rows
-d_b e_a^T+d_a e_b^T, so C=iZ, Z^T Z=lambda Q and Z d=0.
L134(5), with the same unmodified L097 paths, gives

    z_v d=-2 Z E v.

For real physical v this vector is real; the imaginary part of z_v
annihilates d. Therefore L098's full alternating symbol is

    alpha_v=P z_v^* C Q
           =d (z_v d)^* iZ Q/lambda
           =-2i d v^T E Q.                              (5)

This identity retains every plane and physical component, and does
not commute a variable coefficient through a finite projection.
It is a contraction inside the already established torus functional.
At fixed angle, the matrices do not depend on x, so

    omega_k=alpha_(V_k) u_1 E^2,
    partial_1 omega_k
        =alpha_(partial_1 V_k) u_1 E^2
                              +alpha_(V_k)(partial_1 u_1)E^2. (6)

For arbitrary real v,w, (5) gives the exact bilinear trace

    Tr[(Q/lambda)alpha_w^* alpha_v E^2]
                           =4 v^T E Q E^2 Q E w.         (7)

Both copies of Q and the unequal component filters E^2 remain in
(7). Replacing its middle E^2 by the identity would change the scalar
and is not used. Its matrix is symmetric and bounded uniformly at
every nonzero lambda, since E and Q have norm at most one.

### 2. The full angle integral is scalar on physical components

Put X_a=d_a^2 and L=sum_a X_a=lambda. With B=E Q E^2 Q E,

    B_rs=eta_r eta_s sum_b eta_b^2
                     (delta_rb-d_r d_b/L)(delta_bs-d_b d_s/L).

For r!=s, each term is odd in angle r and angle s. More explicitly,
it is eta_r eta_s d_r d_s times

    -(eta_r^2+eta_s^2)/L+sum_b eta_b^2 X_b/L^2.

That expression depends otherwise only on the X's and eta's, all
even under separate angle reflection. Its integral is zero. The
complete diagonal entries are

    B_aa=eta_a^2[eta_a^2(1-X_a/L)^2
                            +sum_(b!=a) eta_b^2 X_a X_b/L^2]. (8)

Permutation of the three angle coordinates preserves the normalized
measure, d, eta and the full domain. Thus their integrals agree.
Cyclicity and Q^2=Q give

    Tr B=Tr[E^2 Q E^2 Q]=Tr[(Q E^2 Q)^2].

Hence integral 4B=t_ax I, exactly with (1). Separate parity deletes
only off-diagonal physical entries; it deletes neither a plane nor
an exterior mode. Boundedness permits all these integrations.

### 3. Retain the kink and both derivatives in axial integration by parts

First restrict k,l to the same finite rectangular mode cutoff.
Its coefficient matrix is still real symmetric. Let

    S_i(x)=sum_(k,l)c_(i;kl) V_l(x) dot V_k(x).

Symmetry gives sum c V_l dot partial_1 V_k=(partial_1 S_i)/2.
Insert (6)--(7) into L098(2), keeping its initial minus sign and
the kink half-weight. The finite-sum functional is

    -t_ax integral_D [(u_1/2+ell partial_1 u_1)S_i
                                      +(ell u_1/2)partial_1 S_i]. (9)

There is no boundary term when integrating the second summand by
parts in x_1: u_1 vanishes in fixed collars of both axial faces,
whereas no upper pin or compact support is imposed on V. Since
partial_1 ell=1, (9) equals

    -t_ax integral_D [(u_1/2+ell partial_1 u_1)
                            -(u_1+ell partial_1 u_1)/2]S_i
       =-(t_ax/2) integral_D ell (partial_1 u_1) S_i.    (10)

In particular the terms proportional to u_1 cancel, rather than
being individually discarded. L008 proves div u=0, so
partial_1 u_1=-div_T u. Equation (10) is exactly (t_ax/2) times
L132's P_(i,D) at that cutoff. No condition div_T V=0 is needed.

L098 proof sections 1 and 5 bound V_k and its first axial derivative
by mode polynomials and give a summable full heat majorant for the
original functional. The new torus matrix is uniformly bounded.
The compact weights in (9)--(10) and L132's amplitude/heat bounds
therefore justify passage from these finite-sum identities to the
full sums by dominated absolute convergence. This proves (2)'s
functional identity without deleting either direct/prefix term,
constant axial mode, transition region or probe sector.

### 4. Analytic strict scalar bounds

Write B_0=E^2, with diagonal e_a=1-X_a/4, and let
T=Tr(Q B_0 Q)=sum_a e_a(1-X_a/L). For nonzero L, Q has rank two.
Its positive compressed matrix Q B_0 Q has two nonnegative
eigenvalues. Their elementary square inequality gives

    Tr[(Q B_0 Q)^2]>=T^2/2.

Expanding T gives

    T=2-L/4+(sum_a X_a^2)/(4L)>=2-L/6.                (11)

The last inequality is the square inequality sum X_a^2>=L^2/3.
It is strict unless all three X_a coincide, a set of measure zero.
For normalized angle measure integral X_a=2, hence integral L=6
and integral T>1. The identity
integral(T-integral T)^2>=0 gives integral T^2>1. Equation (1)
then yields t_ax>2/3.

For the upper bound, multiplication on either side by an orthogonal
projection contracts the Hilbert--Schmidt norm. Thus

    Tr[(Q B_0 Q)^2]=||Q B_0 Q||_HS^2<=||B_0||_HS^2
                                                    =sum_a e_a^2.

This inequality is strict on a set of positive measure: where all
e_a>0 and d!=0, B_0 is invertible and its omitted gradient row is
nonzero. The orthogonal block decomposition with P=I-Q exhibits
that row as a strictly positive lost squared norm. Finally
integral cos^4(theta_a/2)=3/8, by the elementary cosine expansion.
Therefore t_ax<(4/3)*3*(3/8)=3/2. No numerical torus evaluation,
singular operator approximation or claimed continuous corner value
is involved in either strict bound.

### 5. Certified physical intervals and complete spectral tail

Both full P_(i,D) intervals in L133 are positive. Multiplying them
by 1/3<t_ax/2<3/4 gives the more precise endpoints

    23591/30<K_(3,ax)<8847/5,
    3518/15<K_(6,ax)<21111/40.

These imply (3), preserving every qualification on L133's intervals.
The identity in section 3 holds at every rectangular cutoff with
the same scalar. Apply L132(4) to its D form and multiply by 3/4
to obtain (4). At K=96, L132's exact positive exponential bound gives

    (3/4) C_D N_6 H(96)
      <(3/4)*20582100*1640736*2717908992/20^27
      <10^-12.

N_3<N_6, so the same bound covers both probes. This is an omission
bound, not a new retained quadrature certificate. The full numerical
intervals already incorporate L133's retained errors and tails.

Reproduction command from the active notebook:

    python3 scripts/combined-ward-response/check_ax_physical_reduction.py

The script retains exact denominator-cleared path/projected-symbol
checks for every physical component, all nine filtered matrix entries
and their parity, and rational endpoint/tail comparisons in
`scripts/combined-ward-response/ax-physical-reduction-certificate.json`.
The angle symmetry, strict scalar bounds and spatial integration by
parts are proved above; a polynomial certificate alone is not their
proof. The script does not evaluate a torus integral or any new
retained heat tensor. This is local RESEARCH / REPRODUCTION under
the unchanged prior EXPLORE comparison assessment, using the existing
finite contraction and ordinary exact linear algebra/IBP methods.
Reproof is limited to the different axial filter and derivative
contraction, which Q's strain multiplier and E's cumulative multiplier
do not cover. No known continuum Ward/flow theorem is rederived.

## Mathlib

Full matching axial physical contraction and strict scalar bounds:
**not checked**. Supporting Fourier parity, orthogonal projections,
trace/Hilbert--Schmidt inequalities, integration by parts, elementary
cosine integration and dominated convergence: **not checked**.
Unknown availability is not absence. No separate source theorem
assigns this isolated coefficient here.
