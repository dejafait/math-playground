# Compressed direction/incidence relation — fixed cost stop

2026-10-16, step 249. This stop concerns the new compressed relation
implementation, not scalar-fixed direction algebras or incidence in general.

## WHY IT FAILS

The invariant-first stage succeeded: [L070](../lemmas/L070-conductor389-seven-direction-algebra.md)
gives the full degree-eight direction algebra, mixed inverse and both
coordinate transports, with independent finite replay. The following whole
compressed-relation stage produced only 26 of 336 required columns when its
180-second alarm fired. Its final recorded time is 180.00775816699024 seconds
(including interruption/report overhead); the independent watchdog returned
after 180.06937699997798 seconds without needing to kill the child. Its report
counts 6014113 bytes against 134217728; the completed watchdog counts 6014535
bytes including final reports. Neither limit was increased and no stage was
retrospectively split. Complete cost/partial-column evidence remains in
`scripts/seven-torsion/compressed-249/`. The producer's compressed-domain and
new translation identities and all 26 relation columns lack independent
replay; they certify no quotient, full transport, norm or Selmer bound.
Park this presentation together with the separate uncompressed stop in
ATTEMPTS/035. A later reopening needs a materially different mechanism and
discriminating test. A fresh critical audit of completed partial L070 is
independently testable; it must not resume the capped relation.
