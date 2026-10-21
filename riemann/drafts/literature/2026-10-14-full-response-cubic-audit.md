# Full-response signed cubic critical audit — completed source coverage

TARGET: Critically audit L409's full-response signed cubic asymptotic, including uniform rational-twist errors, sharp endpoints, zero-carrier resonances and the sequential limits.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step-116 discovery and source exclusions; read full L409, L407 (3)–(9) and audit ranges, L408 hypotheses/(1)–(2)/step-115 audit, L406 hypotheses/(1)–(2)/step-106 audit, and narrow recent cubic histories plus L394/L399/L400 failure records. No completed L409 audit or matching imported full-response theorem was found in these inspected records; no novelty claim.
SOURCE_EVIDENCE: Retrieved Milinovich–Ng author-hosted 19-page manuscript Lemma 6.1 p. 9, https://home.olemiss.edu/~mbmilino/Lower_Bounds.pdf#page=9; retrieved Gonek (1984) §3 Lemmas 1–3 pp. 129–130, especially Lemma 2 and its endpoint/exterior proof, https://www.sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf#page=8; reuse audited L407/L391 coefficients/connectors, L408 fixed-N coefficient and L406 complete absolute physical transfer.
COMPARISON: The explicit single-frequency chi kernel covers the source tool used in L409; response-summed uniform errors, integer resonances, analytic weight variation and H-first passage remain local application checks. No inspected source imports the full cubic statistic. Gonek's correct locator is §3, not §4; the next audit must repair L409's citation.
GAP: No essential source remains inaccessible for this bounded audit. L409 correctness, twist-uniform constants, all summability estimates and sequential-limit quantifiers remain unaudited; clipping, regulator choice, total L367 margin, common-zero upper counts and global mixed positivity remain independent.
REASON: Completed separate coverage comparison authorizes exactly TARGET for a later REPRODUCTION proof_audit; this turn establishes audit readiness and a precise source locator, not the cubic asymptotic's correctness or a new mathematical result.
LITERATURE_REASON: The newly completed L409 proof needs separate audit-scope approval under the gate; reuse ready coverage and inspect only its load-bearing kernel hypotheses and proof cases. Scope approval is complete, so the next turn defaults to mathematics.
SCOPE: Actual ordinary critical jets through order two; complete response with zero/single carriers; every positive rational twist; sharp real-H dyadic endpoints; H tends to infinity first at each fixed N; audited finite-head coefficient and absolute physical transfer. No growing-N rate, clipping, regulator choice, phase independence or RH input.
COVERED_TARGET: Critically audit L409's full-response signed cubic asymptotic, including uniform rational-twist errors, sharp endpoints, zero-carrier resonances and the sequential limits.

## Proposed checks

Essential inputs are L409 and the exact portions of L407 (3)--(9),
L408 (1)--(2), and L406 (1)--(2) that it invokes. Reuse existing
source assessments while their hypotheses match. Inspect the primary
frequency kernel only as needed to settle its uniform constant,
parameter range, complete chi normalization and endpoint convention.
No new discovery or theorem import is claimed by this proposal.

Check L409's coefficient-summed frequency remainder for every r>0:
small/large rH, the endpoint lattice spacing, bounded-variation weights,
and summability of r^(11/20), r^(-49/100), r^(51/100) with all logarithms.
Check both sharp connectors and the full response identity on the
complex rectangle. For zero carrier, keep every integer resonance,
the j=1 case and the near-integer denominator estimate. Verify the
absolute main-sum majorant, beta convergence and H-first quantifiers.
Finally verify the absolute physical transfer without an implicit
clipping or sign assumption.

Continue only if these checks support the stated o(H(log H)^2)
errors and sequential limit. Repair any real mathematical error in
the canonical result; do not infer a clipped mean or RH consequence.
Full matching Mathlib coverage remains unchecked. The proof is a local
known-tool specialization, with no originality assertion beyond the
sources previously inspected.

## Completed scope comparison — 2026-10-14, step 118

The proposal above is preserved as the audit checklist. This comparison
approves its source scope, without performing that mathematical audit.
No lemma, mathematical script, certificate, argument assembly or DAG
was modified. ADVANCE means newly usable local audit coverage, not
progress beyond the inspected source mathematics or a verified L409.

The main gap is global actual-theta mixed positivity. The intermediate
target is exactly TARGET: critically check the complete signed cubic
benchmark. Its plausible downstream use is a reliable input to a later
clipping/sign-imbalance attempt. That use still requires an independently
approved clipped estimate and does not supply a total pencil margin.

### Primary source scope and citation correction

M. B. Milinovich and N. Ng, *Lower bounds for moments of zeta'(rho)*,
[author-hosted manuscript, Lemma 6.1, p. 9](https://home.olemiss.edu/~mbmilino/Lower_Bounds.pdf#page=9),
retrieved 2026-10-14: 19 pages, no reliable printed version date,
placeholder DOI; do not identify it with the seven-page arXiv v1 or
silently substitute published lemma numbering. For x,kappa0>0 it gives

    (1/(2pi i)) integral_(kappa+i)^(kappa+iT)
                    chi(1-s)x^(-s) ds
      =indicator_(0<=x<=T/(2pi)) exp(-2pi i x)
       +O(x^(-kappa)[T^(kappa-1/2)
          +T^(kappa+1/2)/(|T-2pi x|+sqrt(T))]),
    uniformly for kappa0<=kappa<=2.

Read the full remainder, closed indicator convention, proof attribution
and adjoining use (6.4)–(6.5). The analytic lemma invokes Gonek and
Stirling; it has no RH/GRH assumption. The subsequent character-error
estimate uses GRH and is excluded. L409 uses kappa=21/20, x=j/r,
not an imported coefficient-summed error from that conditional argument.

S. M. Gonek, *Mean values of the Riemann zeta-function and its
derivatives*, Invent. Math. **75** (1984), 123–141,
[§3, Lemma 2, p. 130](https://www.sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf#page=8).
Read §3's heading and Lemma 1 on p. 129, Lemma 2's statement and
proof, and the weighted Lemma 3 on p. 130. The hypotheses are large A,
A<B<=2A and fixed exponent a; the saddle parameter is positive.
Lemma 2 separates the interior saddle, endpoint transition neighborhoods
of square-root width and exterior cases. Its proof uses stationary
phase centrally and integration by parts outside, retaining both
endpoint denominators. This supports the explicit frequency remainder,
rather than a fixed integer-grid summation constant. Independence from
the notebook twist must still be checked through these cases during
the audit. No new stationary-phase reproof is requested.

The existing §4 locator in L409 and the prior passage assessment is
incorrect: the scan labels this material §3. The lemma number, page
and mathematical source are identifiable. Record the correction here;
repair the canonical citation during the next research audit. This
bibliographic finding does not decide any mathematical error.

### Reused coverage, exclusions and application obligations

Reuse the step-116 search terms and inspected comparisons in
`drafts/literature/2026-10-14-full-response-cubic-passage.md`.
There is no changed mathematical target requiring a new broad search.
The tempting unproved twisted-third-moment import, smooth Voronoi
formula without sharp infinite-response control and larger absolute
cubic envelope do not replace L409's claimed signed-tail argument.
The L394/L399/L400 failures concern different weights, are preserved,
and neither establish nor forbid the present audit. Narrow local
searches found only the newly completed L409 and its explicit audit
deferral, not a completed duplicate audit.

L407 (3)–(9) and its step-111 audit provide the exact carrier pairing,
ordinary coefficients including j=1, analytic weight derivative bounds,
complete chi normalization and sharp connector tools from L391.
Their finite-twist bounds do not themselves assert N-uniform errors.
L408 (1)–(2) and its step-115 audit provide beta_N at fixed N, including
coalesced Hurwitz poles, principal-log sectors and absolute boundary
limits. Its finite algebra need not be rerun. L406 (1)–(2) and its
step-106 audit provide the complete physical transfer with full ordinary
response derivatives and curvature; the exponent is 5/4, below 2.
Ready assessments of these inputs remain within scope and are reused.

The difference requiring local verification is the full-response
application. Check L409 (9)–(14) at both endpoints for all r>0,
including empty small-rH bands, a saddle at an endpoint, large rH and
the rational-grid spacing. Verify the three claimed powers of r with
their logarithms, Stieltjes weight terms and constants independent of
r,N,H,V. Check normal convergence on a neighborhood of the full
rectangle and both oriented connector sums, with the actual holomorphic
response continuation. These are proof obligations, not additional
source conclusions imported by this assessment.

Check every zero-carrier integer resonance in (17)–(19), j=1 and the
near-integer denominator bound, then the claimed O(H) total. Check
the complete main-term majorant (15)–(16), the absolute tail inequality
(21), beta convergence and H-first quantifiers. Verify that L406's
absolute replacement transfers the complete physical statistic without
a division at zeros or a hidden clipping/sign assumption.

Accept the application only if all errors are o(H(log H)^2), the
signed-tail double limit vanishes and beta is finite and positive with
the printed hypotheses. Repair any real mathematical defect in the
canonical result during the research audit; a citation typo alone need
not invalidate the existing coefficient. If a necessary twist factor
is nonsummable, a resonance/endpoint exceeds the scale, or an essential
tool falls outside this assessed scope, preserve the precise failed
bound and park that dependent certificate. Any genuinely uncovered
replacement target requires separate REVIEW_REQUIRED coverage.

Essential continuation inputs are L409, audited L407 (3)–(9), L408
(1)–(2), L406 (1)–(2), and inherited L391 connector/jet tools plus
the cited kernels. Unresolved assumptions are the correctness of
L409's uniform summation and limit passage, clipping, regulator choice,
total L367 margin/remainder, actual common-zero upper counts and global
mixed positivity. No RH or phase independence is assumed. Full matching
Mathlib coverage is unchecked; no formal verification or absence is
asserted. The next invocation is the separate mathematical proof audit.
