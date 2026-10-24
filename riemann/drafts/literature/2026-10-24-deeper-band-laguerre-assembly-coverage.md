# Coverage: deeper-band conditional Laguerre assembly

TARGET: Assemble L459 and audited L460 on 13/16≤m/r≤7/8 into a conditional coupled Laguerre sign with exact positive normalization, complete relative error and one uniform onset.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-band arithmetic and theta discovery/comparison assessments and their critical-audit coverage; compared L459/L460 statements and final audit passages with C458a's assembly and audit, the narrower assembly assessment, the October overlap/input register and L323/L327 failure records. No fresh external search or exhaustive duplicate claim.
SOURCE_EVIDENCE: Reused inspected DLMF 2.4.10–2.4.16 and Temme arXiv:1308.1547v1 Sections 2.2–2.3 and 4.1; Csordas arXiv:1309.0055v2 Lemma 3.6 and Theorem 3.7 (3.10)–(3.14), DLMF 2.3.21–2.3.23 and 7.2.6–7.2.9; Titchmarsh–Heath-Brown (1986) Theorem 14.2 and Section 14.3, pp. 336–339, through existing assessments; the pinned September 30 Theorem 1.1 through the register. No primary page was newly fetched or external proof verified.
COMPARISON: Audited L459/L460 have identical real-r/even-m closed-band domains, exact h,a and full finite signed S. Sources cover their mechanisms, not this combined inequality. C458a supplies the same assembly method on a narrower band with exponent 2/3; its conclusion cannot be imported here, where the stated scale exponent is 15/16.
GAP: Apply the two audited statements with the exact P and factorial-normalized M*, comparing the entire additive theta error to the lower scale and arithmetic relative error with one uniform onset. This literature review establishes no combined inequality or sign.
REASON: The separate exact-scope comparison finds adequate essential coverage for one REPRODUCTION application. No new saddle, sector theorem, external-premise audit or general error theorem is required; the changed-scale quantitative application still needs its own proof.
SCOPE: Positive real r tending to infinity, positive even m with 13/16≤m/r≤7/8, L459's exact a,S,M* and L460's exact positive P; conditional coupled assembly only, with no every-height transfer or external-premise audit.
LITERATURE_REASON: The saved assembly nomination was outside the preceding audit-only scopes; compare this precise new application using ready source coverage, without repeating browsing for unchanged hypotheses.

## Original nomination, preserved

The following nomination described the uncovered state at invocation
start. Its review requirement is discharged by the comparison below;
the newly ready continuation receives separate approval next turn.

The main gap remains initial low-index signs and global mixed positivity.
The proposed intermediate result is a conditional sign on this coupled
band. Its plausible downstream use is a later, separately assessed
every-height transfer. Neither step would complete the initial indices,
bounded exterior heights, mixed positivity or selected-law/regulator
realization obligations.

Reuse the [arithmetic coverage](2026-10-24-deeper-band-moving-saddle-coverage.md),
its [critical-audit coverage](2026-10-24-deeper-band-moving-saddle-critical-audit-coverage.md),
the [theta coverage](2026-10-24-deeper-band-whole-plane-theta-coverage.md)
and its [critical-audit coverage](2026-10-24-deeper-band-theta-critical-audit-coverage.md).
The [earlier assembly assessment](2026-10-24-lower-band-laguerre-assembly-coverage.md)
is the narrow comparison to inspect before approving this changed band.
No renewed broad source search is requested merely to repeat ready work.

Essential inputs are L459 and audited L460. Preserve the complete signed
S, including zero weight at product-cutoff equality, the exact a and h,
the positive factorial-normalized M*, and P with m! and one reflection.
The required comparison must retain the whole O((1+r)^2 exp(-r/200))
additive error and L459's |log M*|<=C r^(15/16) lower-scale control,
as well as its O((log r)^3/sqrt(r)) relative arithmetic error. These are
existing input statements, not a completed assembly. Continue only if
the whole theta error is subordinate to the desired arithmetic relative
scale with one onset; otherwise isolate the unmatched hypothesis or
failed error comparison.

Any application retains OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re s > 7/8*, September 30, 2026, Theorem 1.1 at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`, exactly as in L459:
strict Re(s)>7/8, pole at 1 allowed, external manuscript and formal
import closure not independently audited locally. No boundary exclusion
or full RH is assumed or concluded. Full and supporting Mathlib coverage
remain unchecked. L323 and L327's recorded obstructions keep their
stated scopes; no unsigned-sum replacement is proposed.

## Completed separate source comparison — 2026-10-24

This step is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. It adds
exact-scope coverage, not a mathematical input or progress beyond the
sources checked. No lemma, mathematical script, DAG or main argument
is changed. Mathematical exploration usage remains 0 of 3.

### Reused primary evidence and limitations

The arithmetic construction and audit assessments linked above record
[DLMF 2.4(iii)–(iv)](https://dlmf.nist.gov/2.4#iii), (2.4.10)–(2.4.16):
analytic phase/amplitude neighborhoods, convergent endpoint expansions,
absolute uniform far-end convergence and a strict phase gap. The
interior case splits into two half-paths and selects the Gaussian root
by direction. [Temme, arXiv:1308.1547v1, 7 August 2013](https://arxiv.org/html/1308.1547v1),
Sections 2.2–2.3, (2.9)–(2.13), and 4.1, (4.1)–(4.5), requires
analytic contour neighborhoods and convergence; additional parameters
may change uniformity, and nearby poles require separate treatment.
Neither gives the paired-zeta margin directly. L459's audited explicit
estimates supply that input, including both residues and all tails.

The theta construction and audit assessments record Csordas,
[*Fourier transforms of positive definite kernels and the Riemann
ξ-Function*, arXiv:1309.0055v2, 21 February 2014](https://arxiv.org/html/1309.0055v2),
Definition 1.2, Theorem 3.5, Lemma 3.6 and Theorem 3.7,
(3.10)–(3.14). Smooth positive even decreasing kernels with the stated
super-Gaussian derivative decay are required; Theorem 3.5 additionally
uses strict logarithmic concavity and separates the two admissibility
cases. The coefficient identity retains its Jacobian and factorial.
All-level positive definiteness remains a premise, not a consequence.
[DLMF 2.3(iv)](https://dlmf.nist.gov/2.3#iv), hypotheses (a)–(d),
(2.3.21)–(2.3.23), requires smooth phase/amplitude, nonzero phase
derivative away from the stationary endpoint, differentiable endpoint
expansions and controlled endpoint limits or uniform convergence.
Both finite endpoints contribute. [DLMF 7.2(iii)](https://dlmf.nist.gov/7.2#iii),
(7.2.6)–(7.2.9), supplies scalar Fresnel limits. These sources do not
give moving-domain uniform error bounds; the audited L460 does.

Reuse the saved Littlewood assessment named in the arithmetic coverage:
Titchmarsh–Heath-Brown, second edition (1986), Theorem 14.2 and proof,
pp. 336–337, and Section 14.3, pp. 338–339. Its printed RH hypothesis
is not silently removed. Only the assessed analytic-logarithm,
Borel–Caratheodory, three-circles and Cauchy mechanisms are used in
the local specialization. The external-input register retains the
precise pinned Theorem 1.1 premise above. This review neither rereads
nor verifies the external manuscript/import closure. The pole at one,
strict boundary and lack of an Euler reciprocal expansion below one
remain essential qualifications.

Prior exact-sum and changed-band queries are reused from the linked
assessments. The theta assessment also screened rStation paper 41 v3,
23 October 2026, Theorems 1/1a/3/4 and Section 4.1: its pointwise
range is higher and its lower-order conclusions allow exceptional
heights. It was not imported. Olver/de Bruijn, Flajolet–Sedgewick and
Olver/Lyness remain nonessential unread leads. No fresh source is needed
for this elementary application of the two already audited statements.

### Exact interface, duplicates and failures

Read L459's Hypotheses/Conclusion, Section 6, final audit and Mathlib;
L460's Hypotheses/Conclusion, Section 4, final audit and Mathlib; and
C458a's hypotheses, assembly proof and separate audit. This is an
interface review, not another correctness audit of either input.
L459 and L460 both quantify over positive real r and positive even m
with 13/16≤m/r≤7/8. They use h=9/2+m/(2r), the same positive
square root for a and identical weight/phase in S, zero at cutoff
equality. Both conclusions have constants independent of the pair and
one onset on the entire closed band.

L459 states M*>0, |log M*|≤K r^(15/16) and relative arithmetic error
O((log r)^3/sqrt(r)); its M* includes A=m!/(2r)^m, N=m+1 and
the positive sqrt(2πλ). L460 states D=P(S+ε), with real ε bounded
by C(1+r)^2 exp(-r/200). Its P=[2^(m−1)/m!]C₀exp(Φ_*)π/a
is positive and already includes one reflection. These are input
statements, not an assembled inequality proved in this review.

C458a covers 7/8≤m/r≤31/32 with scale exponent 2/3. It supplies
an audited method template but no theorem on the deeper band except
their shared endpoint. C455a uses a still narrower, different band and
a fixed-center square. L459 is arithmetic-only; L460 is additive-only.
No matching combined theorem was identified by the reused bounded
searches; this is neither exhaustive absence nor a novelty assertion.

The inspected L323 r/4-strip failure and L327 balanced-AFE/PSD failure
keep their scopes. L460 uses the smaller-strip estimates and retains
the actual signed S, so neither failed implementation is reopened.
L456's fixed-center certificate is not retried: the proposed assembly
uses M*, without asserting fixed-center relative freezing. Fixed-r or
arbitrary-unit-phase failures do not refute the coupled conclusion.

### One bounded continuation and decision test

SPECIALIZE covers exactly one REPRODUCTION assembly attempt at the
unchanged TARGET. Use L459 and L460 as inputs, without reproving their
saddle/sector results or extending their domains. Write the full
elementary comparison of the stated additive error to M* and to the
arithmetic relative-error scale, retaining the changed exponent 15/16.
Choose one maximum of all required real-r thresholds; do not claim
an effective numerical onset. Preserve P and M* exactly, including
their separate factorials and the single reflection.

Continue only if that complete comparison proves the requested uniform
relative estimate and a positive normalized lower margin throughout
the closed band. If any domain, normalization or error comparison
fails, isolate that defect and repair or abandon this application;
a local main term is insufficient. No such combined estimate is proved
here. A successful construction still needs separate critical review.

Essential continuation inputs are L459 and audited L460, with L459's
unchanged pinned external premise and unaudited manuscript/import
closure. A later separately assessed every-height transfer is the
plausible downstream use. Initial low-index signs, bounded heights,
global mixed positivity and selected-law/regulator realization remain
independent gaps. Full matching and supporting Mathlib coverage is
unchecked, not asserted absent. No RH candidate or new sign is claimed.
