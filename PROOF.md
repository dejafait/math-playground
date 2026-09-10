# Current best argument — incomplete

The write-up establishes partial results, not RH. Current research status and the next task live in [PROGRESS.md](PROGRESS.md). The sole node-and-edge definition and lemma navigation live in [DAG.md](DAG.md); full statements and proofs live in individual lemma files. Standard definitions and named starting theorems are in [foundations](foundations/notation-and-inputs.md).

## Assembly and unresolved gap

The current main route begins with the classical zero localization and theta representation, proves the growth required for an unconditional Hadamard product, and translates that product into summable reciprocal-zero nodes. Lemmas 30–32 then prove that all mixed polynomial forms being nonnegative would force the nodes to be real and hence prove RH. This is a proved equivalence, not a proved positivity assertion.

For the actual theta moments, the analytical estimates prove six individual power-sum signs and a degree-two Jensen test. The interval certificates additionally prove H_1 and H_2 positive definite, under the explicit arithmetic contracts. No step extends these finite results to arbitrary degree. Proving that extension—or finding a different argument that excludes every off-line zero—is the unresolved gap.

Counterexamples retained in the lemma chain and archived in ATTEMPTS rule out the tested shortcuts: symmetry alone, continued prime positivity, positive Laplace/Fourier kernels alone, all scalar power-sum signs alone, and coarse strip geometry alone do not supply the missing mixed positivity. None is a counterexample to RH itself.

The later comparison-kernel results strengthen these obstructions: even strict log-concavity, superexponential decay, the established generic zero geometry, and any fixed finite number of positive Hankel tests can coexist with nonreal zeros. The comparison function may depend on the number of tests; none is asserted to pass every degree. These are counterexamples to proposed sufficient conditions, not to RH.

## Partial results

The write-up establishes classical zero localization, the entire theta completion and cosine representation, a paired Hadamard product, reciprocal-zero identities, a small zero-free rectangle, six scalar signs, and a degree-two Jensen test. The actual theta kernel is also shown to be strictly log-concave with a smooth even extension. The saved interval certificates establish positive definiteness of H_1 and H_2 under explicit arithmetic contracts. Detailed statements and qualifications belong in the lemma files accessible through the DAG.

No novelty or proof of RH is claimed. The all-degree positivity assertion remains the missing theorem.

## Known traps checked

- No explicit-formula error estimate, prime-number-theorem error term, or unproved zero-free strip is used.
- No RH-equivalent positivity is assumed. Corollary 32a explicitly labels its all-degree condition as RH-equivalent and unproved; it is never used as a premise for an unconditional conclusion.
- Every infinite manipulation has a stated bound: Dirichlet/prime absolute sums, compact alternating-series tails, exponential theta tails, or summable reciprocal squares. The boundary proof uses local Taylor/Laurent bounds, not a boundary interchange of prime sums.
- There are no numerical zero computations or extrapolations from finitely many zeros. The finite determinant calculations use proved tails, proved quadrature remainders, and outward interval arithmetic, with their implementation contracts explicitly stated. An ordinary decimal value would not suffice.
- A positive kernel does not make its Fourier transform real-rooted. Reflection invariance of a set does not make every point fixed. Concrete counterexamples are retained.
- Algebraic squares in mixed forms are not replaced by modulus squares; that replacement would erase the very obstruction being tested.
- Finite positive scalar sums, a degree-two Jensen polynomial, and two finite positive Hankel matrices are not an all-degree theorem. No Li, Robin, Lagarias, or Nyman–Beurling criterion is claimed proved.

## What a Lean check would need

The [formalization inventory](foundations/formalization.md) records exact obligations and the limits of its coverage. Lemma statements and their analytic bounds are the authoritative mathematical text. No Lean is used or written; checking these partial results would still leave the all-degree positivity requirement unproved.
