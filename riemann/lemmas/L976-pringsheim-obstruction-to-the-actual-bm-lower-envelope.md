# Lemma 976: Pringsheim obstructs the actual b_m lower envelope

## Hypotheses

Use the actual entire completion xi and its symmetries and zero
correspondence from L018, and real-strip nonvanishing from L013.
Use L975's actual logarithm germ, with its already justified branch:

    g(w)=xi(1/(2-w)),
    G(w)=F(w-1)=sum_(m>=0) b_m w^m,      |w|<3/2,
    exp G(w)=g(w),                       G(1)=-log 2.     (1)

All b_m are real by L975. Import unconditional existence of a
nontrivial zeta zero from [NIST DLMF 25.10(i), Distribution](https://dlmf.nist.gov/25.10.i),
as inspected in steps208-209. This handbook states infinitely many
strip zeros; only one is needed. No RH, simple-zero condition,
numerical zero location, coefficient sign, or radius-two logarithm
is assumed. L026's localization is already used within L975; it is
not reapplied here. L968's Li criterion is not an input to this proof.

## Conclusion

The exact Taylor radius of the actual germ (1) is

    R=min_{xi(rho)=0} |2-1/rho|,        3/2 <= R < 2.    (2)

The minimum exists and is attained. The same germ nevertheless has
an analytic continuation across the positive real point w=R.

L975's additional hypothesis

    for every delta in (0,1), there is C_delta>0 such that
    b_m >= -C_delta (2-delta)^(-m) for all m>=1          (H)

is false for these actual coefficients. It remains false if, for
each delta, the inequality is required only for m>=M_delta, where
M_delta is any finite integer depending on delta.

This stops payment by this particular sufficient envelope. It does
not invalidate L975's interior inverse or conditional implication,
and proves neither RH nor its negation. Classification: REPRODUCTION,
an actual-xi specialization of the inspected boundary theorem, with
no claim of novelty beyond the sources checked. Written in step210,
10 November 2026; passed the separate conceptual audit in step212 on
the same date. The statement and mathematical argument are unchanged.

## Proof

### Imported boundary theorem and analytic tools

Import Pringsheim's theorem in P. Flajolet and R. Sedgewick,
*Analytic Combinatorics — Complex Asymptotics*, zeroth edition,
8 May 2004, [Theorem IV.3(ii), printed pp.15-16, PDF pp.23-24](https://algo.inria.fr/flajolet/Publications/ch4567.pdf#page=23):
a power series with nonnegative real coefficients and finite positive
radius of convergence R is singular at the positive real point R.
The statement and its complete proof were inspected in steps208-209.
This is the 2004 theorem numbering. It is imported, not reproved.

The local analytic tools are the Taylor and zero-order facts in
[DLMF 1.10(i)](https://dlmf.nist.gov/1.10.i), analytic continuation
and the identity theorem in [1.10(ii)](https://dlmf.nist.gov/1.10.ii),
and the normalized local logarithm expansion in
[1.9(vi), (1.9.53)-(1.9.57)](https://dlmf.nist.gov/1.9.vi).
For a zero-free disk we use the holomorphic logarithm theorem with
normalization, as already justified by integration of g'/g in L975.
The source theorem supplies no radius or coefficient signs for this
signed germ; those applications require the checks that follow.

### A mapped zero lies strictly inside radius two

Choose a nontrivial zero rho=beta+i*gamma. L018 identifies it with
a zero of xi in 0<beta<1, and permits replacing rho by 1-rho.
We can therefore arrange beta>=1/2. Every such rho is nonzero.
At its mapped point w_rho=2-1/rho the inner map is regular and
g(w_rho)=0. Direct algebra gives

    |w_rho|^2
      =4-4*Re(1/rho)+|1/rho|^2
      =4+(1-4*beta)/|rho|^2
      <=4-1/|rho|^2 < 4.                               (3)

Write r_0=|w_rho|<2. This is an exact strict inequality from an
existing zero; it does not use a first-zero approximation or RH.

The function g is holomorphic on |w|<2. Its zeros there are exactly
the points 2-1/rho that lie in that disk. Since (1) expresses g as
an exponential on |w|<3/2, g has no zeros in that smaller disk.

There are finitely many mapped zeros with |w|<=r_0: for such w,

    |1/(2-w)| <= 1/(2-r_0),

so the corresponding xi zeros lie in a compact disk. The entire
function xi is not identically zero, since xi(1)=1/2, hence has only
finitely many zeros there. The map is injective. The set of mapped
zeros of modulus at most r_0 is nonempty and finite, so it has a
least modulus R. Every other mapped zero has modulus greater than
r_0. Thus this R is exactly the global minimum in (2), and
3/2<=R<=r_0<2. Select one attaining point w_* with corresponding
zero rho_*.

### Exact radius and arbitrary zero multiplicities

The disk |w|<R is zero-free for g and simply connected. Its analytic
logarithm normalized to G(0)=b_0 agrees with (1), by uniqueness on
their common disk. We continue to call it G. Thus G's Taylor series
has radius at least R, and exp G=g throughout |w|<R.

Let k>=1 be the multiplicity of rho_*. Locally,

    xi(s)=(s-rho_*)^k v(s),              v(rho_*)!=0.

The derivative of s(w)=1/(2-w) at w_* is rho_*^2!=0.
Consequently, on a small disk about w_*,

    g(w)=(w-w_*)^k u(w),                 u(w_*)!=0,     (4)

where u is holomorphic and nonzero after shrinking the disk.
In particular this is a genuine zero for every allowed multiplicity.
The logarithmic derivative has local form

    g'(w)/g(w)=k/(w-w_*)+u'(w)/u(w).                    (5)

There is no holomorphic extension of G across w_* agreeing with
its values inside |w|<R. Indeed, if H_* were such an extension,
exp H_*=g on the nonempty overlap, then on its whole small disk by
the identity theorem. At w_* this would give exp H_*(w_*)=0,
which is impossible. Equivalently, (5) has nonzero residue k that
an analytic derivative cannot have. No choice of a logarithm
constant removes this zero singularity.

If the Taylor radius of G were greater than R, its Taylor sum would
provide precisely that forbidden extension at w_*. The exact radius
is therefore R. The argument makes no sum over zeros and requires
neither simplicity nor an estimate on their spacing.

### Continuation of the same branch at the positive radius

For real 0<=x<2, s(x)=1/(2-x) is real and at least 1/2.
L013 excludes a zero for 1/2<=s<1; L018 gives xi(1)=1/2 and
excludes zeros for s>1. Conjugation symmetry makes g(x) real.
It is nonzero on the connected interval [0,2), and g(1)=1/2>0,
so g(x)>0 throughout that interval.

On 0<=x<R, exp G(x)=g(x)>0. Hence Im G(x) lies in 2*pi*Z
and is constant by continuity. Because 1<R and G(1)=-log 2,
that constant is zero. Therefore

    G(x)=log g(x)      (ordinary real logarithm), 0<=x<R. (6)

At x=R<2, g is holomorphic and g(R)>0. Choose a disk B centered
at R, of radius less than 2-R, on which

    |g(w)/g(R)-1| < 1/2.

The convergent local logarithm series defines an analytic L on B
with exp L=g and L(R)=log g(R). For real x in B it is the real
logarithm of g(x). Thus L(x)=G(x) on a nonempty real interval
immediately to the left of R. The intersection B with |w|<R is
connected (both disks are convex); the identity theorem gives
L=G on the whole intersection. This is an analytic extension of
the same Taylor germ across R, with its constant explicitly fixed.
It is not a global branch through any xi zero.

### The hypothetical envelope supplies a forbidden correction

Suppose the eventual version of (H) holds. Choose the single value

    a=(R+2)/2,       delta=2-a=(2-R)/2.                 (7)

Then R<a<2 and 0<delta<=1/4<1. The universal quantifier in
(H) supplies C_delta>0 and a finite integer M>=1 such that
b_m>=-C_delta*a^(-m) for every m>=M. Enlarge the constant to

    C=max(1, C_delta, -b_0,
          {max(0,-b_m)*a^m : 1<=m<M}).                 (8)

An empty prefix contributes no elements to this finite maximum.
Every b_m is finite and real, so C is finite and positive. For

    K(w)=G(w)+C/(1-w/a)
        =sum_(m>=0) c_m w^m,       |w|<R,

the coefficients are c_m=b_m+C*a^(-m). Equation (8) gives
c_0>=0, pays every exceptional index 1<=m<M, and, together
with C>=C_delta, gives c_m>=0 for every m>=M.
Thus every coefficient, including the constant term, is nonnegative.
This coefficient identity uses a geometric series strictly within
its radius a, never a boundary substitution or a zero-sum exchange.

The correction C/(1-w/a) is holomorphic throughout |w|<a.
It is analytic at every point of |w|=R, since R<a. Therefore K
is analytic in |w|<R, and cannot extend across w_*: subtracting
the analytic correction from such an extension would extend G
there, contradicting (4)-(5). K's exact Taylor radius is R.
In particular, this radius is not inferred merely from the disk on
which the two summands were initially expanded.

On the other hand, the extension L just constructed, plus the same
correction, analytically extends K across the positive point R.
Shrink B further to radius less than a-R if necessary. The overlap
agreement is preserved. We have now verified all three hypotheses
needed for the contradiction: nonnegative coefficients, finite
positive radius R, and regularity of this germ at its positive
radius point. Pringsheim's theorem forbids the last property.

The eventual version of (H) is false. Its all-index version is
the special case M=1 and is false as well. The choice (7) may
depend on the actual radius; no effective value is needed because
(H) quantified over every delta before choosing its constants.

### Scope of the obstruction

The strict radius gap comes from an existing zero and reflection,
whether or not all zeros lie on the critical line. It supplies no
off-line zero. Failure of a sufficient condition for RH does not
negate RH. L975's complete inverse and its conditional implication
remain intact; L030-L032/C032a positivity and L966's signed forcing
remain unresolved. This proof does not assess weaker envelopes,
cancellation-sensitive inverse estimates, or Coffey's conditional
asymptotic. Those are outside the approved bounded test.

### Independent conceptual audit, step212

The audit accepts the stated obstruction, including its eventual-prefix
version, under the named inputs. It adds validation of this specialization,
not a new theorem or a stronger coefficient conclusion. The following
checks concern the actual germ, rather than a formal model.

The interior input used from L975 is its branch and real coefficients,
not its conditional Li conclusion. Its domain check uses |s|<2 and
L026's |Im s|>4 for a possible zero, so is independent of any assumed
zero signs. L026's rectangle excludes |Re alpha|<=4 because its strict
error bound is 11/24<1/2; L018 supplies the strip restriction needed
there. On the simply connected disk the normalized logarithm is unique.
Translation to w puts its normalizing point at w=1, inside the disk.
Thus the audit does not borrow (H), RH, or L968 to construct G.

In (3) reflection supplies beta>=1/2 without fixing gamma or its sign.
The finite nonempty set within r_0 contains all possible competitors
for the global minimum: a mapped zero outside that set has modulus
greater than r_0. The bound on |rho| makes this set compact in the
entire-function variable, where zeros are isolated. No compactness at
w=2 is asserted. The existing zero-free disk gives R>=3/2 and hence
R>1. The local inner derivative rho_*^2 is nonzero, so every positive
integer multiplicity remains a genuine zero. An extension of G would
exponentiate to g across this zero by the identity theorem and is
impossible. These facts justify an exact radius, not just a lower bound.

For the positive point R, the interval [0,2) maps into [1/2,infinity).
L013 handles the open-strip part, and L018 handles 1 and the part above
1. The sign follows by continuity from g(1)=1/2. The imaginary part of
G is fixed to zero on [0,R) by that same normalizing point. The local
logarithm at R consequently agrees with G on a real interval with
an accumulation point in the connected intersection of the two disks.
This verifies continuation of the original germ, not merely existence
of a different logarithm near R.

The single delta=(2-R)/2 belongs to (0,1/4], including R=3/2.
The claimed every-delta envelope must hold at this delta even though R
is ineffective. Its one finite threshold M can be increased to at least
1. Equation (8) then covers b_0, every m<M, and all m>=M with a single
finite constant; it asks for no uniformity of M or C across deltas.
The correction's pole lies at a>R. Subtracting this analytic correction
from a purported extension of K at w_* would extend G, so K also has
exact radius R. Adding it to the verified branch at positive R gives
the extension forbidden by the cited Pringsheim theorem. All coefficient,
radius and continuation hypotheses of that theorem are therefore met.

The direct local mathematical inputs remain L013, L018 and L975;
L026 is used through L975. L968 concerns downstream sufficiency only.
No new DAG edge, numerical certificate, theorem reproof, or source
hypothesis is needed. The inverse, replacement signed estimates, and
the main positivity gap retain their previously stated qualifications.

## Mathlib

Full matching coverage of this actual-xi Pringsheim specialization
has not been checked and is unknown. No Mathlib theorem is imported.
Generic power-series or analytic-logarithm support would not by
itself identify this radius, branch, or envelope quantifier.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
