# Coordinate-Haar contraction in the combined response

The target remains the exact TARGET in
drafts/literature/2026-09-26-current-target.md. The saved SPECIALIZE
assessment is reused without changing hypotheses or doing literature work.
The shared/local rules, whole overview and DAG, L008--L011, L017, and the
previous direct-expansion and forest-representation records were read.
All existing work and stopped approaches are preserved.

The local gap is the unevaluated interacting coefficient in L011. This
step tests its actual coordinate-Haar contribution against both leading
quadratic probes, retaining the tree residual rather than setting it to
zero. This could guide the grouping of contractions needed for the full
cutoff logarithm. The full action/insertion/nonlinear-flow coefficient,
physical-boundary control and an interacting reflected error <= c_box/2
remain unresolved. No continuum or mass-gap claim is sought here.

Discriminating test: evaluate the connected M2 contraction, and compare
two genuinely different rooted forests. If it is forest dependent, stop
interpreting that isolated contribution as an invariant logarithmic
coefficient and require cancellation with the other terms. If it is
independent in the tests, that still does not establish a full logarithm
or license omission of the remaining vertices. A bare formula without an
evaluated contraction is inconclusive.

Working reasoning saved before computational work:

- In forest coordinates let H be the positive Wilson Hessian,
  Sigma=H^{-1}, B_i the full-flow leading probe matrix, and
  R=(H k+k^T H)/2-Q_3-Q_6 the symmetric residual matrix from L017.
  The density insertion is M2=sum_c |x^c|^2/12. Gaussian quadratic
  cumulants give -kappa(f_i0,r0,M2)=-2 Tr(B_i Sigma R Sigma^2),
  including the three independent colors. No density/divergence
  identification is made.
- For a change of forest x'=T x, the leading probe and residual
  transform by congruence, and Sigma'=T Sigma T^T. In contrast M2'
  pulls back to sum_c (x^c)^T T^T T x^c/12. Its contribution is
  -2 Tr(B_i Sigma R Sigma T^T T Sigma); it is not invariant merely
  because the exact nonlinear Haar quotient is invariant.
- Equivalently lift the quadratic M2 to the full free cochains by
  the explicit retraction R_F. Its matrix is G_F=R_F^T R_F, and the
  full Hodge covariance in x=a A coordinates is the inverse of the
  unscaled relative Hodge Laplacian. The trace is then
  -2 Tr(B_i Sigma R Sigma G_F Sigma). This lift is explicitly
  free-gauge invariant and justified by the existing linear quotient
  law; it does not transfer higher nonlinear forest vertices to a
  Hodge gauge.
- A lower-face straight forest and a forest rooted at both opposing
  faces with its omitted axial link in the middle have different path
  lengths. They avoid comparing two symmetry-related forests of the
  original displacement. The actual smooth cutoff, central differences,
  average of squares, clover shear, full heat flow and tau=1/16 are
  retained in any original-probe computation.

## Completed contraction and forest test

[L018](../lemmas/L018-coordinate-haar-contraction-and-forest-change.md)
proves the finite Wick contraction, its explicit full-Hodge lift, and
the change-of-forest formula. The lift first replaces the coordinate
density by ||R_F x||^2/12; only that free-gauge-invariant polynomial is
transferred. The full and forest traces are equal by the Gaussian
quotient law. No nonlinear vertex is moved to a different gauge law.

For a unit direction-1 edge at the upper face, the lower-rooted forest
leaves squared norm 1. The forest rooted on both opposing faces and
omitting axial level 12 has squared norm 67 when N=24. Its quadratic
density therefore changes by exactly 11/2. The field entries after
retraction are integers; the matrix-free check reproduces these values
exactly. This proves a difference of density functions, not a difference
of all their contractions against the two fixed probes.

The [dense check output](../scripts/combined-ward-response/haar-dense-results.json)
uses L017's N=4 rational one-site weights, explicitly a diagnostic other
than the original smooth displacement. It independently compares dense
incidence/probe/generator/covariance/heat matrices with the matrix-free
operators, with maximum discrepancy 5.2e-15. Both full/slice Wick traces
agree within 3e-11. Changing the omitted axial edge from 3 to 2 gives
the two contribution differences (0.0052164913,0.0007841645). These
floating values are not asserted as rigorously rounded nonzero theorems.

The [original-probe output](../scripts/combined-ward-response/haar-original-results.json)
uses rho and all central-difference and quadratic conventions of L008,
tau=1/16, and the admitted N=24 mesh (a=1/3). Active vertex indices
are 2 through 22, keeping all incident stencils strictly inside the
box. All 1,168,032 full one-form entries per color are retained; product
sine/cosine transforms implement the full covariance and heat operator.
There is no spectral truncation. The calculation evaluates an unbiased
randomized trace statistic whose expectation is the exact M2 contraction;
its finite sample mean is not an exact evaluation of that expectation.

For 64 shared Gaussian samples, seed 2704, the triplet/shear means are
(-5692.71,-35447.30) for the upper-edge-omitting forest and
(-916.38,-18632.83) for the middle-edge-omitting forest. Sample standard
errors are respectively (422.85,368.49) and (146.87,150.12). Paired
differences are (4776.32,16814.47), with sample standard errors
(315.38,256.75). These suggest forest dependence of both actual
contractions, without a proven confidence guarantee or exact
nonvanishing claim. The original two probes have been tested at one
admitted mesh; no cutoff exponent or logarithmic coefficient is fitted.

The complete coefficient is exactly independent of the forest at fixed
mesh, by equality of the original nonlinear gauge-invariant covariance
and uniqueness of L011's expansion coefficient. Thus every change of
the M2 contraction is exactly compensated by the sum of the remaining
terms. This does not identify the cancellation in any particular
quartic action, paired cubic action, insertion, or flow term.

Outcome: NEGATIVE / RESEARCH / REPRODUCTION. The negative result is the
exact obstruction to forest independence of the isolated density
function, together with evaluated and qualified contraction evidence.
Stop interpreting or extrapolating M2 alone as an invariant coefficient;
retain the full combined-response mechanism. The new finite identities
reproduce covered Gaussian/forest machinery, without a claim beyond the
checked literature. No inconclusive mathematical exploration turn is
spent by this informative negative test; earlier stopped-branch evidence
is retained.

The complete Gamma, including its cutoff logarithm and possible faster
cutoff behavior, remains unevaluated. No reflected-error estimate has
been obtained, compared with the actual required bound <= c_box/2.
Finite matching, physical-boundary subtraction, continuum fields, full
reflection positivity, infrared control and finite positive mass remain
open. STATUS remains IN_PROGRESS with no candidate solution.

The same exact saved TARGET and ready assessment are retained. The
continuation mechanism is to combine the coordinate density with the
quartic and paired cubic action contractions, retain all insertion and
nonlinear-flow terms, and test the complete fixed-mesh sum under the same
forest change before interpreting a logarithm. No new source review or
unassessed hypothesis is introduced by that continuation.

Reproduction commands are recorded in L018 and in the script's help.
The documentation checker and final mathematical/dependency review are
recorded in the dated history entry.
