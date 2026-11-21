# Periodic potential radial graphs — completed source comparison

TARGET: Determine whether L847's actual r=2,k=1 form admits a smooth periodic radial graph u=b+grad(phi), with b in R^2 and phi real and 2pi-periodic, whose full oriented pullback is real and nonnegative everywhere, retaining every zero of F.
CHECKED: 2026-11-07
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded periodic-potential, prescribed-phase, Bernstein-rigidity, vanishing-volume-form and negative-ray searches completed; exact queries and targeted local duplicate/failure checks below. No matching global actual-G theorem inspected; search failure is not novelty evidence.
SOURCE_EVIDENCE: Yuan arXiv:math/0201186v1 equation(1.1), Theorems1.1-1.3 pp1-2 and Lemma2.1/proof pp3-4; Collins-Picard-Wu arXiv:1607.07194v1 equation(1.2), Theorem1.1 pp1-2 and Section3.4 pp17-18; Auroux author manuscript slaginvol.pdf Section2.2 pp4-5, Definition2.1/Proposition2.2 and weighted deformation identities. Reuse the recorded Lotay-Pacini and Delay/Teixeira comparisons at unchanged hypotheses.
COMPARISON: Bernstein rigidity assumes a Euclidean minimal gradient graph, while the Dirichlet theorem assumes prescribed phase, a subsolution and boundary data. Auroux deforms an existing special Lagrangian in a nonvanishing-form complement. None supplies the variable actual-G problem across its zero divisor. Product, vector-patch and compatible-period results do not decide the potential subclass.
GAP: Existence and nonexistence both remain open. No minimality, scalar global phase branch, subsolution, positive seed, divisor estimate or all-degree transfer is supplied. A narrower negative-ray incidence test is separately prepared; its proposed obstruction bridge remains to be proved.
REASON: Source comparison rules out the proposed automatic rigidity/existence imports at their stated hypotheses, without proving nonexistence. Recovery selects a different, independently testable global phase-range mechanism instead of another weak-defect attempt or a general existence search.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target introduced the global scalar-potential constraint, outside the ready vector-patch and calibration coverage; primary prescribed-phase and rigidity hypotheses were essential unread inputs.
SCOPE: Exactly TARGET with arbitrary constant b, smooth real periodic phi and L847's unchanged G,R,C,F, orientation and zeros. This turn derives no specialization or lemma. The narrower continuation in 2026-11-07-potential-negative-ray-incidence.md is newly ready and requires separate next-turn approval.

## Completed comparison, step87

The main gap is L030-L032/C032a all-degree actual-Xi mixed positivity.
The reviewed intermediate target is a fixed r=2,k=1 potential contour.
Success could support a later contour mechanism; even a valid contour
would leave growing orders, other shifts and positivity transfer open.
This source review establishes neither a contour nor its impossibility.

### Primary hypotheses and essential proof cases

Yu Yuan, *A Bernstein problem for special Lagrangian equations*,
[arXiv:math/0201186v1, 20 January 2002](https://arxiv.org/pdf/math/0201186),
equation(1.1) and Theorems1.1-1.3, pp1-2, concern entire smooth
Euclidean minimal gradient graphs. The first theorem assumes convexity;
the second a small dimensional lower Hessian bound; the third is
three-dimensional with a finite lower bound. The opening determinant
description gives the standard Hessian eigenvalue phase. Lemma2.1 and
its complete proof, pp3-4, explicitly use the minimal surface equation
to eliminate fourth derivatives. Thus periodicity and bounded Hessian
alone do not license its rigidity argument here: Euclidean minimality
or constant phase for the flat volume form has not been supplied.
No Bernstein theorem is imported for actual G, and no replacement
subharmonicity calculation is performed.

Tristan C. Collins, Sebastien Picard and Xuan Wu, *Concavity of the
Lagrangian Phase Operator and Applications*,
[arXiv:1607.07194v1, 25 July 2016](https://arxiv.org/pdf/1607.07194),
equation(1.2)/Theorem1.1, pp1-2: a bounded C4 real domain, C4 boundary
data, prescribed C2 h taking values in
[(n-2)pi/2+delta,n*pi/2), delta>0, and a C4 subsolution in the sense
of (1.3), with the same boundary values, yield a unique C^(3,alpha)
solution, smooth for smooth data. Section3.4, pp17-18, was read through
the continuity path, openness, closedness, uniqueness and nonsmooth-data
limit. The path starts at the supplied subsolution and preserves the
phase margin. This is not a periodic theorem with unknown gradient-
dependent phase. Neither its data, branch nor subsolution is supplied
by F(Phi_u), especially at F=0. No conclusion is imported for G.
The PDF text's inequality glyphs are ambiguous; use the exact source
(1.3), not an inferred strict-subsolution requirement. A screenshot
request returned no readable image and counts as no additional evidence.

Denis Auroux, *Special Lagrangian fibrations, mirror symmetry and
Calabi-Yau double covers*, Astérisque321 (2008), 99-128,
[27-page author manuscript, Section2.2, pp4-5](https://people.math.harvard.edu/~auroux/papers/slaginvol.pdf#page=4),
Definition2.1/Proposition2.2: the ambient form is nonvanishing on the
divisor complement and the initial special Lagrangian already exists.
Read the closed-alpha/closed-beta deformation conditions and positive
weight psi. They do not construct an initial graph or cover zero weight.
The proposition attributes unobstructedness to McLean and other work;
their original proofs are not newly inspected or imported. This reuses
the existing local assessment, adding no repeated access attempt.

These sources are compared at their inspected versions; equality with
later journal versions is not asserted. No essential source is blocked
for the bounded continuation. Full matching Mathlib coverage is unchecked.

### Local evidence and three mechanisms compared

Read L847's actual form, full determinant, graph homotopy and product
proof ranges; its periodic-moment discussion supplies no global
potential. C858a's argument calculation uses prescribed exchange/collar
data and yields compatible periods, not an obstruction. L863 requires
an independently invertible flux matrix and permits arbitrary vector
variations; its solver need not return a gradient. Reuse the ready
Lotay-Pacini comparison in 2026-11-06-actual-g-radial-graph-full-phase.md
and Delay/Teixeira in 2026-11-06-full-phase-elliptic-deformation-scope.md.
Do not repeat L874's completed audit or the patch inverse.

1. **Flat special-Lagrangian rigidity:** park automatic import because
   the required Euclidean minimality/flat constant phase is unavailable.
2. **Prescribed-phase elliptic existence:** park automatic import because
   a branch, subsolution and periodic/global divisor treatment are missing.
3. **Symmetric-Hessian phase range and density ray incidence:** select
   a necessary-condition obstruction test instead of solving the PDE.
   The precise question is whether every allowed potential graph hits
   F in the strictly negative real ray at some point. This is not proved
   by the sources or by the compatible-period calculation. The proposed
   implication from such a hit to failure of q>=0 must itself be checked
   from the standard determinant phase in a later research turn.

The third mechanism is different from L893's weak dual-defect rigidity:
it concerns the image of the actual holomorphic coefficient on a global
integrable graph, with no calibration coefficients or saturation trace.
The exhausted route remains parked with its original evidence in
ATTEMPTS/2026-11-07-actual-fiber-mixed-compatibility-inconclusive-86.md.
The new comparison does not reset its 3/3 mathematical exploration use.

### Search record and bounded continuation

Queries issued included `periodic special Lagrangian potential equation
torus variable phase holomorphic volume form zeros existence`,
`Yuan Bernstein special Lagrangian 2002 theorem dimension two`,
`site.arxiv.org Collins Picard Wu Lagrangian phase equation Dirichlet
problem theorem subsolution`, `"holomorphic" "gradient graph" "phase"
torus`, `"special Lagrangian" "vanishing" "periodic" potential`,
`"holomorphic" "torus" "gradient" "negative real axis"`,
`"perfect contour" "negative real" zeros`, and
`"G(z1)" "G(z2)" "radial" graph positivity`.
The local search used only the named graph/phase literature, L847-L894
and November6-7 failure records for potential, Hessian, Maslov, scalar
phase, negative-ray and slit-plane claims. It found the existing
principal-log input and collar-period test, not a matching incidence
result. Search snippets, aggregators and the newer tropical/K3 leads
were not read as theorem evidence and are not used.

The exact new test, its continuation/abandonment threshold and all
remaining hypotheses are in
[the negative-ray assessment](2026-11-07-potential-negative-ray-incidence.md).
A strict negative-ray hit must have F!=0; a zero or a phase limit alone
is insufficient. A ray-avoiding graph would retire this universal
incidence mechanism without being a nonnegative full-pullback contour.
No mathematics, lemma, script, DAG edge or PROOF argument changed.

## Original nomination, preserved as historical scope

## Proposed object and downstream purpose

Use L847's fixed full form, with the same positive R,C and entire G.
The prospective graph is z_j=R*exp(u_j(y)+i*y_j), where
u=b+grad(phi), b is a constant real two-vector, and phi is a smooth
real function periodic in both angular coordinates. The required
quantity is the complete L847 pullback
Q=F(Phi_u)*det(I-iDu), real and nonnegative at every point.
No global graph of this type is supplied. No exchange symmetry,
prescribed collar, smallness, convexity, zero-free image or nonzero
pullback is added. The constant b prevents an unintended zero-mean
restriction on the radial displacement.

The main gap remains L030–L032/C032a all-degree mixed positivity.
This source review asks whether the potential constraint gives a
usable global existence or obstruction theorem for a structured
coupled contour class. A positive answer would only supply a fixed
r=2,k=1 mechanism; the corresponding finite sign is not being claimed
as a new discovery. A negative answer would remove this subclass.
Either outcome leaves all-degree construction/transfer and RH open.

The new issue is integrability through one periodic scalar potential,
not another local extension of L893's dual coefficients. Do not assume
the restricted phase operator is elliptic or that a supported vector
right inverse returns a gradient. Do not derive such a statement during
this nomination or its literature-only approval turn.

## Reuse and duplicate boundaries

The original graph assessment records Lotay–Pacini's global nonzero
unit (n,0)-form hypotheses and its constant-phase/calibration statements,
which do not construct submanifolds. Those qualifications remain.
L847's full F has zeros; a theorem on its complement does not settle
the requested global problem.

L863 concerns a fixed compact off-divisor patch, an independently
assumed invertible actual flux matrix, zero-integral supported sources
and arbitrary vector variations. Its divergence solver and norm bound
do not resolve the scalar-potential constraint, a global seed or the
divisor. Reuse that assessment rather than repeat its linear calculation.
L862's open-ample failure remains; the nomination does not claim that a
change of unknown removes it.

C858a's logarithmic-frame periods already vanish under its special
exchange/collar assumptions, with compatible ambient periods. Merely
recomputing those integers supplies no new obstruction. L874's finite
heat identities were independently audited in history step11; a second
audit without new evidence was rejected as a duplicate during routing.
The stopped theta-score sign is not revived by this nomination.

The local weak-calibration results and failures L887–L894, including
the new L893 necessary conditions, remain independent comparisons.
No conclusion about a stationary graph's existence is assumed from
them. No cross-notebook result is requested.

## Source-review discriminator

First inspect primary existence/rigidity theorem hypotheses and the
essential proof cases for prescribed-phase or special-Lagrangian
periodic potential graphs, including any ambient-volume, exactness,
phase-range, ellipticity and divisor assumptions. Reuse the recorded
comparisons only within their actual scopes. A theorem requiring a
preexisting calibrated graph, an unknown global sign, a nonvanishing
volume form or a divisor-free image must be labeled accordingly.

Continue only if a matching import or a concrete bounded mathematical
test for this exact potential subclass survives that comparison.
If no adequate theorem or independently testable mechanism is found,
record the bounded negative source evidence and choose another target;
do not default to the exhausted weak-defect problem or repeat patch
inversion. Any changed subtarget needs its own explicit coverage.
Mathlib coverage has not been checked, with no absence claim.
