# Conductor-36 ordinary cusp-class compression: fixed-plan workload stop

2026-10-12, BSD-178. The canonical finite proof and source qualifications
are in [L053](../lemmas/L053-conductor36-cusp-compression-workload-stop.md).
The complete plan and replay are
`scripts/conductor36-table/compressed_plan.json` and
`scripts/conductor36-table/compressed_plan_verification.json`.

## WHY IT FAILS

The cumulative representative/ell=37 ordinary closing plan covers all
144 endpoints and independently passes every matrix, point and full
weighted two-sided tail check, but needs cutoff 48600>4860 and
7047552>1000000 primitive terms. Compression improves on the preserved
direct workload without reaching the bounded execution limits. Even
setting all cutoffs to 4860 makes the prescribed conservative tail bound
for {2/9,1/4} exceed 5; redistributing precision on these same points
cannot repair that bound. This is neither a lower bound on actual error
nor a universal obstruction to other integration methods. No new sums
were run. Preserve ATTEMPTS/025--026 and this complete plan. A materially
different candidate is coupled closing at the small good prime 5 on the
twelve cusp classes, instead of individually closing each representative
at 37. Its source coverage, infinity treatment, solvability, full error
weights and feasibility are unestablished: separate literature review
must precede any construction or mathematical approval.
