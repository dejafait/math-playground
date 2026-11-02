# Sextic damping and the monotone-Stein criterion: completed comparison

TARGET: Assess a Gaussian-damped sextic-law counterexample to monotone-Stein first-sign transfer using Newman necessity and a first-sign heat-collision test.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed exact/stronger sextic, Gaussian damping, Stein monotonicity, Laguerre-sign and collision searches; primary statements and necessity cases inspected below. Local L606, L605 and the C233b/L604/fixed-quartic stops distinguish previous failures. No matching counterexample with BOTH required properties was found in the inspected sources; no novelty or absence claim.
SOURCE_EVIDENCE: Newman https://sites.math.northwestern.edu/~auffing/papers/Newman.pdf Theorem 2/(1.8)-(1.10), pp. 246-247, full necessity proof pp. 248-251; Newman-Wu arXiv:1901.06596v2 https://arxiv.org/pdf/1901.06596v2 Sections 2.2, 2.5 and 3.2.1 Case 2, pp. 5-6,11,17; Csordas arXiv:1309.0055v2 https://arxiv.org/pdf/1309.0055v2 (2.1), Open Problem 4.7 and Proposition 4.9, pp. 2-3,12; Bagnoli-Bergstrom 2004 https://escholarship.org/content/qt0xt8k6sd/qt0xt8k6sd_noSplash_d3b995fc634e40551bbd3dc90a1b0e43.pdf Theorem 3/Corollary 2 p. 4 and Appendix 8.2 concave case p. 25. Saumard's centered ratio hypotheses reused from L606/L605; no sextic application performed.
COMPARISON: Known results classify all-damping real-zero preservation and explicitly list exp(-u^(2q)), q>=3, as finite-threshold examples. They do not supply the required negative first sign or a finite sextic collision. Hazard monotonicity provides a named spatial input, conditional on checking its auxiliary-density hypotheses. The distinct bounded test below measures the first sign directly rather than inferring it from nonreal zeros.
GAP: Sextic density/decay and global Stein-hazard applicability, a certified negative first-sign value, and any asserted finite collision remain mathematical obligations. A finite-threshold theorem does not discharge them. Actual-Xi transfer and all higher signs remain independent.
REASON: Missing essential source cases have now been inspected. Approve bounded exploration of the exact family only, with a direct first-sign acceptance test and no assumed collision. New target coverage is nominated separately for next-turn approval; no mathematics is derived here.
SCOPE: Source review only this turn. A future bounded test may specialize the hazard theorem and inspect one finite damping/frequency rectangle; Newman is imported, not reproved. No global parameter sweep or theorem asserting finite collision is covered.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED for Newman's unread necessity and the missing first-sign/collision interface; this is the first completed comparison of those cases, not extra browsing on a ready target.

## Original nomination (preserved; its pending language is historical)

The proposed object is the normalized family
\(p_b(u)=Z_b^{-1}\exp(-u^6-bu^2)\), \(b\ge0\), with
\(F_b(x)=\int_{\mathbb R}p_b(u)e^{ixu}\,du\) and
\(\tau_b(u)=\int_u^\infty v p_b(v)\,dv/p_b(u)\).
These are definitions for source review, not an established realization
or sign conclusion. The discriminating target would be some finite b>0
and real x with a rigorous negative first Laguerre form, together with
global nonincrease of tau_b on (0,infinity) and every original density
hypothesis. No parameter sweep, numerical search, derivative calculation
or proof of these obligations was performed during nomination.

The main gap remains actual-Xi all-degree signs at unbounded heights.
A valid counterexample would invalidate the generic monotone-Stein
transfer proposed for L605's actual-theta premise; it would not refute an
actual-Xi sign. All higher signs and any replacement transfer stay open.
The precise new question is whether a damping-path obstruction can give
the first-sign evidence absent from mere nonreal-zero location. This is
not the pointwise sign argument stopped in L604, the failed fixed-mixture
premise in C233b, or the quartic sufficiency calculation in L606.

First review Newman's necessity statement and essential proof cases,
and search exact/stronger Gaussian-damping, Laguerre and collision results.
Check any proposed monotonicity input with its full hypotheses. A moving
zero must not be assumed to cross the real line at a finite parameter:
entry from infinity and existence of an initial real-zero regime are
explicit unresolved possibilities. A negative first sign is stronger
evidence than nonreal zeros for this diagnostic, and cannot be inferred
from them without the missing argument. Import a matching theorem if one
is found; do not reprove it or infer novelty from an unsuccessful search.

Continuation test: source review must supply either a matching known
counterexample or precise ready hypotheses for one bounded damping-path
test of BOTH required properties. If the necessary first-sign interface
remains unspecified, record the blocker and park this mechanism; do not
renew it with a parameter change. Generic spatial monotonicity is not a
frequency-local sign theorem. This nomination approves no mathematics.

L606 supplies motivation and the closed quartic-model contrast only;
C233b, L604 and L605 are relevance/failure context, not premises for a
sextic result. No cross-notebook input. No new lemma or dependency is
asserted. Mathlib coverage is unchecked. A justified creative actual-Xi
attempt remains blocked by the absence of an independently controlled
signed remainder; this source task is not labeled creative to fill a quota.

## Completed comparison — 1 November 2026

No density calculation, Fourier evaluation, collision construction,
new lemma or mathematical script was undertaken. The new continuation
is [the finite test](2026-11-01-sextic-finite-first-sign-test.md); it
requires separate approval before invocation.

**Necessity cases inspected.** Newman, *Fourier Transforms with Only
Real Zeros*, Proc. AMS 61 (1976), 245–251, Theorem 2, assumes a finite
even nonnegative measure and imaginary zeros of its damped Laplace
transform for EVERY b>0. Its continuous class (1.8) has density
K*t^(2m)*exp(-alpha*t^4-beta*t^2) times the product of
(1+t^2/a_j^2)*exp(-t^2/a_j^2), where K>0, m>=0 is integral,
a_j>0, sum a_j^(-4)<infinity, and either alpha>0, beta real, or
alpha=0, beta+sum a_j^(-2)>0 (an infinite sum qualifies). Empty,
finite and infinite products are allowed. The other case is symmetric
two-atom measures; the completion also includes a mass at zero.
Only nonzero positive measures matter here. The complete necessity
proof, pp. 248–251, was read: Gaussian-convolution product reduction;
Lemma 1's bounded-parameter compactness; Lemmas 2–4's divergent-parameter
support restrictions; and the completion's atomic degenerations.
The lower bound (1.9) is a source conclusion, not a sextic comparison
proved here. Import this classification, rather than reprove it.
It gives neither a first-sign value nor a finite collision.

**Stronger lead, not the desired theorem.** Newman–Wu, arXiv:1901.06596v2,
13 March 2019, Section 3.2.1 Case 2, p. 17, explicitly lists
exp(-x^(2q)), q>=3, as finite-threshold examples. Their Gaussian
parameter has sign opposite to b. Section 2.2, p. 6, records Pólya's
undamped real-zero result. Neither passage supplies the threshold's
value, a finite collision, its multiplicity, or a negative first sign.
Section 2.5, p. 11, points to Simon–Griffiths, CMP 33 (1973), 145–164,
for some sextic Lee–Yang failures, without the required first-sign
witness for this exact family. The original Pólya and Simon–Griffiths
proofs were not read: these are motivation, not inputs needed for
the proposed direct determinant certificate. A Springer PDF request
redirected to an article page; no theorem was imported from that page.

**Collision scope.** Csordas v2, Proposition 4.9, p. 12, presupposes
a multiple real zero of the stated xi heat family and bounds its time
by the threshold. It does not produce a sextic collision or negative
first sign. Its cited original is Csordas–Smith–Varga, *Lehmer Pairs
of Zeros and the Riemann xi-Function*, PSAM 48 (1994), 553–556,
Proposition 1, p. 554. Direct PDF text was unavailable; an indexed
page describes a local-extremum argument but is only an unread
proof lead. No generic collision theorem is imported. Entry from
infinity remains unexcluded. Csordas (2.1) is a necessary sign for
Laguerre–Pólya membership, not a degree-one converse.

**Spatial scope.** Bagnoli–Bergstrom's Theorem 3/Corollary 2 assumes a
probability density, C1 and log-concave on its support interval, and
gives log-concave survival/nondecreasing hazard. The entire concave
case of Appendix 8.2 Lemma 4 was read. Its final sign/reference typo
is already recorded in L605; the preceding inequality and Remark 4
agree with the theorem. A sextic application still must check the
auxiliary normalization, weighted-tail coordinate change, concavity
and endpoint limits. None was calculated here. Saumard's centered
ratio is reused with connected support, finite absolute first moment,
and its boundary/integrability qualifications. Spatial monotonicity
does not itself sign a Fourier determinant. Mathlib coverage unchecked.

**Actual search and duplicate checks.** Queries included
`"exp(-t^6" "Laguerre"`, `Newman Fourier transform exp sextic Gaussian
all zeros real b 1976 necessity`, `"sextic" "Laguerre" "Fourier"`,
`"Gaussian" "Laguerre inequality" "heat" zeros`,
`"Stein kernel" "exponential power" monotonicity`, and
`Csordas Smith Varga "multiple real zero" "Proposition 1"`, plus
follow-ups to the named original references. Unrelated hits were not
inputs. L606's quartic stop, C233b's failed Stein premise and L604's
pointwise remainder stop are preserved. L605 is a methodological
example, not a sextic premise. The initial broad local keyword output
was truncated and does not establish complete archive inspection;
subsequent checks used the named proofs, assessments and stops only.

**Decision.** Source scope is adequate for one bounded test of BOTH
properties, using a direct first-sign certificate rather than an
unproved global collision inference. A heat-collision search may
locate a candidate; either directly enclose the determinant strictly
below zero or prove a local implication with certified hypotheses
and remainders. Verify global Stein nonincrease at the same parameter.
Nonreal zeros alone fail the test. If no witness is certified in the
saved budget, stop that finite test as inconclusive; neither positivity
nor a global family stop follows. No automatic parameter enlargement.

Outcome EXPLORATION: new source comparison and a specific known
finite-threshold lead, not a new mathematical result or a certified
counterexample. No mathematical exploration turn is spent or reset.
