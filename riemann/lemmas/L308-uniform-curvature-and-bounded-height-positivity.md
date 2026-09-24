# Lemma 308: uniform theta curvature gives bounded-height all-level positivity

**Hypotheses.** Let k(u)=K(|u|) be the positive smooth even actual theta kernel of L019 and L048, and put W=−log k. For integers n≥1 use L267's definitions

A_n(t)=∫_R s^(2n)k(s+t)k(s−t)ds,
V_n=∫_R t²A_n(t)dt / ∫_R A_n(t)dt,
Ξ(a+iy)Ξ(a−iy)=Σ_(n≥0)D_n(Ξ;a)y^(2n).

**Conclusion.** For every real u and every integer n≥1,

W''(u)>17,                         V_n<1/34.

Consequently D_n(Ξ;a)>0 for every n≥1 and every real |a|≤sqrt(17). No nonreal zero of Ξ can have real part in that interval. In particular, the bound settles every index on 7/2≤|a|≤4, not just sufficiently large indices.

This is a bounded-height statement. It proves neither a bound of order log(n+2)/(n+1) for V_n nor the signs at unbounded heights required for RH.

**Proof.** First sharpen the curvature estimate by retaining the rational part of each summand's curvature. For u≥0 put v=πexp(2u)>3, and write L019's positive summands as

k_m(u)=4m²v(2m²v−3)exp(u/2−m²v),
w_m=k_m/k,                         ℓ_m=log k_m.

Termwise differentiation gives

ℓ_m'=9/2−2m²v+6/(2m²v−3),
−ℓ_m''=g(m²v),                    g(x)=4x+24x/(2x−3)².

The theta series and its first two derivatives converge uniformly on compact u intervals. Their tails are dominated by a polynomial in m times exp(−πm²), after allowing constants depending on the interval. The same bounds justify the weighted first and second slope moments. Differentiating log k therefore gives the exact identity

W''=Σ_m w_m g(m²v)−Var_w(ℓ_m').                 (1)

For every x≥3, g(x)>19. Indeed, set y=2x−3≥3 and t=y−4≥−1. Then

(g(x)−19)y²=2y³−13y²+12y+36
 =4+4t+11t²+2t³
 ≥4+4t+9t²
 =9(t+2/9)²+32/9>0.                            (2)

Thus the weighted mean in (1) is strictly greater than 19. We next bound the variance by 2 uniformly. For m≥2,

w_m≤k_m/k_1
 =m²(2m²v−3)/(2v−3) exp(−(m²−1)v)
 ≤2m⁴ exp(−(m²−1)v),

because 2v−3≥v. The positive slope difference obeys

0<ℓ_1'−ℓ_m'
 =2(m²−1)v+6/(2v−3)−6/(2m²v−3)
 ≤2(m²−1)v+2
 ≤(20/9)(m²−1)v,                              (3)

where (m²−1)v≥9. Centering at ℓ_1' instead of the weighted mean can only increase a second moment. Hence

Var_w(ℓ_m')≤(800/81)v² Σ_(m≥2)m⁴(m²−1)² exp(−(m²−1)v).       (4)

Here the first polynomial weight is 2⁴(2²−1)²=144. If b_m=m⁴(m²−1)², then for m≥2

b_(m+1)/b_m
 =((m+1)/m)⁴ [m(m+2)/((m−1)(m+1))]²
 ≤(3/2)⁴(8/3)²=36.

The second bracket is at most 8/3 because
8(m²−1)−3m(m+2)=(m−2)(5m+4)≥0.
For m=2+j with integer j≥0, also m²−1≥3+5j. Therefore

Σ_(m≥2)b_m exp(−(m²−1)v)
 ≤144 exp(−3v)/(1−36exp(−5v))
 <180 exp(−3v).                                (5)

For the strict denominator bound, e³>20 implies e^(5v)>e^15>20⁵>180, so 36exp(−5v)<1/5. The elementary exponential bound follows already from Σ_(j=0)^8 3^j/j!=89641/4480>20. Finally, v²exp(−3v) decreases for v≥3, and

v²exp(−3v)≤9exp(−9)<9/8000.

Combining (4) and (5) gives

Var_w(ℓ_m')<(800/81)·180·9/8000=2.

Equations (1) and (2) yield W''>17 on u≥0. Smoothness and evenness from L048 extend this inequality to every real u, including zero.

Fix any real s and set

q_s(t)=k(s+t)k(s−t),
U_s(t)=−log q_s(t)=W(s+t)+W(s−t).

Then U_s'(0)=0 and U_s''(t)>34 everywhere. Integration from zero, with the sign of t accounted for, gives

tU_s'(t)>34t²                         (t≠0).                (6)

There is no boundary term in integration by parts:

∫_R tU_s'(t)q_s(t)dt=∫_R q_s(t)dt.                          (7)

To check this directly, q_s'=−U_s'q_s. Differentiating L019's summands once, factoring out the first Gaussian, and using the convergent sum of m⁶exp(−π(m²−1)) gives, for some finite constant C,

|k(u)|+|k'(u)|≤C exp(13|u|/2−πexp(2|u|)).

Evenness supplies the negative half-line. For fixed s this bound makes q_s and t q_s' absolutely integrable and t q_s(t) tend to zero at both ends. Integrating (t q_s)' proves (7). Positivity of q_s and the strict inequality (6) now imply

∫_R t²q_s(t)dt < (1/34)∫_R q_s(t)dt.

Multiply by s^(2n) and integrate over s. All integrals are finite by the superexponential domination in L267; Tonelli applies to the nonnegative integrands. Strictness persists since the difference is positive for every s and the weight is positive off s=0. Division by the positive total mass proves V_n<1/34.

By L267, with c_n=2^(2n−1)/(2n)!>0,

D_n(Ξ;a)≥c_n(∫_R A_n(t)dt)(1−2a²V_n).

For a²≤17 the last factor is strictly positive, also at a²=17 because the variance bound is strict. This proves every asserted sign.

Finally, for such a, the entire Taylor product has D_0(Ξ;a)=Ξ(a)²≥0 and D_n(Ξ;a)>0 for n≥1. For any real b≠0 its convergent value

Ξ(a+ib)Ξ(a−ib)=Σ_(n≥0)D_n(Ξ;a)b^(2n)

is strictly positive. Thus Ξ(a+ib) cannot vanish. This exclusion uses all established coefficients and their entire expansion, not a finite-level extrapolation. ∎

At |a|=4 the sufficient test needs V_n≤1/32; the achieved bound 1/34 is strictly smaller. It also extends the earlier compact all-level interval from 7/2 to sqrt(17), and excludes a small additional range of possible nonreal centers beyond the previously recorded zero localization |Re z|>4. No conclusion at all exterior heights follows. L268's large-height obstruction to this quadratic certificate is unchanged; the endpoint arithmetic lower bound and the remaining low-index signs are still missing.

**Mathlib.** Full statement: not checked. Supporting weighted-variance identities, integration by parts, exponential-series bounds, and Taylor coefficient positivity: not checked. The proof above is direct and uses no unverified library match. The earlier Mathlib qualifications in L019, L048 and L267 remain unchanged.
