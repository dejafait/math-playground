# Lemma 342: an aggregate endpoint prime-phase budget

**Hypotheses.** Let r tend to infinity through positive real values.
Put L=sqrt(r), y=exp(6L), σ=1+1/(2L), A=ζ(2)², and

W_r(j,k)=(jk)^(−1/2)(1−log(jk)/(2r))_+^r,
J_r={j≥1: j<exp(3r/4)},
S_r[ω]=Σ_(j,k≥1)W_r(j,k)ω(j)conjugate(ω(k)),
T_r[ω]=Σ_(j,k∈J_r)W_r(j,k)ω(j)conjugate(ω(k)).

Here ω is completely multiplicative with |ω(m)|=1. These sums
are finite and real, the latter by exchanging j and k. For p≤y
write ω(p)=−exp(iθ_p), with arbitrary real representatives θ_p,
and define

q_p=p^(−σ),
d_r(p)=(log p)q_p(1+q_p)/(1−q_p)^3,
B_r(θ)=Σ_(p≤y)(1−cos θ_p)d_r(p).

Assume only the aggregate budget

B_r(θ)≤L/32.                                         (1)

There is no restriction on primes p>y. For Re s>1 define

H_r(s)=∏_(p≤y)(1+p^(−s))²/
              [(1+exp(iθ_p)p^(−s))(1+exp(−iθ_p)p^(−s))],
h_r=H_r(σ).

Both H_r and h_r depend on the assignment as well as on r.

**Conclusion.** For every such assignment,

1≤h_r≤(1+2sqrt(r))^4.                               (2)

With β=412505/3437154<1/8, uniformly over assignments satisfying
(1),

limsup_(r→∞) sup_ω |r S_r[ω]/h_r+A/4|≤Aβ,
limsup_(r→∞) sup_ω |r T_r[ω]/h_r+A/4|≤Aβ.            (3)

Consequently, for all sufficiently large r, uniformly in the head
phases and in every larger-prime completion,

S_r[ω]≤−A h_r/(8r)≤−A/(8r),
T_r[ω]≤−A h_r/(8r)≤−A/(8r).                         (4)

No numerical starting r is asserted. The margin dominates
E_r=(1+r)²exp(−r/256), because rE_r→0.

For all sufficiently large r, the budget set contains the full
coordinate box |θ_p|≤1/10 of L339. It is strictly larger: every
assignment on primes p≤r is allowed if θ_p=0 for r<p≤y,
with primes above y still arbitrary. Thus many individual phases
may lie outside the old box without losing (4).

For actual phases ω(m)=m^(−ia), the budget reads
Σ_(p≤y)(1+cos(a log p))d_r(p)≤L/32. This is a sufficient
negative-sign condition, not a statement about its frequency or
occurrence at a_n=sqrt(4π²exp(4r)−25), r=2n. Its measure and
return times remain unestimated here. No Laguerre sign, exclusion
range, or RH candidate follows.

**Proof.** We first remove the coordinatewise restriction in the
paired logarithmic derivative. For every real θ and integer m≥1,

1−exp(imθ)=(1−exp(iθ))Σ_(j=0)^(m−1)exp(ijθ).

Taking absolute values and squaring gives

1−cos(mθ)≤m²(1−cos θ).                              (5)

This includes θ≡0 mod 2π and needs no small-angle assumption.
The analytic logarithm defined by the absolutely convergent
power series has the exact expansion

log H_r(s)=2Σ_(p≤y)Σ_(m≥1)(−1)^(m+1)
                          (1−cos(mθ_p))p^(−ms)/m.    (6)

Exponentiating the series gives the displayed product for H_r.
The prime sum is finite, and the inner series and their derivatives
converge uniformly on each closed half-plane Re s≥σ_0>1. Thus
termwise differentiation is justified. On Re s=σ, (5) implies

|(log H_r)'(s)|
 ≤2Σ_(p≤y)(log p)(1−cos θ_p)Σ_(m≥1)m²q_p^m
 =2B_r(θ)≤L/16.                                    (7)

Here Σ_(m≥1)m²q^m=q(1+q)/(1−q)^3 follows by applying
q d/dq twice to the geometric series for |q|<1.

At s=σ each Euler factor equals

(1+q_p)²/(1+2q_p cos θ_p+q_p²)≥1.                  (8)

Its denominator is |1+q_p exp(iθ_p)|²>0. The paired series
(6) is real at σ, so it gives the real logarithm of this positive
product there. In particular h_r≥1.

The global size estimate must also permit large individual angles.
For every real v the triangle and reverse triangle inequalities give

|H_r(σ+iv)|≤∏_(p≤y)((1+q_p)/(1−q_p))²
           ≤∏_(p≤y)(1−q_p)^(−4)
           ≤ζ(σ)^4≤(1+2L)^4.                       (9)

The middle inequality uses (1+q)(1−q)=1−q²≤1.
The absolutely convergent Euler product gives the next one; the
final bound follows from
Σ_(n≥1)n^(−σ)≤1+∫_1^∞x^(−σ)dx=1+1/(σ−1).
Equation (9) at v=0 proves (2).

Normalize by Hhat_r(v)=H_r(σ+iv)/h_r. Integrating (7) along
the vertical segment, and putting t=Lv, yields

|log H_r(σ+iv)−log h_r|≤|t|/16,
|Hhat_r(v)|≤exp(|t|/16),
|Hhat_r(v)−1|≤exp(|t|/16)−1.                         (10)

The last step uses |exp z−1|≤exp(|z|)−1. Separately, (9)
and h_r≥1 give the phase-uniform global bound

|Hhat_r(v)|≤(1+2L)^4=O(r²).                         (11)

It is (11), not the exponentially growing bound in (10), that
will be used at infinite v.

For Re s>1 write F_ω(s)=Σ_(m≥1)ω(m)m^(−s) and
F_λ(s)=ζ(2s)/ζ(s), where λ(p)=−1. Absolute Euler products,
as in L338, give at a single complex argument

F_ω(s)F_(conjugate ω)(s)=F_λ(s)²H_r(s)Q_r(s),        (12)

where Q_r is the product over p>y of
(1+p^(−s))²/[(1−ω(p)p^(−s))(1−conjugate(ω(p))p^(−s))].
This analytic product is not replaced by a modulus square.
L338's phase-independent prime-tail estimate states that, on
Re s=σ,

|Q_r(s)|≤exp(4U_r),   |Q_r(s)−1|≤exp(4U_r)−1,
U_r=Σ_(p>y)Σ_(m≥1)p^(−mσ)/m
   →J_6(1/2)=∫_6^∞exp(−x/2)dx/x,
4J_6(1/2)<1/15.                                    (13)

Hence 4U_r≤1/15 for all sufficiently large r, independently
of every phase. Combining (10) and (13) gives

|Hhat_r(v)Q_r(σ+iv)−1|
 ≤exp(|t|/16+1/15)−1.                               (14)

Combining (11) and (13) separately bounds this expression by
1+C r² on the entire line.

Use the Mellin representation and estimates proved in L338 with
c=1/2+1/(2L):

K_r(v)=Γ(r+1)(2r)^(−r)exp(2r(c+iv))
                            ·(c+iv)^(−r−1)/(2π).

Inserting (12) in that representation and subtracting the
Liouville assignment gives

S_r[ω]/h_r−S_r[λ]
 =∫_ℝK_r(v)F_λ(σ+iv)²
                     [Hhat_r(v)Q_r(σ+iv)−1]dv.     (15)

For each r, the Dirichlet factors on σ>1 are bounded in absolute
sum by ζ(σ), and the kernel is integrable. Thus the formula and
subtraction involve only absolutely convergent integrals and sums.

We recall the exact contour bounds needed to make (15) uniform.
With u=1/2+it, the limits on every bounded t interval are

K_r(t/L)/L→sqrt(2/π)exp(2u²),
L F_λ(1+u/L)→ζ(2)u.                                (16)

For a fixed sufficiently small δ>0, L338 proves

r|K_r(t/L)/L| |F_λ(σ+it/L)|²
               ≤C(1+t²)exp(−t²/4)  on |t|≤δL,      (17)
r∫_(|v|>δ)|K_r(v)| |F_λ(σ+iv)|²dv
               =O(r^(5/2)exp(−κr))                 (18)

for some κ>0. Multiplication of (18) by 1+C r² still tends
to zero. On |t|≤δL, (17) times the right side of (14) is
integrable on ℝ independently of r and of all assignments.
Apply dominated convergence to this common upper bound using
(16); on the complement use (18). The result is

limsup_(r→∞) sup_ω |rS_r[ω]/h_r−rS_r[λ]|≤A I,
I=sqrt(2/π)exp(1/2)∫_ℝ(1/4+t²)exp(−2t²)
                           [exp(|t|/16+1/15)−1]dt.  (19)

The supremum is bounded before taking the limit; no convergence
of the assignments themselves is assumed.

This is the same Gaussian budget as in L339. Its exact rational
bound uses |t|≤(1+t²)/2 and z=64/63 to give

I≤[exp(1/2)/2][exp(47/480)z^(3/2)−1]
 <(5/6)[(480/433)(64/63)²−1]
 =412505/3437154=β<1/8.                              (20)

The first inequality follows by integrating the Gaussian and its
second moment with exponents −2t² and −(63/32)t². The next
uses exp(1/2)<5/3, exp(x)<1/(1−x) for 0<x<1, and z>1.
L339 proves these elementary bounds and the exact positive slack
1/8−β=68557/13748616.

L335 gives rS_r[λ]→−A/4. Thus (19)–(20) prove the first
bound in (3). L303's omitted-index estimate uses only the absolute
weights and holds for every unit assignment:

|T_r[ω]−S_r[ω]|≤C r exp(−9r/128).

Multiplication by r/h_r≤r makes this uniformly o(1), proving
the second bound in (3). Since β<1/8, both real normalized sums
are eventually at most −A/8. This proves (4), uniformly over
the entire budget set and all completions.

Finally we check that the new condition really enlarges the old
one. L339 establishes the phase-independent estimate

D_r:=Σ_(p≤y)d_r(p)≤6L+o(L).

When |θ_p|≤1/10, 1−cos θ_p≤θ_p²/2≤1/200, so
B_r(θ)≤(3/100+o(1))L<L/32 eventually. This proves containment.

For the stronger example, leave every θ_p with p≤r arbitrary
and set θ_p=0 for r<p≤y. For large r one has r<y. Since
q_p≤1/p≤1/2,

d_r(p)≤12(log p)/p.

Therefore, for r≥2,

B_r(θ)≤24Σ_(p≤r)(log p)/p
 ≤24(log r)Σ_(2≤m≤r)1/m
 ≤24(log r)(1+log r)=o(sqrt(r)).                     (21)

The harmonic-sum bound follows by integral comparison. Thus
every such assignment satisfies (1) eventually, uniformly in
all its small-prime phases. Choosing θ_2=π places one of them
outside L339's box. This does not conflict with L337's positive
completion fixing only the smallest primes: here the primes
between r and exp(6sqrt(r)) are constrained instead.

For actual phases, exp(iθ_p)=−p^(−ia), so
cos θ_p=−cos(a log p), proving the final interpretation of (1).
None of the inequalities supplies an actual visit or a sign at the
prescribed coupled heights. The enlarged sufficient region leaves
those arithmetic and global positivity gaps unresolved. ∎

**Mathlib.** Full statement: not checked. Coverage of the aggregate
phase inequality, its normalized Euler-product comparison and the
uniform Mellin conclusion is not checked. No full matching theorem
or absence from checked sources is claimed. The chord inequality,
large-angle product bound and strict enlargement are proved above.

The supporting nonvanishing theorem inherited through L335 and
L338 is recorded as present in L001:
[`riemannZeta_ne_zero_of_one_lt_re`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#riemannZeta_ne_zero_of_one_lt_re).
It is not rechecked here and is not a match for phase stability.
The prime-tail and D_r estimates retain the supporting Mertens
third theorem recorded in foundations and in Ross G. Pinsky,
*Probabilistic Proofs of Some Generalized Mertens' Formulas Via
Generalized Dickman Distributions* (2018),
[equation (1.1), p. 2](https://arxiv.org/pdf/1809.04888#page=2).
That external reference was checked in the earlier step and is
not rechecked here; its Mathlib coverage is not checked. It supports
prime estimates, not the full statement (1)–(4).

The contour bounds, reference Liouville asymptotic, discrete tail
and rational Gaussian budget are the proved inputs cited in the
proof. The existing check
`python3 scripts/laguerre/check_endpoint_phase_neighborhood.py`
reproduces the paired-log algebra and strict rational budget;
it does not certify an asymptotic sign or a return time numerically.
