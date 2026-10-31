# Two-branch detector test for the weighted off-line count

TARGET: Test a two-branch zero-detector proof of W_delta(T)<=C T delta(log T)^2 exp(-c delta log T) at delta=log log T/log T, retaining both detector branches and full multiplicities.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuses the completed exact-weight and stronger-result search in drafts/literature/2026-10-30-zeta-squared-weighted-local-density.md; an additional notebook-local identifier/detector search found no earlier matching assessment or ATTEMPTS entry. No novelty inference.
SOURCE_EVIDENCE: Direct primary sources: Baier, Acta Arith. 113 (2004), Proposition 4 pp. 83--84 and Section 6 pp. 90--92, https://www.impan.pl/shop/en/publication/transaction/download/product/83115 ; versioned text https://arxiv.org/html/math/0512445v1 ; Fazzari arXiv:1912.08127v2 Lemma 2.1 p. 3, https://arxiv.org/html/1912.08127v2 . Reopened 2026-10-30 for this approval; source arithmetic proofs remain cited inputs, not independently audited.
COMPARISON: Existing sources supply a two-type pointwise zero detector and short-polynomial twisted moments; they do not supply their proposed positive continuous zeta-squared weighted application. This attempt must construct and bound that application before separating the count from the amplitude, rather than repeat L486 or assume a weighted moment at selected zeros.
GAP: Retain the local amplitude through both detector types, justify the resulting integrations and multiplicities, and obtain the displayed estimate with absolute C,c>0 at the single bounded scale; uniformity on the full delta interval and transfer to B remain later obligations.
REASON: New primary coverage identifies an independently testable detector mechanism at the surviving amplitude/count correlation gap. EXPLORE licenses one bounded attempt, including an informative failure, without approving its mathematics. The separate literature approval on 2026-10-30 repaired direct-source provenance; this remains approval to attempt, not approval of the proposed mathematics.
SCOPE: Actual zeta, every sufficiently large real T at delta=log log T/log T, strict beta>1/2+delta/2, closed |gamma-t|<=2delta, full multiplicities, no simplicity, spacing, independence, selected-zero moment, RH or external half-plane premise. Use only the inspected detector/short-polynomial tools and canonical L471/L483/L485/L486 for normalization and comparison; no new analytical input is silently assumed.

## Preserved target and downstream role

W_delta and its full-range inequality are defined in the completed
source assessment named above. The current test is one scale of that
same proposed inequality, not a replacement definition or an assertion
that the full uniform estimate follows. The main gap is actual-Xi
initial signs at unbounded heights and all-degree mixed positivity.
A retained-amplitude density estimate could be used in L486's finite
nonnegative kernel instead of its count/amplitude Cauchy--Schwarz step.
That kernel transfer, displacement bands beyond this scale, complementary
mass, full negative-mass saving and individual-height signs are unresolved.
L474 is only a contrast for the small-displacement sector; no additional
specialization of its shifted moment is presumed.

## One bounded attempt

Use the two alternatives in Baier's Proposition 4 as the proposed
starting detector, not his final weighted-density conclusion with a
different polynomial weight. Treat both the Gamma-integral branch and
the smoothed-tail branch. All source parameters must meet the stated
logarithmic comparability, height and length conditions with fixed
constants; if height padding is needed, justify it. The strict target
cutoff avoids beta=1/2, but estimates must retain any Gamma cost as
beta approaches that line. Empty/truncated windows and repeated zeros
must be handled without a separation or simplicity assumption.

Fazzari's unconditional Lemma 2.1 is a possible short-polynomial tool,
not an automatic bound for a translated, truncated or zero-dependent
family. Verify its coefficient hypotheses, fixed strict length margin
and error uniformity for any family actually introduced. A source
statement is cited rather than reproved; any necessary extension is a
named unresolved obligation. No RH-dependent log-derivative estimate,
complex-statistic positivity, general-weight Maples--Rodgers assertion,
or new selected-value theorem may be inserted as an input.

Continue if both branches yield the displayed C,c estimate at the
specified scale, or a rigorously identified distinct correlation term
with a concrete test. If either branch requires the missing weighted
selection theorem as a premise, or every justified estimate simply
reproduces the known losing separation, record the exact surviving
term and stop this detector implementation. Do not turn a failed upper
bound into a lower bound for W_delta, an impossibility theorem, or a
refutation of RH. A new source or refined mechanism is required before
repeating a failed attempt. Mathlib coverage remains unchecked.

## Routing

Recommend proof_attempt/creative, deep_research/max. The critical claim
is whether a positive off-line detector can retain the |zeta|^2 weight
without the extra logarithmic loss from separating amplitudes and counts.
The decisive bounded test is the displayed W_delta inequality with some
fixed c>0 at delta=log log T/log T and every sufficiently large real T.
No calculation, proof, parameter optimization or new lemma was performed
while writing this assessment. Its separate approval should reuse the
completed source record, not restart discovery without a changed premise.

## Separate source-gate approval, 30 October 2026

LITERATURE_REASON: Supervisor recovery identified missing direct source URLs in this assessment; reuse the completed comparison, repair provenance and approve the unchanged target without another discovery search.

Reopened the linked primary texts: Baier Proposition 4, equations
(16)--(22), and Section 6 equations (79)--(84); Fazzari Lemma 2.1.
The journal PDF was accessible; the versioned Baier text supplied
searchable formulas. The source qualifications in the completed
assessment remain in force. Baier's detector includes the Gamma
integral and smoothed tail, under logarithmic parameter comparability
and a lower height cutoff. Its Section 6 estimates use a particular
polynomial weight and separated subsets; they are not an arbitrary
positive-weight theorem. Fazzari requires divisor-size coefficients
and theta+2sigma<1; its stated error does not itself certify uniformity
for a zero-dependent family. These are application obligations, not
essential unread input theorems silently granted by this approval.

Decision remains EXPLORE for exactly TARGET and SCOPE above. This
separate review completes the requested approval using existing coverage.
No mathematical application, new bound, reproof or lemma was made.
The next invocation should attempt the bounded test, retaining
multiplicities, both branches, near-line Gamma costs and fixed length
margin; stop if it needs the missing weighted theorem as a premise.
The full-range estimate, kernel transfer and individual signs remain
open. Mathlib coverage is unchecked. This is a provenance/process
repair, not a mathematical advance or a renewed exploration budget.
