# L094 — The actual reverse-prefix block cannot have a linear bound

## Hypotheses

Use L008's actual compact displacement, L009's exact endpoint/clover
generator, L026's dimensionless stored-coordinate relative spaces and
L085's straight lower-rooted forest. The box is (-4,4)^4, N is admitted
and even, a=8/N tends to zero, and all pinned rows and axial end edges
are retained. Keep L092–L093's maps

    Tcal=I_(N-1) tensor T,  G_v=I_(N-1) tensor (T^T T)^(-1),
    C=Tcal G_v B,  G_T1=I_T^T K_a I_1,
    Qcal=I-Tcal G_v Tcal^T,
    B_(s,ell)=1_(ell<s),  1<=s<N, 0<=ell<N.

All transposes and norms are ordinary stored-coordinate ones. T has
tail-minus-head orientation and pinned vertex values; Qcal is the
transverse co-closed projection, independently at every interior axial
level. Define the actual reverse block in L093(3) by

    R_N=C G_T1^T Qcal.

This is an operator in the already contracted expression, with its
actual coefficient placement. It is not a modified cubic vertex or
a frozen replacement for that expression. The bare small-coupling
coefficient is still taken at fixed mesh first. Both actual L010 probes,
both connected classes and both generator orientations remain in the
complete other/other target.

## Conclusion

For some c>0 independent of sufficiently fine admitted N,

    ||R_N|| >= c/a^2 = (c/64) N^2.                       (1)

Thus the proposed O(N) operator bound on this reverse block is false.
L093's O(N) first-orientation bound cannot be extended to it, even
with the actual compact displacement and all fixed-boundary rows.
This is new negative evidence for that sufficient norm shortcut, not
growth of the signed R_R trace. Equation (1) does not disprove a cubic
trace bound or a finite a^3 limit of the complete group: its exterior
alternating maps, covariance factors and signed sum remain essential.

There is no complete other/other coefficient or compensation with
-12 gamma D_i, and no Yang–Mills candidate. The H diagonal, limits
of the already bounded traces, other jets, N^2 remainders, slower powers
and logarithm, matching, interacting error <=c_box/2, continuum axioms,
reflection positivity, infrared control and finite positive mass remain
unresolved.

## Proof

### 1. An exact gradient column with an exactly prescribed adjoint prefix

Import L092's C and L085's pinned transverse incidence. For every
pinned four-dimensional vertex field phi,

    C^T Tcal phi=B^T G_v Tcal^T Tcal phi=B^T phi.         (2)

This uses the complete invertible transverse vertex Laplacian on each
level; it assumes no rough-input smoothness or coefficient commutation.

Let b(t)=exp[-1/(1-t^2)] for |t|<1 and zero otherwise, and set

    h(x_1)=b((x_1-5/4)/(3/4)),
    eta(x_T)=b(x_2/2)b(x_3/2)b(x_4/2).

Thus h is supported in (1/2,2) and eta in (-2,2)^3. Both are smooth.
Write z_r=-4+ar, including half-integral edge indices, and define

    rho_a(s)=[h(z_(s-1/2))-h(z_(s+1/2))]/a,
    phi_N(s,j_T)=a^2 rho_a(s) eta(z_(j_T))
                           exp[i(pi j_2/2+pi j_3)],
    y_N=Tcal phi_N.                                    (3)

The vertex field vanishes near every face, and y_N is in the exact
gradient range. Normal transverse end edges are included with their
actual pinned endpoint values. On every axial edge ell, telescoping
over all s>ell gives

    (B^T phi_N)(ell,j_T)
       =a [h(z_(ell+1/2))-h(z_(N-1/2))]
                    eta(z_(j_T)) exp[i(pi j_2/2+pi j_3)]
       =a h(z_(ell+1/2)) eta(z_(j_T))
                                      exp[i(pi j_2/2+pi j_3)]. (4)

For sufficiently small a the last h value is zero. The equality holds
also at ell=0 and ell=N-1: the latter sum is empty, and both h values
there vanish. Hence (4) is an exact finite-prefix identity on every
row, not a bulk approximation. It constructs a compact component-1
input of amplitude a from a vertex field of amplitude a^2, retaining
the full 1/a gain of the adjoint prefix.

### 2. The actual transverse curl retains the unequal filters

Put Dcal=I_(N-1) tensor D, where D is the full relative transverse
circulation. L085 gives Dcal Qcal=Dcal. Its norm is at most sqrt(12):
D^T D=Delta_T(I-P), and each of the three natural interval Laplacians
has spectrum in [0,4], including its actual endpoint rows. Therefore

    ||R_N^T y_N||=||Qcal G_T1 C^T y_N||
                  >=||Dcal G_T1 B^T phi_N||/sqrt(12).   (5)

To bound the right side below, retain just its 23-plaquette component.
Use the exact staggered carrier convention of L088 and the checked
pure component-1 generator formula from L066, proof section 2:

    (G_T1)_mu=-(i/a) u_1 eta_mu^2 eta_1 d_mu,
    d_j=2 sin(theta_j/2), eta_j=cos(theta_j/2).

Here eta_j denotes a carrier average, distinct from the envelope eta.
At theta=(0,pi/2,pi,0),

    d=(0,sqrt(2),2,0),  (eta_1,eta_2,eta_3,eta_4)
                                      =(1,1/sqrt(2),0,1),
    G_T1=-(i u_1/(sqrt(2)a)) e_2.

Both transverse output filters are retained. In particular the third
output is zero at this carrier because eta_3=0, not because that
component was deleted. The 23 circulation row is
-i d_3 e_2^T+i d_2 e_3^T, so its composite symbol is

    (D_23 G_T1)(theta)=-sqrt(2) u_1/a.                  (6)

An overall circulation orientation reversal changes only the sign,
which is immaterial to (5). This nonzero composite is the reason Qcal
does not remove the reverse column. It is the same unequal-filter
mechanism identified in L066, now applied to the exact prefix (4),
rather than to L066's whitened residual block. No residual theorem
is being transferred across components by polarization.

### 3. Justify the symbol on the actual compact packet

Every nonzero entry of (4) and every neighboring generator/circulation
stencil lies in a fixed compact subset of the core for small a.
L008's central-difference displacement is exactly
u_a=(x_1,x_2,-x_3,-x_4) on this neighborhood. In particular u_(a,1)=x_1.
There is no face stencil on the support; zero extension gives the
exact finite-domain action and preserves every pinned row.

The map D_23 G_T1 is a finite sum of shifts with one displacement
coefficient, bounded fixed stencil constants and one factor 1/a.
For each shift, use (4) and retain its carrier phase exactly.
The difference between h eta at shifted staggered points and at the
output point is O(a), uniformly by the mean value theorem. The same
is true of replacing the shifted u_1 by x_1. The input amplitude is a,
so, after the factor 1/a, each error is O(a) per entry. This also
accounts for the axial input averaging: h at its two adjacent edge
midpoints differs by O(a) from h at the output vertex. The finite
number and multiplicity of shifts are independent of N. The exact
carrier calculation (6) consequently yields, on the full plaquette
array with its ordinary norm,

    (D_23 G_T1 B^T phi_N)(s,p)
       =-sqrt(2) z_s h(z_s) eta(z_p)
          exp[i(pi(j_2+1/2)/2+pi(j_3+1/2))]+e_N(s,p),
    a^2 ||e_N||<=C a.                                  (7)

Here p has midpoint coordinates in directions 2 and 3 and a vertex
coordinate in direction 4; the omitted carrier phase in direction 4
is one. Outside a fixed neighborhood of the compact support both
the actual field and the displayed leading field vanish. Inside it
there are O(a^-4) plaquette entries, so the O(a) entry error proves
the second line of (7). This proves an actual packet estimate, rather
than substituting a frozen symbol for the finite operator.

Define the finite strictly positive integrals

    J_eta=integral_((-4,4)^3) eta^2,
    J_rho=integral_(-4)^4 (h')^2,
    J_h=integral_(-4)^4 x_1^2 h(x_1)^2.

Ordinary midpoint/vertex Riemann sums and (7) give

    a^2 ||D_23 G_T1 B^T phi_N|| -> sqrt(2 J_h J_eta).   (8)

For completeness the input normalization is also controlled on the
actual relative spaces. rho_a converges uniformly to -h', and it is
uniformly bounded. An unscaled transverse incidence on the carrier
in (3) has squared magnitude d_2^2+d_3^2+d_4^2=6. Replacing its
shifted envelope by the midpoint envelope costs O(a^3) per edge
(input amplitude a^2 times an O(a) envelope difference), hence O(a)
in the ordinary full-edge norm. There are no boundary terms because
the envelope and its neighboring shifts are compact. Riemann sums
therefore give

    ||y_N||^2 -> 6 J_rho J_eta>0.                       (9)

Equations (8)–(9) inspect the complete relevant analytical evidence:
no numerical preview, low-mode truncation or asymptotic fit is used.

### 4. The discriminating lower bound and its precise limitation

A real matrix has the same operator norm on its complexification:
for real v,w, ||R(v+iw)||^2=||Rv||^2+||Rw||^2. Thus the complex
packets are admissible norm tests for the real block. From (2), (5),
(8) and (9), and the fact that retaining only D_23 decreases a norm,

    liminf_(a->0) a^2 ||R_N||
       >= sqrt(2 J_h J_eta)/sqrt(12*6 J_rho J_eta)
       =(1/6) sqrt(J_h/J_rho)>0.                       (10)

Taking c=(1/12)sqrt(J_h/J_rho) proves (1) for all sufficiently fine
admitted even meshes. No divisibility condition on N is needed:
the carrier is a compact finite-space field, not a periodic mode.

In L093 the first generator orientation has the exact O(1/a) row
bound ||H_g K_a I_T||. For the actual reverse trace, L093(13) gives
||K_h Omega_(gh,k)^T||_HS<=C p(k)N. The other factor also has a
linear bound, for a different reason: L088's actual coefficient and
bounded-stencil bounds give ||Omega_l||<=C a p(l), while its ambient
dimension is at most 3N^4. Hence
||Omega_(hh,l)||_HS<=sqrt(3)N^2 ||Omega_l||<=C p(l)N.
Replacing R_N by a row of size O(N) would therefore suffice for a
cubic trace bound by Hilbert–Schmidt Cauchy–Schwarz in its actual
order. Equation (10) rules out that particular operator-norm premise.
It gives no lower bound for

    sum_(k,l)c_(i;kl)
      Tr(K_h Omega_(gh,k)^T R_N Omega_(hh,l)),

because this trace tests different, constrained columns and sums
signed terms. Even the eventual comparison -4 gamma D_i before
L085's outside factor 3 remains uncomputed. L082's saved-table/IEEE
qualifications still attach to any numerical comparison through L084;
no numerical coefficient is used here. Neither the H diagonal nor
the other traces may be discarded in a later signed analysis.

This is a RESEARCH / REPRODUCTION obstruction test under the unchanged
EXPLORE assessment `drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
The finite contractions are imported unchanged. Reusing L066's exact
carrier and localization method is necessary to test the newly retained
prefix composition; its earlier residual norm statement alone does not
imply (1). This is local negative evidence, with no claim of originality
beyond the checked literature. A signed finite-trace or joint-sector
analysis is a different mechanism; repeating the O(N) reverse-block
norm shortcut is not justified by compact support or transpose symmetry.

## Mathlib

Full matching reverse-prefix operator obstruction: **not checked**.
Supporting complexification of real operator norms, finite incidence
spectral bounds and Riemann sums: **not checked**. Unknown availability
is not evidence of absence. The proof uses the explicit local inputs
and the displayed exact prefix and compact-packet estimates, rather
than an external Ward or flow-finiteness theorem.
