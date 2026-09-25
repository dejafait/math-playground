# Inverse branch compatibility test, 2026-09-25

## Gap, intermediate target, and relevance

Universal eventual descent remains open. The narrower active gap is
exclusion of infinite aperiodic itineraries using only the complete-block
types (2,1) and (3,1). L005 excludes eventual periodicity but supplies no
least-start bound tending to infinity uniformly over all mixed words.

This single step tests whether both inverse branches

    G_2(m) = (8m-5)/9,     G_3(m) = (16m-19)/27

can have a legal earlier predecessor in the same alphabet. If one branch
must stop immediately, this would give forced backward decoding of long
histories and limit collisions of mixed-word endpoint classes. Such a
constraint could support a later height or counting argument. A uniform
bound on the starting integer would still be needed to exclude infinite
forward paths; other block types and universal descent remain separate.

The discriminating test is exact congruence compatibility, with positivity,
oddness, and maximal run lengths retained. Continue the inverse mechanism
if the two branches cannot both extend and an unrestricted decoding or
multiplicity statement follows. Abandon this proposed rigidity if an exact
positive family has two extendible branches. Neither a finite enumeration
nor uniqueness of backward histories by itself establishes forward escape.

The whole overview and DAG, current diff, L002, L005, L006, all six attempt
records, and the two latest histories were inspected. The earlier failures
concern bounded forward descent, fixed-word bounds, and powers-of-2
potentials. This test uses powers-of-3 divisibility and is not a rerun of
those tests. Existing unfinished work and identifiers are preserved. The
primary [source](https://mathprize.net/posts/collatz-conjecture/) was
rechecked on 2026-09-25 and retains the universal positive-integer target.

## Saved reasoning before proof and verification

For an odd endpoint m, integrality requires m=4 modulo 9 for G_2 and
m=13 modulo 27 for G_3. The second class is contained in the first.
When both exist, write m=27t+13. The formal predecessors are

    G_2(m)=24t+11,     G_3(m)=16t+7.

The first is 2 modulo 3, whereas every endpoint of either block type
is 1 modulo 3. It therefore appears that the G_2 branch is terminal
whenever G_3 exists. Direct algebra gives the proposed exact tests

    G_2(m) has an earlier predecessor iff m=76 modulo 81;
    G_3(m) has an earlier predecessor iff m=175 modulo 243.

These classes have residues 22 and 13 modulo 27, so are disjoint.
The tasks within this step are to verify sufficiency with positive odd
integers, prove the resulting bound of at most two histories at any fixed
depth, and determine exactly what this gives toward the required bound.
No infinite-path exclusion or complete candidate is asserted.

## Completed assessment

[L007](../lemmas/L007-inverse-branch-rigidity.md) proves the exact two
congruences for extendibility, with all small positive cases and maximal
run conditions included. At most one immediate predecessor can have an
earlier allowed block. Induction then bounds the number of histories of
any fixed depth ending at a given m by two; they differ only in their
earliest state. Thus every later block can be decoded uniquely backward.

The sought intermediate rigidity holds. The stronger bound required to
exclude all infinite mixed itineraries is still mu_K tending to infinity,
uniformly over length-K words. The achieved multiplicity bound is two
per endpoint, while its size consequence n_0<(8/9)^K m is an upper bound
in terms of the freely varying endpoint. It supplies no divergent lower
bound on n_0. A finite past at each growing endpoint does not imply a
finite future at one fixed starting integer.

The [exact check](../scripts/inverse-branches/check_branches.py) passed
all 243 positive odd representatives modulo 486 against independent
forward maximal-block iteration. It also checked 510 words through length
eight with two starting representatives each, giving 1,020 constructed
endpoints and 7,172 backward history levels. The
[output](../scripts/inverse-branches/result.json) records the finite
scope. These checks support the elementary proof, not forward convergence.
Mathlib coverage is not checked.

This is ADVANCE for a useful intermediate constraint, not a resolution
of the restricted or full target. Consecutive exploration turns without
an advance or informative negative remain zero. The inverse mechanism
merits a further bounded test because its surviving classes are disjoint;
an endpoint count might combine that separation with forward size growth.
The unresolved issue is whether the residue-class boundary error can be
controlled, rather than merely computing a small limiting density. No
complete candidate has appeared.
