# Lemma 348: first-order endpoint subtraction retains large coefficient mass

**Hypotheses.** Use L332's endpoint sum and reduced-ratio expansion,
with r≥2, σ=1+1/r and a real:

S_r(a)=Σ_(j,k≥1)(jk)^(-1/2)(1−log(jk)/(2r))_+^r exp(ia log(k/j)),
R_r(a)=S_r(a)/|ζ(σ+ia)|²−1
      =Σ_((p,q)=1)b_r(p,q)exp(ia log(q/p)).

Retain its polynomial and finite divisor expression

P(t)=t−t²/8,
U(m,n)=Σ_(j|m,k|n)μ(m/j)μ(n/k)P(log(jk)).

Define the exact first-order correction, including its moving exponent,

Q_r(a)=(1/r)Σ_(m,n≥1)(mn)^(-σ)U(m,n)exp(ia log(n/m)),
q_r(p,q)=(1/r)Σ_(d≥1)(d²pq)^(-σ)U(dp,dq),  gcd(p,q)=1.

For any real scalar t put

E_(r,t)(a)=R_r(a)−t Q_r(a),
e_(r,t)(p,q)=b_r(p,q)−t q_r(p,q),
A_r(t)=Σ_((p,q)=1,p≠q)|e_(r,t)(p,q)|.

All these coefficient series converge absolutely for each fixed r,t,
as checked below. Write L(s)=ζ′(s)/ζ(s); the prime on L means
complex differentiation in s, not differentiation in the height a.
For an absolutely summable reduced-ratio series, its Liouville
evaluation means replacing exp(ia log(q/p)) by λ(p)λ(q), where
λ(m)=(−1)^Ω(m). Denote this evaluation by brackets [λ].

**Conclusion.** At s=σ+ia the exact identity is

Q_r(a)=[−2 Re L(s)−Re L′(s)/4−(Re L(s))²/2]/r.          (1)

Subtracting Q_r improves the long-height mean-square bound:

lim_(H→∞)(1/(2H))∫_(−H)^H |E_(r,1)(a)|²da
 =Σ_((p,q)=1)|e_(r,1)(p,q)|²=O(r^(-4)).                 (2)

Nevertheless the two character tests give

Q_r[λ]=−r/4+O(1),    E_(r,1)[λ]=O(1),
Q_r(0)=−3r/4+O(1),  E_(r,1)(0)=3r/4+O(1).             (3)

Consequently there is an absolute C such that, for all sufficiently
large r,

A_r(1)≥3r/4−C,
inf_(t∈ℝ) A_r(t)≥3r/16−C.                              (4)

The second bound allows t to depend arbitrarily on r. Thus cancellation
of the leading Liouville value does not remove the order-r coefficient
mass, even after optimizing a scalar multiple of this correction.

For the samples a_n=sqrt(4π²exp(8n)−25), N≤n<2N, every positive-weight
sampling/operator-norm and absolute vector-Abel certificate of L347's
form, applied to E_(2n,t_n)(a_n), has normalized budget at least cN.
The coarser full-interval norm product is at least cN², against the
required o(N). This holds for arbitrary real t_n, positive weights and
independent weights on consecutive sample-interval partitions.

These are obstructions to those upper-bound certificates, not lower
bounds on the sampled remainder's mean square. Neither Q_r(a_n) nor
E_(r,1)(a_n) is controlled here. No endpoint margin, Laguerre sign,
zero-exclusion range or RH candidate follows.

**Proof.** First, L332 gives

|U(m,n)|≤C τ(m)τ(n)(1+log(mn))².

For σ>1, the sum of this majorant divided by (mn)^σ converges:
expand τ(m) as the number of factorizations m=uv, separate the
logarithmic powers, and use convergence of
Σ_(k≥1)(1+log k)^j k^(-σ) for each fixed j. The same argument
justifies twice differentiating the Dirichlet series on compact
subsets of Re s>1. It also justifies every reciprocal product and
regrouping below. L332 supplies absolute convergence for b_r.

Put Z=ζ(s). In the series for Q_r, write m=ju,n=kv and use the
two absolutely convergent reciprocal series at s and conjugate(s).
After the finite divisor sums have been expanded this gives

r Q_r(a)=1/(Z conjugate(Z))
          ·Σ_(j,k≥1)j^(-s)k^(-conjugate(s))P(log j+log k).

Termwise Dirichlet differentiation therefore yields

r Q_r=−2 Re(Z′/Z)−Re(Z″/Z)/4−|Z′/Z|²/4.

Since Z″/Z=L′+L² and Re(L²)+|L|²=2(Re L)², this proves (1),
including the signs and the mixed derivative coefficient. Division
is valid throughout this half-plane by L332's nonvanishing input.
Unique ratio reduction m=dp,n=dq proves the stated expression for
q_r and hence the series for E_(r,t).

The improved square norm follows from L332's uniform scalar estimate,
not from a fixed finite-head Taylor expansion. With

f_r(v)=exp(v/2+v/r)(1−v/(2r))_+^r,
H_r(m,n)=Σ_(j|m,k|n)μ(m/j)μ(n/k)[f_r(log(jk))−1],

that estimate is

|H_r(m,n)−U(m,n)/r|
 ≤C τ(m)τ(n)(1+log(mn))^4/r².                          (5)

Sum (5) over m=dp,n=dq with the exact factor (d²pq)^(-σ).
Using σ≥1, τ(dp)≤τ(d)τ(p), and
1+log(d²pq)≤(1+2log d)(1+log(pq)), gives

|e_(r,1)(p,q)|≤(C/r²)D_4(p,q),
D_4(p,q)=τ(p)τ(q)(1+log(pq))^4/(pq).                   (6)

L332 proves the convergence of the required d sum and square
summability of D_4. In particular e_(r,1)(1,1)=O(r^(-2)). At each
fixed r the coefficient series is absolutely summable, so dominated
averaging of its squared exponential series retains exactly equal
reduced ratios. This proves the equality and bound in (2). The height
limit is taken first; no estimate at a_n follows from this operation.

For later use, L332's divisor identity gives U(d,d)=−Λ(d)²/4 for
d>1 and U(1,1)=0. Thus

q_r(1,1)=−(1/(4r))Σ_(d≥2)Λ(d)²/d^(2σ)=O(1/r),
b_r(1,1)=O(1/r).                                      (7)

The first constant is uniform because Λ(d)≤log d and σ≥1; the
second is L332's mean formula. Hence the constant coefficient of
E_(r,t) is O((1+|t|)/r). It is not responsible for (4).

We now test both characters. L335 proves that
H(w)=wζ(1+w) is analytic near zero with H(0)=1, and that

F(s)=Σ_(m≥1)λ(m)m^(-s)=ζ(2s)/ζ(s),  Re s>1,
F(1+w)=w J(w),  J(w)=ζ(2+2w)/H(w),  J(0)=ζ(2)>0.      (8)

After shrinking the disk, H and J are analytic and nonzero there.
Their logarithmic derivatives and the derivatives of those
logarithmic derivatives are consequently bounded on a smaller disk.
At real w=1/r this proves, with constants independent of r,

L(1+w)=−1/w+O(1),   L′(1+w)=1/w²+O(1),
l(1+w)=1/w+O(1),    l′(1+w)=−1/w²+O(1),              (9)

where l=F′/F. These are local expansions at the fixed pole/zero,
not derivative estimates at a growing height. Substituting the first
line into (1) at a=0 gives

Q_r(0)=[−r²/4−r²/2+O(r)]/r=−3r/4+O(1).              (10)

For the Liouville evaluation, the absolutely convergent Möbius
series twisted by λ equals 1/F on Re s>1, as proved in L347.
The same differentiated product calculation as for (1) therefore
holds with Z replaced by F, evaluated at the real point σ. When
grouping m=dp,n=dq, λ(dp)λ(dq)=λ(p)λ(q), so this is exactly the
evaluation of the grouped q_r coefficients, with no omitted
equal-ratio collisions. Thus (9) gives

Q_r[λ]=[−2l(σ)−l′(σ)/4−l(σ)²/2]/r
      =[r²/4−r²/2+O(r)]/r=−r/4+O(1).                (11)

L334 proves R_r(0)=−1+O(1/r). L347 proves the exact normalized
Liouville identity and its asymptotic R_r[λ]=−r/4+O(1).
Combining these with (10)–(11) proves (3). The improved ℓ² bound
(2) is compatible with these large values; the tests concern the
sum of coefficient absolute values, not their squares.

Remove the constant frequency using (7). Evaluating the remaining
coefficients at the trivial and Liouville characters gives,
uniformly over all real t,

Σ_((p,q)=1,p≠q)e_(r,t)(p,q)
 =3tr/4+O(1+|t|),
Σ_((p,q)=1,p≠q)e_(r,t)(p,q)λ(p)λ(q)
 =(t−1)r/4+O(1+|t|).                                 (12)

Each character has modulus one at every frequency, so the absolute
value of each sum is at most A_r(t). At t=1 the first identity
proves the first bound in (4). For general t let

M(t)=max(3|t|,|t−1|).

The triangle inequality 1≤|t|+|t−1| shows M(t)≥3/4;
also |t|≤M(t)/3. A common error constant K in (12) therefore gives

A_r(t)≥(r/4)M(t)−K(1+|t|)
      ≥(r/4−K/3)M(t)−K
      ≥3r/16−5K/4                                    (13)

once r/4−K/3≥0. This proves (4) with a constant uniform in t.
The leading minimax value 3/4 is attained at t=1/4; no assertion
that (13) is a sharp estimate of the actual coefficient mass is made.

Finally apply the elementary sampling comparison proved in L347 to
the new nonconstant coefficient vectors e_(2n,t_n). It uses only
absolute summability, not their arithmetic signs. For any positive
summable weights w on a sample interval I, put W=Σw and
x_n=e_(2n,t_n)/sqrt(w). If any x_n is not in ℓ², the certificate
is infinite. Otherwise every nonempty prefix sampling Gram matrix
has diagonal W and operator norm at least W. Cauchy–Schwarz and
the exact finite telescoping identity for the x_n give

sqrt(W)||x_n||_2≥A_(2n)(t_n),
B_I≥sqrt(W)(||x_v||_2+Σ_(j=u)^(v−1)||x_j−x_(j+1)||_2)
   ≥A_(2n)(t_n)  for every n∈I.                       (14)

Here B_I is precisely the prefix-norm vector-Abel budget in L347,
and I=[u,v]. The coarser full-Gram budget obeys the same inequality.
Equation (4) implies B_I≥3N/8−C≥N/4 for large N, uniformly in
every nonempty I⊆[N,2N−1]. Adding back the constant coefficient's
sample norm only increases the triangle certificate. On any
partition into such intervals its normalized squared budget is
therefore at least N/16. On the full interval its squared norm
product is at least cN² instead of o(N). All series and vector
domains satisfy exactly the convergence conditions in L347.

This stops first-order polynomial subtraction as a repair for that
absolute sampling certificate. The failure is already visible from
the different behavior of the fixed zeta pole and the Liouville
zero; no sample-spacing bound is used. It leaves signed estimates
coupling the actual coefficients to a_n, and other normalizations,
untested. The character evaluations do not locate an exception at
a_n, and no lower bound on the actual sampled mean is claimed. ∎

**Mathlib.** Full statement: not checked. Coverage of (1), the
subtracted mean square, the two-character coefficient-mass bound
and the sampling consequence is not checked; the arguments are
given above. L332, L335 and L347 retain these supporting results
recorded as present through L001:
[`ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius),
[`ArithmeticFunction.LSeriesSummable_moebius_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeriesSummable_moebius_iff),
and [`riemannZeta_ne_zero_of_one_lt_re`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#riemannZeta_ne_zero_of_one_lt_re).
Those links were not rechecked. They support the reciprocal expansion
and denominator, not the full statement here. No full library match
or absence from checked sources is asserted.
