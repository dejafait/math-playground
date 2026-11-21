# C029v — The fixed N=6 quadratic/Jensen defect has nonzero bulk modes

## Hypotheses

Use C029m's full real coefficients, including all odd terms, from
Alexey Kuznetsov, *Expansion of the Riemann Xi Function in
Meixner-Pollaczek Polynomials*, Canad. Math. Bull. 51(4) (2008),
561–569, [primary source](https://doi.org/10.4153/CMB-2008-055-0),
equations (2)/(4)/(9)/(13), printed pp563–564/566, and the Jensen
weights pp568–569. Explicitly,

    p_(-1)=0, p_0=1,
    (n+1)p_(n+1)=t p_n-(n+1/2)p_(n-1),
    u_n=-n!/sqrt(2) * sum_(h=0)^n
      4^h(4^(h+1)-1) B_(2h+2)(2pi)^(h+1)
      *sin(pi(n-h)/2+pi/8)/((n-h)!(2h+2)!),
    beta_k=4k(k-1)u_(k-2)+(8k^2+12k+7)u_k
           +(2k+3)(2k+5)u_(k+2).

The first term of beta_k is omitted for k=0,1; B_1=-1/2. Only
u_0,...,u_8 and beta_0,...,beta_6 are needed. Define

    q(t)=1+4t^2,  A_8=sum_(k=0)^8 u_k p_k,
    w_k=6!/((6-k)!6^k) for 0<=k<=6,  w_k=0 for k>6,
    J_6[p_k]=w_k p_k,
    T_6=sum_(k=0)^6 w_k beta_k p_k,
    R_6=J_6(q A_8)-q J_6(A_8).

The operator is defined on finite polynomials by this basis. The
recurrence gives deg(p_k)=k with leading coefficient 1/k!, so the
basis coordinates and J_6 are unambiguous. Put S=sin(pi/8)/sqrt(2)>0,
as in C029n. Use precisely C029n's fixed rational enclosures of pi
and sqrt(2), with its justification by Machin's identity, 48-term
arctangent bounds and integer squared endpoints. No new precision
or approximation hypothesis is introduced.

## Conclusion

The numerator identity J_6(q A_8)=T_6 holds exactly. If c_k denotes
the coefficient of p_k in R_6/S, the following are closed rational
enclosures (each decimal is an exact rational with denominator 10^12):

| Coefficient | Lower bound | Upper bound |
| --- | ---: | ---: |
| c_2 | -22.184393875256 | -22.184393875255 |
| c_3 | -6.599923769988 | -6.599923769987 |
| c_4 | -2.675150248313 | -2.675150248312 |

In particular all three coefficients are strictly negative, and

    R_6 not in span_R{p_0,p_1,p_5,p_6,p_7,p_8}.

This rejects the fixed N=6 endpoint-only defect ansatz. It does not
rule out an eventual-only relation, a different auxiliary polynomial,
a nonlocal signed mechanism or other Jensen weights. It supplies no
root count, auxiliary hyperbolicity, Hermite index bound, all-degree
positivity, or proof/disproof of RH. The finite identity and the three
strict rational bounds were independently audited in step2046.

## Proof

**Finite multiplication and the numerator.** Import source (9), the
quadratic basis multiplication identity obtained from (2). To check
its use at the bottom indices and its implementation here, apply (2)
twice: for n>=2,

    q p_n=4(n+1)(n+2)p_(n+2)+(8n^2+12n+7)p_n
          +(2n-1)(2n+1)p_(n-2).

Indeed t p_n=(n+1)p_(n+1)+(n+1/2)p_(n-1); the coefficient of p_n
in t^2 p_n is (n+1)(n+3/2)+n(n+1/2). Multiplying by four and
adding p_n gives the displayed middle coefficient. Directly at the
bottom, p_1=t and 2p_2=t^2-3/2 give

    q p_0=7p_0+8p_2,   q p_1=27p_1+24p_3.

These are also the nonnegative-index terms of the displayed formula;
no p_(-2) or negative-index u is evaluated. This is a finite
applicability/implementation check of the imported identity, not a
new multiplication theorem. The script additionally constructs
p_0,...,p_10 from (2), multiplies each p_n, 0<=n<=8, directly by q in
monomials and converts back by triangular elimination. All eleven
components agree for every n, including 0 and 1.

Collecting the coefficient of p_k in q A_8, for 0<=k<=6, gives

    4k(k-1)u_(k-2)+(8k^2+12k+7)u_k
       +(2k+3)(2k+5)u_(k+2)=beta_k,

with the same omissions at k=0,1. All needed upper coefficients
u_(k+2) are included in A_8. J_6 kills every mode above six and
weights each retained coefficient by w_k. This proves the full
numerator identity. The exact certificate also verifies that all
eleven components of J_6(q A_8)/S-T_6/S are zero, independently of
any numerical interval evaluation. No infinite expansion or analytic
limit is used.

**The three bulk coefficients.** Write v_n=u_n/S. In a retained
bulk row k=2,3,4 the middle multiplication terms cancel, leaving

    c_k=4k(k-1)(w_k-w_(k-2))v_(k-2)
         +(2k+3)(2k+5)(w_k-w_(k+2))v_(k+2).

Here (w_0,...,w_6)=(1,1,5/6,5/9,5/18,5/54,5/324). Thus

    c_2=-(4/3)v_0+35v_4,
    c_3=-(32/3)v_1+(275/6)v_5,
    c_4=-(80/3)v_2+(12155/324)v_6.

For a complete finite specification of their values, put x=pi and
r=1+sqrt(2). By the elementary half-angle identity used in C029n,

    sin(pi*m/2+pi/8)/sin(pi/8)=1,r,-1,-r

for m congruent to 0,1,2,3 modulo four. Substitute this into the
given u_n formula and use

    (B_2,B_4,...,B_18)=
    (1/6,-1/30,1/42,-1/30,5/66,-691/2730,7/6,-3617/510,43867/798).

The resulting exact expressions in Q(sqrt(2))[x] are

    c_2=-(101/6)x-(140/3)r*x^2+112x^3
         +(544/3)r*x^4-(3968/27)x^5,
    c_3=-(211/12)r*x+(437/6)x^2+(2200/9)r*x^3
         -(37400/63)x^4-(545600/567)r*x^5+(442240/567)x^6,
    c_4=(3515/648)x+(9275/162)r*x^2-(23158/81)x^3
         -(1653080/1701)r*x^4+(12057760/5103)x^5
         +(19547008/5103)r*x^6-(47532544/15309)x^7.

These are the actual-coefficient calculations not supplied by the
source theorem. Their computation is needed to decide this test;
no novelty beyond the checked sources is claimed. A nonzero formal
polynomial would not alone certify its value at pi and sqrt(2).
The strict enclosures supply that additional step.

**Rational verification.** Reuse the proved C029n intervals exactly.
The script regenerates their 48-term Machin construction and the
integer-square-root construction and verifies equality to the stored
input intervals. It also regenerates Bernoulli numbers through B_18
by their defining recurrence and checks every normalized u and beta
polynomial against the C029n certificate. This guards the distinction
between the source's u_n, full beta_n, and its other auxiliary sequences.

For each displayed c_k polynomial, enclose a+b sqrt(2) by the fixed
sqrt(2) interval, reversing endpoints for b<0, and evaluate by interval
Horner arithmetic in the fixed pi interval. Interval addition adds
endpoints and multiplication uses the extrema of the four products.
These operations enclose the exact value by induction. All operations
are on integers and Fractions. Outward rounding to the 10^(-12) grid
gives precisely the table in the conclusion. Each upper endpoint is
negative, so none of these values is zero. S>0 transfers the signs
to the unnormalized coefficients. Linear independence of the p_k
then excludes the specified endpoint span.

Reproduction command, relative to this notebook:

    python3 scripts/pollaczek/jensen_quadratic_endpoint_2044.py

Full exact coefficients, all basis polynomials through p_10, both
quadratic multiplication constructions, every normalized u_0,...,u_8,
weights, both terms of R_6, its full coefficient vector, numerator
residual, full rational interval endpoints, input hashes and failures
are saved in `scripts/pollaczek/jensen-quadratic-endpoint-2044.json`.
All 38 implementation/identity checks pass; failures are empty. The
negative mathematical test outcome is recorded separately from those
checks. The complete bulk polynomials and their unrounded endpoints,
all numerator residual entries, constants and check flags were inspected
with the scoped JSON inspector, using selected full values.

No sweep, root isolation, precision increase, fitted correction,
continuous deformation, double-zero hypothesis or analytic convergence
claim enters this proof. C029m's eventual index premise and its
qualified weighted-limit/upstream[9] input remain separate.

**Independent audit2046.** The unchanged SPECIALIZE assessment2044,
completed by source recovery2045, covers exactly this finite replay.
The audit reads C029m's full formulas and C029n's enclosure proof;
it imports no code from calculation2044 or the C029n implementation.
The original certificates are comparison data, not sign premises.
Reproduce the independent standard-library calculation with

    python3 scripts/pollaczek/jensen_quadratic_endpoint_audit_2046.py

Its full certificate is
`scripts/pollaczek/jensen-quadratic-endpoint-audit-2046.json`.
It stores all independently reconstructed coefficients, the eleven
numerator residual entries, all multiplication columns, the full
unrounded rational endpoints, comparisons, input hashes and failures.
All 433 exact checks pass; failures are empty. The full bulk entries,
all residual entries and both constant intervals were inspected with
selected full JSON values. The other saved coefficient data were
compared in their entirety by exact equality, not by previews or labels.

For clarity about independence and completeness, the new implementation
uses sparse polynomials in t,x,y over Q, reducing y^2=2 at every
multiplication. The recurrence constructs all p_0,...,p_10; direct
monomial multiplication by 1+4t^2 and descending triangular elimination
give every basis coordinate. Its denominator at degree k is precisely
the nonzero leading coefficient 1/k!. The source-(9) columns, including
both bottom cases, are constructed separately and agree in every row.
The full coefficient formulas reconstruct u_0/S,...,u_8/S and all seven
beta_k/S with the four phases and the original weights. Bernoulli
numbers are independently generated as

    B_n=sum_(j=0)^n (-1)^j j! S(n,j)/(j+1),

where S(n,j) are Stirling numbers of the second kind. This finite
identity follows by taking the coefficient of z^n/n! in
sum_(j>=0)(-1)^j(e^z-1)^j/(j+1)=z/(e^z-1); coefficient extraction
through n uses only j<=n, so no analytic convergence is involved.
It retains B_1=-1/2 and reproduces every B_0,...,B_18 entry of C029n.
All nine u and all seven beta polynomials agree exactly with both
saved input certificates. The directly reconstructed qA, J_6(qA),
qJ_6(A), R_6 and T_6 agree in every component, including killed upper
modes. Independently, J_6(qA)/S-T_6/S is the zero polynomial in all
eleven rows. Thus agreement is not inferred from three selected rows.

On paper the cancellation in rows k=2,3,4 leaves exactly the displayed
two-term c_k formula. Substitution of the weights gives respectively
the factors (-4/3,35), (-32/3,275/6), (-80/3,12155/324), confirming
the signs and all retained upper u indices. The independent expansion
matches each displayed polynomial in full.

The audit regenerates every arctangent term, both positive remainder
bounds and both Machin endpoints, then the unchanged outward 10^(-60)
pi interval. Integer squared endpoints independently certify the same
sqrt(2) interval. The branch justification is the one proved in C029n;
no numerical pi or square-root decimal is an input. Independently
implemented interval products and Horner evaluation reproduce exactly
both unrounded rational endpoints of each original bulk enclosure.
They lie within, and outward-round to, the three displayed intervals.
In particular the respective upper endpoints are

    -22.184393875255, -6.599923769987, -2.675150248312,

each a strictly negative exact rational. This verifies the nonzero
bulk modes and the span exclusion under S>0 and basis independence.
No mathematical correction was needed. This is verification of the
existing finite obstruction, not a newly discovered obstruction or
an estimate of C029m's eventual Hermite index. The analytic and uniform
gaps, and the Mathlib qualification below, remain unchanged.

## Mathlib

Full matching coverage for this actual-coefficient commutator and its
finite certificate has not been checked. No presence or absence claim
is made. The basis and coefficient identities are imported by precise
source citation; the arithmetic above is an ordinary finite specialization.
