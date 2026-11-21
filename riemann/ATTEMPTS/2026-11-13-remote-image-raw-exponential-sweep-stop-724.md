# Uncompressed derivative-measure sweep: prescription stop724

Canonical proof: [C998u Section3](../lemmas/C998u-fixed-remote-image-derivative-measure-energy.md).
Exact finite evidence: `scripts/separation-seven/remote-image-measure-preflight-724.json`.

WHY IT FAILS: The specified geometric-prefix rule uses the complete BV
tail majorant and reserves1e-7 of the1e-6 total error budget. Its least
sufficient cutoff is43,980,465,111,040,000,001 exponentials, already
exceeding1e8 operations at one accumulation per term with all sweeps,
density preparation and other costs assigned favorable zero. Giving
the tail the entire error allowance still selects more than4.39e18
terms. This is a failure of one sufficient bound/prescription, not
an actual-error lower bound or an obstruction to compression. The
continuous measure identity remains useful partial progress, pending
separate audit. Density/mixed-term quadrature, finite arithmetic,
precision and storage are unpaid; no scalar or Gram was evaluated.
All11 finite checks pass. Preserve earlier implementation stops and
all signed/global gaps.
