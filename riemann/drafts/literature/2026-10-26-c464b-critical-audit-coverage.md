# C464b critical audit — source scope approved

TARGET: Critically audit C464b's nonreal-near-degree threshold, including every shifted order, strict endpoints and central multiplicities.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-target search and duplicate/failure comparison in 2026-10-26-nonreal-near-degree-threshold-coverage.md; read C464b completely, L464 hypotheses/conclusion and Sections 1–2, and the specialization and source-comparison histories. No new external search was needed for this unchanged mechanism.
SOURCE_EVIDENCE: Existing inspected coverage of bramble_trace, Generalized Laguerre positivity at growing orders, paper 41 v4 (24 October 2026 07:18 UTC), Section 4.3 (18c)–(18h), is reused through the nonreal-degree and local-factor audit assessments; canonical L464 contains the full comparison and positive-scalar Xi split.
COMPARISON: The primary comparison covers arbitrary monic real finite factors with bounded root moduli and repeated or zero roots; C464b proposes a real/nonreal finite split and applies that comparison at each shifted order. The source does not state this exact M_nr threshold. Existing coverage permits an independent applicability audit, not a novelty claim or automatic import of C464b.
GAP: No essential source gap remains for this exact audit; correctness of the finite split, every shift, strict endpoints and degenerate cases remains for a separate research turn. Initial signs, improved nonreal counts and effective common-height onset remain independent gaps.
REASON: Approve the newly nominated critical audit by comparing its exact scope against ready source coverage; this is not the mathematical audit or a new derivation.
SCOPE: Exactly TARGET: actual Xi, real t>=2, integer p>=M+(17/2)M_nr U_t, unchanged near window |gamma-t|<2, all multiplicities and central zeros, and precisely L464's far sum U_t. No simplicity, RH or external fixed-half-plane premise.
LITERATURE_REASON: The new audit nomination was REVIEW_REQUIRED and expressly requested a separate source-scope approval. This turn resolves that gate using ready assessments without repeating external browsing or the completed specialization.

## Relevance and decision test

The main gap is initial actual-Xi signs at unbounded heights and global
mixed positivity. The intermediate target is the exact critical audit
above. A validated C464b could make a future bound on nonreal near degree
useful for a tail estimate; it does not provide that bound or the missing
initial signs. Continue with the independent audit if the inherited
comparison and normalization cover its actual hypotheses. Correct or
narrow C464b if any shifted order, endpoint, central multiplicity or
zero-degree case fails. Source readiness passes; mathematical validity
is deliberately undecided here.

## Reused primary coverage and exact limits

The [nonreal-degree assessment](2026-10-26-nonreal-near-degree-threshold-coverage.md)
already inspected [paper 41 v4, Section 4.3](https://rstation.ai/problems/riemann_hypothesis/papers/41)
through (18h), including the complete comparison and Xi allocation.
The [local-factor audit assessment](2026-10-25-local-factor-coefficient-audit-coverage.md)
records its full hypotheses and the primary count input. This turn
reuses those inspections; it does not claim a fresh external read or
an independent full-manuscript review.

The load-bearing comparison, canonical in L464 Section 1, assumes
G=product_i(1+u_i x+v_i x^2), infinitely many factors, u_i>0,
0<=2v_i<=u_i^2 and U=sum_i u_i<infinity. For a monic real B of
degree m>=1 with all root moduli <=R_0, it bounds the relative
coefficient remainder for integer k>=m by
(1+R_0 U/(k-m+1))^m-1, and gives strict positivity when
k-m+1>=2R_0 m U. Degree zero is handled separately. Repeated,
nonreal and zero roots are allowed. The positive coefficients,
coefficient-limit argument and explicit strict remainder constant
are all present in the inherited input; the audit need not reprove
them as new mathematics.

L464 Section 2 supplies the exact positive-scalar factorization with
all central factors in the finite near polynomial, no division by
Xi(t), far endpoints |gamma-t|=2 included, and every gamma+t factor
far. Its root bound is R_0=17/4. Far-product summability and
infinitude remain inherited L464 inputs, not assumptions to replace
by finite numerical evidence. The future audit should trace those
input uses as needed; this scope review does not reopen their proofs.
Titchmarsh, second edition (1986), Theorem 9.2, (9.2.1), printed p. 211,
is already covered by the local-factor assessment; no new shell-count
or effective constant is required for the C464b specialization.

## Duplicates, failures and audit obligations

The reused nonreal-degree assessment compared L255, L251, L257 and
L354, paper 50 v2 Section 2 Lemma 1, and the distinct eventual-power
results of Michelen–Sahasrabudhe. Its exact queries and inspected
statements are retained there. Those comparisons found no inspected
copy of the precise M_nr threshold; this does not establish novelty.
Their first-sign, finite-sign and count/gap masking obstructions do
not decide this parameter-sensitive eventual-order assertion.
Re-running that search is unnecessary because the claim and inputs
have not changed. No new source blocker or changed hypothesis was
identified in the scope comparison.

The later audit must read the complete C464b argument independently:
check the real/nonreal split and multiplicity conventions against
L464; verify applicability to every finite convolution shift with
unchanged U_t; check integer equality, n=M_nr=0, M=0, a vanishing
constant term at central zeros, and the term ensuring strictness.
It must distinguish the positive scalar from a central-value
normalization. These are audit obligations, not correctness findings
of this literature turn. The finite-degree refinement is the reason
a specialization audit is needed instead of merely citing the
source's all-near-degree application.

Mathlib full matching and supporting coverage remain unchecked, with
no absence claim. The broader saddle estimates, logarithmic endpoint,
initial signs, improved nonreal counts, numerical onset, global mixed
positivity and RH are outside this approval. L464's L018/L024/L026/L027
foundations are inherited; no cross-notebook theorem is used.

Outcome: EXPLORATION / LITERATURE / NOVELTY_UNCHECKED. This is a new
scope comparison approving the unchanged target under SPECIALIZE for
one later REPRODUCTION proof audit. It is neither a mathematical
advance nor a proof verdict. No lemma, mathematical script, DAG or
proof overview was modified. Mathematical exploration usage remains
zero consecutive turns after the prior ADVANCE.
