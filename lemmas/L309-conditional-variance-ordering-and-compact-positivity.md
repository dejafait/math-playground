# Lemma 309: conditional-variance ordering and a larger compact sign interval

**Hypotheses.** Let k(u)=K(|u|) be the actual positive smooth even theta kernel of L019 and L048, let W=−log k, and put

q_s(t)=k(s+t)k(s−t),
Z(s)=∫_R q_s(t)dt,
v(s)=Z(s)^(−1)∫_R t²q_s(t)dt.

For integers n≥1 use the variances V_n and generalized Laguerre coefficients D_n(Ξ;a) of L267. Assume the explicit directed-rounding and exponential arithmetic contracts of L037 for the finite interval calculations below. The saved moment enclosures are those in `scripts/hankel/hankel-certificate.json`, justified by L037.

**Conclusion.** W'''(u)>0 for every u>0. The conditional variance satisfies v'(s)<0 for every s>0, and

V_(n+1)<V_n≤V_1,
2069/100000 < V_1 < 207/10000 < 50/2401.

Consequently D_n(Ξ;a)>0 for every n≥1 and every |a|≤49/10. No nonreal zero of Ξ has real part in this interval. These assertions retain the stated arithmetic contracts; they are bounded-height partial results, not an all-height sign theorem or an RH candidate. At |a|=5 the quadratic test of L267 already fails for n=1, since V_1>1/50. This last fact concerns the sufficient test, not the actual sign of D_1.

**Proof.** We first establish the actual-theta curvature ordering. For u≥0 write x=πexp(2u) and use the positive series

k(u)=4exp(u/2)Σ_(m≥1)P_0(m²x)exp(−m²x),
P_0(X)=2X²−3X.

Every fixed derivative series converges locally uniformly, by its polynomial times Gaussian bound in m. L048 supplies smooth evenness of W, in particular W'''(0)=0. The variable x in the following calculation is distinct from the conditional variance v(s).

First consider 3≤x≤4. Define integer polynomials recursively by

P_(j+1)(X)=2X(P_j'(X)−P_j(X)),                  0≤j≤3,
H_j(x)=Σ_(m≥1)P_j(m²x)exp(−(m²−1)x),         0≤j≤4.

If H(u)=Σ P_0(m²x)exp(−m²x), then H_j=exp(x)H^(j)(u). Thus, with R_j=H_j/H_0, the linear term u/2 in log k drops out and

W''''(u)=−R_4+4R_3R_1+3R_2²−12R_2R_1²+6R_1⁴.             (1)

Here and below primes on W and H mean u derivatives; the polynomial primes mean derivatives of their displayed argument.

We give an explicit bound for the omitted terms m≥3, including all four derivatives. If P_j(X)=Σ_i p_(j,i)X^i and d=j+2, set the positive rational number

C_j=Σ_i |p_(j,i)|/27^(d−i).

For X≥27, |P_j(X)|≤C_j X^d. For m≥3 the function x^d exp(−(m²−1)x) decreases on x≥3, because d/x≤2<m²−1. Also, with m=3+l,

m^(2d)≤3^(2d)(4/3)^(2dl),
m²−1≥8+7l.

The first inequality follows by multiplying the successive ratios (m+1)/m≤4/3. The bound e³>20 follows from the positive exponential series through degree eight, whose sum is 89641/4480. Since 2d≤12,

(4/3)^(2d)exp(−21)<(4/3)^12/20^7<1/2.

Geometric summation therefore proves, uniformly for 3≤x≤4,

|Σ_(m≥3)P_j(m²x)exp(−(m²−1)x)|
 < E_j:=2C_j 3^(3j+6)/20^8.                               (2)

These bounds concern the exact infinite series, not merely its finite head. The rational values for j=0,…,4 are

1539/12800000000, 891/128000000, 266247/640000000,
40987377/1600000000, 81134379/50000000.

The finite calculation evaluates P_j(x)+P_j(4x)exp(−3x), enlarges it by [−E_j,E_j], and substitutes the resulting intervals in (1). It covers [3,4] by the 1024 closed panels

[3+l/1024, 3+(l+1)/1024],                  0≤l≤1023.

Polynomial evaluation uses Horner's rule; the interval operations and exponentials obey L037. Every denominator H_0 is enclosed strictly above zero. All resulting lower endpoints exceed 114, and in particular

W''''(u)>100 whenever 3≤πexp(2u)≤4.                       (3)

The exact rational decimal endpoints, polynomials, tail bounds and minimum lower endpoint are saved in `scripts/laguerre/conditional-variance-certificate.json`. The reproducible command is

`python3 scripts/laguerre/certify_conditional_variance.py > scripts/laguerre/conditional-variance-certificate.json`

Its minimum lower endpoint begins 114.9790530305976679734; the displayed abbreviation is not an arithmetic input. Equations (1)–(2) and L037 justify the enclosing calculation at every point of every panel. Since 3<π<4, integrating (3) from u=0 proves W'''(u)>0 on 0<u≤(1/2)log(4/π).

It remains to handle the infinite tail x≥4 analytically. Factor the first summand:

k(u)=4x(2x−3)exp(u/2−x)(1+r(x)),
r(x)=Σ_(m≥2)[m⁴+3m²(m²−1)/(2x−3)]exp(−(m²−1)x).

Put D=2x d/dx, λ=m²−1≥3, and c=3m²λ. The absolute jth ordinary x derivative of the mth summand of r is exactly

exp(−λx)[m⁴λ^j+c Σ_(h=0)^j binom(j,h)λ^(j−h)2^h h!/(2x−3)^(h+1)].

For x≥4, c/(2x−3)≤(3/5)m⁴ and 2/[λ(2x−3)]≤2/15. For 0≤j≤3 the remaining finite sum is at most

1+3(2/15)+6(2/15)²+6(2/15)³ < 8/5.

Thus these derivative magnitudes are less than 2m⁴λ^j exp(−λx). Writing T_j=Σ_(m≥2)m⁴λ^j exp(−λx), the identities

D²=4x²(d/dx)²+4x(d/dx),
D³=8x³(d/dx)³+24x²(d/dx)²+8x(d/dx)

and λx≥12 imply

|Dr|≤4xT_1,     |D²r|≤9x²T_2,     |D³r|≤21x³T_3.

For 1≤j≤3, successive polynomial weights m⁴(m²−1)^j have ratio at most

(3/2)^4(8/3)^3=96.

Indeed (m+1)/m≤3/2 and m(m+2)/((m−1)(m+1))≤8/3 for m≥2. The exponential ratio is at most exp(−5x), so 96exp(−5x)<1/2 on x≥4. Consequently T_j<32·3^j exp(−3x), and

|Dr|<384x exp(−3x)≤6/625,
|D²r|<2592x² exp(−3x)≤162/625,
|D³r|<18144x³ exp(−3x)≤4536/625.                         (4)

For the last constants, x^j exp(−3x) decreases on x≥4 and exp(12)>20^4. Since r≥0, logarithmic differentiation gives

|D³log(1+r)|
 ≤|D³r|+3|Dr||D²r|+2|Dr|³
 <4536/625+3(6/625)(162/625)+2(6/625)³<8.                (5)

For the negative logarithm of the first summand alone, the third u derivative is

B(x)=8x−48x(2x+3)/(2x−3)³.

Its u derivative equals

DB(x)=16x+96x(4x²+24x+9)/(2x−3)^4>0.

Hence B(x)≥B(4)=1888/125>15 on x≥4. Subtracting the correction (5) yields W'''(u)>1888/125−8>0 throughout this tail. Together with (3) this proves the global curvature ordering. All differentiated r series used in this estimate are justified by the same summable Gaussian bounds, now uniform on x≥4.

We next turn that ordering into a variance comparison. For fixed s define the probability density p_s=q_s/Z(s), and set

B_s(t)=W'(s+t)+W'(s−t).

Differentiation of the normalized integrals gives

v'(s)=−Cov_(p_s)(t²,B_s(t)).                              (6)

This differentiation is legitimate locally uniformly in s: differentiating the theta series gives

|k(u)|+|k'(u)|≤C exp(13|u|/2−πexp(2|u|)),

by factoring exp(−πexp(2|u|)) and summing a fixed polynomial in m against exp(−π(m²−1)). Evenness handles negative u. This bound dominates q_s and its s derivative with every fixed polynomial in t when s lies in a compact set; Z(s)>0. It also makes the covariance in (6) absolutely integrable.

Since W'' is even and strictly increasing on the positive half-line, for s,t>0 we have

∂_t B_s(t)=W''(s+t)−W''(s−t)>0,

because |s+t|>|s−t|. The function B_s is even in t. For independent variables T,T' with density p_s,

2Cov_(p_s)(t²,B_s(t))
 =E[(T²−T'²)(B_s(T)−B_s(T'))]>0.

The integrand is positive whenever |T|≠|T'|, a set of full measure for this positive continuous density. Thus v'(s)<0 for s>0. Both Z and v are even.

Fubini and the polynomially weighted theta decay give

V_n=∫_0^∞ s^(2n)Z(s)v(s)ds / ∫_0^∞ s^(2n)Z(s)ds.

Let μ_n be the positive probability measure on (0,∞) proportional to s^(2n)Z(s)ds. Then

V_(n+1)−V_n=Cov_(μ_n)(s²,v(s))/E_(μ_n)[s²]<0,             (7)

by the same two-copy covariance identity, now pairing a strictly increasing function with a strictly decreasing one. Integrability follows from the theta decay, or by writing v(s)Z(s) as its defining positive integral. This proves V_n≤V_1.

For the constant, write M_j=∫_R u^j k(u)du. The moment formula of L267 at n=1 reduces exactly to

V_1=(M_4/M_2−M_2/M_0)/4.                                (8)

The stored moment certificate uses half-line moments; the factor two cancels in both ratios. Applying L037's interval operations to its full endpoints in (8) gives

0.02069150187712839056049… ≤ V_1
 ≤ 0.02069191733031206998871… .

The exact enclosing endpoints are saved in the new certificate; the proof uses those endpoints, not the abbreviated display. Exact rational comparisons give the bounds asserted in the conclusion. In particular, the required threshold at A=49/10 is 1/(2A²)=50/2401, and

50/2401−207/10000=2993/24010000>0.

By L267, for c_n=2^(2n−1)/(2n)!>0,

D_n(Ξ;a)≥c_n(∫_R A_n(t)dt)(1−2a²V_n)>0

whenever |a|≤49/10. The positive mass factor is finite. Finally D_0(Ξ;a)=Ξ(a)²≥0, so for every real b≠0 the entire expansion

Ξ(a+ib)Ξ(a−ib)=Σ_(n≥0)D_n(Ξ;a)b^(2n)>0

excludes a nonreal zero with this real center. This uses the established signs at every level, not a finite extrapolation. At |a|=5, (8)'s certified lower bound exceeds 1/50, proving only the stated failure of the quadratic sufficient test there. ∎

The result extends the compact interval in L308 from sqrt(17) to 49/10. It supplies no sign at the endpoint arithmetic sequence of L302 and no low-index estimate at unbounded heights. L268's obstruction to the quadratic certificate through the growing-height witness cutoff remains applicable.

**Mathlib.** Full statement: not checked. Supporting logarithmic-derivative identities, covariance comparisons, interval arithmetic and entire Taylor-product positivity: not checked. No matching library theorem is asserted. L037's arithmetic implementation contract and its supporting reference remain unchanged; the new calculation reuses that interval implementation and the previously certified moments. The analytic ordering and tail arguments are written out above.
