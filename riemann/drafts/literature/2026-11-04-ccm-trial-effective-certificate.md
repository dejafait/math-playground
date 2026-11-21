# Effective certificate for the exact CCM trial — nominated continuation

TARGET: Construct an effective residual-and-tail certificate for CCM's prolate modes 0 and 4 at lambda=sqrt(13), sufficient to enclose all 241 coefficients of P_120 k_lambda without imposing inversion parity.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step367's exact-trial, certified-PSWF, Legendre and a-posteriori searches and local duplicate/failure comparison in drafts/literature/2026-11-04-finite-ccm-trial-comparison.md. No matching complete interval coefficient certificate was identified in the sources inspected; no novelty claim follows.
SOURCE_EVIDENCE: [CCM2511.22755v1](https://arxiv.org/html/2511.22755v1#S7) (7.2),(7.5)-(7.6); [Connes2602.04022v1](https://arxiv.org/html/2602.04022v1#S6.SS3) sections6.3-6.4/(20), footnote20; [Connes--Consani2106.01715v1](https://arxiv.org/html/2106.01715v1#S3) section3/(3.3)-(3.4); [Osipov--Rokhlin1301.1707v1](https://arxiv.org/html/1301.1707v1#S3.SS2) Theorems1,3,10/(53)-(67), Remark9 and section5.1; named self-adjoint spectral theorem and min-max principle. Exact source representation, conventions and qualification record are in the parent assessment; asymptotic estimates are not inputs.
COMPARISON: Known results identify the exact compact trial and infinite symmetric Legendre eigenproblem, including its simple labelled modes. A validated realization must replace the numerical cutoff/iteration recipe by explicit infinite-tail and residual errors and then pay the finite projection. This is a specialization/implementation task, not a fresh prolate asymptotic or claimed ground-state comparison theorem.
GAP: Produce effective mode isolation and L2 errors, zero-integral combination errors and a bound for every projected coefficient; do not assume a prolate tail bound, an inversion symmetry, or a nonzero projected boundary value. No such certificate is established in this assessment.
REASON: The next independently testable missing input is the rigorous trial coefficient budget. Source hypotheses are available; effective constants and enclosures are mathematical work still to be done. The later ground/trial observable cannot be certified by numerical eigenvectors alone. Step368 repaired the missing direct URLs and separately checked the nominated source scope; the exact mathematical target is unchanged and ready for the next invocation.
SCOPE: One fixed lambda=sqrt(13), prolate indices 0 and 4, N=120 projection in the exact translated L759 basis; no parameter sweep, discarded coefficient directions, fitted vector, family theorem or limiting argument.

## Required certificate and applicability

The parent assessment contains direct version-specific primary links,
the exact Legendre matrix and the distinction from the approximate
parity-restricted construction. Import those formulas by citation;
do not rederive prolate spectral theory. Use the compact angular modes,
not full-line band-limited continuations. The additive zero-integral
combination is the saved trial. Either fixed known mode normalization
or an explicitly justified common-scalar convention is acceptable;
independent rescalings cannot silently change its mixing coefficients.

The proposed implementation must specify and prove its finite-to-infinite
certificate before treating any numerical candidate as evidence. It must
identify modes 0 and 4, bound omitted coupling/tails and isolate the
relevant simple eigenvalues of the infinite self-adjoint problem.
Finite Ritz gaps alone are insufficient. The nonnegative bounded
potential and the Legendre diagonal offer standard min-max/tail control;
the actual bounds must be written and checked, not assumed from that
description. The standard spectral theorem supplies residual-to-eigenspace
control only after the required separation is proved. L759's tiny Weil
gap is not a prolate eigenvalue separation.

Specify finite polynomial approximants to the modes, explicit L2 errors
and error propagation through their additive integrals and linear
combination. State a computable error bound for each coefficient
<V_j,k_lambda> with the conjugation and du/u measure of L759, all
-120<=j<=120. The E-sum is finite in this cell; split at its support
breaks and pay quadrature/rounding errors. L2 mode errors can be used
only after proving bounded transport to these coefficient functionals.
No exact inversion symmetry of k_lambda is an input. A normwise
coefficient error bound is acceptable if it bounds every direction.
This paragraph is an output specification, not a proved error formula.

Essential local inputs are L759 (exact projection basis) and L760
(definitions of b and ell and the audited ground comparison input).
The present prerequisite does not need to recompute their matrices or
reduced resolvents. A result, if obtained, belongs in a canonical lemma
with Hypotheses, Conclusion, Proof and Mathlib; it must retain software
trust assumptions for any certificate. Mathlib coverage is unchecked.

## Bounded continuation/abandonment test

Complete one fixed-cell certificate mechanism. Continue if it yields
proved finite-to-infinite mode bounds and explicit errors for the full
projected vector. If mode identification, the omitted block or the
coefficient transport cannot be controlled, retain that exact unpaid
inequality and stop this attempt; tighter floating-point agreement is
not a substitute. No asymptotic-source hunt is necessary for this test.

Downstream purpose: enable the originally saved comparison at z=i/4,
with v=P_120 k_lambda and L760's b,ell,xi. That future test may divide
only after b(v) is enclosed away from zero and must compare
|ell(v)/b(v)-ell(xi)|/max(1,|ell(xi)|) with 1/10. A certified larger
value is negative evidence for that observable; straddling is inconclusive.
This prerequisite asserts neither the denominator nor the comparison.
Full-vector ground/trial errors, family boundary control, both limiting
steps, actual-Xi signs and RH remain unresolved even after success.

## Direct-source recovery check — step368

On 2026-11-04 all four version-specific primary URLs in SOURCE_EVIDENCE
resolved. This is a process repair, not new mathematical evidence or a
new search assessment. Reuse the parent review's exact-statement searches,
duplicate comparison and recorded failed shortcuts; no scope change
requires repeating them. The following selected passages were inspected:

- [CCM section7](https://arxiv.org/html/2511.22755v1#S7): (7.2),
  (7.5)-(7.6), the paragraph defining the zero-integral combination,
  and Lemma7.2's scaling case (7.9). These match the saved trial.
  Its asymptotic constants remain unused; the asserted full Fourier
  invariance is qualified by the compact/compressed formulation below.
- [Connes sections6.3-6.4](https://arxiv.org/html/2602.04022v1#S6.SS3):
  (18), Fact6.3, the angular-mode definition and zero extension,
  restricted Fourier identity, (20) and footnote20. These specify
  lambda>1, dimensionless bandwidth 2pi lambda^2, and the finite sum.
  They do not certify ground/trial agreement or its boundary denominator.
- [Osipov--Rokhlin sections3.1-3.2](https://arxiv.org/html/1301.1707v1#S3.SS2):
  Theorem3's c>0 and continuous-endpoint characterization; (53)-(67),
  the full even/odd alternatives of Theorem10, and Remark9. These
  provide the exact infinite matrix and mode conventions, while the
  truncation recommendation alone supplies no effective omitted-block
  enclosure. No new tail estimate is imported here.
- [Connes--Consani section3](https://arxiv.org/html/2106.01715v1#S3):
  the compact extension and restricted Fourier identity, the
  vanishing-at-zero combination, and the approximate-parity passage
  preceding (3.4). That recipe remains outside the exact saved target.

Decision remains SPECIALIZE. Standard self-adjoint spectral and min-max
theorems are named background inputs, not certificates for this operator:
the future proof must verify their domain and separation hypotheses.
No mathematical derivation, lemma, script, new coefficient error or
Mathlib coverage check was performed. This repair is STALLED with respect
to mathematics and does not renew an exploration budget. Continue with
the exact target and bounded certificate test already stated above.
