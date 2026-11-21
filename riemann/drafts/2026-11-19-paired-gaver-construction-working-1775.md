# Paired Gaver construction1775: saved working reasoning

Approved target: assessment1773, SPECIALIZE, separately approved1774.
Main gap: actual-Xi all-degree positivity and signed-height/realization.
Bounded target: quantify C033l's TV<=2 separation using C033i/j's
exact residual jump; no numerical or unrestricted-inverse claim.

Read C033i's construction and norm, C033j's measure/density/mixture
and jump proof, C033l, C033q's complete proof and audit, and C033p's
qualified Lipschitz statement. Reused source-notes1774. Stops1571,
1576 and closure1768 remain in force for their stated mechanisms.

Working construction (not yet a completed proof): fix delta in (0,1/8),
x_minus=1-delta, x_plus=1+delta and rho=delta/2. Both rho-neighborhoods
lie in C033p's interval and avoid the residual jump. Apply C033q's
kernel identities for these variable centers. A common second-moment
bound is b_n=(1+delta)*sqrt(n+2)/(n*log(2)). Outside each neighborhood,
use the full variation norm and the supremum bound a_max*n*q_delta^n,
where q_delta=max h(1-rho/(1+delta)),h(1+rho/(1+delta))<1 and
h(v)=4*2^(-v)*(1-2^(-v)). This requires a proof, not a citation of
C033q's two-point conclusion at new centers.

Candidate orientation: left kernel minus right kernel. Width mixtures
have density difference at most 4*L*delta and four times the single
kernel error. Lambda's left density is zero and its right density is
-g(t), g(t)=exp(m)*ell_1(t), with g(1)>0. Use a compact continuity
modulus for g, not Lipschitz continuity across the jump. First fix delta,
then a local modulus scale, then choose finite n. All signed tails and
the zero atom must remain accounted for. Transfer each finite coefficient
back by division by exp(-B_1(s))>0; record data and divisor error bounds.

Success requires a strictly positive class-wide gap after all errors;
mere qualitative convergence or an unbounded global inverse will not
pass. B,L,V and residual modulus may remain nonnumerical. Unfinished
C033k and all preexisting changes are preserved. No new lemma yet
at the time this working checkpoint was saved.

Completion1775: the construction and all error budgets are now written
in canonical C033r. Fix delta, then tau, then n; the residual-minus-class
gap is at least J/2. The full proof retains both signed tails and zero
atoms and gives finite original-transform coefficients and data/divisor
error allowances. Its separate critical audit and all numerical input
certificates remain outstanding. This working note is not a second proof.
