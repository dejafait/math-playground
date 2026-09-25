# Non-descending suffix test, 2026-09-26

## Gap, intermediate target, and discriminating test

Universal eventual descent remains the exact missing claim. The proposed
intermediate target is common-suffix rigidity for depth-K histories in
the four-type alphabet {(1,1),(2,1),(3,1),(1,2)} after imposing n_0>1
and n_j>=n_0 for every j. These inequalities are necessary for a history
that has not yet descended. By L002 they also control every intermediate
shortcut state, not just block endpoints.

If this restriction restores rigidity, it could support a count or
starting-height estimate for exceptional histories. Rigidity alone still
would not give the required finite non-descent depth at each fixed start;
that quantitative passage and treatment of all other block types remain
unresolved. Test every word class through six blocks with exact arithmetic.
A pair of compatible word classes with different suffixes and infinitely
many positive non-descending realizations would stop this repair. Absence
of such a pair in this finite test would justify only a further argument,
not an all-depth theorem.

The shared instructions, local goal/checkpoint, complete overview and DAG,
existing local diffs, L002/L009/L010, the previous saved test and history,
and the recorded failures were inspected. The existing uncommitted L010
artifacts and overview updates are retained. L010's unrestricted examples
do not settle this stricter question. The density-only and per-block
potential obstructions remain applicable; none is a global research ban.
The primary [statement](https://mathprize.net/posts/collatz-conjecture/)
was rechecked on 2026-09-26 and still has the universal positive-integer
target recorded in foundations.

## Saved reasoning before calculation

For a positive odd endpoint m, L010 supplies the exact inverse
G_(a,b)(m)=(2^(a+b)m-(3^a-2^a))/3^a, including maximal run lengths.
For a fixed word, compose these inverses as
n_j=(p_j m-c_j)/q_j, with p_j a power of 2 and q_j a power of 3.
Starting from (p_K,c_K,q_K)=(1,0,1), a preceding block (a,b) changes
the triple to (2^(a+b)p, 2^(a+b)c+(3^a-2^a)q, 3^a q).
The full inverse's integrality should force all intermediate integrality
by reduction modulo the smaller powers of 3. Retain oddness by using
one endpoint residue class modulo 2q_0.

Each condition n_j>=n_0 becomes one integer linear inequality in m;
n_0>1 is n_0>=3 because starts are odd. Their intersection with the
endpoint class can therefore be computed without an endpoint cutoff.
Two words can meet only when their classes agree modulo the smaller
modulus. A compatible pair with unequal suffix words and an unbounded
common feasible interval would give the desired infinite family of
failures. Integrality sufficiency, all inequalities, exact runs, and an
explicit family require proof and independent forward checks before
drawing the continuation decision. No complete candidate is present.

## Completed test and assessment

The [exact-arithmetic screen](../scripts/nondescending-suffix/check_histories.py)
enumerated all 5,460 words of lengths one through six. For each word it
computed the endpoint class modulo 2q_0 and solved every inequality

    (p_j q_0 - p_0 q_j)m >= c_j q_0 - c_0 q_j,

together with p_0 m>=c_0+3q_0 and m>=1. Upper bounds, empty intervals,
and the strict initial cutoff n_0>1 were retained. Since all endpoint
moduli are twice a power of 3, pairwise class compatibility is an exact
divisibility test. On compatible feasible classes, suffix word equality
is equivalent to suffix state equality: inverses are unique for each
type, and the forward maximal-block map determines each type from its
starting state. The computation therefore did not restrict the endpoint
to a numerical height range.

The [output](../scripts/nondescending-suffix/result.json) reports:

| Depth | All words | Nonempty non-descending classes | Compatible pairs | Pairs with different suffixes |
| --- | ---: | ---: | ---: | ---: |
| 1 | 4 | 2 | 1 | 0 |
| 2 | 16 | 5 | 2 | 0 |
| 3 | 64 | 14 | 5 | 0 |
| 4 | 256 | 45 | 16 | 0 |
| 5 | 1024 | 141 | 49 | 0 |
| 6 | 4096 | 488 | 167 | 0 |

All admitted classes in this test have no upper endpoint bound. There
was no failure requiring a positive counterexample family. Independent
shortcut iteration checked 2,780 class realizations and 480 compatible
pair realizations, including large parameter lifts. A separate forward
scan of all 50,001 odd starts up to 100,001 agreed on 62,299 allowed
prefixes, including rejected non-descent cases. This finite scan is a
diagnostic for the class calculation, not its search domain. No positive
boundary point outside an admitted class interval arose in this test.

The mathematical investigation also isolated a restriction on failures
at arbitrary depth, proved in
[L011](../lemmas/L011-nondescending-first-merge-reduction.md).
At a first merge m with 2m+1=3^s w, branches with a<=s-2 die after two
backward steps because the second predecessor is divisible by 3. Two
long enough incoming histories must therefore use s in {2,3} and the
adjacent branches s-1 and s. Their states obey z=4y+1 at indices one
block apart. Requiring both prefixes to exist forces y=1 modulo 3 and
two consecutive (1,2) blocks on the larger side. Those contractions
rule out a non-descending first merge at depth three; depth two is
excluded separately. The full proof and its limitations are in L011.
Ten exact tail-family lifts and an explicit pair ending at 103 were
checked by direct shortcut iteration.

This step is ADVANCE for the proved first-merge restriction and
three-block rigidity, not for extrapolation of the six-block screen.
The test supports continuing the restricted suffix question. Its
actual remaining threshold is rigidity at every depth; even that
would still need a quantitative starting-height or escape argument to
address the main target. Earlier growth might compensate the forced
contractions, so no fixed-window or universal descent conclusion is
drawn. No complete candidate appeared. Zero consecutive exploration
turns without ADVANCE/NEGATIVE have been used after this mathematical
input. The reason for the next direction is the new concrete pair
relation and its depth offset, rather than a further numerical height
search. The single next action is recorded in PROGRESS.md.

## Mathlib

Full first-merge statement and supporting library results: **not checked**.
L011 contains the elementary proof using L002 and L010. No Mathlib
theorem names or direct links were checked, and no absence is asserted.
