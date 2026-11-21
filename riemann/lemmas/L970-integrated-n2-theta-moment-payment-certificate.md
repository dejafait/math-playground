# Lemma 970: an integrated n=2 theta-moment payment certificate

## Hypotheses

Use the actual positive theta kernel K of L019 and the actual moments
I_r(x)=integral_0^infinity K(u)H_r(x,u)du of L966. Fix only

    n=2, b=1/4, h=5184, Delta=h-b=20735/4,
    d1=4h^2/Delta^2=1719926784/429940225,
    d2=h/Delta=20736/20735.

Q=Q_{1/5184}(2) has exactly L966's prescribed definition, with its
algebraic square. Use the n=2 coefficients and normalization in
L967(5). No RH, simplicity, Stieltjes representation, numerical-zero
premise, assumed moment estimate or cumulant sign is a hypothesis.

## Conclusion

The actual moment ratios satisfy

    1/50 <= I_1(b)/I_0(b) <= 1/40,
    0 < I_1(h)/I_0(h) <= 1/100.

Keeping both negative terms of the complete expression gives

    Q > 423263556/10748505625 > 39/1000 > 0.                (1)

This is one fixed-index sign and a certificate of this integrated
payment test. It proves neither higher-index L966(16), all-degree
L030-L032/C032a positivity, nor RH. The complete proof and arithmetic
certificate below were written in step184 and independently audited
in step186. No originality or progress beyond the sources checked is
certified.

## Proof

### The complete signed propagation

Put r=I_1(b)/I_0(b), s=I_2(b)/I_0(b), t=I_1(h)/I_0(h).
Divide L967(5)'s integrated numerator by I_0(b)^2 I_0(h)>0.
Equivalently specialize L966(12) through the second logarithmic
derivative. The resulting exact expression is

    Q=d1*r+d2*s-d2*r^2-d1*t.                              (2)

L966 gives s>0. Once the claimed boxes for r,t are proved, positivity
of r and the positive coefficients imply

    Q > d1/50-d2/1600-d1/100
      =423263556/10748505625 > 39/1000.

Thus the positive second-derivative contribution may be bounded below
by zero, but the repeated-first-derivative block and the distant-h
resolvent are both fully charged. The rest of the proof establishes
the actual boxes, rather than assuming them.

### Finite integrands and their second derivatives

Set a=sqrt(x), so a=1/2 or 72, and define

    H0=cosh(a*u), H1=u*sinh(a*u)/(2a),
    H0'=a*sinh(a*u), H0''=a^2*cosh(a*u),
    H1'=sinh(a*u)/(2a)+u*cosh(a*u)/2,
    H1''=cosh(a*u)+a*u*sinh(a*u)/2.                         (3)

Primes in this subsection mean u derivatives. These are the r=0,1
specializations of L966's entire H series; no moment differentiation
or integration interchange is newly required here.

For v=pi*m^2*exp(2u), the mth kernel summand is
exp(u/2-v)P0(v), where the following three polynomials give its
value, first derivative and second derivative:

    P0(v)=8v^2-12v,
    P1(v)=-16v^3+60v^2-30v,
    P2(v)=32v^4-224v^3+330v^2-75v.                         (4)

Indeed v'=2v and each successive polynomial is
(1/2-2v)P(v)+2vP'(v), verifying every coefficient in (4).
Let K4 sum only m=1,...,4, and f_{x,r}=K4*H_r(x,.).
It is C^2 on [0,3], with the exact finite formula

    f''=K4''*H_r+2K4'*H_r'+K4*H_r''.                       (5)

The script evaluates (3)-(5) by outward interval arithmetic on every
closed integration cell. Polynomial cancellation cannot invalidate
an enclosure: signed operations use lower and upper endpoints.

### Omitted theta summands and the improper-u tail

For u>=0 put c=pi*exp(2u)>3. The consecutive-term ratio of
m^4*exp(-c*m^2) is at most

    16*exp(-3c) < 16*exp(-9) < 1/2.

For the last inequality exp(9)>=1+9+81/2>32 suffices.
Every summand of K is positive by L019. Dropping its negative
polynomial term and summing the geometric majorant therefore gives

    0<K-K4 <=10000*pi^2*exp(9u/2-25*pi*exp(2u)),            (6)
    0<K <=16*pi^2*exp(9u/2-pi*exp(2u)).                    (7)

For example, the sum starting at m=5 is at most
2*5^4*exp(-25c); multiplication by 8*pi^2*exp(9u/2)
gives (6). The same argument starting at m=1 gives (7).
On a cell of width delta, multiply the interval upper bound for (6)
by the interval upper bound of the appropriate nonnegative H_r and
by delta. Summing gives an upper bound for the omitted-m integral
on [0,3]. No series remainder is quadrature-sampled or assigned an
unknown constant, and only the finite K4 needs a derivative bound.

For u>=3 each of the four H factors in (3) is at most
u*exp(72u). For H0 use cosh(au)<=exp(au) and 1<=u;
for H1 use sinh(au)<=exp(au) and 1/(2a)<=1.
Thus every full integrand is at most

    16*pi^2*u*exp(phi(u)), phi(u)=77u-pi*exp(2u).

Here 9/2+72=76.5<=77, phi''<0, and the certified elementary
evaluation below gives phi'(3)<-2000. Hence
phi(u)<=phi(3)-2000(u-3) for u>=3. The exact exponential integral
of this linear bound yields the common improper-tail bound

    integral_3^infinity K H_r
      <=16*pi^2*exp(231-pi*exp(6))*(3/2000+1/2000^2)
      <2*10^(-451).                                      (8)

The certificate encloses phi'(3) between -2457.818 and -2457.817.
Both (6) and (8) bound positive omitted terms. They widen only the
upper moment endpoint; the quadrature error widens both endpoints.

### Outward arithmetic and quadrature certificate

Import the trapezoidal remainder theorem for a real C^2 integrand
on a compact interval from NIST DLMF version1.2.8,
[3.5.1-3](https://dlmf.nist.gov/3.5.i). Its hypotheses hold for each
f_{x,r} by its finite elementary formula. Applying its one-cell
case on each cell gives, with T the composite trapezoidal sum,

    |integral_0^3 f-T| <= sum_cells delta^3 sup_cell |f''|/12. (9)

This cites the quadrature theorem; the effective specialization (5)
and all bounds in (6)-(8) are supplied here because L019's
existential rapid-decay constant alone does not certify a computation.
The source assessment for this bounded attempt was saved before
invocation in
`drafts/literature/2026-11-10-integrated-theta-variance-review-182.md`.

Run

    python3 scripts/li-theta/integrated-moment-certificate-184.py

The initial and only mesh has N=3072 cells on [0,3], delta=1/1024,
and theta truncation m<=4. The full certificate is
`scripts/li-theta/integrated-moment-certificate-184.json`.
It retains every cell's complete four second-derivative enclosures
and omitted-theta bounds, aggregate trapezoidal enclosures, every
error, moment and ratio endpoint, exact d1,d2 and the signed bound.
No precision/mesh refinement was used.

Arithmetic uses 60-digit decimal endpoints with directed rounding
for every rational operation. Each finite decimal endpoint represents
an exact rational number. Products take the minimum/maximum of all
four directed endpoint products; reciprocals are taken only across
intervals excluding zero. No binary floating-point or library
transcendental evaluation is used. All ranges are within the declared
decimal exponent limits, so neither overflow nor underflow is used
as an estimate.

For completeness, the elementary-value certificates are as follows.
Pi uses Machin's identity pi=16 arctan(1/5)-4 arctan(1/239).
For each arctangent, its alternating rational series brackets the
value between a partial sum and the sum including its next term.
The script stops when the next term is less than 10^(-70), after
49 and 14 terms respectively, and saves the exact rational bounds.
Machin's identity follows directly from tangent addition: if
A=arctan(1/5) and B=arctan(1/239), then tan(2A)=5/12,
tan(4A)=120/119, and tan(4A-B)=1. Also 0<4A-B<4/5<pi/2,
using pi>3; hence 4A-B=pi/4. This verifies the branch.
The resulting outward pi interval is

    [3.14159265358979323846264338327950288419716939937510582097494,
     3.14159265358979323846264338327950288419716939937510582097495].

For an exponential at a scalar rational endpoint y, reduce |y| by
a power of two to z<=1/8. Sum sum_{j=0}^{30} z^j/j! by interval
operations, with tail between zero and 2z^31/31!. The tail bound
follows because the first omitted term is z^31/31! and successive
term ratios are at most 1/256. Repeated squaring encloses exp(|y|);
for negative y, reciprocation encloses exp(y). Monotonicity then
encloses exp on any interval by its endpoint enclosures. Cosh and
sinh use the two enclosed exponentials and their exact half-sum
and half-difference. Thus all errors in their evaluation, including
cancellation, are included in the saved endpoints.

The complete aggregate errors, inspected after the run, imply these
conservative upper bounds (quadrature errors are absolute):

| Moment | Quadrature error | Omitted-m integral on [0,3] |
| --- | --- | --- |
| I_0(b) | 8*10^(-7) | 6*10^(-32) |
| I_1(b) | 5*10^(-8) | 3*10^(-36) |
| I_0(h) | 8.63*10^21 | 8*10^(-32) |
| I_1(h) | 7.69*10^19 | 4*10^(-36) |

Each moment additionally has the common positive error (8).
Combining the trapezoid enclosure and all errors produces the
following outward rational enclosures; displayed decimals are exact:

| Moment | Lower endpoint | Upper endpoint |
| --- | --- | --- |
| I_0(b) | 0.4999992 | 0.5000008 |
| I_1(b) | 0.01154780 | 0.01154791 |
| I_0(h) | 6.22365*10^25 | 6.22539*10^25 |
| I_1(h) | 5.37525*10^23 | 5.37679*10^23 |

In particular both denominator lower endpoints are strictly positive.
Dividing the full certificate endpoints outward gives

    r in [0.02309557, 0.02309585],
    t in [0.00863441, 0.00863928].                          (10)

These displayed ratio endpoints use the unrounded moment intervals
in the certificate. They are not obtained by narrowing the coarser
displayed moment table. The certificate's full intervals for r,t
are respectively contained in (10), and (10) lies strictly inside
the proposed boxes [1/50,1/40] and (0,1/100]. This proves those
boxes and then (1) by the complete propagation (2). Direct use of
the full endpoints gives the supplementary lower bound
Q>0.0572973163569718; (1) uses only the conservative rational boxes.

### Scope and remaining gaps

The proof combines the known trapezoidal remainder theorem, its
explicit actual-kernel specialization and a finite outward certificate.
It does not reprove an ordinary Li sign or use one as a substitute
for the regularized observable. The local advance is the nominated
quantitative base case; the bounded source search did not certify
novelty of this fixed-index result. Other methods might already
imply the sign.

L967/L969 and C969a's negative pointwise regions remain valid:
positive integrated payment does not make their fixed kernels or
marginal pointwise positive. No negative block was omitted and no
algebraic square was changed into a modulus square. The positive
I_2 contribution was used only through L966's established strict
positivity. All higher n and a uniform changing-partition mechanism
remain unproved. Audited L968 already supplies the conditional
all-index prescribed-sign implication to RH; the missing premise
is that all-index sign, not its implication. L968 is downstream
context, not an input to this fixed-index proof. One index cannot
resolve the main gap.

### Independent conceptual audit, step186

The audit accepts (1)-(10) without changing their hypotheses, formulas
or endpoints. Its mathematical inputs remain L019, L966 and L967.
The ready SPECIALIZE coverage is
`drafts/literature/2026-11-10-l970-independent-audit-coverage-185.md`;
its direct DLMF and Python documentation URLs cover the imported
quadrature and directed-arithmetic contracts, not the effective bounds.
This is reproduction and validation of the existing finite result,
not a new sign theorem beyond the sources checked.

Independently differentiating exp(u/2-v)P(v) gives the operator
P -> (1/2-2v)P+2vP', which recovers every coefficient in (4).
Direct differentiation of cosh(au) and u*sinh(au)/(2a) recovers (3),
and the finite product rule gives (5). On u>=0 the consecutive ratio
of m^4 exp(-c*m^2) is at most 16 exp(-3c)<1/2 since c>=pi>3
and exp(9)>32. Starting at m=5 or m=1 gives exactly the constants
10000 and 16 in (6)-(7). Positivity licenses their use solely as
upper bounds for omitted mass. For u>=3, all four H factors obey
H<=u exp(72u); phi''<0 and the verified phi'(3)<-2000 then give
(8) by integrating (3+t)exp(-2000t). These arguments control entire
omitted regions, rather than checking their values at selected points.

For arithmetic, every Decimal string/int is an exact rational input.
Directed addition and multiplication enclose their exact rational
operations, with all four products used for signed multiplication.
Exact copy_negate reverses interval endpoints. For an interval
excluding zero, 1/x is decreasing on either of its possible sign
domains, giving precisely the reciprocal endpoints used in division.
Repeated interval multiplication encloses every nonnegative integer
power even when cancellation makes the enclosure wide. The original
positive-argument exponential reduction chooses k using upward-rounded
halving, so its actual |y|/2^k is <=1/8. Its positive degree-30
Taylor sum and tail 2z^31/31! enclose exp(z), since all subsequent
term ratios are <=1/256. Squaring and reciprocal operations preserve
the enclosure, and monotonicity handles interval arguments. Machin's
branch and both exact alternating bounds were checked as above.
No Decimal.exp or float evaluation is used in either implementation.

Run `python3 scripts/li-theta/integrated-moment-audit-186.py`.
This program imports no construction code. It uses 90-digit directed
intervals, exact-rational range reduction to |z|<=1/16, a degree-50
positive exponential series with tail 2z^51/51! (subsequent ratios
<=1/832), and independent fixed alternating sums with 80 and 30
terms for Machin's identity. Thus its elementary errors are independently
bounded, rather than estimated by agreement of floating-point values.
It reconstructs the derivative polynomials by the displayed operator.

The complete certificate is
`scripts/li-theta/integrated-moment-audit-186.json`. All 3072 cells
have their exact endpoints and indices checked. For each of the four
integrands, every independent second-derivative interval is contained
in the original saved interval, and every saved omitted-theta upper
bound dominates the independent upper bound. All 12288 derivative
and 12288 tail comparisons pass. Exact Fraction sums of the original
cell maxima times delta^3/12 and omitted-theta uppers times delta
are enclosed by the saved aggregate errors. Independent evaluation
of all 3073 nodes gives trapezoidal intervals contained in the saved
ones. Both improper-tail intervals also contain the independent
enclosures, whose slope upper endpoint is below -2457.817 and whose
tail upper endpoint is below 2*10^(-451). No overflow, underflow,
subnormal, clamped, invalid or zero-division signal occurred in the
independent arithmetic. Finite exponent ranges are amply sufficient:
on these cells u<=3, exp(2u)<404, v<25856 and the elementary
exponential arguments have magnitude below 40400.

Exact rational checks then verify all four moment propagations,
positive denominators, every displayed moment/error/ratio box, both
required boxes and every coefficient and negative term in (2).
The full conservative lower endpoint is exactly
423263556/10748505625>39/1000. The complete direct rational expression
d1*r_lo-d2*r_hi^2-d1*t_hi is enclosed in the original saved direct
interval and exceeds 0.0572973163569718. Strictness uses only the
already established d2*s>0. All 48 aggregate checks pass, with no
failed cells or residual failure fields; full selected checks, both
tail endpoints and signed propagation were inspected after execution.
The first audit run stopped only on Python's integer-string formatting
limit for a long exact tail sum; the unchanged arithmetic was rerun
after disabling that formatting limit. Original evidence is preserved.

The all-index inequality remains open. This audit makes no all-n
extrapolation and changes none of the retained pointwise obstructions.

## Mathlib

Full matching coverage for these moment boxes, the regularized sign,
and this computational certificate was not checked and is unknown.
No Mathlib theorem is imported. Elementary interval, derivative or
quadrature support alone would not certify these effective endpoints.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
