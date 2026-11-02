# Specified rational periodic storage: whole-family obstruction

The approved test adds only c*x_0^3*y_0/(x_0^2+y_0^2), with its C1
zero extension, to arbitrary four-state homogeneous quadratic storage.
It retains both global branches on R^6, the full trace and the actual
closed-I cone dual. The requested certificate cost is below 1/288.

WHY IT FAILS: [L590](../lemmas/L590-rational-periodic-storage-finite-law-obstruction.md)
constructs a bounded finite law with second matrix K that annihilates
every allowed storage derivative and has clipped mean 625/48384.
Every global certificate therefore has at least this cost, even before
the cone-dual constraint, exceeding 1/288 by 457/48384. The original
law's nonzero rational-derivative expectation was only an inconclusive
first test; changing the test law supplies the uniform obstruction.
The separate conceptual audit in L590 Section 6 passes (31 October
2026), including its origin, full covariance and global-domain steps.
This stops the specified W+cR family,
not general periodic clipping, arbitrary nonlinear storage or Xi
signs. Any further construction needs a materially different,
separately assessed target; repeating coefficient optimization cannot
evade the displayed witness.
