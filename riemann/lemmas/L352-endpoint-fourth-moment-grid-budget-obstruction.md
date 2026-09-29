# Lemma 352: the imported rational-grid budget is trivial on the weighted range

**Hypotheses.** Use L351's F, w_N, W_N, B_N, c_N(k,l), and
a_n=sqrt(4π²exp(8n)−25), with I_N={N,…,2N−1}. Thus

c_N(k,l)=Σ_(q|k,p|l)w_N(p,q)w_N(k/q,l/p),
Σ_(k,l)c_N(k,l)=W_N²,  Σ_k c_N(k,k)=B_N,

where weights outside F are zero. For any nonempty J⊆I_N put
s=|J|, C_J(x)=s^(-1)Σ_(n∈J)exp(ia_n x), and define

Q_N=Σ_(ν,μ∈F)w_N(ν)w_N(μ)|C_(I_N)(ω_ν−ω_μ)|⁴/W_N².

Let X_N be the smallest power of two at least
exp(32 sqrt(N) log N). Partition {1,…,X_N} into {1} and the
blocks (M,2M] for powers of two M<X_N.

The tested certificate uses Guth–Maynard Lemma 11.6 on these
square grids, Cauchy–Schwarz for unequal blocks, the maximum
c_N(k,l) on each block rectangle to transfer the weights, and
the better of that bound and |C_J|≤1. It may remove the exact
k=l contribution first. It may partition I_N into arbitrary
nonempty subsets and combine their bounds by the L⁴ triangle
inequality. Every use of the imported theorem has a fixed positive
implicit constant and fixed ε>0. This defines the certificate
being tested, not an assumption on cancellation.

**Conclusion.** The exact fourth-moment identity and tail bound are

Q_N=W_N^(-2)Σ_(k,l≥1)c_N(k,l)|C_(I_N)(log(k/l))|⁴,
Σ_(max(k,l)>X_N)c_N(k,l)=O(N^(-4)).                    (1)

The equal-frequency contribution is B_N/W_N²=O(1/N). For every
nonempty subset J, the tolerance-one additive energy of its actual
heights is exactly

E({a_n:n∈J})=2s²−s.                                  (2)

Nevertheless the stated certificate returns the entire retained
off-diagonal weight, which after normalization is

W_N^(-2)Σ_(k,l≤X_N,k≠l)c_N(k,l)=1−O(1/N).           (3)

Including the exact diagonal and a tail bound leaves a budget
tending to one. Sample partitioning as specified above does not
improve it. This fails the sufficient threshold Q_N=o(N^(-1/2)).

The conclusion is a lower bound on this upper-bound certificate.
It is not a lower bound on Q_N and does not refute the target
M_N(N^(-1/8))=o(1). No endpoint margin, Laguerre sign,
zero-exclusion extension, or RH candidate follows.

**Proof.** All weights are nonnegative and W_N is finite. Expanding
the definitions and grouping k=qu, l=pv is therefore legitimate
by Tonelli, since |C_J|≤1. It gives the first identity in (1)
and its identical version for every J. This grouping retains
all unreduced-ratio collisions. L351 proves that k=l corresponds
exactly to equal reduced frequency pairs, giving B_N, rather
than an extra uncounted diagonal.

Set δ=1/(2sqrt(N)). L351's pointwise majorant is

c_N(k,l)≤C d_4(k)d_4(l)/(kl)^(1+δ),                  (4)

with an absolute constant. On k>X, use
k^(-δ/2)≤X^(-δ/2). Positive ordered-factor sums and the
integral bound ζ(1+u)≤1+1/u give

Σ_(max(k,l)>X)c_N(k,l)
 ≤2C X^(-δ/2)ζ(1+δ/2)^4ζ(1+δ)^4
 ≤C' N⁴ X^(-1/(4sqrt(N))).                           (5)

There is no finite-support or minimum-spacing assumption here.
With X=X_N the last power is at most N^(-8), proving (1).
This tail estimate uses the maximum weights themselves through
(4), rather than weights frozen at a single n. L351 also gives
W_N bounded above and below away from zero, and B_N=O(1/N).
Subtracting the tail and diagonal from the total W_N² proves (3).

We next check the sample geometry without approximating a_n.
Squaring shows, for j≥1,

a_(j+1)>exp(4)a_j>4a_j.                              (6)

For two unequal multisets of two indices, cancel shared indices
and let j be the largest remaining one. The side containing j
exceeds the other by at least a_j−2a_(j−1)>a_j/2>1.
If no smaller index occurs, the conclusion is immediate instead.
Consequently |a_i+a_j−a_k−a_l|≤1 holds exactly for matching
unordered pairs. For each of the s(s−1) ordered distinct pairs
on the first side there are two matching orders on the second;
each repeated pair has one. Thus the number is
2s(s−1)+s=2s²−s. This proves (2), including s=1.

For s≥2 let T_J=max_(n∈J)a_n−min_(n∈J)a_n. L351's
actual gap estimate, or (6) and a_n≥πexp(4n), gives

c exp(4N)≤T_J≤C exp(8N).                            (7)

In particular the sets are 1-separated. The full set has
T_(I_N) comparable to exp(8N). Translating a set to start at
zero changes its exponential sum by a unit-modulus factor only.

Use the [imported fourth-moment input](../foundations/endpoint-fourth-moment-input.md).
For a block B=(M,2M] and s≥2 it bounds the normalized
square-grid moment by

U_J(M)=C_ε T_J^ε
 [M+M²(2s²−s)/s⁴+(2s²−s)^(3/4)T_J^(1/2)M/s³].      (8)

The fixed theorem constant can be enlarged to be at least one.
Nothing in this argument requires evaluating it or varying ε
with N. The third term alone, (7), and s≤N imply, uniformly
for all such J and M<X_N,

U_J(M)/M²
 ≥c exp(2N)/(N^(3/2)X_N) → ∞.                       (9)

Indeed log X_N≤32sqrt(N)log N+log 2=o(N). Even formally
removing the T_J^ε factor would leave this divergence. Thus
small additive energy does not address this term on the range
containing all but O(N^(-4)) of the weight. The T_J^ε loss is
never interpreted as N^ε.

For clarity, unequal block scales require no new analytic input.
Write R_J(v)=Σ_(n∈J)v^(ia_n). For any finite integer blocks
B,D define A_J(B,D)=Σ_(k∈B,l∈D)|R_J(k/l)|⁴. Expanding
in the four sample indices gives, with
Δ=a_(n₁)+a_(n₂)−a_(n₃)−a_(n₄),

A_J(B,D)=Σ_((n₁,n₂,n₃,n₄)∈J⁴)
  [Σ_(k∈B)k^(iΔ)] conjugate([Σ_(l∈D)l^(iΔ)]).

Cauchy–Schwarz on this finite tuple set yields

A_J(B,D)≤sqrt(A_J(B,B)A_J(D,D)).                     (10)

Use (8) after dividing by s⁴. For the singleton block {1}
its normalized square moment is exactly one; set U_J({1})=1.
For any other block B let U_J(B) be (8). Equations (9)–(10)
show that the rectangular certificate sqrt(U_J(B)U_J(D))
is at least |B||D| for every pair of blocks, eventually uniformly
in J. Capping square-grid estimates by their trivial |B|²
bounds before (10) gives exactly the same rectangular threshold.

Let m_(B,D)=Σ_(k∈B,l∈D,k≠l)c_N(k,l), and let
v_(B,D) be the largest of these finitely many coefficients,
zero if the set is empty. The weight-transfer step gives

Σ_(k∈B,l∈D,k≠l)c_N(k,l)|C_J(log(k/l))|⁴
 ≤min(m_(B,D), v_(B,D)sqrt(U_J(B)U_J(D))).            (11)

The second argument is at least v_(B,D)|B||D|≥m_(B,D).
Thus (11) reduces exactly to m_(B,D). Subtracting the known
unweighted diagonal when B=D does not alter this conclusion:
its size is |B|, while (9) implies U_J(B)−|B|≥|B|²−|B|.
The singleton diagonal is empty. Further restriction to a subset
of entries while still invoking the enclosing grid estimate also
leaves the second argument above the corresponding total mass.

If s=1, |C_J| is identically one, so the trivial retained-weight
bound is exact. For s≥2, summing (11) proves (3) as the budget
of the specified certificate for each J. All constants and the
eventual comparison are uniform over these subsets.

Finally suppose I_N is partitioned into J₁,…,J_h. Then
C_(I_N)=Σ_j (|J_j|/N)C_(J_j). Apply the L⁴ triangle
inequality with the finite positive measure
c_N(k,l)/W_N² on the retained off-diagonal entries. Each
subset's certificate for the fourth power of its norm is the
same mass m. The combined norm budget is therefore
Σ_j (|J_j|/N)m^(1/4)=m^(1/4), whose fourth power is m
again. Different such partitions on different rectangles have
the same limitation. This establishes the sample-partition claim
for the specified triangle-inequality assembly.

The exact full diagonal plus the retained off-diagonal entries
has normalized mass
1−O(N^(-4)). Adding the upper tail estimate from (5) gives
1+O(N^(-4)), also cappable by Q_N≤1. This budget is far above
o(N^(-1/2)). Indeed Markov's inequality would need that latter
scale to prove M_N(N^(-1/8))≤N^(1/2)Q_N=o(1).

The imported grid theorem has been specialized, not reproved.
The additional work checks its complete weighted applicability
and limitations, including unequal scales and sample subsets.
It supplies no obstruction to an estimate that retains more
arithmetic information than this maximum-coefficient transfer.
Even a successful moment estimate would leave L351's exceptional
sampled indices and the pointwise margin exceeding
(1+2n)²exp(−2n/256) unresolved. ∎

Finite algebra check: run
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/laguerre/check_endpoint_fourth_moment.py`.
It passes nine exact collision, four-sample expansion and constant-term
identities, including repeated samples, and checks the energy count on
63 subsets of a superincreasing integer toy sequence. These checks do
not test actual a_n, the infinite tail, or any sampled sign; those
qualifications are part of the analytic argument above.

**Mathlib.** Full statement: **not checked**. This includes the
weight-tail estimate, actual-sample energy, rectangular reduction,
and certificate comparison. The external input is specifically
Guth–Maynard Lemma 11.6, cited in foundations; it is not a claim
of Mathlib coverage. L351's supporting Euler-product references
remain unchanged and concern the construction of the weights,
not this full statement. No absence from checked library sources
or mathematical novelty is asserted.
