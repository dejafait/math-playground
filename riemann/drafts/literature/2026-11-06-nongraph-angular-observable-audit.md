# First conceptual audit of the non-graph angular obstruction

TARGET: Critically audit L857's exclusion of L856's non-graph annular fillings, checking whole-chart primitives, angular extrema, induced boundary signs and the first-observable error against r M_0, including n=1.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed bounded searches and duplicate/failure comparison in 2026-11-06-nongraph-annular-filling-scope.md and the invocation-start 2026-11-06-nongraph-angular-observable-test.md; the target is the first audit of that single test's completed proof, with unchanged surface class, pair, chart, collars and observable. No fresh search or novelty inference is made.
SOURCE_EVIDENCE: Reuse inspected Lebl SCV v4.4 TheoremC.6/proof p224 and Theorem1.2.1/proof pp20-21, https://www.jirka.org/scv/scv.pdf ; Lebl Basic Analysis I v6.3 Theorem7.5.6 p290/Lemma4.2.2 pp162-163 and Basic Analysis II v6.3 Theorem8.3.7 p38; L855's inspected Lebl CA v1.10 Corollary3.2.12/proof pp67-68; L856's di Dio-Schmudgen arXiv:1809.00584v1 positivity(5)/Definition5 pp4-5/Proposition24(i) p12. No immersion or filling theorem is imported.
COMPARISON: The standard sources cover joint primitives, manifold Stokes, extrema/Fermat/chain rule and positive integration; they do not directly state this fixed angular separator. The audit must check the specialization in L857 without assuming a w-graph or a smaller allowed chart.
GAP: Independently verify or repair L857's whole-B primitive, use of real restricted omega, boundary orientations and all error bounds at the vanishing-mass scale; the new proof has not had its first independent audit. Actual exterior data and all-degree signs remain outside its conclusion.
REASON: This reuses adequate standard-tool coverage for an essential first conceptual audit of the completed mathematical attempt. Separate literature-only review completed on 2026-11-06: the reused coverage is adequate for the exact first audit; this source-gate approval does not audit or approve L857's proof.
SCOPE: Exactly TARGET; fixed actual G,R,C and pair of L855/L856, finite n>=1, original product, unchanged B/log branches, exact inward collars, compact smooth embedded oriented annulus, nonnegative real full form including zeros, strictly positive original angular two-form. No new observable, different collars, filling construction or global sign argument.

## Reused evidence and the precise critical checks

The primary hypotheses and proof cases were actually inspected in
`2026-11-06-nongraph-annular-filling-scope.md`,
`2026-11-06-actual-g-real-zero-interval-stationarity.md`, and the
source notes retained in L855/L856. Haskins-Pacini remains a comparison
only; its relative immersion theorem supplies no input here. No new
essential source or changed mathematical hypothesis is being introduced.

Audit the completed proof in
`lemmas/L857-angular-first-moment-excludes-nongraph-annular-fillings.md`.
In particular, check the normalized logarithms and the segment primitive
on the original product before composition with the inverse chart. A
primitive valid only near the circles does not suffice. Distinguish
the closed holomorphic weighted form from the real angularly weighted
ambient form; verify the use of reality only after pullback to Sigma.

Check compact extrema with full-rank angular projection at every point,
including zeros of w or omega and folds of w. Check the exact inward
collars and the induced outer/inner signs. Independently reproduce the
linear coefficient, Laurent contribution, integrated remainders and
comparison with r M_0, especially the limiting multiplicity n=1.
The small compact neighborhood used for boundary Taylor estimates must
not become an unstated restriction on the rest of the filling.

Accept only the local conditional obstruction if these checks all pass;
otherwise repair or withdraw the unsupported portion while preserving
the attempt. Do not repeat the completed L856 audit or start a sequence
of higher moments. This is an audit nomination, not another proof or a
new filling claim. Actual matching, global homology/exchange, other
orders and the L030-L032/C032a positivity gap remain unresolved.

Full matching Mathlib coverage is unchecked. The previously inspected
supporting [coordinate Fermat theorem](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/LocalExtr/Basic.html#IsLocalMax.hasFDerivAt_eq_zero)
does not establish this surface obstruction. No cross-notebook input.

## Separate source-gate review — 6 November 2026

Approved for the exact TARGET, with DECISION unchanged at SPECIALIZE.
This review read the parent scope assessment's inspected-tool and
search/failure comparison (sections “Inspected and reused tools” and
“Searches, duplicates”), the stationarity assessment's precise extrema
and chain-rule statements, the complete L857 to inventory its source
requirements, and L855/L856's relevant citation passages. It reused the
recorded primary inspections; no external source was newly opened.
Reading L857 here inventories coverage, not a mathematical audit.

| Audit obligation | Covered standard input | Still to be checked mathematically |
| --- | --- | --- |
| Primitive throughout B | Lebl SCV Theorem 1.2.1, including compact-subpolydisc convergence; CA Corollary 3.2.12 on star-like domains | Original product, branches, joint dependence, composition, derivative and smoothness at w=0 |
| Weighted Stokes and boundary signs | Lebl SCV Theorem C.6 for smooth oriented compact manifolds with induced boundary orientation | Closed holomorphic weighted form versus real restricted form; collar-induced signs |
| Angular extrema without a w graph | Basic Analysis I Theorem 7.5.6 and Lemma 4.2.2; II Theorem 8.3.7 | Nonzero angular differential at every interior point, including zeros and folds |
| Positive-measure comparison | di Dio–Schmüdgen v1 positivity (5), Definition 5, Proposition 24(i) | Real nonnegative pullback, bounded observable and strictly positive total mass |
| Boundary estimates | Joint holomorphic expansion on compact subpolydiscs; L855/L856 fixed chart and periods | Linear coefficient, Laurent term and every error at scale r M_0, including n=1 |

The SCV expansion theorem's closure hypothesis must be met on smaller
closed polydiscs inside the original holomorphic product. Such auxiliary
sets are for applying the cited theorem and bounding boundary traces;
they do not authorize restricting the hypothetical filling to a smaller
B. No general filling theorem, global logarithm on an arbitrary domain,
or ambient closedness of a real angularly weighted form is imported.
No new theorem is needed to pose these checks. The primitive and
vanishing-mass estimates remain precisely the specialization to audit.

The parent assessment already compares the relative immersion theorem
and records why it does not supply these constrained embedded fillings.
The existing scalar-flux and graph-only stops are preserved. The exact
first audit is neither a repeated L856 audit nor a higher-moment route.
No changed target, new essential unread source, or independently justified
central creative mechanism emerged. Full matching Mathlib coverage
remains unchecked; supporting coordinate Fermat coverage is not a formal
verification of L857. No lemma, calculation, or proof repair is made here.

This is a process approval with no new mathematical evidence, reported
STALLED rather than ADVANCE. The same exact TARGET is now ready for a
research audit without another source approval. Accept only after its
listed checks pass; repair or withdraw any unsupported portion otherwise.
