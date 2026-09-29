# Four-block syndrome-line literature assessment

TARGET: For the four blocks A_i={8^(4i+j):0<=j<4}, 0<=i<4, in F_97, reduce syndrome lines meeting all four associated error spaces to a 4-by-4 eigenvector problem and test the resulting lines against L010's sixteen-challenge criterion over F_(97^20).
CHECKED: 2026-09-27
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Reused the September 26 geometric and coding searches and September 27 review 013; review 014 additionally checked official-companion source availability and Zenodo, EPFL, Bocconi and Stanford deposit leads, alongside the primary links and author entries. Dated queries and access results are below; no authoritative readable July copy was found.
SOURCE_EVIDENCE: Reused September 26 readings of Martin del Campo Sanchez (2012), §III.D.1, pp. 29–30; Sottile, arXiv:alg-geom/9510017v1, §7.1, pp. 14–15; Yuan–Zhu, arXiv:2605.07595v2, Definition 4.1 and Theorem 6.6; Gao–Yang–Xu–Kan, arXiv:2607.10572v1, Definitions 7–8 and Corollary 2; and Chojecki's named statements below. September 27 reviews read ABF26 metadata, author entries and the official companion README; the PDF and archive remained inaccessible. No additional primary mathematical statement was recovered.
COMPARISON: Classical geometry covers the generic eigenvector mechanism; the inspected coding results do not supply this fixed-block sixteen-challenge witness or a uniform fifteen-challenge bound. Comparison with ABF26's updated attack bounds remains incomplete.
GAP: Read the authoritative July ABF26 event, smooth-domain and field qualifications, endpoint convention, and added MCA lower bound; then assess the prescribed finite-field specialization and locator equality test against them.
REASON: Preserve the exact proposed calculation and cited geometric ingredients, but stop the exhausted retrieval sequence after three reviews without a new bound or informative negative result. The essential July source gap still prevents a complete comparison; no dependent research is authorized by this assessment.

## Gap, relevance, and discriminating test

In the pinned affine-line model, the four-omission cell for
RS[F_(97^20),H,8] has recorded global bounds 10/q and 69/q. L010 bounds
its nondegenerate class by sixteen; the recorded field-budget comparison
permits fifteen. The intermediate target is to describe the lines incident
with the four prescribed error spaces and check their full locator incidence.
Sixteen valid bad parameters would prove unsafety for this model at the
selected radius. An exhaustive obstruction for this partition would stop
that construction, without settling general lines or the challenge.

The eventual test must check the field of definition, affine parameters,
same-support failure, and every equality condition in L010. A generic count
of transversal lines is not a count of bad challenges on one line. Repeated
eigenvalues or an unsplit characteristic polynomial cannot be dismissed by
assuming a generic configuration. General sharpness, the excluded locator
degeneracies, other cells, and ABF26 correspondence remain separate gaps.
No matrices, eigenvalues, locator polynomials, or new bounds were calculated.

## Local redundancy and previous failures

The overview and DAG were read before L009 and L010, the locator-incidence
draft and history, and the stopped full-orbit attempt. L009 limits one full
subgroup orbit to four projective directions; it does not exclude the saved
quartet. L008 already gives ten, so reproducing its two-family construction
cannot reach sixteen. The earlier sparse-lifting hypotheses do not cover
the selected four-error case. L010's locator converse and same-support
argument are already available under its nonvanishing hypotheses.

## September 26 search and access record

Queries included:

- `"Open Problems in List Decoding and Correlated Agreement" pdf`
- `"2026/680" "MCA" lower bound`
- `"2026/680" "Definition 4.3"`
- `Reed Solomon mutual correlated agreement syndrome four subspaces eigenvector`
- `"four subspaces" "eigenvectors" common transversals`
- `"Schubert" "eigenvectors" "four"`
- `Sottile "Enumerative geometry for the real Grassmannian of lines" pdf`
- `"List-Decoding Counterexamples Yield Lower Bounds"`
- `"Reed–Solomon Mutual Correlated Agreement Beyond" Jo pdf`

The [official challenge](https://proximityprize.org/) still gives the four
rates, a largest real radius, example error 2^-128, and an unspecified
sufficient-field-size qualification. It remains preliminary. The
[ABF26 record](https://eprint.iacr.org/2026/680) still lists July 6, 2026
as the latest of three revisions, with changed attack estimates and an
added MCA lower bound. Metadata does not supply those theorem statements.

The [PDF](https://eprint.iacr.org/2026/680.pdf) returned HTTP 403; its
download-query variant and [version archive](https://eprint.iacr.org/archive/versions/2026/680)
also failed. Local `curl -I --max-time 15` could not resolve the ePrint
host. [Arnon](https://galarnon42.github.io/) and [Fenzi](https://gfenzi.io/)
still link to ePrint. [Boneh's topic index](https://crypto.stanford.edu/~dabo/pubs/pubsbytopic.html)
had no match for `Correlated` or the report ID. The
[ePrint Classic index](https://eprint-classic.github.io/2026.html) points to
the same PDF. The [third-party mirror](https://raw.githubusercontent.com/przchojecki/rs-mca/main/open-proximity.pdf)
was also unreadable. The previously inspected April reconstruction remains
uncertified for July. None is treated as a recovered primary definition.

## Known geometric input

### Hypotheses

Martin del Campo Sanchez, *Galois Groups of Schubert Problems* (August
2012 dissertation), [§III.D.1, printed pp. 29–30](https://franksottile.github.io/advising/martindelcampo.pdf#page=36),
considers four general a-dimensional subspaces H1,...,H4 in dimension 2a.
Using H1 direct-sum H2, write H3,H4 as graphs of isomorphisms phi3,phi4.

### Conclusion

The source describes transversal two-planes by eigenlines of
psi=phi4^(-1) phi3: an eigenvector v gives span(v,phi3(v)). In its
generic split case there are a such planes.

### Proof

Use the cited argument; no reproof is supplied. The prescribed quartet
still requires its own hypothesis and field-of-definition checks.

The earlier reference was followed to Frank Sottile,
[*Explicit Enumerative Geometry for the Real Grassmannian of Lines in
Projective Space*, arXiv:alg-geom/9510017v1](https://arxiv.org/pdf/alg-geom/9510017v1#page=14),
October 31, 1995, §7.1, printed pp. 14–15. It describes the transversals
to three disjoint (a-1)-planes by a Segre variety, then intersects a fourth
general plane. Its finite-field existence discussion concerns configurations
one can choose, not rationality for our prescribed blocks. The dissertation
cites §8.1 of the 1997 Duke publication; the version actually read here has
the relevant discussion in §7.1. These version locators are kept distinct.

### Mathlib

Full four-subspace result: **not checked**. Supporting graph, eigenvector,
and finite-field results: **not checked**. The cited sources cover the
generic geometric mechanism, not the full MCA target. The pinned ArkLib
declarations remain definition sources, not a formalization of this reduction.

## Other inspected results and their limits

**Yuan–Zhu, July 10, 2026, v2.**
[*A Syndrome-Space Approach to Proximity Gaps and Correlated Agreement for
Random Linear Codes and Random Reed–Solomon Codes*](https://arxiv.org/html/2605.07595v2),
Definition 4.1, uses a common sparse lift of an affine syndrome space.
Theorem 6.6 gives quantitative affine-space and curve bounds with high
probability for iid random RS evaluations, for sufficiently large length
and its stated alphabet bound. It allows equal input and output radii in
that ensemble. This does not certify the fixed order-16 subgroup. Nor is a
common-lift conclusion automatically an exact-support MCA bound.

**Gao–Yang–Xu–Kan, July 12, 2026, v1.**
[*List-Decoding Counterexamples Yield Lower Bounds on Mutual Correlated
Agreement Error*](https://arxiv.org/html/2607.10572v1), Corollary 2, assumes
n>k, failure of (p,L)-list decodability, and p<1-k/n. It produces an RS
code on S' of the same size with error at least
q^(-1) ceil((L+1)q/(q+L(k-1))). Its construction may change an evaluation
point. It supplies no witness on our prescribed H or smoothness guarantee
for S'. Definitions 7–8 were also read; their two-word event and strict
error convention do not certify the current ABF26 statement.

**Chojecki, author-hosted source.** The mutable
[`RS_MCA_Paving_v9.2.tex`](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex)
was read on September 26; its header says July 17, 2026. Byte identity with
[ePrint 2026/1463](https://eprint.iacr.org/2026/1463) is not asserted.
The `Syndrome-line normal form` proposition, (3.2), and `Exact syndrome--secant
compiler` theorem, (3.3)–(3.4), cover the noncontained line/error-space
formulation, not the sixteen-incidence test. The `Exact deep numerator`
corollary overlaps L006's range. The `Integral BCHKS completion` theorem
requires 2r<R, R=n-k; the saved target has 2r=R. These statements were
inspected, without deriving new specializations. Its citations identify
ABF26 Definition 4.3, Lemma 4.6, Remark 4.10, and Jo's Theorems 4.2–4.3
as retrieval leads; those attributions do not establish their primary text.

**Unread leads.** Jo's [ePrint 2026/1432 record](https://eprint.iacr.org/2026/1432)
lists an August 19 revision, but its PDF could not be read. Its
circuit-incidence and endpoint theorems are not imported from the later
attribution. ABF26's updated lower bound and qualifications remain essential
unread material. A failed search or inaccessible source does not prove novelty.

## September 26 assessment and continuation decision

Decision: SOURCE_BLOCKED. The new evidence identifies known geometric
coverage and the scope limits of nearby coding results. It does not finish
the exact target's literature comparison. The generic reduction should be
reused by citation after the source gate and specialization hypotheses are
resolved; deriving it afresh would be reproduction. No reproof is justified
merely by the local notation.

The exact research target is retained in PROGRESS.md. Its dependent
calculations must wait for the primary comparison. Thereafter a certified
sixteen-challenge line would justify continuing this partition; an exhaustive
failure over the specified field would justify abandoning this partition
alone. No successful or failed eigenvector experiment is asserted here.

Outcome: EXPLORATION, one of three exploration turns used since the preceding
advance. Newly read theorem statements make this more than a repeated stop
review, but there is no new mathematical bound and no budget reset.
Classification of the full-target review is NOVELTY_UNCHECKED. The geometric
ingredient is known; coverage of the remaining target is unresolved. No
complete challenge candidate appeared, and lemmas/ and scripts/ are unchanged.

## September 27 source-access reassessment

This literature-only follow-up preserves the exact TARGET. The whole overview,
DAG, checkpoint, source foundations, L010 and stopped full-orbit attempt were
read. The previously sufficient geometric and nearby-coding comparisons above
were reused; none was mechanically repeated or promoted to a match for the
full statement. The essential unresolved item remains the July ABF26 text.

The retrieval mechanisms compared were the primary archive and PDF links,
author/institutional copies, and independent bibliographic or repository
leads. Queries included:

- `"Open Problems in List Decoding and Correlated Agreement" filetype:pdf`
- `"2026/680" "July" "MCA"`
- `"Open Problems in List Decoding and Correlated Agreement" Arnon Boneh Fenzi pdf July`
- `site:eprint.iacr.org/2026/680 "Definition 4.3"`
- `"Open Problems in List Decoding" site:infoscience.epfl.ch`
- `"Open Problems in List Decoding" site:crypto.stanford.edu`
- `"Open Problems in List Decoding" site:arxiv.org`
- `"Open Problems in List Decoding" "July 6" "pdf"`
- `"Arnon" "Fenzi" "MCA" "Lemma 4.6"`
- `"Open Problems in List Decoding" github pdf`

The [primary record](https://eprint.iacr.org/2026/680), particularly its
update note and History, still identifies July 6 as the latest revision and
announces the added MCA lower bound. The [official page](https://proximityprize.org/)
still displays the previously recorded challenge parameters and preliminary
qualification. Neither supplies the missing theorem-level comparison.

| Retrieval source | September 27 observation |
| --- | --- |
| [Primary PDF](https://eprint.iacr.org/2026/680.pdf) and the record's PDF link | Both returned Internal Error; no pages were read. |
| [Version archive](https://eprint.iacr.org/archive/versions/2026/680) | Internal Error; no revision-specific download recovered. |
| [Short-domain PDF](https://ia.cr/2026/680.pdf) and [HTTP PDF](http://eprint.iacr.org/2026/680.pdf) | Internal Error; no alternative text recovered. |
| [Arnon's technical-report entry](https://galarnon42.github.io/) and [Fenzi's ABF26 entry](https://gfenzi.io/) | Read the publication entries and links; both point back to ePrint. |
| Institutional/arXiv title searches | No readable matching deposit appeared in the returned results; this is not a claim that no deposit exists. |
| Bibliographic/repository search | DBLP and third-party citations appeared; the [DBLP XML request](https://dblp.org/rec/journals/iacr/ArnonBF26.xml) failed. No source with verified July provenance was recovered. |

No new theorem or counterexample was read. The April reconstruction,
third-party attributions to Definition 4.3, Lemma 4.6 and Remark 4.10, and
Jo's unread primary text retain their previous qualifications. No claim from
a search snippet is imported as mathematics. Failed retrieval does not
establish either novelty or the absence of a relevant bound.

Decision remains SOURCE_BLOCKED. To change it, a readable authoritative July
copy must permit comparison of the event, domain and field assumptions,
endpoint convention and new lower bound with the saved test. A definition
mismatch or an already covering theorem would require reassessment before
calculation. A matching source would permit a later, separately invoked
specialization step, subject to the comparison's actual conclusion.

The intended intermediate target, downstream use and discriminating test
remain those above: a certified sixteen-challenge witness exceeds fifteen;
an exhaustive failure only rules out this partition. The existing global
10/q and 69/q bounds, restricted sixteen bound, degeneracy gap and unresolved
challenge correspondence are unchanged. No source import, reproduction or
result beyond the checked literature is claimed in this follow-up. Mathlib
coverage remains **not checked**.

Outcome: STALLED, since this is a repeated source-stop decision with no new
theorem-level evidence or actionable test. STEP_KIND is LITERATURE and
STEP_CLASSIFICATION is NOVELTY_UNCHECKED. Conservatively this uses the second
of three review/exploration turns since L010, without resetting the budget.
The exact Next action and assessment path are retained; further dependent
research remains gated. No complete candidate appeared. No mathematical
calculation was performed, and lemmas/, scripts/, PROOF.md and DAG.md were
left unchanged.

## September 27 final source-recovery review (014)

This third review reused the theorem-level comparisons above. Its bounded
retrieval alternatives were an authoritative paper/version link, an author
or institutional deposit, and material supplied by the official companion
project. The last two were checked for a readable copy, not treated as
substitutes for the July paper. Additional queries included:

- `"Open Problems in List Decoding and Correlated Agreement" -site:eprint.iacr.org -site:eprint-classic.github.io`
- `"Open Problems in List Decoding" site:zenodo.org`
- `"Open Problems in List Decoding" site:infoscience.epfl.ch`
- `"Open Problems in List Decoding" site:iris.unibocconi.it`
- `"Open Problems in List Decoding" site:searchworks.stanford.edu`
- `"Open Problems in List Decoding" site:github.com/proximity-prize`
- `"Open Problems in List Decoding" ABF26 PDF July`

The full-title query was also run with a domain filter for the four deposit
sites above. No readable matching July deposit appeared in the returned
results. This does not establish that no deposit exists. General searches
returned bibliographic entries and later papers citing ABF26; their snippets
were not imported as theorem statements.

| Source actually inspected | Result and scope |
| --- | --- |
| [ABF26 primary record](https://eprint.iacr.org/2026/680), Note and History | Still identifies the July 6 revision and added MCA lower bound; no theorem text. |
| [Primary PDF](https://eprint.iacr.org/2026/680.pdf) and [version archive](https://eprint.iacr.org/archive/versions/2026/680) | PDF retrieval reported a restricted URL; archive was inaccessible through the tool. No pages or revision-specific statement were read. |
| [Arnon technical-report entry](https://galarnon42.github.io/) and [Fenzi ABF26 entry](https://gfenzi.io/) | Both still link to ePrint. [Boneh's publication list](https://crypto.stanford.edu/~dabo/pubs.html) had no match for `Correlated`. |
| [Official challenge](https://proximityprize.org/), grand MCA section | The preliminary rate, error, largest-real-radius and sufficient-field-size wording is unchanged. |
| [Official companion README](https://raw.githubusercontent.com/proximity-prize/proximity-prize/main/README.md), opening and Challenges sections; [repository root](https://github.com/proximity-prize/proximity-prize) | Read the description of the separate IRS reduction-error tracks and inspected the root listing. Neither supplied the paper; this is not an exhaustive repository search. The recursive-tree API request was inaccessible. |

The companion README's protected-target descriptions do not certify the
ABF26 MCA event, its added lower bound, or the endpoint convention. Its
protocol scope was already distinguished in the source audit, so rereading
that distinction does not change the mathematical assessment. The prior
unread-source qualifications, including Jo's text, remain in force.

The assessment therefore ends **SOURCE_BLOCKED**, with outcome **STALLED**,
STEP_KIND **LITERATURE**, and STEP_CLASSIFICATION **NOVELTY_UNCHECKED**.
No result is imported, reproduced or claimed beyond the checked literature
in this follow-up. Mathlib coverage remains **not checked**. This is the
second consecutive stalled review and conservatively exhausts the three-turn
review/exploration budget since L010; it does not reset that budget.

Stop this repeated retrieval sequence. A further unchanged metadata check is
not a useful continuation. The exact four-block target and its discriminating
test remain preserved: sixteen valid challenges would exceed the budget of
fifteen, while exhaustive failure would stop only this partition. The source
access failure establishes neither result. A readable authoritative July
text or concrete new source evidence would justify reopening the comparison;
the current record does not authorize the dependent calculation. This is a
stop for the retrieval approach, not a mathematical rejection of the target
or a global research ban. No launcher or retry state was changed.
