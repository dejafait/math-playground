# Corollary 32a: an explicit RH-equivalent condition, not a proof of it

**Hypotheses.** The actual Ξ nodes β_j=α_j^{-2} and power sums S_k are as in Lemmas 24–25.

**Conclusion.** RH holds if and only if every finite Hankel matrix H_d=(S_{m+n+2})_{0≤m,n≤d} is positive semidefinite.

**Proof.** The node summability is Lemma 24, and conjugation invariance follows from Lemma 18 (squaring reciprocals makes the ± representative choice irrelevant). Lemmas 30 and 32 identify matrix positivity with all β_j being real. A real β_j could be negative only if α_j were purely imaginary: writing α=x+iy, real α² forces xy=0, and negative α² forces x=0. Lemma 26 excludes such α_j. Thus all β_j real here means all α_j real, which is RH by Lemma 18. The forward implication is already Lemma 30. ∎

### Unresolved requirement
 No argument in this write-up proves H_d positive semidefinite for every d. Corollary 32a is openly RH-equivalent and cannot be used as an unconditional positivity input. Lemma 27 proves only the scalar cases S_2,S_4,S_6>0 among its diagonal entries, not the mixed forms.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
