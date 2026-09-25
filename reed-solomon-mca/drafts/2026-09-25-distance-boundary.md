# Three omissions at the minimum-distance boundary

Date: 2026-09-25. One focused test in the frozen affine-line model.

## Gap, intermediate target, and decision test

L006 determines the small cells only when 3r<=n-k. The first uncovered
cell for the smooth length-16, dimension-8 code has r=3 and distance nine.
Test whether five bad challenges can occur at support cutoff thirteen,
exceeding the tentative extension (r+1)/q=4/q. A witness would stop that
extension; an obstruction could sharpen the upper bound at the boundary.
This could determine one further cell's exact field threshold. Wider cells,
the maximal radius, and the ABF26 event and parameter correspondence would
still be unresolved.

The existing endpoint failures and field-size qualifications are preserved.
L006 explicitly left equality at minimum distance open; no earlier lemma
determines this cell. The official https://proximityprize.org/ statement was
reread on this date, with the same preliminary target and qualifications.
The starting exploration count is zero.

## Saved unfinished reasoning

For three distinct parameters, the affine discrepancy of three errors of
weight at most three is a codeword of weight at most nine. If nonzero, its
three supports must be disjoint triples. Given such a triple of errors, any
further error cannot be an affine combination of two of them: its weight
would be six. Applying the discrepancy test repeatedly should force all
error supports to be disjoint triples, giving at most floor(16/3)=5.
Otherwise all errors have one affine lift and the coordinate-root count
should still give at most four, including the small-active-support case.

A candidate five-support construction uses the order-three transformation
T(x)=1/(1-x) on the projective line over F_17. The exceptional orbit is
{infinity,0,1}; the other fifteen elements should form five disjoint triples.
Their monic root polynomials lie in the cubic pencil
P_t(X)=X^3-tX^2+(t-3)X+1. The remaining task is to turn this support
pencil into actual collinear error syndromes, construct input words, and
verify the original same-support failure event. This is unfinished, not a
claimed theorem or a complete challenge candidate.

## Completed assessment

The five-parameter test succeeds. The full proof is
[L007](../lemmas/L007-minimum-distance-boundary-sharp-error.md): at distance
3r the errors either share an affine lift or have pairwise disjoint
supports of size r. The respective counts are at most r+1 and floor(n/r).
For length 16 and r=3 this proves an upper bound of five. The cubic pencil
has five disjoint split fibers at parameters 0,3,6,10,14. Weighting each
fiber by U'(x)/(P_t'(x)B(x)^2), with U=X^16-1 and B=X^2-X, makes
their quotient classes affine in t. The lemma supplies explicit input
words and proves failure on every witnessing thirteen-coordinate support.

The exact error is 5/q on [3/16,1/4) for this domain over every F_(17^s).
Thus the unconditional extension of the r+1 count fails; the
[failed inference](../ATTEMPTS/003-unconditional-distance-boundary-extension.md)
is retained separately. The same dichotomy also proves the exact count
44 at n=256,k=128,r=43, since floor(256/43)=5<44. This adds one exact
cell, without extending L004's wider sufficient interval delta<90/256.

At the actual budget, the new smooth example is safe on its proved cell
exactly when q>=5*2^128. The least exponent in this tower is 32, where
L004's count 23 is too large to certify safety. The exact integer budget
there allows six bad parameters; seven would prove unsafety. This gives
a concrete reason to test the next cell, where the distance argument no
longer forces errors to have disjoint supports. It does not resolve the
general maximal radius or the source correspondence.

The auxiliary script checks the original event for every parameter of
F_17 and every admissible support of the explicit pair, as well as the
polynomial identities and budget comparisons. It does not maximize over
all input pairs; the proof provides that upper bound and the extension-field
claim. Review covered nonzero interpolation coefficients, the equality
case in the weight bound, the small-active-support failure condition,
all denominators, and codeword degree seven. No prior lemma is used as
a mathematical input to L007; L004 and L006 are comparisons. Mathlib
coverage is not checked. No complete challenge candidate appeared.

Outcome: ADVANCE, with zero consecutive exploration turns. The sole
current next action is in PROGRESS.md.
