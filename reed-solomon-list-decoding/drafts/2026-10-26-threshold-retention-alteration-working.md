# Threshold-retention alteration — work in progress

The approved target is the exact retention-to-ambient-overlap implication
in the saved 2026-10-26 assessment. Essential inputs are L030's arbitrary
bijection construction and L125's distinguished-point counts. No other
notebook is used. Existing unfinished drafts are preserved.

Fix the left labeling with b at (16,0), and delete its q^2 blocks through
b. Condition the right labeling on a specified dummy mapping to a.
Every remaining left residual and every right residual is a seven-subset
of Y, of size 962. Right blocks have uniform images among those subsets.
Cross intersections of the 68-supports are 60 plus residual intersection;
thus forbidden pairs have residual intersection at least four. The full
right ambient star at a is empty, so ambient-star overlap is identically
zero. Equal cross supports are impossible because their a,b incidences
differ. Local packing restrictions are inherited from L030.

The exact calculation multiplies (q^3-q^2)q^3 by
sum_{j=4}^7 binom(7,j)binom(955,7-j)/binom(962,7).
Finite averaging supplies a labeling with no more than the floor of this
expectation in conflict edges. Deleting all right endpoints costs no
more than that edge count, with no independence assumption. Compare
the remaining right size with 1532496; the unchanged left eligible size
must also clear that threshold.

Completed in canonical L130: the expectation lies strictly between
225024 and 225025, leaving at least 2346329 right supports and exactly
2552584 left supports. Both clear the threshold with zero ambient
overlap. All eleven exact-arithmetic checks passed; the complete eight
intersection cases, rational expectation and size bounds were inspected.
The canonical proof supplies the finite existence argument. A separate
critical audit remains required; this working record preserves the
pre-calculation reasoning rather than replacing that proof.
