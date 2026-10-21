# Palindrome affine-ABP critical-audit coverage

TARGET: Critically audit L033's F₂ palindrome coefficient-rank proof, affine-DAG normalization and full binary bounds.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-family search in drafts/literature/2026-10-07-polynomial-degree-circuit-abp-obstruction.md; inspected L033, its saved work/history 070–071, Attempt 020 and the repeated-approval failure in Attempt 018; no new discovery search was needed.
SOURCE_EVIDENCE: Reopened the same nine-page Nisan extended abstract, Definition 1 (§2, PDF p.4), Theorem 1 lower-bound proof (§3, PDF p.5) and Theorem 4 (§4.2, PDF p.6); reopened the same 16-page Raz–Shpilka manuscript Definition 1 and Lemma 2, including Steps 2–5 and runtime qualifications, printed pp.4–6.
COMPARISON: The audit is within the previously inspected rank and normalization mechanisms, but neither cited theorem states L033's complete F₂ affine-DAG/full-encoding result; those already written applicability arguments remain the object of the mathematical audit.
GAP: No essential source is missing for auditing L033; the correctness of its local field/model specialization and full bounds has not yet been critically checked.
REASON: Approve the newly proposed audit scope by reusing adequate primary coverage; this is a coverage repair, not a mathematical audit or progress beyond the known palindrome separation.
SCOPE: Only the existing L033 over free F₂<x_0,x_1>, identical formal output, explicit finite acyclic affine-edge graphs, and its stated circuit/normalization/binary bounds; no new lower-bound theorem or IPS target.

## Approved audit scope

Audit only the completed canonical result, not a new lower-bound target. Reuse prior primary coverage if adequate, without a new search for its own sake. Check the unique word expansion, middle-cut permutation rank in F₂, path decomposition with affine labels and canceling constant paths, finite acyclic closure, normalization with a unique designated source/sink, all circuit/internal degrees including k=0, full binary threshold, and absence of unintended mathematical dependencies. The only comparison needed is whether these checks stay inside the inspected field/model proof cases. No audit verdict is recorded here.

Inputs: L033 and the named Nisan/Raz–Shpilka proof cases; L017/L018/L032 and Attempt 016 are context or contrasts only. Unresolved independent assumptions remain general ER data, IPS realization/unavoidable output, changing certificates, every-certificate hardness, arbitrary-circuit identity checking and decision transfer. Nothing in this continuation supplies them.

## Mathlib

Coverage remains not checked; approval must not infer an absent theorem from that qualification.

## Source-level comparison and approval boundary

The primary references and source versions remain those of the prior assessment: Noam Nisan, *Lower Bounds for Non-Commutative Computation (Extended Abstract)*, STOC 1991, pp.410–418, [DOI](https://doi.org/10.1145/103418.103462), [nine-page primary-paper mirror](https://www.csa.iisc.ac.in/~chandan/courses/arithmetic_circuits/notes/noncomm.pdf); Ran Raz and Amir Shpilka, *Deterministic Polynomial Identity Testing in Non Commutative Models*, [author-hosted 16-page manuscript](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf), no revision date printed. Retrieval on 2026-10-07 confirmed the relevant statements and proof cases, rather than relying on snippets. The prior later-paper duplicate comparison is reused; no unread lead is promoted to an input.

Nisan's Definition 1 uses consecutive layers, homogeneous linear labels and vertex size over the reals. Theorem 1's lower-bound proof factors a coefficient matrix through one layer; Theorem 4 treats the exact palindrome family and displayed sandwich recurrence. These support the known mechanism, not a verbatim theorem for arbitrary affine DAGs over F₂. The audit must examine L033's field and receiving-model arguments, including the reversal ordering, rather than import the real theorem unchanged. Its upper-bound characterization and depth result are unnecessary.

Raz–Shpilka's field F has no stated characteristic restriction. Lemma 2 assumes a formula and zero free term. Steps 2–5 address degree copies, pruning, scalar-edge removal and component selection; the runtime discussion uses formula-derived size and degree facts. These support the operations, but do not give L033's arbitrary-DAG runtime or exact edge/bit counts. The audit must check the local finite-closure implementation, source/terminal handling and positive-degree restriction, without importing formula-specific runtime or assuming formula unfolding. No source statement by itself verifies those local arguments.

Full binary accounting and k=0 are explicit local conventions, so their audit requires the canonical text rather than another theorem search. Replaying the cited mathematics is justified only to test the changed field/model and costs. The ready classification for that later mathematical step is REPRODUCTION. This approval supplies no verdict on L033 and changes no lemma, dependency or assembled argument.

The intermediate target is a trustworthy audited obstruction to degree-only identical-output conversion. Its plausible downstream use is to exclude that blanket conversion while assessing stronger structured or changed-certificate routes. Continue after an audit confirming every stated hypothesis and asymptotic threshold; if a load-bearing error is found, record it and repair or narrow L033 before relying on it. Do not repeat this source approval: Attempt 018 records why repeated approvals without an audit are unproductive. The main P versus NP gap and the independent assumptions listed above remain unresolved.
