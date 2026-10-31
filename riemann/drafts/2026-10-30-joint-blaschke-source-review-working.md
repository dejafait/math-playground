# Joint local zero extraction: source review working note

Literature-only step, 30 October 2026. No lemma or mathematical script
is being changed. Target and normalization are those in the supplied
joint-Blaschke assessment; L471, L474 and C483a match the one-copy
quotient, full multiplicities and clipped-window convention.

L474 Section 3 and L475 Section 2 already divide by all selected pair
factors, retaining the other copies. A changed mechanism must use
additional zeros (including real Xi zeros or pairs outside the selected
band) and control sparse neighborhoods. L475's audited exp(7u)/(7u^4)
envelope remains the comparison stop; its polynomial is a local-tool
test, not an actual-Xi counterexample. The aggregate recovery stop is
procedural, not a global prohibition.

Primary Broughan II Theorem 3.3 and Bettin v1 Theorem 1 are accessible.
The exact finite and central-zero factorization cases and the stated
real-shift restriction are being inspected. A new relevant primary lead
is Maples--Rodgers, arXiv:1404.3080v2, Theorem 1.2 and Proposition 2.5:
unconditional mesoscopic counts and local density moments. Theorem 1.2
counts ordinates with multiplicity at uniform heights, not disk zeros
weighted by pair-divided norms; n(T) must tend to infinity. No transfer,
sparse weighted bound or fixed-scale conclusion is inferred. Exact
Proposition 2.5 hypotheses/proof and neighboring tools remain to read.

Provisional decision: the whole mesoscopic little-o bound is not yet
covered. Complete the primary comparison before choosing readiness or
an independently testable narrower continuation. Mathlib matching is
unchecked. No mathematical calculation has been carried out.

## Completed evidence and precise source scope

Primary links inspected on 2026-10-30:

- Broughan II (2017), Theorem 3.3, proof (1),(4), printed pp. 26--27:
  https://api.pageplace.de/preview/DT0400.9781108195430_A31720577/preview-9781108195430_A31720577.pdf#page=48.
  For a holomorphic disk function bounded by M, finite Blaschke division
  at its zeros preserves the bound M. Repeated zeros repeat factors;
  central zeros use powers and Schwarz's lemma. Xi is entire, so compact
  local disks meet the regularity requirements. Only the finite case is
  needed. It permits extra real zeros, but gives no assertion that they
  occur in enough selected disks and no arithmetic sum estimate.
- Bettin, arXiv:1111.0925v1, Theorem 1, printed p. 2:
  https://arxiv.org/pdf/1111.0925v1#page=2.
  The real parts of both shifts are O(1/log T); large imaginary shifts
  do not remove that restriction. At coincident shifts the two main
  terms have a joint pointwise limit. Reuse the small-shift proof case
  already assessed in the scale-adapted review; do not enlarge its
  real-shift range to the full mesoscopic radii.
- Maples--Rodgers, *Bootstrapped zero density estimates and a central
  limit theorem for the zeros of the zeta function*, IJNT 11 (2015),
  2087--2107, arXiv:1404.3080v2 (4 June 2016):
  https://arxiv.org/html/1404.3080v2 and
  https://arxiv.org/pdf/1404.3080v2.
  Read Theorem 1.2, Theorem 2.4, Proposition 2.5, definition (8),
  Corollaries 4.1--4.2 and their complete proofs, and (18)--(23)
  with Lemma 4.3 and its complete bootstrap proof. No arithmetic
  proof of Fujii/Selberg/Jutila was independently audited.

The last source's Proposition 2.5 states, with multiplicities and
N(sigma,U) counting beta>sigma and 0<gamma_0<U,

    (1/T) integral_0^T |N(sigma,t+H/log T)-N(sigma,t)|^k dt
      <<_(c,k) H^k T^(-c(sigma-1/2)),

for integers k>=1, 1<=H<=T^(1/4), fixed 0<c<1/2. Our proposed
use is restricted to 1/2<=sigma<=1. The underlying Theorem 2.4
states N(sigma,U)<<_b U log U * U^(-b(sigma-1/2)) for fixed
0<b<1. Corollary 4.2 bounds count moments for test functions under
a macroscopic weight with finite Q-norm, where Q(x)=1/[pi(1+x^2)],
with both its local step-majorant norm and far-tail error retained.
The source's Gaussian theorem is not required for this restricted
bootstrap. Its Section 4 uses two Holder inequalities, a convolution
bound and unweighted count moments; it supplies no |Z| or quotient
weight. These are known statements, not new notebook results.

### Audit questions found by reading the primary proof

Equation (8) defines A_gamma by beta_0=1/2+A_gamma/log T.
The printed line immediately after (23), p. 12, instead names an
indicator cutoff sigma-1/2 in the A_gamma variable. Its displayed
indicator/Cauchy-kernel comparison also requires checking its
normalization and constants against the earlier definition of Q.
Both features occur in the PDF as well as the HTML. The passage
(18) to (19) asserts a bound for general piecewise-continuous f;
its hypotheses must not be treated as an automatic weighted-density
input. Only upper-tail indicators are proposed for audit. No repair,
counterexample or new bound is derived in this literature turn.

### Bounded discovery and comparison

Queries: `Riemann zeta zeros Blaschke product local zero density sparse
intervals mean square`; `zeta function small gaps zeros local moments
Blaschke factors near zeros`; `Fujii Selberg moments S(t+h)-S(t)
unconditional log h log T theorem`; `zeta zeros short intervals sparse
intervals Selberg moment N(t+h)-N(t) unconditional`; `Rodgers mesoscopic
central limit theorem zeta zeros unconditional Theorem 1.1`; `zeta
Blaschke sparse`; and exact Proposition 2.5/erratum searches. No erratum
was identified in the latter bounded searches; this is not evidence of
its absence. Uninspected conditional gap/ratio and Nevanlinna-class
leads are not used. The primary unconditional source above was followed
rather than treating snippets or the older RH-conditional Rodgers
paper as adequate evidence.

Local duplicate/failure reads: L471 definitions and kernel setup;
L474 full proof through Section 5; L475 full proof and audit; C483a
through its uniform density comparison; the scale-adapted assessment
and its ATTEMPTS record; the aggregate procedural stop; the prior
zero-conditioned source assessment. Exact Maples--Rodgers/1404.3080
searches in drafts/literature, foundations, ATTEMPTS and history found
no earlier local assessment. No cross-notebook theorem was used.

Decision: park whole-sector joint suppression for missing weighted
sparse control, and nominate one conceptual audit of the concrete
count-only source input. Stop that audit if it cannot obtain the stated
uniform indicator result from the named inputs without an extra density
or weight premise. If it passes, a later independently approved kernel
application can compare its actual scale with T(log T)^3. Fixed-scale
annuli and conversion to pointwise/all-degree signs remain open even
then. Mathlib coverage has not been checked; no absence claim.

Direct filesystem downloads failed with network DNS restrictions;
primary browser text was accessible and supplied the complete relevant
passages, so this is not a source-access blocker. No source binary was
saved. No lemma, calculation certificate or mathematical script was made.
