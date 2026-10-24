# L102 — Capped rational Taylor enclosures for the finite kernels

## Hypotheses

Let c_* be an arbitrary supplied rational number in [3/10,1/2], and
let 1<=n<=128 be an integer. Use the finite kernel of L101,

J_n(c_*) = integral_1^128 exp(-n*c_* y) log(y)/y dy.

Use L031's rational endpoint/min-max interval rules, with outward grid
q=2^-256 in place of its instance precision. All endpoints are integer
multiples of q; this is 256 fractional bits, as in the prior assessment.
Exact rational input conversion is allowed and checked by integer cross
multiplication. This is an arithmetic-operation bound, not a bit-time
bound independent of the supplied rational input's encoding length.

## Conclusion

There is the following completely specified rational interval scheme
on the unchanged 1016 panels [1+j/8,1+(j+1)/8], 0<=j<1016. It returns
an interval containing J_n(c_*) with radius strictly less than 2^-183,
hence at most 2^-50, uniformly in every permitted n,c_*.

The panel polynomial has degree at most 256. Each scalar series uses
at most 128 terms, except the 129-term degree-128 panel exponential;
all are below the cap of 256 terms. Each scalar exponential uses exactly
sixteen squarings. All discarded analytic terms, coefficient errors,
full polynomial products, integration rounding and panel summation
errors are included below. No derivative is evaluated.

A complete producing pass for all 128 kernels requires fewer than
2^38 elementary endpoint integer arithmetic/comparison operations in
the model specified below; another complete replay has the same bound.
This loose finite bound asserts neither practical runtime nor a storage
bound for an implementation. No program, parameter enclosure, coefficient
table, actual kernel value or derivative is produced here. The numerical
plan reproduces standard Taylor/integration methods. The separate
critical audit below passes for this fixed specialization.

## Proof

### Imported inputs, relevance and scope

Import the finite Taylor theorem, including its C^(d+1) hypothesis and
Lagrange remainder, from NIST DLMF v1.2.8 (2026-09-15), equations
[1.4.35--37](https://dlmf.nist.gov/1.4.vi). Import continuous integration
and change of variable from [1.4.26](https://dlmf.nist.gov/1.4.E26),
[1.4.28](https://dlmf.nist.gov/1.4.E28) and the nonnegative-weight
integration bound [1.4.29](https://dlmf.nist.gov/1.4.E29).
The elementary identities used are the exponential series
[4.2.19](https://dlmf.nist.gov/4.2.E19), logarithm series
[4.6.1 and 4.6.4](https://dlmf.nist.gov/4.6), exponential/logarithm
and power derivatives [4.7.3/7/8/10](https://dlmf.nist.gov/4.7),
positive-real logarithm additivity [4.8.2](https://dlmf.nist.gov/4.8.E2),
exponential multiplication [4.8.16](https://dlmf.nist.gov/4.8.E16),
and finite geometric summation [1.2.11](https://dlmf.nist.gov/1.2.E11).
L031 supplies the elementary exact rational outward arithmetic rules.
All imported hypotheses/cases were inspected in
`drafts/source-notes/2026-10-21-rational-kernel-source-review.md`;
the pre-existing SPECIALIZE assessment is
`drafts/literature/2026-10-21-rational-kernel-plan.md`.

These theorems are imported, not reproved. The needed specialization is
the uniform capped error and operation count. Every Taylor interval is
positive for log/reciprocal, and exp is entire, so the smoothness
hypotheses hold on each entire panel, including y=1. The optional unread
Taylor-model paper and unavailable integration library are not inputs.
L035 already imports this fixed curve's complex order; changing its
certificate provenance does not establish a new BSD case. Arbitrary-curve
rank/order comparison remains independent.

### Arithmetic convention and elementary error rules

For an interval I containing a specified exact scalar x, write
err(I;x)=max(|inf I-x|,|sup I-x|). Each directed endpoint rounding
adds less than q, and conservatively at most q, to this bound.
Addition/subtraction of grid endpoints is exact; negation is exact.
Multiplication uses the extrema of all four exact endpoint products
and rounds both outwards. Division here is only by specified positive
integers, followed by outward rounding. For example, when I contains x
and B contains b, with |B|<=K and err(B;b)<=epsilon,

err(round(B I);bx) <= K err(I;x)+|x| epsilon+q.       (1)

Indeed each unrounded product uv differs from bx by
u(v-x)+(u-b)x. This includes arbitrary signs and both endpoints.
Dividing this interval by an integer k>=1 divides the previous bound
by k and adds at most q. Clipping to a proved containing dyadic interval
preserves containment and can only decrease err. Such clipping is used
only in the explicit ranges given below. No non-dyadic clip is used.

For coefficient intervals I_k of a polynomial A=sum a_k s^k, define
Delta_A=sum_k err(I_k;a_k), and M_A=sum_k max(|inf I_k|,|sup I_k|).
Write ||A||_1=sum_k |a_k|. Then M_A<=||A||_1+Delta_A. A convolution
retains every pair of coefficients, rounds each product, and adds to
the appropriate initially zero coefficient by exact dyadic additions.
For a product A B with p coefficient pairs its output error satisfies

Delta_(AB) <= M_B Delta_A+||A||_1 Delta_B+p q.        (2)

This follows by applying the unrounded part of (1) separately to every
pair, summing, then adding at most q per product. It does not assume
that interval endpoints select one common pair of polynomials. All
identities and error bounds concern the entire coefficient arrays.

### Scalar logarithm constants

For the panel left endpoint a=1+j/8, 1<=a<128, choose the unique
integer k in {0,...,6} with b=a/2^k in [1,2). Set
z=(b-1)/(b+1), so 0<=z<1/3; log a=k log 2+log b.
For log 2 use z=1/3. The positive-real identity gives

H(z)=2 sum_(r=0)^127 z^(2r+1)/(2r+1).

Its omitted tail is nonnegative and is at most
2 z^257/[257(1-z^2)] <= (9/1028)3^-257 < 2^-384.   (3)

For the last comparison, 3^256>2^384 follows from 3^2>2^3;
the displayed prefactor and the remaining factor 1/3 are less than one.
This is a geometric tail comparison of the imported series; the
largest retained power is 255 and there are 128 terms.

Convert z outward to Z with err<=q and clip to [0,1/2]. Form T=Z*Z,
round outward and clip to [0,1/4]. Since z^2<=1/9, both clips contain
the true value. Formula (1) gives err(T;z^2)<=2q. Start W_0=Z and
form W_(r+1)=round(W_r T). Since |T|<=1/4 and |z^(2r+1)|<=1,
its errors obey E_(r+1)<=E_r/4+3q; from E_0<=q, all E_r<=4q.
Divide each W_r by 2r+1, sum by exact dyadic additions, and multiply
by two exactly. The endpoint error relative to H(z) is at most
2*128*5q=1280q<2^11 q. Enlarge both endpoints by q to cover (3).
The resulting log interval has err<2^12 q. Compute log 2 once and
log b by the same rule; form k log 2+log b using exact integer
multiplication/addition. As k+1<=7, its error is <2^15 q. Clip log a
to [0,7], which contains it because log a<log128=7 log2<7.
Here log2<1 follows, for example, from log x<=x-1 as recorded in L101.

This includes a=1 (z=0, k=0), without division by z or log a.
No logarithm evaluation is imported as a numerical primitive.

### Scalar exponential constants

Put alpha=n*c_*, so 0<alpha<=64. Set w=alpha*a/2^16; then
0<w<1/8. Convert this exact rational outward and clip W to [0,1/8].
Compute the 128-term polynomial sum_(r=0)^127 (-w)^r/r! by interval
recurrences V_0=1, V_r=round(-W V_(r-1)/r), rounding after both the
multiplication and division. True term magnitudes are <=1. From (1),
the errors satisfy E_r<=E_(r-1)/8+3q, hence E_r<4q.
The sum error is <512q. The degree-127 Taylor remainder for exp(-w)
is at most w^128/128!<=2^-384<q: its derivative magnitude is at most
one on [0,w]. Enlarge the summed interval by q on both sides and clip
to [0,1]. Its error is <2^10 q.

Square sixteen times, rounding outward and clipping each result to
[0,1]. Both exact and clipped values stay in [0,1], so each squaring
satisfies E_(i+1)<=2 E_i+q. Therefore the final interval C for
exp(-alpha*a) has

err(C;exp(-alpha*a)) < 2^27 q,    |C|<=1.            (4)

This retains the possible underflow-sized true positive constants;
zero is allowed as an enclosing endpoint. It never substitutes an
uncertified zero for the true exponential. The argument reduction uses
exactly sixteen squarings and no alternating-series assumption at a
large argument.

### Panel polynomials, truncation and coefficient arithmetic

Use y=a+s/8, 0<=s<=1, beta=alpha/8 in (0,8], and rho=1/(8a)<=1/8.
Define exact polynomials

E(s)=sum_(r=0)^128 (-beta)^r s^r/r!,
R(s)=(1/a) sum_(r=0)^64 (-rho)^r s^r,
H(s)=log a+sum_(r=1)^64 (-1)^(r+1)rho^r s^r/r.

The exact approximating integrand is exp(-alpha*a) E(s) R(s) H(s).
The full product P=ERH has degree at most 128+64+64=256.
No product coefficient, high-degree cross term or zero slot is omitted.

The finite Taylor/geometric remainders hold uniformly for s in [0,1]:

|E(s)-exp(-beta s)| <= 8^129/129! < 2^-272,
|R(s)-1/(a+s/8)| <= rho^65/a <= 2^-195,
|H(s)-log(a+s/8)| <= rho^65/65 <= 2^-195.             (5)

For the first strict comparison, 16!=20922789888000>2^44;
the factors 17--32, 33--64, 65--128 and 129 give respectively
lower bounds 2^64, 2^160, 2^384 and 2^7. Thus 129!>2^659 and
8^129=2^387. The exponential Taylor derivative on [0,beta s] has
magnitude at most one. The reciprocal error is the exact finite
geometric remainder with denominator 1+rho s>=1. The log derivative
formula and Taylor remainder on [0,rho s] give the third bound,
including its factor 1/65. All are real finite remainders.

Since e<3, from its positive series (r!>=2^(r-1) for r>=2, strictly
for some r), e^8<3^8<2^13. Consequently

||E||_1<=e^8<2^13,   ||R||_1<=8/7<2,
||H||_1<7+1/7<8.                                  (6)

Convert beta and rho directly from exact rationals to grid intervals,
clipping them to [0,8] and [0,1/8]. Convert 1/a and clip to [0,1].
Each conversion has err<=q. The logarithmic constant is enclosed above.
Compute E_r by the coefficient recurrence -beta*E_(r-1)/r, rounding
after both operations. As each true coefficient magnitude is <2^13,
(1) implies

e_r <= (8/r)e_(r-1)+(2^13+2)q.

Here e_0=0. Iterating, each accumulated factor satisfies
8^(r-j) j!/r! <= 8^(r-j)/(r-j)! for 1<=j<=r.
Hence e_r<2^14 e^8 q<2^27 q. Summing all 129 coefficients gives

Delta_E<2^35 q,   M_E<2^14.                         (7)

For R start with the converted 1/a and recur by multiplication by
-rho. True coefficients have magnitude <=1. Its errors satisfy
e_0<=q, e_r<=e_(r-1)/8+2q, so e_r<3q and

Delta_R<2^8 q,   M_R<4.                            (8)

For the nonconstant H coefficients compute powers of rho from 1 by
successive outward multiplication, then divide the r-th power by r
and apply its exact sign. Power errors satisfy the same recurrence
as R and are <3q; division adds at most q, so each coefficient error
is <4q. Including the log a interval yields

Delta_H <2^15 q+64*4q <2^16 q,   M_H<16.            (9)

Form Q=ER, retaining all 129*65=8385 coefficient pairs. Its exact
norm is <2^14, and (2), (7)--(8) give

Delta_Q < (2^37+2^21+2^14)q <2^38 q.

Form P=QH with its entire 193*65=12545 pairs. From (2) and (9),

Delta_P < (2^42+2^30+2^14)q <2^43 q,
||P||_1<2^17.                                     (10)

These estimates deliberately allow the large absolute coefficient norm
of the alternating exponential. No stability or cancellation assumption
is used to improve them.

### Integration, summed radius and all remainders

Compute the interval U=sum_(r=0)^256 P_r/(r+1), with outward division
and exact dyadic summation. It encloses integral_0^1 P(s) ds, with
endpoint error <2^43 q+257q<2^44 q. Its exact magnitude is <2^17.
Multiply U by the scalar exponential interval C, round outwards, then
divide by eight and round. By (4) and (1) the error of the product
before the last division is

< (2^44+2^17*2^27+1)q <2^46 q.

After the division it remains <2^46 q. This is endpoint error relative
to the integral of the exact approximating panel integrand, including
the dy=ds/8 factor. Sum all 1016 panels by exact dyadic addition. The
result I_n encloses the summed exact polynomial approximation, with
endpoint error <1016*2^46 q<2^56 q=2^-200. Thus its radius is also
strictly less than 2^-200.                               (11)

To compare the exact polynomial approximation with the true integrand,
write e=exp(-beta s), r=1/(a+s/8), h=log(a+s/8). On the entire panel,
0<e,r<=1, 0<=h<7; (5) implies |R|<2 and |H|<8. The telescoping
identity ERH-erh=(E-e)RH+e(R-r)H+er(H-h) gives error

<16*2^-272+8*2^-195+2^-195 <2^-191.                  (12)

Multiplication by exp(-alpha*a)<=1 cannot increase this error. The
complete integration path has length 127<128, so integration of this
uniform continuous bound gives total analytic approximation error
strictly less than 2^-184. This includes every panel remainder.
There is no numerical differentiation or interchange of infinite sums.

Enlarge both endpoints of I_n by exactly 2^-184. This is a grid
quantity, so the enlargement is exact. By (11)--(12) the resulting
K_n contains J_n(c_*), and

radius(K_n) < 2^-200+2^-184 <2^-183 <2^-50.           (13)

The midpoint is rational, as required by L101. The proof is uniform
for all 128 n and all supplied rational c_* in the stated closed
parameter interval; it asserts no evaluated midpoint. A later L101
application still needs actual certified narrow c endpoints, all exact
a_n, actual K_n, exact signed summation (eta=0), and zero exclusion
with B=2^-43+200*delta+4*sum(|a_n|/n)e_n. Other arithmetic and BSD
comparison gaps remain. The present inequality does not evaluate L''
and does not claim that it is nonzero.

### Finite operation bound and independent replay obligations

An interval primitive is an outward multiplication, division by a
positive integer, exact addition/subtraction/integer scaling, sign
change, clip, or direct rational input conversion. Count at most 32
endpoint integer arithmetic/comparison operations for each primitive;
integer multiply/divide, shift, floor/ceiling and comparison each count
as one operation, regardless of operand bit length. Four-product
interval multiplication fits this bound. Rational input conversions
use a bounded number of products/divisions; input bit complexity is
explicitly not bounded here. Arithmetic on the grid is always exact
integer arithmetic before the specified outward step.

Per n,panel the following loose primitive counts cover the procedure:

* Exact rational setup, three factor conversions and dyadic clips: 128.
* Two 128-term scalar log evaluations, their tails, combination and
  clipping (allowing log 2 to be recomputed): 2048.
* The scalar exponential series, sixteen rounded/clipped squarings
  and its argument conversion: 1024.
* All three polynomial coefficient arrays, including every sign,
  multiplication/division and initial conversion: 2048.
* Both full convolutions: 2*(8385+12545)=41860, one multiplication
  and one exact addition for every pair, including zeros.
* All 257 integration divisions/additions, scalar multiplication,
  factor 1/8, kernel accumulation and final enlargement: 2048.

The total 49156 is less than 2^16. Even assigning all setup and the
final enlargement to every panel overcounts them. Since
128*1016=130048<2^17, one full producing pass costs less than
2^16*32*2^17=2^38 endpoint operations. Repeating these finite operations
with independently written integer floor/ceiling and coefficient loops
has the same bound; producing plus one full replay is <2^39. There is
no time/byte cap or evaluated runtime claim in this proof-only step.
A subsequent implementation must select its own separately reviewed
resource contract before executing it.

Replay must check the rational input range; all 1017 endpoints and
1016 panels; every binary log reduction and exact input conversion;
every scalar term, sign, outward endpoint and clip; all 16 squarings;
every coefficient slot and all 20930 product pairs per panel; every
integration divisor 1,...,257; all panel sums and the final enlargement.
A rational endpoint check uses integer inequalities, so backend
rounding or transcendental tolerances are never trusted. The finite
error proof above certifies the method; a preview or sample of the
future arrays is not a full execution certificate. This step produces
no such arrays. The separate audit below validates the strict radius
bound, operation count and dependency scope before implementation.

### Separate critical audit — 2026-10-22, step 402

This is a proof audit under the pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-21-rational-kernel-plan-audit.md`, not an
implementation or numerical replay. The audit checks the complete proof
above, using L031 only for exact endpoint arithmetic and L101 only for
the kernel definition and its conditional downstream error contract.
The inspected primary theorem cases and exponential multiplication law
are recorded in `drafts/source-notes/2026-10-22-rational-kernel-audit-coverage.md`.
Their hypotheses are retained: the log and reciprocal arguments stay
positive, the exponential Taylor segments are real and nonnegative
before applying exp(-x), and every integrand is continuous on its
closed panel. At a Taylor expansion endpoint the identity is exact.
Positive-real log additivity has no phase ambiguity. No additional
source, optional Taylor-model theorem or numerical backend is assumed.

**Endpoint and constant containment.** Let q=2^-256. For every possible
endpoint pair u in B, v in I the exact identity
uv-bx=u(v-x)+(u-b)x proves (1); taking all four products therefore
handles signs and dependence between repeated quantities. Intersecting
with a stated containing interval cannot remove the exact value.
Summing the same identity over all coefficient pairs proves (2),
without needing endpoints to arise from one common polynomial.

The largest panel left endpoint is 1023/8<128. Its binary log reduction
has k<=6 and 1<=b<2; for log 2 itself the transformed argument equals
1/3. Thus every log series case has 0<=z<=1/3. Bounding all omitted
denominators below by 257 gives
2*z^257/(257*(1-z^2)) <= (9/1028)*3^-257.
Since 3^256>2^384, this is strictly below 2^-384, hence below q.
Conversion/clipping gives |Z|<=1/2; the error in its rounded square
is at most (1/2+1/3)q+q<2q. The power recurrence is consequently
E_(r+1)<=E_r/4+3q, so E_r<=4q. Each divided term has error at most
5q, and doubling the 128-term sum gives at most 1280q. Tail
enlargement adds q and shifting the exact target from the truncated
sum to the logarithm adds less than q: total error <1282q<2^12 q.
Integer combination
multiplies this by at most seven, below 2^15 q. The clip [0,7]
contains log a, including the endpoint a=1. No division by a vanishing
logarithm or transformed argument occurs.

For the scalar exponential, 0<alpha*a/2^16<1/8 holds even at n=128,
c_*=1/2 and a=1023/8. Each recurrence uses the unrounded true term
of magnitude at most one, so E_r<=E_(r-1)/8+3q<4q. There are 128
terms, starting with exact 1. The Taylor remainder has derivative
magnitude at most one on [0,w] and is bounded by 2^-384/128!<q.
The enlarged clipped starting interval therefore has error
<512q+q+q<2^10 q, including both enlargement and the remainder's
shift of the exact target.
If t is the current exact exponential and u,v are clipped endpoints,
|uv-t^2|<=|u|*|v-t|+|t|*|u-t|<=2E because all lie in [0,1].
After sixteen rounded squares the error is
<2^16*2^10 q+(2^16-1)q<2^27 q. Exponential multiplication identifies
the exact target as exp(-alpha*a). This argument remains valid when
the outward lower endpoint is zero and the true value is tiny.

**Panel remainders and coefficient arrays.** The substitution
y=a+s/8 covers each whole panel, has dy=ds/8 and gives beta<=8,
rho<=1/8. The first omitted powers of E,R,H are respectively
129,65,65. In the factorial comparison, 16!>2^44 and the successive
blocks 17--32, 33--64, 65--128 and 129 contribute lower exponents
64,160,384,7. Their sum with 44 is 659. Hence 8^129/129!<2^-272.
The exact reciprocal remainder has the divisor 1+rho*s>=1, while
the log Taylor derivative gives its additional divisor 65. This
verifies all three bounds (5), including the panel starting at one.
The elementary positive exponential series gives e<3, so e^8<2^13;
the geometric coefficient sums give ||R||_1<2 and ||H||_1<8.

For E, rounding multiplication then division yields
e_r<=(8/r)e_(r-1)+(2^13+2)q. The propagation of an error introduced
at index j is bounded by 8^(r-j)/(r-j)!, since r!/j!>=(r-j)!.
Summing this bound gives e_r<2^14 e^8 q<2^27 q. There are 129
coefficients, so Delta_E<2^35 q. For R the initial error is <=q
and the recurrence E/8+2q preserves E<3q; 65*3<2^8.
For H the same power recurrence, division by r and the audited
log constant give Delta_H<2^15 q+256q<2^16 q. These arguments
also prove the stated containing norms M_E<2^14, M_R<4, M_H<16;
there is no assumption that cancellation reduces interval errors.

The first convolution has all 129*65=8385 pairs and 193 output
slots, including zeros. The second has all 193*65=12545 pairs and
257 slots. Applying the endpoint error rule gives
Delta_Q<(2^37+2^21+2^14)q<2^38 q and
Delta_P<(2^42+2^30+2^14)q<2^43 q.
The exact norms are ||Q||_1<2^14 and ||P||_1<2^17.
Thus high-degree cross terms, signs and coefficient uncertainties
are covered by the written arrays and bounds; no term is discarded.

**Integral and final radius.** Dividing every P_r by r+1 and adding
gives endpoint error <(2^43+257)q<2^44 q for the exact polynomial
integral, whose absolute value is <2^17. Multiplication by C gives
error <(2^44+2^44+1)q<2^46 q. Division by eight adds at most q;
indeed (2^44+2^44+1)q/8+q<2^46 q, so the same displayed bound
still holds after this extra rounding. Summing 1016 panels gives
endpoint error <2^56 q=2^-200 about the summed exact polynomial
integral. Containment in this step concerns that polynomial integral,
not yet J_n; its endpoint-error bound also bounds the interval radius.

For the analytic difference, e,r<=1, h<7 and the remainders imply
|R|<2, |H|<8. The three terms in the displayed telescoping identity
are bounded by 16*2^-272, 8*2^-195 and 2^-195. In units of 2^-195
their sum is 2^-73+9<16, proving the strict 2^-191 bound without
an unaccounted cross term. The factor exp(-alpha*a)<=1 cannot
increase it. The union of the 1016 panels has length exactly 127,
so the total analytic error is <127*2^-191<2^-184. Adding exactly
2^-184 to each side is allowed on the original grid and yields
containment of J_n and radius <2^-200+2^-184<2^-183<2^-50.
Thus both the required radius and the stronger written radius pass;
neither has been weakened or inferred from a numerical preview.

**Finite operation count.** This audit checks the specified integer
operation model, not bit complexity, storage or practical speed.
Write c_*=u/v with positive integers u,v, without requiring fraction
reduction. Exact panel setup can use
alpha=n*u/v, a=(8+j)/8, w=n*u*(8+j)/(v*8*2^16),
beta=n*u/(8*v), rho=1/(8+j), 1/a=8/(8+j), and
z=((8+j)-8*2^k)/((8+j)+8*2^k).
At most seven binary comparisons select k. These explicit formulas,
range tests and conversions fit well within the 128-primitive setup
allowance, independently of the input's bit length.

One grid multiplication uses four integer products, at most six
comparisons for extrema and two directed grid divisions. Ceiling
can be implemented by integer negation and floor division. Including
two endpoint comparisons in an independent replay and loop/index
arithmetic still fits 32 integer operations. Grid addition, positive
integer division, sign, clipping, scaling and rational conversion
cost less; no gcd, transcendental evaluation or integer factorization
is a hidden primitive. Initialization/copying and disk operations are
outside this arithmetic model, not given an implicit time bound.

The per-panel ledger is conservative: each log series needs 127
power multiplications, 128 divisions, 128 additions and bounded
initialization/scaling/clipping; two fit 2048 primitives. The scalar
exp needs 127 signed multiply/divide recurrences, 127 additions,
sixteen multiply/clip pairs and bounded setup, within 1024. The
128 exponential, 64 reciprocal and 64 log coefficient recurrences
with signs/conversions fit 2048. The two convolutions require exactly
2*(8385+12545)=41860 multiplication/addition primitives. Integration
has 257 divisions and additions plus final operations, within 2048.
Together with setup these allowances sum to 49156<65536.
They also accommodate the bounded counter/range work; checks of
individual produced endpoints fit the per-primitive allowance above.
There are 128*1016=130048<131072 panel instances. Therefore each
whole arithmetic pass is <2^16*32*2^17=2^38 operations, and two
passes are <2^39. A replay can recompute every interval by separate
integer routines and compare every endpoint within this same model;
this is an existence/cost statement, not an executed replay.

**Verdict and remaining obligations.** All containment, cap, stronger
radius and finite-cost claims pass this separate audit. Degrees stay
128+64+64, scalar series stay within 256 terms, squaring count is
sixteen and the grid is unchanged. No failed stronger bound was found.
The direct mathematical inputs remain L031 and L101; the added explicit
exponential-product citation was already inspected in the ready
assessment. No new DAG edge or new mathematical result beyond this
known-method validation is asserted. Actual c endpoints, all Fourier
coefficients, numerical kernels, an implementation resource contract,
signed sum and zero exclusion remain missing. L101's factor four and
B=2^-43+200*delta+4*sum(|a_n|/n)e_n for exact summation remain required.
The arbitrary-curve BSD gap and L035's fixed-case source overlap remain.

## Mathlib

Not checked. No claim of a full matching Mathlib theorem or of absence
is made. The cited finite Taylor/integration results and L031's exact
interval rules are the mathematical inputs; the fixed cap/radius and
cost specialization is proved here and passes the separate audit above.
