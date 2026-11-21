# Integrated n=2 theta-moment test — completed source comparison

TARGET: Test an integrated theta moment/variance bound for Q_{1/5184}(2)>=0 using L966(12), retaining the even-block and distant-resolvent subtractions.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step183 compared the exact two-point target with ready Li/cumulant and covariance assessments, searched regularized-Li/theta, imaginary-axis logarithmic derivatives and tilted moment inequalities, and inspected primary hypotheses and quadrature error conditions below. No inspected match supplies the requested bound; this bounded search establishes no novelty.
SOURCE_EVIDENCE: Reuse Biane-Pitman-Yor Proposition2.1/Section2.3 from step167 and Carlen-Cordero-Erausquin-Lieb Theorem1.1/proof plus Csordas Theorem2.2/Corollary2.11 from step95; directly inspect arXiv:1106.0709v2 pp1-4, Csordas1998 pp37-42 and NIST DLMF3.5.1-3, version1.2.8. L019, audited L966, L967(5),(8), L969/C969a and L242 delimit the observable and failures.
COMPARISON: Ordinary Li signs and unweighted adjacent-moment inequalities omit the h-resolvent. Absolute BL covariance requires the chosen density's curvature and weighted integrability and supplies no two-point sign by itself. Rigorous quadrature supplies an enclosure method, not moment values or Q's sign. A fixed-index certificate would validate this local payment mechanism, not an all-degree or originality claim.
GAP: Establish effective enclosures for the actual b- and h-moment ratios and propagate them through the complete n=2 expression, including both subtractions. No enclosure, variance bound or sign is proved here; higher indices and main positivity remain open.
REASON: Approve one bounded integrated-moment attempt with proposed rational ratio boxes and rigorous quadrature/tail control, rather than automatic covariance import. The method and discriminator below are specified without deriving or approving previously uncovered mathematics as true.
LITERATURE_REASON: The integrated two-point observable was REVIEW_REQUIRED at startup; step167's transfer calculus and step95's Schur comparison do not assess a quantitative certificate for it. This completes essential coverage without repeating parked retrievals.
SCOPE: Fixed n=2,b=1/4,h=5184 and actual K,H_r,I_r,F of L019/L966; one effective moment-enclosure test of the full expression. No RH, simplicity, Stieltjes law, numerical moment premise, profile tuning, zero-free-region work or all-n extension. Optional covariance improvements are compared, not unchecked sign inputs.

## Completed review — step183

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity;
on this route it is all-index L966(16). The intermediate target is
exactly TARGET above. An integrated n=2 certificate would test payment
after the pointwise failures and provide a quantitative base case for
a separately justified higher-index mechanism. That mechanism and all
higher indices would remain unpaid.

### Observable, duplicates and retained failures

Read L966 in full, L019, the complete C969a proof/audit, L969's fixed
rule/audit, and L967's n=2 formula (5) and transfer (8). L966(12) is
the evaluation formula; L967(5) already lists its four signed tensors
and exact coefficients. The negative repeated-first-derivative block
and negative distant derivative are distinct obligations. No identity
is derived again. L242 already gives G'=E[b_x]+Var(a_x), G=F'/F,
under the actual cosh-tilted density. Read its entire proof and L046's
mixture-variance warning; renaming an identity does not bound its terms.

L967/L969 and audited C969a stop their fixed pointwise payment rules,
not an integrated inequality. Keep their negative regions and actual
normalizations. Preserve
`ATTEMPTS/2026-11-10-finite-li-index-mixed-degree-import-limit-158.md`:
a regularized fixed-index sign is not an ordinary Li sign, mixed degree
or all-n certificate. The scoped November10 Li/theta assessment/attempt
search located no duplicate certificate for this integrated n=2 target.
This is not exhaustive absence or novelty. No claim is made that other
existing zero-geometry methods cannot give this low-index sign; the
test concerns the nominated actual-moment mechanism.

### Source scopes checked

Reuse the ready comparison in
`2026-11-10-li-theta-ibp-remainder-review-166.md`: Biane-Pitman-Yor,
*Bull. AMS*38(4)(2001),435-465, Proposition2.1/(2.13), Section2.3/
(2.21)-(2.24), pp438-441,
[primary PDF](https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/biane-pitman-yor.pdf).
Its specific law has Mellin transform 2xi(s); its logarithmic cumulants
give the first two ordinary Li signs. Neither the new denominator nor
a distant-h estimate is supplied. No source reproof is needed.

Reuse `2026-11-07-logarithmic-hankel-schur-covariance-review.md`:
Carlen-Cordero-Erausquin-Lieb, *AIHP Probab.Stat.*49(2013),1-12,
Theorem1.1/(1.3)-(1.6), full proof pp2-5,
[published PDF](https://webusers.imj-prg.fr/~dario.cordero/Docs/articles/Carlen_CE_Lieb_IHP.pdf).
Directly checked matching hypotheses/formulas and the start of the
regularization/Poisson proof in
[arXiv:1106.0709v2](https://arxiv.org/pdf/1106.0709v2),24 October2011,
pp1-4. The normalized density on R^d is exp(-V), V C^2 with everywhere
positive Hessian. Tests are locally Lipschitz and square integrable;
the inverse-Hessian derivative norms require control. The estimate
bounds absolute covariance. The reused assessment includes the full
proof and limiting p=infinity case.

Our chosen density is L242's K cosh tilt. Base-K curvature does not
check the tilted potential; a full-line extension or half-line theorem
also needs justification. Even granting those hypotheses, an upper
variance bound alone does not lower-bound the whole signed two-point
expression. Step95's even-function improvement is a compared scope,
not a new quantitative input to retrieve. L048's local base-curvature
claim was read for context, not audited or used. Park automatic BL
payment for this test. The earlier Schur stop remains scoped to its
missing logarithmic interface, not a ban on actual moment estimates.

Csordas, *Convexity and the Riemann xi-function*, *Glasnik Mat.*33(53)
(1998),37-50,
[journal PDF](https://web.math.pmf.unizg.hr/glasnik/33.1/33105.pdf):
reuse step95's Theorem2.2/Corollary2.11 comparison; directly inspected
(1.2), Theorem2.2, Remark2.6, Definition2.7 and Theorem2.8, pp37-42.
The latter assumes an analytic, positive, even, decreasing admissible
kernel with rapid decay and square-coordinate log-concavity. It bounds
adjacent even power moments, including finite-cutoff boundary terms,
not a cosh-tilted two-point resolvent. Its triple-integral proof is not
imported or claimed fully audited. The previously checked scaling is
K(u)=4Phi(u/2); scaling or probability normalization does not supply a
missing tilted-weight theorem. No new specialization is derived here.

**Effective enclosure tool.** NIST DLMF version1.2.8, released
15 September2026,
[3.5(i), equations3.5.1-3](https://dlmf.nist.gov/3.5.i), read with
the C^2 hypotheses and error formula. For real f in C^2[a,c], the
composite trapezoidal sum of mesh delta=(c-a)/N has error

    -(c-a) delta^2 f''(xi)/12,  a<xi<c.

A proved supremum of |f''| gives an absolute enclosure. This is a
cited method, not a computed bound for our integrands. The attempt
must supply that bound, outward elementary-value enclosures and
explicit omitted-theta-summand and improper-u tails. L019/L966 give
compact smoothness and fixed-parameter integrability, but existential
constants are not effective certificates. The explicit positive theta
series is available to produce constants; standard nonnegative series/
integral comparison covers the method, with monotonicity and effective
constants still to check. Do not reprove the quadrature theorem. No
zero table or ordinary Li coefficient is an input to this method.

### One bounded mathematical test, not performed here

For the unchanged TARGET, try these conservative rational boxes for
the actual ratios:

    1/50 <= I_1(b)/I_0(b) <= 1/40,
    0 < I_1(h)/I_0(h) <= 1/100.

These are proposed thresholds, not estimates obtained in this review.
L966 already proves I_2(b)/I_0(b)>0. The attempt must first check
whether these boxes, that established positivity and the existing
n=2 coefficients give a strict positive lower bound when propagated
through all four terms of L967(5)/L966(12). No new scalar sign
implication is proved here. If propagation fails, report that failure.

Enclose I_0,I_1 at b,h on a fixed explicit finite interval and finite
theta truncation, with every omitted tail and roundoff error proved.
Common positive scaling at fixed x may avoid huge h-values only after
its exact ratio cancellation is justified. Lower denominator endpoints
must be positive. The positive I_2 contribution may conservatively use
its established lower bound zero; fully charge the negative squared
I_1 term. This is an integrated moment test, not a new pointwise
profile or marginal. It needs no new covariance identity.

Use one fixed initial certificate construction and at most one justified
precision/mesh refinement. Save exact formulas, effective derivative/
tail constants and all interval endpoints. Report actual/required
bounds and the complete signed lower endpoint. A floating point preview,
numerical moment premise or enclosure containing zero does not pass.
Failed boxes defeat this conservative test, not Q's sign. A certified
negative full upper endpoint would instead refute the nominated sign.
Any positive certificate requires later independent audit.

Continue after a successful base certificate only with a separately
assessed higher-index mechanism controlling the changing signed
partition; do not accumulate isolated finite signs. Abandon these
boxes if the bounded test fails, requires unknown Xi signs, or yields
only an unbounded restatement of Q>=0. No all-n or pointwise route is
globally banned. Low-index success alone does not justify generalization.

### Search record and disposition

Queries: `Riemann xi theta kernel variance logarithmic derivative
Brascamp Lieb inequality`; `Riemann xi logarithmic concavity imaginary
axis second derivative moments inequality`; `"Li" "regularized"
"theta" positivity resolvent`; `"xi" "moment" "cosh" "Turan"
inequalities theta kernel`; `"theta" "regularized" "Li coefficients"
variance`; `"xi" "logarithmic derivative" "5184"`. The inspected
sources above are distinguished from unread search hits. Recent kernel/
PF preprints and snippets were not imported; no assertion about their
full contents is made. Coffey and optional mean-comparison access
blockers remain parked without repeated retrievals. No essential source
blocker remains for this narrow enclosure method; success is unverified.

Outcome EXPLORATION: completed source/method coverage and a concrete
test, not a sign or discovery beyond the checked sources. No lemma,
mathematical script, DAG or PROOF argument changed. Full matching
Mathlib coverage for Q or these boxes is unknown and was not checked;
no library theorem is asserted to supply the missing sign. Essential
inputs are L019 and audited L966, plus existing L967(5),(8) coefficients/
normalization. L242 is comparison only and L969/C969a are retained
obstructions. L018/L024/L026 are inherited through L966. Effective
constants, ratio boxes and signed propagation remain unproved. No
cross-notebook input is used. The completed assessment prepares this
same target for separate supervisor approval, then one calculation.

## Original nomination — step182, preserved

The following records the initial status; its REVIEW_REQUIRED decision
is superseded by the completed EXPLORE assessment above.

The completed step182 target is the independent C969a audit. This new
assessment is deliberately REVIEW_REQUIRED. Its TARGET preserves the
proposed mathematical test; the next invocation is a literature-only
comparison of that exact target, not a variance calculation.

The main gap remains L030-L032/C032a all-degree positivity, on this
route all-index L966(16). An integrated bound at n=2 would verify one
index and assess a payment mechanism unaffected by a small negative
pointwise region. It would leave every higher index unpaid. The new
test concerns aggregate moment control, not a further pointwise
marginal sign, a profile adjustment or repetition of C969a's limit.

Essential inputs are L019 and audited L966, with audited L969 and
C969a specifying the preserved negative-region limitations. The
L018/L024/L026 analytic and node framework is inherited through L966.
No cross-notebook result is proposed. The moments and normalization
must remain actual; no positive Stieltjes law, RH-dependent variance
bound, unverified finite-height sign or assumed cumulant sign is allowed.

Reuse the ready source work in
`2026-11-10-li-theta-ibp-remainder-review-166.md`: Biane-Pitman-Yor,
*Bull. AMS* 38(4) (2001), 435-465, Proposition2.1/(2.13) and
Section2.3/(2.21)-(2.24), as actually inspected there. Its ordinary
first two Li signs supply no automatic regularized sign. Read primary
hypotheses only for an essential changed inequality. The prior optional
Coffey/mean-comparison access blockers remain parked. Do not repeat
blocked retrievals merely to fill this review. Also preserve
`ATTEMPTS/2026-11-10-finite-li-index-mixed-degree-import-limit-158.md`:
a finite ordinary Li index is not a mixed degree or this observable.

Continue only if the review supplies an applicable theorem, or identifies
a concrete quantitative variance/moment estimate with adequate method
coverage and a bounded discriminating test. If the proposed bound merely
restates Q_eta(2)>=0, relies on RH, or imports ordinary Li positivity
without the missing regularization argument, abandon that mechanism
and nominate a materially different target. No sign, estimate, covariance
identity or novelty is established by this nomination. Full matching
Mathlib coverage is unknown. Separate source approval is required.
