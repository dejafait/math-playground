# Fixed-family support feasibility working note

Approved target: determine whether eight labels from L163's forty-label
set can join L162's four supports with intersections at most one and
coordinate degrees at most four. Reuse the invocation-start SPECIALIZE
assessment; no new source search is needed.

The main gap is uniform twelve-row exclusion. This bounded test addresses
only the fixed L162 family. Inspecting the original labels suggests that
their S-pairs have indices 4,9,16,18,20, hence all contain coordinate 27.
The fixed row 477 also contains 27. Verify the complete label universe,
fixed contributions and integer capacities before using this obstruction.
If confirmed, any eight additions give degree nine at 27, exceeding four.
This would stop this particular twelve-row construction; it would leave
other plane families and every coding/source/radius gap unresolved.

Completed: the common-coordinate obstruction is confirmed. Canonical
proof: L164; complete incidence producer and independent verifier are
`scripts/seven-coordinate/forty_support_compatibility.py` and
`scripts/seven-coordinate/verify_forty_support_compatibility.py`.
All 226 verification checks pass, including every B label and fixed row.
This is an informative negative finite feasibility decision; no longer
an unresolved search. Separate later critical audit remains pending.

Continuation/abandonment test: require all forty reconstructions and a
separate checker to agree with the canonical labels; otherwise preserve
the failed check and leave finite feasibility unresolved. A complete
short obstruction replaces exhaustive subset enumeration without using
any maximal-clique-only shortcut.
