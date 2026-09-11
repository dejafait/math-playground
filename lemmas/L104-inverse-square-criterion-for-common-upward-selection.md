# Lemma 104: inverse-square criterion for common upward selection

**Hypotheses.** Use any prescribed set P and coordinates x_n of Lemma
100. Let A⊆P be infinite and put

K_s=Σ_{j>s}(x_j−x_s)^(−2).

For each strictly increasing positive bounded height sequence b_n,
use the product f and full upward contribution E_f of Lemma 100.

**Conclusion.** E_f(x_s+i b_s) tends to zero as s→∞ through A for
every such height sequence if and only if sup_{s∈A}K_s<∞.
Consequently a height-independent common vanishing subsequence in P
exists if and only if K_s is bounded on some infinite subset of P.
If K_s is unbounded on A, one permitted height sequence has
E_f(x_s+i b_s)≥2/9 at infinitely many s∈A.

## Proof

Each K_s is finite. Indeed x_j≥j^(3/4) by Lemma 100, so for fixed s
and sufficiently large j we have x_j−x_s≥j^(3/4)/2. The resulting
inverse-square tail is summable, and the finite prefix has strictly
positive gaps. Lemma 100 supplies the product properties and the split

E_f(x_s+i b_s)=U_s+V_s,
U_s=2Σ_{j>s}(b_j−b_s)/[(x_j−x_s)²+(b_j−b_s)²],
0≤V_s≤4H s^(−1/2),

where H=lim b_n. If K_s≤C on A, then U_s≤2C(H−b_s)→0
there, and the bound on V_s proves sufficiency.

For necessity suppose K_s is unbounded on A. For fixed s define

F_s(t)=Σ_{j>s} t/[(x_j−x_s)²+t²],  t≥0.

On [0,ε] the summands are bounded by ε(x_j−x_s)^(−2), a
summable majorant. Thus F_s is continuous on that interval and
F_s(0)=0. If 0<ε≤1/2 and F_s(ε)<1, each summand is less
than 1. Writing d=x_j−x_s, this gives d²>ε−ε² and hence

1/d²=(1+ε²/d²)/(d²+ε²)
     ≤1/[(1−ε)(d²+ε²)].

Summing proves K_s≤F_s(ε)/[ε(1−ε)]<2/ε.
Therefore K_s>2/ε implies F_s(ε)≥1, and the intermediate
value theorem gives 0<δ≤ε with F_s(δ)=1.

We now recursively choose n_l∈A increasing and δ_l>0. Start with
ε_1=1/2. After δ_(l−1) is chosen, set
ε_l=min(2^(−l),δ_(l−1)/4). Choose n_l larger than its predecessor
with K_(n_l)>2/ε_l, then choose a root F_(n_l)(δ_l)=1 in
(0,ε_l]. These choices are possible: removing any finite prefix
from A leaves K unbounded, since every individual K_s is finite.
In particular Σ_lδ_l≤1 and δ_(l+1)≤δ_l/4.

For every integer r≥1 set

c_r=2^(−r) min({1}∪{δ_l:n_l≤r}),
Δ_r=c_r+Σ_{l:n_l=r}δ_l,
b_n=1+Σ_{r<n}Δ_r.

The minimum is over a finite nonempty set of positive numbers. Thus
c_r>0, all heights strictly increase, and
Σ_rΔ_r≤1+1=2. They converge to H≤3.
For n=n_l and every j>n, the marked jump at r=n gives
b_j−b_n≥δ_l. Conversely the entire remaining height budget satisfies

Σ_{r≥n_l}Δ_r
 ≤δ_l+Σ_{k>l}δ_k+Σ_{r≥n_l}c_r
 ≤δ_l+δ_l/3+δ_lΣ_{r≥n_l}2^(−r)
 ≤(7/3)δ_l≤3δ_l.

Here c_r≤2^(−r)δ_l for every r≥n_l, and n_l≥1.
For each higher direct zero, therefore,

(b_j−b_n)/[(x_j−x_n)²+(b_j−b_n)²]
 ≥δ_l/[(x_j−x_n)²+9δ_l²]
 ≥(1/9)δ_l/[(x_j−x_n)²+δ_l²].

Summing these nonnegative inequalities and using F_n(δ_l)=1 gives
U_(n_l)≥2/9. The reflected contribution is nonnegative, so the same
bound holds for E_f at every marked index. This contradicts common
vanishing on A and proves necessity. Applying the fixed-A equivalence
to the range of any proposed common subsequence proves the existential
statement. ∎

## Qualifications and verification

The common subsequence depends only on the coordinates. Each individual
height sequence has convergence along it; no uniform rate over all
height sequences is claimed. The adversarial heights may depend on A.
This characterizes common selection for the interpolation of Lemma 100;
it does not assert that every P satisfies the condition, resolve general
height-dependent selection for arbitrary coordinates, or imply RH.

Verification is analytic and requires no numerical certificate. The
proof checks fixed-index summability, continuity including t=0, the
strict threshold implication, removal of finite prefixes, positivity
and summability of the background increments, the geometric tail, and
the factor 2 and denominator direction in the lower bound. All infinite
inequalities follow first for finite sums and then by nonnegative limits.
Formalization would require these estimates, recursive selection and the
intermediate value theorem, and the product and full-sum statements of
Lemma 100.
