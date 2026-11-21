# Exact aggregate Machin repair — nomination after step581

TARGET: Certify the stored census579 pi interval by exact rational Machin partial sums and alternating remainders, without rerunning the census, and determine whether this bypasses the failed power-inclusion premise.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step578/580 inclusion assessments and step581 failure; searched Machin formula 239 with DLMF/author-source terms and alternating-series remainder. Inspected DLMF4.24.3, Rycroft AM205 Unit0 PDF p13, OpenStax Calculus2 Section5.5 Thms5.13–5.14 and Python3.15.2 fractions contracts; Brown Machin notes inaccessible and not relied on.
SOURCE_EVIDENCE: DLMF4.24.3 https://dlmf.nist.gov/4.24#E3 ; Chris H. Rycroft, Harvard AM205 Unit0, slide13 (PDF p13, zero-based12), https://people.math.wisc.edu/~chr/am205/slides/am205_unit0.pdf ; OpenStax Calculus Volume2 Section5.5 Thms5.13–5.14 https://openstax.org/books/calculus-volume-2/pages/5-5-alternating-series ; Python3.15.2 fractions https://docs.python.org/3/library/fractions.html ; inspected L815 audit qualification and census579 atan source.
COMPARISON: Standard Machin identity, convergent arctangent series and alternating remainder cover exact rational aggregation for q=5,239 with120 terms. They do not certify containment in the saved decimal endpoints; that implementation-specific comparison is the only approved difference. No general Decimal power guarantee is needed or restored.
GAP: Exact aggregate enclosure and both endpoint comparisons remain uncomputed; original certificate provenance must be retained and checked. All thirteen exclusions remain unverified pending the remaining tails/trig/normalization/whole-cell audit even if pi containment succeeds.
REASON: Essential source scope is now inspected for the changed aggregate repair after step581. Approve one later bounded exact-arithmetic specialization, not a new theorem, census rerun or precision increase.
SCOPE: Only the saved pi interval and exact q=5,239 series with120 terms and next-term remainder; no transform evaluation, census rerun, new analytic sign mechanism or cross-notebook input.

Essential inputs are L815, the pi/atan source in
`scripts/polya-census/census-579.py`, the original pi endpoints in
`scripts/polya-census/census-579.json`, and the exact step581 failure.
L016/L019/L020/L021/L814 remain downstream mathematical inputs if a later
full audit resumes; they do not supply the missing arithmetic enclosure.

The source approval should compare the proposed exact finite aggregation
with the already used Machin identity and alternating-series remainder,
including signs and branch qualification. Do not approve it by deriving
the requested numeric containment in the literature turn. If coverage is
adequate, a later research step may use exact integer/rational arithmetic
to enclose the real pi and compare both endpoints with the saved interval.
No generic correctly rounded power premise is to be restored.

Continue only if the aggregate enclosure is contained in the saved pi
interval; otherwise retain the original certificate as unsupported and
identify the needed correction without rerunning the stopped scan. A
successful repair would settle only this arithmetic premise: full tails,
normalization, trig inclusion and all claimed cells still need the rest
of the independent audit. Unbounded x, signs, common/multiple zeros and
actual-Xi all-degree mixed positivity remain open. Full matching Mathlib
coverage is unchecked. No prepared creative signed mechanism is available;
the discovered essential arithmetic flaw is the immediate blocker.

## Completed source comparison — step582, 5 November 2026

This is a literature-only approval of the unchanged TARGET. The earlier
nomination is preserved above as prospective context. No containment
calculation, new lemma or mathematical script was produced.

### Inspected standard inputs and qualifications

[DLMF4.24.3](https://dlmf.nist.gov/4.24#E3), online equation accessed
5 November 2026, states the principal arctangent power series on |z|<=1,
z!=+i,-i. Both positive reciprocals lie strictly inside its disk.
There is no boundary-convergence or complex-branch problem here.

[Rycroft, Harvard AM205 Unit0](https://people.math.wisc.edu/~chr/am205/slides/am205_unit0.pdf),
slide13, PDF page13, “Formula of John Machin”, states
pi/4=4 arctan(1/5)-arctan(1/239). Its displayed proof uses double angles
and tangent subtraction: tan(2 alpha)=5/12, tan(4 alpha)=120/119,
and tan(4 alpha-pi/4)=1/239. Import the named Machin identity with
principal real arctangents; tangent equality alone for an arbitrary
alpha would only identify an angle modulo pi. The intended principal
angle lies in the branch needed for the final inverse-tangent step.
No local reproof of Machin's identity is needed. This undated source
version is identified by its URL and inspected slide, accessed today.
The PDF text of that entire proof slide was read; its separate screenshot
request failed. Brown's author-hosted Machin notes twice timed out and
are an unread lead, not evidence or an essential blocker.

[OpenStax, Calculus Volume2 Section5.5](https://openstax.org/books/calculus-volume-2/pages/5-5-alternating-series),
Theorems5.13–5.14, online version accessed today: positive nonincreasing
term magnitudes tending to zero imply convergence; the remainder after
N terms has absolute value at most the next magnitude. The accompanying
partial-sum discussion places the limit between consecutive partial sums.
The q>1 reciprocal odd-power terms meet these hypotheses. The saved
code uses indices k=0,...,119 and next exponent241, denominator241;
its symmetric remainder is allowed by Theorem5.14, without requiring
a stronger signed enclosure. A later certificate must record its indexing
and remainder convention explicitly. Negative coefficient -4 requires
reversing the second arctangent interval's endpoints when aggregating;
a triangle-inequality symmetric error is also admissible. These are
applicability obligations for the known theorem, not a new analytic result.

[Python3.15.2 fractions](https://docs.python.org/3/library/fractions.html),
Fraction constructors and Rational operations, documents rational
arithmetic and exact conversion from finite decimal strings/Decimals.
Its examples distinguish exact string input from binary floating input.
Use integer numerator/denominator construction for all terms and parse
the two saved endpoint strings exactly. Do not use floats,
limit_denominator, rounded decimal renderings or Decimal powers in a
load-bearing comparison. Save complete integer/rational values and
comparison certificates; a printed decimal preview does not verify them.

### Approved specialization and decision test

Reuse step578's inclusion principle; do not reprove interval arithmetic
or repeat searches for a finite census. Read the preserved pi field of
census579.json and the step581 provenance evidence. Form exact finite
rational sums for q=5 and239 with the saved120-term truncation and the
cited next-term bounds; combine by the stated Machin coefficients.
Check both exact containment inequalities against the saved endpoints.
Also check the imported identity's principal-branch qualification in the
canonical write-up. Full certificates and input hashes belong in the
later research artifacts; do not execute census579.py's census loop.

If contained, this supplies an independent initial pi enclosure and
bypasses only its failed compositional power premise. It does not validate
that primitive on intervals, remove step581's counterexample, or establish
the subsequent numerical claims. If not contained, report the exact
failed inequality and retain the census as unsupported; noncontainment
of a conservative enclosure alone does not prove pi is outside the saved
interval. Preserve the fixed-cap cancellation stop and unresolved [6.5,40].

Essential arithmetic inputs: L815's qualification, census579.py/json and
audit581.py/json. Downstream L016/L019/L020/L021/L814 still require their
remaining analytic/numerical audit. This finite arithmetic target has no
RH-level sign conclusion. Actual-Xi mixed positivity, unbounded x and
common/multiple zeros remain open. Full matching Mathlib coverage is
unchecked. No cross-notebook input or new creative mechanism is used.
