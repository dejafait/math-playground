# Lemma 764: centered fixed-Gaussian Hermite-grid residue obstruction

## Hypotheses

Use the actual theta kernel K of L019, the moments M_(2j) of L021,
and the actual entire function and reciprocal Jensen polynomials of L763:

    gamma_j=j! M_(2j)/(2j)!,
    Theta(z)=sum_(j>=0) gamma_j z^j/j!,
    Q_d^(a)(X)=sum_(j=0)^d binom(d,j)
                    (Theta(z)exp(-az^2))^(j)(0) X^(d-j).

Here a>0 is real and fixed independently of the integer d. Write

    c=gamma_1/gamma_0,
    b_j=(Theta(z)exp(-cz))^(j)(0)/gamma_0,
    P_d(x)=Q_d^(a)(2sqrt(a)x-c),
    K_d=2 gamma_0 a^(d/2)>0.

H_m denotes the physicists' Hermite polynomial. No hyperbolicity or
Riemann hypothesis is assumed.

## Conclusion

For every fixed a>0 and every integer

    d >= D(a):=max{6,ceil(12000000 a)},

there is a (necessarily nonzero) real zero r of H_(d-1) such that

    P_d(r) H_d(r)<0.

In particular no fixed a satisfies the proposed strict positive signs at
all these prescribed extrema in every degree. This stops this centered
prescribed grid only, not hyperbolicity of Q_d^(a), other grids, or RH.

More precisely, for d>=4 the full quotient has expansion

    P_d(x)/(K_d H_(d-1)(x))
       =x+A_d/x+B_d/x^2+C_d/x^3+O(x^-4),
    A_d=d(d-1)b_2/(8a)-(d-1)/2,
    B_d=d(d-1)(d-2)b_3/(48a^(3/2)),
    C_d=d(d-1)(d-2)(d-3)b_4/(384a^2)
          +d(d-1)(d-2)b_2/(16a)-(d-1)(d-2)/4.

The actual-coefficient certificate below proves

    -0.000038 < b_2 < -0.000037,
    0.00000000016 < b_4 < 0.00000000018.

These finite actual-coefficient bounds do not assert higher-degree signs.
The proposed positive extremum signs would require A_d<0, C_d<=0 and
A_d C_d-B_d^2>=0. The C_d condition already fails throughout d>=D(a).

## Proof

### 1. Imported Hermite and residue interface

The physicists' identities are

    H_m'=2m H_(m-1),
    H_(m+1)=2x H_m-2m H_(m-1).

Precise standard inputs: [DLMF 18.9.25](https://dlmf.nist.gov/18.9.E25),
[18.9.1 and Table 18.9.1, Hermite row](https://dlmf.nist.gov/18.9#T1),
and simple real zeros from orthogonal-polynomial separation in
[DLMF 18.2(vi)](https://dlmf.nist.gov/18.2#vi).
Thus at a zero r of H_(d-1), H_d(r)=-H_(d-1)'(r), and the derivative
is nonzero. This checks the orientation explicitly.

Steve Fisk, *Polynomials, roots, and interlacing*,
[arXiv:math/0612833v2](https://arxiv.org/pdf/math/0612833v2),
Section 1.3, Lemma 1.20(3), printed pp.12–14, gives the simple-pole
residue characterization for polynomials of consecutive degrees with
positive leading coefficients. Here those coefficients are
 gamma_0(2sqrt(a))^d and 2^(d-1), both positive. The partial-fraction
representation and orientation specialize to

    P_d(x)/(K_d H_(d-1)(x))=x+sum_i rho_i/(x-r_i),
    rho_i=P_d(r_i)/(K_d H_(d-1)'(r_i)).

There is no constant polynomial part by the centering, verified below.
The sum is indexed by every denominator zero. If P_d shares a zero with
H_(d-1), the corresponding rho_i is zero and its apparent pole is
removable; no coprimality hypothesis is needed for this representation.
In particular the proposed signs P_d(r_i)H_d(r_i)>0 imply rho_i<0.
We use this necessary direction only; no converse or actual interlacing
is assumed. Expanding the finite simple-pole sum at infinity gives

    A_d=sum_i rho_i,
    B_d=sum_i rho_i r_i,
    C_d=sum_i rho_i r_i^2.

If every rho_i<0, the positive weights w_i=-rho_i give
-A_d>0, -C_d>=0 and B_d^2<=A_d C_d by finite Cauchy–Schwarz applied
to 1 and r_i. Distinct real support and positive weights are established
hypotheses of this implication, not assumed properties of actual Q.
Conversely C_d>0 forces some rho_i>0 with r_i!=0, and then
P_d(r_i)H_d(r_i)=-K_d rho_i (H_(d-1)'(r_i))^2<0.

### 2. Full-polynomial division

Translation of a reciprocal Jensen polynomial by -c multiplies its input
series by exp(-cz), by the binomial theorem. Thus, exactly and finitely,

    P_d(x)=gamma_0 sum_(j=0)^d binom(d,j)
             (exp(-az^2) sum_(k>=0) b_k z^k/k!)^(j)(0)
             (2sqrt(a)x)^(d-j).

Here b_0=1 and b_1=0. Normalize by the leading coefficient
 gamma_0(2sqrt(a))^d. Its first relevant coefficients are

    x^d+p_2 x^(d-2)+p_3 x^(d-3)+p_4 x^(d-4)+lower terms,
    p_2=d(d-1)(b_2-2a)/(8a),
    p_3=d(d-1)(d-2)b_3/(48a^(3/2)),
    p_4=d(d-1)(d-2)(d-3)(b_4-12ab_2+12a^2)/(384a^2).

Normalize H_(d-1) by its leading coefficient 2^(d-1):

    x^(d-1)+h_2 x^(d-3)+h_4 x^(d-5)+lower terms,
    h_2=-(d-1)(d-2)/4,
    h_4=(d-1)(d-2)(d-3)(d-4)/32.

If d=4 the h_4 term is absent and its displayed coefficient is zero.
There are no degree d-1 numerator or degree d-2 denominator terms.
Finite division therefore gives A_d=p_2-h_2, B_d=p_3 and
C_d=p_4-p_2 h_2+h_2^2-h_4, yielding the formulas in the conclusion.
Every omitted numerator term has degree at most d-5 and hence quotient
order at most x^-4. No summand has been dropped in an evaluation at a
Hermite zero: this is division of the full polynomial at infinity.

### 3. Rigorous actual-theta coefficient bounds

This is an essential numerical specialization, not a new general theorem
about centered moment sequences. Positive raw moments alone do not prove
b_4>0. Put g_j=gamma_j/gamma_0. The exact formulas used are

    b_2=g_2-g_1^2,
    b_3=g_3-3g_1 g_2+2g_1^3,
    b_4=g_4-4g_1 g_3+6g_1^2 g_2-3g_1^4.

The complete reproducible certificate and standard-library implementation
are `scripts/centered-hermite/residue-moment-382.json` and
`scripts/centered-hermite/residue-moment-382.py`. Reproduce from the
notebook root with

    python3 scripts/centered-hermite/residue-moment-382.py

Here are all analytic and rounding bounds required to interpret it.
L019 and L021 give, for p=0,2,4,6,8,

    M_p=integral_0^infinity u^p sum_(n>=1) K_n(u) du,
    K_n(u)=exp(u/2-v)(8v^2-12v), v=pi n^2 exp(2u).

All terms are positive. Integrate n=1,...,4 on [0,2] by composite
Simpson with N=65536 even mesh intervals of length h=2/N. For r<=4,

    K_n^(r)(u)=exp(u/2-v) P_r(v),
    P_0(v)=8v^2-12v,
    P_(r+1)(v)=(1/2-2v)P_r(v)+2v P_r'(v).

The polynomials have rational coefficients. For v>=0,
v^k exp(-v)<=k!, directly from the exponential series. Since
exp(u/2)<3 on [0,2], a valid uniform bound for the fourth derivative
of u^p sum_(n=1)^4 K_n(u) is

    E_p=12 sum_(s=0)^min(4,p) binom(4,s) (p!/(p-s)!) 2^(p-s)
                  sum_k |[v^k]P_(4-s)| k!.

For p=0,2,4,6,8 these exact values are respectively
8545509, 42485796, 210292560, 1036026432, 5079115008.
The two-sided Simpson error is at most (2/180)h^4 E_p; in particular
it is less than 4.895e-11 for every retained moment. The imported theorem
is [DLMF 3.5(ii), equations 3.5.6–3.5.8](https://dlmf.nist.gov/3.5#ii):
the integrand is C4 on the closed interval and the number N of mesh
intervals is even, as required here. We retain the following elementary
kernel check to verify the implementation's normalization, not as a new
quadrature theorem. Taylor's integral remainder gives:
on a unit-mesh panel [0,2], the error kernel for Simpson minus integral
is t^3(4-3t)/72 on [0,1], and its reflection on [1,2]. It is nonnegative
with integral 1/90. Scaling and summing N/2 panels gives the stated
bound. This supplies the implementation bound rather than treating
high-precision quadrature output as evidence by itself.

The omitted n>=5 contribution on [0,2], for each of these p, is bounded
by

    T_n=2*256*8pi^2 exp(9)*1250 exp(-25pi) < 1e-20.

Indeed K_n<=8pi^2 n^4 exp(9) exp(-pi n^2), u^p<=256, and
n^4<=625*3^(n-5), n^2>=25+11(n-5). The resulting geometric-series
factor is less than 2. All quantities are positive, so this tail only
increases the upper endpoint of a moment enclosure.

For u>=2, put v_0=pi exp(2u). The bounds
n^4<=16^(n-1), n^2>=1+3(n-1) imply
sum_(n>=1) n^4 exp(-v_0 n^2)<=2exp(-v_0). Moreover
u^p<=u^8<=exp(4u), since log u<=u/2 for u>=2. Hence the omitted
u>=2 integral, including every n, is at most

    8pi^2 integral_(exp(4))^infinity t^(13/4)exp(-pi t) dt
      <=384pi exp(-pi exp(4)/2)=T_u < 1e-30.

Here t^(13/4)<=t^4 and t^4 exp(-pi t/2)<=24(2/pi)^4<24.
This also is a positive upper-endpoint addition. Thus no infinite sum
or tail has been silently truncated.

The script evaluates all mesh contributions and moment/coefficient
operations as outward intervals at 60 decimal digits. Directed FLOOR
and CEILING contexts enclose arithmetic. Decimal.exp is correctly rounded
to nearest; its adjacent representable values enclose the exact
exponential, and monotonicity gives interval endpoints. Negations use
exact sign copies. These operation specifications are documented in
[Python's decimal reference](https://docs.python.org/3/library/decimal.html),
entries Decimal.exp, next_minus/next_plus, copy_negate, Context and
ROUND_FLOOR/ROUND_CEILING (the source assessment inspected the documentation
served as 3.15.2; the replay interpreter is identified below).
The pi enclosure follows from Machin's identity
pi=16atan(1/5)-4atan(1/239), using rational alternating-series bounds
with 50 and 15 terms. No floating-point pi or uncertified quadrature
routine enters the certificate. Exact rational mesh points are converted
outward. Each Simpson interval is enlarged by its two-sided derivative
error and the two positive tails. The resulting moment intervals are
then converted to g_j and b_j with outward arithmetic, with g_0=1 exact.

The certificate yields, with endpoints widened here for readable rational
bounds,

    -0.000037172600 < b_2 < -0.000037172598,
     0.00000000016714 < b_4 < 0.00000000016730.

These imply the looser rational bounds in the conclusion, with strict
room at both endpoints. Full moment, normalized gamma, centered
coefficient, tail and quadrature-error intervals are stored in the
certificate; no finite sample of degrees is used to conclude signs.

### 4. Uniform eventual wrong sign for each fixed a

Write beta=0.000038 and epsilon=0.00000000016. The preceding actual
bounds give b_2>-beta and b_4>epsilon. For d>=6, d-3>=d/2, so

    C_d/((d-1)(d-2))
      > epsilon d^2/(768a^2)-beta d/(16a)-1/4.

Set t=d/a. If d>=D(a), then t>=12000000. In exact rational arithmetic,

    epsilon t/768-beta/16
       >= epsilon*12000000/768-beta/16
        = 1/8000000.

Consequently

    C_d/((d-1)(d-2)) > t/8000000-1/4 >= 5/4 >0.

The residue-moment implication in section 1 now supplies a nonzero node
with strictly negative P_d(r)H_d(r). This proves the conclusion for every
real a>0, including arbitrarily small a and equality in the integer
threshold. It does not exclude real zeros of P_d lying in different
locations, and is not a disproof of RH or a hyperbolicity obstruction.

### 5. Independent conceptual audit and preserved replay — step384

The audit retained the statement without a mathematical correction. It
checked the factorial normalization against L021 and the definitions in
L763, the translation identity, all coefficients of the full division,
the simple-root hypotheses and residue orientation, and the removable-pole
case explicitly described above. In particular d=4 gives h_4=0, and a
possible zero node contributes zero to C_d; a positive C_d therefore
forces a nonzero node of the asserted strict wrong sign.

For the analytic enclosure, differentiating each monomial gives the
recurrence in section 3. Its five polynomials and all five E_p were checked
as exact rationals. Leibniz's rule, the four retained n values and
exp(u/2)<3 give precisely the factor 12 in E_p. The finite integrands are
C-infinity, so no endpoint smoothness assumption is missing in Simpson's
theorem. Its largest error is

    4.894922245313182429526932537555694580078125e-11 < 4.895e-11.

Both omitted tails were checked on their full domains. For integers n>=5,
((n+1)/n)^4<3 and n^2-25-11(n-5)=(n-5)(n-6)>=0 justify the n-tail
comparison; 3exp(-11pi)<1/2 supplies its factor 2. For n>=1,
((n+1)/n)^4<=16 and n^2-1-3(n-1)=(n-1)(n-2)>=0 give the u-tail
comparison, with 16exp(-3pi exp(2u))<1/2 for u>=2. Also
u/2-log(u) is nondecreasing on [2,infinity) and positive at 2, proving
the bound u^8<=exp(4u). The substitution t=exp(2u) gives exactly the
power t^(13/4), followed by the exponential-series bound and convergent
integral displayed in section 3. The outward tail upper bounds are
respectively less than 3.182814e-23 and 6.843349e-35. They enter only the
upper moment endpoints because the exact K_n are positive for u>=0.

Reproduce the audit, preserving the original program and certificate, by

    python3 scripts/centered-hermite/residue-audit-384.py

The full audit certificate is `scripts/centered-hermite/residue-audit-384.json`;
the complete reproduced moment certificate is
`scripts/centered-hermite/replay-384/residue-moment-382.json`.
The original and reproduced certificates are byte-identical. The replay
used CPython 3.15.0 with libmpdec 4.0.1. Observers around the original
local contexts and interval constructor do not alter any arithmetic
operation. Every arithmetic context had precision 60, Emin=-999999,
Emax=999999 and clamp=0, with precisely the prescribed FLOOR, CEILING or
HALF_EVEN rounding. All 6816009 constructed intervals had finite ordered
endpoints; nonzero endpoint adjusted exponents ranged from -1192 to 11.
Only Inexact and Rounded signals occurred: no underflow, subnormal,
clamped, overflow, invalid operation, float conversion or division by
zero was observed. Thus exponent limitations do not invalidate the
adjacent-representable exponential enclosures in this replay.

The arithmetic review checked the whole implementation: exact integer and
Decimal construction, rational conversion in directed contexts, endpoint
addition, all four endpoint products, reciprocal ordering for a denominator
interval excluding zero, repeated nonnegative integral powers, exact
sign-copy negation, and monotonic exponential endpoints padded by one
representable neighbor. All operations outside those contexts are exact
integer/Fraction operations, exact Decimal construction/comparison/sign
copies or indexing. Mesh points are exact dyadic rationals; Simpson's
weights and h/3 are included. Division by M_0 is valid because its entire
interval is positive. Setting g_0=1 is the exact identity M_0/M_0, not a
numerical approximation.

Every moment, normalized coefficient, centered coefficient, derivative
polynomial, quadrature error and tail field of the original certificate
was inspected in full. An independent Fraction-interval calculation from
the moment endpoints encloses g_j and b_2,b_3,b_4 inside the corresponding
Decimal intervals; the exact rational endpoints are retained in the audit
certificate. In particular the cancellation defining b_4 still gives

    1.67141028e-10 < b_4 < 1.67291635e-10,

strictly inside the required (1.6e-10,1.8e-10). The wider b_2 bounds in the
conclusion also pass. Exact polynomial identities in d independently
check the Laurent division, and exact rational arithmetic verifies
epsilon*12000000/768-beta/16=1/8000000 and the final 5/4 lower margin.
The inequalities use d>=6 and d/a>=12000000 only, so include every real
a>0, the ceiling equality and the small-a case D(a)=6. The strictness
comes from the coefficient enclosures even when those threshold
inequalities are equalities.

All 18 recorded audit checks pass. This is a reproduction and validation
of the local obstruction, not an additional theorem beyond the source
comparison or a formal machine proof. The analytic proof and code review
are essential: replay equality alone would not certify the integrals or
their relevance to actual Theta. No higher residue hierarchy or altered
grid was tested.

## Mathlib

Not checked. Availability of a full matching theorem is unknown. The
Hermite identities and simple-root facts above are imported from the
specified DLMF entries; the actual-coefficient calculation and interval
implementation have not been formalized. No Mathlib coverage or machine
proof is claimed: https://leanprover-community.github.io/mathlib4_docs/ .
