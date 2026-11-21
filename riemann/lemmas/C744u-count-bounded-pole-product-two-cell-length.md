# C744u: A qualified two-cell length without internal pole separation

## Hypotheses

Retain all data and conventions of C744t(1)-(4), including its
unconditional complete Hermitian form and actual generator energy.
Explicitly, Z is the set of distinct zeros of Xi(z)=xi(1/2+iz),
with multiplicities r_z and |Im(z)|<1/2. A hypothetical z0 in Z satisfies

    |Re(z0)|<=T, -Im(z0)>=delta, T>=1, 0<delta<1/2.

Write p=iz0, t0=Im(p)=Re(z0), and kappa=|z0^2+1/4|>0. Supply
A>=1 with the COMPLETE two-sided count, including multiplicities
and endpoints,

    sum_(|Re(z)|<=U) r_z <= A U log(eU), U>=1.             (1)

Retain C744t's nonnegative integral-one smooth bump psi, its supplied
seminorms, tau, and neutral real profile phi supported in (0,w),
w=ell/4, ell=log(3)/2. Retain its explicit positive constants B,S,C
and the strict-slack data

    f0 in N, ||f0||_2=1, b=||f0||_H2<M0, Delta=M0-b>0,

where N is the space of complex C_c^infinity(0,ell) functions with
both exp(plus/minus x/2) moments zero, and
||f||_H2^2=sum_(j=0)^2 ||f^(j)||_2^2. In particular S is the
complete absolute residue bound in C744t(2),(5), and C is exactly
the strict-slack bound in C744t(4),(8), not an independent positivity
assumption. Define, as in C744t,

    R=min{delta/4,1/8,kappa/[64(T+2)]},
    N_*=ceil(A(T+1)log(e(T+1))),
    d=R/[4(N_*+1)], alpha=3kappa^2/4.                    (2)

All these data remain qualifications. No numerical count constant,
positive lower certificate for kappa, or profile seminorm certificate
is constructed here. No off-line zero is exhibited. No internal
separation, rightmost zero, or finite off-line census is assumed.

## Conclusion

The following finite constants depend only on the displayed supplied
data and C744t's explicit S,C:

    N_P=ceil(A(T+2)log(e(T+2))),
    rho=delta/32, n=ceil(1/rho), lambda=1/2-rho,
    M=S+4C/delta, Q=S/lambda,
    mu=(d/4)^N_P, beta=alpha mu/(2R),
    H_*=[max{0,log(Q/M)}+2^n log(M/beta)+1]/lambda,
    K_*=max{2,1+ceil(H_*/ell)}.                           (3)

There is a nonzero f in N with ||f||_H2/||f||_2<M0 and a nonzero
vector (c_0,...,c_(K_*-1)) with at most two nonzero entries such that

    U(x)=sum_(j=0)^(K_*-1) c_j f(x-j ell),
    E_(K_* ell)(U/||U||_2)<0.                            (4)

The proof establishes a uniform whole-contour estimate under the
contrary, finite-window nonnegativity assumption. For C744t's
count-selected r in [R,2R] and Gamma={s:|s-p|=r}, it gives, for
H=(K-1)ell,

    sup_Gamma |G-J_H|
       <=mu^(-1) M^(1-2^(-n)) [Q exp(-lambda H)]^(2^(-n)). (5)

At H>=H_* this is at most

    alpha exp(-2^(-n))/(2R) < alpha/r,                   (6)

contradicting C744t's original UNWEIGHTED cluster integral. The
product used to prove (5) includes every potential pole in a padded
propagation domain; its full infinite complement is bounded, not
deleted. Its division cost mu^(-1) is explicitly paid.

This removes C744s's additional all-other-pole-clearance chain from
this qualified detector construction. The length is explicit in
the supplied symbolic data and does not depend on locating the
product's factors or the radius r numerically. It is not a numerical
zero-location certificate, a bound from T,delta alone, a negative
energy margin, or independent finite-window positivity. Actual-Xi
positivity, C744q's margin, non-neutral coverage and global assembly
remain open. The separate step528 conceptual audit in Section6 accepts
this step526 specialization under its unchanged hypotheses and constants;
it is not an RH candidate. Classification REPRODUCTION records
an application of the assessed standard analytic tools and makes no
originality claim.

## Proof

### 1. Fix the finite-window contradiction and import its exact bounds

Fix an integer K>=2 and suppose every admitted same-profile train
with at most two occupied cells in this K-cell window has nonnegative
normalized actual energy. Admission includes nonzero f in N with
strict ratio ||f||_H2/||f||_2<M0. Use C744t(5)-(11), whose separate
step524 audit checks precisely this assumption and the complete count.
In its Fourier-minus convention, put

    a_z=r_z F_phi(z)conj(F_phi(conj(z))),
    h(t)=sum_z a_z exp(itz), G(s)=sum_z a_z/(s-iz),
    J_H(s)=integral_0^H h(t)exp(-st)dt, H=(K-1)ell.

The imported statements give sum_z |a_z|<=S, |h(t)|<=C on [0,H],
and an entire J_H. Thus for any positive a,

    |J_H(s)|<=C/a when Re(s)>=a.                          (7)

The complete Laplace-tail identity is used only in Re(s)>1/2,
where C744t(11) gives

    |G(s)-J_H(s)|
       <=S exp(-(Re(s)-1/2)H)/(Re(s)-1/2).               (8)

C744t also supplies r in [R,2R] whose whole circle has distance
at least d from EVERY iz. Its interior cluster contains z0, and,
with omega=(z0^2+1/4)^2/kappa^2 and |omega|=1,

    Re(conj(omega) sum_(|iz-p|<r) a_z)>=alpha m_r>=alpha,
    (1/(2pi i)) integral_Gamma (G-J_H)(s)ds
         =sum_(|iz-p|<r) a_z.                            (9)

Here m_r is the cluster's total multiplicity. No sign or phase of
any complementary residue is an input. In particular |a_z0|>=alpha,
so S>=alpha>0.

These are uses of the accepted C744t estimates, not reproofs of the
compact-smooth Weil formula. The underlying precise import remains
Suzuki, *Aspects of the screw function corresponding to the Riemann
zeta-function*, [arXiv:2206.03682v4](https://arxiv.org/pdf/2206.03682v4),
Section2.2 p.7 and Sections3.1-3.5 pp.9-11, especially (3.3),(3.5)
and Proposition3.1 with its distributional interpretation. The
unconditional pairing and smooth domains are already specialized
in C744r and used by C744t. No RH-conditional square formula is used.

### 2. Cancel a complete count-bounded band and pay its full complement

Let

    U={s: delta/4<=Re(s)<=2, |Im(s)-t0|<=1},
    V={s: delta/8<Re(s)<3, |Im(s)-t0|<3/2},
    Z_P={z in Z: |Re(z)-t0|<=2}, m=|Z_P|,
    P(s)=product_(z in Z_P) (s-iz)/4.

U is compact and lies in the open padded domain V. Every pole in V
is among these factors. Since |t0|<=T, all members of Z_P satisfy
|Re(z)|<=T+2; (1) therefore gives 1<=m<=N_P. The lower bound
holds because z0 belongs to Z_P. Each DISTINCT zero occurs once
in P: G has at most a simple pole at iz, and multiplicity is already
in a_z. Include also zeros with a_z=0; an extra factor is harmless.

For s in U and z in Z_P, the zero strip gives

    |Re(s)-Re(iz)|<5/2, |Im(s)-Im(iz)|<=3,
    |s-iz|<sqrt(25/4+9)=sqrt(61)/2<4.                    (10)

Consequently |P(s)|<=1 and the polynomial obtained by removing any
one factor satisfies

    |P(s)/(s-iz)|<=1/4, z in Z_P, s in U,                (11)

including s=iz by its polynomial extension. For z outside Z_P,
the imaginary-coordinate separation instead gives |s-iz|>1 on U
and |s-iz|>1/2 throughout V. Hence the ENTIRE exterior series

    G_ext(s)=sum_(z not in Z_P) a_z/(s-iz)

converges normally on V, with summable majorant 2|a_z|, and is
holomorphic there. Finite local pole cancellation is the standard
factorization theorem, Beck, Marchesi, Pixton and Sabalka,
*A First Course in Complex Analysis*,
[Section7.4, Theorem7.4.8](https://complexanalysis.org/web/sec_singularities.html).
Its punctured-disk hypothesis holds at each of the finitely many
at-most-simple poles; removable terms need no pole theorem.
No meromorphy-at-infinity or rationality statement is invoked.
In the present specialization the holomorphic extension is explicitly

    F_H(s)=P(s)(G(s)-J_H(s))
          =sum_(z in Z_P) a_z P(s)/(s-iz)
             +P(s)G_ext(s)-P(s)J_H(s), s in V.           (12)

The complete sums, (7), and (10)-(11) give on U

    |F_H(s)|
       <=(1/4)sum_(Z_P)|a_z|+sum_(Z\Z_P)|a_z|+4C/delta
       <=S+4C/delta=M.                                  (13)

This M is independent of H under the fixed-window assumption.
No residue separation appears, and no exterior term was discarded.
The elementary estimates (10)-(13) are the specialization missing
from the imported factorization theorem; that theorem alone would
not provide them.

### 3. A finite cover of every point of Gamma and its common disk bound

Set c=1+it0. Since delta<=Re(p)<1/2 and r<=2R<=delta/2,
every s in Gamma satisfies

    delta/2<=Re(s)<3/4,
    |Im(s)-t0|<=2R<=1/4,
    |s-c|<=1-Re(p)+r<=1-delta/2<1.                      (14)

Choose J=ceil(2pi r/rho) points
s_j=p+r exp(2pi i j/J), j=0,...,J-1. For every point of Gamma,
the shorter arc to one of these points has length at most
pi r/J<=rho/2; Euclidean distance is at most arc length. Thus the
closed radius-rho disks about s_j cover ALL Gamma, including the
case J=1. Moreover J<=ceil(4pi R/rho)<=ceil(32pi), so this is
a finite cover with an explicit uniform cardinality bound.

For each j, join c to s_j by the centers

    c_(j,k)=c+(k/n)(s_j-c), k=0,...,n.

Their consecutive distances are <1/n<=rho by (14) and the choice
n=ceil(1/rho). Every center has real part in [delta/2,1] and
imaginary-coordinate distance at most 1/4 from t0. Hence every
closed radius-4rho disk about any center lies in U: indeed

    Re(s)>=delta/2-4rho=3delta/8>delta/4,
    Re(s)<=1+4rho=1+delta/8<2,
    |Im(s)-t0|<=1/4+4rho=1/4+delta/8<1.

The extension F_H is therefore holomorphic on a neighborhood of
each such closed disk, with the SAME radius-4rho bound M in (13).
In particular this covers the initial radius-rho disk about c,
where Re(s)-1/2>=lambda>0. Since |P|<=1 there, (8) yields

    sup_(|s-c|<=rho)|F_H(s)|<=Q exp(-lambda H).           (15)

Import Hadamard's three-circle theorem in the disk-maxima form:
holomorphy on a neighborhood of the closed radius-4rho disk gives
A(2rho)<=sqrt(A(rho)A(4rho)). A precise inspected source is
Boas, [*Math618: Three-circles theorem*, 23 April2004](https://haroldpboas.gitlab.io/courses/618-2004a/apr23.pdf),
p.1 SectionI(1)-(2) and proof discussions1-2. The maximum principle
changes circle maxima to disk maxima; zeros of F_H are allowed.
This known theorem is not reproved. Its hypotheses have just been
verified for every disk used here.

The next radius-rho disk lies in the current radius-2rho disk.
After n such steps, (13),(15) and the theorem therefore give, on
each endpoint disk,

    |F_H(s)|<=M^(1-2^(-n))[Q exp(-lambda H)]^(2^(-n)).    (16)

The zero-function case satisfies the same inequality directly.
Because the endpoint disks cover the whole circle, (16) bounds its
supremum; there is no sum over disks and no unpriced covering loss.

### 4. Divide on Gamma and meet the unweighted threshold

C744t's distance d is from EVERY pole, including every factor of P.
Therefore on Gamma,

    |P(s)|>= (d/4)^m >= (d/4)^N_P=mu>0,                 (17)

because m<=N_P and 0<d/4<1. No lower bound is claimed inside the
circle, where P vanishes. Dividing (16) only on Gamma proves (5).
In particular no weighted-residue sum is required to have a sign.

All logarithms in (3) are legitimate, with lambda>0, M>0, Q>0.
Also N_P>=1, 0<d/4<1, and

    beta=alpha mu/(2R)
       <=alpha d/(8R)=alpha/[32(N_*+1)]<alpha<=S<=M.     (18)

Thus log(M/beta)>0 and H_*>0. For any H>=H_* the exact formula
gives

    log(Q/M)-lambda H <= -2^n log(M/beta)-1.

Substituting this into (16) bounds sup_Gamma |F_H| by
beta exp(-2^(-n)); division by mu gives (6). Using (9), the
ordinary contour-length bound now yields the contradiction

    alpha <=alpha m_r
       <=|sum_(|iz-p|<r) a_z|
       <=r sup_Gamma |G-J_H|
       <=alpha [r/(2R)] exp(-2^(-n))<alpha.              (19)

The residue identity in (9) remains the original one from C744t,
whose precise source is Beck et al.,
[Section8.1, Theorems8.1.5 and8.1.7(1)](https://complexanalysis.org/web/sec_residue-thm.html).
Its circle is positively oriented, avoids all poles, and has only
finitely many interior poles; the full exterior and J_H are
holomorphic near its disk. We do not integrate F_H as a substitute
for that identity.

Taking K=K_* ensures H=(K_*-1)ell>=H_* by the ceiling in (3),
even at equality. Consequently nonnegativity cannot hold for all
admitted same-profile trains with at most two occupied cells in
that window. Its negation is exactly (4). The strict-budget
perturbations, finite horizon including its endpoints, smooth
generator domain, and positive normalization denominator are
the unchanged finite-window implication already verified in C744t;
no positivity of mixed independent-profile trains is assumed.

### 5. Scope of the gain and surviving stops

The count, not a finite computed zero list, bounds the complete
product degree. The propagation domain and constants are independent
of H. All factors, the infinite exterior, the whole circle and the
division loss are paid. Internal pole gaps may tend to zero without
altering (3); dependence on kappa, A, bump costs and strict slack
has not been removed. Although a particular product and r enter
the existence proof, their locations do not enter the stated upper
length formula. Specifying a finite actual numerical length still
requires certified input data and controlled evaluation of (3).

C645d's inverse-Blaschke cancellation is a contrast, not a premise:
this argument never asks for a positive weighted residue. The
Gram-dual norm stop is not evaded; C744t's B and C pay narrowing
and strict-slack perturbations. The removed-remainder stop is
respected by (12)-(13) and the complete unweighted identity (9).
No log-height efficiency is claimed, so the earlier fixed-geometry
Cartan coefficient failure is not contradicted. The bound can be
extremely large and supplies no sign for any finite window.

The prior SPECIALIZE assessment is
`drafts/literature/2026-11-11-cluster-pole-product-test-525.md`.
Its completed source comparison is reused without a new search.
The local work here is the explicit domain, degree, norm, covering
and division estimate connecting those standard inputs. It is
not a new general continuation theorem or a claim of originality.

### 6. Separate conceptual audit — 12 November 2026, step528

The prior SPECIALIZE assessment
`drafts/literature/2026-11-11-count-bounded-pole-product-audit-526.md`
was separately approved in step527. This audit checks (1)-(19),
including the inherited finite-window interface, without adding
hypotheses or changing a constant. The precise standard sources in
Sections1-4 and the completed step525 theorem/duplicate comparison
are reused. No general continuation theorem is reproved. All claims
below are verifications of the proposed proof, not stronger estimates.

1. **Finite-window assumption, strict admission and full series.**
   The assumption is nonnegativity for EVERY admitted profile and
   every nonzero coefficient vector with at most two occupied cells
   in this ONE K-cell window. It includes padded one-cell tests.
   For 0<=m<=K-1 these give |q_m(g)|<=d(g), in the notation of
   C744s(6). Inherited C744t(4) has epsilon B<=1/2 and
   (1+M0)epsilon B<=Delta/2. Consequently every perturbation
   g_+=f0+epsilon v and g_-=f0-epsilon v with ||v||_H2<=B satisfies

       ||g_+||_2, ||g_-||_2 >= 1/2,
       b+epsilon B < M0(1-epsilon B).

   Both perturbations are strictly admitted, including when a
   minimum defining epsilon is attained. The quadratic second
   difference and |H(v,v)|<=D||v||_H2^2 give exactly

       2epsilon^2 |q_m(v)|
          <=2D(b+1/2)^2+2Db^2=2epsilon^2 C.

   Complex polarization uses the four directions v+/-w', v+/-iw';
   each has norm <=B when ||v||_H2+||w'||_H2<=B. This bounds the
   mixed pairing by C without assuming mixed-profile positivity.
   For every t in [0,(K-1)ell], a nearest index remains in
   {0,...,K-1}; its residual is in [-ell/2,ell/2]. Since w=ell/4,
   two shifts in [0,ell-w] realize that residual. Their translates
   of phi remain neutral and compactly inside the cell, with total
   H2 norm <=B. This verifies |h(t)|<=C at every t, including both
   endpoints. C is independent of K; no estimate past this horizon
   is inferred from the finite-window assumption.

   The inherited complete sum has sum |a_z|<=S and
   |h(t)|<=S exp(t/2) for t>=0, without that assumption. Absolute
   Laplace summation therefore justifies (8) only in Re(s)>1/2.
   Differentiating the finite integral on compact s sets proves
   J_H entire and (7). No infinite integral is continued to the
   left half of the propagation region. These checks use the
   unconditional pairing in C744r(5),(13)-(14), as imported in
   C744t; no conditional square representation from L742 is used.

2. **Padded domain, multiplicities and every exterior term.**
   The complete count at U=T+2 bounds the band's total multiplicity,
   so its number m of distinct zeros obeys 1<=m<=N_P. The lower
   bound follows from z0 in the band. A multiple Xi zero still
   contributes one simple fraction to G; its multiplicity is in
   a_z. One factor per distinct zero is therefore sufficient.
   A zero coefficient causes only an extra harmless factor.

   For every s in V and every zero outside Z_P, the imaginary
   coordinate gives |s-iz|>2-3/2=1/2. The full exterior series is
   thus normally convergent on V by the summable majorant 2|a_z|.
   Every possible pole in V lies in the canceled band. The finite
   polynomials P(s)/(s-iz) in (12) supply the removable values,
   so F_H is holomorphic on the OPEN neighborhood V of U.

   On U the factor bound is |s-iz|<sqrt(61)/2<4. Removing one
   normalized factor leaves modulus <=1/4 for P(s)/(s-iz),
   not merely a bound away from its apparent singularity. For
   exterior terms the stronger U separation is >1. Along with
   |P|<=1 and Re(s)>=delta/4, these prove precisely M=S+4C/delta
   in (13). Uniform boundedness is needed on U, not on all V;
   holomorphy on V supplies neighborhoods for the closed disks.
   No uncounted boundary pole or infinite complement is omitted.

3. **All of Gamma and all enlarged disks.**
   C744t's count-selected circle avoids EVERY zero point iz by d,
   has r in [R,2R], and satisfies (14), using
   delta<=Re(p)<1/2 and 2R<=min(delta/2,1/4).
   For J=ceil(2pi r/rho)>=1 the shorter-arc distance from any
   point on Gamma to a selected center is <=pi r/J<=rho/2.
   This remains true when J=1. Also J<=ceil(32pi), since
   R<=delta/4 and rho=delta/32. Thus the endpoint disks cover
   the complete circle, not merely a selected arc.

   On each straight path the centers have real parts in
   [delta/2,1] and imaginary displacement at most 1/4. The
   radius-4rho disks lie strictly inside U by the three displayed
   bounds in Section3. Since |s_j-c|<1 and n=ceil(1/rho), every
   hop is <1/n<=rho. The next closed rho disk is contained in
   the current closed 2rho disk. The same M controls every
   radius-4rho disk, and each is in the holomorphy neighborhood V.

   The initial rho disk has Re(s)-1/2>=lambda>0, so its bound
   is Q exp(-lambda H). The cited Hadamard theorem gives the
   recurrence A_(k+1)<=sqrt(M A_k). After exactly n hops this
   is (16), with exponent 2^(-n), for EACH endpoint disk. Taking
   the supremum over a finite cover adds no factor J. A zero
   function satisfies the same estimate directly; zeros introduced
   by P do not violate the imported three-circle theorem.

4. **Division, logarithms and the strict threshold.**
   The selected contour has distance >=d from every factor, so
   |P|>0 on it. Because 0<d/4<1 and m<=N_P, the direction
   (d/4)^m >= (d/4)^N_P is correct. Division only on Gamma
   proves (5) with exactly mu^(-1). No assertion about a
   positive weighted residue sum or an interior lower product
   bound is required.

   Inherited C744t(6) at z0 gives |a_z0|>=alpha r_z0>=alpha,
   hence S>=alpha>0. Also N_P>=1, lambda=1/2-rho>0,
   Q>0 and M>0. Since mu<=d/4, the exact substitution

       beta <= alpha d/(8R)=alpha/[32(N_*+1)] < alpha <= M

   verifies (18), log(M/beta)>0 and H_*>0. Put theta=2^(-n).
   For H>=H_*,

       log(Q/M)-lambda H
          <= -theta^(-1)log(M/beta)-1.

   The logarithm of the positive upper expression in (16)
   is therefore <=log(beta)-theta. This statement does not
   take a logarithm of F_H or assume that it is nonzero.
   Dividing by mu gives exactly alpha exp(-theta)/(2R),
   strictly below alpha/r even when r=2R or H=H_*.
   Although theta can be extremely small, it is strictly
   positive for every admitted delta, so the strictness is real.
   This is a symbolic bound, not a floating-point certificate.

5. **Original residues, integer horizon and quantifier negation.**
   The contour functional is (9) for the ORIGINAL G-J_H.
   C744t already supplies its finite interior cluster, full
   holomorphic exterior and positive projected mass alpha m_r.
   Thus its modulus is at least alpha m_r and at most
   r sup_Gamma|G-J_H|. Item4 makes the latter strictly less
   than alpha, yielding (19). Integrating the holomorphic
   canceled product instead would not give this contradiction.

   The displayed K_* is a finite integer >=2 and satisfies
   (K_*-1)ell>=H_*; no strict ceiling or additional cell is
   needed. The contrary assumption for this specific window
   therefore fails. Its negation is a nonzero strictly admitted
   f and nonzero at-most-two-cell vector with negative energy,
   as in (4), not merely a sequence approaching zero energy.
   Energy is real by the inherited Hermitian pairing. Smooth
   disjoint supports give

       ||U||_2^2=||f||_2^2 sum_j |c_j|^2>0,
       ||U/||U||_2||_H2=||f||_H2/||f||_2<M0,

   and the train lies in the actual smooth generator domain.
   The count-selected r and the band factors need only exist;
   the upper horizon formula uses their count and clearance
   bounds, not their numerically known locations.

No failed inequality, missing hypothesis or mathematical repair was
found. C744t remains the sole direct lemma input: the inherited
C744r/C744s/L742/L744 interfaces checked above enter through it.
The independent strict-budget and numerical input qualifications
remain essential. This accepts a previously unaudited local
specialization of standard methods; it establishes no new theorem
beyond the sources checked, no independent finite-window signs,
no C744q margin, and no RH candidate. The earlier inverse-Blaschke,
Gram-dual, removed-complement and optimized Cartan stops remain in
their original scopes.

## Mathlib

Full matching Mathlib coverage of this qualified count-bounded
two-cell length has not been checked. Unknown coverage is not
absence. The cited pole-factorization, three-circle and residue
theorems are supporting standard mathematics, not evidence that
this exact quantitative specialization is already formalized.
C744t's imported pairing and smooth-domain qualifications remain.
