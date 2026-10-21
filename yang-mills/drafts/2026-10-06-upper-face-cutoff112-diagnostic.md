# Upper-face cutoff-112 diagnostic — working record

STEP_ID: YM-20261006-048-upper-face-cutoff112-diagnostic

Reuse `drafts/literature/2026-09-26-current-target.md` (SPECIALIZE)
for the unchanged exact combined-response target. Main gap: an interacting
cutoff removal and ultraviolet-uniform reflected comparison. This bounded
calculation tests L033's tensor/Laplace retained sum at M=112, refining
coefficient and time quadrature at that same cutoff. Essential inputs:
L008 and L030–L033, `check_continuum_tensor.py`, and its coefficient
integrals from `check_continuum_pure_sectors.py`. The prior small-cutoff
validation and ATTEMPTS/011–015 are preserved; the failed global-norm
shortcut is not reopened. Known flow/matching inputs remain imported in
the ready assessment; no general source theorem is reproved.

Downstream use: determine whether numerical evaluation at L033's useful
tail cutoff is feasible before certifying the signed upper-face power
term and examining compensation in the full response. Continuation test:
the inverse-weight discrepancies must be <1e-11 across the finite
spectrum; compare all pure-sector/axial parts on refined passing rules,
and coefficient degrees at fixed cutoff. Use diagnostic tolerances
1e-8+1e-9 times the absolute refined part for retained-sum agreement.
Failure stops use of that rule and is recorded, not suppressed. Passing
these tests does not enclose quadrature or rounding. A sign requires a
certified retained value, all numerical error bounds, and L033's tail
at the SAME cutoff, with total error smaller than its absolute value.

Unfinished reasoning saved before the calculation: first test the
inherited time rules on every integer squared-frequency sum from 3 to
4*112^2. Refine the rule near its lower endpoint if necessary, before
the more expensive tensor contraction. Compare coefficient degrees 96
and 144 and two passing time rules. The seven-index array remains absent.
Save all raw values, thresholds, rule parameters and failures to local
certificates. No diagnostic refinement establishes an analytic bound.

Unresolved assumptions: coefficient/time quadrature and integration-tail
enclosures, rounding, I_3/I_6 signs, all other plaquettes and pairing
classes, action/measure/insertion/flow jets, L019 compensation, full
Gamma and its logarithm, finite matching, reflected error <= c_box/2
along a prescribed trajectory, continuum field content, full reflection
positivity, infrared control and finite positive mass. None is a premise.
Mathlib coverage of this computation is not checked; it is not formalized.

The inherited degree-8 and degree-12 time rules fail at M=112, with
worst relative inverse-weight discrepancies 0.8972 and 0.3917, respectively.
These rules are not used for a retained sum. Uniform refinement needs
1024 nodes for a passing degree-32 rule at panel width 0.25. Subdividing
the first log-time panel dyadically into eight additional panels gives
passing degrees 8,12,16 with 192,288,384 nodes. All failed rules and
their complete diagnostics remain in
`scripts/combined-ward-response/continuum-tensor112-rule-diagnostic.json`.
The program now accepts `--endpoint-levels`, records all log-time edges,
and skips retained-sum evaluation after a failed inverse-weight test.
Next evaluate at coefficient degrees 96 and 144 using this passing rule.
## Completed bounded calculation

Outcome: EXPLORATION / RESEARCH / REPRODUCTION; actual task calculation.
This applies L033's existing identity; no new lemma, theorem, certified
sign or full response coefficient is established. The smaller-cutoff
checks share the weak expansion and coefficient integrals, so an error
common to those inputs remains possible. No claim of mathematical
progress beyond the sources checked is made.

At M=112 the relative one-form spectrum lies in
[3(pi/8)^2, 4*112^2(pi/8)^2] = [0.4626377063,7737.7698505].
Both inverse weights were tested at every integer squared-frequency
sum from 3 through 50176, a superset of the finite spectrum. The
original uniform-log-time rules have the following maximum relative
discrepancies (s weight, r weight), against the required <1e-11:

| Log panel width | Degree | Nodes | Actual discrepancies | Result |
| --- | --- | --- | --- | --- |
| 0.5 | 8 | 128 | (0.5086,0.8972) | fail |
| 0.5 | 12 | 192 | (0.3917,0.3795) | fail |
| 0.5 | 24 | 384 | (0.004185,0.0004973) | fail |
| 0.25 | 24 | 768 | (8.869e-7,5.220e-8) | fail |
| 0.25 | 32 | 1024 | (1.497e-12,3.197e-14) | pass |

The efficient rule replaces only the first of the original sixteen
log-time panels by a dyadic subdivision. If h is its width, its new
edges are 0,h/256,h/128,...,h/2,h; all later panels are retained.
There are 24 panels, with the original upper endpoint
tau+80/[3(pi/8)^2]=172.9839867495898. Degrees 8,12,16 give
192,288,384 nodes and discrepancies respectively
(6.035e-12,1.529e-12), (4.441e-15,1.066e-14),
and (3.775e-15,3.220e-15). These passing diagnostics do not certify
rounding, endpoint integration errors or contraction errors.

At coefficient degree 144 and time degree 16 the pure-sector/axial
parts of the retained functional are:

| Probe | 13, axial zero | 13, axial positive | 24, axial zero | 24, axial positive | Total |
| --- | --- | --- | --- | --- | --- |
| 3 | 0 | 229.581533601481 | 152.636186785531 | 70.855936657275 | 453.073657044287 |
| 6 | 0 | 1998.389578906053 | 932.170248049077 | 422.033328064252 | 3352.593155019382 |

Every second-index component and its permitted zero/positive frequencies
are retained. The exact 13-axial-zero exclusion comes from L032; it is
not inferred from these numerical zeros. The mixed potentials were
already canceled mathematically in L032. L033's tensor identity uses
all finite weak monomials, coefficient transitions, both inverse weights
and both heat factors; no seven-index allocation is made at M=112.

For all eight parts, agreement is tested against
1e-8+1e-9*abs(refined part). Raising time degree 8 to 12 at coefficient
degree 96 changes any part by at most 9.095e-13; raising 12 to 16 at
coefficient degree 144 changes any part by at most 4.548e-13.
Raising coefficient degree 96 to 144 at fixed time degree 12 changes
any part by at most 5.069e-10, and changes the two totals by
(1.102e-10,8.582e-10). Its largest fraction of the componentwise
tolerance is 0.0002813. All refinement checks pass. These observed
differences are not bounds on true errors; no extrapolation is used.

Reproduction commands, relative to this notebook:

```sh
OPENBLAS_NUM_THREADS=1 python3 scripts/combined-ward-response/check_continuum_tensor.py --cutoffs 112 --coefficient-degree 96 --time-degrees 8 12 --endpoint-levels 8 --output scripts/combined-ward-response/continuum-tensor112-degree96-certificate.json
OPENBLAS_NUM_THREADS=1 python3 scripts/combined-ward-response/check_continuum_tensor.py --cutoffs 112 --coefficient-degree 144 --time-degrees 12 16 --endpoint-levels 8 --output scripts/combined-ward-response/continuum-tensor112-degree144-certificate.json
OPENBLAS_NUM_THREADS=1 python3 scripts/combined-ward-response/check_tensor112_refinement.py
```

The last program saves the complete rule diagnostics and failures in
`scripts/combined-ward-response/continuum-tensor112-rule-diagnostic.json`
and all parts, differences and actual/required thresholds in
`scripts/combined-ward-response/continuum-tensor112-refinement-certificate.json`.
The two retained-sum certificates save complete numerical values and
parameters. Their output logs are the corresponding degree96/degree144
`-output.txt` files. The full relevant `/checks`, `/failures`, retained
`/rows/1/pure_sector_axial_parts`, inverse diagnostics and final time
edges were inspected using the supervisor JSON inspector with `--full`.

The numerical feasibility test passes after the inherited-rule failure
is repaired. The full spectral tails in L033 remain <=1.374e-11 and
<=5.496e-11 at this SAME cutoff, but neither those rigorous tail bounds
nor numerical refinement supplies the missing retained-value enclosure.
Thus I_3/I_6 have no certified signs here. In particular multiplying
these numerical totals by -48 is not a proved upper-face asymptotic
coefficient. The other contributions and L019 compensation are still
unresolved, so no full power term or logarithm has been determined.

Continue with one bounded attempt to enclose the retained values,
including coefficient integrals, time integration/tails and arithmetic
error, using the exact inputs above. A total rigorous error below the
retained absolute value minus L033's tail would certify a sign only for
this selected class. If an explicit enclosure exceeds that threshold,
record the failed bound and reassess the certification mechanism.
Exploration usage is 2 of 3 after L033; exhausted prior branches retain
their stop evidence. The exact approved target/assessment is unchanged;
no new ready assessment is written or approved during this turn.
