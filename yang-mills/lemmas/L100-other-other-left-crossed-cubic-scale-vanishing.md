# L100 — The left crossed generator orientation vanishes at cubic scale

## Hypotheses

Use L093's exact R_L for SU(2), both actual L010 probes i=3,6,
L018's residual, the straight lower-rooted direction-1 forest,
relative all-face fixed-link box (-4,4)^4, sufficiently fine admitted
even N, a=8/N and tau=1/16. Take the bare small-coupling coefficient
at fixed mesh before refinement. Coordinates, transposes and norms
are ordinary stored ones. Keep all interior axial levels, transverse
end rows, ordered plaquette pairs including coincidences and the full
exterior heat sum.

On the interior transverse-link space E import L088's actual skew
matrices Omega_k and real coefficients c_(i;kl,a). Use L093's maps
and write P=Pcal, Q=Qcal, T=Tcal here. Thus

    Delta_E=L_D tensor I+I tensor Delta_T,
    K=K_h=Delta_E^(-1) Q,
    Omega_(gh,k)=P Omega_k Q, Omega_(hh,k)=Q Omega_k Q,
    A=H_g K_a I_T,
    R_L=sum_(k,l)c_(i;kl,a)
             Tr(K Omega_(gh,k)^T A K Omega_(hh,l)).       (1)

P and Q are fixed selectors in an already differentiated contraction.
K commutes with them and with Delta_E. K_a retains L009's actual
endpoint/clover filters and compact displacement. No projection
identity is differentiated, and no variable coefficient is commuted
through a projection or covariance.

## Conclusion

For both actual probes,

    lim_(N->infinity) a^3 R_L=0.                         (2)

This removes one orientation of L093's co-closed-base crossed pair
at cubic scale. Together with its existing a^3 R_Q -> 0, it leaves
the reverse orientation R_R unchanged as a leading-scale obligation.
It supplies neither an O(N^2) bound nor a finer coefficient.

The transverse H generator and R_R still lack cubic control. The
E diagonal and gradient-base crossed pair still lack scaled limits,
and the H axial and curvature functionals remain unevaluated. No joint
limit -4 gamma D_i before the outside factor 3, or compensation of
L084's mixed coefficient, follows. Other response jets, finer powers
and logarithm, matching, interacting error <=c_box/2, continuum axioms,
reflection positivity, infrared control and finite positive mass
remain unresolved. No Yang–Mills candidate is asserted.

## Proof

### 1. Cubic-scale resolvent regularization in the actual trace order

Import L093's ||A||<=C/a. Enlarge the fixed mode polynomial p from
L088/L090 when needed; all estimates below retain

    sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i.                  (3)

Write Omega_k=F_k+H_k as in L089, with F_k the actual two
exterior-circulation terms. Bounded path multiplicity and L088 give
||F_k||<=C a^2 p(k). For Pi_eta=1_(Delta_E<=eta),
0<eta<=1, L090(8)--(11) therefore imply

    ||Omega_k K||_HS<=C p(k) N,
    ||Omega_k K Pi_eta||_HS
                   <=C p(k) N [sqrt(eta)+beta_N],
    beta_N=sqrt(log(eN)/N)+sqrt(log(eN))/N ->0.          (4)

Indeed the H_k terms are exactly L090(11), including staggered
boundary collars. The F_k terms are at most
C a^2 p(k)||K||_HS<=C p(k)sqrt(log(eN)), by L089(6),
and this fits the N beta_N allowance for the low part as well.
These bounds use the full four-dimensional relative spectrum.

For epsilon>0 put R_epsilon=(Delta_E+epsilon I)^(-1) and
K_epsilon=R_epsilon Q. The exact difference is

    K-K_epsilon=K epsilon(Delta_E+epsilon I)^(-1).

Its low part has a contraction on the right; its complementary
part has norm at most epsilon/eta. Equations (4) give

    ||Omega_k(K-K_epsilon)||_HS
        <=C p(k)N [sqrt(eta)+beta_N+epsilon/eta].        (5)

The same bounds apply to the left products in (1). For example
K Omega_(gh,k)^T=K Omega_k^T P and its transpose is
P Omega_k K. For the hh factor use KQ=K and skew-symmetry of
Omega_k. The fixed projections are contractions; there is no
commutation through Omega_k. Replacing K by K_epsilon only
decreases these Hilbert–Schmidt bounds, since
K_epsilon=K Delta_E(Delta_E+epsilon I)^(-1).

Let R_L,epsilon replace both K occurrences in (1) by K_epsilon,
leaving every other factor unchanged. Expand the difference at
these two positions and use, in their exact order,

    |Tr(X A Y)|<=||X||_HS ||A|| ||Y||_HS.

Using (3)--(5) and ||A||<=C/a gives

    limsup_N |a^3(R_L-R_L,epsilon)|
                          <=C_i [sqrt(eta)+epsilon/eta]. (6)

Here a^3 N^2/a is bounded since aN=8. Taking eta=sqrt(epsilon)
for 0<epsilon<=1 makes this error tend to zero with epsilon. This
is a uniform cubic-scale error; it differs from the undifferentiated
prefix error in the transverse H trace. It does not choose a mass
depending on N or approximate a singular inverse in operator norm.

### 2. The complete prefix coefficient commutator is subleading

Keep L093's pinned interval notation n=N-1,
S=B C_1^T, (T_1 x)_j=(x_(j+1)-x_(j-1))/2 and
H_av=(2I+S_++S_-)/4, with x_0=x_N=0. For
U_mu=M_(u_(a,mu)) on the interior vertex array, L093(6),(8)
give the exact identity

    a A=A_loc+E_pref,
    A_loc=P(a G0)-T sum_(mu=2)^4 H_av U_mu C_mu,
    E_pref=-T sum_(mu=2)^4 S[U_mu,T_1] C_mu,
    G0=I_T^T K_a I_T.                                 (7)

Axial maps are tensored with the transverse vertex identity;
C_mu averages transverse mu-edges onto vertices. The order of
H_av, U_mu and C_mu is as displayed. Compact displacement support
gives u_(a,mu)(1,y)=0, so L093's retained lower-end term
-(1/2)1 e_1^T U_mu is exactly zero. The pinned upper value remains
in H_av. No endpoint or prefix row has been omitted.

Both ||A_loc|| and ||E_pref|| are bounded uniformly in N. For the
former use ||aG0||<=C, ||P||=1, ||T||<=sqrt(12),
||H_av||,||C_mu||<=1 and bounded displacement. For the latter
use ||S||<=N and ||[U_mu,T_1]||<=Ca from L093.
In addition there is a smaller Hilbert–Schmidt bound

    ||E_pref||_HS<=C N^(3/2).                           (8)

To prove it, fix one transverse vertex y. The commutator has at
most two entries in each column, each bounded by Ca. The entries
of S are 0,1/2 or 1. Hence every entry of the n by n matrix
S[U_mu,T_1] at y is bounded by 2Ca. Its squared Hilbert–Schmidt
norm is at most C a^2 n^2. There are (N-1)^3 transverse vertex
columns; these matrices form their direct sum. Thus the squared
norm on the full vertex array is at most C a^2 N^5<=C' N^3.
Multiplication by the bounded T and C_mu, and summation over three
components, prove (8). This counts the full prefix, including its
tail beyond coefficient support and both end rows. It assumes no
decay or cancellation of that tail.

Fix epsilon>0. The entire Omega_k has ||Omega_k||<=Ca p(k):
use L088's bounded path/circulation maps and coefficient bounds,
with a bounded for the F_k term. Also dim E<=3N^4 and
||K_epsilon||<=1/epsilon. In particular

    ||K_epsilon Omega_(gh,k)^T||<=C_epsilon a p(k),
    ||K_epsilon Omega_(hh,l)||_HS
                               <=C_epsilon a p(l)N^2.

Let R_loc,epsilon be R_L,epsilon with A replaced by A_loc/a.
The Schatten product inequality in the same trace order gives

    |R_L,epsilon-R_loc,epsilon|
      <=sum |c_(i;kl,a)|
         ||K_epsilon Omega_(gh,k)^T||
         ||E_pref/a||_HS ||K_epsilon Omega_(hh,l)||_HS
      <=C_(i,epsilon) a N^(7/2)
      <=C'_(i,epsilon) N^(5/2).                        (9)

Consequently its a^3-scaled value tends to zero at each fixed
epsilon. This does not claim that the prefix commutator is small
in operator norm. Mass removal occurred first in (6), using the
whole A, so (9) needs no estimate uniform as epsilon tends to zero.

### 3. Regularize all projections after the resolvent

Put Omega_tilde_k=Omega_k/a and G_tilde=aG0. Formula (1),(7)
gives exactly

    a^3 R_loc,epsilon
      =a^4 sum_(k,l)c_(i;kl,a)
        Tr(K_epsilon Omega_tilde_(gh,k)^T
                             A_loc K_epsilon Omega_tilde_(hh,l)).
                                                               (10)

All displayed factors have uniform operator bounds at fixed
epsilon, with a factor p(k) or p(l) for each exterior column.
Define

    P_delta=T(I_ax tensor (Delta_0+delta I)^(-1))T^T,
    Q_delta=I-P_delta,
    K_(epsilon,delta)=R_epsilon Q_delta,
    A_loc,delta=P_delta G_tilde
                           -T sum_mu H_av U_mu C_mu.     (11)

Use P_delta Omega_tilde_k Q_delta and
Q_delta Omega_tilde_l Q_delta in place of the two projected
alternating factors. This specifies the regularized trace by
substitution in (10); no simplification using idempotence of
Q_delta is made. P_delta and Q_delta are positive contractions.
L090(15), with the same transverse vertex spectrum and axial
multiplicity, proves

    N^(-4)||P-P_delta||_HS^2
       <=C [zeta^(3/2)+(delta/zeta)^2],  0<zeta<=1.     (12)

Explicitly the low transverse vertex modes have three positive
indices at most N sqrt(zeta)/2, so there are at most
C N^3 zeta^(3/2) of them at each of the N-1 axial levels. Each
other singular difference is delta/(lambda+delta)<=delta/zeta.
There is no relative transverse vertex zero mode.

Telescoping all changed factors in (10), the finite inequality
|Tr(X E Y)|<=||X|| ||Y||sqrt(dim E)||E||_HS gives

    |a^3 R_loc,epsilon-T_(epsilon,delta,N)|
                   <=C_(i,epsilon) N^(-2)||P-P_delta||_HS. (13)

Here T_(epsilon,delta,N) denotes the normalized trace just defined.
The prefactor is a^4 sqrt(dim E)<=C N^-2. The heat sum (3)
controls the exterior factors. Take zeta=sqrt(delta) in (12);
the right side of (13) tends to zero with delta uniformly in N.
This normalized Hilbert–Schmidt approximation is made after mass
regularization; it asserts no operator-norm projection gain.

### 4. Transfer the local odd symbol to the finite trace

Fix epsilon,delta>0. Apply L090(17)'s finite geometric polynomial
approximation to R_epsilon on [0,16] and to
(Delta_0+delta I)^(-1) on [0,12]. Write the approximants as
r(Delta_E) and p(Delta_0), and put

    P_p=T(I_ax tensor p(Delta_0))T^T, Q_p=I-P_p.

Substitute them in every occurrence in (10)--(11). Polynomial
errors tend to zero in operator norm uniformly in N at these fixed
masses. All normalized remaining factors are bounded, and
a^4 dim E is bounded. A finite product telescoping estimate
therefore makes the normalized trace error tend to zero with the
degrees, after (3). Positive polynomial approximants are unnecessary;
their operator norms remain bounded when the errors are small.

At fixed degrees this is a finite-range trace of real stencils.
The f_k part of Omega_tilde_k has norm <=Ca p(k). Removing it
from either alternating factor now costs O_(i,epsilon,delta)(a)
in the normalized trace, by the same bounded-product estimate.
Thus only L089's H_k/a is needed for its frozen principal symbol.
The original f_k factors have been retained in (4)--(6) and are not
deleted from the singular trace by a formal symbol argument.

Consider the finite-range polynomial trace. A collar wider than its
fixed total stencil range has O(N^3) rows and costs
O(a^4 N^3)=O(1/N) in the normalized trace. This estimates all pinned
axial and transverse end rows, including staggered end exceptions.
In each remaining cell group the three transverse component diagonals
at a common vertex. All normalized coefficient changes across a
fixed number of lattice steps are O(a p(k)) for H_k/a, by
L090(6), and O(a) for G_tilde and U_mu, by smooth displacement.
Component midpoint moves have the same bounds, using L028's actual
smooth forest exterior columns. Freeze these coefficients at that
common point in each cell. The normalized diagonal error is
O(a p(k)p(l)); (3) and a^4 times the number of cells bound the
total error by O_i(a), with constants depending on the fixed
polynomial degrees. Axial coefficient derivatives inside G_tilde
are covered by its original finite stencil, not an altered generator.

It remains to evaluate the sum of the three frozen component
diagonals. In the staggered phases of L088 write

    d_j=2 sin(theta_j/2), eta_j=cos(theta_j/2),
    h=sum_(j=1)^4 d_j^2, lambda=sum_(j=2)^4 d_j^2.

The polynomial symbols are real and even under simultaneous
theta -> -theta:

    P_p=p(lambda)d_T d_T^T, Q_p=I-P_p,
    r(Delta_E)=r(h)I,
    H_av=eta_1^2, C_mu=eta_mu.                          (14)

The transverse incidence T has symbol -i d_T in L092's
tail-minus-head convention. The exact frozen generator satisfies
G_tilde=i W_TT, where W_TT is real and odd under theta -> -theta
by L088(14): every term has one d and otherwise eta factors.
Hence the frozen symbol of A_loc,p is

    i W_loc,
    W_loc=P_p W_TT+eta_1^2 d_T v_u^T,
    (v_u)_mu=u_mu eta_mu.                              (15)

W_loc is real and odd. This formula uses the actual axial endpoint
filters: it is eta_1^2 from H_av, not an unfiltered identity.

L088(11)--(13) give H_k/a=i S_k for the frozen real exterior
vector at the same point. S_k is real symmetric and odd under
simultaneous frequency reversal. The imaginary path contributions
cancel exactly in that formula; none is omitted in obtaining it.
Projected gh and hh symbols are respectively
i P_p S_k Q_p and i Q_p S_k Q_p. A real-matrix transpose becomes
the Hermitian adjoint at the same frequency, so the first transpose
in (10) has symbol -i Q_p S_k P_p.

The frozen trace symbol is therefore i times a real scalar function
which is odd under theta -> -theta. There are three odd imaginary
factors: the gh adjoint, A_loc,p and the hh factor. Every resolvent
and projection polynomial is real and even. Matrix products need
not commute. The diagonal sum of a translation-invariant finite
stencil is the torus integral of its matrix trace. This integrand
has integral zero over [-pi,pi]^4 by the inversion symmetry of
the domain. Equivalently its closed-walk trace is real while its
displayed symbol is purely imaginary and odd. The argument holds
for every pair k,l and for arbitrary real frozen displacement and
exterior vectors; symmetry of the exterior coefficients is not
needed for this cancellation. At lambda=0 or h=0 the polynomial
symbols remain defined and the same parity holds.

Thus at fixed polynomial degrees the actual normalized trace tends
to zero, with its collar and freezing errors controlled. Remove the
polynomial errors at fixed epsilon,delta. This proves

    lim_N T_(epsilon,delta,N)=0
                             for every epsilon,delta>0. (16)

No continuum external coefficient limit or internal frequency cutoff
has been assumed. The full heat sum is controlled by (3); one may
also first take a finite exterior square and then remove its uniform
Gaussian tail. Singular inverses were regularized before finite-range
freezing, and the whole prefix commutator was estimated before that
local step.

### 5. Remove the regularizers and retain the scope

For fixed epsilon, (12)--(13) and (16), followed by delta -> 0,
give lim_N a^3 R_loc,epsilon=0. Equation (9) then gives
lim_N a^3 R_L,epsilon=0. Finally (6), first with
eta=sqrt(epsilon) and then epsilon -> 0, proves (2).
The order is fixed masses, N limit, and subsequent removal of
approximation errors and masses. No mesh-dependent mass choice
or smallness of an individual multiplier/projection commutator
occurs.

This is local RESEARCH / REPRODUCTION under the unchanged EXPLORE
assessment `drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
L048's finite contraction and its normalization are imported through
L088/L093, rather than reproved. The additional specialization is
needed because L093 only bounded this ordered trace: its exact
prefix identity, the Hilbert–Schmidt count (8), and the cubic-scale
regularization justify a finite-to-frozen passage for this orientation.
The methods are the existing finite spectral, trace and stencil
methods, with no originality claim beyond the checked sources.
No numerical evidence or IEEE hypothesis is used for the zero limit.
Any subsequent comparison with D_i retains L082's saved-table/IEEE
qualifications.

The reverse orientation retains C G_T1^T Q rather than A K, so
neither (7) nor the two Omega K mass estimate establishes its limit.
The H transverse trace retains K_g between its exterior factors;
it does not have (1)'s pair of resolvent-weighted alternating factors.
Neither obstruction is removed by (2). Full compensation and all
independent continuum requirements remain open.

## Mathlib

Full matching left-crossed trace limit: **not checked**. Supporting
finite spectral, Schatten/Hilbert–Schmidt product, geometric polynomial,
Fourier finite-stencil and relative incidence coverage: **not checked**.
Unknown availability is not absence. No continuum Ward or general
flow-finiteness theorem is used to infer this isolated asymptotic.
