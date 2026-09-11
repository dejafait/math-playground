# Lemma 163: restricted triple-product diagonal

**Hypotheses.** Fix 0<a<b. Let N≥max(1,1/b), let I be the positive
integers in [aN,bN], and let nonnegative amplitudes satisfy
A_n≤K N^(−1/2). Define D3 as in L162.

**Conclusion.** There is a constant C_(a,b,K) such that

D3≤C_(a,b,K)(1+log N)^4.                                 (1)

Consequently, in the Gaussian window of L156, uniformly for T≤t≤2T,
the mass W of L162 satisfies

0≤W≤D3≤C_(a,b)(1+log T)^4.                               (2)

For the cutoff of L162 its bound (3) therefore holds with exponent four
in place of eight. This is not a bound uniform in T for fixed M.

**Proof.**

Let E be the number of ordered pairs of triples in I³ with equal
products. Expanding the square and bounding each of its six amplitudes
gives D3≤K^6 N^(−3) E.

Consider positive integer 3-by-3 matrices x=(x_ij) whose three row
products and three column products all belong to I. The map taking
these six products maps onto the equal-product pairs counted by E.
Indeed, for each prime dividing their common product, its three row
exponents and three column exponents have equal total. Allocate this
exponent mass by repeatedly assigning the minimum of an unfilled row
and column margin to their intersection and subtracting it. A positive
allocation exhausts at least one margin; zero margins are skipped.
This terminates with a nonnegative integer matrix having the specified
margins. Multiply the corresponding prime powers in each cell. Only
finitely many primes occur; common product one gives the all-one matrix.
Thus E is at most the number of these integer matrices. Injectivity is
not required.

For such a matrix put e_ij=floor(log2 x_ij)≥0. Each row product lies
in [2^(sum_j e_ij),2^(sum_j e_ij+3)), and likewise for columns. Therefore
all six exponent sums belong to the real interval

J=(log2(aN)−3, log2(bN)].

Its length is L=3+log2(b/a), independent of N. Each cell exponent is
at most B=floor(log2(bN)): other entries in its row are at least one.
Set H=ceil(L)+1, an upper bound for the number of integers in any
translate of J.

Choose e_11,e_12,e_21,e_22 first, in at most (B+1)^4 ways.
The first two row restrictions then give at most H choices each for
e_13,e_23. The first two column restrictions give at most H choices
each for e_31,e_32. The third row restriction gives at most H choices
for e_33. Nonnegativity, the bound B, and the remaining column
restriction can only decrease the count. Hence there are at most
(B+1)^4 H^5 admissible exponent boxes.

In a fixed box each x_ij ranges over exactly 2^e_ij integers before
imposing the margin restrictions. Their total number is 2^(sum_ij e_ij).
Since each row exponent sum is at most log2(bN), this number is at most
(bN)^3. Counting the boxes proves

E≤b³ N³ H^5(B+1)^4.

As B+1≤C_b(1+log N), this proves (1). All counts are finite;
no average divisor theorem or limiting interchange is used.

L156 supplies the amplitude bound in the Gaussian window with
N=sqrt(T/(2π)); L162 supplies 0≤W≤D3. These prove (2).
Finally χ''(Q/M) vanishes unless M<Q<2M. Multiplying (2) by its
supremum norm and integrating gives precisely

|E_T[χ''(Q/M)W]/(2M²)|
 ≤ C_(a,b)||χ''||∞ (1+log T)^4 P_T(M<Q<2M)/M².

This proves the stated cutoff consequence. ∎

## Scope and verification

The gain retains individual row and column factor bounds; merely
bounding the common product loses these constraints. Four freely
chosen exponents provide an upper bound, not a matching lower bound.
No optimality, cancellation with nonresonant terms, or fixed-cutoff tail
estimate is asserted. RH remains unproved.

The exact regression `python3 scripts/heat/check_restricted_triple.py`
checks the primewise construction for every equal-product pair of
triples in several small windows and checks all six output margins.
The proof of the bound for arbitrary N is the finite box count above.
Formalization would require prime factorization, integer transportation,
the dyadic partition, and this five-stage count of constrained exponents.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
