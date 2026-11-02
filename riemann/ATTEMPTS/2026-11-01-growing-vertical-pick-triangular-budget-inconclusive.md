# Growing vertical Pick block: triangular reduction remains inconclusive

WHY IT FAILS: [L640](../lemmas/L640-vertical-pick-full-gram-arithmetic-reduction.md)
retains the full Cauchy Gram, controls the gamma and rational correction,
and now converts the arithmetic to exact orthonormal triangular coordinates,
with the full tail beyond ceil(T^12) charged and total normalized error
at most 37/T. The remaining finite signed matrix has no established norm
margin or asymptotic lower witness. Its underlying sample matrix has
Hermitian part (1/2)I+(3/2)11*, so its numerical range touches the critical
line even though every eigenvalue has real part 2. An argument requiring
that numerical range to lie in Re(s)>1 is therefore unavailable. This
does not show that the signed norm is at least one; the large absolute
upper bounds also do not show it. This first bounded attempt is
inconclusive, not an exhausted route or a refutation of RH. The exact
triangular representation is a specific refinement for a further signed
test; repeating the absolute majorant alone would provide no new evidence.
