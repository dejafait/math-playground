# Weighted two-branch detector: bounded attempt

Work in progress, 30 October 2026. Approved starting assessment:
`drafts/literature/2026-10-30-weighted-two-branch-detector-test.md`
(EXPLORE, saved before this invocation). No new source gate is being
approved during this research step.

The main gap is actual-Xi all-degree mixed positivity and initial signs
at unbounded heights. Write L=log T and delta=log L/L. The one target is
W_delta(T)<=C T delta L^2 exp(-c delta L) for fixed absolute C,c>0,
where W_delta integrates |zeta(1/2+it)|^2 against the full-multiplicity
count of zeros beta>1/2+delta/2 and |gamma-t|<=2delta. A successful bound
might enter the L486 nonnegative kernel before amplitude/count
separation. Kernel transfer, other displacement scales, complementary
mass and individual signs remain independent open obligations.

Attempt both alternatives of Baier Proposition 4, retaining the local
amplitude integral at each zero. Check Gamma near-line cost, polynomial
length, finite-window transfer and multiplicities against Fazzari
Lemma 2.1. Continue only if both branches meet the target or yield a
distinct explicit correlation term with a test. Stop this implementation
if it requires the missing weighted selection theorem or reproduces the
L486 loss. Existing count-only, selected-supremum and Blaschke stops
remain evidence, not global prohibitions.

Checkpoint after the mathematical reduction: choose X=T^(1/8),
Y=T^(1/4), source upper height and N both 3T. Each selected zero has
weight E_rho=integral_[T,2T]intersect[gamma-2delta,gamma+2delta]
|zeta(1/2+it)|^2 dt. The two positive detector sums are
sum m_rho E_rho U_j(rho)^2, and W_delta is at most four times their
sum. No zero separation or simplicity enters this finite identity.

For a=delta/2, the uniform Gamma envelope is
g_a(v)=(a^2+v^2)^(-1/2) on |v|<=1 and
exp(-pi|v|/2)|v|^(-1/2) outside. Its mass is comparable to
1+log(1/a), so the Gamma branch leaves the explicit correlation
sum m_rho E_rho integral g_a(v)|zeta M_X(1/2+i(gamma+v))|^2 dv,
multiplied by O(Y^(-delta)(1+log(1/a))). The short tail branch
leaves sum m_rho E_rho |P_(beta-1/2)(1/2+i gamma)|^2.
Both remain unbounded at the required scale. The latter polynomial
has length <=T^(3/8), so lack of a strict length margin is not its
problem: Fazzari's deterministic continuous moment still has neither
the selected offsets nor their multiplicity-counted sampling measure.
The Gamma branch additionally has a second zeta-squared amplitude.

The count-only fallback from L485 and the continuous fourth moment is
W_delta<=C T delta L^3 exp(-delta L/16), hence its normalized
certificate is C L^(15/16) at this test scale, versus the required
O(L^(-c)). This is a failed upper-bound certificate, not a lower bound.
Full hypotheses, derivation and source comparison are preserved in
`lemmas/L500-weighted-two-branch-detector-reduction.md`; this file keeps
the interrupted-work checkpoints, not a second canonical proof.
No target bound or independent critical audit is claimed. The final
implementation stop is in
`ATTEMPTS/2026-10-30-weighted-two-branch-detector-stop.md`.
