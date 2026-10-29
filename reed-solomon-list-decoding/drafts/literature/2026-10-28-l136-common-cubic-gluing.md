# Common cubic for all retained components — specialization coverage

TARGET: Assess whether the per-triple cubics in L136 force one nonzero homogeneous cubic over K containing all six or seven retained dual direction components, including every reducible and collinear case.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the per-triple assessment and searched the specific cone/bridge/cyclic assessments, histories 523/525/530/533 and ATTEMPTS/031–032,109 for gluing and ordinary-net failures; new queries and exact reading limits are recorded below. No exact all-label gluing theorem was located in this bounded search; no novelty claim follows.
SOURCE_EVIDENCE: Inspected Bogya–Korchmaros–Nagy arXiv:1601.08009v1, pp. 1–3 definitions/scope, pp. 4–8 Propositions 2.1–2.4/3.1–3.3/4.3 and Corollaries 3.4/4.4 with proofs, pp. 9–13 Proposition 5.1/Theorems 5.2–5.3/Corollary 5.4 and the relevant cubic cases; reused and reread Korchmaros–Nagy arXiv:1710.00172v1 pp. 3–4 Lemmas 2.2/2.4/2.5 and p. 8 Section 4 setup. L135/L136 supply separation and per-triple cyclic labeling/cubic containment, not the missing ordinary-net upgrade.
COMPARISON: The strongest relevant inspected input excludes an ordinary dual 4-net of order at least seven with an algebraic derived triple; use the conservative characteristic condition p>n throughout the reducible cases. It can replace geometric gluing in the noncollinear branch only after proving the local incidence upgrade; the wholly collinear branch and descent remain explicit obligations.
GAP: Establish, rather than assume, a prime-order all-collinear/ordinary-net dichotomy for the simultaneous L135 components, then justify the imported exclusion and a containing form over K. Neither this dichotomy nor common-cubic containment is proved in this literature turn.
REASON: Exact primary coverage now supports a bounded known-theorem specialization, avoiding an unsupported uniqueness claim for cubics sharing components. Derive only the local applicability difference in a later research turn; do not reprove the cubic classification or exclusion theorem.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED: per-triple coverage did not include simultaneous gluing or the ordinary dual-4-net exclusion. This review closes that essential source-comparison gap; it is not additional browsing of an already ready target.
SCOPE: L135/L136 hypotheses unchanged: q=137, K=E or F of characteristic 65537, arbitrary permitted actual 61-core/bijection, coefficient-difference span exactly two, repeated messages, six or seven complete retained directions, all singular/reducible/collinear possibilities retained.
COVERED_TARGET: Determine whether all retained dual direction components in L135 lie on one nonzero homogeneous cubic over K, using L136 and a prime-order light-to-ordinary-net dichotomy with the algebraic dual-4-net exclusion.

The main gap remains arbitrary-center 67/68 safety. A common containing
cubic could supply a single geometric object for later comparison with
the evaluation-label restrictions. It would still leave span-two
collapse, span three, deletion robustness and RS transfer unresolved.

## Primary sources and qualifications

Norbert Bogya, Gábor Korchmáros and Gábor P. Nagy, *Classification of
k-nets*, *European Journal of Combinatorics* 48 (2015), 177–185,
[DOI](https://doi.org/10.1016/j.ejc.2015.02.019), inspected
[arXiv:1601.08009v1](https://arxiv.org/pdf/1601.08009v1).
The arXiv wrapper says 29 January 2016; the retrieved 15-page manuscript
internally says 15 February 2018. Page references below are printed
manuscript pages, not journal pagination.

Corollary 5.4, p. 13, excludes an embedded ordinary dual 4-net of
order n>=7 over an algebraically closed field of characteristic other
than 2 or 3 when a derived triple lies on a plane cubic. Retain p>n:
the reducible branches use that stronger condition. Corollary 3.4,
p. 7, excludes regular/triangular derived triples; Corollary 4.4,
p. 9, excludes conic-line triples. Section 5, p. 9, reduces reducible
cubics for ordinary nets to these types. Theorem 5.3, p. 13, treats
irreducible cubics: singular curves and nonsingular curves with nonzero
j-invariant have no perspective center; j=0 permits at most three.
The proof chain inspected includes constant cross-ratio (Proposition
2.3), the seven-triple criterion (Proposition 5.1), nodal and nonsingular
calculations, and Theorem 5.2. The cuspidal computation is described
but omitted by the authors; no independent reproof is claimed here.
This is a theorem import, with the conservative characteristic scope,
not an independent critical audit of every source calculation.

Gábor Korchmáros and Gábor P. Nagy, *Group-labeled light dual
multinets in the projective plane (with Appendix)*,
[arXiv:1710.00172v1](https://arxiv.org/pdf/1710.00172v1),
30 September 2017, Lemmas 2.2/2.4/2.5, pp. 3–4, give equal component
intersection sizes on a multinet line, principal loop relabeling and
a subloop describing that intersection. Section 4, p. 8, uses a
maximal-line subgroup for a group labeling and explicitly separates
the wholly collinear case. These are source inputs for a proposed
prime-order incidence specialization; they do not themselves state
the local simultaneous dichotomy. Proposition 4.5 remains the audited
per-triple input through L136.

Korchmáros–Nagy–Pace,
[arXiv:1104.4439v3](https://arxiv.org/pdf/1104.4439v3),
17 June 2011, Section 4, p. 7, calls the cubic of an algebraic ordinary
dual 3-net of order at least four uniquely determined. This terminology
does not identify cubics for different triples or cover light
degenerations. The existing cyclic assessment supplies the already
inspected Proposition 6.1 propagation input; it is reused, not reproved.
No assertion that two shared components alone determine a cubic is
imported. Bézout with possible common components is insufficient for
such an assertion.

## Explicit obligations for the later specialization

These are unproved tasks, not a proof or new lemma.

1. Use L136's actual index permutations for each triple. Justify that
   the principal loop relabeling in Lemmas 2.4/2.5 has the needed group
   structure in this cyclic prime-order setting; do not silently apply
   group subgroup divisibility to an arbitrary quasigroup subloop.
   Determine all permitted sizes of an intersection with a line meeting
   two components, including the size-137 possibility.
2. Prove compatibility across triples. In particular, handle a wholly
   collinear triple and propagation to every other retained direction.
   If the full union is not collinear, establish exact one-point-per-
   component incidence for four chosen components. Injectivity alone
   does not supply this property. Account for repeated g_P and repeated
   connecting lines. No ordinary-net hypothesis may be assumed.
3. Only in a proved ordinary-4-net branch invoke the cited exclusion,
   using a derived triple's L136 cubic over the algebraic closure.
   Check n=137>=7 and p=65537>n, all component separations, and the
   definition of a perspective center if that formulation is used.
   Do not assume any cubic is irreducible or its factors descend.
4. In every surviving branch justify a nonzero degree-three form over
   K, rather than merely over its algebraic closure. Reuse L136's
   rational-point/rank-descent method or its line branch as applicable;
   a new proof of descent is unnecessary. Do not claim span-two
   impossibility, a retention bound or RS transfer from source coverage.

Continue only if all obligations give the saved common-containing-form
conclusion under the unchanged hypotheses. If the incidence upgrade
fails, preserve its exact permitted configuration or missing implication
and stop this specialization; do not replace it by generic labels or
assert cubic uniqueness. This is an independently testable incidence
mechanism, not ATTEMPTS/109's stopped residual-rank computation.
ATTEMPTS/031–032 concern local cap failures; they remain valid and do
not forbid this source-based test. Both failed direction-omission probes
also remain preserved. No cross-notebook input is proposed.

## Search record, coverage and next gate

Queries: `light dual multinet cyclic algebraic cubic common components
Korchmaros Nagy`; `dual k nets algebraic cubic reducible components
Bezout four nets finite characteristic`; `"Classification of k-nets"
Nagy Pace arxiv theorem 1.1`; `"algebraic" "dual 4-net" cubic common
component`. Search snippets were leads only; the cited primary PDFs
supplied the theorem statements and proof-case comparison. Searches of
the specific local assessments and failure files found no ready coverage
of this simultaneous upgrade. No claim of exhaustive literature search
or mathematical originality is made.

Mathlib coverage of light multinets, the simultaneous incidence upgrade
and the algebraic dual-4-net exclusion was not checked. No absence is
asserted; L136's supporting field-extension/root-bound coverage is
unchanged.

The assessment is SPECIALIZE for the unchanged review target and its
single covered mathematical continuation. It needs separate supervisor
approval before that continuation is invoked. No local gluing theorem,
collapse, new lemma, mathematical script, DAG edge or main argument was
derived or changed in this literature-only turn. The July ABF source
qualification, the 955–957 bracket and all independent main-goal gaps
remain unchanged.
