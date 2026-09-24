# Lemma 241: sparse tail levels and exclusion of the controlled peak sector

**Hypotheses.** Use the actual theta quantities ε_N, B_N=π(N+1)², E_N and F of L238–L239. For the last assertion let r_N be any positive strict maximum of F in [3B_N,4B_N] with κ_N=−F''(r_N)>0, whenever such a maximum exists.

**Conclusion.** The adjacent mass ratio satisfies

ε_(N+1)/ε_N = exp(−π(2N+3))(1+O(N^(−2))) → 0.

The positive strictly decreasing sequence ε_N therefore is not a relatively fine mesh near zero. More precisely, for h_N=√(ε_N ε_(N+1)),

inf_{M≥1} |ε_M−h_N|/h_N → 1.

At the hypothesized sector maxima put d_N=E_N(r_N)−F(r_N). For all sufficiently large N, d_N>0 and

d_N/κ_N ≥ c exp(B_N/2)

for an absolute c>0. In particular no sequence of these maxima meets L240's condition d_N/κ_N→0.

**Proof.** Apply L238's mass asymptotic at N and N+1. Since B_(N+1)−B_N=π(2N+3), division gives the first formula; both relative errors are O(N^(−2)), and division is legitimate for large N.

Strict decrease follows because the removed summand has strictly positive mass, as used in L238. Write q_N=ε_(N+1)/ε_N. For M≤N, ε_M/h_N≥q_N^(−1/2), and for M≥N+1, ε_M/h_N≤q_N^(1/2). Both endpoint values are attained, so the infimum in the conclusion equals

min(q_N^(−1/2)−1, 1−q_N^(1/2)) → 1.

This is a statement about tail masses, not an assertion that h_N are theta peak heights. At these hypothetical heights, even the first larger tail mass has relative excess q_N^(−1/2)−1→∞. Thus merely crossing a mass level by changing the integer cutoff does not imply small relative excess.

For the sector assertion, L238 gives E_N(r)/ε_N=p(r/B_N)+O(B_N^(−1)) uniformly on [3B_N,4B_N], where p≥1/5. L239 gives |F(r)|/ε_N≤C exp(−B_N/2) and |F''(r)|/ε_N≤C exp(−B_N/2) uniformly on the same sector. (For j=2, divide its displayed bound by B_N².) Hence eventually d_N≥ε_N/10, while 0<κ_N≤C ε_N exp(−B_N/2). Dividing proves the stated lower bound with c=1/(10C), enlarging C to be positive if needed. No existence or count of these maxima is used. ∎

The sparse-mesh assertion alone does not exclude a special sequence of actual theta peak encounters: peak heights and curvature could be correlated with the cutoffs. The sector assertion does exclude the sufficient L240 window in the region controlled by L239. Elsewhere the exponential upper bounds supply neither a lower bound on peak curvature nor a relative peak-height encounter estimate. Neither assertion settles a_N^*→0, and neither proves a nonvanishing lower bound for that threshold. Higher-order positivity is still missing.

**Mathlib.** Not checked for the full statement or supporting asymptotic and geometric-mean results. No matching theorem is claimed. General documentation: https://leanprover-community.github.io/mathlib4_docs/
