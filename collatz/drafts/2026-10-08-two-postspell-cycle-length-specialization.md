# Two-postspell cycle-length specialization — working record

Gate-approved target: Compare L039's N<4500 ceiling with a primary
published lower bound for the length of a positive nontrivial shortcut
cycle, checking primitive and represented counts.

Prior coverage: `drafts/literature/2026-10-08-two-postspell-cycle-length-comparison.md`
(SPECIALIZE, saved before invocation). Main gap: universal eventual
descent. Intermediate target: exclude the actual closed two-word language
of L039. Downstream use: remove this restricted cycle possibility without
assuming universal entry or excluding other cycles or divergence.
Continuation test: compatible positive nontrivial primitive cycle and
odd-count convention must give a lower threshold exceeding the ceiling;
a scope/count mismatch would abandon this comparison.

Saved reasoning before canonical write-up: L039 supplies represented
N<4500. L035 supplies K=3(J_1+J_2)+H_1+H_2, N=K+L and
primitive scaling N=rp, K=rK_0 with r>=1. The primitive orbit is positive
and nontrivial since it contains n>=47 outside {1,2}. Simons–de Weger,
Acta Arith. 117 (2005), Corollary 2, p. 53, gives K_0>225640000.
Thus 225640000<K_0<=K<=N<4500 is impossible. No global minimum is
identified with a junction. Both tails, x=n and repeated periods survive.
The source height and continued-fraction computations and L039's inherited
Rhin/source computations remain imports, not fresh certificates.

L031's already proved equivalence then excludes Delta>0 and Delta|C
for its entire parameter domain. This is a consequence of the same
language exclusion, not a new guard argument. Attempt 019 and history
069 remain valid for their distinct failed mechanisms. No numerical
enumeration, mathematical script, new general theorem or novelty claim
is needed. Full canonical proof will be L040; its separate audit remains
future work. Mathlib coverage is not checked.
