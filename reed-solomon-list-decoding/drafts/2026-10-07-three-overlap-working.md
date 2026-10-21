# Three-overlap criterion working checkpoint

Approved target: exact realizability for three 68-supports, common core
60, three disjoint pair-only triples, two private points each. Prior
SPECIALIZE assessment: literature/2026-10-07-sixty-core-three-overlap-criterion.md.

Attempt in progress: remove degree-60 common-root product. Each cyclic
row difference is a constant times its monic overlap cubic. Thus the
4-by-3 coefficient matrix must have a nonzero kernel. Any two columns
are independent because their monic cubics have disjoint roots; rank two
therefore forces all three kernel coordinates nonzero. Descend the rank
test to E, construct scalar messages and a compatible center, append zero
rows. Consecutive-power triples should be rank three by a Vandermonde
minor on coefficients of X^3,X^2,X. Nonvacuity is still being tested.
A preliminary sum-zero search found only two triples per fixed quadratic
coefficient; this exploratory observation is not a nonexistence proof.

Main gap remains arbitrary-center safety at 68/67 agreements. A
nonvacuous new restriction might support a 60-core cap, but no such cap,
transfer, or large-list realization is proved. Continue if both realized
and forbidden configurations exist; otherwise retain the unresolved
nonvacuity and do not claim a useful counting restriction.

Completed outcome: L033 contains the canonical criterion and both exact
actual-label examples; scripts/finite-support/three-overlap-results.json
retains the complete certificate. A fixed-sum-one diagnostic found the
three recorded overlap triples. All realized maximal minors vanish and
all forbidden ones are nonzero. Independent critical audit is next, after
separate approval; no quantitative cap was attempted.
