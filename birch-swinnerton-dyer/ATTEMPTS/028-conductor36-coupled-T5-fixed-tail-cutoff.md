# Conductor-36 coupled T_5: fixed-tail cutoff stop

2026-10-12, BSD-180. Canonical exact equations, finite replay and cutoff
obstruction are in
[L054](../lemmas/L054-conductor36-coupled-T5-closing-workload-stop.md).
Full evidence is `scripts/conductor36-table/coupled_plan.json` and
`scripts/conductor36-table/coupled_plan_verification.json`.

## WHY IT FAILS

The twelve-class T_5 system closes with unique infinity-normalized solution
and complete replay. It reduces the term workload to 149244<=1000000, but
the prescribed uniform primitive radius needs cutoff 5358>4860. Even every
cutoff set to 4860 makes two uncombined contributions to {-1/27,0} exceed
the normalized width threshold 2^-38. Thus redistributing cutoffs on these
fixed points cannot satisfy this conservative tail rule. The obstruction
concerns a certified upper bound, not actual error, source solvability or
table existence. Stop this point-and-tail schedule; preserve the coupled
solution and ATTEMPTS/025--027. A materially different error mechanism is
certified use of Wuthrich's full exponential tail rather than its dyadic
majorant. That changed numerical convention needs separate source review
before any dependent calculation; no improved feasibility is asserted.
