# 2026-09-25 — Complementary-plaquette reflection test

## Preflight and saved reasoning

Read the shared instructions, local target and checkpoint, the whole argument overview and DAG, the relevant Gaussian and normalization proofs, and the three stopped approaches. Existing changes are retained. Reopened the current Clay page and its linked Jaffe–Witten statement, section 4, p. 6 and footnote 2 on p. 12; the target recorded in foundations/01-target-and-scope.md is unchanged.

Gap: the complementary-plane stress-tensor channel has no established fixed-box Gaussian reflection lower bound. The earlier single-plane bound cannot be transferred by subtraction without controlling mixed terms. This is distinct from the stopped common-counterterm prescription and from the independent-link and direct-source-import failures.

Intermediate target: with the exact relative boundary conditions, Wilson normalization, and test f_* of L003, derive the Gaussian coefficient of F_12(f_*) - F_34(f_*), prove a finite separated mesh limit, and find a constant c_D > 0 independent of sufficiently small mesh. Its plausible use is a nonzero leading coefficient for a correctly matched interacting observable. A later estimate |Q^D_(a,g(a)) - q^D_a| <= c_D/2 would then preserve this one reflection norm; finite lattice matching, the coupling trajectory, field axioms, infrared control, and finite positive mass remain separate gaps.

Discriminating test: compute the mixed covariance and the electric 34 reflection kernel, including the temporal midpoint grid and contact term. Continue if the mixed terms vanish or can be bounded and a positive mesh-independent coefficient survives. Abandon the naive difference if cancellations force zero or no positive uniform bound can be justified. A fixed-mesh positive number alone is insufficient.

Working observation, to be proved and checked: L003's Gaussian Hodge Laplacian is diagonal in the four potential components. Thus B_12 uses only A_1,A_2 and B_34 only A_3,A_4; their entire Gaussian families should be independent. For the electric channel, spatial waves are v_(k1)v_(k2)e_(k3), with k1,k2 >= 1 and k3 >= 0. Writing Omega^2 = omega_1^2 + omega_2^2 + omega_3^2, its time covariance is

    omega_3^2 (D D* + Omega^2)^(-1)
      + D (D* D + Omega^2)^(-1) D*
    = I - (omega_1^2 + omega_2^2) (D D* + Omega^2)^(-1).

The identity term vanishes between reflected and positive temporal edges. The remaining Neumann edge kernel should factor with cosh instead of the magnetic Dirichlet kernel's sinh. The electric curvature is odd under reflection but its square is even. If these statements hold, the centered difference coefficient is the sum of two nonnegative square forms, and retains L003's c_box. No interacting independence is proposed.

This was the first turn for this specific test; no inconclusive exploration turns were carried over. The preceding reasoning was saved before the detailed proof and computations.

## Completed assessment

[L005](../lemmas/L005-complementary-plaquette-gaussian-reflection.md) establishes the intermediate target. Independence of complementary Gaussian curvature families eliminates both mixed centered terms. The electric covariance is the contact identity minus beta times the Neumann edge resolvent; the contact contribution vanishes only after restricting to separated reflected supports. The resolvent factors with cosh time waves, so the electric-square reflection form is a nonnegative sum of squares. A summable exponential spatial-mode bound proves its finite mesh limit. Thus the difference retains exactly the already available lower-bound constant c_box, without assuming interacting independence or transferring the bound by subtraction.

The [finite-matrix checks](../scripts/complementary-plaquette/check.py) independently invert the temporal operators at N = 4,8,16 and the full four-dimensional relative Hodge matrix at N = 3. They confirm the contact identity, edge Green normalization, mixed covariance zero, and separated electric spatial-mode formula. Maximum errors were 2e-15 for the temporal formulas and 3.79e-19 for the electric cochain comparison. These are checks of the analytic proof, not evidence for a uniform interacting estimate.

The achieved bound is q^D_a >= c_box and q^D_box >= (3/2)d_box^2. The required later bound remains an interacting error <= c_box/2 for a correctly matched observable and prescribed coupling trajectory; nothing here bounds that error. Decision: ADVANCE, with zero inconclusive exploration turns. The Gaussian test supports investigating finite lattice matching, while full construction and mass remain unresolved. There is no complete candidate solution.
