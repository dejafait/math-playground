# Longer dictionary calculation checkpoint

9 November 2026. Approved target and prior SPECIALIZE coverage:
drafts/literature/2026-11-09-longer-arithmetic-dictionary-test.md.

Keep exactly L637's fixed w,u0,psi,g,Z and N=floor(T^(1/5)).
Use L737's full form F_A, finite inequality F_A>=(A-4log N)Q,
and local numerator (14), with audited L926 at epsilon=1/4.
L925 is not an input. The changed-length source comparison covers
BCR with fixed padded exponent theta=1/4 at the three comparable scales.

Calculation: padded raw remainder has exponent 9/16+eta; take
eta=1/80, obtaining 23/40. Restoring B^2<=N||c||_2^2 gives
C N T^(23/40)||c||_2^2. The full-form margin is at least
L/5-C0>=L/10, and Q>=a_(1/4)N^(-1/4)||c||_2^2.
Thus error divided by T L N^(-1/4)||c||_2^2 is bounded by
C N^(5/4)T^(-17/40)/L<=C T^(-7/40)/L ->0.
Retaining half the main margin gives norm squared at least
(a_(1/4)/20)T L N^(-1/4)||c||_2^2.
L737(14) then gives projection squared <=C N^(5/4)/(sqrt(T)L^2)
<=C T^(-1/4)/L^2. All constants and onsets must be uniform in X,c;
that follows from the existing weight-family/coefficient normalization
audit, not from assuming a pointwise big-O is uniformly bounded.

This records the reasoning before canonical completion. The full proof
is to be saved in L927. It is a source-covered analytic specialization,
not a new moment or conditioning theorem. It extends a fixed-dictionary
realization obstruction; signed transfer and actual-Xi positivity remain
independent gaps. Existing route stops and unfinished work are preserved.

Completion: the full argument is now canonical in
lemmas/L927-longer-arithmetic-multiplier-bump-projection.md. The working
calculation above is retained as the pre-completion checkpoint.
