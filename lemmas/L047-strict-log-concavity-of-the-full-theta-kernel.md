# Lemma 47: strict log-concavity of the full theta kernel

**Hypotheses.** u≥0, v=πe^{2u}, and K=Σ_{n≥1}K_n is the actual theta kernel.

**Conclusion.**

(log K(u))'' < -(68/125)v <0.

Thus K is strictly log-concave on [0,∞). This does not by itself assert real zeros for its Fourier transform.

**Proof.** Here v>3 and v_n=n²v. The explicit factors in Lemma 45 give

K_n/K_1=n²(2n²v-3)/(2v-3)·e^{-(n²-1)v}≤2n⁴e^{-(n²-1)v},

since 2v-3≥v and 2n²v-3≤2n²v. For n≥2, the slope difference from Lemma 45 is negative, with absolute value at most 2(n²-1)v+6/(2v-3)≤2(n²-1)v+2≤3(n²-1)v.

Variance is minimized by centering at the weighted mean, so it is bounded above by the mean square distance from the first slope. Using w_n≤K_n/K_1 gives

Var_w(ℓ_n')≤Σ_{n≥2}w_n(ℓ_n'-ℓ_1')²
≤18v²Σ_{n≥2}n⁴(n²-1)²e^{-(n²-1)v}
≤18v²Σ_{n≥2}n⁸e^{-(n²-1)v}.

Write n=2+j. Then n⁸≤256·256^j, because 2+j≤2(j+1) and j+1≤2^j. Also n²-1≥3+5j for integer j≥0. Therefore

Σ_{n≥2}n⁸e^{-(n²-1)v}≤256e^{-3v}/(1-256e^{-5v})<512e^{-3v}.

For the denominator bound, v>3 and e³>20 imply e^{5v}>e^{15}>20⁵>512. The elementary bound e³>20 follows by summing its exponential series from degree zero through eight (all later terms are positive). Thus the variance is <9216v²e^{-3v}.

The mean curvature in Lemma 46 is strictly less than -4Σw_n n²v≤-4v by Lemma 45. The function v e^{-3v} decreases for v≥3, so

2304v e^{-3v}≤6912e^{-9}<6912/8000=108/125,

again using e³>20. Combining the mean and variance bounds yields

(log K)''<-4v+9216v²e^{-3v}<-4v(1-108/125)=-(68/125)v.

All sums and derivatives are justified by Lemma 46. ∎
