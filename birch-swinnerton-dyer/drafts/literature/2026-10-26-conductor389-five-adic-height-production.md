# Conductor-389 absolute 5-adic height production — coverage request

TARGET: Produce absolute Harvey 5-adic height certificates modulo 5^6 for P=(0,0), Q=(1,0) and P+Q on E=[0,1,1,-2,0] using the standard Frobenius/sigma algorithm, then apply L119 equations (3)--(6) with L120.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the three assessed height inputs and scoped L119/L120/L030/L034, L082 and ATTEMPTS/032/034/057; exact-curve/Harvey/Sage searches found existing regulator examples, and precision/errata searches led to the published Harvey paper and pinned Sage 10.6 sources; details and queries are in the source note.
SOURCE_EVIDENCE: Direct primary URLs https://arxiv.org/pdf/0708.3404v1 ; https://ems.press/content/book-chapter-files/27479 ; https://arxiv.org/pdf/math/0105031v2 . Inspected Harvey arXiv:0708.3404v1 Theorems 1--3 and effective Sections 3--5, compared published LMS J. Comput. Math. 11 (2008), 40--59, Theorems 1--3 pp.40--41; MST06 Section 3.2/Algorithm 3.2 pp.590--591 and Section 4.3 p.596; Kedlaya math/0105031v2 Sections 3--4, Lemmas 2--3 pp.4--5; Sage tag 10.6 padics.py and relevant monsky_washnitzer.py precision/expansion sections. Exact URLs and limits are in drafts/source-notes/2026-10-26-conductor389-height-producer-coverage.md.
COMPARISON: Harvey supplies a certified ordinary-height algorithm at the requested absolute precision; MST already tabulates this fixed regulator. Reproduction is justified only to provide checkable pointwise certificates matching L119, with explicit Frobenius/model transport and precision ledger; no new arithmetic theorem or novelty is claimed.
GAP: Source coverage is ready for one bounded standalone reproduction, but no E_2/sigma values, exact point-sum/multiple certificates, implementation correctness or strict determinant success is established. Sage is absent from PATH, so use the inspected standard Frobenius algorithm rather than presume a runtime.
REASON: The exact producer scope required separate review; inspected primary effective results now cover the arithmetic method, while source-code sign and sigma-index differences rule out treating raw Sage height output as Harvey q_H.
SCOPE: E=[0,1,1,-2,0], p=5, P=(0,0), Q=(1,0), and their exact sum; Harvey q_H as in L119, absolute output precision m=6 for each point; full Selmer input L120, with original published arithmetic computations accepted but unreplayed.

LITERATURE_REASON: Essential previously unread producer details were Frobenius/differential transport, sigma precision and actual implementation normalization; the existing ready conditional height assessments were reused without a general re-audit.
COVERED_TARGET: Produce absolute Harvey 5-adic height certificates modulo 5^6 for P=(0,0), Q=(1,0) and P+Q on E=[0,1,1,-2,0] using the standard Frobenius/sigma algorithm, then apply L119 equations (3)--(6) with L120.

## Intended bounded test and use

The main unresolved claim is rational rank equal to arbitrary complex
analytic order. This intermediate target would fill the remaining
height input in one fixed k=2 L119 application, not solve that main gap.
The source comparison must preserve the proposed calculation: certified
values modulo 5^6 for these three points, followed by the strict scaled
determinant test of L119 equations (3)--(6). No success or sufficient
precision is predicted. At this proposed bound, an enclosure admitting
zero is an inconclusive failed certificate, not height degeneracy;
increasing precision would require a separately justified continuation.

Essential local inputs are L119's audited canonical-height replacement,
L120's audited full Selmer result, and L030/L034's exact model/group
provenance. The eventual producer must certify the exact point sum and
its eligibility, Tamagawa/multiplication factors, E_2 and sigma precision,
logarithm evaluation and absolute precision after division. It must not
replace an absolute error bound by relative digits or use the unresolved
printed SW sigma convention. The inspected sources supply a method; its actual inputs and every implemented precision claim still require certification in the covered reproduction.

Reuse drafts/literature/2026-10-25-selmer-height-finite-certificate.md,
drafts/literature/2026-10-25-canonical-cyclotomic-height-replacement.md
and drafts/literature/2026-10-26-canonical-height-replacement-critical-audit.md
where their hypotheses match; inspect only the missing producer evidence
and relevant local duplicates. The source comparison below explains why
reproduction is needed: a checkable absolute-height input, not a claim
of new arithmetic. Preserve ATTEMPTS/032/034/057 and L082's distinct
p=7 result. No cross-notebook input is proposed.

## Completed source decision (step 504)

SPECIALIZE approves the mathematical coverage for the single covered target,
subject to separate next-turn approval of this newly written continuation.
The original step-504 source-review TARGET was: Assess source coverage for producing absolute 5-adic height certificates modulo 5^6 for P=(0,0), Q=(1,0) and P+Q on E=[0,1,1,-2,0], with L119's strict determinant test and L120's Selmer input.
The [source note](../source-notes/2026-10-26-conductor389-height-producer-coverage.md)
records primary hypotheses, cases, implementation differences, duplicate
arithmetic and the bounded certificate requirements. No height deduction,
new lemma, mathematical script or determinant test was performed here.
Full matching Mathlib coverage is not checked.

Use the standard small-characteristic Frobenius algorithm, importing
Kedlaya's reduction/loss bounds and Harvey's three theorems. A standalone
implementation is within coverage; an unsupported replacement truncation,
new sigma normalization, different curve/prime or raised output bound is
outside it. The source algorithms are not to be reproved. Exact arithmetic
replay and implementation-specific error accounting are necessary because
the notebook needs independently inspectable pointwise inputs, rather than
a printed regulator or software display. Failure to complete the bounded
producer must be recorded without supplying invented values.

Continue only after the exact point/multiple eligibility and full absolute
precision ledger pass. Then evaluate L119's strict determinant test. If it
admits zero, stop this m=6 test as inconclusive. Trace/determinant checks on
Frobenius, a sigma differential-equation residual, comparison with published
digits or two agreeing software runs are useful checks, but none replaces
the relevant source hypotheses and error proof. No uniform producer,
complex-order comparison, SW correction or BSD candidate follows.

## Separate continuation approval (step 505, 2026-10-26)

The supervisor required direct source URLs in the ready assessment. They
are now explicit in SOURCE_EVIDENCE, and TARGET exactly matches the retained
production action. Reopened the primary PDFs and rechecked Harvey Theorems
1--3 (pp.1--2), MST Section 3.2/Algorithm 3.2 (pp.590--591), and Kedlaya
Lemmas 2--3 (p.4); reuse step 504 for the detailed effective proof cases,
implementation comparison, duplicates and recorded failures. No changed
hypothesis or new method is proposed. SPECIALIZE approves this exact
continuation for a subsequent research turn, retaining every original
precision, eligibility and determinant obligation. This is a process repair
(STALLED), not additional mathematical evidence or another source advance.
The earlier separate-approval condition is discharged by this review.
No height, new lemma, script, or mathematical deduction was produced.
