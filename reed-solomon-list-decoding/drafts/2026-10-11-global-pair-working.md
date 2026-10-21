# Global prescribed pair slice — bounded exact attempt

Step rsld-2026-10-11-160-global-pair-slice. The pre-invocation
SPECIALIZE assessment is drafts/literature/2026-10-07-global-pair-marginal-extension.md.
No additional literature is needed for its unchanged target.

Main gap: arbitrary-center safety at 68/67 agreements. Intermediate
target: exactly the assessed global pair slice, with every prescribed
overlap, nonnegative entries and the augmented constant coordinate.
Feasibility parks only this diagnostic; exact infeasibility excludes
only this prescription. Neither implies a representing distribution,
an RS list, higher-moment consistency or a boundary improvement.

Inputs read: L021's complete LP proof, L027's selected-support/core
restriction, L030's complete pair-moment computation, foundations/08–09,
and ATTEMPTS/011,019,021,022. No duplicate completed global test was found
in these targeted records. ATTEMPTS/022 is an administrative park.

Put V=binomial(1024,68), v=binomial(963,7), rho=2571353/v.
For relation distance i write a_i=binomial(68,i)binomial(956,i)F_i/rho.
Then a_0=1, a_1,...,a_4=0, and a_5,a_6,a_7 are prescribed by
L030's local N_2,N_1,N_0 respectively. Only a_8,...,a_68 are free.
The imported spectral and Schur criteria require
1+sum_i q_ji a_i>=0 (j=1,...,68), all a_i>=0, and
1+sum_i a_i>=V*rho. This last condition retains the constant eigenspace
of F-rho^2 J, not just PSD of F. Exact singular cases are admissible.

First bounded reconstruction: set the first 61 nonconstant inequalities
to equality and solve for the 61 free coordinates, then check every
coordinate and all 69 inequalities exactly. A failed candidate is not
infeasibility; a complete rational primal or Farkas certificate is required.
All certificate data will be saved under scripts/finite-support/.

The initial exact candidate has nonnegative entries and constant Schur
sum zero, but negative spectral sums at j=63,64. A bounded 120-basis
search did not find feasibility; this search is not an infeasibility
certificate and is retained in the calculation output.

Potential exact obstruction: for each 61-core C, the covariance
K=F-rho^2 J has u_C^t K u_C=0, since all its local row sums are
rho*2571353 and v*rho=2571353. PSD therefore forces K u_C=0.
After averaging, put b_i=F_i/rho. For r=|S intersect C|=61-t,
the row equation is
sum_(i=t)^(t+7) binomial(7+t,t+7-i)binomial(956-t,i-t)b_i=2571353.
For t=1,...,61 this is triangular in b_8,...,b_68, with positive
leading coefficient binomial(956-t,7). Verify this forced vector,
all core equations and every Johnson eigenvalue exactly. A negative
eigenvalue of this unique vector is a proved obstruction; the failed
basis search plays no role in its proof.

Completed: the triangular vector equals the initial reconstruction.
All core equations hold and all entries are nonnegative, but the exact
spectral sums at j=63,64 are negative. The canonical full proof is
lemmas/L051-prescribed-global-pair-slice-infeasibility.md. Independent
arithmetic reconstruction checks all 5038 values/conditions without
failure. The unsuccessful 120-basis evidence is preserved separately
in scripts/finite-support/global-pair-slice-discovery-results.json;
default reproduction now omits that unnecessary discovery search.
This is a fixed-slice exclusion only; a separate critical audit remains
pending, and no arbitrary-center bound or complete solution follows.
