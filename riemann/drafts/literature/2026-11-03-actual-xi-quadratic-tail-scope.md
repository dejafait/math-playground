# Actual-Xi quadratic-tail normalization — completed source comparison

TARGET: Assess quadratic-tail normalization of the actual-Xi local Hadamard product on |v|<=1 for a first-Laguerre sign-transfer test with all actual zeros and multiplicities retained.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed bounded local duplicate/failure comparisons and five targeted web queries listed below; inspected the primary hybrid-product and Laguerre statements and essential proof cases, and reused the fixed-radius and count assessments. No matching full hard-cutoff C2/sign-margin theorem was established by this search; no novelty inference.
SOURCE_EVIDENCE: Csordas arXiv:1309.0055v2 (21 February 2014), Definition 1.1, Propositions 2.2–2.3 and proofs (2.3)/(2.5), pp.3–4; Gonek–Hughes–Keating arXiv:math/0511182v1 (7 November 2005), Theorem 1 (4)–(7) and Section 2 (10)–(14), including branch and zero cases; Najnudel–Nikeghbali v1 A.1 coverage reused from step 221 and changed-radius tail passages reopened; Bellotti–Wong v2 Theorem 1.1/Section 5 coverage reused through L467's source/application audits. Exact locators and qualifications below.
COMPARISON: Exact product differentiation and multiplicity-counted shells cover the ingredients of a quantitative application. A.1 has fixed microscopic radius; the hybrid product uses smoothing and retains a prime factor; L471 already gives the exact signed reciprocal-square and gauge identities. None of these supplies a favorable actual-local-polynomial margin. L464's high-order coefficient tail and L476's shrinking clipped integral have different conclusions.
GAP: A fixed-physical-disk C2 bound with explicit constants and a zero-safe signed quadratic transfer still needs a separate application proof. A favorable local margin, normalization at central zeros, higher signs and global coverage remain unproved; no source-independent sign mechanism was found.
REASON: Source coverage suffices for one quantitative REPRODUCTION specialization, specified in 2026-11-03-actual-xi-quadratic-tail-calculation.md, subject to separate next-turn approval. Park unconditional sign transfer; do not schedule further normalizations without a materially new signed input.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target changed from a synthetic profile to all actual zeros and from a fixed microscopic to a fixed physical disk; its essential radius and signed-factor comparison was previously missing. This turn completes that comparison without mathematics.

## Completed comparison, 3 November 2026

Outcome EXPLORATION, LITERATURE / NOVELTY_UNCHECKED. This is new source
scope, not a mathematical estimate or progress beyond the inspected
results. The earlier nomination below is preserved as the question
reviewed; its requests for review are discharged by this section.

### Primary statements and applicability

[Csordas, v2](https://arxiv.org/html/1309.0055v2), Definition 1.1 and
Proposition 2.2 proof (2.3), pp.3–4, gives the signed real/conjugate-zero
reciprocal-square identity with quadratic-exponential contribution 2a.
The proposition's interval exclusion is an extra sign hypothesis, not a
condition needed for that identity. L024 and L471 Section 1 already justify
the actual-Xi application with a=0, multiplicities and local convergence.
Proposition 2.3/(2.5) retains a competing residual first-Laguerre term;
its small-displacement conclusion with fixed residual supplies no uniform
margin for a moving actual zero and changing residual. Both short proofs
were read. L471 (7) already records the gauge curvature term. Import these
identities by citation; only the new normalization application needs work.

[Gonek–Hughes–Keating, v1](https://arxiv.org/html/math/0511182v1),
Theorem 1, assumes sigma>=0, |t|>=2, X>=2, fixed positive integer K and
a smooth nonnegative unit-mass u supported on [exp(1-1/X),e]. Equations
(4)–(7) express zeta as P_X Z_X with relative error
O(X^(K+2)/(|s|log X)^K)+O(X^(-sigma)log X); constants depend on u,K.
Z_X uses exponential-integral smoothing over all nontrivial zeros.
Section 2, (10)–(14), was read through its branch-cut convention,
absolute-convergence argument, pole/trivial-zero estimates, smoothing
replacement and final zero extension. This is a stronger flexible
factorization lead, but not the proposed hard-cutoff polynomial. It
retains P_X and supplies no signed first-Laguerre margin. A complex disk
around the critical line also needs attention to the stated sigma>=0
domain before derivative estimates. No replacement or differentiated
error is imported, and the manuscript is not independently audited.

[Najnudel–Nikeghbali, v1](https://arxiv.org/pdf/2609.15862v1),
Proposition A.1/(A.12), is reused from the complete step-221 assessment.
The statement and radius-relevant tail passages (A.6)–(A.12) were reopened.
Its r is fixed before T grows. Its complex-zero and logarithmic-tail proof
does not license a growing-r substitution in a constant indexed by r.
This is the exact quantifier difference for the present review.

The independent complete-count input is already ready: Bellotti–Wong
v2 (7 July 2025), Theorem 1.1 p.1 and Section 5 pp.23–24, assessed in
`2026-10-25-explicit-unit-shell-count-coverage.md` and
`2026-10-25-l467-critical-audit-coverage.md`. Reuse L467's closed-shell
18 log(v+2) count, including multiplicities and low heights; do not reprove
the source computations. Read its hypotheses/conclusion and L464 Section 3
only as the existing reciprocal-square shell implementation. A cubic
tail after quadratic subtraction is the proposed application difference,
not an established estimate in this review.

### Search, overlap and limits

Queries actually made:

- `zeta xi local Hadamard product logarithmic derivative sum zeros truncated second derivative Laguerre inequality`
- `Riemann xi local polynomial approximation exponential quadratic zeros Hadamard product`
- `"xi" "quadratic" "local" "Laguerre" product tail`
- `"zeta" "Hadamard" "C2" tail approximation`
- `"Riemann" "local product" "quadratic" normalization`

Only the primary texts above support this comparison. Search snippets,
purported RH proofs, notebook mirrors and unrelated polynomial products
were not imported. No search proves absence of a stronger theorem.

L024 already proves the full product: no new Hadamard lemma is needed.
L471 (6) already gives the exact first-sign sum; a new factorization
cannot be advertised as a new sign identity. Reused the Gaussian-regulator
assessment, whose function and error scale differ. The mesoscopic
signed-truncation assessment approves a shrinking-cutoff weighted integral,
not a uniform analytic logarithm; its realized result is L476. L464's
coefficient orders likewise do not supply the proposed local margin.
The heat exponential-sum curvature stop in
`ATTEMPTS/2026-11-01-uniform-quadratic-curvature-budget-stop.md` has a
different object and remains evidence for its own route only. No historical
stop is interpreted as a ban on actual local products.

### One continuation and its stopping test

The continuation is the exact quantitative target in
`2026-11-03-actual-xi-quadratic-tail-calculation.md`, using
L018/L024/L467/L471. Its threshold is C/log T for the full complex-disk
second-derivative remainder, with explicit absolute C and onset. This is
a proposed threshold, not a theorem established here. Retain the full
quadratic curvature and state a conditional margin without division by
the local factor at its zeros. Its use is a certified conditional local
test and a quantitative separation of the tail error from the independent
sign gap; it will not establish the favorable margin itself.

Continue only if the complete tail, signed factor and stated uniformity
can all be certified. Otherwise record the failed bound or assumption.
Even success ends this normalization calculation: subsequent signing
work requires a materially new, separately assessed actual-local margin
or witness. There is no justified creative mechanism yet, since none of
the compared inputs controls that signed residual. The new ready
continuation requires separate approval next turn. Full matching Mathlib
coverage remains unchecked; no canonical lemma, mathematical script,
DAG edge or mathematical assembly was changed in this source review.

## Preserved original nomination

## Exact proposed objects and one source test

The main gap remains actual-Xi mixed positivity, including initial signs
at unbounded heights. The proposed intermediate target is quantitative
separation of an actual finite zero block from its analytic tail, with
the effect of the latter on the first sign stated explicitly. Its possible
use is a genuinely actual-Xi local sign test; the local polynomial's sign,
central zeros, higher signs and global coverage would remain independent.
This review must decide whether the target offers such a test or merely
repackages the unknown sign. It is not a request to prove RH by finite
approximation.

Use only the actual Xi of L018/L024. Put L=log T, t in [T/L,T],
Xi(t)!=0, and H_T=2*pi*L. For comparison with A.1, the proposed local
factor uses every distinct actual Xi zero alpha=gamma+i*(1/2-beta)
with |gamma-t|<=H_T, raised to its full multiplicity:

    P_(t,T)(v)=product_(|Re(alpha)-t|<=H_T)
                         (1-v/(alpha-t))^(m_alpha).

Retain equality at the cutoff. The proposed remaining factor is
Xi(t+v)/(Xi(t)*P_(t,T)(v)), with cancellation interpreted analytically.
Its normalized logarithm E_(t,T) on a neighborhood of |v|<=1 and its
real quadratic Taylor polynomial Q_(t,T) must be justified before use.
The source task asks whether there is already a theorem giving an
explicit uniform bound tending to zero for

    sup_(|v|<=1) |(E_(t,T)-Q_(t,T))''(v)|,

and an applicable description of Q_(t,T)'' and its contribution to
D_1(f;t)=f'(t)^2-f(t)*f''(t). This displayed bound is a proposed
threshold, not a derived estimate. Account for all exterior zeros in E;
do not delete them, impose simplicity or project their positions.
Do not assert that removing a real quadratic exponential preserves the
sign, nor divide by a local polynomial at its zeros. If only a
conditional sign margin follows, state the required margin and why it
would be a useful independently testable input. A small norm alone is
not a sign result.

Primary starting point is Najnudel–Nikeghbali,
[*Cauchy laws for zeta logarithmic derivatives and stationary Stieltjes
transforms*, arXiv:2609.15862v1](https://arxiv.org/pdf/2609.15862v1),
Proposition A.1 and its proof (A.1)–(A.12), pp.32–35. Reuse the
already inspected fixed-radius statement/proof; search exact/stronger
growing-radius and derivative-tail results before considering a reproof
or extension. Constants hidden by fixed-r notation do not justify
substitution of a growing radius. No external fixed-half-plane premise,
arbitrary zero placement or numerical zero evidence is an input.

Continuation test: an inspected theorem must either cover the proposed
C2 tail bound and signed-factor interface with all hypotheses, or
identify a bounded, independently testable uncovered difference. If
the resulting comparison only replaces the full unknown sign by an
equally uncontrolled local polynomial/counterterm sign, park that sign
implementation rather than schedule repeated normalizations. A useful
quantitative intermediate bound may leave the independent sign gap open;
its precise downstream test must still be stated before mathematics.

## Existing evidence to reuse, not repeat

Essential input IDs are L018, L024 and L471. L464 is the exact comparison
for finite/far high-coefficient tails if that interface is needed; load
only its relevant statement/range after reading the ready assessment
`2026-10-25-local-factor-coefficient-audit-coverage.md`. No cross-notebook
input is proposed. A.1's source reading and the parked C651a realization
are recorded in `2026-11-03-fixed-profile-xi-realization-scope.md`.

The `2026-10-05-gaussian-coupled-laguerre-transfer.md` assessment treats
a Gaussian regulator response, with a separately required signed margin;
it does not approve this actual-zero tail. The uniform quadratic-curvature
stop under ATTEMPTS concerns a heat-flow exponential-sum envelope, not
this product. L470's finite polynomial linear-ODE stop likewise does not
ban local factors. L471's weighted negative-mass and the local-L2/tilted
norm stops prevent replacing missing pair-divided or normalized estimates
by ordinary moments. Preserve all these scopes and their evidence.

No mathematical estimate, script, sign claim or new canonical lemma was
created in nominating this target. Full matching Mathlib coverage is
unchecked. A creative central attempt would require a specific signed
mechanism and decisive quantitative test beyond tail approximation;
neither is certified ready merely by this nomination. The next turn is
source comparison with standard/high routing, not an automatic creative
proof invocation or a renewed synthetic-profile audit.
