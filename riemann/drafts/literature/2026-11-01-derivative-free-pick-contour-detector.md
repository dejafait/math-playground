# Residue-based pole detector — completed source review

TARGET: Assess a derivative-free pole detector for F-P on L645's grid, using its unit residue and a zero-avoiding contour instead of evaluation through zeta'(rho).
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the ready finite-Pick/holomorphic-residual assessments; checked L645, C645b/C645c, L018, L467 and the named generalized-Schur and logarithmic-threshold stops. Searched meromorphic interpolation remainder, contour residues, polefinding and meromorphic Schwarz/Blaschke terminology; inspected the primary statements and proof cases below. No exact logarithmic vertical-grid certificate was found in the inspected sources; absence or novelty is not established.
SOURCE_EVIDENCE: Bello Hernández–de la Calle Ysern, arXiv:1211.5573v1, Section 2.3, Theorem 2.2 and Lemma 2.3 with complete proof, pp.5–8; Austin–Kravanja–Trefethen (2014), author revised manuscript, Sections 3.2, 4.1 and full 4.3; Gonek (1984), printed pp.126–127, selected-height paragraph and (16)–(17); Beck et al., A First Course in Complex Analysis, online Section 8.1, Theorems 8.1.5/8.1.7 and proofs. Exact citations and restrictions below.
COMPARISON: Inspected meromorphic approximation results use special rational approximants and a fixed pole budget; contour algorithms use boundary samples. They do not bound F-P for arbitrary n-dependent positive-real P on this vertical grid. The residue theorem retains every enclosed pole and requires a nonsingular boundary. C645c's scalar rate and the generalized-Schur scope stop remain unchanged.
GAP: A derivative-free certificate still needs a zero-avoiding contour, uniform boundary control, and a quantitative noncancellation argument for the weighted sum of all enclosed residues. No inspected theorem supplies these together or makes the old circle admissible. A small pole-cluster cancellation test is an independently testable part of this gap.
REASON: The bounded source review identifies a concrete test but neither proves nor refutes the actual-Xi detector. EXPLORE permits investigation of that stated gap, with no novelty assertion or new theorem approved as true. The narrower continuation has its own exact-target assessment and is subject to separate approval.
SCOPE: Source review of TARGET is complete. Standard residue calculus and previously covered finite-Pick bounds may be cited; no meromorphic error bound, pole separation, residue-sum lower bound or actual matrix sign has been established.

## Original nomination, retained as historical scope

The paragraphs below preserve the invocation-start proposal. Their
REVIEW_REQUIRED status and future-tense source instructions are
superseded by the completed review following them; no second action
or mathematical conclusion is asserted.

Main gap: actual-Xi signs at unbounded heights/all-degree mixed
positivity. The proposed intermediate target is a source assessment of
using F and temporary P directly, replacing evaluation through the
small zeta'(rho) in the old analytic residual by pole-residue information.
A useful later result would be a quantitative finite-grid contradiction
with every contour and growth cost explicit. No contour formula, error
bound or new theorem is derived here. Repeating C645c or adding a
derivative upper bound cannot settle its actual-envelope gap.

Essential inputs: L645's nodes, disk and temporary interpolants;
audited C645b's uniform P control; audited C645c's comparison and its
envelope-direction qualification; L018's completion. The generalized-
Schur source-limit attempt is a contrast, not a mathematical input.
No cross-notebook input. Keep fixed delta in (0,1/2), stipulated simple
rho, and no asserted zero existence. Other zeros, multiplicities and
proximity to a proposed contour are uncontrolled. The old disk may
meet other zeros or have zeros on its boundary; it is not automatically
a valid zero-avoiding contour for F. P may vary with n.

The next turn is literature-only. Search the exact derivative-free
meromorphic interpolation-error question and standard residue/contour
terminology, check duplicates and obstructions in the named Pick
assessments/stops, then inspect primary theorem hypotheses and relevant
proof cases. Reuse unchanged finite-Pick coverage. Bounded holomorphic
division alone does not cover meromorphic F-P. An argument-principle
identity alone does not supply controlled boundary errors. Qualitative
safe-sampling or index results are not quantitative logarithmic-grid
certificates without additional estimates.

Continue toward a separately gated mathematical test only if the
comparison identifies checkable hypotheses and estimates, or a precise
bounded gap with a discriminating test. Abandon if necessary contour
costs simply hide the missing derivative lower bound, uncontrolled
close zeros or target-equivalent positivity. Record a source limit
rather than assuming the contour or classifying the proposal creative.
Matching Mathlib coverage is not checked. No ready assessment or new
mathematics is claimed by this nomination. The q_delta, completed-norm
and reserve stops remain preserved in their original scopes.

LITERATURE_REASON: The residue/meromorphic-contour proposal changes the assessed holomorphic residual. This turn inspected the previously unread quantitative hypotheses and obstruction comparisons; further unchanged source review is unnecessary beyond the supervisor's separate continuation approval.

## Completed comparison — 1 November 2026

This was one literature-only step. The main gap is still actual-Xi signs
at unbounded heights/all-degree mixed positivity. The intermediate target
was the exact TARGET above. A quantitative meromorphic detector could
avoid the derivative normalization in L645/C645b, but would still need
independent matrix positivity to exclude an actual zero. No new contour
identity, estimate, lemma or mathematical script was produced here.

### Primary quantitative meromorphic comparison

M. Bello Hernández and B. de la Calle Ysern, *Meromorphic continuation of
functions and arbitrary distribution of interpolation points*,
[arXiv:1211.5573v1](https://arxiv.org/pdf/1211.5573v1),
23 November 2012, Section 2.3, Theorem 2.2 and Lemma 2.3, pp.5–8.
Read the definitions, hypotheses, excluded sets and complete lemma proof.
Multipoint Padé approximants have prescribed numerator/denominator
degree bounds; the interpolation-point measures converge weakly.
Theorem 2.2 assumes exactly m poles in the designated meromorphy domain
and gives pole convergence and geometric convergence off those poles.
Lemma 2.3 removes small neighborhoods of poles and denominator zeros.
Its proof clears all poles and obtains (12), with an n^(2m) factor,
an interpolation-polynomial ratio, and a constant depending on the
fixed function, contour and exclusion parameters. Here m is fixed.

This does not cover arbitrary positive-real P, nor uniformity as the
height and local pole count grow. Its contour estimate cannot be
transferred to F-P merely because the data interpolate. This is scope
evidence, not an assertion that every meromorphic approximation method
must pay precisely that factor. No theorem is imported into PROOF.md.

### Contour polefinding and conditioning

A. P. Austin, P. Kravanja and L. N. Trefethen, *Numerical algorithms based
on analytic function values at roots of unity*, SIAM J. Numer. Anal.
**52** (2014), 1795–1821,
[author revised manuscript](https://people.maths.ox.ac.uk/trefethen/austin_kravanja_trefethen_revised.pdf),
Sections 3.2, 4.1 and complete 4.3, manuscript pp.14–17. Section 4 assumes
meromorphy in a disk larger than the unit disk, with exactly K poles,
all inside the unit disk; samples lie at roots of unity. Section 4.3
derives equivalence of its linearized rational interpolation and
discrete contour moment construction. The resulting bilinear form is
explicitly not a positive definite Hermitian inner product. The preceding
discussion notes possible ill-conditioning, including nearly equal zeros.

These algorithms neither sample our interior vertical segment nor give
a uniform actual-Xi logarithmic-grid sign. The unit-residue setting
could remove one conditioning issue; that alone is not the theorem's
error analysis. Trefethen's December 2019 *Complex Computing* notes,
Sections 1.2.6–1.2.7, were used only to locate this primary paper, not
as an additional quantitative theorem.

### Boundary and residue hypotheses

S. M. Gonek, *Mean values of the Riemann zeta-function and its
derivatives*, Invent. Math. **75** (1984), 123–141,
[author-hosted published PDF](https://sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf),
Section 2, printed pp.126–127. Read the selected-height construction,
local partial-fraction statement, (16), completion identity (17), and
following completed-function bound. The O(log^2 T) estimate in (16),
uniform for -1<sigma<=2, applies to the selected heights that avoid
zero ordinates; it is not a bound on our prescribed circle. The local
formula keeps nearby zero terms. It may support a later clearance
argument, but that argument and its constants remain unproved here.
Reuse audited C645b's uniform P bound and completion estimate only in
their stated domains. L467 supplies a multiplicity-counted shell upper
bound, not a minimum spacing or circle-clearance theorem.

M. Beck et al., *A First Course in Complex Analysis*,
[online Section 8.1](https://complexanalysis.org/web/sec_residue-thm.html),
Theorems 8.1.5 and 8.1.7, accessed 1 November 2026, unversioned.
Read both statements and proofs, including the finite disjoint small
circles in the residue theorem and the simple-pole limit rule. A simple
positively oriented contour must avoid all singularities, and the
integral sums all enclosed residues. This supplies standard calculus,
not a boundary norm or a lower bound for a complex weighted sum.
Reproving this named theorem would add nothing; a later attempt should
justify only its particular meromorphic integrand and contour.

### Duplicates, failure checks and bounded continuation

The local search for pole-clearing, residue cancellation and Pick/contour
work in the relevant 1 November assessments/stops found no completed
test of the proposed small cluster. Reused L645's finite interpolation
coverage and checked its residual proof through (6); checked C645b's
uniformity argument and C645c's qualified conclusion. The generalized-
Schur index import supplies no actual-Xi sign. C645a's completed-growth
stop, C645b's factorwise stop and C644a's reserve stop are preserved;
none rules out a changed residue mechanism. No cross-notebook input.

Three source-level options were compared: importing meromorphic Padé
convergence (different approximants and nonuniform pole budget), using
boundary polefinding algorithms (different samples), and testing a
cluster residue certificate with the existing grid factors. Only the
last leaves a small independent mathematical test without claiming the
source already supplies the detector. It does not yet solve contour
clearance or actual boundary control.

The new exact-target assessment is
[the cluster test](2026-11-01-pick-cluster-residue-cancellation.md).
It defines a finite family and a proposed normalized sum, not a derived
certificate. A certified exact cancellation family would stop the
universal residue-noncancellation shortcut, even with a safe boundary.
A positive lower bound would justify investigating larger clusters and
actual contour costs separately. Failure of a toy model is not a
counterexample to actual Xi, and success for three poles is not control
of every enclosed zero. No mathematical test was run in this review.

Queries included `meromorphic function interpolation remainder contour
integral Blaschke product poles quantitative`, `Nevanlinna Pick
meromorphic interpolation logarithmic derivative residue finite sampling
pole detection`, `meromorphic Schwarz lemma zeros poles finite Blaschke
product bound contour`, `zeta logarithmic derivative avoiding zeros O log
squared T lemma circle`, and `meromorphic interpolation remainder contour
residues Gonchar multipoint rational interpolants`. Searches are bounded
overlap evidence, not novelty certification. Search leads on meromorphic
Riemann–Hilbert factorization and Mathlib canonical decomposition were
not inspected in their needed proof cases and are not inputs. An EMIS
follow-up timed out twice; the lead is nonessential. No persistent source
blocker is claimed. Full matching Mathlib coverage is unchecked; the
existing Borel–Caratheodory support remains as recorded in L645.

The source outcome is EXPLORATION: no actual-Xi certificate was obtained
or refuted. The resulting narrower, ready-in-scope nomination requires
the supervisor's separate approval before research. This completes the
saved source target; it does not approve newly derived mathematics.
