# C744t: A qualified actual-residue cluster bound without internal separation

## Hypotheses

Use C744r's Fourier convention F_v(z)=integral v(x)exp(-izx)dx,
neutral space N on (0,ell), ell=log(3)/2, complete Hermitian form H,
and actual Xi zeros Z with multiplicities r_z. In particular
|Im z|<1/2, and no RH-conditional positivity is an input. Suppose
there is a hypothetical z0 in Z with

    |Re z0|<=T, -Im z0>=delta, T>=1, 0<delta<1/2.

Put p=iz0, q(z)=z^2+1/4, kappa=|q(z0)| and L=T+2. The open
strip implies kappa>0. Its numerical value, or a certified positive
lower bound, is ADDITIONAL data: no uniform positive lower bound
for it from the displayed T,delta inequalities is proved here.
No actual off-line zero is exhibited.

Supply a constant A>=1 certifying the COMPLETE two-sided count

    sum_(z in Z, |Re z|<=U) r_z <= A U log(eU), U>=1.       (1)

The count includes multiplicity, both signs, the endpoints and any
zero with Re z=0. It is not the size of a computed list. A numerical
A satisfying (1) is not produced here. For possible certification,
the inspected primary count source is Bellotti--Wong,
*Improved estimates for the argument and zero-counting function of
the Riemann zeta-function*,
[arXiv:2412.15470v2](https://arxiv.org/html/2412.15470v2),
7 July 2025, Theorem1.1 and Section5: with multiplicities and
0<Im rho<=U, U>=e, it gives, among its two alternatives,

    |N(U)-U log(U/(2pi e))/(2pi)|
       <=0.11200 log U+0.12567 log log U+3.77417.

This theorem is cited, not reproved or silently identified with (1).
Under rho=1/2+iz its height is Re z. Any use to certify (1) must
handle the two signs, U in [1,e] and the zero-height convention.
No constants from the corrected older HSW version are used.

Choose a real nonnegative psi in C_c^infinity(-1,1) of integral one.
Its seminorms below are supplied profile data, not numerical
certificates obtained in this step. Set

    w=ell/4, x_*=w/2,
    0<tau<=min{w/4,1/(64L)},
    eta(x)=tau^(-1) psi((x-x_*)/tau), phi=eta''-eta/4,
    d_j=||psi^(j)||_1, b_j=||psi^(j)||_2, 0<=j<=4,
    P0=tau^(-2)d_2+1/4,
    P2=tau^(-4)d_4+tau^(-2)d_2/4,
    B=2 [sum_(j=0)^2
          (tau^(-j-5/2)b_(j+2)+tau^(-j-1/2)b_j/4)^2]^(1/2),
    S=e^w A(P0^2+5P2^2).                                  (2)

Finally set

    R=min{delta/4,1/8,kappa/(64L)},
    N_*=ceil(A(T+1)log(e(T+1))),
    d=R/[4(N_*+1)], sigma=delta/2,
    omega=q(z0)^2/kappa^2, alpha=3kappa^2/4.                (3)

Here |omega|=1. Neither R nor d is a stipulated pairwise gap
between zeros. For the finite-window conclusion also assume
C744s's strict-slack data f0 in N, ||f0||_2=1,
b=||f0||_H2<M0, Delta=M0-b>0, and define

    D=4+8sqrt(2)/3+log(4pi),
    epsilon=min{1/(2B),Delta/[2(1+M0)B]},
    C=D[(b+1/2)^2+b^2]/epsilon^2.                          (4)

## Conclusion

The real phi is nonzero, neutral, compactly supported in (0,w),
and 2||phi||_H2<=B. Its ACTUAL complete residues satisfy

    a_z=r_z F_phi(z)conj(F_phi(conj(z)))
        =r_z q(z)^2 F_eta(z)F_eta(-z),
    sum_z |a_z|<=S.                                       (5)

For every zero with |z-z0|<=2R,

    Re(conj(omega)a_z)>=alpha r_z.                        (6)

There exists r in [R,2R] such that the circle Gamma={|s-p|=r},
positively oriented, has Re(s)>=sigma and distance at least d
from EVERY pole iz. For its finite interior cluster
Z_r={z:|z-z0|<r}, including z0, put m_r=sum_(Z_r)r_z. Then

    Re(conj(omega)sum_(Z_r)a_z)>=alpha m_r>=alpha>0.        (7)

No separation of the zeros within Z_r is required.

Let h(t)=H(phi,tau_t phi)=sum_z a_z exp(itz),
G(s)=sum_z a_z/(s-iz), and J_H(s)=integral_0^H h(t)exp(-st)dt.
Fix an integer K>=2 and H=(K-1)ell. IF all admitted same-profile trains
with at most two occupied cells in this K-cell window have
nonnegative normalized energy, then

    |h(t)|<=C (0<=t<=H),
    sup_Gamma |G-J_H|<=S/d+C/sigma,                       (8)
    (1/(2pi i)) integral_Gamma (G-J_H)(s)ds
          =sum_(Z_r)a_z.                                 (9)

In particular

    alpha m_r <= r sup_Gamma |G-J_H|
                 <= r(S/d+C/sigma).                      (10)

The full exterior sum is retained in (8); its vanishing contour
integral in (9) follows from holomorphy, not a deletion or a sign.
For comparison, in Re(s)>1/2 the complete tail also obeys

    |G(s)-J_H(s)|<=S exp(-(Re(s)-1/2)H)/(Re(s)-1/2).        (11)

These are qualified lower and boundary estimates, NOT a two-cell
length bound. The upper bound in (8) has no decay in H. A quantitative
propagation from (11) to the whole Gamma, strong enough to give
sup_Gamma|G-J_H|<alpha/r, is still missing. Kappa, (1), and the
profile data remain explicit qualifications, not inferred numerical
certificates. Independent finite-window signs and the main actual-Xi
positivity, non-neutral coverage and all-window assembly remain open.
The separate conceptual audit in Section5 (11 November 2026, step524)
accepts (5)-(11) under exactly the displayed qualifications.
POTENTIALLY_NEW describes the original bounded comparison only,
not established originality or progress beyond all existing literature.

## Proof

### 1. Profile, neutralizing factor and actual cluster phase

The support of eta, and of each derivative, is a compact subset of
(w/4,3w/4). Integration by parts twice, with no endpoint terms,
gives integral exp(plus/minus x/2)phi(x)dx=0 and
F_phi(z)=-q(z)F_eta(z). For real phi,
conj(F_phi(conj(z)))=F_phi(-z). Since q(-z)=q(z), this proves
the factorization in (5), with its complex square rather than
|q(z)|^2. Translation of eta cancels from F_eta(z)F_eta(-z).

For |z-z0|<=2R we have |z0|<=T+1/2 and |z|<L. Also

    |q(z)-q(z0)|<=|z-z0|(|z|+|z0|)
                 <=4RL<=kappa/16.

Thus u=q(z)/q(z0) satisfies |u-1|<=1/16,
|u|<=17/16 and |u^2-1|<=33/256.
Finite-support Fubini and the nonnegative integral-one bump give

    P(z):=F_eta(z)F_eta(-z)
         =integral integral eta(x)eta(y)exp(-iz(x-y))dxdy,
    |P(z)-1|<=exp(2tau|z|)-1<=exp(1/32)-1<=1/31<1/16.

The last exponential inequality follows termwise from
exp(t)<=sum_(n>=0)t^n=1/(1-t) for 0<=t<1. This is an
elementary estimate, not an assumed common-phase theorem. Hence

    |a_z/(r_z q(z0)^2)-1|
       =|u^2 P(z)-1|
       <=(289/256)(1/16)+33/256
       =817/4096<1/4.

Rotating by conj(omega) proves (6), and summing proves (7) for
any such cluster containing z0. At z0 the product is nonzero,
so phi is nonzero. No arbitrary signed-residue model replaces
these Fourier products, and no phase claim is made outside the disk.

### 2. Explicit profile and complete spectral-mass costs

Scaling the bump gives
||eta^(j)||_1=tau^(-j)d_j and
||eta^(j)||_2=tau^(-j-1/2)b_j. The triangle inequality for
phi^(j)=eta^(j+2)-eta^(j)/4 proves 2||phi||_H2<=B,
||phi||_1<=P0 and ||phi''||_1<=P2. These bounds display the
cost of narrowing the bump; it is not treated as a bounded-norm
unit-ball perturbation. C744s uses B through epsilon in (4).

For every z in the zero strip, absolute integration, and separately
two integrations by parts when z!=0, give

    |F_phi(z)|, |F_phi(-z)|
       <=e^(w/2)P0,
    |F_phi(z)|, |F_phi(-z)|
       <=e^(w/2)P2/|z|^2  (z!=0).

The contribution from |Re z|<=1 is at most e^w A P0^2 by (1).
For j>=0, on 2^j<|Re z|<=2^(j+1), |z|>2^j and (1) bounds
the total multiplicity by A2^(j+1)[1+(j+1)log2]. Therefore
the full complementary absolute sum is at most

    e^w A P2^2 sum_(j>=0)2^(1-3j)[1+(j+1)log2]
       =e^w A P2^2[16/7+(128/49)log2]
       <5e^w A P2^2.

Here sum 8^(-j)=8/7 and sum (j+1)8^(-j)=64/49;
log2<1 gives 16/7+128/49=240/49<5. The core and shells
partition all zeros, including every endpoint exactly once.
This proves (5) with a convergent majorant for the ENTIRE sum.
It is not a finite truncation, an RH spectral-square assertion,
or an unsigned estimate assigned to the value of the signed sum.

### 3. A count-selected boundary, with no internal gap

Every zero with |iz-p|=|z-z0|<=3R has |Re z|<=T+3R<T+1.
By (1), there are at most N_* such distinct zeros, even when
multiplicity is counted. Exclude from [R,2R] the open intervals

    (|iz-p|-d, |iz-p|+d)

for all those zeros. Their total length is at most
2dN_*=R N_*/[2(N_*+1)]<R/2. Thus they do not cover [R,2R];
choose r in the remainder. For each of these near zeros and each
s on Gamma, the reverse triangle inequality gives |s-iz|>=d.
For every other zero, |iz-p|>3R and r<=2R give |s-iz|>R>=d.
This is a certificate of existence from the complete count. Locating
a particular numerical r would require additional certified spectral
information; no algorithm based on an incomplete zero list is claimed.

The entire disk has Re(s)>=Re p-2R>=delta/2=sigma.
Its enclosed zeros are finite, include z0 and satisfy the phase
estimate of Section1. Distinct zeros may be arbitrarily close inside
the disk. The radius construction separates the boundary from poles,
not one zero from every other zero. Count multiplicities only make
the excluded-length bound more conservative.

### 4. The complete contour functional and the remaining interface

Import C744r's complete meromorphic expansion and smooth-domain
pairing, with its source Suzuki, *Aspects of the screw function
corresponding to the Riemann zeta-function*,
[arXiv:2206.03682v4](https://arxiv.org/pdf/2206.03682v4),
Section2.2 p.7 and Sections3.1-3.5 pp.9-11, especially (3.3),
(3.5), Proposition3.1 and the distributional interpretation.
The Fourier-minus and multiplicity specialization is C744r(5),(13)-(14).
It is reused, not reproved. Absolute convergence from Section2
gives |G(s)|<=S/d on Gamma and normal convergence of the full
exterior series on a neighborhood of the closed disk. For example,
each exterior pole is at distance at least d from the disk, so a
d/2 neighborhood has the summable majorant 2|a_z|/d.

Under the stated finite-window nonnegativity assumption, C744s(7)-(8)
applies with this neutral phi, 0<w<ell/2 and 2||phi||_H2<=B.
Its strict-slack perturbations and polarization yield |h(t)|<=C
on [0,H], using only admitted same-profile two-cell tests.
No positivity for independently chosen cell profiles is inserted.
The finite integral J_H is entire and satisfies |J_H(s)|<=C/sigma
on Re(s)>=sigma. This proves (8) including the full exterior sum.

Import the residue theorem from Beck, Marchesi, Pixton and Sabalka,
*A First Course in Complex Analysis*,
[Section8.1, Theorems8.1.5 and8.1.7(1)](https://complexanalysis.org/web/sec_residue-thm.html),
online text inspected in the prior source assessment on 11 November
2026. Gamma is a simple positively oriented circle, its disk is
simply connected, G has finitely many interior simple poles with
residues a_z (multiplicity already in a_z), and there are no boundary
poles. The complete exterior part and J_H are holomorphic on a
neighborhood of the disk. The theorem therefore gives exactly (9).
Together with (7) and the contour-length estimate this proves (10).
There is no weight with hidden poles and no assumed positivity
of the complementary residues.

C744s(10) gives (11) with the present full S. Its proof uses
|h(t)|<=S exp(t/2) and absolute Laplace summation only in Re(s)>1/2;
it does not continue that integral across its convergence boundary.
The boundedness of J_H in the left part uses the finite-window
assumption instead. We have not propagated the small right-half-plane
bound to Gamma. In particular G-J_H has poles inside Gamma, so
C744s's selected-pole function (s-p)(G-J_H) cannot be declared
holomorphic on the whole disk when other cluster poles are present.
The estimate (8) alone is independent of H and does not force a
contradiction for any K. This is the precise unpaid next analytic
interface; no impossibility result for all cluster methods follows.

The pre-existing C645d inverse-Blaschke cancellation example is a
contrast, not an input or a counterexample to (6). Its weighted
synthetic residues are different. The present local phase estimate
also makes no assertion about L717's growing outer kernel. The
profile norm and complete complement are explicitly paid relative
to (1)-(4), preserving the Gram-dual and removed-remainder stops.

### 5. Separate conceptual audit — 11 November 2026, step524

This audit uses the unchanged EXPLORE assessment
`drafts/literature/2026-11-11-actual-cluster-bound-audit-521.md`,
approved in step522 and with primary URLs repaired in step523.
The entire proof above was checked against C744r(5),(8)-(14),
C744s(6)-(11), unconditional L742(8)-(12), and L744(1),(6),(8).
The exact source statements and essential proof cases in the assessment
are reused. This verifies the proposed quantitative specialization;
it neither reproves Suzuki's formula nor imports RH positivity.

1. **Actual factors and phase.** The support lies strictly between
   w/4 and 3w/4, also when tau=w/4, because psi has compact support
   strictly inside (-1,1). Twice integrating by parts gives the two
   zero moments and F_phi=-q F_eta. Reality gives
   conj(F_phi(conj(z)))=F_phi(-z); replacing q(z)^2 by |q(z)|^2
   would be incorrect. The shift x_* cancels in the product.

   For |z-z0|<=2R, |z0|<=T+1/2 and 2R<=1/4 imply |z|<L.
   Thus |q(z)-q(z0)|<=4RL<=kappa/16. The zero strip excludes
   z0=plus/minus i/2, so division by q(z0) is legitimate. In the
   double bump integral, |x-y|<=2tau and both density factors are
   nonnegative with total mass one. Hence |P-1|<=1/31<1/16.
   The full relative error is bounded by

       (17/16)^2/16+33/256 = 817/4096 < 1024/4096.

   In particular Re(conj(omega)a_z)>3kappa^2 r_z/4 throughout
   the closed 2R disk. This proves the stated weak inequality (6),
   nonvanishing at z0, and (7) for every enclosed cluster. It says
   nothing about the phase outside that disk or the size of kappa
   from T,delta alone.

2. **Norms and the entire mass.** The L1 scaling exponent is -j
   and the L2 exponent is -j-1/2. Applying these to
   phi^(j)=eta^(j+2)-eta^(j)/4 for j=0,1,2 gives the upper bound B/2;
   applying the L1 bounds at j=0,2 gives P0 and P2. Each transform
   on the closed zero strip is bounded by e^(w/2)P0, and, when
   z!=0, by e^(w/2)P2/|z|^2. The core includes z=0 if present.

   The core |Re z|<=1 and the disjoint shells
   2^j<|Re z|<=2^(j+1) cover the full set with endpoints once.
   Using the total count for each shell only overestimates its mass.
   The shell multiplier sums to 16/7+(128/49)log(2), which is
   less than 240/49<5. Thus S bounds the complete absolute sum,
   including multiplicity and both height signs. No source count
   on U>=e has been substituted for the assumed count on U>=1.
   No numerical profile seminorm or A has been certified.

3. **Every pole and the closed disk.** R>0, d>0, and the complete
   count at T+1 bounds the number of distinct zeros within 3R by
   N_*. The excluded open radial intervals have total length at
   most 2dN_*<R/2, even with overlaps or repeated multiplicities.
   A point in their complement in [R,2R] has distance at least d
   from every near pole on its circle. Poles farther than 3R are
   at distance greater than R>=d from the circle. Equality at a
   deleted-interval endpoint is harmless because d is positive.

   The closed disk lies in Re(s)>=delta-2R>=sigma. Its interior
   zero set is finite and includes z0. For an exterior pole its
   distance from the closed disk equals its distance from the circle,
   so it is at least d. On the open d/2 neighborhood of the disk,
   the full exterior series has summable majorant 2|a_z|/d and is
   holomorphic by locally uniform convergence. The interior is a
   finite sum of simple fractions, whose residues already include
   multiplicity. Each interior residue is nonzero by item1; exterior
   zero coefficients merely give removable apparent singularities.
   This verifies the cited residue theorem's domain hypotheses,
   including the boundary, without an internal zero gap.

4. **Strict budget and the whole finite horizon.** The finite-window
   portion C744s(6)-(8) needs no pole-clearance chain from that lemma's
   later continuation argument. For the present B, epsilon B<=1/2
   and (1+M0)epsilon B<=Delta/2. Every direction v of H2 norm <=B
   therefore gives nonzero neutral f0+/-epsilon v with L2 norm >=1/2
   and normalized H2 norm strictly below M0. The fixed-cell estimate
   |H(v,v)|<=D||v||_H2^2 follows from neutrality, exp(ell)<2, and
   L744(8). Padded one-cell and same-profile two-cell tests yield
   |q_m(g)|<=H(g,g) for 0<=m<=K-1. The second difference gives

       2 epsilon^2 |q_m(v)| <= 2D(b+1/2)^2+2Db^2.

   Non-Hermitian complex polarization is valid for the sesquilinear
   H(v,tau_(m ell)w'); its four directions v+/-w', v+/-iw' have
   norm <=B whenever ||v||_H2+||w'||_H2<=B. Thus their mixed
   magnitude is bounded by the same C, without assuming positivity
   for independently chosen profiles in different cells.

   For t in [0,(K-1)ell], a nearest integer m to t/ell remains in
   {0,...,K-1}. Its residual has magnitude <=ell/2<ell-w. It is
   the difference of two shifts in [0,ell-w]; the corresponding
   translates of phi have total H2 norm <=B, both neutral moments,
   and compact support uniformly inside the cell. Common-translation
   invariance gives |h(t)|<=C, including both endpoints and m=0.
   The actual smooth generator domains and positive normalizing
   denominators remain those checked in C744r. The integer nature
   of K, already implicit in a K-cell window, is made explicit above.

5. **Complete contour and unpaid propagation.** The absolute mass
   bound gives uniform convergence of h on compact real intervals,
   hence J_H is entire by differentiation under a finite integral.
   On Re(s)>=sigma its magnitude is at most
   C(1-exp(-sigma H))/sigma<=C/sigma. On Gamma the complete G
   is bounded by S/d. The exterior series and J_H integrate to zero
   by holomorphy, so the contour integral is the unweighted sum of
   every interior residue. Taking its rotated real part and then
   using contour length 2pi r gives exactly (9)-(10).

   Separately, sum |a_z exp(itz)|<=S exp(t/2) justifies absolute
   Laplace summation only for Re(s)>1/2. Integrating its tail from H
   proves (11), with no use of the finite-window hypothesis beyond H.
   Nothing propagates that decay to the left part of Gamma. The
   upper bound S/d+C/sigma is independent of H. The sufficient strict
   target sup_Gamma|G-J_H|<alpha/r is still unproved; mere finiteness
   or removal of only the selected pole cannot supply it.

No failed inequality or substantive scope repair was found. This is
local verification of the existing qualified input, with no stronger
estimate, numerical detector, sign theorem or progress beyond the
sources checked asserted. The inverse-Blaschke cancellation, outer
kernel phase, Gram-dual norm and removed-complement stops remain
applicable to their original scopes. Independent actual-Xi signs,
C744q's margin, non-neutral coverage and all-window assembly remain open.

## Mathlib

Full matching coverage of this actual-residue cluster statement has
not been checked. No claim of absence follows. The imported residue
theorem and standard smooth Fourier manipulations are supporting
mathematics, not evidence that this quantitative statement is already
formalized. C744r/C744s retain their existing Mathlib qualifications.
