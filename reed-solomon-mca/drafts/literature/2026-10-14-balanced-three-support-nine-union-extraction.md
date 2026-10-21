# Balanced support families — proposed three-support extraction

TARGET: Determine whether sixteen distinct four-subsets of a sixteen-set, with every vertex in exactly four subsets, must contain three subsets whose union has at most nine vertices.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed exact three-edge/nine-vertex, G_4(9,3), regular Berge-girth and Moore-bound searches; inspected Ellis–Linial Lemma 1 and its complete proof, Shangguan's sparse-configuration definition and Theorem 3, and the relevant local incidence statements and stops listed below.
SOURCE_EVIDENCE: Ellis–Linial, arXiv:1302.5090v5 (12 July 2017), Section 1 pp. 3–4 and Section 2 Lemma 1, equations (5)–(6) and complete proof, pp. 5–6, supplies the finite regular Berge-girth bound; at r=d=4 the girth-four threshold is forty vertices. L010's equality conclusion and proof supply the intended simple degree-four family.
COMPARISON: The Moore bound covers the linear, short-cycle-free obstruction, but does not state this three-edge extraction for a possibly nonlinear family. Shangguan's asymptotic Theorem 3 has union threshold eight at r=4,e=3, not nine, and gives no exact sixteen-vertex regular conclusion. Recorded failures concern different extractions.
GAP: Justify the precise bridge from absence of a three-edge union of size at most nine to the source's short-cycle hypotheses, including nonlinear two-edge cycles, distinct third edges and finite/disconnected cases; then specialize the cited bound. No bridge or extraction is proved in this turn.
REASON: Essential source coverage now permits one bounded reproduction proof attempt on the unchanged target; cite the standard Moore bound rather than reprove it. No originality or global MCA improvement is claimed.
SCOPE: Simple four-uniform hypergraphs with exactly sixteen vertices and sixteen edges, all vertex degrees four; no field labeling, moment compatibility, triangle premise, matching-number restriction or existence of a useful pair is assumed.

## Intended use and bounded decision

The unresolved local goal is exclusion of arbitrary nonpersistent
sixteen-count equality. L010 would turn any such equality pencil into
exactly the incidence family in TARGET. The proposed intermediate test
asks only for one three-support union of size at most nine. It does not
assert the extraction, classify the resulting triple, or close a count.
If established, the union-at-most-eight and union-nine local analyses
could become relevant to arbitrary families. The uniform triangle bound,
complete applicability assembly and challenge qualifications would still
be independent gaps; no global fifteen claim is proposed.

Essential continuation input is L010's distinct four-support and
four-incidences-per-coordinate conclusion. L032 and L041 are prospective
downstream local classifications, not premises of the incidence claim.
No cross-notebook input is used. Arbitrary F_(97^20) weights and the
original finite chart would remain when a later RS application is made.

The source comparison now approves a separate mathematical attempt on
exactly TARGET. Continue if every short-cycle case can be converted to
the required union statement under the actual degree and simplicity
hypotheses, and the Moore-bound applicability is complete. Abandon the
implication if a counterexample satisfies every target hypothesis; park
this mechanism if its bridge needs an unsupported extra assumption.
Do not reinterpret either finding as an RS counterexample or assume a
moment-compatible equality pencil. No such conversion or proof was
performed in this literature turn.

## Primary source and remaining specialization

David Ellis and Nathan Linial, *On regular hypergraphs of high girth*,
version [arXiv:1302.5090v5](https://arxiv.org/pdf/1302.5090v5),
12 July 2017, Section 1, printed pp. 3–4, defines Berge cycles using
distinct edges and distinct successive intersection vertices, including
cycles of length two. Two edges meeting in at least two vertices form
such a cycle; girth at least three therefore requires linearity.
Section 2, **Lemma 1**, equations (5)–(6), printed pp. 5–6, assumes
integers d>=2 and r,g>=3 and an r-uniform, d-regular, n-vertex
hypergraph of girth g. Its lower bounds are
\[
 n\ge 1+d(r-1)\sum_{i=0}^{k-1}((d-1)(r-1))^i
 \quad(g=2k+1),
\]
\[
 n\ge r\sum_{i=0}^{k-1}((d-1)(r-1))^i
 \quad(g=2k).
\]
The complete proof counts a vertex-centered ball in the odd case and
vertices at distance at most k-1 from a fixed edge in the even case.
At r=d=4,g=4 the latter bound is 4(1+9)=40, compared with
the target's sixteen vertices; larger finite girths strengthen it.
These are source bounds under extra cycle hypotheses, not bounds yet
established for TARGET.

The essential remaining work is the union/cycle bridge, particularly
the nonlinear branch: a two-edge cycle alone supplies only two edges,
whereas TARGET requires three distinct edges. Degree four is available
but its use must be proved. The three-edge cycle case must retain the
source's distinct intersection vertices. A proof must also explain
finite girth or use the inspected neighborhood argument directly, and
handle components without adding a connectivity hypothesis. None of
these obligations is silently assumed solved. The generic Moore bound
needs no reproof; any written counting explanation should be limited
to verifying its hypotheses and specialization.

The published primary version is *Electronic Journal of Combinatorics*
21(1) (2014), P1.54, DOI
[10.37236/3851](https://doi.org/10.37236/3851), Section 2 Lemma 1,
printed p. 4. Its theorem/proof text was retrieved, but later PDF opens
timed out and screenshot output was unavailable. The versioned arXiv
copy above supplied readable inequality signs, full definitions and
both complete proof cases; it is the controlling citation here.
No source blocker remains for this bounded specialization.

## Exact searches, stronger-result comparison and duplicates

Queries on 2026-10-14 included `uniform hypergraph Moore bound girth 4
regular hypergraph vertices r d`, `4 uniform hypergraph (9,3) problem
linear triangle free minimum degree`, `"On regular hypergraphs of high
girth" Ellis Linial pdf`, `"four-uniform" "three edges" "nine"
hypergraph`, `"G_4(9,3)"`, and `"hypergraph" "16" "girth"
"4-regular"`. Searches for Brown–Erdős–Sós terminology and regular
hypergraphs supplied comparison leads rather than an exact import of
TARGET. Search failure does not establish novelty.

Chong Shangguan, *Degenerate Turán densities of sparse hypergraphs II:
a solution to the Brown-Erdős-Sós problem for every uniformity*,
[arXiv:2210.11338v1](https://arxiv.org/pdf/2210.11338v1),
20 October 2022, Section 1, printed pp. 1–2, was inspected for the
definition, Theorem 3 and the adjacent proof outline/Lemma 4.
G_r(v,e)-free means every e distinct edges have union at least v+1;
the present negated target is G_4(9,3)-freeness. Theorem 3 concerns
existence of an asymptotic density limit for v=er-2(e-1), which gives
eight at r=4,e=3. Neither its parameter nor its asymptotic conclusion
settles the exact target. Its auxiliary exclusions do not supply the
required finite bridge. No inapplicable full proof is imported.

The separate search lead called the *even-uniform hypergraph Moore
bound* uses even covers, not the inspected Berge-cycle definition;
its theorem was not read or used. Other high-girth construction and
spectral-bound leads remain unread and are unnecessary once the
finite Ellis–Linial bound is available.

Locally, read L010's hypotheses, conclusion and equality/distinctness
proof, L023's cyclic incidence construction, L025's statement and
displayed edges, L072's affine-plane construction, and ATTEMPTS/016,
017,027. The existing three-support and nine-union assessments address
coding compatibility conditional on a chosen union, not extraction.
The matching/small-union assessment's prior sparse-hypergraph comparison
was reused for orientation; its different threshold is not approval of
this target. L072 explicitly includes a nine-union triple and so is
not a counterexample to TARGET. No new test of L023 or L025 is claimed.

## Recorded stops to retain

ATTEMPTS/016, through L023, blocks forcing three disjoint supports.
ATTEMPTS/017, through L025, blocks forcing six supports on at most eight
vertices under matching number two. ATTEMPTS/027, through L072, blocks
forcing a union-five/six additional pair from a prescribed triangle and
balance. These exact stopped statements differ from TARGET; this
comparison neither certifies their examples pass the new test nor
licenses reopening their stopped implications. The completed L083 audit
is independent of this proposed continuation and remains valid.

Full matching and supporting Mathlib coverage for the extraction and
the Moore bound: not checked. Unknown coverage is not absence. No
novelty claim is made. SPECIALIZE approves the unchanged TARGET for
one later REPRODUCTION proof attempt, with all bridge obligations above
retained. No lemma, script, extraction result or global bound was added.
