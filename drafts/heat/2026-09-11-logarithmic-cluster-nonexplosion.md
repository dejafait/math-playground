# Logarithmic cluster payoff — 2026-09-11

Inspected existing changes and the completed L109 checkpoint; no earlier
work was discarded or repeated. Candidate, initially UNPROVED: for
m_k≤M k/log(k+1)^2, use f(k)=sqrt(log(k+1)), constant inside each cluster.
The intercluster generator is at most (16/9) times
Σ_{l>k} m_l(f(l)−f(k))/(l−k)^2. For k<l≤2k, concavity gives
f(l)−f(k)≤(l−k)/(2(k+1)sqrt(log(k+1))) and
m_l≤2Mk/log(k+1)^2. The near sum is bounded by
M(1+log k)/log(k+1)^(5/2). For l>2k, the sum is bounded
by 4M Σ_{l>2k}1/(l log(l+1)^(3/2)), uniformly finite.

Resume checkpoint: audit concavity, the uniform near bound, the infinite
tail and integer count example, then apply the cluster cutoff proof with
exit payoff sqrt(log(R+1)). General summable counts remain unproved.

Completed audit: candidate proved and stored in Lemma 110. Both generator
ranges have explicit uniform bounds, the exit cap retains all rates,
and the logarithmic count example satisfies the count bound with M=1.
No unfinished claim from this scoped step is promoted beyond that lemma.
