# Residue/contour source review — working record

Invocation target: assess the derivative-free pole detector nominated in
`literature/2026-11-01-derivative-free-pick-contour-detector.md`.
Literature only; no new mathematical derivation or script.

Read the relevant L645 interpolation/residual proof, C645b/C645c
hypotheses and conclusions, L018, L467's shell statement and the
generalized-Schur source-limit stop. Existing interpolation coverage is
reused. No existing work was discarded.

Inspected primary sources so far:

- Bello Hernández–de la Calle Ysern, arXiv:1211.5573v1, Section 2.3,
  Theorem 2.2, Lemma 2.3 and its complete proof, pp.5–8. The theorem
  treats multipoint Padé approximants with fixed pole budget, not an
  arbitrary positive-real interpolant. The proof clears all poles and
  removes neighborhoods of denominator zeros. These are material
  applicability differences, not a quantitative actual-Xi certificate.
- Austin–Kravanja–Trefethen, author revised manuscript corresponding to
  SIAM J. Numer. Anal. 52 (2014), 1795–1821, Sections 3.2, 4 and 4.3.
  Its contour and rational-interpolation methods use roots-of-unity
  samples and a pole budget. Their algebraic equivalence does not
  provide our vertical-grid sign or a uniform residual norm estimate.
- Gonek (1984), printed p.126, selected-height construction, local
  partial-fraction statement and (16), followed by completion identity
  (17). The displayed O(log^2 T) bound is at selected heights, not on
  the unchanged radius-R circle. Do not use it there without a separate
  applicability argument.
- Beck et al., *A First Course in Complex Analysis*, online Section 8.1,
  Theorems 8.1.5 and 8.1.7 and their proofs. The residue theorem requires
  no singularity on the contour and sums every enclosed singularity;
  the simple-pole residue rule supplies no boundary-error estimate.

At the working-record checkpoint, the provisional direction was a
cluster contour test retaining all enclosed
zeros may be independently testable without evaluating zeta'(rho).
Neither an admissible contour nor a quantitative bound is established.
Do not clear only the stipulated pole or assume a lower separation
from other zeros. The completed review and separate cluster nomination
are now saved in `literature/2026-11-01-derivative-free-pick-contour-detector.md`
and `literature/2026-11-01-pick-cluster-residue-cancellation.md`. No
mathematical result was added after this source-work checkpoint.
