# Lemma 172: frozen third moment and first moment test

**Hypotheses.** Use the normalized frozen sums Z_j and normalized block
averages E_j of L171, at H=T^(3/4). Set Y_j=|Z_j| and
B(T)=T^(1/4)log T. All assertions concern sufficiently large T.

**Conclusion.** Uniformly in j,

(E_j Y_j²)²/(E_j Y_j) ≤ E_j Y_j³ ≤ C sqrt(B(T)).          (1)

The available second- and fourth-moment bounds alone cannot improve the
upper bound in (1) to O(1). A uniform bound E_j Y_j³≤C would imply
uniform integrability of Y_j² and a positive uniform lower bound on
E_j Y_j. Conversely, if some sequence T_k→∞ and blocks j_k satisfies
E_(j_k)Y_(j_k)→0, then E_(j_k)Y_(j_k)³→∞ and the squares along that
sequence are not uniformly integrable. No such sequence is established
for the actual sums here.

**Proof.**

L171 gives E_jY_j²=1+O(T^(−1/4)log T) and E_jY_j⁴≤CB(T).
In particular the second moment lies between 1/2 and 2 eventually.
All moments are finite because each sum is finite on a compact block.
Cauchy–Schwarz applied to Y_j and Y_j² gives

E_jY_j³ ≤ sqrt(E_jY_j² E_jY_j⁴) ≤ C sqrt(B(T)).

Applied instead to Y_j^(1/2) and Y_j^(3/2), it gives

E_jY_j² ≤ sqrt(E_jY_j E_jY_j³).

The first moment is positive since the second is positive, proving (1).
If E_jY_j³≤C, the latter inequality yields E_jY_j≥1/(4C).
For every K>0, the pointwise inequality on Y_j²>K gives

E_j[Y_j² 1_(Y_j²>K)] ≤ K^(−1/2)E_jY_j³ ≤ C/sqrt(K).

This proves the asserted uniform integrability (over sufficiently large
T and all their blocks).

For sharpness of inference from the two moment bounds, take an abstract
nonnegative variable Y_T equal to sqrt(B(T)) with probability 1/B(T)
and zero otherwise. For T large enough B(T)≥1. Its second, third and
fourth moments are exactly 1, sqrt(B(T)), and B(T). Thus it meets the
stated moment bounds and attains the interpolation scale. It is not
claimed to satisfy the oscillatory structure of the actual frozen sums.

Finally suppose the specified actual sequence has first moments tending
to zero. The lower bound in (1) makes its third moments tend to infinity.
To prove failure of uniform integrability directly, for any fixed K>0,

E_j[Y_j² 1_(Y_j²≤K)] ≤ sqrt(K) E_jY_j.

Along the sequence this tends to zero, whereas E_jY_j² tends to one.
Hence E_j[Y_j² 1_(Y_j²>K)] tends to one for every fixed K. The supremum
of those tails cannot tend to zero as K→∞. This proves the conditional
obstruction without an interchange of limits. ∎

## Scope, verification, and formalization obligations

This completes the interpolation test, a scoped part of the proposed
fractional-moment route. It neither proves nor disproves a uniform third
moment for the actual sums. The first absolute moment test needs new
oscillatory information; second and fourth moments do not settle it.
Uniform integrability, cutoff covariance and RH remain unproved.

Verification is analytic: both Cauchy–Schwarz factorizations, positivity
of the denominator, all three moments of the probability model, the
square-root cutoff factors, and the order of the two tail limits are
explicit above. Formalization would require these elementary probability
inequalities together with L171's uniform estimates. No numerical
certificate or external theorem is needed.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
