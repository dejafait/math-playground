# Signed stationary odd-contact continuation — completed source comparison

TARGET: Test whether every single odd-order contact G(z_j)=0 on a graph satisfying L879 extends with the same zero label zeta around the entire angular fiber y_j=arg(zeta), retaining all simultaneous-G and diagonal vertices and distinguishing a failed argument from an actual terminating stationary contact.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed exact-target, constant-phase/divisor and finite-order smooth-nodal searches; read L879's full statement, edge and intrinsic-fiber arguments and audit, L847's full form/homotopy, L864-L866 hypotheses/conclusions and L866's sign-dependent normalization/fiber proof. Reused named ready assessments and session43 stop; queries and primary read ranges below. No matching through-vertex theorem was found in this bounded comparison; no novelty inference.
SOURCE_EVIDENCE: Newly inspected Beck-Becker-Kahn-Hanin arXiv:1604.04307v3 (17 October 2016), Theorem1 pp2-3 and Section2.1-2.2 pp6-8 https://arxiv.org/pdf/1604.04307v3 ; reopened Michalek Algebraic Varieties (17 April 2018), Example7 p4 https://www.math.uni-konstanz.de/~michalek/april17.pdf and Lawrence-Yamauchi arXiv:2311.13002v2 II B (9)-(16) pp3-4 https://arxiv.org/html/2311.13002v2#S2.SS2 ; reuse Lebl CA v1.10 Theorem2.4.7 pp49-50 https://www.jirka.org/ca/ca.pdf and the ready elementary/geometry comparisons below.
COMPARISON: L879 establishes a local same-label odd-contact fiber and a global phase line, not continuation through actual-divisor vertices. L864-L866 require nonnegative density. Smooth-nodal coverage supplies containing graphs, not equality with a labeled divisor branch; conjugation of polynomial factors constrains a real leading polynomial, not an exact smooth contact set. Neither is a theorem deciding TARGET.
GAP: One bounded attempt must test exact same-label continuation through simultaneous-G and G-diagonal vertices with arbitrary finite multiplicities, without positivity or analytic-u assumptions. A first-order or finite-jet obstruction to an argument is not an actual terminating contact or a global stationary-graph counterexample.
REASON: The missing target-specific comparison is complete for one elementary actual-divisor attempt under EXPLORE; assessed factorization, differentiation, continuity and real-polynomial tools suffice for that test. No essential source blocker or matching import remains. This newly ready assessment requires separate next-invocation gate approval; no continuation theorem is proved or accepted here.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED concerned signed same-label continuation through vertices, outside the accepted L879 audit and nonnegative-contact scope. The finite-order nodal lead and exact hypothesis comparison address that changed assertion, not another stationarity audit.
SCOPE: Exactly TARGET for L847's unchanged actual G,R,C,F, full pullback and original angular orientation; smooth real periodic u satisfying L879's nowhere-zero J and all real radial variations compactly supported off Q=0. Retain every simultaneous-G and diagonal coincidence, actual multiplicities and nonisolated contact sets. No nonnegativity, analytic u, contact existence, simple-zero, finite pulled-back census, symmetry, collar, graph-realization, flow or RH assumption is added. A bounded proof attempt or precise failure diagnosis is covered; replacement mechanisms require separate review.

## Original nomination retained for context

The paragraphs below record the invocation-start nomination; its
REVIEW_REQUIRED source decision is superseded by the completed
comparison below. They make no mathematical assertion of continuation.

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. The proposed intermediate target concerns the remaining
odd-contact branch in audited L879. Same-label global continuation,
if valid, would impose a global periodic constraint on that branch
that could be tested separately. It would not by itself exclude the
branch, construct a graph or establish the sharp mass threshold.

L879 and L847 are the essential established inputs to examine.
L864-L866 are named comparison results, not premises in this signed
problem. Reuse the ready
`2026-11-06-l879-stationary-phase-line-audit.md`,
`2026-11-06-stationary-graph-phase-components.md` and
`2026-11-06-odd-divisor-contact-scope.md` for their unchanged inputs.
The new comparison must cover the vertex-continuation assertion
rather than repeat the accepted off-zero variation or phase-line audit.

The discriminating test is a full argument at every possible endpoint
of the same-label odd-contact fiber, including simultaneous-G and
G-diagonal contacts. If continuation is established, retain its exact
hypotheses; if an essential case fails, record that case and the failed
implication. A formal compatible jet or an unclosed proof is not an
actual terminating contact on a global stationary graph. The target
does not license a replacement alignment mechanism or a claim that
such a graph exists.

The automatic-global-ray stop in
`ATTEMPTS/2026-11-06-stationary-global-ray-unresolved-43.md` remains.
The product-graph, retired two-period and positive-contact scope
limitations also remain. This nomination proposes a specific new
through-vertex test; it derives and approves no mathematics.
Graph existence, odd-contact exclusion/realization, compactness,
sharp period, higher signs and Xi transfer remain independent gaps.
Full matching and supporting Mathlib coverage is not checked.

## Source comparison completed 6 November 2026

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION: adequate source
coverage for the unchanged test, not an imported answer, mathematical
advance beyond the sources or new obstruction. No lemma, mathematical
script, DAG or PROOF change is made. The following comparisons do not
derive vertex behavior.

### Local overlap and recorded failures

L879 (11)-(13), its intrinsic criterion and the independent audit
separate open edges from vertices. Its single-odd-contact argument
shrinks until the other G factor and diagonal factor are nonzero.
Its global phase-line proof handles vertices by density; it explicitly
does not propagate contact germs through them. The accepted result is
an input, not a duplicate answer to TARGET.

Read L864-L866's hypotheses and conclusions, and L866's direct
normalization and horizontal-fiber proof through its exact-contact
conclusion. Its decisive real-part inequality uses q>=0; signed real
density is not that premise. Its even-order conclusion does not cover
arbitrary signed multiplicities. L864's global statements additionally
impose their entire-contact census. These are hypothesis comparisons,
not new rank or parity results.

Reuse the ready stationary-graph, L879-audit and odd-contact assessments.
Read the relevant source paragraphs in the simultaneous-multiple-
contact-rank and double-contact-isolation assessments and the actual-G
full-phase geometry comparison. The session43 automatic-ray stop
remains, as do the recorded product, retired two-period, positive-contact,
C868c and L872/L873 limitations. Neither a generic cosine example,
free jet nor separate component sign rotation supplies an actual
terminating stationary contact. No cross-notebook input is used.

### Primary statements and essential proof cases

Thomas Beck, Spencer Becker-Kahn and Boris Hanin, *Nodal Sets of Smooth
Functions with Finite Vanishing Order and p-Sweepouts*,
[arXiv:1604.04307v3, 17 October 2016, Theorem1 pp2-3;
Section2.1-2.2 pp6-8](https://arxiv.org/pdf/1604.04307v3).
Its real family F is C-infinity on U x Theta, with U open in R^(n+1)
and Theta a finite-dimensional compact smooth manifold, possibly with
boundary. Assume finite vanishing order gamma of F(.,theta0) at x0.
Theorem1 gives a ball, parameter neighborhood and hyperplane on which
the nearby nodal sets are contained in gamma W1,p graphs for some p>1,
with uniform norms. Read the preparation reduction, root selection and
Sobolev proof. The selected graphs use real parts of complex roots:
containment (2.9), not equality, is essential. Neither a specified
angular graph nor a fixed G-zero label follows. No finite-order
hypothesis for a selected pullback is verified here; the theorem is
not applied and even conditional applicability leaves TARGET undecided.
Malgrange preparation and Parusinski-Rainer root regularity are cited
proof inputs, not independently imported tools. Later sweepout, heat
flow and measure results are not used.

Mateusz Michalek, *Algebraic Varieties*, notes of 17 April 2018,
[Example7, printed p4](https://www.math.uni-konstanz.de/~michalek/april17.pdf#page=4).
Reopened the FTA factorization paragraph and real-coefficient
conjugation/divisibility argument. Projective complex linear factors
are unique up to constants and order; real coefficients preserve
their multiset under conjugation. This part needs no nonnegativity.
It is an available standard input only after a later attempt establishes
a nonzero real homogeneous leading polynomial with all factors and
scalar tracked. It constrains that polynomial, not an exact smooth
contact set. No target-specific polynomial or rank condition is derived
here. The nonnegative binary-form sum-of-squares and even-real-root
conclusions in the ready assessment have extra sign premises and are
not imported for signed density. Extracted missing conjugation bars
are not treated as corrected formulas; the explicit conjugation-
invariance prose fixes the scope.

Scott Lawrence and Yukari Yamauchi, *Convex optimization and contour
deformations*, [arXiv:2311.13002v2, II B (9)-(16), pp3-4](https://arxiv.org/html/2311.13002v2#S2.SS2).
Reopened the necessary stationarity derivation through the weighted
phase condition and subsequent zero-separation discussion. It uses an
invertible complex Jacobian and unrestricted contour variations;
phase constancy is away from zeros. Reuse L879's accepted constrained
specialization. The source supplies no same-divisor branch continuation
through a density zero. Reuse the ready 2021 fixed-point/conditional-
family comparison and Lotay-Pacini Section9.1 Lemmas9.2-9.4, pp666-668:
no unconditional family is supplied, and a nonzero ambient-form setting
does not cover the retained divisor. No new analytic continuation,
existence, sufficiency or calibration input is imported.

Reuse Jiří Lebl, *Guide to Cultivating Complex Analysis*, v1.10,
5 November 2026, [Theorem2.4.7 and factorization/identity proof,
pp49-50](https://www.jirka.org/ca/ca.pdf#page=49).
G is entire and G(0)>0, so finite-order holomorphic units and isolated
ambient labels are available. This is not an identity theorem for
the smooth real parameter map u. Reuse Lebl *Basic Analysis I* v6.3,
[Definition4.1.1 p155 and Theorem3.3.8 pp132-134](https://www.jirka.org/ra/realanal.pdf),
and *Basic Analysis II* v6.3,
[Theorem8.5.6 and proof pp55-56](https://www.jirka.org/ra/html/sec_svinvfuncthm.html),
through the ready double-contact-isolation comparison. First-order
differentiation and the intermediate value theorem apply to their
stated real curves; an implicit-function application must check its
own dependent-variable derivative. Complex J!=0 alone is not that
check. These elementary tools, continuity and L879's finite angular
arrangement suffice for a bounded attempt. No reproof of a standard
theorem or essential unread source is required.

### Searches and bounded next test

Queries actually issued, grouped by comparison:

- `"locally perfect" contour zeros "globally" Lawrence Yamauchi`;
  `"stationary" "contour" "zero" "continuation" Yamauchi`;
  `"perfect contour" "zeros" "multiplicity"`.
- `"constant phase" "holomorphic" "divisor" continuation submanifold`;
  `"constant phase" "zero" "divisor" "totally real"`;
  `"holomorphic" "volume form" "zeros" "continuation"`;
  `"totally real" "zero set" "holomorphic volume" singular`;
  `"special totally real" "vanishing" "form"`;
  `"normal crossing" "real" "constant phase"`.
- `"stationary" "radial graph" "zero" holomorphic phase`;
  `"same" "label" "fiber" "stationary" "holomorphic"`;
  `"holomorphic" "constant argument" "zero set" "smooth"`;
  `"nodal set" "smooth function" "finite order" "branches"`;
  `Beck Becker-Kahn Hanin "Nodal sets of smooth functions" arxiv`.

Exact searches returned the contour sources or unrelated material.
The smooth-nodal lead was followed to its primary theorem and relevant
proof above. Other PDE, physics, review and abstract snippets were
discovery leads only. The BBH proof's specialized root estimates are
unnecessary for the elementary test, so their separate primary proofs
are not essential unread inputs. A bounded search does not establish
novelty or impossibility. Full matching and supporting Mathlib coverage
remains unchecked, not absent.

After separate gate approval, attempt continuation of the existing
local same-label fiber through every actual vertex and around the
circle, using L879 and L847 as essential inputs. Compare incident face
phases and retain the full factorization when another factor vanishes.
Polynomial conjugation may test necessary conditions; it cannot replace
exact contact continuation. Include simultaneous distinct G zeros,
a G zero on the diagonal (where both G factors meet), arbitrary orders
and angular identifications. This is a plan, not a derived case split.

Continue if the same label is established across every actual vertex
under the unchanged smooth hypotheses. If a case is unresolved, save
the precise missing implication and stop that attempt. Failure of a
proposed argument must not be called a realizable endpoint; refuting
the global assertion requires an actual smooth periodic stationary
graph satisfying L879. Do not add analyticity, positivity, simplicity,
isolated contacts or a finite entire census. Graph existence,
odd-contact exclusion/realization, compactness, sharp period, higher
signs and actual-Xi transfer remain independent gaps. Newly ready
EXPLORE coverage receives separate next-invocation approval.
