# Common-five-label recovery cluster — completed source comparison

TARGET: Bound the number of additional recoveries by twelve for a gated L057 triangle containing two distinct full-weight additional recoveries whose supports have union size five.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Six bounded exact-support, affine-syndrome and projective-coset queries; read full L015 and ATTEMPTS/007,025,026, its original test/history and the complete finite-configuration producer/verifier paths; reused ready L057 recurrence and general triangle-count comparisons.
SOURCE_EVIDENCE: Hall, Notes on Coding Theory, GRS chapter, Theorem 5.1.1 and complete proof, printed pp. 63–64, undated author PDF retrieved 2026-10-11; canonical L015's complete analytic reduction and certificate specification; inspected selected saved certificate fields, without replay; reused primary recurrence/shortening extractions cited below.
COMPARISON: L015 already states the five-coordinate total-bad-set bound 5+M(A), including the two-full-error union-five reduction, arbitrary extension-field weights and finite charts. Its recorded maximum six is stronger than needed if certified, but is computational evidence rather than an unconditional numerical conclusion of L015. No new cluster mechanism needs to be invented.
GAP: Apply the existing reduction to the exact L057 recovery set and validate the complete finite upper-bound certificate, preserving scalar deduplication, all lower-weight and both-zero cases and the three base parameters; the conditional twelve bound is not proved in this review.
REASON: Known local coverage changes the route from new support-concentration research to a bounded application/certificate check. SPECIALIZE approves only this applicability and verification difference, without reproving L015, importing its unaudited numerical maximum or claiming originality.
SCOPE: F=F_(97^20), fixed H, arbitrary gated L057 labels and normalized weights, arbitrary original gamma_i and lambda; two distinct additional finite parameters with full four-error supports having union size five. The desired bound counts all additional recoveries, including both-zero and lower-weight cases, with scalar deduplication and the original finite exclusions.
LITERATURE_REASON: The changed common-five-label target was REVIEW_REQUIRED; its exact overlap with L015 and computational count obligations had not been assessed. Existing recurrence and general MCA assessments are reused.

## Exact local overlap and remaining application obligations

Read L015 in full, L010 through its complete kernel, distance,
uniqueness, locator and same-support passages, L041's local converse
and standard-input specialization, and L057's complete statement and
imported recurrence passage. L057 explicitly supplies independent
coefficient syndromes, nonzero D and nonzero coordinate-locator
polynomials in the original finite chart. Its three base events are
full, distinct and finite; it retains initially zero fourth weights.

L015 assumes exactly the same F and H and the pinned four-omission
event. Its final paragraph already treats two full four-errors at
distinct parameters whose supports intersect in three labels: their
union supplies its five-set A. Its conclusion concerns the total
original bad set B, rather than just isolated, disjoint-P or additional
supports. The analytic proof includes coordinate cancellations,
lower-weight representatives, distinct external configuration points,
and extension-field projective lines. In particular, the line is
descended only when it contains two rational configuration points;
the original affine chart is never declared rational. These are
existing L015 claims to use and check, not new derivations here.

The numerical distinction is essential. L015 proves |B|<=5+M(A);
it does not prove M(A)<=6 analytically. A total count at most fifteen
would suffice for twelve additional parameters after the three base
events. Thus even a certified M(A)<=10 would meet the needed threshold.
The saved maximum six would give a stronger total bound, but no such
application is established in this literature turn. The next attempt
must justify that every counted relaxed L057 parameter lies in this
same B, count parameters rather than witnesses, and remove the three
distinct base events exactly once. Both-zero quotient lifts must not
be discarded. No universal cluster extraction is assumed.

## Certificate scope and verification obligation

Read `scripts/coefficient-feasibility/five_coordinate_lines.cpp` in
full and the Python verifier's `point_configuration`, `line_key`,
`on_line`, `verify_record`, `independent_configuration_check` and
`main`. The saved original test is
`drafts/2026-10-04-five-coordinate-constrained-test.md`, with history
023 and ATTEMPTS/007. The producer enumerates all 330 external
four-support points for each of 273 multiplicative five-set orbits
and all 54,285 pairs per configuration. It groups normalized ten-minor
keys and converts pair multiplicities to line sizes. The verifier
checks all 4,368 five-sets are covered without orbit duplication,
every stored maximal line by full point membership and histogram
totals, but independently recounts every line for just mask 539.
Checking a stored maximal line proves its attained size, not that
every other line is smaller; the complete producer census remains
load-bearing for the upper bound.

Used the supervisor JSON inspector on these exact fields of
`scripts/coefficient-feasibility/five-coordinate-result.json`:
`/maximum_external_points` is 6;
`/orbit_maximum_histogram` is {5:265,6:8};
`/independent_complete_configuration_check` records mask 539,
54,285 pairs and maximum 6. These selected complete values identify
the saved claim and its independence limitation; they do not verify
all 273 configurations. No mathematical program was run, no JSONL
coverage was asserted from a preview, and no certificate was rewritten.

A ready bounded attempt may audit/replay the complete producer census
and orbit coverage, preferably check every orbit by a different line
membership/count path, and apply L015 if the resulting bound is <=10.
It should save full evidence and preserve the original certificates.
There is no need to rerun selected actual-pencil/L013 root audits:
those witnesses are not premises of this universal configuration bound.
No arbitrary-triangle or extension-weight sweep is authorized by this
assessment. Failure of the upper-bound certificate or a count above
ten requires recording the exact failed obligation, not inventing a
replacement lemma or claiming the target false from a configuration.

## Primary ingredients, stronger results and bounded searches

J. I. Hall, *Notes on Coding Theory*,
[author-hosted GRS chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
Theorem 5.1.1 and complete proof, printed pp. 63–64, retrieved
2026-10-11. Distinct evaluation points, nonzero multipliers and
0<k<=n give dimension k and distance n-k+1 over any field. Here
n=16, k=8, multipliers one and H consists of distinct field elements;
distance nine is covered directly. Reuse L010's moment kernel and
L015's existing sparse/projective application; no distance reproof
or new five-coordinate reduction is needed.

Reuse `2026-10-10-tau-zero-triangle-fourth-support.md` and the read
primary-result/count passages in `2026-10-10-triangle-twelve-recovery-bound.md`.
These record Chojecki, *Shortening Bounds for Reed–Solomon MCA*,
[live author TeX v9.2](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex),
dated July 17, 2026: DR2 (`drc:lem-locator-recurrence`) and
DR6–DRC (`drc:thm-exact-compiler`), full proofs/zero cases at source
lines 2785–2935; count comparisons at 1370–1460, 2936–2966 and
3000–3055. The R=8,t=4, multiplier-x specialization is unchanged.
The generic compiler needs a fiber count; the fixed-circuit theorem
requires all counted supports inside one nine-set and gives 36;
the fixed-core result requires a core for every counted witness.
None replaces the five-coordinate configuration bound. This source
was not freshly retrieved or identified with ePrint 2026/1463.

The same ready assessments retain Marquez-Corbella–Pellikaan,
*A characterization of MDS codes that have an error correcting pair*,
FFAA 40 (2016), 224–245,
[DOI 10.1016/j.ffa.2016.04.004](https://doi.org/10.1016/j.ffa.2016.04.004),
2016-02-29 accepted manuscript section 5, Definitions 5.1–5.2,
Lemma 5.3 and subsequent shortening formula, printed pp. 7–8.
Its already checked application supplies L041's base triple; no
new shortening specialization is needed. The saved BCHKS, Tamo and
subspace-design comparisons remain outside the required sharp count
or require absent fixed-H hypotheses; they are not refreshed.

Queries on 2026-10-11:

- `"Reed-Solomon" "five" "syndrome" "line"`
- `"mutual correlated agreement" "support" "overlap"`
- `"Shortening Bounds for Reed" "five"`
- `"MDS code" "coset" "projective line" sparse`
- `"Reed-Solomon" "error supports" "intersect" "affine"`
- `"mutual correlated agreement" "five-coordinate"`

No searched primary theorem was identified as a replacement for L015.
One primary scope lead was Blokhuis–Pellikaan–Szőnyi,
*The extended coset leader weight enumerator of a twisted cubic code*,
DCC 90 (2022), 2223–2247, version of record June 20, 2022,
[DOI 10.1007/s10623-022-01060-0](https://doi.org/10.1007/s10623-022-01060-0).
Read its abstract and inspected Theorem 8.1's opening setup, not its
complete classification proof. The abstract specifies the
[q+1,q-3,5] code and projective three-space, so it is a different
scope from this fixed length-sixteen distance-nine configuration.
Its theorem is an unread full-proof lead, not an imported count.
Generic decoding hits and a secondary paper index are not evidence.
Search absence proves no novelty; unread July/Jo sources remain parked
and are not essential inputs to this conditional application.

## Decision, relevance and preserved failures

Main gap: uniform triangle twelve bound. This conditional cluster
could remove a concentrated-support branch; other triangle families,
other L041 patterns, arbitrary extraction and challenge definitions
remain independent gaps. L068 motivates the question only.
ATTEMPTS/007 stops five-coordinate *generation of sixteen*; it does
not ban reuse of its upper-bound mechanism. ATTEMPTS/025's formal
common-root sampling and ATTEMPTS/026's false enlarged isolated bound
remain stopped. This application uses neither route nor a sampled
isolated maximum.

Essential prospective inputs: L015, audited L057 and inherited
L010/L041; the complete five-coordinate certificate is explicitly
unverified in this turn. Continue if the source applicability and
complete census yield M(A)<=10 and cover every original finite
recovery. Otherwise preserve the obstruction and reassess this
conditional route. No claim that every high-count triangle has this
pair, no new lemma, and no proved conditional count is made here.
Full matching and supporting Mathlib coverage remain **not checked**;
unknown coverage is not absence. No cross-notebook theorem is used.

The TARGET is unchanged. This newly completed SPECIALIZE assessment
is ready for separate supervisor approval; subsequent mathematics
should be an application/certificate check, classified REPRODUCTION.

## Original proposed scope retained

The following is the pre-review proposal; its unread/source-approval
statements describe the starting checkpoint, superseded by the fields above.

Essential prospective inputs: audited L057 and its inherited L010/L041
premises. L015 is an exact local theorem lead, not an imported premise;
read its hypotheses and relevant certificate obligations narrowly next turn.
No cross-notebook input is proposed. The known recurrence and shortening
sources in the L057 assessment can be reused within their covered scope.

Main gap: uniform triangle twelve bound; independent gaps are the other
patterns, arbitrary-family extraction and challenge definitions. A bound
for this conditional cluster would isolate a concrete part of the triangle
case and distinguish support concentration from a large isolated subcount.
No assertion that all high-count triangles contain such a cluster is made.

Continuation test: determine whether an inspected known result directly
covers the stated conditional bound, or whether it leaves a precisely
specified applicability or count gap that merits one approved mathematical
attempt. If the five-coordinate lead does not apply, record the exact
hypothesis failure before proposing an alternative. Do not treat the five
explicit L068 rows or the stopped enlarged sweep as a uniform count.

Preserve ATTEMPTS/025–026 and the successful L068 audit. No new lemma,
count, certificate maximum or source approval is established by this note.
