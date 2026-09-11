# Lemma 69: positive divergence of the full sparse interaction

**Hypotheses.** Let f, x_n=2^n, b_n=1-2^{-n}, and c_n=1-2^{-n-1} be the explicit product and parameters of Lemma 68. Put w_n=x_n+i b_n.

**Conclusion.** There are real remainders R_n such that

Im(f''(w_n)/f'(w_n)) = 2^{n+2}-1/b_n-2/(b_n+c_n)+R_n,

|R_n| ≤ [4+128(n-1)+128/3]4^{-n}.

In particular Im(f''(w_n)/f'(w_n))=2^{n+2}-2+o(1) tends to positive infinity, although Im w_n tends to the nonattained height supremum 1.

## Proof

Lemma 68 proves that these zeros are simple and gives the exact product and reciprocal-square summability. The logarithmic-derivative proof of Lemma 64 applies to this explicit paired product: remove the factor containing w_n, differentiate the residual logarithmic tail uniformly on a small disc about w_n, and use the product rule. That proof uses only the product and its summability for this identity, not the theta heat equation. It gives

f''(w_n)/f'(w_n) = 2Σ_{ρ≠w_n} 1/(w_n-ρ),

where ρ ranges over all other zeros. Here even the unpaired complex series converges absolutely: there are eight zeros per cluster and Σ_ρ |ρ|^{-1}≤8Σ_{m≥1}2^{-m}<∞, while |w_n-ρ|≥|ρ|/2 in its tail. Thus rearranging the paired identity into this series is justified. For ρ=u+iv its imaginary summand is

Im(2/(w_n-ρ)) = 2(v-b_n)/[(x_n-u)²+(b_n-v)²].

At u=x_n there are three other zeros. The higher zero x_n+i c_n contributes 2/(c_n-b_n)=2^{n+2}. The two lower zeros x_n-i b_n and x_n-i c_n contribute -1/b_n and -2/(b_n+c_n), respectively.

Define R_n to be the sum over all remaining zeros. Since every height lies in (-1,1), the absolute numerator in each imaginary summand is at most 4. The four zeros with real coordinate -x_n have horizontal distance 2x_n; their total absolute contribution is at most 4/x_n².

For m≠n each of the eight zeros in cluster m has horizontal distance at least |x_n-x_m|: the negative real coordinate has distance x_n+x_m, which is larger. The total absolute contribution of cluster m is therefore at most 32/(x_n-x_m)². If m<n, then x_m≤x_n/2, so

Σ_{m<n} 1/(x_n-x_m)² ≤ 4(n-1)4^{-n}.

If m>n, then x_n≤x_m/2, so

Σ_{m>n} 1/(x_n-x_m)² ≤ 4Σ_{m>n}4^{-m} = (4/3)4^{-n}.

Adding these bounds proves the claimed estimate for R_n. Its upper bound tends to zero since n4^{-n}→0. Finally b_n,c_n→1, so the two exact negative terms tend to -2, proving the asymptotic and divergence. ∎

## Qualifications

This rules out a universal nonpositive limiting full interaction along every sequence approaching the height supremum under these generic product and strip assumptions. It does not exclude a favorable sequence of other zeros. The expression is an instantaneous velocity only if a suitable heat evolution through f is separately established; no such evolution or positive Fourier kernel is asserted here. No conclusion about the theta heat slices, a time-dependent height envelope, or RH follows.

## Verification and formalization obligations

The proof is analytic; finite computation is not its justification for convergence or divergence. `python3 scripts/heat/check_sparse_net_interaction.py` checks the three exact local contributions and the stated bounds for finite cluster sums using rational arithmetic. Formalization would require the explicit-product logarithmic derivative, absolute rearrangement, the horizontal-distance bounds, the geometric tail sum, and the elementary asymptotic limit.
