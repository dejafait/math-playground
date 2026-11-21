# Compact-core branch-transport compatibility — reviewed1267

TARGET: Assess the compact-core branch-transport compatibility test at omega=1/4 and z=i: whether a nonzero complex f in C_c^infinity(0,infinity) can satisfy G_{sigma,-}f=c G_{sigma,+}f for every u>=0 and both branches, with Psi(s)=Phi(s/2) and c=Xi(3i/4)/Xi(5i/4), independently of Green contraction.
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Exact Volterra/Xi joint-Gram and theta compact-support injectivity searches, followed by analytic-Hankel, convolution and Laplace uniqueness searches, found no inspected theorem deciding this equation; primary comparisons and local duplicate/failure checks are recorded below. No novelty claim.
SOURCE_EVIDENCE: Freedman arXiv2606.29555v1 (28 June 2026), Section 3 (1), Appendix C.1 Hardy vectors/common-U/four-Gram passages and continuous branch features, Appendix D.1 Psi convention; Ransford arXiv2011.05420v1 Theorem 1.1, Lemma 2.1 and Sections 3–5 proof; Liehr DOI10.1112/blms.13134 Section 3 Theorem 3.1 and Corollary 3.2/full proof; DLMF 1.14(i) Uniqueness and 1.14(iii) (17)–(20), convergence and uniqueness. Reading limits below.
COMPARISON: A complex-linear common isometry preserves the displayed Hardy scalar dependence; the fixed equation screens an added compact-profile exact realization only. Classical transform uniqueness covers complex inputs, but its reduction from this weighted sum-kernel integral is unpaid. Titchmarsh's lower-support conclusion does not directly decide vanishing on u>=0 here.
GAP: Existence/nonexistence for arbitrary complex compact f remains unproved. An analytic-continuation/convolution or Laplace reduction must verify every domain, decay, interchange and nontrivial-transform hypothesis; no such reduction is established in this literature turn. Completed range, quantitative approximation and RH positivity remain separate.
REASON: Essential source comparison is now sufficient for one bounded exact compact-profile attempt. Reuse the checked uniqueness results if their hypotheses can be verified; do not reprove them or import source numerical fits as theorems. Keep the Green-mass route parked.
SCOPE: Fixed omega=1/4, z=i, full Phi with the normalization below, complex f in C_c^infinity(0,infinity), both sigma and every u>=0, exactly the nominated scalar c. Standard transform uniqueness and theta modular continuation may be used only with explicit applicability proofs; no generalized parameter theorem, completed-domain obstruction or positivity construction is approved.
COVERED_TARGET: Attempt to decide whether a nonzero complex f in C_c^infinity(0,infinity) satisfies G_{sigma,-}f=c G_{sigma,+}f for every u>=0 and sigma=+/-1 at omega=1/4, with Psi(s)=Phi(s/2) and c=Xi(3i/4)/Xi(5i/4), using justified analytic continuation and transform uniqueness.
LITERATURE_REASON: The startup REVIEW_REQUIRED target changes the earlier Green-mass mechanism to exact common-branch compatibility. Its essential primary feature and complex-transform hypotheses required this one review; further browsing is not needed for the covered bounded attempt.

## Completed source comparison — step1267

The main gap remains L030-L032/C032a actual-Xi positivity in every
degree. The intermediate target is the exact equation in TARGET.
Its use is to accept or reject one compact exact branch realization,
before spending work on a transport construction. It supplies no sign.
The continuation test is a proof for arbitrary complex f, or a rigorously
verified nonzero example. Failure of the analytic reduction must be
recorded as unfinished reasoning, not inferred nonexistence. A finite
fit, nonnegative-f argument or tail asymptotic without cancellation
control does not meet this test. An example in a common nullspace
would satisfy the equation but would not realize a nonzero Hardy vector.

### Source conventions and scope

Read [Freedman, *Finite-core Volterra reductions for a Weyl-positive
Riemann phase kernel*, arXiv:2606.29555v1, Appendix C.1](https://arxiv.org/html/2606.29555v1#A3.SS1):
the Hardy features, common isometry, four joint Grams, continuous
g features and ensuing coupled-system/coarea/nonlocal tests. Also
checked Section 3 (1) and D.1's Psi convention. The Hardy pair is
h_z^+=(2pi)^(-1/2)Xi(z+i omega)exp(izr),
h_z^-=(2pi)^(-1/2)Xi(z-i omega)exp(izr).
The continuous features contain
sqrt(w_sigma/4)(1+/-r)exp(sigma omega r/2)Psi(s+u)/Psi(s), r=s+u.
The isometry and completed trace realization are proposed bridge
conditions; compact scalar preimages are an additional restriction.
Reported finite fits do not decide the compact exact question.

For the local normalization, the displayed source Phi is K/2, with
K exactly L019. Thus its even Fourier integral matches L020's Xi.
Use full Phi, not the corrected three-mode kernel used elsewhere in
the source. This comparison does not identify those two models.
L018 applies directly at Xi(5i/4)=xi(-3/4) and
Xi(3i/4)=xi(-1/4): both arguments of xi are outside the open
critical strip, where L018 establishes nonvanishing. Hence c is defined
without an RH assumption. L019 supplies the positive denominator
Psi(s) on the positive real axis. These are normalization and
hypothesis checks using existing results, not new sign lemmas.

At the fixed point, the displayed Hardy definitions give the nominated
ratio h_i^-=c h_i^+. A *complex-linear* common isometry must preserve
this dependence. Comparing it with simultaneous images of a single
scalar f gives the proposed equation. Positive constant branch factors
sqrt(w_sigma/4), when present in both signs, cancel. This is a necessary
condition for that restricted realization, not a condition imposed on
all possible Weyl/KLM pullbacks. In particular, no assumption that an
evaluation minimizer actually belongs to C_c^infinity is imported.

### Transform results actually inspected

1. [NIST DLMF, Section 1.14(i), Uniqueness](https://dlmf.nist.gov/1.14.i)
states Fourier uniqueness for continuous absolutely integrable functions
on R whose transforms agree for all real frequencies. Section
[1.14(iii)](https://dlmf.nist.gov/1.14.iii), (17)–(20) and Uniqueness,
allows complex functions; its running hypotheses include piecewise
continuity and an exponential growth bound, with Re(s) beyond that
bound. The uniqueness statement adds continuity; inversion (20) also
requires piecewise continuous derivative. These exact hypotheses were
read, not just a search snippet. They concern actual Fourier/Laplace
transforms, not every integral with a decaying kernel.

2. [Lukas Liehr, *Arithmetic progressions and holomorphic phase
retrieval*, Bulletin of the London Mathematical Society 56 (2024),
DOI 10.1112/blms.13134, Section 3](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.13134):
read the complex L1(R_+) transform definition, Theorem 3.1,
Corollary 3.2 and its full proof. For distinct positive sampling points
u_j with sum 1/u_j divergent, Corollary 3.2 gives Laplace uniqueness.
Its proof bounds the holomorphic transform by the L1 norm, uses
classical uniqueness to exclude an identically zero transform for
nonzero input, and applies the bounded-holomorphic zero condition in
Theorem 3.1. No nonnegative-input restriction is present. This supplies
no automatic replacement of the theta sum-kernel by a Laplace kernel;
such a replacement and its integrability remain proof obligations.

3. [Thomas Ransford, *A short complex-variable proof of the Titchmarsh
convolution theorem*, arXiv:2011.05420v1 (4 November 2020),
Theorem 1.1](https://arxiv.org/html/2011.05420v1): for complex L1(R)
functions with finite lower support endpoints, the lower endpoint of
their convolution is the sum of the endpoints. Read Lemma 2.1 and
the proof through Sections 3–5, including both directions of Corollary
4.2. The proof handles cancellation using canonical factorization,
not a positivity estimate. This theorem cannot be substituted for an
unproved claim that vanishing of the proposed profiles on a right
half-line forces f=0: the direction of support, kernel support and
convolution representation must first match its hypotheses. No
Titchmarsh theorem is imported as a solution of TARGET.

The original 1926 Titchmarsh publisher record was located; the original
paper was not read. Ransford supplies the inspected primary modern
proof. Generic Hankel-kernel/inner-function and unrelated theta-lift
search hits were not read or used as theorem inputs. DLMF's cited
Schiff book and the Pólya–Szegö reference were not read; no claim based
on their additional content is made.

### Search, overlap and bounded continuation

Queries included `theta compact support Hankel injectivity`,
`Laplace transform uniqueness complex measures compact support theorem`,
`Titchmarsh 1926 zeros integral functions convolution theorem support`,
`Volterra branch 2606.29555`, `analytic Hankel compactly supported injective`,
`convolution real analytic compact support injectivity`,
`theta kernel injectivity transform` and `Volterra Xi joint Gram`.
The bounded search found supporting classical results, not an inspected
matching theorem for the full weighted equation. It establishes no
novelty. A source supplying the exact theta range theorem would replace
the corresponding calculation with citation and applicability checks.

Local duplicate/failure searches were confined to the named October31
construction files and November17 branch/Green reviews and stops.
Read the October31 assessment's three primary comparisons and its
ATTEMPTS stop, review1265's normalization/mass limits and continuation,
and full C032d. No inspected local proof decides TARGET. C032d refutes
an abstract compression inference, not this theta equation. The older
conditional/shifted-construction stop supplies no compact range theorem.
No source numerical-fit claim is upgraded to an exact obstruction.

The ready continuation is one analytic compatibility attempt, not a
new positive representation: verify a transform reduction on the stated
compact class, including any continuation through the origin, all
uniform convergence and convolution identities, and nonvanishing needed
to apply the checked uniqueness statements. L016's modular identity,
L018's Xi conventions, L019's kernel and L020's integral are essential
local inputs; C032d is contrast only. No injectivity theorem for this
theta map has been proved in this review. Any new source dependency
outside this assessed scope needs a separate review.

Nonexistence would stop only the compact exact ansatz. It would give
neither a lower bound on approximate defects nor a contradiction to
completed noncompact transports, nonisometric pullbacks or closed-cone
limits. Existence would still leave plus-profile nonvanishing, norm
matching, other evaluation points, traces and completion unverified.
The Green-mass route remains parked; actual-Xi signing, realization,
initialization and the Weyl/RH bridge remain open.

Outcome EXPLORATION: essential source comparison completed and a bounded
test is ready, but no new mathematical result or progress beyond the
checked sources is claimed. This turn spends zero mathematical attempts
and resets no supervisor counter. Full and supporting Mathlib coverage
for the branch test/uniqueness argument is unchecked. L016 retains its
previous supporting references; there is no new formal verification.
No cross-notebook input, lemma, mathematical script, PROOF or DAG edit.

## Original nomination1266 — preserved scope and proposed equation

Use the full positive-side theta density Phi with the local L019
normalization and Xi as in L018-L020; do not substitute the corrected
three-mode core. The proposed scalar-profile equation uses

    G_{sigma,+/-}f(u)
      = integral_0^infinity f(s)(1 +/- (s+u))
          exp(sigma*omega*(s+u)/2) Psi(s+u)/Psi(s) ds,
    sigma in {-1,+1}, omega=1/4, Psi(s)=Phi(s/2).

This specifies the proposed test, not an established result.
Positive nonzero scalar branch weights would cancel from its equation;
no identification of a source completed space is asserted. Verify
nonvanishing of Xi(5i/4) and the local conventions before using c.
Complex f is allowed; a sign argument only for nonnegative f does not
settle the proposed test.

The motivating primary passages are
[Freedman2606.29555v1, Appendix C.1](https://arxiv.org/html/2606.29555v1#A3.SS1):
the h_z^+/- definitions, the common-U requirement, joint-Gram criterion,
and g_+/- features. Review which exact compatibility condition follows
from that formulation rather than assuming the proposed equation
already blocks the actual bridge. Retrieve primary hypotheses and
essential proof cases for any convolution/transform uniqueness result
used. Search exact and stronger statements plus recorded local failures
before approving a bounded mathematical attempt. No source numerical
fit or script name is a theorem about this equation.

Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
Plausible use: test one overstrong compact exact transport ansatz before
using it in a positive-kernel bridge; it cannot itself supply that
positivity. The continuation discriminator is a rigorous compact-core
existence/nonexistence argument applicable to arbitrary complex f,
or a precise theorem showing why this screen does not address the
source ansatz. Nonexistence would stop only this compact exact ansatz;
completed noncompact Green minimizers, nonisometric pullbacks and
closed-cone limits would remain separate. Existence of one f would not
construct an isometry or match other evaluation points.

Essential continuation inputs are the source's two explicit feature
families, L018-L020's full theta normalization, and C032d's parked
inference obstruction as context. The direct construction assessment
`2026-10-31-theta-de-branges-kernel-construction-review.md` is reusable
only for its conditional/shifted/translation hypotheses, not this new
range test. Source-core identification, completed domains, uniform
parameters, actual-Xi signing, graph realization and initialization
remain unresolved. No theorem or novel mathematics was derived here;
Mathlib coverage is unchecked and no cross-notebook result is used.
