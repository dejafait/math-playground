# Fixed affine four-neighbor test — working checkpoint

The gate-approved target is the exact TARGET in
`literature/2026-10-08-affine-four-neighbor-incidence-test.md`.
Main gap: arbitrary-center 68-agreement safety, with the 955–957 bracket.
Downstream use: decide whole-pattern avoidance for L035's fixed family;
neither incidence presence nor absence proves actual-label admissibility
or the L034 family cap. Stop the avoidance route on a verified witness.

Before computation, the prospective complete reduction is as follows.
Equal head classes have intersection at least three, hence cannot occur
in the required pattern. Distinct slopes have at most one common tail
point. Each of the six pairs therefore needs at least one common head
point. Empty triple intersections imply that each head point belongs to
at most two blocks. The twelve head memberships can supply at most six
pair-head points, so all six pair intersections have exactly one head
point and one tail point. No private head points remain. The six head
points are distinct. Thus the four heads are the stars of the six edges
of K4 embedded in the eight-point head. Enumerate all four-subsets of
the 56 triples and retain these precise head conditions (expected 840).

For each fixed ordered head quadruple, subtract the first intercept
from every intercept. This common vertical translation preserves the
family, every pair/triple intersection and private part. Normalize b1=0.
Enumerate the three coordinates x12,x13,x14 in {0,...,4}; they must be
distinct since a shared incident coordinate would create a triple tail
point. Set bj=(s1-sj)*x1j modulo 191. Test the remaining pair crossings,
then directly intersect the complete eight-point blocks. Opposite edges
may reuse coordinates when their ordinates differ. A miss is conclusive
only after verifying this enumeration covers every normalized quadruple.

Inputs read: L035's full fixed-family construction and intersection
argument; L031's complete incidence hypotheses; L032's witness and
coordinate-reuse trap; relevant ATTEMPTS/019–021,023–024. The ready
assessment reuses inspected AGL/AVZ sources. No additional literature is
needed for this finite test. Existing unfinished work is preserved.

Unresolved: actual-label ranks, nonanchored L033, full admissibility,
L034 conversion, cross-core consistency, common-center RS realization,
67-agreement safety and ABF equivalence. F_191 is auxiliary.

## Completed finite attempt

The complete reduction and result are now canonical in L036. The
producer exhausted all 50400 reduced candidates without a witness.
The independent checker retained all 105000 candidates, including
repeated incident coordinates, reconstructed every producer row, and
found 4220 all-six-tail-pair cases but zero with empty triples. All
checks passed and failures are empty. Full certificates are under
`scripts/finite-support/affine-four-incidence*-results.json`.
This establishes the fixed-family exclusion only; the separate critical
review remains pending its coverage assessment in PROGRESS.md.
