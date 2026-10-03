# Strong relative domain with unrestricted Dirichlet ghosts

Tested 2026-10-03. The proposed domain imposes A_t = 0, partial_n A_n = 0 and c = bar c = b = 0 on all physical faces while retaining independent b and allowing arbitrary smooth ghosts off shell.

## WHY IT FAILS

[L012](../lemmas/L012-relative-boundary-domain-is-not-off-shell-brst-closed.md) gives a smooth single-colour cube counterexample at A = 0: the Dirichlet ghost and even its first normal derivative vanish on all faces, but the BRST variation of partial_n A_n is nonzero on the upper face. Thus this strong connection domain cannot justify an off-shell boundary Ward exclusion with the stated ghosts. This is a domain obstruction, not a counterterm, divergence or renormalizability result. Spectral/equation restrictions remain distinct, and L003's Gaussian construction is retained. A formulation imposing the auxiliary-field boundary condition before eliminating b is a different mechanism; its covariance and boundary identity require a separate applicability assessment rather than another test of this failed domain.
