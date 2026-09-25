# Lattice stress-tensor matching: source and scope

Checked 2026-09-25: Leonardo Giusti and Michele Pepe, *Energy-momentum tensor on the lattice: non-perturbative renormalization in Yang–Mills theory*, Phys. Rev. D **91**, 114504 (2015), [arXiv:1503.07042v2](https://arxiv.org/abs/1503.07042v2), section III, [equations (26)–(28)](https://arxiv.org/html/1503.07042v2#S3).

The diagonal traceless stress components form a hypercubic triplet. Equation (27) assigns that triplet the multiplicative factor Z_T z_T; only the singlet requires identity mixing. The factors are finite in the paper's renormalization framework. Section III.1, equations (29)–(32), specifies Ward-identity normalization conditions and their finite-size qualifications.

This is supporting precedent, not a matching theorem for this notebook. The paper uses SU(3), a clover field-strength discretization, and shifted temporal boundary conditions. Its coefficients are not transferred to the SU(2) average of plaquette traces with fixed boundary links. L006 proves the relevant polynomial classification and treats that discretization directly. Neither the citation nor that classification supplies the required fixed-box interacting error bound.

## Local translation identities

Checked 2026-09-25: L. Del Debbio, A. Patella, and A. Rago, *Space-time symmetries and the Yang–Mills gradient flow*, JHEP **11** (2013) 212, [primary paper, arXiv:1306.1173](https://arxiv.org/pdf/1306.1173). Section 3, equations (3.1)–(3.3), introduces gauge-covariant local translations. Section 6, equations (6.1)–(6.4), retains the lattice translation-breaking insertion. Equations (6.12)–(6.17) distinguish normalization of the translation generator from normalization of the stress tensor. The passage to (6.14)–(6.16) explicitly assumes restoration of continuum translation invariance; it is not a construction theorem proving that restoration. Positive-flow-time probes address contact singularities within that framework.

These are supporting normalization mechanisms. They do not determine the SU(2) site-plaquette coefficient or a fixed-boundary error bound here. L007 proves a separate geometric obstruction to selecting only the triplet by a compact displacement and gives the exact finite-product Haar identity without assuming restored symmetry.

## Mathlib

Coverage of the source's renormalization statements and supporting representation theory: **not checked**. No inspected Mathlib theorem or direct library link is asserted. This source is not a constructive Yang–Mills existence or mass-gap result.
