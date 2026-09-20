# Lemma 32: polynomial detection of a nonreal summable node

**Hypotheses.** (β_j) is a finite or countable sequence of nonzero complex numbers, invariant under conjugation including multiplicity, with Σ_j|β_j|<∞. Suppose a nonreal node w occurs.

**Conclusion.** There is a polynomial q with real coefficients for which Σ_jβ_j²q(β_j)²<0. Consequently all these real polynomial forms are nonnegative if and only if all nodes β_j are real.

**Proof.** Put r=|w|/2 and let E be the finite set of distinct nodes of modulus at least r. Finiteness follows from summability; conjugation invariance makes E conjugation-invariant. Both w and conj(w) belong to E and have the same finite multiplicity μ≥1. For v∈E let

L_v(X)=Π_{a∈E, a≠v}(X-a)/(v-a).

Then L_v(a) is 1 at a=v and 0 at the other nodes in E. The coefficients of L_conj(w) are conjugates of those of L_w. For each integer N≥1 define

q_N(X)=(i/w)(X/w)^N L_w(X) -(i/conj(w))(X/conj(w))^N L_conj(w)(X).

Writing A_N(X)=(i/w)(X/w)^N L_w(X), the second displayed term is the coefficientwise conjugate of A_N. Hence q_N=A_N+conj(A_N) has real coefficients; this is coefficient conjugation, not evaluation conjugation. It equals i/w at w, -i/conj(w) at conj(w), and 0 at every other node in E. Thus the contribution to the form from nodes in E, with multiplicity, is -2μ.

Fix M=max_{|X|≤r} max(|L_w(X)|,|L_conj(w)(X)|), finite by continuity on the closed disk, and C=2M/|w|. Both E and these constants are independent of N. On |X|≤r the triangle inequality gives |q_N(X)|≤C(r/|w|)^N=C2^{-N}. Put T=Σ_{|β_j|<r}|β_j|²<∞: indeed B=Σ_j|β_j| bounds every |β_j|, so Σ_j|β_j|²≤B². The tail R_N of the form therefore satisfies |R_N|≤C²T4^{-N}. The finite head and this bound prove absolute convergence for each N. Conjugation invariance with multiplicity then makes the whole sum real, so Q(q_N)=-2μ+R_N≤-2μ+C²T4^{-N}. Choose any integer N≥1 with C²T4^{-N}<μ (automatic if T=0). This gives Q(q_N)<-μ<0, strictly stronger than the needed negative threshold. The interpolation uses distinct nodes, while μ and T count multiplicities; every nonzero node has finite multiplicity by summability. Conversely, if all β_j are real, each β_j²q(β_j)² is nonnegative, proving the final equivalence. ∎

The degree of this witness is at most N+|E|-1. This is a bound for a fixed hypothesized nonreal node and the entire fixed multiset, not a uniform cutoff for unknown nodes: E, C, T and the necessary N depend on them. The proof therefore gives no finite-test stopping rule for the actual Ξ matrices and no unconditional positivity assertion.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
