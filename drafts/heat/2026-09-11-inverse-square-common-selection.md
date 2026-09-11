# Inverse-square common selection — 2026-09-11

Checkpoint: prior Lemma 103 is complete; no earlier work is discarded.
For a fixed infinite A⊆P, conjectured exact condition is sup_A K_s<∞.
Sufficiency: U_s≤2(H−b_s)K_s and the reflected tail vanishes.

Necessity proof draft: write F_s(t)=Σ_{j>s}t/(d_j²+t²).
If 0<ε≤1/2 and F_s(ε)<1, each term gives d_j²>ε−ε²,
hence K_s≤F_s(ε)/(ε(1−ε))<2/ε. Thus arbitrarily large K
allows a root F_s(δ)=1 with δ≤ε. Select increasing marked indices
n_l in A with K>2/ε_l, ε_l≤2^(−l), and ε_l≤δ_(l−1)/4.
Continuity at zero follows by domination using finite K_s.
Place a jump δ_l at n_l. Future marked jumps total at most δ_l/3.
Use positive background increments 2^(−r) min({1}∪{δ_l:n_l≤r});
the background tail from n_l is at most δ_l. All subsequent height
differences from n_l lie between δ_l and 3δ_l, so U_(n_l)≥2/9.

Resume: audit finiteness of K, quantifiers, background and tail bounds;
then save canonical lemma and graph, history, progress, run validator.
These draft claims are not DAG inputs until the proof audit is complete.

Completed: audited and stored as Lemma 104. The draft resume instruction
above is historical; the current next action is in PROGRESS.md.
