# Stable support lifts — working record

The exact saved target has the prior SPECIALIZE assessment in
[the source review](literature/2026-10-03-degree-three-support-stable-lifts.md).
Reuse it unchanged. The gap is support compatibility and a
criterion that includes images contained in collision strata.
Its downstream use is screening an independent non-scalar
support map before pulling back the universal sheaf. Such a map,
its action, transverse coverage and the universal Hodge gap remain
later unresolved steps.

Continue if Yoshioka's specified transform preserves the weighted
support on every stable fibre and the pulled-back Rees algebra
gives the correct lift data. Restrict a claimed criterion if either
check fails. The scalar one-moving-point recipe remains stopped.

## Reasoning saved before the boundary check

Use the isomorphism in Yoshioka's Proposition 3.4, not an arbitrary
abstract isomorphism. Its fibre transform is
G(E)=Rp_{2*}RHom(p_1^*E,I_Delta), with only G^1(E)=I_Z nonzero.
For Q=E^{**}/E, applying the diagonal triangle should give

0 -> I_Z -> Ext^1(E,O_S) tensor O_S
  -> sheaf Ext^1(E,O_S) -> 0.

L039's fibre calculation gives E^{**}=O_S^2 and
dim Ext^1(E,O_S)=1. Dualizing the hull sequence identifies the
last sheaf with sheaf Ext^2(Q,O_S). The remaining checks are the
evaluation isomorphism in degree zero, the triangle's direction,
and preservation of each punctual length by this finite-length
dual. If these hold, the quotient is O_Z up to a scalar line,
not the original module Q. This would give support agreement
even at a nonreduced triple point, without a density assumption
on a particular parameter surface.

For Y=S^{(3)}, retain Ekedahl--Skjelnes' actual ideal of norms J
and its Rees algebra R=direct sum J^n. Stable lifts of g:B -> Y
should correspond to a line bundle L and a graded quotient
g^*R -> direct sum L^{tensor n}, surjective in degree one.
The map must respect the Rees relations; g^*R cannot be replaced
by the Rees algebra of the image ideal J O_B when g lands in
the centre. For an integral B generically outside the centre,
test necessity as well as sufficiency of invertibility of
J O_B. No assertion that every support map lifts is intended.

Known moduli and Proj statements are imported. Only the support
comparison and applicability differences are being specialized.
No originality, non-scalar cycle or complete candidate is claimed.

## Completed specialization and critical checks

The full proof is [L040](../lemmas/L040-degree-three-support-stable-lifting-criterion.md).
The saved continuation test passes. The diagonal triangle gives
the proposed sequence, with a degree-zero evaluation isomorphism
and a one-dimensional global Ext coefficient. Its quotient is
the finite-length dual of Q. A composition series and the local
Koszul resolution preserve each punctual length, establishing
support agreement at every collision. Equality on all closed
points then proves equality of the parameter morphisms because
the smooth parameter surface is reduced; no dense distinct-point
locus is needed.

The imported Hilbert--Chow blowup is over the actual symmetric
product. Its relative-Proj functor gives the line-bundle quotient
with all Rees relations. For an integral parameter surface
generically outside the centre, pulling back the tautological
ideal gives a generically nonzero map from a line bundle to O_B.
It is injective there and everywhere on the integral base,
proving the necessity of an invertible image ideal. The cited
Cartier universal property gives sufficiency and uniqueness.
For an entirely exceptional image this proof has no nonempty
open set; a constant map to any punctual length-three subscheme
is a lift despite the zero image ideal. The full Rees algebra
retains those exceptional fibres.

Read the exact supporting statements while checking their
applicability: Yoshioka's Proposition 3.4, especially its
specified transform and all-fibre vanishings; Ekedahl--Skjelnes'
section 7.24 and Corollary 7.28 with the over-base norm map;
Stacks Tags 01O4 and 0806. The prior SPECIALIZE assessment
was reused byte-for-byte, and the known global model was not
reproved. No new target was researched in this step.

L040 uses L039 for the actual fibre data, family support
morphism and action. Earlier scalar and deformation failures
are contrasts, not mathematical inputs to its proof. No
script or numerical calculation is needed for this criterion.
Classification is REPRODUCTION, with Mathlib coverage not
checked and no claimed progress beyond the checked literature.
The known span remains 21 on the Dickson family, with three
RM directions against four required. An independent non-scalar
support action remains missing.
