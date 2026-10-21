# Curvature two-jet calculation — working checkpoint

Approved target: assess L143's exact (r,s)=(2,1) tuple under the
necessary type, Bianchi, differentiated Bianchi and full Ricci identities.
Pre-existing SPECIALIZE coverage:
`drafts/literature/2026-10-21-mixed-curvature-two-jet-feasibility.md`.
No new source review or changed target is being undertaken.

The universal primitive Hodge gap and equality-kernel existence remain
open. A compatibility verdict would delimit this finite obstruction;
incompatibility or a residual base-curvature condition could identify an
additional necessary constraint. Stop at that verdict, without higher
prolongation, flat substitution or connection-realization inference.

Inputs read: L071's full invariant-Chern/connection passage, L131's
actual determinant-one connection, all of L143 and ATTEMPTS/083–084.
Their older sign and variational stops remain intact. Existing notebook
changes, including L043, are preserved.

Prospective convention: V_ij;ab=(nabla^2 R)(e_i,e_j;e_a,e_b), with
[nabla_i,nabla_j] acting as coefficient commutator minus the two base
covector actions. Choose U=0, which solves the homogeneous first Bianchi
test without asserting the actual derivative vanishes. Parametrize each
K3 base block by a symmetric trace-free 3x3 matrix on its ASD forms;
retain all five parameters in each block. Solve for the 36x10 symmetric-
derivative degrees of freedom per su(2) coordinate over Q, then verify
every original equation coefficientwise in the ten parameters. This is
a necessary tensor feasibility test only.

Completed: the uniform compatibility verdict, full proof, exact affine
witness, all original-equation checks and limitations are canonical in
L144 and `scripts/curvature-two-jet/fixed_tuple_certificate.json`.
There are no residual base-curvature conditions. The bounded exclusion
route is parked; the separate critical audit remains pending. No local
connection or global bundle realization is claimed.
