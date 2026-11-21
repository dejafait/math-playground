# Fixed full-domain cumulant comparison — audit nomination

TARGET: Audit L767 and L768's fixed r=3,m=5 full-domain comparison, including normalization, analytic remainders, directed rounding, and the complete theta tail.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step396 reused the full-first-theta-summand assessment, checked the two relevant recorded transfer stops, and retrieved official Python Decimal method contracts; no repeat broad Nuttall search.
SOURCE_EVIDENCE: Reused step393 primary-source comparison: wronskRH.pdf Sections3.1–4.1, basicRH.pdf Theorem3.1, RHsplit.pdf Sections2–3, det3CAEXP_2.pdf Theorems2.2/3.5; newly read Python 3.15 Decimal docs, Decimal.exp/ln, Context method equivalence, next_minus/next_plus and context semantics.
COMPARISON: The same fixed comparison remains within the known source program; the new full-domain certificate needs an independent hypothesis and implementation audit, not a novelty claim or import of source numerics.
GAP: Source scope is adequate for the unchanged fixed-order audit; correctness of analytic disks, derivative majorants, every interval operation and all-summand estimates remains unverified. No inspected source certifies L768.
REASON: Separate literature gate completed in step396; approve an independent audit of the existing quantitative reproduction, without treating Nuttall numerical evidence or software documentation as verification of the certificate.
LITERATURE_REASON: Mandatory separate gate for the newly nominated audit; the implementation rounding contract was an essential source premise to locate, while mathematical overlap coverage was reusable.
SCOPE: Independent audit of the unchanged fixed r=3,m=5 comparison only; no all-order smoothing, exceptional coefficient transfer or RH candidate review.
COVERED_TARGET: Audit L767 and L768's fixed r=3,m=5 full-domain comparison, including normalization, analytic remainders, directed rounding, and the complete theta tail.

The completed research step is covered by
`2026-11-04-full-first-theta-summand-cumulant-review.md`, whose
COVERED_TARGET was the exact comparison now addressed. This new
assessment does not retroactively gate or reject that completed work.
The initial REVIEW_REQUIRED nomination is preserved by this account;
step396 changes it to EXPLORE after reviewing scope and the essential
implementation source. This approves examination, not the result.

Essential local inputs are L019's exact kernel and decay, L767's
normalization/finite differences/full-theta bound, and L768's
degree-20 tail and compact certificate. Inspect the canonical proofs
and scripts/cumulant-comparison/compact-certificate-395.py and its
JSON evidence. L018/L021 matter only to later Xi transfer, not the
fixed comparison. The historical different-kernel direct-transfer
and norm stops remain intact and do not contradict this fixed test.

The audit should check the radius-2 q-panel Cauchy estimate, the
radius-1 x-system bound and degree-64 remainder, the derivative
recurrence including p=0, every compact cell rather than sampled
points, strict overlap at x=32, and all n>=2 in the tail. Check the
Decimal exp/ln rounding contract or replace it by an independently
justified enclosure if needed. No matching Mathlib theorem was
checked; unknown coverage is not evidence of absence.

Continue only if the complete analytic and finite evidence supports
positive base and relative error below 1/2 including x=pi. A genuine
error requires repair or withdrawal of the affected bound; an
unproved implementation premise must be recorded explicitly. A
successful audit remains a fixed-order result, with effective
all-order smoothing and exceptional coefficient transfer unresolved.


## Step396: source gate completed

The unchanged mathematical scope is covered by the step393 assessment
`2026-11-04-full-first-theta-summand-cumulant-review.md`, read in full.
Its primary-source statements and essential proof-case comparisons
are reused, not independently re-audited. In particular Nuttall's
2013 finite-order theorem is an unsmoothed sign result, whereas the
2012 positive-level reports give numerical splits and conjectures.
None supplies the stated uniform absolute relative bound at m=5.
The local normalization/conclusion sections of L767/L768 and L768's
certificate-premise section were read to confirm the audit's scope;
no mathematical claim was proved or critically accepted this turn.

The narrowly inspected stops are
`ATTEMPTS/2026-11-04-conrey-ghosh-cumulant-direct-transfer-stop.md`
and `ATTEMPTS/2026-11-04-actual-theta-product-compensation-source-limit.md`.
They concern a different kernel and missing exceptional coefficient
transfer, respectively; neither forbids verifying this fixed comparison.
The current all-degree gap is unchanged. No new source theorem is
imported and no reproof of a matching theorem is requested.

### Primary implementation source

Read on 2026-11-04: Python's official
[Decimal reference](https://docs.python.org/3.15/library/decimal.html),
served as version 3.15.2. Relevant sections are Decimal.exp,
Decimal.ln, Context's correspondence with Decimal methods,
Context.next_minus/next_plus and the context description.
The reference specifies nearest-even correct rounding for exp and ln;
the Context correspondence applies those methods with the supplied
context. Adjacent-value methods use the representable numbers in
that context. Contexts also determine exponent limits and signals.
These are software contracts, not a proof that the local program
implements outward arithmetic at every call site. L768 records a
3.15.0 replay; the audit must check its installed implementation and
any relevant version difference rather than silently equating versions.
The script's Ball methods and 55-digit contexts were located, without
running or validating the program. Documentation's warning about
Context.power's weaker rounding guarantee must not be confused with
exp/ln; the audit should inspect actual operations used.

### Approved bounded audit and limits

Inputs: L019 for exact K/B and decay; L767 for normalization and
complete theta tail; L768 and its cited compact-certificate-395.py/JSON
for the full-domain claim. Read complete relevant evidence during
the audit, not just the conclusion sections read here. Verify the
factorial/derivative convention, signed determinant, radius-2 panel
analytic branches and bounds, radius-1 complex system and degree-64
remainder, p=0 recurrence, all 29 closed cells and their 2784 panels,
x=pi and x=32 overlap, degree-20 tail and every n>=2 contribution.
Check context use, conversions, arithmetic outside Ball, exponent
range, special values and directed rounding against the source contract.
Cauchy's coefficient estimate, Taylor remainder, Tonelli and elementary
Gronwall are named standard tools; their application hypotheses and
constants remain the substance of the audit, not accepted premises.

Accept downstream use only after signed positivity and error below
1/2 are supported on the complete domain. Repair or withdraw an
unsupported bound; do not replace it by sampling. This does not
approve any new mathematical target. All-order smoothing and the
exceptional k=r-1 transfer remain independent unresolved gaps.
No justified creative all-degree mechanism emerged from this bounded
scope review; the essential outstanding audit precedes further use.
Mathlib coverage remains not checked, not claimed absent.
