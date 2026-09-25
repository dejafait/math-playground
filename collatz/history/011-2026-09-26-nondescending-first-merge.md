# 2026-09-26 — Non-descent forces a special first-merge pattern

Step `collatz-2026-09-26-011-nondescending-first-merge` concluded ADVANCE.
The [saved test](../drafts/2026-09-26-nondescending-suffix-test.md) records
the gap, intermediate target, decision threshold, and finite results.
Existing uncommitted L010 work and overview changes were preserved;
only the active notebook was edited. The primary
[statement](https://mathprize.net/posts/collatz-conjecture/) was rechecked
on this date and still agrees with the recorded universal target.

[L011](../lemmas/L011-nondescending-first-merge-reduction.md) proves that
four-type histories staying above their own starts have common suffixes
through depth three. At any deeper first merge, the two incoming
odd-run lengths must be adjacent, with maximum 2 or 3. The resulting
pair z=4y+1 is one block apart in depth, and one history must undergo
two consecutive (1,2) contractions. This is the new mathematical input;
it does not bound the compensating earlier growth.

The [screen](../scripts/nondescending-suffix/check_histories.py) considered
all 5,460 word classes through depth six, solving endpoint congruences
and non-descent inequalities without an endpoint-height cutoff. No
distinct-suffix pair survived. The [output](../scripts/nondescending-suffix/result.json)
records 695 nonempty classes and 240 compatible pairs across the tested
depths. Direct shortcut iteration checked 2,780 class realizations,
480 pair realizations, ten forced-tail lifts, and a comparison pair
ending at 103. A separate scan of 50,001 odd starts agreed on 62,299
allowed prefixes. These checks do not extend the theorem to all depths.

The route remains open because the stricter non-descent condition
survived the prescribed test and now has a concrete arithmetic
restriction. The unresolved step is whether both earlier prefixes can
compensate the forced contractions while maintaining non-descent.
Even all-depth rigidity would still leave the fixed-start depth bound
and other block types unresolved. This is one completed focused step,
with zero consecutive exploration turns without a mathematical advance
or informative negative result. No complete candidate appeared.

Mathematical review checked deterministic first merging, truncation of
non-descending histories, the endpoint classes, the branch-length cases,
and the offset between z and y. L002 and L010 are the genuine direct
inputs; L009 is a comparison only. Mathlib coverage is not checked.

Validation: `python3 scripts/nondescending-suffix/check_histories.py`
passed. `python3 ../scripts/docs/check_structure.py --problem collatz`
passed with 11 nodes, 10 edges, complete file coverage, valid links, and
compact overviews. `git diff --check -- .` passed. Structural validation
checks documentation consistency, not mathematical correctness.
