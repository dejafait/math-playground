# Scalar-placement error: joint closed-trace test

Ready assessment: drafts/literature/2026-10-10-other-other-cubic-leading-scale.md.
One bounded subtest of its unchanged complete other/other target.
Main gap: interacting ultraviolet control and a nonzero physical continuum
sector, with independent axioms, positivity and infrared/mass obligations.
Intermediate target: a finite cubic-scaled limit for
Delta_sc=R_bulk,moved-R_bulk,sc in L113(9). Its downstream use is another
retained coefficient of transverse H. The exterior-circulation and
energy-placement errors and all coefficient evaluations remain open.

Initial working reasoning, subsequently checked in L121:
replace P by P_bulk in both terms. L114's compact-row estimate applies
to the first term too: X F_l^T has compact input columns because X
ends with the compact displacement multiplier. This should cost
O(N^(5/2)(log N)^(3/4)) after the complete level and heat sum.
It requires compact projection-adjacent rows, never compact X output.

Use (S_alpha v)(z)=sum_h s_alpha(h)v(z+h), and write p(d) for
P_inf's edge kernel. Let g_(r,j)(d) be the plaquette kernel of
D T_r C_r E_j. For d=x-y, the original and collected scalar factors
in a closed trace are respectively
phi_(l,alpha,s)(y) phi_(k,beta,t)(x) and
phi_(l,alpha,s)(x-n) phi_(k,beta,t)(x-n), where n is the right
S_beta shift; their common matrix factor is
g_(r,j)(d) s_alpha(h)^T p(-d-h+n) s_beta(n), multiplied by b_(r,t)(y).
This exact difference retains both path-placement errors and the middle
scalar commutator. No separate term has been discarded.

At fixed offsets, expanding about y gives a times
sum_m [n_m phi_l partial_m phi_k-(d_m-n_m) partial_m phi_l phi_k].
The remainder test is joint: sum_d (|d|+C)|g_j(d)||p(-d-h+n)|,
bounded by C(Q_j+W_j)||p||_2 and summable over j by L110/L111.
No separate absolute first moment or projection norm gain is assumed.
Compact b(y) and fixed d make both stencil columns interior, so only
after uniform tail removal are unrestricted full-grid entries exact.
Fixed-mode C^1 convergence must be checked for the actual signed paths,
using the exact lower prefix and constant mode, rather than a smooth
extension through the upper pin. The expected normalization is
a^3 a^-1 a^2 a min(s,t)=a^4 [a min(s,t)].

Essential inputs L028 L080 L088 L110 L111 L113 L114 L120; L115/L118
locate the remaining energy error, L091/L095 fix assembly and
L084/L079/L080/L082 fix the reference and its arithmetic qualifications.
Preserve ATTEMPTS/028--032 and the unfinished generator-error notes.
Continue only if the projection comparison, exact scalar difference,
uniform joint tails and fixed-mode derivative limit close. Abandon this
mechanism if it needs an unsupported support transfer, coefficient
zero-extension smoothness or a failed separate kernel moment. A norm
bound alone is not a signed-growth conclusion. No limit, evaluated
coefficient or compensation is assumed by the initial test.

Completed: [L121](../lemmas/L121-other-other-scalar-placement-error-limit.md)
proves a^3 Delta_sc -> K_(i,sc) for both actual probes and an explicit
first-derivative comparison with o(N^3) error. The scalar difference
above is exact for the complete error. The projection replacement in
both terms costs O(N^(5/2)(log N)^(3/4)); norm-one component selectors
retain partial boundary stencil restrictions, and a positive joint
kernel majorant controls their full spatial/axial tails. The actual
signed paths converge in transverse C^1 at fixed modes by their exact
prefix formula. The normalization and heat tails close. The real
functional is absolutely convergent and unevaluated. Outcome ADVANCE,
RESEARCH / REPRODUCTION: local standard-method progress only. No
numerical script or independent source refresh was needed.

Concrete continuation inside the unchanged approved target: test
Delta_en=R_bulk,sc,Pbulk-R_prod in L115(3). Start from its exact
rectangular identity (6)-(7), retaining finite compressions, the path
coefficient difference and the joint energy commutator; seek a finite
cubic-scaled limit by a closed-trace derivative test or a discriminating
obstruction. This is a proposed subtest, with no energy-error reduction,
limit or value assumed. Continue if compact input placement, uniform
joint tails and fixed-offset derivative convergence all close. Abandon
the mechanism if it needs unsupported support transfer, zero-extension
smoothness or separate absolute moments. Insufficient generic norm
bounds are not signed-growth evidence.

Essential continuation inputs: L028 L080 L088 L110 L111 L113 L114
L115 L120 L121. L116/L118 fix the zero full-grid comparison, L091/L095
fix assembly, and L084/L079/L080/L082 fix the reference and its arithmetic
qualifications. The exterior-circulation limit, every coefficient
evaluation, complete compensation, finer powers/logarithm, other jets,
interacting error <=c_box/2, continuum fields/axioms, reflection
positivity, infrared control and finite positive mass stay unresolved.
Preserve ATTEMPTS/028--032. The exact saved Next action and prior EXPLORE
assessment are unchanged; no new source assessment is written.
