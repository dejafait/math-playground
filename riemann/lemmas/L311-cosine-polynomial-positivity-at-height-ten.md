# Lemma 311: cosine polynomial certificates and all-level positivity at height ten

**Hypotheses.** Use the positive even actual-theta kernel k, associated kernels A_n(t), and generalized Laguerre coefficients D_n(Ξ;a) of L267. Assume L037's explicit arithmetic contracts and use the certified half-line moments μ_p=∫_0^∞ u^p k(u)du, for even 0≤p≤130, from L310. The high-level conclusion of L310 retains the same contracts.

**Conclusion.** For every integer n≥1 and every real |a|≤10,

D_n(Ξ;a) > (1/400) [2^(2n−1)/(2n)!] ∫_R A_n(t)dt > 0.

In particular, Ξ has no nonreal zero whose real part lies in [−10,10]. This extends the compact all-level interval from [−49/10,49/10]. It supplies no all-height positivity assertion, endpoint arithmetic lower bound, or proof of RH.

**Proof.** We first prove the global polynomial inequality used in the finite calculation. For m≥0 put

P_m(x)=Σ_(j=0)^m (−1)^j x^(2j)/(2j)!,
E_m(x)=cos x−P_m(x).

We have E_0≤0, while E_m''=−E_(m−1) and E_m(0)=E_m'(0)=0 for m≥1. Integrating twice on [0,x], induction shows (−1)^(m+1)E_m(x)≥0 for x≥0. Evenness extends this to every real x. Thus, for every odd m,

cos x≥P_m(x),                       x∈R.                 (1)

This is a global lower bound, not an alternating-series estimate restricted to small x. Every polynomial moment below is integrable by the theta decay already used in L267.

For integers n≥1 and j≥0, let c_(n,j,l) be the coefficient of u^l v^(2n+2j−l) in (u+v)^(2n)(u−v)^(2j). Explicitly,

c_(n,j,l)=Σ_b (−1)^b binom(2j,b)binom(2n,l−b),            (2)

where max(0,l−2n)≤b≤min(l,2j). For d=2n+2j define

H_(n,j)=Σ_(l=0,2,…,d) c_(n,j,l) μ_l μ_(d−l).             (3)

Odd full-line moments vanish and even full-line moments are 2μ_l. Consequently 4H_(n,j) is the full-plane integral of (u+v)^(2n)(u−v)^(2j)k(u)k(v). This integral is strictly positive and finite. The substitution u=s+t, v=s−t has Jacobian 1/2 and gives

∫_R t^(2j)A_n(t)dt = 2^(1−2n−2j)H_(n,j),
∫t^(2j)A_n / ∫A_n = H_(n,j)/(4^j H_(n,0)).              (4)

For example H_(1,0)=2μ_0μ_2 and H_(1,1)=2(μ_0μ_4−μ_2²), so (4) at j=1 agrees with L267's variance normalization. The general formula follows from the same change of variables, not from this example.

Set q=a²/100. For |a|≤10 we have 0≤q≤1. Integrating (1) against the probability density A_n/∫A_n and using (4) yields

∫A_n(t)cos(2at)dt / ∫A_n ≥ B_(n,m)(q),
B_(n,m)(q)=Σ_(j=0)^m α_(n,j) q^j,
α_(n,0)=1,
α_(n,j)=(−1)^j 100^j H_(n,j)/[(2j)!H_(n,0)]  (j≥1).     (5)

No infinite Taylor series is interchanged here: m is finite and (1) holds on the entire integration domain.

To bound each polynomial on a whole interval, write it in the Bernstein basis of degree m:

B_(n,m)(q)=Σ_(i=0)^m β_(n,m,i) binom(m,i)q^i(1−q)^(m−i),
β_(n,m,i)=Σ_(j=0)^i α_(n,j) binom(i,j)/binom(m,j).         (6)

For completeness, the identity follows by expanding each monomial as

q^j=Σ_(i=j)^m [binom(i,j)/binom(m,j)]binom(m,i)q^i(1−q)^(m−i).

Indeed binom(m,i)binom(i,j)=binom(m,j)binom(m−j,i−j), and the sum reduces to q^j(q+1−q)^(m−j). The Bernstein basis terms in (6) are nonnegative on [0,1] and sum to one. Hence a common lower bound for their coefficients bounds B_(n,m) everywhere, including both endpoints; no height sampling or monotonicity assumption is used.

The finite choices are:

| Levels n | Odd Taylor index m | Cosine polynomial degree |
| --- | --- | --- |
| 1–3 | 11 | 22 |
| 4–6 | 9 | 18 |
| 7–11 | 7 | 14 |
| 12–21 | 5 | 10 |
| 22–47 | 3 | 6 |
| 48–63 | 1 | 2 |

Every required moment has degree 2n+2j≤128, within L310's degree-130 certificate. Evaluate (2) with exact integers, and (3), (5), and (6) by L037's enclosing interval operations on those saved moment endpoints. Symmetry gives c_(n,j,l)=c_(n,j,d−l); the script combines these equal terms before interval evaluation and uses the midpoint term only once. All subtractions and divisions are enclosed explicitly, and every denominator interval is strictly positive. The constant coefficient in (5) is exactly one.

The reproducible command is

`python3 scripts/laguerre/certify_cosine_polynomials.py > scripts/laguerre/cosine-polynomial-certificate.json`

The certificate identifies its input moment file and SHA-256 digest, stores every weighted sum, power coefficient and Bernstein coefficient interval, and checks the lower endpoints as exact rational numbers against 1/400. There are 302 Bernstein coefficients for 63 levels. Their smallest lower endpoint occurs at n=1, m=i=11 and begins

0.00260402224201706788869458241177357989807535471405535810980480999409949.

The full endpoint in the certificate is greater than 1/400=0.0025, with surplus greater than 1/10000. The proof uses the full rational endpoints, not rounded displayed approximations. Thus (6) proves

B_(n,m)(q)>1/400            (1≤n≤63, 0≤q≤1).             (7)

Combining (5), (7), and L267's exact identity

D_n(Ξ;a)=[2^(2n−1)/(2n)!] ∫A_n(t)cos(2at)dt

proves the conclusion for the finite remainder. For n≥64, L310 already supplies the stronger normalized lower bound 87/500>1/400 throughout the same height interval. This covers every positive integer level.

Finally D_0(Ξ;a)=Ξ(a)²≥0. The entire Taylor product of L267 converges for every real b and satisfies

|Ξ(a+ib)|²=Ξ(a+ib)Ξ(a−ib)=Σ_(n≥0)D_n(Ξ;a)b^(2n)>0

when |a|≤10 and b≠0, since its n=1 term is strictly positive and every other term is nonnegative. This excludes nonreal zeros with those centers without extrapolating a finite list of levels or inspecting zeros numerically. Heights |a|>10 and the independent endpoint arithmetic threshold remain outside the conclusion. ∎

**Mathlib.** Full statement: not checked. Supporting cosine polynomial bounds, moment changes of variables, Bernstein basis identities, interval arithmetic and entire Taylor-product positivity: not checked for Mathlib coverage. No matching library theorem is asserted. The required polynomial inequalities and identities are proved above. L037's [official Decimal reference](https://docs.python.org/3/library/decimal.html) supports the retained arithmetic contract, not the full theorem or an independently verified implementation; L310 supplies the infinite-kernel moment enclosures under that contract.
