# Local-count replacement of the transport count floor

TARGET: Assess whether replacing C488a's eta(x) by 1/[1000 log(2+sqrt(x^2+R^2))] preserves its nearby real-partner absorption (7) for every real a, R>=200 and 0<=t<=1/5, using C488c and counting multiplicity.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step2116 searched weighted nonreal counts, mixed-pair absorption and the logarithmic floor; inspected paper186 AppendixB and Polymath3.1/1.5(iv), reused assessment2111 and checked C488a-c, L058, L133, the2113 bridge stop and September20 moving-supremum audit. No exact changed-floor theorem was located; no novelty inference.
SOURCE_EVIDENCE: bramble_trace, An unsigned strip bound for the de Bruijn--Newman constant, rStation paper186/v1,20November2026, Section1 and AppendixB/(B.1)-(B.4), complete nearby mixed-pair and own-conjugate cases, https://rstation.ai/problems/riemann_hypothesis/papers/186 ; D.H.J.Polymath1904.12438v2,4August2019, Proposition3.1(i)-(ii)/(28)-(33) and relevant proof, Theorems1.5(iv)/3.2 and Section9/(105), https://arxiv.org/html/1904.12438v2 . Numerical count coverage is reused from assessment2111 and audited C488b/C488c.
COMPARISON: C488a(7) already audits the source absorption mechanism for the older eta and restricted center/scale. C488c supplies the off-center numerical count. The proposed weight and widened domain require a quantitative specialization, not a new transport mechanism or a direct import.
GAP: Prove or fail the exact half-loss bound for the proposed p on the full closed domain; pay its changed derivative and the central region using established counts. No changed-weight inequality is established in this literature turn.
REASON: Essential source comparison is complete for one bounded calculation using the known mixed-pair mechanism. A citation does not cover the modified weight/domain; apply the existing count results with their actual hypotheses.
SCOPE: Exact TARGET only: differentiate the proposed p and test the existing nearby mixed-pair absorption using C488a(4),(7), C488b/C488c and L058. Retain closed windows, all multiplicities, arbitrary real a, R>=200 and 0<=t<=1/5. Full transport, higher derivatives, tails, collisions and all-height overlap are outside this approval.
LITERATURE_REASON: The start assessment was REVIEW_REQUIRED for a changed count floor and widened center/scale; this review supplies the missing theorem-level comparison without repeating the ready local-count audit.

## Original nomination2115 (historical; current decision above)

Main gap: actual-Xi all-degree mixed positivity in L030-L032/C032a.
The proposed intermediate target changes one cost in the established
transport mechanism. A larger count floor might strengthen detection
of zeros with very small nonreal ordinate. This is a routine quantitative
specialization to investigate, not a proposed new central sign mechanism.
The full transport differential inequality, its tails, collisions,
summability, initial mass, all-height overlap and mixed signs remain
independent obligations. No improvement in any of them is claimed.

Keep C488a's w(x)=exp(-sqrt(1+((x-a)/R)^2)), and define the proposed
p(x)=w(x)/[1000 log(2+sqrt(x^2+R^2))]. The precise test is whether,
for each nonreal zero copy z_j=x_j+i y_j, the sum over real zero copies
with |x_k-x_j|<=R of

    2(x_j-x_k)p'(x_j)/((x_j-x_k)^2+y_j^2)

is at most w(x_j)/(2|y_j|). This is a proposed inequality, not a
derived result. It retains the closed nearby cutoff and arbitrary real
a, and asks for no separation or positive minimum |y_j|. The analytic
expression is meaningful at a repeated copy; any later use as a velocity
formula must retain C488a's regular-time and collision qualifications.

Essential inputs for comparison are C488a(7), C488b/C488c, L058 and
the Polymath source cited there. C488c covers radius R only when
|x_j|>=2R; the central region must be paid separately, for example
from the existing global count if sufficient. No subtraction of two
global upper counts is permitted. L133 supplies an exterior inverse-
square estimate, not this first-derivative mixed-pair absorption. Its
larger-window maximum and time-uniformity gaps remain untouched.

The2113 global-only bridge failure is preserved. It does not refute
this new target, whose proposed new input is the now-audited local
count. Likewise the earlier global moving-supremum obstruction is not
removed by changing this floor. Search exact weight/absorption results
and relevant local failures before approving any calculation. Reuse
the already inspected local-count source coverage; only the changed
transport application needs comparison. Full matching Mathlib coverage
is unchecked, and no absence or novelty claim is made.

Continue only if source coverage supports a bounded proof or explicit
failed inequality for the stated half-loss threshold. A failure must
identify the parameter regime or inequality that fails; it would stop
this proposed floor, not RH or all uses of local counts. A known exact
result should be imported with its hypotheses. This file remains
REVIEW_REQUIRED for the next turn, with no new mathematical derivation.


## Completed source comparison2116 — 21 November2026

### Primary source and applicability

bramble_trace, *An unsigned strip bound for the de Bruijn--Newman
constant*, [rStation paper186, v1, 20November2026,
Section1 and AppendixB](https://rstation.ai/problems/riemann_hypothesis/papers/186).
Read (B.1)-(B.4) and the complete nearby mixed-pair/own-conjugate
cases. The stated domain is |a|<=X, R>=200, R/V<=1/1000,
with R=3000000 in the final comparison. The absorption uses
|p'(x_j)|/|y_j| per real partner and the global count. Those claims
are already audited in C488a. Its derivative constants and finite-head
conclusion do not state the new weight or wider parameters.

D.H.J.Polymath, *Effective approximation of heat flow evolution of
the Riemann xi function, and a new upper bound for the de
Bruijn--Newman constant*, Research in the Mathematical Sciences
6 (2019), article31, [arXiv1904.12438v2, 4August2019,
Proposition3.1(i)-(ii), (28)-(33); Theorems1.5(iv),3.2;
Section9/(105)](https://arxiv.org/html/1904.12438v2).
Inspected these statements and relevant proof cases. The selected
simple zero's velocity uses opposite-paired summation; other zeros
may be complex or repeated. Hermite splitting includes cluster
exhaustion by Rouche. Theorem3.2 cites de Bruijn1950 Theorem13.
Theorem1.5(iv) has an unspecified absolute count constant,
0<t<=1/2, without an exp(C/t) restriction. Its off-axis proof
states no changed weighted absorption. No numerical constant is
assigned to its O notation.

Reuse assessment2111's inspected local-count coverage and the completed
C488b/C488c audit. C488c(2) counts every complex copy in a closed
window, includes t=0, and requires |x|>=2r>=400. C488a(4) counts
all copies with |Re z|<=r for every r>=0 over the whole time band.
These are the two available spatial inputs; their sufficiency for the
new floor remains to be tested. L058 supplies the actual family and
normalization qualifications. No fresh theorem or numerical estimate
was derived in this comparison.

### Duplicates, failures and search limits

C488a(7) is the existing absorption proof, so its changed-weight use
must be identified as specialization. L133's full proof controls an
exterior inverse-square sum under unit-window counts; it is not this
nearby first-derivative bound. The2113
[global-only bridge failure](../../ATTEMPTS/2026-11-21-local-count-global-bridge-unpaid-2113.md)
concerns the old count onset, subsequently paid by C488c, and supplies
no counterexample to the modified floor. The September20
[heat-route audit](../../ATTEMPTS/2026-09-20-heat-fourier-relevance-audit.md)
retains the independent whole-plane moving-supremum obstruction.
These historical stops are not prohibitions on this local test.

Queries included `"heat flow" "nonreal" zeros "weight" de Bruijn
Newman`, `"zeros" "nearby" "count" "absorption" "Newman"`,
`"nonreal" "weighted count" zeros heat`, `"1000" "log"
"absorption" "H_t"`, `"de Bruijn" "weighted" "nonreal"
"logarithmic"`, and `"de Bruijn" "real" "absorption" "zeros"`.
Exact-floor and partner searches returned much irrelevant material;
only inspected primary statements support this comparison. Caceres's
cluster-absorption and a backward-parabolic-barrier paper appeared as
search leads. Their theorem/proof cases were not inspected for this
target and are not premises or assessed obstructions. Assessment2111's
narrower Caceres count comparison remains available with its recorded
restrictions. This bounded search establishes neither originality nor
an absence theorem. No essential source blocker remains for this test.

### Permitted next test and limits

Retain the exact TARGET, including its word “Assess”; the next
mathematical step must prove or explicitly fail the inequality written
in the nomination. That finite mixed-pair expression is meaningful at
a repeated selected nonreal copy. Calling it a velocity contribution
additionally requires the selected-zero regularity in Proposition3.1;
no new collision assertion is approved.

Use the off-center count only where its radius hypothesis holds, and
the global count for the remaining central region. Track the modified
p' uniformly in a and R rather than copy (B.4). Keep the closed
cutoff, real partners with multiplicity and arbitrarily small nonzero
|y_j|. Test against exactly w(x_j)/(2|y_j|). A failed sufficient
majorant must be labeled as such, not as a counterexample to the
actual-zero inequality. Sampling cannot certify the domain.

Continue only with a full-domain proof or a specific failed inequality
that changes the route decision. A pass pays this single nearby cost;
it does not establish a changed-weight total differential inequality,
initial mass estimate, all-height reality, overlap or mixed positivity.
The main gap is still L030-L032/C032a. No justified new central
mechanism follows from these sources, so routine specialization is
the appropriate continuation; no creative label is assigned to fill
the scheduling preference. Full matching Mathlib coverage is unchecked.
No lemma, mathematical script, DAG or proof assembly was changed.
This newly ready assessment is available for separate supervisor
approval before the mathematical attempt; it does not approve work
already performed in this turn.
