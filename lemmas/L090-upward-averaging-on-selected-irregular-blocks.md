# Lemma 90: upward averaging on selected irregular blocks

**Hypotheses.** Let 0<x_1<x_2<⋯ with Σ_n x_n^{-2}<∞, and let
0<b_1<b_2<⋯ tend to H<∞. Set a_n=x_n/sqrt(n) and
S={n≥1: a_j≥a_n for every j≥n}. For an integer N with
B_N=S∩[N,2N) nonempty, put M_N=|B_N| and A_N=min_{n∈B_N}a_n.
Define

Q_n=Σ_{j=n+1}^{2n}(b_j−b_n)/[(x_j−x_n)²+(b_j−b_n)²].

**Conclusion.** Every such block satisfies

(1/M_N)Σ_{n∈B_N}Q_n
 ≤16H N(2+log M_N)/(M_N A_N²).                         (1)

If an unbounded sequence of these blocks satisfies

N(2+log M_N)/(M_N A_N²)→0,                             (2)

then Q_n and the full upward contribution E_f(x_n+i b_n) for the
paired product of Lemma 84 tend to zero on a common unbounded
subsequence of S. There are coordinates satisfying (2) for which
Σ_{n∈S}n/x_n² diverges and liminf_N M_N/N=0 (with M_N=0 allowed
when stating this lower density).

## Proof

Fix a nonempty block and abbreviate M=M_N and A=A_N. For n∈B_N
and n<j≤2n<4N the suffix property gives

x_j−x_n≥a_n(sqrt(j)−sqrt(n))≥A(j−n)/(4sqrt(N)).

The last inequality uses sqrt(j)+sqrt(n)<4sqrt(N). Thus

Q_n≤16N A^{-2}Σ_{j=n+1}^{2n}(b_j−b_n)/(j−n)².

Expand b_j−b_n=Σ_{r=n}^{j−1}Δ_r, where Δ_r=b_{r+1}−b_r>0.
All sums over this block are finite. For each fixed r and k=j−n,
there are at most k choices of n with n≤r<n+k and at most M choices
in B_N. Therefore the coefficient of Δ_r, after summing over n,
is at most

Σ_{k=1}^{4N}min(k,M)/k²
 ≤Σ_{k=1}^{M}1/k+MΣ_{k=M+1}^∞1/k²
 ≤1+log M+M∫_M^∞t^{-2}dt=2+log M.

This also holds for M=1. Eligible r belong to [N,4N), so their
increments sum to at most b_{4N}−b_N≤H. Dividing by M proves (1).
Under (2), choose a minimizer of Q_n in each selected block. Passing
first to blocks with each new N at least twice the preceding N makes
these chosen indices strictly increasing. Their Q_n tend to zero by
(1) and nonnegativity. Lemma 84 supplies the product and the estimates

0≤E_f(x_n+i b_n)≤2Q_n+32HΣ_{j>2n}x_j^{-2}
                         +2HΣ_{j>n}x_j^{-2},  n∈S.

The reciprocal-square tails vanish, proving the common subsequence claim.

### Example with divergent suffix weights and zero lower density

For k=0,1,2,… put u_k=16^k, m_k=4u_k and T_k=16u_k=u_{k+1}.
Set x_n=n for u_k≤n≤m_k. At the remaining integer indices
m_k<n<T_k set

x_n=sqrt(T_k n)(1+(T_k−n)/(4T_k)).                       (3)

These intervals partition the positive integers. On a gap, the
continuous function in (3) has derivative

sqrt(T_k)(5T_k−3t)/(8T_k sqrt(t))>0,  m_k≤t≤T_k.

Its value at m_k is greater than sqrt(T_k m_k)=2m_k,
and its value at T_k is T_k. Thus the jump from x_{m_k}=m_k
to x_{m_k+1} is strictly upward, and all subsequent coordinates
increase strictly up to x_{T_k}=T_k. Dense intervals also increase
strictly, so the entire sequence does. On every gap x_n≥sqrt(T_k n)≥n,
and on the other intervals x_n=n. Consequently Σx_n^{-2}≤Σn^{-2}<∞.

On a gap, a_n=sqrt(T_k)(1+(T_k−n)/(4T_k)) decreases strictly
and exceeds a_{T_k}=sqrt(T_k). No gap interior belongs to S.
On [u_k,m_k], a_n=sqrt(n); all later points in this same interval
have larger a, the ensuing gap has a>sqrt(T_k)>sqrt(m_k), and
all subsequent intervals and gaps have a≥sqrt(T_k). Hence

S=⋃_{k≥0}([u_k,m_k]∩the positive integers).

For each k, the subinterval [u_k,2u_k) lies in S, and its contribution
to Σ_{n∈S}n/x_n² is Σ_{n=u_k}^{2u_k−1}1/n≥1/2. These intervals
are disjoint, proving divergence. For N=2m_k=8u_k, every integer
in [N,2N) lies in a gap interior, so M_N=0; the lower density is zero.
On the other hand, at N=u_k we have M_N=N and A_N²=N, making the
ratio in (2) equal to (2+log N)/N→0. Any positive strictly increasing
bounded heights can be used. This verifies every claimed property. ∎

## Qualifications

This is a sufficient selected-block condition, not a resolution for all
irregular suffix sets. Its explicit example lies outside the hypotheses
of both Lemmas 88 and 89; those lemmas are comparisons, not proof inputs.
The proof makes no height-rate assumption and proves neither pointwise
convergence nor a conclusion about theta-specific zeros or RH. Whether
the near-sum liminf is zero when no sequence of blocks satisfies (2)
remains unproved in the divergent-weight, zero-lower-density case.

## Verification and formalization obligations

The proof is analytic and needs no numerical certificate. Check the
finite crossing multiplicity min(k,M), both integral comparisons,
subsequence extraction, and the full-tail estimates from Lemma 84.
For the example check the derivative, both gap boundaries, the exact
suffix set, disjoint harmonic lower bounds, and the half-open empty
blocks. The only direct lemma input is Lemma 84 for the paired product
and its full-contribution tail estimates.
