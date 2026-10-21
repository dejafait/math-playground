# Conditional triple classification — saved attempt

Date: 2026-10-07. Approved target: classify the support incidences and
nonzero weight relations of three L010 equality errors at distinct finite
parameters with union of size at most eight, using their fixed-block affine
lift and separating L015's five-coordinate case. RESEARCH / REPRODUCTION.
Prior assessment: `literature/2026-10-06-three-support-fixed-block-classification.md`.

Main gap: arbitrary-family sixteen-count equality; interval 11/q–16/q
against allowable fifteen. Input L010 supplies actual full-weight errors,
distinct supports and eight-column invertibility. Reuse the fixed-block
passage in L031 and scalar-affine zero accounting in L006/L007; their
global sparse bounds are not applicable here. L015 is a field-specific
comparison, not a uniform premise. ATTEMPTS/017, /019, /020 stay stopped.

Saved reasoning before the full write-up: enlarge the selected union U to
eight coordinates and invert the moment map. Each used coordinate is a
nonzero affine polynomial, so it can be absent at only one of the three
selected parameters. Let Z_i=U minus A_i and m=|U|. The Z_i are disjoint,
each has m-4 elements, and 3(m-4)<=m. Distinct supports give m>=5;
therefore m=5 or 6. The common intersection has 12-2m elements. On Z_i,
f_x(T)=c_x(T-gamma_i), c_x nonzero. On the common intersection, f_x is
any affine polynomial nonzero at all selected parameters, including
nonzero constants. This is a prospective exact local classification;
its converse must be limited to the three errors' affine/moment
compatibility, never existence of an equality completion.

Continuation/abandonment test: complete an exhaustive, field-uniform
proof and all nonzero-weight relations. Abandon a stronger exclusion if
these local conditions admit a triple. No universal small-union triple,
all-sixteen completion, global fifteen bound, source correspondence or
stronger-source novelty claim is available. The canonical completed
result will replace this draft as the proof reference; preserve this
setup as evidence of the bounded attempt.

## Completed bounded attempt

The full specialization is now canonical in
[L032](../lemmas/L032-three-support-fixed-block-classification.md).
Outcome ADVANCE / REPRODUCTION: exhaustive conditional incidence and
weight relations, plus a converse limited to local affine-moment
compatibility. No sixteen-error completion or global bound improvement.
A separate critical-audit scope approval is the only next action.
