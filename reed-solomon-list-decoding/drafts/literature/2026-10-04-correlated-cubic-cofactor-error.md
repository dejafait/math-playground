# Correlated cubic/cofactor error: completed bounded assessment

TARGET: Test whether averaged correlations between the cubic subgroup cycle sums and the complete residual-factor sum give a uniform degree-67/66-agreement list bound below 65537^28/2^128 on the fixed order-1024 subgroup.
CHECKED: 2026-10-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched subgroup distance-distribution errors, averaged polynomial subset sums, higher moments, Parseval and double character sums; inspected the primary passages below and reused adequate prior coefficient/cofactor coverage.
SOURCE_EVIDENCE: Li-Wan arXiv:1507.06329v1 Theorem 2.1, Corollary 2.2 and Lemma 3.1; Lai-Marino-Robinson-Wan arXiv:1910.05894v2 Proposition 1 and Section 3 large-k sieve; Gao-Li arXiv:2205.02277v1 Theorem 5 and Section 3 Proposition 2; Tao 245C Notes 2 (2009-04-06), Exercises 14 and 16, Lemma 17 and Corollary 22; Chang-Shparlinski author-hosted 2014 manuscript Theorem 4 and Section 3.4.
COMPARISON: Exact signed cycle identities and finite-group Parseval support a correlation test; the inspected effective distance-distribution bounds require full-field roots, factorial moments average random codewords, and subgroup double-sum estimates concern multiplicative characters with asymptotic constants. None supplies the required uniform cubic/cofactor certificate on H.
GAP: Obtain an effective cofactor-weighted moment bound for the signed subset sum, with the trivial Fourier term removed, strong enough for a worst-center upper comparison; no such estimate or list bound is established here.
REASON: Adequate bounded comparison found supporting identities but no full matching theorem; approve one explicit energy test without claiming novelty or assuming cancellation. This differs from L016's stopped constant-weight absolute sum.
SCOPE: Q=65537, H of order 1024 in E=F_Q, k=64, A=66, degree-67 scalar centers over E, other rows zero, ambient F=F_{Q^28}, every m>=1. Covers a bounded application of character orthogonality, Parseval, Cauchy–Schwarz and the signed weighted sieve; excludes an assumed new character-sum theorem, full-field substitution, broader centers and ABF26 recovery.
COVERED_TARGET: Test a Parseval/Cauchy–Schwarz upper certificate retaining the cofactor-weighted second moment of the signed cubic sieve for degree-67 centers at 66 agreements on the fixed order-1024 subgroup, against 65537^28/2^128.
LITERATURE_REASON: The saved target changes the intermediate input from separate pointwise caps to correlated Fourier/sieve error; prior ready coverage explicitly excluded a new character estimate.

## Gap, relevance and prior failures

The degree-67 family's maximum at 66 agreements remains unknown. A
uniform bound at most the ambient threshold would eliminate this family
as an unsafe witness; it would leave arbitrary received centers and the
sharp boundary unresolved. An attained list strictly above threshold
would exclude that grid radius. No such result is claimed in this turn.

Reuse [L015](../../lemmas/L015-degree-sixty-seven-linear-cofactor-dictionary.md)
for the exact incidence-minus-extra-root dictionary and extension-field
and interleaving checks. Reuse
[L016](../../lemmas/L016-cubic-cofactor-sieve-cap-and-limitation.md)
for the stopped estimate: its upper cap exceeds 320297 times threshold,
while its constant-cap absolute allowance exceeds 35496 times threshold.
Neither number measures the true list or signed error. The older support
cap also misses threshold. The averaging lower certificate is only about
0.111 times threshold. These saved comparisons are not recalculated.

The proposed intermediate target is an effective second-moment bound
that keeps the subset sum and residual factor coupled. Its plausible use
is a uniform Fourier-error certificate. Merely knowing the cofactor norm,
replacing the subset sum by the same constant cap, or computing an average
list does not meet that target. No new identity is derived in this review.

## Primary statements read and applicability

**Signed sieve.** Li and Wan,
[Counting polynomial subset sums, v1](https://arxiv.org/pdf/1507.06329v1),
2015-07-22, Theorem 2.1 and Corollary 2.2, printed p. 5; Lemma 3.1,
p. 8. The weighted identity applies to complex functions on arbitrary
finite domains. The lemma keeps a signed character sum over cycle types
before subsequent estimates. It supplies an exact starting point, not an
averaged cubic/cofactor bound. Import the sieve; the changed vector moment
and residual-factor weighting need local verification. Theorem 1.4,
p. 4, instead assumes a near-full-field domain, so it is not a shortcut
for this sparse subgroup. The author's UCI PDF endpoint failed; the
versioned arXiv PDF was readable and resolves this supporting source.

**Moment terminology.** Lai, Marino, Robinson and Wan,
[Moment subset sums over finite fields, v2](https://arxiv.org/html/1910.05894v2),
2019-10-19, Proposition 1 and Section 3, subsection “k-MSS(m) for large k”,
through its cycle factorization. Their moments are prescribed power sums
of subset elements, not statistical moments of Fourier errors. Their
monomial-domain estimate and signed cycle representation support the
existing framework. The subsequent error estimate uses individual cycle
caps; it does not assert the required correlation with a complete residual
sum. Reuse its adequate prior scope rather than reprove it. The complete
field Weil bound in Theorem 4 is also readable, but a smaller cofactor
pointwise constant alone would still be the stopped mechanism.

**Distance moments versus a worst center.** Gao and Li,
[Improved error bounds for the distance distribution of Reed-Solomon codes, v1](https://arxiv.org/html/2205.02277v1),
2022-05-04, Theorem 5, equation (14), and Section 3, Proposition 2,
equations (20)-(23), printed pp. 5-7. Theorem 5 averages the agreement
count of a random codeword at a fixed center. Above the message dimension,
its factorial moments contain the unresolved incidence counts. It does
not supply the second moment over centers sought here. Section 3 sets
D=F_q; its error proof separately bounds cofactor and root sums. It
therefore provides neither proper-H coverage nor the proposed correlated
certificate. The arbitrary-domain dictionary remains useful by citation.

**Finite-group energy identities.** Terence Tao,
[245C Notes 2: The Fourier transform](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/),
2009-04-06, Section 1 Exercises 14 and 16 and Section 2 Lemma 17,
Theorem 21 and Corollary 22. These state convolution/product compatibility,
character orthogonality, Parseval and its inner-product form, explicitly
including finite abelian groups. They apply on the additive group E^3
with normalized counting measure. Import these standard facts, checking
the conversion to L016's unnormalized sums and all Q factors locally.
They allow an energy test, but do not estimate the relevant subset
collision count or yield a finite-code threshold theorem. A new effective
estimate remains a research question, not an imported conclusion.

**Adjacent correlation theorem, different characters.** Chang and
Shparlinski,
[Double Character Sums over Subgroups and Intervals, author manuscript](https://math.ucr.edu/~mcc/paper/151%20CharSums-InterGroup.pdf),
2014, Theorem 4, printed p. 4, and Section 3.4, p. 13. The result bounds a
double multiplicative-character sum of an affine sum of subgroup elements;
its proof uses subgroup additive energy. It illustrates preservation of
averaged information, but is not an additive cubic moment/cofactor theorem
and has asymptotic terms unsuitable for this exact certificate without
further work. No application is approved. The arXiv PDF endpoint returned
inconsistent authorship/date/numbering on successive reads; use the
inspected author copy, whose title, authors and numbering were checked.
This access anomaly is resolved for the comparison, not a research input.

## Search record and unresolved leads

Queries used:

- `Reed Solomon distance distribution multiplicative subgroup second moment character sums prescribed coefficients`
- `polynomial subset sums multiplicative subgroup averaged character sums Li Wan cofactor`
- `"subset sums" "higher moments" "multiplicative subgroups" character`
- `"polynomial" "subset sums" "variance" character`
- `"character sums" "subgroups" "correlation" cubic additive energy`
- `"Double character sums over subgroups and intervals" Chang Shparlinski`
- `"subset sums" "Parseval" finite fields`
- `"moment subset sums" "correlation"`
- `site.terrytao.wordpress.com finite abelian Fourier Parseval convolution Cauchy Schwarz`

Search snippets are discovery evidence only. The 2026 second-moment
publisher lead resurfaced but remains parked and is not an input; its
terminology alone does not supply a cubic correlation theorem. ABF26
access and unrelated sum-distinct-set hits were not pursued. No essential
unread source is being used in the approved standard energy test. This
bounded search does not establish originality or exhaust the literature.

## Authorized bounded test and decision threshold

Approve one mathematical turn under the exact COVERED_TARGET above.
Start with L016's Fourier representation, keeping the signed sieve until
an explicitly stated Cauchy–Schwarz step. Separate trivial and linear
phases correctly. Seek a cofactor-weighted second moment by Parseval or
orthogonality, interpreting its collision constraints before bounding it.
Do not assume independent moment coordinates, random phase signs, or
uniform center fibers. Any reduced-instance computation audits an identity
only; it is not evidence of the uniform bound at Q=65537.

Continue this mechanism only if the test supplies a uniform certificate
at most 65537^28/2^128, or an effective improvement and a precise remaining
estimate that could plausibly cross it. If the bound merely recovers the
stopped constant-cap allowance, or leaves an equally hard unestimated
66-subset collision count, record that limitation and reassess rather
than repeatedly changing the norm. Preserve the nonnegative subtractive
term in the exact dictionary; it may be dropped for an upper test, but
no helpful lower bound on it is assumed. Remaining full-code gaps persist.

This review is EXPLORATION, LITERATURE, NOVELTY_UNCHECKED. It supplies new
source-scope comparisons and a screened bounded test, not a mathematical
advance. A subsequent application of standard energy tools can be reported
as REPRODUCTION; POTENTIALLY_NEW requires an actual unmatched effective
estimate and still does not certify originality. Exploration turns used
remain 0/3 because literature spends no calculation turn. STATUS remains
IN_PROGRESS. Lemmas, scripts, PROOF.md and DAG.md are unchanged.

## Mathlib

Full correlated cubic/proper-subgroup/cofactor threshold result: **not
checked**. Formal coverage of the cited sieve and character estimates:
**not checked**. Parseval, convolution, Cauchy–Schwarz and finite character
orthogonality: **not checked** in Mathlib; the direct primary references
above supply standard supporting results, not a full matching theorem.
Pinned ArkLib definitions remain **present** as recorded in foundations/;
they define the model, not the proposed energy estimate.
