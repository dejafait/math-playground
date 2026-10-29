# Forty-support compatibility — completed source-scope review

TARGET: Determine whether eight labels from L163's forty-label set can join L162's four fixed supports with all pairwise intersections at most one and every coordinate of S union J having degree at most four.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched exact L163/forty-support terminology, Bron–Kerbosch enumeration, degree-constrained clique enumeration, and binary set-packing methods; inspected Eppstein–Loffler–Strash arXiv:1006.5440v1 sections 2.2–3 and SCIP 8.0.4 constraint-handler definitions; checked the local twelve-row reviews and ATTEMPTS/049–052 where relevant.
SOURCE_EVIDENCE: Eppstein–Loffler–Strash, arXiv:1006.5440v1 (2010), section 2.2/Figure 2 pp. 4–5 and Theorem 1/Figure 4 p. 6, provide complete maximal-clique enumeration; SCIP 8.0.4 documents binary packing, knapsack and general linear constraints. L109/L162/L163 supply the exact finite instance, not its feasibility decision.
COMPARISON: Known exhaustive methods cover finite selection and capacity constraints; none of the inspected sources decides this indexed instance. L163's individual-row tests and the earlier gated twelve-row specification do not check mutual selection from B. Ordinary disjoint set packing is stronger than the requested intersection-at-most-one predicate and must not replace it.
GAP: Reconstruct all forty original supports and four fixed supports, justify the exact selection test, and produce a directly checked witness or complete replayable impossibility evidence; no such computation or new combinatorial result is supplied by this review.
REASON: Essential method coverage is now adequate for one REPRODUCTION calculation on the unchanged finite target. Specialization is needed because the sources do not evaluate these labels, include their fixed-row degree contributions, or certify a local implementation.
LITERATURE_REASON: The incoming REVIEW_REQUIRED assessment names a new finite support-selection target outside the preceding additional-row audit; this turn supplies its missing method comparison without repeating that audit.
SCOPE: Exactly the saved TARGET, L109's original labeling, L162's fixed S/J and four supports, and L163's forty labels; exact integer incidence and degree tests only, with inherited rank-one information at [1:94]. No other plane family, coding gate, symmetry reduction or global twelve-row claim is approved.

## Proposed bounded target and use

Use exactly L162's S, J, labels (35,522,477,566), L109's original
Cartesian labeling, and L163's forty-label set B. Seek eight distinct
additional labels; include the four fixed supports in every intersection
and degree check. No quotient by symmetry, subset sampling or presumed
coding admissibility is allowed. The only permitted family parameter
for additional rank-one rows is [1:94], by audited L163.

The main gap is uniform twelve-row exclusion. This proposed finite
test could decide whether this fixed family survives the stated
necessary support constraints at twelve rows. A positive result is only
a support/rank candidate and must retain all coding and weight gates;
a negative result would concern this family alone. Continue with an
explicit twelve-support witness or a complete independently checkable
impossibility certificate; incomplete search does not decide the target.

The completed approval checks relevant known results and local overlaps;
the later calculation must justify its chosen complete enumeration.
ATTEMPTS/052's unconditional four-row-finiteness obstruction remains
valid; this target imposes additional constraints and does not reopen it.
This source review derives no new compatibility fact; it approves only
the bounded finite specialization described below.

Unresolved independent issues include other plane families, second-pair
extraction, q=97^20 and k=8 coding realization, the pinned cell, t=0,
U_S, nonzero D/locators, sixteen events, weights/chart, L056/L069/L040
and L051/L055 gates, L104/L151 qualifications, arbitrary representation,
challenge identification and sharp radius. No cross-notebook input is
proposed. Full matching Mathlib coverage is not checked.

## Inspected primary sources and their limits

Eppstein, Loffler and Strash, *Listing All Maximal Cliques in Sparse
Graphs in Near-optimal Time*, arXiv:1006.5440v1, 28 June 2010,
[PDF](https://arxiv.org/pdf/1006.5440), section 2.2 pp. 4–5,
Figure 2, and section 3 pp. 5–6, Figure 4 and Theorem 1:
the setting is a finite undirected graph with adjacency-list input.
The recursive state separates included, candidate and excluded vertices;
the empty-candidate/empty-excluded case reports a maximal clique.
The pivot argument uses maximality. Theorem 1's proof assigns each
maximal clique to its earliest vertex, excluding duplicate reports.
These are complete graph-enumeration tools, not degree-capacity tests.
No sparsity or running-time benefit is assumed for the present instance.
The PDF calls the correctness result Theorem 1; the generated HTML
renumbers it 3.1. Its prose reverses one move between R and P;
Figure 2's explicit recursive call adds v to R, and is the reference
for that operation. No reproof of the general algorithm is needed.

SCIP, version 8.0.4, official
[Constraint Handlers](https://www.scipopt.org/doc-8.0.4/html/group__CONSHDLRS.php),
inspected sections "Knapsack Constraints", "Linear Constraints" and
"Set Packing/Partitioning/Covering Constraints": binary nonnegative
integer knapsack inequalities, rational two-sided linear constraints,
and binary at-most-one constraints are supported. These definitions
cover capacity and conflict formulations. They provide neither a
proof-producing guarantee for a solver run nor this instance's answer.
No solver dependency is required or installed by this review.

Bron and Kerbosch, CACM 16(9) (1973), 575–577, Algorithm 457,
[DOI](https://doi.org/10.1145/362342.362367), is the original lead.
Its publisher metadata was inspected, but the full PDF was inaccessible
(ACM 403; UCI mirror 502/timeout). Indexed extracts are not treated as
full inspection. The accessible primary Eppstein–Loffler–Strash paper
supplies the needed algorithm statements and correctness cases, so
that access failure does not block this target. Tomita et al. (2006)
is a reference within that paper, not separately inspected or needed
for a new complexity claim. No search establishes novelty.

Queries included `Bron Kerbosch Algorithm 457 finding all cliques
undirected graph 1973`, `set packing conflict graph integer programming
constraints clique enumeration`, `"L163" "forty" "supports" Reed Solomon`,
`"degree constrained" "clique" enumeration subset`, and
`site.scipopt.org doc linear constraints binary variables set packing`.

## Local overlap and failure comparison

Read L109's hypotheses, quotient-map formula, conclusion and initial
reduction; L162's hypotheses and conclusion; and L163's hypotheses,
complete forty-label statement and qualification. Their audited proofs
are reused, not re-audited. Read the relevant bounded-test obligations
in `drafts/literature/2026-10-25-twelve-row-certificate-specification-review.md`
and compared the gated-feasibility review: the earlier task retained
field, weight and chart gates and counted a formula without solving it.
It is not a duplicate finite compatibility calculation.

ATTEMPTS/049 stops recycling passed input audits or a large formula
without an actionable solving test. ATTEMPTS/050 excludes three other
sample infinite-family constructions, not this B. ATTEMPTS/052 preserves
L162's counterexample to unconditional four-row finiteness. The proposed
additional-row incidence test changes the hypotheses and does not
reopen that false claim. No new broad rank census is authorized.

## Approved later calculation and evidence contract

Use every original label in B and reconstruct its I/K support by the
stated Cartesian lexicographic convention; include all four fixed rows
in intersection and coordinate-degree checks. Establish the selection
predicate's exact match to the saved target before using pruning.
Integer counts must stay integer counts, not equations modulo 97.
An exact binary conflict/capacity encoding or an ordered exhaustive
subset search is within scope. A transparent complete search and a
separate direct checker are preferred over an unexplained solver flag.

If using a graph, define adjacency by the requested support predicate,
not disjointness. The cited maximal-clique theorem alone does not
approve checking only whole maximal cliques against degree bounds.
Require coverage of all relevant eight-element subsets, or a separately
justified capacity-aware enumeration. Likewise, do not transplant a
maximality-based pivot rule into a constrained search without proving
its coverage. These are explicit later verification obligations, not
instance-specific lemmas established in this literature turn.

A positive certificate must print the eight distinct additional labels,
their reconstructed supports and all twelve supports' pairwise
intersections and degrees, with actual versus required bounds. A
negative certificate must expose the full finite universe and exact
branch/pruning rules, with a completeness argument and independent
replay or a short checkable combinatorial obstruction. An interrupted
search, sampled branches, an LP relaxation or a solver status alone
does not prove impossibility. Save full evidence under the notebook's
scripts/seven-coordinate/ and report concise summaries and paths.

Continue with the finite decision only on that evidence standard;
if a branch cannot be certified, preserve the failure and report the
decision unresolved. A witness licenses only later review of missing
coding gates. Impossibility would stop twelve-row use of this particular
family under these necessary conditions; it would not exclude other
families or settle the challenge. This is routine reproduction and
specialization, not a justified creative mechanism. Creative discovery
remains deferred until the finite test gives evidence for selecting a
new central mechanism; no invented creative label is warranted here.
