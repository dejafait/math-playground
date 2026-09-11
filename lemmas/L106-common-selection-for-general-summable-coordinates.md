# Lemma 106: common selection for general summable coordinates

**Hypotheses.** Let 0<x_1<x_2<⋯ and Σ_n x_n^(−2)<∞. Let A be
an infinite subset of the positive integers and set

K_n=Σ_{j>n}(x_j−x_n)^(−2).

For each strictly increasing positive bounded sequence b_n, write
H=lim b_n, w_n=x_n+i b_n, and define

f(z)=Π_{n≥1}(1−z²/w_n²)(1−z²/conjugate(w_n)²),
E_f(w_n)=2Σ_{Im ρ>b_n}(Im ρ−b_n)/|ρ−w_n|²,

where ρ runs over zeros with multiplicity.

**Conclusion.** These products are nonzero even real entire functions
with exactly the simple zeros ±w_n, ±conjugate(w_n); each K_n and
E_f(w_n) is finite. The following are equivalent:

1. For every permitted height sequence, E_f(w_n)→0 as n→∞ through A.
2. sup_{n∈A} K_n<∞.

If condition 2 fails, one permitted height sequence satisfies
E_f(w_n)≥2/9 at infinitely many n∈A. Thus a subsequence common to all
height sequences exists inside an infinite prescribed set P exactly
when K_n is bounded on some infinite subset of P, equivalently when
liminf_{n→∞, n∈P} K_n<∞.

## Proof

Summability implies x_n→∞: otherwise monotonicity would bound every
x_n above and prevent x_n^(−2) from tending to zero. Lemma 74 applies
and gives the asserted product properties. Its zero enumeration gives

E_f(w_n)=U_n+V_n,
U_n=2Σ_{j>n}(b_j−b_n)/[(x_j−x_n)²+(b_j−b_n)²],
0≤V_n≤2HΣ_{j>n}x_j^(−2)→0.                         (1)

Indeed the higher zeros are exactly w_j and −conjugate(w_j) for j>n.
For fixed n, eventually x_j≥2x_n and hence x_j−x_n≥x_j/2.
Thus K_n has a finite prefix of finite terms and a tail bounded by
4Σ_j x_j^(−2). In particular U_n≤2(H−b_n)K_n is finite.
If K_n≤C on A, this last bound tends to zero there, proving sufficiency.

For completeness we carry out the marked-jump argument of Lemma 104
under these general hypotheses. No interpolation estimate is needed.
For fixed n put

F_n(t)=Σ_{j>n}t/[(x_j−x_n)²+t²], t≥0.

For 0≤t≤ε the terms are bounded by ε(x_j−x_n)^(−2), so the
series is uniformly convergent and continuous on that interval and
F_n(0)=0. If 0<ε≤1/2 and F_n(ε)<1, each summand is less
than 1. With d=x_j−x_n this implies d²>ε−ε² and therefore

1/d²=(1+ε²/d²)/(d²+ε²)
     ≤1/[(1−ε)(d²+ε²)].

Summation gives K_n≤F_n(ε)/[ε(1−ε)]<2/ε. Consequently
K_n>2/ε implies F_n(ε)≥1, and continuity gives a δ∈(0,ε]
with F_n(δ)=1.

Suppose K is unbounded on A. Removing any finite prefix leaves it
unbounded, since every K_n is finite. Set ε_1=1/2. Recursively choose
increasing n_l∈A with K_(n_l)>2/ε_l and a root
F_(n_l)(δ_l)=1 with 0<δ_l≤ε_l; after choosing δ_l set
ε_(l+1)=min(2^(−l−1),δ_l/4). Then Σ_l δ_l≤1 and
δ_(l+1)≤δ_l/4.

Define, for integers r≥1,

c_r=2^(−r) min({1}∪{δ_l:n_l≤r}),
Δ_r=c_r+Σ_{l:n_l=r}δ_l,
b_n=1+Σ_{r<n}Δ_r.

Each minimum contains only finitely many positive numbers. Thus
Δ_r>0, Σ_r c_r≤1, and Σ_r Δ_r≤2. The heights strictly
increase and converge to H≤3. At n=n_l the marked jump is included
in b_j−b_n for every j>n, and the entire remaining budget is bounded by

δ_l≤b_j−b_(n_l)≤Σ_{r≥n_l}Δ_r
 ≤δ_l+δ_l/3+δ_l Σ_{r≥n_l}2^(−r)
 ≤(7/3)δ_l≤3δ_l.

For d=x_j−x_(n_l), this yields

(b_j−b_(n_l))/[d²+(b_j−b_(n_l))²]
 ≥δ_l/(d²+9δ_l²)≥(1/9)δ_l/(d²+δ_l²).

Summing gives U_(n_l)≥(2/9)F_(n_l)(δ_l)=2/9. Since V is
nonnegative, these heights violate condition 1. This proves necessity.
All infinite inequalities above hold first for finite sums and then
by nonnegative limits or the stated summable majorants.

Finally, the range of a common subsequence is an infinite A satisfying
condition 1. Apply the equivalence. Boundedness on an infinite subset
of P is equivalent to finite liminf along P: one direction is immediate,
and in the other any constant strictly above that liminf bounds K at
infinitely many indices. This proves the remaining assertions. ∎

## Qualifications and verification

The common subsequence is chosen from the coordinates alone. Convergence
is asserted separately for each height sequence, with no uniform rate
or common bound on H. Adversarial heights may depend on A. This extends
Lemma 104 beyond its interpolation family; it does not settle whether
for every height sequence some height-dependent vanishing subsequence
exists for arbitrary coordinates, and it has no RH implication.

The proof is analytic and requires no computational certificate. The
audit checks the fixed-index summable majorant, the complete higher-zero
enumeration, the reflected tail, the threshold at ε=1/2, finite-prefix
removal, strict and summable height increments, the geometric budget,
and both nonlinear lower-bound inequalities. Formalization would need
the product statement of Lemma 74, uniform convergence of F_n on compact
parameter intervals, the intermediate value theorem, recursive choices,
nonnegative sum limits, and the displayed estimates. Lemma 104 supplies
the reused proof construction, whose hypotheses are verified above.
