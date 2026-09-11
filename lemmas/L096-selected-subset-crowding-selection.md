# Lemma 96: selected-subset crowding selection

**Hypotheses.** Assume the coordinates and heights of Lemma 94, and use
its suffix set S, near sums Q_n, blocks B_N and height increments D_N.
For each N in any set I of positive integers, choose a nonempty subset
F_N⊆B_N. Define

m_N=|F_N|, α_N=min_{n∈F_N} x_n/sqrt(n),
c_N=max_{r∈integers, N≤r<4N} Σ_{n∈F_N,n≤r}1/(r−n+1),
W_N=N c_N/(m_N α_N²).

**Conclusion.** For every N∈I,

(1/m_N)Σ_{n∈F_N}Q_n≤32 W_N D_N.                         (1)

There is a common increasing subsequence of indices in S along which
Q_n and the full paired-product upward contribution E_f(x_n+i b_n)
tend to zero if either W_N is bounded on an unbounded subset of I, or
Σ_{k≥0: 2^k∈I}1/W_(2^k)=∞.

## Proof

The finite expansion in Lemma 92 applies with the summation restricted
to F_N. Indeed, for n∈F_N and 1≤q≤n the suffix inequality gives

x_{n+q}−x_n≥α_N q/(4sqrt(N)).

With Δ_r=b_{r+1}−b_r, expanding b_{n+q}−b_n into its finite
increments and discarding the squared height difference gives

Σ_{n∈F_N}Q_n≤16N α_N^(-2) Σ_{r=N}^{4N−1}Δ_r
  Σ_{n∈F_N,n≤r} Σ_{1≤q≤n, q≥r−n+1} q^(-2).

The integral estimate Σ_{q=ℓ}^∞q^(-2)≤2/ℓ for integer ℓ≥1 bounds
the double coefficient by 2c_N. Telescoping proves (1). All increment
rearrangements are finite; the extended numerical series converges.

Every c_N≥1, by evaluating at a member of F_N; all W_N are finite
and positive. Along bounded-W blocks, D_N≤H−b_N→0 gives vanishing
averages. Pass to starts at least doubling and minimize Q on F_N to
obtain an increasing sequence. For the second criterion, the budget
Σ_k D_(2^k)≤2(H−b_1) from Lemma 91 implies
liminf_{k:2^k∈I} W_(2^k)D_(2^k)=0: a positive eventual lower bound
would force a divergent sum of D_(2^k). Choose increasing k with these
products tending to zero and minimize Q on their selected subsets.
The dyadic blocks are disjoint and ordered, so the indices increase.

Finally Lemma 84 supplies the product and the estimate for n∈S,

0≤E_f(x_n+i b_n)≤2Q_n+32HΣ_{j>2n}x_j^(-2)
                         +2HΣ_{j>n}x_j^(-2).

Both tails vanish on the same sequence, proving the assertion. ∎

## Qualifications and verification

Taking F_N=B_N recovers the criterion of Lemma 94. Subsets may depend
on the coordinates; the proof does not require a rule for finding them.
No claim that suitable subsets always exist is made. This is a generic
product result and supplies no theta-specific or RH conclusion.
The proof is analytic and needs no numerical certificate. Formalization
should check restricted separation, finite increment endpoints, the
harmonic tail estimate, positive finite maxima, the dyadic budget and
ordered minimizers, and convergence of both full-product tails.
