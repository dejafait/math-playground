# Three quaternionic lines — saved calculation

Approved target: the exact TARGET in
`literature/2026-10-17-three-quaternionic-lines-gluing-test.md` (SPECIALIZE).
One proof attempt, classified REPRODUCTION; no external source refresh.

Let R=C[[x_1,x_2,y_1,y_2]], with ideals I_1=(y_1,y_2),
I_2=(x_1,x_2), I_3=(y_1-x_1,y_2-x_2). Use their intersection,
not a fibre-constant gluing, for the reduced union A. In its normalization
T=C[[z_1,z_2]]^3, restriction sends F to
(F(z,0),F(0,z),F(z,z)). Its image consists exactly of triples (a,b,c)
with equal constants and dc(0)=da(0)+db(0). For sufficiency start with
a(x)+b(y)-a(0) and correct the diagonal residual q in (z_1,z_2)^2
by x_1 q_1(y)+x_2 q_2(y), where q=z_1 q_1+z_2 q_2 and q_i have
zero constant. This proves termination in all degrees, not a jet guess.

Thus Q=T/A has two constant and two linear dimensions, length 4 > 2.
Each pair sum I_i+I_j is the full maximal ideal, but
I_i+intersection_{j!=i} I_j restricts to the square of the branch maximal
ideal, not the maximal ideal. All simultaneous identities fail. Each
branch is a quaternionic totally geodesic plane; isometric diagonal
parametrization is u -> (u,u)/sqrt(2). Pair fibre products are reduced
points; the off-diagonal part has six ordered points, separated from the
diagonal. Normalization is finite and unramified, componentwise birational.

Scope: independent flat germ only. It retains selected local consequences
of audited L118/L120/L121, not the nonflat K3 metric, connected global
normalization, global F or mixed tensor. Actual-image defect remains
uncomputed. Full canonical proof will be saved as L122; no general
arrangement calculation or global coherent-cohomology attempt is needed.
