# Four leading coefficients do not test the large-cutoff Gram certificate

The approved bandwidth-two diagnostic is completed in
[L566](../lemmas/L566-hermite-banded-leading-test-limitation.md),
now independently audited. For every N>=3 its four coefficient
equations have a PSD zero-filled matrix satisfying the proposed
sparsity; the result does not need special coefficient ratios. The
actual N=2 discriminant instead has a certified negative value.
The [rational certificate](../scripts/hermite-gram/leading-block-boundary-certificate.json)
includes all panels and both omitted tails, not a numerical sign guess.

**WHY IT FAILS.** The leading equations do not constrain the endpoint
diagonal coupled to their last visible off-diagonal entry. Retaining
that necessary free variable permits explicit positive-definite
supported blocks for every larger cutoff. Therefore the test cannot
reject the restricted certificate at unbounded cutoffs; discarding
that diagonal would create a false obstruction. N=2 sees the entire
polynomial and fails, but L564 uses only N>=64. Park this completed
four-coefficient diagnostic. A full lower-coefficient or other global
constraint would be a materially different target requiring separate
review; the bandwidth restriction itself remains open at large N.
L565's earlier diagonal-CD stop is preserved with its own scope.
