# Lemma 7: nonvanishing on Re(s)=1

**Hypotheses.** t∈R and t≠0.

**Conclusion.** ζ(1+it)≠0.

**Proof.** Suppose ζ has a zero of order m≥1 at 1+it. Such an order is finite: ζ is holomorphic there, is not identically zero by Lemma 1, and the identity theorem applies. Put h=σ-1>0. The simple pole at 1 gives |ζ(1+h)|≤C_0/h for sufficiently small h. The Taylor factorization at 1+it gives |ζ(1+h+it)|≤C_1 h^m. Since t≠0 implies 1+2it≠1, holomorphicity at 1+2it gives |ζ(1+h+2it)|≤C_2. Choose a common sufficiently small interval of h on which all three bounds hold. Lemma 6 then yields

1 ≤ ζ(1+h)³|ζ(1+h+it)|⁴|ζ(1+h+2it)| ≤ C_0³C_1⁴C_2 h^{4m-3}.

The right side tends to zero, since 4m-3≥1, a contradiction. No boundary limit of the prime sum was taken: only the already-proved inequality for h>0 and finite local Taylor/Laurent estimates were used. ∎
