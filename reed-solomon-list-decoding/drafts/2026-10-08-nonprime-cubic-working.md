# Changed-coordinate cubic diagnostic — working record

Approved target: Test whole-pattern avoidance for the shortened cubic family over F_121 on {0,1,2,3,4,5,6,u}.

The gate-approved EXPLORE assessment is
`drafts/literature/2026-10-08-nonprime-coordinate-cubic-pattern.md`.
Main gap: arbitrary-center 67/68-agreement safety, with the existing
955–957 bracket. Intermediate target: one exact permitted four-block
incidence witness on this fixed evaluation set. A witness stops this
avoidance construction; a bounded miss leaves the question unresolved.
Possible downstream use of complete avoidance would still require the
independent L033 clause, actual labels and L034 cap conversion.

Inputs read: full L032 and ATTEMPTS/023, exact L031 and L034
hypotheses/conclusions. Sources and their restrictions are reused from
the approved assessment; no further literature is needed for direct
finite verification. The original stop is preserved. No verified GRS
equivalence transferring the old witness is available.

Bounded plan: test the old coefficients directly; test the prescribed
parallelogram subclass by signed matrices; if needed, test at most 10000
deterministically sampled general K4 edge-pair assignments with disjoint
incident coordinate sets. Search completeness is never an exclusion
claim. Check all eight graph values, complete pair intersections,
mutually disjoint point sets, two private points per block and deletion.
Auxiliary K is not the actual subgroup field. No RS realization or cap
comparison follows from an abstract witness.

Completed: the first parallelogram partition supplies the exact witness
recorded in canonical L039. Its complete certificate is
`scripts/finite-support/nonprime-cubic-results.json`: 192 checks, no
failures. The general sampling stage was not reached. The old
coefficients directly fail the required edge-14 size, but the new
witness refutes avoidance; this is an informative NEGATIVE, not a
search miss or a boundary advance. Preserve ATTEMPTS/025 as this
family's stop. No further coordinate changes were tested.
