# Unrestricted cluster cutoff audit — 2026-09-11

Scoped target: remove m_k <= Ck from the separated-cluster consequence
of Lemma 111 using the payoff proved in Lemma 119. For points in
[k,k+1/4], set f(i)=F(cluster(i)). Internal increments vanish;
external distances are at least 3(l-k)/4, giving generator bound
(16/9) B_F. The finite absorbing cutoff from Lemma 111 then applies.

Checkpoint before final audit: verify full exit rates, finite transient
state set, capped-payoff direction, and convergence of exit times to the
original lifetime. No general-coordinate nonexplosion is proved here.
For arbitrary unit-cell clustering, neighboring-cell gaps have no
positive lower bound; the same comparison cannot be asserted.

Audit completed in Lemma 120: the separated-cluster conclusion holds
without a count envelope. Full tail exit rates and the original lifetime
coupling justify the cutoff. The arbitrary-coordinate extension remains
unproved; its adjacent-cell distance comparison has no uniform constant.
