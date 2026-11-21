# Lemma 820: two unit gaps and a third positive gap have bounded degree

## Hypotheses

Use L791's actual shift-zero ratios q_k=R_(k+1)^2/(R_k R_(k+2)),
k=0,1,2, with gamma(j)=8*4^j*j!*a_j and R_j=gamma(j)/gamma(0).
Retain its L018/L021/L776/L778 completion, normalization, analytic-error,
data, evaluator and software contracts. The input is its audited closed
enclosure product, not decimal midpoint data:

    q_0 in [1.07484394250019421126346157158,1.07484394250019421126346157162],
    q_1 in [1.06274366627144916855311401273,1.06274366627144916855311401285],
    q_2 in [1.05430333113463476927545484495,1.05430333113463476927545484516].

Let d>=2 be an integer, and let A_i,B_i>0, i=1,2,3, satisfy exactly

    q_k=product_(i=1)^3 (A_i+k)(B_i+k+1)/[(A_i+k+1)(B_i+k)],
    k=0,1,2,
    A_1-B_1=A_2-B_2=1,
    A_3-B_3>d-2.

All six parameters may depend on d. No fixed L791 solution box or fixed
third denominator is imposed.

## Conclusion

Necessarily A_3<999999 and d<=1000000. Thus this precise three-factor
regime cannot match the exact central quotient data in unbounded degrees.
The certificate excludes the entire displayed q enclosure product,
including the correlated actual triple and all relevant escaping limits.

This is a conditional computer-assisted algebraic obstruction, not a
feasibility theorem in the surviving degrees, an optimal cap, or an RH
sign result. The finite obstruction passed the independent step609 audit
below, subject to the inherited input and software contracts. Its
exact-integer arithmetic uses the ordinary Python runtime as a
software contract; no formal verification or backend attestation is
claimed. Normalization of a generalized model, root simplicity,
separation, signed compensation and actual mixed positivity remain open.

## Proof

**Literature scope and specialization.** The pre-invocation SPECIALIZE
assessment is
`drafts/literature/2026-11-05-three-factor-unit-gap-feasibility.md`.
A. Martinez-Finkelshtein, R. Morales and D. Perales, *Real roots of
hypergeometric polynomials via finite free convolution*,
[arXiv:2309.10970v3](https://arxiv.org/pdf/2309.10970v3), 2 May 2024,
printed pp.15–16, Theorem3.1, p.23, Table2 row2, and pp.11–12,
Proposition2.7(iii), supply concatenation and sufficient root-preserving
building blocks with positive integer gaps or gaps >d-2. Jonathan
Holland, [arXiv:2608.08682v1](https://arxiv.org/html/2608.08682v1),
9 August 2026, (66)–(71), Lemma6.2, supplies a conditional two-factor
quotient-matching argument. These cited facts motivate the assessed
regime; they are not used as premises of the obstruction. No source
root theorem, multiplicity assertion or matching induction is reproved.
The local difference is exact compatibility with the particular central
data, which the inspected source statements do not decide. The bounded
source search does not establish originality of this obstruction.

**Compactification and all escaping cases.** Suppose, for contradiction,
that A_3>=999999. Set

    x=1/(B_1+1), y=1/(B_2+1), b=1/(B_3+1), t=1/(A_3+1),
    Q=q_0, R=q_1, Z=q_2, epsilon=1/1000000.

Then 0<x,y,b<1 and 0<t<=epsilon. Unit gaps give the exact factors

    u_x(k)=(1+kx)^2/[(1+(k-1)x)(1+(k+1)x)]

and similarly for y. The third factor is

    (1+(k-1)t)(1+kb)/[(1+kt)(1+(k-1)b)].

Put D=(1-x^2)(1-y^2), W=QD and V=1-t. The k=0 equation is

    Q=V/[D(1-b)], hence b=(W-V)/W.                 (1)

In particular W>0 and W-V>=0. Also Q>=V/(1-x^2) and Q>=V/(1-y^2).
Writing Q_+ for the supplied upper endpoint, the exact rational check

    Q_+*(1-(27/100)^2)<1-epsilon                   (2)

therefore forces x,y<27/100. By symmetry assume x<=y. Consequently it
suffices to exclude solutions in the closed domain

    0<=x<=y<=27/100, 0<=t<=epsilon,

with Q,R,Z in the supplied closed intervals, subject to W-V>=0 and the
two cleared equations below. This enlarged domain includes x=0 or y=0
(an infinite unit-gap denominator), b=0 (an infinite third denominator),
and t=0 (an infinite third numerator). A unit-gap denominator tending to
zero contradicts (2). A third denominator tending to zero would force
b to 1, whereas (1) gives b<=1-(1-epsilon)/Q_+<1. No positive lower
bound on x,y,b or t is assumed.
The elimination of b is valid for every original tuple since W>0.
There is no need to solve the boundary equations or infer an exact
solution from a limiting residual.

**Cleared exact equations.** At k=1 and k=2 respectively the equations
are, before eliminating b,

    R=(1+x)^2(1+y)^2(1+b)/[(1+2x)(1+2y)(1+t)],
    Z=(1+2x)^2(1+2y)^2(1+t)(1+2b)
      /[(1+x)(1+3x)(1+y)(1+3y)(1+2t)(1+b)].

All original denominators are positive. Substituting (1) and multiplying
by positive W gives the necessary polynomial identities

    F1=(1+x)^2(1+y)^2(2W-V)
       -R(1+2x)(1+2y)(1+t)W=0,
    F2=(1+2x)^2(1+2y)^2(1+t)(3W-2V)
       -Z(1+x)(1+3x)(1+y)(1+3y)(1+2t)(2W-V)=0.    (3)

Only necessity is used: any additional extraneous solutions introduced
by clearing denominators would enlarge the tested set, not invalidate
an exclusion. In particular no denominator is divided out during the
interval exclusion.

**Full rational interval exclusion.** Reproduce from this notebook with

    python3 scripts/central-jacobi/three_factor_606.py

The complete certificate is
`scripts/central-jacobi/three-factor-certificate-606.json`. The program
transcribes the full q endpoints, checks (2) using exact Fraction
arithmetic, and builds precisely (3) by bivariate polynomial addition
and multiplication. Coefficients are intervals enclosing their values
for every fixed Q,R,Z,t in their complete input intervals. They may be
correlated; treating coefficient intervals independently enlarges the
enclosure. The stored `polynomial_coefficients` retain every monomial.

Every interval endpoint in the polynomial calculation is an integer
multiple of 10^(-60). Initialization takes exact rational floor/ceiling.
Addition and negation are exact on this grid. For multiplication take
the minimum and maximum of the four integer endpoint products, divide
by 10^60, and round outward with integer floor and ceiling. Thus each
operation encloses its mathematical interval, without a floating-point
premise, unstated error estimate, or division by a variable interval.

On each closed rectangle X times Y, each F in (3) is bounded by the
centered interval expression

    F(c_x,c_y)+Ix*(X-c_x)+Iy*(Y-c_y),             (4)

where Ix and Iy enclose partial_x F and partial_y F throughout X times Y.

Here c_x,c_y are actual grid points inside the rectangle, and all three
polynomials are evaluated by outward bivariate Horner arithmetic.
Differentiation is coefficientwise before evaluation. For every fixed
parameter tuple the ordinary mean-value formula on the segment from
the center to a point of the rectangle proves (4); the coefficient
intervals enclose every such fixed tuple. Correlation loss can weaken
this enclosure but cannot produce a false strict sign.

Start with [0,27/100]^2. A rectangle is excluded only if its entire
x interval lies strictly above its y interval, if interval evaluation
gives W-V<0 throughout, or if (4) for F1 or F2 excludes zero. Otherwise
bisect a longest coordinate interval at its integer midpoint. The two
closed children cover their parent, including their shared boundary.
Depth and node caps would retain every unresolved rectangle in the
certificate and report INCONCLUSIVE; no unresolved rectangle is silently
discarded. Every terminal rectangle is recorded by its full binary
path and its exclusion reason; nonsymmetry leaves retain the entire
strict interval bound. Paths and the specified deterministic splitting
rule recover every rectangle, so the certificate is a full finite cover,
not a sample, scan, or summary of favorable boxes.

The execution returned PASS: 727 visited nodes, maximum depth20,
364 leaves (15 symmetry, 2 negative-b, 226 F1, 121 F2), and zero
unresolved rectangles. Leaf paths are prefix-free and their exact Kraft
sum is 1. In this finite binary subdivision those facts independently
check complete combinatorial coverage. A complete consistency pass
inspected every stored nonsymmetry bound for a strict sign and both
negative-b bounds for the required negative sign; it also checked all
paths and the exact sum. Evidence is
`scripts/central-jacobi/three-factor-consistency-606.json`. This is a
certificate consistency check, not an independent replay of the interval
evaluations or an audit of the inherited actual coefficient evaluator.
The generating program, its hash, full input endpoints and L791 file
hash are retained in the main certificate. No failed leaf or stopping
limit occurred in this run. That generating/consistency evidence alone was not an independent audit.
The separate step609 audit below verifies the finite obstruction while
retaining the stated mathematical input and software contracts.

Thus (1) and (3) cannot hold for A_3>=999999, proving A_3<999999.
Since B_3>0, the stipulated degree gap satisfies

    d-2<A_3-B_3<A_3<999999.

Hence d<1000001 and integer d<=1000000. This is an obstruction to this
specific unbounded-degree family only. It says nothing about models
with more factors, different gaps or different sufficient root regimes,
and supplies no off-line zero or actual mixed sign.

### Independent proof and certificate audit — 5 November 2026, step609

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-11-05-three-factor-cap-audit.md`; this is a
REPRODUCTION audit of this exact statement, not a new source theorem,
stronger cap, matching construction or actual sign result. Run

    python3 scripts/central-jacobi/audit_609.py

The full new report is
`scripts/central-jacobi/three-factor-audit-609.json`. Neither step606
program was imported or rerun; every original artifact is preserved.
The report records source/program hashes, the complete input endpoints,
every coefficient polynomial and extremum, all recovered rectangles,
center values, derivative intervals, strict exclusions and all failures.

**Compactification and algebra.** For original positive parameters,
0<x,y,b<1 and 0<t<=10^(-6). The k=0 equation gives
Q=V/[D(1-b)] and W=QD=V/(1-b)>0. Since each remaining denominator
factor is at most1, Q>=V/(1-x^2) and Q>=V/(1-y^2).
The independently recomputed exact margin in (2) is

    1-10^(-6)-Q_+*(1-(27/100)^2) > .0035111809080699 > 0.

Thus x,y<27/100 strictly, including at t=10^(-6). Swapping the two
unit factors permits x<=y. On the entire enlarged square, D>0 and
Q>0, so W>0 also holds there. Equation (1) is a legitimate elimination
for every original tuple. Its relaxed condition W-V>=0 retains b=0;
it excludes only negative b. Moreover
b<=1-(1-10^(-6))/Q_+<1 excludes B3 tending to zero.
B1 or B2 tending to zero contradicts x,y<27/100. All other infinite
positive-parameter limits are represented by x=0, y=0, b=0 or t=0.
No lower bound away from those boundaries is used. In particular,
omitting the original extra relation between b and t only enlarges
the excluded set.

At k=1 the unit factors are (1+x)^2/(1+2x) and its y counterpart;
at k=2 they are (1+2x)^2/[(1+x)(1+3x)] and its y counterpart.
The third factors are (1+b)/(1+t) and
(1+t)(1+2b)/[(1+2t)(1+b)], respectively. Substitution gives
1+b=(2W-V)/W and 1+2b=(3W-2V)/W. Clearing the original positive
denominators yields exactly (3). The audit expands their direct
numerators and independently regrouped forms in the exact polynomial
ring Q[x,y,Q,R,Z,t] and checks equality of every coefficient.
Only necessary equations are used, so no reverse implication at an
added boundary is needed.

**Independent coefficient enclosures.** The audit does not trust the
stored polynomial intervals. For each x^i y^j it reconstructs its
exact polynomial in Q,R,Z,t. Each is multi-affine in Q,R,Z and of
degree at most2 in t, as checked for every monomial. For fixed t,
iterated linear interpolation expresses its value as a convex
combination of the eight Q,R,Z vertex values. At each vertex the
remaining quadratic on [0,10^(-6)] attains its extrema at the two
endpoints or its stationary point when that point lies inside.
The audit evaluates every such candidate with exact rational arithmetic.
It verifies that every stored coefficient interval contains the
resulting exact range, including identically zero coefficients given
wider stored bounds. It checks for missing monomials and compares all
six q endpoints with both canonical statements. L791's file and the
original generator match their saved hashes. This verifies use of
L791's enclosure; it does not reattest its inherited evaluator.

**Independent leaf arithmetic.** The audit uses Fraction endpoints
with no finite-grid rounding, not the generator's interval class.
For the now verified stored coefficient intervals it independently
forms both partial derivatives and evaluates the centered expression
(4) by exact nested univariate Horner arithmetic. The same elementary
interval rules apply: addition adds endpoints, negation exchanges
negated endpoints, multiplication takes the minimum/maximum of all
four endpoint products. Exact arithmetic needs no rounding allowance.
Every recorded leaf bound contains its recomputed rational bound;
all strict signs pass. For comparison, the generator's initialization
and multiplication floor/ceiling rules round outwards even for
negative integers, and its grid addition/negation are exact. No
floating-point or interval-division premise enters either calculation.

For each fixed admissible parameter tuple, polynomial differentiability
and the integrated mean-value formula along a segment inside the
rectangle justify (4). All derivative values on that segment are
inside the computed partial-derivative intervals. The chosen integer-grid
center lies in the rectangle. Parameter and coefficient correlations
may widen these ranges; no correlation assumption is used for a sign.
The b-negative leaves use the necessary inequality W-V>=0, and the
symmetry leaves require strictly x_low>y_high. Equality boundaries
are never removed by symmetry.

Every full binary path is replayed from [0,27/100]^2 using integer
coordinates on the original 10^(-60) grid, the stated longest-side rule,
x tie-breaking and floor midpoint. Both children are closed and their
union equals their parent. All paths are distinct and prefix-free;
the recovered tree has both children at every internal node. It has
727 nodes, 363 internal nodes, 364 leaves and maximum depth20. The
exact Kraft sum is1; there is no unresolved path. All 15 symmetry,
2 negative-b, 226 F1 and 121 F2 leaves pass. The following conservative
lower bounds on the minimum strict exclusion margins all exceed the
required threshold0:

    symmetry: .0010546875;
    negative b numerator: .0033074549872084;
    F1: .0000000737559817;
    F2: .0000022568253942.

The certificate stores the complete exact rational values, not these
rounded-down displays. The run reports PASS, 1561 checks, zero failures.
Thus the cover excludes the closed compactified domain, including all
escaping cases, for every q triple in the input product. Finally
A3>=999999 is exactly t<=10^(-6) for positive A3, and
d-2<A3-B3<A3<999999 gives d<1000001, hence integer d<=1000000.
The strict endpoints and B3>0 have both been retained.

This establishes the conditional finite obstruction and makes the
precise unbounded-degree regime a retained stop. It does not import
any root-preservation or matching assertion from the motivating papers,
verify any transcendental evaluator or binary, assert feasibility below
the cap, or settle any independent actual-Xi sign or realization gap.

## Mathlib

Full matching-result and certificate-verification coverage is unchecked.
Supporting input is the ordinary multivariable mean-value formula for
polynomials on a convex rectangle, with exact rational interval
arithmetic justified above. No absence claim, formal verification or
general root-preserver input is asserted.
