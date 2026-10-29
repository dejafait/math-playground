# Saved span 3 — bounded earlier-prefix scalar test

TARGET: Test whether every exact-rank-one plane in the complete saved span-3 kernel for actual prefix (0,51,98) has recovered scalar lambda_0=0 over every extension of F_97, using L109's original row 0 and no new block-rank tests.
CHECKED: 2026-10-29
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step 547's exact-prefix and coordinate-kernel comparison in drafts/literature/2026-10-29-span-3-prefix-full-weight-review.md; its selected local proofs/failures and two external queries supplied no inspected exact-prefix disposition, without any novelty inference.
SOURCE_EVIDENCE: L109 equations (3)–(6), reconstruction and separate audit; reused L115 method comparison and step-547 shortening coverage; direct primary sources Hall Theorem 5.1.1 https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf, Conrad Theorems 4.2/7.1/7.5 https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf, and Stacks https://stacks.math.columbia.edu/tag/089T https://stacks.math.columbia.edu/tag/07ZA https://stacks.math.columbia.edu/tag/07ZC; retrieval details below.
COMPARISON: Known homogeneous recovery tools cover this bounded applicability test, but no inspected source proves the numerical scalar predicate; L172's five-row exclusion does not imply an exclusion of this prefix, and L110/L113/L115's specified families differ.
GAP: Bind the complete selected saved basis and root-to-node-3 transitions, then prove universal row-0 scalar vanishing or exhibit an exact plane satisfying all three rank-one gates with nonzero lambda_0; neither alternative is established in this literature turn.
REASON: Step 548 repairs the missing direct-source-URL defect and confirms unchanged SPECIALIZE scope using accessible primary sources and prior inspected coverage; mathematical invocation is deferred to the next turn.
SCOPE: Actual prefix (0,51,98), node 3, saved span 3, original S/J/label order and row 0, arbitrary extension E/F_97, with reused saved completeness. No other prefix, row sweep, rank traversal, cover mutation or pruning.

## Direct-source repair — step 548

2026-10-29. This is a literature-only process repair, honestly STALLED:
the comparison and target are unchanged, and no numerical predicate is
proved. Reuse step 547's duplicate/failure searches and saved-input
inspection; do not repeat a rank traversal or infer originality.

Reopened Hall's [GRS chapter, Theorem 5.1.1, printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf).
Its hypotheses require distinct evaluation labels, nonzero multipliers
and 0<=k<=n; the distance conclusion requires k!=0. This matches L109's
inherited sixteen-label, dimension-eight setup; it does not establish a
scalar condition on a particular prefix.

Reopened Conrad's [Exterior Powers, Theorems 4.2, 7.1 and 7.5,
printed pp. 11–12 and 23–25](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf).
Read the exterior-basis statement and proof passage, the explicit
all-fields qualification for 7.1 and the statement/proof of 7.5.
The tools concern exterior coordinates, independence and equality of
spanned subspaces. They apply over extension fields of F_97; no
characteristic-zero restriction is imported. They give no numerical
vanishing theorem for this kernel.

Reopened [Stacks Lemma 27.22.1, Tag 089T](https://stacks.math.columbia.edu/tag/089T),
including its quotient-chart construction; G(2,7) uses rank-five
quotients and dimension-two kernels. Reopened [Lemma 15.8.4(3),
Tag 07ZA](https://stacks.math.columbia.edu/tag/07ZA), including its
presentation/base-change proof, and [Lemma 15.8.7, Tag 07ZC](https://stacks.math.columbia.edu/tag/07ZC),
including its residue-field dimension criterion and proof. These are
supporting chart/minor tools, not an exact-prefix conclusion. Retrieved
the live pages on this date; no source change requiring reassessment was
identified against the recorded statements.

The [Marquez-Corbella–Pellikaan accepted manuscript, 2016-02-29,
section 5, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf)
failed to reopen through the web tool (internal/access error). This is
not a new inspection of that manuscript. Reuse the prior inspected
Definitions 5.1–5.2, Lemma 5.3 and shortening formula explicitly recorded
in step 547 and L109's separate audit; the shortening hypotheses have
not changed. The failed repeat fetch creates no essential missing
coverage. No alternate unread result is substituted.

Reread L109's necessary reconstruction/gates and separate-audit passages:
rank one, nonzero scalar, overlap weights and prescribed finite chart
remain distinct requirements. Its converse needs r>=6 and is unavailable
here. The exact target, all-extension requirement and stopping test below
remain unchanged. No lemma, script, argument overview, DAG or cover is
modified. Full matching Mathlib coverage remains not checked.

## Required-input scope (unchanged)

The main gap is uniform twelve-row exclusion for an unspecified pair.
An earlier-prefix full-weight obstruction could inform later gate-aware
cover work. It would not itself prove uniformity, representation,
challenge equivalence or an improved radius.

Use L109's necessary direction, its original Q/N maps, nonzero
decomposable wedge, unique exact-rank-one recovery line and equations
(3)–(6). L115 is a method precedent only. L172 is an audited comparison
and actual-chain source, not a premise asserting a shorter exclusion.
L170 and L159–L161 are not premises. No new general coding or exterior
theorem needs reproof.

Use complete selected records in `scripts/pair-free-envelope/cover.json`
and `verification.json`, with the three already checked root-to-node-3
transitions copied at `/saved_actual_history_chain/4`, `/3`, `/2` of
`scripts/span-274-full-weight/certificate.json`. Step 547 inspected the
complete six-vector saved basis and the original-minor evidence in
`verification.json` at `/spans/3`. Reuse the saved completeness explicitly;
do not claim that hashes or this source inspection reaudited elimination.
Bind the original row-0 map to the same label convention. All relevant
original coefficients must be inspected and independently checked if
used in a new coefficient argument.

For coding necessity retain L010/L104/L086/L109's inherited qualifications,
F=F_(97^20), order-sixteen H, k=8, unit multipliers,
1/4<=delta<5/16, both syndromes in U_S, sixteen original finite events,
t=0, nonzero actual D and every locator, arbitrary weights and original
possibly nonrational chart, distinct linear two-overlap supports and
degree at most four. S=(1,8,12,18,22,27,33) and
J=(47,50,64,70,75,79,85,89,96). L109's r>=6 converse cannot be applied
to three rows. No coding realization is inferred from a scalar survivor.

## One bounded test and stopping rule

Attempt one complete homogeneous reduction using the saved kernel and
original row-0 gate. Do not assume decomposability, a common factor or
universal vanishing from the appearance of the saved basis. Prove every
structural implication used, covering all nonzero extension-valued
tensors and their planes. A chart argument must retain every nonzero
Plucker pivot and all rank-one branches; zero coefficients and endpoints
cannot be discarded. Rank-zero restrictions are rejected by actual
nonpersistence and never used as recovery directions.

At exact rank one use any nonzero h in L intersect ker(Q_0) and
lambda_0=h_z0/g_0(z0). Keep both overlap-weight and original finite-chart
gates separate. A universal intrinsic zero may establish the intended
conditional exclusion before those extra gates. An exact nonzero
decomposable wedge meeting all three actual-history rank-one tests and
lambda_0!=0 rejects this scalar mechanism; it need not realize full
weights or a coding event. Finite-field samples cannot prove universal
vanishing. Incomplete branches or an unsuccessful reduction are
inconclusive: preserve partial reasoning and stop without solver or
rank sweeps. Do not change the target within the attempt.

Save reasoning before lengthy work. Independently check load-bearing
new identities and input bindings; any later scripts save full
certificates and print actual/required bounds, failures and paths.
No new N-block, stack or child-rank test, traversal, cap increase,
pruning or cover mutation is permitted. All 1665 obligations remain.
Full matching Mathlib coverage is not checked. Route as
calculation/standard/high, REPRODUCTION; this routine specialization is
not creative discovery.
