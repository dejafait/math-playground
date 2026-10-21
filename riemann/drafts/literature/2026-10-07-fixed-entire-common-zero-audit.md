# Coverage: critical audit of the fixed-function construction

TARGET: Critically audit L376's fixed-function sparse-product common-zero construction, including uniform phase bounds, simultaneous solvability, the infinite-product limit and the complete simple zero set.
CHECKED: 2026-10-07
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the exact construction assessment and its duplicate/failure comparison; read L376 in full to inventory its audit scope, searched the named topological inputs, and inspected primary Brouwer and bounded-subsequence statements plus the scoped Mathlib source.
SOURCE_EVIDENCE: Laugesen (22 December 2020), Linear Analysis and Partial Differential Equations, Theorem 1.16, printed p. 23 (PDF page 22); Mathlib commit 4beb549110aa44b87d699166cece6e3642bddf34, Topology/MetricSpace/Sequences.lean, tendsto_subseq_of_bounded and its complete short proof; reuse Laine (1993), Theorems 1.2.3–1.2.4, pp. 7–8, from the construction assessment.
COMPARISON: Standard sources cover the finite-dimensional fixed-point, coordinate-subsequence and prescribed-zero product inputs, but do not certify L376's uniform phase bounds or passage of every exact equation to one limiting function; L375's varying family and L068's nonreal-root construction remain different targets.
GAP: The critical mathematical audit of L376 remains undone; its phase branch, constants, self-map property, diagonal/tail limit, nonvanishing residual product, complete simple zero set and order must all be checked independently.
REASON: The new audit-scope inventory and exact standard-input checks remove the essential source-coverage gap; the unchanged construction search supports one separate critical audit, without a matching theorem import or a correctness verdict.
SCOPE: Only the stated L376 audit for the fixed product with A=10^6, a_n=A^n, boxes |d_n-(2-32(n-1))|≤1, shift -2i and divisor 5/2+it; standard inputs may be cited, while all construction estimates and limiting claims require mathematical verification. No actual-theta, kernel, count, physical-discriminant or RH assertion is covered.

## Reused coverage and new source comparison

Reuse [the construction assessment](2026-10-07-fixed-function-exact-shift-common-zeros.md)
for the exact geometric class and sparse paired-real-root mechanism.
Its inspected Katkova–Tyaglov–Vishnyakova, Cardon and Walker results
localize shifted-output zeros but do not settle this pair's infinite
common-zero set. Its Laine comparison covers canonical-product
existence for the stated convergence-exponent/genus hypotheses, not
phase interpolation. The saved Lagarias comparison likewise treats
complementary shifted projections, not an unshifted P paired with this
divided projection. These adequate comparisons were not browsed again.
No source establishes originality or substitutes for auditing L376.

Richard S. Laugesen, *Linear Analysis and Partial Differential
Equations*, University of Illinois lecture notes, dated 22 December
2020, [Theorem 1.16](https://publish.illinois.edu/rlaugesen/files/2023/07/554-Lectures.pdf),
printed p. 23, zero-based PDF page 22, states Brouwer for a continuous
self-map of a nonempty closed, bounded, convex subset of a
finite-dimensional normed linear space. Read the full statement and
its proof paragraph: the notes cite the standard theorem rather than
prove it, referring to Zeidler Chapters 12–13. Those chapters were not
read. The named Brouwer theorem is a permitted standard input. The
intended L376 domains are finite rectangles in R^N; the audit must
verify that the displayed map is defined, continuous and a self-map
on each entire rectangle. No contraction, uniqueness or infinite-
dimensional fixed-point conclusion is supplied by this theorem.
The adjacent distinction from Schauder was inspected; Schauder is not
an input and no reproof of either theorem is needed.

The primary [Mathlib source](https://github.com/leanprover-community/mathlib4/blob/4beb549110aa44b87d699166cece6e3642bddf34/Mathlib/Topology/MetricSpace/Sequences.lean)
at commit `4beb549110aa44b87d699166cece6e3642bddf34`, retrieved
2026-10-07, contains `tendsto_subseq_of_bounded`. Its hypotheses are a
pseudometric proper space, a bounded set s and a sequence lying in s.
It returns a limit in closure(s) and a strictly increasing subsequence
index map. Read both this statement and the complete proof reducing it
to `tendsto_subseq_of_frequently_bounded`; that theorem's displayed
proof invokes sequential compactness of the bounded set's closure.
For L376 the intended uses are bounded real coordinates in closed
intervals, followed by a countable diagonal extraction. This supports
the named Bolzano–Weierstrass input; it does not itself check the
diagonal selection or interchange an infinite phase sum with a limit.
Those are part of the separate audit. No new diagonal lemma was proved
in this source review.

L376 writes direct logarithmic-tail and growth estimates rather than
assuming a stronger product theorem. Prior Laine coverage remains
adequate for comparison. The audit must check compact holomorphic
convergence, using the standard Weierstrass locally uniform convergence
theorem where needed, and nonvanishing of the logarithmic tail.
Canonical-product existence alone does not prove the phase equations,
simple multiplicities or the claimed order bound. Independent checking
of these specializations is necessary because the known sources do not
state their uniformity over the adjustable boxes.

## Search record, duplicates and blockers

New queries were `Brouwer fixed point theorem nonempty compact convex
subset finite dimensional continuous map lecture notes proof pdf`,
`site.leanprover-community.github.io/mathlib4_docs Bolzano Weierstrass
subsequence compact sequential`, and
`site.leanprover-community.github.io/mathlib4_docs "Brouwer" fixed point`.
Read the notes' title/date and the targeted theorem range; retrieved the
bounded-subsequence source through its documentation link and inspected
its pinned version. A TIFR PDF request failed; it is a nonessential
alternative, and no statement from it is used. Walker (1997) remains
the prior unread nonessential lead. Neither access failure blocks this
audit of explicit estimates and standard named inputs.

Read L376 in full for its statement and proof inventory, and read the
construction history and the fixed-function/pointwise stop notes.
The prior assessment already checked the local duplicates and L068's
full proof; no repeat scan or sibling notebook read was necessary.
L375's audited finite-family result is a contrast, not an input.
The earlier pointwise stop does not ban this fixed-function audit.
L068 is a technique comparison with a different zero set and objective;
it and L375 are not direct mathematical premises of L376. Their proofs
are not being re-audited here. Preserve the recorded geometry-only
stop while its stronger fixed-function evidence remains pending audit.

Supporting Mathlib coverage was found for bounded subsequences. The
[Mathlib theorem index](https://github.com/leanprover-community/mathlib4/blob/master/docs/100.yaml),
entry 36, inspected 2026-10-07, points to an external Brouwer
formalization without listing a Mathlib declaration; that external proof
was not inspected. This is not a repository-wide absence claim.
Full matching L376 coverage remains unchecked. No formal verification
or mathematical verdict follows from the index or supporting theorem.

## Relevance, acceptance test and licensed continuation

The main gap remains global actual-theta mixed positivity and L367's
total signed margin. Actual eventual disjointness, D≤0 and the signed
arithmetic count comparison are independent unresolved requirements.
The intermediate target is the exact TARGET above: a reliable audit of
one fixed admissible P, with exact common zeros tending to infinity.
Its downstream use is determining whether geometry-only eventual
disjointness is validly obstructed, so an actual-family argument must
identify additional structure. An order-zero comparison does not meet
the actual family's count asymptotic or establish any physical sign.

The next turn may critically check L376's four proof parts: the phase
branch and complete divisor; every uniform constant for all n and box
choices, including finite truncations; finite-map continuity and
self-mapping; a diagonal subsequence with indices tending to infinity;
the uniform phase tail before tangent and the exact equations pass to
the limit; compact product convergence and nonvanishing off its roots;
distinct roots, simple residual products, growth and nonzero shifted
values. This is an audit checklist, not verification of those claims.
The essential canonical input is L376 plus the named standard inputs
above. No actual-theta, kernel, count, D≤0 or response-sign premise is
assumed, and no cross-notebook input is used.

Continue retaining the obstruction only if every load-bearing claim
passes for the same limiting sequence and the same function P. If an
estimate, self-map hypothesis or limiting identity fails, repair only
when a complete justification is available; otherwise leave the affected
claim unverified and preserve the failure. Finite-stage solvability,
small residuals, or different functions for different heights do not
pass. The audited conclusion, even if valid, supplies no actual-theta
common zero, Laguerre sign, zero-exclusion range or RH counterexample.

This literature-only approval derives no result and changes no lemma or
mathematical script. It permits the separate mathematical audit next
turn, classified under the reused EXPLORE scope; it is not that audit's
verdict or a new discovery beyond the sources checked.
