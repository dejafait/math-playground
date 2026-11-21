# Step66 working record: the approved full polynomial field class

Started 9 November 2026 under the unchanged EXPLORE assessment
`drafts/literature/2026-11-09-l938-simplex-residual-certificate-test-63.md`.
This retains the working reasoning and diagnostic, not a crossing
certificate or a later audit.

The main gap is L030–L032/C032a actual-Xi all-degree mixed positivity.
The sole target is the existing degree-at-most-13, E-independent,
rational, equivariant, tangent and face-preserving field, affine a(E),
and uniform strict residual on 1/4<=E<=4. Compact crossings could feed
the Laplace route; all other energies and independent endpoint signs
remain unresolved. Success requires a rigorous uniform positive
residual or a rigorous dual for the entire allowed class. A numerical
feasibility result is only diagnostic.

Read L019, L938's full row table and analytic-k input, L940's averaging
definition and proof, L942's complete proof, and step63's inspected
source notes. The recorded two-field stop is retained. No source
refresh, new target or enlarged ansatz is being proposed.

The exact 171-dimensional representation and its full proof are now
canonical in [L943](../lemmas/L943-full-degree-thirteen-simplex-field-coordinates.md).
Its later independent audit remains pending. The numerical screen
includes L942's root midpoints, which are explicitly not substituted
for exact algebraic zeros in any proof, and the vertex limit.

The record is `scripts/heat/l938-full-field-screen-66.json` plus `.npz`.
One fixed E=1/4 screen used 598 rational points. It retained 168 of
172 numerical columns and stopped at the coefficient magnitude limit.
Its nominal positive sampled minimum and negative dual objective are
inconclusive: neither is certified and the dual column defect is nonzero.
A held-out E=4 evaluation of the same field with constant a has 298
negative samples. No uniform residual or full-class obstruction results.

During implementation, grouping the polynomial and theta summands
before rather than after division by n_r produced a different floating
candidate (initial printed sample minimum 4.91746912*10^12, final
3.21451459*10^12). These are algebraically equivalent formulas, not
two independent mathematical tests. The discrepancy reinforces the
need for exact conditioning and certified arithmetic. Only the final
complete matrix/candidate is retained; the earlier printed diagnostic
is recorded here without claiming a reproducible certificate for it.

This is one EXPLORATION attempt, not an informative full-class negative
result. The representation is useful local preparation; originality
and progress beyond the checked sources are not claimed. The refined
continuation is exact algebraic conditioning of the same 171 columns,
with both energy endpoints included before attempting uniform bounds.
It must still prove a uniform margin or an exact annihilating dual;
another sampled positive fit alone would not satisfy the target.
