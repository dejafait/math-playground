# Draft: arbitrary summable lacunary masses — 2026-09-11

Scoped target: m_k=1 plus arbitrary nonnegative integer masses M_j at
integers n_j with n_(j+1)>=2n_j and Σ M_j/n_j² finite.
Choose increasing indices J_h with Σ_(j>J_h) M_j/n_j² <=2^-h.
Put P(k)=1+Σ_h 1_(n_(J_h)<k). It is unbounded but only jumps just
after selected spikes. At any spike l in (k,2k), P(l)=P(k).
Add B(k)=1-1/(k+1). Near baseline increment <=2, near extra
contribution <=2A, A=Σ M_j/n_j². Far generator <=4D.
Weighted integrability: extra part of P is A+Σ_h tail(J_h);
baseline P(k)<=2+log_2 k. These are nonnegative sum identities.

Checkpoint: construction and estimates drafted, not yet promoted.
Resume by auditing n_1=1, l=2k far boundary, threshold strictness,
and cutoff applicability. General nonlacunary supports remain unproved.

Audit completed: the result is stored in Lemma 113. The unit-baseline
near contribution is at most 4, extra near contribution at most 2A,
and the far contribution at most 4D. Boundary n_1=1 is harmless;
l=2k is assigned to the far range. This draft is retained as the
intermediate checkpoint, not an additional source of proved inputs.
