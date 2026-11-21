# Fixed-real-rate scale comparison: attempt1234

17 November 2026. One bounded RESEARCH attempt under the unchanged ready
EXPLORE assessment1232/review1233, supplied and gate-approved at startup.
The exact target is beta_(i,0)(t)>=beta_(i,0)(x)/2 on 3*x/4<=t<=x,
uniformly over C030r's stated fixed real-rate family and allowed ranks.

## Initial reasoning checkpoint

The main gap is L030-L032/C032a actual-Xi positivity in every degree.
A uniform comparison would supply C030t's additional premise and,
conditional on auditing that reduction, its full phase bound with
constant 28. Reference evolution, Xi supply, degree/time, complement,
theta signing and graph realization remain independent gaps.

Read C030r and C030t in full; searched the paired working1231/1232,
C030q and the joint-route stop1232. Reused the supplied source review
and its scoped prior-failure comparison. Neither the real pointwise
upper bound nor positive-law recurrence theory pays this lower ratio.
Unfinished1218 and all pre-existing changes are preserved.

The discriminating test is a uniform proof or a rigorously certified
admissible violation. Rates must remain fixed between the two times;
repeats, n=2m, endpoints and all contrasts remain in scope. Finite
samples alone cannot establish or refute the universal claim. A
violation would reject this half-value premise, not the full complex
phase bound or every positive constant.

The initial route is the exact derivative-Hankel representation of
C030r. Its positive beta is not a positive-functional recurrence
coefficient. Examine time dependence using confluent exponential
formulas; no monotonicity or beta floor is assumed. At this checkpoint
there is no new result, counterexample or numerical evidence.

## Analytical checkpoint after the diagnostic

The bounded Decimal screen is saved in
scripts/paired-subdiagonal/real-scale-1234.json. It found no sampled
violation or increase; this is not a certificate. No additional screen
is needed to establish a universal claim.

A possible exact mechanism is now identified. For every 1<=i<n,
extend the same positive determinant ratio algebraically and put
v_i=(log beta_i)'. The derivative-Hankel identity suggests
v_i''=2*beta_i^2*v_i-beta_(i-1)^2*v_(i-1)-beta_(i+1)^2*v_(i+1),
with zero endpoint products. Sum over indices where v_i>0. Each
positive term has at most two positive neighbors, while a nonpositive
neighbor contributes with the favorable sign. Thus the sum of positive
parts should be convex, including crossing points. The orbital formula
gives v_i<0 near zero and v_i->-(q_(i+1)-q_i)/2<=0 at infinity when
the rates are sorted. Convexity would force all positive parts to vanish.

This is unfinished reasoning at this checkpoint. Check the signed Toda
identity, a rigorous positive-part convexity argument, all endpoint
indices and the Laplace-concentration limit at repeated rates before
promoting it. The proposed argument remains within the approved uniform
comparison target; no new target or literature approval is declared.

## Completed attempt

The exact argument closes the approved half-value premise, with the
stronger comparison constant 1, in
[C030u](../../lemmas/C030u-real-subdiagonal-monotonicity.md).
That file contains the full hypotheses, imported determinant citation,
signed evolution, endpoint concentration (including repeated rates),
positive-part convexity proof and Mathlib qualification. It awaits
independent conceptual audit. C030t's conditional reduction remains
unaudited; its phase conclusion is not promoted in this turn.

Outcome ADVANCE is a local intermediate result, not a new discovery
beyond the sources checked or an RH candidate. POTENTIALLY_NEW has only
the bounded-search meaning prescribed in the shared policy. The known
determinant formula is imported, not presented as original. No new
literature search, cross-notebook input or rate-uniform asymptotic
estimate is invoked. The exact finite-family sign implies a uniform
comparison without requiring a uniform onset in the endpoint limits.

The new audit nomination is REVIEW_REQUIRED. It does not approve the
new proof during its own derivation turn. Essential continuation input
is C030r; C030t is downstream motivation, not a proof input. Preserve
the full rank chain 1,...,n-1 in the convexity argument even though the
requested coefficients occupy its first half. Independent Xi supply,
evolution, degree/time, complement, theta signing and realization remain
unresolved. A central creative mechanism is not substituted for this
essential audit; the missing signed actual-Xi input and its coverage
remain the blocker to such a nomination.

## Diagnostic scope and reproducibility

Run python3 scripts/paired-subdiagonal/real_scale_1234.py from riemann.
The complete diagnostic is scripts/paired-subdiagonal/real-scale-1234.json.
It contains 1647 earlier/end-time ratios, no recorded signed-pivot failure,
and no sampled ratio below 1 (hence none below the required 1/2).
The minimum is about 1.0101010526771394, at shifted rates
(0 repeated14,1 repeated2), x=1/10, i=1, t/x=99/100. Every shifted
rate q denotes the admissible positive rate q+1, fixed at both times.
These rounded values are not bounds, verification of monotonicity, or
mathematical inputs to C030u. No precision replay was needed for the
analytic proof; no claim of certified numerical accuracy is made.

For completeness the implementation computes rational confluent partial
fractions of product_q(s+q)^(-mu_q). At the pole -q, expand the product
over r!=q in powers of s+q up to degree mu_q-1. Its coefficient c_j
gives c_j/(s+q)^(mu_q-j), whose inverse Laplace term is
c_j*t^(mu_q-j-1)*exp(-q*t)/(mu_q-j-1)!. This is a finite exact rational
identity before evaluation. Applying (partial_t-q) to each polynomial
generates the derivative moments. The omitted product of positive
rates multiplies every moment by the same constant. A common shift
q->q+1 multiplies the function by exp(-t); Leibniz's rule transforms
the Hankel matrix by two triangular binomial matrices of determinant
one and an overall exp(-t). Thus its size-k determinant gains the
factor exp(-k*t), which cancels in beta. Unpivoted elimination gives
signed pivots Delta_(i+1)/Delta_i and beta_i^2=-pivot_i/pivot_(i-1).
The program checks their expected alternating signs, but uses rounded
Decimal exponentials and arithmetic throughout evaluation. Its JSON
retains all cases and failure fields, not just the selected minimum.

The analytic argument, unlike this diagnostic, handles every allowed
dimension, contrast, time and endpoint. The diagnostic was exploratory
evidence only and is retained to avoid disguising finite samples as
the reason for the proof's conclusion.
