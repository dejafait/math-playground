# One additional agreement: completed coefficient-fiber assessment

TARGET: Determine whether monic degree-(k+1) root products with a common X^k coefficient give a threshold-relevant attained list at A=k+1 on the pinned smooth domains for every m>=1.
CHECKED: 2026-10-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the endpoint construction assessment; searched degree-(k+1) RS lists, prescribed coefficient fibers and subset sums over multiplicative subgroups. The new primary readings and exact queries are recorded below; full-field formulas were distinguished from subgroup estimates and unread leads.
SOURCE_EVIDENCE: Read Zhu-Wan arXiv:1101.0289v1 (2010-12-31), Theorem 1.1, Corollaries 4.2 and 4.5 and their surrounding Section 4 passages; Li-Wan arXiv:0708.2456v1 (2007-08-18), Theorem 1.2 and the Section 5 coefficient/factorization passage; and Li-Wan arXiv:1806.00152v3, Section 1.2 and Theorem 1.5. Reused Ben-Sasson-Kopparty-Radhakrishnan, Section 1.3 and Proposition 3.4, with the changed coefficient scope checked directly.
COMPARISON: The coefficient-collision construction and the scalar coefficient/subset-sum correspondence are known. Subgroup fiber estimates cover the domain's algebraic structure; an exact formula covers a full nonzero field. These do not directly state the pinned coset/interleaved list or its comparison with the ambient epsilon* q, and none determines the full worst-case boundary.
GAP: A later applicability argument must check the coefficient sign, strict degree cancellation, prescribed roots, distinct evaluation words, common-center and simultaneous agreement, then compare a certified fiber count with epsilon* q in a fixed admissible instance. Exact largest fibers on general smooth domains and the general sharp boundary remain unresolved.
REASON: Approve this bounded reproduction of known constructions and cited counts. Import the counting results rather than reprove their sieves; derive only the identified domain/metric and threshold applicability. This turn completes source coverage without constructing a local center, proving an A=k+1 bound or running a calculation.
SCOPE: The unchanged TARGET, for pinned smooth cosets L=aH of power-of-two order n>=16 at the four prize rates, row degree less than k, m>=1 and closed column-Hamming balls at A=k+1. Covers the coefficient-fiber/common-pivot specialization, elementary coefficient-collision averaging, citation-based subgroup estimates or exact full-nonzero-field counts, and a fixed-instance threshold test, including a domain contained in a subfield. Does not approve a sharp worst-case equality, uniform fiber distribution, other agreement levels, differential covers or ABF26 retrieval.
COVERED_TARGET: Verify the coefficient-fiber/common-center correspondence at A=k+1 with strict degree less than k and simultaneous agreement for every m>=1.
COVERED_TARGET: Apply the cited subset-sum counts to one pinned smooth instance, retaining the ambient field in the threshold and any smaller field containing the evaluation domain only in the source count.

LITERATURE_REASON: A=k+1 introduces a fixed next-to-leading coefficient outside the prior A=k assessment's SCOPE; an essential theorem-level comparison for subset-sum fibers on multiplicative domains was missing.

## Gap, use and continuation test

The current endpoint reproduction is recorded in
[L011](../../lemmas/L011-root-product-endpoint-attainment.md). It shows that
the boundary must move below n-k when the exact endpoint condition fails,
so an actual-list construction at the next agreement level could bound
that movement. The [endpoint assessment](2026-10-03-root-product-endpoint.md)
does not cover this target: its SCOPE ends at A=k. The research target has
been preserved verbatim during this separate review.

The precise main gap is the value of t_star below n-k when
1<=epsilon* q<binomial(n,k). An actual list at k+1 simultaneous agreements
could supply an unsafe-radius certificate one grid point inside the known
endpoint. The test is to certify a single center's candidate count and
compare it with epsilon* q for the given field, with threshold equality
retained. A successful lower witness would constrain t_star; it would not
bound lists around every center or locate the complete boundary.

Continue if the cited mechanism survives the degree, distinctness, domain
and common-column checks and its certified count exceeds the actual
threshold in a stated admissible instance. Stop the proposed specialization
if those checks fail. If the available lower certificates cannot affect the
threshold in the chosen instance, stop that instance test; a vacuous
character-sum estimate or unsuccessful lower witness does not certify
safety or refute all coefficient-fiber constructions. No such calculation
or continuation result is asserted in this review.

## Primary statements actually inspected

**Common pivot.** Ben-Sasson, Kopparty and Radhakrishnan,
[Subspace Polynomials and List Decoding of Reed-Solomon Codes](https://www.math.utoronto.ca/swastik/rsld.pdf),
author-hosted eight-page manuscript, Section 1.3, printed p. 3, and
Proposition 3.4 with proof, p. 6. The manuscript has no recovered revision
identifier. Its scalar, full-field argument partitions monic root
polynomials by high coefficients and obtains at least
binomial(N,T) N^{-(T-K-1)} candidates with degree at most K and T agreements.
Proposition 3.4 relates a common-pivot root-rich family to one received-word
list. This is known construction coverage, reused from the endpoint review;
its additive-subspace theorem is outside the present domain comparison.
No prescribed-domain or interleaved bound is imported from that theorem.

**Multiplicative subgroup counts.** Zhu and Wan,
[An Asymptotic Formula For Counting Subset Sums Over Subgroups Of Finite Fields,
arXiv:1101.0289v1](https://arxiv.org/pdf/1101.0289v1), dated 2010-12-31;
[matching HTML](https://arxiv.org/html/1101.0289v1). Read Theorem 1.1, p. 2,
and Section 4, including Corollary 4.2, p. 16, and Corollary 4.5, p. 17.
Use s for subset cardinality and i for subgroup index to avoid confusing
the source's k and m with message dimension and interleaving width. For
H<=F_Q^*, i=[F_Q^*:H], characteristic p and 1<=s<=|H|, the source counts
unordered subsets M_H(s,b) with sum b. Its main term is
Q^{-1} binomial((Q-1)/i,s). Theorem 1.1 gives the errors

\[
\begin{cases}
\displaystyle {2\over\sqrt Q}
 \binom{\sqrt Q+s+Q/(ip)}s,&b\ne0,\\[3pt]
\displaystyle \binom{\sqrt Q+s+Q/(ip)}s,&b=0.
\end{cases}
\]

Corollary 4.5 states the tighter zero-sum error
binomial(sqrt(Q)+s-1+Q/(ip),s); no local reproof is supplied. The weaker
Theorem 1.1 estimate is sufficient coverage for the planned test.
Corollary 1.2's positivity result additionally assumes p>2,
i<c sqrt(Q) and 6 ln(Q)<s<=|H|/2. Positivity alone is insufficient
for the notebook's list threshold. The estimates need not be useful at
every allowed index. Ordered counts N_H in Section 4 are different objects.

**Exact full-nonzero-field count and scalar dictionary.** Li and Wan,
[On the subset sum problem over finite fields,
arXiv:0708.2456v1](https://arxiv.org/pdf/0708.2456v1), dated 2007-08-18.
Read Theorem 1.2, p. 2, and Section 5, pp. 14-15, especially the
factorization/coefficient passage on p. 15. For F_Q of characteristic p
and 1<=s<=Q-1, the theorem gives the exact number of s-element subsets of
F_Q^* of sum b:

\[
 N(s,b,F_Q^*)={1\over Q}\binom{Q-1}s+
 {(-1)^{s+\lfloor s/p\rfloor}v(b)\over Q}
 \binom{Q/p-1}{\lfloor s/p\rfloor},
 \qquad v(0)=Q-1,\quad v(b)=-1\ (b\ne0).
\]

Section 5 uses arbitrary distinct evaluation sets D and message degree at
most k-1. It relates maximal-root agreement for a monic degree-(k+m)
received polynomial to factorization over D with matching leading
elementary symmetric coefficients. Its m is degree excess. That scalar
correspondence directly supports the proposed coefficient test, but is
not a theorem about the worst-case interleaved list size. The exact formula
requires F_Q^*, rather than an arbitrary subgroup; applying it within a
subfield needs the embedding and domain hypotheses checked separately.

**Full-field distance distribution.** Li and Wan,
[Distance Distribution in Reed-Solomon Codes,
arXiv:1806.00152v3](https://arxiv.org/html/1806.00152v3), dated 2019-07-30.
Read Section 1.2, p. 3 in the corresponding PDF, and Theorem 1.5, p. 4.
Section 1.2 attributes exact degree-(k+1) formulas to Zhou, Wang and Wang,
reference [25]; it does not display that formula. Theorem 1.5 gives a
general root-count estimate after explicitly restricting D to F_q.
Neither is silently used as a multiplicative-subgroup formula. The already
checked Corollary 1.6 at degree k is only endpoint coverage.

The source formulas above are transcribed named results, not new local
inequalities. PDF screenshots were requested for the theorem/coefficient
pages but returned references without readable images; PDF text and the
Zhu-Wan and 2019 Li-Wan HTML supplied the inspected statements. No source
access failure blocks the selected specialization.

## Applicability and redundancy comparison

| Known coverage | Remaining local check and limitation |
| --- | --- |
| Monic high-coefficient collision and common pivot | Match degree at most K to strict degree less than k, retaining the common X^k constraint at the changed agreement level. Do not repeat the endpoint proof as if it settled this fiber. |
| Scalar coefficient/factorization dictionary on D | Check the coefficient sign and all prescribed roots, construct one received word, and establish distinct evaluation candidates. Only then count its list. |
| Subgroup subset sums | For L=aH, justify any rescaling of roots and sums before applying a theorem about H. Do not assume uniform distribution or use an ordered count. |
| Exact F_Q^* formula | Check the full-nonzero-field domain hypothesis. If that field is a subfield of the ambient F_q, track both field sizes: the prize threshold still uses q. No subfield applicability result is proved here. |
| Scalar list | Check the common received array and simultaneous agreement for every m>=1. Independent row lists or a power-of-m extrapolation do not suffice. |
| Fiber count at one center | Compare to epsilon* q, including equality and epsilon* q>=1; do not infer the worst-case maximum or safety from failure of a lower certificate. |

L001's bound at A=k+1 can be used as an already established upper comparison,
but there is no attainment theorem at this level in the notebook. L011
settles only A=k. The earlier field-polynomial transfer and unfiltered
Riccati failures concern different gaps; neither has been reopened. The
simple-zero source blocker remains parked in its existing assessment and
attempt record. The independent target does not require ABF26 to be read
before its explicitly pinned-model test.

The strongest relevant inspected coverage is exact scalar subset counting
on F_Q^* and explicit subgroup fiber estimates, together with a known
common-pivot construction. No inspected theorem determines the largest
fiber for every pinned domain, states the complete simultaneous-interleaved
TARGET, or gives the all-field sharp list boundary. This bounded review
therefore authorizes SPECIALIZE and a later REPRODUCTION, not a novelty
claim. Import the named counting theorems; a local proof is warranted only
for the displayed applicability differences and effective threshold test.

## Search record and unread leads

Reused the [endpoint assessment](2026-10-03-root-product-endpoint.md)'s
construction and domain exclusions. The changed-scope queries were:

- `Reed Solomon list size subset sum multiplicative subgroup common coefficient root polynomial Li Wan`
- `Zhu Wan subset sum problem multiplicative subgroups finite fields theorem`
- `Li Wan distance distribution Reed Solomon degree k+1 evaluation subset subset sum`
- `"subset sum" "multiplicative subgroup" "exact formula" Reed Solomon`
- `"Reed-Solomon" "k+1" "multiplicative subgroup" subset sum list size`

Following Zhu-Wan reference [4] recovered the versioned Li-Wan 2007
manuscript and its explicit theorem, rather than relying on an original
reference that remains unread. The 2018 paper *The k-subset sum problem over
finite fields*, [DOI](https://doi.org/10.1016/j.ffa.2018.02.001), was located
through publisher abstract/search text; a direct reader request failed.
Its theorem statements were not read and it is not an input. Zhou-Wang-Wang
reference [25], the original Justesen-Høholdt paper, and the later journal
versions of the inspected manuscripts were not read. None is essential
to the bounded application of the explicit primary statements above.
Traceability-code results, changed metrics and an unversioned web claim of
a prize reduction were discovery leads only; no theorem from them was
inspected or relied on. Failed or incomplete searches certify no novelty.

## Completed review and continuation

Outcome: EXPLORATION; STEP_KIND: LITERATURE; classification:
NOVELTY_UNCHECKED. The new subgroup theorem and exact-count comparison
complete the missing source scope and make the unchanged target ready.
Known results are recorded by citation; no local mathematical input has
been added to the assembled argument and no progress beyond the checked
literature is claimed. A later completed specialization should be labeled
REPRODUCTION. Exploration turns remain 0/3: literature spends no
calculation budget. No center, fiber value, threshold inequality for the
pinned domain, computation, new lemma or complete candidate was produced.
The boundary and ABF26 comparison remain unresolved.

## Mathlib

Full coefficient-fiber and interleaved A=k+1 statement: **not checked**.
Supporting subset-sum and root-polynomial theorem coverage: **not checked**.
Formal versions of the named Zhu-Wan, Li-Wan and common-pivot results:
**not checked**. The pinned ArkLib definitions are present as recorded in
the model; they supply conventions rather than this construction or its
count. No full matching library theorem is asserted.
