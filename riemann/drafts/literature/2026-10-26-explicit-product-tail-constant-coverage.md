# Explicit product-tail constant — source scope approved

TARGET: Give an explicit numerical C in L464's all-height quadratic-order Xi tail using L467's A=18 and rigorous upper bounds for S_0 and S_1, without a saddle or common-onset claim.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready product-comparison and explicit-shell assessments; searched notebook lemmas, literature and attempts for S_0, S_1, numerical C and quadratic-order duplicates; inspected the recorded effective-onset stop. Two targeted external searches found the source and unrelated coefficient-sequence leads, not an inspected numerical substitute.
SOURCE_EVIDENCE: bramble_trace, Generalized Laguerre positivity at growing orders, https://rstation.ai/problems/riemann_hypothesis/papers/41, v4 (24 October 2026 07:18 UTC), Section 4.3 (18c)–(18h), complete comparison and product case; Bellotti–Wong, https://arxiv.org/pdf/2412.15470v2 (7 July 2025), Theorem 1.1 p. 1, with Section 5 pp. 23–24 coverage reused and its closing two height cases reconfirmed; local L464 Section 3 and audited L467.
COMPARISON: The known product theorem already supplies the unconditional quadratic-order tail; L464 expresses its constant through A and two convergent sums, and L467 supplies A=18. A numerical value is a quantitative specialization of those inputs, not a new positivity mechanism or claimed discovery.
GAP: No essential source coverage is missing for the exact product-only calculation. Complete rigorous sum upper bounds and conservative numerical substitution remain undone; the logarithmic-order saddle constants, common onset and initial signs remain independent gaps.
REASON: Approve a bounded REPRODUCTION calculation from existing verified local inequalities; avoid reproof of the count theorem, product comparison or saddle estimates.
SCOPE: Actual Xi, every real t>=2 and integer p>=C log^2(t+2), natural logarithms, all multiplicities and central zeros; inputs L018, L464 and L467. No RH, simplicity or fixed-half-plane premise. Only the exact TARGET is approved.
LITERATURE_REASON: The numerical product-only constant was outside the completed shell audit; this separate review supplies its quantitative scope using ready source assessments and the recorded stop.

## Gap, use and decision test

The main gap is initial actual-Xi signs at unbounded heights; effective
bounded-height/tail overlap and global mixed positivity also remain open.
The intermediate target is an explicit all-height quadratic-order tail
constant. Its downstream use is an effective upper-order certificate for
the product mechanism. It leaves a growing initial segment unchecked.
Continue if complete sum majorants give one fixed numerical C for all
stated t and p. A partial sum without a tail bound does not pass. Park
this component if it needs uncovered saddle or amplitude estimates.

This review approves the calculation, not a numerical value or a proof
verdict. No new mathematical result or mathematical script was produced.

## Primary theorem comparison and reused coverage

[bramble_trace v4, Section 4.3](https://rstation.ai/problems/riemann_hypothesis/papers/41)
was read through all of (18c)–(18h). It compares a finite monic factor
with an infinite positive-coefficient product, including repeated and
zero roots. The Xi split retains multiplicities and positive normalization
at central zeros. Local shell counting gives the existential quadratic
threshold. Section 4.4 separately uses large-height overlap; it supplies
no numerical common onset. L464 already reproduces the product argument.

[Bellotti–Wong v2, Theorem 1.1, p. 1](https://arxiv.org/pdf/2412.15470v2)
gives its explicit global zero-count error for every T>=e, using positive
ordinates through T. Its Section 5 conclusion combines large-height
Table 2 bounds with the compact-height computation and gamma estimate.
The prior primary-source assessments cover these cases and the argument-
principle multiplicity convention. Their analytic and computational
proofs remain cited inputs, not independently rerun here. L467's dated
critical audit checks the elementary A=18 specialization, including closed
shell endpoints and low heights. No further count estimate is needed.

Reused assessments are
[product comparison](2026-10-25-local-factor-coefficient-audit-coverage.md),
[explicit count](2026-10-25-explicit-unit-shell-count-coverage.md), and
[L467 audit scope](2026-10-25-l467-critical-audit-coverage.md).
The exact local constant formula is in L464 Section 3, following (9).
This review does not independently re-audit L464's proof.

## Duplicate and failure comparison

The notebook-scoped search located L464 as the sole matching product-tail
formula and this nomination as its pending numerical specialization.
Other S_0/S_1 occurrences refer to different quantities. No matching
numerical constant was located; this is not a novelty claim. Existing
compact-interval factor results do not supply the requested all-height
constant. The initial-sign and finite-sign obstructions remain intact.

The [effective-onset assessment](2026-10-25-unconditional-tail-effective-onset-coverage.md)
parks the full numerical common-onset package because saddle, amplitude
and count constants were missing. L467 addresses the count component;
it does not supply the other components. The product-only target neither
reopens that package nor claims overlap with finite-height signs.
The witness/upper-tail threshold-matching attempt concerns surviving
logarithmic low indices; a quadratic tail constant does not resolve it.

Queries on 26 October 2026 were “"Generalized Laguerre positivity at
growing orders" explicit constant” and “"Xi" "Laguerre" "log"
"explicit" coefficient tail”. Results about Li coefficients and Taylor-
coefficient log-concavity have different targets and supply no input.
A Nankai-hosted Laguerre-inequalities PDF lead timed out; its search
snippet is not theorem coverage and is not essential to the present
specialization. No novelty or stronger theorem is inferred from searches.

## Approved calculation obligations

Use the displayed L464 formula unchanged and substitute L467's A=18.
Bound both complete positive sums by proved majorants: an integral-test
bound with a justified monotone range, or finite terms plus an analytic
tail, is acceptable. Any logarithm bounds must have rigorous direction
and enough precision for a conservative final integer C. Numerical
floating-point output alone is insufficient. Check the p versus 2p
normalization and the endpoint p>=C log^2(t+2), with M=0 and central
zeros inherited exactly from L464. This specifies work to do next turn;
no inequalities or numerical values are established here.

A successful specialization belongs in its own canonical corollary with
hypotheses, proof, source qualifications and Mathlib section. Full matching
and supporting Mathlib coverage remain unchecked, with no absence claim.
No change to PROOF.md or DAG.md is needed for this source-only review.
