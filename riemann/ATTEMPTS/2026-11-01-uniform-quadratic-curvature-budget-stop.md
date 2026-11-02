# Uniform quadratic-curvature/absolute-tail envelope — stop

The approved test is completed in
[C499d](../lemmas/C499d-uniform-quadratic-curvature-envelope-stop.md),
with the full exact certificate under `scripts/heat/` as cited there.
This is an informative failure of one known-method specialization.

WHY IT FAILS: after the integer-valued quadratic subtraction, near-cutoff
curvature is small and an entry equality prevents a positive-curvature
estimate through the final point. Every tested smooth-initial/absolute-tail
split costs more than the trivial full-prefix bound 256, even with a
sharper endpoint curvature cap. Abel weighting and complete Euler/resultant
triangle bounds then give a uniform sufficient cost >.00072254689,
against r0<.00042249382. Both charges are independently uniform and
the enclosure width is <1e-30, so precision is not the obstruction.
This does not bound the actual increment below, refute uniform exclusion,
or affect C499c's qualified endpoint certificate. Park this envelope;
reopening needs a different estimate retaining additional signed structure,
with separate source coverage and an independently testable whole-interval
criterion. No adjacent endpoint calculation is a continuation of this test.
