# Attempt: Cauchy–Binet makes every Hankel determinant positive

Date: 2026-09-09

Outcome: the determinant identity succeeds; the positivity shortcut fails.

The mathematical counterexample or obstruction is proved in [Lemma 42](../lemmas/L042-absolutely-convergent-vandermonde-expansion.md).

**WHY IT FAILS.** The moment matrix factors as VVᵀ, not VV*, because the power sums use algebraic powers of complex reciprocal zeros. Cauchy–Binet therefore produces algebraic squares. For a conjugate pair c,conj(c), the Vandermonde contribution is |c|⁴(c-conj(c))²=-4|c|⁴(Im c)²<0. Declaring these squares nonnegative would assume real nodes, exactly the unproved zero-location property. The actual theta representation supplies positive ordinary moments, but no identity turning these reciprocal-zero determinants into nonnegative modulus-square integrals has been proved.
