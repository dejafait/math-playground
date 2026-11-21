# 2026-11-04 — full fixed cumulant comparison, step395

Completed the unchanged gate-approved r=3,m=5 comparison in
[L768](../lemmas/L768-fixed-third-fifth-cumulant-full-domain-comparison.md).
The analytic tail now starts at x=32; certified integration and
Taylor continuation cover the remaining compact domain including
x=pi. The complete certificate is
`scripts/cumulant-comparison/compact-certificate-395.json`.
Every cell passes the signed lower bound and relative-error test.

The final certificate replay and scoped documentation checker passed;
the DAG remains acyclic. The installed Python 3.15.0 Decimal exp/ln
docstrings confirm the rounding contract used by the enclosure code.

This is local quantitative progress within Nuttall's known comparison
program, classified REPRODUCTION, with no claim of novelty beyond the
sources checked. L767/L768 and the new certificate remain independently
unaudited. No all-order or RH claim follows. Earlier changes and failed
routes are preserved; no new attempt-stop note is needed for this pass.

Next obtain a separate scope review and independent conceptual audit
of the exact fixed comparison and its analytic remainders. The new
audit nomination is REVIEW_REQUIRED. A creative all-degree mechanism
is not yet justified by this fixed-order result; this essential audit
precedes any such use. The short overview's compact-gap sentence was
replaced by the full fixed comparison; no other argument changed.
