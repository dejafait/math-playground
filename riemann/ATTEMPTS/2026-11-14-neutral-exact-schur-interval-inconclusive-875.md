# Fixed U12 interval energy-block evaluator — inconclusive875

The single gate-approved calculation is complete; its full definitions,
method, numerical qualifications and unresolved signs are canonical in
[C750c Proof5](../lemmas/C750c-fixed-neutral-scalar-floor-schur-rejection.md).
Matrices and all errors are in `scripts/neutral-exact-schur/`.

WHY IT FAILS: Complete interval entries and139 accounting checks do not
certify the complementary block: in both reflection sectors the second
unshifted elimination pivot overlaps zero. Neither a positive block nor
an exact kernel is established, so the calculation cannot apply either
the inverse or the singular generalized Schur test. This is a limitation
of this bounded evaluator, not a negative-energy direction or a stop for
the exact-block route itself. No mode/window/shift or precision sweep was
performed. Preserve scalar-stop873 separately. The next nominated source
comparison, assessment875, concerns a different zero-Gram/remainder
certificate for the same fixed space and remains REVIEW_REQUIRED.
