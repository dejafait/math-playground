# Degree-67 centers with one residual factor: completed assessment

TARGET: Determine whether a degree-67 scalar polynomial center over F_65537, with all other interleaved rows zero, gives an unsafe list at 66 agreements on the order-1024 subgroup inside F_{65537^28} at rate 1/16, for every m>=1.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched partial root agreement, three prescribed leading coefficients and subgroup distance distributions; read Gao's arbitrary-domain cofactor formula and the Gao-Li follow-up, then followed its Li-Wan reference through the latest version. Reused the adequate weighted-sieve review; exact queries and inspected passages are below.
SOURCE_EVIDENCE: Gao arXiv:2105.12845v3 Section 2, Proposition 1 and Theorem 1 equations (7)-(8); Gao-Li arXiv:2205.02277v1 Theorems 4-5, pp. 4-5, and Section 3, Proposition 2 equations (20)-(23) and Theorem 6, pp. 6-7; Li-Wan arXiv:1806.00152v3 Theorem 1.5, Lemma 4.1, Theorem 5.1 and equation (5.2); Lai-Marino-Robinson-Wan arXiv:1910.05894v2 Proposition 1 and Section 3 equation (4); Li-Wan arXiv:1507.06329v1 Theorem 2.1, Corollary 2.2 and Lemma 2.7.
COMPARISON: Residual-factor coefficient counts and the distinction between root-subset incidences and exact agreement counts are known, including arbitrary-D identities. The sharper distance-distribution error theorems use a full field, while Gao's explicit two-coefficient formulas use a subfield. Neither gives the requested effective proper-subgroup threshold comparison; known monomial character estimates and the arbitrary-domain weighted sieve support a bounded specialization.
GAP: Verify the degree-67/66-agreement dictionary, including possible extra roots and ambient-extension messages, then obtain and test an effective count on H against 65537^28/2^128. The largest list in this family and the maximum over arbitrary centers remain uncomputed.
REASON: Approve a mathematical application of known coefficient/cofactor and counting tools with only the changed subgroup, metric and finite-threshold checks derived locally. Citation alone does not settle those differences. No local constraint identity, list bound or threshold calculation is established in this review.
SCOPE: H of order 1024 in E=F_65537 inside F=F_{65537^28}, k=64, A=66, epsilon*=2^-128, degree-exactly-67 center over E, other rows zero and m>=1. Covers scalar normalization, the known leading-coefficient/residual-linear-factor correspondence, incidence versus exact-list accounting, extension-field and simultaneous-column checks, and a bounded effective upper/lower comparison using the cited character and weighted-sieve tools. Does not cover a new character-sum theorem, unrelated center degrees, the full-code sharp boundary or ABF26 retrieval.
COVERED_TARGET: Verify the exact degree-67/linear-cofactor correspondence at 66 agreements on the fixed order-1024 subgroup, including extra agreement roots, extension-field messages and every m>=1.
COVERED_TARGET: Test a uniform upper bound for every degree-67 center at 66 agreements on the fixed order-1024 subgroup using three-moment character estimates, the weighted distinct-coordinate sieve and the residual-linear-factor count against 65537^28/2^128.
LITERATURE_REASON: Degree 67 with 66 agreements introduces a residual linear cofactor; the ready assessment explicitly covers only maximal-root degree-66 centers and their two-moment fibers.

## Gap and discriminating test

[L014](../../lemmas/L014-rate-sixteenth-uniform-two-moment-upper.md)
settles the saved upper comparison: every assessed degree-66 center family
list at A=66 is below threshold. The largest safe error index for the
full rate-1/16 code remains at most 958, with its actual value unknown.
A degree-67 family is an independently testable intermediate step toward
the missing comparison over arbitrary centers. It retains the field,
domain and metric, while allowing a residual factor rather than requiring
all roots of a degree-66 difference to be agreement roots.

The later test should seek either a certified attained list strictly
above 65537^28/2^128 or a uniform upper bound for this new family at most
that threshold. An ineffective upper estimate or averaging lower bound
is inconclusive; record the limitation rather than infer full-code safety
or unsafety. Exact agreement sets, message degree and extension-field
messages must be checked. Arbitrary received arrays and the complete
sharp boundary remain later gaps even if this family is decided.

L013's unsuccessful rate-1/16 collision certificate and L014's successful
upper comparison are preserved. The established degree-66 upper is below
2^317, against the required threshold above 2^320. These are prior results;
they do not transfer to degree 67. This review addresses the changed
cofactor mechanism, rather than repeating that averaging test or a stop
review. Exploration turns used remain 0/3.

## Primary statements inspected

**Coefficient classes and residual factors.** Gao,
[Counting polynomials over finite fields with prescribed leading coefficients and linear factors, v3](https://arxiv.org/html/2105.12845v3),
2022-11-10, Section 2, Proposition 1 and Theorem 1, equations (7)-(8).
The first equation counts incidences with chosen distinct roots and a
monic cofactor of degree k+ell-r; the second uses inclusion-exclusion for
exact-root counts. The changed scope has ell=3 and r=66. Import this
framework, retaining the source's X+x convention. The explicit estimates
in Theorems 4-5 remain restricted to subfield domains and two coefficients.
Use the following paper's explicit D-based generating function when
specifying which extra roots are excluded.

**Arbitrary domains versus effective full-field estimates.** Gao and Li,
[Improved error bounds for the distance distribution of Reed-Solomon codes, v1](https://arxiv.org/html/2205.02277v1),
2022-05-04. Read Theorems 4-5, equations (7)-(14), printed pp. 4-5;
W_j counts root-subset/cofactor incidences, and the formulas recover exact
root counts and factorial moments for arbitrary D. Section 3 explicitly
sets D=F_q. Its Proposition 2 and Theorem 6, equations (20)-(24), pp. 6-7,
therefore do not provide a subgroup error theorem. The proof separates
the cofactor character sum from the root-domain sum; equation (22) bounds
the former. This is a useful supporting input if its character conventions
are matched, not permission to substitute |H| for q in the theorem.

**Original cofactor and character statements.** Li and Wan,
[Distance Distribution in Reed-Solomon Codes, v3](https://arxiv.org/html/1806.00152v3),
2019-07-30. Read Theorem 1.5, Lemma 4.1 (printed pp. 9-10),
Theorem 5.1 and its proof through equation (5.2), pp. 10-13.
The last passage explicitly factors a received polynomial plus a message
as a distinct-root product times a monic residual factor. Lemma 4.1 bounds
nontrivial residue-ring character sums, with an additional estimate for
characters trivial on field units. Theorem 1.5 and Theorem 5.1's numerical
estimates use roots in the full field; the primitive-code remark does not
cover a proper multiplicative subgroup. Read v2 first, then followed the
record's revision history to v3; use v3's numbering, not v2's Lemma 5.1.

**Moment characters on monomial images.** Lai, Marino, Robinson and Wan,
[Moment subset sums over finite fields, v2](https://arxiv.org/html/1910.05894v2),
2019-10-19. Rechecked Proposition 1, printed p. 6: a nontrivial additive
character sum of a degree-r polynomial on {x^d:x in F_Q} is at most
r sqrt(Q), provided p does not divide r and (d+1)^2<=Q. Read Section 3
through equation (4), pp. 19-20, for the distinct-tuple moment error and
cycle factorization. The count there is ordered. Theorem 10 adds
quantitative assumptions to conclude positivity, which does not answer
the required list-size comparison. The proposed application must handle
the zero element in the monomial image separately and use the actual
character parameter, rather than import that positivity theorem.

**Weighted sieve on an arbitrary domain.** Li and Wan,
[Counting polynomial subset sums, v1](https://arxiv.org/pdf/1507.06329v1),
2015-07-22, Theorem 2.1 and Corollary 2.2, p. 5; Lemma 2.7, p. 7.
Rechecked the weighted identity and cycle bound, reusing the
[existing assessment](2026-10-04-rate-sixteenth-joint-fiber-upper-bound.md)
for its Fourier normalization and applicability. These inputs allow a
later three-moment application on H without assuming H is a subfield.
Import them; reprove neither the sieve nor its cycle estimate.

The versioned PDFs of Gao v3, Gao-Li v1 and Li-Wan v3 were also opened
to check numbering and printed pages. The HTML supplied readable formulas.
The scalar maximum-root dictionary in Li-Wan's 2007 Section 5 and the
earlier common-pivot construction retain the adequate coverage recorded in
the [two-coefficient assessment](2026-10-04-two-leading-coefficient-fibers.md).
No full matching interleaved threshold theorem was found in these inspected
statements. This bounded comparison is not evidence of originality.

## Authorized specialization and continuation decision

Keep the coefficient field E separate from the threshold field F. A later
application should normalize an arbitrary nonzero leading coefficient
and account for lower message-degree translations before using monic
formulas. Check the cancellation through degree 64 explicitly. Establish
the residual factor's coefficient field for F-valued candidates; do not
silently limit messages to E. Check why the other interleaved rows are
forced to vanish on a list with the required common agreement columns.

Follow the source dictionary for the first three prescribed coefficients.
For fixed residual factor, Newton identities provide the standard link to
the first three power sums; verify signs and denominators locally. Root
subsets with a cofactor are incidence data, and a polynomial can be counted
from more than one chosen subset. Distinguish a residual root outside H,
inside H but outside the chosen subset, and repeated at a chosen root.
Use the cited exact-root or factorial-moment identities to justify whatever
deduplication or upper bound is needed. Do not assert a subset-incidence
count is the entire list size.

The effective-count subtarget is also screened. Apply the imported
monomial character estimate to the degree-at-most-three phases only after
checking its hypotheses, deleting zero and checking every sieve cycle.
Retain the unordered factorial divisor and all cofactor summations.
The source residue-character estimate is available if cancellation in
the cofactor sum is used; match its nontriviality and field-unit hypotheses
before importing it. Full-field root-domain estimates remain unavailable
on H. No new character estimate is approved merely by this scope record.

One mathematical application may first establish the dictionary, then a
subsequent one may perform the preapproved effective comparison without
another literature turn. Test exact finite inequalities against
65537^28/2^128. A uniform bound below threshold stops this family as an
unsafe witness; an attained list strictly above it excludes the tested
grid radius. A missed upper or lower certificate is inconclusive and must
be preserved as such. Reassess after two unproductive mathematical turns;
do not relabel the same estimate to renew the budget. Arbitrary received
arrays, sharper boundaries and the general interpolant cover remain
independent unresolved steps.

This work is justified as a prescribed-domain and interleaved
specialization of known scalar results. A successful application of the
approved tools should be classified REPRODUCTION. No extension beyond
the checked literature, exact fiber value or new local theorem is claimed.

## Search and access record

The changed-scope queries were:

- `"Reed Solomon" "prescribed leading coefficients" "linear factors" degree`
- `"Reed Solomon" "k+3" "k+2" list decoding polynomials`
- `"Reed Solomon" "multiplicative subgroup" "three" "coefficients"`
- `"Reed-Solomon" "three leading coefficients"`
- `"distance distribution" "multiplicative subgroup" polynomials Gao`
- `"partial agreement" "Reed-Solomon" polynomial leading coefficients`
- `Reed Solomon degree k+3 partial split roots multiplicative subgroup distance distribution`
- `"Distance distribution to received words" "Li" "Wan"`

Search hits were discovery leads; the statements above were read in
primary texts. The Gao-Li follow-up and its original Li-Wan reference
resolve the missing partial-agreement source scope. Other factorization
pattern hits were not read and are not inputs. The newer second-moment
publisher lead and the ABF26 comparison remain unread and parked as
recorded in the earlier assessments; neither is essential to this bounded
application. No access retry on either was made. The same-day prize/model
freeze is reused, with its existing source qualifications preserved.

## Completed review

Outcome: EXPLORATION; STEP_KIND: LITERATURE; classification:
NOVELTY_UNCHECKED. The unchanged target now has SPECIALIZE-ready coverage,
including two exact preapproved mathematical subtargets. This is new
source-scope information and an actionable test, not a mathematical
advance or a solved threshold comparison. No local cofactor constraints,
moment bound, attained list or numerical certificate was derived.
Exploration turns used remain 0/3; literature spends no calculation turn.
STATUS remains IN_PROGRESS, with no complete candidate. Lemmas,
mathematical scripts, the overview and the ID-only DAG are unchanged.

## Mathlib

Full linear-cofactor/partial-agreement/ambient-threshold target:
**not checked**. Formal coverage of the named coefficient-class,
residue-character, moment-count and weighted-sieve results: **not checked**.
Supporting Newton identities and polynomial/root/finite-field facts:
**not checked**. The direct primary links above give supporting scalar
results, not a full matching library theorem. The pinned ArkLib model
definitions remain **present** as recorded in foundations/; they fix the
code and metric but do not establish this changed target.
