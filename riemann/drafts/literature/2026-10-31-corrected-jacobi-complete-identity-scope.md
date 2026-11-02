# Corrected Jacobi profile: completed identity-scope review

TARGET: Assess whether the explicitly corrected profile Q_c(u)=Q(u)+(12/pi)exp(-5u/2) supports a complete Jacobi-heat integration-by-parts decomposition of L233's A(t), retaining all boundary and signed residual terms, and select one bounded identity or residual test.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded corrected-profile, zero-mode, heat/IBP and stronger associated-kernel searches; reused the ready theta-heat and fixed-M comparisons and checked exact local correction/identity terminology. No inspected theorem supplies a complete corrected identity; searches and limits below, without a novelty claim.
SOURCE_EVIDENCE: Reused DLMF v1.2.8 20.2.3/20.2(ii) and rechecked 20.1, 20.7.32 with its preceding branch convention, and 20.13.1-4 in primary HTML; rechecked Csordas arXiv:1309.0055v2, printed pp.11-12, Theorems 4.5-4.6/Open Problem 4.7. Read L019/L233/L600/L601 and the real-axis proof of L239. The Umihara lead below remains unread primary material, not an input.
COMPARISON: The standard Jacobi formulas concern finite lattice parameters and elliptic derivatives; they state no Q_c decomposition of A or signed residual bound. L600/L601 stop only their uncorrected implementations. Associated-kernel admissibility and the historical first-sign question do not fill the identity gap.
GAP: No complete candidate corrected-profile identity or precise independently controlled residual emerged. Q_c admissibility, all endpoint terms, its relation to A and every Xi sign remain unproved; the proposed subtraction is not a theorem application to A.
REASON: The bounded review supplies no qualifying identity/residual discriminator, so park correction-to-identity work under the saved abandonment test. Prepare the materially different actual-k normalized-overlap factor mechanism, with separate source coverage before any mathematics.
SCOPE: Completed literature comparison of exactly Q_c above and the complete L233 kernel; no corrected-profile calculation, lemma, sign transfer or general exclusion of Jacobi methods is approved.
LITERATURE_REASON: The start target was REVIEW_REQUIRED and changes Q; ready uncorrected-profile coverage did not cover a complete corrected identity. This is the required single source-review step, not an additional survey of a ready target.

## Completed review, 2026-10-31

The main gap is actual-Xi all-degree positivity at unbounded heights.
The intermediate target was an exact heat/IBP formula for the complete
first associated kernel with a separately controlled signed residual.
Its possible use is the first spectral sign only. Higher signs and
all-height estimates remain independent. No new formula or estimate
for the correction was derived in this literature-only step.

Reused the full source comparisons in
`2026-10-31-theta-heat-autocorrelation-scope.md`,
`2026-10-31-jacobi-heat-profile-integrability.md`, and
`2026-10-31-jacobi-mixed-correlation-admissibility.md` within their
unchanged scopes. L600 and L601, including their recorded audits,
were read completely. L019 fixes k; L239's real-axis modular/evenness
and decay argument was read; L233 was read completely for normalization
and its signed remainder. The uncorrected stops in ATTEMPTS remain
valid. Targeted correction searches in the Jacobi drafts, assessments,
histories and attempts found this proposal but no completed identity.
The earlier generic weighted-autocorrelation, parity and finite-theta
failures retain the scope recorded in the parent assessment. No
cross-notebook theorem or sibling proof was read.

### Primary statements and applicability limits

[DLMF 20.1](https://dlmf.nist.gov/20.1), v1.2.8, released 2026-09-15,
requires Im(tau)>0 and fixes q=exp(i*pi*tau); primes are elliptic
derivatives. Reuse the prior complete reading of 20.2.3 and 20.2(ii)
for the series and finite-parameter analyticity.
[20.7.32](https://dlmf.nist.gov/20.7#E32), together with the sentence
before 20.7.30, gives tau'=-1/tau, principal square roots, and

    (-i*tau)^(1/2) theta_3(z|tau)
      = exp(i*tau'*z^2/pi) theta_3(z*tau'|tau').

For the proposed parameters, tau=i*exp(2u) is in this domain at every
finite real u. Both multiplier and transformed argument must remain.
This standard identity is imported by citation, without reproof.
It states neither a logarithmic-endpoint boundary value nor a
bilinear identity for A. No differentiation or specialization producing
a new corrected-profile assertion was carried out here.

[DLMF 20.13.1-4](https://dlmf.nist.gov/20.13) gives
partial_tau theta=-(i*pi/4)partial_z^2 theta, diffusion constant pi/4
for tau=i*t, and a periodized Gaussian formula. These are in lattice
time and elliptic position. They give no full-line integration-by-parts
formula involving Q_c and A. Local differentiability is insufficient
to discard an infinite-endpoint term or to sign a residual. There is
no upstream theorem here that needs reproving.

Csordas, *Fourier transforms of positive definite kernels and the
Riemann xi-function*, [arXiv:1309.0055v2](https://arxiv.org/pdf/1309.0055v2),
21 February 2014, printed pp.11-12, Theorems 4.5-4.6 and Open Problem
4.7, was rechecked at the associated-kernel interface. The statements
give admissibility and an all-degree positive-definiteness criterion;
they do not state the corrected decomposition. The first Laguerre sign
is posed separately. Its historical status is not evidence that no
later result exists. No theorem or normalization transfer from that
source is newly applied in this review.

### Bounded searches and an unread lead

Queries actually used included:

- `"Riemann" theta "zero mode" "integration by parts" kernel`;
- `"theta" "12/pi" "autocorrelation"`;
- `"Jacobi" "associated kernel" Riemann`;
- `"Riemann" "theta" "heat equation" "residual"`;
- `"theta" "zero-mode" "Laguerre"`;
- `"Riemann" "autocorrelation" "derivative" kernel theta`;
- `"Riemann xi" "heat" "sum of squares"`;
- `"theta" "corrected" "associated kernel"`;
- `"Jacobi" "corrected profile" theta Riemann`;
- `"theta" "Q_c" "12" Riemann autocorrelation`;
- `"Riemann" "corrected" "Jacobi" "autocorrelation"`.

No inspected primary result supplies the requested identity or an
independent residual comparison. Unrelated PDE/q-Jacobi hits and
unverified proof repositories were not used as mathematical evidence.
This is a bounded negative search result, not a nonexistence theorem.

A secondary index surfaced Hideo Umihara, *A Fourth-Derivative
Inequality for the Riemann Xi Kernel (Letter)*, attributed there to
12 August 2026, DOI `10.5281/zenodo.21902312`. The primary DOI,
`https://zenodo.org/records/21902312`, and its public API endpoint
were attempted and returned access errors through the web tool.
The title/DOI were identified at
`https://globalresearchspace.com/space?star=W7202287933` only.
No theorem number, primary hypotheses, proof or version was retrieved;
none of its advertised curvature, covariance or factorization claims
is imported. It is an optional unread lead, not essential coverage
for the present Jacobi comparison and not a premise of the next target.
Additional exact-title/DOI and overlap-variance searches found no
accessible primary copy. Do not repeat those failed endpoints as a
dependent continuation without new access evidence.

### Decision and independently testable continuation

The saved continuation test required a complete candidate identity or
a precise independent residual claim. Neither emerged. Park this
correction-to-identity proposal; do not perform a replacement norm or
temperedness test merely because a zero mode was specified. This is
not a mathematical refutation of Q_c or a global ban on Jacobi methods.
No new essential dependency was added to the argument, so PROOF and
DAG require no change.

A materially different proposal uses only actual k and the explicit
normalized factor V(t)=A(t)/C_k(2t), rather than an auxiliary elliptic
derivative. This is a definition for a future source review, not an
asserted positive-definite factor. The proposed discriminator is a
fixed fourth-order jet necessary condition for V; its source coverage,
well-definedness and any Schur-product application must be checked
before calculation. The full quotient property is stronger than a
pointwise sign or decrease, and cannot be assumed from either.
No inaccessible Umihara claim is needed to state this proposal.

The sole continuation is recorded in
`2026-10-31-normalized-overlap-factor-source-scope.md` as
REVIEW_REQUIRED. It should compare this stronger actual-k factor
mechanism with recorded shape/finite-test failures and decide whether
the fixed fourth-order jet test is justified.
A failed necessary condition would stop only this factor mechanism;
passing it would be prerequisite evidence, not the full first sign.
Essential coverage is missing, so no creative mathematical attempt is
approved yet. Preparing that mechanism takes precedence over another
uncorrected-profile audit or unspecified correction.

Outcome: EXPLORATION, a completed new source comparison and route
selection, with no new mathematical result or progress beyond the
sources checked. Literature work does not spend or reset the
mathematical exploration budget. Full-result and supporting Mathlib
coverage for the corrected identity remain unchecked, not absent.

## Original nomination, preserved as history of this assessment

The completed step remains the mathematical audit of L601. This new
assessment records a future target only. It does not derive a result
about Q_c, approve a calculation, or perform additional literature work.

Essential inputs for the next review are L019/L239 for actual k,
L233 for the exact first associated kernel and Fourier normalization,
L600 for the exact auxiliary profile and L601 for the audited stop.
Start with the existing heat-autocorrelation source comparison and
the exact-M assessment; preserve their negative evidence. Search
specifically for this correction and complete identities, including
stronger known results and local failures, before reading primary
statements with their full boundary/parameter hypotheses. No new
zero-free result or cross-notebook theorem is proposed.

The correction is a specified change to the failed input, motivated by
the exact zero-mode coefficient in L600, not a claim that removing that
mode proves an identity. Do not spend another research turn merely
testing a norm of the auxiliary profile. The desired downstream use is
a complete representation of A with an independently controllable
signed residual, potentially addressing its actual-Xi first Fourier
sign. All higher signs and unbounded-height uniformity remain separate.

Continue only if source comparison yields a complete candidate identity
or a precise residual target with its input hypotheses and a bounded
discriminator. Otherwise park this correction-to-identity route and
nominate a materially different central mechanism in bounded discovery;
another unspecified correction does not renew exploration. A negative
result for the uncorrected M is not a global ban on Jacobi methods.
No creative proof route is justified until such a mechanism is specified
and its essential literature coverage is ready. Mathlib matching
coverage for the changed target is unknown and has not been checked.
