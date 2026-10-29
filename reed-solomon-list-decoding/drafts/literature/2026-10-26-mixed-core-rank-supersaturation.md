# Mixed-core rank-sensitive supersaturation comparison

TARGET: Assess whether a rank-sensitive two-core supersaturation argument can force an L031-nonrealizable four-support pattern in every packed pair of L030 ambient subfamilies of size at least 1532496.
CHECKED: 2026-10-26
DECISION: EXPLORE
SEARCH_EVIDENCE: Eight targeted queries compared fixed-evaluation RS rank, hypergraph removal/supersaturation and forbidden-intersection results; primary statements below were inspected. Scoped local reads covered L030/L031/L130/L131, the two mixed-core assessments, ATTEMPTS/031–032,103–106 and history/508–509,511. No inspected theorem supplies the universal finite bound; no novelty claim follows.
SOURCE_EVIDENCE: Reused AGL arXiv:2304.09445v3 Definition 2.5/Lemma 2.7 and L031's audited specialization; rechecked Theorem 2.9/Remark 2.10, p. 9. Read Rodl–Schacht, Generalizations of the removal lemma, author PDF Theorems 2 and 6, pp. 2–3; Ferber–McKinley–Samotij arXiv:1710.04517v1 Theorem 13, p. 8; Keevash–Long, Trans. AMS 369 (2017), Theorems 1.7 and 1.10, p. 1149, with the cross-version warning.
COMPARISON: Signed matrices provide a necessary common-center restriction, not its frequency in arbitrary relabeled families. Removal needs distance from a forbidden-pattern-free class; balanced sparse supersaturation needs extremal bounds; forbidden-intersection theorems concern cardinalities in full layers/Hamming spaces, not actual-label signed rank. None establishes the requested threshold 1532496 on this fixed domain.
GAP: Universal full-rank occurrence remains open. First test whether the synchronized auxiliary quadratic-translation orbit of the audited L131 example can even force a witness at the retention threshold for its fixed maps; a positive result would still require arbitrary-label uniformity, packing-to-list transfer and a global cap.
REASON: This completes essential source comparison for the universal target and selects a finite rank-sensitive coverage test rather than assuming that one embedding or ambient density supplies supersaturation.
SCOPE: The proposed universal scope below is unchanged; its truth is not asserted. The separately specified continuation tests only one fixed-map witness mechanism, with no claim of a packed counterexample from a witness-cover alone.

LITERATURE_REASON: Invocation-start REVIEW_REQUIRED explicitly lacked theorem-level coverage for universal density and a bounded test. This review supplies that comparison; it does not repeat the ready prescribed-embedding review or derive a lemma.

## Exact reviewed scope

Use L030's q=137, seven columns and four dummies in the pinned
E=F_65537, F=F_(65537^28), H of order 1024, k=64 instance.
Let C=K union {a}, C'=K union {b}, with |K|=60 and a!=b outside K.
Allow arbitrary actual-label bijections to H minus the corresponding
core, with the distinguished left graph image b and right dummy image
a as in L130. Consider subfamilies on each side of size at least
1532496 whose distinct supports jointly intersect in at most 63 points.
No marginal law or RS realization is assumed. An eventual universal
statement must quantify over these bijections and retained subfamilies,
not just L131's single labeling.

The proposed obstruction is two selected supports per side with common
60-core K, six mutually disjoint pair-only two-sets and four disjoint
private two-sets, satisfying L031's hypotheses, and whose signed
12-by-12 matrix has full rank over E. Actual labels must be retained;
an incidence pattern or generic-domain rank theorem alone is inadequate.
The proposed forcing statement is a target for assessment, not a result.
If forced, it could give a mixed-core common-center cap. Transfer from
such a cap to the whole list and arbitrary-center safety remains an
independent unresolved step.

## Primary theorem comparison

The prior `2026-10-26-mixed-core-common-center-rank.md` and
`2026-10-26-mixed-core-l031-embedding.md` already assess the signed
matrix and common-root inputs. Reuse their AGL v3 Definition 2.5 and
Lemma 2.7, pp. 7–8, and Shangguan–Tamo v1 Lemma 4.3 specialization;
do not reprove them. A fresh check of [AGL v3](https://arxiv.org/pdf/2304.09445v3),
Theorem 2.9/Remark 2.10, printed p. 9, confirms that full rank is over
F_q(X_1,...,X_n). It does not certify specialization to H. L031's
antipodal example already prevents treating incidence as sufficient
for actual-label nonrealizability. L131 imports the consecutive example
at its original labels; its arbitrary bijection completion is not a
symmetry preserving rank.

Vojtech Rodl and Mathias Schacht, *Generalizations of the removal lemma*,
[author PDF](https://www.math.uni-hamburg.de/home/schacht/2009/gen_removal.pdf),
25-page version at that URL checked 2026-10-26, Theorem 2, p. 2:
for a fixed k-uniform F on ell vertices and eta>0 there are c>0,n0
such that an n>=n0 vertex hypergraph with at most c n^ell copies of F
can be made F-free by deleting at most eta binom(n,k) edges.
Theorem 6, p. 3, extends to induced forbidden families using bounded-size
tests and edge additions/deletions. Neither asserts that density alone
forces a specified pattern. We lack the needed distance-from-free
premise and quantitative applicability at this instance. Encoding labels
or rank would require justification; induced removal does not supply it.
Both complete theorem statements, rather than their proof machinery,
were inspected: no application is made.

Asaf Ferber, Gweneth Anne McKinley and Wojciech Samotij,
*Supersaturated sparse graphs and hypergraphs*,
[arXiv:1710.04517v1](https://arxiv.org/pdf/1710.04517v1),
12 October 2017, Theorem 13, printed p. 8, requires gamma>1,
alpha>r-1/m_r(J) and ex(s,J)<=M(s/n)^alpha for every 1<=s<=n.
For gamma^t M<e(G)<=gamma^(t+1)M with integer t>t0 it gives a
collection of J-copies with controlled codegrees (equation (11), all
1<=ell<=e(J)); t0 depends on alpha,gamma,J. The full statement,
including its enumeration consequence, was inspected. Here no such
extremal estimate or rank-preserving encoding is supplied. Thus this
theorem cannot replace the missing finite extremal bound by an appeal
to containers or balanced supersaturation. Its published numbering may
differ; this citation deliberately pins v1, Theorem 13.

Peter Keevash and Eoin Long, *Frankl–Rodl-type theorems for codes and
permutations*, Trans. AMS 369 (2017), 1147–1162,
DOI [10.1090/tran/7015](https://doi.org/10.1090/tran/7015),
[author PDF](https://people.maths.ox.ac.uk/keevash/papers/franklrodl-journal.pdf),
Theorem 1.7, p. 1149, bounds the product of sizes of two k-uniform
families avoiding one cross-intersection ell, for k=floor(alpha n)
and ell separated by epsilon n from both feasible endpoints, by
(1-delta)^n binom(n,k)^2. Theorem 1.10 gives distance supersaturation
in a Hamming space above its stated near-full exponential size
threshold. The intervening warning says the improved cross-versions
of Theorems 1.3/1.4 do not hold generally. These are pair-cardinality
relations, not four-support signed determinants. Density inside L030's
q^3-block family is not the requisite density in an entire layer or
Hamming space; an arbitrary relabeling adds no rank guarantee. These
statements were inspected and excluded, not imported as a bound.

## Search and local failure record

Queries on 2026-10-26 (search snippets alone are not coverage):

- `Reed Solomon intersection matrix supersaturation fixed evaluation set agreement hypergraph`
- `hypergraph removal lemma partite forbidden configuration supersaturation density theorem`
- `Reed Solomon higher order MDS fixed evaluation points full rank intersection matrix generic`
- `"Reed Solomon" "supersaturation"`
- `"intersection matrix" "fixed" "subgroup" Reed Solomon`
- `"forbidden intersections" "Frankl" "Rödl" theorem uniform families`
- `"Supersaturated Sparse Graphs and Hypergraphs" arxiv`
- `Rödl Skokan hypergraph regularity applications removal theorem 5 pdf`

AGL and the prior BGM comparison supply the generic-rank distinction.
Sparse supersaturation was recovered at arXiv after the author URL
returned 502 and the DOI redirect failed; no v2 exists at the tested
URL. A removal-paper DOI and a PMC landing page were inaccessible;
the full Rodl–Schacht author PDF supplied the comparison instead.
Those access failures are not persistent essential blockers. Search hits
on recent forbidden sparse intersections, forbidden code intersections,
ordered removal and a higher-order MDS proceedings paper were not
inspected or used; this is bounded comparison, not exhaustive coverage.

L030 is a genuine arbitrary-label single-core packing, so an ambient
configuration budget alone cannot establish its false local cap
(ATTEMPTS/103). L125's full-law coupling failure and L126's full-star
thinning failure (ATTEMPTS/104–105) require their respective extra
hypotheses. L130, accepted separately, closes retention-only star-overlap
forcing (ATTEMPTS/106). Its averaging proof does not promise that any
L131 witness survives; L131 does not promise its fixed maps admit L130's
retention bounds. Neither settles this universal rank-sensitive target.

ATTEMPTS/031–032 concern the exact common-shift and auxiliary affine
single-core cap mechanisms, with explicit deletion obstructions. The
proposed continuation uses mixed-core actual-label four-support rank
and a different finite witness collection. It must not quietly revive
those stopped caps or infer a new obstruction merely by renaming them.

## Decision and bounded continuation

No checked theorem proves or disproves the reviewed universal assertion.
EXPLORE means only that this bounded comparison found no adequate match.
The exact continuation is recorded in
`2026-10-26-synchronized-translation-witness-cover.md`. It tests whether
one natural enlargement of L131's isolated embedding has enough witness
coverage at all, before investing in a label-uniform forcing proof.
That is a narrower intermediate target, not a replacement theorem for
the universal assertion. Positive fixed-map coverage would leave
arbitrary-label uniformity and global list transfer unresolved.

This completed literature step performs no orbit enumeration, determinant
calculation, new proof or lemma/script write. Its outcome is EXPLORATION:
new source comparison and a concrete test, not an informative mathematical
negative or a new theorem. Full/supporting Mathlib coverage is not checked;
no cross-notebook result is used. A protected creative universal argument
is not yet justified: an actual-label expansion mechanism remains missing.
The finite coverage diagnosis is an ordinary calculation, not creative
research relabeled to meet scheduling targets. The new continuation's
approval is deferred to a separate supervisor turn.
