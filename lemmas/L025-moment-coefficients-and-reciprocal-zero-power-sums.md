# Lemma 25: moment coefficients and reciprocal-zero power sums

**Hypotheses.** α_j are the representatives in Lemma 24, and M_{2n} are as in Lemma 21. Define S_k=Σ_jα_j^{-2k} for integers k≥1.

**Conclusion.** All S_k converge absolutely and are real. In particular

S_1=M_2/(2M_0),

S_2=(3M_2²-M_0M_4)/(12M_0²).

If RH holds, then S_k≥0 for every k≥1, so M_0M_4≤3M_2² is a necessary consequence of RH. No sufficiency is claimed.

**Proof.** Because Ξ(0)≠0 and its zeros are isolated, there is a zero-free disk around 0; hence |α_j| have a positive lower bound. Lemma 24 then gives absolute summability of every even reciprocal power. For |z| smaller than half that lower bound, expand the paired logarithms. The sum of the absolute values of the full double series is bounded by a constant times |z|²Σ|α_j|^{-2}, so

log(Ξ(z)/M_0)=-Σ_{k≥1}S_k z^{2k}/k,

using the local analytic logarithm that is zero at 0. Conjugation symmetry makes the left side's Taylor coefficients real, proving S_k real. The moment expansion gives Ξ(z)/M_0=1-a z²+b z⁴+O(z⁶), where a=M_2/(2M_0) and b=M_4/(24M_0). Its logarithm is -a z²+(b-a²/2)z⁴+O(z⁶). Comparing coefficients proves the formulas. Under RH every α_j is real and nonzero by Lemma 18, so every term of each S_k is positive. The asserted nonnegative sign and the necessary moment inequality follow conditionally.

The unconditional Cauchy–Schwarz inequality in Lemma 21 gives M_2²≤M_0M_4, which is a lower bound and does not give the needed upper bound M_0M_4≤3M_2². ∎
