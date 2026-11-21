# Distant-derivative boundary profile — completed source comparison

TARGET: Test whether replacing every origin mass in L967's complete n=2,3 face sums by A(u)[H_0(h,u)+H_1(h,u)]/[2(c_0+c_1)] yields a nonnegative fully symmetrized kernel, retaining every intersection and the distant h term.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step175 completed bounded Li/theta boundary-compensation, derivative-weighted/size-biased distribution and symmetrized-kernel searches; narrow November10 notebook searches found this nomination and L967's old-profile stop, not a duplicate test. Reused the ready step167 calculus and the recorded partition/cumulant-transfer comparisons. No inspected exact-profile sign theorem was found; absence or novelty is not inferred.
SOURCE_EVIDENCE: Biane-Pitman-Yor, Bull.AMS38(4)(2001),435-465, Section3.6/Proposition3.1/(3.20)-(3.21), p446, including its proof paragraph; Patil-Rao, Biometrics34(2)(1978),179-189, Section1/(1.1), pp179-180, and Section3 OCR qualifications below; Planat, preprints202606.0062v1, 1June2026, Sections3.1-3.2,5.4/Proposition3 and6.2-6.3/Theorem4/Problem1. Source scope only; no new theorem import into the argument.
COMPARISON: Weighted-law normalization and special size-bias characterizations supply no sign for the complete signed Bell tensor. Planat's compensation concerns a different two-variable oscillatory integral and leaves global positivity as a problem. L967's rigorous ray excludes only the old b-profile; the h-derivative-aware replacement changes that mechanism but has no proved sign. Known transfer calculus is reused, not reproved.
GAP: Derive and verify the complete kernel for this one fixed replacement, including all origins/intersections and the distant h subtraction, then prove its full-orthant sign or a rigorous negative configuration at n=2 or3. No such calculation ran in this review. Both small-order success and a structural general-n mechanism would still be needed before an all-n development.
REASON: Approve one bounded mathematical attempt under the unchanged TARGET and SCOPE. The source comparison supplies tools and limits, not the missing inequality. The independently testable change addresses the precise distant-derivative obstruction without assuming Xi signs; no inspected theorem makes the proposed test redundant and no essential source is blocked.
LITERATURE_REASON: At invocation the changed h-derivative profile was REVIEW_REQUIRED and outside the saved old-profile assessment; this separate literature-only step completes that comparison. Further browsing on this unchanged target needs a new essential hypothesis or source.
SCOPE: Actual A,K of L019 and H_r of L966; n in {2,3}, b=1/4, h=64*9^n, and c_r=integral_0^infinity A(u)H_r(h,u)du as in L967. Replace each origin mass 1/2 by the displayed density times du, including h-origin masses and all intersections. No RH, simplicity, sign assumption or change to Q_eta is permitted.

## Completed review — 10 November 2026, step175

The unchanged TARGET is now covered for one mathematical attempt. This
decision supersedes the nomination's historical REVIEW_REQUIRED status
and literature-only next-turn instructions below. Outcome EXPLORATION,
kind LITERATURE, classification NOVELTY_UNCHECKED: no mathematical result,
new sign, new representation or originality claim is established.

### Primary comparisons

Biane, Pitman and Yor, [*Probability laws related to the Jacobi theta
and Riemann zeta functions, and Brownian excursions*](https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/biane-pitman-yor.pdf),
Bull. AMS 38(4) (2001), 435-465, DOI10.1090/S0273-0979-01-00912-0,
published version, Section3.6, p446. Proposition3.1 concerns a
nonnegative random variable X and its size bias
P(X* in dx)=xP(X in dx)/E(X). Case(i) characterizes S_2 by E(X)=2/3
and X*=X+H X* in distribution, using independent right-hand variables
and density (h^(-1/2)-1) on (0,1) for H. Case(ii) characterizes C_2
by E(X)=2 and X*=X+U^2 Xhat, with independent X,U,Xhat, Xhat a copy
of X and U uniform on [0,1]. Its proof paragraph uses the resulting
Laplace-transform equation and cites further details; those external
details were not inspected. These particular identities neither identify
the nominated A-weighted law with S_2/C_2 nor sign its Bell tensor.
No such identification, independent-addition law or infinite-divisibility
premise is imported. Step167's separate Section2.3 Li/cumulant comparison
is reused unchanged, without another derivation.

Patil and Rao, [*Weighted Distributions and Size-Biased Sampling with
Applications to Wildlife Populations and Human Families*](https://paperzz.com/doc/7051795/weighted-distributions-and-size-biased-sampling-with-appl...),
Biometrics 34(2) (June1978), 179-189, DOI10.2307/2530008. Inspected
the primary article's reproduced text, Section1/(1.1), pp179-180:
weighting uses an arbitrary nonnegative weight, including unbounded
weights, and its finite nonzero normalization; size bias is the special
weight x. This is relevant terminology, not a signed-kernel theorem.
The Section3/Theorem4 statement and short proof concern weighted mean
comparisons via a monotone weight ratio. OCR damages some formulas,
including the integrability display; no exact inequality or specialization
of that theorem is imported. The DOI endpoint was inaccessible. This
optional mean-comparison lead is parked and is not essential coverage
for the specified pointwise test. Normalizing a density does not itself
control a signed multivariate observable.

Planat, [*A Theta-Kernel Reformulation of a Growth Theorem and the
Riemann Hypothesis*](https://www.preprints.org/manuscript/202606.0062),
DOI10.20944/preprints202606.0062.v1, posted1June2026. Inspected
Sections3.1-3.2 for the Phi/double-integral convention, Section5.4/
Proposition3 with its proof paragraph, and Section6.2-6.3/Theorem4/
Problem1. Proposition3 states a compensation identity for x!=0 on
a>b>0, using sine/hyperbolic factors and integration by parts.
Problem1 still asks for global positivity for every x,y>0. This is
a different oscillatory two-variable observable, without this profile,
the n+1 Bell tensor or the prescribed h term. Neither its endpoint
assertions nor claimed equivalences are independently audited or used.
The linked published-version DOI was inaccessible; the named v1 scope
comparison suffices and no published-version theorem is silently assumed.

### Reuse, duplicate and failure checks

The step167 assessment
`2026-11-10-li-theta-ibp-remainder-review-166.md` already supplies
NIST DLMF1.4.16 and1.4.22-23 transfer calculus, with convergence and
endpoint qualifications. L967(5)-(16) already supplies the complete
finite numerators, all faces and symmetrization. Reuse these exact
identities; do not redo the transfer as a purported new mechanism.
L019 supplies the actual density and decay; no external approximation
or replacement law is needed to formulate the bounded test.

The step168 ATTEMPTS record and L967(4),(18)-(21) stop the b-profile
because of its retained distant derivative. They do not test the
nominated profile. The November6 connected-partition comparison and
November4 Nuttall cumulant-transfer assessment/ATTEMPTS stop were read
at the relevant scope: connectedness does not impose signs, and the
different-kernel determinant perturbation lacks an actual-K transfer.
No blocked GHS/Coffey retrieval or direct cumulant-transfer campaign is
reopened. The step158 finite-window limit remains separate. No broader
notebook or cross-notebook input was read.

Queries included `"Riemann" "Li coefficients" "integration by parts"
theta kernel`, `"Li" "theta" "boundary" "compensation" positivity`,
`"cosh" "Li coefficients" "kernel"`, `"Riemann" "theta"
"derivative" "boundary mass"`, `"theta" "Li" "H_1" "H_0"`,
`"Riemann" "boundary spreading"`, `"Li coefficients" "weighted
distribution"`, `"theta kernel" "derivative" "symmetrized" positivity`,
and derivative-weighted/size-biased/Patil-Rao searches. Several returned
only unrelated results; none is taken as evidence of nonexistence.
Narrow local searches covered November10 assessments, histories and
ATTEMPTS records for H_0/H_1, derivative-aware and weighting terms.
Only the nomination and old-profile records matched the mechanism;
the known sources above remain comparisons, not certified novelty.

### Approved bounded continuation

Keep exactly the saved TARGET. Use L019, L966 and L967 as essential
inputs, and audited L968 for downstream sufficiency: a full all-index
proof of L966(16) would suffice for RH at the prescribed eta. There is
no remaining detector-parameter mismatch to repair by this test.
L018/L024/L026 retain the actual-node and multiplicity framework.

In the next mathematical turn, substitute this single profile in the
complete saved face expansion, retaining the h-origin atom and every
intersection. Verify the resulting integral identity and convergence
before asserting signs. Seek a rigorous negative point/ray, including
one-coordinate and competing-coordinate escape, or a full-orthant
certificate at n=2,3. Any actual normalization constants need proved
bounds if their values are load-bearing; floating-point fits or positive
grids cannot decide the test. Do not tune a new profile during this test.

A rigorous negative configuration at either order retires this pointwise
profile, not the integrated inequality. Continue toward general n only
after global signs at both orders and an identified structural feature
that could extend; low-order success alone leaves all-n L966(16) and
mixed positivity open. Save partial reasoning if the bounded attempt
does not decide a sign. This review derives no new kernel or asymptotic.
Full matching Mathlib coverage is unknown and no Mathlib result is used.

The mathematical purpose is proof_attempt/creative: the changed
compensation is a concrete new mechanism at the central sign gap, while
the representation and calculus are established inputs. The bounded
test and decisive evidence above are required, with no repeat approval
of the unchanged detector or old-profile audit.

## Original nomination — step174, preserved

## Relevance and bounded discriminator

The main gap remains L030-L032/C032a actual-Xi mixed positivity;
the current route's unpaid condition is all-index L966(16).
L968 now validates the sufficiency of that condition. The proposed
intermediate target is a different, explicitly specified way of
spreading the boundary masses in the existing exact numerator.
An eventual full-orthant certificate at the two small orders could
identify a mechanism to develop for general n. It would itself
establish only those test orders, with all-n closure still unresolved.

L967's negative ray identifies the distant derivative as a concrete
obstruction to the old profile. Including that very H_1(h,u) factor
in the proposed density is the new idea to assess, not evidence that
it works. The denominator uses L967's existing actual integrals,
not a fitted sign, an unknown positive part of Q, or a zero location.
No new transfer, sign, asymptotic or normalization lemma is derived
in this nomination. The old profile remains stopped.

The next turn is literature-only. Search the exact profile and the
standard boundary-measure redistribution and theta-integral terminology;
reuse the already inspected calculus and probability coverage where
its hypotheses match. Inspect primary hypotheses and relevant proof
cases before approving an attempt. Compare any proposed positivity
input with the complete signed Bell numerator, rather than inferring
it from positive ordinary moments or an unsigned partition formula.
Do not reopen blocked source retrieval unless an essential new
theorem has been identified. No mathematical script is authorized
until this changed target has ready coverage saved before invocation.

If coverage permits a later attempt, substitute this one fixed profile
in the already complete face sums; do not repeat the derivation of
L966/L967. Test both n=2 and n=3, including origin intersections,
one-coordinate escape and competing-coordinate escape regimes.
A rigorous negative point or ray at either order abandons this
pointwise profile; it would not refute the integrated inequality.
A finite positive grid is insufficient. Continue toward general n
only after a proved full-orthant sign at both orders and an identified
structural feature that could survive growing n. Otherwise retain
partial reasoning and require materially new input before repeating.

The step158 finite Li-window/mixed-degree import limit remains separate.
The step168 fixed-profile stop is the motivating obstruction, not a
global ban on other profiles. The 6 November connected-partition stop
and 4 November Conrey-Ghosh transfer stop rule out automatic generic
sign imports; no new cumulant hypothesis is smuggled into this target.
Full matching Mathlib coverage is unknown and no Mathlib input is used.

Essential prospective inputs are L019/L966/L967, with L968 explaining
downstream sufficiency and L018/L024/L026 maintaining the actual-node
framework. The profile sign, general-n construction, all-n inequality
and RH remain unresolved. No cross-notebook result is proposed.
After a separate ready source review, the mathematical purpose would
be proof_attempt/creative: test whether this concrete derivative-aware
profile repairs the specific ray obstruction at the central sign gap.
The decisive evidence must be an exact global certificate or a rigorous
negative configuration, not a changed label or another approval audit.
