# Dyadic spike payoff — 2026-09-11

Inspected and preserved all existing changes; L111 is complete.
Candidate UNPROVED at this checkpoint: let
P(k)=1+Σ_{j≥1:2^j<k}1/j and F(k)=P(k)+1−1/(k+1).
The weighted sum Σ m_k F(k)/k² should converge since P(2^j)≤1+H_j.
For a spike l=2^j, P(l)−P(k)>0 requires k<2^(j−1),
so its contribution is a far-tail contribution. Baseline near increments
P(l)−P(k) for k<l≤2k are at most 2. The strictly increasing bounded
correction has increment (l−k)/((k+1)(l+1)); near spikes have uniformly
bounded contribution, while the far sum uses weighted integrability.

Resume: audit the boundary k=1 and strict spike-index inequality, count
near spikes, prove weighted integrability and the full uniform bound;
then save a lemma and apply L111's finite-cluster cutoff argument.
No summability-only theorem or RH conclusion is claimed.

Completed: Lemma 112 proves the candidate. Boundary correction to the
draft: P(2^j)−P(k)>0 can occur at k=2^(j−1), so the far range must
include l=2k. With near range k<l<2k the spike's P increment is zero.
The full bound is 8+4D. No claim for arbitrary summable counts is made.
