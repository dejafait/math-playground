# Local branch-recovery construction — proposed audit source gate

TARGET: Assess source coverage for a critical audit of C997c's finite-shift branch recovery with norm at most n^2 and absolute error O(exp(-n/32)) times slope-measure TV.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step321 reused review318's completed comparison, searched the exact local branch/binomial/finite-shift records and stops293/314/315/316/318, and retrieved primary binomial, Legendre, finite Fourier and complex-measure contracts; queries and inspected cases are below.
SOURCE_EVIDENCE: Complete C997c read; L997(4) and C997a(1)-(2) inspected; NIST DLMF 4.6.7, 18.12.11 with its section-wide domain qualification, 1.8.4; Tao 245A Notes6 Theorem43 and proof; Axler Measure, Integration & Real Analysis (author version 12 June2026), 9.10 pp260-261 and 9.41 p274 with relevant complex-measure proof cases.
COMPARISON: The general identities and measure tools are known; none of the inspected sources states C997c's joint finite-window norm/error contract. Its finite coefficient estimates, frequency geometry and complete TV accounting are written local specializations requiring audit, not grounds for claiming novelty.
GAP: Independently verify C997c(1)-(18), including use of polynomial coefficients outside the initial Legendre convergence domain, complex measures, accessible finite shifts and the all-n quantitative margins; no essential source blocker remains for that audit.
REASON: Step321 completes source/scope approval for the exact covered audit below, without performing it or certifying C997c's conclusion; step320's unaudited construction and all independent RH gaps are preserved.
LITERATURE_REASON: Newly written C997c uses a specific Legendre/binomial finite-shift construction not inspected in review318; this separate turn checks those essential source contracts and approves its conceptual audit, without refreshing the unchanged broader bibliography.
SCOPE: Only the critical audit of the existing C997c construction with L997(4) and C997a(1)-(2); no new filter, stronger rates, selected continuation, slope inversion or actual-Xi transfer is approved.
COVERED_TARGET: Critically audit C997c's finite-shift branch recovery for every finite complex slope measure, verifying norm at most n^2 and absolute error at most C*exp(-n/32)*||mu||_TV for n>=48 on the closed interior band.

## Exact scope to assess

Read C997c's complete proof before approving its audit. Reuse the unchanged
review318 comparison, not an automatic refresh of its entire bibliography.
The relevant elementary mechanism is a truncated binomial generating
polynomial on the narrow complete frequency band, realized as finite
point-evaluation shifts. It does not invoke an optimal entire sign theorem,
global Hilbert-transform boundedness or a sampling theorem.

The audit must check every finite complex slope measure, both original
short intervals, beta reflection, K's -1, the factor -2 in H_n^+, and both
closed output endpoints. Check the positive/negative multiplier convention,
the polynomial's bound on the FULL sine range, the l1 coefficient bound,
and the SAME sequence for every positive exponential norm allowance.
Verify that the rate log(49)/12-9/32 exceeds 1/32 and that lower-band
growth introduced by the operator is paid by exp(-n/16). The exact scalar
certificate supports arithmetic only and is not an all-n or conceptual audit.

Essential local mathematical inputs are L997(4), C997a(1)-(2) and the
new C997c. Review312 is background coverage, not an extra theorem premise.
The prior endpoint, interpolation, Chebyshev and strip-transfer stops
remain scope comparisons. No cross-notebook result is proposed.

Passing source comparison may approve a later proof_audit/conceptual_audit
of the stated construction. A missing essential source contract must be
identified precisely; model memory, a citation label or numerical agreement
must not stand in for that contract. This document itself approves no audit
or downstream mathematical target during step320.

The main target still needs L030-L032/C032a actual-Xi positivity and
L966/L968 signed forcing. Selected normalization/continuation, original
slope-assay feasibility, actual reconstruction, signed recovery,
infinite-zero complements, regulator uniformity, L993 and L984(H) are
unresolved. No claim that local branch recovery closes these gaps is made.
Mathlib full matching coverage is unchecked and unknown.

## Completed source comparison — step321, 10 November 2026

This is one literature-only comparison of the saved TARGET. The nomination
above records step320's earlier state; the SPECIALIZE decision now approves
only the covered audit. No proof audit, new derivation, certificate replay,
lemma edit or mathematical script was performed in step321.

### Relevance, bounded test and reuse

The main gap is still L030-L032/C032a actual-Xi positivity and L966/L968
signed forcing, with L984(H)'s bound unpaid. The intermediate target is
independent verification of the existing local branch-recovery claim.
If valid, it supplies branch information for a later separately assessed
continuation/localization test; it supplies neither selected normalization
nor an inversion of the slope measure. Continue only if the full complex-
measure construction, closed-window access, SAME-sequence quantifier and
fixed positive TV-error exponent survive audit. Repair or withdraw the
claimed bound if any essential support, normalization or rate fails.
Failure of this construction would not exclude every local operator.

Read the complete C997c proof and the essential L997(4), C997a(1)-(2)
definitions and quartet reduction. Reuse review318's inspected sign,
sampling and truncated-transform comparison unchanged. Those sources do
not provide a norm-controlled representation of this specific filter;
their statements need not be searched again. No cross-notebook input.

Local searches in the two local-branch reviews and corresponding histories
for `C997c`, `Legendre`, `finite.shift` and `binomial` found the construction
and nomination, not an independent audit. This is a bounded duplicate
check, not a novelty finding. Read the specific ATTEMPTS records293/314/
315/316/318 and history317. The audited fixed-bump leakage and prescribed
Chebyshev-slope cost concern particular slope measures; the interpolation
and strip trials have unpaid amplification estimates. They do not decide
an operator that extracts a different observable. Preserve their stops;
the new helper does not reopen their failed quantitative certificates.

### Primary contracts and applicability limits

**Binomial and Legendre coefficients.** NIST DLMF, version1.2.8,
released 15 September2026, inspected online 10 November2026:
[4.6.7 and its following domain statement](https://dlmf.nist.gov/4.6.E7),
[18.12.11](https://dlmf.nist.gov/18.12.E11) and the section18.12 opening
domain qualification. The binomial series permits complex exponent and
argument of modulus less than one; exponent -1/2 is allowed. The Legendre
generating function initially takes its real polynomial argument in
[-1,1], with series variable of modulus less than one. C997c(7)-(9) also
uses arguments below -1. Its finite coefficient identity near zero must
therefore be distinguished from evaluating the infinite series at a
fixed radius there. Audit the written root-factor/binomial argument
rather than importing unrestricted convergence from the displayed DLMF
formula. The actual infinite-series evaluation in C997c(12) is on [-1,1].
These source identities are imported, not reproved; the explicit global
coefficient and norm estimates remain local specializations requiring
verification. No extremal sign-approximation theorem is a premise.

**Finite Fourier convention.** Inspected
[DLMF1.8.4](https://dlmf.nist.gov/1.8.E4), with the complex exponential
convention of1.8.3, same version/date. This supplies the coefficient
normalization. C997c uses a finite trigonometric polynomial, so a theorem
on convergence of arbitrary Fourier series or a global Hilbert transform
is unnecessary. The later audit must check the coefficient bound, degree,
accessible shifts and multiplier sign in C997c(13)-(15). The citation
alone does not prove their operator norm on the full continuous space.

**Complex measures.** Sheldon Axler,
[*Measure, Integration & Real Analysis*](https://measure.axler.net/MIRA.pdf),
author-hosted version dated12 June2026, 9.10 pp260-261 (PDF pages274-275),
9.41(b) p274 (PDF page288). Inspected both statements, 9.10's complex
simple-function approximation case and 9.41's full short proof; also
9.36's hypotheses and its real/complex reduction on p274. For positive
measure lambda and h in L1(lambda), 9.10 identifies the variation of
h dlambda as |h| dlambda. Theorem9.41 represents any complex measure by
a measurable unit-modulus density against its variation. These justify
using variation as the positive controlling measure; they do not supply
C997c's numerical TV exponents. Audit its parameter-dependent densities,
their measurability, finite integrability and resulting marginal measures.
Endpoint atoms in the slope variable remain allowed.

**Interchange.** Terence Tao,
[*245A, Notes6: Outer measures, pre-measures, and product measures*](https://terrytao.wordpress.com/2010/10/30/245a-notes-6-outer-measures-pre-measures-and-product-measures/),
30 October2010, Theorem43 and its proof following Theorem42, inspected
10 November2026. Its complete sigma-finite positive measure spaces and
complex absolutely integrable product integrand give equality of the
product and both iterated integrals, with integrable sections almost
everywhere. The proof reduces the real case to positive/negative parts
using Tonelli, then treats real and imaginary parts. For C997c the
audit can use completions of finite |mu| and finite restricted Lebesgue
measure, with Axler's density representation for mu. Borel densities
and a compact parameter rectangle are the stated applicability mechanism;
checking them for the written formulas remains the audit's task.
This does not license an infinite-zero interchange or regulator limit.

Queries were `site.terrytao.wordpress.com Fubini Tonelli complex valued
sigma finite 245a` and `site.measure.axler.net complex measures total
variation integration Fubini theorem`, together with direct retrieval of
the cited DLMF sections. Search snippets were locators only. Axler and
Tao were inspected at theorem/proof level; other returned notes, textbook
mirrors, forums and unrelated recent papers were not used as evidence.
No source access failure blocks this audit. Full matching Mathlib
coverage remains unchecked and unknown; no absence is inferred.

### Exact audit continuation

The covered audit is a proof_audit/conceptual_audit, not a creative filter
attempt. It must replay C997c's complete argument for every finite complex
mu, retaining C997a's -4 cosine response versus the -2 nominated branch,
both beta terms, both intervals, K's -1 and both closed output endpoints.
Check the full sine range and intervening polynomial bound, the l1
coefficient cost and every finite shift, and establish the SAME sequence
for every epsilon>0. Independently verify n>=48, the floor choices,
log(49)/12-9/32>1/32, and payment of the lower band after operator growth.
If replaying the scalar certificate, inspect its complete relevant checks;
its historical 18 passes alone certify neither the conceptual proof nor
the all-n bounds. No further discovery turn is needed for this unchanged
audit. Any enlarged mathematical target requires its own coverage.

Selected continuation/value1, the original simultaneous suppression and
subexponential slope-TV assay, actual reconstruction, signed recovery,
infinite-zero complements, regulator uniformity, L993 and L984(H) remain
unresolved independently of whether this audit passes. No RH candidate,
stronger source theorem or claim of mathematical originality is made.
