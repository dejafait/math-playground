# BSD-176 — bounded full-table implementation attempt

Work is confined to the already approved full conductor-36 table target
in `drafts/literature/2026-10-12-conductor36-full-generator-recovery.md`.
The main gap is arbitrary-curve rank/analytic-order comparison. A complete
table would test full-relative normalization at nonsquarefree level; it
would not supply that comparison, rational directions, Sha finiteness or
a useful coefficient. The curve is CM and cannot meet L027's hypothesis.

The complete N=36 presentation is now built and independently replayed
under L038's structural hypotheses (P empty). Its 72 generators, 144
source relations, saturation rank 59 and free rank 13 pass full checks.
Evidence is in `scripts/conductor36-table/presentation.json` and
`scripts/conductor36-table/presentation_verification.json`. No original
certificate or unfinished work was overwritten.

Before expensive analytic work, `build_plan.py` retains every original
endpoint and all 38 good-prime transports for each distinct finite cusp.
It applies L049's constructive congruence and L051's balanced interior
points, with independently reduced phases planned. The direct plan has
66 finite cusps, 2508 transports and 4465 points; its finite Fourier
schedule has 1796075850 terms and maximum cutoff 7420560. This is a
workload result, not a failed analytic enclosure or a runtime lower bound
for every algorithm. No new coefficient/period/table evidence is asserted.
The plan and independent verifier are saved separately. Complete replay
now passes: every endpoint, all transports, both Bezout identities,
congruences, matrix products, cusp equations, positive Mobius images,
phase-reduced indices and complete deduplicated point domain are checked.
For every point, H passes the full tail bound and H-1 fails it. Changing
t through all congruence solutions changes C by
m*q*(36/gcd(m*q,36)); both adjacent choices have absolute value at least
|C|. This checks the minimal |C| within the retained congruence family,
not optimality over different analytic evaluation strategies.

The full report is `scripts/conductor36-table/plan_verification.json`.
The worst transport sends -1/35 to 314/1295 with matrix
[-192779,-5499,-795060,-22679]. Both interior heights are 1/795060,
requiring H=7420560. The full term count is 1796075850. An exact sieve
calculation gives 503262 good primes and 1798961486482 x-counts for the
unchanged coefficient method. No such point counts or analytic terms
were executed. The selected worst record, all 59 unit pivots and the
workload fields were inspected in full after complete replay.

**Decision and honest outcome.** ADVANCE is for the concrete full
integral input in canonical L038, under its named Stein/Cremona imports.
This is RESEARCH/REPRODUCTION, actual task implementation. The approved
full-table target is incomplete; no discovery beyond the sources or BSD
candidate is asserted. The direct plan's workload changes the execution
choice, with no analytic failure or universal infeasibility claim.
Park that schedule with ATTEMPTS/026 rather than begin its trillion-check
coefficient loop in this bounded step. ATTEMPTS/025's separate rectangle
failure and all prior work remain unchanged.

The full-table success test remains complete zero-failure analytic
containment, positive-period replay, 24-scaled integer isolation including
zero, and all source/saturated relations. None was passed here. The
N=36 structural instance has production replay and awaits separate
critical audit. DAG is unchanged; PROOF records the new concrete domain.

A different execution candidate is a complete cusp-class representative
table with certified Gamma_0(36) transport from every saved endpoint.
This is an unassessed implementation/source lead, not an established
compression. Proposed discriminating limits are cutoff<=4860 (the
existing audited coefficient segment) and total distinct primitive
Fourier terms<=1000000, with full tail budget 2^-38. These are execution
tests, not known theorem bounds. Separate scope/coverage approval is
required before that calculation; its assessment is REVIEW_REQUIRED.
All rank, rational-direction, Sha and useful-coefficient gaps persist.
No cross-notebook input is used.
