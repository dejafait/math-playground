# Endpoint-pair incidence count — completed bounded source comparison

TARGET: Compute and certify the maximum number of C122a's ordered triples containing both endpoints of a specified unordered pair, over all unordered pairs in H.
CHECKED: 2026-10-25
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded searches for prescribed/fixed-pair collinear triples, sum/product pair images, multiplicative-subgroup codegrees and Bonferroni deletion; reused the inspected 2017/2020 incidence comparisons and searched the exact local count/core-transfer assessments and ATTEMPTS/010. No inspected matching endpoint-pair maximum was found; this is not a novelty claim.
SOURCE_EVIDENCE: Read L122's reduction and endpoint/orbit proof, C122a's statement/applicability, L020's exact predicate and the recorded primary-source comparisons; read UConn Probability inequalities, Section 15.1, Proposition 15.2, printed pp.196–197, https://probability.oer.math.uconn.edu/wp-content/uploads/sites/2187/2020/08/ch15M.pdf for the complete Bonferroni statement and its k=1,2 discussion (general proof explicitly omitted).
COMPARISON: Existing global/Cartesian-product moments do not give the conditioned maximum. Bonferroni supplies a possible upper-survivor diagnostic using pair-overlap upper bounds plus justified single-endpoint counts; it does not supply the field-specific codegrees, a lower-survivor improvement or selected-support supersaturation.
GAP: A later attempt must establish complete same-pair/different-pair counting, ordering and orbit multiplicities, certify maximum and attainment over all endpoint pairs, and assess usefulness; no such formula, maximum or numerical deletion bound is established here.
REASON: Essential source comparison for the unchanged saved target is now sufficient for one bounded mathematical attempt; the missing finite specialization is explicit and independently testable, while the old transfer failures remain in force.
SCOPE: Exactly TARGET: prove and implement the necessary endpoint-conditioned enumeration using L122/C122a, with full same-pair/different-pair, vertical, horizontal, star and antipodal cases and justified endpoint-pair orbit coverage; no new uniform-core or list-size theorem is preapproved.
LITERATURE_REASON: The endpoint-pair conditioning was outside the ready full-H count/audit coverage; this separate turn reviews that changed scope rather than repeating the ready audit.

The main gap remains arbitrary-center 67/68 safety. For distinct a,b in H,
let d(a,b) denote the number of the ordered triples counted by C122a for
which both a and b occur among the six distinct endpoints. They may lie
in the same pair object or in two different pair objects. The target is
the exact maximum of d(a,b) over unordered endpoint pairs, with full case
coverage. This definition is a proposed statistic, not a derived formula.

Plausible downstream use: control overlaps between incidences of deleted
endpoints when comparing the full domain to H minus a 61-point core.
The source review should check whether that use is quantitatively meaningful
and whether known codegree/deletion bounds already give what is needed.
A uniform core bound, a selected-support-family transfer, threshold saving
and actual RS realization remain separate unresolved steps. In particular,
this proposed maximum is not itself a list bound.

Essential inputs for later work: C122a, L122, L020, C001a and foundations/02;
the audited full-H histograms and certificates. Any reduction by multiplication
in H must prove that it preserves endpoint conditioning and cover all pair
types, including antipodal pairs. The original histogram row totals alone
are not assumed to determine this statistic. No cross-notebook input.

Continuation test: approve only after inspecting matching primary theorem
hypotheses/proof cases or documenting the precise uncovered specialization.
If approved later, seek a complete exact maximum with attaining pair and
certified coverage of every endpoint pair or justified orbit, rather than
a sampled value. A discrepancy between same-pair and different-pair cases,
or lack of a defensible deletion use, requires repair or abandonment of
this target. Retain ATTEMPTS/010's actual antipodal configurations and the
prior global/core supersaturation stops. Mathlib matching coverage is not
checked. No new mathematics or implementation for this target occurred
during the C122a audit; the proposal at that time granted no research approval.

## Completed review, 2026-10-25

The preceding proposal is historical scope. This separate turn approves
EXPLORE for its unchanged TARGET and explicit SCOPE above: an attempt,
not a counting claim. No lemma or mathematical program was written or run.
This review is EXPLORATION: no inspected source resolves the maximum,
and no mathematical advance or originality is claimed.

### Primary sources and applicability

Reuse the primary statements and essential proof cases recorded in
[the labeled-count assessment](2026-10-24-labeled-collinear-pair-triple-count.md):
Murphy–Petridis, [arXiv:1601.03981v3](https://arxiv.org/pdf/1601.03981v3),
Lemma 1, printed p.2 and full Section 2 proof p.5; Macourt–Shkredov–Shparlinski,
[arXiv:1701.06192v2](https://arxiv.org/pdf/1701.06192v2), Definition 1.1,
Theorem 1.2 and Lemma 2.4/proof; Macourt–Petridis–Shkredov–Shparlinski,
[arXiv:2003.03493v1](https://arxiv.org/pdf/2003.03493v1), Section 3,
Theorem 5.2/proof. These are reused assessments, not fresh PDF reads.
The first allows arbitrary finite-plane point sets but gives an unexcluded
second moment. The others concern Cartesian-product triples with different
ratio/distinctness conventions and asymptotic constants. None of these
inspected conclusions determines the endpoint-conditioned count. Do not
reprove their general incidence results.

New primary read: [Probability inequalities, Chapter 15](https://probability.oer.math.uconn.edu/wp-content/uploads/sites/2187/2020/08/ch15M.pdf),
UConn-hosted ch15M.pdf, inspected 2026-10-25, Section 15.1,
Proposition 15.2, printed pp.196–197. It assumes finitely many events in
any probability space, without independence. If S_j sums j-event
intersection probabilities, odd alternating truncations bound the union
above and even truncations below. At k=2 the lower bound is S_1-S_2.
Read the full boxed statement and k=1,2 discussion; the general proof is
explicitly omitted. The intermediate “S_1-S_1” on p.197 is a typo: the
boxed theorem and expanded pair-intersection expression agree. Import
the standard named Bonferroni inequalities; no general reproof is needed.

Applicability: use the finite uniform space of C122a's ordered configurations
(nonempty by C122a), with an event for each endpoint to occur. Two-event
intersections are exactly the statistic in TARGET, including endpoints in
different pair objects. The second truncation permits an upper bound on
core-avoiding configurations using justified singleton counts and upper
bounds on pair intersections. The singleton counts and their symmetry
remain later obligations. This explains a possible diagnostic; no
field-specific formula or quantitative deletion bound is derived here.
It cannot by itself improve a lower-survivor estimate.

### Duplicates, failures and continuation test

L122 already handles unordered pairs, ordered triples, matching lines,
star exclusion and slope orbits; that orbit argument does not establish
transitivity on endpoint pairs or cores. C122a counts only the full domain.
Targeted local material contains no identified duplicate of the new maximum.
Reuse these results and preserve their programs/histograms; justify only
the changed conditioning. No new replay of the audited count is needed.

Read L020's exact conclusion and ATTEMPTS/010: antipodal realizations
remain genuine. Reuse [the core-transfer review](2026-10-06-core-conditioned-determinant-transfer.md):
the inspected pair-supersaturation theorem has an unavailable finite
parameter range and does not supply labeled triple supersaturation;
cardinality transfer remains missing. A codegree diagnostic does not
repair those failures or establish selected-family uniformity.

Continue with one bounded attempt seeking a certified maximum, attaining
pair and complete coverage of all pairs or proved orbits, retaining both
endpoint-placement cases and antipodal pairs. Establish a credible
enumeration cost before a long run. Independently check small instances
and complete double-counting identities justified in that attempt;
sampled maxima are insufficient. For the proposed deletion use, state
the bound direction and compare its certified strength against ignoring
pair overlaps. If coverage fails, enumeration is intractable or no
nontrivial improvement is available, preserve the failure and stop this
target. No useful numerical saving is assumed in advance.

Essential later inputs: C122a, L122, L020, C001a, foundations/02 and the
audited histogram/audit certificates. No cross-notebook input. Uniform
core estimates, selected-family transfer, list-threshold saving, RS
realization, safety and ABF comparison remain unresolved. Full matching
Mathlib coverage is not checked. Future POTENTIALLY_NEW classification
would mean only lack of a matching result in this bounded search; this
literature turn is NOVELTY_UNCHECKED.

### Search and access evidence

Queries included `"collinear triples" "prescribed" finite field
multiplicative subgroup`, `"hypergraph" "codegrees" "Bonferroni" deletion`,
`"point line" incidences "fixed" "unordered pairs" finite fields subgroup`,
`"sum product" "collinear triples" "subgroups"`, `"fixed pair" "codegree"
"collinear" finite fields`, `"multiplicative subgroup" "collinear triples"
"codegree"`, `"sum product" "pair" "collinear" "65537"`, and
`Bonferroni inequalities proof site:edu`. No matching theorem was inspected;
search failure proves neither absence nor novelty. Unrelated hits are not
inputs.

Driver's UCSD notes (May/June 2019), Sutner's CMU probability slides,
USC annotated slides and Chicago homework were leads. Relevant full
passages could not be retrieved: follow-up PDF opens/finds timed out or
returned no match; USC exceeded the fetch-size cap; shell download could
not resolve the host. Driver's title/contents and CMU's initial pages were
accessible, but their Bonferroni proofs were not read. MIT's video page
exposed no theorem transcript. These are not assessed proof inputs.
The accessible UConn theorem statement supplies the essential standard
deletion comparison; no essential blocker remains for the exact-count
attempt. No claim relies on an unread proof or a search snippet.
