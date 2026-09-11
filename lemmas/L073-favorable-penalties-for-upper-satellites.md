# Lemma 73: favorable penalties for upper satellites

**Hypotheses.** Use the fixed product f and parameters X_n, b_n, ε_n, d_n, δ_n, c_n, w_n, v_n of Lemma 72, for n≥1. Set η_n=(5/12)ε_n. For a zero u define

S_f(u)=Σ_{Im ρ>Im u}|ρ−u|^{-2},
E_f(u)=2Σ_{Im ρ>Im u}(Im ρ−Im u)/|ρ−u|².

**Conclusion.** At penalty η_n, the only maximizers of Im ρ−η_n(Re ρ)² are v_n and −conjugate(v_n). At both maximizers,

0≤S_f(v_n)≤12·4^{-n},   0≤E_f(v_n)≤24·8^{-n}.

In particular η_n↓0, their heights tend to 1, and every selection of maximizing zeros along these penalties has upward contribution tending to zero. Combined with Lemma 72, this same product has both favorable and unfavorable penalty subsequences.

## Proof

Lemma 72 supplies the complete simple zero set, its product convergence, and the inequalities 0<b_k<c_k<1−(3/4)2^{-k}. Reflection across the imaginary axis preserves scores, heights, and distances. Negative-height zeros have strictly smaller scores than their conjugates. It therefore suffices to compare the right-half-plane positive-height zeros.

Fix n and put t=2^{-n}. The center w_n has score

q_n=b_n−η_n X_n²=1−(29/24)t.

The satellite's score exceeds q_n, since d_n=ε_nX_n and

δ_n−η_n(2X_nd_n+d_n²)
=d_n²[1−(5/12)(2+ε_n)]>0.

Indeed ε_n≤1/16, so the bracket is at least 1−(5/12)(33/16)=9/64>0.

For k<n, either positive-height zero has score less than its height bound 1−(3/4)2^{-k}≤1−(3/2)t<q_n.

For k=n+1, δ_{n+1}=2^{-4n-6}<t/16, since δ_{n+1}/t=2^{-3n-6}≤1/512. Thus either height is at most c_{n+1}<1−(7/16)t. Its squared real coordinate is at least 4^{n+1}, giving score strictly less than

1−(7/16)t−η_n4^{n+1}=1−(61/48)t<q_n.

For k≥n+2, the height is less than 1 and the penalty is at least η_n4^{n+2}=(10/3)t, so the score is again strictly less than q_n. These exhaustive comparisons prove the exact maximizing pair for every n, including n=1 where the earlier-cluster case is empty.

For the interaction bound, clusters m<n have all their heights below b_n: their maximum is less than 1−(3/4)2^{-m}≤1−(3/2)t<b_n. Cluster n has no height above c_n. Therefore every zero strictly higher than v_n belongs to a cluster m>n, with at most four eligible zeros per cluster. Its horizontal distance from v_n is at least

X_m−X_n−d_n≥X_m/2−1/8≥X_m/3,

where X_m≥4 and d_n≤1/8. This also bounds the reflected higher zeros, whose horizontal distances are larger. Hence the nonnegative partial sums satisfy

S_f(v_n)≤36Σ_{m>n}4^{-m}=12·4^{-n}.

The convergent geometric majorant both justifies the infinite sum and proves its bound. Each positive height difference is less than 1−c_n<t, so termwise multiplication and passage through the nonnegative partial sums give

E_f(v_n)≤2t S_f(v_n)≤24·8^{-n}.

Reflection gives identical sums at the other maximizer. Geometric decay proves the stated limits. ∎

## Qualifications

This resolves the favorable-subsequence question for the single explicit product in Lemma 72. It does not prove that every strip paired product admits such a sequence, or identify this product with a theta heat slice. Neither a time-uniform heat-envelope estimate nor RH follows. The unfavorable subsequence in Lemma 72 remains valid.

## Verification and formalization obligations

The proof uses all-index score inequalities and an infinite geometric majorant, not numerical extrapolation. Supplementary exact rational checks are reproducible with `python3 scripts/heat/check_satellite_penalties.py`. Formalization would require the exact zero set from Lemma 72, the exhaustive score comparisons, the reflection bijection, nonnegative summation by clusters, and geometric decay.
