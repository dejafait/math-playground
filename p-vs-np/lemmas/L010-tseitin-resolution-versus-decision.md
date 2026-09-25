# L010 — Exponential resolution length with polynomial-time parity decision

## Hypotheses

Use ordinary explicit binary CNF encoding. Resolution size means the minimum number of clauses in a refutation using resolution and weakening, with arbitrary reuse of earlier clauses and no extension axioms. Its precise width inputs are in [the standard theorem note](../foundations/04-resolution-width-theorems.md).

For a simple connected graph G=(V,E) and charges χ:V→F₂, put one variable x_e on each edge. At v impose

⊕_{e incident with v} x_e = χ(v).

Write T(G,χ) for the CNF obtained by forbidding each local assignment of the wrong parity. A forbidden tuple a contributes the clause with literal x_e when a_e=0 and literal ¬x_e when a_e=1. There are no auxiliary variables.

## Conclusion

For every n≥4 there exists a connected simple graph G_n on n vertices with degrees between 2 and 26 and at least n/12 crossing edges in every cut with both sides of size at least n/3. For every charge vector χ:

1. T(G_n,χ) is satisfiable exactly when ⊕_v χ(v)=0. It has m≤13n variables, at most 2²⁵n clauses, width at most 26, and binary length N=Θ(n log n) using consecutive variable indices.
2. For odd χ, every resolution refutation has size at least exp(cn)=2^{Ω(N/log N)}, for one absolute c>0 and all sufficiently large n.
3. There is one total deterministic SAT decider A and one polynomial Q such that A takes at most Q(N) steps on every T(G_n,χ), for both even and odd charges. It needs only the CNF, with no supplied graph, promise, advice, or expansion certificate. Its running time outside a recognized parity class need not be polynomial.

Thus minimum resolution refutation size does not polynomially bound below the running time of an unrestricted SAT decider on these inputs. This does not establish SAT∈P or any complexity-class separation. The graph sequence need not be efficiently generated.

## Proof

**A bounded-degree graph with large balanced cuts.** On [n], take a fixed Hamilton cycle and twelve independent uniform permutations π₁,…,π₁₂. Add undirected edges {v,π_i(v)}, discard loops, and merge repeated edges. Each permutation adds at most two incident edges at a vertex, so the resulting simple connected graph has 2≤deg(v)≤26.

For fixed disjoint A,B⊆[n] with |A|≥n/4 and |B|≥n/3, the probability that one permutation maps no element of A into B is

((n−|B|)_{|A|})/(n_{|A|}) ≤ (1−|B|/n)^{|A|} ≤ (2/3)^{n/4},

where (t)_r is the falling factorial; the probability is zero if t<r. Each factor (n−|B|−j)/(n−j) is at most (n−|B|)/n. Independence of the twelve permutations bounds the probability of no edge directed from A into B by (2/3)^{3n}. There are at most 3^n disjoint ordered pairs (A,B), by assigning each vertex to A, B, or neither. A union bound gives a failure probability at most

3^n (2/3)^{3n} = (8/9)^n < 1.

Choose a tuple for which every such pair has an edge. Discarding loops and merging parallel copies preserve the existence of an edge between disjoint sets, and the cycle can only add edges.

Suppose n/3≤|S|≤2n/3 and fewer than n/12 edges cross from S to its complement. Remove from S every endpoint on the S side of a crossing edge, obtaining A with |A|>n/4. Take B=V\S, of size at least n/3. There is no edge between A and B, a contradiction. Hence e(G_n)≥n/12. Finite enumeration could select a suitable tuple for each n; no polynomial construction time is claimed or used by the decider below.

**CNF equivalence, length, and both outcomes.** A clause associated with a local tuple a is false exactly on a, so the clauses at v enforce exactly its parity equation. A vertex of degree d contributes 2^{d−1} clauses of width d. The Hamilton cycle ensures m≥n, while the degree bound gives m≤13n. Thus there are between 2n and 2²⁵n clauses. With fixed-width binary indices of length ceil(log₂(m+1)), signs, and separators, N=Θ(n log n). The upper estimate also holds for ordinary self-delimiting binary indices; the constants may be large but are fixed independently of n and χ.

Summing all vertex equations over F₂ cancels every edge twice, so odd total charge is inconsistent. Conversely, fix a spanning tree of G and set every non-tree edge to zero. Repeatedly remove a non-root leaf v: set its remaining tree edge to the residual charge at v, and add that charge to its parent's residual charge. This satisfies the removed equation. At the root the remaining residual is the original total charge, because each elimination preserves the sum of the remaining residuals. Even total charge therefore gives a satisfying assignment. In particular, the comparison covers both satisfiable and unsatisfiable formulas, not just an always-negative promise.

**Recovering the equations from the CNF alone.** The following preprocessing applies to an arbitrary input CNF. First normalize clauses, deleting repeated literals, tautological clauses, and duplicate clauses; an empty clause immediately certifies unsatisfiability. Group the remaining clauses by their sets of variables. Within a group of r≥1 variables, each clause forbids exactly one r-bit tuple, obtained from its signs. Accept the group as a parity block precisely when it contains 2^{r−1} distinct tuples and all those tuples have the same parity b. These conditions imply that the group forbids exactly the parity-b tuples, so it is equivalent to the equation with right-hand side 1−b. There is no need to enumerate missing tuples: their total number of either parity is exactly 2^{r−1}.

The tests are polynomial in the full input length: signs and supports are already written out, sorting costs polynomial time, and the integer 2^{r−1} needs only r bits. Rename distinct variable identifiers densely before constructing the matrix, so large binary variable labels do not increase its dimension beyond the input length. If every group passes, solve the recovered system by Gaussian elimination over F₂. Row swaps and row additions preserve its solution set; an inconsistent row 0=1 gives NO, and otherwise back-substitution with arbitrary free variables gives YES. The number of rows and columns is at most the input length, so the whole procedure has one polynomial Turing-machine bound. An empty conjunction returns YES.

Every T(G_n,χ) passes this test. Two different vertices of a simple graph have incident-edge sets intersecting in at most their one common edge. Since each vertex has degree at least two, their complete incident-edge sets cannot coincide. Hence grouping by support separates the vertex blocks exactly; it requires no recovery of the particular graph construction or verification of expansion.

Define A to run this preprocessing and elimination whenever they certify parity-block form, and otherwise exhaustively test all assignments to the variables appearing in the input. Reject malformed encodings. The equivalences above make its answers sound on every input, and the fallback makes it a total SAT decider. All family members use its polynomial branch. The fallback supplies no polynomial worst-case bound for arbitrary SAT.

**Resolution lower bound.** For odd χ, the two cited width theorems give, with one absolute K,

n/12 ≤ W(T(G_n,χ)) ≤ 26 + K sqrt(m ln S(T(G_n,χ))).

For n≥624, n/12−26≥n/24. Since m≤13n,

ln S(T(G_n,χ)) ≥ (n/24)²/(13K²n) = n/(7488K²).

This proves the asserted exponential lower bound with c=1/(7488K²). Because N=Θ(n log n), it is 2^{Ω(N/log N)} in binary input length, hence exceeds every fixed polynomial in N. It is not stated as 2^{Ω(N)}. The theorem concerns the original CNF without added extension definitions; algebraic preprocessing is part of unrestricted computation, not an allowed resolution inference.

**Required versus achieved threshold.** Let p_A be any fixed polynomial in N and A's running time on an input. For odd-charge family members, p_A(N,time_A(T(G_n,χ))) is polynomial in N, whereas the minimum resolution size is superpolynomial. Therefore a proposed universal simulation producing a resolution refutation of size at most p_A(N,time_A(F)) from every rejecting SAT computation is false, even allowing p_A to depend on the decider. A resolution proof producer must still pay for its long explicit output; arbitrary decision algorithms need not produce that proof. This refutes the stated instancewise simulation, not every possible global implication with premise SAT∈P. Establishing hardness for every SAT decider would require an additional valid model-transfer argument or a different measure. This lemma supplies neither such an argument nor a lower bound for stronger proof systems.

Supplementary verification: `python3 scripts/tseitin-resolution/check_small_cases.py` compares CNF evaluation, recovered-system elimination, and the graph charge criterion on small graphs with every charge vector. It also checks which subsets of a full-support clause set are recognized as complete parity blocks. On 2026-09-25, all 252 local valuations, 232 charge vectors on 13 graphs, and 256 clause subsets passed, including reordered clauses and large variable identifiers. Output is in `scripts/tseitin-resolution/small-cases.txt`. These checks address encoding and recognition, not the asymptotic resolution theorem or the graph existence proof.

## Mathlib

Coverage: **not checked** for the full statement or its finite-field, graph, and CNF support. No absence claim or unverified Mathlib identifier is made. The named external width theorems are supporting inputs; the graph construction, encoding, recognizer, and decision-time comparison are proved here. They are not a resolution of P versus NP.
