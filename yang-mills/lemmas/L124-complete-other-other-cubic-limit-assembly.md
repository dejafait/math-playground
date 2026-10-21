# L124 — The complete other/other cubic contribution has a finite scaled limit

## Hypotheses

Use the common setup of L048, L085 and L091: SU(2), both actual L010
probes i=3,6 at tau=1/16, the actual L018 residual, the straight
lower-rooted direction-1 forest, and the all-face relative fixed-link
box (-4,4)^4. Let a=8/N through sufficiently fine admitted even meshes.
Take the bare small-coupling coefficient at each fixed mesh before
refinement. All coordinates, transposes and traces are ordinary stored
ones. Retain all interior axial levels, transverse end rows, ordered
plaquette pairs including coincidences, both connected pairing classes,
both residual orientations and the complete exterior heat sums.

Put C=S3_top, Y=S3-C and

    O_i(a)=(1/2) kappa(f_(i,0),r0,Y,Y).

Use exactly the finite traces of L085/L086/L091, L093, L095 and
L110--L116. The real coefficients K_(i,Q), K_(i,ax), K_(i,E),
K_(i,G), K_(i,R), K_(i,V), K_(i,sc), K_(i,en) and K_(i,f) are
the canonical functionals defined respectively in L097, L098, L101,
L104, L107, L120, L121, L122 and L123. These definitions include their
original signs, phases, mode normalizations and actual prefix fields.
No coefficient is refrozen or identified with a different functional.

For comparison use L084's complete mixed response
M_i(a)=kappa(f_(i,0),r0,C,Y), with its gamma>0 and continuum D_i.
The analytic comparison requires no numerical assumptions. Any use
of the strict negative signs or enclosures for D_i retains L084's
L082 saved-table, certified-input and IEEE rounding qualifications.

## Conclusion

Define the finite real number

    K_(i,oo)=K_(i,E)+K_(i,ax)-K_(i,Q)+K_(i,G)+K_(i,R)
                      +K_(i,f)+K_(i,V)+K_(i,sc)+K_(i,en).       (1)

Then for both probes

    lim_(a->0) a^3 O_i(a)=3 K_(i,oo),
    O_i(a)=3 K_(i,oo) a^-3+o(a^-3).                           (2)

In particular the complete group is O(a^-3); no stronger power remains
in this group. Its coefficient can be compared exactly with the
requested opposite mixed coefficient as follows:

    lim_(a->0) a^3 [O_i(a)+M_i(a)]
                         =3 [K_(i,oo)+4 gamma D_i].           (3)

Thus cancellation between these two groups at cubic scale is equivalent
to K_(i,oo)=-4 gamma D_i for each probe. The values of K_(i,oo), their
signs and this equality are unresolved. Equation (3) gives a comparison
formula, not an evaluated ordering, a cancellation proof or a new sign
certificate. The outside factor 3 is applied once in (2)--(3).

This is local RESEARCH / REPRODUCTION progress under the unchanged
EXPLORE assessment `drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
It assembles existing local limits rather than claiming progress beyond
the sources checked. It gives no O(a^-2) remainder, finer power or
logarithmic coefficient, complete-response compensation, interacting
matching or reflected-error bound <=c_box/2. Continuum fields/axioms,
reflection positivity, infrared control and finite positive mass remain
independent gaps. There is no Yang--Mills candidate.

## Proof

### 1. Account for both connected classes and every rough sector

Import L048's complete finite contraction and its no-upper restriction
L085(5), with the unchanged normalization verified in L085, proof
section 3. L086's definitions then give the exact finite identity

    O_i=3(T_Z+T_UV).

The ordered pair sum includes coincident plaquettes. T_Z includes both
covariance paths through the two quadratic vertices; T_UV includes all
six distinct-row replacements. Neither connected class is discarded
by algebra. L091(4) gives, in its whitened notation,

    T_UV=T_gg+T_hh+R_H+R_E+R_gx+R_hx,
    R_H=sum_(k,l)c_(i;kl,a) Tr(J_k H J_l^T),
    R_E=sum_(k,l)c_(i;kl,a) Tr(J_k^T E J_l).

The crossed traces R_gx and R_hx each already contain their factor 2
from the two residual orientations. In particular this factor must
not be applied again when importing their later limits. L086, L087
and L090 establish, respectively,

    T_Z=O(N^(3/2)), T_gg=O(N^2), a^3 T_hh ->0.             (4)

Since a^3=512/N^3, all three have zero cubic-scaled limit.

L095(3) and L093(2)--(4) supply the exact further splits

    R_H=R_H,ax+R_H,tr-R_H,Q,
    R_hx=R_L+R_R-R_Q,        R_Q=O(N^(5/2)).               (5)

R_Q in the second line is the off-diagonal curvature insertion of
L093. It is different from the H diagonal subtraction R_H,Q in the
first line. Only the former is subcubic here. L100 proves a^3 R_L->0.
L101 proves a^3 R_E->K_(i,E). L097 and L098 prove, with the same
actual alternating blocks and full heat sum,

    a^3 R_H,Q ->K_(i,Q), a^3 R_H,ax ->K_(i,ax).            (6)

In particular the canonical positive-definition R_H,Q limit enters
with a minus sign, irrespective of the unevaluated sign of K_(i,Q).

For the gradient-base crossed pair, L102(2) has
R_gx=G_L+G_R-G_Q with G_L=O(N^(5/2)), G_Q=O(N^2).
L104(2) therefore proves a^3 R_gx->K_(i,G) for the complete pair.
For the distinct co-closed-base reverse trace, L107(3) proves
a^3 R_R->K_(i,R). Its canonical formula's triangular half-weight
is already included in K_(i,R); it is not another cumulant factor.

### 2. Telescope the transverse H trace with its finite difference signs

L099, proof section 1, consumes the generator insertion's factor 1/2
by transposing one orientation and using the symmetric exterior sum.
L110 uses exactly that full R_H,tr, not a single orientation. Its
definition and L111(4) give exact finite equalities

    R_H,tr=E_(i,N)^f+R_H,tr^D,
    R_H,tr^D=R_bulk+R_pin.

Define the finite differences in their original orientations:

    Delta_V=R_bulk-R_bulk,moved,
    Delta_sc=R_bulk,moved-R_bulk,sc,
    Delta_P=R_bulk,sc-R_bulk,sc,Pbulk,
    Delta_en=R_bulk,sc,Pbulk-R_prod,
    Delta_C=R_prod-R_inf.                                  (7)

The first definition is L119's Delta_V for the move in L111(5).
The next three match L121's hypothesis, L114(3), and L122's hypothesis
for L115(3). The last matches L116(3). These are actual finite scalar
differences; no variable multiplier or component filter is commuted
without retaining its difference. Adding (7) gives the exact identity

    R_H,tr=E_(i,N)^f+R_pin+Delta_V+Delta_sc+Delta_P
                                +Delta_en+Delta_C+R_inf.   (8)

Every difference enters with a plus sign. In particular L122's
closed-trace scalar difference is psi(y+d-n)-psi(y), corresponding
to the orientation of Delta_en in (7), rather than its negative.

L112, L114 and L116 supply all discarded comparison bounds:

    |R_pin|<=C_i N^(5/2) log N,
    |Delta_P|<=C_i N^(5/2)(log N)^(3/4),
    |Delta_C|<=C_i N^3 eta_N, eta_N->0.                    (9)

Each bound is o(N^3); multiplying by a^3 sends it to zero.
L118 proves R_inf=0 exactly for sufficiently fine meshes, retaining
each ordered stencil. There is no coefficient left in R_prod to add.
The four remaining terms in (8) are not discarded: L123, L120, L121
and L122 prove respectively

    a^3 E_(i,N)^f ->K_(i,f), a^3 Delta_V ->K_(i,V),
    a^3 Delta_sc ->K_(i,sc), a^3 Delta_en ->K_(i,en).

Consequently (8)--(9) imply

    a^3 R_H,tr ->K_(i,f)+K_(i,V)+K_(i,sc)+K_(i,en).        (10)

All imported limits apply to the same SU(2) fixed box, straight forest,
admitted mesh sequence, probes, actual residual and tau. The scalar
extensions and bulk projection in (7) are only comparison operators
at the stages specified by their defining lemmas. Their boundary
differences are (9), not silently changed original boundary conditions.
The individual limit theorems retain both original axial coefficient
levels and prove passage through the complete exterior heat sum.
Here only finitely many convergent scalar sequences are added; no new
exchange of infinite sums, integrals or regularization limits is made.

### 3. Restore the normalization and compare with the mixed group

Insert (5), (6) and (10), the R_E, R_gx, R_R limits, and the zero
limits in (4) into the exact identity of section 1. Finite linearity
of limits gives (1)--(2), with the unchanged outside factor 3.
Convergence to a finite number bounds a^3 O_i eventually, which proves
the stated O(a^-3) estimate without claiming its coefficient is nonzero.

L084(1) is lim a^3 M_i=12 gamma D_i for the complete mixed group.
Adding this single limit to (2) gives (3). The coefficient is zero
if and only if 3 K_(i,oo)+12 gamma D_i=0, equivalently the equality
stated after (3). No other response jets are part of this comparison.
No top/top or conditional mixed quartic coefficient is added again.

The audit therefore closes the existence-of-limit part of the assessed
target. It leaves its numerical/analytic coefficient comparison open.
A vanishing coefficient would give only o(a^-3), not an O(a^-2) bound
or the interacting bound needed for the main Yang--Mills problem.

## Mathlib

Full matching theorem: **not checked**. Supporting finite linearity
of limits and asymptotic arithmetic: **not checked**. Unknown coverage
does not imply absence. All specialized finite contractions and scaled
limits are imported by their canonical local equation/section citations
above. No fresh external theorem, numerical certificate or reproof of
the existing Wick, kernel or localization estimates is used.
