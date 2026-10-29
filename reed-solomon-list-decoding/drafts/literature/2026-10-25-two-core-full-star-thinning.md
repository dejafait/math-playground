# Two-core thinning with a preserved full star — source and scope assessment

TARGET: Assess whether two subfamilies of L030's polynomial families can each retain at least 1532496 blocks, preserve the same full common star at the left column 16, and satisfy the distinct-support intersection bound 63.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: On 2026-10-25 searched exact full-star thinning terminology, Reed–Solomon cross-intersecting families, polynomial agreement/cross diameter, bipartite cross-independent sets and matching/vertex-cover bounds; inspected the primary statements listed below. Targeted local checks found no existing retention theorem in L030, L125, ATTEMPTS/104 or the two-core working record.
SOURCE_EVIDENCE: König (1931), authorized translation arXiv:2009.03780v1 https://arxiv.org/pdf/2009.03780v1, unnumbered main theorem p. 3 and complete graph proof pp. 1–2; Wang–Zhang arXiv:1101.2257v1 https://arxiv.org/pdf/1101.2257v1, definitions pp. 3–4 and Theorem 1.1 p. 5; Borg–Feghali arXiv:2012.15356v2 https://arxiv.org/pdf/2012.15356v2, Theorem 1 p. 3. L125's audited common-star rigidity and formula (8) are available local inputs.
COMPARISON: Matching/vertex-cover theory covers arbitrary finite bipartite conflict graphs but does not identify the conflict graph or certify this balanced threshold; part-transitive and cross-intersecting theorems require additional unverified or different hypotheses. L125 supplies rigidity and a conflict formula for full stars, but no deletion bound. Specialize only that remaining counting step, importing the standard matching theorem if needed.
GAP: Verify whether L125's forced conflict correspondence remains bijective on nonstar blocks after both full stars are retained, and whether its resulting deletion constraint rules out 1532496 retained blocks on each side; no retention inequality is established in this review.
REASON: Essential discovery and theorem-level comparison for the changed deletion question are now completed. The finite structural difference is independently testable using audited inputs; neither the full-law Hall event nor an unverified symmetry theorem answers it.
SCOPE: Exactly TARGET and the scope below; one bounded deterministic proof attempt through preserved-star rigidity and conflict matching/counting. No incomplete stars, altered marginals, other distinguished columns on the left, global compatibility, or RS realization are approved.

## Exact proposed scope and downstream use

Use H,K,a,b,C,C',T,Omega and the two arbitrary bijections from L125.
The left distinguished point b is represented in column 16, at some
symbol y_0. Choose subfamilies of the two full families. Retain every
left block containing b; require that the right common-support star is
identical and contains every block of its ambient right family containing
a. Thus both retain the same complete 18769-element common star. The
right distinguished coordinate is not assumed to equal 16 at the outset.
All other blocks may be deleted independently. Require equality of
common-support indicators and intersection at most 63 for distinct
supports in the union, identifying equal supports as in L125. Test
whether both retained families can have at least 1532496 members.

Essential inputs are L030 and the audited L125 star-rigidity proof and
certificate. No independent sampling, uniform law on subfamilies,
common RS center, or compatibility on more than two cores is assumed.
L051 and ATTEMPTS/033 remain contrasts, not inputs. No cross-notebook
result is needed. The new target has not been calculated or proved in
the audit turn that proposed it.

A retention bound below the threshold would rule out this particular
way to repair the full-law construction. A construction above it would
justify testing its consistency beyond two cores. Either result would
leave incomplete-star thinning, other local laws and the main RS safety
claim unresolved. This restriction is not a proposed universal cap.
This completed source/scope comparison approves only the stated deterministic
threshold test for a later research turn. Do not reopen the failed
complete-law coupling or treat this approval as a retention result.


## Inspected primary statements and applicability

**Matching.** Dénes König, *Graphok és matrixok*, Matematikai és Fizikai
Lapok 38 (1931), authorized English translation by Gábor Szárnyas,
*Graphs and matrices*, arXiv:2009.03780v1 (5 September 2020),
[main theorem, PDF p. 3](https://arxiv.org/pdf/2009.03780v1).
For a finite bipartite graph, maximum matching size equals minimum
vertex-cover size. Read the graph definitions and the entire graph proof
on pp. 1–2: absence of an augmenting alternating path, choice of one
endpoint per matched edge, all four coverage cases, and the reverse
inequality. No regularity, connectedness or positive vertex-degree
hypothesis is required. This theorem is available for a conflict graph
whose vertices are tagged left/right blocks and whose edges represent
forbidden pairs. It does not prescribe the number deleted from each
part or force undeletable star vertices to survive. The next proof must
handle those restrictions explicitly; a total vertex-cover optimum alone
is not a certificate for a balanced retention problem. A directly exhibited
matching would need only the elementary disjoint-edge counting argument,
not a reproof of König's theorem. No instance matching is asserted here.

**Symmetric bipartite bounds.** Jun Wang and Huajun Zhang,
*Nontrivial independent sets of bipartite graphs and cross-intersecting
families*, arXiv:1101.2257v1 (12 January 2011),
[Theorem 1.1, printed p. 5](https://arxiv.org/pdf/1101.2257v1).
For a non-complete bipartite graph with |X|<=|Y|, a part-transitive
action and every fragment in both parts primitive under that action,
the largest nontrivial independent set has size |Y|-d(X)+1.
Inspected definitions of part-transitivity, fragments and primitivity
on printed pp. 3–4 and the complete theorem statement, including its
equality qualifications. These action and fragment assumptions have not
been verified for the retained-star conflict graph with arbitrary
ambient labelings. Thus no instance bound is imported, nor is their
proof needed. The distinction is material: two arbitrary relabelings
are not automatically a common group action preserving conflicts.

**Ordinary cross-intersection.** Peter Borg and Carl Feghali,
*The maximum sum of sizes of cross-intersecting families of subsets of
a set*, arXiv:2012.15356v2 (22 January 2021),
[Theorem 1, printed p. 3](https://arxiv.org/pdf/2012.15356v2).
For n>=1, 1<=r<=s and nonempty cross-intersecting families
A subset binom([n],<=r), B subset binom([n],<=s), it bounds their
sum by 1+sum_{i=1}^s (binom(n,i)-binom(n-r,i)).
Inspected the complete statement, including its equality example.
The local condition bounds intersections above for distinct supports;
this theorem bounds them below for every cross pair. No conversion
preserving the needed polynomial-family sizes and threshold is supplied
by that statement. It therefore does not solve this target, and no
compression or extremal classification is imported.

**Evaluation-code scope and unread leads.** L030 fixes the quadratic
evaluation family and its within-family packing property. L125 already
proves the stronger needed arbitrary-symbol star rigidity over the prime
field, with its accepted 840-map certificate; use this local input rather
than assuming a linear-code automorphism classification. Dür, *The
automorphism groups of Reed-Solomon codes*, JCTA 44 (1987), 69–82,
DOI 10.1016/0097-3165(87)90060-4, appeared as a relevant lead but its
publisher endpoint returned 403. The IACR 2014/353 PDF endpoint also
returned 403. Neither full theorem was inspected or used. These are
optional leads, not essential blockers: no result from either is needed
for the already audited rigidity input. A general list-decoding search
hit (ECCC TR26-169) was not inspected and supplies no input to this
finite deletion question. This review makes no broader challenge claim.

## Search and duplicate record

Queries included `cross intersecting families Reed Solomon codes polynomial
agreement cross diameter`, `cross intersecting families maximum sum sizes
bipartite graph independent sets matching theorem`, `Reed Solomon code
cross intersecting families prescribed star quadratic polynomials`,
`"two" "full star" "thinning" polynomial families`,
`"Reed Solomon" "cross-intersecting"`, and
`"Reed-Solomon" "isometries" arbitrary symbol permutations automorphism`.
The bounded search found tools and scope mismatches, not an exact theorem
for the numerical retained-star problem. This is not evidence of novelty.

Local reads covered L030's construction and packing proof, L125's
hypotheses, common-star rigidity and forced-conflict formula, ATTEMPTS/104,
and the finite Strassen note in foundations/16. Specific searches of the
two-core working record and prior audit assessment found no retention
bound. L125 and ATTEMPTS/104 concern full laws; Strassen concerns prescribed
probability marginals, absent here. L030's local-cap counterexample remains
valid and must not be replaced by a supposed universal thinning cap.
No polynomial enumeration, certificate replay, new derivation, lemma or
mathematical script was performed in this literature turn.

## Approved bounded test and stopping condition

Use the full common star to invoke the audited rigidity input. Check
formula (8) on all nonstar polynomial indices symbolically, including
injectivity, surjectivity and the distinguished-value condition; verify
that it still identifies forbidden pairs for arbitrary allowed labels.
Only then compare the resulting retention constraint with 1532496 on
both sides. This is a proposed proof test, not a completed calculation.
If the constraint excludes that threshold, stop with a restricted
obstruction and preserve the independent gaps. If it does not, abandon
this matching argument as sufficient evidence for the threshold; do not
infer feasibility from necessary constraints or expand into unreviewed
incomplete-star optimization in the same turn. Other collision edges
can strengthen an upper bound but are not assumed exhausted.

Mathlib: matching, vertex-cover and full instance coverage not checked;
unknown availability is not evidence of absence. Canonical theorem use
and any instance proof belong in a later lemma, not this assessment.
