# L738 independent audit — completed source and scope review

TARGET: Review coverage for an independent audit of L738's fixed-kernel admissibility, Fourier normalization, damping errors and four signed margins, without extending the kernel family or transferring signs to Xi.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-target searches and L050/L607 duplicate comparisons in 2026-11-04-critical-point-modulated-kernel-test.md and 2026-11-04-xi-critical-point-sign-scope.md; read the complete L738 proof for scope and the step-263 history/route stop. Narrow primary-source retrieval confirmed the definition, normalization, Gaussian row and relevant associated-kernel comparison; no broader discovery search or mathematical audit was performed.
SOURCE_EVIDENCE: Csordas arXiv:1309.0055v2 (21 February 2014), https://arxiv.org/pdf/1309.0055v2, (1.1), Definition 1.2, Theorems 3.5/3.7 with their relevant proof cases, Remark 3.8(a), Example 3.12, printed pp.1-2/6-9; NIST DLMF live edition accessed 4 November 2026, https://dlmf.nist.gov/1.14.E1, https://dlmf.nist.gov/1.14.E2 and https://dlmf.nist.gov/1.14.T1, Gaussian row a>0, all inspected directly.
COMPARISON: Csordas supplies the exact admissibility definition and two explicitly different transform conventions; DLMF supplies the normalized undamped Gaussian transform. Neither source supplies L738's quartic-damped estimates or adverse stationary value. Its existing local analytic specialization and four signed margins require audit; scalar replay alone is insufficient.
GAP: Source coverage is adequate for the bounded audit, but global shape/common-epsilon tails, compact complex domination, moment errors, every strict margin and the critical-point conclusion remain independently unverified. No actual-Xi sign or realization is covered.
REASON: Approve one independent audit of the already-written fixed example, rather than reprove an imported transform or expand the kernel family. The review establishes source applicability and audit obligations only; it does not certify L738 or its originality.
SCOPE: Only L738 at delta=10^(-8), frequency 10 and modulation 1/100, its full-line F on [6,7], and the existing exact scalar replay; no parameter change, actual-Xi transfer or stronger zero-location conclusion.
COVERED_TARGET: Independently audit L738's fixed-kernel admissibility, Fourier normalization, damping errors and four signed margins, replaying its exact scalar certificate without extending the kernel family or transferring signs to Xi.
LITERATURE_REASON: The new independent-audit scope required separate source/hypothesis comparison after step 263; ready coverage for the original calculation did not itself certify or approve that audit.

## Scope for the requested review

Use the prior assessment `2026-11-04-critical-point-modulated-kernel-test.md`
and the canonical L738 proof. The exact primary inputs are Csordas,
[*Fourier transforms of positive definite kernels and the Riemann xi-function*,
arXiv:1309.0055v2](https://arxiv.org/pdf/1309.0055v2), Definition 1.2,
printed p.2, and [NIST DLMF 1.14.1](https://dlmf.nist.gov/1.14.E1)
with [Table 1.14.1](https://dlmf.nist.gov/1.14.T1), Gaussian row a>0.
The source review should distinguish the cited undamped transform
from the proved damped comparison and verify the full-line versus
half-line normalization. Existing primary evidence can be reused;
additional browsing is not requested just to repeat it.

The proposed later audit must inspect global strict decrease,
all-derivative decay with one common epsilon, entire differentiation,
the three moment bounds, every uniform/endpoint margin, and the
critical-point conclusion. The supplementary replay is
`python3 scripts/critical-minimum/fixed-rational-margins-263.py`.
It certifies exact scalar inequalities, not the analytic proof.

There are no essential local mathematical input IDs beyond the new
object to be audited, L738. L050 and L607 are contrasts only. No
actual-Xi sign, zero strip, order-one transform, modularity, simplicity,
or realization premise is authorized. A successful audit would confirm
only a generic counterexample. A failed hypothesis or sign margin
requires preserving the error and parking or repairing this exact test,
without changing parameters in the same audit.

## Completed review — step 264, 4 November 2026

This separate literature-only turn approves the COVERED_TARGET above
as SPECIALIZE. No new result was derived, no scalar certificate was
replayed, and the mathematical proof remains unaudited. The target
at entry was the source/scope review stated in TARGET; the covered
continuation is the later research audit, not another literature pass.

### Exact source applicability

Csordas Definition 1.2 requires all five conditions, including one
epsilon>0 for the derivative decay of every nonnegative order. The
big-O constants are not stated to be uniform in derivative order.
The audit must compare L738's common epsilon=1 argument with this
quantifier; decay of the undamped Gaussian alone is insufficient.
No extra kernel zero-strip or transform-order hypothesis occurs in
that definition. Strict log-concavity is an additional asserted
property, not a replacement for any admissibility condition.

Csordas (1.1), printed p.1, uses one half of the full-line transform,
equal to the half-line cosine integral for an even kernel. In contrast,
Theorem 3.7, printed p.8, explicitly defines its F by the full-line
integral. Thus the future audit must specify the convention at each
comparison; the paper does not use one convention throughout. Remark
3.8(a) gives the first Laguerre expression in that full-line setting.
L738's last paragraph compares with (1.1)'s convention only. Checking
its scaling statement is an audit obligation, not a sign theorem
imported from the paper.

DLMF 1.14.1 uses exp(ixt)/sqrt(2 pi) on the full real line. The
Table 1.14.1 Gaussian row is exp(-a t^2) mapped to
exp(-x^2/(4a))/sqrt(2a), with a>0. L738's undamped reference has
a=1, within those hypotheses; its unnormalized convention requires
the factor sqrt(2 pi). The modulating cosine requires the elementary
frequency-shift specialization already written locally. The quartic
factor is outside the row and must not be silently included in it.
DLMF 1.14.2 is an absolute-integral bound under L1 integrability; it
does not by itself justify differentiation for complex arguments.
No general Gaussian transform is to be reproved in the audit.

The strongest relevant comparison remains Csordas Theorem 3.5:
strictly log-concave admissibility implies admissibility of associated
kernels, not their positive definiteness. Its two proof intervals
(0,t) and (t,infinity), and Theorem 3.7's coefficient/positive-definite
interface, were inspected for this distinction. Neither supplies
L738's required stationary sign. Example 3.12 explicitly fails decay
condition (v), and has a favorable first sign; it cannot replace the
fixed fully admissible countertest. These are comparisons only, not
essential inputs to L738. Proposition 3.10 is not imported. Reuse the
prior bounded duplicate search; no new originality claim follows.
The previously inaccessible supplementary Schubr manuscript is not
essential, and no new access attempt or theorem import is needed.

### Bounded audit obligations and decision test

Read the canonical L738 proof in full and check its assertions against
the precise sources above. In particular, independently inspect:

1. Global positivity/evenness/smoothness, strict log-curvature,
   strict decrease on the whole positive half-line, and common-epsilon
   decay for every derivative, with constants allowed to depend on
   derivative order and the fixed delta.
2. Compact complex domination for entire differentiation, real/even
   symmetry, the DLMF normalization and frequency shifts. Real-axis
   estimates alone must not stand in for the complex domination.
3. The three absolute moments, integration-by-parts endpoints,
   the uniform j=0,1,2 perturbation bounds, and division by sqrt(pi).
   This is a finite fixed-delta comparison, not a formal expansion.
4. Complete interval value/curvature margins, both derivative endpoint
   signs, the elementary exponential bounds, strict rational slack,
   and the existence/uniqueness and negative Laguerre conclusion.

The existing script may supplement item 4 only. Inspect its complete
load-bearing assertions/certificate fields if replayed; twelve passed
scalar comparisons do not verify items 1-3 or the final implications.
Full matching Mathlib coverage remains unchecked; no absence is claimed.
Standard dominated differentiation, integration by parts and the
intermediate value theorem are already explicitly applied locally;
no additional specialized external theorem is essential to this scope.

Continue only if the full analytic argument and all stated strict
margins survive. A failing hypothesis, factor, endpoint or inequality
must be preserved and identified in the canonical audit record, with
repair or parking of this exact test as appropriate. Do not change
parameters, sweep a family, infer novelty, or transfer any sign to Xi.
A pass confirms only the generic obstruction. The actual-theta signed
residual, other centers, degeneracies and higher mixed signs remain
independent gaps. No justified creative central-gap mechanism is ready
without an explicit independently testable theta-specific residual.
