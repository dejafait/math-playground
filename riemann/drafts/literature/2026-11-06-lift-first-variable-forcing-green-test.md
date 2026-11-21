# Proposed lift-first variable-forcing Green test

TARGET: Assess literature for a lift-first four-frequency variable-forcing countermodel with full zero-fiber closure and a negative Green form at mass H.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed the named local Green/fixed-forcing failure comparison and bounded exact-system, periodic inhomogeneous Cauchy-Riemann, finite Fourier and prescribed-mass Green searches listed below; no inspected matching theorem decides the simultaneous variable-forcing test. Reused the two named ready assessments for unchanged elementary inputs; no originality inference.
SOURCE_EVIDENCE: Reuse 2026-11-06-green-countermodel-zero-fiber-lift.md and 2026-11-06-fixed-green-zero-fiber-obstruction-audit.md for their inspected Green/ODE/Fourier/trace inputs; inspected Lebl, Tasty Bits of Several Complex Variables v4.4 (2026-05-31), Theorem4.5.3 and full cutoff/division proof pp147-148, https://www.jirka.org/scv/scv.pdf ; checked Lebl Diffy Qs Theorem2.2.1(1)/Example2.2.1 and Bhatia (2007) Section1.1 pp1-2 at the primary URLs below.
COMPARISON: L869 supplies only the abstract negative form and C869a stops only its fixed h. The inspected extension theorem provides a closed extension of smooth closed hyperplane data under a cohomology hypothesis; it supplies no nonnegative forcing with the prescribed finite support, two means and negative Green form. Scalar ODE solvability does not establish the simultaneous constraints or remove unrestricted lift modes.
GAP: Construct one global C1 periodic lift together with a changed forcing satisfying the complete package and a strictly negative specified Green form, or prove an obstruction covering all allowed profiles and lift modes. No such result is established here; full actual-F admissibility and the period inequality remain outside this test.
REASON: Essential source comparison is adequate for the one bounded test below, and no essential source remains blocked. EXPLORE permits a later mathematical attempt after separate approval, without asserting feasibility, impossibility, novelty or a general existence theorem.
LITERATURE_REASON: Mandatory review of the changed simultaneous variable-forcing, closure and trace scope; the ready fixed-forcing assessments do not cover choosing h and its lift together. Unchanged elementary coverage is reused.
SCOPE: Exactly the displayed eight-frequency compact C1 forcing profiles, arbitrary radial zero mode satisfying both stated means, H>0, fixed C868b ell,phi, and unrestricted real global C1 periodic q,r with both closure equations and the full one-fiber trace. No growth, lift bandwidth, actual-F domination or other zero/diagonal premise is added.
COVERED_TARGET: Attempt a lift-first four-frequency variable-forcing countermodel with full zero-fiber closure and a negative Green form at mass H.

## Exact proposed mathematical test for review

Fix ell and phi from the one actual zero in C868b, and H>0.
Allow h to vary, rather than retaining L869's cutoff formula.
Require exactly L869's nonnegative real C1 bounded-profile package
(1)-(3), including its reality relation, both mean identities,
the bound |U_n|<=H and every opposite-index Toeplitz test.
Restrict its nonzero angular support to the eight frequencies
plus/minus (1,0), (0,1), (1,1), (1,-1), with C1 compactly
supported profiles U_n; its radial zero mode may vary as in L869.
In addition, require real global C1 periodic q,r satisfying

\[
r_{x_j}=q_{y_j},\qquad (q+h)_{x_j}=-r_{y_j}\quad(j=1,2),
\qquad q((\ell,s),(\phi,v))=r((\ell,s),(\phi,v))=0
\quad(s,v\in\mathbb R).
\]

No finite-band, growth or homogeneous-mode restriction is imposed
on the lift q,r. The intended construction starts with simultaneous
closure and trace constraints on q,r,h, rather than choosing h
from the abstract package and trying to repair its lift afterward.
This is a proposed mechanism, not a derivation of feasibility.

Use exactly L869(4)'s Green data, with b_0=H. Seek a point x*
where the form on E=(0,(1,0),(0,1),(1,1)) for
c=(1,-1,-1,1) is strictly negative. Thus the threshold is <0,
not a numerical eigenvalue preview. The selected x*, profile
shapes and their centers are free; L869's failed fixed cutoffs are
not retained. Passing only C869a's necessary h_x2=0 condition
does not count as constructing a lift.

A rigorous construction satisfying all the stated conditions would
show that even this full one-fiber closure compatibility cannot
restore the four-index joint-positivity implication. An obstruction
valid for all allowed profiles and all lift modes would stop this
bounded mechanism. An unsuccessful finite ansatz alone would do
neither. This screens the proposed positive-correction route toward
K>=-|M| and ultimately L030-L032/C032a; it does not prove either.
Actual-F domination away from the fiber, other zeros, the actual
diagonal pointwise trace, graph realization and actual-Xi signs
remain separate unresolved requirements. The two mean identities
are retained and do not substitute for those stronger requirements.

## Required source comparison and continuation test

Essential local inputs are L869's exact package and Green operator,
C869a's audited obstruction, C868a's profile interface and C868b's
one-fiber parameters. Reuse
`2026-11-06-green-countermodel-zero-fiber-lift.md` and
`2026-11-06-fixed-green-zero-fiber-obstruction-audit.md` where their
elementary inputs remain adequate. Compare the changed simultaneous
closure/trace feasibility statement with primary results before
approving a mathematical construction. Inspect relevant theorem
hypotheses and proof cases; do not infer sufficiency from scalar
ODE solvability or general extension theorems. Search these named
local stops first:
`ATTEMPTS/2026-11-06-green-fixed-mass-joint-positivity-stop.md` and
`ATTEMPTS/2026-11-06-fixed-green-zero-fiber-lift-stop.md`.

Approve a later bounded mathematical test only if the changed
scope has adequate source coverage and no known result already
decides it. Import a matching result if located. Park the mechanism
if an essential source remains persistently blocked, or if a known
obstruction rules out this finite-frequency setting. Do not repeat
the fixed h, enlarge a matrix without new compatibility, or call
the present nomination a creative mathematical attempt. A later
genuinely new lift-first proof attempt may warrant creative routing:
its precise obstruction is the conflict between an entire zero
fiber, global closure/nonnegativity and a negative prescribed-mass
Green form. Full matching Mathlib coverage is unchecked.

## Completed literature-only comparison, 6 November 2026

The main gap is L030-L032/C032a actual-Xi all-degree mixed
positivity. The intermediate target is exactly the simultaneous
feasibility test above. Its plausible use is to decide whether full
one-fiber compatibility repairs the failed abstract positive-correction
implication before pursuing K>=-|M|. The continuation below changes
neither the frequency set nor the negative-form threshold.

### Local evidence and reused coverage

Read L869's full construction, C869a's full obstruction and audit,
C868a's coefficient interface and C868b's actual-zero parameters,
fiber means and coefficient restrictions. Read both named ATTEMPTS
records. The scoped search for `lift-first`, `variable.forcing` and
`simultaneous.*closure` in the named 6 November Green assessments,
stops and histories found the present nomination, not a completed
variable-forcing construction. This is a local duplicate check,
not an assertion about all literature or other notebooks.

L869 does not supply q,r. C869a is valid against all lift modes,
but its contradiction evaluates that particular h. Replacing h
therefore requires a new test, rather than an attempted repair by
adding homogeneous terms to the stopped forcing. The necessary
condition in C869a remains binding; satisfying it alone is insufficient.
Neither C868a nor C868b claims sufficiency or joint Green positivity.
The original stops and unfinished stronger conditions are preserved.

Reuse the actual inspected source evidence and applicability arguments
in `2026-11-06-green-countermodel-zero-fiber-lift.md` and
`2026-11-06-fixed-green-zero-fiber-obstruction-audit.md`:

- Engel-Nagel, *One-Parameter Semigroups for Linear Evolution
  Equations*, GTM194 (2000), VI.4.1, proof (4.2)-(4.3), pp384-386,
  [primary PDF](https://www.math.uni-tuebingen.de/de/forschung/agfa/members/engel-nagel_one-parameter-semigroups.pdf#page=400).
  Every permitted U_n is continuous with compact support, hence has
  finite endpoint limits as required for that scalar resolvent input.
  This covers the specified particular Green solution; it neither
  selects the lift's homogeneous terms nor controls its zero mode.
- Lebl, *Notes on Diffy Qs*, online Section2.2,
  [Theorem2.2.1(1), Example2.2.1](https://www.jirka.org/diffyqs/html/sec_ccsol.html#thm:ccsol),
  accessed 2026-11-06. The distinct real root case describes the
  entire homogeneous scalar solution space. At roots +/-1 it gives
  both exponentials, with real and imaginary parts treated separately
  for complex profiles. No global boundedness of q,r is assumed.
  The statement and this example were checked at the primary page;
  the existing assessment's elementary ODE coverage is reused.
- Rudin, *Principles of Mathematical Analysis*, third edition (1976),
  Theorem9.42, pp236-237, and Grafakos, *Classical Fourier Analysis*,
  third edition (2014), Proposition3.1.10/Corollary3.2.2 pp180-183,
  Theorem3.3.9(a) pp196-197 and corrected Theorem1.2.19(2), pp27-29,
  with direct primary links in the reused assessment. On each compact
  radial neighborhood, global C1 regularity and angular periodicity
  meet the compact differentiation, integration-by-parts and product
  Fejer hypotheses. This supports C868a's interface and continuous
  slice traces, not an unweighted differentiated infinite series.
- Bhatia, *Positive Definite Matrices* (2007),
  [Section1.1, pp1-2](https://assets.press.princeton.edu/chapters/s8445.pdf),
  checked at the publisher PDF. The finite Hermitian quadratic-form
  criterion applies once the actual entries are identified. It does
  not provide their sign; no general factorization is needed here.

The previously inspected definition of a partial derivative in Lebl,
*Basic Analysis II*, Section8.3, Definition8.3.8, is reused exactly
as in C869a's audit assessment. It licenses tangential differentiation
of a C1 pointwise trace, not zero normal derivatives. None of these
standard inputs is reproved or asserted as a new result.

### Extension comparison and exact limits

Lebl, *Tasty Bits of Several Complex Variables*, v4.4, 31 May2026,
[Theorem4.5.3 and proof, pp147-148](https://www.jirka.org/scv/scv.pdf#page=147):
smooth closed (p,q)-data on an affine hyperplane extend to a smooth
closed form on open U if H^(p,q+1)(U)=0. Read the full cutoff,
division by the transverse coordinate, smooth extension of the
correction data and cohomological solvability cases. For functions,
the prescribed data must already be holomorphic. The theorem gives
no sign, finite-frequency, compact-profile, mean or Green-form
control. It cannot certify this simultaneous feasibility test.

Reuse the earlier comparison with the same book's Theorem4.2.1,
pp132-134: smooth compactly supported compatible data on C^n,
n>=2, have a unique compactly supported solution. Compact support of
each one-variable U_n is not the asserted support hypothesis on data
in C^n; the target also allows C1 data. No conversion of the present
system to that theorem is performed. These are scope comparisons,
not imported existence assertions for q,r,h.

The bounded searches additionally used these exact queries:

1. `"inhomogeneous Cauchy Riemann" "zero" "hyperplane"`
2. `"Cauchy Riemann" "nonnegative" "forcing" periodic`
3. `site.jirka.org scv Laurent series Reinhardt domain theorem`
4. `"Fourier" "Cauchy-Riemann" "nonhomogeneous" "periodic"`
5. `"positive" "Green" "Fourier" "prescribed mean" kernel`
6. `"compactly supported" "forcing" "Cauchy-Riemann" trace`
7. `"r_{x_j}" "q_{y_j}" "h"`
8. `"Cauchy-Riemann" "trigonometric polynomial" "inhomogeneous"`
9. `"positive definite" "Green" "frequency-dependent" Fourier`

No matching result was located in the inspected primary statements.
Laurent-expansion, numerical CR, Hermitian-analysis and physical
Green-function search hits were not used as theorem evidence; no
new essential lead was identified in them. Search snippets do not
establish coverage, impossibility or originality. The PDF text was
accessible through the full relevant proof. A screenshot timeout,
an inaccessible guessed HTML endpoint and a 404 guessed source path
did not block the primary text or the reused assessments.

### Decision and single bounded continuation

The exact COVERED_TARGET is ready for separate approval. The intended
mechanism is lift-first: impose closure and the full trace while
choosing the forcing, instead of retaining L869's incompatible cutoff.
It may use the known profile interface and elementary ODE/Fourier
operations. This approval covers the exact stated feasibility test,
including a full-class obstruction, not broader function classes or
new general PDE machinery. Any uncovered essential theorem must first
receive its own source assessment.

Continue on a rigorous construction satisfying every displayed
condition with the stated quadratic form <0, or an obstruction valid
for all allowed forcing profiles and unrestricted lift modes. Preserve
any intermediate compatibility result with its remaining quantified
test. A failed finite lift ansatz, numerical negative eigenvalue,
passing only h_x2=0 on the fiber, or an example without global h>=0
does not decide the test. If only such incomplete evidence is reached,
save it and require a refined mechanism before repetition; do not
silently discard unrestricted modes or enlarge the matrix.

Essential inputs are L869(1)-(4), C869a and C868a/C868b at their
audited scopes. Actual-F domination away from the fiber, other zeros,
the actual diagonal trace, K>=-|M|, graph realization and Xi signs
remain unresolved. No cross-notebook input is used. Full matching
Mathlib coverage is unchecked, with no absence inference. This review
is source preparation only: no new result, construction, impossibility
proof, lemma or mathematical script was produced. PROOF.md and DAG.md
therefore require no change.
