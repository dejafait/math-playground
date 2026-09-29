# 2026-09-27 — Higher-genus Prym determinant transfer exclusion

STEP_ID: 2026-09-27-hodge-058-higher-genus-prym-lefschetz-exclusion.
Outcome: NEGATIVE. Kind: RESEARCH. Classification: REPRODUCTION.

Read the shared goal and prompt, local goal and checkpoint, whole
proof overview and ID-only DAG; inspected existing changes and
preserved unfinished work. The exact saved Next action had a
ready SPECIALIZE assessment, reused without changing its target
or decision. No new target was investigated in this invocation.

The main local gap is algebraic beta_U beyond the Dickson family,
with algebraic kappa separate. The intermediate target was its
image under divisor-generated transfers of higher-genus Prym
determinants, allowing degree-lowering. Such a transfer could
have supplied one input to the conditional Kuga--Satake route.
The discriminating test was containment in the divisor algebra
already excluded for beta_U, rather than a total-dimension bound.

[L034](../lemmas/L034-prym-determinant-lefschetz-transfers-miss-cubic-tensor.md)
proves that every allowed image lies in D^2(A^4). It computes
the full target centralizer as GL(64)^4 and treats the projection
of the joint group, including common isogeny factors. Source
determinant lines are characters; their images are fixed by the
target derived group. Degree-four weights have magnitude at
most four, against the divisibility-by-64 requirement, forcing
full invariance. The proof retains special Pryms, mixed divisors,
all multiplicities, rational descent, lowering and rational sums.

The achieved image is zero in H^4(A^4,Q)/D^2(A^4), whereas the
whole beta_U has nonzero image. This supplies new route evidence
beyond the old genus-three homomorphism exclusion. The underlying
Prym, centralizer and operator results are imported by citation;
the image comparison is a reproduction/application of known
representation theory, not a claimed original discovery.

Reconsulted the assessed Milne source for precise isogeny-factor
and operator statements, including Proposition 1.5 and the
author's lowering erratum. The prior Prym and spin inputs were
reused; no essential unread source remains. The
[working notes](../drafts/2026-09-27-higher-genus-prym-lefschetz-test.md)
were saved before completing the proof and now record the checks.
An exact integer check of 4096 standard/dual words found 225
central weights; all 168 words trivial on the central 64th roots
have zero scalar weight. This only checks bookkeeping.

Stop this channel, as recorded in the
[attempt](../ATTEMPTS/024-higher-genus-prym-determinant-lefschetz-transfer.md).
The new target screens nonabelian Prym constructions for source
classes with nontrivial derived-group action, preserving L032's
small-factor and L034's determinant exclusions. Its
[assessment](../drafts/literature/2026-09-27-nonabelian-prym-degree-four-transfer.md)
is REVIEW_REQUIRED: no discovery or calculation on it was done.
The next invocation is literature-only. Exploration count is
zero after this informative negative result.

No new cycle or transverse RM surface was obtained. The attained
span remains 21 and three RM directions against four required.
Algebraic kappa, arbitrary correspondences, primitive fourfold
classes and higher-dimensional cases remain unresolved. STATUS
stays IN_PROGRESS; no complete candidate appears. Mathlib coverage
is not checked. The overview records the scoped route stop; the
only new DAG inputs are L031 and L032 for L034.

Validation: python3 ../scripts/docs/check_structure.py --problem hodge
passed with 35 nodes and 83 edges, valid links and compact overviews.
Metadata checks confirmed all required fields, the prior SPECIALIZE
assessment, RESEARCH/REPRODUCTION classification and exact matching
of the new target to its REVIEW_REQUIRED assessment. Whitespace
checks passed. SHA-256 comparison confirmed preservation of all
53 existing lemma/script files and every existing file except the
three intended checkpoint/overview/DAG updates; five artifacts
were added and none deleted. The checker validates documentation,
not mathematical correctness or the main Hodge conjecture.
