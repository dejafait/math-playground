# Fixed gamma/geometric first-contact attempt895

Prior gate: unchanged EXPLORE assessment892, read in the supplied snapshot.
The target remains exactly its fixed shape3/2, rate1 gamma convolved with
the rate-2^n exponential sum; no changed parameters or actual-Xi inference.

Main gap: L030-L032/C032a actual-Xi all-degree positivity. The intermediate
target is D3'(x_*)<0 at this model's first D3 zero. Its downstream use is
to determine whether the scalar Volterra premises permit the stipulated
adverse contact geometry. C466d supplies fully written but unaudited
admissibility, strict global D1/D2 and opposite D3 endpoint signs.

Test: establish the full positive prefix and strict derivative, or prove
incompatible contact geometry. Endpoint signs or a negative numerical
sample alone do not decide the test. Reuse assessment891 completion892's
source/duplicate/failure screen and preserve the scalar-preservation,
bell-shape and finite-root stops. No new literature is needed for this
bounded attempt, and no new source theorem is being assumed.

Unfinished approach saved before extended reasoning: seek an identity
for exponential convolution that controls third-Wronskian zeros, using
the fixed model's finite heads and infinite-tail limit. A convolution
identity is not itself a zero-count theorem; any required mixed minor,
strictness, endpoint or limit estimate must be made explicit. If this
does not close, preserve the exact obstruction rather than certify the
first zero from C466d's endpoint argument.

Essential inputs/limitations: C466d; unchanged assessment892. C466a/b/c
are motivation only. Actual-density identification, actual-H signed
weights, all higher contacts and L030 assembly remain independent.
Mathlib coverage of the joint model/contact statement is unchecked.

## Completed bounded diagnostic; first-contact proof still open

The exponential-convolution approach did not supply a proved zero-count
or strictness identity. In particular, writing a smoothed factor as an
antiderivative leaves mixed derivative expressions of uncontrolled sign;
no variation-diminishing assertion was imported to fill that gap.
This is unfinished reasoning, not an impossibility result for that method.

The same fixed-density attempt then used explicit finite-head partial
fractions to obtain an evaluable series. Its complete proof, derivative
interchanges and exact omitted-series bound are now canonical in C466d,
equations (16)-(21); they use no new mathematical input. Do not copy the
proof here or mistake it for control of the evaluation error.

Reproduction command:

    python3 scripts/gamma-geometric/contact-diagnostic-895.py

The full diagnostic is `scripts/gamma-geometric/contact-diagnostic-895.json`.
It retains all 512 samples on {k/32:1<=k<=512}, computation settings,
the proposed contact and higher-precision replay, analytic series-tail
expressions, and failures. This is explicitly NOT an interval certificate.
The script uses only the Python standard library; no packages were added.

Observed values, not proved signs: all 139 sampled points through 139/32
have Z=D3(Q)/Q^3>0; the remaining 373 samples have Z<0. The sole sampled
sign-change bracket is I=[139/32,35/8]. Its endpoint values are approximately
5.6945742e-6 and -2.4948394e-6. Sample bisection proposes
x=4.3650866609817478652 and Z'=-2.5638848267e-4. Replaying that point
at 140 decimal digits, 40 exponential terms and 220 large-argument terms
agrees in Z to about 1.9e-97. Neither agreement nor bisection certifies
the value, its derivative, uniqueness, or the first zero.

For orders 0..5 on [1/32,16], the largest decimal evaluation of C466d's
exact omitted-exponential-series bound (19), using N=32, is about
6.755e-98. This controls only that series truncation. The script does
not enclose decimal rounding, the truncated convergent evaluation series,
or its alternative large-argument expansion. It also does not cover
between-sample signs. The complete relevant /candidate,
/coarse_contact_endpoints, /sample_summary and /failures values were
inspected with the supervisor JSON inspector; those values remain
diagnostic rather than proof evidence.

Refined continuation inside unchanged assessment892: seek Z>0 throughout
(0,139/32], Z(35/8)<0, and Z'<-1/5000 on I. These would prove one simple
first downward crossing. They are proposed thresholds, not inequalities
proved by this turn. C466d's initial positivity has no effective endpoint;
the initial interval must be quantified and joined to certified compact
coverage. All finite evaluation errors and matrix/quotient propagation
must be bounded, in addition to (19). No earlier tangency is excluded yet.

Outcome EXPLORATION: a new fixed-model diagnostic and usable exact
evaluation bounds, without a certified new contact/sign conclusion.
Classification REPRODUCTION: finite partial fractions, differentiation
and geometric tail bounds are standard tools specialized here; no
originality claim. The model is neither stopped nor accepted as a witness.
The new rational bracket and explicit proposed margins justify one
refined attempt, subject to the shared stopping rules. No new central
actual-H creative mechanism is justified without signed-weight control.
