# Compact tilted-primitive zero-count nomination

TARGET: Establish or refute that U_(1/10) has exactly one simple zero in (1/4,4) using L946 and L947 without changing the density or asserting a global zero count.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step82 searched exact positive-slope-at-zeros and critical-point-minimum uniqueness terminology, inspected Lebl's primary calculus statements and essential proofs, and compared the specific local primitive, direct-cover and failure records listed below. No matching actual-v compact-zero theorem was identified in this bounded check; no novelty is inferred.
SOURCE_EVIDENCE: Jiri Lebl, Basic Analysis I, author-hosted HTML accessed 2026-11-09: Theorems3.3.2,3.3.8 and Lemma3.3.7; Lemma4.2.2, Theorems4.2.3–4, Propositions4.2.7–9; Theorem5.3.3. Statements and relevant proofs were read; Proposition4.2.8's strict case is stated with proof left as an exercise. Direct section URLs and hypotheses are below. L938 continuity, C944a differentiation scope, L946's full compact argument and L947's definition/proof were inspected.
COMPARISON: These standard calculus inputs cover the methods needed for a separate compact specialization. They do not state this exact signed-density conclusion. The remaining work is the local applicability and zero-count argument, including simplicity, without assuming global convexity or a finite zero set. Ratio/field failures and the raw-U transform-domain stop do not supply or refute this compact inference.
GAP: The actual-U specialization is not proved in this literature turn. Establish its derivative identity and handle stationary points, arbitrary pairs of zeros, accumulation, tangencies and nonzero slope at the claimed crossing under the inherited contracts. L947 remains numerically unaudited. Global variation, effective tail join, parameter signs and all-degree transfer remain open.
REASON: Essential calculus coverage is now inspected for the previously nominated compact target; proceed to one separate ordinary specialization using the existing qualified inputs. No additional source campaign or budget refinement is indicated.
LITERATURE_REASON: The supplied assessment was REVIEW_REQUIRED for the changed compact-zero target; endpoint-integration coverage79 did not cover uniqueness, tangencies or multiplicities.
SCOPE: Only b=1/10, the unchanged L938 density and normalization, and zeros in (1/4,4). Standard calculus application; no new enclosure, global zero-count theorem, transform identity or tail estimate is approved.

The step81 nomination required a separate literature turn because this
target was outside the endpoint assessment. Step82 completes that review
below and approves only the exact target above for a later specialization.
No compact-zero result is derived or approved as a proved theorem here.

Essential proposed inputs are L938's actual normalized v, L946's closed
compact zero-slope certificate and L947's strict tilted endpoint inclusions.
Keep the arithmetic/library qualifications and the fixed b=1/10. The exact
identity U'=exp(E/10)v and the regularity needed for any zero-count argument
must be checked as part of the later specialization, not presumed verified
by this nomination. A sign change alone does not establish simplicity or
uniqueness. No cross-notebook input is proposed.

Continue only if a source-covered argument yields an explicit test for the
claimed unique simple crossing throughout this compact interval. Otherwise
record the precise missing hypothesis or counterexample and stop this local
inference. No parameter fit, refinement, new tail estimate, other degree,
contact inference or global zero-count application is included. Full and
supporting Mathlib coverage is unchecked.

This is ordinary calculus specialization, not a creative central mechanism.
A justified creative nomination still lacks a concrete effective global
primitive variation/tail-join mechanism and its discriminating test. The
compact signs alone must not be relabeled as that missing mechanism.

## Completed source comparison — 9 November 2026, step82

The main gap remains L030–L032/C032a actual-Xi all-degree mixed
positivity. The intermediate target is the exact compact claim in TARGET.
Its plausible use is a compact primitive sign geometry input for a later
global variation argument. A compact conclusion would leave that argument's
head/tail control, parameter signs and independent degrees unresolved.

### Inspected primary calculus coverage

Use Jiri Lebl, *Basic Analysis I: Introduction to Real Analysis, Volume I*,
author-hosted HTML as accessed 9 November2026. The HTML does not expose a
release identifier in the inspected sections; citations below use its exact
displayed theorem numbers and section URLs, not a guessed PDF edition.

[Section3.3](https://www.jirka.org/ra/html/sec_minmaxint.html):
Theorem3.3.2 gives attained extrema for a real continuous function on a
closed bounded interval. Lemma3.3.7 gives an interior zero under continuity
and strict negative/positive endpoint signs; Theorem3.3.8 permits either
ordering and any strictly intermediate value. Read the extrema proof and
the complete bisection proof, including the common limit, continuity and
endpoint exclusions, and the reduction to the general intermediate value
theorem. These results assert existence, not uniqueness or simplicity.

[Section4.2](https://www.jirka.org/ra/html/sec_mvt.html):
Lemma4.2.2 requires differentiability at an interior relative extremum and
concludes zero derivative. Rolle's Theorem4.2.3 and MVT4.2.4 require
continuity on the closed interval and differentiability throughout its
interior; Rolle additionally requires equal endpoint values. Read the
two-sided quotient proof, Rolle's constant and nonconstant cases, and the
affine-subtraction MVT proof. Propositions4.2.7–8 give monotonicity from
weak/strict derivative signs on an interval. Proposition4.2.9 is the first
derivative test: continuity at the candidate, differentiability on its two
sides, and nonpositive/nonnegative derivatives give a minimum; reversed
signs give a maximum. Read its minimum proof; the maximum follows by
negating the function. The strict-monotonicity proof in4.2.8 is an exercise,
so a later application should use the inspected MVT directly for strictness.
No global convexity premise is supplied by these statements.

[Section5.3](https://www.jirka.org/ra/html/sec_ftc.html):
Theorem5.3.3 assumes a Riemann-integrable real function on a compact
interval. Its integral from the left endpoint is continuous; at points
where the integrand is continuous its derivative equals the integrand.
Read the full proof: boundedness gives continuity and the two-sided
integral difference quotient gives differentiation. Later use is only at
interior positive energies, so no convention on two-sided derivatives at
energy0 is needed. Apply with the original base0; changing the base or
subtracting a limiting mass is unnecessary.

The search also returned Lebl's older PDF second-derivative test with a
C^2 hypothesis and an exercise weakening that hypothesis. That snippet
is an unread alternative, not an imported theorem or proof. No need for
that stronger regularity or an exercise solution has been established.
Higher-dimensional mountain-pass leads have different hypotheses and
were not inspected or imported. Mathlib coverage of either the full
fixed-density statement or these supporting formal theorems is unchecked;
availability remains unknown.

### Exact applicability and remaining specialization

L938's Conclusion and proof(6)–(9) supply continuity of the original v
including0, with its original34 rows, twelve labelled factors and M_0^12.
L947 uses precisely the weighted integral from0 at b=1/10. Thus the
continuity requirement for the compact FTC application is covered by
existing inputs and the continuous exponential. The identity
U'(E)=exp(E/10)v(E) must be written out in the later proof as that FTC
application, not treated as a new numerical assertion or presumed
verified by endpoint signs.

L946 gives v'(E)>0 at every v zero on the entire closed [1/4,4],
conditional on the stated execution contracts. Its full proof and step78
audit were read, including closed-leaf coverage, shared/outer endpoints,
and differentiation qualifications. C944a's proof supplies dominated
differentiation of the actual simplex density; it does not differentiate
a cell-error bound. No need to enlarge the derivative scope is identified
for this nomination. The future proof should use only the regularity
actually needed, rather than silently assume an analytic zero set or a
uniform lower bound for v' outside the certified zero condition.

L947 supplies the strict U endpoint contrast, subject to its unchanged
Decimal/exponential/pi/integer contracts and the step50/75 reused inputs.
Its exact-integration argument and weighted-error allowances were read
for object and hypothesis matching, not independently replayed. Its new
numerical implementation remains unaudited. No additional numerical
claim or unconditional validation is made in this source review.

The later specialization must distinguish stationary points of U from
zeros of U; translate L946's condition at the former using the FTC
identity; and use the cited extrema/MVT tools to address arbitrary pairs
of zeros and stationary tangencies. It must establish nonzero first
derivative at the claimed U zero: sign change alone also allows a flat
crossing. Do not begin by enumerating consecutive zeros without ruling
out accumulation. Compact closed-subinterval extrema and arbitrary-pair
arguments are covered tools that do not require such enumeration. This
is a list of proof obligations and allowed tools, not their completed
mathematical derivation. No general one-crossing lemma is claimed here.

Continue only if these unchanged local hypotheses yield the claimed
unique simple compact zero with all cases justified. If a hypothesis is
missing or a counterexample survives them, record it and stop the
inference without refining any numerical budget or changing the density.
No conclusion about energies outside [1/4,4] is authorized.

### Search, duplicates, failures and decision

Queries included `site.jirka.org ra Rolle theorem fundamental theorem
calculus real analysis`, `"derivative" "positive at every zero" uniqueness`,
`"every critical point" "strict local minimum" "unique"`,
`site.jirka.org/ra/html "second derivative test"` and
`"primitive" "positive derivative at" "zeros"`. Searches located the
author's primary calculus text; they did not identify a theorem for this
exact v. No novelty conclusion follows. One guessed section URL failed;
the author's index supplied the correct section URLs. A Penn lecture
page returned403 and is not evidence used here; the complete relevant
Lebl proofs were accessible, so no essential source blocker remains.

Local duplicate/obstruction comparison was restricted to L938, L946,
L947, C944a's differentiation proof; the cumulative assessment78,
endpoint assessment79, zero-superlevel assessment56, relevant named
step80/81 histories; and
`ATTEMPTS/2026-11-09-raw-cumulative-positive-tilt-domain-stop-79.md`.
Targeted searches of the November9 L938 assessment paths located direct
density and simplex/field targets, not an existing proof of the nominated
compact-U conclusion. Assessment78 already records the pointwise
ratio/field failures and their scopes; that comparison is reused. They
concern different observables and are not new evidence against this test.
The raw-U stop retains its transform-domain objection on positive lambda;
the present review does not reopen or remove it. No cross-notebook input
was read or proposed.

Decision SPECIALIZE: the elementary tools and local input scopes are
adequately covered for one separate proof attempt. This changes the
nomination's source gate from REVIEW_REQUIRED, not the mathematical
status of its conclusion. No known result is presented as a new discovery,
and no lemma, mathematical script, DAG or PROOF assembly changes in this
literature-only turn. Global variation/tail-join and the main RH gap stay
open. No justified creative central mechanism is nominated: a concrete
effective global join and a discriminating variation mechanism remain
missing. Further literature on this unchanged ready compact target is
not indicated.
