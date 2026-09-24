# Lemma 339: a fixed endpoint prime-phase neighborhood

**Hypotheses.** Let r tend to infinity through positive real values,
put L=sqrt(r), y=exp(6L), σ=1+1/(2L), and A=ζ(2)². Use the
finite real sums and weights

W_r(j,k)=(jk)^(−1/2)(1−log(jk)/(2r))_+^r,
J_r={j≥1: j<exp(3r/4)},
S_r[ω]=Σ_(j,k≥1)W_r(j,k)ω(j)conjugate(ω(k)),
T_r[ω]=Σ_(j,k∈J_r)W_r(j,k)ω(j)conjugate(ω(k)).

Here ω is completely multiplicative with |ω(m)|=1. For every
prime p≤y suppose

ω(p)=−exp(iθ_p),  θ_p∈ℝ,  |θ_p|≤1/10.               (1)

There is no restriction on primes greater than y. For Re s>1 set

H_r(s)=∏_(p≤y)(1+p^(−s))²/
              [(1+exp(iθ_p)p^(−s))(1+exp(−iθ_p)p^(−s))],
h_r=H_r(σ).

The functions H_r and numbers h_r may depend on ω as well as r.

**Conclusion.** Uniformly over all assignments satisfying (1),

1≤h_r≤C r^(1/200),                                  (2)

and, with β=412505/3437154<1/8,

limsup_(r→∞) sup_ω |r S_r[ω]/h_r+A/4|≤Aβ,
limsup_(r→∞) sup_ω |r T_r[ω]/h_r+A/4|≤Aβ.            (3)

Consequently, for every sufficiently large r, both sums satisfy

S_r[ω]≤−A h_r/(8r)≤−A/(8r),
T_r[ω]≤−A h_r/(8r)≤−A/(8r).                         (4)

The constant C and the starting r are independent of all phases;
no numerical starting r is asserted. Thus a fixed angular tolerance
of 1/10 radians around −1 suffices at the prime cutoff exp(6sqrt(r)).
The margin exceeds E_r=(1+r)²exp(−r/256), since rE_r→0.

For the actual assignment ω(m)=m^(−ia), condition (1) means the
circular distance of −a log p from π is at most 1/10 for every
prime through y. This statement gives no return time and does not
place such a height at a_n=sqrt(4π²exp(4r)−25), r=2n. It neither
signs a Laguerre coefficient nor changes a zero-exclusion range;
the endpoint and low-index gaps remain open. It is not an RH candidate.

**Proof.** The estimates below retain the product at one complex
argument. They never replace an analytic product by a modulus square.
Let ε=1/10. The absolutely convergent logarithmic power series gives

log H_r(s)=2Σ_(p≤y)Σ_(m≥1)(−1)^(m+1)
                         (1−cos(mθ_p))p^(−ms)/m.     (5)

Since 2(1−cos(mθ_p))≤m²ε², on Re s=σ one has

|log H_r(s)|≤ε² G_r,
G_r=Σ_(p≤y)p^(−σ)/(1−p^(−σ))²,                      (6)

and termwise differentiation gives

|(log H_r)'(s)|≤ε² D_r,
D_r=Σ_(p≤y)log p·p^(−σ)(1+p^(−σ))/(1−p^(−σ))³.       (7)

The prime product is finite and the inner series and their derivatives
converge absolutely and uniformly on every closed smaller half-plane
Re s≥σ_0>1. Thus the logarithm and differentiation are justified.
The identities used in (6) and (7) are
Σ_(m≥1)m q^m=q/(1−q)² and
Σ_(m≥1)m²q^m=q(1+q)/(1−q)³, obtained by differentiating the
geometric series for |q|<1.

We need a bound on D_r of order L, without a factor log r. L338
derives from Mertens' third theorem the reciprocal-prime asymptotic

P(x):=Σ_(p≤x)1/p=log log x+B+o(1).                   (8)

Stieltjes partial summation, including the upper atom, gives

Σ_(p≤y)(log p)/p=(log y)P(y)−∫_2^y P(x)dx/x
                            =log y+o(log y).          (9)

For the last equality, integrate log log x and B explicitly.
If e(x)=P(x)−log log x−B, then e(y)log y=o(log y), and
∫_2^y e(x)dx/x=o(log y): split at a fixed X, bound the remaining
integral by sup_(x≥X)|e(x)| log y, and then let X increase.
This argument requires no quantitative Mertens remainder.

For 0≤q≤1/2 the positive series show

q/(1−q)²≤q+6q²,
q(1+q)/(1−q)³≤q+22q².                               (10)

Indeed, after dividing the tails by q², their maxima occur at
q=1/2 and equal 6 and 22, respectively. Since p^(−σ)≤1/p,
(8)–(10) and the convergence of Σ_(n≥2)(log n)/n² give

G_r≤log log y+O(1)=(1/2)log r+O(1),
D_r≤log y+o(log y)=6L+o(L).                         (11)

All constants here are independent of the phases. In particular
ε²D_r/L≤1/16 eventually, because 6/100<1/16.

At the real point σ, writing q=p^(−σ) gives the exact positive factor

(1+q)²/(1+2q cos θ_p+q²)≥1.                         (12)

The denominator is |1+q exp(iθ_p)|²>0, and cos θ_p≤1 proves
the inequality. Thus h_r≥1. Equations (6) and (11) also give
h_r≤exp(ε²G_r)≤C r^(1/200), proving (2). The logarithm (5)
is real at σ and equals the real logarithm of h_r there; this
follows directly by pairing the conjugate logarithmic series.

Normalize the head product by writing Hhat_r(v)=H_r(σ+iv)/h_r.
Integrating its logarithmic derivative along the vertical segment
from σ to σ+iv in (7) gives, for all real v and sufficiently large r,

|log H_r(σ+iv)−log h_r|≤L|v|/16.

Hence, with t=Lv,

|Hhat_r(v)|≤exp(|t|/16),
|Hhat_r(v)−1|≤exp(|t|/16)−1.                         (13)

The elementary inequality |exp z−1|≤exp(|z|)−1 justifies the
second bound. A second, global bound will be needed for the far tail:
(6), (11) and h_r≥1 give

|Hhat_r(v)|≤C r^(1/200)  for all real v.             (14)

This polynomial bound is essential; (13) alone is unsuitable at
infinite v for a kernel with an algebraic far tail.

For Re s>1 put F_ω(s)=Σ_(m≥1)ω(m)m^(−s). Absolute Euler products
and F_λ(s)=ζ(2s)/ζ(s), with λ the Liouville assignment, give

F_ω(s)F_(conjugate ω)(s)=F_λ(s)² H_r(s) Q_r(s),      (15)

where Q_r is the product over primes p>y of

(1+p^(−s))²/[(1−ω(p)p^(−s))(1−conjugate(ω(p))p^(−s))].

L338's absolute tail estimate, which uses no restriction on those
phases, says on Re s=σ

|Q_r(s)|≤exp(4B_r),  |Q_r(s)−1|≤exp(4B_r)−1,
B_r=Σ_(p>y)Σ_(m≥1)p^(−mσ)/m
       →J_6(1/2)=∫_6^∞ exp(−x/2)dx/x.               (16)

It also proves 4J_6(1/2)<1/15, so eventually 4B_r≤1/15.
Combining (13) and (16), uniformly in all the allowed phases,

|Hhat_r(v)Q_r(σ+iv)−1|
                  ≤exp(|t|/16+1/15)−1.              (17)

This uses |HQ−1|≤|H||Q−1|+|H−1|. Equations (14) and
(16) separately bound its left side by 1+C r^(1/200) on the
entire vertical line.

We next integrate these bounds, keeping the signed reference integral.
Let c=1/2+1/(2L) and use L338's Mellin kernel at α=1/2:

K_r(v)=Γ(r+1)(2r)^(−r)exp(2r(c+iv))
                                  ·(c+iv)^(−r−1)/(2π).

The absolute Mellin representation established there and (15) give

S_r[ω]/h_r−S_r[λ]
 =∫_ℝ K_r(v)F_λ(σ+iv)²
                         [Hhat_r(v)Q_r(σ+iv)−1]dv.  (18)

For each r the Dirichlet factors are absolutely convergent on σ>1
and bounded by ζ(σ), and the Mellin kernel is integrable. Thus
(18) involves no exchange of a conditionally convergent series.

Here are the precise L338 kernel inputs needed for uniform passage
to the scaled integral. On every fixed bounded t interval,

K_r(t/L)/L→sqrt(2/π)exp(2(1/2+it)²),
L F_λ(1+(1/2+it)/L)→ζ(2)(1/2+it).                  (19)

For a fixed sufficiently small δ>0 its proof gives, on |t|≤δL,

r|K_r(t/L)/L| |F_λ(σ+it/L)|²
                         ≤C(1+t²)exp(−t²/4).        (20)

The same proof bounds the integral on |v|>δ by

r∫_(|v|>δ)|K_r(v)| |F_λ(σ+iv)|²dv
                            =O(r^(5/2)exp(−κr))     (21)

for some κ>0. These are actual bounds on the whole complementary
contour, not merely a compact kernel limit. Multiplying (21) by
1+C r^(1/200) still gives o(1), so (14) controls the far part
of (18), uniformly over all assignments.

On |t|≤δL, multiply (20) by the right side of (17). The result
is integrable on ℝ independently of r. Dominated convergence
therefore applies to this common upper bound, using (19). It yields

limsup_(r→∞) sup_ω |rS_r[ω]/h_r−rS_r[λ]|≤A I,

I=sqrt(2/π)exp(1/2)∫_ℝ(1/4+t²)exp(−2t²)
                              [exp(|t|/16+1/15)−1]dt. (22)

No convergence of the phase assignments is needed: the bound is
independent of them before taking the supremum or the limit.

We now verify a strictly sufficient rational bound for I.
Use |t|≤(1+t²)/2 and put z=64/63. The standard Gaussian integral
and an integration by parts give

sqrt(2/π)∫(1/4+t²)exp(−2t²)dt=1/2,
sqrt(2/π)∫(1/4+t²)exp(−(63/32)t²)dt
                                  =(1/4)sqrt(z)(1+z)
                                  ≤(1/2)z^(3/2).

Consequently

I≤[exp(1/2)/2][exp(47/480)z^(3/2)−1]
 <(5/6)[(480/433)(64/63)²−1]
 =412505/3437154=β<1/8.                              (23)

All inequalities can be checked without decimal approximations.
The exponential series gives exp(1/2)≤33/20<5/3: after its
quadratic term 1/8, successive ratios are at most 1/6, so the
tail starting at that term is at most 3/20. Also
exp(x)<1/(1−x) for 0<x<1 by termwise series comparison, applied
at x=47/480. Finally z>1 implies z^(3/2)<z², and direct rational
subtraction gives 1/8−β=68557/13748616>0.

L335 proves rS_r[λ]→−A/4. Equations (22)–(23) prove the first
assertion of (3). L303's omitted-index estimate is phase independent:

|T_r[ω]−S_r[ω]|≤C r exp(−9r/128).

Because h_r≥1, multiplying this estimate by r/h_r gives o(1)
uniformly. This proves the second assertion of (3). Its strict
slack β<1/8 yields (4) for all sufficiently large r, with a
starting value independent of both head and tail phases.

The fixed tolerance removes the shrinking phase-width requirement
of the earlier coefficient-mass argument. It does not control how
quickly the orbit −a log p enters this growing-dimensional box, and
does not establish its occurrence at the prescribed coupled heights.
Thus no sign statement about the actual theta coefficients follows. ∎

**Mathlib.** Full statement: not checked. Coverage of the normalized
paired Euler-product estimate, fixed phase neighborhood, Gaussian
error budget and uniform Mellin passage is not checked. No full
matching theorem or absence from checked sources is claimed.

The reciprocal-prime asymptotic and Mellin estimates are inherited
from L338, with their proofs and qualifications retained there. Its
supporting Mertens input is the standard third theorem recorded in
foundations, with the source Ross G. Pinsky, *Probabilistic Proofs
of Some Generalized Mertens' Formulas Via Generalized Dickman
Distributions* (2018),
[equation (1.1), p. 2](https://arxiv.org/pdf/1809.04888#page=2).
That reference was checked in the earlier step and is not rechecked
here; it supports (8), not this full statement.

The supporting nonvanishing theorem inherited through L335 is
recorded as present in L001:
[`riemannZeta_ne_zero_of_one_lt_re`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#riemannZeta_ne_zero_of_one_lt_re).
It is not rechecked here and does not assert phase stability.
L303 supplies the discrete tail. The elementary algebra and strict
rational margins are reproducible with
`python3 scripts/laguerre/check_endpoint_phase_neighborhood.py`;
that check does not numerically certify an asymptotic or a return time.
