# L101 — Rational scaling quotient and exact primitive lifting

## Hypotheses

Use the forms Q and H and the two complete systems of audited L095.
Fix d in {1,5}, put n=dC, and consider their common rational version

    n−5m=d^11 u^5,             H(m,n)=d^11 a^3.             (1)

The rational variety below is restricted to n,u,a nonzero. The positive
part has m,n,u,a>0. An admissible integral representative means precisely
m,u,a positive integers, C=n/d a positive integer, and

    gcd(m,u)=1, gcd(m,55)=1, gcd(C,15)=1.                  (2)

These are the original L095 conditions, not an enlarged notion of
weighted primitivity. For d=1, (1) is system I; for d=5 it is system II.

## Conclusion

The rational action

    lambda·(m,n,u,a)=(lambda^15 m,lambda^15 n,
                     lambda^3 u,lambda^40 a)             (3)

preserves (1). On the indicated open set its invariant field is Q(t),
where t=m/n is the original rational-root ratio. More precisely, put

    h(t)=H(t,1),
    F_d(t)=d^77 h(t)/(1−5t)^8,
    w=a/u^13.

There is a rational isomorphism with the pairs (t,w) satisfying
w!=0, h(t)!=0, and 1−5t!=0, given by the displayed forward formulas
and the following inverse:

    u=w^3/F_d(t),
    a=w^40/F_d(t)^13,
    n=d^11 w^15 / ((1−5t) F_d(t)^5),
    m=tn,                    C=n/d.                      (4)

The action on these coordinates is (t,w) -> (t,lambda w).
Consequently each rational t with h(t)(1−5t)!=0 gives exactly one
rational orbit, with a rational section w=1. Positive rational orbits
are parametrized by every rational t in (0,1/5), with w>0. Thus this
quotient supplies no rational-point exclusion on that interval.

Write such a t=M/N in positive reduced form. Its orbit has an
admissible integral representative if and only if all the following
hold:

1. N/d is an integer, gcd(N/d,15)=1, and gcd(M,55)=1.
2. (N−5M)/d^11 is the fifth power of a positive integer u.
3. H(M,N)/d^11 is the cube of a positive integer a.

If it exists, this representative is unique: m=M, n=N, C=N/d, with
u and a as above. These tests are exactly the original two L095 power
equations and gcd restrictions in reduced-root coordinates. They do
not yield an additional necessary restriction, a positive-genus curve,
a primitive solution or an exclusion. Direct quotient rationality
therefore fails the approved exclusion-oriented continuation test.

## Proof

### One common scale and its rational coordinates

Both m and n have weight fifteen. Since H is homogeneous of degree
eight, its value has weight 120, which is three times the weight forty
of a. The first equation of (1) has weight fifteen, five times the
weight three of u. Its constant d^11 and that in the second equation
are fixed. This proves (3), including d=5. Also C=n/d has weight
fifteen, so that no replacement of the second argument 5C in II occurs.

For any point in the specified open set, the first equation implies

    n=d^11 u^5/(1−5t).

Its denominator is nonzero because n and u are nonzero. Homogeneity
and the second equation then imply

    a^3=n^8 h(t)/d^11
       =d^77 u^40 h(t)/(1−5t)^8
       =F_d(t) u^40.                                    (5)

In particular h(t) is nonzero. With w=a/u^13, equation (5) gives
w^3=F_d(t)u. This is precisely the first formula in (4); the formula
for a follows from a=w u^13 and the formula for n from the first
equation. Thus every forward image has exactly the stated inverse.

Conversely take any rational t,w satisfying the three open conditions
and define (4). Every coordinate required nonzero is nonzero, and

    n(1−5t)=d^11 w^15/F_d(t)^5=d^11 u^5.

For the other equation, compute the entire scalar, not just its class:

    n^8 h(t)/d^11
      = d^77 w^120 h(t) / ((1−5t)^8 F_d(t)^40)
      = w^120/F_d(t)^39
      = a^3.

Moreover m/n=t and a/u^13=w. These are two-sided rational inverses,
not merely a dominant parametrization. They prove the asserted open
isomorphism and its function field Q(t,w). The weights give weight
zero for t and weight 40−13·3=1 for w.

For completeness, the invariant subfield for this action is exactly
Q(t). Over the algebraic closure of Q(t), the finite set of zeros and
poles of a rational function of w cannot contain a nonzero finite
point and be invariant under multiplication by every nonzero rational
lambda: such a point has infinitely many distinct translates.
Consequently an invariant function is c w^k; its invariance forces
k=0. Its membership in Q(t,w) then makes c belong to Q(t). The
reverse inclusion is immediate. This is an elementary calculation,
not an application of an uninspected quotient theorem.

For any rational pair of points with the same t, their nonzero rational
w coordinates differ by a nonzero rational lambda. Formula (4) proves
that (3) carries one to the other. Hence rational coarse parameters
have actual rational orbits and a section; there is no residual
rational twist being ignored on this open set.

### Positive domain and omitted loci

On the positive part of (1), n−5m>0, so 0<t<1/5. Every coefficient
of H is positive, so h(t)>0 on this interval; hence F_d(t)>0 and
w=a/u^13>0. Conversely every rational t in this interval and rational
w>0 gives positive m,n,u,a,C by (4). Positive points in a single
orbit are related by a positive rational lambda.

The removed sets n=0, u=0 and a=0 do not meet the original positive
integer domain. The first equation makes 1−5t=0 equivalent to u=0
when n!=0; the second makes h(t)=0 equivalent to a=0 there.
The endpoint t=0 means m=0 and is also outside the target. Nothing
has been asserted about components supported on these boundary sets
or about projective compactifications. None is needed to cover any
positive L095 representative. No zero of Q is lost either: Q(m,n)>0
for positive m,n, and the formulas do not divide by Q.

### Primitive integral lifting

First suppose a representative satisfies (1) and (2). In system I,

    gcd(m,n)=gcd(m,5m+u^5)=1.

In system II, gcd(m,5)=1 by (2), and

    gcd(m,C)=gcd(m,m+5^10u^5)=1,

so gcd(m,n)=gcd(m,5C)=1 as well. Thus m/n is already a reduced
positive fraction. Uniqueness of the positive reduced representation
of M/N forces m=M and n=N. In particular its coordinates cannot
be varied to clear denominators while retaining (2). Equations (1)
and (2) now imply all three tests in the conclusion.

Conversely suppose the tests hold. Set m=M, n=N, C=N/d and use the
positive integer roots u,a in tests 2 and 3. They give exactly (1).
If a prime divided both M and u, the equality

    N=5M+d^11 u^5

would make it divide N, contradicting gcd(M,N)=1. Thus gcd(m,u)=1;
the other two gcd conditions are test 1. For d=1 this is the complete
system I and for d=5 it is the complete system II. L095's converses
therefore give the original positive primitive reconstructed bases
A=ma and B=Q(m,n)u, as required. No new existence is being claimed:
tests 2 and 3 remain unsolved simultaneous conditions.

The roots, if present, are unique since the fifth- and cube-power
maps are strictly increasing on positive integers. This proves
uniqueness of the admissible representative. It really lies in the
rational orbit at t: its w=a/u^13 is rational and nonzero, and the
previous orbit calculation applies. In particular there is no
additional rational-scale existence condition omitted from the tests.
For an arbitrary rational starting point (t,w_0), the scale to that
representative is exactly lambda=(a/u^13)/w_0.

Although any rational tuple can be made integral by taking a sufficiently
divisible positive integer lambda in (3), this does not establish (2).
After obtaining an integral tuple, further scaling by any integer prime
q multiplies m by q^15 and u by q^3 and makes their gcd at least q^3.
Primitive lifting is exactly the three tests proved above, rather than
unrestricted weighted denominator clearing.

### Qualifications and source comparison

The method specializes the known degree-coprime scaling phenomenon in
H. Darmon and A. Granville, *On the equations z^m=F(x,y) and
Ax^p+By^q=Cz^r*, Bull. London Math. Soc. 27 (1995), 513–543,
p.515 and Section 1.1 pp.518–519,
[DOI](https://doi.org/10.1112/blms/27.6.513),
[published author-hosted text](https://www.math.mcgill.ca/darmon/pub/Articles/Research/12.Granville/pub12.pdf).
Those passages, including their proper/improper qualification, were
inspected in the reused assessment. No general theorem from that
paper is reproved or needed as a mathematical premise here. The
explicit specialization is necessary because rationality of the
original Fermat surface alone would not prove rationality of this
rational-factor pullback, nor primitive integer lifting for it.

This result is a local notebook advance in understanding the failed
shortcut, classified REPRODUCTION of the assessed scaling method;
no originality is claimed. The rational-quotient shortcut is parked,
without ruling out nonlinear covers, number-field descent or the
original integer equations. Other algebra types and other signatures
are independent unresolved gaps. The independent critical audit below
confirms the calculation without correction.

### Independent critical audit — 2026-10-19

Verdict: **PASS without correction**, under the unchanged prior SPECIALIZE
assessment `drafts/literature/2026-10-19-rational-factor-scaling-quotient.md`.
The mathematical input remains audited L095 alone. The cited scaling
literature supplies method coverage, not an additional theorem premise.
This audit proves no new integer restriction and does not reopen the
direct-quotient exclusion route.

The scalar calculation can be checked independently before choosing w.
Put b=1−5t and f=d^77 h(t)/b^8. On the stated open set,

    n=d^11 u^5/b,
    a^3=d^(88−11) u^40 h(t)/b^8=f u^40.

Thus the exponent 77 is exact for each fixed d, not just modulo cubes.
The common weights (15,15,3,40) give weights 15 and 120 to the two
equations. For d=5, n=5C converts the first equation to
C=m+5^10u^5 and leaves the second as H(m,5C)=5^11a^3.
Neither scaling nor division has changed its constant.

Now w=a/u^13 gives w^3=fu, since 40−39=1. Hence
u=w^3/f, a=w^40/f^13, n=d^11 w^15/(b f^5), and m=tn.
Substituting these expressions gives, respectively,

    n−5m=d^11 w^15/f^5=d^11 u^5,
    H(m,n)/d^11=d^77 w^120 h(t)/(b^8 f^40)
                   =w^120/f^39=a^3.

In the other direction a/u^13=w^(40−39) f^(13−13)=w,
and m/n=t. All divisions have nonzero denominators by the explicit
open conditions. These two compositions establish the open isomorphism,
not merely a parametrization or a dimension count.

The weight of w is 40−13·3=1. In particular, for two rational points
over the same t, lambda=w_2/w_1 is itself rational and sends one point
to the other: the inverse formulas scale u,a,n,m by lambda^3,
lambda^40,lambda^15,lambda^15. There is no root extraction or residual
twist in this orbit comparison. Setting w=1 gives a rational section.
For the invariant-field assertion, extend Q(t) to its algebraic closure.
An invariant rational function in w has a finite divisor stable under
every rational nonzero multiplier. Any nonzero finite zero or pole would
have infinitely many distinct translates in characteristic zero. Its
divisor is therefore supported on 0 and infinity, so the function is
c w^k. Invariance under, for example, lambda=2 forces k=0. A constant
in w belonging to Q(t,w) lies in Q(t), as is also seen by evaluating a
rational presentation at any rational w avoiding its denominator.
This proves the invariant field with no quotient theorem assumed.

Positivity and deleted loci also pass. A positive point has n−5m>0,
hence 0<t<1/5. Positive coefficients of H give h(t)>0, so f>0.
Every rational t in this interval and w>0 reconstructs positive values
of every coordinate. Conversely positive coordinates give w>0. No
positive integral point lies on n=0, u=0, a=0 or m=0; when n is
nonzero, b=0 forces u=0 and h(t)=0 forces a=0. Q is positive in
this domain and is not a denominator in the inverse formulas. Thus the
open calculation covers the entire domain needed for L095, without
claiming anything about omitted components or compactifications.

For integral lifting, let t=M/N with positive coprime M,N. In I an
admissible representative satisfies gcd(m,n)=gcd(m,u^5)=1. In II,
gcd(m,5)=1 and gcd(m,u)=1 give gcd(m,C)=1 and then gcd(m,5C)=1.
In both cases m=M and n=N, by uniqueness of reduced positive fractions.
Consequently N/d must be an integer prime to 15, M must be prime to 55,
and the exact fifth- and cube-power tests in the conclusion are necessary.
For d=1 these conditions force v_5(N)=0; for d=5 they force v_5(N)=1.
The two denominator cases have not been identified with one another.

Conversely, from the three tests choose their unique positive integer
roots u and a, and set m=M, n=N, C=N/d. If a prime divided M and u,
the equality N=5M+d^11u^5 would force it to divide N, a contradiction.
This proves the one gcd condition not explicitly listed in test 1;
all remaining integrality and gcd conditions are exactly that test.
L095's audited converse then supplies positive primitive A=ma,
B=Q(m,n)u and C with the correct rational direct factor. This use of
L095 is essential to reconstruction of the original equation, and is
already recorded by the single DAG input. Positive integer power roots
are unique, so there is at most one admissible representative. Its
rational w=a/u^13 places it in the actual orbit, with rational scale
w/w_0 from any chosen rational starting point in that orbit.

Finally, denominator clearing can make all coordinates integral because
their weights are positive, but it cannot establish these gcd tests.
After an integral point is obtained, an additional prime scale q forces
q^3 to divide both m and u. Thus rationality and primitivity are distinct
conditions in the exact calculation, rather than an unproved warning.
The audit confirms only that this quotient's rational-point condition
is vacuous on the positive interval and its primitive-lifting conditions
restore L095. It does not prove all possible class-free arguments fail,
give a height bound, solve either integer system, or exclude any algebra
type or signature. No script, numerical sample or new theorem is needed
for these exact identities and gcd implications.

## Mathlib

Full matching coverage of these explicit quotient and lifting formulas:
**not checked**. The proof is elementary rational algebra, homogeneity,
integer gcd arithmetic and L095's audited converse. No formal
verification or absence claim is made.
