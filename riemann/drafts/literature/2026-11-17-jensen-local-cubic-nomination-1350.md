# Actual Jensen local integral: completed cubic Taylor source comparison1351

TARGET: Assess whether replacing the actual Jensen local contribution on |theta|<=(log d)*d^(-1/3) by its exact degree-dependent cubic Taylor phase at theta=0 and constant amplitude a_q(0) has uniform additive error o(M_d(x)) for K=Q, q=q_e+x*d^(-2/3), 1<=x<=4, keeping C019c's radius, prefactor and both arc orientations.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1351 searched the exact identifier with cubic/Taylor/Airy and unshifted-Jensen cubic terminology; inspected Ono v1 and the Planat Theorem3 lead below. Reused assessments1344/1347, the automatic-Airy stop1345 and canonical C019c/C019d; no inspected source states this exact finite replacement. This bounded search establishes no novelty.
SOURCE_EVIDENCE: Ono arXiv2610.38870v1 (28 October2026), Sections3-5: (3.2), Lemma7/(3.6)-(3.11), Lemma8/(3.12), Lemma9 statement and complete proof, Lemma12/(4.3), (4.4)-(4.5), Lemma13's half-plane proof, Lemma14's exponential-comparison proof case, Proposition15/(5.2)-(5.5) and angular assembly; https://arxiv.org/html/2610.38870v1 . DLMF1.10(i)/(1.10.1) was inspected for analytic Taylor hypotheses; prior CFU/Olde Daalhuis-Temme comparisons are reused below.
COMPARISON: Ono's Lemma14 proof supplies an exact complex exponential-difference identity and a conditional contraction inequality; neither its Gaussian conclusion nor the prior Airy results are this Taylor replacement. Lemma9 states only first-through-third angular derivative bounds. C019d already proves normalized amplitude and actual theta-derivative bounds on a larger fixed interval. The remaining phase/remainder comparison needs an explicit specialization, not a general theorem reproof.
GAP: Establish a common fourth-derivative bound and branch at zero, control the shifted cubic exponential or the interpolation between exact and cubic phases, replace the amplitude using C019d, and integrate both errors on the unchanged M_d scale uniformly in x. The desired additive o(M_d) and its rate remain unproved.
REASON: Essential source coverage now suffices for one bounded mathematical attempt at exactly TARGET. Imported elementary comparison tools and existing amplitude control do not settle the actual phase estimates. SPECIALIZE authorizes testing those obligations after separate supervisor approval; it asserts neither a successful replacement nor a signed reference.
SCOPE: Exact TARGET including its finite I_3 below; same K=Q, source r(d,x), q_e(d), exact coefficients, P_d=d!/d^d and M_d(x). Established-route REPRODUCTION; no contour deformation, local sign, infinite Airy integral, reference lower bound or hyperbolicity assertion. A newly ready assessment receives separate approval before research invocation.
LITERATURE_REASON: The nominated local finite Taylor observable needs fourth-order and complex exponential-remainder coverage outside the ready annulus scope. Review1351 completes that missing comparison; no further generic Airy review is required for this exact test.

## Completed source comparison1351

**Precise imported comparison tool.** In the proof of Lemma14, just
before its central-interval error estimate, Ono v1 uses
\[
 e^{z_1}-e^{z_2}=(z_1-z_2)
       \int_0^1 e^{t z_1+(1-t)z_2}\,dt.
\]
Its stated bound by \(|z_1-z_2|\) requires both real parts to be
nonpositive. That requirement must be checked for any substitution;
the identity itself is available without that restriction. No such
check for the proposed cubic is made here. Lemma9's proof describes
the angular phase by a finite elementary-function basis, but its
stated derivative conclusion stops at order three. Lemma13's stated
local C1 norm uses the rescaled saddle coordinate, whereas its proof's
Euler-product bounds hold in the specified half-plane. Proposition15
requires \(n_q\geq1\) and retains a separate exterior error.
These source assertions do not state the saved finite cubic estimate.

**Taylor input and its limits.** The standard named Taylor theorem,
in analytic form [DLMF1.10(i), equation1.10.1](https://dlmf.nist.gov/1.10#i),
assumes analyticity on a disk. Its convergence statement alone provides
no degree-uniform fourth-order remainder constant. A later proof may
use Taylor's theorem with integral remainder on the real angular
interval, for a complex-valued C4 function, after verifying its uniform
fourth-derivative hypothesis. That is an elementary theorem application,
not a reason to reprove a general coalescing-saddle theorem. Neither
the fourth derivative nor a remainder rate was calculated in1351.

**Existing coverage reused.** C019c supplies the actual normalization,
uniform near-edge range and nonzero saddle scale. C019d's proof under
"Amplitude and its actual angular derivative" supplies B0/B1 on the
larger fixed lower interval, including zero; its conjugation argument
handles the upper arc. These are already proved inputs, rather than
an extrapolation of a rescaled local C1 assertion. Reuse their exact
constants and domains; do not reprove the exterior or annular payment.
Their phase-envelope input controls the actual exponential. It does
not by citation control the truncated cubic exponential.

Assessment1344 remains adequate for Chester-Friedman-Ursell,
*An extension of the method of steepest descents*, Proc.Cambridge
Philos.Soc.53(1957),599-611, Theorems1-2/Sections2-5,
[DOI](https://doi.org/10.1017/S0305004100032655), and Olde Daalhuis-Temme,
*Uniform Airy-type expansions of integrals*, SIAM J.Math.Anal.25(1994),
304-321, Sections3/5/Appendix,
[primary PDF](https://ir.cwi.nl/pub/1473/1473D.pdf).
Their assessed analytic cubic-map and contour requirements are not the
same observable as the original angular Taylor polynomial at zero.
No rereading, new import of their remainder constants or automatic
Airy/sign assertion is needed. The stop1345 remains in force for that
automatic import; it does not prohibit this finite replacement test.

**Obligations for the exact specialization, all still unproved here.**

- Verify the common branch and angular C4 control across zero on both
  retained arcs, using the exact phase and its degree-dependent
  parameters. Source order-three control alone is insufficient.
- Keep the constant and all three nonconstant Taylor coefficients.
  Check the real part of the cubic relative to H_q, or bound the full
  interpolation exponential in the imported identity. Do not assume
  that Taylor truncation inherits the actual phase's modulus bound.
- Apply the existing normalized theta-amplitude bound to the same
  interval and denominator. Include its variation and the phase error
  separately, with the full angular lengths, d in the exponent,
  factorial prefactor and d^(-1/3) normalization.
- Prove one uniform additive upper certificate tending to zero, or
  record the precise failed estimate. No division by a cubic integral
  or reference value is permitted. No infinite-interval completion or
  signed lower bound is part of this target.

This is adequate source coverage for an attempt, not verification of
these obligations. A failed proposed upper certificate stops that
certificate and need not refute the finite integral approximation.
No derivative, Taylor coefficient, new asymptotic rate, lemma or
mathematical script was derived or written during this literature turn.
Full matching Mathlib coverage remains unchecked.

## Bounded search and stronger-result check1351

Queries: `"2610.38870" cubic Taylor Airy`;
`"unshifted Jensen" "cubic" asymptotic`;
`"Jensen" "Ono" "Airy" 2026`;
`"2610.38870" "Taylor"`;
`"Jensen" "finite-strip obstruction" "1884"`.
Aggregator text and snippets were locators only. Direct primary v1 HTML
was readable, with displayed formulas; the PDF was also accessible.
Only the named phase, geometry, amplitude and comparison cases were
needed; no whole-paper or claimed Lean-artifact audit is asserted.

The search located Michel Planat, *Asymptotic Hyperbolicity of Jensen
Polynomials and the Finite-Strip Obstruction to the Riemann Hypothesis*,
Mathematics14(2026),1884,
[Section3.3, Theorem3](https://www.mdpi.com/2227-7390/14/11/1884).
Its inspected theorem states a large-shift condition n>=C_0^infinity*d^4.
That condition does not cover the unshifted n=0 observable. No theorem
or obstruction from that paper is imported, and its proofs were not
audited. This scope check suffices for the present lead; it is not a
claim that all its results have been compared or verified.

Named notebook searches covered the Jensen assessments1344-1350,
working notes1349/1350, stop1345 and canonical C019c/C019d. They found
no completed matching cubic replacement in those relevant materials.
No general novelty or absence claim follows. No essential source
blocker remains for this exact target. The initial notebook-scoped git
status output was oversized and truncated; it supplied no mathematical
evidence. Subsequent reads were narrow and all prior work is preserved.

## Exact proposed observable

Use C019c's data and \(\epsilon_d=(\log d)d^{-1/3}\). Define
\(I_{\rm loc}\) by C019d's actual Cauchy integral with angular set
\(|\theta|\leq\epsilon_d\), keeping both arcs counterclockwise.
On this neighborhood of the positive real axis use the common principal
branch to define
\[
 \Psi_{d,x}(\theta)=h_q(r^2e^{i\theta}),\qquad
 \mathcal T_{3,d,x}(\theta)=
   \sum_{j=0}^{3}\frac{\Psi_{d,x}^{(j)}(0)}{j!}\theta^j.
\]
The amplitude at zero is exactly C019c's \(a_q(0)\); the proposed
comparison quantity is the finite integral
\[
 I_3(d,x)=\frac{P_d a_q(0)}{2\pi}
       \int_{-\epsilon_d}^{\epsilon_d}
                   e^{d\mathcal T_{3,d,x}(\theta)}\,d\theta.
\]
The question is whether
\(\sup_{1\leq x\leq4}|I_{\rm loc}-I_3|/M_d(x)\to0\).
These definitions specify a test; they do not assert that it succeeds.
Keep the exact \(d,x\)-dependent Taylor coefficients, including the
constant term. A limiting phase with an uncontrolled
\(1/\Lambda\) error is not this target. Division is only by the
positive scale \(M_d\), never by a possibly zero cubic/Airy value.

## Relevance, discriminator and retained limitations

The main gap is still L030–L032/C032a actual-Xi all-degree positivity.
A successful replacement, combined with the audited C019c/C019d tails,
could reduce this bounded edge window to an explicit finite cubic
integral for a later real reference comparison. It would not identify
that reference, prove a nonzero signed margin, remove exceptional roots
or establish every-degree hyperbolicity.

In a separately approved research turn, continue only if a complete normalized additive
upper bound tends to zero uniformly in x. A failed modulus, derivative
or amplitude estimate stops that proposed certificate, not cancellation
itself. No calculation of Taylor coefficients or remainder rates is
performed in this turn. This is established-route development, not a
new creative central mechanism.

Retain the automatic-Airy stop at
`ATTEMPTS/2026-11-17-unshifted-edge-automatic-airy-import-stop-1345.md`.
The new usable evidence is the paid exterior and annulus, not an
assumption that the old missing local hypotheses now hold. Essential
inputs for any continuation are C019c/C019d and Ono's exact phase,
near-edge geometry and amplitude factorization. Uniform local remainder
control, a later signed reference and global root control remain
unresolved. Mathlib coverage for this proposed result is not checked.
