# Finite-height all-order signs — completed source review

TARGET: Assess source coverage for extending L255 to nonnegative actual-Xi Laguerre signs at every order on |t|<=3*10^12-1/2, including central multiplicities, using Platt–Trudgian Theorem 1 without a tail-onset premise.
CHECKED: 2026-10-25
DECISION: IMPORT
SEARCH_EVIDENCE: Reused the initial-sign comparison and checked L018/L255; retried the author PDF through its landing-page link successfully. Queries: site:suvrit.github.io/papers/riem-xi "1.3" "1.5"; Suvrit Sra On some positivity properties Riemann Xi 2026. No new mechanism search was needed.
SOURCE_EVIDENCE: Sra, On some positivity properties of the Riemann Xi function, v1 (20 October 2026), (1.1), (1.5), Theorem 1.3, pp. 1–3; Lemmas 4.1–4.2 and the complete Theorem 1.3 proof, pp. 9–11. Platt–Trudgian arXiv:2004.09765v1, Theorem 1 and Section 2, p. 2. Both primary texts inspected; reuse confirmed.
COMPARISON: The exact finite interval and all multiplicities are explicitly source-covered. L255 covers only noncentral points in its generalization; importing the source closes that documentation gap without a new proof.
GAP: No missing theorem hypothesis for this finite-height import was identified. Large-height low orders, effective tail overlap and mixed positivity remain open locally; the source manuscript is not independently audited in full.
REASON: Approve citation-only import, not a reproduction or novelty claim. This review resolves the nomination's source-scope questions; no lemma or mathematical script is written this turn.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED required separate approval of central multiplicities, coefficient convention and endpoint; prior primary-read coverage was reused and the needed cases were freshly accessible.

Essential inputs: L018 for actual Xi, L024 for the product, L026 for
unconditional strip localization, L027 for infinite zeros, and L255 for
the existing noncentral argument. Platt–Trudgian Theorem 1 supplies the
finite verified zero range. No cross-notebook input is proposed.

Downstream use: canonical finite-height all-order coverage could isolate
large-height low orders as the remaining sign obligation. It does not
resolve global mixed positivity. Continue only if the recorded or newly
retrieved primary hypotheses cover the coefficient convention and central
multiplicities; otherwise state the precise missing case and retain
REVIEW_REQUIRED or SOURCE_BLOCKED without a new proof. A reproof must be
justified as an audit of the missing case, not a novelty claim.

## Primary coverage and applicability record

Precise citations: Suvrit Sra, [On some positivity properties of the
Riemann Xi function, v1](https://suvrit.github.io/papers/riem-xi/riem-xi-v1.pdf),
20 October 2026, Theorem 1.3, printed p. 3, and (1.5), p. 2;
Dave Platt and Tim Trudgian, [The Riemann hypothesis is true up to
3 times 10^12](https://arxiv.org/pdf/2004.09765v1), Theorem 1, printed p. 2.
The author landing page identifies Sra's version; its PDF link succeeded
after a direct URL request failed. There is no remaining access blocker.

Sra assumes T>1/2 and all nontrivial zeros with 0<gamma<=T on the line.
Theorem 1.3 gives L_n(Xi;x)>=0 for n>=0 and |x|<=T-1/2,
including multiple central zeros. Equation (1.5) is exactly L255's D_n:
(2n)!^(-1) binomial(2n,j)=1/(j!(2n-j)!). Equation (1.1) matches L018.
Thus no order doubling or normalization conversion is needed.
Platt–Trudgian's theorem verifies a height 3,000,175,332,800,
which includes the proposed T=3*10^12. No simplicity input is needed.

The inspected proof cases in Lemma 4.2 include real factors, conjugate
pairs, the exponential prefactor and locally uniform coefficient limits.
They avoid division by the center value. The final Theorem 1.3 proof
also treats central multiplicity explicitly. The endpoint is included
in the theorem's closed interval. Only nonnegativity is proposed for
import; blanket strictness at every order is not proposed.

## Duplicate and failure comparison

The initial-sign assessment already records the primary result and its
finite-height limitation. L255's proof should not be reproduced as a
new finding. Its nonzero-center restriction is the reason to canonicalize
the source theorem rather than merely relabel its existing generalization.
The masking and count/gap failures recorded in that reused assessment
concern generic global inferences; no such inference is used here.
The effective-onset review's missing constants are untouched. This review
neither supplies those constants nor turns an existential tail onset into
overlap with the finite interval.

The turn's continuation test passes for citation-only finite-height
coverage. The nominated scope has no uncovered multiplicity or endpoint
case. A later import needs only identify the coefficient convention and
verified-height specialization; an independent product reproof is
unnecessary. Full matching Mathlib coverage is unchecked, not absent.
The prepared import assessment receives separate next-turn approval as
required for a newly written continuation. No change to PROOF.md or DAG.md
is appropriate before the canonical import is actually performed.
