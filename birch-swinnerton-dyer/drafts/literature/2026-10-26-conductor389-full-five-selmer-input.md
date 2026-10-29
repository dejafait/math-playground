# Conductor-389 full 5-Selmer input — source coverage

TARGET: Assess unconditional source coverage for certifying dim_F5 Sel_5(E/Q)<=2 for E: y^2+y=x^3+x^2-2x as L119's first concrete full-Selmer input.
CHECKED: 2026-10-26
DECISION: IMPORT
SEARCH_EVIDENCE: Exact-curve 5-Selmer/5-descent and stronger Sha searches located Stein--Wuthrich Theorem 12.3; inspected its statement, proof and Algorithm 11.1's ordinary proof case. Reused the full-descent assessment and checked ATTEMPTS/032/034/057 and L034 for overlap. Queries and read locators are in the source note below.
SOURCE_EVIDENCE: Stein--Wuthrich, Math. Comp. 82 (2013), Theorem 12.3 and proof p.1788, Section 12.4 pp.1787--1788, Algorithm 11.1 and proof pp.1783--1784; Cremona, corrected second edition (1997), Table 1 p.157 row 389A1 with column definitions p.109, Table 2 p.257 and its definition p.255. Reuse L001's assessed Kummer relation and L034's arithmetic-group provenance.
COMPARISON: A published unconditional computational theorem supplies the stronger Sha[5] vanishing input; the published arithmetic rank/torsion inputs and existing Kummer relation cover the requested full multiplication-by-5 Selmer bound. A new full descent or general interface is unnecessary for this cited-result target.
GAP: The canonical import and explicit Kummer applicability argument remain for a separate mathematical turn; this review performs no new Selmer deduction or arithmetic replay. Absolute height certificates, a uniform producer and arbitrary complex-order comparison are not supplied.
REASON: Essential coverage is now inspected and the exact-curve result is known. Import the published theorem with transparent provenance rather than reproduce its large calculation or substitute a rank/analytic-Sha table alone for a Selmer bound.
SCOPE: Only E=[0,1,1,-2,0] over Q and the full classical multiplication-by-5 Selmer group. Published unconditional computational results are allowed as precise citations; no BSD, full Sha finiteness or independently replayed descent is assumed.
LITERATURE_REASON: The saved exact-curve target had REVIEW_REQUIRED coverage; the height-audit assessment did not cover an arithmetic full 5-Selmer input.
COVERED_TARGET: Import dim_F5 Sel_5(E/Q)=2 for E: y^2+y=x^3+x^2-2x from Stein--Wuthrich Theorem 12.3, Cremona's published rank/torsion data and L001's Kummer relation, recording published-computation provenance.

## Gap, relevance and decision test

The main gap remains rank/order equality for arbitrary E/Q of analytic
order at least two. The intermediate target is exactly TARGET. Its
plausible use is L119's k=2 sharp full-Selmer input; eligible points,
good ordinary applicability and absolute canonical-height certificates
would still be needed for that consumer. The source's stronger arithmetic
conclusion must not be advertised as a new consequence discovered here.

The test was an unconditional inspected exact-curve result or a complete
certified full-Selmer method. The first alternative is met at the level
of source coverage. The subsequent import must match model, prime and
full Selmer group, include the torsion correction, and record the cited
computation. Stop if it needs an analytic-BSD value, an unchecked software
output or an assumed finite Sha. Independent arithmetic replay is a
different target.

## Primary comparison and import boundary

[Stein--Wuthrich, Theorem 12.3, p.1788](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=32)
identifies its curve as 389a immediately before the statement. Its
covered primes include 5; the exceptional ordinary prime is 16231,
and its bad/supersingular exclusions do not include 5. The arithmetic
Sha[p] assertion is distinct from its accompanying conjectural-order
congruence. The source note records the ordinary proof case and why
conjectural general termination is not a premise of a completed case.

[Cremona, Table 1, p.157](https://johncremona.github.io/book/fulltext/table1.pdf#page=49)
has the sole row 389A1 with coefficients [0,1,1,-2,0], rank 2 and torsion
order 1. The [column definitions, p.109](https://johncremona.github.io/book/fulltext/table1.pdf#page=1)
identify arithmetic rank and rational torsion order. The
[Table 2 definition, p.255, and row p.257](https://johncremona.github.io/book/fulltext/table2.pdf#page=3)
give Mordell--Weil generators (0,0),(1,0), rather than analytic-rank
predictions. L034 already records the group-result provenance and
computational qualifications; no fresh saturation proof is needed.
The author's [ecdata explanation](https://johncremona.github.io/ecdata/)
explicitly uses this example and confirms the model/label. The inspected
[2003 errata](https://johncremona.github.io/book/errata.pdf)
contain no correction to this entry.

L001 supplies the assessed finite Kummer relation. The next import must
write its specialization at n=1, p=5 and justify the rational-group
quotient from the cited group data. These are approved applicability
obligations, not a new derivation performed in this literature turn.
No L119 conclusion is needed to justify the import; L119 is a possible
later consumer only. No circular use of its rank/Sha conclusion is allowed.

## Duplicates, failures and qualifications

The ready `2026-10-15-full-descent-finite-quotient-upper-enclosure.md`
assessment covers a general Schaefer--Stoll producer interface, without
this curve's arithmetic output. ATTEMPTS/034 stops repeated interface
work; ATTEMPTS/032 records a different capped p=7 scalar failure.
Neither prevents the exact published p=5 import.

ATTEMPTS/057 and L119's printed SW sigma/E_2 discrepancy remain open.
This assessment approves citing the published arithmetic theorem as a
whole, not reconstructing it from the disputed displayed height formula.
Algorithm 11.1 cites MST/Harvey for its height computation. This reference
is not an implementation audit or a correction of the printed formula.
Neither historical execution nor regulator values were independently
replayed here. Preserve that distinction in the canonical import.

No essential source access blocker remains. Fisher's explicit 5-descent
paper is an unread alternative-method lead; talk notes and Sage examples
are discovery aids, not the proposed theorem input. Full matching Mathlib
coverage has not been checked. This is local source coverage, without
progress beyond the cited arithmetic theorem or a BSD candidate.

Detailed queries and read coverage:
`drafts/source-notes/2026-10-26-conductor389-full-five-selmer-coverage.md`.
The single covered continuation above receives separate supervisor
approval next turn; no mathematical application occurs here.
