# Lemma 328: finite Möbius convolution and the surviving rough-ratio budget

**Hypotheses.** Use L327's paired sequence and notation

r=8n/3, p=2n=3r/4, a=sqrt(4π²exp(4r)−(39/8)²),
q=a/(2π), X=sqrt(q), L=log X, N=floor(X),
E_r=(1+r)²exp(−r/200), γ=(3/4)log 2−1/2>1/54.

Thus L<r and r−L=O(exp(−4r)). Put R=floor(r). The Möbius function is defined by μ(1)=1, μ(m)=0 if m has a squared prime factor, and μ(m)=(−1)^k otherwise, where k is the number of its distinct prime factors. All sums below are finite. Set

M_±(z)=Σ_(m≤R) μ(m)m^(−1/2∓ia)exp(−z log m),
H_M(z)=M_+(z)M_−(z),
𝒞_r^M=[p!/(2(2r)^p)] [z^p]{H_M(z)q^z F_a(z)},

where F_a(z)=ζ(1/2+z+ia)ζ(1/2+z−ia). No reciprocal series in Re s≤1 is assumed.

To discuss equal-frequency regrouping, temporarily replace a in the finite phases by an independent real variable v, keeping r,L,N,R and χ₀=χ(1/2+ia) fixed. Let a star on an entire function mean conjugation of its coefficients. Define

c_ell=Σ_(m|ell, m≤R, ell/m≤N) μ(m)  (ell≤RN),
H_(b,d)=Σ_(k≤min(R/d,N/b)) μ(kd)/k,
β_(b,d)=H_(b,d)/sqrt(bd)  (b≤N, d≤R, gcd(b,d)=1),

A_v(z)=Σ_(ell≤RN) c_ell ell^(−1/2)exp(−iv log ell)
                          exp((L−log ell)z),
D_v(z)=Σ_(b,d) β_(b,d)exp(iv log(b/d))
                          exp((log(b/d)−L)z).

Every upper bound on an integer index means its floor. In particular the definitions include every cutoff tie. With J_r(f)=p![z^p]f/(2(2r)^p), write

ℛ_r(v)=J_r(A_v A_v*+D_v D_v*),
ℙ_r(v)=J_r(conjugate(χ₀)A_v D_v*+χ₀D_v A_v*),
ℋ_r(v)=ℛ_r(v)+ℙ_r(v).

These are finite exponential polynomials in v. Group *all* equal positive rational ratios t to write ℋ_r(v)=Σ_t h_t exp(iv log t), and similarly ℛ_r with real coefficients ρ_t and ℙ_r with coefficients π_t. This grouping concerns the formal finite polynomial at fixed cutoffs, not an approximate functional equation at variable v.

**Conclusion.** The finite convolution is exact, and

c_1=1, c_ell=0 for 2≤ell≤R.

Nevertheless, for all sufficiently large r,

𝒞_r^M=ℋ_r(a)+O(R^(7/4)sqrt(r)exp(−3r/4)),           (1)
Σ_t |π_t|≤C R^(5/2)exp(−γr)=o(E_r).                (2)

Call an integer R-rough if none of its prime factors is at most R, and put

𝒬_r={ell integer: exp(r/2)≤ell≤2exp(r/2), ell R-rough},
w_ell=ell^(−1/2)((2L−log ell)/(2r))^p,
κ=1/4+(3/4)log(3/4)>7/216>1/32.

The fully grouped ratio coefficients and the zero-frequency coefficient satisfy

ρ_ell≥w_ell/4>0 for every ell∈𝒬_r,                 (3)
Σ_(ell∈𝒬_r)|h_ell|≥c exp(κr)/r,
0≤ρ_1≤C(1+r)^4, |h_1|≤C(1+r)^4.                  (4)

Consequently the absolute remainder certificate

ℋ_r(a)≥h_1−Σ_(t≠1)|h_t|                          (5)

has right side tending to −∞, even after both direct and dual sums and every equal-ratio collision have been included. Its remainder budget exceeds the entire zero-frequency term, not just E_r. The analytic and cross-term errors in (1)–(2) are o(E_r), so they cannot repair that certificate.

This stops finite Möbius convolution followed by constant-term dominance using absolute coefficients. It does not sign 𝒞_r^M or S_r(a), and it does not exclude a bound using their actual phases. Even positivity of 𝒞_r^M would require an additional transfer argument to sign L327's unmollified coefficient and hence obtain L326's sufficient margin.

**Proof.** The normalization and fixed-disk estimates in L327 give, on |z|≤3/8,

q^(z/2)ζ(1/2+ia+z)=U_a(z)+χ₀U_a*(−z)+O(X^(−1/2)),
U_v(z)=Σ_(j≤N)j^(−1/2)exp(−iv log j)exp((L−log j)z).

The corresponding conjugated identity also holds. L327 bounds the difference between the normalized zeta product and the product of these two main expressions by an analytic O(1), uniformly at every cutoff transition. Multiplication by M_+ gives exactly

M_+(z)U_a(z)=A_a(z),
M_+(z)U_a*(−z)=D_a(z).

The first equality groups by ell=jm. For the second, put j=kb and m=kd, with gcd(b,d)=1. Then (jm)^(−1/2)=1/(k sqrt(bd)), j/m=b/d and k≤min(N/b,R/d), giving exactly β_(b,d). Multiplication of the conjugate factor proves the main-expression identity defining ℋ_r(a). No infinite interchange occurs. For ell≤R<N all divisors are allowed in c_ell, so its sum is 1 for ell=1 and (1−1)^k=0 otherwise, by expanding over the distinct prime factors. This proves the stated finite cancellation.

On the disk, |M_±(z)|≤Σ_(m≤R)m^(−1/8)≤C R^(7/8), by integral comparison. Thus the analytic product error after multiplication is O(R^(7/4)). Cauchy's coefficient estimate and 2r(3/8)=p give

|J_r(error)|≤C R^(7/4)p!/p^p
             ≤C R^(7/4)sqrt(r)exp(−3r/4).

This is (1). Only the already proved fixed-disk bound is multiplied; no real error term is differentiated.

For (2), expand the cross term before grouping ratios. Up to the factor 1/2 in J_r, each of its coefficients has absolute value bounded by

|μ(m)μ(l)|/(sqrt(mljk))
 ·((|log(k/j)|+log(ml))/(2r))^p,

where m,l≤R and j,k≤N. Put T=L+2log R and α=p/T. For sufficiently large r, 2/3≤α≤1. If 0≤u≤L and 0≤d≤2log R, the inequality log x≤x−1 gives

((u+d)/(2r))^p≤(T/(2r))^p exp(−α(L−u)).             (6)

The left side is zero if u+d=0. For j<k the resulting j,k sum is bounded by

X^(−α) Σ_j j^(−1/2−α) Σ_k k^(α−1/2)≤C X^(1/2).

Both sums can be bounded by integrals uniformly for 2/3≤α≤1; the first infinite sum is finite and the second is O(X^(α+1/2)). The diagonal costs at most X^(−α)(1+L), also bounded by C X^(1/2). The same estimate covers j>k. Since (Σ_(m≤R)m^(−1/2))²≤4R, the total cross coefficient budget is at most

C R X^(1/2)(T/(2r))^p
 ≤C R exp(r/2)2^(−p)(1+2log R/r)^p
 ≤C R^(5/2)exp(−γr).

Both cross expressions are included, |χ₀|=1, and regrouping cannot increase this absolute budget. This proves (2). Its rate γ>1/54, and the rate 3/4 in (1), both exceed 1/200; their polynomial factors therefore leave errors o(E_r).

We next retain all collisions at an integer frequency ell∈𝒬_r. For large r, R<ell<N and gcd(ell,m)=1 for every m≤R. Let Δ=L−log N=O(exp(−r))≥0. The coefficient of exp(iv log ell) in J_r(A_v A_v*) is exactly

ρ_ell^A=1/(2sqrt(ell)) Σ_(t≤RN/ell) (c_t c_(ell t)/t)
             ·((2L−log ell−2log t)/(2r))^p.           (7)

For t≤N/ell no cutoff affects either divisor sum. Coprimality gives m|ell t if and only if m|t for m≤R, hence c_(ell t)=c_t. These summands are nonnegative because p is even. The t=1 term is w_ell/2.

For N/ell<t≤RN/ell, the numerator in the power in (7) lies between log ell+2Δ−2log R and log ell+2Δ. Both endpoints are positive for large r. Also |c_t|,|c_(ell t)|≤R, and the harmonic sum on this interval is at most 1+log R, because its lower endpoint tends to infinity. Therefore the possibly negative remainder in (7) has absolute value at most

R²(1+log R)/(2sqrt(ell))
 ·((log ell+2Δ)/(2r))^p.                              (8)

Now include the entire dual ratio coefficient. Since ell is coprime to every d≤R, multiplication of a reduced fraction b/d by ell keeps its denominator d. Thus every pair of dual frequencies with quotient ell occurs once as (ell b/d,b/d), with b≤N/ell, d≤R and gcd(b,d)=1. It follows that

ρ_ell^D=(1/2)Σ_(b,d) β_(ell b,d)β_(b,d)
             ·((log ell+2log(b/d)−2L)/(2r))^p.        (9)

If ell b≤Nd/R, then both sums defining the two H coefficients have upper bound floor(R/d). Consequently

β_(ell b,d)β_(b,d)
 =1/(sqrt(ell)bd) ·(Σ_(k≤R/d)μ(kd)/k)²≥0.           (10)

Every term in this range is nonnegative, including cutoff ties. In the remaining range, b/d>N/(ell R), while b/d≤N/ell. The absolute numerator in (9) is therefore between log ell+2Δ and log ell+2Δ+2log R. To bound these remaining terms use

|H_(b,d)|≤1+log R,
Σ_(b≤N/ell,d≤R) 1/(bd)≤(1+L)(1+log R).

Their total absolute value is at most

(1+L)(1+log R)³/(2sqrt(ell))
 ·((log ell+2Δ+2log R)/(2r))^p.                      (11)

This also bounds the sum with the coprimality restriction. Uniformly for ell∈𝒬_r, log ell=r/2+O(1). Hence, for all sufficiently large r,

(log ell+2Δ+2log R)/(2L−log ell)≤1/2.

Dividing (8) and (11) by w_ell bounds their sum by a fixed polynomial in r times 2^(−p), which tends to zero. Equations (7)–(11) imply

ρ_ell=ρ_ell^A+ρ_ell^D≥w_ell/2−o(w_ell)≥w_ell/4.

This proves (3) after all direct and dual equal-ratio terms have been combined; inspecting only the uncancelled t=1 term would not have sufficed.

For completeness, there are enough such rough integers without any prime-distribution theorem. Let Y=exp(r/2), let ℘ be the primes at most R, and let P be their product. Inclusion–exclusion counts integers in [Y,2Y] coprime to P with an error at most 2^|℘|:

|𝒬_r|=Y ∏_(ℓ∈℘)(1−1/ℓ)+O(2^|℘|).

Each multiple count differs from Y/d by at most one, including integral endpoints. The product is at least

∏_(k=2)^R(1−1/k)=1/R,

because all its omitted factors lie in (0,1). Apart from 2 every prime is odd, so |℘|≤R/2+1. As log 2<1, the error 2^(R/2+1) is o(Y/R), and

|𝒬_r|≥Y/(2R)                                       (12)

for large r. This uses only finite inclusion–exclusion. Throughout this interval, the mean value theorem for log on a fixed neighborhood of 3/4 gives

w_ell≥c exp(−r/4)(3/4)^p.

Combining (3) and (12) yields

Σ_(ell∈𝒬_r)ρ_ell≥c exp(κr)/R≥c exp(κr)/r.          (13)

To check its strictly positive exponential rate without decimals, the alternating integral/geometric-series bound gives

log(4/3)<1/3−1/18+1/81=47/162,
κ>1/4−(3/4)(47/162)=7/216>1/32.

We also compare with the *full* diagonal, not only the surviving ell=1 term. At frequency one the direct expression is

ρ_1^A=(1/2)Σ_(t≤RN)c_t²/t ·((L−log t)/r)^p.

For large r, |L−log t|≤max(L,log R)<r, so this lies between zero and C R²(1+log(RN)). Similarly

ρ_1^D=(1/2)Σ_(b,d)β_(b,d)²
                       ·((log(b/d)−L)/r)^p≥0.

Here |log(b/d)−L|≤L+log R, so the power is at most R^(3/4). Bounding the H coefficients as above gives

ρ_1^D≤C R^(3/4)(1+L)(1+log R)³.

Both estimates are bounded by C(1+r)^4, proving the diagonal claim. Equation (2) now implies |h_1|≤C(1+r)^4 and, by the reverse triangle inequality and (13),

Σ_(ell∈𝒬_r)|h_ell|
 ≥Σ_(ell∈𝒬_r)ρ_ell−Σ_t|π_t|
 ≥c exp(κr)/r.

The real-valued polynomial ℋ_r has h_(1/t)=conjugate(h_t), so h_1 is real. In particular the right side of (5) is bounded above by C(1+r)^4−c exp(κr)/r, which tends to −∞. This is failure of the specified triangle-inequality certificate; it is not an upper bound on ℋ_r(a).

Finally, multiplication has not supplied a sign-preserving transfer. If H_M(z)=Σ_j h_j^M z^j and q^zF_a(z)=Σ_j f_j z^j locally at zero, then exactly

𝒞_r^M=[p!/(2(2r)^p)]Σ_(j=0)^p h_j^M f_(p−j),
𝒞_r=[p!/(2(2r)^p)]f_p.

Although h_0^M=|M_+(0)|²≥0, every lower coefficient in the first formula remains. No bound or helpful sign for these terms, nor a lower bound for h_0^M, has been proved here. Nonnegativity of a multiplier on the real axis is not enough: (1+2z)² is nonnegative there, but multiplying 1−z² changes its quadratic coefficient from −1 to 3. This algebraic example is not asserted to model the actual zeta factors. The finite identity above, rather than division by an unproved reciprocal series or omission of lower coefficients, is the transfer that would have to be controlled. ∎

The achieved errors are o(E_r), whereas the absolute nonzero-frequency budget grows exponentially and exceeds the whole polynomial-size diagonal. Therefore this particular certificate cannot supply a positive surplus, even on the mollified coefficient. Arithmetic cancellation at the actual height, a valid transfer to S_r, and the remaining low-index signs stay open. There is no new Laguerre sign, zero exclusion or RH candidate.

The command `python3 scripts/laguerre/check_finite_mobius_convolution.py` checks finite direct/dual grouping and their even coefficient formulas with exact rational additive test frequencies, including equal-ratio collisions and cutoff ties. It checks finite inclusion–exclusion counts and the rational exponent comparison. These are algebra checks, not zeta-value certificates; the asymptotic inequalities are proved above.

**Mathlib.** Full statement: not checked. Supporting finite divisor convolution, inclusion–exclusion, Taylor coefficient identities and harmonic-sum bounds: not checked for a library match. L001 records the related half-plane results [`ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius) and [`ArithmeticFunction.LSeriesSummable_moebius_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeriesSummable_moebius_iff); their coverage has not been rechecked here. They concern the convergent infinite reciprocal on Re s>1, are not used in this finite proof, and do not match the present statement. L327 supplies the analytic balanced equation and its uniform product error. All additional arithmetic, regrouping and budget estimates are proved here.
