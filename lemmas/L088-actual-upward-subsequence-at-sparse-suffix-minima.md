# Lemma 88: actual upward subsequence at sparse suffix minima

**Hypotheses.** Let 0<x_1<x_2<⋯ satisfy Σ_n x_n^{-2}<∞, and let
0<b_1<b_2<⋯ tend to H<∞. Define a_n=x_n/sqrt(n) and

S={n≥1: a_j≥a_n for every j≥n}.

Enumerate S increasingly as s_1<s_2<⋯. Assume additionally that

Σ_l s_l/x_{s_l}²<∞.                                      (1)

**Conclusion.** For the actual near sum

Q_n=Σ_{j=n+1}^{2n}(b_j−b_n)/[(x_j−x_n)²+(b_j−b_n)²],

one has liminf_{l→∞} Q_{s_l}=0. The same subsequence makes the full
upward contribution E_f(x_{s_l}+i b_{s_l}) tend to zero for the paired
product f of Lemma 84. Condition (1) holds, in particular, if there are
q>1 and l_0 such that s_{l+1}≥q s_l for every l≥l_0.

## Proof

Lemma 84 proves a_n→∞, unboundedness of S, and attainment of a minimum
on every tail. For each l, the earliest minimizer t of a_j over j>s_l
is exactly s_{l+1}. Indeed, t belongs to S; any r∈S with s_l<r<t would
satisfy a_r≤a_t by its suffix property and a_r≥a_t by minimality. That
would contradict t being the earliest minimizer. Consequently

a_j≥a_{s_{l+1}} for every j>s_l.

Put c_l=s_l/x_{s_l}²>0 and epsilon_l=a_{s_{l+1}}/a_{s_l}−1≥0.
The nonnegativity follows from s_l∈S. For n=s_l and 1≤k≤n,

x_{n+k}≥(1+epsilon_l)x_n sqrt(1+k/n),

x_{n+k}−x_n≥x_n(epsilon_l+k/(3n)).                       (2)

Here sqrt(1+k/n)−1=(k/n)/(sqrt(1+k/n)+1)≥k/(3n), and
multiplication by 1+epsilon_l only increases the extra term.
For epsilon_l>0, discard the squared height difference from the
denominator and use 0<b_{n+k}−b_n≤H. The decreasing function
(t↦(epsilon_l+t/(3n))^{-2}) gives

Q_n≤(H/x_n²)Σ_{k=1}^n(epsilon_l+k/(3n))^{-2}
   ≤(H/x_n²)∫_0^∞(epsilon_l+t/(3n))^{-2}dt
   =3H c_l/epsilon_l.                                   (3)

The sum-to-integral inequality follows term by term by integrating on
[k−1,k], followed by enlarging the integration interval. There is no
assertion of (3) when epsilon_l=0.

On the other hand, for every L≥1,

Σ_{l=1}^L log(1+epsilon_l)=log(a_{s_{L+1}}/a_{s_1})→∞.

Since log(1+t)≤t for t≥0, Σ_l epsilon_l=∞. Together with (1), this
implies that for every δ>0 and every K there is l≥K with epsilon_l>0
and c_l/epsilon_l<δ. Otherwise epsilon_l≤c_l/δ for all l≥K with
positive epsilon_l, and the same inequality holds for zero epsilon_l;
summing would contradict divergence of Σ epsilon_l. Recursively select
increasing l_m with positive epsilon_{l_m} and c_{l_m}/epsilon_{l_m}<1/m.
Equation (3) and nonnegativity yield Q_{s_{l_m}}→0.

Lemma 84 applies to the coordinate and height hypotheses and supplies
the paired product, its simple zeros, fixed-index convergence, and the
far and reflected bounds. With its normalization of E_f these give,
for every n∈S,

0≤E_f(x_n+i b_n)≤2Q_n+32HΣ_{j>2n}x_j^{-2}
                         +2HΣ_{j>n}x_j^{-2}.

The convergent-series tails tend to zero, so the same selected
subsequence proves the full-contribution assertion.

Finally suppose s_{l+1}≥q s_l eventually. For each sufficiently large l,
the disjoint integer block s_{l−1}<r≤s_l has at least
(1−1/q)s_l indices. Coordinate monotonicity gives

Σ_{r=s_{l−1}+1}^{s_l}x_r^{-2}≥(1−1/q)s_l/x_{s_l}².

Sum over these disjoint blocks and use Σ_r x_r^{-2}<∞. This proves
(1); finitely many initial terms do not affect convergence. ∎

## Qualifications

This is a scoped result for suffix sets satisfying (1), including the
geometric spacing appearing in the previously tested sparse-endpoint
obstruction. No rate assumption on the height increments is used.
The actual successor minimum supplies extra separation that is lost
when one uses only a_j≥a_n.

Condition (1) is not automatic. For example, x_n=n and b_n=1−1/(n+1)
satisfy the coordinate and height hypotheses, and a_n=sqrt(n) strictly
increases, so S consists of every positive integer. Then
Σ_{n∈S}n/x_n²=Σ_n1/n diverges. This only shows the limitation of the
new sufficient condition; it is not a counterexample to near-sum
liminf zero. The unrestricted assertion for arbitrary suffix sets and
the RH gap remain unresolved. No claim about theta-specific zeros is made.

## Verification and formalization obligations

This is an analytic proof, requiring no numerical certificate. Verify
the earliest-tail-minimizer argument including ties, (2), the decreasing
sum-to-integral bound, telescoping logarithms, selection only at positive
epsilon_l, the factor 2 relating Q_n to E_f, and the disjoint integer
blocks. Lemma 84 supplies the tail-minimum existence, growth, product
properties and full-tail estimates. The limitation example uses only
convergence of Σn^{-2} and divergence of the harmonic series.
