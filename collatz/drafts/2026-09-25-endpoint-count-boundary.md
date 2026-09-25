# Endpoint count and boundary test, 2026-09-25

## Gap, intermediate target, and relevance

Universal eventual descent is open. The narrower gap under test is exclusion
of infinite aperiodic itineraries of complete blocks (2,1) and (3,1).
The current step tests the endpoint-count proposal following L007: for
fixed N, bound the number of depth-K endpoints below
X_K=(27/16)^K(N+5) by a quantity eventually less than one. Every allowed
K-block path starting at most N ends below this cutoff. An endpoint
exclusion at every fixed N would imply escape from the restricted alphabet;
other block types and compensation toward universal descent would remain
unresolved.

Continue this particular counting certificate only if the finite-interval
bound, including its residue offsets, reaches the less-than-one threshold.
If only the density term shrinks and a surviving boundary term cannot be
discarded, stop the density-only inference and identify the missing
arithmetic information. A finite test alone will not exclude infinite paths.

The shared instructions, local goal and checkpoint, whole overview and DAG,
existing diff, relevant proofs L002/L005/L007, recent histories, and the
attempt records were inspected or searched before this test. Earlier work
has no finite-interval endpoint count. Fixed-word repetition estimates and
the stopped valuation potentials do not settle this test. All existing
work and identifiers are preserved. The primary
[statement](https://mathprize.net/posts/collatz-conjecture/) was rechecked
on 2026-09-25 and retains the universal positive-integer target already
recorded in foundations/01-target-and-scope.md.

## Saved reasoning before proof and verification

Let E_K be the positive odd endpoints admitting K allowed blocks. L007
gives E_1 as the odd integers equal to 4 modulo 9. If one class of E_K
is r modulo 3^s (restricted to odd integers), appending a block of type
(a,1) should give the class

    m = 2^(-(a+1)) (3^a r + 3^a - 2^a) modulo 3^(s+a).

Here the inverse is modular. L007 should ensure all positive members
have positive exact predecessors, so there are no missing initial terms.
The two appended types are disjoint because their predecessors already
have a predecessor. Induction therefore predicts 2^(K-1) disjoint classes
and density delta_K=(1/18)(1/9+1/27)^(K-1).

Counting each class below X gives its density times X and an error of
absolute value less than one. The resulting bound is

    |#(E_K intersect [1,X]) - delta_K X| < 2^(K-1).

At X_K the density term is 3(N+5)/(8*4^K), whereas the available
boundary bound grows. The old finite path 603,679,1147,1291,1453 has
four allowed blocks. With N=175, its endpoint appears to lie below X_4
even though delta_4 X_4=135/512<1. This would directly refute dropping
the boundary term at the proposed cutoff; it would not refute eventual
vanishing of the true count for each fixed N.

The proof must check exact class coverage, positivity, disjointness,
the count error and all constants. The arithmetic check will compare
small complete residue periods with direct forward maximal-block
iteration, and evaluate the witness using rational arithmetic. No complete
candidate for Collatz or restricted escape is asserted.

## Completed assessment

[L008](../lemmas/L008-endpoint-count-and-boundary.md) proves the exact
recursive classes, their disjointness and positivity, and the predicted
density and finite-interval bound. Its only prior mathematical input is
L007. The old four-block example is checked directly from those block
formulas; L005 is a historical comparison, not an additional premise.
Mathlib coverage is not checked.

The density contribution at the proposed cutoff is indeed
3(N+5)/(8*4^K), but the explicit boundary bound is 2^(K-1), so the
achieved upper count never becomes less than one. The witness at
N=175, K=4 proves that the density contribution cannot serve as the
upper count: an endpoint is present with an error at least 377/512.
The [exact check](../scripts/endpoint-count/result.json) finds exactly
one endpoint there. This refutes dropping the boundary term; it does
not show that the true count fails to vanish for fixed N. The witness
starts above N, also exposing the overcount in this sufficient criterion.

The unrestricted claims have full proofs. Independent forward iteration
over complete periods for depths 1–4 checked 183,960 positive odd starts.
The [script](../scripts/endpoint-count/check_count.py) also checked every
integer cutoff in those periods, 2,046 endpoint representatives through
depth 10, and 174,251 pairs of residue classes. All checks passed using
integer or rational arithmetic. These finite checks do not establish an
infinite-depth bound or convergence.

The outcome is NEGATIVE for the density-only inference, preserved in the
[attempt record](../ATTEMPTS/007-density-only-endpoint-count.md).
Consecutive exploration turns without an advance or informative negative
remain zero. The main gap remains open and no complete candidate has
appeared. Controlling the actual residue offsets is still unproved; the
broader gap also includes contraction and later compensation. This
motivates testing whether the inverse arithmetic survives the addition of
a contracting block, rather than reiterating density estimates. The sole
concrete continuation is recorded in PROGRESS.md.
