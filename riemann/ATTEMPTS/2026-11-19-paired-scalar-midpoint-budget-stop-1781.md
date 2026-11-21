# Paired scalar norm/midpoint certification stop1781

WHY IT FAILS: The finite convolution-polynomial observable reduces to
four scalar Laplace samples, but the displayed norm-based error
propagation assigns uniform input tolerance2^-112. Under the chosen
real composite-midpoint certificate, its normalization m alone requires
166165941979008264 outer nodes to pay quadrature allowance2^-113,
versus10^7 terms for the entire evaluator. This counts m once and grants
all nested profile, prime and arithmetic work for free. It therefore
stops before allocating quadrature or evaluating any observable.

The full proof, hypotheses and exact limitations are in
[C033t](../lemmas/C033t-finite-paired-scalar-interface-and-midpoint-budget-stop.md),
with the [rational certificate](../scripts/smoothed-law/paired_scalar_preflight_1781.json).
This is a failure of one sufficient-error certificate, not a lower bound
on the actual midpoint error, optimal scalar accuracy, or all algorithms.
The conditional error allocation passes; cost and512-bit implementation
do not pass. C033s remains unaudited and every external qualification
is retained. No RH or positive-separation claim follows.

Park this certificate. A materially different continuation is to prove
a complex-domain majorant and analytic-ellipse quadrature cost for the
same logarithmic-time scalar integrals, retaining the finite polynomial
or paying any replacement. Assessment1780 already covers that conditional
callback case; the majorant and full cost are not supplied by its source.
The bounded test remains total error2^-20, at most10^7 elementary terms
and at most512-bit precision before implementation. Failure of that
distinct test should park this numerical interface, rather than trigger
another midpoint refinement or qualitative-effectivity audit. Preserve
the separate independent-box1571 and expanding-spatial-disk1576 stops.

19 November2026, audit1789: C033s's omission input passed audit1787;
C033t's conditional scalar interface and specified midpoint stop now
pass its canonical conceptual audit, including complex approximate
scalar data and an independent exact certificate. No cost mechanism
was reopened. Source-wide/zero-data correctness and numerical
implementation remain uncertified; the stop above remains in force.
