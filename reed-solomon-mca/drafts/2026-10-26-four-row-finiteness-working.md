# Step 499 — bounded four-row finiteness attempt

The invocation-start EXPLORE assessment is
`drafts/literature/2026-10-25-four-row-finiteness-review.md`.
Main gap: uniform twelve-row exclusion. The approved intermediate target
is universal four-row finiteness on its exact two-disjoint-pairs domain,
or one explicit infinite exact-rank-one family over algebraic closure.
Finiteness could reduce later-row tests to finitely many branches;
second-pair extraction and all coding gates remain independent gaps.

Before calculation: L115's common-factor infinite locus fails disjointness
of the second pair. L117's crossed overlap pairs have a two-point locus,
but its second pair also intersects (at 75). L120 and the recorded
L110/L125 fixed-pair calculations do not establish the universal claim.
ATTEMPTS/041–043,/048–049 forbid neither an exact local locus computation
nor this changed mechanism; rank alone is insufficient.

Test at most these three explicit quadruples, in the displayed a,b,c,d
order, with original L109 maps and S={1,8,12,18,22,27,33}:

1. ((1,8),(47,50)), ((12,18),(64,79)),
   ((1,12),(70,75)), ((8,18),(85,89)).
2. ((1,8),(64,96)), ((12,18),(79,89)),
   ((1,12),(47,85)), ((8,18),(50,70)).
3. ((1,8),(47,50)), ((12,18),(64,79)),
   ((1,22),(70,75)), ((8,27),(85,89)).

The first two replace the inadmissible common-factor pattern by crossed
overlap pairs, with different external labels. The third breaks that
rectangle. They are specified before computation; no census or random
search will follow. Compute complete original exterior kernels with
nonzero minors, then resolve all decomposability equations and four
rank-zero exclusions. Continue this local mechanism only if it gives an
infinite family; otherwise record the exact local failure and do not
infer universal finiteness. A positive exterior dimension or finite-field
samples alone do not meet the test. No coding gates are assumed.

The standard arbitrary-field linear algebra is imported through the
ready assessment (Kostrikin–Manin, Chapter 1 Theorem 3.12 and sections
6.2–6.9); L109 supplies the original quotient and Plucker formulas.
Preexisting work is preserved.

Completed: exact locus cardinalities are 2, 2 and 0. Full proofs and
the three nonzero-minor witnesses are canonical in L158; the complete
certificate is `scripts/seven-coordinate/four-row-finiteness-probe.json`.
Both nonempty loci contain exactly span(e_1,e_18) and span(e_8,e_12),
with four ranks exactly one. All 35 restricted Plucker equations and
all 16 nonempty-case quotient restrictions were inspected completely.
There were no calculation-check failures. The candidate infinite-family
test failed in all three cases, so this finite perturbation experiment
stops here. Universal finiteness is unresolved; these new local negative
tests do not establish that no other exceptional family exists.

Continuation under the unchanged ready target should use a structural
argument on arbitrary original quadruples, separating coincident from
distinct kernel-intersection lines. Neither branch is assumed finite.
No fourth numeric example, repeat rank census or source retrieval is
proposed. The exact same target and assessment remain in PROGRESS.md.
