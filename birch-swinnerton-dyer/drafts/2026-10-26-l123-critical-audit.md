# L123 conceptual audit — step 515

2026-10-26. Completed. RESEARCH / proof_audit / conceptual_audit /
REPRODUCTION / EXPLORATION.
Prior unchanged gate: drafts/literature/2026-10-26-plectic-retained-plus-cancellation.md
(EXPLORE). Supplied settings: gpt-6-astra, xhigh; actual runtime not
independently observable. No token accounting.

Main gap: rational rank versus complex order for arbitrary curves.
Intermediate target: audit the complete-integral residual in L123,
especially (6)–(10), under its existing hypotheses. A sound residual
could support an arithmetic test of the same-prime local component.
Nonvanishing, rational Kummer membership, a multiplicative-prime
replacement for L005 and the general analytic-order comparison remain
independent and unproved.

Continue only if coefficient conjugation, integration before Hecke
localization, the domain/naturality of pr_A, descent and both factors
1/2 survive. Otherwise retain the valid subclaims and record the exact
failure; do not use raw finite moments as projected evidence.

The supplied overview, DAG and ready assessment were used without
rereading. L123, step-514 scratch and source notes, and ATTEMPTS/003,
/004, /030, /058, /059 were inspected. Existing unfinished notebook
changes are preserved. Primary-source retrieval in this turn is a
proof audit of already assessed inputs, not new literature discovery.

## Verdict and canonical evidence

PASS for the formal reduction only. Full mathematical reasoning and
the descent clarification remain canonical in
[L123](../lemmas/L123-retained-plus-norm-moment.md), especially its
coefficient-action, scalar-projection, full-integral/descent and raw
moment arguments. No new lemma or mathematical script was written.
No CM coefficient or projected local class was evaluated. This is a
successful check of existing reasoning, not an arithmetic advance or
progress beyond the inspected sources.

The checks below are audit findings, not a second proof:

| Check | Result and limit |
| --- | --- |
| (9), restriction and changing the lift | PASS; the inner-action difference is a coboundary, while raw C need not square to one. |
| Coefficient domain and naturality | PASS; C preserves the raw module and commutes with the stated projection on its invariant domain. |
| (10), scalar projection and Tate normalization | PASS; the trace gives the norm logarithm, lambda is equivariant, and u_1 is nonzero. |
| Full integral and initial descent | PASS; L123 now writes the extraction by Tr composed with lambda^{-1} explicitly and checks uniqueness. |
| Finite descent and (6) | PASS; rational averaging permits p-divisible class-field degree; the two half-projectors give 1/4. |
| (7), raw cells | PASS as an input specification, not an arithmetic evaluation or a conjugate-CM reindexing formula. |
| (8), infinite series | PASS; the lower bound n-v_p(n) >= n-floor(log_p n) is monotone and tends to infinity. Integration occurs in the complete raw module. |
| Finite-evidence claims | PASS; no projected precision or exact zero/nonzero follows from a raw truncation. |

The first descent was implicit through the source construction; making
its scalar extraction and injectivity explicit repairs no false
conclusion and is not counted as an ADVANCE. The original proof and
all prior stop evidence are retained. DAG dependencies are unchanged:
no local lemma is used as an input to L123.

## Source audit scope

Primary source: Fornea, *Plectic Heegner classes*,
[arXiv:2603.28327v2, 13 April 2026](https://arxiv.org/html/2603.28327v2).
The existing assessment was reused. Targeted theorem/proof passages
were retrieved for Lemma 2.16, Proposition 2.18, Corollary 2.21, Corollary 3.9,
Lemma 4.12, Corollary 4.15 and Corollary 4.24; definitions and formulas
(20)–(23), (31), (36), (50), (52)–(54), (63), (68), Definition 4.17
and Remark 4.20 were compared. Corollary 2.21 explicitly describes
its ordinary transition isomorphisms as Galois equivariant. That
source input is imported, not independently reproved; no new theorem
certification of Fornea's construction is claimed. The constant-mass
and mock-projection comparison is reused from the prior assessment.

A separate attempted HTML extraction through Python failed at DNS
resolution before writing a file. The web tool supplied the relevant
primary passages. This failure is not mathematical evidence and does
not make the audit source-blocked. No numerical checks were needed.
Mathlib coverage remains not checked.

## Decision

Two of three mathematical exploration turns have now been used;
passing a formal audit does not reset that budget. ATTEMPTS/059 still
parks scalar-sign and mass-only cancellation. The remaining arithmetic
test needs the action on actual CM points with their level structure,
not merely the already checked naturality of C. The proposed next
target is a CM conjugation/reciprocity transformation of the complete
norm moment and a test of its implication for R. Its essential
arithmetic transformation theorem has not been
assessed; the new continuation is REVIEW_REQUIRED, not approved here.
No further mathematical attempt is made in this turn.
