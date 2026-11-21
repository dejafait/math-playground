# C744s: A conditional finite length from complete spectral certificates

## Hypotheses

Use C744r's complex neutral space N on (0,ell), ell=log(3)/2,
Fourier convention F_v(z)=integral v(x)exp(-izx)dx, complete Hermitian
form H and actual generator energy E_L. In particular N consists of
smooth compactly supported functions whose two exp(plus/minus x/2)
moments vanish, and ||v||_H2^2=sum_(j=0)^2 ||v^(j)||_2^2.
Fix the supplied data

    f0 in N, ||f0||_2=1, b=||f0||_H2<M0, Delta=M0-b>0.       (1)

Let Z be the distinct zeros of Xi, with multiplicities r_z, and suppose
z0 in Z satisfies |Re z0|<=T, -Im z0>=delta, T>=1 and
0<delta<1/2. Put p=i z0. All zeros obey |Im z|<1/2.
This is a hypothetical zero, not an exhibited counterexample to RH.

Choose 0<w<ell/2 and nonzero phi in N supported compactly in (0,w),
as in C744r Section 4, with F_phi(z0)F_phi(conj(z0))!=0. Write

    a_z=r_z F_phi(z)conj(F_phi(conj(z))),
    h(t)=H(phi,tau_t phi)=sum_z a_z exp(itz),
    G(s)=sum_z a_z/(s-iz).                                  (2)

The sum of |a_z| is finite, and G is meromorphic with its complete
complement retained, by C744r. Its selected residue is a_z0.
The quantitative statement requires the following ADDITIONAL certified
numerical data; qualitative finiteness and discreteness do not supply
their numerical values:

* S>0 and alpha>0 with sum_z |a_z|<=S and |a_z0|>=alpha.
* B>0 with 2||phi||_H2<=B.
* An integer n>=1, complex centers c_0,...,c_n and 0<r<=1/8,
  with c_0=1+i Im(p), c_n=p and |c_(j+1)-c_j|<=r.
* For U=union_(j=0)^n {s:|s-c_j|<=4r}, the numbers

      sigma=min_j Re(c_j)-4r > 0,
      R=max_j (|c_j-p|+4r),                                (3)

  and a certified d>0 such that |s-iz|>=d for EVERY s in U and
  EVERY z in Z other than z0. Multiplicity at z0 stays in a_z0.

The last certificate concerns all other zeros, not merely a computed
list or zeros with nonzero coefficients. The first certificate likewise
includes the entire tail. No sign of that tail is assumed. These
certificates are not asserted to follow effectively from T,delta,(1).

## Conclusion

Define the following constants entirely from the displayed data:

    D=4+8sqrt(2)/3+log(4pi),
    epsilon=min{1/(2B), Delta/[2(1+M0)B]},
    C=D[(b+1/2)^2+b^2]/epsilon^2,
    lambda=1/2-r,
    M=S+R(S/d+C/sigma),        Q=R S/lambda,
    H_*=[max{0,log(Q/M)}+2^n log(M/alpha)+1]/lambda,
    K_*=max{2,1+ceil(H_*/ell)}.                            (4)

Then there is a nonzero f in N, with ||f||_H2/||f||_2<M0,
and a nonzero same-profile train U_f supported on at most two occupied
cells of a K_*-cell window such that

    E_(K_* ell)(U_f/||U_f||_2)<0.                           (5)

Thus (4) is an explicit CONDITIONAL length formula. It is not a bound
in T,delta,M0,f0 alone: S,alpha,B and the complete pole-clearance chain
must be certified. No negative numerical margin, actual off-line zero,
finite-window positivity or RH resolution is established. This result
was unaudited at step517; the separate conceptual audit in Section 5
(step519) accepts the formula under exactly the displayed certificates.
POTENTIALLY_NEW records only the prior bounded
source comparison, not an originality claim; the continuation inequality
used below is the standard Hadamard three-circle theorem.

## Proof

### 1. Restrict the existing strict-slack argument to a finite horizon

Fix any integer K>=2 and assume that every admitted same-profile
section with at most two occupied cells in a K-cell window has
nonnegative normalized energy. One-cell tests may be padded by zeros.
For each admitted g and every integer 0<=m<=K-1, C744r's two-by-two
calculation therefore gives

    |q_m(g)|<=d(g),
    q_m(g)=H(g,tau_(m ell)g),       d(g)=H(g,g)>=0.          (6)

For m=0 this is simply |d(g)|=d(g). For m>=1 it follows from the
two-cell coefficients 1 and -q_m(g)/|q_m(g)| when q_m(g)!=0.

Apply C744r(8)-(11) only for these m. For any neutral direction v
with ||v||_H2<=B, both f0+epsilon v and f0-epsilon v have L2 norm
at least 1/2 and normalized H2 norm strictly below M0, since

    M0(1-epsilon B)-(b+epsilon B)>=Delta/2.

The quadratic second difference, the local bound |d(v)|<=D||v||_H2^2,
and the complex polarization identity give

    |H(v,tau_(m ell)w')|<=C
    if ||v||_H2+||w'||_H2<=B,       0<=m<=K-1.             (7)

This is exactly the finite-index restriction of C744r's proof, not
positivity for independent-profile trains. In its polarization step
the four directions v+w', v-w', v+iw', v-iw' all have H2 norm <=B;
only their strict-slack perturbations of f0 are tested for positivity.

Put H_K=(K-1)ell. For each 0<=t<=H_K, choose a nearest integer m
to t/ell in {0,...,K-1}. Its residual t-m ell lies in [-ell/2,ell/2].
As in C744r(12), it equals b0-a for a,b0 in [0,ell-w]. The translates
tau_a phi and tau_b0 phi stay compactly inside the cell, retain both
neutral moments, and have total H2 norm at most B. Translation
invariance in (7) consequently gives

    |h(t)|<=C,                 0<=t<=H_K.                 (8)

The endpoint and m=0 cases are included. No assertion for t>H_K
is made. C744r's domain verification and disjoint-support norm identity
apply unchanged to all the finite trains just used.

### 2. The full finite-horizon Laplace defect

For H=H_K define the entire finite integral J_H and the generally
meromorphic defect F_H by

    J_H(s)=integral_0^H h(t)exp(-st)dt,
    F_H(s)=(s-p)(G(s)-J_H(s)),                             (9)

with the selected singularity in F_H removed. The complete coefficient
bound gives |h(t)|<=S exp(t/2) for t>=0, independent of (8).
For Re(s)>1/2, absolute integral summation, bounded by
S/(Re(s)-1/2), yields the exact identity

    G(s)-J_H(s)=integral_H^infinity h(t)exp(-st)dt.

Hence, writing v=Re(s)-1/2>0,

    |G(s)-J_H(s)|<=S exp(-vH)/v.                          (10)

This is the only region where the infinite Laplace tail is used.
It is not analytically continued as an integral past Re(s)=1/2.
The finite integral J_H is entire by differentiation on its compact
integration interval; (8) gives, for Re(s)>=sigma,

    |J_H(s)|<=C/sigma.                                    (11)

The complete meromorphic tail in C744r and the clearance d show
F_H is holomorphic on a neighborhood of each closed disk in U.
At p it has value a_z0. On U, including p by continuity,

    F_H(s)=a_z0+(s-p)sum_(z!=z0) a_z/(s-iz)-(s-p)J_H(s),
    |F_H(s)|<=S+R(S/d+C/sigma)=M.                         (12)

Uniform convergence of the complementary series follows also directly
from the summable majorant |a_z|/d on U (and a smaller clearance on
a neighborhood). No complementary residue is removed or assigned a
favorable sign. The estimate M is independent of H under (8).

On the starting disk |s-c_0|<=r one has Re(s)-1/2>=lambda>0
and |s-p|<=R. Applying (10) there gives

    max_(|s-c_0|<=r)|F_H(s)|<=Q exp(-lambda H).            (13)

### 3. Quantitative continuation through the certified disks

Use the standard named Hadamard three-circle theorem: if F is
holomorphic on a neighborhood of the closed disk of radius 4r,
and A(t)=max_(|s-c|<=t)|F(s)|, then log A(t) is convex in log t
(with the zero function understood by continuity). In particular

    A(2r)<=sqrt(A(r)A(4r)).

Every disk used here satisfies the holomorphy hypothesis by (12).
Because |c_(j+1)-c_j|<=r, the radius-r disk about c_(j+1) lies
inside the radius-2r disk about c_j. With the common radius-4r bound
M, iterating the displayed inequality n times from (13) gives

    |a_z0|=|F_H(p)|
       <=M^(1-2^(-n)) [Q exp(-lambda H)]^(2^(-n)).         (14)

This is a finite analytic-continuation estimate, not the qualitative
identity-theorem contradiction of C744r. The exponent 2^(-n) and the
resulting potentially large length cost are retained explicitly.
No effective Tauberian theorem, zero-separation theorem or truncated
power-sum estimate is being imported or presumed.

Since M>=S>=|a_z0|>=alpha>0, log(M/alpha)>=0. If H>=H_* in (4),
then

    log(Q/M)-lambda H<=-2^n log(M/alpha)-1.

Thus (14) gives |a_z0|<=alpha exp(-2^(-n))<alpha, a contradiction.
For K=K_* the ceiling ensures H_K>=H_*, including equality.
Consequently the assumed nonnegativity of all admitted two-cell
sections in that window fails. This is exactly (5), with a single
profile strictly inside the prescribed budget. Normalization has a
positive denominator and preserves the sign by C744r(4)-(6).

### 4. What is and is not paid

All-zero absolute mass and all-other-pole clearance enter (12)
explicitly. A bound for only a finite zero list cannot replace either
certificate. Smoothness and discreteness do imply that some such data
exist for a chosen z0 and suitable phi: use a compact path in Re(s)>0
from 1+i Im(p) to p avoiding the other discrete poles, then a sufficiently
small common radius and a finite chain. The path has positive distance
from the complementary closed discrete set and the half-plane boundary.
This observation gives no numerical certificate in the original data.
In particular n and d in (4) are not bounded in terms of T,delta here.

The ready source comparison does not supply those constants. Step517
stops with the conditional estimate, before any unprovided isolation,
tail-count or profile-bound assertion. Certifying its inputs uniformly
would be a further mathematical task requiring its own source scope.
Even an unconditional length bound would need independently proved
finite-window signs before excluding the hypothetical zeros. The main
actual-Xi positivity, non-neutral coverage and all-window assembly remain
unresolved, as does C744q's positive margin.

The complete pairing is reused from C744r, with its precise Suzuki
input: *Aspects of the screw function corresponding to the Riemann
zeta-function*, [arXiv:2206.03682v4](https://arxiv.org/pdf/2206.03682v4),
Section 2.2, printed p.7,
Sections 3.1-3.5, printed pp.9-11, (3.3), (3.5), Proposition 3.1,
and its distributional interpretation. No reproof or new source claim
is made. The standard three-circle theorem is specialized only to the
three radii r,2r,4r; its hypotheses are verified above.

### 5. Separate conceptual audit — 11 November 2026, step519

The prior EXPLORE assessment is
`drafts/literature/2026-11-11-certified-two-cell-length-audit-517.md`,
separately approved in step518. This audit checks (1)-(14) under their
stated certificates, using C744r's audited pairing and strict-slack
argument. Its unconditional L742(8)-(12) and L744(1),(6),(8) inputs
were checked at the relevant ranges. No RH-conditional part of L742,
desired finite-window sign, or effective zero-count theorem is used.

1. **Finite-window quantifiers and the prescribed budget.** For a fixed
   K, the contradiction hypothesis ranges over every nonzero neutral
   profile strictly inside M0 and every section with at most two
   occupied cells among 0,...,K-1. Padded one-cell tests give d(g)>=0.
   For m>=1 the section with coefficients 1 and -q_m(g)/|q_m(g)|
   has unnormalized energy 2(d(g)-|q_m(g)|); this proves (6), with
   q_m(g)=0 and m=0 handled separately. Each such section fits the
   same K-cell window. Normalization never changes its sign.

   The fixed epsilon obeys epsilon B<=1/2 and
   (1+M0)epsilon B<=Delta/2, so every tested perturbation of f0
   has L2 norm at least 1/2 and strict normalized budget below M0.
   The local symbol estimate and neutrality give the fixed D in (4).
   For any direction u of H2 norm at most B the second difference
   therefore yields

       2 epsilon^2 |q_m(u)| <= 2D(b+1/2)^2+2Db^2.

   For first-slot-linear B_m(v,w')=H(v,tau_(m ell)w'), its polarization
   identity is

       4B_m(v,w')=q_m(v+w')-q_m(v-w')
                    +i q_m(v+iw')-i q_m(v-iw').

   It applies even though B_m need not be Hermitian. The four directions
   have norm at most B, proving (7) with precisely C. They are directions
   for strict-slack perturbations, not an assumed positive mixed-profile
   family. All constants are independent of m and K.

2. **Closed continuous horizon.** For 0<=t<=H_K, a nearest integer to
   t/ell belongs to {0,...,K-1}, and its residual e satisfies |e|<=ell/2.
   Choose (a,b0)=(0,e) if e>=0 and (-e,0) otherwise. Both shifts lie
   in [0,ell-w] because w<ell/2. If supp(phi) is contained in
   [u,v] inside (0,w), every such translate stays at least
   min(u,w-v)>0 from the cell endpoints. Its moments remain zero
   and its derivative norms are unchanged. Translation invariance
   gives B_m(tau_a phi,tau_b0 phi)=h(t); hence (8), including t=0
   and t=H_K. This uses no sampling theorem or positivity beyond K.
   C744r's smooth-domain check and disjoint derivative supports still
   apply to every actual train used here.

3. **Entire integral, full complement and uniform bound.** Complete
   absolute coefficient summability makes h continuous on every compact
   real interval and gives |h(t)|<=S exp(t/2) for t>=0. For Re(s)>1/2,
   the integral of the sum of the absolute terms is at most
   S/(Re(s)-1/2). This justifies the exact Laplace identity and its
   tail estimate (10), only in that half-plane. Differentiation under
   the finite integral makes J_H entire. Under (8), its magnitude on U
   is at most C integral_0^H exp(-sigma t)dt<=C/sigma, uniformly in H.

   Take a positive eta<min(d/2,sigma/2). On the open eta-neighborhood
   of U every complementary denominator has modulus greater than d/2.
   The full complementary series consequently converges normally there,
   with majorant 2|a_z|/d. After the selected term is canceled, F_H
   is holomorphic there, including p, with F_H(p)=a_z0. Multiplicity
   is already included in a_z0; no further coincident pole remains in
   the distinct-zero index set. On U itself (12) gives exactly M,
   independently of H under the fixed-window contradiction hypothesis.
   F_H is generally meromorphic elsewhere. The wording before (9)
   has been clarified accordingly; no global holomorphy was used.

4. **Precise three-circle import and iteration.** The source is Harold
   P. Boas, *Math 618: Three-circles theorem*, 23 April 2004,
   [p.1, Section I, (1)-(2)](https://haroldpboas.gitlab.io/courses/618-2004a/apr23.pdf),
   already inspected at the source gate, including both proof cases.
   Its annular holomorphy and boundary-continuity hypotheses hold on
   r<=|s-c_j|<=4r by item 3. The standard maximum-modulus theorem
   identifies the circle suprema with the closed-disk maxima. The
   radii r,2r,4r have logarithmic interpolation weight 1/2. No zero-free
   hypothesis is required, and the multiplicative inequality includes
   a zero maximum by continuity.

   On the initial radius-r disk, Re(s)-1/2>=1/2-r=lambda>0,
   and |s-p|<=R, giving (13). If A_j is the radius-r maximum at c_j,
   disk inclusion and three circles give A_(j+1)<=sqrt(M A_j).
   Exactly n inclusions therefore give

       A_n <= M^(1-2^(-n)) [Q exp(-lambda H)]^(2^(-n)).

   Since c_n=p, this is (14). The common bound M covers every
   radius-4r disk, including the whole complement. It is not a bound
   inferred from a finite list. This use is a specialization of the
   named theorem, not a reproof or an effective Tauberian import.

5. **Strict threshold and conclusion.** The certificates imply
   Q>0, M>=S>=|a_z0|>=alpha>0 and lambda>0, so H_* is finite
   and positive. For H>=H_*,

       log(Q/M)-lambda H
         <= log(Q/M)-max{0,log(Q/M)}-2^n log(M/alpha)-1
         <= -2^n log(M/alpha)-1.

   Taking logarithms of the positive right side in (14) bounds it
   by log(alpha)-2^(-n), strictly below log(alpha). This contradicts
   |a_z0|>=alpha even at H=H_*. The ceiling in (4) gives
   (K_*-1)ell>=H_*; no extra cell or strict rounding is needed.
   Failure of the universal fixed-window nonnegativity assumption
   supplies one finite negative same-profile section inside the
   strict budget. It does not merely supply a limiting zero energy.

The audit accepts (4)-(5) without changing a hypothesis, constant,
inequality or conclusion. The only correction is the domain wording
before (9). The qualitative path observation in Section 4 is also
consistent: the complementary pole set is closed and discrete, a
compact path in Re(s)>0 can avoid it, and sufficiently small common
disks and a finite subdivision then have positive clearance. That
existence statement provides no certified numerical S, alpha, B, d,
sigma or n. Thus this is local verification of the existing conditional
result, not a new result beyond its derivation or a numerical detector.
Uniform certificates, independent finite-window signs, the C744q margin,
non-neutral coverage and all-window assembly remain unresolved.

## Mathlib

Full matching formal coverage of the conditional detector and the exact
disk-chain specialization has not been checked. The named Hadamard
three-circle theorem is a standard supporting result, not a claim that
Mathlib contains this complete argument. C744r's source-specific
pairing and generator qualifications remain in force. No absence claim
or computational verification of the additional certificates is made.
