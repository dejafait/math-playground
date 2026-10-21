# Triangle pair-free balanced supports — completed source comparison

TARGET: Decide whether sixteen distinct four-subsets of a sixteen-label set can contain the prescribed L057 triangle, use each label four times, and have every pair of the thirteen remaining subsets intersect in at most one label.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Six targeted packing, affine-plane, transversal-design and triangle queries; narrowly compared L010/L052/L057/L069/L071, the prior balanced-support assessment and ATTEMPTS/007,016,017,021,025,026. Read the primary constructions and numbered statements below; no feasibility calculation was performed.
SOURCE_EVIDENCE: Olmez–Ramamoorthy arXiv:1210.2110v1 (7 October 2012), Section III, Definition 3 and class-selection paragraph, pp. 3–4; Section III.A explicit plane construction, p. 4, and Lemma 2, p. 5. Silberstein–Gal, author PDF dated 16 August 2014, Section 2 affine-plane definition, pp. 5–6, and Theorem 5, p. 6.
COMPARISON: Known prime-power affine planes and selection of parallel classes cover the underlying regular linear packing mechanism. The sources do not state the prescribed labeled triangle embedding. L052 has fifteen supports and a tau-one triple, and the prior cyclic/matching counterexamples impose different incidences; none decides this exact labeled instance as recorded.
GAP: Specialize the cited construction to order four, verify a nonconcurrent three-line triangle and its label bijection while selecting four parallel classes, and check the complete resulting family against the exact target. Moment realization and universal actual-error extraction remain separate gaps.
REASON: Essential finite-design coverage was missing at invocation start; this literature-only review now licenses a bounded citation specialization, without proving its previously uncovered triangle instance in the same turn.
SCOPE: Abstract sixteen-label set, fixed triangle A_0={a,b,y_1,y_2}, A_1={a,c,z_1,z_2}, A_2={b,c,w_1,w_2} with nine distinct labels, thirteen other distinct four-sets, exact degree four at every label, and pair intersections at most one among those thirteen sets only. Covered mechanism: cited order-four affine plane with four selected parallel classes and an explicitly verified triangle relabeling; no stronger moment or field-labeling target is approved.
COVERED_TARGET: Decide whether sixteen distinct four-subsets of a sixteen-label set can contain the prescribed L057 triangle, use each label four times, and have every pair of the thirteen remaining subsets intersect in at most one label.

The source comparison is complete; the exact feasibility test remains
unperformed. The main gap is useful-pair extraction for a hypothetical
thirteen-additional triangle violation. The intermediate test asks
whether coordinate balance and the fixed triangle alone can force a
pair with larger intersection. An impossibility result could support
that extraction after checking its actual-error application; a witness
would show these selected incidence constraints are insufficient and
direct subsequent work toward moment equations or stronger constraints.

The continuation test is exact feasibility: either a complete explicit
family with every stated constraint verified, or a rigorous exhaustive
or analytic impossibility argument. A sampled absence is insufficient.
A witness ends this support-only forcing route; it does not refute
uniform triangle twelve. No field labeling, original parameters,
nonzero error weights, locator splitting or actual recovery is supplied
by an abstract family. Those remain unresolved realization conditions.

Essential motivating input IDs are L010, L057, L069 and L071. L052 is
a comparison, not an input proof. Retain the fixed F_(97^20), H and arbitrary original chart
for any later transfer to pencils; the abstract test itself does not
identify labels with field elements. All relaxed L057 recoveries must
remain until a separately justified equality application supplies full
errors. No uniform extraction or challenge-level identification is
assumed. Mathlib coverage is not checked. No cross-notebook input is used.

## Primary source evidence and qualifications

Oktay Olmez and Aditya Ramamoorthy, *Repairable Replication-based Storage
Systems Using Resolvable Designs*,
[arXiv:1210.2110v1](https://arxiv.org/pdf/1210.2110v1), 7 October 2012.
For a prime power t the point set is F_t^2. Blocks are y=mx+d and
vertical lines. There are t+1 parallel classes, each of t blocks of
size t. Definition 3 makes each class a partition; the selection
paragraph allows any rho distinct classes, rho<=t+1, with replication
rho. Lemma 2 assumes an affine resolvable BIBD and gives intersection
alpha^2/theta between different classes. These cover the same-class
and different-class cases. Only the explicit plane construction is
needed. Its underlying book [6], Beth–Jungnickel–Lenz, was not read.

Natalia Silberstein and Anna Gal, *Optimal Combinatorial Batch Codes
based on Block Designs*,
[author PDF](https://www.cs.utexas.edu/~panni/batch.pdf), dated
16 August 2014, read 12 October 2026. Section 2, printed pp. 5–6,
defines an order-t plane by t^2 points, t(t+1) blocks of size t,
and unique coverage of every point pair, and specifies its resolution.
Theorem 5, p. 6, asserts existence for every prime power. Its cited
book proof was not inspected; the first source supplies the explicit
coordinate construction. This corroborates the incidence convention;
its batch-code optimization theorems are not used. Example 4 concerns
TD(3,4), with twelve points, and is not a witness for this target.

The source order t=4 is a prime power, as required. It is an auxiliary
combinatorial field order, not the RS field size 97^20; no embedding
of F_4 into that field is proposed. The relevant known conclusion is
a selectable-class affine-plane packing with exact replication.
The missing specialization is the prescribed three-block triangle,
its full bijective relabeling and retention in the chosen classes.
These sources license that check; they are not cited as already
verifying the notebook's labeled family. Import the plane and
class-selection results by these citations. A reproof of general
finite-plane existence or a new packing theorem is unnecessary.

## Local comparison and recorded stops

Read L010's equality conclusion and L057's hypotheses (1)–(3), plus
L069/L071's conditional statements. Equality supplies distinct full
four-errors and degree four, whereas the conditional pair bounds need
an actual pair with union five or six. This source review asserts no
new implication between those statements. Read L052's displayed
family, conclusion and incidence verification: it has fifteen edges,
only capacity bounds, and a tau-one triple, so it is not this witness.
The narrow local affine-plane/transversal-design/pair-free search
found no already recorded exact witness; that is not a novelty claim.

Reused `2026-10-04-balanced-support-disjoint-triple.md` for its matching
comparison and retained ATTEMPTS/016–017: cyclic matching-number-two
families address disjoint-triple or small-union forcing, not this fixed
triangle with linear additional supports. ATTEMPTS/021 records a
different union-six matching profile and leaves moment compatibility
essential. ATTEMPTS/007 concerns actual five-coordinate pencils;
ATTEMPTS/025 stops unstructured triangle samples and formal common-root
tests; ATTEMPTS/026 refutes an enlarged isolated-scalar bound. None
blocks this independently checkable abstract design specialization.
No old moment enumeration, stopped maximum or sampled exclusion is
reopened.

## Bounded continuation and gate decision

The exact TARGET is ready under SPECIALIZE. On the next mathematical
turn, use the cited plane construction and selected classes, explicitly
identify three nonconcurrent lines with the required pairwise singleton
intersections, give the label bijection and verify every required count
and intersection. A complete displayed witness with an analytic
verification suffices; exhaustive search or a new mathematical script
is not required. No construction or triangle verification was executed
in this literature-only turn.

If that specialization succeeds, stop balance-plus-triangle forcing
of an additional useful pair and turn subsequently to actual moment
constraints or a separately reviewed stronger incidence condition.
If it fails, identify the failed gate without inferring nonexistence;
only a rigorous impossibility argument would justify pair forcing.
Even a feasible abstract witness supplies no H-label realization,
weights, finite parameters, splitting locators or same-support failure.
The uniform triangle twelve and global 11/q–16/q gap remain open.

Queries read as searches: `affine plane finite field order q resolvable
design q squared q lines parallel classes construction pdf`;
`"TD(4,4)" transversal design construction`;
`"16" "4" "packing" "triangle" affine plane blocks`;
`"Repairable Replication-based Storage Systems Using Resolvable Designs" arxiv`;
`"affine plane" "four parallel classes" "16"`;
`"triangle" "affine plane" "nonconcurrent" lines`.
These are six query strings, submitted across two search calls.
Other returned books, summaries and the inaccessible ISI lecture-note
page were leads only. PDF text retrieval supplied the cited passages;
the second PDF screenshot timed out, with no missing textual theorem
coverage. No inference rests on snippets or the failed screenshot.
Outcome: EXPLORATION / LITERATURE / NOVELTY_UNCHECKED. This completes
coverage, not the feasibility target or an original mathematical result.
