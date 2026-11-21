# Lemma 947: fixed tilted primitive endpoint contrast

## Hypotheses

Use exactly L938's continuous signed density v, all 34 rows, twelve
labelled factors, factorials and retained normalization M_0^12. In
particular v is not the density for a determinant with a reduced
normalization. Put

    U(E) = integral_0^E exp(t/10) v(t) dt.

Use the unchanged L938 degree256 kernel polynomial p, 257 nodes,
theta cutoff8, precision200, rational coefficient grid10^-120, and its
full uniform error epsilon. The numerical statements inherit L938's
directed Decimal/exponential/pi inclusion and exact-integer execution
contracts. Step50's polynomial identity and step75's audit are reused,
not independently rerun here; correctness of their library and integer
implementations remains an explicit qualification. There is no RH,
contact, determinant-sign or crossing-count hypothesis.

## Conclusion

Subject to those arithmetic contracts, the following outward inclusions
hold for the actual density:

| E | lower bound for U(E) | upper bound for U(E) |
|---:|---:|---:|
| 1/4 | -3.746311642022141*10^-54 | -3.746276087699016*10^-54 |
| 4 | 8.935649629627030*10^-35 | 8.952439684011220*10^-35 |

Thus U(1/4)<0<U(4). This is a fixed two-endpoint contrast. No
uniqueness, simplicity or global count of primitive zeros, tail join,
parameter sign, contact exclusion, other-degree conclusion or RH
conclusion is claimed. The result is a local specialization of known
Taylor/integration methods, not a new general theorem beyond the
sources checked. The independent step85 audit below validates the
numerical implementation under the retained execution contracts.

## Proof

### Absolute whole-interval bounds

Let v_p be L938's polynomial-kernel density on [0,8]. L938's simplex
formula, all twelve positive half-integer beta parameters, and all34
rows give, with

    W = sum_alpha |c_alpha|/product_k(k!)^alpha_k = 293/540,
    Z = W/(2^36*17!) = 293/13199033127778602178314240000,

the following *pointwise* bounds for 0<=t<=4:

    |v(t)-v_p(t)|/pi^6 <= 12 epsilon 8^11 Z t^17,
    |v_p(t)|/pi^6 <= 8^12 Z t^17.                              (1)

Indeed K<7 and epsilon<10^-34<1 imply |p|<8 on the entire
interval. For the difference of twelve products use L938(16);
for the absolute polynomial product use 8^12. Integrating the same
positive simplex weight in each row gives precisely Z, as in
L938(9),(17). This argument bounds absolute densities before any
signed integration, rather than weighting an already cancelled cell
error. At t=0 both continuous densities are zero and (1) still holds.
The integrable beta weights include the singular k=0 factors, whose
individual boundary values do not affect the integral.

### Fixed exponential enclosure and combined error

Fix T(t)=sum_(j=0)^32 (t/10)^j/j!. Use the exponential power series
[DLMF4.2.19](https://dlmf.nist.gov/4.2#E19), and Taylor's theorem with
Lagrange remainder, [DLMF1.4.35–36](https://dlmf.nist.gov/1.4#E35),
for the C^33 function exp(x) on [0,2/5]. These are imported standard
results; no reproof is needed. For x=2/5 the positive degree32 sum
plus its tail bound

    sum_(j=0)^32 x^j/j! + (x^33/33!)/(1-x/34) < 3/2             (2)

is an exact rational comparison saved in the certificate. The tail
bound follows since every successive tail-term ratio is at most
x/34=1/85. Consequently exp(t/10)<3/2 on [0,4]. Taylor's theorem
applies to every t>0 there, with the endpoint t=0 exact, and gives

    |exp(t/10)-T(t)| <= (3/2)*(E/10)^33/33!,   0<=t<=E<=4.     (3)

All derivatives required by the cited theorem exist on the closed
interval; their bound is supplied by (2). Define the exact signed
polynomial center and two positive error allowances, with pi^6 removed:

    c(E) = pi^-6 integral_0^E T(t)v_p(t)dt,
    A(E) = Z E^18/18,
    r_K(E) = (3/2)*12 epsilon 8^11 A(E),
    r_T(E) = (3/2)*(E/10)^33/33! *8^12 A(E).

The exact decomposition

    exp(t/10)v(t)-T(t)v_p(t)
       = exp(t/10)(v(t)-v_p(t))+(exp(t/10)-T(t))v_p(t)

combined with (1)–(3) proves

    |U(E)/pi^6-c(E)| <= r_K(E)+r_T(E).                          (4)

This pays the full weighted kernel error and finite exponential error.
There is no missing cross term: the kernel difference is multiplied
by the exact exponential, already bounded by 3/2, while the Taylor
error is multiplied by the full absolute bound for v_p. No assertion
about the polynomial replacement outside the compact interval is used.

### Exact finite signed integration

Write L938(18) as

    v_p(t)/pi^6 = (1/D) sum_(l=0)^3072 R_l t^(17+l)/(17+l)!,
    D=C^12,

using its complete unchanged integer coefficients and denominator.
Set R_l=0 outside this range. Multiplication by the stipulated T gives

    S_m=sum_(j=0)^min(32,m) R_(m-j) binom(17+m,j)10^(32-j),
    c(E)=1/(D*10^32) sum_(m=0)^3104 S_m E^(18+m)/(18+m)!.       (5)

To verify the coefficient, put l=m-j: multiplication by t^j/(10^j j!)
contributes R_l*(17+m)!/((17+l)!j!10^j) in the factorial basis.
That is R_l binom(17+m,j)/10^j, exactly (5). Thus all operations
through integration are finite integer/rational operations; there is
no quadrature, floating-point cancellation or interchange of infinite
signed sums.

For E=a/q in lowest terms, put d=3104 and H=(18+d)!. The integer
numerator for (5), over D*10^32*H*q^(18+d), is

    sum_(m=0)^d S_m [H/(18+m)!] a^(18+m) q^(d-m).               (6)

Every factorial quotient is an integer. The script evaluates (6)
both by descending homogeneous Horner accumulation and independently
by forward monomial accumulation, checking all factorial divisions
and exact equality of the two signed rational results. The whole
degree3104 product and exact centers/errors are retained on disk.

### Certificate and comparisons with the required margin

Reproduce with `python3 scripts/heat/l938-tilted-endpoints-81.py`.
Its full certificate is `scripts/heat/l938-tilted-endpoints-81.json`.
It loads every selected coefficient, checks the unchanged input hashes,
all5101 step50 and15620 step75 audit flags, the inherited zero residual
and coefficient-uniqueness bound, every one of the257 coefficient
allowances, every canonical row and beta weight, epsilon, D and (2).
The large polynomial identity evaluation, theta-node production and
transcendental libraries are not rerun; those inherited qualifications
are not replaced by a checksum. The complete exact product, endpoint
centers, both separate radii, pi enclosure and actual final intervals
are recorded, with no failed checks.

For scale, these are outward bounds on the exact normalized quantities:

| E | c(E) | r_K(E) | r_T(E) |
|---:|---:|---:|---:|
| 1/4 | [-3.896750545872593,-3.896750545872592]*10^-57 | [1.849111856134714,1.849111856134715]*10^-62 | [2.887213200283499,2.887213200283500]*10^-117 |
| 4 | [9.303250667460876,9.303250667460877]*10^-38 | [8.732183852487454,8.732183852487455]*10^-41 | [7.423316373475691,7.423316373475692]*10^-56 |

Exact rational checks place c/(r_K+r_T) in
[-210736.3344702226,-210736.3344702225] at1/4 and
[1065.397937631688,1065.397937631689] at4. The required strict-sign
threshold is absolute ratio greater than1, with the stipulated negative
and positive center signs. Both pass without any budget change.
Finally multiply the full interval (4) by the inherited positive pi^6
enclosure, taking the minimum and maximum of its four endpoint products.
Directed 16-digit decimal conversion is checked against exact rationals.
This proves the two displayed actual-U inclusions. The complete summary
and selected exact constants, not just truncated previews, were inspected.

### Independent endpoint audit — 9 November 2026, step85

The prior SPECIALIZE assessment83, separately approved in step84,
covers precisely this endpoint audit together with C947a's compact
calculus. The audit imports the cited exponential/Taylor results with
their stated smoothness and compact-domain hypotheses; no new theorem,
budget or approximation is introduced. Reproduce with

    python3 scripts/heat/audit-c947a-endpoints-85.py

The complete report is `scripts/heat/c947a-endpoint-audit-85.json`;
all114230 checks pass with no failures. The independent full ordinary
product is `scripts/heat/c947a-ordinary-product-85.json`. Neither the
step81 producer nor any of its functions is imported or executed.

Here is the independent calculation, including its exact denominators.
Let H=3089!, J=32!, d=3104 and let D be the denominator in (5).
For every 0<=l<=3072 and 0<=j<=32 form integers

    B_l=R_l H/(17+l)!,      T_j=10^(32-j)J/j!,
    P_m=sum_(l+j=m) B_l T_j,          0<=m<=d.

All divisions are exact, checked individually. This is multiplication
in the ordinary power basis, so

    T(t)v_p(t)/pi^6 = t^17 sum_m P_m t^m/(D H 10^32 J).

The verifier constructs every P_m by integer convolution, independently
of (5)'s binomial-coefficient formula. For every m it verifies the full
signed equality

    P_m (17+m)! = S_m H J.

Every residual is zero; no selection of coefficients, modular test or
floating cancellation is used. The complete P_m and all3105 residuals
are saved, including all zero coefficients.

For integration use L=lcm(18,19,...,3122), independently of (6)'s
factorial denominator. For E=a/q in lowest terms the exact center is

    sum_(m=0)^d P_m [L/(18+m)] a^(18+m)q^(d-m)
        / [D H 10^32 J L q^3122].

Each divisor18+m divides L. The numerator is accumulated in separate
even/odd ordinary-power sums. This is the termwise integral of the
finite polynomial just displayed and agrees exactly with both complete
saved endpoint centers. The report retains the two parity numerators,
common denominator and reduced center for each endpoint.

Independently rebuild all257 coefficient allowances and epsilon, all34
canonical rows with twelve labelled positive beta parameters, and W,Z.
The beta normalization cancels each (2k)! against
Gamma(k+1/2)/sqrt(pi)=(2k)!/(4^k k!), leaving exactly
2^-36/17! times the stated row weight. This checks the pointwise
absolute-density bound, not merely the cancelled cell bound.
The finite exp(2/5) comparison is exact; its first omitted term has
all later successive ratios <=1/85. Smoothness on [0,2/5] then permits
the cited Taylor remainder. The error decomposition above uses the
exact exponential on v-v_p and T's error on v_p, so neither a cross
term nor a singular-face contribution is missing. At zero, the
continuous densities and both pointwise majorants vanish.

Every constant, both separate positive error radii, their sum, the
full normalized interval, signed center/error ratio, pi enclosure and
actual endpoint interval is compared as an exact rational. The final
pi multiplication is checked independently by choosing the scaling
endpoint according to each bound's sign. Every displayed16-digit
outward interval is verified against those exact rationals, with no
new Decimal rounding assumption. The strict ratios remain
[-210736.3344702226,-210736.3344702225] and
[1065.397937631688,1065.397937631689], respectively, against |ratio|>1.
Both stipulated signs and both actual-U intervals in the Conclusion pass.

For the combined audit, all saved step50,75,78 and81 check entries
and their input hashes are read completely. The step50 integer identity
and its full coefficient uniqueness bound and theta-node production
remain inherited audited inputs. The step75 derivative and step78 cover
are used only for C947a, not for these endpoint signs. Hashes do not
independently establish their mathematics or verify their libraries.
The present audit
reconstructs the new endpoint algebra and errors, and preserves exactly
the original Decimal/exponential/pi and integer execution qualifications.
It establishes local numerical reliability within that scope, not a new
general theorem, global variation bound, parameter sign or RH result.

## Mathlib

Full or supporting Mathlib coverage of this exact density, weighted
majorant and certificate is not checked. Unknown availability is not
evidence of absence. The source inputs used here are the cited standard
exponential series and Taylor theorem, together with L938's already
qualified density and exact beta-integration identities.
