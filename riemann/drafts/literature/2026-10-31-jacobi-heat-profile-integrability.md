# Jacobi heat derivative: one full-line integrability discriminator

TARGET: Determine whether the complete Jacobi heat derivative profile Q defined in this assessment belongs to L2(R), retaining every modular multiplier and both infinite endpoints.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed exact-object and heat/modular comparison in 2026-10-31-theta-heat-autocorrelation-scope.md; exact auxiliary-lift/elliptic-derivative searches in the local theta records found no completed version of this fixed test. No claim of novelty follows.
SOURCE_EVIDENCE: NIST DLMF v1.2.8 (2026-09-15), https://dlmf.nist.gov/20.1 ; https://dlmf.nist.gov/20.2#E3 ; https://dlmf.nist.gov/20.2#ii ; https://dlmf.nist.gov/20.7#E32 ; https://dlmf.nist.gov/20.13#E1 ; https://dlmf.nist.gov/20.13#E2 ; direct HTML inspected 2026-10-31 for domains, full modular multiplier/transformed argument, analyticity and heat normalization. Reuse parent reading of L019/L239 for their limited actual-k interface.
COMPARISON: The sources supply exact Jacobi identities and fixed-parameter derivatives, but not the L2 property after logarithmic pullback and the notebook's differential operator. The proposed work is their explicit specialization, not a reproof or a new general heat mechanism.
GAP: Calculate both endpoint asymptotics with a controlled full-series remainder; decide the L2 threshold. No profile asymptotic, integrability result, autocorrelation identity or actual-Xi sign is assumed.
REASON: Before using a Jacobi heat derivative as a square-integrable autocorrelation factor, test its exact admissibility independently of the first spectral sign. This is a necessary-condition test of that particular implementation; failure does not stop corrected lifts or weighted cross terms.
SCOPE: Exactly the uncorrected Q below, all real u, elliptic derivative evaluated at z=0, and ordinary Lebesgue L2. No Gaussian regulator, endpoint subtraction, finite theta truncation or sign transfer is preapproved.

Define, for u real and z complex,

B(u,z) = (1/2) exp(u/2) [theta_3(z | i exp(2u))-1],
Q(u) = (2 d^2/du^2 - 1/2) [partial_z^2 B(u,z)|_(z=0)].

These are prospective definitions, not an asserted decomposition.
The elliptic derivative uses the DLMF z convention (cos(2nz));
u derivatives act on the entire bracket. At z=0 the original lift B
uses exactly L019's A. Do not assign actual k's decay/evenness to the
auxiliary derivative without proof.

Essential local inputs are L019 (normalization) and L239 (actual-k
continuation and its limits), with L233 for the downstream first-sign
threshold and signed-term warning. L599 and finite/parity stops are
contrasts only. No cross-notebook input is used. Exact DLMF citations
and reading records are in the completed parent assessment; import
those identities rather than reprove modularity or the heat equation.

For the later test, compute the full modular transform before taking
the negative-u limit. Retain its Gaussian multiplier, transformed
elliptic argument, zero mode and every derivative contribution;
justify local uniform differentiation. Bound the remaining infinite
series and required u derivatives, rather than extrapolate a finite
sum. At positive infinity use the complete direct series with summable
derivative bounds. Inspect both endpoints. No calculation was made
while writing this assessment.

The decisive threshold is integral_R |Q(u)|^2 du < infinity.
An endpoint lower bound proving divergence stops this uncorrected Q
as an ordinary L2 autocorrelation factor. Integrable upper bounds at
both ends permit only that prerequisite. Neither outcome signs the
associated kernel. Divergence does not exclude integrable cross
products with actual k, corrected lifts, distributional identities or
compensated residuals. These are uncovered targets requiring separate
assessment, not automatic repairs licensed here. No numerical scan is
required.

Downstream, a valid square factor could enter a future complete-kernel
decomposition. That identity and an independent compensating residual
bound would still need specification and proof. All higher signs and
unbounded-height RH remain open. Repeating an unsuccessful test requires
a materially changed input, not a renamed heat parameter.

Suggested task: calculation, standard/high. This is ordinary
specialization, not creative research. A protected creative invocation
remains unjustified without a concrete complete residual/sign mechanism.
Separate literature approval completed 2026-10-31 for this unchanged target and scope; direct source URLs repaired. The next invocation may perform the fixed calculation under SPECIALIZE coverage.

Mathlib: full Q integrability and supporting heat/modular derivative
coverage not checked; availability unknown.


## Direct-source recovery and separate approval, 2026-10-31

The recovery issue was missing direct URLs in this ready assessment.
This literature-only review preserves TARGET, definitions and SCOPE.
The parent assessment's search and failure comparisons remain applicable;
no repeated broad survey or new theorem claim is needed.

Inspected primary HTML, with the following exact inputs:

- [20.1](https://dlmf.nist.gov/20.1): Im(tau)>0,
  q=exp(i pi tau); primes differentiate the elliptic argument.
- [20.2.3](https://dlmf.nist.gov/20.2#E3):
  theta_3(z|tau)=1+2 sum_(n>=1) q^(n^2) cos(2nz).
  [20.2(ii)](https://dlmf.nist.gov/20.2#ii) gives entire z dependence
  and analytic tau dependence in the upper half-plane, not at tau=0.
- [20.7.32](https://dlmf.nist.gov/20.7#E32), including the convention
  immediately preceding 20.7.30: tau'=-1/tau, principal square roots,
  (-i tau)^(1/2) theta_3(z|tau)
  =exp(i tau' z^2/pi) theta_3(z tau'|tau').
- [20.13.1-2](https://dlmf.nist.gov/20.13#E1):
  partial_tau theta=-(i pi/4) partial_z^2 theta;
  [20.13.2](https://dlmf.nist.gov/20.13#E2) specifies diffusion
  coefficient pi/4 for tau=i t. This is not an equation in u.

The page footers identify v1.2.8, released 2026-09-15. The optional
TeX endpoint returned unsupported content type; the complete modular
formula and its branch convention were read successfully in HTML.
There is no essential source blocker. No upstream proof is being
reproved: import these standard identities by the precise citations.

SPECIALIZE is approved only for the fixed prospective Q and its
ordinary full-line L2 test. The sources do not assert its pullback
asymptotics, derivative remainder estimates or integrability. Those
are the next mathematical work, including local uniform differentiation
and control at both infinite endpoints. No cancellation, profile parity,
autocorrelation identity or sign follows from this source approval.
The parent assessment retains duplicate and failed-route comparisons;
L599 remains a contrast only. Mathlib coverage remains unchecked.

Outcome: STALLED as mathematical progress; a concrete citation and
approval repair is complete. No new mathematical evidence, lemma,
script or exploration-budget reset is claimed. The main gap and the
saved continuation test are unchanged.
