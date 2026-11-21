# Standalone right horizontal Mellin tail: completed source comparison

TARGET: Assess the standalone right horizontal theta-Mellin tail on D against (14u/sqrt(Q))exp(-(77/50)Qd^2), without assuming the global contour or continued-endpoint identity.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step522 searched Mellin-named local assessments and ATTEMPTS for the exact ray, T_R, horizontal concavity and log-concavity; only this nomination matched the standalone observable. External queries covered effective nonstationary Laplace endpoints, bramble_trace horizontal tails, exact 14u/Mellin/77, and log-concave tangent tail bounds. No novelty inference.
SOURCE_EVIDENCE: Reinspected paper23 v1 (18 October 2026), Section3 Lemma2 (10)–(14); NIST DLMF2.3(iii), hypotheses(a)–(c), (2.3.13)–(2.3.15), and 2.4(iii), hypotheses(a)–(c), (2.4.10)–(2.4.12); Luc Devroye, Non-Uniform Random Variate Generation (1986), ChapterVII Section2.6, pp299–300, envelope preceding Theorem2.6 and first integral in its proof, author-hosted primary PDF. Exact scope below.
COMPARISON: Fixed-data Laplace asymptotics do not pay this effective moving-parameter allowance. Devroye's pointwise exponential envelope has no asymptotic or fixed-phase constant; full-ray amplitude, real-phase concavity and negative endpoint slope are specialization obligations, not imported facts about theta.
GAP: Prove absolute convergence and the normalized 14u/sqrt(Q), 77/50 bound uniformly on all D by checking the full-ray hypotheses; L798/L799's finite bounds alone do not do this. No right-tail estimate is established here.
REASON: Accessible effective endpoint envelopes remove the essential source-method gap for an independent reproduction test. Parameter-specific hypotheses and constants remain mathematical work; unread supplements and the global contour are unnecessary premises for that test.
LITERATURE_REASON: The changed target is an actual-theta infinite horizontal ray; Gaussian completion and local amplitude assessments did not cover effective endpoint envelopes or their whole-ray hypotheses.
SCOPE: Literature-only step522 completes step521's nomination. No new convergence proof, estimate, lemma or script. A separately nominated research continuation requires next-turn supervisor approval.

The main gap remains actual-Xi all-degree mixed positivity. The target
is a right-tail component of a possible Mellin approximation; even
success leaves left tails, continued endpoint, global deformation,
assembly, quotient/inversion, certificates and sufficient signs open.
No justified central creative mechanism follows from the Gaussian audit.

Use exactly D, x=u+ih, Q, d, S_s, A, a and C=sqrt(2pi/A) from
L798/L800, and L799's theta series P on U={z: |Im z|<pi/4}.
Set z_R=x+da. The candidate observable, with no properties presumed, is

    T_R(s) = | integral_0^infinity
                    exp(2s Log(z_R+t)) P(z_R+t) dt |
             / |4pi^2 exp(S_s(x)) C(s)|.

The proposed threshold is

    T_R(s) <= (14u/sqrt(Q)) exp(-(77/50)Qd^2), s in D.

This allocates the source's whole horizontal-tail budget to a proposed
test of this one component; it does not assert that both horizontal
contributions fit that budget. The contour is only the specified
horizontal half-line. Its use in an equality for continued M(s) is
outside scope. Retain principal branches and the full complex numerator.

First search exact claims/failures in Mellin-named local assessments
and ATTEMPTS, then inspect relevant primary effective nonstationary
Laplace hypotheses and essential proof cases. Reuse the inspected
paper23 outline. Unread Derivations42/43/65/87 are not premises;
do not repeat supplement-access searches. A fixed-data saddle theorem
cannot be imported without checking moving-parameter uniformity.

Continue to a separately approved mathematical test only if accessible
independent hypotheses cover the entire half-line, absolute convergence,
both closed boundaries of D, both signs of h, h=0 and unbounded u.
If coverage still requires the blocked global assertion or supplement,
park this target and select another independently testable mechanism.
Failure of a sufficient envelope is not a counterexample to T_R or RH.
No numerical sample or endpoint heuristic verifies D.

Essential proposed local inputs are L797/L798 geometry and branches
and L799's P and strip holomorphy. L800 is finite-Gaussian context,
not an infinite-tail estimate. Mathlib full matching coverage is
unchecked. No cross-notebook input is proposed.

## Completed review, step522

The nomination above is retained as the exact target specification and
historical decision test. This section records source readiness, not
verification of its proposed actual-theta inequalities.

### Primary statements and essential proof cases

[paper23 v1](https://rstation.ai/problems/riemann_hypothesis/papers/23),
Section3 Lemma2 (10)–(14), reinspected 5 November 2026, assigns its
horizontal allowance to two tails and delegates their concavity and
endpoint regimes to Derivations42/43/65. This separate right-ray target
spends the whole allowance on one component; it cannot certify the
combined allowance. The full-contour import stop remains valid.
No supplement-access search was repeated.

[DLMF2.3(iii)](https://dlmf.nist.gov/2.3#iii), hypotheses(a)–(c),
(2.3.13)–(2.3.15), requires an isolated endpoint minimum, differentiable
endpoint expansions with positive leading phase coefficient and positive
orders, and absolute convergence for sufficiently large real parameter.
Its conclusion is asymptotic. [DLMF2.4(iii)](https://dlmf.nist.gov/2.4#iii),
hypotheses(a)–(c), (2.4.10)–(2.4.12), additionally requires analytic
path data, continuous endpoint branches, a sector narrower than pi,
absolute uniform convergence, and strict real-phase domination with a
uniform remote-endpoint gap. Neither pays effective moving-phase
constants. Reuse step511's inspected O'Sullivan localization/inverse
cases; no stronger result from that source is imported here.

Luc Devroye, [*Non-Uniform Random Variate Generation*, ChapterVII
Section2.6, pp299–300](https://luc.devroye.org/chapter_seven.pdf),
Springer-Verlag, 1986, author-hosted scan, inspected 5 November 2026:
the paragraph and displayed envelope before Theorem2.6 use the tangent
majorization for differentiable concave h=log f,

    f(y) <= f(b) exp((y-b)h'(b)).

The proof's first displayed integral on p300 integrates the exponential
right piece. A finite negative slope is essential for finite right mass;
zero or positive slope supplies no integrable right envelope. The
optimization theorem's mode selection and probability normalization are
not needed inputs here. Later use for an unnormalized phase must justify
the tangent step directly, without normalizing an integral whose
convergence is unproved. This effective whole-half-line envelope contains
no constant depending on a fixed analytic neighborhood. It asserts no
log-concavity of the complex theta series or its modulus. No actual-theta
theorem is attributed to this source.

### Applicability and decision

The method uses a real phase envelope along the specified complex ray
and a separate absolute theta-amplitude bound. Its scope includes an
infinite real parameter interval and a variable finite negative endpoint
slope, without a fixed strip width or global Mellin identity. Thus there
is no essential unread source for trying it. Actual uniform hypothesis
verification remains mathematical work:

1. Keep the entire ray in L799's U and the principal Log domain for all
   t>=0 and all s in the closed D, both signs of h, h=0 and unbounded u.
   Finite-disc admissibility alone is insufficient.
2. Bound the full theta amplitude on the entire ray using L799's series
   and factorization. Its finite-diameter eta bound is not a ray bound.
   Do not assume log-concavity of |P| or interchange an infinite integral
   and series without an absolute majorant.
3. Verify real-phase concavity on the entire ray and a quantitative
   strictly negative endpoint slope. L798's finite endpoint decrement
   is available, but does not establish horizontal slope or global
   concavity. Prove absolute convergence and pay the normalized constants.

These are obligations, not results established here. Continue only if
they pay the exact threshold everywhere on D. Otherwise record the
precise failed sufficient bound and park that mechanism; this does not
refute T_R or RH. Do not import unread horizontal derivations or replace
uniform checks by endpoint sampling. This is an independent test of one
component, not reopening the blocked global import.

Queries included `effective error bounds Laplace method nonstationary
endpoint unbounded interval uniform parameter O Sullivan`,
`"bramble_trace" "horizontal" Mellin`, `"14u" "Mellin" "77"`,
`log concave density tail bound f(x) derivative log f(x) hazard tangent
inequality`, `Laplace method tail integral bound convex f derivative
endpoint exp f`, and `"nonstationary" "Laplace" "bounds" endpoint`.
Search snippets and probability reviews supplied leads only; Devroye's
author table of contents led to the primary chapter. Stanford-hosted
convex-text/exercise requests failed; those texts and the exercise mirror
were not used. These optional failures are not essential blockers after
the primary envelope was read. No inference of novelty from this search.

Mathlib full matching coverage remains unchecked. The local scoped search
found no duplicate standalone proof. No cross-notebook input was read.
No central creative sufficient-sign mechanism follows from this method.
The [research nomination](2026-11-05-mellin-right-horizontal-tail-test.md)
requires separate supervisor approval next turn. This is local source
progress only, with no new estimate or advance on the RH sign gap.
