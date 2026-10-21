# Conductor-36 coupled T_5 plan — completed bounded attempt

Approved scope: the exact TARGET in the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-12-conductor36-coupled-small-prime-closing.md`.
Main gap: arbitrary analytic-order-at-least-two rank equality. Intermediate
target: full twelve-class T_5 closure, infinity-normalized unique consistent
solution, then all 144 endpoint plans under the fixed workload/tail bounds.
Downstream use: complete normalized relative integration table only.

Inputs: L038 saved presentation (N=36 instance critical audit pending),
audited L049 identities/tails, L050 curve/conductor, audited L051 coefficients
through 4860 and positive total period, L053 saved classes/transports (its
instance audit pending). Audited L052 clearing integer 24 is downstream only.
ATTEMPTS/025--027 remain preserved. No cross-notebook input.

Plan: reconstruct the domain and all six Hecke images for every class,
including actual infinity. Count the target at five independently. For
P(s_i)=u_i and each image v of s_i assigned to s_j, write
P(v)=u_j+d_v, where d_v=P(gamma_v tau_v)-P(tau_v). Assemble
(a_5 I-A)u=d, retaining multiplicities and signs. Append u_infinity=0;
do not omit the full infinity Hecke row. Save exact row-operation witnesses
and test rank and symbolic consistency before composing endpoint weights.
Stop on failed closure, deficient rank or inconsistency with an exact witness.
If it passes, replay every matrix/inverse, point and uncombined error
occurrence. Require max H<=4860, sum H<=1000000, and every normalized
two-sided conservative tail width<=2^-38 before proposing analytic sums.
No central vanishing, spectral invertibility or table value is assumed.

Completed as BSD-180. The full proof and qualifications are canonical in
[L054](../lemmas/L054-conductor36-coupled-T5-closing-workload-stop.md).
All images close and the infinity-normalized system is uniquely consistent;
complete independent replay has zero failures. The fixed schedule requires
5358>4860 cutoff, though its 149244 terms meet the term limit. At the maximum
permitted cutoff, two retained error contributions alone exceed 2^-38.
This is a finite NEGATIVE for the fixed bound convention, not an analytic
failure. No new sums or table were executed. The existing component sources
are imported and the finite test specializes them; no algorithmic novelty
is claimed. Full Mathlib coverage was not checked. Original evidence and
pending structural/instance critical audits remain preserved.
