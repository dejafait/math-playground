# Corollary 984a: symmetric quartic real-radius coefficient obstruction

## Hypotheses

Use exactly the polynomial completion

    Q(s)=((s-3/4)^2+1)*((s-1/4)^2+1),
    xi_Q(s)=Q(s)/(2*Q(1)),
    H_Q(z)=2*xi_Q(1/(1-z)).

The normalized holomorphic logarithm of H_Q at z=0 defines the
ordinary, undivided real coefficients ell_n by

    log H_Q(z)=sum_(n>=1) (ell_n/n)*z^n.

For integers n>=2 set d_n=sum_(k=2)^n ell_k. Define the meromorphic
continuation of the cumulative local germ by

    F_Q(z)=[z*H_Q'(z)/H_Q(z)-ell_1*z]/(1-z).                (1)

The existence, reality and normalization of this local logarithm are
verified below. This is a polynomial model; it is not the actual xi
function and is not assumed to satisfy its arithmetic identities.

## Conclusion

The completion is entire, real under conjugation and invariant under
s -> 1-s, with xi_Q(0)=xi_Q(1)=1/2. It is positive on the real axis
and has exactly the four simple zeros 3/4+-i and 1/4+-i, all with
positive integer order. Nevertheless the following both hold:

    sup_(0<=r<1) (1-r)^2*|F_Q(r)| <= 5,                    (2)

and, with the fixed positive number epsilon_0=(1/4)*log(25/17),

    for every finite D>=0 there is an integer n>=2 such that
    d_n < -D*exp(epsilon_0*n).                              (3)

In particular the every-epsilon lower envelope for these d_n fails.
The Taylor coefficients of F_Q are exactly 0 at degrees0 and1 and
d_n at every degree n>=2. Its Taylor radius is R=sqrt(17)/5<1,
even though (1) is holomorphic near every real point 0<=r<1.
The values in (2) past R are values of meromorphic continuation,
not convergent Abel sums of that Taylor series.

Thus reality, reflection, this normalization, positive-real zero
exclusion, positive integer zero orders and the weak radial bound
(2) do not alone imply the coefficient lower envelope in L984(1).
This does not refute a zeta-specific recovery theorem with additional
independently paid input, and gives no information about actual Li
coefficient signs or actual off-line zeta zeros.

## Proof

### Imported theorem and scope

Import Pringsheim's theorem: a power series with nonnegative real
coefficients and finite positive Taylor radius R is singular at the
positive real point R. The precise source is P. Flajolet and
R. Sedgewick, *Analytic Combinatorics — Complex Asymptotics*,
zeroth edition, 8 May 2004,
[Theorem IV.3(ii), printed pp15-16/PDF23-24](https://algo.inria.fr/flajolet/Publications/ch4567.pdf#page=23).
Its primary statement and proof were inspected in the reused source
assessment. We import this theorem, not reprove it. The local Taylor
calculus and zero-order factorization used below are standard
holomorphic-function facts; see [DLMF 1.10(i)-(ii)](https://dlmf.nist.gov/1.10).

The general source tools are known. The work here checks their
applicability to this exact normalized polynomial and cumulative
observable, which the source does not compute. No general rational
coefficient asymptotic is needed: the argument retains the complete
germ and all its finite coefficients. In particular it does not drop
the polynomial part of an improper rational function. L984 is a
comparison and proof template only, not a mathematical premise about
arbitrary completions.

### Completion, normalization and local coefficients

Each factor of Q has real coefficients and is strictly positive at
every real s. Replacing s by 1-s interchanges the two factors, so
Q(1-s)=Q(s). The four listed zeros are distinct and are precisely
the zeros of the two quadratics; each is simple. Multiplication by
the positive constant 1/(2*Q(1)) changes none of these properties.
Direct evaluation gives Q(1)=Q(0)=425/256, establishing both
normalizations for xi_Q.

The substitution s=1/(1-z) gives the exact rational function

    H_Q(z)=(17-26z+25z^2)*(25-26z+17z^2)
                         /[425*(1-z)^4].                  (4)

It is holomorphic for |z|<1 and has H_Q(0)=1. Consequently it is
nonzero on a sufficiently small disk about0 and has a unique local
holomorphic logarithm with value0 there. For real z sufficiently
near0, H_Q(z)>0, so this logarithm is real; its Taylor coefficients
and hence every ell_n are real. Equation (4) gives

    ell_1=H_Q'(0)/H_Q(0)=4-26/17-26/25=608/425.            (5)

On a small common disk where the logarithm and geometric series
converge absolutely, differentiation and multiplication give

    z*H_Q'/H_Q=sum_(k>=1) ell_k*z^k,
    F_Q(z)=(sum_(k>=2) ell_k*z^k)*(sum_(j>=0) z^j)
          =sum_(n>=2) d_n*z^n.                             (6)

This proves the asserted finite-degree normalization as well as
the exact undivided coefficients. Subsequent use of (1) is of a
single-valued rational function, requiring no global logarithm.

### A bound on the entire positive real radius

For 0<=r<1 put s=1/(1-r)>=1. Logarithmic differentiation of Q
and the chain rule give

    Q'(s)/Q(s)=sum_(a in {1/4,3/4}) 2*(s-a)/((s-a)^2+1),
    (1-r)^2*F_Q(r)=r*s*Q'(s)/Q(s)-ell_1*r*(1-r).           (7)

For each a set t=s-a>0. Using 2*t<=t^2+1,

    0 < 2*s*(s-a)/((s-a)^2+1)
      =2*t^2/(t^2+1)+2*a*t/(t^2+1) <= 2+a.

Thus A=r*s*Q'(s)/Q(s) lies in [0,5], including r=0.
By (5) and r*(1-r)<=1/4, the quantity
B=ell_1*r*(1-r) lies in [0,152/425], a subset of [0,5].
It follows that |A-B|<=5, proving (2) for every r in the
whole interval, without numerical sampling or a limiting interchange.

### Taylor radius, pole survival and positive-point regularity

The zeros of the two numerator factors in (4) are respectively

    w_+=(13+16*i)/25,  w_-=(13-16*i)/25,
    v_+=(13+16*i)/17,  v_-=(13-16*i)/17.                   (8)

They are distinct and simple. Their moduli satisfy

    |w_+|^2=|w_-|^2=17/25,
    |v_+|^2=|v_-|^2=25/17.

There are no other zeros. Neither 0 nor1 is a zero, and
R=|w_+|=|w_-|=sqrt(17)/5 is strictly between0 and1.
The map s(z)=1/(1-z) has derivative s(z)^2, nonzero at each
mapped zero, consistent with preservation of the original simple
orders. In particular the inner zero orders have not been replaced
by signed or fractional residues.

At an inner zero w, local factorization writes
H_Q(z)=(z-w)*u(z), with u holomorphic and nonzero near w.
It follows from (1) that

    Res_(z=w) F_Q(z)=w/(1-w) != 0.                        (9)

The subtracted ell_1*z/(1-z) is holomorphic there and cannot
cancel the pole; neither can contributions from the other zeros,
which are regular near w. Formula (1) is holomorphic for |z|<R,
so (6) has radius at least R. Its nonzero pole (9) prevents a
larger Taylor radius, by uniqueness of holomorphic continuation.
Thus the radius is exactly R.

For every real 0<=r<1 the number s(r) is real and at least1.
Both quadratic factors of Q are positive, so H_Q(r)>0.
Consequently (1) is holomorphic on a neighborhood of each such r,
including the positive point R. Its expression on that neighborhood
agrees with the same rational function (6) inside |z|<R.
This is continuation of the same germ across R, rather than a
different branch or a convergent Taylor sum beyond its radius.

### Failure at one fixed epsilon

Set epsilon_0=-(log R)/2=(1/4)*log(25/17)>0 and
b=exp(-epsilon_0)=sqrt(R), so R<b<1. Suppose that some finite
D>=0 obeys d_n>=-D*exp(epsilon_0*n) for every n>=2.
The correction

    E_D(z)=D*(z/b)^2/(1-z/b)
          =sum_(n>=2) D*exp(epsilon_0*n)*z^n               (10)

is holomorphic for |z|<b. The Taylor coefficients of K=F_Q+E_D
are then nonnegative real numbers in every degree: they are0
at degrees0 and1, and d_n+D*exp(epsilon_0*n) thereafter.

The function K is holomorphic for |z|<R, retains the nonzero
pole (9) at w_+, since E_D is holomorphic there, and therefore
has Taylor radius exactly R. This is a finite positive radius.
At the positive real point R, both F_Q and E_D are holomorphic
on a common neighborhood and agree with their local sums on its
intersection with |z|<R. Thus K extends holomorphically across R.
Pringsheim's theorem, with every hypothesis now checked, contradicts
this regularity. No such D exists, proving (3).

This fixes epsilon_0 once and for all, before the supposed D.
It is stronger than merely finding a negative coefficient; arbitrary
finite exceptional degrees could be absorbed by enlarging D and
so cannot account for the obstruction. No explicit phase-density
or asymptotic negative-subsequence assertion is needed.

### Scope and route decision

Both approved thresholds hold for this one model. Hence park the
claim that the retained properties alone force the every-epsilon
lower coefficient envelope. This is an informative model obstruction,
not an impossibility theorem for every real-axis method. It omits
actual-xi order-one growth, gamma factors, zero counts, the Euler
product and the arithmetic identity used in L984. The actual
arithmetic premise, actual-Xi positivity, forcing and capped E_n
bridge remain open. The earlier direct Tauberian import stop concerns
source hypotheses; this calculation supplies the separate concrete
model evidence without changing that stop's scope.

Written in step418, 11 November 2026, using the pre-existing
SPECIALIZE assessment review417. Classification: REPRODUCTION.
This is local progress through a known-tool specialization, not a
claim of mathematics beyond the checked sources. The independent
audit below accepts this limited result; it is not a complete RH candidate.

### Independent audit — step420, 11 November 2026

This audit uses the pre-existing SPECIALIZE review418, separately
approved in step419. The imported Pringsheim and local holomorphic
calculus contracts above are reused. No new general theorem, numerical
sampling or rational-asymptotic theorem is needed.

**Algebra and retained properties.** At s=1 the two factors are
17/16 and 25/16, so Q(1)=425/256. Reflection interchanges them
and gives Q(0)=Q(1). Each is positive for every real argument.
Their roots 3/4+-i and 1/4+-i are pairwise distinct, each simple;
the positive normalization therefore preserves all four orders.
After s=1/(1-z), the two factor numerators, with common denominator
16*(1-z)^2, are respectively

    (1+3z)^2+16*(1-z)^2=17-26z+25z^2,
    (3+z)^2+16*(1-z)^2=25-26z+17z^2.

Their product is 425-1092z+1590z^2-1092z^3+425z^4.
Thus (4) is exact, H_Q(0)=1, and the logarithmic derivative at
zero is 4-1092/425=608/425 as claimed. A sufficiently small
zero-free disk supplies the normalized local logarithm; reality
follows from conjugation and uniqueness of that normalization.
Differentiating its convergent Taylor series gives ell_k, without
a remaining factor k. Subtracting ell_1*z removes degree1 exactly;
multiplication by the convergent geometric series gives zero at
degrees0/1 and sum_(k=2)^n ell_k at every degree n>=2.

**Uniform real-radius estimate.** The derivative of s(r) is s(r)^2.
Multiplying (1) by (1-r)^2 therefore gives precisely (7), since
(1-r)*s(r)^2=s(r). For each a in {1/4,3/4}, t=s-a>0 and
2*t<=t^2+1 imply 2*t^2/(t^2+1)<=2 and
2*a*t/(t^2+1)<=a. Summing gives 0<=A<=r*(4+1)<=5.
Also 0<=B<=ell_1/4=152/425<5. The inequality
|A-B|<=max(A,B)<=5 proves the required bound over the whole
interval, including r=0. No Taylor convergence at these real
arguments beyond R is asserted or required.

**Exact radius and continuation.** Both quadratic discriminants
are -1024. Their roots are exactly (8), with squared moduli 17/25
and 25/17. The inner pair is nonreal, nonzero and distinct from1;
the outer pair lies outside the unit disk. H_Q is holomorphic in
the unit disk and has no zero of smaller modulus than R. Near
each inner root w its simple factor gives H_Q'/H_Q=1/(z-w)
plus a holomorphic term. Multiplication by z/(1-z) leaves residue
w/(1-w)!=0. All other terms of (1), including the subtracted
degree-one contribution, are regular there. The germ is analytic
inside R and has this genuine boundary pole, so its Taylor radius
is exactly R by uniqueness of continuation. On the real interval
[0,1), positivity of Q(s(r)) ensures H_Q(r)>0. The rational
expression is therefore holomorphic near positive R, and its
agreement with the Taylor germ on the inner overlap supplies
continuation of that same germ. A global logarithm is never used.

**Fixed epsilon and Pringsheim hypotheses.** The specified
epsilon_0=-log(R)/2=log(25/17)/4 is positive and independent
of D. Its correction radius b=exp(-epsilon_0)=sqrt(R) is
strictly larger than R. For any proposed finite D>=0, (10) has
exact coefficients D*exp(epsilon_0*n) for n>=2 and zero for
n=0,1. If the supposed coefficient lower bound held at every
n>=2, K would thus have real nonnegative coefficients at every
degree. E_D is analytic on |z|<b, also when D=0, and cannot
cancel either inner pole. K consequently has finite positive
Taylor radius R. A sufficiently small disk about positive R lies
inside |z|<b and the regularity neighborhood of F_Q, providing
holomorphic continuation of the same K germ across R. These
are all the hypotheses and the contradictory regularity conclusion
of the imported Pringsheim theorem. Hence each finite D fails at
some n>=2, with the strict inequality in (3). This also rules out
an eventual lower bound: finitely many real exceptional coefficients
could otherwise be covered by increasing D.

Audit decision: accept (2), (3), and exactly the stated retained
properties without a mathematical repair. The model establishes
neither an actual-zeta estimate nor failure of such an estimate.
Its self-contained specialization has no direct local lemma inputs;
L984 remains comparison only, so the DAG row stays empty.
This is first independent validation of the written obstruction,
not a new result beyond the cited tools. Actual-xi growth, gamma
factors, zero census, Euler product, arithmetic, signs, forcing and
the capped E_n bridge remain unpaid. Mathlib coverage remains
unchecked and unknown.

### Repeated independent replay — step443, 11 November 2026

The invocation again nominated the exact review418 audit, although
step420 above already completed it. A fresh replay accepts the same
conclusions without repair: (4)-(6) retain every coefficient including
degrees0/1; (7) gives |A-B|<=5 on the full real interval; (8)-(9)
give the exact inner radius and uncancelled residues. For the fixed
epsilon_0, R<exp(-epsilon_0)=sqrt(R) makes the correction analytic
at each inner pole and at positive R. The putative lower bound gives
nonnegative coefficients in every degree, contradicting the cited
Pringsheim theorem at that regular positive boundary point. D=0
causes no exception: its correction is identically zero and remains
analytic on the required larger disk. The finite-prefix enlargement
argument also remains valid.

This is repeated validation of the existing step420 result, with no
new mathematical evidence or advance beyond the cited tools. Outcome
STALLED; actual task proof_audit, RESEARCH/REPRODUCTION. No broader
model, actual-zeta conclusion, new mathematical dependency or change
to the argument is introduced. The earlier audit is preserved and
this exact audit should not be the next action again without new input.

## Mathlib

Full matching Mathlib coverage for this exact normalized model and
its combined radial/coefficient conclusion was not checked and is
unknown. No absence claim or formal verification is made. The proof
imports the precisely cited analytic theorem and explicitly checks
its model hypotheses; it does not rely on a presumed Mathlib theorem.
