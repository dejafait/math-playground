# Ready nomination: finite rejection test for the neutral scalar-floor certificate

TARGET: Test whether the fixed first-twelve-mode compression excludes every scalar-floor Schur lower certificate for the exact-neutral first-six cutoff modes at T=4log(3).
CHECKED: 2026-11-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed comparison870 in 2026-11-14-supported-neutral-galerkin-certificate-869.md supplies exact-scope primary searches and local duplicate/failure checks; this nomination adds no search or claim of originality.
SOURCE_EVIDENCE: Direct primary URLs rechecked871: https://arxiv.org/html/2606.09096v2 Theorem1.1/Section3.2; https://arxiv.org/html/2611.13129v1#S8.SS6 Lemma8.16/full proof; https://rstation.ai/problems/riemann_hypothesis/papers/45 v2 Sections4-5; https://www.cis.upenn.edu/~jean/schur-comp.pdf Propositions2.1-2.2/pp3-4; https://arxiv.org/pdf/0903.3639v1 AppendixA LemmaA.1/full proof/printed pp28-29. Reuse assessments804/861 for scalar-floor and validated integration; direct method URLs and applicability below. L744(6)-(8), C750a and L750(8) remain local inputs.
COMPARISON: Full Schur and scalar-floor comparisons are standard. A finite complementary Ritz upper bound and a finite lower covariance compression can test necessary feasibility of that sufficient certificate without assuming a positive infinite complement. Neither the outcome nor the exact local specialization has been established.
GAP: Exact moment/projection coordinates, complete finite full-form entries and their rigorous errors, the rejection implication and a strictly signed certificate remain to be established. Passing this diagnostic supplies no full complementary floor, covariance upper bound, exact Schur sign or Weil positivity.
REASON: Separate literature-only recovery871 repairs missing direct URLs and approves the unchanged finite rejection scope using inspected primary hypotheses and reusable coverage. Ready for one calculation/REPRODUCTION attempt; no mathematical implication or sign has been established here.
SCOPE: Only T=4log3, C750a's unchanged cutoff, first-six retained modes, first-twelve diagnostic modes, both exact moments, complete31-power unshifted form and complex coefficients. No mode/window/shift sweep, positivity premise or Xi transfer.

The completed literature-only comparison is
[assessment869](2026-11-14-supported-neutral-galerkin-certificate-869.md).
This file specifies a question and its intended certificate, not a new
lemma, a proved rejection implication or a numerical result.

## Fixed objects for the later attempt

Use C750a's exact chi at T=4log3 and set
phi_k=chi sin(k*pi*x/T), k=1,...,12. Let U_j be the exact common
kernel of both exponential moments on the complex span of phi_1,...,phi_j,
for j=6,12. Set V=U_6 and Z=U_12 intersect V-perp in the original
L2 metric. The full neutral Hilbert space H is the L2 moment kernel;
W=H intersect V-perp, with the actual supported logarithmic form domain.
Verify all ranks, nonzero spaces, admissibility, exact constraints and
metric factors rather than taking approximate nullspaces as definitions.

The lower-certificate family under investigation is the source's
scalar-floor comparison: independently prove E(w)>=d||w||² on the
whole W form domain for d>0; represent the complete cross map into W
and pay its entire covariance K; then certify A-K/d>=0 on V. Here A
is E's retained Hermitian matrix in an L2 orthonormal basis. This is
a sufficient comparison, not the exact Schur complement with D inverse.
No existence of d or sign of A is presumed.

For this *rejection* preflight use only finite data: the full E matrix
on U_12 and its exact L2 Gram, decomposed as V plus Z. Denote its
orthonormal blocks by A,G,C, where G is the E matrix on Z. The intended
covariance lower compression is K_Z=C C*. Verify the Bessel comparison
with the complete cross map and all conjugations on the full form
domain. Prove representability where needed; do not infer an L2
operator-domain fact merely from finite form norm. C759d Section1 is
a method comparison, not an input for these new functions or constants.

Seek a certified Rayleigh upper bound d_plus on E(z)/||z||² for one
nonzero z in Z, and a certified negative retained direction for the
candidate matrix A-K_Z/d_plus when d_plus>0. The proposed rejection
logic combines the Rayleigh restriction on any valid d, the covariance
lower compression and inverse scalar order; justify it explicitly from
the cited variational/block results during the attempt. If d_plus<=0
is established, treat the absence of a strictly positive floor separately
and respect whether the inequality is strict or zero. Do not call an
approximate eigenvalue an upper bound without its Rayleigh/error proof.

A more economical single retained direction and a few orthogonal Z
vectors may certify the same test if their bounds are enough. They
must remain in this fixed U_12 and keep all full-form terms; no
optimization/basis growth beyond it is licensed. Positive leading
pivots or failed enclosure attempts are not rejection evidence.

## Full entries and stopping conditions

L744(6) is the definition. Both exact moments cancel the pole product;
retain every prime power below81 and the full archimedean contribution.
L750(8) is an already proved smooth difference representation that can
be polarized, with a justified near-zero estimate and the full u>T tail.
Alternatively use the Fourier form with a rigorously paid infinite
frequency tail. Neither a finite frequency grid nor a bounded-frequency
integral alone is a complete entry. Reuse the assessed digamma and real
interval integration methods; every cutoff derivative, flat join,
projection coefficient, quadrature and rounding error must be covered.
Exact integrals define moment ratios and projections, with numerical
enclosures only. Do not assume exponential-cutoff analyticity across
its flat joins. Finite covariance here is a lower bound in a rejection
direction, so no omitted covariance term may be called an upper bound.

Continue this sufficient family only if the bounded diagnostic survives;
even then record the missing infinite floor, full covariance upper
bound and retained Schur sign. A strict certified rejection stops only
the scalar-floor family for V. Exact D inverse or a different split is
not refuted. Overlapping bounds, unresolved entry tails or no rejection
within one coherent attempt are inconclusive: preserve reasoning and
stop without a sweep or invented lemma. No sign result is claimed now.

Essential input IDs: L744, C750a; L750 supplies the existing smooth
kernel and moment construction. C750b, C759d and C998x are comparison
and stop evidence, not positivity premises. No RH, positive complement,
primitive-surjectivity, H2-prime, source-certificate replay, cross-notebook
input or Xi-realization assumption. Full matching Mathlib coverage is
unchecked. A successful local positivity input would still leave other
windows, non-neutral directions, global assembly and L030-L032/C032a open.

Prospective mathematics: calculation, standard/high, REPRODUCTION.
This is a known-method necessary-feasibility test, not creative discovery.
The separate literature approval was completed in recovery871 below.
The next task is the fixed calculation, subject to supervisor routing.


## Separate source-link recovery and scope approval871 — 14 November 2026

LITERATURE_REASON: Supervisor recovery identified missing direct primary URLs in this ready assessment. This turn repairs that evidence field and checks primary hypotheses for the unchanged target; it does not repeat discovery or perform the proposed mathematics.

Reused assessment869's exact-target searches, stronger-window comparison
and duplicate/failure checks, plus the completed805 and862 source reviews
in assessments804 and861. No newly uncovered theorem or stronger support
claim is asserted. The earlier nomination remains preserved above; this
section completes its separate approval.

Opened Suzuki v2 at the direct URL in SOURCE_EVIDENCE and inspected
Theorem1.1 and Section3.2's core/closure argument. This is an operator
realization for arbitrary positive support radius, not a positivity
input. Restricting to the two-moment kernel and checking the new finite
projections remain local obligations; H1 operator domain and logarithmic
form domain must be distinguished.

Opened Andrews–Connes–La Gatta v1, Lemma8.16 and its entire square
completion proof. The result assumes a finite orthogonal form split,
a strictly positive complementary floor and a form-dual cross map.
It supplies conditional Schur theory, not the floor. An L2 covariance
requires the additional representability in the nomination; form-dual
continuity alone does not supply it. Complex finite blocks are covered
by the bounded-operator reference below, subject to local applicability.

Opened Li paper45, displayed v2 dated9November2026, and inspected
(4.1)-(5.5), including the closure passage, square completion, full
Parseval covariance and monotone tail comparison. Its complement and
basis differ from this target. Only the method is reused, not its
constants, support sign or external numerical certificate.

Read Gallier's24August2019 Propositions2.1-2.2 with the congruence proof,
printed pp3-4. The invertible block must be positive for the stated
semidefinite equivalence; invertibility alone does not suffice. Read
Dritschel–Rovnyak v1, AppendixA LemmaA.1 and its full factorization and
partial-isometry proof, printed pp28-29. It concerns bounded operators
on a complex Hilbert space, with positive diagonal blocks and a
contractive factorization. It cannot directly justify an unbounded
Weil cross operator. Neither source establishes this diagnostic's
rejection implication; that specialization is the future attempt.

Numerical methods retain completed862's hypotheses and direct sources:
[Johansson1802.07942v1 Section2](https://arxiv.org/html/1802.07942v1),
[DLMF5.5.2](https://dlmf.nist.gov/5.5.E2),
[DLMF5.11.2](https://dlmf.nist.gov/5.11.E2), and
[DLMF5.11(ii)](https://dlmf.nist.gov/5.11#ii).
Reopened Johansson and DLMF5.11; reused862's detailed integration and
remainder assessment. Real interval enclosures remain permitted;
Gaussian analytic bounds must not cross flat cutoff joins. Reused805's
[Rump2010 Section10.8, Lemma10.12](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf)
only as optional residual verification machinery. No numerical bound,
finite matrix, source computation or mathematical script was produced.

Decision SPECIALIZE is retained for the exact TARGET and SCOPE above.
No change to V, Z, the window, moment constraints, full prime-power form
or stopping test is approved. The finite rejection test is independently
testable without assuming positive infinite-complement coercivity.
Its success, all entry/tail bounds and its local implication are still
unproved. Survival is inconclusive. Full matching Mathlib coverage
remains unchecked. This repairs process evidence, not the RH gap.
