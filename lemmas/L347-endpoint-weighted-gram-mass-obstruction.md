# Lemma 347: a coefficient-mass obstruction for weighted endpoint sampling

**Hypotheses.** Use L332's absolutely convergent reduced-ratio expansion

R_r(a)=S_r(a)/|ζ(1+1/r+ia)|²−1
      =Σ_((p,q)=1)b_r(p,q)exp(ia log(q/p)),  r≥2,
b_r(p,q)=Σ_(d≥1)(d²pq)^(-1−1/r)H_r(dp,dq),
H_r(m,n)=Σ_(j|m,k|n)μ(m/j)μ(n/k)[f_r(log(jk))−1],
f_r(t)=exp(t/2+t/r)(1−t/(2r))_+^r.

Here S_r is L335's full endpoint sum. Put

F={(p,q): p,q≥1, gcd(p,q)=1, p≠q},
ω_(p,q)=log(q/p),  A_r=Σ_(ν∈F)|b_r(ν)|,
a_n=sqrt(4π²exp(8n)−25),
D_N=(1/N)Σ_(n=N)^(2N−1)|R_(2n)(a_n)|².

For a nonempty consecutive interval I=[u,v]⊆{N,…,2N−1}, allow
any frequency weights w_I(ν)>0 on the union of the supports of
b_(2n)|_F, n∈I. Zero coefficients throughout I may be omitted.
Require W_I=Σ_ν w_I(ν)<∞ and set

x_n(ν)=b_(2n)(ν)/sqrt(w_I(ν)),  n∈I.

Require x_n∈ℓ²; otherwise the norm certificate below is infinite.
For each nonempty J⊆I let

G_(I,J)(n,m)=Σ_ν w_I(ν)exp(i(a_n−a_m)ω_ν),  n,m∈J,
L_(I,J)=||G_(I,J)||op,
V_I=||x_v||_2+Σ_(t=u)^(v−1)||x_t−x_(t+1)||_2,
B_I=sqrt(L_(I,I))||x_v||_2
    +Σ_(t=u)^(v−1)sqrt(L_(I,[u,t]))||x_t−x_(t+1)||_2.   (1)

Thus B_I uses the optimal weighted sampling norm separately on
each interval appearing in exact vector Abel summation. Independent
weights on different intervals of a partition are allowed. The
certificate joins these norm bounds by the triangle inequality;
it does not retain signed correlations between their vectors.

The weights proposed in the preceding assessment are
w_N(ν)=max_(N≤n<2N)|b_(2n)(ν)| on the full sample interval,
with G_N=G_(I,I) and V_N=V_I. They satisfy all finiteness
requirements, as proved below.

**Conclusion.** There is an absolute K such that, for all large r,

A_r≥r/4−K.                                             (2)

In particular, the proposed full-interval target fails:

||G_N||op V_N²≥(N−K)²,                                 (3)

after increasing K. Its required scale is o(N), so its normalized
upper-bound budget diverges at least linearly instead of tending
to zero. The same obstruction holds for every admissible choice
of positive weights, not just w_N.

More precisely, for every partition into nonempty consecutive I,
with independent admissible weights, let d_n=b_(2n)(1,1) and

U_N=(1/N)Σ_I (||(d_n)_(n∈I)||_2+B_I)².

Then

D_N≤U_N,  U_N≥cN                                      (4)

eventually, with an absolute c>0 independent of the partition
and the weights. Therefore neither this optimal weighted
vector-Abel certificate nor its coarser full-Gram version can
prove D_N=o(1) or D_N<1/4.

These are lower bounds on upper-bound certificates. They do not
give a lower bound on D_N, a value of R at any prescribed a_n,
an endpoint sign, or an additional zero-exclusion range.

**Proof.** The main new input to the norm comparison is the size
of a multiplicative evaluation of the fully grouped coefficients.
Let λ(m)=(−1)^Ω(m) be L335's Liouville assignment and σ=1+1/r.
Absolute convergence on Re s>1 and finite Möbius inversion give

F_λ(σ)=Σ_(m≥1)λ(m)m^(−σ)=ζ(2σ)/ζ(σ)>0,
M_λ(σ)=Σ_(m≥1)μ(m)λ(m)m^(−σ)=1/F_λ(σ).                (5)

The first identity is proved in L335. For the second, multiply
the two absolutely convergent series: the coefficient at m is
λ(m)Σ_(d|m)μ(d), which is one at m=1 and zero otherwise.
This uses no conditional series or growing-height zero estimate.

Multiply the absolutely summable two-index expansion in L332
by λ(m)λ(n). In the part containing f_r, write m=ju, n=kv.
Complete multiplicativity gives λ(m)λ(n)=λ(j)λ(k)λ(u)λ(v),
and (jk)^(−σ)f_r(log(jk)) is the original weight W_r(j,k).
The constant part of the divisor sum contributes exactly one.
Consequently

Σ_(m,n≥1)(mn)^(−σ)H_r(m,n)λ(m)λ(n)
 =S_r[λ]M_λ(σ)²−1.

The majorant (e+1)τ(m)τ(n)/(mn)^σ from L332 is summable,
so all products and regroupings in this identity are justified.
For m=dp,n=dq, λ(dp)λ(dq)=λ(p)λ(q) since λ(d)²=1.
Thus the exact reduced-ratio identity is

Σ_((p,q)=1)b_r(p,q)λ(p)λ(q)
 =S_r[λ]/F_λ(σ)²−1.                                  (6)

In particular all equal-frequency collisions have already been
retained. Evaluating the absolutely convergent character series
does not claim that this character occurs at any sampled height.

L335 proves S_r[λ]=−ζ(2)²/(4r)+O(r^(−2)). Its analytic
expansion F_λ(1+w)=wζ(2+2w)/H(w), H(0)=1, also gives

F_λ(1+1/r)=ζ(2)/r+O(r^(−2)),
F_λ(1+1/r)²=ζ(2)²/r²(1+O(1/r)).                       (7)

Dividing the numerator asymptotic by (7), a positive nonzero
quantity, shows that (6) equals −r/4+O(1). L332 gives
b_r(1,1)=O(1/r). Removing this constant frequency therefore yields

Σ_(ν=(p,q)∈F)b_r(ν)λ(p)λ(q)=−r/4+O(1).                (8)

The absolute value of (8) is at most A_r, proving (2).
This growth is compatible with L332's ℓ² norm O(1/r): ℓ¹
and ℓ² norms on the infinite frequency set control different
quantities. No uniform ℓ¹ expansion was inferred from that
ℓ² asymptotic.

We next check the weights and the sampling identities exactly.
For the proposed maximum weights, a finite sum of summable
sequences bounds their total:

Σ_ν w_N(ν)≤Σ_(n=N)^(2N−1)Σ_ν |b_(2n)(ν)|<∞.

Also |b_(2n)(ν)|²/w_N(ν)≤|b_(2n)(ν)| at every retained
frequency. Hence every x_n is in ℓ², and V_N is finite because
it has finitely many terms. The same reasoning applies if the
maximum is restricted to one interval of a partition.

For general admissible weights define the sampling map

(T_J z)_n=Σ_ν sqrt(w_I(ν))z_ν exp(ia_nω_ν),  n∈J.

Cauchy–Schwarz makes each row a bounded ℓ² functional of norm
sqrt(W_I). Since J is finite, T_J is bounded. Direct multiplication
gives T_J T_J*=G_(I,J); all its entries converge absolutely.
The Hilbert-space operator identity ||T_J||²=||T_J T_J*||
therefore identifies L_(I,J) as its optimal squared norm.
It also shows that G is positive semidefinite. Each diagonal
entry of this matrix is exactly W_I. Evaluating its quadratic
form on a coordinate unit vector gives

L_(I,J)≥W_I  for every nonempty J.                     (9)

No sample-spacing estimate is used in (9); it holds at the actual
samples and at any other real sample locations.

For each n∈I, Cauchy–Schwarz in the frequency variables gives

A_(2n)=Σ_ν sqrt(w_I(ν))|x_n(ν)|
 ≤sqrt(W_I)||x_n||_2.                                 (10)

The exact finite telescoping identity

x_n=x_v+Σ_(t=n)^(v−1)(x_t−x_(t+1))

shows ||x_n||_2≤V_I. Equations (9), (10) and (1) imply

sqrt(L_(I,I))V_I≥sqrt(W_I)V_I≥A_(2n),
B_I≥sqrt(W_I)V_I≥A_(2n)  for every n∈I.                (11)

For the full interval choose n=v=2N−1. By (2),
A_(2v)≥v/2−K=N−1/2−K. Squaring the first inequality
in (11) proves (3) after changing K. This bound is uniform
over all admissible weights, even weights chosen with knowledge
of all the sample phases. Infinite norms cannot improve it.

To verify the upper certificate in (4), write

y_n=Σ_ν b_(2n)(ν)exp(ia_nω_ν)=R_(2n)(a_n)−d_n.

Apply T_I to x_v. The difference vector x_t−x_(t+1)
is sampled only on [u,t] and extended by zero on the rest of I.
The telescoping identity above gives precisely the sum of these
sample vectors, equal to (y_n)_(n∈I). Their triangle bound is
B_I, using the exact operator norm on each prefix. Thus
||(R_(2n)(a_n))_(n∈I)||_2≤||d|_I||_2+B_I. Squaring
and summing over disjoint I proves D_N≤U_N. The series involved
are absolutely convergent by L332, and only finitely many
sample and vector terms occur, so no limiting interchange is
needed here.

Finally every nonempty I has v≥N. Equations (2) and (11) give
B_I≥v/2−K≥N/2−K≥N/4 for all sufficiently large N.
If the partition has k≥1 intervals, it follows that

U_N≥k N/16≥N/16.

This proves (4) uniformly over partitions and their weights.
The constant frequency has already been separated; its normalized
sample norm is O(1/N) by L332 and is not the source of the loss.

The test stops separating a full coefficient-space sampling
operator norm from the vector norm and joining the moving terms
absolutely. Positive diagonal weights cannot remove the large
total mass detected by (8). A signed estimate that uses the
actual coefficient vectors together with their sample phases,
or an algebraic subtraction changing the sampled remainder,
is not ruled out. No assertion about actual D_N or RH follows. ∎

**Mathlib.** Full statement: not checked. Coverage of the normalized
Liouville identity, nonconstant coefficient-mass lower bound,
weighted Gram comparison and partitioned vector-Abel obstruction
is not checked; all required arguments are given above. L332 and
L335 retain supporting results recorded as present through L001:
[`ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius),
[`ArithmeticFunction.LSeriesSummable_moebius_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeriesSummable_moebius_iff),
and [`riemannZeta_ne_zero_of_one_lt_re`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#riemannZeta_ne_zero_of_one_lt_re).
Those links were not rechecked. They support the original reciprocal
expansion and denominator, not the present conclusion. No full
library match or absence from checked sources is asserted.
