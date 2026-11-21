# Actual-theta contact node-mass source comparison

TARGET: Assess whether actual-theta d=2 contact measures satisfy the nodewise restriction t(w_t-t^2)<=0, using kernel-specific hypotheses rather than finite ordinary moment compatibility.
CHECKED: 2026-11-21
DECISION: EXPLORE
SEARCH_EVIDENCE: Step2139 completed bounded exact/stronger-result searches for theta logarithmic-Hankel contact masses, reciprocal-zero multiplicities, Christoffel weights and quadratic-tilt cumulants; reused finite-moment, score/GHS and modular comparisons and checked recorded H2 stops. No inspected result supplies the restriction; search failure establishes neither novelty nor nonexistence.
SOURCE_EVIDENCE: Lasserre-Pauwels arXiv:1701.02886, Section3.1 (3.1)-(3.2), Theorems3.1/3.3, PDF pp7-8, complete Section6.2 proof p21; reused Curto-Fialkow1991 Theorem3.1/Lemma2.3 via C874b, Choi2611.04359v1 Theorem4.1/(19)-(20) via the ready low-time-H2 comparison, and the ready November6/9 score reviews. BPY2001 Proposition3.1(i) statement was inspected only as a continuation lead, not a contact theorem.
COMPARISON: The nonsingular Christoffel inverse formula is not applicable to singular H2; no theta-to-auxiliary measure comparison was found. Real-zero Gram structure lacks its premise below the known cutoff and does not identify finite contact masses. Checked theta shape/Stein/GHS observables do not imply this bound; C874b-d already defeat generic finite extensions/ordinary-prefix compatibility.
GAP: A kernel-specific relation between the actual density and the auxiliary logarithmic-coefficient atoms, strong enough to control each w_t relative to t^2, remains missing. No actual contact, violation or signed estimate was established.
REASON: Park nodewise signing: this bounded review found no independently sufficient theta estimate or justified mathematical test. EXPLORE records source discovery/comparison only; a distinct distributional-identity interface is nominated separately with REVIEW_REQUIRED, not derived or approved here.
SCOPE: Source review for real 0<lambda<=1/8, the exact L058/L874 theta family, H_3>=0, H_2 c=0 with real c!=0 and S_2>0, and C874b's distinct real contact roots t and positive masses w_t representing S_2,...,S_7; no all-degree positivity premise or actual contact existence is assumed.
LITERATURE_REASON: The saved target had REVIEW_REQUIRED coverage; ready finite moment theory covers auxiliary representation but not the actual-kernel mass restriction. This is the required changed-observable comparison, not a repeat of finite compatibility.

## Completed source review — 21 November 2026, step2139

The main gap remains L030-L032/C032a actual-Xi all-degree algebraic
mixed positivity. The intermediate target is exactly TARGET; its possible
use is C874b's contact flux sign. Actual H3 positivity, contact existence,
initialization, equality and all-degree continuation would remain open.
The continuation test was an applicable primary theorem or a sufficient
kernel-specific estimate with a bounded independent discriminator. No
such input was identified. This is not a proof of falsity or impossibility.

### Three formulations compared

1. **Quadrature/Christoffel control.** Jean B. Lasserre and Edouard
   Pauwels, *The empirical Christoffel function with applications in data
   analysis*, [arXiv:1701.02886](https://arxiv.org/pdf/1701.02886),
   downloaded 21 November2026, PDF pp7-8, Section3.1, (3.1)-(3.2),
   Theorems3.1/3.3, and complete Section6.2 proof, PDF p21, were read.
   The setup assumes a finite Borel measure with all moments and positive
   definite moment matrices. The variational minimum of the integral
   of P^2 with P(x)=1 is the reciprocal evaluation-kernel diagonal.
   The optimizer proof uses a matrix inverse and strong convexity.
   This is not a singular-contact theorem. No singular extension,
   atom-mass specialization or new inequality is proved here. There is
   no comparison between the physical u-law and auxiliary t-law; H2
   is singular at the proposed contact. A pseudoinverse substitution
   is not licensed by this source. Reuse C874b's precise Curto-Fialkow
   citation for the valid singular representation; its audited examples
   already prevent generic positive extensions from supplying the bound.

2. **Reciprocal-zero weights.** Reuse Choi v1 Theorem4.1, its full proof
   and (19)-(20) as inspected in
   [the low-time H2 comparison](2026-11-09-low-time-h2-contact-exclusion-review.md).
   That assessment checks K/4, a=lambda, and the unconditional real-zero
   regime lambda>=1/20 using the cited Platt-Trudgian result. The
   lower-time interior lacks that premise. An infinite reciprocal-zero
   Gram law is not an identification of C874b's at-most-two atoms.
   No product or multiplicity specialization is derived. Present Choi
   HTML line/find requests timed out; adequate saved coverage is reused,
   without claiming fresh inspection of unread passages. Polymath,
   [arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2), introduction
   (1)-(4) and the following transition paragraph, was readable. Its
   global real-zero transition does not supply the finite mass estimate.
   No source-access retry is nominated.

3. **Kernel score/correlation control.** Reuse
   [the November6 comparison](2026-11-06-actual-theta-contact-score-pairing.md)
   and [the scoped November9 review](2026-11-09-actual-theta-score-contact-41.md).
   Their positive-tilt, unbounded-test and GHS-cone qualifications are
   unchanged. Absolute covariance/variance bounds and scalar susceptibility
   signs do not identify these auxiliary masses. The proposed pointwise
   score correction is another unpaid inequality, not source evidence
   for this target. November9 records L874's completed step11 audit,
   correcting the older unaudited description; no repeat audit is needed.
   The modular review likewise supplies no specified signed operator.

Negative/zero roots, lower-degree p and repeated roots remain in scope
as in C874b. No positive-support assumption was added. Generic laws are
not actual-theta counterexamples. Full and supporting Mathlib coverage
of the nodewise claim is unchecked; no absence is claimed.

### Search, duplicates and decision

Queries actually used included `Riemann Xi theta kernel Hankel cumulants
finite rank contact measure Christoffel weights heat flow`, `Riemann xi
reciprocal zeros moment Hankel singular finite rank multiplicities theta
kernel`, `de Bruijn Newman heat flow zeros multiplicities logarithmic
derivatives theta kernel theorem`, `Christoffel function atom weight
moment upper bound theorem`, `theta kernel cumulant Hankel positivity`,
`Riemann Hankel contact weights`, `Christoffel function extremal property
atom mass positive moment matrix Lasserre Pauwels pdf`, and `theta Hankel
positive quadratic tilt determinant`. Snippets, secondary reposts and
apparent RH claims were discovery aids, not theorem evidence.
Lasserre's [disintegration paper](https://www.numdam.org/item/10.5802/crmath.380.pdf),
Section2.1 (3)-(5), was also read: its inverse setup assumes nonsingular
moment matrices and does not repair this interface. It is not an input.

Read C874b's complete finite proof, L874's actual-law definition and
recurrence, L058's analytic setup, the C874c/d stated finite-law scopes
and the two nominated stops. Reused ready finite moment theory rather
than browsing it again. Narrow H2 comparisons also locate the recorded
full-moment box, shared-parameter Taylor, finite-head/tail and energy-cell
tests; none becomes fresh merely by renaming its objective. No stopped
certificate or mathematical program was executed.

Park nodewise signing until a materially new actual-kernel estimate
appears. The blocker for a creative attempt is the missing controlled
kernel-to-auxiliary interface and bounded discriminator, not a global
ban on contact work. Outcome EXPLORATION, LITERATURE,
NOVELTY_UNCHECKED: no mathematical advance, new negative theorem,
novelty claim or exploration-budget reset. PROOF.md/DAG.md, lemmas and
mathematical scripts are unchanged; unfinished work is preserved.

A narrow new lead is Biane-Pitman-Yor, *Bull. AMS*38(4)(2001),435-465,
DOI10.1090/S0273-0979-01-00912-0,
[primary PDF](https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/biane-pitman-yor.pdf),
Section3.6 Proposition3.1(i), p446. Its size-bias statement and paragraph
pointing to proof references were read; those proofs are unread. The
ready Li/theta assessment covers its different Section2 interface,
not this tilted identity. No transform to L058 or sign is asserted.
The [separate nomination](2026-11-21-theta-size-bias-contact-nomination-2139.md)
requires source comparison before mathematics. No cross-notebook input.

## Original nomination — preserved, not the completed decision

This is a nomination, not approval or a new lemma. Its possible use is
through the existing C874b formula

    Phi=8 sum_t w_t t p'(t)^2 (w_t-t^2).

The proposed nodewise restriction asks for more than the aggregate
signed bound. It may fail or be needlessly strong; no evidence for it
is asserted. It is not furnished by the ordinary probability law
constructed in C874d. Negative and zero roots, lower-degree p and
repeated roots must remain in scope; do not silently assume positive
support or simple full-degree roots. S_2=0 already has its separate
audited zero-flux branch in C874b.

Essential local inputs for the later source comparison are
C874b,C874c,C874d,L058,L874 and the preserved stops
`ATTEMPTS/2026-11-21-single-extension-contact-sign-stop-2128.md`
and `ATTEMPTS/2026-11-21-contact-joint-eighth-stop-2136.md`.
Reuse the ready finite moment-theory assessments without rediscovery.
For generic shape/score overlap, narrowly inspect the relevant scopes
of `2026-11-06-actual-theta-contact-score-pairing.md` and its named
failures before reading further sources. The modular-scale review
`2026-11-06-theta-modular-scale-invariant-discovery.md` already failed
to specify a signed operator; modular identity alone is not new input.

Continuation test: identify a precise primary theorem or an explicit
kernel-dependent inequality with checked hypotheses and a bounded
test that can fail independently of RH. Compare at most three concrete
formulations of that restriction if discovery is needed. Abandon the
nodewise mechanism if it only restates the flux, requires unproved
all-degree positivity, uses the same finite compatibility premises
already refuted, or supplies no independently testable kernel estimate.
Do not calculate new lemmas in the source turn or renew exhausted
extension/parameter sweeps. An unsuccessful search is not evidence
of impossibility or novelty.

Even successful conditional mass control would leave actual H_3
positivity, contact existence/continuation, initialization, equality,
higher degrees and the RH endpoint unresolved. It is a possible
intermediate target rather than a complete route. Full and supporting
Mathlib coverage is unchecked. There is no cross-notebook input.
A creative proof attempt is not yet justified: a usable actual-kernel
estimate and its bounded discriminator are missing. If the separate
review finds them, nominate its exact central mechanism with the
required escalation then; do not relabel this source comparison creative.
