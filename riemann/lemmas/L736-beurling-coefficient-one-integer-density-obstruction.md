# Lemma 736: L735's coefficient-1 defect excludes the tested integer-count remainder

## Hypotheses

Let P be any discrete system supplied by L735. Its generalized integers
G are the free commutative semigroup on its prime indices, with
norm |g| the product of the corresponding real prime powers. Distinct
formal exponent vectors remain distinct, including when norms coincide.
The norm is locally finite, the unit has norm 1, and every other element
has norm greater than 1. Define

    N(x)=#{g in G: |g|<=x},
    psi(x)=sum_(g in G, |g|<=x) Lambda(g),                 x>=1,

where Lambda is log p_j on each positive formal power of generator j
and zero on other elements, including the unit. All upper endpoints
are included. In particular N(1)=1 and psi(1)=0. The audited input from
L735, with b=3/4 fixed, is

    psi(x)=x-x^b+O(sqrt(x)log x)                  as real x->infinity. (1)

The assertion being tested is the existence of fixed constants
kappa>0 and 0<=theta<b such that

    N(x)=kappa x+O(x^theta)                     as real x->infinity. (2)

It is a hypothetical added assertion, not an input established by L735.

## Conclusion

No such kappa and theta exist. Thus (1) for L735's system cannot coexist
with (2), including theta=0. The contradiction is local: (2) would make
the same Beurling zeta function holomorphic at b, whereas (1) would
force its negative logarithmic derivative to have residue -3/4 there.
A holomorphic function's corresponding residue is a nonpositive
integer, the negative of its zero order.

This is a REPRODUCTION specialization of the inspected Mellin,
continuation and integer-order inputs. It identifies integer-count
structure absent from the coarse countermodel; no result beyond the
checked literature is claimed. The separate conceptual audit passed on
2026-11-04 (step 258), with no mathematical repair. Nothing is asserted at theta=b or
for weaker integer-count estimates. In particular this does not prove
a precise remainder for N, locate an actual zeta zero, exclude arbitrary
zeros, or prove an ordinary-prime prefix bound or actual-Xi sign.

## Proof

### Imported results and the reason for this specialization

Use Sz. Gy. Révész, *A Riemann-von Mangoldt-type formula for the
distribution of Beurling primes*,
[arXiv:2110.11463, requested-v1 PDF](https://arxiv.org/pdf/2110.11463v1),
Definition 1.1, (1.2)–(1.5) and its endpoint footnote, printed p. 2;
Lemma 2.1, (2.2),(2.4) and proof, printed pp. 4–5. For a locally finite
normed free semigroup, the bound
|N(x)-kappa(x-1)|<=A x^eta (x>=1), kappa,A>0, 0<eta<1,
gives meromorphic continuation of its zeta to Re(s)>eta, with only a
simple pole at 1. The source's lower Stieltjes endpoint is 1-minus,
so its unit atom is included. Version qualification: the requested-v1
URL inspected on 2026-11-04 serves a 29-page PDF with a v2 footer;
the cited pagination and equations identify the inspected manuscript.

For the Euler product and logarithmic derivative use Révész,
*Oscillation of the remainder term in the prime number theorem of
Beurling, caused by a given zeta-zero*,
[arXiv:2202.01837v3](https://arxiv.org/pdf/2202.01837v3), Section 1,
(1)–(7), pp. 1–3, including footnote 1. Formal multiplicities agree
with those above. Section 7, pp. 17–18, Mellin paragraph and (52)–(54),
provides the inspected power-transform comparison; its constructed
rational factorization is not an identity imported for our system.

Use the standard identity theorem for meromorphic functions and Taylor
zero order, as recorded in [NIST DLMF 1.10(i),(ii)](https://dlmf.nist.gov/1.10),
especially (1.10.1) and the zero-multiplicity definition. The equivalent
logarithmic-derivative count is [DLMF (1.10.9)](https://dlmf.nist.gov/1.10.E9).

The prior assessment found no exact coefficient-1 necessity theorem to
import. What follows verifies only its specified difference: the
normalization in (2), theta=0, exact endpoints, analytic error transform,
and common continuation before the local residue comparison. It does
not reprove the discretization or a global explicit formula.

### Matching Axiom A, including the zero exponent

Suppose (2) holds, and fix

    eta=(theta+b)/2.

Then 0<eta<b<1 and theta<eta, including when theta=0. Extend the
eventual estimate in (2) to all x>=1: on a fixed interval [1,X_0],
local finiteness bounds N(x) by N(X_0), and x^theta>=1. Thus for
some finite C_N,

    |N(x)-kappa x|<=C_N x^theta                 for every x>=1.

For R_N(x)=N(x)-kappa(x-1) we consequently have

    |R_N(x)|<=C_N x^theta+kappa<=(C_N+kappa)x^eta.      (3)

Taking A>=max{1,C_N+kappa} verifies the source hypotheses with the
strictly positive exponent eta. In particular the source applies to
theta=0 without extending its theorem to an excluded endpoint.
Denote its continuation by Z. It is holomorphic at b and meromorphic
on Re(s)>eta with its only pole at 1.

### The same zeta, with the unit and all endpoints retained

For any real X>=1 and complex s, finite summation of

    |g|^(-s)=X^(-s)+s integral_(|g|)^X t^(-s-1)dt

over |g|<=X gives

    sum_(|g|<=X) |g|^(-s)
      =N(X)X^(-s)+s integral_1^X N(t)t^(-s-1)dt.       (4)

For the unit, the right-hand contribution is
X^(-s)+s integral_1^X t^(-s-1)dt=1. An atom at X has zero
integral but keeps its X^(-s) term. Colliding norms contribute once
per formal element to both sides. No atom is lost in (4).

Equation (2) implies N(x)=O(x), so (4), first with real s>1,
proves absolute convergence of the zeta series for Re(s)>1. It is
locally uniformly convergent there by domination with a fixed real
exponent greater than 1. The boundary in (4) tends to zero, and

    zeta_P(s)=s integral_1^infinity N(x)x^(-s-1)dx
      =kappa/(s-1)+s integral_1^infinity R_N(x)x^(-s-1)dx,
                                                    Re(s)>1. (5)

Here s integral_1^infinity (x-1)x^(-s-1)dx=1/(s-1).
By (3) the last integral is holomorphic on Re(s)>eta: on a compact
set its integrand and s derivative are dominated by a constant times
x^(-1-delta)(1+log x) for some delta>0. This verifies directly that
the source continuation in (5) is of the same zeta series, with no
extra unit or endpoint correction. This normalization check, rather
than a different choice of zeta, is the purpose of (4)–(5).

The imported Euler product is therefore applicable in Re(s)>1:

    zeta_P(s)=product_j (1-p_j^(-s))^(-1),
    -zeta_P'(s)/zeta_P(s)=sum_g Lambda(g)|g|^(-s).       (6)

For clarity, the convergence hypotheses also hold at this exact
half-plane: the prime sum is bounded by the absolutely convergent
integer sum; p_1>1 keeps every factor away from its geometric-series
singularity on Re(s)>=1+epsilon. The product is nonzero there.
The logarithmic-derivative sum is absolutely locally uniformly
convergent because (1) gives psi(x)=O(x), by the weighted version of
(4). These checks justify using (6) with the formal multiplicities
and show that Z is not identically zero.

### Analytic remainder of the psi transform

Put E(x)=psi(x)-x+x^b for all x>=1. On any fixed compact interval
E is bounded by local finiteness, and E(1)=0. Combining this with
(1), enlarge a constant to obtain

    |E(x)|<=C_E sqrt(x)log(2x)                  for every x>=1. (7)

The factor log(2x)>0 avoids an artificial small-x restriction. Define

    H(s)=s integral_1^infinity E(x)x^(-s-1)dx,
                                                    Re(s)>1/2. (8)

For any compact K in this half-plane, let
delta=min_(s in K)(Re(s)-1/2)>0 and M=max_(s in K)|s|.
The integrand is bounded in absolute value by
M C_E x^(-1-delta)log(2x), whose integral is

    M C_E (log 2/delta+1/delta^2)<infinity.             (9)

For its s derivative use
C_E x^(-1-delta)log(2x)(1+M log x), also integrable.
Such domination on compact neighborhoods proves that H is holomorphic
throughout Re(s)>1/2, including at b. This argument does not require
absolute convergence of the Stieltjes transform of dE in that region.

Multiplying the finite identity used in (4) by Lambda(g) and summing
gives, with no lower endpoint term since Lambda(unit)=psi(1)=0,

    sum_(|g|<=X) Lambda(g)|g|^(-s)
      =psi(X)X^(-s)+s integral_1^X psi(x)x^(-s-1)dx.   (10)

Equality atoms and colliding norms are retained exactly as in (4).
For Re(s)>1 the boundary vanishes by psi(x)=O(x); the absolute
convergence already checked permits passage to infinity. Substituting
the exact equality psi(x)=x-x^b+E(x), valid even on the initial
interval, gives

    -Z'(s)/Z(s)=s/(s-1)-s/(s-b)+H(s)
               =1/(s-1)-b/(s-b)+H(s),                Re(s)>1. (11)

The two constant terms in the second equality cancel. Equivalently,
the smooth combined main term x-x^b vanishes at 1; there is no missing
lower-endpoint constant. Compact deviations are included in E and
hence in the analytic H, not omitted as an asymptotic substitution.

### Common continuation and the integer-order contradiction

Let alpha=max{eta,1/2}<b and D={s: Re(s)>alpha}. On this connected
domain, Z is meromorphic and not identically zero, so -Z'/Z is
meromorphic. The right-hand side of (11) is meromorphic on D by
(8), with possible poles only at 1 and b. They agree on the open
set Re(s)>1. The meromorphic identity theorem therefore extends
(11) to D. It does not require assuming Z is zero-free in D or
choosing a branch of log Z.

Choose a sufficiently small disk about b contained in D and avoiding
1. Since Z is holomorphic there and not identically zero, Taylor's
theorem gives an integer m>=0 and a holomorphic h, nonvanishing on
a possibly smaller disk, such that

    Z(s)=(s-b)^m h(s).

The case m=0 includes Z(b)!=0. On the punctured disk,

    -Z'(s)/Z(s)=-m/(s-b)-h'(s)/h(s).

Its residue at b is -m. In (11), H and 1/(s-1) are holomorphic
at b, while -b/(s-b) has residue -b=-3/4. Equality of the
meromorphic functions forces m=3/4, impossible for an integer m.
This contradiction disproves (2) for every fixed kappa>0 and
0<=theta<3/4. It uses the residue only after both continuations
and their common origin have been justified.

The original coarse bound of L735 is not an input to this argument
and is not refuted. Its simultaneous coefficient-1 defect and that
bound remain valid. What fails is adding (2) to that same system.
The argument uses no property of ordinary primes or actual Xi;
upper-prefix estimates, scalar anchors, complementary residuals and
all-degree mixed positivity remain independent unresolved claims.

### Separate conceptual audit — step 258

The audit reuses the approved source scope in
`drafts/literature/2026-11-04-beurling-integer-density-audit.md`
and the previously inspected primary statements and proof cases cited
above. L735 supplies the formal system, local finiteness and precisely
(1); its coarse convolution estimate is not used. No construction,
source manuscript or stronger integer-count theorem is being re-audited.

**Counting convention and the positive source exponent.** For each
fixed pair in (2), theta<eta<b and eta>=3/8>0. Enlarging the constant
on [1,X_0] is legitimate because there are finitely many formal elements
there and x^theta>=1. Adding kappa to change kappa*x into kappa*(x-1)
is absorbed by x^eta>=1. Thus (3) verifies the source's strictly positive
exponent hypothesis even at theta=0, with no uniformity in theta or
kappa claimed. Every nonunit norm is greater than 1; no extra lower
atom occurs. For X=1, (4) reads 1=1, and (10) reads 0=0. At an upper
atom the associated integral is zero while the boundary term retains
that atom. Distinct exponent vectors with equal norms are summed
separately throughout, as required by the free-semigroup Euler product.

**Identity of the analytic function.** N=O(x) proves absolute and compact
uniform convergence of the same integer series on Re(s)>1. For a compact
subset there, choose sigma_0>1 below every real part. The sum of
p_j^(-sigma_0) is finite, and |p_j^(-s)|<=p_1^(-sigma_0)<1.
Consequently the logarithms of the Euler factors converge normally:
their absolute sum is bounded by
sum_j p_j^(-sigma_0)/(1-p_1^(-sigma_0)). Finite products enumerate formal
integers, and absolute convergence permits their limit. This verifies
both equality with the series and nonvanishing. The weighted identity
(10), with psi=O(x), likewise gives normal absolute convergence of the
logarithmic-derivative series. Thus no hidden factor, distinct choice
of zeta or unproved logarithmic branch is used in (6). The integral of
x-1 in (5) is exactly 1/(s-1) after multiplication by s, and the unit
is already included through (4). The R_N integral is holomorphic on
Re(s)>eta, so the sole possible pole in that half-plane is at 1;
its residue is the nonzero kappa. This is the imported continuation's
normalization, not a new continuation theorem.

**Remainder and common domain.** The global estimate (7) is valid on
the initial interval as well as at infinity: local finiteness bounds
psi there, and sqrt(x)log(2x) is positive for x>=1. For each compact
K in Re(s)>1/2, both the majorant in (9) and its derivative majorant
are integrable. Explicitly the latter has integral at most

    C_E [log(2)/delta + 1/delta^2
         + M*(log(2)/delta^2 + 2/delta^3)].

This checks differentiation under the ordinary integral on compact
neighborhoods, including a neighborhood of b. It makes no assertion
about absolute convergence of the Stieltjes integral of dE there.
The weighted finite identity proves (11) first in Re(s)>1 with
vanishing boundary psi(X)X^(-s); both compact endpoint deviations and
all equality atoms remain in E. The constants in s/(s-1)-s/(s-b)
cancel, giving exactly residue -b at b. Since alpha=max(eta,1/2)<b,
the connected domain D contains both the original half-plane and an
open disk around b. Both sides of (11) are meromorphic on all of D,
even at possible zeros of Z. Their identity therefore does not depend
on the connectedness of a domain with those zeros removed.

**Zero order and verdict.** Z is holomorphic near b and is not identically
zero, as proved in the Euler-product half-plane. Hence its Taylor order
at b is finite and integral, and a smaller disk makes h nonvanishing.
For m=0 the residue of -Z'/Z is zero; for every positive integer m it
is -m. Neither equals -3/4. The analytic H and the pole term at 1
cannot change this local residue. This contradiction holds for every
stated fixed pair, including theta=0 and every theta strictly below b.
At theta=b the source-exponent construction would no longer place b
inside the continuation domain; no endpoint extension is asserted.

All checks pass. The audit validates the existing REPRODUCTION
specialization with unchanged conclusion and mathematical inputs.
It supplies no quantitative N remainder, no new literature theorem and
no ordinary-prime or actual-Xi sign. In particular an integer-order
obstruction to this coefficient-1 model is not an exclusion of genuine
off-line zeros, whose logarithmic derivatives already have integer
residues. The coarse diagnostic remains valid at its original scope.

## Mathlib

Full matching specialization not checked; availability is unknown.
The supporting ingredients are finite partial summation, dominated
holomorphic parameter integration, the meromorphic identity theorem
and integer Taylor zero order. No exact Mathlib declaration or absence
claim is asserted. The source results and their qualifications are
given above; this proof asserts no formal verification.
