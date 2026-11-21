# Logarithmic-floor full regular-time transport: comparison2119

TARGET: Assess whether C488d's logarithmic-floor statistic satisfies A'(t)<=sum_j 40(|x_j|+R)log(32(|x_j|+R))A_j/R^2 at every time 0<t<=1/5 with no multiple zero, for all real a and R>=200, counting multiplicity.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step2119 searched weighted trace/count transport and the exact logarithmic-floor terminology, read paper186/v1 AppendixB's complete nearby and distant cases through (B.5), compared Polymath3.1(i),1.5(i)-(ii),3.2, and reused assessment2115 with C488a/c/d and L488. No matching changed-floor/rate40 theorem was located; this is not an absence or novelty claim.
SOURCE_EVIDENCE: bramble_trace, An unsigned strip bound for the de Bruijn--Newman constant, rStation paper186/v1,20November2026, Section1 and AppendixB/(B.1)-(B.5), https://rstation.ai/problems/riemann_hypothesis/papers/186 ; D.H.J.Polymath, Research in the Mathematical Sciences6(2019),article31, arXiv1904.12438v2,4August2019, Proposition3.1(i)/(28), Theorems1.5(i)-(ii),3.2, https://arxiv.org/html/1904.12438v2 . These statements were inspected; prior velocity-proof coverage is reused from assessment2115. Local normalization, counts and regularity are reused as specified below.
COMPARISON: C488a(6)-(8) already provide the full pair decomposition and paired exterior bounds for the older floor; C488d pays the changed nearby real-partner term. The changed p'' and segment comparisons, and the resulting rate40 budget for arbitrary a,R>=200, remain a quantitative specialization rather than a directly cited theorem or a new transport mechanism.
GAP: Prove or explicitly fail the changed floor's second-derivative and short-segment bounds, then assemble all regular-time contributions against the exact rate40 threshold. No changed-floor full differential inequality has been proved in this review.
REASON: Essential proof cases and applicability are now assessed; no source blocker remains for one bounded mathematical test. Citation alone does not supply the changed derivatives or widened-domain constants. This approval covers attempting the target, not its truth.
SCOPE: Exact TARGET only, with C488d's fixed a,R,w,p, all-copy counts, positive regular times and opposite-paired exterior summation. Permits the needed derivative/segment calculations and full rate-budget test; excludes collisions, integration, time-zero passage, initial mass and global conclusions.
LITERATURE_REASON: The start nomination excluded nonreal pairs and distant reciprocal tails from ready coverage; their changed-weight applicability was essential unread coverage. This turn completes that comparison and does not repeat the ready count audit.

## Preserved nomination2118: exact proposed statistic and decision test

Use the actual H_t family and normalization of L058/C488a. For fixed
real a and R>=200, use exactly C488d's w and p, and put

    A_j(t)=1_(y_j!=0)[w(x_j)|y_j|+p(x_j)],
    A(t)=sum_j A_j(t),   z_j=x_j+i y_j.

The proposed inequality sums over the nonreal copies. At the stated
positive regular times the existing actual-family confinement input
makes their number finite; the exterior zeros still enter the velocity
law in its prescribed opposite-paired order. Time derivatives are with
a and R fixed. No assertion at a collision or derivative at t=0 is
included in this target. The number40 is a proposed sufficient rate
budget, not a bound already calculated or approved in step2118.

Essential proposed inputs are C488a's count, strip, paired product,
velocity law and nearby/distant proof cases, C488c's count, and the
now-audited C488d payment. Reuse their literature assessments wherever
the hypotheses agree; inspect the primary proof cases needed to decide
the changed-weight application. Search for stronger or matching known
weighted transport results and relevant recorded failures. Import any
matching result with precise hypotheses rather than reproduce it.

Main gap: L030-L032/C032a actual-Xi all-degree algebraic mixed
positivity. This intermediate target tests whether the single paid
cost fits an entire regular-time transport inequality. A pass would
permit a subsequent assessment of integrated finite-head exclusion
with the larger count floor. It would not itself establish that
integration, improved exclusion, all-height reality, or mixed signs.

Continue only if the source comparison approves this exact bound or
identifies a precise already-known replacement with a justified use.
Stop this proposed rate if a necessary estimate fails; distinguish a
failed majorant from a counterexample to the actual-family inequality.
Keep collisions, summability through time zero, initial mass, exterior
forcing and all-height overlap as separate unpaid obligations. The2113
global-only bridge failure and the September20 whole-plane supremum
obstruction remain evidence, not global prohibitions. Full matching
Mathlib coverage is unchecked. No full-transport mathematics was
derived or approved in this nomination.

No bounded new central sign mechanism is justified by the completed
nearby-cost audit. In particular a larger count floor does not supply
the missing actual-Xi signs or global initialization. This is a
routine established-route source comparison, not a creative target
selected to satisfy a routing frequency.

## Completed source comparison2119 — 21 November2026

The preceding nomination records what was uncovered at entry. The
single-line decision above and this section supersede its readiness
statement; its exact proposed inequality is unchanged. This was a
literature-only step. No new derivative inequality, transport bound,
lemma, mathematical script or candidate solution was produced.

### Primary statements and essential cases actually inspected

bramble_trace, *An unsigned strip bound for the de Bruijn--Newman
constant*, [paper186/v1, 20November2026, AppendixB,
(B.1)-(B.5)](https://rstation.ai/problems/riemann_hypothesis/papers/186):
read the same-sign, opposite-sign, mixed, own-conjugate, count-curvature,
distant-vertical and opposite-paired-horizontal cases, including the
coefficient assembly. Its floor is R/[4Q log(4Q)], Q=V+sqrt(x^2+R^2),
V=6*10^12; its stated domain restricts |a|<=X, R>=200 and
R/V<=1/1000. It states rate20 for that statistic, not this target.
Its author theorem and reviewer's broader computational claims are
not independently verified by this reading.

D.H.J.Polymath, *Effective approximation of heat flow evolution of
the Riemann xi function, and a new upper bound for the de Bruijn--Newman
constant*, [arXiv1904.12438v2, 4August2019,
Proposition3.1(i), (28); Theorems1.5(i)-(ii),3.2](https://arxiv.org/html/1904.12438v2):
the selected zero must be simple; other copies need not be real or
simple. Reciprocal tails use opposite pairing. For 0<t<=1/2 the
large-abscissa zeros are real, with unique multiplicity-counted zeros
in the specified small disks. Theorem3.2 imports de Bruijn1950,
Theorem13, with initial upper strip height h>0 and later bound
sqrt(max(h^2-2(t-s),0)). These statements supply no changed-weight
transport estimate. The source's general constants are unspecified.

### Applicability and exact remaining specialization

Use canonical C488a's audited formulas (2),(4),(6)-(8), rather than
assuming the whole author theorem. Its count proof (4) has independent
domain u>=0, 0<=t<=1/5. The finite-head parameters elsewhere in C488a
do not restrict that proof. C488c(2) supplies the closed-window local
count on |x|>=2r>=400; C488d already handles the central regime
separately and gives coefficient3/25 for the nearby mixed count cost.
Assessment2115 and the audit in C488d are reused unchanged; this turn
does not reprove the count or the absorption.

L058 and C488a identify the actual H_t normalization. L488 supplies
a common compact set for nonreal or multiple zeros on every compact
positive-time interval; its coordinate conversion is lambda=t/4 and
F(lambda,z)=8H_(4lambda)(2z). For a fixed regular time this is the
input for a finite differentiable contributing sum and persistence
of the real exterior. It does not supply a compact set down to zero.
At t=1/5 the source time range permits a positive neighborhood on
both sides; the target is still only the regular-time derivative.

The outstanding work can therefore be localized precisely:

- For the unchanged w, the nearby height terms are the already
  audited C488a(6) cases. For the changed p, the nearby nonreal
  contribution requires its own bound on sup_segment |p''| in
  endpoint p units. C488d's first derivative bound alone is
  insufficient. The old constants1.01 and3 cannot be copied.
- Keep the own-conjugate loss separate when applying C488d, so it
  is not also charged as a generic nearby pair. Use the exact closed
  cutoff |d|<=R and count all copies. The source's summation by
  endpoints uses C488a(4); a new local-count summation theorem is
  not required for the proposed rate scale.
- The distant vertical sign and its absolute convergence use the
  actual strip and conjugation, not the choice of p. The distant
  horizontal reciprocal estimate in C488a uses m=|x_j|+R, a finite
  portion |x_k|<=2m and an opposite-paired tail |x_k|>2m. Its
  geometric/count inputs have no dependence on a or V; the changed
  trace multiplier still needs to be bounded in A_j units. Preserve
  the source's pairing order, rather than asserting absolute
  convergence of unpaired complex reciprocals.
- The final numerical assembly must be redone with the proved new
  constants. It must meet 40m log(32m)/R^2 for every m>=R>=200,
  with no sampled-domain argument or suppressed additive constants.
  This review makes no claim that it does so.

This is a specialization of a known proof, requiring changed
hypotheses and effective constants. No reproof of the general velocity,
confinement or count theorems is needed. The narrow replay of pair
bookkeeping is justified to ensure that the changed derivatives pay
every term on the widened domain. Full matching Mathlib coverage
remains unchecked; no absence claim or Mathlib input is used.

### Searches, duplicates and recorded failures

Fresh queries: `"de Bruijn" "weighted" "nonreal" transport zeros`,
`"zeros" "logarithmic" "floor" "heat" Newman transport`,
`"de Bruijn" "weighted trace" zeros`,
`"nonreal" "transport" "1000" "log"`, and
`"nonreal" "weighted count" "heat" zeros logarithmic`.
Most exact-floor results were irrelevant; the directly relevant
primary hit was the already identified AppendixB. Read the opening
and weighted-propagation scope of the author's
[discussion96](https://rstation.ai/r/riemann_hypothesis/posts/96):
it points back to paper186 and offers no matching changed-floor
statement. Its review reports are not substitutes for primary proofs.
Other search hits on collision exclusion, translated probes and
heat-flow lifetimes were not inspected theorem-by-theorem and are
unread leads, not imported results or evidence of an obstruction.
This bounded search does not establish novelty or exhaust the literature.

C488a is the existing full-transport duplicate mechanism; C488d is
only the changed nearby mixed input. L133 controls an inverse-square
exterior sum under unit-window counts, not the first-derivative
opposite-paired horizontal sum or the full weighted trace. Its proof
and the specific stops were checked, without opening its other
dependencies. The [2113 global-only bridge stop](../../ATTEMPTS/2026-11-21-local-count-global-bridge-unpaid-2113.md)
is a failed sufficient count bridge, subsequently addressed by C488c;
it is not a counterexample to this target. The
[September20 heat-route audit](../../ATTEMPTS/2026-09-20-heat-fourier-relevance-audit.md)
records the separate moving-supremum and global-closure gaps. Their
evidence is preserved; neither is a ban on this finite-sum test.

### Continuation and abandonment test

The exact TARGET is now ready for a separate mathematical invocation,
subject to the supervisor's separate approval of this changed
assessment. Classify that work as REPRODUCTION unless a changed
target first receives another assessment. Prove the full stated
regular-time inequality, or record an explicit failed necessary step
of this sufficient majorant with its parameter regime. A failed
majorant stops that argument for rate40; it does not refute the
actual-family inequality without an actual-zero counterexample.
Preserve partial reasoning if the budget does not close.

A pass would justify assessing an integrated finite-head application
with this larger detection floor. It would leave collision passage,
time-zero summability, initial mass and all-height
overlap unresolved, and would not imply L030-L032/C032a. No new
central sign mechanism is justified by this source comparison;
the missing bridge to actual-Xi all-degree signs and initialization
blocks a defensible creative nomination. The next task is one
bounded quantitative specialization, not further browsing to fill a
quota or a creative label attached to an established mechanism.
