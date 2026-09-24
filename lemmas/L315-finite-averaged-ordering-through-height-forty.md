# Lemma 315: finite averaged level ordering through height forty

**Hypotheses.** Use the positive even actual-theta kernel k(u)=K(|u|), associated kernels A_n and generalized Laguerre coefficients D_n(Ξ;a) of L267. Put

R_n(a)=∫_R A_n(t)cos(2at)dt / ∫_R A_n(t)dt.

Assume L037's explicit arithmetic contracts for the finite calculation below and for L310's saved half-line moment enclosures. These contracts do not include an independently verified implementation.

**Conclusion.** For every real a with 20≤|a|≤40,

R_1(a)>5/10^20,
R_(n+1)(a)−R_n(a)>7/10^19                 (1≤n≤16).

Consequently D_n(Ξ;a)>0 for every 1≤n≤17 throughout this band. This finite ordering does not prove ordering for arbitrary n or a, the full exterior witness target of L266, any enlarged exclusion interval for nonreal centers, or RH.

**Proof.** Set

m_j=∫_0^∞u^jK(u)du,       f(a)=Ξ(a)=∫_0^∞K(u)cos(au)du.

L019's superexponential decay justifies every polynomially weighted integral, differentiation on the real axis, and Taylor-product extraction on compact complex sets. In particular,

f^(j)(a)=∫_0^∞u^jK(u)cos(au+jπ/2)du,       |f^(j)(a)|≤m_j.     (1)

Extract the coefficient of y^(2n) in f(a+iy)f(a−iy). Multiplication of the two powers of i gives

(2n)! D_n(Ξ;a)=N_n(a),
N_n(a)=Σ_(j=0)^(2n)(−1)^(n+j) binom(2n,j) f^(j)(a)f^(2n−j)(a). (2)

At a=0 the odd derivatives vanish and f^(2l)(0)=(−1)^l m_(2l). Thus

B_n:=N_n(0)=Σ_(j even) binom(2n,j)m_jm_(2n−j)>0,
R_n(a)=N_n(a)/B_n.                                            (3)

The last identity also follows directly from L267's mass normalization. This checks the signs and factorials for every level used here.

We first enclose d_(c,j)=f^(j)(c) for c=25,35 and 0≤j≤80. For K_4 equal to the first four summands in L019, the common tail bound is

E=(512/461)2^130 exp(−141)+1280exp(−75)+180exp(−520),
∫_0^2u^j(K−K_4)(u)du+∫_2^∞u^jK(u)du≤E.                      (4)

L310 proves (4) by positive summation and exponential majorants. Its power comparisons are u^j≤1 for 0≤u≤1 and u^j≤u^130 for u≥1, so they apply to every integer j≤130, including odd j. Multiplication by a signed cosine only changes the error enclosure to [−E,E]. No oscillatory tail sign is assumed.

For each finite integral of

g_(c,j)(u)=u^jK_4(u)cos(cu+jπ/2),       0≤u≤2,

use 128 equal panels, centers v_l=(2l+1)/128 and half-width h=1/128. The order-sixteen version of L036 is

∫_(v_l−h)^(v_l+h)g_(c,j)(u)du
 ∈ 2Σ_(q=0)^7 [g_(c,j)^(2q)(v_l)/(2q)!] h^(2q+1)/(2q+1)
       +[−2C_(c,j,l)h^17/17,2C_(c,j,l)h^17/17],               (5)

where C_(c,j,l) bounds |g_(c,j)^(16)|/16! on the entire panel. To prove (5), Taylor-expand through degree fifteen, bound the remainder by C_(c,j,l)|u−v_l|^16, and integrate. Odd monomials vanish and the integrated remainder is 2C_(c,j,l)h^17/17. The normalized product and exponential recurrences proved in L036 apply at every finite derivative order, so they enclose both the midpoint coefficients and the sixteenth derivative on a panel.

The normalized lth derivative of u^j is binom(j,l)u^(j−l), or zero for l>j. The trigonometric coefficient is

c^l cos(cu+(j+l)π/2)/l!.

Use L312's rational sine/cosine construction: reduce by a fixed integer multiple of 2π using L037's π interval, check the resulting interval has absolute value at most four, and enclose the degree-49 Taylor polynomials with symmetric remainder |x|^50/50!. This covers every point of the panel. All arithmetic in (5) obeys L037. Summing the panels and adding (4) gives intervals I_(c,j) containing d_(c,j). The largest accumulated quadrature remainder among all derivatives and both centers is less than 8/10^18; the calculation retains the individual, much sharper errors needed in the final sums.

Next enclose every height, rather than sampled points. Since 2u^81≤u^80+u^82,

m_81≤B:=(m_80+m_82)/2.

For |δ|≤5 and 0≤j≤34, the real Taylor theorem and (1) give

f^(j)(c+δ)=P_(c,j)(δ)+e_(c,j)(δ),
P_(c,j)(δ)=Σ_(l=0)^(80−j) d_(c,j+l)δ^l/l!,
|e_(c,j)(δ)|≤E_j:=B·5^(81−j)/(81−j)!.                         (6)

L310's moment boxes enclose B. The largest E_j upper endpoint is less than 3/10^32. In particular this remainder controls the highest derivative needed for level seventeen throughout both radius-five bands.

It is essential to form the polynomial sums before evaluating height intervals. Define the exact polynomials

Q_(c,n)(δ)=B_n^(−1)Σ_(j=0)^(2n)(−1)^(n+j) binom(2n,j)
                                      P_(c,j)(δ)P_(c,2n−j)(δ).

Writing k=2n−j, (1) and (6) show

|f^(j)f^(k)−P_(c,j)P_(c,k)|≤m_jE_k+m_kE_j+E_jE_k.

Indeed P_(c,j)=f^(j)−e_(c,j); expansion of the product and the triangle inequality give precisely these three terms. Therefore

|R_n(c+δ)−Q_(c,n)(δ)|≤β_n,
β_n=B_n^(−1)Σ_(j=0)^(2n) binom(2n,j)(m_jE_k+m_kE_j+E_jE_k).   (7)

For odd j, use the upper bound m_j≤(m_(j−1)+m_(j+1))/2; no equality of these moments is assumed. All weights in the error sum are nonnegative. The maximum upper endpoint of β_n for 1≤n≤17 is less than 7/10^31. These are absolute errors. They do not require the actual coefficient or Fourier transform to be bounded away from zero.

The coefficients of Q_(c,n) are enclosed by convolution of the interval coefficients in (6), summation with the exact signs in (2), and division by the positive enclosing B_n. Pairing j and 2n−j merely doubles the terms with j<n; the middle term has positive coefficient binom(2n,n). This pairing does not change the polynomial. The relevant comparison polynomials are Q_(c,1) and Q_(c,n+1)−Q_(c,n), with respective errors β_1 and β_(n+1)+β_n. Losing correlations between interval coefficients enlarges their enclosures and cannot invalidate them.

Partition each [c−5,c+5] into 512 closed equal intervals. Their half-width is H=5/512. Let c+b be a cell midpoint and write δ=b+x with |x|≤H. For any comparison polynomial Q, evaluate its normalized derivatives at b from its power coefficients. Taylor's theorem yields

Q(b+x)=Σ_(l=0)^7 [Q^(l)(b)/l!]x^l+ρ(x),
|ρ(x)|≤H^8 sup_(|t−b|≤H)|Q^(8)(t)|/8!.                      (8)

The interval polynomial coefficients enclose each derivative coefficient by multiplication with the exact binomial factors. Horner evaluation at b encloses the first eight coefficients in (8); Horner evaluation on [b−H,b+H] encloses the eighth normalized derivative. Evaluate the local degree-seven polynomial on [−H,H], add the symmetric remainder in (8), and then add the symmetric error from (7). This procedure encloses the actual R_1 or adjacent difference at every point of the cell, while retaining the signed cancellation in the global coefficients.

Reproduction commands are

`python3 scripts/laguerre/certify_exterior_ordering.py --fourier-only > scripts/laguerre/exterior-ordering-fourier-inputs.json`

`python3 scripts/laguerre/certify_exterior_ordering_polynomials.py > scripts/laguerre/exterior-ordering-certificate.json`

The Fourier input file records its source moment file and SHA-256 digest, both centers, all 162 derivative intervals with their quadrature errors, the common tail and height remainder bounds, and the mass denominators. It also retains the failed preliminary derivative-box assessment: 10507 comparisons were unresolved by that less precise assembly, without any certified negative sign. The polynomial certificate records the Fourier-input digest, full comparison polynomial enclosures, product error bounds, and all 17408 comparison enclosures on 1024 height cells.

The minimum lower endpoints are

| Quantity | Minimum lower endpoint, abbreviated | Strict rational target |
| --- | --- | --- |
| R_1 | 6.10363043744666·10^(−20) | 5/10^20 |
| R_(n+1)−R_n, over all 1≤n≤16 | 7.97233209940828·10^(−19) | 7/10^19 |

Both displayed minima occur in the last cell [10235/256,40], the second at n=1. Exact rational comparisons of the full saved endpoints verify the targets on every cell. The initial non-certified point screen and the abbreviated decimals in this table are not proof inputs.

The separate command

`python3 scripts/laguerre/audit_exterior_ordering.py > scripts/laguerre/exterior-ordering-audit.json`

checks the source digests and positive denominators and independently extracts all 34 constant comparison coefficients from the unpaired sums with exact fractions. It also proves positivity of the saved polynomial enclosures, including the product errors, on a different partition of 256 closed height cells. This audit evaluates midpoint derivatives as exact rational intervals and bounds the eighth derivative by its coefficient absolute sum; all 4352 resulting lower bounds are positive. It separately checks the original cells' coverage and stated margins. The audit does not independently verify every polynomial coefficient's construction, the Fourier quadrature, or the Decimal implementation; the original arithmetic-contract qualification is retained.

The cells cover [20,40] including endpoints. Evenness of the cosine integral gives R_n(−a)=R_n(a). Finally the first-level sign and the sixteen positive adjacent differences imply R_n>0 for 1≤n≤17; (3) transfers these signs to D_n. ∎

The achieved margins exceed the required zero threshold for this finite comparison. They supply actual signs and level transfers on the stated band, while leaving the arbitrary-height first-level sign, uniform level ordering and any uncovered indices through L266's location-dependent cutoff unresolved. Thus the previous exclusion of nonreal centers through twenty and the all-level interval through ten are unchanged. The endpoint arithmetic margin is also untouched.

**Mathlib.** Full statement: not checked. Supporting entire Taylor-product extraction, differentiation under the integral, finite polynomial convolution, Taylor remainders and interval arithmetic: not checked for Mathlib coverage. No matching theorem is asserted. The needed identities and estimates are proved above using the specified earlier inputs. L037's [official Decimal reference](https://docs.python.org/3/library/decimal.html) supports the inherited arithmetic contract, not the full statement or an independently verified implementation.
