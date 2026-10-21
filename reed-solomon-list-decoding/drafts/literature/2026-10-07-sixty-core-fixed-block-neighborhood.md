# Fixed-block neighborhood — completed source comparison

TARGET: Review source coverage for bounding L034's fixed-block neighborhoods of 8-sets meeting the block in exactly three points, retaining the L033 rank-two restriction.
CHECKED: 2026-10-08
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched generalized packing designs, fixed-codeword intersection neighborhoods, doubly constant-weight Johnson bounds, subgroup cubic collinearity and split polynomial pencils; checked L034/L033/L031, L029's affine proof, retained packing/rank/theta assessments and ATTEMPTS/019–021,023. No inspected result supplies a stronger finite labeled neighborhood bound; this is not a novelty claim.
SOURCE_EVIDENCE: Read Bailey–Burgess, Generalized packing designs, November 14, 2011 manuscript, Definitions 2.1.1/2.1.2 and Section 3.1, pp. 3–6 (https://www.math.mun.ca/rbailey00/papers/packings.pdf); read Agrell–Vardy–Zeger, Upper Bounds for Constant-Weight Codes, June 24, 2000 manuscript, definition (5), p. 3, Theorem 8 (37), p. 6, Theorem 32, p. 16, and Theorem 36 (142)–(145), p. 17 (https://publications.lib.chalmers.se/records/fulltext/local_14986.pdf). Reused inspected ST/AGL and recursive-theta coverage below.
COMPARISON: Ordinary neighborhoods have the assessed two-block parameters T(3,8,5,956,10); Johnson shortening ignores actual labels. The rank restriction supplies only specified edges in the distinguished-block link. Neither generic RS-rank results nor whole-pattern sparse-design bounds give the missing labeled improvement or a whole-family conversion. L029 supplies a closely related affine obstruction method, rather than the answer for these changed parameters.
GAP: A quantitative improvement using all L034 restrictions and its conversion to the 184665717 family cap remain unproved. Sharpness of the weaker pair-plus-distinguished-block graph is a concrete finite prerequisite test, not sharpness of the full admissible neighborhood.
REASON: Park direct theorem import of a stronger cap; propose one scoped affine sharpness test before attempting graph optimization. Its new ready assessment needs separate supervisor approval next turn.
LITERATURE_REASON: The startup assessment was REVIEW_REQUIRED for changed 60-core, three-point-intersection neighborhood hypotheses; ordinary packing/rank coverage did not assess this quantitative target.
SCOPE: C001a's fixed actual H, any 60-core C, any admissible family I of L034, and a distinguished A in I; the neighborhood consists of B in I other than A with |A intersect B|=3. Retain ordinary pair packing and all L034 restrictions, applying L033 only when A,B,B' satisfy its complete incidence hypotheses.

The main gap is arbitrary-center 68-agreement safety. The reviewed
intermediate target is a finite bound on this explicitly specified
neighborhood. Its plausible use is a local counting inequality for the
admissible family, subsequently tested against L034's exact cap threshold.
A useful neighborhood estimate would still leave the conversion to a
whole-family cap unresolved. No such conversion is assumed here.

## Source hypotheses and applicability

Bailey–Burgess defines generalized packings using disjoint parts and
all admissible strength allocations, with componentwise block sizes.
Its bounds are unlabeled. Here the parts are A and H minus (C union A),
of sizes 8 and 956; neighbors select 3 and 5 points, respectively.
Ordinary intersection at most three supplies the strength-four property.
No theorem there imposes L033's coefficient ranks or L031's tests.

AVZ's definition (5) requires exact head/tail weights, unlike T'.
Use T(3,8,5,956,10): indicator words have total weight eight and minimum
distance at least ten by L034's pair condition. The source's Section VI
octant conditions hold: 8<=956, 3<=8/2, 5<=956/2. Theorem 36 (142)
shortens a positive head weight and keeps distance d; Theorem 32 removes
a zero-weight head; Theorem 8 (37) gives A(n,2w,w)=floor(n/w).
These are imported statements, with proofs omitted there. No reproof
or evaluation of their iterated finite bound was undertaken this turn.
A later exact specialization must preserve every floor and may justify
the elementary shortening/base cases for its certificate.

The primary publisher page for *Improved linear programming bound on
sizes of doubly constant-weight codes*, DOI 10.1016/j.ffa.2018.08.009,
was inspected only for its introduction and Section 5: it reports
computations at total length <=28. Its full Theorems 4,7,9,11,15 were
not accessible in the returned passage and remain unread leads, not
essential inputs or evidence of a bound at length 964. No LP claim
is imported. Split-pencil searches likewise yielded no inspected
matching theorem; no Chebotarev or character-sum assertion is used.

Reuse ST arXiv:1911.01502v1 Definition 4.1/kernel equivalence and
Lemma 4.3, PDF pp. 9–11, and AGL arXiv:2304.09445v3 Definition 2.5,
Lemma 2.7 and proof, printed pp. 7–8, from
`drafts/literature/2026-10-07-sixty-core-three-overlap-criterion.md`.
L033 already completes the required fixed-label specialization.
Neither source provides the missing finite neighborhood estimate.
Generic/random full-rank conclusions are not applicable at fixed H.
Recursive-theta coverage in `foundations/07-core-conditioned-theta-source.md`
is ready for finite graphs, but gives no quantitative value for this link;
the proposed direct independent-family test needs no new theta theorem.

## Duplicates, obstruction comparison and bounded continuation

L029's proof uses 21 pair classes on a seven-point distinguished block,
with five-point affine graphs over F_191 on 956 outside points. That
certificate stops its old conditional-link repair (ATTEMPTS/020).
It is not already a proof for the 56 triple classes of an eight-point
block. The new test changes those hypotheses and asks about the exact
ordinary neighborhood benchmark, not L028's unchanged moment row.
L030/ATTEMPTS/021 retain the stronger stop for their seven-position
quadratic families. No additional moment level on that model is proposed.
L032/ATTEMPTS/023 supplies a four-pattern witness for a different
shortened cubic construction; its avoidance failure is preserved.
The scoped duplicate search found no completed 56-slope test.

For a necessary graph relaxation retain pair-conflict edges and exactly
L033-forbidden triples containing the distinguished A. This deliberately
does not encode triples consisting only of neighbors or L031's quadruples.
They remain required in the full L034 family. A sharpness result for this
graph would park this relaxation alone, with no full-neighborhood or
whole-family extremal assertion. The precise construction and test are
in `drafts/literature/2026-10-08-affine-fixed-block-neighborhood-test.md`.
No construction proof or mathematical script was produced here.

Continue with the single affine sharpness test because it can decide
whether these particular labeled link edges improve the ordinary
benchmark. Equality would stop graph-only improvement; a violated edge
would reject this prescribed construction without proving a smaller cap.
No cap conversion, spectrum, label symmetry or uniform-core behavior is
granted. Restrictions among neighbors, L031, and other overlap types
remain separate possible mechanisms.

Essential inputs are L034, L033, L031, L001 and C001a. L029/L030 and
ATTEMPTS/019–021,023 are comparisons, not assumed constraints on this
family. The numerical cap, global conversion, cross-core consistency,
common-center realization, 67-agreement safety and ABF equivalence remain
unresolved. Matching Mathlib coverage has not been checked. This note
does not derive new mathematics and asserts no novelty. Matching full
Mathlib coverage and supporting doubly constant-weight bounds: not checked.

Queries actually issued included `"generalized packing designs" Bailey
Burgess Proposition 3.1.2 bounds`; `constant weight code fixed codeword
neighbors intersection three local bound generalized packing designs`;
`"Reed Solomon" "link" "rank" extremal triple intersections`;
`"doubly constant weight" "Johnson" upper bound`;
`"multiplicative subgroup" "cubics" "collinear" packing`;
`"generalized packing" "rank" "Reed"`; `"polynomial pencils"
"finite fields" "split"`; and `"completely split" "fibers"
"rational function" finite fields Chebotarev`. Nonmatching hits and
search snippets supplied no theorem evidence. A PDF screenshot request
failed; the complete relevant theorem formulas were readable in the
primary PDF's text extraction, so no essential blocker remains.
