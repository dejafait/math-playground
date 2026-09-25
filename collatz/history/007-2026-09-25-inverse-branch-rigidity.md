# 2026-09-25 — Forced backward decoding of mixed blocks

Step `collatz-2026-09-25-007-inverse-branch-rigidity` concluded ADVANCE
for an intermediate arithmetic constraint. The
[saved test](../drafts/2026-09-25-inverse-branch-rigidity.md) records
the gap, relevance, and continuation threshold. The primary
[source](https://mathprize.net/posts/collatz-conjecture/) was rechecked
and retains the universal positive-integer target. Existing changes and
inactive branches were preserved; edits were confined to this notebook.

[L007](../lemmas/L007-inverse-branch-rigidity.md) proves that the two
inverse branches cannot both have an earlier allowed predecessor. Its
exact powers-of-3 congruences force every block except the earliest when
decoding a finite history backward. At each endpoint there are at most
two histories of any fixed depth. This is different information from
the stopped powers-of-2 potential route and the fixed-word repetition
bound; it supplies a restriction on collisions between mixed histories.

The main gap remains open. The required least-start bound must tend to
infinity uniformly with word length, whereas the achieved bound controls
only the number of histories per endpoint. Its size estimate bounds
backward depth for a fixed endpoint, with no bound on the future endpoint
of a fixed start. No complete candidate has appeared. Disjoint inverse
classes motivate a bounded finite-interval counting test; controlling the
boundary error, not density alone, would be necessary to obtain escape.
Consecutive exploration turns without an advance or informative negative
remain zero after this one coherent step.

Validation: `python3 scripts/inverse-branches/check_branches.py` passed
243 odd endpoints in a complete period modulo 486, plus 1,020 endpoints
constructed from all 510 words through length eight and two starting
representatives per word. All 7,172 backward history levels satisfied
the exact congruences, multiplicity, and size bounds. The
[output](../scripts/inverse-branches/result.json) is finite arithmetic
evidence only. Mathematical review checked positivity, oddness, exact
maximal runs, both directions of the congruences, and the history induction.
L002 is the sole earlier mathematical input; L005 is a comparison with
the missing bound, and L006 is historical motivation. Mathlib coverage
is not checked.

Documentation validation: `python3 ../scripts/docs/check_structure.py --problem collatz`
passed with seven nodes, five edges, complete lemma coverage, valid local
links, and compact overviews. The new DAG row records only L002 as a
mathematical input to L007. Structural validation does not establish
proof correctness or completeness of the recorded inputs.
