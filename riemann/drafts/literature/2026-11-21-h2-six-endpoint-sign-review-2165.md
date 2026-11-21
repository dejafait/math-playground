# Six real endpoint signs: completed source comparison2166

TARGET: Review source coverage for certifying F(lambda,a)F(lambda,b)<0 uniformly on 0<=lambda<=1/20 for (a,b)=(14,29/2),(41/2,43/2),(49/2,51/2) by validated direct theta-kernel integration with complete theta and integration tails.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step2166 searched direct heat-theta signed integration and checked the named local confinement/coefficient/inner-contour stops; reused reviews2157,2161,2066/2067 and inspected the primary quadrature and Taylor statements/proof cases below. No matching six-sign certificate was located; no novelty inference follows.
SOURCE_EVIDENCE: Johansson1802.07942v1 Sections2,2.1,3.2 https://arxiv.org/html/1802.07942v1 ; Arb2.23 evaluator/Integration contract https://arblib.org/acb_calc.html ; DLMF3.5(ii),(3.5.6)-(3.5.8) https://dlmf.nist.gov/3.5.ii ; OpenStax Calculus Volume2 Section6.3 Theorem6.7 and proof https://openstax.org/books/calculus-volume-2/pages/6-3-taylor-and-maclaurin-series ; L019/L058 exact kernel/domination. Qualifications below.
COMPARISON: Known quadrature and Taylor remainder theorems cover a direct signed-integral attempt without division by F. They do not import the six signs. Explicit theta-index, spatial, quadrature, arithmetic and uniform-time errors remain specialization obligations, now scoped to one fixed test.
GAP: No endpoint value, tail constant, fourth-derivative constant, ninth-time-derivative bound or final signed enclosure has been established. Actual placement and head assembly remain open. The finite settings below are proposed test parameters, not certified adequate errors.
REASON: A uniform-time Taylor comparison supplies a bounded source-covered alternative to sample-only time evaluation and unpaid F_z/F neighborhoods. Nominate one later specialization without reproducing general source theorems or inferring feasibility from benchmarks.
LITERATURE_REASON: New specific target outside the ready propagation and fixed-box assessments: closed-band signs of six oscillatory real integrals, including their complete truncation and arithmetic error budgets. Reuse the integration comparison from step2156 where applicable; do not repeat the general confinement search.
SCOPE: Completed literature-only comparison of TARGET. No lemma, mathematical script, integral evaluation, interval sweep or propagation reproof was performed. Original nomination below is historical; the separate ready calculation assessment2166 requires supervisor approval next turn.

## Original nomination and restrictions (retained)

Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
The intermediate purpose is actual placement in exactly C919e's three
disjoint boxes. A later head application would still have to justify
the positive contribution of the remaining head using C919d and
combine it with C919c's signed exterior budget. Neither assembly nor
placement is proved here. Higher-degree and global signs stay open.

Essential inputs are L019,L058,C919c,C919d,C919e, with C919c's inherited
L919/C919a/C919b normalization and Decimal qualifications unchanged.
Initial multiplicities are allowed. No simple initial census, tabulated
brackets, RH or cross-notebook input may be assumed. The proposed signs
are hypotheses to test, not inferred from the familiar initial zeros.
The review must cover all times, including both endpoints; samples and
uncertified cancellation estimates cannot supply that coverage.

Inspect the primary validated-integration theorem and its relevant
proof cases and the existing complete-kernel estimates before deciding
whether to import or specialize. The old integration lead is not itself
a paid evaluator or magnitude bound. The source review should specify
one finite certificate test with every error charged, or identify the
missing input and park this dependent proposal. It must not derive that
new certificate while approving it. Full matching Mathlib coverage is
unchecked.

Continuation test: approve later work only if the source comparison
supplies a genuinely enclosing direct-integral method and a concrete
bounded uniform-sign test. Abandon that method if its certified errors
cannot separate the needed signs or an essential hypothesis is unpaid;
do not convert non-decision into a negative mathematical sign. Preserve
the step206 fixed coefficient-width and step2157 inner-contour stops.
This is not a finer replay of either mechanism: the candidate observables
are six real function values, with no inverse moments or F_z/F contour.

This nomination is not a central creative mechanism. No justified bridge
from the finite H2 margin to uniform degree/global positivity has been
identified. That is the blocker to creative routing, not a quota reason
to rename routine certification as discovery. No new mathematics was
undertaken in preparing this uncovered continuation.

## Completed comparison, 21 November 2026 (step2166)

The exact target remains the six signed real integrals and their three
products on the closed time band. Outcome EXPLORATION: a bounded test
is documented, but no mathematical sign or negative numerical result.
No new mathematical result was derived or approved in this review.

### Primary coverage

F. Johansson, *Numerical integration in arbitrary-precision ball
arithmetic*, arXiv:1802.07942v1, 22 February2018, Sections2,2.1,3.2:
read the callback, ellipse bound, direct-box fallback, work-limit and
improper-integral cases. The finite-segment method needs an enclosing
callback; Gaussian error also needs analyticity and a finite magnitude
bound on an enclosing complex ellipse. Parameter uncertainty and work
limits can prevent requested accuracy. Inspect returned radii, not
tolerances. Section3.2 leaves improper tails to the caller. An infinite
theta sum is not a supplied callback, and benchmarks prove no sign or
work budget for this problem. This reuses and extends review2157's
comparison to signed real integrals; no Gaussian evaluator is approved.

The frozen [Arb2.23 contract](https://arblib.org/acb_calc.html), Types,
Integration and Options, was read through the nonconvergence and
evaluation-limit cases. It agrees with this interpretation. Current
FLINT3.7.0-dev documentation (generated20November2026) was consulted
as comparison, not the sole theorem authority. The continuation instead
selects the already assessed real Simpson method.

[NIST DLMF3.5(ii)](https://dlmf.nist.gov/3.5.ii), (3.5.6)-(3.5.8),
citing Davis and Rabinowitz (1984), pp57-58: read the full real C4
hypothesis, rule, positive even panel count and remainder. Composite
Simpson absolute error is bounded by (b-a)h^4 sup|f''''|/180,
h=(b-a)/n. Finite smooth theta sums with real exponential, power and
cosine factors fit once their specialized derivative bound is proved.
The source supplies no such numerical bound. No reproof of Simpson's
theorem is justified; its application and error arithmetic are the work.

G. Strang and E. Herman, *Calculus Volume2*, OpenStax (2016),
[Section6.3, Theorem6.7](https://openstax.org/books/calculus-volume-2/pages/6-3-taylor-and-maclaurin-series):
read the statement and complete Rolle/telescoping proof. In the safe
C^(n+1) case on an interval containing the center and evaluation point,
a bound M on the (n+1)st derivative gives error at most
M|x-a|^(n+1)/(n+1)!. L058 supplies time smoothness and integral
derivatives; the numerical uniform bound remains unpaid. The theorem
also permits finite real trigonometric evaluation with a proved error.
One proof sentence calls its auxiliary g a polynomial, generally false;
the required differentiability follows under the safe smoothness
hypothesis used here. That wording is not an additional premise.

Reuse completed arithmetic coverage2066/2067 in
`2026-11-21-direct-theta-four-coefficient-certificate-review-2065.md`
and `2026-11-21-direct-theta-coefficient-calculation-2066.md`:
[Python Decimal](https://docs.python.org/3/library/decimal.html),
exp/contexts/neighbors/rounding/signals. Directed basic operations and
outward neighbors around correctly rounded half-even exp can enclose
real expressions. No certified built-in Decimal cosine is assumed.
Use the inspected finite Taylor theorem with charged remainder, or
another separately justified implementation. Constants, actual runtime,
flags and cancellation require checks. No old coefficient/error number
transfers to these changed weights.

L019/L058 were read completely: exact positive summands, a geometric
polynomial identity, compact derivative domination and an explicit full
spatial envelope are available. They do not pay a finite error budget
for this target. A later specialization may bound omitted indices on
the compact interval and the complete spatial tail separately. Retain
both and all coefficient weights. No specialized estimate is proved here.

### Search, overlap and test specification

Reused review2161's placement comparison and read C919e's hypotheses
and conclusion plus step206/2157/2161 stop notes. The scoped C919/H2
search found no completed six-endpoint certificate. The conditional
box and old coefficient/F_z/F stops remain unchanged. A time polynomial
of direct signed values is a different observable from inverse moments
or the inner logarithmic contour; initial simplicity is unnecessary.

Queries actually used: `Johansson 2018 numerical integration arbitrary
precision ball arithmetic rigorous integration Petras algorithm`;
`de Bruijn Newman H t rigorous computation integral theta tail Polymath
2019 appendix`; `"H_t" "theta" "integral" "interval arithmetic" signs`;
`"de Bruijn" "14" "29" "integration" signs`; `"theta kernel"
"validated" integration signs heat`. Unrelated and speculative hits
were not used. Inspected Polymath arXiv:1904.12438v1 (1)-(4) only for
normalization comparison; existing motion coverage was reused. Tao's
primary [fifth Polymath15 thread](https://terrytao.wordpress.com/2018/03/02/polymath15-fifth-thread-finishing-off-the-test-problem/),
2March2018, describes the small-x direct integration approach but gives
no six-sign certificate. Linked contour-shift wiki estimates/comments
and Petras's original paper remain unread leads, unnecessary for the
selected unshifted real rule. No exhaustive search or novelty claim.

One proposed test fixes U=4,N=4,80-digit outward real arithmetic,
degree-8 time Taylor expansion at lambda=1/40, and 2^18 equal Simpson
subintervals of [0,4]. Permit at most1024 equal spatial cells to certify
fourth-derivative bounds. Range the resulting time polynomial on exactly
128 equal closed cells of [0,1/20], retaining a uniform time remainder.
These are test settings, not proved errors or a runtime guarantee.

Charge omitted theta-index and full spatial errors for every coefficient,
finite quadrature, arithmetic/constants/trigonometric errors, and the
time remainder. The complete ninth-time-derivative bound on the closed
band needs its own certified tails; a compact-only bound is insufficient.
Prove the enclosing method and obtain certified error bounds before a
lengthy node pass; save partial work first. No earlier coefficient value
or error magnitude may be substituted for these new integrals.

Accept only strict opposite pair signs on every closed time cell after
all errors, recording explicit distance from zero. Samples, a requested
tolerance and a preview are insufficient. A zero-containing enclosure
is inconclusive. If a prerequisite or any sign remains uncertified at
the fixed settings, stop and preserve the controlling error without a
cutoff, precision, order or mesh sweep. No non-decision is a sign reversal
or an impossibility theorem. No such test was executed in this review.

The exact later calculation target is saved in
`2026-11-21-h2-six-endpoint-certificate-2166.md`, SPECIALIZE, for separate
supervisor approval next turn. Success could pay a placement input;
H2 assembly, all-degree mixed positivity and global coverage remain
separate. No central creative bridge is identified, so this finite
specialization is not relabeled creative. Full matching Mathlib coverage
is unchecked. No lemma/script, cross-notebook input or runtime state
was modified or used.
