# Fixed continuous Mellin-density floor discriminator1177

TARGET: Test C040c's fixed continuous Mellin-ratio density against Kawano's quantitative lower floor at a=1/20, uniformly for lambda in [4329/1000,4331/1000], without parameter or sample retuning.
CHECKED: 2026-11-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Discovery1177 searched exact Kawano/continuous-counterexample and fixed1F2/Mellin terms and checked777/778/780/785 plus C040c's canonical proof. The quantitative continuous premise was expressly excluded there; no completed instance of this exact test was found and no novelty is inferred.
SOURCE_EVIDENCE: Kawano Preprints.org202611.0383v1 Theorem1.2/(5)-(9), Section2/(10)-(16), Lemma3.1/Proposition3.2 with proofs; NIST DLMF5.12.1 with Re(a),Re(b)>0,5.5.1-2 away from poles, and1.14(iii) equations17-19/uniqueness with continuous functions of exponential growth. Exact citations and application obligations below.
COMPARISON: C040c already disproves the qualitative coefficient-to-logarithmic-Hankel implication, but establishes no comparison with the exact source lower floor. Beta moments and digamma recurrence permit an independent continuous-ratio calculation; Laplace uniqueness prevents substituting another continuous exponential-order density. Neither a fixed-point pass nor complete monotonicity alone gives the stronger all-a bound or L030's signs.
GAP: Identify the continuous Mellin transform from the actual fixed model density, justify every real-p integral and differentiation, construct and identify its inverse density, and enclose one scalar deficit uniformly in lambda. Nothing in this proposal asserts its value, sign, full-a lower bound, source upper envelope or actual-Xi transfer.
REASON: This is a materially additional quantitative hypothesis explicitly left open by the audited qualitative stop. One fixed-point necessary-condition test can distinguish it without a model/degree sweep or an audit of unrelated external certificates. New ready continuation awaits separate supervisor approval before mathematics.
SCOPE: Only C040c's unchanged F and cosine density, p>0, eta=15287777/250000000, a=1/20, lambda in [4329/1000,4331/1000]; no parameter selection, extra sampling, new model, full RH-equivalent sign or source certificate replay.

## Exact target and relevance

Essential inputs: C040c for its unchanged
F(t)=1F2(3/2;1,100;-t^2/4) and the normalized cosine density m(u)
in its equations(4)-(6); L030-L032/C032a supply the central gap and
explain why the model's already negative logarithmic H_1 matters.
C040c's H_1 and qualitative premises are accepted audited inputs and
must not be recalculated here. C040c is a model, never actual Xi.

Define the proposed continuous interface, for real p>0, by

    I_F(p)=integral_0^1 u^(2p-1) m(u) du,
    G_F(p)=1/p+I_F'(p)/I_F(p)-I_F'(p+1)/I_F(p+1).

These are target definitions, not a derived expression or an established
Laplace representation. The multiplicative normalization of I cancels
in G; a change of p or of the u scale cannot be made silently. Seek a
continuous real exponential-order k_F with
G_F(p)=integral_0^infinity exp(-pa) k_F(a) da for all p>0,
with every asserted convergence domain justified. Then test only

    D(lambda)=k_F(1/20)-eta*exp(-lambda/20).

A certified upper bound sup_lambda D(lambda)<0 disproves this model's
compatibility with the added lower premise for every lambda in the
source enclosure. Continuity/uniqueness must be justified before using
one point to rule out any alternative admissible inverse density.
If the interval meets zero, stop inconclusive; if it is positive, record
only that this necessary point test passes. No additional point, model
parameter or precision campaign is authorized automatically.

Plausible use: decide whether the existing generic countermodel also
disposes of an explicitly quantitative continuous ingredient, or whether
that ingredient survives it as an additional hypothesis requiring a new
theta-specific bridge. Neither finding proves the strengthened implication,
constructs an actual-Xi sign, or resolves any all-degree/global gap.

## Precise sources and specialization obligations

Kawano, *Logarithmic Inequalities of Arbitrary Order for the Riemann Xi
Coefficients*, [Preprints.org202611.0383v1](https://www.preprints.org/manuscript/202611.0383),
posted4November2026, is unrefereed. Theorem1.2/(5)-(9) defines I,J,G
and claims the floor with the eta and lambda enclosure above. Its full
assertion also includes an exponentially weighted upper bound and a
specified zero of J. Those stronger premises and the actual-theta
certificates are outside this test. No truth of that actual-theta theorem
is needed to compare a fixed model with its displayed lower premise.
Section2's discrete consequences and its inverse-coefficient moment
sequence are distinct from L030's reciprocal-zero moments.

[NIST DLMF5.12.1](https://dlmf.nist.gov/5.12#E1) is Euler's beta
integral, with Re(a)>0,Re(b)>0 as explicitly stated before the formula.
Use it on C040c's nonnegative beta/arcsine integral after Tonelli,
checking all exponents and finite endpoints for every p>0. Positive
integer moments alone do not identify a Mellin transform on that domain.
No interpolation of the integer coefficient formula is acceptable.

[NIST DLMF5.5.1-2](https://dlmf.nist.gov/5.5#E2) gives gamma and
digamma recurrence away from their poles. A future gamma expression
must retain its complete p-dependent normalization; differentiating it
requires a justified analytic or real differentiated Mellin identity.
Import the recurrences, rather than reprove gamma theory. C040c's bound
on m and compact support are available for checking domination, including
the logarithm weights on compact p intervals bounded away from zero.
No boundary p=0 value is an input.

[NIST DLMF1.14(iii)](https://dlmf.nist.gov/1.14#iii), equations1.14.17-19
and the subsection 'Uniqueness', supplies Laplace definition, convergence
and uniqueness. Its standing hypotheses are piecewise continuity and
exponential growth; uniqueness assumes continuity. Verify the growth
and a common right half-plane for both densities before importing it.
The existence of a formal inverse or values at integer p is insufficient.
The source uniqueness statement is imported, not reproved.

No source supplies the local scalar deficit. Necessary algebra and one
rigorous exponential enclosure are ordinary specialization/REPRODUCTION,
routed calculation/standard/high. This is not a creative central mechanism.
Use exact rational comparisons or fully certified intervals; report the
actual bound and required threshold0, including any failure. If a script
is needed after approval, store the complete certificate under a local
topic path and print only its checks, threshold and path.

## Limits, duplicates and gate

Preserve C040c's audited qualitative negative and the KPS ordinary-
membership/separated-Bernstein-Pick distinction in the508/785 records.
The new hypothesis is the source's exact continuous lower floor; it is
neither the already-refuted qualitative premises nor an assumed positive
logarithmic Hankel form. This test does not claim to exhaust quantitative
bridges or to test all of Theorem1.2. No stronger result or exact matching
test was located in the bounded search. Matching Mathlib coverage is
unchecked, not absent. No cross-notebook input is used.

No model specialization, formula for k_F, scalar computation or new lemma
was made1177. This assessment is newly saved and requires separate approval
next turn. An unproved normalization, nonunique inverse or unresolved
interval is a limitation, never evidence of a sign. End the bounded test
without retuning. Actual signed Xi structure remains the blocker to a
justified protected creative proof attempt.
