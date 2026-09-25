# Contracting inverse-branch test, 2026-09-25

## Gap, intermediate target, and test

Universal eventual descent remains open. The narrower intermediate target
is to extend forced backward decoding from the growing complete blocks
(2,1),(3,1) to the alphabet (1,1),(2,1),(3,1). The first new type contracts
at every allowed start greater than 1. A decoder that survives this addition
could constrain histories containing growth and contraction together.
It would still leave the quantitative balance along forward trajectories,
escape from this alphabet, and the other block types unresolved.

Continue this intermediate mechanism if exact congruences prove that at most
one immediate predecessor can itself have an allowed predecessor. Abandon
that uniqueness claim if two branches extend at any positive odd endpoint.
Retain the fixed point 1 explicitly: a universal finite-depth exclusion
would be false. Even successful uniqueness must be compared with the actual
requirement of eventual descent or escape for each starting integer above 1;
bounded multiplicity alone is not such an estimate.

The shared rules, local goal and checkpoint, full overview, DAG, existing
diff, L002/L007 and the endpoint-count failure were inspected. A search of
the existing lemmas, attempts, drafts and histories found the proposed
addition in the last checkpoint but no completed test. This does not reopen
the stopped finite-window, valuation-potential or density-only inferences.
All earlier work and identifiers are retained. The primary
[statement](https://mathprize.net/posts/collatz-conjecture/) was rechecked
on 2026-09-25 and agrees with the recorded universal positive-integer target.

## Saved reasoning before proof and verification

For a block of type (a,1), L002 gives the formal inverse

    G_a(m) = 2^a (2m+1)/3^a - 1.

For positive odd m, integrality is equivalent to 3^a dividing 2m+1.
When integral, u=(2m+1)/3^a is positive odd, and n=2^a u-1 has
exact odd run a and exact even run 1 because 3^a u-1=2m.
For the three-letter alphabet the proposed existence classes are
m=1 modulo 3, m=4 modulo 9, m=13 modulo 27. Their union is the first
class. Thus extendibility requires G_a(m)=1 modulo 3, leading to

    a=1: m=1 modulo 9;
    a=2: m=22 modulo 27;
    a=3: m=13 modulo 81.

The first class is 1 modulo 9, the others 4 modulo 9; the latter two
are distinct modulo 27. They appear pairwise disjoint. Another explanation
is that, for s=v_3(2m+1), every integral branch with a<s has predecessor
-1 modulo 3 and cannot extend. The only possible extendible branch is
a=s, when s is allowed and its unit part meets the remaining congruence.

Induction should then give at most three depth-K histories at any endpoint,
all agreeing after their earliest state. Unlike the old alphabet, inverse
size does not always decrease: G_1(m)-m=(m-1)/3. Also G_1(1)=1, with
no other allowed predecessor at 1; every finite history ending there is
constant. These are explicit limits of the new rigidity, not convergence
claims. The proof and exact forward-iteration check must retain positivity,
parity, maximality, both directions of each congruence and the small cases.

## Completed assessment

[L009](../lemmas/L009-contracting-block-inverse-rigidity.md) proves all
three exact extendibility classes and their disjointness. The valuation
description handles s=0 and s>3 as well as the permitted cases. The
history bound is three, with a sharp depth-two example, and every history
ending at 1 is constant. The contracting block therefore preserves the
decoder but invalidates the old uniform inverse size decrease, even for
an extendible branch away from 1. L002 is the only prior mathematical
input; L007 is a comparison with the earlier alphabet. Mathlib coverage
is not checked.

The achieved threshold is the proposed uniqueness of an extendible branch.
The required forward escape or eventual-descent estimate is still absent;
bounded histories per endpoint cannot replace it. This is an ADVANCE for
an intermediate arithmetic constraint, not a complete candidate. No
numerical or density inference is used to claim infinite-depth escape.
Consecutive exploration turns without an advance or informative negative
remain zero after this single extension test.

The [exact check](../scripts/contracting-inverse/check_branches.py) passed
all 81 odd endpoints in a complete period modulo 162, independently
enumerating forward blocks for 143 odd starts to include all needed
predecessors. It also checked two representatives for each of 3,279 words
through length seven and all 42,648 backward history levels. The
[output](../scripts/contracting-inverse/result.json) records the fixed
point, sharp bound, and extendible inverse-growth example. These are
finite arithmetic checks supporting the proof, not convergence evidence.

The common even-run length is essential in the derivation of the valuation
decoder. Testing that limitation is the reason for the next direction;
the single concrete continuation is recorded in PROGRESS.md.
