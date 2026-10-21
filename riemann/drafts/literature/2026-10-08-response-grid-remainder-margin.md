# Exact response-grid Riemann–Siegel margin test

TARGET: Test whether the full Riemann–Siegel sum at L372's exact G phase levels has a nonvanishing margin dominating its O(t^(-1/4)) remainder, using only the recorded carrier and Euler-log bounds.
CHECKED: 2026-10-08
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the exact-pair, Gram-grid and shifted-projection discovery and scoped duplicate checks in drafts/literature/2026-10-08-actual-common-zero-count-bound.md; no matching margin theorem established in inspected sources.
SOURCE_EVIDENCE: NIST DLMF 25.10.1–3 and full stated remainder read on 2026-10-08, version 1.2.8; Titchmarsh second edition (1986), §4.17, (4.17.2)/(4.17.4), p. 89, as cited there; exact L366 (1) and L372 (2)–(9) read; prior Lagarias/Li coverage reused.
COMPARISON: The unconditional Riemann–Siegel formula covers real positive heights with the exact moving cutoff; it supplies an additive remainder but no lower margin at the response grid. Fixed-angle moment and RH-dependent correlation theorems do not repair that difference.
GAP: Determine whether the recorded bounds can control the full signed finite sum at actual response phase levels strongly enough to exceed the remainder; no such estimate or certificate failure is asserted yet.
REASON: A bounded arithmetic sufficiency test is available with fully read scalar source coverage; direct count import has been parked. It retains the exact response grid and does not reopen generic geometry or the source-blocked discriminant mean.
SCOPE: L366's actual fixed F_0,G, real t tending to +infinity with G(t)=0, L372's continuous full phase, m=floor(sqrt(t/(2π))); no RH, F_0 simplicity, noncoincidence, D≤0, finite-height onset or arbitrary independent prime-phase substitution.

This ready assessment is newly written and requires separate supervisor
approval next turn before research. No formula has been specialized,
new inequality derived, or mathematical script run here.

The parent assessment records exact primary-source scope and failures.
The named scalar input is the unconditional Riemann–Siegel formula,
[DLMF 25.10.3](https://dlmf.nist.gov/25.10#E3), with the Hardy
phase conventions in 25.10.1–2 and R(t)=O(t^(−1/4)). Import it by
citation; do not reprove it. A later attempt must justify its phase
convention against Q and the extra b in L372. A change of continuous
gamma branch can change signs but cannot justify changing sample
heights. The Euler logarithm on Re s=5/2 must remain the actual one.
The full finite cosine sum and its moving cutoff are essential;
replacing it by its first term, a fixed-angle grid, or a modulus
square is not within coverage.

The concrete sufficient threshold sought is uniform growth of the
absolute full finite sum divided by t^(−1/4) along all sufficiently
large G zeros. This would exceed the unspecified remainder constant.
Alternatively a uniform explicit surplus against a justified remainder
constant would suffice. These are proposed tests, not derived results.
Any nonvanishing consequence would be stronger than the parent count
goal and potentially useful with L377/L378; actual D≤0 and the global
signed margin remain separate unresolved premises.

Continue only if the recorded phase/Euler bounds produce a genuine
uniform signed-sum margin. If they leave an uncontrolled critical-line
sum, or an absolute error of at least the prospective margin, record
the missing estimate and stop this certificate. Do not infer an actual
common zero, falsity of the count bound, or RH from such a failure.
Do not silently enlarge scope to a new sampling theorem or changed
arithmetic hypothesis. Save the reasoning in drafts before lengthy work;
no new lemma is required merely to record a failed certificate.

Expected completed classification for a later scalar specialization or
certificate audit: REPRODUCTION, with no novelty claim. Full matching
Mathlib coverage is not checked. Essential local inputs: L366 and L372;
L377/L378 are downstream context only. L371/L373 and L375/L376 remain
recorded obstructions; no cross-notebook input is used.
