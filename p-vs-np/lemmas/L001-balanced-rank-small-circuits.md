# L001 — Exponential rank at every balanced split is compatible with small circuits

## Hypotheses

Let n = 2m ≥ 16. For a simple undirected graph G on the labeled vertices {1,…,n}, define the Boolean function

q_G(x) = ⊕_{ {i,j} ∈ E(G) } (x_i ∧ x_j).

The XOR is addition in F₂. For each partition A ⊔ B = {1,…,n} with |A| = |B| = m, define the real 0/1 communication matrix

M_{G,A,B}(a,b) = q_G(a,b),    a ∈ {0,1}^A, b ∈ {0,1}^B.

A residual function at this split is the row function b ↦ q_G(a,b) for a fixed a. Circuits use fan-in-two AND/OR, fan-in-one NOT, and unrestricted fan-out. Matrix ranks are over R except where F₂ is explicitly specified.

## Conclusion

There exists G such that **every** balanced split satisfies

rank_R M_{G,A,B} ≥ 2^(floor(n/8)+1) − 1.

The number of distinct residual functions is at least that large at each split. Nevertheless, q_G has a circuit of size at most 5·binom(n,2).

Moreover there is a fixed CNF template for each G, with n varying unit-clause signs t ∈ {0,1}^n, producing formulas Φ_{G,t} of length N_G = O(n² log n) such that

Φ_{G,t} is satisfiable iff q_G(t) = 1.

Thus the SAT decision function on these n free encoding bits has exponential rank at every balanced split, but polynomial-size circuits. The conclusion concerns all balanced partitions of those **free** bits, not partitions of all bits of an unrestricted SAT input.

The graph choice is existential; no polynomial-time construction of a sequence n ↦ G_n is asserted. Evaluation and the encoding are polynomial-time when G is supplied. The existence statement already refutes an unrestricted circuit-size criterion based solely on superpolynomial split rank, even when the rank is minimized over balanced splits.

## Proof

**A graph with large binary cut ranks.** Choose each of the binom(2m,2) edges independently with probability 1/2. For a fixed balanced partition, its cross-adjacency matrix H ∈ F₂^(m×m) has independent unbiased entries. Symmetry of the full adjacency matrix imposes no equalities between distinct entries in this one cross block.

Put r = floor(m/4). Every binary m-by-m matrix of rank at most r factors as UV with U of shape m-by-r and V of shape r-by-m: choose a basis of its column space, express its columns in that basis, and pad unused basis positions with zeros. There are at most 2^(2mr) pairs (U,V). Therefore

Pr(rank_F₂ H ≤ r) ≤ 2^(2mr−m²).

There are at most 2^(2m) choices of A. A union bound, which does not require independence between cuts, gives

Pr(some balanced cut has rank ≤ r)
  ≤ 2^(2m+2mr−m²)
  ≤ 2^(2m−m²/2)
  < 1                 (m ≥ 8).

So a graph exists with binary rank k ≥ r+1 at every balanced cut. Fix one such graph.

**From binary cut rank to real function rank.** Fix a cut and write its function over F₂ as

q_G(a,b) = q_A(a) + q_B(b) + aᵀHb,

where q_A and q_B contain the edges internal to their respective parts. Let K(a,b) = (−1)^(aᵀHb), a real sign matrix. Its row at a is the Boolean character b ↦ (−1)^((Hᵀa)·b). The image of Hᵀ has 2^k elements. Distinct characters are orthogonal over R: for u ≠ v, choose a coordinate where u+v is 1 and pair each b with the vector obtained by flipping that coordinate. Their contributions to Σ_b (−1)^((u+v)·b) cancel. Each character has squared norm 2^m. Thus the 2^k distinct rows are linearly independent and span all rows, proving rank_R K = 2^k.

Let S(a,b) = (−1)^(q_G(a,b)). Multiplying row a of K by (−1)^(q_A(a)) and column b by (−1)^(q_B(b)) gives S. These are invertible diagonal scalings, so rank_R S = 2^k. With J the all-ones matrix, M = (J−S)/2. Since S = J−2M and rank J = 1, subadditivity of rank gives

rank_R M ≥ rank_R S − 1 = 2^k−1 ≥ 2^(r+1)−1.

The span of the rows has dimension at most their number of distinct values, proving the residual-count assertion. This argument explicitly separates binary adjacency rank from real Boolean-function rank; they are not identified.

**Small unrestricted circuits.** Write e = |E(G)|. The positive cut ranks ensure e ≥ 1. Compute each edge product with one AND gate. Combine these e bits by e−1 two-input XOR operations. Each XOR has the four-gate implementation

u ⊕ v = (u ∨ v) ∧ ¬(u ∧ v).

The resulting circuit has e + 4(e−1) ≤ 5·binom(n,2) gates. Its gate list can be generated from the adjacency matrix of G in polynomial time. This also gives polynomial-time evaluation from (G,t), without needing to discover G from n.

**Embedding as a SAT slice.** Give every input and every gate output its own propositional variable. For a gate output z, impose its equivalence to its inputs u,v with the following clauses:

- z = u ∧ v: (¬z ∨ u), (¬z ∨ v), (z ∨ ¬u ∨ ¬v).
- z = u ∨ v: (z ∨ ¬u), (z ∨ ¬v), (¬z ∨ u ∨ v).
- z = ¬u: (¬z ∨ ¬u), (z ∨ u).

For fixed u,v these clauses force exactly the indicated value of z, as each displayed equivalence can be checked for the possible input bits. Append a positive unit clause for the circuit output. Finally, for each input x_i append the unit clause x_i if t_i = 1 and ¬x_i if t_i = 0. This is Φ_{G,t}.

If q_G(t) = 1, actual gate evaluations extend the fixed input assignment to a satisfying assignment. Conversely, any satisfying assignment has inputs t, and induction along a topological ordering forces every gate variable to equal its computed value. The output unit clause then forces q_G(t) = 1. This proves equisatisfiability in both directions; existential gate variables cannot conceal an inconsistent computation.

There are O(n²) variables and clauses, each clause has width at most three, and each variable index takes O(log n) bits. Use an explicit encoding with a sign bit even for positive literals. Its fixed skeleton has length N_G = O(n² log n), independent of t. Only the n signs of the input unit clauses vary. Restricting SAT to this skeleton therefore gives exactly q_G, with the same split matrices, while the circuit above computes its answer on the varying bits. If viewed as a circuit on the whole fixed-length encoding slice, all other coordinates can simply be ignored under this restriction.

**Threshold and scope.** The achieved rank is at least 2^(n/8)−1; it exceeds N_G^d for every fixed d at all sufficiently large even n, since N_G ≤ C n² log n. Yet the slice circuit has O(n²), hence polynomially many, gates. In particular, no universal bound rank ≤ poly(n, circuit size), nor the implication “superpolynomial minimum balanced rank forces superpolynomial circuit size,” is valid for general Boolean circuits. The same counterexample applies to raw residual counts. It does not rule out a different measure with additional hypotheses proved to be preserved by general computation. It supplies neither a SAT algorithm on arbitrary inputs nor a lower bound against every polynomial-time SAT decider.

Supplementary finite verification: `python3 scripts/balanced-rank/check_small_cases.py` checks all 530 binary square matrices of widths 1–3 using exact rational elimination for the sign-rank identity and the 0/1-rank inequality, including internal quadratic row/column signs. It also exhausts the 20 gate-equivalence valuations and four XOR inputs. All checks passed on 2026-09-24. They check small algebraic and encoding cases; the general existence and complexity claims rest on the proof above.

## Mathlib

Coverage: **not checked** for this full statement or its supporting finite-field, matrix-rank, character-orthogonality, circuit, and CNF-encoding facts. No absence claim or unverified theorem identifier is asserted. The proof is self-contained and does not depend on a Mathlib lookup.
