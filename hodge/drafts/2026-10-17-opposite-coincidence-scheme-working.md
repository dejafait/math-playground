# Opposite coincidence scheme — step 356 working checkpoint

Approved target: test finiteness and reducedness of the entire
off-diagonal fibre product of L118's actual opposite map, using the
pre-existing EXPLORE assessment
`drafts/literature/2026-10-17-opposite-coincidence-scheme-finiteness.md`.
No additional literature search or mathematical script is planned.

Inputs read: audited L118's actual quaternionic differential, common
ambient harmonic metric and parametrized geodesy; audited L120's finite
unramified map and degree-one normalization. The older two-branch source
comparison does not force equal tangents. ATTEMPTS/046 allows isolated
Hom jumps and remains stopped. Existing unfinished notebook changes are
preserved; no sibling notebook is used.

Proposed argument, not yet a checked conclusion: at a collision,
the two tangent images are quaternionic lines. Equal lines would give
the same local image by exponential-map uniqueness for totally geodesic
immersions. Two disjoint source neighborhoods would then contradict
the finite birational map's isomorphism on a dense open of its image.
Distinct quaternionic lines intersect trivially, so the actual
fibre-product tangent is zero; Nakayama should make its local ring C.
The diagonal is open by unramifiedness and closed by separatedness,
so its complement is proper. Zero tangent at every closed point should
then give a finite reduced C-scheme, including the empty case.

Remaining checks: use one actual common ambient chart and metric at
isomorphic fibres; justify the overlap/dense-open contradiction without
globalizing a local isometry; compute the scheme tangent with dual
numbers and retain nilpotents; prove properness of the off-diagonal
scheme before invoking proper plus locally quasi-finite finiteness.

Continue only if all these local/global passages work. Do not assume
normality of the original image, a complete ambient metric, emptiness
of collisions or existence of F. Possible downstream use is a finite
collision reduction for a later separation invariant; the primitive
Hodge-realization and transverse-transport gaps stay independent.

Completion: the argument and all these passages are now written in
`lemmas/L121-opposite-finite-reduced-coincidences.md`. The working
proposal above is retained as the pre-proof interruption checkpoint.
The achieved result is conditional finiteness and reducedness, not
collision emptiness, and awaits a separate critical audit. This file
does not replace the canonical proof or current PROGRESS.md routing.
