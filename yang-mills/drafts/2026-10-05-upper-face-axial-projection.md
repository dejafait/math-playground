# Upper-face axial projection — bounded working record

STEP_ID: YM-20261005-043-upper-face-axial-projection

The unchanged SPECIALIZE assessment in
`drafts/literature/2026-09-26-current-target.md` covers this attempt
inside the complete combined Ward-response target. The main gap is
the full order-g^2 response and its cutoff logarithm. The intermediate
test is whether L030's I_3 and I_6 have a signed cancellation identity
after their exact axial-zero projection. A nonzero value would direct
the compensating-jet calculation; zero would still leave slower powers
and logarithms. Continue only with a justified signed identity or a
controlled nonzero value. Do not infer a sign from norm bounds or reuse
ATTEMPTS/014's failed low-mode/global-norm certificate.

Essential inputs: L008's precise probes and relative modes, L009's
generator, and L028–L030's residual stencil and scaled limit. L019 is
the retained framework for a later compensation calculation, not an
assumed cancellation. The supplied literature comparison is reused;
no general flow or renormalization theorem is being reproved.

Unfinished reasoning: T* T = 8 P, where P is the component-1,
zero-axial-frequency projection. Formally this converts I_i into a
weighted pairing of Q_i and N_2 with only the first mode index in P.
Check all covariance factors, the unprojected second index, and
symmetries before claiming either a zero or sign. Independent gaps
include other plaquette/pairing classes, all compensating jets, finite
matching, the reflected-error threshold c_box/2 on a prescribed
trajectory, continuum fields, full reflection positivity, infrared
control and finite positive mass.

Completed: NEGATIVE / RESEARCH / POTENTIALLY_NEW; actual task proof_attempt.
The exact reduction and counterexample to axial annihilation are in
`lemmas/L031-upper-face-axial-projection-test.md`. Both covariance
denominators and the factor 8 from T*T are retained. The 13 displacement
vanishes only in the doubly compressed operator; it cannot be removed
from the full signed sum. The 24 displacement gives a nonzero compact-
test residual in the affine transverse core. This rules out the proposed
projection-only zero identity (ATTEMPTS/015), not cancellation of I_i.
Neither original functional has been evaluated. Continue with the full
weighted sum and the original transition coefficients; no low-mode/global-
norm certificate, sign from the core test, or compensating identity is
assumed. L019 and ATTEMPTS/011–014 remain unchanged.
