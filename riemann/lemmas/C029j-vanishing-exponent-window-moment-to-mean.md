# Corollary C029j: vanishing-exponent window moment-to-mean comparison

## Hypotheses

Use C028d and C029i's actual family, with precisely their normalization:

    b_j=gamma_j/gamma_0,  b_0=1,
    P_d(x)=sum_(j=0)^d binom(d,j)b_j x^(d-j),
    Q_d(y)=P_d(y-b_1),
    f_d(y)=log|Q_d(y)|-d log|y|,  t_d(y)=f_d(y)/d.

Here d>=3 is an integer, gamma_0>0, and Q_d is monic of degree d.
Count roots with algebraic multiplicity. Define t_d by the displayed
formula off zero and the real roots of Q_d, and choose any finite values
on that finite null set. All integrals are Lebesgue integrals.

C028d gives t_d in L1(R). Fix a finite constant C from audited C029i,
independent of d, so that

    integral_R t_d(y)^2 exp(|t_d(y)|/4) dy <= C.             (1)

These are proved local inputs for the actual family. No RH,
real-rootedness, simplicity, exclusion of a root at zero, or sign of a
finite-window signed mean is assumed. For each real A>=1 set

    q=q_d=1/(4d),  L=L_(d,A)=2Ad,  W=[-Ad,Ad],
    I=integral_W t_d(y)dy,
    Z=Z_(d,A)=(1/L) integral_W exp(q t_d(y))dy.

The exponential is the quotient power |Q_d(y)/y^d|^(1/(4d^2))
almost everywhere, not the power 1/(4d).

## Conclusion

The number Z is positive and finite. In particular the real quantity

    E_(d,A)=(L/q)log Z-I

is defined, and for every integer d>=3 and real A>=1,

    0 <= E_(d,A) <= C/(8d).                                (2)

Thus the approved threshold holds with C_*=C/8, uniformly in both
parameters. The constant is finite and depends only on the actual
family through C029i; no effective numerical value is certified.
This is a standard Taylor/Jensen specialization, not a claim of a new
general concentration theorem. Independent audit1986 below accepts the
comparison under the stated input contracts.

## Proof

### Imported scalar results and applicability

Reuse assessment1982 as completed by source review1983. Its covered
target is exactly (2), including the prefactor L/q=8Ad^2. The primary
scalar inputs, whose statements and essential proofs were inspected in
that review, are:

* Roos and Seeger, *Analysis: Foundations and Selected Topics*, revision
  30 October 2026, [Section 2.4, Theorem 2.49/(2.5), printed p.71](https://people.math.wisc.edu/~aseeger/book/Real_Analysis_Vol_1.pdf):
  Taylor's formula with integral remainder for a C^(n+1) function on
  an interval containing a and a+h. Both signs of h are included.
* Cover and Thomas, *Elements of Information Theory*, first edition
  (1991), [Section 2.6, Theorems 2.6.1-2.6.2, printed pp.24-26](https://sites.stat.columbia.edu/liam/teaching/neurostat-spr11/papers/EM/Cover%26Thomas-Ch2.pdf):
  Jensen's inequality for a convex function on a probability space.
  We verify integrability of both the statistic and its exponential.
* NIST DLMF, [Section 4.5(i), equation (4.5.4)](https://dlmf.nist.gov/4.5.E4):
  log x<=x-1 for every real x>0.

No general theorem is reproved. The necessary specialization is to an
unbounded logarithmic statistic, a changing uniform probability measure,
and the full growing L/q factor. The cited inputs alone do not state
the actual-family uniform estimate.

### Integrable remainder and positive finite moment

Fix d and A in the stated ranges. Write t=t_d. C028d gives I finite
and integral_W |t| finite. At every point where t is finite, apply the
imported Taylor formula to the scalar function exp at a=0, n=1,
h=q t. Its C2 hypothesis holds on all of R. This gives

    exp(q t)=1+q t+r_q(t),
    r_q(t)=q^2 t^2 integral_0^1 (1-s)exp(s q t)ds.

The formula requires no smoothness of y->t(y). Since 0<q<=1/12<1/4,

    0<=r_q(t)<= (q^2/2)t^2 exp(q|t|)
               <= (q^2/2)t^2 exp(|t|/4).                   (3)

This holds almost everywhere; the finite representatives at the
exceptional points are harmless as well. The right side is integrable
by (1). In particular

    exp(qt)<=1+q|t|+(q^2/2)t^2 exp(|t|/4)

is an integrable upper bound on W, whose length is L<infinity.
The moment integral is therefore finite. Its integrand is positive
almost everywhere on W, and W has positive measure, so Z>0.
This establishes both prerequisites for the later logarithm inequality.

All singularities are retained. For a nonzero real root r of
multiplicity m, local factorization gives

    t_d(y)=(m/d)log|y-r|+O_d(1).

Near zero, if its multiplicity as a root of Q_d is m (including m=0),
the corresponding expression is

    t_d(y)=(m/d-1)log|y|+O_d(1).

Thus the exponential has a nonnegative power q m/d at r!=0,
and exponent q(m/d-1)>=-q>=-1/12>-1 at zero. These local checks
include m=d and all repeated roots. They corroborate finiteness but
provide no uniform constants; the uniform estimate comes exclusively
from the complete C029i bound in (1). No neighborhoods are removed,
and no separation of roots is assumed.

Let R=integral_W r_q(t(y))dy. By (1) and (3),

    0<=R<=q^2 C/2,
    Z=1+(q/L)I+R/L.                                       (4)

All terms are finite, so integrating the Taylor identity uses ordinary
linearity of integrals, with no exchange of an infinite expansion or
any limit in d or A.

### Lower and upper comparisons, retaining the window factor

Equip W with probability measure dy/L. The random variable q t is
integrable and its exponential is integrable by the preceding argument.
Jensen's inequality for exp therefore gives

    exp(q I/L)<=Z.

Take logarithms and multiply by the positive number L/q. The result
is I<=(L/q)log Z, which is the lower bound in (2). No sign of I or
of Z-1 was used.

For the upper bound apply log Z<=Z-1, valid because 0<Z<infinity.
Use the exact identity (4) before estimating its remainder:

    E_(d,A)=(L/q)log Z-I
       <=(L/q)(Z-1)-I
        =(L/q)((q/L)I+R/L)-I
        =R/q
       <=q C/2
        =C/(8d).

In particular the normalized remainder is bounded by q^2 C/(2L)
before multiplication by L/q=8Ad^2; the entire factor is paid.
The constant in (1) is common to all d, and no estimate above depends
on A except through factors that cancel exactly. This proves (2) for
all the required d,A, not merely at fixed A or after an ordered limit.

### Remaining gap and scope

The achieved error tends to zero uniformly over A>=1 as d grows.
It establishes no upper bound tending to zero for (L/q)log Z itself
or for I. C028d's full-line identity remains

    integral_R t_d(y)dy=pi H_d/d.

Consequently the signed upper payment, C028b's H_d=o(d), compact
nonreal-divisor exclusion and actual-Xi mixed positivity are still
open. No limit interchange is asserted. C029f's fixed-exponent loss
and the fixed-exponent paired source limit remain within their stated
scopes; neither is contradicted or used as an input. No claimed
resolution of RH is being made.

### Independent audit1986 (20 November 2026)

Replay the whole proof under unchanged SPECIALIZE assessment1984,
separately approved1985. C028d and audited C029i use exactly the same
actual centered monic polynomial, normalization t_d=f_d/d, degrees
d>=3 and finite exceptional set as this statement. C028d supplies L1
at each degree; C029i supplies one finite C for all those degrees.
The latter input is reused, not re-audited. No correction to the
comparison, its constants or its mathematical dependencies is needed.

For any fixed finite A>=1, W has length 2Ad>0. The logarithmic statistic
is measurable and finite almost everywhere, and finite choices on the
exceptional set do not change its integrals. Local factorization gives
the stated coefficients m/d at a nonzero root and m/d-1 at zero.
For every multiplicity 0<=m<=d the latter exponential exponent is at
least -q>-1; when m=d the logarithmic singularity cancels. The former
exponent is nonnegative. Thus neither an origin root nor repeated roots
invalidate the local checks. These checks supply no uniform root
separation or domination; those are not substituted for (1).

Taylor's scalar formula applies for either sign of q t. Its remainder
is nonnegative, with integral R<=q^2 C/2, since q<=1/12<1/4. On W,
the other two terms 1 and q t are integrable. Hence the exponential is
integrable before the identity Z=1+qI/L+R/L is integrated. It is positive
almost everywhere on a set of positive measure, giving Z>0 independently
of that identity. Jensen therefore applies to q t with probability
measure dy/L, and log Z<=Z-1 has its positive finite argument. Neither
application requires I>=0 or Z>=1. The exponent of the polynomial
quotient is q/d=1/(4d^2); changing it would change this claim.

Explicitly the normalized error satisfies

    R/L <= q^2 C/(2L) = C/(64 A d^3).

Multiplying the exact identity by L/q=8Ad^2 cancels qI/L against I,
and multiplies this entire normalized error by 8Ad^2. This gives
C/(8d), while Jensen gives the lower bound zero. This verifies uniformity
for all finite real A>=1 and integer d>=3 simultaneously. No infinite
series is integrated, no limit is exchanged and no numerical check is
used. The accepted result is local verification of the existing standard
specialization; it adds no signed upper estimate or new theorem beyond
the checked scalar sources and local inputs. The remaining gaps stated
above persist, as do stop1963, source-limit1966 and closure1982 within
their scopes. Full matching Mathlib coverage remains unchecked.

## Mathlib

Not checked. Full matching theorem availability is unknown. Standard
Taylor remainder, Jensen, logarithm inequalities and Lebesgue
integration would be supporting results, not evidence that this exact
actual-family specialization is formalized. No absence or formal
verification is asserted.
