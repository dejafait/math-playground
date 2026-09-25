# Fixed-box Gaussian plaquette test, 2026-09-25

## Preflight and bounded target

Read the shared GOAL.md and PROMPT.md, local GOAL.md and PROGRESS.md, the entire PROOF.md and DAG.md, existing changes, the relevant free-field proof and regulator conventions, and both recorded failed approaches. Existing unfinished work is preserved. Reopened the official Clay page and its linked Jaffe–Witten description: section 4 still requires a nontrivial continuum theory and finite positive mass; the recorded target is unchanged.

Gap: the positive free coefficient in L002 has not yet been matched to a gauge-invariant lattice observable with an explicit infrared regulator. The proposed intermediate target is the quadratic Gaussian coefficient of a centered SU(2) Wilson plaquette smeared with the same normalized positive-time bump, in the fixed box [-4,4]^4 with links contained in its boundary fixed to the identity. Seek a strictly positive lower bound uniform as the mesh tends to zero.

Plausible downstream use: this would provide a concrete reference coefficient for an interacting reflected-correlation comparison in the same box and normalization. An ultraviolet-uniform smaller interacting remainder, renormalized field construction, full limiting reflection positivity, other gauge groups, and infrared removal with finite positive mass remain unproved. A positive Gaussian coefficient does not supply any of them.

Discriminating test: derive the actual quadratic Wilson action and plaquette coefficient, account for gauge degeneracy and the boundary condition, and isolate a positive contribution to the reflected coefficient that survives mesh refinement. Continue the comparison if its lower bound has positive liminf; reject this regulator/observable match if it vanishes, or withhold the match if the gauge or boundary calculation cannot be justified. This differs from the stopped independent-link endpoint and the unsupported direct MRS positivity import, and is not already contained in the infinite-volume calculation.

## Saved reasoning before the detailed calculation

Represent the box by a product of one-dimensional relative cochain complexes: interior vertex values vanish at endpoints, while edge values are unrestricted. Thus one-form components are Dirichlet in the three transverse coordinates and have the edge version of Neumann conditions in their own coordinate. This fixes tangential boundary links without silently imposing Dirichlet conditions on every gauge-potential component.

Add the finite-dimensional quadratic gauge-fixing term ||d* A||^2 to ||d A||^2. The relative Hodge Laplacian should separate into sine vertex modes and cosine midpoint edge modes. The curvature covariance is unchanged by this gauge fixing, since d kills gradients. For a spatial magnetic component, its time coordinate has Dirichlet boundary conditions. The massive one-dimensional Dirichlet Green function across the reflection plane factors into a product of positive functions of the two positive times.

This suggests a direct mode expansion of the reflected curvature covariance. Squaring and smearing a nonnegative bump should make every ordered pair of modes a nonnegative squared term. Keeping one mode whose curvature is nonzero in the support could give a uniform positive lower bound without comparing boundary corrections pointwise with the infinite-volume covariance. The mode choice, factors of a and g, Green-function normalization, continuum limit of this contribution, and limits of the claim are still to be checked.

## Saved derivation and remaining checks

Use even N, a = 8/N, and Hermitian generators with Tr(T^c T^d) = delta_cd/2. For U_e = exp(i g a A_e), the deficit P_p = 1 - Tr(U_p)/2 has quadratic term g^2 a^4 sum_c (d A)_p,c^2 / 8. Thus beta = 4/g^2 gives canonical Maxwell action, and the observable (4/g^2) sum_p f(z_p) P_p has Gaussian term (a^4/2) sum_p,c f(z_p) (d A)_p,c^2. Centering gives the same color/Wick factor 3/2 as before.

The selected spatial mode is (k_1,k_2,k_3) = (0,2,1). With omega_k,a = (2/a) sin(k pi/(2N)), its continuum mass parameter is Omega = pi sqrt(5)/8 and magnetic numerator alpha = pi^2/16. Its squared spatial eigenfunction is bounded below on the test support by m_phi = cos^2(pi/16) cos^2(pi/32)/128. The time resolvent across the plane factors as a sinh(gamma(4-t)) sinh(gamma(4-s)) / [sinh(a gamma) sinh(8 gamma)], where gamma = (2/a) asinh(a Omega_a/2).

The anticipated continuum lower coefficient is d_box = m_phi alpha sinh^2(2 Omega) / [Omega sinh(8 Omega)], giving q_box >= (3/2) d_box^2. A summable mode bound of the form C |k| exp(-|k|/4), valid for t,s in [1,2], should justify convergence of the entire separated covariance, not just the retained mode. The proof must retain the distinction between fixed-mesh small-coupling Laplace asymptotics and an estimate uniform in the ultraviolet cutoff.

For the finite-mesh matching, a rooted forest from interior vertices to the boundary removes gauge freedom exactly by Haar invariance. The action on remaining links has a unique flat minimum: plaquette flatness on the cubical box implies path independence, and boundary links and forest links are identity. Its Hessian is positive since a closed relative one-cochain is a gradient, killed by the forest condition. Ordinary finite-dimensional Laplace scaling can then identify the Gaussian limit at each fixed mesh. Orthogonal decomposition into gradients and their complement identifies its curvature law with the relative Hodge gauge-fixed covariance. Detailed normalization and domination checks remain to be written out in the lemma.

## Completed assessment

The full proof is in [L003](../lemmas/L003-fixed-box-wilson-gaussian-reflection.md). The finite-dimensional gauge reduction and Laplace argument identify the Gaussian coefficient of the actual centered Wilson observable at each fixed mesh. Its relative boundary modes yield the reflected kernel factorization, a summable bound for the full separated limit, and the explicit surviving-mode lower bound. Thus the test passes: the Gaussian reflection coefficient has a finite positive continuum limit in this fixed box and an eventual mesh-independent positive lower bound.

The result supplies the previously missing regulator and normalization match, not a simultaneous interacting ultraviolet limit. The Laplace estimates have mesh-dependent constants. An arbitrarily small bare coupling chosen separately at each mesh does not control a prescribed physical renormalization trajectory. The actual comparison still needs an ultraviolet-uniform interacting error smaller than the free coefficient, with an adequate observable renormalization. Studying the ultraviolet correction is justified because it tests that remaining requirement before treating the bare coefficient as an interacting lower bound.

The [sanity-check script](../scripts/fixed-box-gaussian/check.py) verifies the cochain identities with integer arithmetic and checks the interval modes, Green-function normalization, and retained-mode sums numerically. It is supporting evidence only: the convergence and uniform bound are proved analytically in L003. No new failed approach, full candidate solution, or disproof arose. Mathlib coverage is not checked.
