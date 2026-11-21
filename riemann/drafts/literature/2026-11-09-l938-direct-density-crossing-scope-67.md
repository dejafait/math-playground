# Direct actual-density crossing — completed method comparison

TARGET: Seek a direct full-kernel interval certificate that v'(E)>0 at every zero of L938's actual density on 1/4<=E<=4, using simultaneous enclosures of v and v'.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step68 checked exact-object signed-convolution/crossing queries and validated integration, endpoint-singularity and interval-root terminology; inspected the primary sources and local duplicate/failure ranges recorded in 2026-11-09-l938-direct-density-source-notes-68.md. No inspected source supplies the actual crossing sign; a failed search is not novelty evidence.
SOURCE_EVIDENCE: Johansson, arXiv:1802.07942v1, Sections2/2.1/3.2 pp2-4,6, https://arxiv.org/pdf/1802.07942v1 ; FLINT v3.3.1 arb_calc root-isolation contract, https://raw.githubusercontent.com/flintlib/flint/v3.3.1/doc/source/arb_calc.rst and complete isolation implementation https://raw.githubusercontent.com/flintlib/flint/v3.3.1/src/arb_calc/isolate_roots.c ; DLMF18.9.21 https://dlmf.nist.gov/18.9#E21 , 18.14.4 https://dlmf.nist.gov/18.14#E4 and Cauchy derivative formula1.9.31 https://dlmf.nist.gov/1.9#E31 . Reuse L938's exact beta integration and the step46 Laplace assessment only within their existing scope.
COMPARISON: Validated inclusion and exclusion are known methods, not actual-theta crossing theorems. Singular eleven-dimensional integration is not covered automatically by a univariate Petras call. L938 already integrates its polynomial replacement exactly; new pointwise and first-derivative error bounds, preserving the signed finite algebra, are the application difference. L942/L943 do not decide it.
GAP: Produce justified whole-interval enclosures for the full actual v and v', including analytic interpolation, coefficient-rounding, derivative and twelve-factor errors. The existing cell-mass bound cannot be differentiated. No sign margin, numerical feasibility or coverage certificate is established in this literature turn.
REASON: Essential method coverage is now available for one fixed-budget known-method specialization, subject to separate approval of this newly completed scope. Its actual crossing conclusion remains open; no general theorem is to be reproved.
LITERATURE_REASON: The startup REVIEW_REQUIRED gate concerns a changed direct-integral mechanism; existing divergence and cell-mass assessments do not cover simultaneous pointwise/derivative inclusion.
SCOPE: Exactly TARGET, full L938 normalization, E in [1/4,4]. One later REPRODUCTION attempt using the existing degree256 polynomial and exact beta-integrated coefficients; no new fit, theta cutoff, interpolation degree or precision campaign. At most depth12 dyadic subdivisions from the whole closed interval and 8191 examined intervals; unresolved leaves remain unresolved. Detailed obligations and stop conditions are in the step68 source notes. Separate next-turn approval is required before research.

## Initial step67 nomination, retained as historical scope

The following nomination preceded the completed comparison above. Its
requests for a future source review are superseded by step68; its
mathematical limitations remain in force.

The main gap remains L030–L032/C032a actual-Xi all-degree mixed
positivity. This target addresses only compact-energy upward crossings
of the fixed H2 density. Other energies, contacts, degrees, parameter
endpoint signs, initialization, realization and continuation remain open.

Essential prospective inputs: L019; L938's complete 34 rows, twelve
factors, factorials, M_0^12 and analytic k; L940(1)'s exact averaging;
L942(3)-(4)'s derivative identity, still awaiting independent audit.
The step46 Laplace assessment may cover downstream use but must not be
mistaken for a ready assessment of the new enclosure method. No
cross-notebook theorem is nominated. Full/supporting Mathlib coverage
for the prospective direct certificate is unchecked.

A later source-only turn should compare exact target statements and
primary hypotheses with existing certified methods and recorded local
failure evidence. The desired future bounded test would cover each
compact subinterval by a rigorous nonzero sign enclosure for v or by a
strict positive enclosure for v' wherever v=0 remains possible. It
must pay full-kernel approximation errors and signed cancellation.
This is a proposed test, not a derived certificate or approved algorithm.
Numerical quadrature signs and the old signed cell masses are not
pointwise or derivative enclosures. Abandon a proposed implementation
if its actual/required error comparison cannot certify either sign;
do not enlarge energy range or claim all-degree positivity.
