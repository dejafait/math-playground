# Lemma 76: full upward subsequence under bounded local count

**Hypotheses.** Assume the monotone quartet hypotheses of Lemma 74: 0<x_1<x_2<⋯ tends to infinity, 0<b_1<b_2<⋯ tends to H<∞, and Σ_n x_n^{-2}<∞. Let f be its paired product and w_n=x_n+i b_n. Assume additionally that there is an integer M≥1 such that every half-open interval [t,t+1), for real t≥0, contains at most M of the coordinates x_j.

Define the full upward contribution at w_n by

E_f(w_n)=2Σ_{Im ρ>b_n}(Im ρ−b_n)/|ρ−w_n|²,

where ρ ranges over all zeros of f.

**Conclusion.** There are infinitely many indices n with x_{n+1}−x_n≥1/(2M). Along those indices E_f(w_n)→0. In particular

liminf_{n→∞} E_f(w_n)=0.

No lower bound on every successor gap is required.

## Proof

Lemma 74 supplies the exact simple zero set and the product properties. Since b_n>0 and the heights are strictly increasing, the higher zeros are precisely x_j+i b_j and −x_j+i b_j for j>n. Consequently E_f(w_n)=U_n+V_n, where

U_n=2Σ_{j>n}(b_j−b_n)/[(x_j−x_n)²+(b_j−b_n)²]

and V_n is the reflected sum in Lemma 74. These series converge at each fixed n: once x_j≥2x_n, the summand in U_n is at most 8H/x_j²; finitely many earlier terms have nonzero denominators. The reflected sum converges by Lemma 74.

Set g=1/(2M). Counting in the intervals [k,k+1), for integers 0≤k≤floor(x_n), gives

n≤M(floor(x_n)+1)≤M(x_n+1),

and hence x_n≥n/M−1. If there were only finitely many gaps at least g, some N would satisfy x_{n+1}−x_n<g for every n≥N. Summing gives x_n≤x_N+(n−N)g for n>N. Combined with the lower bound this implies

n/(2M)≤x_N−Ng+1

for all n>N, an impossibility. Thus the set S={n:x_{n+1}−x_n≥g} is infinite and unbounded.

Fix n∈S and put h_n=H−b_n. Every future coordinate is at least x_n+g. Partition [x_n+g,∞) into the half-open intervals

I_k=[x_n+g+k,x_n+g+k+1),  k=0,1,2,….

Each contains at most M coordinates. For x_j∈I_k, x_j−x_n≥g+k and 0<b_j−b_n≤h_n. Dropping the nonnegative squared height difference from the denominator yields

0≤U_n≤2h_n M Σ_{k≥0}(g+k)^{-2}
≤2h_n M(g^{-2}+2).                                      (1)

For the last inequality, Σ_{k≥1}(g+k)^{-2}≤Σ_{k≥1}k^{-2}≤2, the latter following by comparison of the terms k≥2 with the integral of t^{-2} over [1,∞). Apply the interval bounds first to finitely many bins and then take the increasing limit; thus no unproved interchange of limits is involved.

Lemma 74 also gives

0≤V_n≤2HΣ_{j>n}x_j^{-2}→0.                              (2)

As n tends to infinity through S, h_n→0. Equations (1) and (2) prove E_f(w_n)→0 on S. Nonnegativity then gives the asserted lower limit over all indices. ∎

## Qualifications

The uniform local count is an additional hypothesis, not a consequence of reciprocal-square summability. For example, placing k distinct coordinates inside [2^k,2^k+1/4) gives finite reciprocal-square sum, bounded by Σ k4^{-k}, but unbounded unit-interval counts. Strictly increasing heights tending to H can be assigned to their ordered enumeration. Thus the proof does not settle the unrestricted monotone class.

Arbitrarily small gaps are compatible with the additional hypothesis: the coordinates 3k and 3k+2^{-k}, k≥1, have at most two points in every unit interval. The result supplies a subsequence, not full convergence at every index, and does not impose a quadratic-penalty selection rule. No theta-specific local count bound, signed-motion estimate, or RH assertion is proved.

## Verification and formalization obligations

The proof is analytic; no numerical certificate is required. Formalization would require the half-open interval counting bound, the contradiction between the two linear growth rates, enumeration of the unbounded set S, the nonnegative binwise infinite-sum estimate, and the subsequence limit. The only reused mathematical input is Lemma 74's zero-set identification and reflected-sum bound. The full right-hand tail is bounded directly here.
