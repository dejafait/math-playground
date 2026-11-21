# Fixed full-Weil shifted Schur test — completed source scope

TARGET: Test whether the complete 120-mode shifted Schur estimate is positive at tau=11/200, using C759c's floor and rigorously bounded form-dual coupling on C759a's W.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step805 searched Weil/Schur/coupling, fixed120/sine and exact11/200 terms; compared assessments791-793/800, the generic joint-energy stop, C759a/c and L759's scalar/inertia methods. Exact queries and source distinctions below; no matching shifted certificate found in inspected material and no novelty claim.
SOURCE_EVIDENCE: Read Andrews-Connes-LaGatta2611.13129v1 Lemma8.16 and its full proof; Li paper45/v2 Theorem1.1, (2.1), (4.1)-(5.5) with closed-form comparison/square completion/Parseval cases; bramble_trace paper60/v1 Theorem1.1 and Section7 through(7.8); Rump Acta Numerica2010 Section10.8 Lemma10.12 and(10.53)-(10.55), printed p71. Reuse Suzuki core/domain and CCM finite-entry coverage in assessments791-793 and L759's assessed scalar methods.
COMPARISON: Generic closed-form Schur reduction, full covariance accounting and verified matrix positivity are known machinery. Stronger support-radius positivity results do not give this shifted120-mode inequality or parity ordering. C759c pays the formerly missing complement; complete coupling and the finite sign remain to be established locally.
GAP: Prove and enclose the complete coupling covariance for the fixed integer-sine split, then certify a positive retained matrix after its penalty and every enclosure error. No coupling bound, numerical Schur sign or parity/Xi consequence is established in this literature turn.
REASON: Separate literature approval805 completes the changed coupling/finite-matrix scope. Approve one RESEARCH/REPRODUCTION attempt at the unchanged TARGET using the sufficient scalar-floor comparison below; no generic Schur reproof or source-computation import is needed.
SCOPE: Approved fixed interval(-1,1), real odd first120 integer sine modes, their complete L2 complement W, full logarithmic form domain, all five prime-power shifts and both poles, tau=11/200; scalar-floor sufficient comparison only, with no window enlargement or replacement by a prime-only form.
LITERATURE_REASON: The invocation-start target was REVIEW_REQUIRED for essential quantitative coupling and finite-matrix coverage; ready trace-audit coverage alone did not cover this changed target.

Step804 recorded a proposed continuation, without source approval or a
mathematical result. Step805's separate source approval is below.
The completed step804 C759c audit is independent of this later approval.

Essential local inputs are C759a (the full form/domain, retained space,
original costs and the qualified even trial bound) and C759c (audited
shifted complementary floor at least0.2859). L744 fixes the complete
Weil normalization. C759b and L743 are stop evidence, not positive
premises. Reuse the already inspected domain and conditional Schur
sources where their hypotheses match; inspect only the additional
essential theorem/proof cases and implementation coverage for the new
coupling/finite-matrix scope. Search the exact statement, stronger
results, duplicates and known obstacles before approving any attempt.

The bounded test sought is a certified positive retained shifted matrix
after subtracting a justified full form-dual coupling penalty. The
review must make that sufficient comparison precise from its source;
no formula, finite-matrix positivity or operator-domain condition is
silently presumed here. A successful certificate could combine with
C759a's even trial to support a conditional fixed-window parity
comparison. Even simplicity/sign and actual-Xi realization with
multiplicities remain independent unresolved steps.

Continue only if exact source scope and a reproducible finite comparison
are specified with the complete infinite complementary form controlled.
A certified failure of the chosen sufficient matrix test stops that
estimate, not the actual parity inequality. An inconclusive enclosure
does not count as a negative result. Preserve the previous separate-cost,
arithmetic3/2 and generic joint-energy stops: the new input is C759c's
positive complementary floor, not a claim that those stops were false.

No bounded new central Xi mechanism was identified in this audit.
This established conditional route must not be labeled creative merely
because a scheduling preference requests discovery; the missing
independently testable Xi bridge is the blocker. Source review is needed
for the changed target, not to repeat the ready trace coverage.

## Separate approval — step805, 13 November2026

The nomination above records step804's pending scope; this section and
the current fields supersede that gate. This is one literature-only
comparison. No new mathematical result, numerical test, lemma or
mathematical script was produced. The exact TARGET is now ready for
one bounded REPRODUCTION attempt. Its success is not presumed.

### Primary coverage actually inspected

Andrews, Connes and La Gatta, *The uncertainty operator, the Weil ground
state and the zeros of zeta: a numerical study and conditional positivity
of the Weil quadratic form*, [arXiv:2611.13129v1](https://arxiv.org/html/2611.13129v1#S8.SS6),
9 November2026, Lemma8.16: a finite-dimensional orthogonal form split
needs a strictly coercive complementary closed form and a continuous
form-dual cross map. Its proof eliminates the cross map by square
completion. Use its nonnegative Schur implication after shifting Q;
a positive Schur eigenvalue is not itself a full-operator gap. No
conditional ladder hypothesis or Theorem8.14 estimate is imported.

Hongmin Li, *Cutoff-free positivity of localized Weil forms through
the (log11)/2 threshold*, [paper45/v2](https://rstation.ai/problems/riemann_hypothesis/papers/45),
9 November2026: Theorem1.1 is unshifted positivity through(log11)/2,
with no explicit coercivity constant or parity ordering. Read(2.1),
Sections4-5 including the core-to-closure comparison(4.7)-(4.8), square
completion(4.9), and complete covariance/tail comparison(5.1)-(5.5).
They justify the abstract lower-block/covariance method, not a numerical
bound for this different integer-sine120 split. Its400-mode odd basis
is half-integer; neither its finite arrays nor its tail constants apply
here. Supplements and source computations were not replayed.

bramble_trace, *Full-source Schur certificates for Weil positivity at
support radius two*, [paper60/v1](https://rstation.ai/problems/riemann_hypothesis/papers/60),
26 October2026: inspected Theorem1.1 and Section7,(7.1)-(7.8), including
the complete omitted-tail estimate. It asserts unshifted positivity
through radius2 using a different response/core elimination and large
intermediate matrix. This supplies overlap evidence for the method,
not the required shifted120-mode bound. No numerical constant or
external certificate is imported. Historical access stops do not
invalidate today's readable theorem; no archive retry is necessary.

Siegfried M. Rump, *Verification methods: Rigorous results using
floating-point arithmetic*, Acta Numerica19(2010),287-449,
[corrected author PDF](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf),
Section10.8, printed p71, Lemma10.12 and(10.53)-(10.55), including the
residual argument following the lemma. For a real symmetric matrix S,
any proposed factor R and scalar alpha, a rigorous bound
||S-alpha I-R^T R||_2<=epsilon gives
lambda_min(S)>=alpha-epsilon. Require alpha>epsilon. Entry, integration,
tail and factorization errors must all enter the residual enclosure.
An approximate factor alone proves nothing. The surrounding linear
solver's a priori positivity assumption is not needed for this
a posteriori implication. The separate2006 positive-definiteness paper
was found but is an unused lead; its optimized algorithm is unnecessary.

Reuse, without a new domain review, the Suzuki2606.09096v2 core/parity
coverage in assessments791-793 and C759a Sections1/6. Reuse CCM
2511.22755v1 Lemma2.3 and Section4(4.2)-(4.4) through the November4
spectral-triples finite-entry assessment. That normalization applies
at lambda=e, L=2; the lambda=sqrt13 numerical output does not.
L759 Section3's scalar/remainder/outward-rounding methods and Section4's
finite spectral/inertia procedure are supporting methods only.
No source positivity computation, RH assumption or cross-notebook
result is an input. Full matching Mathlib coverage is not checked.

### Precisely approved sufficient comparison, not a derived bound

Keep C759a's V,W and complete form domain. For q_tau=Q-tau||.||^2,
tau=11/200, write its retained matrix A and cross form B in this
orthonormal integer-sine basis. C759c supplies the existing complementary
bound D>=dI with the exact rational d=2859/10000. The next attempt may
use the scalar lower-block case of the cited square completion:

    S_d = A - K/d,

where K is the covariance of the complete cross map into W, provided
that map is first proved to have L2 representers. This is the source's
comparison with lower complementary operator dI, not an identification
of the exact Schur complement A-BD^(-1)B*. Prove the applicability and
all quantitative values next turn; neither L2 representability nor a
covariance enclosure is asserted by this approval.

The concrete research obligations are:

- Identify the full cross representer for each of the120 sine vectors
  from Q, including the archimedean multiplier, all five prime-power
  translations and the signed pole. Prove L2 membership and the pairing
  identity on the whole complementary form domain. Finite form norm
  by itself must not be called an L2 operator-domain argument.
- Apply the exact W projection and enclose its full Gram matrix K.
  Plancherel/Parseval are the standard named inputs for this step.
  Use the Fourier integral definition at removable sine denominators;
  C759a(7)'s stated frequency restriction is not a global tail bound.
  Every integral and infinite-frequency remainder needs a justified
  upper enclosure. Keep mixed prime/archimedean/pole terms; separate
  component norms require a proved collective upper bound.
- Enclose A from the defining full Q at the present window, with the
  exact shift subtracted. Certify K<=K_plus in quadratic-form order,
  then test the finite sufficient matrix A-K_plus/d, accounting also
  for A's enclosure. Entrywise upper bounds alone do not give a matrix
  upper bound. A norm-error times identity is an admissible correction
  if its norm bound is proved. Use verified symmetric elimination or
  Rump's residual method, with all120 directions and errors included.

This prescription fixes one sufficient estimate rather than silently
requesting an exact infinite inverse. It makes the saved TARGET
reproducible without claiming the local specialization. If the L2
representers cannot be justified under these hypotheses, record that
obstruction and stop this estimate; a different form-dual mechanism
needs its own source gate. No retained-mode growth, window sweep,
alternative basis or arbitrary change of shift is approved here.

A certified strictly positive sufficient matrix retains this conditional
route. A rigorously negative Rayleigh value of the chosen S_d stops
that sufficient estimate, even if the true Schur form could be positive.
Failure to find a positive enclosure, pivot overlap or an unresolved
tail is inconclusive. Do not turn an upper-bound failure into evidence
against the actual parity inequality. Successful positivity would pay
the odd floor at tau and permit comparison with C759a's qualified even
trial U<tau; simplicity/sign and Xi realization remain independent.

### Search, duplicates and stopping evidence

Queries actually issued: `"Weil" "Schur complement" "coupling"`;
`"Weil" "120" "sine" positivity`; `"Weil" "120" "Schur" shifted sine`;
`"Weil" "Schur" "11/200"`; `"Weil" "integer sine" coupling complement`;
`Rump verified positive definiteness interval Cholesky matrices theorem pdf`.
The exact-shift and sine searches did not supply a matching primary
certificate. Search summaries, discussion posts, aggregators, screened
papers at other radii and secondary matrix expositions were not used
as theorem inputs. No novelty is inferred from this bounded search.

The scoped local comparison used assessments791-793/800, C759a's
domain/stop, C759c's exact conclusion and L759's methods. C759b/L743
are retained stop evidence as qualified in those assessments; no new
prime-only estimate or source refresh is needed. The4 November generic
joint-energy source stop remains correct: Schur algebra did not pay a
complement or a cross estimate. C759c changes the first prerequisite,
not that historical reasoning. No duplicate full coupling certificate
was found in the inspected local paths. Broad archive orientation was
not undertaken.

The new evidence is completed source coverage and an explicit bounded
comparison, not mathematical progress beyond the inspected sources.
This established-route specialization defaults next to mathematics.
There is still no justified creative central Xi mechanism: an
independently testable full-energy-to-Xi bridge is missing. Do not
relabel covariance certification as creative to satisfy a preference.
