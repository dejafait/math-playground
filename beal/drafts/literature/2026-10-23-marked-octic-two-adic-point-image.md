# Marked-octic two-adic fake point image — source approval

TARGET: Determine the exact two-adic fake point image of L113's marked octic in L114's full norm-admissible common scalar quotient, with exhaustive charts and both infinity evaluations.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped marked-octic/dyadic text and filename searches in drafts/literature, history, ATTEMPTS, lemmas and scripts/pair-genus-two found only this proposal and history/429, not a duplicate computation. Web queries were "3025" "31460" hyperelliptic; "275" "2860" "6930" "descent"; and Bruin Stoll two cover descent hyperelliptic dyadic SquareClasses errata. No exact-instance result was identified; unsuccessful search is not evidence of novelty.
SOURCE_EVIDENCE: Reused the complete Section 2/4 extraction in drafts/literature/2026-10-23-marked-octic-five-adic-point-image.md; directly reread Bruin–Stoll arXiv:0803.2052v2 Section 4 opening p.6, dyadic discussion and Lemma 4.4 with full proof p.8, all SquareClasses steps/explanations pp.9–10 and all LocalImage steps/explanations pp.10–11. Read L113's model hypotheses and L114's map and infinity evaluations; retained ATTEMPTS/050–052.
COMPARISON: The inspected general algorithm expressly covers dyadic fields and bad polynomial reduction. Its two extra base-field digits and both terminal cases cover the changed precision issue; the remaining work is a certified instance execution, not a missing general theorem. Neither this source nor the inspected local records provides the octic's Q2 image, complete local models or ambient quotient.
GAP: Exact full Q2 factor models with theta/scalar transport, complete square/norm/common-scalar tables, exhaustive chart bounds and realizations remain to be computed. Global supported class/unit arithmetic and rational/integer point control remain independent gaps.
REASON: Coverage now suffices for one later reproduction of the known local algorithm on the unchanged model; no mathematical calculation or new lemma is performed in this review.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED; residue characteristic changed to two, requiring the previously unapproved dyadic precision and terminal-case comparison.
SCOPE: Exactly TARGET on L113's unchanged smooth proper curve over Q2 and L114's entire even-degree quotient; includes certified full local factor models, square/norm labels, one common scalar image, exhaustive finite/reciprocal charts, branch cases, both infinity rows and realizations. L116/L117 are not assumed inputs; no global arithmetic, other-place calculation or point-completeness claim is approved.

## Citation and inspected dyadic cases

Import Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
curves*, Math. Comp. **78** (2009), 2347–2370,
[DOI 10.1090/S0025-5718-09-02255-8](https://doi.org/10.1090/S0025-5718-09-02255-8).
Page references use [arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2),
21 October 2008. Reuse the prior detailed extraction linked above.

Section 4 assumes a characteristic-zero complete discretely valued field
with finite residue field, an integral squarefree polynomial and its full
irreducible factorization. Even residue characteristic is explicitly included.
Lemma 4.3's odd-residue shortcut is unavailable.

Lemma 4.4 p.8 assumes irreducible g and the strict coefficient-minimum
inequality ord(g(x0+epsilon*pi^e)−g(x0))>ord(g(x0)); it gives constant
square class on x0+pi^(e+ord(4))O. Its full proof includes ramified
extensions. SquareClasses step 7 and explanations ad 6–8 require the
extra ord(4) digits after the last factor transition. At Q2 this is two,
not zero. Step 4 uses finite-ring unit-square tests to precision at most
ord(4)+1. Ad 8 distinguishes a closed constant-class disk with an actual
point from one unresolved linear factor covered by its branch image;
ad 11 requires further refinement otherwise. LocalImage covers integral
coordinates and the reciprocal chart, inserts infinity, and projects raw
classes by the common scalar group. These are imported algorithm cases,
not an execution or reproof here.

## Instance comparison and execution contract

Use precisely the supplied L113 model

    G(t)=3025t^8−31460t^6+76230t^4−39204t^2+2673,
    Y²=G(t),  A_2=Q2[t]/(G),  theta=t mod G.

L113 supplies degree eight, squarefreeness and smooth proper charts;
L114 supplies the actual fake map. Thus the polynomial hypotheses hold
over Q2. L114's discriminant valuation 72 and residue characteristic two
prevent the shortcut independently. Do not change the twist to G/11.
No factorization or field identification is inferred in this review.

The required comparison is with the entire

    H_2={delta in A_2*/(A_2*² Q2*): N(delta) in 3025 Q2*²}.

This is L114's definition, not a new norm reduction. Every field factor,
the actual theta and the single embedded rational scalar must be retained.
A later computation must certify complete square-class equality tests,
norms and scalar transports before comparing the image with H_2. Neither
positive valuation nor residue-field square tests alone certify a dyadic
square. Specify valuation normalization in every ramified factor and
report actual versus required precision. A finite-precision root or
prime degree list alone cannot define a field or theta transport.

Execute the approved recursive method, or give a rigorously exhaustive
compression of its disks and infinite tail. Certify each rejection,
each constant-class bound and every claimed class realization. Close
both t in Z2 and q=1/t in 2 Z2, retaining any rational branch evaluations.
The reciprocal affine representative is L114's q(1−q theta); at q=0
use its separate infinity convention. Keep both distinct rows Z=−55
and Z=55 with image [1], as already proved in L114. Their equality of
images does not merge the points or permit an empty-image conclusion.

This approval imports no external implementation and requires no parked
global backend. If a later attempt uses L116/L117 rather than constructing
local models directly, first read the complete relevant canonical proof
and justify the full local transport; their uninspected arithmetic is not
an input here. Preserve L119's recorded quotient-label convention failure:
choose and verify one labeling convention and retain every collision.
The point image must be computed as a set before any subgroup claim.
Mathlib coverage of this full algorithm and exact instance is unchecked.

## Relevance, bounded test and remaining gaps

The main gap is global supported class/unit arithmetic and rational/
integer point control. This intermediate membership test could filter
later supported representatives; it need not settle those independent
gaps to be useful. Properness versus the full H_2 supports extra pruning;
equality stops that local pruning mechanism. Unclosed disks, uncertified
models, incomplete square-class tables or unrealized labels leave the
exact image unresolved. No ambient or image size is asserted here.

The source already supplies the general method. A later REPRODUCTION
must establish its instance data; citing the algorithm alone cannot do
so. The exact-instance search provides no claim of originality or of
progress beyond the checked sources. L119–L121 treat other primes and
do not settle this target. Preserve the three-/eleven-adic equality stops,
ATTEMPTS/050–052, unfinished L108 and the restriction against backend
probes. Supported units, ordinary S-class two-torsion, surviving-cover
points, degree-nine rational-root recovery, compatible remaining factors,
both L095 systems and minus-eleven remain unresolved.
