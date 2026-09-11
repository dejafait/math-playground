# Lemma 87: sparse suffix minima obstruct increment-bound selection

**Hypotheses and construction.** Put N_0=0 and N_k=4^k for k≥1.
For the unique k with N_{k−1}<n≤N_k define

x_n²=k²(N_k+n)/2,   x_n>0.

Define positive increments by Δ_r=2^{−r}+k²/4^k if r=N_k for
some k≥1, and Δ_r=2^{−r} otherwise. Set b_1=1,
b_n=1+Σ_{r=1}^{n−1}Δ_r and H=1+Σ_{r≥1}Δ_r. Define

S={n≥1: x_j/sqrt(j)≥x_n/sqrt(n) for all j≥n},

T_n=(n²/x_n²)Σ_{r=n}^{2n−1}Δ_r/(r−n+1).

**Conclusion.** The coordinates are strictly increasing and satisfy
Σ_n x_n^{−2}<∞; the heights strictly increase to finite H. Moreover,

S={N_k:k≥1},   T_{N_k}≥1.

Thus the assertion that every admissible pair of sequences satisfies
liminf_{n→∞, n∈S}T_n=0 is false. Nevertheless, for the paired product

f(z)=Π_{n≥1}(1−z²/(x_n+i b_n)²)(1−z²/(x_n−i b_n)²),

the full upward contribution E_f(x_{N_k}+i b_{N_k}), as defined in
Lemma 84, tends to zero.

## Proof

Within a block x_n² increases strictly with n. At a boundary k≥2,
the preceding endpoint has square (k−1)²N_{k−1}, whereas the first
new square is greater than k²N_k/2=2k²N_{k−1}. Thus strict increase
also holds across boundaries. Each block contains at most N_k indices
and x_n²≥k²N_k/2, so its reciprocal-square sum is at most 2/k².
Summing gives convergence, since Σk^{−2} converges by the integral
test. The extra increment masses sum to Σk²/4^k<∞: the ratio of
successive terms is (1+1/k)²/4≤9/16 for k≥2. Also Σ2^{−r}=1.
This proves all coordinate and height hypotheses.

Inside block k,

x_n²/n=(k²/2)(N_k/n+1)

strictly decreases with n and equals k² at n=N_k. Every nonendpoint
therefore has a later, strictly smaller ratio and does not belong to S.
At endpoint N_k, all later indices belong to blocks l>k, where their
ratios are at least l²>k². Thus N_k belongs to S, proving its exact
description (squaring preserves comparisons between positive ratios).
Since x_{N_k}²=k²N_k, the first term in T_{N_k} gives

T_{N_k}≥(N_k/k²)Δ_{N_k}≥(N_k/k²)(k²/N_k)=1.

The set S is unbounded, so this lower bound disproves the proposed
zero lower limit through S.

For clarity, the true upward sum behaves differently in this example.
Lemma 84 applies to the verified coordinate and height hypotheses and
supplies product properties, the exact simple zero set, and the identity
E_f(w_n)=U_n+V_n, where w_n=x_n+i b_n and

U_n=2Σ_{j>n}(b_j−b_n)/[(x_j−x_n)²+(b_j−b_n)²],

V_n≤2HΣ_{j>n}x_j^{−2}.

For n=N_k, the first coordinate in the next block satisfies

x_{n+1}²=(k+1)²(4N_k+N_k+1)/2>2k²N_k=2x_n².

Monotonicity implies x_j>sqrt(2)x_n for every j>n. Hence
x_j−x_n>(1−1/sqrt(2))x_j>x_j/4. Using b_j−b_n≤H gives
U_n≤32HΣ_{j>n}x_j^{−2}, first for finite partial sums and then by
nonnegative limits. Consequently

0≤E_f(w_{N_k})≤34HΣ_{j>N_k}x_j^{−2}→0.

The convergent reciprocal-square series justifies this last limit. ∎

## Qualifications

The obstruction concerns the sufficient bound in Lemma 86, not that
lemma's validity or the unrestricted upward liminf assertion. Its generic
suffix separation estimate loses the large actual jump after each
endpoint. Sparse endpoints allow a summable amount of increment mass
to make T large at every selected index. In this very construction the
actual full contribution vanishes along those same indices. No conclusion
about theta zeros or RH follows.

## Verification and formalization obligations

The proof is exact and analytic; no numerical certificate is needed.
Check the block partition including its first four indices, cross-boundary
strict increase, block series bound, geometric increment bound, exact
suffix-set characterization, first-term lower bound, and the full-sum
tail estimate. Lemma 84 supplies only the product, zero enumeration and
reflected-sum estimate. The mention of Lemma 86 identifies the tested
bound and is not an input to the proof of the counterexample.
