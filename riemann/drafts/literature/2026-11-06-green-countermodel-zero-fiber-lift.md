# Proposed stronger zero-fiber closure-lift test

TARGET: Review whether L869's prescribed h admits a global C1 closure lift q,r vanishing on one actual G-zero fiber, allowing all homogeneous modes and zero modes.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded exact-system, periodic inhomogeneous Cauchy-Riemann, prescribed-trace and hyperplane-extension searches; compared the named local stops and inspected the primary statements/proof cases listed below. No matching fixed-h global C1 lift or obstruction theorem was located; no novelty inference.
SOURCE_EVIDENCE: Reuse Engel-Nagel (2000), VI.4.1 pp384-386; Lebl, Notes on Diffy Qs, Theorem2.2.1(1)/Example2.2.1; Grafakos (2014), Corollary3.2.2 and corrected approximate-identity input; and the assessed Hardy input in C868b. Newly inspected Lebl, Tasty Bits of Several Complex Variables, v4.4 (31 May2026), Definition1.1.2/Proposition1.1.3 pp14-16, Theorem4.2.1/proof pp132-134, Theorem4.4.5 statement p141, Theorem4.5.3/proof pp147-148, https://www.jirka.org/scv/scv.pdf . Scope and exclusions below.
COMPARISON: Scalar ODE freedom and compact Fourier traces are covered. General smooth dbar existence or extension of already holomorphic hyperplane data does not settle simultaneous prescribed forcing and zero trace in this C1 periodic problem. L869 does not realize q,r; C868a/C868b give necessary restrictions only. No known import inspected decides the fixed-h test.
GAP: Construct a global C1 closure lift of L869's fixed h with the chosen fiber trace, or prove an obstruction valid against every homogeneous mode and compatible zero mode. Neither conclusion is asserted; full actual-F admissibility and the sharp period bound remain outside this test.
REASON: Essential elementary ODE/Fourier inputs are reusable and the added existence/trace theorem comparison is complete for one bounded test. EXPLORE authorizes a later attempt after separate approval, not a lift theorem, source-regularity extension or novelty claim in this literature turn.
LITERATURE_REASON: Changed hypotheses add simultaneous global closure realization and pointwise zero-fiber traces absent from the abstract-package test; reuse old inputs rather than repeat their searches.
SCOPE: Exactly the fixed L869 h, H>0, actual Hardy-zero a and corresponding ell,phi of C868b, real global C1 angularly periodic q,r satisfying both displayed closure equations and the one displayed fiber trace; all homogeneous and compatible zero modes allowed; no growth, bandwidth, domination, diagonal, period or graph assumption added.
COVERED_TARGET: Test whether L869's prescribed h admits a global C1 closure lift q,r vanishing on one actual G-zero fiber, allowing all homogeneous modes and zero modes.

## Exact nomination and scope boundary

Inputs are L869's fixed finite-mode h, C868a's closure/profile
interface and C868b's chosen actual Hardy zero a of G. Fix the
corresponding ell=log(|a|/R) and phi=arg(a), and H>0 in L869.
Ask whether real, globally C1, angularly periodic q,r can satisfy

\[
 r_{x_j}=q_{y_j},\qquad (q+h)_{x_j}=-r_{y_j}\quad(j=1,2),
 \qquad q((\ell,s),(\phi,v))=r((\ell,s),(\phi,v))=0
 \quad(s,v\in\mathbb R).
\]

The displayed conditions define the proposed test; no lift is asserted.
Allow every homogeneous term permitted by B_n-B_n''=U_n,
including frequencies whose U_n is zero, and every compatible zero
mode and constant K. Do not infer finite bandwidth of q,r from
finite bandwidth of h. Continuous traces must be handled without
an unproved interchange of an unweighted Fourier sum.

This test retains the chosen fiber's actual phase, not all angles
y1 at x1=ell. It deliberately tests only one necessary consequence
of actual-F domination. It does not impose or certify domination
away from the fiber, the actual diagonal traces, other zero fibers,
the period threshold, or full L868 admissibility.

The discriminating next mathematical result, after source approval,
would be a global lift satisfying every displayed condition, or
an obstruction valid against all allowed homogeneous and zero modes.
A lift would show that even these stronger restrictions fail to
exclude the fixed Green witness; an obstruction would identify
additional actual-zero compatibility missed by the abstract package.
Either could refine a future joint-positivity test, but neither
alone controls K>=-|M| or closes the actual-Xi mixed-positivity gap.
Do not continue by repeating only C868b's already known mean trace.

The nomination was REVIEW_REQUIRED at invocation start. The completed
literature-only review below supersedes that source-gate state without
performing the mathematical test. The newly ready continuation requires
its separate approval before research; this does not invalidate the
completed review. Matching Mathlib coverage remains unchecked.

## Completed source comparison, 6 November 2026

### Local inputs, duplicates and retained failures

Read L869 through the complete definition of h, all U_n, and the
Green profile construction, equations (1)-(15); read L868's exact
global coefficient/closure/period interface and C868a/C868b through
their profile and trace arguments. The chosen fiber is x1=ell,
y1=phi with both second coordinates free. It is not the whole
angular torus at x1=ell. L869 was built for every real ell, whereas
the present test uses the actual a and phase from C868b. The existing
Hardy applicability argument there is reused, including absence of
a simplicity or RH assumption; no new zero is required.

Checked the exact source records
`2026-11-06-bounded-profile-green-positivity-scope.md`,
`2026-11-06-one-sided-fourier-diagonal-period-test.md`,
`2026-11-06-one-sided-g-zero-fiber-period-scope.md`, and
`2026-11-06-fixed-g-zero-fiber-bound-audit.md`, plus the named
one-sided, diagonal, fixed-fiber and Green ATTEMPTS records and
`../../history/2026-11-06-green-counterexample-audit-01.md`.
No completed prescribed-h lift test was found in those records.
The Green negative form remains accepted at its exact abstract scope.
The diagonal/fiber tests stop short of sufficiency and period control;
they cannot be used as an existence theorem. The older stops are
preserved, not promoted to bans on this stronger compatibility test.

### Reused inputs and their exact limits

Reuse the inspected sources in the bounded-profile assessment:
[Engel-Nagel, VI.4.1, pp384-386](https://www.math.uni-tuebingen.de/de/forschung/agfa/members/engel-nagel_one-parameter-semigroups.pdf#page=400)
supplies the particular scalar Green kernel at parameter one for the
compactly supported C1 U_n already verified by L869. Its endpoint-limit
function space is not a new assumption on q,r or arbitrary B_n.
[Lebl, Notes on Diffy Qs, Theorem2.2.1(1)/Example2.2.1](https://www.jirka.org/diffyqs/html/sec_ccsol.html#thm:ccsol)
supplies the complete homogeneous solutions of the scalar equation,
with distinct roots +1,-1. Real and imaginary parts handle complex
coefficients. There is no global growth hypothesis to eliminate this
freedom. No reproof of either source is needed.

Reuse [Grafakos, Classical Fourier Analysis, third edition (2014),
Proposition3.1.10/Corollary3.2.2 pp180-183 and Theorem3.3.9(a)
pp196-197](https://www.math.stonybrook.edu/~bishop/classes/math638.F20/Grafakos_Classical_Fourier_Analysis.pdf),
with [corrected Theorem1.2.19(2), pp27-29](https://grafakos.missouri.edu/Books_Correction_Pages/CFA-Page27-29.pdf),
and Rudin Theorem9.42 as assessed in the diagonal review. C1 functions
on each fixed compact radial neighborhood times T2 meet the compact
differentiation and angular reconstruction hypotheses. Product Fejer
convergence supports continuous-slice traces; it does not certify a
globally convergent differentiated Fourier ansatz or finite bandwidth.
The current test may use C868a's existing mode interface, but must
justify any reconstruction beyond these operations. No source search
was repeated for these unchanged inputs.

### Newly inspected primary comparison

[Jiří Lebl, Tasty Bits of Several Complex Variables, v4.4,
31 May2026](https://www.jirka.org/scv/scv.pdf): Definition1.1.2 and
Proposition1.1.3, pp14-16, give the C1 Cauchy-Riemann characterization
and holomorphic smoothness. Read the iterated Cauchy-integral proof.
Theorem4.2.1, pp132-134, assumes smooth compactly supported compatible
data on C^n, n>=2; its unique solution is compactly supported. Read the
integral, compatibility, differentiation, support and uniqueness cases.
Theorem4.4.5, p141, concerns smooth closed forms on products of discs
or planes; only its statement was inspected. Theorem4.5.3, pp147-148,
assumes vanishing H^(p,q+1)(U) and smooth closed hyperplane data.
Read its cutoff/division correction proof. For functions the data must
already be holomorphic. These statements neither impose the present
fixed forcing nor directly handle its C1 regularity, punctured-product
domain and simultaneous zero trace. They are comparisons, not imported
existence assertions for this target. Exercise4.4.18 on punctured
products is an exercise, not an inspected proof. Matching Mathlib
coverage is unchecked.

The target-specific transformation into any inhomogeneous complex
equation, its sign conventions, the compatibility of its forcing,
and a complete treatment of its homogeneous and zero modes remain
mathematical work. None was derived here. In particular, citing an
extension theorem for holomorphic data would leave verification of
the proposed trace data unresolved. A failure of a particular Green
choice would leave all other homogeneous choices unresolved.

### Search and access record

Queries were `"inhomogeneous Cauchy Riemann" "Cauchy data" periodic`,
`"closed" "r" "q+h" Fourier differential equations`,
`site.jirka.org scv inhomogeneous dbar equation Cauchy Riemann Laurent theorem`,
`"periodic" "Cauchy-Riemann" "prescribed" "trace"`,
`"inhomogeneous" "Cauchy-Riemann" "hyperplane" vanishing`,
`"periodic" "inhomogeneous Cauchy-Riemann" "trace"`,
`"prescribed" "closed form" "Fourier" "homogeneous" torus`, and
`"Cauchy" "Riemann" "homogeneous" "hyperplane" extension prescribed forcing`.
The author-hosted v4.4 PDF was accessible. An HTML endpoint failed;
there is no essential source blocker. Search-result leads to Jarnicki,
Hörmander, Wiegerinck, boundary-value texts and Cauchy-Kovalevskaya
notes were not read and supply no theorem input or claimed obstruction.
The bounded search does not establish absence or originality.

### Approved test boundary and decision

After separate approval, attempt exactly the COVERED_TARGET using
L869's fixed h and C868a/C868b's interface. A valid positive result
must provide global C1 periodic q,r and check every closure equation
and the entire chosen fiber trace, including all finite real second
radial coordinates. A valid negative result must exclude all allowed
homogeneous and zero modes; examining only L869's eight active modes
or only its particular Green solution is insufficient. A local trace
obstruction, if established for every possible lift, is sufficient
to answer the global existence question negatively.

Continue only with such a lift, a full-class obstruction, or an exact
new compatibility condition with a discriminating remaining test.
Abandon an unchanged finite-band or particular-solution calculation
if it leaves unrestricted modes unpaid; preserve any partial argument
and require a refined mechanism before repeating it. Neither outcome
would certify actual-F domination, all other zero/diagonal conditions,
K>=-|M|, graph realization, actual-Xi signs or RH. The present outcome
is source preparation only: no new lemma, lift calculation, mathematical
script or change to PROOF.md/DAG.md.
