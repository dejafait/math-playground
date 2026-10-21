# L096 — The transverse transport multiplier has no small projection commutator

## Hypotheses

Use L095's actual H-diagonal trace in L091, on L085's finite relative
transverse edge spaces at interior axial levels. The box is (-4,4)^4,
N is sufficiently large and even, a=8/N, the forest is lower-rooted
in direction 1, and u_a is exactly L008's displacement in L009's
clover/endpoint generator. The two actual L010 probes, full exterior
heat sums and fixed-mesh small-coupling convention are unchanged.
Norms in this lemma are ordinary stored-coordinate operator norms.

At the level s=N/2 (physical x_1=0), let T and D be the transverse
relative gradient and circulation of L085, with
P=T(T^T T)^(-1)T^T and Q=I-P. Let C_nu average a transverse nu-edge
onto its two vertex endpoints. Its transpose averages vertices onto
nu-edges. All coefficients below vanish before physical boundary
stencils; the actual relative end rows are retained.

Define the block-diagonal map on the three transverse components by

    U=diag_(nu=2,3,4)[C_nu^T M_(u_(a,2)) C_nu].          (1)

Also let U^off have the same components 3,4 and zero component 2.
The map U^off is the actual diagonal transport multiplier for the
rho=2 part of G_tr in L095. In fact its diagonal-input contribution
is a^-1 U^off T_2, where T_2 is the centered, unscaled direction-2
index difference on each component grid. The cross-component terms
from -partial_nu A_2 remain in G_tr; they are not part of U^off T_2.
The full map U in (1) is useful for distinguishing unequal endpoint
filters from merely deleting the rho component.

## Conclusion

For all sufficiently large admitted even N, one may take c=1/100 in

    ||Q U P|| >= c,          ||[P,U]|| >= c,
    ||Q U^off P|| >= c,      ||[P,U^off]|| >= c,
    ||Q U^off T_2 P|| >= c.                              (2)

Thus neither an O(a) nor an o(1) projection commutator estimate holds
for these transport multipliers. The projected diagonal transport
has norm at least c/a. Smoothness of u_a alone does not supply the
missing power in a termwise transverse summation argument.

This is an operator obstruction to that shortcut, not a lower bound
for R_H,tr or either probe response. Indeed the complete transverse
curl generator satisfies G_tr Pcal=0 exactly: its cross-component
terms cancel the diagonal transport on gradient inputs. L095's
actual signed trace retains both generator orientations, its exterior
alternating factors, the entire min(s,t) covariance and resolvent.
No cubic bound, scaled limit, signed growth, failure of the complete
limit, or compensation coefficient follows from (2).

## Proof

### 1. Identify the multiplier without replacing the generator

For output nu different from rho=2, L009(3)'s diagonal input term
comes from the partial_2 A_nu part of F_(2,nu). Clover averaging
first applies the direction-2 interval average to its incidence,
which gives the exact centered difference T_2, and the direction-nu
edge-to-vertex average C_nu. Endpoint output averaging gives C_nu^T.
The coefficient remains between the two nu averages. Since C_nu
and T_2 act in different coordinates, this term is exactly

    a^-1 C_nu^T M_(u_(a,2)) C_nu T_2 A_nu.             (3)

For nu=2, F_(2,2)=0, so no such diagonal term occurs; this is why
U^off, rather than U alone, appears in (3). The separate input-A_2
terms of F_(2,nu) are retained in the complete generator. No multiplier
has been moved through P, Q, an incidence or a resolvent in (3).
Compact displacement support makes the same calculation valid with
the actual relative domains. U is the extension restoring just the
nu=2 averaging block, not an asserted standalone generator.

### 2. Use an exact gradient in the actual finite box

Choose a nonzero real smooth function eta compactly supported in

    (1/2,3/2) x (-1,1) x (-1,1)

of the physical transverse coordinates (x_2,x_3,x_4). At x_1=0,
this support and every neighboring stencil lie in L008's affine core
for sufficiently small a. There u_(a,2)=x_2 exactly: the central
x_4 difference of Psi_24=x_2 x_4 is x_2, with no cutoff derivative.

For transverse vertex index j, set

    theta=(pi/2, pi, pi/2),
    phi_N(j)=eta(-4+a j_2,-4+a j_3,-4+a j_4)
                         exp(i theta dot j),
    y_N=T phi_N.                                         (4)

The vertex field is zero near every physical face and is an admissible
pinned field. Thus P y_N=y_N and D y_N=0 exactly, including every
end row. There is no approximate projection onto gradients.

For completeness, fixed finite stencils admit the following controlled
packet calculation. In component-center phases write

    d_nu=2 sin(theta_nu/2), h_nu=cos(theta_nu/2).

An edge difference T phi=phi(v)-phi(w) has leading symbol -i d_nu;
either direction of C_nu has leading symbol h_nu. Replacing eta at
one of the finitely many shifted points by eta at the stencil center
has pointwise error at most C_eta a. The same estimate applies to
u_(a,2)=x_2. There are O(a^-3) support rows and bounded repetitions
per row. Consequently the l2 error in each displayed finite stencil
composition is at most C a a^-3/2. Riemann sums give

    a^3 ||phi_N||^2 -> integral eta^2 >0,

so this error is at most C' a ||phi_N||. The same Riemann estimate
compares the norms of eta sampled on a vertex grid and a fixed
plaquette-center grid with relative error O(a). Constants are
independent of N. All compositions used below have fixed range;
this calculation makes no approximation to the nonlocal P or Q.

### 3. Detect circulation in the two active output components

At the carrier in (4),

    (d_2,d_3,d_4)=(sqrt(2),2,sqrt(2)),
    (h_2^2,h_3^2,h_4^2)=(1/2,0,1/2).

The leading symbol of U on this packet is therefore
x_2 diag(1/2,0,1/2). For U^off it is x_2 diag(0,0,1/2).
Both have the same components 3,4. In the 34 plane the circulation
row is -i d_4 e_3^T+i d_3 e_4^T, in the convention just fixed.
Applying it to U T phi gives the real leading multiplier

    x_2 d_3 d_4 (h_4^2-h_3^2)=sqrt(2) x_2.             (5)

An overall reversal of circulation orientation changes only its sign.
Equation (5) also holds with U^off. It uses two active output
components of the actual rho=2 transport; it is not caused just by
setting its component 2 to zero. Equalizing the two endpoint filters
would incorrectly delete this circulation.

Since x_2>=1/2 on the support, the packet estimate above implies,
for W=U and W=U^off,

    ||D_34 W T phi_N||
           >= (sqrt(2)/2-C a)||phi_N||
           >= (sqrt(2)/4)||phi_N||                     (6)

for sufficiently small a. The centered T_2 has leading symbol
 i sin(theta_2)=i and has the same O(a) packet remainder. Consequently
(6) also holds with W T phi_N replaced by U^off T_2 T phi_N;
the extra leading factor i changes no norm. This concerns only
stencils supported strictly inside the affine core, so neither
an exterior zero extension nor an end-row convention changes (6).

The full relative spectrum used in L085 gives

    ||T||<=sqrt(12),      ||D_34||<=||D||<=sqrt(12).

For example D^T D=Delta_T Q with 0<=Delta_T<=12 I;
T^T T is the sum of the three Dirichlet interval Laplacians, each
bounded by 4. These inequalities include all relative endpoint rows.
Because D_34 P=0, D_34 Q=D_34. Since y_N=T phi_N is a gradient,
(6) yields

    ||Q W P|| >= ||Q W y_N||/||y_N||
       >= ||D_34 W y_N||/(sqrt(12)||T phi_N||)
       >= sqrt(2)/48 > 1/100.                          (7)

The same estimate with T_2 inserted proves the last bound of (2).
Finally Q[P,W]P=-Q W P, so compression by the two orthogonal
projections proves both commutator bounds.

The matrices are real. Using the complex packet in (4) does not
weaken these real norm lower bounds: for a real matrix A and z=x+iy,
||Az||^2=||Ax||^2+||Ay||^2 and ||z||^2=||x||^2+||y||^2, so one of
x,y has at least the same norm ratio. This completes the finite-box
proof of (2).

### 4. Keep the canceled terms and the signed-trace limitations

The image of P on each level consists of exact transverse gradients.
For such an input, every transverse F_(rho,nu) vanishes before any
clover, multiplication or output averaging. Hence G_tr Pcal=0 on
the full level space, independently of axial boundary conditions.
The lower bound for its selected diagonal transport therefore cannot
be transferred to the full generator, much less to R_H,tr.

The failed estimate in this attempt was to gain a power by commuting
individual actual transport multipliers through P after transverse
summation. Equations (2) refute that norm step, including after the
centered derivative in (3). They do not refute a weighted signed
identity that combines diagonal and cross-component terms first.
The complete R_H,tr retains only its previous O(N^4) upper bound;
that upper bound is not evidence of actual growth. R_R and the scaled
limits of all bounded sectors remain open. The complete other/other
comparison with -12 gamma D_i remains unresolved; any future numerical
comparison keeps L084/L082's saved-table and IEEE qualifications.

This RESEARCH / REPRODUCTION test reuses the unchanged EXPLORE
assessment `drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
L094's compact-packet method is reused, but its axial reverse-prefix
operator is not this transverse multiplier. The new applicability
calculation (3)–(7) is necessary to test the proposed commutator gain.
No general Ward or flow theorem assigns a coefficient here. This is
local informative negative evidence, not a novelty claim or progress
beyond the sources checked. No mathematical script or numerical
certificate is needed. Other jets, finer powers/logarithm, interacting
matching and error <=c_box/2, continuum axioms, reflection positivity,
infrared control and finite positive mass remain unresolved.

## Mathlib

Full matching finite-box commutator obstruction: **not checked**.
Supporting relative-incidence identities, finite-stencil estimates,
Riemann sums and real/complex operator norms: **not checked**. Unknown
availability is not absence. No external theorem is newly imported.
