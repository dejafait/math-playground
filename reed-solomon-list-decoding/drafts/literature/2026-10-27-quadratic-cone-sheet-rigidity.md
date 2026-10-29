# Quadratic-cone formulation — completed source comparison

TARGET: Compare primary rigidity results for the seven-class point-plane configuration on a quadratic cone in (W5), retaining repeated planes and extra incidences, against the full-sheet rank-408 target.
CHECKED: 2026-10-27
DECISION: EXPLORE
SEARCH_EVIDENCE: New bounded searches covered finite Laguerre planes, cone sections, intersecting quadratic-polynomial families, light dual multinets, weak embeddings and noninjective multinets; queries and inspected primary passages are recorded below. Reused the prior plane-net assessment and checked the saved working reduction and ATTEMPTS/031–032,109; no exact all-label collapse theorem was located, and no novelty is inferred.
SOURCE_EVIDENCE: Newly inspected Adriaensen arXiv:2105.05815v1 Theorems 1.2/1.4 and Remark 5.2; arXiv:2201.06067v1 Theorems 1.3/6.5, Proposition 5.10 and Lemma 6.1 with their relevant proofs; Brown, RIMS 1476 (2006), pp. 205–207; Korchmaros–Nagy arXiv:1710.00172v1 Definition 2.1, Lemmas 2.2/2.4/2.5, Theorem 1.1, Proposition 4.5 and its proof; Bogya–Nagy arXiv:1810.00416v1 Introduction and Definition 5.1. Exact versions, hypotheses and reading limits appear below.
COMPARISON: The cone is the standard classical Laguerre model, but circle EKR/stability assumes a set of pairwise-intersecting circles and an unattainable size threshold here; its conclusion is common-point containment rather than equal planes. Light multinets genuinely allow extra incidences, but require injective component maps; their planar reduction and separation are unproved for these assignments. Thus neither literature route supplies rank 408.
GAP: The universal rank-408 claim remains open. A more focused missing bridge is whether a nonconstant coefficient-span-two assignment yields three complete, injective and disjoint dual evaluation-line components despite common-root and coincident-line degeneracies; coefficient span three remains independent.
REASON: New primary-source evidence rules out direct circle-stability import and refines the failed ordinary-net comparison: extra incidences alone do not exclude light multinets. This justifies a bounded degeneration-aware planar bridge target, not a repetition of the 74528-row rank attack or a collapse theorem.
SCOPE: Source comparison only for the pinned E=F_65537, F=F_(65537^28), H=<19139>, q=137 and T={16,64,70,102,112,118,121}, arbitrary 61-core and bijection, with repeated assignments, extra incidences and coefficient-span dimensions two and three retained. No new lemma, rank computation, script, plane embedding or retention theorem is approved.

LITERATURE_REASON: The new lead is the exact point-plane configuration on a quadratic cone obtained in (W5); previously inspected plane-net results do not provide its missing embedding or degeneracy analysis. This is a focused theorem comparison, not a repeated search for the unchanged generic signed-matrix method.

## Exact object to compare

The unfinished working reduction uses the three directions 16,64,70 to
parameterize all compatible quadratic assignments by 411 line values.
After the common-message gauge, (W3) is a 74528-by-408 matrix over E.
The required conclusion is full column rank for every permitted actual
labeling. These formulas are saved working reasoning, not an audited
canonical theorem or a claim that the rank has been computed.

Equivalently, any compatible assignment supplies points
A_(t,y)=[1:x_(t,y):x_(t,y)^2:d_(t,y)] on the cone Z_0 Z_2=Z_1^2.
There are 959 distinct x coordinates in H minus C. Every index
(u,v) in F_137^2 specifies a plane avoiding the cone vertex and
containing the seven points A_(t,u+tv). The 18769 indexed planes
may repeat and may contain additional design points. No plane-net,
injective message map, faithful translation action or preserved field
operation is a premise. Collapse would mean that all indexed planes
coincide. The comparison must retain these qualifications.

The approved-source references remain Alrabiah–Guruswami–Li,
[arXiv:2304.09445v3](https://arxiv.org/pdf/2304.09445v3), Definition 2.5
and Lemma 2.7 with proof, pp. 7–8; Shangguan–Tamo,
[arXiv:1911.01502v1](https://arxiv.org/pdf/1911.01502v1), Lemma 4.3's
common-root proof case, pp. 11–12; and Korchmaros–Nagy–Pace,
[arXiv:1306.5779v1](https://arxiv.org/pdf/1306.5779v1), the plane-net
statements identified above. These were assessed earlier, not reread
or extended in this turn. No unread theorem is an input.

## Relevance and bounded decision

A matching rigidity input could justify a later all-label collapse
attempt, supplying an RS-specific restriction inside every full ambient
L030 family. It would still not give a retained-family cap, compatible
laws, global transfer or 67/68 safety. The completed comparison below
does not provide that input. The direct rank route in ATTEMPTS/109 stays
parked. The newly selected planar bridge has its own assessment; its
approval must occur separately before mathematical work.

Essential local inputs are L030 and the signed/common-root methods in
L031/L047/L049; the working formulas specify the uncovered obstruction.
ATTEMPTS/109 records this bounded stop. ATTEMPTS/031–032,106–108 remain
independent limitations. Full/supporting Mathlib coverage is not checked;
no cross-notebook input or complete solution is proposed. This completed
source review establishes no new mathematical result.

## Primary-source comparison, 2026-10-27

### Cone circles and intersecting families

Sam Adriaensen, *Erdős-Ko-Rado theorems for ovoidal circle geometries
and polynomials over finite fields*,
[arXiv:2105.05815v1](https://arxiv.org/pdf/2105.05815v1), 12 May 2021,
printed p. 2, Theorems 1.2/1.4; p. 12, Remark 5.2.
The latter identifies vertex-avoiding cone sections with quadratic
graphs, extended at infinity by the leading coefficient. Theorem 1.4
bounds a pairwise-intersecting **set** of circles in an ovoidal Laguerre
plane of odd order Q by Q²; equality characterizes a full point-star.
Theorem 1.2 gives the corresponding bounded-degree polynomial result.
Statements and the coordinate identification were read; no equality-case
proof is imported.

For (W5), the coordinate swap Z_0↔Z_2 matches the displayed source
convention. Its ambient order is Q=65537 or 65537^28, never 137.
There are at most 18769 distinct section planes after removing repeated
indices, far below Q². Pairwise intersection of all distinct circles is
not a saved premise. Prescribed shared points only cover selected
auxiliary line pairs. Repetitions cannot be counted as distinct circles
to reach an extremal threshold. A common point would still not mean
equal planes. Thus this identification is useful terminology, not an
applicable collapse result.

Sam Adriaensen, *Stability of Erdős-Ko-Rado Theorems in Circle
Geometries*, [arXiv:2201.06067v1](https://arxiv.org/pdf/2201.06067v1),
16 January 2022, printed pp. 1–2, Theorem 1.3; pp. 15–16,
Proposition 5.10, Lemma 6.1 and Theorem 6.5, including their proofs.
For an intersecting circle family in a known finite circle geometry of
order Q, size at least Q²/√2+2√2Q+8 forces a common point; even
Laguerre order uses the extended plane. The proof uses zero cross-edges
for intersecting families, a mixing bound, and a large point-star.
Here Q is odd, so the nucleus exception is irrelevant. Even the maximum
18769 distinct indexed circles is below Q, hence below that threshold.
No pairwise-intersection or point-star premise is supplied. Neither the
theorem nor those proof steps give weighted/repeated-circle rigidity or
the desired equality of all planes. The repository PDF request failed,
but the pinned arXiv primary text and relevant proof were accessible;
this is not a persistent source blocker.

Matthew R. Brown, *Finite Laguerre geometries and generalized
quadrangles*, *RIMS Kôkyûroku* 1476 (2006), 205–213,
[primary proceedings PDF](https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1476-27.pdf),
pp. 205–207, Section 1, Definitions 1.1/1.2/1.4 and Theorem 1.5.
The cone model and local derived affine-plane description were read.
This concerns the full circle plane and a residue at a fixed point;
it supplies no theorem that an arbitrary selected collection of section
planes contains such a residue or collapses. In particular, deriving a
plane at one cone point does not turn planes avoiding that point into
lines of a common planar net. The printed Definition 1.4 says circles
“not incident” with the point, while its following explanation uses
incident circles; that wording is not imported as an unchecked bridge.
A later repeat fetch timed out; the initially retrieved relevant pages
were readable. Later generalized-quadrangle results were not inspected
and are not inputs.

### Extra incidences versus repeated components

Gábor Korchmáros and Gábor P. Nagy, *Group-labeled light dual
multinets in the projective plane (with Appendix)*,
[arXiv:1710.00172v1](https://arxiv.org/pdf/1710.00172v1),
30 September 2017, pp. 1–4, Introduction, Definition 2.1 and
Lemmas 2.2/2.4/2.5; pp. 8–10, cyclic setup and Proposition 4.5
with proof; pp. 14–15, Theorem 1.1 proof and its case reduction.
A light multinet has injective component maps, with disjoint components
as stipulated in the introduction, and prescribed group-product triples
collinear; additional collinearities are allowed. Over an algebraically
closed field of characteristic zero or p>n, Theorem 1.1 requires a line
meeting each component at least nine times. It allows the all-collinear
case, a length-three line, or the listed triangular/tetrahedral/conic-line
types. Proposition 4.5 makes cyclic light multinets algebraic. Its
Lamé-configuration proof explicitly uses distinct component points and
controls coincident lines. References underlying the dual-net cases
were not reread; no classification is applied here. Although 65537>137,
the required planar maps, injectivity, separation and any long line
remain unproved. This refines the old net objection without resolving it.

Norbert Bogya and Gábor P. Nagy, *Light dual multinets of order six
in the projective plane*,
[arXiv:1810.00416v1](https://arxiv.org/pdf/1810.00416v1), arXiv label
30 September 2018, retrieved manuscript internally dated 30 June 2021:
Introduction, pp. 1–2, and Section 5.1, Definition 5.1, p. 8.
A weak projective embedding over a field extension is still injective
and plane-spanning, and preserves designated collinear triples; it can
introduce extra collinearities. The order-six characteristic-zero
classification described in the introduction does not cover order 137.
Its computational classification and appendices were not read or run.
This definition confirms that “weak” does not authorize identifying
different component points. No theorem in this source removes the
coincident-evaluation-line gap.

## Bounded search record and decision

Queries included:

- `Laguerre plane quadratic cone embedded nets rigidity theorem finite field`
- `"dual 3-nets" "cone"`; `"Laguerre plane" "subnet"`
- `"Laguerre planes" "embedding" "nets"`
- `"Erdős-Ko-Rado theorems for ovoidal circle geometries" arxiv`
- `"Stability of Erdős–Ko–Rado theorems in circle geometries" arxiv`
- `"quadratic cone" "net" "finite" embedding rigidity planes`
- `"light dual multinets" finite field`; `"weak" "3-net" "projective plane" embedding`
- `"noninjective" "dual multinet"`; `"non-injective" "multinets"`
- `"dual multinet" "cyclic" "prime"`; `"quadratic polynomials" "nets" rigidity`

The Cambridge chapter *Flocks and partial flocks of the quadratic cone
in PG(3,q)* appeared as a lead for disjoint sections; only its search
extract was seen, so its theorems remain unread and are not coverage. Real
differential-geometric conical nets and algebraic nets of quadrics concern
different objects; search hits alone provide no coverage. The inspected
finite-circle and weak-multinet statements above are the load-bearing
comparison, not search snippets. No universal absence or novelty claim
is made.

The main gap remains arbitrary-center 67/68 safety. Direct circle-EKR
and circle-stability import fails the stated hypotheses/threshold and
would have the wrong conclusion. The next independently testable
intermediate target isolates the planar coefficient-span-two bridge,
using light multinets rather than requiring the absence of all extra
incidences. A successful bridge could enable a later conditional
classification argument; it would not settle coefficient span three,
deletion to 1532496, compatible laws or RS transfer. Continue only after
separate approval and only with a complete treatment of repetitions and
exceptional evaluations; a permitted obstruction or an unclosed
degeneracy must be saved rather than assumed away. See the new
`2026-10-27-span-two-light-multinet-bridge.md` assessment for the exact
proposed test. No lemma, script, DAG edge or main proof changed.
