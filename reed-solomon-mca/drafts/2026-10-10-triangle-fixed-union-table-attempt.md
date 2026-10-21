# Triangle twelve-count attempt: fixed-union scalar tables

STEP_ID: 2026-10-10-mca-140-triangle-fixed-union-table-test

The unchanged approved target and EXPLORE coverage are in
`literature/2026-10-10-triangle-twelve-recovery-bound.md`. The main gap
is arbitrary sixteen-count equality exclusion. This bounded attempt
tests audited L059's seven-scalar necessary condition; its downstream
use is triangle equality exclusion. Other patterns, arbitrary extraction
and challenge definitions remain independent gaps.

Before calculation: fix shared labels P=the first three labels of sorted H
and U=the first nine labels. Enumerate all 90 ordered partitions of U\P
into unordered Y,Z,W pairs: 15 choices for Y, then 6 for Z. Within-pair
orders leave every L057 equation unchanged. No subgroup scaling,
permutation of P, or change of U is assumed. Thus this is exact restricted
coverage, not coverage of all nine-label assignments.

Construct all 715 disjoint-P support rows per partition with complete
projected data and restored beta equations. Both-zero rows test every
mu in F_97\{0,-1}; retain zero fourth weights; discard only nongated
(p,q,r). Deduplicate mu at each weight point. Independently recover the
first four moments and check all eight moments for every generated gated
table row, without using projected tests as the residual check. Save full
certificates rather than console dumps.

Continuation test: any seven-scalar weight point receives the full M test
over all 1817 nonbase supports. Only thirteen actual additional finite
recoveries would refute twelve. If this restricted family has no seven
survivor, record its exact maximum and coverage and leave arbitrary P,U
open. No enumeration of the 95^3 weights is needed: L059 proves every
nonempty D fiber appears in the table. Preserve all prior stop evidence;
this tests simultaneous equations, rather than replaying degree capacities
or support-only recentering. Reuse the supplied literature comparison;
no new sources, new scope approval, or standard recurrence reproof.

Unfinished reasoning saved before implementation. No count is assumed.

## Completed bounded test

Canonical restricted result and full reconstruction argument:
[L060](../lemmas/L060-fixed-union-triangle-scalar-table.md). All 90
ordered pair partitions and 64,350 disjoint-P support rows were generated.
Independent seven-column moment inversion replayed all 84,144 scalar
tests, including rejected weight gates. Gated rows numbered 55,610,
including 9,498 both-zero rows and 2,160 rows with zero fourth weights;
all eight-moment checks passed, with full empty failure arrays inspected.
The maximum D is 2 (66 cases have maximum 1, 24 have maximum 2),
against required 7, and there are no seven-scalar survivors.

The calculation gives the restricted |R|<=12 consequence through audited
L059, with extension-field weights and original charts retained. It
does not supply an arbitrary-label maximum or global interval improvement.
L060 awaits separate critical audit. Full evidence is in
`scripts/triangle-recovery/fixed-union-table.json` and
`scripts/triangle-recovery/fixed-union-table-verification.json`.
No source refresh or new target approval was performed during research.

ADVANCE / RESEARCH / POTENTIALLY_NEW describes this restricted local
computational input, not a new general theorem or certified originality.
Continue the same ready triangle-count target by changing the singleton
pool while keeping P fixed, rather than repeating this checked table.
Suggested next pool is {18,22,27,64,70,75}, again all 90 ordered pair
partitions and all both-zero scalar tests. No symmetry or uniformity
across pools is licensed; full M testing of any seven-scalar survivor
and original finite gates remain essential.
