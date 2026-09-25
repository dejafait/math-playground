# Lemma 350: bounded moving-vector cost at the endpoint Mellin width

**Hypotheses.** Use L349's real parameter r≥2, δ=r^(-1/2),
σ=1+δ, full endpoint sum S_r, and absolutely convergent expansion

R_r^w(a)=S_r(a)/|ζ(σ+ia)|²−1
       =Σ_((p,q)=1)b_r^w(p,q)exp(ia log(q/p)).

The coefficients are real, by their divisor-sum formula in L349.
Write F={(p,q): gcd(p,q)=1, p≠q} and ω_(p,q)=log(q/p).
For an integer N≥2 set I_N={N,…,2N−1} and

w_N(ν)=max_(n∈I_N)|b_(2n)^w(ν)|,  W_N=Σ_(ν∈F)w_N(ν),
x_n(ν)=b_(2n)^w(ν)/sqrt(w_N(ν)),
V_N=||x_(2N−1)||_2+Σ_(n=N)^(2N−2)||x_(n+1)−x_n||_2.

Omit coordinates with w_N=0. At the prescribed heights define

a_n=sqrt(4π²exp(8n)−25),
G_N(n,m)=Σ_(ν∈F)w_N(ν)exp(i(a_n−a_m)ω_ν),
ρ_N=||G_N||op/(N W_N),
D_N^w=(1/N)Σ_(n∈I_N)|R_(2n)^w(a_n)|².

**Conclusion.** There are absolute constants r₀ and C such that
the full coefficient sequence is twice continuously differentiable
as an ℓ¹-valued function for real r≥r₀, and

||b_r^w||_1≤C,  ||∂_r b_r^w||_1≤C/r,
||∂_r² b_r^w||_1≤C/r².                              (1)

For all sufficiently large N, the maximum weights and vectors
are well defined, W_N>0, and

W_N≤C,  V_N≤C,  W_N V_N²≤C,
liminf_(N→∞) W_N V_N²≥9.                              (2)

In particular the proposed O(1) moving-vector budget is attained;
it does not tend to zero. L347's vector-Abel inequality gives

D_N^w≤(C sqrt(ρ_N)+C/N)²,  1/N≤ρ_N≤1.                 (3)

Thus ρ_N=o(1) would suffice for a vanishing discrete mean. The
full-Gram certificate ||G_N||op V_N²=o(N) is equivalent to
ρ_N=o(1), by the upper and positive lower bounds in (2). Neither
condition on this sampling norm is proved here. Even D_N^w=o(1)
would leave exceptional sampled indices. No pointwise endpoint
margin, new Laguerre sign, zero exclusion or RH candidate follows.

**Proof.** We first differentiate L349's coefficient integral after
rescaling its entire contour. Put c=1/2+δ, v=δt and

k_r(t)=δ Γ(r+1)(2r)^(-r)exp(2r(c+iδt))
                                  ·(c+iδt)^(-r−1)/(2π),
Q_r(t;a)=ζ(1+δ+i(a+δt))/ζ(1+δ+ia).

L349 proves in coefficient ℓ¹, with every equal-ratio collision
retained, the identity

1+R_r^w(a)=∫_ℝ k_r(t)Q_r(t;a)Q_r(t;−a)dt.            (4)

Both factors have the same t. The complex kernel is retained.
Let Q_r(t) also denote the Dirichlet coefficient sequence of the
first factor, so evaluation multiplies its mth coefficient by
exp(−ia log m). In the commutative algebra ℓ¹ of Dirichlet
coefficients, multiplication is divisor convolution and the norm
is submultiplicative. If e_m denotes its mth coordinate vector,
the absolutely convergent Euler logarithm is

h_r(t)=Σ_(ℓ prime)Σ_(k≥1)
 [ℓ^(-k(1+(1+it)δ))−ℓ^(-k(1+δ))]e_(ℓ^k)/k,
Q_r(t)=exp(h_r(t)).                                   (5)

This identity follows by expanding log(1−z) at each local factor
of L349 and then exponentiating in ℓ¹; both logarithmic series
converge absolutely since δ>0. The exact norm from L349 is

E_r(t)=||Q_r(t)||_1
 =Π_ℓ[1+|exp(−itδ log ℓ)−1|/(ℓ^(1+δ)−1)].            (6)

Define B(σ)=Σ_ℓ log ℓ/(ℓ^σ−1). L349's analytic nonzero factor
H(z)=zζ(1+z) near zero gives

B(1+δ)=δ^(-1)−H'(δ)/H(δ)=δ^(-1)+O(1),
−B'(1+δ)=Σ_ℓΣ_(k≥1)k(log ℓ)²ℓ^(-k(1+δ))
        =δ^(-2)+O(1).                                (7)

The second formula is justified either by differentiating the
locally normally convergent series on σ>1 or the displayed
analytic factor. Its bounded remainder uses the derivative of
H'/H, which is analytic on a fixed disk. Consequently, for large r,

E_r(t)≤exp(C|t|),  E_r(t)≤Cr.                         (8)

These are respectively L349's small-phase bound and its uniform
bound ζ(1+δ)²/ζ(2+2δ), with ζ(1+δ)≤1+1/δ.

Differentiate (5) first with respect to δ, keeping t fixed. The
first derivative has coefficient
(log ℓ)[ℓ^(-k(1+δ))−(1+it)ℓ^(-k(1+(1+it)δ))],
and the second has coefficient
k(log ℓ)²[(1+it)²ℓ^(-k(1+(1+it)δ))−ℓ^(-k(1+δ))].
The sums of their moduli are therefore bounded by

||∂_δ h||_1≤C(1+|t|)/δ,
||∂_δ² h||_1≤C(1+t²)/δ².                            (9)

Since δ'=−δ/(2r) and δ''=3δ/(4r²), the chain rule gives
||∂_r h||_1≤C(1+|t|)/r and
||∂_r² h||_1≤C(1+t²)/r². The exponential derivative identities
Q'=Q*h' and Q''=Q*((h')²+h'') hold in this commutative algebra,
by differentiation of its absolutely convergent power series.
For the ungrouped two-index coefficient sequence
P_r(t)=Q_r(t)⊗Q_r(t), it follows that

||∂_r^j P_r(t)||_1≤C_j E_r(t)²(1+|t|)^j/r^j,
                                      j=0,1,2.        (10)

All derivatives so far are in coefficient ℓ¹ on local compact
r-intervals: the logarithm series and its differentiated series
have the summable majorants in (7) and (9).

We next bound two derivatives of the kernel, including its tails.
Put u=2(1+it)/sqrt(r) and

κ_r=Γ(r+1)exp(r)r^(-r−1/2)/π,
H₀(u)=u−Log(1+u).

An exact simplification of the definition of k gives

k_r(t)=κ_r exp(rH₀(u))/(1+u).                         (11)

Here Re u>0, so the principal logarithm and every denominator
are regular. The standard logarithmic complex Stirling formula
and its analytic remainder, recorded in foundations, give

κ_r=O(1),  α_r:=(log κ_r)'=O(r^(-2)),
α'_r=O(r^(-3)).                                      (12)

For precision, use Γ(r+1)=rΓ(r) in
log Γ(r)=(r−1/2)Log r−r+(log(2π))/2+E(r).
On complex disks of radius r/2 about a large positive r,
E is analytic and O(1/r). Cauchy's estimates give
E'=O(r^(-2)), E''=O(r^(-3)), proving (12). The named input is
the logarithmic complex Stirling formula
[NIST DLMF 5.11.1](https://dlmf.nist.gov/5.11.E1), with its
[sectorial remainder bounds](https://dlmf.nist.gov/5.11#ii).
No differentiation of a merely real asymptotic is used.

Set J(u)=u−Log(1+u)−u²/(2(1+u)). Then J(0)=0 and
J'(u)=u²/(2(1+u)²). Since u'=−u/(2r), the exact derivatives
L_r(t)=∂_r log k_r(t) satisfy

L_r(t)=α_r+u/(2r(1+u))+J(u),
∂_r L_r(t)=α'_r−u/(2r²(1+u))−u/(4r²(1+u)²)
                         −u³/(4r(1+u)²).             (13)

Also, directly from the kernel modulus,

|k_r(t)|=|k_r(0)|(1+(v/c)²)^(-(r+1)/2),
|k_r(0)|≤C.                                         (14)

The last bound follows from (11), since u=2/sqrt(r) at t=0
and rH₀(u)=2+O(r^(-1/2)). On |v|≤c, for large r one has
c≤1, |u|≤3 and

|k_r(t)|≤C exp(−t²/4).                               (15)

Indeed log(1+x²)≥x²/2 for |x|≤1. On the straight segment
from 0 to u, |1+su|≥1. Integrating the formula for J' shows
|J(u)|≤|u|³/6≤C|u|² on this central region. Equations (12)–(13),
|u|²=4(1+t²)/r and |u/(1+u)|≤1 therefore imply

|L_r(t)|≤C(1+t²)/r,
|∂_r L_r(t)|≤C(1+t²)/r².

Using k'=kL and k''=k(L²+L'), we obtain

|∂_r^j k_r(t)|≤C_j r^(-j)(1+|t|^(2j))exp(−t²/4),
                     |v|≤c, j=0,1,2.                (16)

The far contour needs a different majorant. For all Re u>0,
|u/(1+u)|≤1 and |Log(1+u)|≤C(1+|u|). Equations (12)–(13)
give |L_r(t)|≤C(1+|v|), |∂_r L_r(t)|≤C(1+|v|)/r, since
|u|≤C(1+|v|). Thus for j≤2,

|∂_r^j k_r(t)|≤C_j|k_r(t)|(1+|v|)^j.                 (17)

For |v|>c and r≥16, split the power in (14) to retain four
integrable powers after discarding an exponential factor:

|k_r(t)|≤C 2^(-r/4)(1+(v/c)²)^(-4).                  (18)

This follows from (r+1)/2≥r/4+4 and 1+(v/c)²≥2.
On this region, (8), (10), t=sqrt(r)v and r≥1 yield
||∂_r^j P_r(t)||_1≤C_j r²(1+|v|)^j for j≤2.
Leibniz's rule, (17)–(18), dt=sqrt(r)dv and 1/2<c≤1 give

∫_(|v|>c)||∂_r^j(k_r(t)P_r(t))||_1 dt
 ≤C_j r^(5/2)2^(-r/4)
   ·∫_ℝ(1+|v|)²(1+(v/c)²)^(-4)dv
 =O(r^(5/2)2^(-r/4))=O(r^(-j)),  j=0,1,2.            (19)

On |v|≤c, combine (8), (10) and (16) instead. Each derivative
integrand is bounded by r^(-j) times a fixed polynomial in |t|
times exp(−t²/4+2C|t|), an integrable function. Together with
(19), this proves

∫_ℝ||∂_r^j(k_r(t)P_r(t))||_1 dt≤C_j/r^j,
                                      j=0,1,2.        (20)

Differentiation under the full integral is justified as follows.
For r in a compact neighborhood of any sufficiently large r₁,
the differentiated coefficient functions above are continuous.
The exact modulus (14) bounds their far tails by a fixed
integrable power of 1+|t| times a polynomial of degree at most two;
take the neighborhood with r≥16. Their bounded t ranges have
continuous uniform majorants. Dominated differentiation in ℓ¹
therefore applies twice. The central/far split was used only for
bounds on the full integral, so no moving boundary was differentiated.

Finally the map grouping m=dp,n=dq into coprime pairs (p,q) is
a fixed linear contraction from ℓ¹(N²) to the reduced-pair ℓ¹
space. Apply it after the integral in (4) and subtract the fixed
constant coefficient 1. L349 identifies the resulting coefficients
with b_r^w. The contraction commutes with these derivatives,
and (20) proves (1), including every ratio collision.

We now use (1) to bound the maximum weights and the variation.
Write y_n=b_(2n)^w restricted to F. The fundamental theorem of
calculus in ℓ¹ gives, coordinate by coordinate,

w_N(ν)≤|b_(2N)^w(ν)|+∫_(2N)^(4N−2)|∂_r b_r^w(ν)|dr.

Sum and use (1); Tonelli applies to the nonnegative integrand.
This proves W_N≤C+C log 2=O(1). Moreover
||x_n||_2²≤Σ_ν|y_n(ν)|≤C, since |y_n(ν)|≤w_N(ν).
Zero weights have identically zero sampled coordinates and may
be omitted even if a coefficient is nonzero between samples.

Let Δy_n=y_(n+1)−y_n. Integration of the first and second
derivatives in (1) gives uniformly in the indicated indices

||Δy_n||_1≤C/N,
||y_(n+1)−2y_n+y_(n−1)||_1≤C/N².                    (21)

For the second estimate use the exact identity
y_(n+1)−2y_n+y_(n−1)
=∫_0²∫_0² b''_(2n−2+s+t)^w ds dt, restricted to F.

The useful bound on the sum of squared increments is an exact
finite summation identity. For real scalar z_u,…,z_v, put
Δz_n=z_(n+1)−z_n and w=max|z_n|. Then

Σ_(n=u)^(v−1)(Δz_n)²
 =z_v Δz_(v−1)−z_u Δz_u
   −Σ_(n=u+1)^(v−1)z_n(Δz_n−Δz_(n−1)).              (22)

Expand the products and telescope to verify it. For w>0 it implies

Σ_(n=u)^(v−1)(Δz_n)²/w
 ≤|Δz_(v−1)|+|Δz_u|
   +Σ_(n=u+1)^(v−1)|z_(n+1)−2z_n+z_(n−1)|.          (23)

Apply (23) at each retained frequency, with u=N and v=2N−1,
and sum. The first bound in (21) is needed only at the two ends;
the second is summed over the interior. Tonelli and (21) give

Σ_(n=N)^(2N−2)||x_(n+1)−x_n||_2²≤C/N.               (24)

Every term is finite, also directly from W_N<∞ and |y_n|≤w_N.
Cauchy–Schwarz in the finite sample index now yields
Σ_n||x_(n+1)−x_n||_2≤sqrt((N−1)C/N)=O(1).
The endpoint vector is bounded too, proving the upper bounds in
(2). This argument avoids summing separate square roots of the
first-difference ℓ¹ bounds, which would lose a factor sqrt(N).

For the lower bound, L349 proves
liminf_(r→∞)Σ_(ν∈F)|b_r^w(ν)|≥3. At the final sample,

Σ_(ν∈F)|b_(4N−2)^w(ν)|
 ≤sqrt(W_N)||x_(2N−1)||_2≤sqrt(W_N)V_N.

This proves W_N>0 eventually and the lower limit in (2).

To prove (3), use L347's exact vector-Abel summation with these
weights. Every prefix sampling operator has norm at most
sqrt(||G_N||op), since deleting output rows is a contraction.
The nonconstant sampled vector consequently has ℓ² norm at most
sqrt(||G_N||op)V_N. L349 bounds the removed constant coefficient
b_(2n)^w(1,1)=O(1/n), whose normalized sample norm is O(1/N).
The triangle inequality after division by sqrt(N) gives

sqrt(D_N^w)≤sqrt(||G_N||op/N)V_N+C/N
           =sqrt(ρ_N W_N V_N²)+C/N.

This proves (3) using (2). The Gram matrix is positive semidefinite
with diagonal W_N and trace N W_N. Hence W_N≤||G_N||op≤N W_N,
which proves the stated elementary bounds on ρ_N. These bounds
do not establish ρ_N=o(1).

The normalized Hilbert–Schmidt diagnostic
H_N=Σ_(n,m∈I_N)|G_N(n,m)|²/(N W_N)² is equivalent for this
purpose. If λ_j are the nonnegative eigenvalues of G_N/(N W_N),
then Σ_j λ_j=1, max_j λ_j=ρ_N and H_N=Σ_j λ_j². Therefore
ρ_N²≤H_N≤ρ_N. Its vanishing is another formulation of the
unproved sampling bound, not an additional result about the samples.

For comparison with the actual endpoint requirement, a pointwise
|R_(2n)^w(a_n)|≤η<1 would give
S_(2n)(a_n)≥(1−η)/(1+sqrt(2n))² by L349. That margin exceeds
(1+2n)²exp(−2n/256), the required assembled error scale. Neither
the bounded budget (2) nor the conditional mean estimate (3)
proves such a pointwise bound. The sampling estimate, exceptional
indices, and the remaining low-index signs are still unresolved. ∎

**Mathlib.** Full statement: not checked. Coverage of the coefficient
parameter derivatives, maximum-weight discrete energy estimate,
and uniform moving-vector budget is not checked; the proof is
given above. L349 retains as present the supporting results
[`ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius),
[`ArithmeticFunction.LSeriesSummable_moebius_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeriesSummable_moebius_iff),
[`riemannZeta_ne_zero_of_one_lt_re`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#riemannZeta_ne_zero_of_one_lt_re),
and [`riemannZeta_eulerProduct_exp_log`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/EulerProduct/DirichletLSeries.html#riemannZeta_eulerProduct_exp_log).
Those inherited links were not rechecked. They support the Euler
and reciprocal expansions on Re s>1, not the full statement here.
No full library match or absence from checked sources is asserted.
