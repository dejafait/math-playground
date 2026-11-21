# Exact totient profile does not saturate the cross pairing

9 November 2026, step17. The full proof, scalar imports, hypotheses
and qualifications are in [L931](../lemmas/L931-exact-totient-profile-cross-pairing.md),
pending separate conceptual audit. This tests exactly the vector
v_d=1/sqrt(phi(d)), N=floor(T^(1/5)), in L930's exact two full
metrics, weight and Hardy phase.

## WHY IT FAILS

The normalized scalar pairing tends uniformly in T<=X<=2T to
sinc(1/5)sinc(4/5)<9/10, with O(1/log T) error. Thus this profile
cannot supply a sequence approaching one and obstructing a fixed joint
contraction gap. The proof retains cancellation between both endpoint
terms; it does not reuse either stopped triangle-majorant estimate.
Park this one saturation witness, without extending the test into a
profile grid or optimization. This is not an operator upper bound or
a joint contraction proof: other coefficient pairs, sufficient margins
after the arithmetic charge, signed realization and Xi transfer remain
open. Preserve the separate L929/L930 certificate-only stops. Audit
the new asymptotic before relying on its scalar exclusion downstream.

Subsequent review, 9 November 2026, step19: the separate conceptual
audit in L931 passes without correction, including all uniform errors
and both full metrics. The pending-review qualification above is
superseded; the original attempt and its scope remain preserved.
The prescribed witness is now parked on audited evidence. No upper
bound for other vectors, operator contraction or signed Xi transfer
follows from that review.
