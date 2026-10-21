# Source comparison: arbitrary-label alternating rank

TARGET: Determine whether the alternating-coordinate necessary-condition matrix for L025's cyclic 0125 family has rank 28 over F_97 for every bijective labeling of its sixteen vertices by H, the order-sixteen subgroup of F_97^*.
CHECKED: 2026-10-05
DECISION: EXPLORE
SEARCH_EVIDENCE: October 5 exact cyclic-pattern, arbitrary-evaluation, exterior/compound-matrix and higher-order-MDS searches found no inspected theorem deciding this universal fixed-H rank; queries, rejected leads and reused coverage are recorded below.
SOURCE_EVIDENCE: Read Brakensiek–Dhar–Gopi arXiv:2310.12888v3, Definitions 1.2–1.3 and 6.1, Theorem 4.1 with base cases and the displayed induction through Case 2, and Theorem 6.4 with its power-series reduction; reused the prior Lovett/BGM/Hall/transversal comparisons and checked L010, L025 and L026's relevant proofs.
COMPARISON: The broader polynomial-code theorem retains generic evaluations and column-span intersections; it supplies no uniform rank certificate for fixed H. L026's eight generator cases are ready test controls, but its cyclic coefficient separation does not cover all bijections.
GAP: Full rank under every bijection, or one exact deficient labeling, remains unproved and untested beyond L026's cyclic cases; sampling cannot establish the universal statement.
REASON: Essential source coverage is adequate for one bounded exact rank test on the unchanged target; no inspected theorem supplies its answer, and no novelty is inferred from the search.
SCOPE: Only L025's sixteen cyclic 0125 abstract edges labeled bijectively by fixed H, with L026's 96-by-28 necessary-condition matrix; permits a bounded falsification search and applicability checks, not arbitrary support families or a claim from genericity or sampling.

## Scope, gap and downstream use

This completes the separate source approval requested by the prior
checkpoint. It establishes no rank, exclusion or realization result.
Essential local inputs are L010's moment map, L025's abstract supports,
and L026's necessary alternating equations and audited cyclic cases.
No cross-notebook input is proposed. The main pinned-model gap remains
whether an L010 equality pencil attains sixteen, against allowable
fifteen; the current interval is 11/q–16/q. Other support families and
the challenge-level ABF26 correspondence remain independent gaps.

For specificity, a labeling is a bijection lambda: Z/16Z -> H. Its
support at t is {lambda(t), lambda(t+1), lambda(t+2), lambda(t+5)}.
For each support, take a basis of the annihilator of its four moment
columns and stack the six pairwise alternating row constraints, with
the same 28 coordinates p_jk as in L026. The proposed target concerns
the rank of this 96-by-28 matrix, independent of basis choices; the
applicability and any symmetry reduction require justification in the
future approved attempt. No claim about arbitrary-label rank is made
by simply defining the test.

Downstream use: a universal rank-28 result, together with the preserved
disjoint pair and L010's column independence, could extend this family's
exclusion to all labelings over F_(97^20). A single rigorously certified
rank-deficient labeling would instead stop that uniform linear criterion
and identify an independently testable exceptional case. Rank deficiency
alone supplies no decomposable alternating vector, full-weight errors,
sixteen distinct finite parameters, or admissible L010 locator pencil.
Any subsequent realization must check all those gates over the full
extension, not just sample prime-field weights. Other support families,
the global fifteen bound and ABF26 correspondence would remain open.

## Literature reuse, duplicates and failures

The [fixed-label assessment](2026-10-05-cyclic-0125-affine-compatibility.md)
is reused for Lovett, *MDS Matrices over Small Fields*, FOCS 2018,
Theorem 1.2, pp. 194–195; Brakensiek–Gopi–Makam,
arXiv:2206.05256v4, Definitions 1.4/1.8, Theorem 1.12 and
Corollary 1.15 with proof; and Hall, *GRS Codes*, §5.1, Theorem 5.1.1,
pp. 63–64. Its inspected theorem statements cover selectable or generic
evaluation points, or RS distance and ordinary Vandermonde independence.
The latter inputs already hold for every distinct labeling through
L010; they do not prove the stacked alternating matrix has rank 28.
No distance theorem is reproved and no generic specialization is imported.

The same assessment records del Campo III.D.1 and Sottile §7.1's
four-subspace graph/eigenline mechanism. Its genericity, direct-sum and
graph-isomorphism requirements are not a universal-label rank certificate.
This comparison remains adequate; no fresh general MCA or ABF26 browsing
was needed. The parked ABF26/Jo sources remain unread, independent leads.

Read L010 through its moment-kernel and eight-column argument, L025's
statement, edge table and disjoint pair, and L026 through equations
(1)–(3) and its separate audit. L026 is a duplicate answer only for
the eight cyclic generator cases. The arbitrary-label matrix construction
is proposed here; its basis independence and any symmetry reduction must
be justified in the future attempt, rather than presumed from the audit.
No saved arbitrary-label search or theorem was located in the targeted
local search. ATTEMPTS/018 preserves the fixed-label exclusion;
ATTEMPTS/017 preserves the failed universal small-union criterion.
Neither is a stop on arbitrary labeling. L009's shifted-weight restriction,
L024's different two-block family, and L022's saved disjoint triple cannot
be silently substituted for the present target.

## Changed-scope search and primary source

Queries issued October 5, 2026:

- `"Reed Solomon" "exterior" "rank" subspaces`
- `"rational normal curve" "Plücker" transversal lines secant spaces`
- `"higher order MDS" "fixed" "evaluation" points`
- `"0,1,2,5" "97" rank cyclic`
- `higher order MDS codes non generic Reed Solomon roots unity counterexample`
- `"Reed-Solomon" "exterior algebra"`
- `"Vandermonde" "exterior" "matroid"`
- `"GM-MDS" "prescribed" "evaluation points"`
- `"Vandermonde" "compound" "rank" subspaces`
- `"Reed-Solomon" "arbitrary evaluation points" "higher order"`
- `"Plucker" "finite fields" "secant" "Schubert"`
- `"cyclic" "0125" "rank"`

The relevant new lead was Brakensiek–Dhar–Gopi,
*Generalized GM-MDS: Polynomial Codes are Higher Order MDS*,
[arXiv:2310.12888v3, June 4, 2025](https://arxiv.org/html/2310.12888v3).
Definition 1.3 requires linearly independent polynomial coordinates;
generic evaluations are algebraically independent. Definition 1.2
concerns common intersections of column spans. Theorem 4.1 treats
monomial matrices with strictly increasing integer exponents at generic
points over an algebraically closed field, for every order at least two.
Read its base cases and induction through Case 2; determinant nonvanishing
is symbolic. Definition 6.1 and Theorem 6.4 retain generic columns on an
irreducible MDS variety. Read the reduction to power series after
Theorem 6.7, conditional on Theorem 6.6. The remaining Case 3 and full
power-series proof were not read or used. This source does not certify
the prescribed finite H, nor identify the target's exterior-coordinate
matrix with its intersection test. No theorem from it is imported.

Search hits on real Schubert calculus, secant embeddings, extensor
algorithms and numerical compound matrices were scope leads, not read
theorems or evidence for fixed-F_97 rank. Secondary notes claiming
roots-of-unity higher-order-MDS defects were not imported as facts.
The failed exact-pattern queries provide no novelty evidence. No essential
unread theorem was identified that blocks this independent rank test.

## Approved bounded attempt and continuation/abandonment test

The unchanged TARGET is approved as EXPLORE for one mathematical turn.
Start from L010, L025 and L026; construct annihilators from the actual
moment columns for each chosen labeling, and justify that different bases
give the same rank question. Do not assume a labeling symmetry without
proving its action on the complete matrix. Reproduce the cyclic cases
only as controls for the new implementation, not as a second research goal.

Use a reproducible, explicitly listed search of at most 4096 bijections,
including cyclic controls, permutations of those labelings, and labelings
chosen to test structured exceptional cases. This is a bound on a
falsification attempt, not an exhaustive decision procedure for all
bijections. Specify the ordering/seed and actual coverage in its certificate.
Use exact F_97 arithmetic. Stop at the first rank below 28 and independently
reconstruct its full 96-by-28 matrix from moment nullspaces, saving the
labeling, all matrix entries, row reduction and nonzero kernel vector.
For full-rank tested cases retain exact maximal-minor evidence and the
complete list of tested labelings. Print actual ranks, required rank 28,
failures and certificate paths; keep the full evidence on disk.

A certified deficient labeling is an informative negative result for
the uniform rank criterion and stops that criterion; it is not a
sixteen-count witness. If no deficiency is found within the bound, record
EXPLORATION and leave the universal quantifier open. Continue only with
a concrete universal certificate mechanism or a new discriminating test;
do not relabel another sample batch as a proof or renew the exploration
budget. Independent full-weight, decomposability, finite distinct-parameter
and actual locator gates remain unresolved for any exceptional labeling.
Any new realization target requires its own coverage assessment.

Mathlib coverage of the exact enlarged target and the new generalized
GM-MDS comparison is **not checked**; supporting Mathlib qualifications
in L010/L026 remain unchanged. This literature turn derived no result,
ran no mathematical enumeration, and modified no lemma or mathematical
script. No proof reimplementation is needed for the cited generic theorems;
the approved exact test addresses their uncovered fixed-evaluation gap.
