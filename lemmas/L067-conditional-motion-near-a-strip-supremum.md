# Lemma 67: conditional motion near a strip supremum

**Hypotheses.** Fix a real theta heat slice as in Lemma 64. Suppose the supremum H of the imaginary parts of its zeros is finite and positive. Let w=a+ib be a simple zero with a≠0 and 0<b≤H. All zero sums below count multiplicities. Write Q={w,-w,conjugate(w),-conjugate(w)} and define

S(w)=Σ_{ρ: Im ρ>b} |w-ρ|^{-2}.

**Conclusion.** S(w) is finite, and the local simple-zero branch has instantaneous imaginary velocity v(w) satisfying

v(w) ≤ -1/b-b/(a²+b²)+2(H-b)S(w).                 (1)

Consequently, if w_n=a_n+ib_n are such simple zeros, b_n→H, and

(H-b_n)S(w_n)→0,                                  (2)

then limsup_n v(w_n)≤-1/H. In particular a uniform bound on S(w_n) suffices. Condition (2) is an additional, unproved condition for the theta zeros, not a conclusion of finite strip height.

## Proof

Evenness gives |Im ρ|≤H for every zero. Reciprocal-square summability in the product used by Lemma 64 implies summability over the full multiset of zeros as well. For fixed w, when |ρ|>2|w|, |w-ρ|≥|ρ|/2. Thus the sum of |w-ρ|^{-2} over all zeros other than w is finite: its tail is bounded by four times the reciprocal-square sum, and its finite part has no zero denominator. This proves finiteness of S(w).

The imaginary parts of the individual reciprocal contributions are now absolutely summable, even though their complex counterparts need not be. Indeed,

|Im(2/(w-ρ))| = 2|b-Im ρ|/|w-ρ|² ≤ 4H/|w-ρ|².

It is therefore legitimate to split the imaginary part of the convergent paired velocity series of Lemma 64 into subsets of zeros. Extracting Q gives the contribution -1/b-b/(a²+b²) by Lemma 66, whose quartet calculation does not require maximal height. The remaining imaginary sum equals

Σ_{ρ outside Q} 2(Im ρ-b)/|w-ρ|².

Terms with Im ρ≤b are nonpositive. All higher zeros are outside Q, and their numerators are at most 2(H-b). Dropping the nonpositive terms and summing proves (1). Applying (1) to w_n, discarding the further nonpositive term -b_n/|w_n|², and using (2) gives the asserted limsup bound. No differentiation in n or of an infinite sum is involved. ∎

## What the estimate does and does not supply

If H is not attained, any sequence of zeros with heights tending to H escapes every compact subset of the plane. Otherwise a bounded subsequence would converge to a zero at height H by continuity, contradicting nonattainment. With bounded imaginary parts this implies |a_n|→∞. The compact convergence in Lemma 64 therefore does not supply uniform estimates along this sequence. Existence of a sequence of *simple* zeros approaching H is also not proved.

The exact nonnegative upward contribution is

E(w)=2Σ_{Im ρ>b}(Im ρ-b)/|w-ρ|².

The same proof permits replacing (2) by E(w_n)→0, a weaker sufficient condition. Neither condition is claimed necessary, since downward terms may offset upward ones. One concrete sufficient estimate for (2) is a horizontal separation d_n>0 from every higher zero, together with

T_n=Σ_{Im ρ>b_n} 1/(1+(a_n-Re ρ)²),
(H-b_n)(1+d_n^{-2})T_n→0.

Indeed |w_n-ρ|^{-2}≤(a_n-Re ρ)^{-2}≤(1+d_n^{-2})/(1+(a_n-Re ρ)²). Each T_n is finite by the strip bound and reciprocal-square summability. Uniform separation or uniform weighted counting bounds are not established here.

The elementary local obstruction to a termwise limit is explicit. For H=1, w=2+i(1-ε), and ρ=2+i(1-ε/2), with 0<ε<1, the single higher-zero contribution equals 4/ε, although both heights approach H. This is only an algebraic configuration, not a claimed theta zero configuration or counterexample to the full velocity bound. It shows why small height differences alone cannot bound the positive terms; nearby denominators must also be controlled.

Finally the limsup here is over velocities of separate local branches at one fixed parameter. It is not an upper Dini derivative bound for the parameter-dependent supremum of all zero heights. Such a passage would additionally require time-uniform control, treatment of multiple zeros, and exclusion of uncontrolled branches arriving from infinity. Those assertions and RH remain unproved.

## Verification and formalization obligations

The proof is analytic and requires no numerical certificate. Check the full-zero reciprocal-square tail bound, the 4H majorant, the extraction of the quartet, and the limsup inequality. Formalization would require absolute summation of imaginary contributions, splitting a countable multiset by height, the conditional sequential limit, and the elementary separation estimate. The small-denominator example is verified directly from |w-ρ|²=ε²/4 and 2(Im ρ-Im w)=ε.
