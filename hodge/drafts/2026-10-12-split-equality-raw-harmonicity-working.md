# Split equality raw harmonicity — working checkpoint

2026-10-12, step 242; approved target and scope are the unchanged
SPECIALIZE assessment `drafts/literature/2026-10-12-split-equality-mixed-curvature-harmonicity.md`.

Main gap: universal primitive rational Hodge realization. Intermediate
test: actual mixed curvature of the hypothetical (14,21) kernel must
be ASD-harmonic and have strictly positive raw norm in every nonzero
base direction. Downstream use: decide the actual zero-derivative
alternative without asserting a realized germ, kernel or transport.

Inputs read: complete L070 and L071; relevant L093 equality passage;
complete L094 including its separate audit; ATTEMPTS/061 and history/240.
The supplied source assessment is reused. No general moduli theorem,
scalar-Laplacian inverse or new source is needed.

Unfinished argument: use S_2 as base and S_1 as fibre, with
r_u(t)=R_F(u,t). Coefficient Bianchi gives d_A r_u= nabla_u R_Y,
with the product Levi-Civita connection and actual coefficient
connection. Fibre ASD and fixed fibre metric imply d_A^+r_u=0.
Hyperholomorphicity gives r_{Iu}=I_c r_u. L094's audited real
contractions give C_I(I_c r_u)=C_0(r_u), so ASD of r_{Iu}
implies C_0(r_u)=0, hence d_A^*r_u=0. Must check horizontal
connection terms, tensorial differentiation and determinant before
finalizing this passage.

For the norm reuse only L070's raw algebraic identity gamma=-c sigma,
checking its connection and transpose hypotheses with factors reversed.
The negative tensor should give [gamma]=-2lambda[sigma], hence c=2lambda
if the actual closed pure-type integral is justified. Strict positivity
would then identify r_u=P_V r_u and remove the zero derivative.
An uncontrolled derivative, merely nonnegative norm, or a sign change
in the ordered integral stops that conclusion. No mathematical result
is claimed by this working checkpoint.

Independent gaps: integration of compatible tangents, exact higher
obstructions, global realization with the full tensor, equality and
positive-Euler kernels, transport and universal Hodge realization.

Completed checkpoint: the full proof attempt is now canonical in
`lemmas/L095-split-equality-raw-harmonicity-and-positive-norm.md`.
The horizontal commutator is retained, Coulomb follows from ASD in
the Iu direction, and first-factor integration gives c=2lambda>0.
This working note preserves the preliminary reasoning; it is not an
additional lemma or an independent verification. Separate audit is
required and no new continuation is approved here.
