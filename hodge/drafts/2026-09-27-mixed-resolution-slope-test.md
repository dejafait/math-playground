# Mixed-divisor resolution — completed presentation test

The prior EXPLORE assessment is
[the multiple-divisor review](literature/2026-09-27-multiple-divisor-stable-resolutions.md).
The target and common metric are unchanged. Reuse its inspected slope
and invariant-class inputs; no new construction theorem is assumed.

## Gap and test

The gap is a stable bundle representing a nonzero multiple of the
cubic action that could support a later transverse transport test.
For the selected recipe, first test the actual terminal inclusion
into a sum of line bundles at L025's metric. Invariant c_1 gives
slope zero. A stable bundle of that slope has no nonzero morphism
to a negative-degree line bundle. Thus anti-ample terminal summands
already exclude the untwisted recipe, independently of c_2.

A final twist changes the terminal summands as well as the bundle.
This necessary test must be applied to those changed terms before
extending the exclusion. It does not follow that all twists fail.
Continue only with an informative scoped obstruction or an actual
presentation candidate; a formal divisor tensor is insufficient.
The main threshold remains four RM directions against three attained,
and the known cycle span remains 21-dimensional. Even compatible bundle
existence would leave transverse transport and the universal goal open.

## Result and limits

For a stable bundle of rank greater than one and degree zero, the
map to a degree-zero line also vanishes: a rank-one image would be
a quotient of positive degree by stability but a subsheaf of a line
of nonpositive degree. Hence every component of the terminal
inclusion into a nonpositive-degree summand vanishes.

Write the twisted terminal sum as Q direct sum R, where Q consists
of its strictly positive-degree summands. The inclusion factors
through Q. The terminal cokernel is torsion-free because it is a
subsheaf of the next line-bundle sum, or of I_C in a one-term
presentation. It follows that Q/E is torsion-free. If rank(Q)=rank(E),
this quotient is zero, forcing E=Q and contradicting degree(E)=0.
Thus at least rank(E)+1 positive-degree summands are necessary.

The completed proof, including all twists and the nonzero transcendental
action, is [L027](../lemmas/L027-mixed-resolution-slope-and-divisor-rank-obstructions.md).
It applies to any finite resolution of the stated form; no particular
length or map-recovery vanishing is assumed. Rank one is impossible
because its second Chern character would act trivially on T(S).

There is also an obstruction that survives every final twist. The
normalized second character has mixed operator eU on T(S) and
2e id+R on NS(S), where e is the resolution's parity sign. The
correction R factors through the spans of the original divisor
classes in each factor. Invariance forces the nonzero eigenvalue
e(lambda-2), of degree three, on R. Thus R has rank at least three,
and both factor spans must have dimension at least three. This
extends the single-polarization exclusion to two-dimensional spans;
it does not exclude arbitrary mixed resolutions.

For terms in the particular W=im(A) of L025, L027 fixes the required
correction as e(A-2 id)pi_W and fixes the W projections of a possible
twisting class. The rational eigenvector has no annihilating nonzero
rational linear functional on W, so these are forced equations,
not adjustable divisor tensors. Integrality of the twist, actual
maps, exactness and stability still require proof.

Stop the untwisted anti-ample recipe and every presentation with at
most two divisor dimensions in either factor. No full compatible
bundle, transverse lift or complete candidate has emerged. A source
comparison for the specific minimal cubic subspace has been saved
as REVIEW_REQUIRED; no construction calculation for it was performed.
The negative result changes the admissible recipe, while the known
21-dimensional cycle span and three-versus-four deformation threshold
remain unchanged.

## Literature and overlap

The saved assessment is reused unchanged. The slope vanishing and
invariant-form facts are imported by their precise citations in L027;
the scoped exclusions are classified as REPRODUCTION. The checked
sources were not established to contain this entire specialization,
and no claim of originality is made. L026 supplies the full action
of C and the twist-invariant Chern calculation. L012's separate
map-recovery hypotheses have not been asserted for a new presentation.

## Mathlib

Coverage: **not checked**. L027 retains the named supporting results
and direct source links. No full matching Mathlib declaration or
absence from checked Mathlib sources is claimed.
