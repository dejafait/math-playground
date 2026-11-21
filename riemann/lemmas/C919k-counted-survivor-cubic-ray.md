# Corollary 919k: counted surviving-band cubic ray

## Hypotheses

Use the actual Xi of L018, the opposite-class multiset alpha_j of
L024 with every zero order retained, beta_j=alpha_j^(-2), and L030's
absolutely convergent algebraic form

    Q(q)=sum_j beta_j^2 q(beta_j)^2.

Use C919f at time zero, retaining its explicit CPython integer/Fraction
and Decimal/libmpdec arithmetic assumptions, including correctly rounded
HALF_EVEN exp. L058 identifies its F(0,z) with Xi(z). Select any one
actual real zero x_i in each of the three open boxes

    (14,29/2), (41/2,43/2), (49/2,51/2),
    a_i=x_i^(-2), P_3(X)=prod_(i=1)^3(X-a_i).

Import David J. Platt, *Isolating some non-trivial zeros of zeta*,
Mathematics of Computation86(307) (2017),2449-2467,
DOI10.1090/mcom/3198, Theorem5.1, accepted manuscript printed p8
(PDF p9), with Sections4.1-4.2/5, pp6-8:
https://research-information.bris.ac.uk/ws/portalfiles/portal/78836669/platt_zeta_submitted.pdf.
It gives critical-line location and simplicity of all nontrivial zeros
with |Im rho|<=30610046000. Only complete reality through1000 and
its zero-ordinate implication are used; simplicity is unnecessary.
The source computation is imported, not replayed.

Import Bellotti-Wong, *Improved estimates for the argument and
zero-counting function of the Riemann zeta-function*, arXiv:2412.15470v2
(7July2025), Theorem1.1 p1 and Section5 pp23-24:
https://arxiv.org/pdf/2412.15470v2.
For the inclusive, multiplicity-counted N(T)=#{rho:0<Im rho<=T},

    |N(T)-F(T)|<=E(T), T>=e,
    F(T)=T log(T/(2pi e))/(2pi),
    E(T)=0.10076 log T+0.24460 log log T+8.08344.

Retain L467's audited inclusive-endpoint interpretation and complete
closed-unit-shell bound18 log(n+2), under that source input. Neither
the source computations nor the whole manuscripts are independently
audited here. CPython integer/Fraction arithmetic is also assumed for
the exact certificate below. No RH, ordered first-three census,
uniqueness in a box, global simplicity or exterior reality is assumed.

## Conclusion

For every such selection and every integer r>=4,

    Q(X^r P_3)>0.

More precisely, set ell=(14,41/2,49/2), u=(29/2,43/2,51/2), and

    g=prod_i(u_i^(-2)-100^(-2)),
    A=prod_i(ell_i^(-2)+1000^(-2)),
    h4=200^(-20)*g^2,
    t4=18*A^2*(1000^(-19)+1000^(-18)/18).

Then g>0, h4>t4>0, N(200)-N(100)>=14, and for k=r-4>=0,

    Q(X^(4+k) P_3)
       >=200^(-4k)*(h4-t4*(1/625)^k)
       >=200^(-4k)*(h4-t4)>0.                         (1)

This is a known-method specialization with a new local finite estimate,
classified REPRODUCTION, not progress beyond the checked general source
methods. The separate step2219 conceptual audit accepts it under the
stated source and arithmetic assumptions. It controls only this
cubic times monomials, at time zero. Arbitrary degree, shift removal
and L030/L032/C032a all-degree positivity remain unresolved. It is not
a complete RH candidate.

## Proof

### Representatives and complete real head

L018 sends rho=sigma+i gamma to alpha=gamma+i(1/2-sigma), preserving
orders. A zero with gamma=0 would, by the symmetric Platt theorem,
have sigma=1/2, hence alpha=0, excluded by L024. Thus every opposite
class has a unique representative Re(alpha)>0. Choose these, retaining
orders. They correspond exactly to all positive-ordinate zeta zeros.
If a nonreal positive-real-part Xi zero has its conjugate as another
zero, both are separate representatives and both are counted. They
are not an opposite pair and are never merged. This also explains why
no extra factor two is inserted in the count or Q.

Let the head consist of every occurrence with 0<gamma<=1000, including
an endpoint at1000. Platt's theorem applies since1000<30610046000,
and makes every head alpha positive real. The head is finite by L467
(or compact-strip finiteness for nonzero entire Xi). Every head term
beta^(2r+2) P_3(beta)^2 is therefore nonnegative. C919f and L058
give the selected x_i in the indicated distinct classes. Their terms
vanish, even if there were repeated occurrences; no contribution from
another head occurrence is discarded as a negative error. We require
a distinct surviving class, not that these are the first three zeros.

### Inclusive count in the fixed surviving band

Apply the imported count bounds at100 and200, both greater than e:

    N(200)-N(100)>=F(200)-F(100)-E(200)-E(100).        (2)

For transparency, elementary bounds suffice; no transcendental
floating-point evaluation or zero table is used. Use3<pi<22/7,
8/3<e<3, and log2>1/2. The e bounds follow from its positive
series: the terms through1/3! sum to8/3; n!>=2^(n-1) for n>=2,
strict for n>=3, bounds the remaining sum to give e<3.
Also log2=integral_1^2 dx/x>1/2.
The exact inequalities (8/3)^6>200 and (8/3)^2>6 give
log T<6 and log log T<2 for both endpoints. Thus

    E(T)<0.10076*6+0.24460*2+8.08344
        =9.17720=22943/2500.                         (3)

Write L=log(100/(2pi)). Since100/(2pi)>100/(44/7)>9>e^2,
we have L>2, and direct subtraction yields

    F(200)-F(100)=100/(2pi)*(L+2log2-1)
        >100/pi>350/11.                             (4)

Equations(2)-(4) imply

    N(200)-N(100)>350/11-2*(22943/2500)
        =185127/13750>13.

The left side is an integer, so it is at least14. Its half-open band
is precisely(100,200], because N is inclusive at each endpoint. The
source convention is the one justified in L467; no generic-height or
nonvanishing endpoint hypothesis is added. Multiplicities are counted.
At these heights every occurrence is real by Platt. Select one such
occurrence y. It cannot coincide with any x_i, since x_i<51/2<100.
Existence, not a labeled zero or interior separation from200, is needed.

### Surviving contribution, uniform over the boxes

Put beta=y^(-2). For100<y<=200,

    200^(-2)<=beta<100^(-2),
    a_i=x_i^(-2)>=u_i^(-2)>100^(-2).

Consequently a_i-beta>=u_i^(-2)-100^(-2)>0, and
|P_3(beta)|=prod_i(a_i-beta)>=g>0. At r=4 the selected survivor
contributes beta^10 P_3(beta)^2>=200^(-20)g^2=h4. Every other
head occurrence is kept as nonnegative, so the entire head is at
least h4. Although the count guarantees14 occurrences, this lower
bound conservatively uses only one, and needs neither simplicity
nor the actual location of that occurrence inside the band.

### Complete exterior in the algebraic convention

For every remaining occurrence gamma=Re(alpha)>1000,
|alpha|>=gamma, |beta|<=gamma^(-2)<=1000^(-2), and

    |P_3(beta)|<=prod_i(|beta|+a_i)
        <=prod_i(1000^(-2)+ell_i^(-2))=A.

At r=4 its contribution in absolute value is therefore at most
A^2 gamma^(-20). Assign gamma to the half-open unit shell(n,n+1]
with integer n>=1000. Its count is bounded by the closed-shell count
18log(n+2) from L467. The closed bound includes any lower endpoint,
which only increases this upper estimate. Both positive-real-part
conjugate occurrences and every order are included. Thus the ENTIRE
exterior, including all intermediate heights and the infinite tail,
satisfies

    sum_(gamma>1000) |beta^10 P_3(beta)^2|
       <=18 A^2 sum_(n>=1000) log(n+2)n^(-20)
       <=18 A^2 sum_(n>=1000) n^(-19)
       <=18 A^2*(1000^(-19)+1000^(-18)/18)=t4.        (5)

For the middle inequality, n+2<=2n, log2<1 and log n<=n-1
give log(n+2)<=n for n>=2. For the last, x^(-19) decreases,
so n^(-19)<=integral_(n-1)^n x^(-19)dx for n>=1001.
Its integral from1000 to infinity is1000^(-18)/18; the n=1000
term is retained separately. There is no truncated or unpaid tail.

L030 ensures absolute convergence for this fixed real polynomial
and reality of Q. Alternatively, conjugating the representative
multiset pairs each nonreal term with its conjugate with the same
order; the entire head is real. Hence the exterior is real and is
bounded below by minus the absolute sum in(5). The modulus in(5)
is solely an error bound on algebraic squares, never a replacement
of Q by a Hermitian moment form. No RH assumption enters.

### Exact comparison and all integer shifts

Run from the active notebook:

    python3 scripts/h2-head/counted_survivor_cubic_2217.py

The full exact certificate is
`scripts/h2-head/counted_survivor_cubic_2217.json`. It evaluates the
fixed rational expressions above, without a parameter sweep, new
quadrature or zero computation. The two products reduce exactly to

    g=6208047042399/449397601000000000000,
    A=4004867809290017969/197767969000000000000000000.

In particular its exact quotient is

    h4/t4=
    2916034726959416459749081500163916668367385864257812500000000 /
    66889253369302664618658915819863921762380740240459701
       >10000000>1.                                 (6)

The inequality is integer cross multiplication with positive
denominators. For orientation only, h4 is approximately1.81990444e-62,
t4 approximately4.17457475e-70, their difference approximately
1.81990440e-62 and their ratio approximately43594966.00836. The
strict comparison is(6), not the rounded displays. The complete
rational count, products, shell bound, h4,t4, margin, cross product,
shift factors, all14 checks and empty failure list were inspected.
This is an arithmetic check of the specialization; the source
computations and analytic proof are separate inputs and obligations.

Let k=r-4 be any nonnegative integer. The chosen real survivor's
contribution gains beta^(2k)=y^(-4k)>=200^(-4k), so the full
nonnegative head is at least200^(-4k)h4. Each exterior absolute
value gains |alpha|^(-4k)<=1000^(-4k). Multiplying the summable
bound(5) thus bounds its entire sum at r by1000^(-4k)t4.
For each fixed k convergence is also given by L030. Therefore

    Q(X^(4+k)P_3)>=200^(-4k)h4-1000^(-4k)t4
       =200^(-4k)*(h4-t4*(200/1000)^(4k)).

Since(200/1000)^4=1/625<1, (6) gives(1) for EVERY integer k>=0.
This is no finite sampling assertion or asymptotic onset. The margin
may decrease with k; no r-independent positive lower bound is claimed.

### Scope and remaining gap

The frozen count and post-cancellation margin both pass without any
change of onset, boxes, band or cutoff. The new surviving-band input
prevents annihilation of the entire lower bound used here. C919h's
quadratic Gram margin was only method/overlap context and is not an
input to this proof. The fixed cubic ray does not cover an arbitrary
L032 interpolating witness with more roots or higher degree, and it
does not remove X^r. The older fixed-degree stops remain relevant.
The independent step2219 critical audit below accepts the representative,
count, complete-tail and all-r arguments without changing the claim.
No global RH candidate is asserted.

### Independent conceptual audit, 21 November 2026 (step2219)

The invocation-start SPECIALIZE assessment2217, separately approved2218,
covers this exact frozen audit. The entire proof and generator were read,
along with L018/L024/L030/L467, the L058 normalization, accepted C919f
hypotheses/conclusion and the scoped C919h/2146/2207 comparisons. Primary
theorem and essential proof-case coverage is reused from approval2218;
there is no new literature premise. The audit accepts (1) under the
retained imports and backend assumptions, without a mathematical repair.

**Source applicability and occurrences.** Both count endpoints100,200
are in T>=e; Platt's symmetric height range includes the complete head
through1000. The zero-ordinate case is essential: Platt would make such
a zero have sigma=1/2, whereas L024 excludes alpha=0. Thus each opposite
class has exactly one representative with positive real part, with its
full order. In an off-line quadruple the two representatives at positive
real part are conjugates, not opposites. Both occur in N and Q. The
coordinate map is injective and order-preserving, so neither an omitted
factor two nor a merged conjugate class occurs. Simplicity is unused.
C919f's open boxes select distinct positive real zeros at time zero;
its Decimal/libmpdec contract is not removed by this rational audit.

**The count and surviving head.** The exact endpoint error upper bound
is22943/2500. Expanding F(200)-F(100) gives precisely the expression
in(4), with L>2 and 2log2>1, hence the strict lower bound350/11.
Subtracting both endpoint errors gives185127/13750>13, so the inclusive
count difference is at least14. L467's one-sided-limit interpretation
includes zeros at200 and excludes those at100, even with multiplicity.
One occurrence suffices. All its reciprocal distances from the selected
three classes exceed the positive lower factors defining g. The rest of
the real head is retained as nonnegative, including additional occurrences
in the boxes or at the cutoff. No ordered census or uniqueness enters.
The summand at r=4 is beta^10 P_3(beta)^2, so its lower bound has the
ordinate exponent20, not10. The gap-product inequalities hold uniformly
over every allowed selection in all three open boxes.

**Complete exterior and all shifts.** Every gamma>1000 belongs to exactly
one half-open shell(n,n+1], n>=1000, and |alpha|>=gamma>n. Applying the
closed-shell bound may only overcount. The uniform polynomial estimate
uses a_i<=ell_i^(-2) and |beta|<=1000^(-2). Thus its full absolute sum
is at most18 A^2 sum log(n+2)n^(-20). Replacing log(n+2) by n and
integrating the decreasing x^(-19) accounts for all n>=1001, with the
n=1000 term kept separately. In particular the tail constant reduces to

    t4=A^2*1018/1000^19.

The modulus estimates only the error in the algebraic form; it does not
replace that form with a Hermitian sum. Absolute convergence and real
coefficients allow conjugate pairing; the real exterior is therefore
at least minus its complete absolute bound. For arbitrary integer k>=0,
the survivor weight gains at least200^(-4k) while every exterior absolute
weight gains at most1000^(-4k). These pointwise bounds multiply summable
majorants for each k. They prove the full integer family with ratio base
1/625, without interchanging a limit in k, sampling k, assuming a uniform
positive margin as k tends to infinity, or asserting exterior reality.

**Independent exact evidence.** Run from the active notebook:

    python3 scripts/h2-head/counted_survivor_cubic_audit_2219.py

The full report is `scripts/h2-head/counted_survivor_cubic_audit_2219.json`.
This reconstruction does not execute or import the original generator.
It builds each reciprocal gap directly with a common integer denominator,
assembles t4 via1018/1000^19, and compares every one of the25 stored
load-bearing rational fields, including all six box endpoints and the
three all-shift factors. It separately checks the frozen metadata,
integer count, cross product and all14 original Boolean claims. All62
audit checks pass; both failure lists are empty. Original generator and
certificate hashes are preserved in the report, and neither file changed.
Complete relevant comparison values and checks were inspected, not merely
a bounded preview. Decimal displays are illustrative only.

The exact integer cross product proving h4>10000000*t4 is positive;
the exact quotient in(6) is reproduced. Consequently the full exterior
budget is below the one-survivor lower bound by a factor exceeding10^7,
and the factor1/625 can only improve that comparison for larger r.
This verifies the necessary threshold h4>t4, not only positivity of h4.

The outcome is local acceptance of a known-method specialization, not
progress beyond the checked general methods. The C919h quadratic margin
is not imported after cancellation; the surviving-band input is genuinely
additional to that estimate. Full source computations, arithmetic backend
implementations and Mathlib coverage remain outside this audit. No new
mathematical dependency or parameter change is needed. The canonical
conclusion remains a single cubic times monomials at time zero; arbitrary
degree, shift removal and actual-Xi all-degree positivity remain open.

## Mathlib

Full matching coverage of this qualified actual-Xi cubic statement
has not been checked. L018/L024/L030/L058/L467 and C919f retain
their separate coverage qualifications. No Lean verification of the
source computations, backend assumptions or the rational certificate
is claimed; unknown coverage is not evidence of absence.
