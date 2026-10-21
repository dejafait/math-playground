# Response zero count — critical-audit source coverage

TARGET: Critically audit L372's full-phase monotonicity, uniform O_H(1) error, simplicity and closed-endpoint count against L005, L366 (1) and L368 (3)–(8).
CHECKED: 2026-10-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-statement searches and inspected primary proof cases recorded in 2026-10-06-response-zero-count.md; compared the audit obligations with L372 and searched the two local count assessments and retained L371 failure for scope conflicts.
SOURCE_EVIDENCE: Reused Lagarias, Acta Arith. 120(2) (2005), 159–184, DOI 10.4064/aa120-2-4, arXiv:math/0601653v2, Theorem 3.1 and complete §3 proof (3.2)–(3.5), PDF pp. 9–10, and Lemma 4.1(1), pp. 11–12; reused DLMF scalar statements/domains from 2026-10-05-gaussian-response-quadratic-sign.md; read L005, L366's hypotheses/(1), L368 (3)–(8), and L372 to identify audit scope.
COMPARISON: Standard phase-level counting and ready scalar coverage suffice for a response-specific critical audit; Lagarias's constant-angle shifted-xi count with O(log X) does not directly certify G, its variable factor, O_H(1), or closed endpoints.
GAP: Independently check L372's use of the exact carrier, single Euler-log branch, full phase derivative, common onset, integrable error, real-analytic simple crossings and all endpoint cases; no proof audit or new result is completed by this source approval.
REASON: The audit stays within the already assessed response and scalar domains; the remaining work is checking the specialization, with no essential unread theorem or critical-strip hypothesis needed.
LITERATURE_REASON: The new critical-audit continuation required separate approval; reuse adequate source evidence rather than repeat searches for the unchanged response family.
SCOPE: Only L372's response-only count on a fixed positive eventual ray, H sufficiently large and X≥H, under L005, L366 (1) and L368 (3)–(8); no effective onset, F_0/G comparison or actual-theta positivity.

## Source reuse and exact applicability

The complete search record, primary theorem comparison and essential
proof cases are retained in
`drafts/literature/2026-10-06-response-zero-count.md`. No external passage
was retrieved afresh this turn: the family and hypotheses have not changed.
The ready assessment, rather than model memory or search snippets, supplies
the primary-source coverage. Its earlier derivation target is distinct
from the present audit target; this file approves the latter's coverage.

J. C. Lagarias, *Zero spacing distributions for differenced L-functions*,
[arXiv:math/0601653v2](https://arxiv.org/pdf/math/0601653v2), 30 January
2006, Theorem 3.1 and its complete §3 proof, equations (3.2)–(3.5),
PDF pp. 9–10, supply the continuous-log/phase-level counting comparison.
Lemma 4.1(1) and its proof, pp. 11–12, cover the absolute-half-plane
logarithmic-derivative case h>1/2. Here the right-line shift is h=2.
The constant-angle shifted-xi theorem is a comparison, not a matching
response theorem. Its O(log X) conclusion and symmetric height count
must not be substituted for L372's positive-ray O_H(1) assertion.
The response's variable completion factor must be checked locally.
The RH-dependent smaller-shift cases are unnecessary and excluded.

The ready scalar assessment
`drafts/literature/2026-10-05-gaussian-response-quadratic-sign.md`
records NIST DLMF v1.2.8 (15 September 2026):
[25.2.1/11](https://dlmf.nist.gov/25.2) on Re v>1,
[5.11.1–2 and §5.11(ii)](https://dlmf.nist.gov/5.11) on
|arg s|≤π−δ with the stated complex remainder bounds, and
[5.15.8–9](https://dlmf.nist.gov/5.15) for separately controlled
polygamma derivatives. The audited inputs use v=5/2+it and
s=1/4+it/2, whose large-height arguments lie in |arg s|≤3π/4.
These domain qualifications cover the proposed audit. No growing shift,
critical-strip Euler product or differentiation of an uncontrolled
asymptotic error is authorized. A new scalar reproof would duplicate
ready inputs; only the response-specific assembly needs checking.

Xiannan Li, arXiv:0904.1051v1, §2 opening and concluding Remark,
is a previously inspected supporting comparison recorded in the count
assessment, not an additional essential theorem. Ki remains an unread
bibliographic lead and is not used. No new source search is needed
merely to audit elementary integer rounding.

## Audit obligations and source sufficiency

Reading L372 this turn identifies what requires review; it does not
critically validate its derivation. One later RESEARCH proof audit may:

- Check L366 (1)'s response convention against L368 (3)–(4) and L372
  (2), including the reflection sign, factor 1/2 and nonzero carrier.
  Use those canonical inputs without reopening the Mellin derivation.
- Check L005's absolute locally uniform Euler logarithm on Re v>1
  gives one bounded branch on the full actual line. Verify all constants
  in L372 (4)–(5) are uniform in t, and that its full phase includes the
  zeta correction. Bounded logarithmic derivative alone is insufficient
  for a bounded accumulated phase error.
- Check L368 (7)–(8)'s sector-controlled carrier derivative and rational
  polynomial correction against L372 (3). Verify a single finite onset
  controls the full phase on the whole ray, and that the integrated error
  bound in L372 (8)–(9) is independent of X.
- Check the positive amplitude and transversality at every zero without
  dividing by G. Check the real-analytic multiplicity qualification.
- Independently check L372 (10)–(12) for neither endpoint a zero, either
  endpoint a zero, both endpoints zeros, empty integer-level intervals,
  and X=H. Verify the final bound is uniform in X for each fixed H.
- Check that the direct mathematical inputs remain exactly L005, L366
  and L368 and that no missing actual-pair assumption enters the count.

These are prospective checks, not new lemmas or a completed proof audit.
SPECIALIZE is appropriate because the cited theorem does not directly
state the response result. The later audit should be REPRODUCTION,
including any necessary local repair within this exact scope.

## Relevance, retained failures and decision test

The main gap remains global actual-theta mixed positivity and the total
L367 signed margin relative to its remainder. The intermediate target
is a critical validation of L372's reference count; its plausible use
is a later actual-family count comparison, whose hypotheses remain
independently unproved. No RH candidate follows even from a successful
audit.

The retained failure in
`ATTEMPTS/2026-10-06-weak-discriminant-distinct-count.md` points to L371:
common multiple F zeros defeat the generic distinct-count implication.
The searched local interlacing assessment retains SOURCE_BLOCKED for
unconditional signed S(t) coverage. Neither obstruction is an essential
source blocker for this G-only audit. L365's fixed-regulator stop,
L370's signed arithmetic residual, the actual-pair common-zero question,
higher low-index signs, heights above forty and endpoint arithmetic
margin all remain unresolved. No sibling notebook was consulted.

Continue with the exact audit because each source obligation has ready
coverage. In that later turn accept L372 only if every dependency and
all uniform/error/endpoint claims survive independent checking. If an
essential domain or uniform bound fails, record the precise failure and
repair within scope or park the count; an O(log X) replacement does not
meet the target. Any genuinely new mathematical target requires separate
coverage review. This source decision itself certifies no count.

Full Mathlib response-count coverage remains **not checked**. Supporting
Euler-product/nonvanishing coverage is recorded canonically in L005 and
L372, including `riemannZeta_eulerProduct_exp_log`; it is not full count
coverage. Unknown availability implies neither absence nor originality.

Completed outcome: EXPLORATION / LITERATURE / NOVELTY_UNCHECKED. This
turn supplies a distinct audit-scope comparison and resolves the essential
coverage question without deriving mathematics. No lemma, mathematical
script, PROOF.md or DAG.md was modified. The newly ready assessment is
subject to the supervisor's separate next-turn approval.
