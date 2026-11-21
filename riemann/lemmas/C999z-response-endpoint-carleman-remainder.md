# C999z: Exact two-parity endpoint split with an effective compact remainder

## Hypotheses

Set a=log(3)/4, c_j=2j+1/2 for every integer j>=0, and epsilon in
{+1,-1}. Work on the complex Hilbert space L2((0,a),dt), with Lebesgue
measure and inner product linear in its first slot. Import C744v
Section3's complete single-cell response, with its unitary half-interval
normalization and its bounded extension. In its original y coordinate,

    r_j^epsilon(y)=exp(-c_j a)
        [exp(c_j y)+epsilon exp(-c_j y)]
        /sqrt(1-epsilon exp(-2c_j a)),       0<y<a.       (1)

In particular every j>=0 is included. This is the analytic identity
imported from Hongmin Li, *Cutoff-free positivity of localized Weil
forms through the (log 11)/2 threshold*, displayed v2, 9 November 2026,
[paper45, Lemma3.1, (2.1)-(3.4)](https://rstation.ai/problems/riemann_hypothesis/papers/45).
C744v's bounded-extension argument follows bramble_trace, displayed v1,
26 October 2026, [paper60, Section2, (2.4)-(2.7)](https://rstation.ai/problems/riemann_hypothesis/papers/60).
Neither source's numerical positivity certificate is used. The analytic
input and its possible later use for Xi keep their existing qualifications;
all assertions below also hold directly for the functions (1).

Let Wv(t)=v(a-t), a unitary reflection. Write S_epsilon for the response
operator in this t coordinate, thus

    <S_epsilon v,v>=sum_(j>=0)|<v,W r_j^epsilon>|^2.     (2)

Here S_epsilon denotes one parity block, rather than the entire two-block
operator on the original cell. Define the truncated Carleman operator

    (Cv)(t)=integral_0^a v(s)/(t+s) ds.

Its bounded extension has norm at most pi, by the weighted Schur estimate
already used in C744v Section3. No assertion of compactness for C is made.

## Conclusion

There is a real continuous symmetric kernel R_epsilon on [0,a]^2 such that

    S_epsilon=(1/2)C+R_epsilon,                         (3)

where the kernel and its integral operator use the same symbol. It is
Hilbert-Schmidt and compact. The coefficient 1/2 is exact in BOTH parities
under (1)'s normalization. For integers m>=1 and J>=0 there are explicit
selfadjoint finite-rank approximants R_epsilon;m,J of rank at most m+2J,
with

    ||R_epsilon-R_epsilon;m,J||_(L2 -> L2)
      <= ||R_epsilon-R_epsilon;m,J||_HS
      <= eta_m,J
       :=303 a^2/(16m)
         +4a exp[-a(2J+1/2)]/[(1-exp(-a))(1-exp(-2a))]. (4)

Thus eta_m,J tends to zero as m,J tend to infinity. The singular part
in (3) stays exact. Every correction term, including j=0, is retained in
the identity and in the error allowance for any omitted indices.

This is a local REPRODUCTION/specialization under review642/comparison643,
not a new general compactness theorem. It establishes raw L2 operator
control. It proves no remainder sign, lower-reference coercivity,
energy-normalized compactness or approximation rate, actual middle-inverse
comparison, S3 positivity, or RH. It does not validate any original
IEEE754/Decimal, source-to-Xi, whole-core or c_* contract. Separate critical
audit646 below upholds this derivation within these qualifications; this
is no complete RH candidate.

## Proof

### 1. Exact product split, with all four products

For t in [0,a] set

    phi_j(t)=exp(-c_j t),
    psi_j(t)=exp[-c_j(2a-t)],
    b_j=exp(-2ac_j),       d=1-exp(-a)>0.

Then W r_j^epsilon=(phi_j+epsilon psi_j)/sqrt(1-epsilon b_j).
All denominators are positive and at least d, because
0<b_j<=exp(-a)<1. Expanding the product gives exactly

    (W r_j^epsilon)(t)(W r_j^epsilon)(s)
      =phi_j(t)phi_j(s)+E_epsilon,j(t,s),              (5)

    E_epsilon,j(t,s)=
      [epsilon b_j phi_j(t)phi_j(s)+psi_j(t)psi_j(s)
       +epsilon phi_j(t)psi_j(s)
       +epsilon psi_j(t)phi_j(s)]/(1-epsilon b_j).

Thus the denominator correction to the first product is present, as are
the reflected product and BOTH cross products. This is an algebraic
identity for each j, including j=0, before any limit or integral.

On the entire closed square, |phi_j|<=1 and |psi_j|<=exp(-ac_j)=sqrt(b_j).
Consequently

    |E_epsilon,j(t,s)|
      <=(2b_j+2sqrt(b_j))/d<=4exp(-ac_j)/d,

    sup_(t,s in [0,a]) |sum_(j>=J)E_epsilon,j(t,s)|
      <=4exp[-a(2J+1/2)]/[d(1-exp(-2a))]=:B_J.         (6)

The series converges absolutely uniformly on the CLOSED square. Its sum
is therefore continuous, real and symmetric. This bound treats the even
and odd denominators separately through their common positive lower bound;
it does not replace their distinct exact values in (5).

For u=t+s>0 the remaining geometric sum is exactly

    sum_(j>=0)phi_j(t)phi_j(s)
      =sum_(j>=0)exp[-(2j+1/2)u]
      =F(u):=exp(-u/2)/(1-exp(-2u)).                   (7)

Define h(u)=F(u)-1/(2u) for u>0. The desired remainder is

    R_epsilon(t,s)=h(t+s)+sum_(j>=0)E_epsilon,j(t,s).   (8)

It remains to extend h at zero, control it effectively, and justify the
operator statement. No term of (7) or (8) has been dropped by neutrality.

### 2. Removable corner and an explicit derivative bound

For 0<=u<=2a put

    p(u)=exp(-u/2),
    q(u)=integral_0^1 exp(-2uv)dv,
    B(u)=p(u)/q(u).

The integral defines a smooth strictly positive q, also at zero. For
u>0, q(u)=(1-exp(-2u))/(2u), so F(u)=B(u)/(2u). Since
B(0)=1, the fundamental theorem of calculus yields the smooth extension

    h(u)=(1/2)integral_0^1 B'(theta u)dtheta,
    h'(u)=(1/2)integral_0^1 theta B''(theta u)dtheta.   (9)

Both formulas include u=0. Here p'(0)=-1/2, q'(0)=-1, hence
B'(0)=1/2 and h(0)=1/4. This proves that the coefficient in (3)
is precisely 1/2; a nonsharp upper majorant is not used to identify it.

On this interval, differentiation under q's finite integral gives

    q>=exp(-4a)=1/3,       |q'|<=integral_0^1 2v dv=1,
    |q''|<=integral_0^1 4v^2 dv=4/3,
    |p|<=1,               |p'|<=1/2,       |p''|<=1/4.

The quotient rule, with every term retained, gives

    B''=p''/q-2p'q'/q^2-p q''/q^2+2p(q')^2/q^3,
    |B''|<=(1/4)*3+9+12+54=303/4.

It follows from (9) that, throughout [0,2a],

    |h'|<=303/16=:H,
    |h(u)|<=1/4+2aH.                                  (10)

In particular (8) extends continuously at (0,0). All other boundary
points are controlled by the same estimates, not just by an interior
limit. At t=a the odd response itself is zero since phi_j(a)=psi_j(a);
the exact cancellation remains in (5). Formula (8) therefore respects
that boundary cancellation. No additional singularity occurs on that
edge, at a mixed corner, or at (a,a). Endpoints have measure zero for the
operator, but the remainder bounds hold there as stated.

### 3. Equality of bounded operators on complex L2

For clarity, C's weighted Schur integral is, for 0<t<a,

    integral_0^a s^(-1/2)/(t+s)ds
      =(2/sqrt(t)) arctan(sqrt(a/t))<=pi t^(-1/2).

The symmetric column estimate is identical; the bounded weighted Schur
test gives ||C||<=pi. This is the existing C744v estimate, specialized
without changing the measure or inserting another normalization factor.
By (6) and (10), R_epsilon has bounded kernel, with

    sup|R_epsilon|<=1/4+2aH+B_0.                       (11)

It is square-integrable on the finite product space, so its integral
operator is bounded. The bound ||K||_op<=||K||_L2(kernel) and compactness
for a square-integrable kernel are imported from Gerald Teschl,
*Mathematical Methods in Quantum Mechanics*, Graduate Studies in
Mathematics 99 (AMS, 2009), Section6.3, printed pp139-141, (6.8)-(6.12)
and Lemma6.9 with proof, in the [author-hosted edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf).
Their hypotheses hold for (8) by (11); no new Hilbert-Schmidt theory is
being reproved. An explicit approximation rate is supplied below.

On f,g in C_c^infinity(0,a), their t and s supports stay a positive
distance from zero. The series (7) then converges uniformly on the
product of those supports, and (6) converges uniformly everywhere.
The finite-prefix kernel identity (5) can therefore be integrated against
f(s)conjugate(g(t)) and passed to its limit by uniform convergence on
that compact product. The left side is the bounded response operator
of C744v, and the right side is (1/2)C+R_epsilon by (7)-(9).
All identities are sesquilinear and valid for complex tests. Both sides
are bounded on L2, so density and continuity extend their equality to
all of L2. This proves (3) and (2)'s corresponding full quadratic-form
identity without any interchange at the singular corner. In particular
j=0's full square is present; its cross-cell cancellation in other
lemmas is irrelevant here.

### 4. Explicit selfadjoint finite-rank approximants

Divide [0,a] into m intervals I_i of equal length a/m and let
xi_i=(i-1/2)a/m, for i=1,...,m. Endpoint choices between adjacent
intervals have no operator effect. Set

    h_m(t,s)=sum_(i,k=1)^m h(xi_i+xi_k)1_(I_i)(t)1_(I_k)(s),

    R_epsilon;m,J(t,s)=h_m(t,s)
                       +sum_(j=0)^(J-1)E_epsilon,j(t,s).  (12)

For J=0 the latter sum is empty and (6) pays every response correction,
including j=0. All h evaluations in (12) have strictly positive arguments;
(7) defines them using elementary exponentials. Each E_epsilon,j has
operator range contained in span{phi_j,psi_j}; h_m has range contained
in span{1_(I_i):1<=i<=m}. Thus (12) has rank at most m+2J.
Its kernel is real symmetric, hence its operator is selfadjoint.

For t in I_i and s in I_k, |t+s-xi_i-xi_k|<=a/m. By (10),

    ess sup|h(t+s)-h_m(t,s)|<=H a/m.

Together with (6), this bounds the kernel error by H a/m+B_J.
The product space has measure a^2, so its L2 error is at most

    a(H a/m+B_J)=eta_m,J.

Teschl's cited kernel norm inequality proves both bounds in (4).
The Hilbert-Schmidt norm here equals the L2 norm of this error kernel,
by Lemma6.9. No positivity of the error or remainder is required.

For an entirely explicit tolerance rule put

    C_a=4a exp(-a/2)/[(1-exp(-a))(1-exp(-2a))].

For any delta>0, the integer choices

    m>=max{1,ceil(2H a^2/delta)},
    J>=max{0,ceil(log(2C_a/delta)/(2a))}

give eta_m,J<=delta. These are computable exact-real expressions.
At the fixed a one may equivalently use exp(-a)=3^(-1/4) and
exp(-2a)=3^(-1/2); the exponential tail factor is
exp[-a(2J+1/2)]=3^(-J/2-1/8). This completes the requested effective
raw-L2 approximation, without a numerical certificate or a floating-point
assumption.

### 5. Scope for a later middle-form reference

The split preserves the entire endpoint singular operator and both parity
boundary responses. Equations (3)-(4) allow later approximations to keep
(1/2)C exact while paying only a vanishing compact-remainder error.
This differs from retaining a finite response prefix or adding two
moments to unchanged598; neither old stopped comparison is resumed.
The approximants (12) need not be positive. To use any resulting lower
reference one would still have to establish its form order and coercivity,
respect the neutral restricted inverse, retain the actual remote operator
and both induced coupling terms, and prove the desired signed comparison.
None of those conclusions follows from compactness or from (4).

### 6. Separate conceptual audit — 12 November 2026, step646

The prior SPECIALIZE assessment644/approval645 covers this exact audit.
The source statements and their inspected proof cases in review642/643
are reused: Li's arbitrary-a normalized smooth-core identity, paper60's
boundedness method as specialized in C744v Section3/audit534, and
Teschl Section6.3's square-integrable-kernel results. No source sign,
radius-two constant, numerical certificate or uninspected theorem is
imported. The audit verifies the local specialization, not those papers
or the full original core/source contracts. All of (3), (4), (8), (12)
and the tolerance rule survive; no mathematical correction is needed.

**Normalization and all products.** The map W is a complex-linear
unitary because t=a-y preserves Lebesgue measure and the interval.
C744v's earlier sqrt(2) parity identification has already been included
in (1); reflection inserts no further factor. Substitution gives phi_j
and psi_j exactly as in Section1. For epsilon=+1 the denominator squared
is 1-b_j>=d; for epsilon=-1 it is 1+b_j>=1>d. In particular
b_0=exp(-a) and both j=0 denominators remain nonzero. In the first
product, 1/(1-epsilon*b_j)-1=epsilon*b_j/(1-epsilon*b_j).
This accounts for its correction in (5); epsilon squared is one in
the psi_j*psi_j product and both cross products carry epsilon.
There is neither an extra half nor a missing j=0 square.

On [0,a], phi_j<=1 and psi_j<=exp(-a*c_j). Each numerator in
absolute value is at most 2b_j+2sqrt(b_j)<=4exp(-a*c_j).
Summing from the actual first omitted index J with ratio exp(-2a)
gives exactly B_J, including B_0 when J=0. The Weierstrass bound
holds on the closed square, so it controls the corner as well as the
interior. The separate geometric sum (7) starts at j=0 with exponent
u/2 and spacing2u; its leading pole is therefore the claimed one.

**Corner, constants and both outer boundaries.** The finite integral
for q is smooth and positive through u=0. On [0,2a], its integrand
is at least exp(-4a)=1/3. Differentiation under that finite integral
gives the stated bounds1 and4/3. The four quotient-rule terms for B''
have absolute bounds3/4,9,12,54, summing to303/4; both signs and
the factor2 in the last term are accounted for. Integrating theta
in (9) contributes1/2 in addition to its prefactor1/2, hence
H=303/16. Also B'(0)=p'(0)-q'(0)=1/2, so h(0)=1/4.
Thus (8) is continuous at (0,0), and a different pole coefficient
could not be absorbed in this continuous remainder. Equations (6)
and (10) prove (11) on the whole square.

The odd boundary cancellation can be checked exactly: at t=a,
phi_j=psi_j=exp(-a*c_j), so every odd product vanishes and
E_{-,j}(a,s)=-phi_j(a)phi_j(s). Since a+s>=a>0, summation is
uniform there and gives

    R_-(a,s)=-1/[2(a+s)],                    0<=s<=a.

The even boundary has zero first derivative of each response at t=a,
because phi'_j(a)=-c_j exp(-a*c_j) and
psi'_j(a)=c_j exp(-a*c_j). This derivative test is legitimate:
the partial derivative of E_j in either variable is bounded by
4c_j exp(-a*c_j)/d, whose series converges, and the derivative of
(7) converges uniformly near this edge. Differentiating the exact
kernel identity there yields

    partial_t R_+(a,s)=1/[2(a+s)^2],         0<=s<=a.

Symmetry gives the corresponding other edge. These checks include
the mixed corners and (a,a); the already removable corner (0,0)
is a separate case. The formulas check boundary cancellation only;
no operator sign is inferred from pointwise remainder values.

**Complex L2 extension.** C744v supplies bounded response partial-sum
quadratic forms and their increasing limit. Their polarized pairing is
the corresponding series: Cauchy--Schwarz bounds the sum of absolute
products of response coefficients by the two finite Bessel norms.
Thus this pairing is exactly the left side used in Section3, rather
than an unproved pointwise-kernel definition of S. For compactly
supported smooth f and g, (7) converges uniformly on the product of
their supports and (6) does so everywhere. Integrating each finite
identity against f(s)conjugate(g(t)) and taking its limit therefore
proves equality of the sesquilinear pairings, with the first slot
linear as required.

The weighted Schur integral in Section3 is exact by s=t*v^2 and is
bounded by pi*t^(-1/2); symmetry supplies the other Schur inequality.
Teschl's kernel bound applies to R because (11) gives a finite L2
norm on the square of measure a^2. It is not applied to 1/(t+s),
which is not square-integrable at (0,0). Hence both sides of (3) are
bounded. Approximate f and g independently in L2 by compact smooth
tests and use continuity of both pairings to obtain their equality
on every complex L2 pair. This closes the domain/limit passage
without interchanging an uncontrolled series at the singular corner.

**Rank, full error and tolerance.** The m-by-m midpoint table acts
through the m indicator functions, so its rank is at most m, not m^2.
Each correction E_j acts into span{phi_j,psi_j}, including j=0;
therefore rank at most m+2J and selfadjointness follow exactly from
(12). The largest displacement of the sum of two coordinates from
their midpoint sum is a/m. Multiplication of the bound H*a/m+B_J
by sqrt(a^2)=a gives precisely (4). The HS norm equals this kernel's
L2 norm by the cited Lemma6.9, and the operator norm is bounded by
it. The allowance pays both the midpoint error and every omitted
correction; neither component is a preview or an uncomputed tail.

Writing eta=H*a^2/m+C_a*exp(-2aJ), the displayed choice of m pays
the first term by delta/2. If delta>=2C_a, J=0 already pays the
second term; otherwise the stated logarithmic ceiling pays it.
This verifies the max-with-zero boundary case as well as J>0.
The two terms vanish as m,J tend to infinity, and all exponential
powers of3 given in Section4 have the stated exponents. The integer
rules define exact mathematical approximants; implementation and
rounding enclosures for evaluating them are not claimed by this proof.

This is an audited local REPRODUCTION/specialization, not progress beyond
the general source theorems or a sign result. C744v is still the sole
local mathematical input; C744z, C999k and C999y are later-use warnings,
not premises. No unchanged598, fixed32-prefix or600/603/635 prescription
has been reopened. A lower-reference form order, coercivity, effective
inverse action on the neutral restriction and the actual remote-plus-
induced comparison require separate work; raw-L2 convergence alone
does not pay any of them. Full matching Mathlib coverage remains
unchecked, as stated below.

## Mathlib

A full matching theorem for this two-parity fixed-kernel split, its exact
coefficient and the effective bound (4) has not been checked in Mathlib.
Supporting Schur and Hilbert-Schmidt facts are used through the precise
sources above; no claim of Mathlib absence, formal verification, or a
new general operator theorem is made.
