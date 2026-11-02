# Phase-sensitive 256-index endpoint calculation

Started under the pre-existing SPECIALIZE covered target in
`drafts/literature/2026-11-01-phase-sensitive-entry-block-review.md`.
Main gap: actual-Xi all-degree signs at unbounded heights. Test only the
literal resultant increment n=691004 to N=691260 at t=.16836,
Y=4*pi*(N^2-t/16). A strict full-charge budget could supply one
qualified endpoint input; uniform transport remains independent.

Inputs read: L494, L495, L496, L499, C499a, C499b, the existing
first-entry producer, and the three September 13 failures named in
the assessment. All existing unfinished work is preserved. No new
source search is needed for this unchanged finite specialization.

Planned exact implementation: with E=product(1-A_p),
J=sum log(p)*A_p/(1-A_p), DeltaS=sum_(n<j<=N) b_j*j^(-nu),
DeltaL=sum_(n<j<=N) b_j*j^(-nu)*log j, finite distributivity gives
DeltaLhat=E*(DeltaL-J*DeltaS). Thus, writing v=exp(i*Theta),
DeltaZ=|E|*v*DeltaS and DeltaW=|E|*v*(DeltaL-J*DeltaS).
Evaluate DeltaG=DeltaZ-DeltaW/ell+conj(DeltaW)/ell before modulus.
This retains every squarefree output. The same actual ell and phase
are used in both finite models. These identities are work in progress
until the canonical proof is written.

Use rational outward elementary intervals, including rigorous argument
reduction, since python-flint is not installed. Preserve full L494
epsilon_1. Independently enlarge primitive/support envelopes for both
charges. Continue iff B_G+U_s+U_r<r0; adequate-precision failure parks
this endpoint comparison, not RH. One precision refinement allowed
only for interval width. No adjacent-block search is authorized.

Completed: canonical proof and qualifications are in C499c; the exact
certificate is `scripts/heat/phase-sensitive-256-block-certificate.json`.
400 producer checks pass, no failures. B_G<5.091337212138e-8;
full cost<.000020881403151711<r0, margin>.000401612412718832.
The moment-based complete absolute-channel envelope exceeds .0007013631,
with envelope/modulus ratio>13775. It is conservative, not an absolute-norm
lower bound. No precision refinement was needed. The product-rule
recurrence agrees with the factored evaluation. Exact selected ell,
DeltaG and combined-cost endpoints were inspected in full. This is
an unaudited finite reproduction; source-manuscript and uniform-transport
gaps remain. No failed attempt or stop artifact is appropriate.
