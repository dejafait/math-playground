# Fixed-face, equality-eliminated joint conic proposal — inconclusive

WHY IT FAILS: The one approved reduced run reaches 10000 iterations with
cone distance 6.244974010438509 against required exact distance zero.
Its one exact reconstruction satisfies all 85 domain rows and all 28
selected equalities but fails 11 moment signs and 28 original modes;
75 of 693 original block principal minors are negative. The exact
48-to-21 variable lift and 140-to-112 face reduction were checked before
iteration, including both lift directions and every mixed/removed
equation. The [working record](../drafts/2026-10-18-reduced-zero-plane-joint-working.md)
documents the method, full residuals and independent 830-check verification.
Complete evidence is `scripts/finite-support/reduced-zero-plane-joint-results.json`
and `scripts/finite-support/reduced-zero-plane-joint-verification.json`.
This is a failed candidate, not a proof of infeasibility; full-domain
joint feasibility remains unresolved. Stop this numerical prescription
without another solve, rounding rule, point scan or weight search.
L084/L085 and ATTEMPTS/052–053,060–067 remain intact. A separate exact
polyhedral sign/equality target is proposed for source review, without
testing it here. No RS boundary improvement follows.
