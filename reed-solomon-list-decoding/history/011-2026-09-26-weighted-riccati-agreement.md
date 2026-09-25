# 2026-09-26 — Weighted Riccati agreement

Read the shared and local goals, prompt, checkpoint, whole overview, DAG,
relevant proofs, prior failure, and existing changes. Preserved the
unfinished L009-related work and all unrelated notebook changes. Rechecked
the [prize statement](https://proximityprize.org/): the list threshold and
field-existence proviso are unchanged. The source comparison with ABF26
remains qualified. The [focused draft](../drafts/2026-09-26-weighted-riccati-agreement.md)
records the intermediate target, continuation test, and saved reasoning.

[L010](../lemmas/L010-weighted-riccati-agreement.md) proves a weighted
agreement bound for polynomial Riccati solution tuples, directly in
the interleaving width. It is useful when the number e of evaluation
zeros of the differential coefficient is controlled. It also bounds
an infinite rate-1/2 smooth-domain subfamily of L009's obstruction by
four candidates at k agreements, despite its superpolynomial unfiltered
solution count. This establishes a relevant conditional input, so the
outcome is ADVANCE and exploration turns are 0/3. STATUS stays IN_PROGRESS;
no complete target candidate or sharp full-code boundary is claimed.

The new bound does not control a general interpolant or the number of
its exceptional columns. Its sufficient family field condition remains
stronger than the prize's mere existence proviso. When every column is
exceptional it gives only the ordinary Johnson cutoff. The shared center
may impose stronger root multiplicities at simple zeros of a; that local
information motivates the subsequent refinement. The stopped unfiltered
polynomial-count route remains stopped, and its counterexample is intact.

`python3 scripts/weighted-riccati/verify.py` passed 321 tuple-pair checks,
20,977 exhaustive center agreement patterns, 45,815 list inequalities,
41,160 ordinary-bound specializations, and ten smooth-domain parameter
instances. It enumerated 7,290 polynomials and included both simultaneous
two-row agreement and a regular root of multiplicity p. The
[results](../scripts/weighted-riccati/results.json) are finite evidence;
the lemma contains the full symbolic proof. Mathlib coverage is not checked.

L010's weighted proof is self-contained; it uses L009 for the unfiltered
subspace construction in the concluding comparison. The DAG records that
actual mathematical input and preserves all existing branches.

The required documentation checker passed with 11 nodes and 8 edges,
using `PYTHONDONTWRITEBYTECODE=1` to keep shared infrastructure read-only.
`git diff --check -- .` passed. The graph input was reviewed against the
proof; structural validation does not establish mathematical correctness.
