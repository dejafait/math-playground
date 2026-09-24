# Forward jump reduction — 2026-09-11

Inspected existing modifications and the completed Lemma 106 checkpoint;
no interrupted proof was found and earlier work is preserved.

Scoped question: can failure of height-dependent upward selection be
reduced to finite-time escape of a coordinate-only forward jump process?
Draft claim, unproved at this checkpoint: put a_nj=(x_j-x_n)^(-2),
K_n=sum_{j>n}a_nj, and use transition probabilities a_nj/K_n.
If the actual upward sums are eventually at least epsilon, then
L b(n)=sum a_nj(b_j-b_n) >= epsilon/4 eventually (the reflected
sum tends to zero). Along the embedded chain Y_m, the conditional
expected height increment is L b(Y_m)/K_(Y_m). Telescoping the bounded
heights should bound E sum_m 1/K_(Y_m). Independent unit exponential
variables divided by K_(Y_m) then give an almost surely finite lifetime.
All K_n are positive and finite by Lemma 106. Y_m increases at least
by one, so this is escape to infinity, not accumulation at a finite index.

Resume: audit conditional expectations and nonnegative limits; formulate
only the necessary escape condition and its sufficient nonescape
contrapositive. Do not claim summability prevents escape without a proof.

Completed scoped reduction: the conditional-expectation and lifetime
audit is stored in Lemma 107. The earlier draft claim is proved there.
The universal nonexplosion assertion remains explicitly unproved;
PROGRESS.md records the next action. No counterexample was constructed.
