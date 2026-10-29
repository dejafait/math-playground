# L135 cyclic cubic-containment specialization — source coverage ready

TARGET: Determine whether the union of any three complete dual direction components supplied by L135 lies on a plane cubic, with every group-labeling and degeneracy hypothesis justified.
CHECKED: 2026-10-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the cone/bridge assessments and searched the active notebook for cyclic-cubic duplicates and ATTEMPTS/031–032,109; new source-following queries were `"3-nets realizing a group" "Proposition 18"` and `Korchmaros Nagy Pace "3-nets realizing a group in a projective plane" arxiv`. No new originality claim or broad discovery search.
SOURCE_EVIDENCE: Inspected Korchmaros–Nagy arXiv:1710.00172v1 pp. 1–4 Definition 2.1/Lemmas 2.2–2.5 and algebraic terminology, pp. 8–10 Section 4 setup/Proposition 4.3/Lemma 4.4/Proposition 4.5 with proof; followed its cyclic-net reference to Korchmaros–Nagy–Pace arXiv:1104.4439v3 p. 3 standing characteristic assumptions, pp. 3–4 Proposition 2.3, pp. 17–18 Proposition 6.1 and its complete cyclic propagation proof.
COMPARISON: The cited cubic theorem covers cyclic light dual multinets, including additional incidences; L135 already supplies component injectivity and disjointness. Explicit cyclic relabeling, extension of the coordinate field, collinear cases and descent to a cubic over K remain local applicability work, not a new classification theorem.
GAP: Prove the missing applicability steps for every ordered triple of retained directions, then cite Proposition 4.5. This assessment does not establish that specialization, common cubic containment of all retained components, collapse, uniqueness, irreducibility, a retention cap or RS transfer.
REASON: The source theorem and its essential degeneration/propagation cases are accessible and sufficient to authorize the bounded specialization. No full reproof is justified; derive only the stated applicability difference in a later research turn after separate supervisor approval.
LITERATURE_REASON: At turn start this changed target had REVIEW_REQUIRED coverage; the cyclic theorem's hidden setup and referenced propagation cases required inspection beyond the ready L135 separation audit. That source gap is now closed.
SCOPE: L135 and L030 with q=137, T={16,64,70,102,112,118,121}, E=F_65537, F=F_(65537^28), H=<19139>, k=64, K=E or F, arbitrary actual 61-core/bijection and coefficient-difference span exactly two. Select any three complete classes retained by L135, allowing repeated g_P, additional incidences and an exceptional direction already omitted. No group labeling, non-collinearity, ordinary-net property, field embedding or classification is assumed.

## Purpose, scope and bounded test

The main gap is arbitrary-center 67/68 safety. A justified cubic-containment
input could constrain the span-two coefficient geometry in a later
collapse attempt. It would not establish collapse, handle span three or
partial-sheet retention, attain threshold 1532496, or transfer to RS lists.

The target is unchanged. Interpret containment separately for each
three-component union, allowing the cubic to depend on that triple.
The desired local conclusion is a nonzero homogeneous cubic form over
K vanishing on that union. A cubic over the algebraic closure alone
must be labeled as such until descent is justified. Reducible, singular
and nonreduced cubics are allowed; there is no asserted uniqueness.

Continue if a later research turn proves every applicability obligation
below and obtains the stated containment by citation. If one fails,
save its exact permitted degeneracy or missing implication. Generic
labels, an assumed ordinary net, an assumed embedding of F_137 in K,
or an assumed faithful action do not pass. Do not restart the stopped
residual-rank computation. The old admission test was source access and
scope; this review passes that test, not the mathematical target.

## Primary theorem and proof cases actually inspected

Gábor Korchmáros and Gábor P. Nagy, *Group-labeled light dual multinets
in the projective plane (with Appendix)*,
[arXiv:1710.00172v1](https://arxiv.org/pdf/1710.00172v1),
30 September 2017, is the theorem version used. Definition 2.1,
printed p. 3, asks for prescribed product triples to be collinear and
for the component maps to be injective in the light case. The
introduction also stipulates disjoint components. Its definition of
algebraic, p. 4, permits reducible or singular cubics. Proposition 4.5,
p. 10, states that finite cyclic light dual multinets are algebraic.
No long-line-nine hypothesis or plane-spanning requirement occurs
there. Theorem 1.1's classification is a different result.

Section 4 first separates the all-collinear case. The noncollinear
proof uses a maximal-line subgroup H: index at most two is handled by
Proposition 4.3 and Lemma 4.4, including the order-four coincidence of
types; higher index uses nine-point Lamé configurations. Distinct
points use lightness and component separation. Coincident construction
lines would force a subgroup of index at most two from label
differences one or two, contradicting the maximal-line bound. These
are source proof cases, not additional hypotheses silently imposed on
L135. For the proposed order-137 application, the later proof must
explain which cases apply or cite the full proposition without deleting
its trivial collinear case. No irreducible-cubic classification is needed.

The essential referenced argument was also read: Gábor Korchmáros,
Gábor P. Nagy and Nicola Pace, *3-nets realizing a group in a projective
plane*, [arXiv:1104.4439v3](https://arxiv.org/pdf/1104.4439v3),
17 June 2011. Its p. 3 standing assumptions are algebraic closure,
characteristic zero or p>=5, and n<p in positive characteristic.
Proposition 2.3, pp. 3–4, is the nine-distinct-intersection Lamé theorem.
Proposition 6.1, pp. 17–18, supplies cyclic-net cubic containment.
Its proof treats n=3 separately, starts a pencil through nine points,
selects the member through one further point, and uses all five
displayed Lamé pairs (i)–(x) to propagate. The n=4 stop and n>=5
continuation are explicit. The final shift repeats this propagation
through the components. Thus the referenced mechanism and its finite
initial cases were read, rather than inferred from a classification
abstract. Korchmáros–Nagy's small-label-difference check is the stated
bridge permitting that mechanism for light multinets.

The 2017 paper cites this work as *J. Algebraic Combinatorics* 39
(2014), 939–966, Proposition 18. The inspected arXiv version numbers
the cyclic theorem Proposition 6.1; these numbering systems must not
be conflated. The [publisher record](https://link.springer.com/article/10.1007/s10801-013-0474-5)
confirms the bibliographic data but exposes only a subscription preview.
The DOI redirect first failed and the ELTE repository returned 502.
The published Proposition 18 text was not independently read; the
accessible, explicitly versioned Proposition 6.1 proof above supplies
the needed propagation evidence. No paid access or credentials were used.

## Exact local applicability work approved for the research turn

1. Fix arbitrary distinct retained directions a,b,c. Use their
   auxiliary line equations u+tv=y to construct three explicit
   bijections from the additive cyclic group F_137 to the three
   direction indices, with the group sum giving the designated third
   index. Verify all coefficients and denominators in F_137, then use
   L135's concurrency/duality statement. No such relabeling is derived
   or certified in this literature turn.
2. Use L135 for all 137 points per component, injectivity and pairwise
   separation, including omission of the entire exceptional direction
   when required. Allow repeated g_P and extra incidences. Neither
   Definition 2.1 nor Proposition 4.5 asks for the converse incidence
   implication of an ordinary dual 3-net.
3. Place the projective dual plane over an algebraic closure of K.
   Justify preservation of distinct projective points and collinearity
   under scalar extension; do not embed the auxiliary field F_137
   into K. Both permitted K have characteristic 65537, so the
   conservative positive-characteristic coverage p>n=137 is adequate
   even for the standing assumptions of the referenced cyclic-net
   proof. This does not assert a field embedding or a group action.
4. Include the wholly collinear case explicitly. In the other cases
   invoke Proposition 4.5 rather than reprove the Lamé construction,
   subgroup classification or Proposition 4.3. Containment alone is
   the conclusion: no nonsingularity, irreducibility or faithful action
   follows from this import.
5. If claiming a cubic defined over K, give the elementary descent
   argument using the degree-three evaluation matrix over K and
   invariance of matrix rank under a field extension (equivalently,
   Gaussian elimination). This is the supporting linear algebra
   specialization to be written, not an established local result in
   this assessment. A possible factorization need only exist over the
   algebraic closure; no descent of the individual factors is required.

These are verification and specialization obligations, not a new
creative mechanism. The source already proves the geometric result
once its labeling hypotheses are met; any local lemma must be
classified as reproduction/specialization and carry the precise import.
Full/supporting Mathlib coverage remains unchecked, not absent.

## Duplicates, recorded failures and continuation boundary

Reused `2026-10-27-quadratic-cone-sheet-rigidity.md`,
`2026-10-27-span-two-light-multinet-bridge.md` and L135's audit coverage.
The targeted notebook search found those earlier conditional comparisons,
not a completed local cyclic-cubic applicability proof. The new work in
this review is inspecting the standing setup and referenced propagation
cases and identifying the exact local difference; it is no novelty claim.

ATTEMPTS/031–032 show why fixed-core shift/translation exclusions do not
give the sufficient cap; cubic containment would not erase those
obstructions. ATTEMPTS/109 parks the all-label residual-rank attack.
Preserve it and L135's two failed stronger omission probes. No
cross-notebook theorem, (W1)–(W5), order-six classification or Theorem 1.1
long-line claim is imported. The pinned July ABF source qualification
is unchanged. Span three, partial-sheet retention, the threshold and
global RS transfer remain independent even if this specialization passes.

The assessment is now SPECIALIZE for the exact saved target, ready for
separate supervisor approval before research. No lemma, mathematical
script, DAG edge or main proof changed. A later creative collapse target
would need its own bounded test and source coverage; this routine
specialization must not be relabeled creative to meet a scheduling aim.
