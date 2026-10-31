# Source coverage for the L526 critical audit

TARGET: Assess source coverage for an independent critical audit of L526's common-pole-phase Sonin increment bound, including its rational Hardy background, uniform weighted evaluations, trace finiteness and inverse-Gram identity.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the approved pole-compensated increment assessment and arithmetic-slope screen, read L526 and its local stop/history, and inspected the specific Hardy, gamma, trace-ideal and Toeplitz proof cases detailed below. The source comparison is now complete for one audit; no originality inference or broad rediscovery.
SOURCE_EVIDENCE: Inspected bramble_trace paper 2 v2 (16 October 2026), Section 1, (5.2), Lemma 6.1 proof, Theorem 6.5 proof (6.20)--(6.26), and Theorem 7.1 proof; Srivastava MA650 notes (updated 2 May 2026), Lemma 8.6(ii), Theorems 8.8 and 8.18(i); Camara--Partington arXiv:1711.04511v2 Section 2.1; Bell (18 April 2016), Theorems 18 and 23; DLMF 5.5.3, 5.11.3 and 5.11.9. Sources are scoped inputs, not independently audited manuscripts.
COMPARISON: The uncorrected increment theorem does not cover the changing pole phase. Its commutator estimates explicitly cover arbitrary Toeplitz kernels; standard Hardy/gamma/trace theorems cover the tools for checking the local rational-background argument. L526 (2)--(20) still require an independent application audit; no known theorem located verifies them together.
GAP: Coverage is sufficient to audit L526, retaining the cited-source qualifications. The range identity, local analytic gluing, parameter-uniform evaluations and legality of localized trace subtraction remain unverified local claims, not missing external conclusions to assume.
REASON: Named standard inputs and inspected source proof cases now specify a bounded conceptual audit. Only audit coverage is approved here; neither L526 nor any RH implication is certified. The ready continuation is recorded separately for the next invocation gate.
LITERATURE_REASON: Essential standard-source scope for the newly written rational-background and uniform-evaluation audit was not yet documented. This one review filled that scope using the previous assessments; no additional discovery turn is requested.
SCOPE: Coverage preparation for one conceptual audit of L526. This assessment does not approve a new estimate, generalization, different padding, or nullvector transfer.

## Exact material for the coverage decision

Read L526, not all previous Weil lemmas. Its mathematical inputs are
the primary manuscript at
https://rstation.ai/problems/riemann_hypothesis/papers/2 (v2,
16 October 2026), the standard half-plane Paley–Wiener theorem and
Hardy Cauchy bound, gamma reflection, and
https://dlmf.nist.gov/5.11.E3 . The existing target assessment is
`2026-10-30-pole-compensated-sonin-increment-test.md`.

The prospective audit must check the sign/reflection convention,
the factor `(1+iz)^2` and fixed symbol `u_inf b^(-2)`, both directions
of the multiplier range identity, and the entire gluing in (7).
It must check the exp(C A) inverse bound, the O(A/L) absolute
weight error, the small-weight interval J, Taylor/interpolation
uniformity in (15)--(17), and the strictly positive envelope gap.
It must also retain both separate finite traces, G^(-1), the
three covariance regions, all powers of the added prime, and the
unchanged pole term. A numerical preview cannot validate these.

The prospective success test is a justified common-M
Delta_p=O_h(p^(-1/2)(log p)^(9/10)) with the exact -2rL arithmetic
benchmark. A wrong range identity, missing uniformity, or illegal
trace subtraction requires a concrete repair or downgrade of L526.
No negative complete-Weil form or actual-nullvector assertion is
part of this result. A mere repetition of the source's Theorem 6.5
does not audit its corrected-background specialization.

For later use only, L515/L516/L521/L522 retain the conditional
nullvector and trace/nonresonance hypotheses, signed pole and both
shifts. Full-form identification, family control, trace vanishing
and Xi transfer are still open. They are downstream limitations,
not mathematical premises of L526. Mathlib remains unchecked.


## Completed source-scope review, 2026-10-30

This is a literature-only assessment. L526 was read in full to locate
its claims, without verifying or repairing them. Its pending critical
audit and the provisional route stop remain intact. Reused
`2026-10-30-pole-compensated-sonin-increment-test.md` and
`2026-10-30-nullvector-arithmetic-slope-discovery.md`, and read only
the matching common-pole ATTEMPTS and history entry. They contain
the relevant duplicate/failure screen. No independent nullvector
estimate or second corrected-increment theorem was identified.

### Primary source scope

[bramble_trace, paper 2 v2](https://rstation.ai/problems/riemann_hypothesis/papers/2),
16 October 2026: read the prime-sum proof and absolute-error refinement,
the complete commutator/covariance proof cases, and the compensated
phase theorem with its support and fixed-test restrictions. These
cover the inputs cited in L526, with their source-proof qualifications.
The arbitrary-Toeplitz scope is explicit, but recognizing the corrected
space as such remains an application obligation. The uncorrected
localization cannot be imported for the corrected weight. The exact
inverse-Gram projection formula and finite-trace subtraction in the
source are templates whose hypotheses must be checked anew. The pole
theorem requires all visible primes for its full-Weil identification;
its fixed-test conclusion supplies no moving-packet uniformity.

The source's reference [11] is
[Camara--Partington, arXiv:1711.04511v2](https://arxiv.org/pdf/1711.04511v2),
Section 2.1, printed pp.2--3. Read the backward-shift definition,
the paragraph proving near invariance of Toeplitz kernels, and
Theorem 2.1. The arXiv header is dated 27 November 2017, though the
PDF title page says 21 June 2021 and paper 2 calls v2 2018. Use the
version identifier, not the latter year. Near invariance alone does
not certify the entire trace-norm estimate: the forward block and
Cayley/Fourier proof cases in paper 2 remain part of the retained
source input. No new commutator theorem was proved here.

### Standard analytic and operator inputs

[Rajesh K. Srivastava, MA650 Advanced Hardy Spaces notes](https://fac.iitg.ac.in/rksri/MA650%20Advanced%20Hardy%20Spaces%20Notes%202022.pdf),
IIT Guwahati, front matter updated 2 May 2026 (the URL's 2022 is not
the inspected revision date): Lemma 8.6(ii), printed pp.119--120,
states the point-evaluation bound for 1<=p<infinity; Theorem 8.8,
p.122, states the H2 upper-half-plane Paley--Wiener representation
with exp(itz) and its norm identity; Theorem 8.18(i), pp.129--130,
states Cauchy representation for 1<p<infinity. Read those statements,
the point-evaluation proof, the short Paley--Wiener proof and its
Fourier convention, and the Hardy boundary discussion. Their p=2
scope covers the standard Hardy tools. Reflection and the change
from normalized Lebesgue measure to dt/(2pi) require explicit
normalization checks. No lower-half-plane conclusion with a contrary
Fourier sign is imported. L526's entire gluing must still justify
local boundary convergence and Morera's theorem on crossing rectangles;
these standard inputs do not prove that its two expressions match.

[DLMF 5.5.3](https://dlmf.nist.gov/5.5.E3) is the gamma reflection
formula, initially away from its integer singularities;
[DLMF 5.11.3](https://dlmf.nist.gov/5.11.E3) gives Stirling in closed
sectors |arg z|<=pi-delta, delta>0;
[DLMF 5.11.9](https://dlmf.nist.gov/5.11.E9) gives the vertical-line
modulus asymptotic. Read the formulas and their stated scopes.
The audit must check sector membership, bounded-height control,
removable singularities and uniformity over the real-part interval
actually used in L526. These formulas do not give its entire glued
function estimate without that application argument.

[Jordan Bell, Trace class operators and Hilbert--Schmidt operators](https://jordanbell.info/LaTeX/mathematics/traceclass/),
18 April 2016, Theorem 18 characterizes trace-class operators as
products of two bounded Hilbert--Schmidt operators; Theorem 23
assumes one trace-class factor and one bounded factor and gives
ideal membership, cyclicity and the trace bound. Read both statements
and the Hilbert--Schmidt-factor proof of the cyclicity assertion.
They permit the finite localized-trace audit once the factors are
proved Hilbert--Schmidt. They do not establish L526's separate trace
finiteness or permit cycling arbitrary bounded operators. Conway,
*A Course in Operator Theory*, Proposition 18.8 p.88 and Theorem
18.11(e) p.89 are Bell's precise book leads, not separately inspected.

### Audit obligations and bounded decision

The rational factor (1+iz)^2, the symbol u_inf b^(-2), and both
inclusions of (5) are local claims. Audit (6)'s exp(C A) bound without
replacing it by a constant. Check (7)--(10) before any trace difference,
including real-line evaluations and the Schwartz-weight integral.
For (11)--(18), retain the absolute O(A/L) prime error, the small-weight
interval J, degree-dependent interpolation constants and the strictly
positive envelope gap. An uncorrected-source theorem is insufficient
for these checks. Elementary Cauchy/Taylor and polynomial estimates
are part of the audit, not newly approved lemmas.

Finally check (19)--(23), both finite traces, G^(-1), all three
covariance regions and (24)'s prime powers, endpoints and common
pole cancellation. Success means a justified o(rL) bound with the
exact -2rL benchmark, retaining external-source qualifications;
failure means an identified error with a concrete repair or downgrade.
No full-Weil identification, nontriviality of the spaces, nullvector
slope sign, family rate or Xi transfer is granted. The source audit
need not resolve these independent downstream gaps. Full Mathlib
coverage is unchecked; no cross-notebook input is used.

The narrow supplementary searches were `Hardy half plane Paley Wiener
theorem Fourier H2 Cauchy representation lecture notes pdf`,
`Toeplitz kernel projection commutator trace norm uniform projection
Hankel finite rank`, `Hardy space upper half plane Paley Wiener theorem
point evaluation author pdf Cauchy`, `trace ideals Hilbert Schmidt
product trace class cyclicity lecture notes pdf theorem`,
`Jordan Bell trace class operators Hilbert Schmidt 2016 theorem 18 23
pdf`, and `Camara Partington Toeplitz kernels model spaces 2017 Section
2.1 arxiv`. Only the inspected passages above support the decision;
unopened results are leads. The manuscript Markdown-download endpoint
was unsupported by the browser, but its HTML exposed all required
passages. A guessed MIT chapter URL was inaccessible and unused;
neither is an essential source blocker. No mathematical script or
lemma was written or modified.
