# Lemma 41: a certified positive H_2 test

**Hypotheses.** The arithmetic contracts of Lemma 37 hold. H_2=(S_{m+n+2})_{0≤m,n≤2} for the actual Ξ zeros.

**Conclusion.** H_2 is positive definite, and its determinant D_2 satisfies

3.10·10^{-31} < D_2 < 3.14·10^{-31}.

This is another finite computer-assisted partial result, not an all-degree positivity theorem.

**Proof/certificate.** The separate script `scripts/hankel/certify_hankel_next.py` imports the already inspected interval and Taylor operations from `scripts/hankel/certify_hankel.py`, integrates moments through M_12, uses E_6 from Lemma 39, and computes S_1,…,S_6 with the recurrence of Lemma 40. Run:

`python3 -B scripts/hankel/certify_hankel_next.py --panels 128 > scripts/hankel/hankel-h2-128.json`

The saved exact decimal interval endpoints give the following looser rational enclosures for the three leading principal minors:

- 0.00003717259927 < S_2 < 0.00003717259930;
- 3.86048·10^{-15} < S_2S_4-S_3² < 3.86050·10^{-15};
- 3.10·10^{-31} < D_2 < 3.14·10^{-31}.

Every lower endpoint is positive. The finite Taylor enclosure, the higher-moment tails, and the interval recurrence are justified by Lemmas 36–40. Thus the true three leading minors are positive and Lemma 40 proves positive definiteness. No extra panel refinement was needed at this degree. ∎
