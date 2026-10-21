# Full-prefix E replacement: joint-mode attempt

Approved target: determine whether L101's full static-replacement error
is O(N^(5/2) log(eN)^2) for both actual probes. Reuse the unchanged
EXPLORE assessment `literature/2026-10-17-e-static-replacement-quantitative-rate.md`.
The main gap is still interacting cutoff removal with reflected error
<=c_box/2, continuum axioms and finite positive mass. This component
rate could help a later complete perturbative remainder estimate.

Unfinished reasoning checkpoint: for each unit transverse curvature
eigenvector e and normalized axial sine phi_m, the r-th column block
of the output row of H_k=Zeta_k U B is
sum_(s=r+1)^(N-1) phi_m(s) e^T Zeta_k(s) U. Partial sine sums are
bounded by C/(sqrt(N) sqrt(mu_m)). Abel summation against the actual
Zeta_k uses only its O(a p(k)) norm and O(a^2 p(k)) neighboring
differences, hence suggests a full row norm squared <=C a^2 p(k)^2/mu_m.
The upper endpoint term is retained, not assumed zero. Multiplying by
L101(9)'s mu_m/(mu_m+lambda) suggests a squared replacement error
<=C a^2 p(k)^2 sum_(m,lambda) 1/(mu_m+lambda)=O(p(k)^2 N^2).
Check the full transverse shell count and the original signed residual
pairing, including its F_k error, before asserting the target.

Essential inputs are L008 L028 L065 L097 L101; L101's existing exact
L085/L088/L091/L092 identities are imported through that lemma.
No coefficient is commuted through a transverse projection. Scalar
path diagonalization is imported from the inspected Dowker v2
section 7, (30)–(31), not reproved. The scoped original drafts and
ATTEMPTS/024, 025, 030 do not establish or refute this error rate.
Continue on a complete heat-summed bound at the requested threshold
or stronger; abandon this estimate if upper-end terms, mode dependence
or a transverse shell sum exceed it. The static trace's continuum
rate, other component rates, L220's separate audit and the interacting
expansion remain unresolved. No scripts or numerical evidence are needed.

Completed: [L223](../lemmas/L223-e-static-replacement-joint-mode-rate.md)
proves the stronger O(N^(5/2)) bound. The weighted joint mode sum is
exactly bounded by a^2 Tr K_h=O(N^2); the original signed pairing
and full exterior heat sum then close. The proof retains the Abel
upper endpoint and every exterior-circulation term. This is a local
standard-method refinement, pending separate critical audit, with no
claim of progress beyond the checked literature. No numerical check
is needed for this finite-dimensional analytic estimate. The next
audit's source scope is recorded separately as REVIEW_REQUIRED;
this turn does not approve that new continuation.
