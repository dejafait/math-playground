# Completed coverage — common-connection normal-jet critical audit

TARGET: Critically audit L127's common-connection normal-jet vanishing and the resulting four-branch lengths 10 and 9.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the preceding normal-jet discovery and inspected primary coverage; compared full L127, L118 conclusions (3)--(4), L126 definitions (1)--(4), its completed audit coverage and history/379--381, and ATTEMPTS/070--072. No duplicate completed L127 audit was found in those scoped records; no fresh external search was needed.
SOURCE_EVIDENCE: Reused Higashijima--Itou--Nitta, hep-th/0203081v3, Section 3.1 equations (3.1)--(3.3), (3.7), Appendix A; Jentsch--Weingart (2020), Theorem 4.6 proof and Corollary 4.9 pp. 389--392; Derksen--Sidman (2002), Theorems 1.2/2.1 and Section 2 proof; Li, Yanqi Lake Lectures Part 3 (2026-07-05), Lemma 5.2.3 p. 53; Stacks 00MA, 07N9, 00MC, 0C0S and 02M1 as inspected in the reused assessments below.
COMPARISON: Known coordinate and completion tools cover the audit's prerequisites; they do not certify L127's common-connection Hessian specialization or its annihilator-quotient comparison. The stronger published submanifold-coordinate statement is optional, with its smooth-versus-analytic qualification retained.
GAP: Independently audit L127's common ambient connection, complexification, source terms, Hessian factor, annihilator quotient and analytic-to-formal comparison; import the separately audited L126 formula without treating source coverage as correctness verification.
REASON: Essential coverage is ready for this exact bounded proof audit, with no source blocker; the present literature-only step derives no result and gives no correctness verdict on L127.
SCOPE: Audit L127 under its unchanged conditional L118/L126 hypotheses; no F existence, collision occurrence, higher-jet linearization or global defect theorem is included.
COVERED_TARGET: Critically audit L127's common-connection normal-jet vanishing and the resulting four-branch lengths 10 and 9.
LITERATURE_REASON: The startup gate requires separate comparison for this new critical-audit target; existing inspected source coverage suffices and is reused without another discovery search.

## Approved bounded review

Reuse the preceding [normal-jet assessment](2026-10-18-four-branch-geodesic-normal-jets.md)
and the inspected theorem statements it records. The exact target above
is a critical verification of a known-tool specialization, not a fresh
normal-coordinate theorem or a request to reopen ATTEMPTS/070--072.
Do not repeat external searches without an essential missing hypothesis
or a specific new relevant lead. Coverage is now ready for a separate
mathematical proof-audit invocation; this note does not perform that audit.

Essential inputs are L118 and L126. Retain locally free rank-two
Omega-polystable F, integral c_1=0 and ch_2=-14e_1-21e_2-tau_D on the
identical marked K3 factors, the common ambient connection and scale
2lambda, exactly four preimages, quaternionic tangent span two and
ambient quaternionic dimension 39. F and collision occurrence remain
unproved. The source fourfold is smooth projective; integral Hodge
counterexamples are outside the rational main target.

The audit should check the full tensor identity before discarding
source terms, the common ambient quadratic polynomial for every ell,
the coordinate-independent rank, and the exact algebraic length descent
imported from L126. A surviving connection term or an invalid formal
comparison requires a precise repair or withdrawal of the claimed
specialization. A clean audit confirms this conditional local input only.
Full matching Mathlib coverage remains not checked.

## Reused primary coverage and applicability boundaries

The primary-source reading record in the preceding normal-jet assessment
is reused, not claimed as new online reading. Higashijima--Itou--Nitta,
[*Normal Coordinates in Kähler Manifolds and the Background Field Method*,
v3, 17 June 2002](https://arxiv.org/pdf/hep-th/0203081v3#page=7),
Section 3.1, equations (3.1)--(3.3), (3.7), PDF pp. 7--9 and Appendix A,
supplies the finite-order holomorphic coordinate and Kähler connection
tools. The audit must distinguish the smooth connection coefficients
from holomorphic branch maps; no infinite normal-coordinate convergence
or real-analytic metric premise is needed or approved.

Jentsch--Weingart, [*Riemannian and Kählerian normal coordinates*,
Asian J. Math. 24 (2020), 369--416](https://archive.intlpress.com/site/pub/files/_fulltext/journals/ajm/2020/0024/0003/AJM-2020-0024-0003-a001.pdf),
Corollary 4.9, pp. 391--392, states compatibility with totally geodesic
complex submanifolds. Its proof is left to the reader; the earlier
assessment inspected the supporting Theorem 4.6 construction,
pp. 389--391. This stronger lead is not essential to L127's direct
second-order identity. Retain the recorded warning about the overbroad
real-analyticity assertion on p. 372; do not use it to upgrade smooth
metric germs to convergent all-orders normal coordinates.

The [completed L126 audit coverage](2026-10-18-four-branch-finite-jet-critical-audit.md)
and [actual-three-branch completion assessment](2026-10-18-actual-three-branch-normalization-length.md)
record the remaining precise tools and their proof cases. Derksen--Sidman,
*Adv. Math.* 172 (2002), Theorems 1.2 and 2.1, pp. 153--154,
with Section 2 proof through p. 156, gives the arrangement regularity
bound without genericity. Li, *Yanqi Lake Lectures on Algebra*, Part 3,
version 2026-07-05, Lemma 5.2.3, printed p. 53, supplies complete
filtered lifting, subject to completeness, separatedness and graded
surjectivity. These support L126's entire cubic tail rather than a
truncated numerical preview. Their precise links and full hypotheses
are retained in that completed coverage; no reproof is proposed.

[Stacks 0C0S](https://stacks.math.columbia.edu/tag/0C0S),
Lemma 10.160.10(2), applies to complete regular local rings over their
residue coefficient field. [00MA](https://stacks.math.columbia.edu/tag/00MA)
and [07N9](https://stacks.math.columbia.edu/tag/07N9), Lemmas 10.97.1
and 10.97.8, supply exact finite-module completion and the finite-algebra
product decomposition over a Noetherian base.
[00MC](https://stacks.math.columbia.edu/tag/00MC) and
[02M1](https://stacks.math.columbia.edu/tag/02M1), Lemmas 10.97.3
and 10.52.13, supply faithful flatness and flat-local length comparison.
They do not alone identify arbitrary analytic coordinates with the
algebraic restriction map: the audit must check L127's Taylor-series
change from algebraic regular parameters and its invertible linear part,
compatibility with the same four branch maps, and L126's coordinate
invariance. This is the finite-order specialization obligation, not a
source gap requiring a theorem on arbitrary analytic normalization.

## Duplicate/failure comparison and outcome

L127 and history/381 contain the completed specialization and the request
for its independent audit. History/379 preserves L126's separate audit;
history/380 supplies the ready normal-coordinate source comparison.
None substitutes for the new L127 audit. ATTEMPTS/070 concerns the failed
minimal-defect inference from selected pairwise data; ATTEMPTS/071 and
072 concern curvature and first-curvature-derivative restrictions.
Their stopped mechanisms remain intact. L126's arbitrary smooth complex
models retain quaternionic tangents but omit common geodesy, so they are
comparison cases rather than counterexamples meeting L127's hypotheses.

This is LITERATURE / REPRODUCTION / EXPLORATION: completion of coverage,
not a new mathematical input or independent verification of the claimed
lengths. The test for the next turn remains exactly the saved target:
confirm every load-bearing identity and comparison, or identify a precise
repair or withdrawal. A clean audit only confirms conditional local
lengths; F, collisions, global defect consequences, transverse transport
and universal primitive Hodge realization remain unresolved. No lemma,
mathematical script, DAG or argument-overview change is made this turn.
