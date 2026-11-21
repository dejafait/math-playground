# Width Newton application audit1827

Saved before exact verification. Approved target is the unchanged SPECIALIZE
assessment `drafts/literature/2026-11-19-width-newton-audit-review-1825.md`.
Audit only C033z extension1825's uniform error<=2^-60 and complete<=100
rational-operation contract, including1802 perturbation and panel clamps.
Main gap remains L030-L032/C032a actual-Xi all-degree positivity; possible
downstream use is arithmetic slack for separately assessed rounding and
C033w interpolation. Signed-height/cancellation/realization remain open.

Written review so far: normalization uses at most15 divisions by4 and
matching divisions by2; a in(1/4,1], including both input endpoints.
The cited Brent-Zimmermann v0.5.9 Lemma3.14 applies at each positive
iterate. The first-step relative error5/16, subsequent coefficient24/11,
and seven subsequent squarings give the claimed exponent128. The ledger
sums to94 without free arithmetic counters or hidden constant formation.
No flaw found so far; this is not yet a completed audit.

Remaining audit work: independently reconstruct all eight rational error
envelopes, recompute1802(14)-(16) bounds, verify panel17's endpoint and
clamp nonexpansiveness, and replay complete relevant1825 certificate
values without trusting their Boolean flags. No1823 value is an input.
Retain the source-wide law/divisor qualifications and unchecked Mathlib
coverage. Algebraic cost supplies no bit-cost, denominator or runtime bound.
Continue only if both thresholds and the full interface pass; otherwise
identify the failed claim and preserve the original evidence.

## Completion

The audit passes without correction. Full proof and qualifications are
canonical in C033z, application audit1827. The independent script and
certificate have stem `scripts/smoothed-law/width_newton_audit_1827`;
all48 checks pass, with94 operations and total error<2^-64. The next
scope proposes a single rounding of the normalized width and requires
separate source coverage; no changed algorithm was derived in this audit.
