# Step176 — bounded derivative-profile test, working checkpoint

Completed: canonical proof and exact check are now in
`../lemmas/L969-h-derivative-boundary-profile-diagonal-obstruction.md`
and `../scripts/li-theta/h-derivative-profile-check-176.json`.
The candidate discriminator below was verified in the construction
step. This earlier checkpoint is preserved; independent audit remains
pending. Current status and routing are solely in PROGRESS.md.

The prior EXPLORE assessment is
`literature/2026-11-10-h-derivative-boundary-profile-review-174.md`.
Only its fixed n=2,3 replacement is being tested. No new profile is
being tuned and no source gate has been changed.

Write gamma=1/[2(c_0+c_1)] and Z=gamma(H_0(h)+H_1(h)). The complete
L967 tensor uses B_0=Z, B_r=2rH_(r-1)(b), C_0=Z+2Delta H_0(h),
C_1=2H_0(h)+2Delta H_1(h). Each origin, including the h-origin,
must receive Z under the A du measure. The moment equalities and
absolute integrability still need to be written out canonically.

Candidate discriminator: take all coordinates equal to t tending to
infinity. Put E=t exp(qt), q=sqrt(h). Then B_0/E and C_0/E tend to
gamma/(4q), C_1/E tends to Delta/(2q), and every B_r/E, r>=1
used here, tends to zero. Every b-Bell term has at least one such
positive-order factor. Therefore the prospective complete diagonal
limit is -d_1 Delta/(2q) [gamma/(4q)]^n, strictly negative. Check
all complete n=2,3 tensors and the replacement identity before
recording this as a result. No numerical c_r bound appears necessary:
only 0<c_0+c_1<infinity is used. This would stop the profile, not the
integrated comparison or RH.

L019 supplies actual positivity/decay; L966 defines the observable;
L967 supplies the audited finite transfer and all faces; L968 explains
downstream all-n sufficiency. No cross-notebook premise or zero sign
is used. Preserve the old one-coordinate stop and the finite-window
stop. Final canonical proof, scoped history and checkpoint are pending.
