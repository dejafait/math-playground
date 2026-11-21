# First absolute moment obstruction — nomination1389, source review1390

TARGET: Test whether a sub-square-root-log first absolute moment for C019n's actual moving-time sum rules out its sufficient bound R<=c_D B/2.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1390 searched sharp fractional zeta moments, first absolute heat moments and weighted Riemann-Siegel moments; narrowly searched the November17 Jensen assessments/history/attempts for first moments, fractional moments, Heap and Fourier multipliers, and reused assessments1374/1376/1381/1385 plus stops1345/1355/1387. No inspected source states the exact moving-time target; no novelty inference.
SOURCE_EVIDENCE: Inspected Heap-Radziwill-Soundararajan arXiv1901.08423v1 Theorem1, Section2 Propositions1-3 and their assembly; NIST DLMF25.9.1-3 (Titchmarsh1986 (4.12.4), (4.17.1), pp79,88), DLMF5.11.1-4 and fixed-sector hypothesis; Tao245C Notes2 (6April2009) Definition32, Example33, Exercises30/34/38, (10)-(11) and inversion proof. Reused C019k/l/m and corrected C019n with their existing source assessments.
COMPARISON: The unconditional critical-line theorem at k=1/2 bounds the ordinary first absolute zeta moment by O(X q^(1/4)), below the requested square-root-log scale. It does not cover V directly. Classical two-sum approximation and Fourier inversion supply tools for one bounded real-smoothing transfer; uniform moving kernels, phase curvature, cutoffs and tails remain a separate application to prove.
GAP: Prove or fail a deterministic transfer giving integral_J |V|=o(B sqrt(q)) with the actual C019n phase/time/floor, then test its sufficient R budget using the existing negative pointwise H and exact bounded total. Neither the transfer nor an implication for R is established by this literature review.
REASON: Separate review1390 supplies the missing primary moment and smoothing-tool coverage for the unchanged nominated target. A direct citation is insufficient because V is a deformed finite real sum. Only the identified application is approved; do not reprove the fractional-moment theorem or assume a heat moment, random value law or signed conclusion.
SCOPE: Exactly corrected C019n and inherited C019l/m, actual xi via C019j/k and L018/L021, d through all sufficiently large integers, t(Y)=Y^2/(2d), own floors at Y and Y+h, h=3*pi/q, J and D unchanged; no RH, Gaussian law, independence, fixed heat time or effective onset.
LITERATURE_REASON: The saved target had REVIEW_REQUIRED: its essential first-absolute-moment source was unread, and the earlier square/correlation assessments do not cover a logarithmic saving. This completes that mandatory review rather than refreshing a ready target.

## Preserved nomination1389, not a derived result

The completed audit1389 retains the partial Laplace reduction. Its
weighted diagonal is negative, but its sufficient upper bound for R is
unpaid. The new candidate is to test that budget against a sharper
first absolute moment of the actual sum and the exact bounded total
in C019n (5)/(9). This asks whether the chosen sufficient condition is
too strong; it does not propose a disproof of (N) or RH. No implication
from the proposed moment estimate has been proved in this nomination.

The concrete moment threshold is integral_J |V|=o(B sqrt(q)). A mere
O(B sqrt(q)) consequence of the square bound is not the requested
input. The absolute comparison in C019l (9) is already available,
but does not by itself supply that improvement. Read only the relevant
C019l/m/n ranges and narrowly matched local assessments/failures before
searching primary theorem statements. Ordinary zeta fractional-moment
or first-moment theorems are leads, not imports: their height interval,
real part, smoothing, uniformity and dependence on the moving heat
parameter must be compared with the exact sum here. Retain all tails
and floor changes in any proposed transfer.

Continue only if source assessment identifies an applicable theorem
or one bounded, explicitly justified transfer to this little-o scale,
with a discriminating test of the stated remainder budget. If only the
existing square estimate or a conjectural joint law is available, say
so and narrow or abandon the proposed mechanism. No repeated generic
search or calculation is authorized by this nomination. The next turn
is literature-only and may approve subsequent mathematics; this audit
neither derives nor approves that previously uncovered target.

Even an obstruction to R<=c_D B/2 would stop only that sufficient
closure. A sharper balance using the actual I_H, (N), ordered samples,
reciprocal root mapping, bulk separation and actual-Xi all-degree
positivity remain unresolved. Stops1345/1355/559 and attempt1387 retain
their scopes. Full matching Mathlib coverage is unchecked.

Next routing: literature_comparison, standard/high. The difficulty is
the exact applicability of moment estimates to a vanishing but moving
heat time and its actual cutoff. No mathematical derivation, script or
new result is part of this nomination.

## Source review1390 — 17 November 2026

This separate literature turn supersedes the nomination's pending-source
status and routing, while retaining its exact TARGET. It establishes
source coverage for an attempt, not the target estimate or an obstruction.
No lemma or mathematical script was written or modified.

### Search, duplicates and failures

Queries included `Heap Radziwill Soundararajan sharp upper bounds
fractional moments Riemann zeta function 0 k 2 theorem 1`,
`Riemann zeta heat flow first absolute moment small time H t fractional
moments`, `"heat" "zeta" "first moment" "absolute"`,
`"Riemann Siegel" "fractional moments" weighted sum`, and
`"zeta" "moving" "heat" "moments"`. Search summaries and public
notebook mirrors were not theorem evidence. The bounded search found
no directly matching statement; it does not establish novelty or absence.

The local comparison used the named November17 Jensen paths, C019l (8)-(9),
C019m hypotheses/(2)/(19), corrected C019n hypotheses/(1)-(9), diagonal
proof/(12)-(14) and qualifications, and attempt1387's audit update.
Assessments1374/1376/1381/1385 already cover the finite-sum reduction,
ordinary shifted moments and square-bound scope. Their unread fractional
Riemann-Siegel remainder lead2610.03728v2 is still not needed or imported.
No completed first-absolute-moment transfer was found in those paths.
Stops1345/1355 concern exterior Airy payment/fixed endpoint signs; stop559's
automatic unshifted bulk import remains as recorded in assessment1381.
Attempt1387 stops origin continuity/direct absolute variation, not every
possible R obstruction. The present amplitude test changes the mechanism;
it does not retry those estimates or reopen parked direct (A).

### Inspected theorem inputs and exact limitations

**Heap, Radziwill and Soundararajan**, *Sharp upper bounds for fractional
moments of the Riemann zeta function*, Q. J. Math.70 (2019), 1387-1396,
DOI10.1093/qmathj/haz027; numbering here is
[arXiv1901.08423v1](https://arxiv.org/html/1901.08423v1), 24 January2019,
Theorem1. For real 0<=k<=2 and U>=10 it states
integral_U^(2U) |zeta(1/2+iy)|^(2k) dy << U(log U)^(k^2),
unconditionally. Taking k=1/2 is within its stated range and yields
the first absolute moment with exponent1/4. Its introduction credits
earlier reciprocal-integer cases to Heath-Brown; no new moment theorem
or priority claim is proposed. Read Section2's Propositions1-3 and their
assembly: both the ordinary short-polynomial mean and the zeta fourth
moment twisted by a short polynomial enter. There is no RH hypothesis
in this upper-bound theorem. The full later proofs were not reread.
It applies on dyadic critical-line intervals, not to an arbitrary
weighted polynomial or a heat curve. Import it, without reproof.

**NIST DLMF25.9**, [equations25.9.1-3](https://dlmf.nist.gov/25.9),
read17 November2026. The approximate functional equation requires
x,y>=1, 2*pi*x*y=u, fixed 0<=sigma<=1, u tending to infinity.
The critical-line case25.9.3 explicitly uses m=floor(sqrt(u/(2*pi)))
in both sums and has error O(u^(-1/4)). Its cited book source is
Titchmarsh, *The Theory of the Riemann Zeta-Function*, second edition,
revised Heath-Brown (1986), (4.17.1), p88;25.9.1 cites (4.12.4), p79.
This is sufficient; no higher-order remainder expansion is needed.
The Rutgers book PDF's opening was accessible but targeted retrieval
timed out; no unread book passage is claimed as evidence. DLMF supplies
the exact needed statement, so there is no essential access blocker.
The source retains the ordinary floor, not C019n's slightly different
floor or any floor at a translated ordinate.

For the Hardy phase, reuse **Gonek-Ivic**,
[*On the distribution of positive and negative values of Hardy's Z-function*, arXiv1604.00517v1](https://arxiv.org/html/1604.00517v1),
2 April2016, (1.1) and the
discussion immediately following it, reopened in this review: Z is real
and |Z(y)|=|zeta(1/2+iy)|. Do not use their RH/pair-correlation Theorem2.
The gamma phase conversion is covered by the reused
[DLMF5.11(i)](https://dlmf.nist.gov/5.11.i), (5.11.1)-(5.11.4),
with fixed sector |arg z|<=pi-delta; these statements and that hypothesis
were reopened. The exact Hardy phase and C019l's elementary vartheta
must still be compared in the application. No derivative of an
uncontrolled asymptotic error is authorized.

**Tao**, [*245C, Notes2: The Fourier transform*](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/),
6 April2009, Definition32, Example33, Exercises30/34/38 and (10)-(11).
Smooth compactly supported functions are Schwartz; the Fourier transform
is continuous on Schwartz space; (11) gives inversion there. Read the
proof via Gaussian approximate identities, Exercises40-42, and the
derivative-to-decay identity in Exercise30. These are tools for uniform
kernel envelopes, not a theorem about variable-time heat sums. The
source's transform uses exp(-2*pi*i*x*xi); the application must fix and
retain its convention. No reproof of Fourier inversion is needed.

Polymath1904.12438v2's Theorem1.3 has 0<t<=1/2, so it must not be
cited at t=0 by simply ignoring this strict hypothesis. Its statement
and Proposition6.2/(48)-(58) were reopened while locating the classical
input. No new use or derivation from that proposition is required:
the existing C019k comparison is reused, and DLMF25.9.3 supplies the
ordinary critical-line approximation separately.

### One bounded application approved, not performed

The known first-moment scale is smaller than B*sqrt(q), since B is
a fixed positive multiple of X and q=log X. This comparison concerns
ordinary zeta only. C019m's square estimate remains the only established
moment bound here for the actual moving sum.

Attempt a real Fourier smoothing of the ordinary two-sum Hardy
approximation: extend the existing bounded-frequency heat weight
smoothly outside the attained v_n(Y)/q range, then test an integrable
kernel envelope uniform over Y and d. Treat the phase correction and
its conjugate together. This is a proposed application of the cited
tools, not an asserted representation or new lemma. Positive heat time
does not license a globally bounded backward-heat operator; a frequency
cutoff and its exact agreement on the finite sum must be proved.

The bounded test must pay phase curvature under translations, the
ordinary/deformed/translated floor discrepancies including equality,
and all Fourier tails before applying the imported moment bound.
Use a kernel dominated uniformly in Y; a separate L1 norm at each Y
alone does not justify exchanging a moving operator and the height mean.
Nearby translated intervals can use the theorem by covering them with
finitely many dyadic intervals; arbitrary tails require their own bound
or truncation, not an unproved global Hardy growth estimate. Finite-sum
tails may instead use the already available pointwise envelope.

Seek O(B*q^(1/4))+o(B*sqrt(q)), or another proved little-o bound with
the same uniformity. O(B*sqrt(q)) alone fails. If this transfer fails,
record the specific unsummable error or missing uniformity and abandon
this smoothing mechanism; do not silently substitute a fixed time,
complex Dirichlet half-sum, Gaussian value law or conjectural moment.
No general moving-coefficient mean-value theorem is being assumed.

Only after the moment is proved, test concentration of E in C019n's
pointwise-negative diagonal integral against its bounded exact total
I_V=I_H+R. Determine whether R<=c_D*B/2 can actually persist; no such
implication is derived here. A failure of that sufficient condition
would leave (N) and RH open. Ordered samples, reciprocal mapping, bulk
separation and all-degree actual-Xi positivity remain independent gaps.

Decision SPECIALIZE authorizes exactly this difference from known
results, under the unchanged TARGET. Source coverage is ready for the
next research attempt. Full matching Mathlib coverage was not checked;
Fourier/integration support would not itself formalize this application.
Completed outcome is a literature EXPLORATION, not a mathematical advance
or a proved obstruction. Next routing is proof_attempt/development,
deep_research/xhigh: the application has moving kernels, curved phases
and cutoffs despite standard source inputs.
