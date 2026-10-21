# L166 — The complete second ordered E,E trace is cubic-bounded

## Hypotheses

Keep L161's full-link SU(2) relative cube, a=8/N through sufficiently
fine admitted even meshes, straight direction-1 lower-rooted forest,
complete compact displacement and both actual L010 probes at tau=1/16.
Expand at fixed mesh before refinement. Use ordinary stored-coordinate
D=D_0, L, Sigma, A, F=Phi Sigma, h=h_k t_c, ell=h_l t_c and
N=T_S(ell,.,.). Hats denote three-color diagonal extensions.
Keep both residual subtractions, every action face and normal end link,
the upper pinned jump, constant axial mode and full exterior heat sum.
The complete tensors precede forest restriction. Define exactly the
second ordered trace of L161(3), including its coefficient:

    Y_i=-12 sum_(k,l,c) c_(i;kl)
                       Tr[Q_A(h) Fhat N Sigmahat].       (1)

## Conclusion

For both actual probes and mesh-independent constants,

    |Y_i|<=C_i N^3,                         i=3,6.       (2)

With L163's exact exterior split N=N_b+N_top,

    Y_i=-12 sum c Tr[Sigmahat Ahat B_h Fhat N_b]
                                      +O_i(N^2).       (3)

The upper-column term is O_i(N^2). The complete smooth-residual
subtraction is O_i(sqrt(log(eN))). Both are subcubic, but the retained
bulk trace is only cubic-bounded. Its scaled limit and vanishing are
unproved. L161(3)'s fourth trace still lacks cubic control; L158/L159's
mixed branches and L165's third trace still lack scaled limits.
No complete-response cubic bound, compensation, finer asymptotics,
interacting reflected error <=c_box/2, continuum construction or
infrared mass conclusion follows. This is local standard-method
progress, with no novelty claim beyond the sources checked.

## Proof

### 1. Exact order and the residual Green kernel

Fix exterior labels k,l,c. Polynomial mode factors are restored when
needed. Finite cyclicity gives exactly

    Tr[Q_A(h) Fhat N Sigmahat]
      =Tr[Sigmahat Ahat B_h Fhat N]
                         -Tr[B_(Ahat h) Fhat N Sigmahat]. (4)

No multiplier or prefix has been commuted. The support of A in both
indices lies in a fixed compact interior enlargement, by L028 and
L159 section 1. Call this set S. Its size is O(N^4). On S,
|h_e|<=C a p(k), by L150's interior exterior bound as used in L159.

For every e in S and every variable link x, put r=1+dist(e,x),
using lattice midpoint distances. We prove the componentwise bound

    |(A Sigma)_(e,x)|<=C a^-1 [r^-4+N^-4].             (5)

Bounded stencil shifts in r are absorbed in C. This is a kernel
estimate, not a bound obtained by applying smooth consistency to a
rough column. L018(2) gives the actual complete residual

    A=(L K_a+K_a^T L)/2-Q_3-Q_6.                       (6)

The compact-observation relative Green estimates needed below are

    |partial_e^j Sigma_(e,x)|
                       <=C_delta [r^(-2-j)+N^(-2-j)],
                                      j=0,1,2.        (7)

Differences in (7) are on a single component's staggered observation
grid, in any coordinate directions, not between different component
kernels. The j=0,1 cases are L164(5)-(6), by symmetry. For j=2 use
L165(8)'s two-difference infinite heat bound on that component's
one-Neumann/three-Dirichlet image formula from L164. The observation
stencil is compact, so nonidentity images are at distance at least
c_delta N(1+|b|), after a fixed finite grouping. Integrating the
two-difference bound through t=N^2, with image decay exponent >8,
gives O(N^-4). For t>=N^2 each observation difference in the relative
sine/cosine expansion contributes at most C|q|/N. The full mode sum
is bounded by C N^-6 exp(-c t/N^2), whose integral is O(N^-4).
The infinite tail has the same bound. Together with its infinite
r^-4 bound this proves j=2. Every source position x, including normal
end edges, is allowed; only the observation stencil is kept interior.
The constant edge mode is included, with zero differences when the
differentiated coordinate is constant.

L028's explicit endpoint/clover composition, in stored coordinates,
is K_a=a^-1 E_a M_a C_a D_1. Thus K_a is a finite sum of shifts
and component maps with coefficients a^-1 k_b(e). On the compact
enlargement the k_b have uniformly bounded physical C^2 extensions.
Their first and second unscaled differences are O(a) and O(a^2).
This follows from the same smooth sampled u_a used in L028(3)-(4);
all fixed averages and staggered shifts preserve those bounds.

On this enlargement each component of L=D_1^T D_1 is a fixed sum
of products of two first differences between the appropriate grids.
For each shifted product k_b(e) Sigma_(e+b,x), the exact twice-applied
discrete product rule bounds its second difference by the sum of
|k_b| times second Green differences, first coefficient differences
times first Green differences, and second coefficient differences
times undifferenced Green entries. Hence (7) gives

    |(L K_a Sigma)_(e,x)| <= C a^-1 [
       r^-4+N^-4+a(r^-3+N^-3)+a^2(r^-2+N^-2)].        (8)

Mixed component entries obey the same estimate, since each of the
finitely many terms uses the corresponding scalar component Green
kernel. No boundary product rule is needed at e: every coefficient
stencil under consideration is interior. Since r<=C N and aN=8,
(8) is bounded by the right side of (5).

For the other generator orientation, L Sigma=P exactly by L157.
L165(6) bounds |P_(e',x)| by C[r^-4+N^-4] for every e' within a
fixed distance of e. K_a^T has bounded stencil radius and entries
O(a^-1), including its shifted coefficient values. Therefore

    |(K_a^T L Sigma)_(e,x)|<=C a^-1[r^-4+N^-4].        (9)

Both subtractions have the exact form Q_j=D_1^T W_j D_1, with
bounded finite-range W_j; W_6 includes its two clover averages.
These are L028's polarized insertion formulas after multiplying the
physical matrices by a^2, as in L156. Retain just the right-hand
D_1 on Sigma. The other local factors have bounded entries and
degree, and (7) with j=1 yields

    |(Q_j Sigma)_(e,x)|<=C[r^-3+N^-3]
                       <=C a^-1[r^-4+N^-4].           (10)

Their supports are compact. This deliberately weaker estimate needs
no cancellation between the two subtractions and does not delete
either one. Equations (6),(8)-(10) prove (5). Since A and Sigma
are symmetric, the required reversed entry satisfies
(Sigma A)_(x,e)=(A Sigma)_(e,x), without assuming they commute.

### 2. Prefix entries with the row fixed instead of the column

We need F_(v,y) for v an endpoint of e in S and arbitrary source y.
L165(9) alone fixed its compact column, so its hypothesis cannot be
transferred by transposition to this different matrix. We instead
prove the global undifferenced estimate, for any same-component links
z,y in the cube,

    |Sigma_(z,y)|<=C[(1+dist(z,y))^-2+N^-2].           (11)

Use the same exact relative heat image formula as above, without
differences. In each coordinate the nearest reflected image
distances are |z_j-y_j|, z_j+y_j and 2N-z_j-y_j, in physical lattice
coordinates with the appropriate half-integer edge centers. Each
is at least |z_j-y_j|. After a fixed number of these nearest image
choices, every other image is at distance >=cN(1+|b|). Absolute
values of the reflection signs only increase this bound. L164(6)
with j=0, integrated up to N^2, bounds the finitely many near images
by C(1+dist(z,y))^-2 and the remaining image sum by C N^-2. For
t>=N^2 the full relative modes give C N^-4 exp(-ct/N^2) uniformly
at all rows, hence another C N^-2. There are at least three positive
component frequencies even when the edge frequency is zero. This
proves (11) without excluding a lower or upper end row. Fixed rows
may be included with value zero.

F has zero columns outside link component 1. In that component its
entry is the complete lower prefix of Sigma, with at most N terms.
Write v=(s,v_T) and let y_T be the transverse coordinate of y. From
(11), summing over all integer axial offsets for its decaying term,

    |F_(v,y)|<=C/(1+|v_T-y_T|)+C/N
                         <=C/(1+|v_T-y_T|).            (12)

Indeed the sum of (1+sqrt(n^2+m^2))^-2 over n is at most
C/(1+m), by comparison with the integral of ((1+m)^2+t^2)^-1.
The last inequality uses m<=C N. This bound is uniform in s and
y, retaining the whole prefix and its constant mode. Pinned vertex
rows are zero. F is a cross matrix throughout, not a covariance.

### 3. Sum the bulk and the actual upper action column

L163's exact split and L164(3) imply: N_b has bounded stencil
radius and degree, and entries bounded by C a p(l), on all action
plaquettes including faces. N_top has O(N^3) entries, each bounded
by C p(l), with both indices in the last axial plaquette layer.
No exterior field is extended smoothly across that pinned jump.

Expand the first trace in (4) in its original order:

    sum_(e,v,y,x) (Sigmahat Ahat)_(x,e)
                            (B_h)_(e,v) Fhat_(v,y) N_(y,x). (13)

Here e belongs to S, v is one of its interior endpoints, and x,y
are a bounded distance apart whenever N_(y,x) is nonzero. Color
multiplicities and endpoint counts are bounded independently of N.
For fixed e, combine (5),(12) and |(B_h)_(e,v)|<=C a p(k).
The spatial sum needed for N_b is uniformly bounded:

    sum_x [(1+dist(e,x))^-4+N^-4]
                          /(1+|e_T-x_T|) <= C.          (14)

To check it, a transverse shell of radius m has O((1+m)^2) sites,
and summing the fourth-power decay over axial offsets gives
C(1+m)^-3. Thus the decaying part has summable shell majorant
C(1+m)^-2. The constant part contributes at most
C N^-4 N sum_(m<=CN)(1+m)=O(N^-1). Fixed component/endpoint
shifts in (13) change only C. It follows that the full bulk trace is

    |Tr(Sigmahat Ahat B_h Fhat N_b)|
       <=C p(k)p(l) N^4 a^-1 a a
       <=C p(k)p(l) N^3.                              (15)

For N_top both x,y are separated from S by delta N. Consequently
(5) is at most C a^-1 N^-4, and the h factor makes their product
C p(k) N^-4. For each e, (12) summed over every transverse top
position is at most C N^2. The bounded number of axial layers and
finite stencil choices does not change this count. Therefore

    |Tr(Sigmahat Ahat B_h Fhat N_top)|
                  <=C p(k)p(l) N^4 N^-4 N^2
                  <=C p(k)p(l) N^2.                    (16)

This retains the full upper action tensor. Its different normal and
tangential rough components could sharpen individual entries, but
no such improvement is used. Every other action face remains in
N_b and was already counted in (14)-(15).

### 4. The smooth-residual subtraction and complete heat sum

L156(9) gives ||A h||_infinity<=C a^5 p(k), by exact gauge
annihilation before smooth consistency. The endpoint map consequently
has ||B_(Ahat h)||<=C a^5 p(k). L161 proves ||Fhat||_HS<=C N^3
and ||N||<=C p(l) globally, including the jump; L165(13) gives
||Sigmahat||_HS<=C N^2 sqrt(log(eN)), with the entire relative
spectrum. The trace Cauchy--Schwarz inequality yields

    |Tr(B_(Ahat h) Fhat N Sigmahat)|
      <=||B_(Ahat h)|| ||Fhat||_HS ||N|| ||Sigmahat||_HS
      <=C p(k)p(l) sqrt(log(eN)).                      (17)

No positivity or independence assumption occurs in (13) or (17).
L156(8) gives uniform summability of
sum_(k,l)|c_(i;kl)|p(k)p(l) for both actual probes. Apply it to
(15)-(17), sum the three exterior colors and retain -12 once.
Equations (2)-(3) follow. The scaled upper error is O(N^-1), and
the scaled subtraction is O(N^-3 sqrt(log(eN))); (15) supplies only
bounded scaled bulk values, not convergence or a zero limit.

The meaningful checks are analytic: both generator orders and both
subtractions in (5), compact observation versus arbitrary source
in (7), the global prefix-row estimate (11)-(12), the shell sum
(14), and the separated upper count (16). No mathematical script
or finite-mesh extrapolation is needed. In particular this estimate
is not transferred to the fourth trace, which has two prefix cross
matrices and no adjacent Sigma on which to place A in this manner.

## Mathlib

Full matching theorem and supporting relative-kernel coverage:
**not checked**. Unknown is not absence. Reuse the unchanged
[target assessment](../drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md).
No external theorem is newly imported or reproved. L018 fixes the
actual residual, L026 supplies the relative product modes as used
in L164/L165, L028 supplies its smooth coefficient/stencil formulas,
L150/L156 the exterior and heat bounds, L157 the gauge/projector
identities, L161 the exact trace/prefix bounds, and L163-L165 the
exterior split and kernel estimates. The extra two-difference component
case and global undifferenced image estimate are justified explicitly
because the different compact-row placement is essential here.
