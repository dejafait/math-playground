# Lemma 313: the first averaged level comparison through height twenty

**Hypotheses.** Use the positive even actual-theta kernel k(u)=K(|u|), associated kernels A_n and generalized Laguerre coefficients D_n(Ξ;a) of L267. Put

R_n(a)=∫_R A_n(t)cos(2at)dt / ∫_R A_n(t)dt.

Assume L037's explicit arithmetic contracts for the finite certificate below and for L310's saved half-line moment enclosures. These contracts do not include an independently verified implementation.

**Conclusion.** For every real a with 10≤|a|≤20,

R_1(a)>1/10^7,
R_2(a)−R_1(a)>4/10^7.

In particular, D_1(Ξ;a)>0 and D_2(Ξ;a)>0 throughout that band. This proves only the first averaged comparison. It does not establish ordering of all levels, any further all-level interval, exclusion of nonreal centers beyond ten, or RH.

**Proof.** Define the half-line moments and transform

m_j=∫_0^∞ u^j K(u)du,
f(a)=∫_0^∞ K(u)cos(au)du=Ξ(a).

The last equality is the theta representation used in L267. L019's superexponential decay makes every m_j finite and justifies differentiation under this integral. In particular, for every integer j≥0 and real a,

f^(j)(a)=∫_0^∞ u^j K(u)cos(au+jπ/2)du,
|f^(j)(a)|≤m_j.                                           (1)

The same domination on compact complex sets justifies the Taylor product in L267. Extracting its y² and y⁴ coefficients gives

D_1(Ξ;a)=f'(a)²−f(a)f''(a),
12D_2(Ξ;a)=f(a)f''''(a)−4f'(a)f'''(a)+3f''(a)².           (2)

At a=0, the odd derivatives vanish and the even ones are (−1)^(j/2)m_j. Since L267 also gives R_n(a)=D_n(Ξ;a)/D_n(Ξ;0), (2) yields the exact positive-denominator identities

B_1=m_0m_2>0,             B_2=m_0m_4+3m_2²>0,
R_1=(f'²−ff'')/B_1,
R_2=(ff''''−4f'f'''+3f''²)/B_2.                          (3)

Thus there is no missing factorial or factor of two in the normalized comparison. Equivalently, writing c_j=∫u^jK(u)cos(au)du for even j and s_j=∫u^jK(u)sin(au)du for odd j gives numerators c_0c_2+s_1² and c_0c_4+4s_1s_3+3c_2². In the latter identity f'=−s_1 and f'''=s_3, which explains the plus sign on 4s_1s_3.

We enclose d_j=f^(j)(15), for 0≤j≤32. The infinite-tail bound needed for all these integrals is

E=(512/461)2^130 exp(−141)+1280exp(−75)+180exp(−520).

If K_4 is the sum of the first four terms of L019's kernel series, then

∫_0^2 u^j(K−K_4)(u)du+∫_2^∞ u^jK(u)du≤E.               (4)

This is L310's tail proof, which applies also to odd j: its only power comparisons are u^j≤1 on [0,1] and u^j≤u^130 on [1,∞), valid for every integer 0≤j≤130. More explicitly, the spatial part is at most (512/461)2^130 exp(−141); the omitted theta indices on [0,1] contribute at most 1280exp(−75); and those on [1,∞) contribute at most 180exp(−520). These bounds may overlap, which only enlarges the error. Positivity of the omitted kernel terms and |cos|≤1 show that the error in each signed derivative integral is enclosed by [−E,E]. No parity assumption or sign of an oscillatory tail is used.

For the finite part of d_j apply L036 to the smooth function

g_j(u)=u^j K_4(u)cos(15u+jπ/2),                 0≤u≤2.

There are 256 equal panels, with centers c_l=(2l+1)/256 and half-width h=1/256, for 0≤l≤255. The normalized Taylor coefficients of u^j are binom(j,q)u^(j−q) for q≤j and zero otherwise. The kernel coefficients use L019's explicit finite series and L036's product and exponential recurrences. The normalized qth derivative of the trigonometric factor is

15^q cos(15u+(j+q)π/2)/q!.

Its sine and cosine values are enclosed by L312's rational Taylor construction: reduce the argument by an integer multiple of 2π using L037's π interval, check that the reduced interval has absolute value at most four, and add the symmetric remainder |x|^50/50! to the degree-49 Taylor polynomials. This is a proved trigonometric remainder estimate, not a new trigonometric arithmetic contract. The reduction integer is fixed within each evaluation, so the enclosure includes every point even when a preferred period boundary is crossed.

Evaluate the coefficients at the midpoint and the eighth normalized derivative on the whole panel. If its interval magnitude is C_(j,l), the panel integral lies in

2Σ_(q=0)^3 [g_j^(2q)(c_l)/(2q)!]h^(2q+1)/(2q+1)
  +[−2C_(j,l)h^9/9,2C_(j,l)h^9/9].                       (5)

L036 proves (5); all its operations satisfy L037. Summing the panels and adding [−E,E] produces intervals I_j containing d_j. The largest accumulated quadrature error upper endpoint is less than 7/10^15. The certificate retains the full endpoints for each derivative rather than treating this common bound as the precision of the final comparison.

We next cover every height in the band, not just sampled heights. The pointwise inequality 2u^33≤u^32+u^34 gives

m_33≤B:=(m_32+m_34)/2.

For 0≤j≤4 and |δ|≤5, Taylor's theorem applied to f^(j), with (1), gives

f^(j)(15+δ)=P_j(δ)+e_j(δ),
P_j(δ)=Σ_(l=0)^(32−j) d_(j+l) δ^l/l!,
|e_j(δ)|≤B·5^(33−j)/(33−j)!.                             (6)

Only the real segment between 15 and 15+δ is used in this Taylor remainder. The derivative in its remainder is f^(33), so the same absolute moment bound B applies to all five formulas. L310's enclosing m_32 and m_34 intervals give enclosing bounds for B; the largest remainder in (6), for j=4, is less than 4/10^18.

Partition [10,20] into the 512 closed intervals

J_l=[10+10l/512,10+10(l+1)/512],                 0≤l≤511.

For its midpoint a_l let b_l=a_l−15 and write δ=b_l+x, where |x|≤5/512. To avoid losing the cancellations at these midpoints, first translate each polynomial in (6) by the exact binomial identity

P_j(b_l+x)=Σ_(q=0)^(32−j) T_(j,l,q)x^q,
T_(j,l,q)=Σ_(v=q)^(32−j) binom(v,q)d_(j+v)b_l^(v−q)/v!.   (7)

Evaluate (7) with d_(j+v) in I_(j+v), evaluate the translated polynomial by interval Horner arithmetic on [−5/512,5/512], and add the symmetric remainder from (6). Interval inclusion gives an enclosure of f^(j)(a) for every a∈J_l. This use of intervals does not assume independence of the derivatives; losing correlations can only enlarge the result. Substitute the five enclosures and L310's moment enclosures into (3), then subtract the resulting R_1 interval from the R_2 interval.

The reproducing command is

`python3 scripts/laguerre/certify_averaged_ordering.py > scripts/laguerre/averaged-ordering-certificate.json`

The certificate stores its input moment file and SHA-256 digest, all 33 derivative integrals and quadrature errors, the tail bound (4), the remainders (6), the positive denominator intervals, and every height interval with its five derivative and three ratio enclosures. Its minimum lower endpoints, over all 512 intervals, occur on J_511=[5115/256,20] and begin

| Quantity | Minimum lower endpoint, abbreviated | Strict rational target |
| --- | --- | --- |
| R_1 | 0.0000001191618387575245385831015384 | 1/10^7 |
| R_2−R_1 | 0.0000004480448410579362642420164717 | 4/10^7 |

The full stored endpoints are exact rationals under L037's contracts; exact fraction comparisons verify both targets on every interval. An independent Fraction calculation using each saved derivative box and the source moment boxes also verifies all 512 final comparisons and their complete coverage of [10,20]. The abbreviated display and the preceding non-certified point screen are not proof inputs.

The intervals J_l include their endpoints and cover the band. Finally R_n is even in a by its cosine integral, so the conclusion extends to negative a. Positivity of D_n(Ξ;0), already used in (3), transfers these two normalized signs to D_1 and D_2. ∎

The achieved comparison has a uniform margin greater than 4/10^7 above the required zero threshold on this band. It survives L312's conditional-ordering obstruction because that obstruction does not sign the averaged covariance. A first adjacent-level comparison, even with both signs established, does not imply any comparison for n≥2; in particular it does not cover every index through L266's witness cutoff. The global low-index gap and the endpoint arithmetic margin remain open.

**Mathlib.** Full statement: not checked. Supporting differentiation under the integral, entire Taylor-product coefficients, Taylor remainder bounds, polynomial translation and interval arithmetic: not checked for Mathlib coverage. No matching library theorem is asserted. The required identities and enclosures are proved above using the specified earlier inputs. The [official Decimal reference](https://docs.python.org/3/library/decimal.html) retained in L037 supports the arithmetic contract, not this full mathematical statement or an independently verified implementation.
