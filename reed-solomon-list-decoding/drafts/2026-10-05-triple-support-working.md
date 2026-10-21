# Triple-support specialization — working checkpoint

Approved target: establish and test the selected three-support criterion in
`literature/2026-10-05-triple-support-rank-diagnostic.md`. Research only on
that target; classification REPRODUCTION of the cited difference-kernel
dictionary. Inputs read: L001, C001a, C001b. Existing work is preserved.

Main gap: arbitrary-center safety at 68/67 agreements. Intermediate target:
three size-68 supports, a common core of size 61, and disjoint pair-only
overlaps of size two. Dividing differences by the common-root product should
leave multiples of the three monic overlap quadratics. Test their 3-by-3
coefficient determinant at actual subgroup points. Pairwise disjoint root
pairs imply that any two quadratics are independent; a nonzero kernel
therefore should have three nonzero entries. Check this and construct a
compatible center, allowing extra agreements and every interleaving width.

Discriminating test: three antipodal pairs have vanishing linear
coefficients and may give a genuine rank-two configuration; compare one
rank-three configuration. Save explicit subgroup points, full support sets,
matrices, kernels, message coefficients and evaluations in a certificate.
Do not infer universality from a sample. A valid singular configuration
abandons universal exclusion of this overlap pattern; a determinant
restriction could still enter a later quantitative extremal count.
That count (required saving factor >2.763), 67-agreement safety, exact
maxima and ABF equivalence remain unresolved. No threshold advance is sought
or inferred from a three-message construction.

Completed: canonical criterion, full proof and both subgroup examples are
in L020; the exact diagnostic and full certificate are
`scripts/finite-support/triple_support_rank.py` and
`scripts/finite-support/triple-support-rank-results.json`. Both rank cases
pass; the antipodal messages have 1016,68,68 agreements. Universal
exclusion is refuted, while an explicit forbidden case remains useful.
The quantitative extremal transfer is uncovered and separately marked
REVIEW_REQUIRED; no further mathematics was attempted on it.
