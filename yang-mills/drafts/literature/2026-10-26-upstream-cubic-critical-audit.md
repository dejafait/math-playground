# Upstream cubic critical audit — completed source-scope comparison

TARGET: Critically audit L286–L290's upstream cubic estimates and asymptotics, including the Wilson jet, finite-range errors, bulk normalization and complete source sums.
CHECKED: 2026-10-26
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the complete-cubic, quartic-audit and distinct-line-audit searches; compared L286–L290 hypotheses, conclusions, relevant proof cases and Mathlib qualifications with those assessments, histories 504–508 and ATTEMPTS/047–049. No separate upstream audit or matching complete theorem was located in these selected paths; no new broad search or novelty claim.
SOURCE_EVIDENCE: Reused the recorded primary readings of Luescher–Weisz hep-lat/9502017v2 sections 3.1–3.3, 4.1–4.2 and Appendix C.1; Bode–Weisz–Wolff hep-lat/9809175v1 sections 2–3; Benzi–Razouk ETNA 28 section 3.5, Theorem 3.4 and proof; Dowker 1207.2096v2 sections 7–8; and the scalar/quotient sources detailed below. No external theorem was newly read or imported this turn.
COMPARISON: The inspected source scope supplies supporting scalar formulas, finite-dimensional extraction and polynomial locality, not the full relative transverse estimates, positive-splitting error, weighted trace sums or Wilson constants in L286–L290. Their written finite proofs can be independently audited without an essential unread theorem; L291's conditional acceptance supplies no upstream verification.
GAP: Audit the exact Wilson jet, full separated pair and external tail, uniform positive-covariance operator error, strong-field/boundary passage, bulk tensor factors and complete weighted source sums. All five proofs remain unverified by this literature comparison; their inherited analytic qualifications remain in force.
REASON: Approve one later RESEARCH / REPRODUCTION conceptual audit on exactly TARGET, using the reused source scope and explicit local estimates. This approves scrutiny rather than the mathematical claims. Stop dependent work for a separate source review if an essential additional theorem is needed.
LITERATURE_REASON: The newly combined upstream audit was registered REVIEW_REQUIRED; its five proof obligations required comparison with the existing narrower assessments. Adequate primary coverage is reused rather than refreshed by repeated browsing.
SCOPE: Exactly TARGET for SU(2), even N>=2, a=8/N, the all-face relative cube, boundary-contained pins, boundary-fixed gauges, every normal link, all colors and source orders, L002's exact product bump and L280's real source domain. All Wilson jets remain on L280's own slice; no stronger rate, higher remainder or continuum assertion.
COVERED_TARGET: Critically audit L286–L290's upstream cubic estimates and asymptotics, including the Wilson jet, finite-range errors, bulk normalization and complete source sums.

## Intended use and bounded test

The main gap remains an interacting continuum theory with nonzero
physical sector and finite positive mass for every compact simple group.
The intermediate target is
independent acceptance or a precise failure of the upstream estimates
on which L291's accepted conditional cancellation depends. This could
make the complete quadratic-scale comparison dependable for later
subleading work. It cannot establish the interacting lower bound.

Essential existing inputs outside the audit target are L003, L279,
L280, L281, L282, L283, L284 and L285, with the exact product bump
from L002 through them. Each must retain its hypotheses and any
unresolved analytic qualifications. Do not promote L291's conditional
acceptance into an upstream verification or use it circularly to prove
L286–L290. The finite Gaussian and local matrix ingredients examined
inside L291's audit do not by themselves verify the full source sums
and all conclusions of those five lemmas.

The official target version recorded in `foundations/01-target-and-scope.md`
is reused; no new route or cross-notebook input is selected. The exact
source domain is (|s|+|t|)||f_*||_infinity<eta<1, with derivatives at
zero. The nonnegative product sources have supports
[-1/4,1/4]^3 times [1,2] and [-2,-1]. Matrices use counting measure;
there is no additional a^4 in the plaquette sums and no nonlinear
transport from a forest slice.

## Primary coverage reused and its limits

The [complete-cubic assessment](2026-10-26-complete-cubic-quadratic-asymptotic.md)
contains the exact-target searches and versioned primary readings:
M. Luescher and P. Weisz, *Coordinate space methods for the evaluation
of Feynman diagrams in lattice field theories*, Nucl. Phys. B **445**
(1995), 429–450, [hep-lat/9502017v2](https://arxiv.org/pdf/hep-lat/9502017v2),
23 February 1995, sections 3.1–3.3, 4.1–4.2 and Appendix C.1,
printed pp. 6–14, 22–23. The scalar infinite-lattice subtraction
examples do not prove uniform relative-box transverse vertex sums.
The harmonic-polynomial zeta representation retains its convergence
restriction, and section 4's remainder convention allows logarithms.
Neither supplies the required complete o(N^2) error here.

A. Bode, P. Weisz and U. Wolff, *Two-loop computation of the
Schrödinger functional in pure SU(3) lattice gauge theory*, Nucl.
Phys. B **540** (1999), 491–499,
[hep-lat/9809175v1](https://arxiv.org/pdf/hep-lat/9809175v1),
25 September 1998, sections 2–3, pp. 2–7, computes diagrams in a
spatially periodic, temporally Dirichlet slab with boundary-field
derivatives and numerically extracted asymptotics. Its group,
background, geometry and observable differ. Its three-propagator
diagram is relevant organization, not a rigorous error theorem for
our complete sums. The uninspected SU(2) calculation referenced there
and original all-orders power-counting papers remain leads, not premises.

The [quartic audit coverage](2026-10-26-complete-quartic-critical-audit.md)
and [distinct-line audit coverage](2026-10-26-distinct-line-cancellation-critical-audit.md)
record the full proof cases of M. Benzi and N. Razouk, *Decay bounds
and O(n) algorithms for approximating functions of sparse matrices*,
ETNA **28** (2007), 16–39,
[section 3.5, pp. 24–25](https://etna.ricam.oeaw.ac.at/vol.28.2007-2008/pp16-39.dir/pp16-39.pdf).
The graph-power argument gives polynomial locality. Theorem 3.4
requires diagonalizability, a spectrum in its continuum F and
analyticity on the specified enclosing domain; its estimate retains
the eigenvector condition number. The proof treats off-diagonal and
diagonal entries, with a unitary eigenbasis in the normal case.
It does not give uniform inverse approximation as the spectral gap
closes. In particular it cannot replace L288's residual diagonal
estimates or its complete two-vertex operator comparison. Those are
explicit audit obligations, not corollaries of analytic decay.

The same assessments reuse J. S. Dowker,
[1207.2096v2](https://arxiv.org/pdf/1207.2096v2), sections 7–8,
(29)–(37), pp. 10–13, for scalar Dirichlet and shifted Neumann
interval conventions, including the Neumann constant mode. Lawler
and Limic, *Random Walk: A Modern Introduction* (2010), Theorem 4.3.1
and Proposition 4.6.2(a), concern transient scalar Green functions
and exit subtraction. Michta–Slade, ALEA **19** (2022), Theorem
1.3(ii), requires d>2q in the massless case, excluding the bare
d=4,q=2 shortcut. None is a projected inverse-square or weighted
relative-box summation theorem. L286 and L290 instead write the
finite time-mode estimates to be checked, with exact endpoint and
normalization conventions from their local inputs.

The quotient/extraction source scope is unchanged: the assessments
for L279/L280 retain Kirwin, [0810.1700v2](https://arxiv.org/pdf/0810.1700v2),
Theorem 2.1, for fixed-dimensional Laplace extraction, not a
mesh-uniform higher remainder. The bulk BRS and single-integral
power-counting sources compared in the complete-cubic assessment
likewise do not identify this isolated local-source response.
No new import, reproof of a known scalar theorem or renormalization
claim is authorized by this comparison. Full and supporting Mathlib
coverage remains **not checked**; unknown coverage is not absence.

## Comparison with the five written proofs

L286 sections 1–3 write a finite four-slot SU(2) jet verification,
then the full longitudinal subtraction and differentiated time Green
function on separated supports. The later audit must check the
claimed O_f(1) complete pair estimate, not only the curl identity or
a fixed-mode kernel. Its inverse-square appearance does not require
the excluded massless full-space theorem: the proof uses a finite
spectral derivative before its exponentially weighted mode sum.
Whether that derivation and all contractions succeed remains open here.

L287 sections 1–4 use the complete curl projection, distinct field
colors, bounded repeated-slot multiplicity and a displayed positive
Schur-product inequality. Their source sandwich retains both orders
and the complete external-mode tail. These are finite matrix/Gaussian
arguments within existing coverage, rather than an unread kernel
theorem. The O_f(N^2) bound, O_f(N sqrt(log(eN))+log(eN)) reduction
error, and the uniform discarded-mode bound all require separate
verification; no pointwise estimate alone supplies them.

L288 sections 1–4 use an independent Gaussian splitting with
covariances widehat G and R=G-widehat G, unlike L291's correlated
common-noise construction. Its stated O((m+1)^-1) whole-operator
and normalized source errors depend on both residual diagonals,
including the stronger curl diagonal, the retained operator bound
and conditional centering. All are written as finite estimates.
Polynomial locality supplies only fixed-m range and bulk agreement;
it does not supply these errors or dispose of a boundary layer.

L289 sections 1–4 explicitly compute the full-action bulk tensor,
then use the uniform approximation before the fixed-range boundary
limit, strong source fields and the complete external tail. Its
24 I_1 tensor and (9 I_1/16) S_f group coefficient are audit targets,
including real Fourier/color factors and counting-to-physical
normalization. The identity I_1=Z_0/2-1/16 has its own punctured-domain
argument in (16); scalar Z_0 citations alone do not establish its
application or the subtotal. No homogenization or boundary-trace
theorem is silently imported by this scope approval.

L290 sections 1–5 write separated rank-one nuclear-norm sums,
fully summed external-curl errors, a weighted independent-splitting
comparison and a restricted 12-plaquette bulk tensor. A positive
unweighted operator bound does not by itself give its nonsymmetric
weighted estimate. Check its left support restriction, full action
domain, factor 8 I_1, complete product Riemann sum and both original
-1/2 prefactors. Each claimed limit -3 I_1 J_f/16 and their combined
subtotal remain unverified in this literature step.

These comparisons concern applicability and proof obligations only.
They do not independently establish any of the five estimates or
validate cancellation at N^2 scale. Ordinary finite Gaussian pairing,
spectral decomposition and singular-value inequalities are already
explicit in the local inputs; no essential unread theorem was identified
for checking the written arguments. A later need for a stronger theorem
would require a separate assessment before its use.

## Duplicates, failures and decision test

Histories 504–508 record the successive derivations and explicitly
leave their separate audits outstanding. The selected proof ranges
and ready assessments locate no completed combined upstream audit.
This is a bounded notebook-local duplicate comparison, not a search
of sibling notebooks or a claim of originality.

ATTEMPTS/047 preserves the uncontrolled forest expectation after
integration by parts; 048 the inadequate global absolute-norm bound;
049 a nonlocal comparison showing that generic gauge identities do
not force Wilson cancellation. The present finite relative-box
estimates must be scrutinized on their Wilson-specific content. They
must not be replaced by any of those stopped arguments. Their stops
do not prohibit this audit or constitute Yang–Mills counterexamples.

Continue with one conceptual audit of exactly TARGET. Accept a claim
only after its full stated error, constants, endpoint cases, boundary
control and complete source sums have been checked with inherited
qualifications explicit. Otherwise isolate the first failed assertion
and the concrete repair threshold, preserving the derivation. Neither
boundedness, a formal bulk tensor nor L291's conditional acceptance
suffices. An essential unread source requires a separate literature
gate before dependent proof work; no such blocker is identified now.

Completed outcome EXPLORATION, kind LITERATURE, classification
NOVELTY_UNCHECKED, actual task literature_comparison. This separate
comparison supersedes the registration's REVIEW_REQUIRED decision
and approves only a later audit. No lemma, mathematical script, DAG
edge or PROOF.md argument changes. Mathematical exploration usage is
zero; no supervisor counter reset is claimed. No justified creative
target is independently prepared while these essential upstream
claims await scrutiny. STATUS remains IN_PROGRESS.
