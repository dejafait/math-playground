# Conductor-36 direct endpoint evaluation: bounded execution stop

2026-10-12, BSD-176. The complete structural input is in
[L038](../lemmas/L038-finite-general-relative-lattice-and-operators.md).
The full direct plan and independent replay are
`scripts/conductor36-table/plan.json` and `plan_verification.json`
in that directory; see
[the attempt notes](../drafts/2026-10-12-conductor36-full-generator-attempt.md).

## WHY IT FAILS

This schedule fails suitability for one bounded execution step, not
analytic containment or table existence. Even with minimal |C| in each
retained congruence family and balanced interior points, it requires
1796075850 Fourier terms, cutoff 7420560 and 1798961486482 x-counts for
the unchanged coefficient method. These workloads are independently
reconstructed, not runtime lower bounds for other algorithms. No new
analytic sums were executed and no enclosure failure is claimed. Preserve
all endpoints and this plan; do not use relation agreement instead of
their analytic containment. A different candidate is complete cusp-class
compression with certified transport witnesses and workload limits.
Its scope needs separate review; no compression is assumed here.
This stops the direct schedule only and leaves L049, alternative
transports and the full-table route open. ATTEMPTS/025's different
rectangle failure remains preserved.
