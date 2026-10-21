# Proposed attainability test for the isolated-anchor cubic bound

TARGET: Determine whether L066's bound of three both-zero recoveries coexisting with one full isolated disjoint-P triangle anchor is attainable.
CHECKED: 2026-10-13
DECISION: EXPLORE
SEARCH_EVIDENCE: Five target-specific searches on 2026-10-13, listed below; inspected L057's full recovery statement, L065's classification and both quadratic branches, L066's determinant/anchor argument, L068's witness and separate audit, ATTEMPTS/025 and 029, and existing ingredient assessments; no matching sharpness result identified in the inspected coverage.
SOURCE_EVIDENCE: Reused Hall Theorem 5.1.1/interpolation pp. 63–65 and Marquez-Corbella–Pellikaan section 5 Lemma 5.3/shortening pp. 7–8; freshly read Chojecki author TeX v9.2 DR0–DR8/DRC, lines 2785–2935, including full proofs and zero-direction cases; bounded local certificate fields and verifier code distinguish projected both-zero diagnostics from actual recoveries.
COMPARISON: The sources supply GRS and complete recurrence membership ingredients, not attainment of L066's bound; L065 describes split-net candidates but requires restored lifts, and audited L068 proves isolated witnesses only. The saved dependent-quadratic regression supplies a concrete finite support family, not an attainability result.
GAP: Find three distinct actual finite both-zero recoveries at weights supplied by a full isolated disjoint-P anchor, or close the specified fixed-assignment witness test without extrapolating to arbitrary labels; determinant roots and projected net membership remain insufficient.
REASON: Completed discovery and theorem comparison justify one bounded mixed-recovery witness test using audited exact criteria; approve the unchanged TARGET with the concrete test below, without claiming a sharpness theorem or certified novelty.
SCOPE: Fixed H of order sixteen over F_(97^20), arbitrary nine distinct triangle labels and admissible L057 weights and original charts; one full isolated anchor disjoint from P, and three distinct actual additional finite both-zero parameters allowing zero fourth weights, exactly as in L066.
LITERATURE_REASON: The new sharpness question concerns actual split-net recoveries, beyond the already approved proof of the cubic upper bound and the completed fixed-label isolated-row audit.

The main gap remains the uniform triangle twelve bound and arbitrary
sixteen-count equality-family exclusion. This intermediate question
tests whether the both-zero contribution in L066's necessary profile
can be reduced. A witness would establish that this particular local
bound cannot be sharpened; a rigorous universal exclusion would tighten
that profile. Neither outcome alone resolves the main gap, extraction,
other triangle patterns or the challenge-definition qualifications.

Essential inputs to assess are L057, L065 and L066. Inspect the existing
L068 witness and its completed audit only as a possible duplicate or
comparison, not as an assumed three-both-zero example. Reuse existing
recurrence/GRS source coverage if its hypotheses suffice. Search exact
sharpness terminology and check the recorded formal-root/sampling stop
in ATTEMPTS/025 before approving any test. The fixed-label stop in
ATTEMPTS/029 remains; no larger isolated-anchor label sweep is proposed.

Continuation/abandonment test: coverage must justify either a concrete
full-moment witness test for three distinct both-zero parameters plus
the full isolated anchor, or a specified uniform obstruction to that
configuration. Every successful determinant root still needs a split
four-support, all restored equations, original finite gates and scalar
deduplication. A root count, sample with fewer than three, or replay of
L066's upper-bound proof does not settle attainability. If no such
bounded test is justified, reassess before calculations. No equality,
rational original chart, full weight on the both-zero recoveries or
sufficiency of the determinant is assumed. The preceding text preserves the startup proposal; the completed
comparison and approved bounded test follow below.


## Completed source comparison — step 191

This is a LITERATURE-only step. The target and full mathematical scope
remain unchanged; no new bound, witness, proof audit or calculation was
performed. The main gap is the uniform triangle twelve bound, within the
arbitrary equality-family gap. Attainment would prevent sharpening L066's
both-zero term by itself; a uniform strict obstruction could strengthen
its necessary profile. Independent isolated-count, extraction, other
patterns and challenge-definition gaps remain unresolved.

### Discovery and primary theorem comparison

Queries issued on 2026-10-13:

- `"Reed Solomon" "quartic net" recoveries`
- `"Shortening Bounds for Reed–Solomon MCA" sharpness`
- `"Reed-Solomon" "isolated" "both-zero"`
- `"Reed-Solomon" "quadratic pencil" sharp bound`
- `"Reed-Solomon" "quartic" "net" sharpness`

The returned author-repository lead was followed to the primary TeX.
Search snippets, mirrors, unrelated decoding results and broad prize
submission summaries were not treated as theorem evidence. No matching
attainment theorem was identified by these searches; this is bounded
coverage, not an originality claim. The primary text search for `quartic`
had no match, which alone would not establish absence of a relevant result.

Reuse the completed ingredient comparisons in
`2026-10-11-triangle-both-zero-classification-audit.md` and
`2026-10-11-triangle-isolated-net-bound-audit.md`:
J. I. Hall, *Notes on Coding Theory*, author-hosted
[GRS chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
Theorem 5.1.1 and proof, printed pp. 63–64, interpolation p. 65;
I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
[accepted manuscript 2016-02-29](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
section 5, Lemma 5.3 and following GRS shortening formula, pp. 7–8.
Their distinct-node/nonzero-multiplier hypotheses and the seven
shortenings supplying Q are unchanged. They provide ingredients rather
than this net's simultaneous recovery count. No general reproof is needed.
The Manin/QRT lead in the earlier assessment remains abstract-only and
unused; curve-pencil terminology does not establish split RS recoveries.

Freshly inspected P. Chojecki, *Shortening Bounds for Reed–Solomon MCA*,
[author TeX v9.2](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex),
version header as recorded July 17, 2026, retrieved October 13;
DR0–DR8/DRC, lines 2785–2935, including both proofs. This is mutable
source, not a certified identification with ePrint 2026/1463. DR2 assumes
distinct weighted Vandermonde columns, nonzero multipliers and t<R.
L057's R=8,t=4,multiplier x specialization satisfies those hypotheses
since H is distinct and nonzero. It covers arbitrary extension-field
syndromes. DR6–DRC test the full recurrence direction and retain its
zero-direction case; they do not identify a zero *projected* pair with
a full common intersection, and do not assert attainment of three.
This source import remains in canonical L057; this review adds no lemma
or reproof. L057's shared-column restoration is still essential.

### Local duplicates and failures

L066's audited conclusion is an upper bound, not an existence result.
Its determinant roots are necessary; its proof explicitly withholds
splitting, recovered weights and finite gates from those roots. L065's
independent-quadratic and dependent-quadratic classifications give actual
split support candidates, but neither claims simultaneous attainment.
L057 equations (9)–(14) supply the exact pivot, restored equations,
weights and finite change of scalar for both branches.

Audited L068 provides five isolated anchors for a different assignment.
Its saved verifier classifies zero projected pairs as
`both_zero_not_counted_as_isolated` without solving their lift in that
branch. Thus neither its diagnostic rows nor its five witnesses settle
this question. No complete mixed-count result was identified in these
scoped records. L080 and ATTEMPTS/029 stop four simultaneous isolated
anchors for L068's fixed labeling, not a mixed both-zero test on another
specified labeling. ATTEMPTS/025 stops unstructured label samples and
formal common-root repetition. Its warning remains: a failed selected
assignment cannot imply a uniform exclusion.

Inspected exact selected fields in
`scripts/triangle-recovery/both-zero-interpolation-check.json`:
case 1 has P=(18,22,27), ordered pairs Y=(1,96), Z=(8,89), W=(12,85),
and recorded double fibers (33,64) and (47,50).
These fields nominate an existing dependent-branch regression for a
future test. They are not a replay or proof of its fiber classification;
L065 is the audited mathematical classification, and the next test must
reconstruct its own complete support set. The existing regression tests
projected/net membership only, with no actual mixed-recovery count.

### Approved bounded test and stopping rule

Approve exactly TARGET for one subsequent RESEARCH calculation, initially
on that single saved dependent-branch assignment. Reconstruct all 715
four-subsets of H minus P. Use L057 (5)–(14) to generate every isolated
disjoint-P anchor's unique p,q,r, retain (3), and require all four anchor
weights nonzero. Deduplicate weight points while preserving anchor
witnesses. At each retained point, solve the full both-zero pivot/lift
for every both-zero support from L065, including the two-original-pair
rejections, and deduplicate actual eligible scalars. Retain zero fourth
weights on the both-zero side. This is a proposed calculation, not one
executed in this source review.

For any three-scalar success, choose and explicitly verify one admissible
original chart that keeps the anchor and all three parameters finite and
outside the three bases. Do not silently use gamma=(0,1,2) if it deletes
a needed scalar. Verify all eight original moments, every weight and
finite gate, and same-support input failure using L057 or a direct
interpolation certificate. A nonprime chart, if used, requires an explicit
field representation and exact checks. No rational original chart is
assumed. L057 already states that a full isolated disjoint-P anchor forces
normalized weights into F_97; that does not descend the original chart.

Success threshold: three distinct eligible both-zero parameters plus one
full isolated disjoint-P parameter, in one actual pencil. This establishes
attainment under L066, not a violation of twelve. If the complete fixed
assignment has no such weight point, preserve that restricted obstruction
and abandon this assignment; do not broaden the label sweep automatically
or claim nonattainment uniformly. If no full anchor exists, record that
failure too. An unread essential theorem or failed exact formula bridge
stops dependent calculations for repair/review. This test differs from
ATTEMPTS/025 by fully covering one structurally nominated split-net family
and testing actual mixed attainability, rather than sampling for a uniform
seven-scalar maximum. The overall attainability question can remain open.

Full matching and supporting Mathlib coverage remain not checked in this
review; no absence or formal-verification claim is made. This approval
supplies source readiness, not a new mathematical input beyond the audited
local results. No lemma, mathematical script, DAG or PROOF.md was changed.
