# Variable even-run inverse test, 2026-09-25

## Gap, intermediate target, and test

Universal eventual descent is still missing. The proposed intermediate
target is to preserve the unique extendible inverse branch after adjoining
(1,2) to the complete-block alphabet {(1,1),(2,1),(3,1)}. This tests whether
the arithmetic decoder can constrain histories with variable even-run
lengths. Successful decoding would still leave forward escape from this
alphabet, quantitative growth versus contraction, and other block types
unresolved.

Continue the unique-decoder mechanism only if at most one immediate
predecessor can itself have an allowed predecessor. Abandon its direct
extension if two distinct branches both extend on a positive residue
class. Compare any achieved multiplicity statement with the actual
requirement of eventual descent for each starting integer: uniqueness
alone was already insufficient in L009.

The shared instructions, local goal and checkpoint, whole overview, DAG,
local git status, L002/L009, recent history, and the stopped endpoint-density
inference were inspected. No existing proof treats this enlarged alphabet;
the previous checkpoint explicitly proposed the test. Existing local work
was clean, and changes in other notebooks are left untouched. The primary
[statement](https://mathprize.net/posts/collatz-conjecture/) was rechecked
on 2026-09-25; it retains the universal positive-integer target recorded in
foundations. No historical route stop is treated as a global research ban.

## Saved reasoning before proof and verification

For a block (a,b), L002 gives the inverse

    G_(a,b)(m) = 2^a (2^b m+1)/3^a - 1.

For positive odd m it exists exactly when 3^a divides 2^b m+1;
the quotient is positive odd, so the inverse has the exact maximal run
lengths. The new branch is (8m-1)/3, with m=2 modulo 3. Thus the union
of all endpoint classes becomes m nonzero modulo 3, and an existing
predecessor extends exactly when it is nonzero modulo 3.

The preliminary extendibility classes are

    (1,1): m=1 or 4 modulo 9;
    (2,1): m=13 or 22 modulo 27;
    (3,1): m=13 or 40 modulo 81;
    (1,2): m=2 or 5 modulo 9.

The three even-run-1 extendibility sets appear nested, rather than
disjoint. In particular m=13 modulo 81 should admit three extendible
branches. At m=13, the putative two-block histories are (45,17,13),
(29,11,13), and (9,7,13). These are finite incoming histories, not cycles.
The exact congruences, positivity, parity, and all maximal run lengths
need independent forward checks and a full proof. No conclusion about
infinite branching or escape is inferred from this finite calculation.

## Completed assessment

[L010](../lemmas/L010-variable-even-run-inverse-branching.md) proves the
four exact existence and extendibility classes. The three even-run-1
extendibility sets are nested, and three branches extend on each of two
classes modulo 81. The displayed family gives distinct penultimate states
at unbounded positive endpoints. The lemma also proves a sharp upper bound
of five depth-two histories, attained at endpoint 661, so the earlier
bound of three at every depth fails as well. The fixed point 1 remains
isolated among incoming histories. L002 is the only earlier mathematical
input; L009 supplies the comparison, not an assumption about the enlarged
alphabet. Mathlib coverage is not checked.

The continuation threshold of unique extendibility fails. This step is
NEGATIVE because it rules out directly extending the decoder to variable
even-run lengths. It does not refute Collatz, establish unbounded history
multiplicity, or supply the forward escape bound required for starts above
1. The new bound five concerns only depth two; it is not substituted for
the missing all-depth starting-height estimate. No complete candidate
appeared. This one bounded test ends with zero consecutive exploration
turns without an advance or informative negative result.

The [check](../scripts/variable-even-inverse/check_branches.py) passed
all 729 odd endpoints in a full period modulo 1458 for two-block inverse
existence, using independent forward iteration of 5,180 odd starts up to
10,359. It verified the congruences, the sharp count, the fixed point,
and five lifts of the explicit positive family. The
[output](../scripts/variable-even-inverse/result.json) records the exact
counts. The proof separately checks every domain restriction, the
recomputed endpoint union, both directions of extendibility, and the
valuation cases for the upper bound.

The unrestricted histories used in this test need not stay above their
starting values. Requiring that non-descent condition is a more direct
connection to the main gap and has not been tested for the enlarged
alphabet. This motivates the single bounded continuation recorded in
PROGRESS.md. The density-only and per-block potential routes remain
stopped for their documented reasons.
