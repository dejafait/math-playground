# Lemma 103: unbounded successor gaps do not give common selection

**Hypotheses.** For k≥1 put S_k=2^(8k), d_k=2^(3k), and

P={1,2,...} ∖ ⋃_{k≥1}{S_k+1,...,S_k+d_k−1}.

Use the coordinates, paired product and full upward contribution of
Lemma 100 for this P.

**Conclusion.** The successor coordinate gaps x_(s+1)−x_s are
unbounded along s∈P. Nevertheless, for every infinite subset A⊆P,
there are strictly increasing positive heights b_n tending to H≤3
such that E_f(x_n+i b_n)≥1/9 at infinitely many n∈A.
Thus unbounded successor coordinate gaps do not suffice for a common
vanishing subsequence independent of the heights, even in this
interpolation family.

## Proof

The removed intervals are disjoint: d_k<S_k and
S_k+d_k<2S_k<S_(k+1). Thus P contains 1 and every S_k, is unbounded,
and the next prescribed integer after S_k is T_k=S_k+d_k.
Lemma 100 supplies strictly increasing coordinates, the nonzero entire
product with exactly its stated simple zeros, and finite full upward
sums for each permitted height sequence.

First bound the gaps from below. Fix s=S_k, d=d_k and t=s+d.
The interpolant g_t(v)=sqrt(v)t^(1/4)(5/4−v/(4t)) is increasing on
[s,t], by its positive derivative computed in Lemma 100. As d≥2,

x_(s+1)−x_s=g_t(s+1)−s^(3/4)≥g_t(s)−s^(3/4).

Writing r=t/s∈[1,2], let F(r)=(5r^(1/4)−r^(−3/4))/4.
Then F(1)=1 and

F'(r)=(5r^(−3/4)+3r^(−7/4))/16≥5/32≥1/8.

Consequently

x_(s+1)−x_s≥s^(3/4)(r−1)/8
             =d/(8s^(1/4))=s^(1/8)/8→∞.             (1)

We next prove, for every integer j≥1,

j^(3/4)≤x_j≤j^(3/4)+(3/4)j^(1/8).                  (2)

The lower bound is in Lemma 100. The upper bound is immediate for
j∈P. Otherwise S_k<j<T_k for one k, and monotonicity of g_(T_k)
gives x_j≤T_k^(3/4). Since T_k−j≤d_k=S_k^(3/8)≤j^(3/8),
the decreasing derivative of v^(3/4) gives

T_k^(3/4)−j^(3/4)≤(3/4)j^(−1/4)(T_k−j)
                         ≤(3/4)j^(1/8).

Fix n≥1 and put D=ceil(n^(3/8)). Then D≤2n^(3/8)≤2n.
For n<j≤n+D, (2) and the same derivative estimate imply

0<x_j−x_n≤(3/4)n^(−1/4)D+(3/4)(3n)^(1/8)
             ≤3n^(1/8),                            (3)

where 3^(1/8)≤2 was used. This bound includes prescribed and
nonprescribed j alike.

Now let A⊆P be infinite. Recursively choose distinct increasing
n_l∈A with n_l≥2^(8l), l≥1. Define for r≥1

Δ_r=2^(−r)+Σ_{l≥1}1_{r=n_l}n_l^(−1/8),
b_n=1+Σ_{r=1}^{n−1}Δ_r.

Each marked sum has at most one nonzero term, all Δ_r are positive,
and Σ_rΔ_r≤1+Σ_l2^(−l)=2. Thus b_n strictly increases to a finite
H≤3. For a marked n=n_l and every n<j≤n+D we have

n^(−1/8)≤b_j−b_n≤H≤3.

The D higher zeros w_j=x_j+i b_j each contribute a nonnegative term
to the full upward sum. Using (3), their denominators satisfy

(x_j−x_n)²+(b_j−b_n)²≤9n^(1/4)+9≤18n^(1/4).

Keeping only these terms proves

E_f(w_n)≥2D n^(−1/8)/(18n^(1/4))
          =D/(9n^(3/8))≥1/9.                       (4)

This holds at every n_l. All omitted direct and reflected contributions
are nonnegative; no cancellation or interchange is used. Given any
proposed common subsequence in P, take A to be its range. Equation (4)
contradicts vanishing for the permitted heights just constructed,
while (1) proves the required unbounded gaps. ∎

## Qualifications and verification

The heights depend on the proposed subsequence. This does not obstruct
height-dependent selection in Lemma 101. In particular even selecting
only the endpoints S_k, whose gaps tend to infinity, cannot give a
common subsequence. The large gaps coexist with sufficiently many
higher coordinates within distance O(n^(1/8)). This is a geometric
counterexample, not a statement about the theta zeros or RH.

Verification is analytic; no numerical certificate is needed. Checks
cover the disjoint removed intervals, interpolation endpoints, the
parameter derivative in (1), both cases in (2), the ceiling and small
n bounds in (3), the total height budget, and the direction and factor
2 in (4). Formalization would require those estimates, sparse
extraction from an infinite subset, convergence of the positive
increment series, and Lemma 100's product and full-sum conclusions.
