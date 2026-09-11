# Increment-sensitive suffix bound — 2026-09-11

Scoped calculation: use the hypotheses and suffix set S of Lemma 84.
Its horizontal near-gap estimate gives

U_near(n) ≤ (18 n²/x_n²) Σ_{k=1}^n (b_{n+k}−b_n)/k².

Writing Δ_r=b_{r+1}−b_r and rearranging this finite sum yields
Σ_{r=n}^{2n−1} Δ_r Σ_{k=r−n+1}^n k^{-2}, bounded above by
2 Σ_{r=n}^{2n−1} Δ_r/(r−n+1). This retains actual increments.
If Δ_r ≤ C/[r log(r+1)] eventually, the last weighted sum is
≤ C(1+log n)/[n log(n+1)]. Multiplication by n²/x_n² then
vanishes because n/x_n²→0. Far and reflected tails are already
uniformly controlled in Lemma 84. Candidate result: convergence of
the full upward sum through all of S under this increment condition.

Checkpoint before full proof: candidate not yet promoted. Verify finite
rearrangement endpoints, the factor 2, and uniform harmonic/log ratio;
write Lemma 86 if correct. Include a slow-height example outside Lemma
84's sufficient condition to establish that the scoped extension is
substantive. General summable positive increments remain UNPROVED;
this computation does not settle the requested rate-free assertion.

Completed audit: finite rearrangement and constants are valid. The scoped
result is now proved in `lemmas/L086-increment-sensitive-upward-bound-at-suffix-minima.md`.
Its example uses Lemma 85's sequences, where the old sufficient factor
diverges but the new increment condition holds. The rate-free assertion
remains unproved; this draft's candidate is superseded by that proof.
