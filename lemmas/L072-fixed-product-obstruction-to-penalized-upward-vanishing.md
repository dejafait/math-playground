# Lemma 72: fixed-product obstruction to penalized upward vanishing

**Hypotheses and construction.** For integers n≥1 put

X_n=2^n, b_n=1−2^{-n}, ε_n=8^{-n}/2,
d_n=4^{-n}/2, δ_n=d_n², c_n=b_n+δ_n,
w_n=X_n+i b_n, v_n=X_n+d_n+i c_n.

Let A_n={w_n, conjugate(w_n), v_n, conjugate(v_n)} and define

f(z)=Π_{n≥1} Π_{α∈A_n}(1−z²/α²).

**Conclusion.** This defines a nonzero even real entire function with precisely the distinct simple zeros ±w_n, ±conjugate(w_n), ±v_n, ±conjugate(v_n). Its full-zero reciprocal-square sum is finite and its zero-height supremum is H=1, not attained. At ε=ε_n the only maximizers of Im ρ−ε(Re ρ)² are w_n and −conjugate(w_n). Both have upward contribution

E_f(w)=2Σ_{Im ρ>Im w}(Im ρ−Im w)/|ρ−w|² >1.

Thus one fixed product can fail upward vanishing along a sequence of penalties decreasing to zero, regardless of the choice among maximizing zeros at those penalties.

## Proof

Since 0<δ_n=(1/4)16^{-n}<(1/4)2^{-n}, we have

0<b_n<c_n<1−(3/4)2^{-n}<1.

Also 0<d_n≤1/8 and X_n+d_n<X_{n+1}. All listed zeros are therefore distinct, nonzero, and lie in |Im z|<1; their heights approach 1. Each cluster has eight zeros of modulus at least 2^n, so its contribution to the full reciprocal-square sum is at most 8·4^{-n}. The total is at most 8/3.

For any fixed disk |z|≤R, the sum over representatives of |z²/α²| is uniformly bounded by R²Σ_n 4·4^{-n}<∞. For all sufficiently large n these quantities are at most 1/2; the analytic power-series logarithm satisfies |log(1−z²/α²)|≤2|z²/α²|. The logarithmic tails converge uniformly on the disk, so their exponentials are analytic and nonvanishing. Multiplication by the finite initial product proves local uniform convergence, analyticity, and that the stated zeros are the only zeros and are simple. Each finite product is even and real under conjugation; the limit inherits those properties and f(0)=1.

Fix n. The score of w_n at ε_n is

m_n=b_n−ε_n X_n²=1−(3/2)2^{-n}.

Negative-height zeros have strictly smaller scores than positive-height zeros at the same real coordinate. Reflection of a positive-height zero across the imaginary axis preserves its score. It suffices to compare right-half-plane positive-height zeros.

For k<n, either zero in cluster k has score at most its height, hence strictly less than 1−(3/4)2^{-k}. Since 2^{-k}≥2·2^{-n}, this is at most m_n. For k>n, either zero has height less than 1 and real coordinate at least 2^{n+1}; its score is therefore strictly less than

1−ε_n 4^{n+1}=1−2·2^{-n}<m_n.

In cluster n, the satellite score minus m_n is

δ_n−ε_n(2X_n d_n+d_n²)
=−d_n²(1+ε_n)<0,

because d_n=ε_n X_n and δ_n=d_n². This proves the claimed exact maximizing set.

The upward sum is well-defined by the reciprocal-square tail argument in Lemma 67, used here only for its definition and convergence estimate: for fixed w and |ρ|>2|w|, |ρ−w|≥|ρ|/2, and the numerator is bounded by 4 since all heights lie in (−1,1). The remaining sum is finite with nonzero denominators. At w_n the single higher zero v_n contributes

2δ_n/(d_n²+δ_n²)=2/(1+d_n²)>1.

Every other upward term is nonnegative. Reflection ρ↦−conjugate(ρ) is a bijection of the zero set preserving heights and distances, so the same bound holds at the other maximizer. Finally ε_n↓0, completing the fixed-product counterexample. ∎

## Qualifications

This disproves the generic fixed-product assertion that every quadratic-penalty selection has E_f(w_ε)→0 as ε↓0. It does not disprove existence of some favorable sequence of penalties or of unpenalized zeros approaching the height supremum. No estimate of the full signed interaction, heat evolution, or theta-specific assertion is proved here. The product is not identified with a theta heat slice and has no implication for RH.

## Verification and formalization obligations

The infinite statements follow from the analytic and all-index inequalities above. Supplementary exact rational checks are reproducible with `python3 scripts/heat/check_fixed_product_penalty.py`; finite checks are not used as evidence for an infinite limit. Formalization would require uniform logarithmic-tail convergence, exact simple zero identification, the geometric reciprocal-square sum, the three all-index score comparisons, and the absolutely convergent nonnegative upward sum and reflection bijection.
