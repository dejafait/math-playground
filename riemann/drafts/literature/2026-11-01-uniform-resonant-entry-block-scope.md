# Uniform resonant entering block — completed source comparison

TARGET: Assess source coverage for a uniform, resonance-aware bound on the moving-cutoff L495 resultant increment over X<=x<=4*pi*(691260^2-t/16) at t=.16836, testing whether quadratic phase reduction can pay both charges below L499's r0.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the finite-block assessment and searched the named heat/literature/history records and three September 13 stops. External queries covered explicit logarithmic/quadratic exponential sums, integer reduction, resonant endpoint transforms, explicit derivative estimates and summation by parts; exact queries/read scope are recorded below. No duplicate uniform certificate was found in that narrow scope; no novelty inference follows.
SOURCE_EVIDENCE: Arias de Reyna arXiv:2407.02094v1 Section 2 Lemmas 4–5 and complete proofs, Lemma 10, Theorem 11 statement/proof entry; HPY arXiv:2207.02366v1 Lemmas 2.3–2.6, complete Section 4 and Section 5 interior/all boundary cases; Vandehey arXiv:1205.0090v1 Theorem 1.1 and Corollary 1.4's three endpoint regimes; Planat v2 Section 6.7 (44)–(45) and frozen-cutoff discussion; DLMF 2.10.9–10, 26.3.1 and 4.14.3/8/9, and Tracy's Abel summation note pp.1–2 inspected.
COMPARISON: Explicit derivative bounds and finite summation by parts support a controlled uniform test, including integer resonances through curvature bounds or a fully charged finite residual piece. They do not establish the strict budget. The weighted transform retains stationary/endpoint terms and supplies no ready effective numerical saving; the endpoint certificate cannot be interpolated.
GAP: Actual phase reduction, uniform derivative ranges, degenerate/resonant pieces, every weighted prefix and equality, complete resultant control and uniform charges remain unproved and uncomputed. No all-height mechanism or new central positivity input is supplied.
REASON: Essential effective source coverage is now available for one standard specialization attempt, not a claim of uniform exclusion or a creative mechanism. The future attempt must test the original strict threshold; failure parks this envelope.
LITERATURE_REASON: The target changes from one endpoint to a continuum with a moving floor and possible resonances; the ready finite-endpoint assessment expressly excludes this essential scope.
SCOPE: Source comparison and the exact covered specialization only; t=.16836, X=6000284561421.5, n=691004, N=691260, Y=4*pi*(N^2-t/16), q(x)=floor(sqrt(x/(4*pi)+t/16)), P={primes<=307}, exact nu(x), actual Euler phase and ell(x), L499 r0 and full L494 epsilon_1.
COVERED_TARGET: Test the uniform moving-cutoff L495 increment on [X,4*pi*(691260^2-t/16)] at t=.16836 by integer-valued quadratic phase reduction, explicit derivative bounds and separately justified two-charge envelopes, requiring B_unif+U_s,unif+U_r,unif<r0.

## Candidate and bounded decision

The main gap remains actual-Xi all-degree signs and collision exclusion.
This proposed intermediate mechanism would bound the complete finite
increment G_tilde_q(x)(x)-G_tilde_n(x) uniformly for X<=x<=Y,
including every cutoff equality. The downstream use would be a finite
spatial interval input at one positive time. Other times, later intervals,
H1, zero time and RH would remain open even if this test succeeded.

The source question is whether reducing the primitive logarithmic phase
by an integer-valued quadratic phase, with explicit treatment of residual
resonances, can yield a useful uniform bound. This is a proposed technique,
not a proved identity application, cancellation estimate or creative result.
First compare stronger known weighted exponential-sum/endpoint estimates;
retain stationary dual terms and verify their constants and hypotheses.
The existing assessment's optional leads are not ready imports for this
changed problem. Retrieve primary theorem statements and the essential
resonant/endpoint proof cases before approving mathematical work.

The exact test would require a bound B_unif for the complete resultant,
not just its unweighted primitive sum, such that

    B_unif + U_s,unif + U_r,unif < r0

throughout the closed interval. The uniform charge envelopes must be
justified separately: C499c's weights evaluated at Y need not upper-bound
weights at smaller x. Preserve all squarefree channels, logarithmic
weights, actual phase/ell, both saddle corrections, product derivative
and full unmollified entering-pair allowance. Freeze q(x) separately when
taking the true remainder's spatial derivative at each centre. No
derivative of the floor, fall credit, moment-only inference or interpolation
of endpoint samples is permitted.

Use C499c, L494, L495, L496 and L499 (L497/L498 through L499's accepted
mass); no cross-notebook input. The saddle/base-phase manuscripts remain
qualified imports, and a uniform cancellation/charge estimate is wholly
unresolved. Keep the three recorded September 13 stops cited in the
finite-block assessment: they concern uncontrolled cutoff derivatives
and moment-only inference, not a blanket ban on signed arithmetic bounds.

Continue to a mathematical attempt only if the review identifies explicit
applicable inputs and a concrete way to test the strict budget, including
resonant cases. A theorem with ineffective constants or omitted resonance
terms is insufficient. A documented obstruction or inability to identify
a controlled test should park this mechanism rather than trigger another
chain of adjacent endpoint calculations. No originality is claimed.

A protected creative attempt is not yet justified: this could be a routine
specialization, and its essential uniform/resonant coverage is missing.
The next source comparison should decide that distinction. It may nominate
creative routing only for a concrete new central mechanism with a bounded
test and precise escalation, not merely because several routine turns passed.

## Completed comparison — 2026-11-01

The preceding candidate is preserved as the nomination. This literature
turn establishes source scope only. SPECIALIZE covers the exact
COVERED_TARGET after separate supervisor approval of this changed
assessment. No phase reduction, derivative specialization, numerical
bound, new lemma or mathematical script was produced here.

### Effective bounds and the resonance case

[Arias de Reyna, *Explicit van der Corput's d-th derivative estimate*,
arXiv:2407.02094v1 (2 July 2024), Section 2, Lemma 5,
PDF p.4](https://arxiv.org/html/2407.02094v1#S2) states: for real
C^2 f on (a,a+L], L>=1, and 0<lambda<=f''<=Lambda throughout,

    |sum_(a<j<=a+L) exp(2*pi*i*f(j))|
       <= A*(Lambda*L+2)/sqrt(lambda),
    A=(2/sqrt(pi))*(1+sqrt(1+3*pi/8)).

It imposes no separation of f' from integers. The complete Lemma 4
proof counts near-integer regions and bounds their complements;
Lemma 5 treats small curvature and the large-curvature trivial case.
Both proofs were inspected. Lemma 10 restates this bound; Theorem 11
allows d>=3, floor(L)>d, positive lower/upper d-th derivatives and
explicit constants. Only its statement and proof entry were read;
it is not needed by the approved scope. A zero or sign change of f''
does not meet Lemma 5: split it off and pay its finite absolute cost.
No derivative hypotheses for the present phase were verified.

[Hiary–Patel–Yang, *An improved explicit estimate for zeta(1/2+it)*,
arXiv:2207.02366v1, Lemma 2.3, PDF pp.2–3;
Section 4, pp.10–11](https://arxiv.org/html/2207.02366v1#S4) requires
continuous monotone f' on [a,b), one integer k and U,V>1 with
k+1/U<=f'<=k+1-1/V; its bound is (U+V)/pi. The complete proof
retains the first/last terms and the singleton case. Section 5,
pp.11–16, explicitly charges resonant intervals and separates all
three left-endpoint regimes and the right endpoint, including equality.
Its Lemmas 2.5–2.6 are for specified logarithmic phases; they cannot
be imported as general derivative tests for a quadratic-modified phase.
Use Lemma 2.3 only on verified separated pieces, never through an
integer crossing. These results are unweighted; their endpoint handling
does not itself bound the required weighted resultant.

This supplies a source-supported test even at resonances: use a valid
curvature estimate where its hypotheses hold, and include every
uncovered finite piece with an explicit absolute bound. Whether the
result is useful is precisely the future calculation. No cancellation
is assumed on those pieces and no stationary contribution is dropped.

### Stronger weighted transforms and elementary interfaces

[Vandehey, *Error term improvements for van der Corput transforms*,
arXiv:1205.0090v1, Theorem 1.1, pp.2–3, and Corollary 1.4,
pp.5–6](https://arxiv.org/html/1205.0090v1#S1) gives a weighted
transform with a stationary dual sum. The former assumes real C^4 f,
real bounded-variation g, M>=b-a, positive f'' comparable to T/M^2
and bounds of orders T/M^3,T/M^4 on the next derivatives. Its error
constant depends on these comparisons. The corollary also assumes
C^2 g, positive U, M=b-a>>1, T>>1, the same phase bounds, and
|g|<<U, |g'|<<U/M, |g''|<<U/M^2. Its starred sums give half weight
to integer endpoints. It distinguishes integer endpoint slopes,
nearby slopes and separated slopes. Some
errors remain implicit. Statements and all endpoint regimes were read,
not the later proof. Neither result supplies our numerical budget.
Karatsuba–Korolev, cited there for explicit errors, remains an unread
optional lead; it is unnecessary for the elementary derivative test.
Robert's previously assessed Theorem 1 remains an inexplicit comparison,
not a newly effective input. No claim that stronger methods fail follows.

[DLMF 2.10.9–10](https://dlmf.nist.gov/2.10.E9) states finite
summation by parts in terms of all prefix sums. [Craig Tracy's
*Abel Partial Summation Formula*, 28 January 2012,
pp.1–2](https://www.math.ucdavis.edu/~tracy/courses/AbelSummation.pdf)
allows complex coefficients and a C^1 complex weight and retains the
endpoint term. These cover weighting only after the actual weights'
variation and every relevant prefix are controlled. An unweighted
full-block bound alone is insufficient. No weight monotonicity or
variation bound for this problem was derived.

[DLMF 26.3.1](https://dlmf.nist.gov/26.3.E1) supplies the binomial
coefficient formula and its combinatorial integer meaning;
[4.14.3, 8–9](https://dlmf.nist.gov/4.14) supplies Euler's identity
and trigonometric periodicity. These are elementary source interfaces
for a proposed integer-valued quadratic shift, not evidence that a
particular shift has favorable residual derivatives. Selection and
verification of that shift belong to the mathematical attempt. No
original theorem or reproof of a derivative estimate is authorized.

### The fixed analytic interface and remaining specialization

[Planat v2 Section 6.7, (44), Lemma 6.10/(45)](https://arxiv.org/html/2609.37164v2#S6.SS7)
retains the complete logarithmic resultant and two separate charges.
Its frozen-cutoff discussion fixes the index before differentiation;
it does not differentiate the floor. The inspected source identities,
charge proof and reflection/Cauchy discussion agree in scope with
L494–L496. Section 6.6's grouped coefficient transport, already assessed,
is a different sufficient method, not a supplied signed uniform bound.
The present review does not audit the source's saddle/base-phase
proofs, ledgers, separator assumption or global assembly.

C499c Sections 1–4 provide the local finite comparison and factored
increment at one endpoint. They suggest the necessary interfaces,
but their statements certify no uniform interval estimate. The next
attempt must justify applying each identity/envelope at variable x;
it may not silently promote an endpoint value to a uniform bound.
L499 retains L497/L498's accepted old mass. No new mass replay or
cross-notebook input is required. Full matching Mathlib coverage for
this uniform application is unchecked; unknown does not mean absent.

The exact obligations are:

1. Check the closed analytic domain on [X,Y] and the canonical floor
   in every cell, including X, every entry equality and Y. The old
   n model is only a finite comparison. Fix the new q(x) when taking
   the true remainder's spatial derivative at each centre.
2. Select and justify the integer-valued quadratic reduction of the
   actual logarithmic phase. Certify all derivative ranges used in
   cited estimates uniformly in x and in every needed prefix. Include
   empty/singleton pieces, all resonances, curvature degeneracies and
   endpoint conventions; a negative-curvature application needs its
   explicit conjugation justification. No assumed separation is allowed.
3. Control the actual heat weights and logarithmic weights by finite
   summation by parts or complete finite bounds. Reconstruct the literal
   complex resultant with actual nu, Euler factors and ell, all
   squarefree channels, exact prime heat products and conjugate terms.
   A theorem for a primitive sum alone is not the completed test.
4. Independently prove uniform U_s,unif and U_r,unif. Keep rho,
   the product derivative, both saddle corrections, full logarithmic
   support, ell0 and L494's full epsilon_1/entering-pair allowance.
   In particular use justified weight envelopes over the interval,
   not C499c's weights at its right endpoint. Justify the old-model
   lower bound at each x from the accepted mass and damping interface.

These are unproved application obligations, not assertions that the
displayed inequalities hold. They leave other times, later intervals,
H1, zero time, source audits and actual-Xi all-degree signs unresolved.

### Bounded attempt, duplicates and decision

Perform one finite, documented uniform-envelope test on this exact
interval. Fix a finite partition respecting the floor cells and the
derivative/resonance hypotheses; bound whole pieces, not sampled
points. Charge unresolved resonant pieces absolutely. Compare
B_unif+U_s,unif+U_r,unif with the exact inherited r0 and print the
actual/required bounds, failures and full certificate path. One
precision refinement may resolve enclosure width; no search over
longer blocks or adjacent endpoints is approved. If the budget cannot
be certified at adequate precision, park this particular envelope,
record whether the issue is constants, resonance cost or uniform
weight/charge control, and preserve the evidence. This is an enclosure
test, not a collision or RH counterexample test.

The narrow duplicate search covered the November 1 entry/cutoff
assessments, named endpoint/audit histories and heat working records.
Only the nomination and finite endpoint result were found. The three
September 13 ATTEMPTS records were read in full: they reject uncontrolled
cutoff derivatives and moment-only inference, not this signed finite
estimate. Their restrictions remain. No sibling proof or checkpoint
was read. No claim of originality follows from this search.

Queries included `explicit exponential sum quadratic phase logarithm
integer quadratic reduction resonant Kusmin Landau Hiary Patel Yang
2207.02366`; `Vandehey 1205.0090 van der Corput transformation explicit
endpoint stationary phase quadratic sums uniform`; `site.dlmf.nist.gov
summation by parts Abel summation`; and `2407.02094 Lemma 5 correction`.
The last returned no usable correction evidence; that is not a source
validation. Primary HTML/PDF text was used, not search snippets as proof.
Shell downloads failed DNS resolution; browser access supplied the
essential passages, so there is no essential access blocker. PDF
screenshots returned no inspectable images and were not used as evidence.

Outcome: EXPLORATION, with actionable effective source scope and no new
uniform bound. This is standard specialization, not a justified creative
central mechanism; the missing all-height/zero-time transfer blocks that
classification. No mathematical exploration budget is spent by this
literature turn. Newly saved ready coverage requires a separate approval
next turn, preserving the completed review.
