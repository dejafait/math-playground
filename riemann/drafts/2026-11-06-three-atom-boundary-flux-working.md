# Fixed three-atom boundary-flux attempt — working record

Approved input: `drafts/literature/2026-11-06-three-atom-heat-minor-boundary-flux.md`
(SPECIALIZE, supplied before this invocation). The exact target is the
fixed support {0,1,4}, rank-two 3-by-3 block, every proper square minor
strictly positive, zero determinant and positive first time derivative.
This is a REPRODUCTION calculation, not an actual-Xi sign claim.

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity. The
downstream use is to test whether raw moment positivity and the proper
minors alone can justify backward heat descent. A witness stops that
premise; nonexistence only covers this family; an inconclusive bounded
attempt does not authorize a support/rank expansion.

Reused the supplied assessment and its parent source comparison; read
L827's exact normalization/finite feasibility and completed-audit scope.
Its reciprocal law is different and supplies no sign input here. The
source Cor3.2/Prop3.3/Prop9.1 is used only for differentiation, with every
finite coefficient shift and determinant derivative to be checked below.
No other lemma is a mathematical input to the new finite law.

Plan: remove the common positive weight using p4, eliminate p0 from the
determinant, and test every minor and the signed flux with exact rational
arithmetic. Save the complete certificate under scripts/heat/; a floating
near-boundary point will not count as equality evidence.

Unresolved at checkpoint: boundary existence, all nine 2-by-2 signs,
rank and flux. Mathlib matching coverage unchecked. Prior notebook work
and stopped actual-theta routes are preserved.

## Completed bounded calculation

Sympy was unavailable (`ModuleNotFoundError`); no installation was
attempted. Exact standard-library Fraction arithmetic sufficed. An
initial diagnostic set p4 to1, tried b/c equal to 1/10000, 1/100, 1/10,
1, 10, 100, 1000, 10000, 1000000, and solved the determinant's linear
equation for a/c. All solutions had a/c<0, hence none was a valid
probability law even where proper 2-by-2 minors and flux were positive.
This was only diagnostic, not nonexistence evidence.

Exact polynomial elimination then gave a strictly positive decomposition
for the determinant throughout the positive simplex. The completed
proof is canonical in L843; do not use the diagnostic as a witness.
The full certificate is
`scripts/heat/three-atom-boundary-flux-20261106.json`, status
FIXED_SUPPORT_NO_BOUNDARY, seven exact identity checks, no failures.
The exact q0–q5, determinant and all three derivative-row terms were
inspected in full through the shared JSON inspector. There is no
boundary; checking nine proper minors cannot restore one, so no minor
search, numerical flux search or support expansion was performed.

The finite-law discriminator closes negatively. This gives neither a
general counterexample nor a cone-invariance theorem and changes no
actual-Xi argument. No unfinished work from another route was altered.
