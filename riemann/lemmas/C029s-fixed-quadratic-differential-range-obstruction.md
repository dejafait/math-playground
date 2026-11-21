# C029s — Full U_6 is outside the fixed-quadratic differential range

## Hypotheses

Use the exact real polynomial T_6 of C029n, with every odd and even
coefficient retained, and set S=sin(pi/8)/sqrt(2)>0 and U_6=T_6/S.
The source is Alexey Kuznetsov, *Expansion of the Riemann Xi Function
in Meixner-Pollaczek Polynomials*, Canad. Math. Bull. 51(4) (2008),
561–569, [primary source](https://doi.org/10.4153/CMB-2008-055-0),
equations (2), (4), (13), printed pp563/566 and the finite weights
pp568–569. Only its finite coefficient formulas are used. C029n
supplies these formulas explicitly, their normalization and the proved
rational pi/sqrt(2) enclosures used below.

Fix q(t)=t^2+1/4. The parameter alpha is real and nonnegative.
A candidate h has real coefficients and degree exactly five.

## Conclusion

There is no pair (alpha,h) under these hypotheses satisfying the
polynomial identity

    U_6(t)=(t^2+1/4)h'(t)+2alpha*t*h(t).

The assertion includes alpha=0 and all arbitrarily large alpha. This
is a finite obstruction to this fixed representation. It is not a
root-count result, an obstruction to a different quadratic, a failure
of an eventual-only coefficient law or a proof/disproof of RH. The
calculation and elimination were independently audited in step2032.

## Proof

### Exact coefficients and their enclosures

Write U_6(t)=sum_(j=0)^6 b_j t^j. Here is a complete prescription for
the coefficients used in the calculation, without numerical root data.
Let v_n=u_n/S and gamma_n=beta_n/S, with u_n and beta_n defined by
the finite source formulas in C029n. Replace each normalized sine
factor by 1,1+sqrt(2),-1,-1-sqrt(2) according to (n-h) modulo four.
Form

    A_k=[6!/((6-k)!6^k)] gamma_k, 0<=k<=6,
    p_0=1, p_(-1)=0,
    p_(k+1)=[t p_k-(k+1/2)p_(k-1)]/(k+1),
    b_j=sum_(k=j)^6 A_k [t^j]p_k.

All v_n (0<=n<=8), gamma_k, A_k and b_j are exact elements of
Q(sqrt(2))[pi]. In particular the normalization is by S only, not by
the leading coefficient. The basis recurrence proves that the leading
coefficient of p_k is 1/k!, and C029n proves A_6<0. Thus b_6=A_6/720<0
and U_6 really has degree six. No assumed degree or root simplicity
is needed.

For reproducibility, the unchanged C029n pi enclosure comes from its
48-term even alternating arctangent bounds at 1/5 and 1/239 and the
proved Machin identity. It is rounded outwards to width 10^(-60).
The sqrt(2) enclosure has the same width and integer-squared endpoint
checks. No precision is increased in this calculation. Represent a
polynomial in pi by its ascending pairs (a,b) for a+b sqrt(2).
Use (a,b)(c,d)=(ac+2bd,ad+bc) and exact rational sums/scaling.
For evaluation, enclose a+b sqrt(2) using the sign of b, then use
interval Horner evaluation in pi. Addition adds endpoints;
multiplication takes the minimum and maximum of the four endpoint
products. These operations enclose the exact value by induction.
Repeated parameters are retained symbolically until this final
enclosure, so no independence assumption about occurrences is made.

The resulting rational outer bounds for the full coefficients are:

| j | lower bound for b_j | upper bound for b_j |
| --- | ---: | ---: |
| 0 | 1.842192025 | 1.842192026 |
| 1 | -1.762759216 | -1.762759215 |
| 2 | 0.602116495 | 0.602116496 |
| 3 | -0.084441231 | -0.084441230 |
| 4 | 0.004543068 | 0.004543069 |
| 5 | -0.000049788 | -0.000049787 |
| 6 | -0.000001242 | -0.000001241 |

Every displayed decimal is an exact rational with denominator 10^9.
The certificate retains every exact source coefficient, basis
polynomial and b_j, as well as the complete rational interval endpoints.
The reconstruction checks every v_n, gamma_k and A_k and every weight
against C029n's unchanged certificate. No odd coefficients are zeroed.

### Necessary compatibility and the entire parameter domain

Write h(t)=sum_(k=0)^5 c_k t^k. Direct differentiation gives

    (t^2+1/4)(t^k)' + 2alpha*t*t^k
       =(k+2alpha)t^(k+1)+(k/4)t^(k-1),

where the last term is omitted for k=0. The four even coefficient
equations of the proposed identity must therefore be

    b_0=c_1/4,
    b_2=(1+2alpha)c_1+(3/4)c_3,
    b_4=(3+2alpha)c_3+(5/4)c_5,
    b_6=(5+2alpha)c_5.                         (1)

The remaining equations, retained but not needed for the contradiction,
are b_1=2alpha*c_0+c_2/2, b_3=(2+2alpha)c_2+c_4 and
b_5=(4+2alpha)c_4. Thus (1) is necessary for the full identity; the
argument does not substitute an even polynomial for U_6.

On alpha>=0 the factors 3+2alpha and 5+2alpha are at least 3 and 5.
Solve the last two equations of (1) for c_5 and c_3, and the first
for c_1=4b_0. Substitution into the second gives the necessary equation

    F(alpha)=(b_2-4(1+2alpha)b_0)(3+2alpha)(5+2alpha)
              -(3/4)b_4(5+2alpha)+(15/16)b_6=0.       (2)

Only the positive factors just checked and the constant 4 were used
as divisors; in particular no division by alpha occurs. Expanding
symbolically, F(alpha)=f_0+f_1 alpha+f_2 alpha^2+f_3 alpha^3, where

    f_0=15b_2-60b_0-(15/4)b_4+(15/16)b_6,
    f_1=16b_2-184b_0-(3/2)b_4,
    f_2=4b_2-144b_0,
    f_3=-32b_0.

The same exact arithmetic and unchanged enclosures give:

| j | lower bound for f_j | upper bound for f_j |
| --- | ---: | ---: |
| 0 | -101.516811776 | -101.516811775 |
| 1 | -329.336283397 | -329.336283396 |
| 2 | -262.867185716 | -262.867185715 |
| 3 | -58.950144823 | -58.950144822 |

All four upper bounds are strictly negative. Consequently, for every
alpha>=0, the constant term is negative and all other terms in F
are nonpositive, so F(alpha)<0. This contradicts (2). It covers
alpha=0 and the whole unbounded tail without parameter sampling,
a root-count algorithm for pi-dependent polynomials or a limiting
interchange. No hyperbolicity condition on h is needed for this
contradiction.

### Verification, source comparison and limits

Reproduce the exact calculation from this notebook with

    python3 scripts/pollaczek/quadratic_differential_range_2030.py

The full certificate is
`scripts/pollaczek/quadratic-differential-range-2030.json`.
All 30 checks pass, with no failures. They include pinned source and
helper hashes, the unchanged input widths, all finite source
coefficients and weights, degree and parity, the operator coefficient
equations, the independent convolution/expanded cubic identity and
containment of every printed outer enclosure. Complete load-bearing
f_j polynomials and rational interval endpoints were inspected, along
with all outer bounds and check results. The script verifies the
finite arithmetic; the necessary-condition argument (1)–(2) above
supplies the logical contradiction. This is not formal verification.

The relevant general forward theorem is already known: Andre Bunton,
Nicole Jacobs, Samantha Jenkins, Charles McKenry Jr., Andrzej
Piotrowski and Louis Scott, *Non-Real Zero Decreasing Operators Related
to Orthogonal Polynomials*, Involve 8 (2015), 129–146,
[arXiv:1312.2283v2](https://arxiv.org/pdf/1312.2283v2), 22 December
2013, Theorem 8 and proof, manuscript pp3–4. It controls nonreal zeros
of qp'+alpha q'p for alpha>=0. It is motivation only here: no zero
bound from that theorem is applied, and it does not assert inverse
range membership. The calculation specializes the inverse-range
condition for the exact U_6; no general theorem is reproved and no
novelty beyond the checked assessment is claimed.

This stops only the fixed q, N=6, quintic baseline. C029m's eventual
index premise, degree/singular cases across the family, initialization,
preimage hyperbolicity for other possible representations, and the
qualified weighted-limit/upstream[9] bridge remain unpaid. C029p's
finite root count and C029q/r's other obstructions are contrasts,
not premises of this proof.

### Independent audit2032

The approved assessment2030 reuses the source extraction for C029n;
no theorem hypothesis, quadratic, degree or precision was changed.
The original range calculation replays with all 30 checks passing.
A separate implementation, importing none of its mathematical helpers,
uses sparse monomials pi^i sqrt(2)^j alpha^k with sqrt(2)^2=2.
It reconstructs every normalized u_0,...,u_8, beta_0,...,beta_6,
finite factorial weight and A_k from the source formulas, retaining
every odd phase. It reconstructs p_0,...,p_6 and all seven b_j.
Complete exact coefficient and endpoint comparisons, rather than
displayed decimal agreement, verify these data against C029n and
the range certificate. No leading-coefficient rescaling is introduced.

The input enclosure replay checks all 48 arctangent terms, sums and
positive remainder bounds at both arguments, both Machin endpoints,
their outward enclosure, the positive squared sqrt(2) bounds, and
the unchanged interval widths 10^(-60). C029n's analytic branch proof
was checked as well: 4theta-phi is positive and less than 4/5,
whereas pi/2>1 follows from arctan(1)>1/2. Its tangent is 1, so
the angle is pi/4. This justifies using the rational Machin enclosure;
an arithmetic tangent-identity check alone would not do so.

Independently differentiating t^k gives the stated operator action.
Reading every row gives exactly the four even and three odd equations
above, with no omitted t^6 or constant equation. Every entry of the
full 7-by-6 operator matrix is checked in the separate replay, including
zeros. In addition, put l_j=j+2alpha and write M for that matrix.
The polynomial row

    R=(-4 l_1 l_3 l_5, 0, l_3 l_5, 0, -(3/4)l_5, 0, 15/16)

annihilates every column of M. For c_1 its two contributions cancel;
for c_3 they are (3/4)l_3 l_5 and its negative; for c_5 they are
-(15/16)l_5 and its negative. Columns c_0,c_2,c_4 have only odd
rows, whose R entries are zero. Thus R*b=F(alpha) must vanish
for any proposed full preimage. The replay checks all six zero
polynomials, and checks that the four coefficients of R*b agree
exactly with the expanded formulas and original certificate.

Backward elimination in (1) divides only by 5+2alpha>=5 and
3+2alpha>=3 (and nonzero numerical constants); c_1=4b_0 uses
no parameter divisor. The row argument also verifies the necessary
condition without parameter division. There is no exceptional case
at alpha=0. Each exact f_j endpoint was independently reconstructed
and compared in full; all four printed outer bounds above contain
those complete intervals and have negative upper endpoints. At
alpha=0, F=f_0<0; for alpha>0 all four summands are negative.
This proves exclusion on the entire unbounded domain without a
root count or an asymptotic approximation. No root simplicity or
hyperbolicity of h is assumed.

Reproduce the independent replay with

    python3 scripts/pollaczek/quadratic_differential_range_audit_2032.py

The full certificate is
`scripts/pollaczek/quadratic-differential-range-audit-2032.json`.
All 108 checks pass, with no failures. It stores input hashes,
complete reconstructed b_j and f_j, rational endpoints, operator
matrix, eliminating row and six zero residuals. The complete f_j
polynomials and intervals were also inspected directly. This is an
independent arithmetic and paper audit, not formal verification.

No mathematical correction was needed. This validates the existing
finite stop, with no newly discovered general theorem or advance on
the eventual index bound. C029n is the only local mathematical input;
the forward zero-count theorem remains motivation, not a premise.
The fixed baseline stays parked. Reopening needs materially new
actual-family structure; initialization, eventual uniformity and the
qualified analytic bridge remain independent unresolved assumptions.

## Mathlib

Full matching range obstruction and its exact coefficient/enclosure
calculation not checked in Mathlib. Supporting polynomial and interval
coverage also not checked; no absence or formalization claim is made.
