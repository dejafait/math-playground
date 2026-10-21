# Left crossed trace — saved ordered bulk attempt

STEP_ID: YM-20261019-338-left-crossed-ordered-bulk-bound

Work under the unchanged ready EXPLORE assessment
`literature/2026-10-19-left-crossed-quantitative-remainder.md`, at its
exact R_L target. The main construction and interacting reflected-error
gaps remain independent. The intermediate target is L240(3)'s literal
whole-grid trace within N^(5/2)log(eN)^2. No upstream audit is claimed.

Write P,Q for the massive contractions, R for the massive covariance,
and define U_k=P Omega_k R Q^2 and H_k=Q Omega_k R Q^2.
Then R Q^2 Omega_k* P=U_k* and
R Q^2 Omega_l Q=-H_l*, so B=-a^-1 sum c Tr(U_k* A H_l*),
where A=P G-TV. This sign needs preservation through the final proof.

Candidate estimates: U_k=a sum_j M_(v_kj) J_gj+E_gk,
H_k=a sum_j M_(v_kj) J_hj+E_hk, with
J_gj=P Omega_j R Q^2 and J_hj=Q Omega_j R Q^2.
Each joint convolution has squared kernel norm O(1), weighted squared
norm O(log(e/epsilon)), and operator norm O(epsilon^-1/2), uniformly
in delta. Check the derivative on the left P as well as all Q factors;
Omega_j=O(r) cancels its transverse derivative singularity.
Projection commutators and local coefficient errors should give
||E_gk||_HS+||E_hk||_HS <= Cp(k)(epsilon^-1/2+sqrt(log(e/epsilon))).
The complete exterior-circulation terms belong to the O(a^2) local
coefficient remainder, using Lipschitz extensions and Cc(constant)=0.

G=sum_r M_(u_r) W_r+O_op(a), with W_r normalized complete generator.
TV=sum_(mu=2)^4 M_(u_mu) Z_mu+O_op(a),
Z_mu=T H_av C_mu, all as edge-space operators. The finite-range
stencil errors keep their supports and original endpoint filters.
For P G first retain [P,M_(u_r)] W_r. Its HS norm is O(aN^2);
in the trace use ||J_g||_op=O(epsilon^-1/2) and
||J_h* M_v||_HS=O(p(l)N^2), with outside factor a.
At epsilon=N^-1 this is O(N^(5/2)). The remaining common scalars
can be collected with the joint J_g* commutator, at cost
O(N^2 sqrt(log(eN))). Do not commute component matrices through P.

The remaining main convolution should be precisely the L100 frozen
word with three imaginary odd factors, all massive P,Q powers intact.
Its closed trace integral is zero for each real k,l pair. Verify signs,
component phases, all domains and trace-ideal justifications before
accepting. Continue if the complete errors are within budget; abandon
any step needing separate absolute first moments or a small projection
commutator in operator norm. All source/end rows and full finite-mesh
heat coefficients stay covered via L240 and its imported qualifications.

Completed: the canonical proof is L241 in
`../lemmas/L241-left-crossed-ordered-bulk-remainder.md`. The exact
sign in (14) is negative. The uniform gh/hh kernel bounds, retained
middle commutator and closed-trace odd cancellation give
|B_i|<=C_i N^(5/2). With L240 this yields
|R_L|<=C_i N^(5/2)sqrt(log(eN)), within the target threshold.
This is a selected component rate relative to imported hypotheses;
the new proof and L237--L240 still require a separate critical audit.
No independent construction gap is closed and no new source or
mathematical script is used. Continue the same approved target by
critically auditing this argument and its exact imported comparisons.
