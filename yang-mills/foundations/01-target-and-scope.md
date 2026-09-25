# Exact target and source audit

Checked 2026-09-24 and reopened 2026-09-25: the [current Clay problem page](https://www.claymath.org/millennium/yang-mills-the-maths-gap/) links to Arthur Jaffe and Edward Witten, [*Quantum Yang–Mills Theory*](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf), 14 pages. The controlling formulation is section 4, p. 6, read with sections 3 and 5 and footnote 2 on p. 12. The linked version and target are unchanged at the second check.

For every compact simple gauge group, the target is a nontrivial quantum Yang–Mills theory on four-dimensional continuum spacetime. Its axiomatic strength must match the cited Wightman/Osterwalder–Schrader frameworks: positive Hilbert space, relativistic covariance, positive energy, unique invariant vacuum, and locality. Local operators must correspond, with renormalization qualifications, to gauge-invariant curvature polynomials and covariant derivatives. Short-distance correlations must have the specified asymptotically free behavior, including stress-tensor and operator-product structure.

With vacuum energy zero, the Hamiltonian must satisfy

\[
\sigma(H)\cap(0,\Delta)=\varnothing\quad\text{for some }\Delta>0,
\qquad
m:=\sup\{\Delta>0:\sigma(H)\cap(0,\Delta)=\varnothing\}<\infty.
\]

Confinement, an isolated particle, and extension to other manifolds are additional questions. Compactness without the required properties of the limit is explicitly insufficient. These requirements come from the linked official description; prize procedures are outside this notebook's mathematical target.

## Operational nontriviality test

For a proposed Euclidean construction, form the positive-time reflection inner product. A centered observable must have strictly positive norm in the quotient if it is to create a nonvacuum state. Nonzero variance in the original probability space is a different test: it does not by itself imply a positive reflection norm. This distinction is proved directly in L001 for one soluble lattice observable sector.

The notebook has not constructed the required Yang–Mills observables, their continuum limits, or their finite positive mass. A failure for a chosen SU(2) plaquette field cannot refute the existence target for SU(2), much less the statement for every gauge group.

## Mathlib

Coverage of the full target and the axiomatic frameworks: **not checked**. No library theorem is asserted to construct the required theory.
