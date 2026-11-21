# Actual contact flux: two-cancellation integrated-tail coverage

TARGET: Assess primary coverage for a two-cancellation integrated-tail criterion for L874's d=2 flux using L915's actual tilted dilation score on 0<lambda<1/20.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step187 reused the step183 generalized-convex comparison, November6 score comparison, degree-nine polynomial-dual pilot and the recorded automatic-sign/one-crossing stops; inspected L019/L058/L874 and L915's definitions, cancellations and support qualifications. New exact/stronger generalized-convex, unbounded convex-order, theta dilation-score/contact and integrated-tail queries are recorded below; no matching actual-contact sign theorem was inspected, and no novelty claim follows.
SOURCE_EVIDENCE: Karlin–Novikoff, Pacific J.Math.13(1963),1251–1279, Section1 pp1252–1253 (i)–(iii), identity(A), Section3(15)–(20), Theorem1 p1264 and LemmasA/B pp1265–1266, https://msp.org/pjm/1963/13-4/pjm-v13-n4-p18-s.pdf ; Leskela–Vihola arXiv:1404.0999v3 (30October2015), Section2.2 Proposition2.3/Remark2.4 p5, https://arxiv.org/pdf/1404.0999v3 ; Csordas arXiv:1309.0055v2 Theorems4.1/4.2(b), https://arxiv.org/pdf/1309.0055v2 , reused through L915 without re-audit.
COMPARISON: The known dual criterion separates a signed integrated residual from comparison-cone membership, rather than requiring one crossing. Ordinary convex order after the proposed score-coordinate change gives a concrete hinge-integral test and inverse-score convexity test; neither is supplied by L915's decreasing score or two cancellations. The unbounded-interval probability formulation avoids importing an unspecified infinite-interval differential-operator extension, but local pushforward, normalization and integrability checks remain unpaid.
GAP: Establish applicability and the two independent sign/shape premises for the actual law; no half-line specialization, inverse-score curvature, integrated-residual sign or flux inequality is proved in this literature turn. The next bounded test isolates inverse-score convexity at lambda=1/40 before any contact-dependent residual work.
REASON: Source scope now supports a concrete, independently testable comparison proposal, not automatic theta positivity. Continue first on its shape prerequisite; abandon this global-convex comparison if the actual inverse score has a rigorously certified negative curvature anywhere at the fixed parameter. A failure would stop this sufficient comparison only, not refute the desired flux or RH.
LITERATURE_REASON: The changed hypotheses are the unbounded actual tilted score as a second test function, the x^(-1/2) density on an infinite interval, and a signed integrated-tail criterion in place of a one-crossing premise. Reuse existing theorem extractions; retrieve only missing hypotheses or an essential new lead.
SCOPE: Completed literature-only comparison for the stated d=2, low-time actual-law target. No lemma, mathematical script, specialization proof, contact search or curvature calculation was produced. A separately saved continuation receives next-turn approval; no research was invoked here.

## Completed source comparison — step187, 9 November 2026

The main gap is L030–L032/C032a actual-Xi all-degree mixed positivity.
The intermediate target is a sufficient two-cancellation comparison for
the L874 flux, potentially yielding a theta-specific boundary test.
Acceptance requires conditions independently testable without the flux
sign; a reformulation alone or another one-crossing premise is rejected.

### Reused evidence and primary passages

The step183 assessment and the November6 score assessment already rule
out automatic variation/Stein/GHS imports at their stated scopes. Read
their source comparisons and the corresponding automatic-sign stops,
plus step184's stop and step186's audit update. The degree-nine
density-dual pilot uses a fixed pointwise multiplier class at d=1 in
a different parameter band; it is not this score-coordinate comparison.
No prior completed actual-score integrated-tail test was found in the
specific November9 contact assessments and stops searched. This limited
duplicate check does not establish originality. L874's older unaudited
label in the November6 note is superseded by its canonical audit.

Karlin–Novikoff Section1 characterizes signed measures nonnegative on
convex tests by zero mass, zero first moment and a nonnegative second
primitive. Identity(A) uses two integrations by parts. Section3 uses
positive smooth weights on a finite interval; Theorem1 requires all
moment cancellations and a nonnegative iterated primitive. Its proof
uses endpoint cancellations for sufficiency and arbitrary positive
differential images for necessity. The following measure version and
both LemmaB proof cases were read. Minimal crossings are sufficient,
not required by Theorem1. Infinite-interval modifications are left to
the reader on p1263.

The primary web extraction of those pages is readable for these
conditions and proof cases, but loses some operator/determinant
typography. Screenshot requests returned placeholders, not viewable
images; shell retrieval failed DNS. No missing high-order display is
used. The proposed ordinary-convex formulation below bypasses those
displays. Stanford's report catalog was inspected only for a possible
alternate copy, not used as theorem evidence.

Leskela–Vihola v3, Proposition2.3, assumes integrable real random
variables, without compact support or smooth densities. It characterizes
convex order by all absolute-value tests and increasing convex order by
all positive-part tests. Remark2.4 permits rational thresholds. The
statement cites Shaked–Shanthikumar, *Stochastic Orders*, Theorems3.A.2
and4.A.2; that book proof was not read. This primary proposition is
sufficient as a named input; no reproof or coupling theorem is needed.

### Explicit proposal and unpaid specialization

Keep exactly L915's Q, nu_lambda and sigma_lambda; do not replace the
law. For source comparison, propose the coordinate h_lambda=-sigma_lambda
and the signed weight -Q dnu_lambda. Its nonzero positive and negative
parts would be normalized to probability laws and pushed forward by h.
The candidate residual to test is

    A_lambda(t)=integral (h_lambda(x)-t)_+*(-Q(x)) dnu_lambda(x),
    A_lambda(t)>=0 for every real t.

The proposed comparison observable is the inverse h_lambda^(-1) on
h_lambda((0,infinity)); the proposed shape premise is its convexity.
These are requested applicability/sign tests, not established local
identities or inequalities. The intended sign is integral x*Q dnu<=0.
The signs of -Q, the positive-part orientation and the inverse observable
must be checked explicitly in a later specialization. In particular,
using inverse concavity would require a different order orientation;
neither reversing a sign nor asserting exactly two crossings is licensed.

L915 supplies strict monotonicity of h, both existing cancellations,
and absolute integrability of Q, xQ and sigma_lambda*Q. Thus the named
inputs provide a plausible interface to finite-first-moment probability
order, rather than an inaccessible endpoint theorem. The later argument
must still pay for pushforward measurability, nonzero equal normalizing
masses, first moments, equal means, the inverse's domain and endpoint
extension, integrability of its test, and the passage from the named
probability statement to this signed application. No truncation may
pretend to preserve either cancellation. The density remains singular
like x^(-1/2) at zero. If working instead with the generalized differential
operator, its weighted boundary products must be proved separately.

Csordas's assessed concavity of log Phi(sqrt(x)), as used in L915,
does not state convexity of this inverse dilation score. L915 proves
a first-score-derivative sign only. No higher derivative or inverse
curvature follows by citation from that statement. The hinge conditions
test a full comparison cone, not just the single desired observable;
they are a stronger candidate sufficient premise, never a demonstrated
theta fact or an equivalent solution of the main gap.

This review therefore isolates an independent shape test. First test
inverse-score convexity at lambda=1/40 on its entire image. One rigorous
negative-curvature witness for the full theta kernel rejects this
global-convex sufficient comparison without finding a contact. A positive
result at that parameter would leave other parameters, the residual
sign, all endpoint checks and the flux unpaid. No inference from a
finite truncation or sampled graph is permitted. The later assessment
is `drafts/literature/2026-11-09-inverse-dilation-score-convexity-test.md`;
it is newly saved and requires separate approval before mathematics.

### Search scope and limitations

New queries included `generalized convex order Chebyshev system integrated
criterion two functions Karlin Novikoff unbounded interval`, `Riemann
theta dilation score Hankel contact integrated tail sign`, `convex order
stop-loss finite first theorem signed measure`, `Riemann theta log Phi
convex sqrt Csordas`, and `Leskela Vihola conditional convex orders
measurable martingale couplings arxiv convex (x-t) positive part theorem`.
Followed the primary Karlin–Novikoff paper and Leskela–Vihola v3 to the
stated passages. A search lead titled *Curvature Transition Layers and
Paired-Tail Positivity for the Riemann Xi-Function* was not inspected;
its title/abstract is not evidence for this normalized contact theorem
and it is not an essential input to the named convex-order test. Other
search snippets and secondary summaries are not mathematical inputs.
No exhaustive search or novelty claim is made.

Outcome EXPLORATION: new source comparison with an actionable independent
test, not a mathematical advance or an informative actual-theta negative.
Full/supporting Mathlib coverage remains unchecked, not asserted absent.
Contact existence, residual sign, flux, initialization, tangency,
all-degree continuation and RH remain open. No cross-notebook input.
No lemma or mathematical script was edited or run; PROOF and DAG are
unchanged because no mathematical argument changed.

## Original nomination (preserved)

The main gap remains L030–L032/C032a actual-Xi all-degree mixed
positivity. The intermediate goal is a usable sufficient comparison for
the exact flux integral of x*Q(x) under L915's nu_lambda. Such a
comparison could identify a concrete theta-specific signed estimate
worth testing. Merely rewriting that flux or assuming its sign is not
progress. No assertion that the proposed criterion exists or holds is
made in this research-turn nomination.

Essential local inputs: L019/L058/L874/L915. Use the actual kernel,
real 0<lambda<1/20, nonzero real c=(c0,c1,c2), H2>=0 and all three
rows H2c=0. Keep every support pattern. L914 is optional only for
c2!=0, under its stated L037 arithmetic contracts. Q, nu_lambda and
sigma_lambda have exactly L915's definitions. The only established
sign-change conclusion is at least two, not exactly two. No sign of a
higher score derivative or of an inverse-score curvature is assumed.

The review should first reuse the step183 primary comparison and its
endpoint qualifications, then test the exact two-function application
against the known automatic-variation, score/GHS and one-crossing stops.
The degree-one polynomial-dual pilot is a different fixed pointwise
multiplier class, not an authorization to change this target's scope.
There is no need to repeat L915's successful audit or the original
theta shape proof.

Continue only if the review isolates one explicit integrated-residual
and comparison-shape test whose validity can be checked without the
desired flux sign or higher-degree positivity. Record every unpaid
theta and endpoint premise. Abandon this proposed application if it
only repackages the desired integral, requires the excluded one-crossing
pattern, or cannot yield an independently testable sufficient condition.
Any new mathematical target requires the appropriate saved assessment;
no mathematics is approved by this REVIEW_REQUIRED file.

Contact existence, flux sign, initialization, tangency, other parameters,
all-degree continuation and RH remain open. A sufficient conditional
criterion would not resolve those independent gaps. No cross-notebook
input. Full and supporting Mathlib coverage for this new comparison is
unchecked, not asserted absent.
