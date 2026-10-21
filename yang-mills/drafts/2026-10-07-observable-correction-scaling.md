# Observable correction — bounded working record

STEP_ID: YM-20261007-067-observable-correction-scaling

The unchanged SPECIALIZE assessment is
`drafts/literature/2026-09-26-current-target.md`. The main local gap is
the complete power/logarithm of the remaining flowed Ward response.
This attempt tests L049's observable correction E in L051's selected
upper-face identity at a^2 scale. A bound could narrow the compensation
comparison with L047; other cubic pairs, full jets and the interacting
reflection estimate remain independent gaps.

Continue if a complete covariance contraction or a justified scaled
bound exposes a controllable part of E. Abandon any inference from
noise/potential independence to independence of the observables, or
from low-mode defect suppression to a rough internal covariance bound.
L049–L051, L029's exterior rates and L041's separated-column proof
were read; ATTEMPTS/017 and the preceding working/history records were
checked. No duplicate contraction of E was located. Existing unfinished
work is preserved and no additional literature premise is introduced.

Saved before further algebra: under exp(sf+tr), use the full one-color
covariance of (eta_e,u(v),u(v')). Isserlis' theorem and SU(2) epsilon
contraction should reduce the cubic-square expectation to 3/4 times
the sum of its cross-edge 3-by-3 determinants. Base noise/potential
cross covariance vanishes, but both first tilt derivatives need not.
Differentiating the noise covariance and those mixed blocks must retain
the complete observable correction. In particular a second derivative
of the noise covariance is O(a^6) entrywise by the smooth exterior
rates; pairing it with two potential covariances may be O(1), since
||N G3||_HS^2=O(N^6), unlike a crude entrywise counting bound. This
estimate and every numerical factor remain to be checked. No bound
for the other differentiated terms or the full E is yet asserted.

Completed: L052 gives the full finite decomposition into E_BA, E_B,
E_A and E_cross. The mixed second noise derivative has a uniform
O(a^6) cross-edge bound; the complete potential covariance obeys
||N G3||_HS^2=O(N^6). Their contraction proves E_BA=O(1), with no
low-mode replacement. Six exact rational checks pass, including the
two complete corrections and additive-constant invariance. The proof
and qualifications are canonical in
`lemmas/L052-observable-correction-contraction.md`; the complete
certificate is `scripts/combined-ward-response/observable-correction-certificate.json`.
All check records and the empty failures array were inspected.

This is local REPRODUCTION progress only. The bound applies to E_BA,
not the complete E. The attempt did not establish a scaled bound for
E_B, E_A, E_cross or either Phi term. Continue within the same approved
response target with L051's two Phi terms and these three explicit
correction sums retained. Essential inputs: L018, L028–L029, L047,
L049–L052; L011/L019 retain the full-jet interpretation. A justified
joint a^2-scaled bound or limit remains the test, with no assumption
of compensation, positivity, small rough-mode defect or full logarithm.
Restore R for any logarithmic calculation. The independent interacting
reflection, continuum and mass gaps remain unresolved.
