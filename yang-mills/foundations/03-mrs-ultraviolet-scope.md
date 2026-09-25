# MRS ultraviolet construction and the reflection-norm gap

## Primary citation and coverage

Jacques Magnen, Vincent Rivasseau, and Roland Sénéor, *Construction of YM4 with an infrared cutoff*, Communications in Mathematical Physics **155** (1993), 325–383, DOI [10.1007/BF02097397](https://link.springer.com/article/10.1007/BF02097397). Checked 2026-09-24 using the publisher record and the [author-uploaded full text](https://www.researchgate.net/publication/251358884_Construction_of_YM_4_with_an_infrared_cutoff). The controlling passages inspected were the abstract, section I (especially p. 327), section II.A (p. 328), the end of section II (p. 347), and section VIII (pp. 377–378). This is a scope audit, not an independent verification of every estimate in sections III–VII.

The paper treats pure SU(2) in the trivial topological sector, in a regularized axial gauge, with a fixed infrared cutoff. Its unnumbered statement on p. 327 asserts existence of ultraviolet-limit Schwinger functions and the infrared-cutoff-adapted Slavnov identities (VIII.6). That page explicitly leaves a detailed proof unwritten and reflection positivity to additional work, suggesting a lattice starting point for the latter. Section VIII ends with a sketch in which the ultraviolet defect delta_N(rho) vanishes while the infrared correction E_N remains. These qualifications belong to the citation; no stronger theorem is imported here.

## The estimate the notebook actually needs

Fix a reflection plane t = 0 and an infrared regulator with physical scale ell. Let rho index ultraviolet cutoff removal. In a prospective construction, choose a renormalized gauge-invariant observable O_(rho,ell)(f), with a specified normalization and fixed test-function support in t > tau > 0, and center it:

\[
F_{\rho,\ell}=O_{\rho,\ell}(f)-\langle O_{\rho,\ell}(f)\rangle_{\rho,\ell},
\qquad
Q_{\rho,\ell}(f)
=\langle\overline{F_{\rho,\ell}^{\theta}}F_{\rho,\ell}\rangle_{\rho,\ell}.
\]

Here the brackets denote prospective normalized Euclidean functionals; their existence and appropriate reflection properties are requirements, not consequences of this notation. Before reflection positivity is established, Q is a candidate reflection form and must not be called a Hilbert-space norm.

The discriminating nontriviality threshold is

\[
\liminf_{\rho\to\infty} Q_{\rho,\ell}(f)\ge c_{\ell,f}>0.
\]

One also needs convergence of the moments defining this form, consistent centering and reflection, and positivity of the limiting reflection form on the entire observable algebra. With those additional properties, the displayed lower bound would give a nonzero vector orthogonal to the vacuum. It would give neither a mass gap nor an infinite-volume construction.

The audited main statement supplies no such O, normalization, or constant c. Vanishing of a defect in a gauge identity is a different assertion from a lower bound on Q. Likewise, nonnegative ordinary integration weights and estimates controlling integrals do not by themselves establish positivity of reflected Gram matrices. This audit establishes no value, positive or zero, for Q in the MRS construction.

## A concrete conditional comparison to investigate

An observable-level perturbative comparison could have the form

\[
Q_{\rho,\ell}(f;g)=q_{0,\ell}(f)+R_{\rho,\ell}(f;g),
\qquad q_{0,\ell}(f)>0,
\qquad
\sup_{\rho\ge\rho_0}|R_{\rho,\ell}(f;g)|
\le\tfrac12q_{0,\ell}(f),
\]

after fixing the coupling and observable normalization so that q_0 is the free leading coefficient. These are proposed requirements, not established estimates: if they held for a real reflection form, elementary subtraction would give Q >= q_0/2. The remainder here is not the Slavnov-identity defect delta_N. Ordinary finite-order perturbation coefficients alone cannot supply the uniform remainder estimate.

The free limit of the magnetic curvature polynomial Tr(F_12^2) is a concrete candidate for testing the leading coefficient. Reflection separates its two insertions, but composite-operator renormalization within each insertion must still be specified. A positive free coefficient would justify examining an interacting comparison; a vanishing coefficient would reject using that particular test function and normalization as a positive leading term for this comparison. No free-field calculation or composite-field construction is claimed in this audit.

Even a successful fixed-ell comparison would leave full reflection positivity, construction of the required field algebra, removal of the infrared regulator with nontriviality preserved, the remaining axioms and gauge groups, and a finite positive physical mass unresolved. The source limitation does not prohibit further work on its ultraviolet mechanism.

## Mathlib

Coverage of the full cited construction, reflection positivity for it, and the proposed composite-observable comparison: **not checked**. No full matching theorem or supporting Mathlib theorem is asserted. The paper is a primary mathematical source with the qualifications above, not a Mathlib match and not a proved input to the local DAG.
