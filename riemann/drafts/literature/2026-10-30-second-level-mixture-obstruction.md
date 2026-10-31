# Second-level curvature of the existing comparison family — source assessment

TARGET: Test whether there exists a_0 in (0,1/100] such that L055's kernels h_a satisfy f_a>0 and (log f_a)''<0 on (0,infinity) for every 0<a<=a_0, where s_a(t)=h_a(sqrt(t)) and f_a=s_a'^2-s_a*s_a'', or exhibit a rigorous violating pair (a,t) arbitrarily near a=0.
CHECKED: 2026-10-30
DECISION: IMPORT
SEARCH_EVIDENCE: Exact/scope searches recorded below located Schubr's finite-atomic second-level shape theorem; read its hypotheses and full relevant proof cases, not just its abstract. Compared L055's full proof, L050's different weights, L057's statement and the September 9/21 stops. No local second-level proof was found in these targeted records; no novelty inference follows.
SOURCE_EVIDENCE: Scott Schubr, Admissible kernel lifts with positive endpoint forms and nonreal Fourier zeros, public Edition 2 (27 October 2026; manuscript 24 October), Section 2 equations (1)-(3), Theorem 2; Section 3 Theorem 3, Lemma 4 and equations (9)-(15), printed pp. 2-6, https://research.luminaryoddities.com/admissible-kernel-lifts-positive-endpoint-forms-nonreal-fourier-zeros/v/2/files/Paper.pdf . Exact theorem and relevant analytic proof read; no independent manuscript/certificate audit or local application completed. Planat--Sole and Csordas scope retained below.
COMPARISON: Schubr's theorem covers the positive even finite-atomic cosh mixtures containing L055's exact family, with explicit small-diameter and weight-ratio hypotheses and closed-half-line signs. Thus an original compact/tail perturbation proof is unnecessary if the uniform parameter conditions are verified. The exact a_0 and applicability proof remain for the mathematical turn; Planat--Sole's theta-only theorem alone would not cover h_a.
GAP: No local second-level sign has been established this turn. Verify uniform small-a applicability of Theorem 3 at the fixed base scale, including varying weights, normalization and t=0; do not substitute the theorem's optional L>=1 sufficient scale for its primary hypotheses. Actual-theta mixed positivity and the collision implication remain open.
REASON: New primary-source overlap changes the proposed proof route to a known theorem application. Approve only that import and its necessary uniform specialization, with the preprint qualification retained; no independent reproof, new kernel search or creative RH mechanism is justified by this target.
SCOPE: Only L055's exact normalized h_a, its parameter a and the displayed second-level curvature; no heat-family realization, collision exclusion, infinite-degree positivity, or transfer to the actual theta kernel is proposed.

The main gap is all-degree mixed positivity for actual Xi. The plausible
use of a positive answer is to test whether a newly available stronger
kernel condition distinguishes actual theta from the existing nonreal-zero
models. A negative answer instead identifies why this particular family
cannot supply that strengthened obstruction. Neither answer proves RH.
No further generic-shape refinement is justified merely by passing a
finite grid or repeating L055's old first-level proof.

Essential local inputs: L055's exact formula and all-small-a qualifications;
L057 only if retaining any fixed finite set of mixed forms in a later
consequence. L050 is a proof-method comparison, not a replacement for
L055's different weights. No cross-notebook input is needed. Matching
Mathlib coverage remains unchecked.

The later bounded mathematical test should begin at the exactly defined
base a=0, h_0(u)=exp(-cosh(2u)), and at the analytic t=0 extension, retaining
the first nonzero parameter terms if an equality occurs. These are tests
to be made, not calculations performed in this literature turn. Continue
to a global perturbation argument only if the base and endpoint tests
support a strict sign with a justified margin; then separate a fixed
compact interval from the unbounded tail. A sign violation at one fixed
a does not negate existence of a_0: a negative resolution needs violations
at arbitrarily small a or a proved limiting/parameter obstruction.
Unsuccessful local evidence should park this family rather than start an
unbounded search over kernel variants. The source review may narrow the
first attempt while keeping these quantifiers explicit.

The preceding test plan is preserved as the original nomination, not as
an instruction to reprove a now-covered general result. The completed
review below replaces its original REVIEW_REQUIRED decision. No proposed
sign was derived during this approval turn.

## Completed review — 30 October 2026

The main gap remains actual-Xi all-degree mixed positivity. The exact
intermediate target is the TARGET above. Its potential use is a stronger
comparison obstruction: determine whether the second shape condition
separates actual theta from L055's already explicit nonreal-zero family.
It is not a claimed actual-theta collision exclusion. Independent gaps
include realization, all-degree signs and C489a's qualified interfaces.

### Local comparison and preserved failures

L055 was read completely, including its uniform compact/tail argument
for the first square-root curvature and its weighted-family proof.
L050's full argument was read to distinguish its 9:1 multiplier from
L055's parameter-dependent weights. L057's statement was checked; its
finite mixed-form conclusion is not a second-level curvature theorem.
The September 9 superexponential-mixture stop and September 21 moment
screen, including its later resolutions, were read at their relevant
scope. They already defeat first-level and weighted-adjacent sufficiency;
they do not assert this new sign. The October 30 discovery assessment's
source-scope decisions are reused. Historical stops remain evidence,
not a prohibition on this changed hypothesis.

### Exact primary-source coverage

[Schubr, Edition 2, Theorem 3](https://research.luminaryoddities.com/admissible-kernel-lifts-positive-endpoint-forms-nonreal-fourier-zeros/v/2/files/Paper.pdf),
printed pp. 4-6, treats any nonzero positive even finite atomic measure,
with distinct atom positions, weights w_j, diameter D, weight ratio q,
T=binom(n,2)q, scale L>0 and Delta=D/L. Its kernel is
phi_L(x)=sum_j w_j exp(-cosh((x-a_j)/L)). The primary conditions are
Delta<=1/125, C_L<1/10 and B_8 T Delta<=1/4, where C_L is equation (3)
and B_8 is the explicit integer in equation (9). The conclusion includes
positive S_L'^2-S_L S_L'' and strictly negative logarithmic curvature
on the closed half-line, with an explicit margin. The optional sufficient
scale in equation (11) is stronger and includes L>=1; it is not a primary
hypothesis. This distinction is essential for the fixed base in L055.

Read the defining data on printed p. 3, Theorem 2's pair-suppression
argument on pp. 3-4, all of Lemma 4 on p. 5, and the coordinate identity
and Theorem 3 proof on p. 6. Those passages address global centered
moments, mixed cumulants, both integration-by-parts boundaries, the
removable endpoint and the final curvature comparison. Their existence
removes the need for an original unbounded-tail stability argument.
This is source comparison, not an independent audit of those estimates.
No source checker was run. PDF extraction was readable; screenshot
requests for two pages timed out and are not evidence of visual review.
The stable Edition 2 page reports SHA-256
`b204ae62af502437122e482681c6a8048e83789cac4475623a134d9bafe8fcfb`.
The search result's older Edition 1 description had different dates and
hashes; it is not the version used for this assessment.

The applicability task is precise: use the fixed cosh base scale matching
g, with atoms at -a,0,a and L055's weights. The measure varies with a;
pointwise applicability for one measure does not by itself establish a
single uniform a_0. Verify its weight ratios and all three primary
budgets uniformly, handle positive normalization, and retain the source
qualification in a canonical citation if the import succeeds. Do not
claim the sign now, use a fixed-shift failure to negate the target, or
infer it merely from continuity on an unbounded interval. Since the
source covers this class, the next task is KNOWN_IMPORTED, not a claim
of new mathematics. A fresh proof would need a specific source defect
or changed hypothesis; neither has been established here.

[Planat--Sole v1, Theorem 1.1](https://arxiv.org/html/2608.19160v1)
remains a theorem stated for the actual Riemann theta kernel. Rechecked
its defining normalization and statement; its proofs and certificates
remain unaudited. Rechecked
[Csordas v2, Theorem 4.2(b), Problem 4.14 and the adjoining explanation](https://arxiv.org/html/1309.0055v2):
the historical conjecture concerns the same second-level expression,
and its advertised coefficient consequence is a necessary condition,
not all-degree mixed positivity. Neither source supplies a missing
theta-to-collision implication. Csordas--Dimitrov, *Numerical Algorithms*
25 (2000), 109-122, Theorem 2.4, was located in an author-hosted search
result; its full original proof was not inspected and is not imported.
No such coefficient consequence is needed for the present target.

### Search record, decision and bounded next test

Queries: `"second level" "concavity" "cosh" kernel`;
`"exp(-cosh" "log" concavity Laguerre`;
`"Schubr" "finite-atomic" concavity`;
`"hyperbolic-cosh" "second-level"`;
`"Second-Level Concavity" counterexample mixture`;
`"exp(-cosh(2" "concavity"`;
`"second-level" "mixture" "concavity" kernel`;
`"Conjectures and theorems in the theory of entire functions" "2.4"`.
The exact-family searches did not provide a separately inspected matching
statement. The general finite-atomic theorem is the stronger relevant
coverage; failed exact searches are not novelty evidence. No sibling
notebook was read. Full matching Mathlib coverage remains unchecked.

Continue by checking the three primary budgets and the exact kernel
normalization uniformly as a decreases. If they hold, cite Theorem 3
and write only the necessary applicability proof. If a primary condition
cannot be paid, record that this sufficient theorem does not decide the
target; failure of a sufficient bound is not a violating pair. A source
defect or essential uncovered extension requires a new source gate,
not an improvised reproof. Passing a finite grid is never decisive.
This target is ordinary known-result application. A creative central
attempt remains unsupported without an independent actual-theta bridge.

Outcome: NEGATIVE overlap evidence displaces the proposed original
perturbation route; no theorem imported locally and no new result proved.
Mathematical exploration usage: zero. Once approved for invocation, reuse
this assessment for the unchanged TARGET without further browsing.
