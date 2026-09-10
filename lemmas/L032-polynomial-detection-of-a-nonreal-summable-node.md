# Lemma 32: polynomial detection of a nonreal summable node

**Hypotheses.** (β_j) is a finite or countable sequence of nonzero complex numbers, invariant under conjugation including multiplicity, with Σ_j|β_j|<∞. Suppose a nonreal node w occurs.

**Conclusion.** There is a polynomial q with real coefficients for which Σ_jβ_j²q(β_j)²<0. Consequently all these real polynomial forms are nonnegative if and only if all nodes β_j are real.

**Proof.** Put r=|w|/2 and let E be the finite set of distinct nodes of modulus at least r. Finiteness follows from summability; conjugation invariance makes E conjugation-invariant. Both w and conj(w) belong to E and have the same finite multiplicity μ≥1. For v∈E let

L_v(X)=Π_{a∈E, a≠v}(X-a)/(v-a).

Then L_v(a) is 1 at a=v and 0 at the other nodes in E. The coefficients of L_conj(w) are conjugates of those of L_w. For each integer N≥1 define

q_N(X)=(i/w)(X/w)^N L_w(X) -(i/conj(w))(X/conj(w))^N L_conj(w)(X).

Its coefficients are real. It equals i/w at w, -i/conj(w) at conj(w), and 0 at every other node in E. Thus the contribution to the form from nodes in E, with multiplicity, is -2μ.

On |X|≤r, the fixed polynomials L_w and L_conj(w) are bounded. Therefore there is C independent of N such that |q_N(X)|≤C(r/|w|)^N=C2^{-N}. The remaining nodes have modulus <r and satisfy Σ|β_j|²<∞ (boundedness plus the original summability). The absolute value of their total contribution is at most C²4^{-N}Σ_{|β_j|<r}|β_j|², tending to zero. The whole form is real by conjugation and absolute convergence. For sufficiently large N it is negative. Conversely, if all β_j are real, each β_j²q(β_j)² is nonnegative, proving the final equivalence. ∎
