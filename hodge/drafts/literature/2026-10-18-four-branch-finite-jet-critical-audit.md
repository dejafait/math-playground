# Completed coverage — critical audit of the four-branch finite-jet formula

TARGET: Critically audit L126's four-branch finite-jet formula, including the complete tail, normal-jet contribution and tangent-rank cases.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the bounded discovery and inspected primary cases in 2026-10-18-actual-four-branch-normalization-jets.md; searched the exact four-branch source/history/working records and read ATTEMPTS/070--072; no new external discovery search was needed for the unchanged tool hypotheses.
SOURCE_EVIDENCE: Reused Derksen--Sidman (2002), Theorems 1.2 and 2.1 and Section 2 proof, pp. 153--156; Li, Yanqi Lake Lectures on Algebra Part 3, version 2026-07-05, Lemma 5.2.3, p. 53; Stacks 00MA, 07N9, 00MC, 0C0S and 02M1, with statement/proof coverage recorded in the two actual-three-branch assessments.
COMPARISON: These sources cover linear-arrangement regularity, complete filtered lifting, exact finite-module and finite-algebra completion, formal coordinates and length descent; they do not certify L126's full nonlinear jet-image elimination or its quaternionic tangent-rank calculation, which are the separate audit's specialization checks.
GAP: Independently verify each application and the complete finite-rank argument in L126; actual geodesic normal jets, collision occurrence, F existence and global defect consequences remain outside this audit.
REASON: Essential tool coverage is ready and reusable for this exact audit; approve a separate mathematical proof audit without repeating discovery or treating this source comparison as correctness verification.
SCOPE: Conditional L118/L120/L121 image with exactly four preimages and quaternionic tangent span two in ambient quaternionic dimension 39; audit L126 as written, including relaxed examples, without evaluating actual normal jets.
COVERED_TARGET: Critically audit L126's four-branch finite-jet formula, including the complete tail, normal-jet contribution and tangent-rank cases.
LITERATURE_REASON: The startup gate requires separate source comparison for the newly saved critical-audit target; this turn approves that scope using existing primary coverage rather than doing the mathematical audit.

## Relevance and bounded decision

The main gap remains universal primitive rational Hodge realization.
The intermediate target is a critical audit of L126's conditional local
normalization formula. A verified local contribution could support later
global coherent-sheaf defect bookkeeping; no global argument is provided.
Continue with this input only if the exact completion, entire tail and
full finite-jet calculation survive. A load-bearing failure requires a
specific repair or qualification of L126 before use. Mere confirmation
is not an ADVANCE, and the audit must not silently extend its scope to
actual geodesic jet evaluation or collision exclusion.

## Reused primary coverage and precise audit obligations

The discovery queries, source versions and relevant proof cases are in
[the four-branch source comparison](2026-10-18-actual-four-branch-normalization-jets.md).
Completion and filtered-map hypotheses are expanded in
[the nonlinear three-branch assessment](2026-10-18-actual-three-branch-normalization-length.md)
and [its audit coverage](2026-10-18-actual-three-branch-length-critical-audit.md).
Those records were read in the relevant ranges this turn. No new online
primary reading is claimed; these are reused inspected sources, not
unread leads. No essential source blocker remains.

1. [Derksen--Sidman, *A sharp bound for the Castelnuovo--Mumford regularity of subspace arrangements*, Adv. Math. 172 (2002), 151--157](https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/05/A.I.a.10.pdf), Theorems 1.2 and 2.1, printed pp. 153--154, with Section 2 proof through Proposition 2.2, pp. 154--156: the intersection ideal for d projective linear spaces is d-regular, with the stated ideal-sheaf cohomology vanishing. No genericity is required. The audit must check the four disjoint projective lines, the sheaf restriction sequence and the exact degree-three cutoff in every higher degree. This theorem alone is not about nonlinear branches.
2. [Wen-Wei Li, *Yanqi Lake Lectures on Algebra, Part 3*, version 2026-07-05](https://www.wwli.asia/downloads/YAlg3.pdf#page=58), Lemma 5.2.3, printed p. 53, PDF p. 58: a filtration-preserving module map with complete source, Hausdorff exhaustive target and surjective associated graded is surjective. The recorded full proof uses convergent successive corrections. The audit must check the actual shifted order-three filtrations, closedness/completeness, module structures and every graded restriction. Neither analytic convergence nor strictness of the original image map follows automatically.
3. [Stacks Lemma 10.97.1, 00MA](https://stacks.math.columbia.edu/tag/00MA) assumes Noetherian base and finite modules for exact completion and its tensor description. [Lemma 10.97.8, 07N9](https://stacks.math.columbia.edu/tag/07N9) applies to a finite algebra over a Noetherian ring and gives product completion at the maximal ideals over the base prime. The audit must check the ambient surjection, actual image injection, quotient, topology comparison and exactly four factors. These tools do not assert that arbitrary normalization commutes with completion.
4. [Stacks Lemma 10.160.10(2), 0C0S](https://stacks.math.columbia.edu/tag/0C0S) provides power-series coordinates for complete regular local rings with the specified residue coefficient field. Apply only after checking smooth ambient and source rings, never regularity of the singular image. [Lemma 10.97.3, 00MC](https://stacks.math.columbia.edu/tag/00MC) gives faithful flatness of local Noetherian completion. [Lemma 10.52.13, 02M1](https://stacks.math.columbia.edu/tag/02M1) compares lengths under a flat local map with its closed-fibre length. The audit must identify the actual finite module, prove the claimed annihilation and check the residue fibre before descending length.
5. [Stacks Section 12.19, 0120](https://stacks.math.columbia.edu/tag/0120), Definition 12.19.3 and Lemmas 12.19.12--13, is the reused strictness warning. The full nonlinear jet map must be checked directly, including the linear-to-quadratic block. No general source here supplies its rank. The separate audit must verify the kernel elimination defining Nbar, both tangent-kernel cases, coordinate changes and every relaxed example, retaining their stated limitations.

The audited specialization is necessary because these tools do not
state L126's exact nonlinear surface formula. No reproof of their general
theorems is proposed. The generic quadratic formula of
Carlini--Catalisano--Geramita, Theorem 3.2/Remark 3.3, remains comparison
only: quaternionic distinctness is not genericity. Greuel--Pfister,
Proposition 11/Corollary 12, remains comparison only: its one-variable
conductor proof is not surface determinacy. Their exact versions and
inspected proof cases are in the reused four-branch assessment. No
additional lead is used as an established theorem. Full matching Mathlib
coverage remains not checked, not asserted absent.

## Scope, duplicates and continuation

The full L126 was read to identify its source obligations, not to perform
its independent mathematical audit. Targeted comparisons used its source
assessment, its working note and history/376--377. L122/L125 are comparison
cases, not inputs supplying four-branch values. ATTEMPTS/070's failed
minimal-defect inference and ATTEMPTS/071--072's curvature stops remain
preserved. The scoped records do not contain an earlier completed L126
critical audit. This does not establish novelty.

Essential continuation inputs are L118, L120, L121 and the full L126.
Retain a rank-two locally free Omega-polystable F, integral c_1=0,
ch_2=-14e_1-21e_2-tau_D, identical marked K3 factors, scale c=2lambda,
exactly four preimages and quaternionic tangent span two in ambient
quaternionic dimension 39. Actual normal-jet rank, F existence, collision
occurrence, global defect exclusion and transport remain unproved. Smooth
complex formal examples must not be promoted to actual quaternionic
totally geodesic K3 collisions.

This is LITERATURE / REPRODUCTION / EXPLORATION: newly completed audit
coverage, no new theorem and no mathematical correctness verdict. The
same exact target is now ready for a separate proof-audit invocation.
No lemmas, mathematical scripts, PROOF.md or DAG.md were modified.
