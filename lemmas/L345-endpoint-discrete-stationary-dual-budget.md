# Lemma 345: the discrete endpoint stationary dual retains an order-N budget

**Hypotheses.** Use the real grouped coefficients h_r(p,q), frequencies
ω_(p,q)=log(p/q), sampled heights a_n=sqrt(4π²exp(8n)−25), and
discrete mean D_N from L344. Only coprime p,q occur. Put

Ω_N={ω_(p,q): exp(−2N)≤|ω_(p,q)|≤exp(N)},
e(t)=exp(2πit),  P_(u,v)(ω)=Σ_(n=u)^v exp(iωa_n),

where N≤u≤v<2N are integers. Fix a smooth nondecreasing function
η:ℝ→[0,1], equal to zero on (−∞,−3/4] and one on [−1/4,∞).
Set W_(u,v)(x)=η(x−u)η(v−x). This equals one on
[u−1/4,v+1/4], vanishes outside [u−3/4,v+3/4], and has derivatives
of every fixed order bounded independently of u,v.

For ω>0 define the finite stationary sum

x_k=(1/4)log(k/(4ω)),
G_ω(k)=(k/4)(1−log(k/(4ω))),
T_(u,v)(ω)=e(1/8)Σ_(k≥1) W_(u,v)(x_k)e(G_ω(k))/(2sqrt(k)).

For ω<0 define T_(u,v)(ω)=conj(T_(u,v)(−ω)). The tested
certificate splits the positive k range into dyadic intervals, uses
classical or Heath-Brown fixed-order derivative bounds of order at
least two, and sums their weighted bounds absolutely. Subdivision,
the trivial bound, and any fixed finite set of derivative orders and
comparison constants are allowed. Moving h_(2n) weights are handled
by absolute Abel summation, as in L344. This specifies a certificate,
not a hypothesis on the actual phase cancellation.
In the budget comparisons below, each chosen derivative estimate has
one fixed positive implicit constant. Taking arbitrary smaller
constants in an O-bound is not an allowed improvement of a certificate.

**Conclusion.** Uniformly in all the displayed partial intervals and
ω∈Ω_N, as N→∞,

P_(u,v)(ω)=T_(u,v)(ω)+O(exp(−N)).                       (1)

More precisely the error is
O((|ω|exp(4u))^(−1/2)+|ω|exp(−4u)). Endpoint transitions are
included in T; no separation of an endpoint slope from an integer
is required. At r∈[2N,4N], frequencies outside Ω_N have total
nonconstant coefficient mass

O(N^17 exp(−2N)+N^9 exp(−N)).                          (2)

After exact Abel summation with the moving coefficients, replacing
every partial P by T changes the normalized off-diagonal part of
D_N by O(N^8 exp(−N)), in addition to (2). Thus neither a discarded
frequency tail nor a transform error prevents this test.

Nevertheless the best scale of the specified dual certificates on
P_(u,v) is comparable to v−u+1, uniformly over Ω_N. Consequently
their absolute moving-weight certificate for the off-diagonal mean
has a positive liminf, against the required o(1). This is a lower
bound on a bound produced by the method, not on D_N. It supplies
no fixed numerical lower bound such as 1/4 for that mean or its
certificate, and no endpoint sign or zero-exclusion extension.

**Proof.** First control the frequencies on which the transform is
needed. L333's absolutely convergent divisor majorant, with
σ=1+1/r, gives

|g_r(k,l)|≤(e+1)²d_4(k)d_4(l)(kl)^(−σ).

Grouping by reduced ratio and using |log(k/l)|≤log(kl), one gets

Σ_(p,q)|h_r(p,q)|≤(e+1)²ζ(σ)^8=O((r+1)^8),
Σ_(p,q)|h_r(p,q)| |ω_(p,q)|
 ≤8(e+1)²ζ(σ)^7 Σ_(m≥1)(log m)m^(−σ)
 =O((r+1)^9).                                         (3)

The factor eight counts which of the eight ordered factors carries
the logarithm. All summands in the majorant are nonnegative, so
Tonelli applies. The elementary integral estimates in L333 give
ζ(σ)≤r+1 and the logarithmic series at most r²+r log 2.
Thus |ω|>exp(N) contributes O(N^9 exp(−N)). L344's inverse-gap
bound handles 0<|ω|<exp(−2N), proving (2). These estimates retain
every collision before taking the absolute value of h.

We prove a uniform smooth transform before estimating its main sum.
For ω>0 put F(x)=ωexp(4x). Smooth Poisson summation gives

Σ_(n∈ℤ) W_(u,v)(n)e(F(n))
 =Σ_(k∈ℤ)∫_ℝ W_(u,v)(x)e(F(x)−kx)dx.                 (4)

The left side is exactly Σ_(n=u)^v e(F(n)). For each fixed ω,u,v,
the integrand is smooth with compact support, and two integrations
by parts give absolute convergence of its Fourier series; this
justifies the named Poisson summation formula here. Bounds uniform
in the growing parameters require the following local calculation.

Take a fixed smooth partition of unity θ_j(x)=θ(x−j), j∈ℤ, with
support in [j−1,j+1]. It can be constructed by dividing a positive
bump on (−1,1) by the positive periodic sum of its integer translates.
Only finitely many pieces meet the support of W. On the jth piece
write x=j+t, Q=ωexp(4j), and b_j(t)=W(j+t)θ(t). Then the Fourier
integral is

e(−kj)∫ b_j(t)e(Qexp(4t)−kt)dt,                       (5)

where b_j is supported in [−1,1] with uniformly bounded smooth
norms. The prefactor is one for integer j,k. For

4exp(−8)Q≤k≤4exp(8)Q

write s=k/Q. The phase φ_s(t)=exp(4t)−st has its unique stationary
point t_s=(1/4)log(s/4) in [−2,2]. On [−3,3] its second
derivative is bounded above and below by fixed positive constants.
The stationary expansion, uniformly even when t_s is outside the
support of b_j, is

∫ b_j(t)e(Qφ_s(t))dt
 = b_j(t_s)e(Qφ_s(t_s)+1/8)/sqrt(Qφ_s''(t_s))
   +O(Q^(−3/2)).                                      (6)

Here is a proof of the uniform error used in (6). Make the exact
change y=sgn(t−t_s)sqrt(2(φ_s(t)−φ_s(t_s))). Its derivative is
bounded above and below, including at t_s, and its smooth inverse
has uniform derivatives because s lies in a fixed compact interval
and φ_s'' stays positive. The transformed amplitude A_s(y),
extended by zero, is supported in a fixed compact interval with
uniform smooth norms. The transformed phase is φ_s(t_s)+y²/2.
With Fourier convention Â(ξ)=∫ A(y)e(−ξy)dy, the damped Gaussian
integral and Fourier inversion give

∫ A(y)exp(πiQy²)dy
 = e(1/8)Q^(−1/2)∫ Â(ξ)exp(−πiξ²/Q)dξ.

One may insert exp(−εy²) first and let ε decrease to zero: the
Gaussian Fourier factors are bounded by a constant times Q^(−1/2),
so integrability of Â justifies the limit. Since
|exp(−πiξ²/Q)−1|≤πξ²/Q and ∫ ξ²|Â(ξ)|dξ is uniformly bounded
by four integrations by parts, the error is O(Q^(−3/2)). Also
A_s(0)=b_j(t_s)/sqrt(φ_s''(t_s)). This proves (6), including a
stationary point crossing either edge of the smooth amplitude.

There are O(Q) integers in this stationary range, so their errors
sum to O(Q^(−1/2)). Outside it, including every k≤0, the phase
derivative in (5) has magnitude at least c(Q+|k|) on [−1,1].
Twice integrating by parts, with no amplitude boundary terms,
gives O((Q+|k|)^(−2)) per mode; derivatives of the phase contribute
only bounded factors since they are O(Q). The sum is O(Q^(−1)).
Thus the total local error is O(Q^(−1/2)) for Q≥1.

At a stationary point F'(x_k)=k one has

F''(x_k)=4k,  F(x_k)−kx_k=G_ω(k).

Summing the local main terms uses Σ_j θ_j(x_k)=1. The nonzero
pieces have j≥u−1, and hence their errors form a geometric series:

Σ_(j≥u−1)(ωexp(4j))^(−1/2)
 ≤C(ωexp(4u))^(−1/2).

This proves the transform with that error for the pure exponential
phase, uniformly in the length v−u. The relevant Q are at least
a fixed multiple of exp(2N) on Ω_N. In particular the smooth
endpoint transitions have already been summed; no hard-cutoff
endpoint error has been discarded.

For the actual phase, set b=25/(4π²). Direct rationalization gives

|a_n/(2π)−exp(4n)|
 = b/[exp(4n)+sqrt(exp(8n)−b)]≤C exp(−4n).

The inequality |e(s)−e(t)|≤2π|s−t| and a geometric sum bound the
change in a partial sum by C|ω|exp(−4u). This proves the precise
error in (1). On Ω_N its two terms are O(exp(−N)) and
O(exp(−3N)). Conjugation treats ω<0. This is an approximation
to the exact square-root phase with a controlled error, not an
unquantified replacement of the sampling heights.

To check the moving coefficients explicitly, for each frequency
write w_n=h_(2n)(p,q). Abel summation gives

Σ_(n=u)^v w_n exp(iωa_n)
 =w_v P_(u,v)(ω)
  +Σ_(t=u)^(v−1)(w_t−w_(t+1))P_(u,t)(ω).               (7)

For precision, if U_(u,t)(ω) bounds the modulus of the dual partial
sum, the sufficient fully weighted target on [N,2N−1] is

Q_N(U)=(1/N)Σ_(ω∈Ω_N)
 [|h_(4N−2)(p,q)| U_(N,2N−1)(ω)
  +Σ_(t=N)^(2N−2)|h_(2t)(p,q)−h_(2t+2)(p,q)| U_(N,t)(ω)]
 =o(1).                                                (7a)

Here (p,q) is the unique reduced ratio for ω. A partial-sum saving
o(N) alone, without this coefficient and variation sum, would not
prove D_N=o(1). The argument below tests (7a), as well as the
unweighted partial-sum scale. Its negligible errors are as follows.

Replacing each P by T incurs at most

C exp(−N)(|w_v|+Σ_(t=u)^(v−1)|w_t−w_(t+1)|)
 ≤2C exp(−N)Σ_(n=u)^v |w_n|.

Summing over Ω_N, applying (3), and dividing by N gives
O(N^8 exp(−N)). No smoothness in r or freezing of h_(2n) has
been assumed. Together with (2), this proves the error assertion
for D_N; all these sums are absolutely convergent.

It remains to test the dual main sum. Exact differentiation gives

G_ω'(k)=−(1/4)log(k/(4ω)),
G_ω^(d)(k)=(−1)^(d−1)(d−2)!/(4k^(d−1)),  d≥2.        (8)

On K≤k<2K its amplitude has supremum plus total variation
O(K^(−1/2)), since x_k'=1/(4k) and W has bounded derivatives.
The second-derivative test bounds every unweighted partial sum
of at most K terms by O(sqrt(K)). Weighted Abel summation
therefore costs O(1) on each whole dyadic interval, including the
transition intervals. The supporting theorem and its hypotheses are
the classical second-derivative estimate stated in the foundations.
There are O(v−u+1) such intervals: the support endpoints have
k ratio exp(4(v−u+3/2)). Thus the available bound is

|T_(u,v)(ω)|=O(v−u+1).                                (9)

We must check that the certificate cannot give a little-o saving,
rather than confuse (9) with a lower bound on the sum. Put
m=v−u+1. On the plateau where W=1 the k ratio is exp(4m−2).
This contains at least c m whole dyadic intervals, uniformly for
integers m≥1 (already exp(2)>4 when m=1). All their K tend to
infinity uniformly on Ω_N. On such an interval the amplitude is
exactly 1/(2sqrt(k)), whose relevant absolute variation norm is
comparable to K^(−1/2).

Consider a subinterval with ℓ integer terms. The classical dth
derivative bound has, among its nonnegative terms, a scale

ℓ λ^(1/(2^d−2)),  λ comparable to K^(1−d).

The upper comparison hypothesis |G^(d)|≤Aλ with fixed A prevents
artificially reducing λ. After weighting, this term is at least a
fixed positive multiple of

ℓ K^(−1/2−(d−1)/(2^d−2)) ≥ ℓ/K.                      (10)

The inequality follows from 2(d−1)≤2^d−2 for every d≥2,
with equality at d=2: on increasing d by one, the two sides
increase by 2 and 2^d, respectively. Heath-Brown's fixed d≥3 estimate has first
term ℓ^(1+ε)λ^(1/(d(d−1))). Its weighted scale is at least

ℓ^(1+ε)K^(−1/2−1/d)≥ℓ/K.                             (11)

The other terms of either theorem are nonnegative and cannot lower
these budgets. The weighted trivial estimate is also at least a
constant times ℓ/K. Empty intervals contribute zero; singleton
estimates satisfy the same comparison directly. These statements
refer to the scales on the right sides of the standard bounds,
not to the values of the exponential sums.

For any subdivision of a plateau dyadic interval, the counts ℓ sum
to a quantity comparable to K. Thus even the minimum of the
allowed fixed finite collection of certificates costs at least a
fixed c_0>0 on that interval. Summing the c m plateau intervals
gives a budget at least c_1 m. The second-derivative estimate gives
the matching upper scale (9). Taking the minimum with the original
trivial bound m preserves a positive multiple of m. All comparison
constants may depend on the chosen finite collection of orders,
but not on N, ω, u or v. The conclusion does not cover orders
growing with N or signed combinations of different dual blocks.

Finally, substituting partial-sum budgets at least c_1(t−u+1)
into the absolute version of (7) costs at least

c_1[(v−u+1)|w_v|
       +Σ_(t=u)^(v−1)(t−u+1)|w_t−w_(t+1)|]
 ≥c_1 Σ_(n=u)^v |w_n|,                                (12)

by the telescoping inequality proved in L344. The same holds
after partitioning the original n interval. L344 gives total
grouped nonconstant mass at least 1−O(1/N); removing the two
tails in (2) leaves the same lower bound on its normalized average
over Ω_N. Equation (12) consequently gives liminf Q_N(U)>0 for
each of the specified certificates. Negligible transform errors
cannot turn that absolute certificate into o(1).

The stationary geometry explains the missing information without
supplying it. Transforming G back has stationary frequencies −n,
at k=4ωexp(4n). Its phase is G(k)+nk=ωexp(4n), its amplitude
is (2sqrt(k))^(−1)/sqrt(|G''(k)|)=1, and its stationary phase
factor cancels e(1/8). Thus at the stationary-main-term level the
original unit-amplitude phases return. This algebra is not a second
error estimate or a proof that all ways of using the dual must fail.
New signed information across its blocks or frequencies remains
possible. Neither (10)–(12) nor this observation signs the actual
mean, locates an exceptional sampled pair, or proves RH. ∎

**Mathlib.** Full statement: not checked. Coverage of the smooth
Poisson transform, uniform stationary remainder, weighted derivative
budget and moving-coefficient estimate is not checked; no library
match or absence is asserted. The uniform stationary remainder is
proved above. [NIST DLMF §2.3(iv)](https://dlmf.nist.gov/2.3#iv)
was checked as a supporting reference for the stationary-phase
method, not as a match for the uniform sampled statement. The
derivative bounds are those already recorded in the foundations:
[Robert, Theorem 1 and Theorem 3, equation (17)](https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf)
and [Heath-Brown, equation (1), p. 1, and Theorem 1, p. 3](https://arxiv.org/pdf/1601.04493).
Heath-Brown's primary source was rechecked during review, including
the derivative comparison hypotheses and every term of both bounds;
Robert's source was not rechecked. Equations (8)–(11) check their
application here. They supply no actual sign and no Mathlib coverage
claim. L333 retains the
supporting references recorded as present through L001:
[`ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius),
[`ArithmeticFunction.LSeriesSummable_moebius_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeriesSummable_moebius_iff),
and [`riemannZeta_ne_zero_of_one_lt_re`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#riemannZeta_ne_zero_of_one_lt_re).
These unrechecked sources support the reciprocal expansion and
nonzero denominator, not the full statement proved here.
