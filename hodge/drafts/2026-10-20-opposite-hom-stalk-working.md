# Opposite Hom stalk — bounded attempt, step 417

Completed: the canonical conditional proof is in
[L135](../lemmas/L135-opposite-off-diagonal-relative-hom-stalk-length.md).
The notes below preserve the pre-proof reasoning; a separate critical
audit is still required.

Approved target: determine the actual ordinary R^2 relative Hom stalk
length at a selected off-diagonal coincidence of L121. Reuse the unchanged
SPECIALIZE assessment `literature/2026-10-20-opposite-off-diagonal-relative-hom-stalk.md`.

Main gap: universal primitive Hodge realization. Intermediate threshold:
length one, potentially useful for a later global coincidence budget,
which is not known. F and the selected collision remain assumptions.

Working calculation: each actual fibre has character 2-21 eta, so pair
Euler characteristic is -76 and the collision Ext dimensions are
(1,78,1). A minimal representative over the smooth four-dimensional
pair base is R -> R^78 -> R. The actual forward degree-one variation
is b |-> a_2 wedge b + b wedge a_1. Paired with a reverse isomorphism
psi, graded cyclicity makes this the negative Serre pairing of
a_1 psi - psi a_2 with b. The reverse degree-zero variation is precisely
that difference. L118's natural KS identification and L121's disjoint
tangent planes should make this difference injective on all four
directions. Its transpose would give I+m^2=m, and Nakayama I=m.

Continuation/abandonment test: justify the actual coefficient/minimal
complex connecting-map comparison, retaining both Hom factors and
the reverse Serre sign. Stop if that comparison or rank fails. Reduced
coincidence and derived Ext^2 dimension one alone are insufficient.
L066 and L110 are method comparisons only; ATTEMPTS/046's separation
stop is preserved. Canonical proof is to be written only after these
checks; no complete result is claimed by this working note.
