# Changed-floor integration: completed source comparison2122

TARGET: Assess whether C488e's unchanged statistic obeys A(t)<=A(0)+integral_0^t sum_(j:y_j(u)!=0) 40(|x_j(u)|+R)log(32(|x_j(u)|+R))A_j(u)/R^2 du, with a finite Lebesgue integral, for every real a, R>=200 and 0<=t<=1/5, including collisions and multiplicity.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step2122 searched de Bruijn weighted/nonreal collisions, heat-flow weighted-trace integrals and the exact logarithmic-floor terminology; inspected the primary cases below and C488a's complete collision/time-zero section; reused assessment2118/2119 and C488e audit2121 for regular times. No matching changed-floor finite-integral statement was found; no novelty or exhaustive-search claim.
SOURCE_EVIDENCE: bramble_trace, An unsigned strip bound for the de Bruijn--Newman constant, paper186/v1,20November2026, AppendixB/(B.1),(B.3),(B.5)-(B.6) and complete collision/time-zero paragraphs, https://rstation.ai/problems/riemann_hypothesis/papers/186 ; D.H.J.Polymath, Research in the Mathematical Sciences6(2019),article31, arXiv1904.12438v2,4August2019, Proposition3.1(ii), formula(30) and proof through its final Rouche argument, Theorems1.5(i)-(ii),3.2, https://arxiv.org/html/1904.12438v2 . These cases were read; the 1950 strip proof and the full saddle estimates are accepted cited inputs, not independently audited.
COMPARISON: The known collision/time-zero mechanism in C488a applies through continuous positive weights and count-controlled exponential tails; the changed p and rate-weighted finite Lebesgue integral need explicit specialization. C488e already supplies the exact regular-time inequality. Neither primary source directly states this full changed-floor/all-a,R assertion.
GAP: A later mathematical attempt must justify multiplicity-preserving time slices and jumps, measurability and a time-uniform summable majorant for the rate-weighted trace, right continuity at zero, and integration through events. No part of the proposed integrated conclusion is established by this review.
REASON: Essential source cases are now covered and isolate an admissible established-route specialization; no essential source blocker remains. Citation alone does not prove the changed-weight integral. Ready scope authorizes a separate mathematical attempt, subject to the supervisor's approval, rather than deriving and approving the result here.
SCOPE: Exact TARGET only, unchanged fixed real a,R>=200,w,p,A and actual H_t on [0,1/5], counting multiplicity; includes the proposed finite integral, collisions and time zero. Reuse C488e at regular times. Excludes initial-smallness estimates, finite-head exclusion, uniformity over unbounded a,R, all-height reality and mixed signs.
LITERATURE_REASON: Changed hypothesis and conclusion: the proposed bound includes collision times and time zero, both expressly excluded by assessment2118/2119 and C488e.

## Preserved nomination2121: exact proposed continuation and relevance

Keep the actual H_t normalization and precisely C488e's fixed real a,
R>=200, w,p and A_j=1_(y_j!=0)(w(x_j)|y_j|+p(x_j)). Extend that
definition to every slice 0<=t<=1/5, counting each zero with its
multiplicity. The proposed integral is a sum over zero copies at
each time; it must not depend on a globally smooth enumeration.
Finiteness of A(0) and of the displayed nonnegative Lebesgue integral
are requirements to assess, not facts established by this nomination.

Main gap: L030-L032/C032a actual-Xi all-degree algebraic mixed
positivity. This intermediate target would permit later finite-head
transport applications when initial mass and exterior forcing are
separately controlled. It neither supplies those controls nor bridges
to all-height reality or all-degree mixed signs. The goal is one
integration statement, not a new finite-head numerical certificate.

Essential local inputs to compare are audited C488e, L058, L488,
C488a(2),(4) and its collision/integration/time-zero discussion, with
C488d retained through C488e. The count, strip and normalization are
unchanged. C488a's different-floor passage is an existing candidate
duplicate mechanism, not already approved coverage for this target.
Its later proof section was not inspected for the changed target in
audit2121. The next turn should first compare the exact primary
collision theorem and essential endpoint proof cases, reusing the
existing source notes wherever their hypotheses agree. Full matching
Mathlib coverage remains unchecked.

Continue only if the source comparison supplies exact coverage or
isolates an admissible quantitative specialization for every required
passage. Otherwise record the precise missing hypothesis or failed
passage and route accordingly. A failed sufficient transport argument
is not an actual-zero counterexample. Keep the2113 global-only count
bridge stop and September20 moving-supremum obstruction as scoped
evidence; neither is a global ban on this separate finite-trace test.

No justified bounded new central sign mechanism emerged from audit2121.
The bridge from this unsigned statistic to actual-Xi mixed signs and
global initialization is still missing. This nomination is consequently
an established-route literature comparison, not creative mathematics
selected to meet a scheduling frequency. Only a later gate may approve
its mathematical attempt. No lemma or mathematical script implements
the proposed integrated assertion in this nomination.

## Completed comparison2122 — 21 November2026

The nomination above preserves the entry state. Its statements about
unassessed coverage are superseded by this comparison and the single-line
fields. The target, statistic and parameter domain have not changed.
This is a literature-only EXPLORATION outcome: source readiness improves,
but no new bound, full-target import or mathematical negative is claimed.

### Primary hypotheses and essential cases actually inspected

[Polymath, arXiv1904.12438v2, Proposition3.1(ii)](https://arxiv.org/html/1904.12438v2#S3),
with formula(30) and the proof's final Taylor/Hermite/Rouche passage,
allows any real base time and any zero of multiplicity m>=2, including
a nonreal center. It exhausts the m-copy cluster; the expansion is
z_0+sqrt(2)(t-s)^(1/2)lambda_l+O(|t-s|), where the Hermite roots
lambda_l are distinct and real. Constants may depend on the cluster.
The proof covers both time directions through its square-root branch.
Theorem1.5(i)-(ii), for 0<t<=1/2 with absolute constants, gives the
large-abscissa real/simple tail used by L488 on compact positive-time
intervals. No such uniform compact set at zero is supplied. Theorem3.2
restates de Bruijn, Duke Math.J.17(1950),197-226, Theorem13: an upper
strip height h>0 at s contracts to sqrt(max(h^2-2(t-s),0)) at t>s.
The accepted initial strip and conjugation give the retained bound1.
These are imported inputs, not results to reprove in the next step.

[bramble_trace, paper186/v1, AppendixB](https://rstation.ai/problems/riemann_hypothesis/papers/186),
from (B.1),(B.3),(B.5) through the complete text following (B.6),
uses the older floor R/[4Qlog(4Q)], |a|<=X and R/V<=1/1000.
It handles real collisions by forward real splitting and downward
count jumps; nonreal clusters contribute continuously. Its compact
positive-time event argument integrates a scalar bound c_0 A+E.
Count-controlled exponential tails and bounded-region root persistence
then give its time-zero passage. The precise changed-floor integral
in our target is not asserted there. This manuscript is an audited
local mechanism in C488a, not an independently verified resolution of
its other claims. Its reviewer report and computational supplement
are not used as proof evidence.

### Exact applicability and remaining specialization

The normalization is unchanged: F(lambda,z)=8H_(4lambda)(2z), with
L058's joint entirety and conjugation. The [tau,T] confinement input is
L488 with lambda in [tau/4,T/4]; here T=1/5, so the upper endpoint
lies inside the source range. This input includes multiple real zeros,
not just nonreal zeros. The count C488a(4) is independent of that
corollary's finite-head choices and counts every copy at every time
in [0,T]. C488e's audit already assessed this independence. Keep
C488d through C488e; no new velocity estimate is requested.

The changed p is a fixed smooth positive function of x. The next
attempt must check its bounded-floor and tail hypotheses explicitly,
instead of copying the older floor's derivative constants or its
finite-head smallness conclusion. Collision geometry itself does not
use those derivative constants. The root expansion is not a global
smooth enumeration, nor does an O(|t-s|) remainder alone prove exact
forward reality: the conjugation-invariant single-root neighborhoods
in the source proof are essential.

Define the proposed right-hand trace by

    B(u)=sum_(j:y_j(u)!=0)
           40(|x_j(u)|+R)log(32(|x_j(u)|+R))A_j(u)/R^2.

The following are the precise remaining proof obligations, approved
for a later specialization attempt rather than discharged here:

1. Define A and B independently of zero labels, with every copy and
   its multiplicity. Establish their finite values and measurable
   dependence on time. Use compact positive-time confinement and the
   cluster proof; do not assume a global enumeration through events.
2. Verify the source's jump direction for the changed trace at a real
   collision, including odd multiplicity, and continuity at a nonreal
   collision. Establish the one-sided values needed at event times and
   at T. Preserve finiteness of events on each [tau,T]; events may
   accumulate as tau tends to zero.
3. Extend C488a's unweighted tail argument to B, which has an additional
   (|x|+R)log(32(|x|+R))/R^2 multiplier. Produce a summable majorant
   uniform in u in [0,T] for each fixed a,R. Finiteness at individual
   positive times and an unweighted A-tail bound do not by themselves
   meet the finite-integral requirement. Constants may depend on a,R;
   no supremum over their entire unbounded domain is required.
4. Establish A(tau)->A(0) by bounded-region multiplicity-preserving
   persistence, forward real splitting at zero and a uniform A-tail.
   Integrate C488e's A'<=B away from the finitely many positive-time
   event times, pass to their one-sided limits with no positive jump,
   then justify the tau-down-to-zero passage for the finite Lebesgue
   integral. Do not infer absolute continuity across a count jump.

These obligations isolate a quantitative/measure-theoretic
specialization of an existing proof. They require neither a new
collision theorem nor a new global count input. Citation alone is
insufficient because the source integrates a different statistic
against a scalar majorant. No summability certificate, integrated
inequality or changed-floor collision lemma is proved in this turn.
Full matching Mathlib coverage remains unchecked; no absence claim.

### Search, overlap and scoped stops

Fresh search queries were `"de Bruijn" "weighted" "nonreal"
"collision"`, `"heat flow" zeros "weighted" "trace" "integral"
Newman`, and `"nonreal" "logarithmic" "floor" "transport"`.
The relevant primary match was the already identified paper186.
Search hits about collision exclusion and translated density were
not read theorem-by-theorem in this turn; they are unread leads and
no imports or obstruction evidence. A failed exact-phrase search is
not a novelty assessment.

Reuse assessment2118/2119 for the regular-time pair estimates;
C488e's audit2121 is retained. C488a's complete collision/integration
section was read as the closest local duplicate, along with L488's
source scope and L058's normalization and joint-entire proof.
The2113 global-count bridge failure and September20 moving-supremum
stop were checked and retained. Neither concerns this fixed-weight
finite-trace passage; neither permits extrapolation to global reality.
No cross-notebook input was used.

### Continuation test and routing

After the supervisor's separate approval of this changed assessment,
attempt exactly TARGET using the inputs above, classified
REPRODUCTION. Continue only if all four obligations can be supplied
with the unchanged floor and full fixed-a,R domain. Otherwise record
the precise failed hypothesis or tail/integration passage and its
parameter regime. Failure of a sufficient argument is not a
counterexample involving actual zeros.

A successful result would enable later finite-head transport tests
after independent initial-mass and exterior-forcing estimates. The
bridge to actual-Xi all-degree signs, global initialization and coverage
remains missing. No defensible new central creative mechanism was
identified by this review; that missing bridge is the blocker to such
a nomination. The next task is established-route development with a
bounded integral/time-passage test, not another source search under
unchanged hypotheses. PROOF.md and DAG.md need no change because no
mathematical argument or dependency has changed.
