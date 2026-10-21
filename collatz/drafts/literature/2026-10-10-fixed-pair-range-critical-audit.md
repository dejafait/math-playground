# Fixed-pair range critical audit — ready coverage

TARGET: Critically audit L051's variable-count cyclic-product exclusion through twenty-two words and its first failure at twenty-three.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the five exact-pair/rational-cycle/cyclic-product queries and theorem comparisons in the ready range assessment; read L051 completely, relevant L041/L046 and L050 audit passages, the complete range generator, histories 131–133 and Attempts 019/021–024; no new discovery search or numerical verification.
SOURCE_EVIDENCE: Reopened Simons–de Weger Acta Arith. 117 (2005), period conventions p. 52, Corollary 2 and complete proof p. 53, Lemma 12 and complete proof p. 61; reopened Hercher JIS 26 (2023), Article 23.3.5, Theorem 16 and complete proof pp. 10–11; reused the range assessment's inspected rational-coding and stronger global-minimum comparisons.
COMPARISON: Published integer-cycle estimates cover the unchanged actual-word bridge, while L050's audited mechanism covers twenty words only; neither supplies a correctness verdict for L051's all-r substitutions, neighboring ceilings, outward rounding or initial sufficient-test range.
GAP: Independently audit the stated variable-count argument and every load-bearing certificate value for r=3 through 23, including both first-failure signs; no further source theorem is essential within this fixed scope.
REASON: Separate changed-audit scope comparison is complete and permits one later RESEARCH/REPRODUCTION proof audit, without new constraints, pair optimization, source recertification or reopening the stopped comparison.
SCOPE: L051's written general-r subsystem and actual-word applicability, its specified initial test through r=23, fixed p=9809721694 and q=6189245291, and complete existing certificate; no extension or optimality claim beyond that test.
LITERATURE_REASON: The newly selected L051 audit had REVIEW_REQUIRED coverage; variable-count proof and certificate scope differ from the ready twenty-word audit, so this separate comparison was essential despite adequate coverage of the unchanged primary inputs.

## Relevance and decision test

Main gap: universal eventual descent. Intermediate target: a reliable
independent audit of L051's claimed restricted exclusion and first
sufficient-test failure. Its downstream use is to establish whether the
twenty-two-word exclusion may be used, or to isolate a concrete defect.
Continue with the conclusion only after every analytic, arithmetic and
actual-word applicability obligation passes under the written hypotheses.
Otherwise preserve the failed implication or unresolved sign and withhold
the affected conclusion. Coverage readiness is not a correctness verdict.
Universal entry, unrestricted cycles, divergence and descent remain open.

Essential input IDs: L051, L050, L041, L046. Retain integer J_i>=2,
H_i>=3, nonnegative a_i congruent to 2 modulo 18, integer represented
counts and primitive scaling K=dK_0, L=dL_0, K_0>225640000.
Real shifted junctions s_i>=540/11 remain permitted; no parity, valuation
or residue hypothesis may be added to them. Keep s_0=min_i s_i, all
exact cyclic endpoints, own-index guards, log r seed and 69r/1034 length
term. Independent tails, repetitions and coincident junctions remain.

## Primary coverage and applicability

John Simons and Benne de Weger, *Theoretical and computational bounds
for m-cycles of the 3n+1-problem*, Acta Arithmetica 117 (2005), 51–70,
[published paper](https://www.impan.pl/shop/en/publication/transaction/download/product/82263):
section 1.2 p. 52 permits nonminimal periods; Corollary 2 and proof
p. 53 supply K>225640000 for nontrivial positive integer cycles;
Lemma 12 and proof p. 61 supply Lambda>exp[-13.3(0.46057+log K)],
using Rhin's Proposition p. 160 and Lemma 8. The period conventions,
corollary's computational/continued-fraction premises and short Lemma 12
proof were reopened. Prior Lemma 8 coverage remains reused.

Christian Hercher, *There are no Collatz m-Cycles with m <= 91*,
JIS 26 (2023), Article 23.3.5,
[Theorem 16 and proof pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf):
the positive cycle linear form is bounded by one third of the full
odd-input reciprocal mass. Reopened its theorem and complete proof,
including the product, mean inequality and odd-run mass partition.
The previously inspected correction leaves this theorem unchanged;
amended Theorem 21 and the full-minimum cutoff are unused here.

These published hypotheses concern integer cycles. L041's existing
all-r occurrence partition, primitive scaling, smallest-designated-junction
seed and own-word identities supply the necessary-condition bridge to
L051. Relevant L041 proof ranges and L046's real-domain transfer/prefix
passages were read. The latter per-occurrence estimates use the guards
and exact endpoint at that occurrence; their eighteen-word conclusion is
not itself a general-r input. This scope comparison licenses checking
L051's specialization, not assuming its result or rederiving it now.

Reuse `2026-10-10-fixed-pair-cyclic-product-range.md` and
`2026-10-10-twenty-cyclic-height-infeasibility-audit.md` in this directory.
Their recorded queries and inspected Halbeisen–Hungerbuehler Lemmas 1/2,
Acta Arith. 78 (1997), pp. 228–229, cover general rational parity coding.
Their stronger global-minimum comparisons do not certify this fixed
designated-junction test. No general coding or transcendence theorem
needs a local reproof. L051's changed-count product algebra does need
independent verification; the exact rational pair requires certified
finite residual signs, not a best-approximation theorem. Unused Knight
and Fernandez–Ibanez leads remain outside essential audit coverage.
No new theorem from those leads is imported, and no novelty is inferred.

The published height 301*2^50, distributed [Ro] computation, Roosendaal
communication, continued-fraction inputs 225644606/397573379 and
Rhin/Crandall originals retain their recorded import qualifications.
Original certificates and external Lean builds are not independently
certified. Full matching Mathlib coverage is not checked, not absent.
The range assessment's 2026-10-10 inspection covers the unchanged
MathPrize positive-integer target; prize adjudication adds no premise.

## Duplicates, failures and the bounded audit

Histories 131–133 record L050's separate twenty-word audit, range
coverage and the completed L051 calculation, respectively. The scoped
records contain no separate completed L051 audit. L050 supplies a
mechanism to compare, not a verdict on changed counts. L049 and Attempts
019/021–023 retain guard-only/scalar stops; none asserts feasibility of
L051's simultaneous system. Attempt 024 preserves the specified test's
first failure at twenty-three. An audit validates or repairs the completed
range; it does not renew that exhausted exclusion test.

The complete `scripts/postspell-word-count/certify_fixed_pair_range.py`
was read for scope only, without execution. A later audit must inspect
the complete relevant operands in its `fixed-pair-range-certificate.json`
using the scoped inspector, and independently check the logarithm
enclosures rather than trust saved flags. Required obligations include:

- The all-r substitutions, positive coefficients, r-1 forward transfers
  covering r input occurrences, every cyclic factor and the two offsets.
- Integer separation z=Nq-Kp>=1, epsilon's sign and strict half-log
  guard; integer counts suffice without integer junctions.
- The whole-real-ray ceiling argument, existence of the least integer
  ceiling and each neighboring-integer certificate, including M-1>A_r.
- The complete remainder/rounding budgets, log2/log3 residual cancellation,
  every row for 3<=r<=23 and both first-failure signs; no preview suffices.
- The non-strict T_r<=225640000 test against strict K<T_r and the
  primitive threshold; equality conventions must match the stated test.
- Actual-word applicability with all source qualifications preserved,
  without replacing the full local-minimum count by r or identifying a
  designated junction with the global minimum.

Do not infer real-system feasibility or a cycle at the first failure.
Keep the fixed pair, seed, transfer and endpoint constraints unchanged;
new bounds or optimization require separate coverage. A fixed-scope
repair must identify its defect and effect explicitly. This approval
authorizes one subsequent RESEARCH/REPRODUCTION audit after supervisor
approval; no mathematical audit verdict is recorded in this turn.

Completed EXPLORATION, LITERATURE/NOVELTY_UNCHECKED, actual task
literature_comparison: new audit-scope coverage, no mathematical advance
or progress beyond the sources checked. No lemma, mathematical script or
certificate was written or executed. PROOF.md and DAG.md are unchanged;
mathematical exploration usage stays zero after the preceding advance.
