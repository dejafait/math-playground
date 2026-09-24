# Lemma 310: a finite variance cutoff at height ten

**Hypotheses.** Let k(u)=K(|u|) be the positive even actual-theta kernel of L019. Use the variances V_n and generalized Laguerre coefficients D_n(Ξ;a) of L267. Assume the directed-rounding, exponential and exceptional-operation contracts of L037. The conditional-variance ordering of L309 is used with those same contracts.

**Conclusion.**

411/100000 < V_64 < 413/100000 < 1/200.

For every integer n≥64 and every real |a|≤10,

D_n(Ξ;a) > (87/500) [2^(2n−1)/(2n)!] ∫_R A_n(t)dt > 0,

where A_n is the positive associated kernel in L267. Consequently, all-level Laguerre nonnegativity on |a|≤10 reduces to the 63 remaining levels 1≤n≤63; D_0(Ξ;a)=Ξ(a)² is already nonnegative. This result does not establish those remaining signs, enlarge the interval on which nonreal centers have been excluded, or prove RH.

**Proof.** Write the even half-line moments as

μ_p=∫_0^∞ u^p K(u)du,                  p=0,2,…,130,

and let B_p be their four-term theta integrals over 0≤u≤2. We first prove a common error bound sufficiently small for these higher moments:

0≤μ_p−B_p≤E,
E=(512/461)2^130 exp(−141)+1280exp(−75)+180exp(−520).       (1)

L019 gives, for u≥0,

K(u)=Σ_(m≥1)K_m(u),
0<K_m(u)=[8π²m⁴exp(9u/2)−12πm²exp(5u/2)]exp(−πm²exp(2u))
        ≤128m⁴exp(9u/2−3m²exp(2u)),                       (2)

using 3<π<4. All sums and integrals in the tail argument have nonnegative terms, so Tonelli's theorem applies.

For X≥1 the inequalities m⁴≤16^(m−1) and m²≥1+3(m−1) give

Σ_(m≥1)m⁴exp(−3m²X)
 ≤exp(−3X)/(1−16exp(−9X))≤2exp(−3X).                    (3)

Here exp(9)>32 follows already from its positive series through degree two. Thus K(u)≤256exp(9u/2−3exp(2u)). On u≥2, every power u^p in question is at most u^130. Set f(u)=u^130 exp(9u/2−3exp(2u)). Its logarithmic derivative obeys

(log f)'=130/u+9/2−6exp(2u)<−461/2,

because exp(4)>50, as follows by summing its positive series through degree seven. Also f(2)<2^130 exp(−141). Integrating the resulting exponential majorant gives

∫_2^∞ u^p K(u)du ≤ (512/461)2^130 exp(−141).             (4)

We bound the omitted m≥5 terms over the whole half-line; the harmless overlap with (4) only enlarges the error. On 0≤u≤1 use u^p≤1 and exp(2u)≥1+2u in (2). Extending the resulting elementary integral to infinity yields

∫_0^1 u^p K_m(u)du
 ≤128m⁴ exp(−3m²)/(6m²−9/2)
 ≤(128/5)m²exp(−3m²),                                  (5)

since m≥5. For m=5+l we have m²≥25+11l, m²≤25·16^l, and m⁴≤625·16^l. Since 16exp(−33)<1/2, geometric summation in (5) bounds the omitted contribution on [0,1] by 1280exp(−75). The same inequalities also give

Σ_(m≥5)m⁴exp(−3m²X)≤1250exp(−75X),       X≥1.           (6)

On u≥1 we again use u^p≤u^130. The logarithmic derivative of

g(u)=u^130 exp(9u/2−75exp(2u))

is at most 130+9/2−150exp(2)<−900, because exp(2)>7 (the series through degree four equals 7 and the remaining terms are positive). Moreover g(1)<exp(−1041/2). Equations (2) and (6) therefore imply

Σ_(m≥5)∫_1^∞ u^p K_m(u)du
 ≤(160000/900)exp(−1041/2)<180exp(−520).                  (7)

Combining (4), (5), and (7) proves (1). The common upper endpoint for E is less than 9·10^(−23). This bound retains the polynomial powers rather than using the inefficient factorial majorant at this degree.

We now enclose B_p by the midpoint Taylor panels of L036. Partition [0,2] into 256 closed panels of half-width h=1/256 and centers c_j=(2j+1)/256 for 0≤j≤255. For the finite smooth function

F_p(u)=u^p Σ_(m=1)^4 K_m(u),

the enclosure on each panel is

2Σ_(q=0)^3 [F_p^(2q)(c_j)/(2q)!] h^(2q+1)/(2q+1)
  + [−2C_(p,j)h^9/9, 2C_(p,j)h^9/9],                  (8)

where C_(p,j) bounds |F_p^(8)|/8! throughout that panel. L036's normalized product and exponential derivative recurrences, evaluated over the full interval, supply C_(p,j). In particular the normalized jth derivative of u^p is binom(p,j)u^(p−j) for j≤p and zero otherwise. These formulas apply to every degree through 130; they do not use a low-degree tail estimate. The script reuses L037's enclosing interval implementation, π enclosure and finite theta derivative evaluation. Summing (8) and adding [0,E] gives positive enclosures for all 66 moments μ_p.

The reproducible command is

`python3 scripts/laguerre/certify_variance_cutoff.py > scripts/laguerre/variance-cutoff-certificate.json`

The certificate stores the parameters, π interval, both tail components, all accumulated quadrature error bounds, all moment endpoints and the three moment sums below. Its 70-digit decimal endpoints are exact rational bounds under L037's arithmetic contracts. No binary floating-point evaluation is used.

Define the positive half-line sums

Z=Σ_(j=0,2,…,128) binom(128,j)μ_j μ_(128−j),
P=Σ_(j=0,2,…,128) binom(128,j)μ_(j+2) μ_(128−j),
Q=Σ_(j=1,3,…,127) binom(128,j)μ_(j+1) μ_(129−j).

The full-line even moments in L267 are 2μ_p and their odd moments vanish. Hence its Z_64, P_64 and Q_64 are respectively 4Z, 4P and 4Q, giving the exact identity

V_64=(P−Q)/(2Z).                                        (9)

The interval calculation propagates the subtraction P−Q, with no assumption that relative moment errors stay small after cancellation. The saved lower endpoint of (9) begins 0.0041187558413737804980 and its upper endpoint begins 0.0041187799142365141472. Comparing the full stored endpoints as exact fractions yields

411/100000 < V_64 < 413/100000,
1/200−413/100000=87/100000>0.                            (10)

Thus the achieved bound lies strictly below the required threshold; the non-certified concentration probe is not an input. Equations (1) and (8) justify the entire infinite-kernel enclosure, rather than only its sampled finite head.

Finally L309 gives V_n≤V_64 for n≥64. If |a|≤10 then

1−2a²V_n ≥1−200V_64 >1−200(413/100000)=87/500.

The exact Fourier representation and quadratic cosine inequality in L267 multiply this lower bound by the positive finite mass factor 2^(2n−1)∫A_n/(2n)!, proving the stated strict signs. There is no inference here about the signs for 1≤n≤63. L309 already covers those levels on |a|≤49/10, so only their exterior band 49/10<|a|≤10 remains for this compact target. The large-height low-index signs and endpoint arithmetic margin are separate unresolved claims. ∎

**Mathlib.** Full statement: not checked. Supporting Tonelli, exponential inequalities, midpoint Taylor remainder, interval arithmetic and Fourier moment identities: not checked for Mathlib coverage. No matching library theorem is asserted. The supporting analytical results are proved above or in L036, L267 and L309; the implementation retains L037's explicit arithmetic contract and its [official Decimal reference](https://docs.python.org/3/library/decimal.html). That documentation supports the arithmetic contract, not the full mathematical statement or an independently verified implementation.
