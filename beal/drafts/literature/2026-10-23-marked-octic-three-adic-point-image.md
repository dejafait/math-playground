# Marked-octic three-adic point image — source approval

TARGET: Determine the exact three-adic fake two-cover point image of L113's marked octic in L114's scalar quotient, retaining every factor and both infinity points.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched marked-octic assessments and history/410–425 for three-adic, Q3, Q_3, 3-adic and LocalImage; read ATTEMPTS/050–052 and the five-adic label-failure record. Web queries were "275" "2860" "6930" "243" hyperelliptic; "Bruin" "Stoll" "two-cover" "3-adic"; "3025" "31460" hyperelliptic; "275" "2860" "6930" "three"; and "Bruin" "Stoll" "LocalImage" "3". No matching instance result was identified; no novelty or exhaustive absence claim follows.
SOURCE_EVIDENCE: Reused the complete inspected primary extraction in drafts/literature/2026-10-23-marked-octic-five-adic-point-image.md: Bruin–Stoll arXiv:0803.2052v2 (21 October 2008), Section 2 p.3 and Section 4 pp.6–11, including complete Lemma 4.4 proof and all SquareClasses/LocalImage explanations. Read that entire assessment and relevant L113/L114 hypotheses, conclusions and smooth charts. No primary PDF was newly retrieved and no essential unread source case was identified.
COMPARISON: Section 4 covers integral squarefree polynomials over characteristic-zero local fields with finite residue field, including bad reduction and ramified factors. The change from Q5 to Q3 stays within those inspected hypotheses. It provides an algorithm, not this octic's image; L119/L120 provide only other-place comparisons.
GAP: Exact Q3 field models and theta transports, square/norm/scalar labels, exhaustive chart coverage, exceptional evaluations, realizations and comparison with the full norm-admissible quotient remain uncomputed.
REASON: Source coverage now suffices for one later mathematical specialization of the known algorithm; this independent membership test needs no parked global class backend and does not reopen the eleven-adic equality stop.
LITERATURE_REASON: Startup REVIEW_REQUIRED requires a separate exact-instance and changed-place comparison; reuse the ready primary extraction rather than repeat its theorem retrieval.
SCOPE: Exactly TARGET on L113's unchanged smooth proper curve over Q3 and L114's entire even-degree scalar quotient, including certified local models, square/norm labels, both coordinate charts, branch evaluations, two infinity rows and realizations. Global supported arithmetic and other places are outside this approval.

## Primary source and applicability

Import Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
curves*, Math. Comp. **78** (2009), 2347–2370,
[DOI 10.1090/S0025-5718-09-02255-8](https://doi.org/10.1090/S0025-5718-09-02255-8).
Page references use [arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2),
21 October 2008. The full prior extraction is retained in
[the five-adic assessment](2026-10-23-marked-octic-five-adic-point-image.md);
its primary statements and proof cases are reused, not newly retrieved.
The web search found the author's paper and references to it, but no
separate exact-instance theorem. Search snippets are not theorem evidence.

Section 4 p.6 assumes a complete discretely valued characteristic-zero
field with finite residue field, an integral squarefree polynomial, and
its complete irreducible factorization. L113 supplies the smooth proper
model and squarefreeness of

    G(t)=3025t^8−31460t^6+76230t^4−39204t^2+2673.

These are precisely the required polynomial hypotheses over Q3. L114
supplies the discriminant and actual fake map. The discriminant valuation
27 at three fails the small-discriminant premise of Lemma 4.3; its
unramified-image shortcut is therefore not approved. Section 4 p.8 and
the recursive algorithm expressly cover bad polynomial reduction and
ramified factors. They require neither good reduction nor a maximal
polynomial order. No Q3 local decomposition is inferred here.

Section 2 p.3 gives the even-degree target

    H_3={delta in A_3*/(A_3*² Q3*): N(delta) in 3025 Q3*²},
    A_3=Q3[t]/(G), theta=t mod G.

For an ordinary affine point use [t−theta]. If a rational branch a
occurs, write G=(t−a)G_tilde and use the invertible representative
[(a−theta)+G_tilde(theta)]. L114 already evaluates each distinct infinity
point as [3025]=[1]. No affine zero evaluation replaces either row.
The quotient uses one common embedded rational scalar, not independent
scalars in each factor. No subgroup property of the point image is
assumed.

## Approved execution and completeness obligations

Lemma 4.4 p.8, with its complete proof as previously extracted, gives a
sufficient constant-class disk bound from a strict coefficient-minimum
valuation inequality for each irreducible factor. Its additional ord(4)
precision is zero at three, as in the already inspected odd-residue case.
This does not supply any universal disk depth or this instance's bounds.
All actual field transports and all factor inequalities must be certified
in the later mathematical attempt; the general lemma needs no reproof.

SquareClasses pp.9–10 recursively retains every residue child, rejects
only certified nonsquare disks, and terminates using the stated strict
bounds. Explanations ad 8 and ad 11 distinguish the closed constant-class
case, with realization, from the unresolved linear-factor case covered
by a branch evaluation; other unresolved cases must be refined. All
these cases were inspected in the reused extraction. LocalImage pp.10–11
covers integral t and the reciprocal chart q=1/t in 3 Z3. Its even-degree
reciprocal representative is q(1−q theta); its auxiliary factor prevents
invalid evaluation at q=0. Insert both infinity rows separately.
Compute square classes first and then their common-scalar projection,
retaining every collision. A rigorously compressed disk organization
is allowed only with exhaustive coverage and the same precision and
realization guarantees; a finite sample is insufficient.

Certify the entire Q3 algebra, transported theta and scalar embedding,
complete square-class equality tests and norms. L117 is not an assumed
input: if its data are used later, read the full relevant statement and
justify its arithmetic transport. Local residue degrees alone are not
field models. Preserve the five-adic convention failure: lexicographic
orbit labels and a chosen normalized section need not coincide, so
state and verify a single label convention before comparing images.
The new Q3 computation is needed because neither the general paper nor
L119/L120 supplies its instance image, ambient quotient or realizations.
This is a specialization of known methods, not a proposed general lemma.
Mathlib coverage of the full algorithm is not checked; no absence claim
is made. No external code execution or implementation is imported.

## Relevance, test and limitations

The main gap remains global supported class/unit arithmetic and
rational/integer point control. This intermediate exact local image
could provide a membership test on later global supported representatives.
Its outcome is independent of eleven's confirmed singleton equality and
of the parked global class backend. Compare its exact image with the full
norm-admissible ambient in the same scalar quotient. Properness supports
a filter; equality stops extra fake-class pruning at three. Unclosed
disks, uncertified transports or unrealized labels leave the image
unresolved. No local cardinality alone removes an identified global class
or proves rational-point completeness or either integer exclusion.

ATTEMPTS/050's bounded genus-two detector and ATTEMPTS/051's false
rank-zero premise are different mechanisms. ATTEMPTS/052's missing
certified backend blocks global class execution, not this local proof
method. Do not repeat backend probes or reopen the eleven-adic stop.
Supported units, ordinary S-class two-torsion, surviving-cover points,
degree-nine root recovery, remaining factors, both L095 systems and
minus-eleven remain unresolved. Preserve unfinished L108. Known boundary
points prevent an empty fake-Selmer-set shortcut. No cross-notebook input
is proposed.

The unchanged TARGET is ready for a separate REPRODUCTION research turn.
This literature-only comparison establishes source applicability, not a
Q3 image or progress beyond the known method; no new mathematics, lemma,
mathematical script, DAG edge or argument assembly was written.
