# Marked-octic eleven-adic point image — source approval

TARGET: Determine the exact eleven-adic fake two-cover point image of L113's marked octic in L114's scalar quotient, retaining every factor and both infinity points.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped searches of marked-octic assessments, working records, L113–L119 and history/412–421 found no existing eleven-adic instance result; checked ATTEMPTS/050–052 and the five-adic label failure. Web queries were "275" "2860" "6930" hyperelliptic eleven; "Bruin" "Stoll" "LocalImage" eleven bad reduction; "3025" "31460" "76230" hyperelliptic; "275t" "2860" curve; and "Two-cover descent on hyperelliptic curves" correction erratum. No matching instance or relevant correction was identified; unsuccessful searches establish no novelty or absence of errata.
SOURCE_EVIDENCE: Reused the inspected primary arXiv:0803.2052v2 (21 October 2008), Section 2 p.3 and Section 4 pp.6–11, with complete Lemma 4.4 proof and SquareClasses/LocalImage explanations recorded in drafts/literature/2026-10-23-marked-octic-five-adic-point-image.md; read its full source/application record and L113–L114 hypotheses/conclusions. No essential new theorem case arises from replacing Q5 by Q11.
COMPARISON: Bruin–Stoll already gives the general exact finite-local algorithm for an integral squarefree polynomial over a characteristic-zero complete discretely valued field with finite residue field, including nonunit leading coefficient and bad reduction. The eleven-adic instance, same-theta field transports, labels and ambient comparison are not supplied by that theorem or L119.
GAP: All eleven-adic field models, norm/scalar square-class labels, exhaustive point disks and realizations remain uncomputed; source coverage for a later certified specialization is adequate.
REASON: Approve the unchanged target by known-method specialization, with no new instance result or reproof of the general algorithm.
LITERATURE_REASON: The saved REVIEW_REQUIRED target changed the finite place from five to eleven; this bounded review checks exact-instance overlap, failures and applicability while reusing ready primary-source coverage.
SCOPE: Exactly TARGET for L113's unchanged smooth proper curve over Q11, L114's entire algebra and actual fake map; includes complete local field/model certification with the same theta, full norm and common-scalar quotient, exhaustive affine/reciprocal charts, branch evaluations, both infinity points, realizations and ambient comparison. No global class/unit calculation or rational-point completeness is approved.

## Primary source reused and applicability

Import Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
curves*, Math. Comp. **78** (2009), 2347–2370,
[DOI 10.1090/S0025-5718-09-02255-8](https://doi.org/10.1090/S0025-5718-09-02255-8).
Precise references use [arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2),
21 October 2008. The existing five-adic assessment records the primary
hypotheses, complete proof cases and algorithm explanations actually
inspected. They are reused rather than retrieved again. Search-result
snippets and the author PDF discovered by search are not new theorem
extractions. No software execution or unread implementation is imported.

Section 4 p.6 assumes a characteristic-zero complete discretely valued
field with finite residue field, an integral squarefree polynomial and
its complete local factorization. Its p.8 discussion explicitly allows
nonunit leading coefficient and bad discriminant. L113 supplies the
squarefree integral octic

    G(t)=3025t^8−31460t^6+76230t^4−39204t^2+2673

and smooth proper charts. Q11 meets the field hypotheses just as Q5
does; the method does not require good reduction or monicity. L114's
leading coefficient and discriminant show that the unit-leading,
small-discriminant shortcut of Lemma 4.3 cannot justify this target.
Do not remove the factor 11 from G or substitute a different twist.
This is a hypothesis comparison, not a new local factorization.

Section 2 p.3 defines the actual even-degree target

    H_Q11={delta in A11*/(A11*² Q11*): N(delta) in 3025 Q11*²},
    A11=Q11[t]/(G), theta=t mod G.

Use [x−theta] for ordinary points, the invertible branch replacement
[(a−theta)+G_tilde(theta)] when G=(t−a)G_tilde, and the identity
for each of the two distinct infinity points, as fixed by L114.
Only one common Q11 scalar is quotiented out; component scalars
cannot be removed independently. Point images need not be subgroups.

Lemma 4.4 p.8 supplies strict coefficient-valuation sufficient bounds
for constant classes, including ramified fields and nonintegral theta.
SquareClasses pp.9–10 supplies all residue children, rejection tests,
both terminal cases (resolved factors or one remaining linear factor),
realization and termination. The odd-residue precision case applies;
no uniform depth or instance bound is imported. LocalImage pp.10–11
covers integral x and the reciprocal chart q in 11 Z11, with the
q(1−q theta) expression, auxiliary factor at q=0 and separate infinity
rows. Its explanation ad 2 requires the subsequent common-scalar
projection. The earlier assessment includes all these proof cases;
there is no essential unread eleven-specific theorem.

## Duplicate and failure comparison

L119 is a five-adic calculation and audit, not an eleven-adic theorem.
Its exact fields, transports, norm bits, labels and disk bounds do not
transfer. Its preserved initial lexicographic/normalized-label mismatch
requires a declared canonical scalar-orbit convention and explicit
collision checks in a later calculation. L118 supplies only a real
filter. L113–L114 supply model and map, not this local image.

No L117 proof is imported in this review. If a later calculation uses
its eleven-prime data, it must read and justify that precise input;
ramification/residue degrees alone neither identify a local field nor
transport theta or square classes. Direct local model certification
from G is permitted within the target without a global class backend.
ATTEMPTS/052's persistent backend blocker therefore does not block this
independent local calculation. ATTEMPTS/050's bounded rank detector and
ATTEMPTS/051's false rank-zero target use different mechanisms and do
not settle this point image. Preserve those stops and unfinished L108.

## Relevance, discriminating test and limits

The main gap is global rational/integer point control. This intermediate
image could give a membership test on future supported representatives;
no complete global route is assumed. Continue a later mathematical
step only with complete actual fields and same-theta transports,
certified square/norm labels in the full scalar quotient, exhaustive
charts, strict bounds, exact realizations and both infinity rows.
Compare the result with the entire norm-admissible ambient set in that
same quotient. Properness supports pruning; equality stops extra
pruning at eleven. Missing factors, undecided disks, unrealized labels
or a computation cap leave exactness unresolved rather than proving
an exclusion. No ambient or image cardinality is asserted here.

Known rational infinity points prevent an empty fake-Selmer-set route.
Supported units, ordinary S-class two-torsion, other local images,
surviving-cover points, degree-nine root recovery, remaining factors,
both L095 systems and minus-eleven remain open. Mathlib coverage of
the full local algorithm is not checked; no absence claim is made.
The general theorem is cited, not reproved. SPECIALIZE permits a later
REPRODUCTION of this instance, with no originality claim. This source
review changes no lemma, mathematical script, PROOF.md or DAG.md.
