# Quartic target: covariance before final heat smoothing

Approved target: Determine whether L011's complete quartic probe-jet response kappa_0(f_(i,2),r_0) has a finite a^3-scaled limit for both actual L010 probes.
Reuse the unchanged EXPLORE assessment
`drafts/literature/2026-10-16-complete-quartic-probe-jet-scale.md`.

The main gap remains the interacting reflected error <=c_box/2 and
the continuum/infrared construction. C212g leaves the two-flow square
and cubic endpoint at cubic scale. This attempt tests a sharper bound
for the former, within the approved complete target. Removing it would
reduce the outstanding cubic limit to the endpoint, without assuming
endpoint convergence or compensation.

Duplicate/failure check: C212c uses pointwise Gaussian moments followed
by the full output row count. C212g and the current quartic drafts
retain its initial square. None supplies the covariance-operator test
below. L022/ATTEMPTS/010 forbid transferring the original forest
summand; the input here is only the co-closed summand already present
in L212. ATTEMPTS/043's failed effective-residual norm concerns a
different tensor. The unchanged assessment supplies source coverage;
no new literature or originality claim is needed.

Saved before completion: write the full quadratic force as C^T W+V
as in C212c(9). Each color component is a finite sum of products of
two different Gaussian colors. A local product covariance bound may
give ||Cov W(H_s z)||<=C/(s+a^2) and
||Cov V(H_s z)||<=C a^2/(s+a^2)^2, using the global input covariance
norm O(a^-2) and the local diagonal of the other factor. At lag at
least tau/2, ||C E_t C^T||_HS=O(a^2) and ||C E_t||_HS=O(a).
These estimates would make the early circulated flow norm O(log(eN))
instead of O(N). The late interval already has an O(log(eN)) bound.
For any centered color-off-diagonal quadratic, the signed tilt acts
on both whitened tensor slots with norm O(N); this may then give an
O(N log(eN)^2) response. All these claims require verification before
promotion to a canonical result.

Continue if the finite local product bound retains all output rows,
the heat Hilbert--Schmidt bound retains every mode, and the quadratic
tilt estimate includes both slots without a constant-chaos term.
Abandon this estimate if it needs entrywise positivity of S, damping
of an uncirculated gradient, same-color independence, discarded end
rows, or a mesh/time interchange. Keep the cubic endpoint, all other
subcubic errors, both probes and both residual subtractions.

## Completion audit — 2026-10-16

STEP_ID: YM-20261016-260-two-flow-covariance-audit

The pre-existing unregistered C212h proof completes this saved test.
Its full proof and qualifications are canonical in
[C212h](../lemmas/C212h-two-quadratic-flow-response-subcubic.md).
Checked the conditional second moment for every finite local-product
family, including bounded output aggregation; the complete relative
heat traces; the early and late endpoint integrals; and the two-slot
whitened derivative. Distinct input colors keep both quadratic
matrices trace zero, including after the signed tilt. The resulting
response is O(N log(eN)^2), below the required cubic scale.

The complete quartic differs from C212b's endpoint by
O(N^(5/2)log(eN)). No endpoint convergence or compensation follows.
Reuse the unchanged complete-target assessment. Within that target,
the remaining concrete test is the internal-tilt E K sum in C212b(4);
its external-tilt products are already O(1). Essential continuation
inputs are L010 L011 L018 L182 L185 L186 L212 C212b C212g C212h.
Keep all five endpoint triples, correlated prefixes, normal end rows,
upper jumps, constant modes, full heat sums and both subtractions.
No separate diagonal limit, smooth rough tilt or compensation is
assumed. Continue only with a uniform cubic-scale approximation error
and a signed limiting contraction; insufficient absolute bounds are
not evidence of nonconvergence. Independent interacting, continuum
and infrared gaps are unchanged. No new source assessment, numerical
certificate or mathematical script was needed.
