# Lemma 70: vanishing upward contribution at upper sparse zeros

**Hypotheses.** Let f, x_n=2^n, b_n=1-2^{-n}, and c_n=1-2^{-n-1} be the product and parameters of Lemma 68. Set u_n=x_n+i c_n. Sum over zeros with multiplicity, and define

S_f(u_n)=Σ_{Im ρ>c_n}|u_n-ρ|^{-2}.

**Conclusion.** These simple zeros approach the nonattained height supremum 1, and

0≤S_f(u_n)≤(16/3)4^{-n},

0≤E_f(u_n)≤(16/3)8^{-n}→0.

In particular (1-c_n)S_f(u_n)→0 as well. Thus this product admits a favorable sequence for both sufficient estimates discussed in Lemma 67, although Lemma 68 supplies another sequence with divergent upward contribution.

## Proof

Lemma 68 supplies the complete simple zero set, the height supremum, and the definition and finiteness of E_f. The positive heights in cluster m are b_m and c_m, each at real coordinates ±x_m. For m≤n both heights are at most c_n. For m=n+1, b_{n+1}=c_n, so the two zeros at that height contribute neither to S_f nor to E_f. Every strictly higher zero therefore belongs to a cluster m>n, with at most four eligible zeros per cluster.

For such a zero the horizontal distance from u_n is at least x_m-x_n≥x_m/2. Consequently its reciprocal squared distance is at most 4·4^{-m}. Summing over the eligible zeros, and harmlessly including all four positive-height zeros in each later cluster, gives

S_f(u_n)≤16Σ_{m>n}4^{-m}=(16/3)4^{-n}.

All terms are nonnegative, so the finite partial-sum inequalities and the convergent geometric majorant justify the infinite bound. For every strictly higher zero, 0<Im ρ-c_n<1-c_n=2^{-n-1}. Multiplying the preceding reciprocal-square bound by 2(1-c_n)=2^{-n} yields

E_f(u_n)=2Σ_{Im ρ>c_n}(Im ρ-c_n)|u_n-ρ|^{-2}
≤2^{-n}S_f(u_n)≤(16/3)8^{-n}.

Both asserted limits follow from geometric decay, and c_n→1. ∎

## Qualifications

This is a statement about the explicit product only. It neither proves a favorable-sequence theorem for general strip products nor supplies a theta heat evolution or time-uniform height-envelope estimate. The universal sequential assertion refuted by Lemma 68 remains false. RH remains unproved.

## Verification and formalization obligations

The proof is analytic and needs no numerical certificate. The finite exact checks in `python3 scripts/heat/check_sparse_upper_contribution.py` verify height eligibility, separation, and the stated bounds; they do not replace the infinite geometric majorant. Formalization would require the listed zero set, splitting a nonnegative sum by cluster, the geometric series, and the limiting bounds. The only direct mathematical input is Lemma 68; Lemma 67 is cited for interpretation only.
