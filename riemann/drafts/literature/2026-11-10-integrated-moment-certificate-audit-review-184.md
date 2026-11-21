# Independent integrated-moment certificate audit — scope review completed

TARGET: Review source and scope coverage for an independent audit of L970's n=2 moment certificate, including outward elementary arithmetic, both tails, quadrature errors and complete signed propagation.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step185 reused 2026-11-10-integrated-theta-variance-review-182.md and its exact searches; checked L970, its complete construction script, step184 history and retained finite-Li/marginal audit records. Direct retrieval was limited to the precise quadrature statement and newly essential Python arithmetic references; no new broad sign search.
SOURCE_EVIDENCE: Directly read DLMF3.5.1-3 with C^2 hypotheses and Python3.15.2 decimal/fractions contracts for construction, Context arithmetic, rounding, signals and rational operations. Local Python reports3.15.2. Read L019 and relevant L966/L967 hypotheses/formulas; retain the prior L969/C969a and ordinary-Li comparisons. Full references and audit scope are in 2026-11-10-l970-independent-audit-coverage-185.md.
COMPARISON: Quadrature and arithmetic contracts cover the method, not effective constants or code correctness. L970's derivative, elementary-value, tail and signed-propagation claims still need independent specialization checks; no source supplies its sign automatically. Independent replay is not a new sign discovery.
GAP: Source/method coverage is complete for this bounded audit, but every effective inequality and arithmetic enclosure supporting L970 remains unverified; PASS, previews and structural checks do not establish correctness. All higher indices of L966(16) remain open.
REASON: Step185 completed the separate source/scope comparison and approved the bounded audit in 2026-11-10-l970-independent-audit-coverage-185.md; no mathematical audit acceptance is claimed.
LITERATURE_REASON: The startup target required separate coverage review of the new effective certificate; the reused quadrature assessment did not inspect the implementation's decimal arithmetic contract.

## Completed review — step185

The exact startup TARGET has been reviewed, with no new derivation,
lemma edit, mathematical script edit or certificate replay. Read L970
and its construction script completely for scope, L019 and relevant
L966/L967 hypotheses and formulas; reused step183's source comparison
and retained pointwise/finite-Li failures. The new primary material is
the Python3.15.2 decimal/fractions contract, matching the installed
`python3 --version`. DLMF3.5.1-3 was directly rechecked, not reproved.
The updated fields above and the completed assessment below record
the work actually done in step185; step184's original nomination
remains below for its proposed obligations.

The separate, now-ready [audit assessment](2026-11-10-l970-independent-audit-coverage-185.md)
contains precise primary references, qualifications and the bounded
acceptance test. Its SPECIALIZE decision approves REPRODUCTION of
the fixed certificate's verification, not acceptance of L970 or a new
sign mechanism. Outcome EXPLORATION, LITERATURE, NOVELTY_UNCHECKED:
coverage is complete and no source is blocked, but no mathematical
bound was independently established. The remaining text preserves
the original nomination and its unperformed audit obligations.

## Original nomination — step184, preserved

The main gap remains actual-Xi all-index L966(16), sufficient for RH
by audited L968. The proposed intermediate target checks the reliability
of one quantitative n=2 base case. It could support a separately
assessed uniform mechanism, but cannot replace one. Do not proceed
to n=3 or another isolated finite sign as part of this audit.

Essential proof inputs are L019, audited L966 and L967's existing
n=2 coefficients and normalization. L968 is downstream context only.
L969/C969a remain contrasting pointwise obstructions. No cross-notebook
input, RH, zero table, assumed moment box or Stieltjes law is used.

The audit should read L970 in full and inspect
`scripts/li-theta/integrated-moment-certificate-184.py` together with
the full selected aggregate fields and all relevant cell evidence in
its JSON certificate. Check the exponential range reduction, rational
Taylor tail, Machin branch and decimal directed-rounding operations;
check both derivative polynomials, every H derivative, the local
trapezoidal remainder, omitted-m geometric majorant, improper-u
majorant and its slope bound. Verify positive denominator endpoints
and propagate both subtractions with I_2(b)>0, including the exact
conservative lower endpoint 423263556/10748505625. Retain failures
and repair rather than overwrite the original certificate if needed.

The continuation test is acceptance of all hypotheses, bounds and
arithmetic under this fixed scope. A missed tail, incorrectly directed
operation or unsupported derivative bound requires correction and
new verification before accepting the sign. If the error cannot be
bounded within this certificate, record the obstruction; do not replace
it by floating-point evidence or extrapolate to all n. Full matching
Mathlib coverage remains unknown. This nomination supplies no new
literature result, mathematical lemma or independent audit outcome.
