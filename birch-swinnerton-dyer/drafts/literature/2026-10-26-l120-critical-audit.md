# L120 critical audit — source scope approved

TARGET: Critically audit L120's exact-curve full 5-Selmer import, including prime/model applicability, torsion-corrected Kummer identification and published-computation qualifications.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step-500 exact-curve discovery queries and inspected import assessment; compared the newly written L120 with L001, L030's model statement, L034's group provenance, foundations/02 and ATTEMPTS/032/034/057. No renewed broad novelty search.
SOURCE_EVIDENCE: Reopened Stein--Wuthrich published author offprint, Math. Comp. 82 (2013), Theorem 12.3 and complete proof p.1788, Section 12.4 pp.1787--1788, Algorithm 11.1 with hypotheses, all steps, proof and Proposition 11.2 pp.1783--1784; Cremona corrected second edition (1997), Table 1 definitions p.109 and row p.157, Table 2 definitions p.255 and row p.257. Reused assessed Milne IV (29), p.113 and IV.3.1, p.114 through foundations/02.
COMPARISON: Published arithmetic theorems cover the input scope; the separate audit must check L120's finite prime count, exact label/model match, torsion correction and full Kummer specialization. These local deductions are audit obligations, not new source theorems or an independent replay of the published computation.
GAP: Coverage is ready for the exact audit; no audit verdict is issued here. Historical computations, the printed SW sigma discrepancy, absolute height certificates and the general rank/complex-order comparison remain outside this approval.
REASON: A theorem-to-obligation comparison now separately covers the newly written L120 audit; it preserves the completed import without treating approval of its production scope as a correctness verdict.
SCOPE: E=[0,1,1,-2,0] over Q, p=5, full classical multiplication-by-5 Selmer group with all local conditions; published unconditional computational results accepted as precise citations, original executions unreplayed; no BSD or full Sha finiteness assumption.
LITERATURE_REASON: The saved audit request was REVIEW_REQUIRED; this step approves the changed critical-review scope using existing discovery and narrowly reopened primary evidence.
COVERED_TARGET: Critically audit L120's exact-curve full 5-Selmer import, including prime/model applicability, torsion-corrected Kummer identification and published-computation qualifications.

## Relevance and decision test

The main unresolved claim is rational rank equal to complex analytic order
for arbitrary E/Q with order at least two. The intermediate target is the
separate critical audit of L120. Its plausible downstream use is the
sharp full-Selmer bound b=2 with torsion correction t=0 in a k=2 L119
application. Eligible points and absolute canonical-height certificates
remain independent requirements; a successful audit would not supply them.

Continue to that audit when inspected sources cover every arithmetic input
and the remaining obligations are checks of the written specialization.
This source-coverage test is met. Reject the local argument if it needs
analytic Sha, BSD, full Sha finiteness, an isogeny-Selmer dimension or
unrecorded software output. Return any genuinely uncovered theorem to
REVIEW_REQUIRED. A failed arithmetic check must be recorded rather than
replaced with a new claim. This turn does not perform those proof checks.

## Primary comparison and audit boundary

[Stein--Wuthrich, published author offprint](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf),
DOI 10.1090/S0025-5718-2012-02649-4, electronically published 2012-09-14,
identifies 389a immediately before Theorem 12.3, printed p.1788. Its
arithmetic Sha[p] conclusion and accompanying conjectural-order congruence
are distinct assertions. The former is the input requested by L120.
Its prime range and exceptions must be applied exactly, with good ordinary
reduction at 5 checked from the model rather than inferred from a label.
The theorem's entire proof invokes a completed computation similar to the
preceding computation, taking several weeks of CPU time. It does not
supply individual execution transcripts in that proof.

Algorithm 11.1, pp.1783--1784, requires p>2, nonadditive reduction and
surjective residual representation. Its ordinary proof uses established
regulator nondegeneracy, the matching order criterion of Theorem 6.1 and
Kato's divisibility for the resulting upper bound. Proposition 11.2's
conjectures concern general algorithmic success and equality. They must
not be imported as assumptions on a completed Theorem 12.3 case. Conversely,
reimplementing Algorithm 11.1 would require independently establishing its
inputs; that is outside this citation-based audit. The regulator and
residual-representation computations belong to the accepted published
input, not new verifications by this notebook. No general termination
claim or independent source-code audit is approved.

[Cremona Table 1](https://johncremona.github.io/book/fulltext/table1.pdf),
printed p.109, explicitly defines its rank and torsion columns as arithmetic
invariants of E(Q). Its p.157 conductor-389 block has row 389A1 with the
coefficient vector used in L120. [Table 2](https://johncremona.github.io/book/fulltext/table2.pdf),
p.255, defines its entries as generators modulo torsion on Table 1's
minimal equation; its p.257 row supplies the two cited points. The audit
must check that the Weierstrass coefficient convention and the author's
389a notation select the same curve, and distinguish the direct table
rank/torsion input from L034's weaker independence use. L034's p=7
conclusions are not premises for a p=5 Selmer bound. The table definitions
and selected rows were reopened as PDF text; screenshot requests returned
no inspectable images, so no visual verification is claimed.

For the Kummer input, reuse foundations/02 and L001 with
[Milne, Elliptic Curves, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf),
Chapter IV, (29), p.113 and Theorem IV.3.1, p.114. A fresh PDF request
this turn timed out; unchanged assessed source coverage is reused rather
than treating that transient fetch failure as a missing theorem. The
audit must verify all local conditions, the n=1 specialization, the
rational torsion factor, the F5-linear identification and the direction
of the Kummer map. Finite full Sha is not a hypothesis of the cited exact
sequence. Do not replace a full Selmer group by a marked subspace.

## Reuse, failures and limits

The step-500 [import assessment](2026-10-26-conductor389-full-five-selmer-input.md)
and [source note](../source-notes/2026-10-26-conductor389-full-five-selmer-coverage.md)
retain discovery queries, primary locators, errata inspection and unread
alternative-method leads. Step 501 already identified the older p=7
import as distinct from L120. ATTEMPTS/032's capped p=7 scalar failure and
ATTEMPTS/034's repeated-interface stop do not forbid this exact p=5 input.
ATTEMPTS/057's SW sigma/E_2 discrepancy remains unresolved. Accepting
Theorem 12.3 as a published theorem does not reconcile that formula or
independently validate its implementation; the audit must keep this
qualification rather than claim a computational replay.

No new lemma, mathematical script, arithmetic deduction or correctness
verdict is produced in this literature step. Mathlib coverage remains
not checked, not absent. SPECIALIZE approves only the exact covered audit
for a separate RESEARCH / REPRODUCTION / proof_audit turn; the canonical
argument and DAG are unchanged.
