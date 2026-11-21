# Finite-degree inverse theta averaging: completed source review

TARGET: Assess whether the inverse of L795's actual theta averaging on real polynomials of degree at most three is variation diminishing on (0,infinity), and prepare one exact necessary-premise test for lower oscillation.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step615 searched finite multiplier sequences, inverse variation diminution, reciprocal moment multipliers and diagonal positivity preservers; primary statements and exact queries below. Scoped actual-theta records contain no matching inverse-quadratic test; no novelty follows.
SOURCE_EVIDENCE: Guterman–Shapiro, J. Fixed Point Theory Appl.3 (2008),411–429, author PDF https://staff.math.su.se/shapiro/Articles/FinalPosit.pdf Lemma3.2/full i=1 proof pp7–8 and Proposition3.10/full counterexamples p10; Branden https://arxiv.org/pdf/math/0403364v2 (29 September2004), Theorem3.14 p8; Kostov–Shapiro https://staff.math.su.se/shapiro/Articles/FinalNote.pdf Theorem1.3 p3; reuse step502's inspected Schoenberg theorem and sign-count convention.
COMPARISON: Finite multiplier criteria preserve real-rootedness rather than sign crossings. The diagonal positivity necessary condition supplies a quadratic diagnostic, but its whole-real-line statement does not automatically decide half-line inverse variation diminution. Generic positivity/inverse-hyperbolicity equivalence is explicitly false in the inspected source.
GAP: Separately verify the proposed finite inverse, strictness of the actual moment inequality using the Cauchy–Schwarz equality case, and positive-half-line crossing counts for the single nominated square. No actual witness calculation or inverse theorem was proved here.
REASON: Known quadratic positivity machinery makes a bounded reproduction feasible without a cubic sweep or RH-equivalent assumption; actual-theta specialization remains future mathematics. This source search supplies no theorem establishing the proposed universal inverse premise.
LITERATURE_REASON: Step615 required a literature-only review because inverse averaging on a polynomial class lay outside the compact-confluence coverage; the essential primary passages have now been inspected and the bounded next specialization is source-ready.
SCOPE: Completed literature comparison only. The separately saved quadratic-test assessment covers the later specialization; this Assess target authorizes no inverse proof, witness calculation, L821 extension or global sign theorem.

## Original nomination: object and decision test

Use the actual untruncated law dmu(u)=K(u)du/m_0 and moments m_j
of L795. The proposed averaging operator is

    (A_3 f)(x)=integral_0^infinity f(u^2 x) dmu(u),

on real polynomials of degree at most three. The proposed inverse
prescription is B_3(x^j)=(m_0/m_j)x^j, 0<=j<=3, extended linearly.
These definitions nominate the object; their inverse relation and any
oscillation property are not proved in step614. All moments must be
those of L019, with L021's finite positive-moment hypotheses retained.

The proposed necessary bridge is that the number of sign changes of
B_3 f on (0,infinity) never exceeds that of f for each nonzero real
polynomial f of degree at most three. Counts must distinguish simple
crossings from even-multiplicity zeros and handle degree drops and
endpoint zeros explicitly. A later justified application to an averaged
Laguerre reference could then seek a lower output count. No such
application, all-degree extension or mixed-sign transfer is asserted.

The source review should compare exact finite-multiplier/oscillation
criteria and stronger known obstructions before authorizing any test.
If a known theorem already decides this property under the actual
nondegenerate positive law, import it with precise hypotheses; do not
reprove it as new mathematics. Otherwise prepare one exact witness
test in this bounded class. An admissible f with strictly more positive
sign changes after B_3 rejects this proposed inverse premise, not RH
or every more restricted inverse construction. Passing a few tests is
not a theorem for all cubics, let alone all degrees. Source failure or
a known obstruction must be recorded without enlarging the class or
repeating forward-variation searches.

## Retained evidence and unresolved obligations

Essential definition inputs are L019/L021/L795. L821 is only the
completed compact diagnostic; no global positivity premise is drawn
from it. Reuse the step502 forward-direction stop and L795's
full-support interlacing obstruction. The common-Favard stop L796 and
step565's actual-theta adjoint source stop remain contrasts, not inputs
to an inverse theorem. The completed step567 three-mechanism discovery
does not cover this finite inverse premise. These stops are local;
none is treated as a global ban on theta research.

Main gap: actual-Xi all-degree mixed positivity. The proposed intermediate
target is only a bounded necessary test of one lower-oscillation
mechanism. The all-degree operator class, applicable sign-count theorem,
reference geometry, unbounded integral interface where needed and
mixed-positivity transfer remain unresolved. Full matching Mathlib
coverage is unchecked; no cross-notebook input is proposed.

No creative mathematical attempt is approved by this nomination.
A later creative route would require an independently justified signed
bridge and a precise bounded test, not merely a successful source review
or L821's positive compact cover. Review this changed target separately;
the completed L821 audit does not depend on its future outcome.

## Completed comparison — 5 November 2026, step615

The preceding nomination is retained as historical scope. This step
reviewed sources only; it did not test B_3 or settle its premise.
The result is EXPLORATION with an actionable, source-covered test,
not a new mathematical advance or an actual-theta counterexample.

### Primary coverage and its limits

P. Branden, *On linear transformations preserving the Polya frequency
property*, [arXiv:math/0403364v2](https://arxiv.org/pdf/math/0403364v2),
29 September2004, p8, definition and Theorem3.14: a real diagonal
sequence preserves real-rootedness for degrees at most n exactly when
its image of (1+x)^n has real roots of one sign. Only the first n+1
multipliers matter. The same criterion is stated in V. Kostov and
B. Shapiro, *On the Schur-Szego composition of polynomials*,
[author-hosted six-page PDF](https://staff.math.su.se/shapiro/Articles/FinalNote.pdf),
p3, Theorem1.3; its preceding definitions were inspected. These are
real-rootedness criteria, with multiplicities retained, not bounds on
crossings for arbitrary inputs. Neither theorem is applied to theta
in this review; its symbol has not been evaluated. No all-degree
multiplier extension is asserted.

A. Guterman and B. Shapiro, *On linear operators preserving the set
of positive polynomials*, J. Fixed Point Theory Appl.3 (2008),411–429,
[publisher record](https://link.springer.com/article/10.1007/s11784-008-0084-3),
[unversioned author PDF, accessed 2026-11-05](https://staff.math.su.se/shapiro/Articles/FinalPosit.pdf).
Lemma3.2, pp7–8, gives lambda_1^2<=lambda_0*lambda_2 as necessary
for a diagonal positivity preserver when degree two is available.
Its full i=1 proof uses strictly positive quadratics and their
discriminants. Definitions distinguish positivity from nonnegativity.
Proposition3.10 and its counterexamples, p10, disprove the claimed
general equivalence between diagonal positivity preservation and
inverse hyperbolicity preservation. The infinite Hankel/moment
criterion in Theorem3.4, pp8–9, was inspected but is not imported
as a finite half-line theorem.

The full-support Cauchy–Schwarz equality case and elementary quadratic
formula are sufficient tools for the proposed specialization; L021's
weak moment inequality alone does not record the needed strictness.
The change from all real x to x>0 must be justified through the
specific quadratic, including the locations and parities of its zeros.
Thus failure of a whole-line positivity hypothesis is not silently
declared a half-line sign-count counterexample.

Reuse [step502](2026-11-05-theta-log-dilation-variation-diminution.md)
for Schoenberg's bounded-input convolution theorem and the count
defined by ordered nonzero sample values. Zeros do not receive signs;
an even-multiplicity interior root contributes no crossing. Endpoint
zeros are outside (0,infinity). For every nonzero polynomial of degree
at most three the count is finite; degree drops and the zero polynomial
must be treated explicitly when verifying the proposed inverse.
No bounded convolution theorem is being applied to an unbounded
polynomial input or to B_3.

### One nominated test and decision

Use f(x)=(1-x)^2, which is within the proposed degree bound. A separate
mathematical step must verify A_3 and B_3 on monomials, analyze the
actual moments with the equality case of Cauchy–Schwarz, and determine
the input/output crossing counts exactly. This nomination is a test
prescription, not a calculation of B_3 f or a claim about its roots.
No moments need numerical estimation. If the count increases, abandon
the universal inverse premise; if it does not, one test establishes
no general property. Do not enlarge the test to a cubic sweep.

The possible downstream use remains lower oscillation of the actual
theta average. Restricted input classes, a valid reference application,
all-degree control and mixed-positivity transfer would still be unpaid
even if this bounded premise survived. L821's compact Q_3 result is
not an inverse theorem. L795's interlacing stop and step565's unpaid
signed residual remain intact, with no global ban inferred.

The exact continuation and its scope are recorded in
[the quadratic assessment](2026-11-05-theta-inverse-quadratic-necessary-test.md).
It is a routine specialization/reproduction, not a creative mechanism.
The requested creative central bridge still lacks independently paid
signed data; completing this necessary test is justified before any
broader inverse proposal. A newly saved ready assessment receives
separate supervisor approval on a later turn.

### Search and reuse record

Queries: "finite multiplier sequences n multiplier sequence Schur Szego
theorem polynomial (1+x)^n"; "variation diminishing diagonal operator
polynomial positive zeros sign changes multiplier sequence inverse
moments"; "On linear operators preserving the set of positive
polynomials pdf"; "inverse moment sequences positivity multiplier
polynomials"; "reciprocal moment sequence multiplier sequence";
"Petter Branden On linear transformations preserving the Polya
frequency property theorem 3.7 pdf"; "inverse variation diminishing
polynomial diagonal quadratic". Search snippets and secondary summaries
were leads only. The primary passages above were read before selecting
the test. The Branden theorem number was checked against v2 rather
than inferred from a search result. No proof of the full finite
multiplier classification is needed or imported for the quadratic test.

Read L019/L021/L795; reused the ready step502 and step565 assessments.
Scoped searches of actual-theta L79x–L82x lemmas, theta/Laguerre
assessments and corresponding ATTEMPTS found no duplicate of this
inverse test. This is bounded overlap checking, not a novelty claim.
No cross-notebook input, lemma/script write or proof/DAG change occurred.
Matching full Mathlib coverage remains unchecked. No essential source
access blocker remains; the publisher's paywall did not obstruct the
accessible author manuscript. No mathematical exploration turn was
spent, and no recovery/exhaustion counter reset is claimed.
