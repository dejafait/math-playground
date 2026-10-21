# Same-boundary joint parameter attempt — working record

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-07-two-postspell-joint-odd-parameter-bound.md`.
The approved target is explicit absolute A,B with
4J_i+H_i<=A log(N)+B at one index of every actual closed two-postspell
word, with independent tails and repeated periods retained.

Main gap: universal eventual descent. Plausible downstream use: organize
asymmetric integer-closure cases using the entire odd-growth portion
of one word. Continue only with explicit constants at the same index;
abandon unsupported height comparisons or separately chosen minima.

Saved intermediate reasoning before final write-up: choose b=min(n,x)
and keep its own J,H. L035 and published Simons–de Weger Lemma 12
give b<(46/11) exp(13.3*0.46057) K^13.3. L031 gives
11b+23>=4*16^J and 2^H<=y+1, where its equation (4) gives
y+1=(27/16)^J(b+23/11)-12/11. Thus putting s=b+23/11,
4J log2<=log s+log(11/4), and
(4J+H)log2<J log27+log s. These inequalities use one word only.

Proposed exact simplification for canonical proof: b>=47; log s is
less than 13.3 log K+8, using 13.3*0.46057<25/4,
log(46/11)<3/2 and log(1+23/(11b))<1/20. With log2>2/3
and log3<4/3, the coefficient of log s is less than 15/4 and
the remaining constant less than 3. Hence A=50,B=33 should suffice.
All strict signs, rational exponential-series comparisons and scope
remain to be written in the canonical lemma. No numerical script needed.

Independent gaps remain: other-word asymmetry, tails and total N,
positive integer closure exclusion, entry into this language, other
cycles, divergence and universal eventual descent. Attempt 019's
guard-only stop and history 069's full-minimum-count mismatch remain
intact. No original transcendence proof or source computation is attempted.

Final outcome: the canonical proof in L037 establishes the proposed
A=50,B=33 with exact constants. This working record preserves the
preliminary reasoning; L037 is the proof authority. Separate critical
audit coverage is REVIEW_REQUIRED, and no complete candidate is claimed.
