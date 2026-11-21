# Corollary C034p: a positive common-base quotient has a strict Laplace error floor

## Hypotheses

Retain C032j's qualified actual-zero laws and precisely C033i's residual,
also used in C033l. Put X=[0,infinity), S=[1,2], I=[1,3/2], and

    L(dt)=ell_1(t)dt, P=L restricted to I, m=P(X),
    R=L restricted to (0,infinity)\I,
    B_1(s)=integral (1-exp(-s*t)) dL(t),
    B_P(s)=integral (1-exp(-s*t)) dP(t),
    B_R(s)=integral (1-exp(-s*t)) dR(t).

Here ell_1 is positive and Borel, integral min(1,t)dL(t)<infinity,
0<m<infinity, and nu_1 and mu are Borel probabilities on X with
zero drift and killing and transforms

    khat_1(s)=exp(-B_1(s)), muhat(s)=exp(-B_R(s)), s>0.

The exact density is ell_1(t)=H(t/(1+4*t))/(t*sqrt(1+4*t)),
where H(u)=sum_(rho in Z+) exp(-u*z_rho^2) and
z_rho=gamma_rho-i*(beta_rho-1/2). Retain the actual divisor,
conjugation and multiplicity conventions, exclusion of ordinate zero,
strict strip |beta-1/2|<1/2, gamma>14, counting
N(T)=O(T log(T+2)), verified zeros through100 and retained real zero
in (14,15), reciprocal-square tail, heat positivity, separate fixed-j
heat-error qualifications through2, Gaussian half-variance convention,
and both fixed-v1 preprint qualifications inherited by C033l. Neither
the preprints nor the finite-zero data are independently certified here.
Some inherited inputs are stronger than this elementary comparison needs.

Let lambda range over every Borel probability on X, and set
q_lambda=nu_1*lambda. There is no width representation, density,
moment, infinite-divisibility or zero-atom exclusion imposed on lambda.
No order between different width densities is assumed.

## Conclusion

The finite canonical quantity

    Delta=exp(-B_1(1))*(exp(B_P(1))-1)
         =muhat(1)-khat_1(1)

is strictly positive. For every such lambda,

    sup_(s in S) |muhat(s)-Laplace(q_lambda)(s)| >= Delta > 0.   (1)

In particular the infimum of these uniform errors over all lambda
is at least Delta. At the single observation s=1 the infimum of
the absolute errors is exactly Delta, attained by lambda=delta_0.
No equality for the uniform infimum is asserted, and no numerical
or effective lower bound for Delta is supplied.

Thus a correction constrained to a positive mass-one quotient after
nu_1 cannot approximate this exact residual with uniform Laplace error
less than Delta on S, even if the quotient is not constrained to a
width span. Applying this obstruction to a width construction requires
proving that its corrected output equals nu_1*lambda with lambda>=0
and lambda(X)=1. Output positivity alone does not establish that premise.
This does not decide the full output-positive signed-width cone,
span-preserving correction by signed quotients, moments, full odd
cancellation, signed height, actual-Xi realization or RH.

## Proof

Reuse SPECIALIZE assessment1898, separately approved1899, for precisely
this single-observation test. For positive half-line convolution
transforms import Ante Mimica, *Laplace transform*, Dresden course,
27 April-1 May2015, [Proposition1.4(iv), pp6-7, including its convolution
proof](https://web.math.pmf.unizg.hr/~amimica/lt.pdf). The hypotheses are
positive Borel half-line measures with finite transforms at positive
arguments. They hold for nu_1 and lambda because both have mass one
and 0<exp(-s*u)<=1 on X. Their convolution is also a probability.
This general transform theorem is imported, not reproved.

The existence and exact transform of mu are already proved in C033i
using Jean Bertoin, *Subordinators, Levy processes with no negative
jumps, and branching processes*, Maphysto2000,
[Theorem1.2(ii), pp7-8; finite-activity discussion p9](https://www.maphysto.dk/oldpages/events/LevyBranch2000/notes/bertoin.pdf).
The residual Levy measure R is positive with integral min(1,t) finite;
zero drift and killing give exactly exp(-B_R). No finite total mass
of R is assumed. We reuse this identification rather than reconstruct
the law or its signed inverse. The remaining work is the unevaluated
comparison and its quantifier over all positive quotients.

For t>0, 0<=1-exp(-t)<=min(1,t). Hence B_1(1) and B_R(1)
are finite and nonnegative. The decomposition L=P+R is an equality
of positive measures; integration of this nonnegative integrable
function therefore gives

    B_1(1)=B_P(1)+B_R(1).                                (2)

This involves no subtraction of infinite total Levy masses. On I,
1-exp(-t)>=1-exp(-1)>0. Consequently

    0<(1-exp(-1))*m <= B_P(1) <= m < infinity.             (3)

Equations (2)-(3) and the retained transforms yield

    muhat(1)=exp(-B_R(1))
            =exp(-B_1(1))*exp(B_P(1)) > exp(-B_1(1))>0.

Thus Delta has the stated exact expression and is strictly positive.
It is finite, since both terms in its difference expression belong
to (0,1]. This comparison needs no numerical heat estimate or moment.

For any allowed lambda, bounded positive integration gives

    0<lambdahat(1)=integral_X exp(-u)dlambda(u)<=1.

The strict lower bound follows, for example, because the increasing
sets [0,n] cover X: one has positive lambda mass for some n and its
contribution is at least exp(-n)*lambda([0,n])>0. Only the upper
bound is needed. The cited convolution theorem gives

    Laplace(q_lambda)(1)=khat_1(1)*lambdahat(1)<=khat_1(1).

It follows for every lambda, without compactness or a restriction
to atomic measures, that

    muhat(1)-Laplace(q_lambda)(1)>=muhat(1)-khat_1(1)=Delta.

This difference is positive, so its absolute value is at least Delta.
Since 1 belongs to S, the supremum in (1) is at least that absolute
value. All transforms on S lie in [0,1], so the supremum is finite.
Taking the infimum preserves the uniform lower bound. For lambda=delta_0,
lambdahat(1)=1, giving equality for the single-observation error only.
The atom at zero is explicitly allowed; no endpoint mass is dropped.

C033j's signed factors and C034n's mass-one affine approximation are
contrasts, not inputs to this inequality. They do not require positive
quotients. In particular C033i's signed inverse has a positive output,
so the implication from output positivity to quotient positivity cannot
be inserted here. We have stopped the sufficient positive-quotient
construction class for this residual, not the larger positive-output
problem. This is a known-tool specialization classified REPRODUCTION,
not a claim of mathematical novelty or an RH candidate.

### First application audit1902 — 20 November 2026

Verdict: the strict margin, all-probability quantifier and subclass
obstruction pass under unchanged SPECIALIZE assessment1900, separately
approved1901. This is a REPRODUCTION audit of the application of the
cited tools. It supplies no stronger inequality, new theorem beyond
the sources checked, or independent certification of the external
preprints and zero data. No mathematical repair is needed.

1. **Exact law and finite restricted mass.** C032j at sigma=1 gives
   precisely the displayed ell_1, a positive Borel Levy density with
   finite integral of min(1,t), and nu_1 with zero drift and killing.
   C033i uses exactly I=[1,3/2], not a changed restriction. Its proof
   gives m<=integral min(1,t)dL<infinity. For strictness, the measurable
   sets {t in I: ell_1(t)>=1/k}, k>=1, cover I. Since I has positive
   Lebesgue measure, one such set has positive measure; hence m>0.
   C033i identifies the residual probability with the restriction R
   and exponent B_R. C033l fixes the same mu and normalization; its
   capped separation theorem is not needed for this inequality. All
   inherited actual-divisor, conjugation, multiplicity, strip, counting,
   finite-height, tail, fixed-j heat, half-variance and fixed-v1
   qualifications remain assumptions of this audit.

2. **Finite split and strict margin.** For every t>0,
   0<=1-exp(-t)<=min(1,t). Thus all three exponents at 1 are finite
   nonnegative integrals. The positive restriction identity L=P+R
   gives B_1(1)=B_P(1)+B_R(1) without subtracting infinite masses.
   Since t>=1 on I, B_P(1)>=(1-exp(-1))*m>0, while B_P(1)<=m.
   In particular exp(-B_1(1)) is strictly positive; it is not a
   possibly vanishing limiting transform. Substitution gives exactly

       muhat(1)-khat_1(1)
         =exp(-B_1(1))*(exp(B_P(1))-1)=Delta>0.

   Both transforms are in (0,1], so Delta is finite. This needs no
   effective estimate of m or Delta and no heat-error differentiation.

3. **Every probability and the closed endpoint.** Any Borel probability
   lambda on X has finite transform at 1, bounded above by its mass 1.
   It is strictly positive: X is the union of [0,n], one of those
   sets has positive lambda mass, and exp(-u)>=exp(-n) there.
   The cited positive-measure convolution theorem applies to nu_1
   and lambda. Their convolution has mass 1 by positive product
   integration. Hence its transform at 1 is at most khat_1(1),
   and the signed difference from muhat(1) is at least Delta.
   This applies without a density, moments, finite support or
   infinite divisibility of lambda, and includes lambda({0})>0.
   Taking the absolute value preserves the inequality because this
   difference is positive. Since 1 is in the closed interval S,
   taking the supremum on S and then the infimum over all lambda
   preserves the same positive bound. No optimizer, compactness or
   exchange of extrema is being assumed.

4. **Sharpness and the construction class.** Lambda=delta_0 gives
   equality at the single observation. This proves exactly the
   stated single-coordinate infimum; it does not bound the errors
   at other s from above by Delta or identify the uniform infimum.
   A width correction is excluded only if its output equals
   nu_1*lambda for a nonnegative mass-one lambda. C033j supplies
   signed factors, not that nonnegativity. C033i disproves positivity
   reflection on arbitrary signed half-line factors. C034n asserts
   affine approximation without output signs. These contrasts give
   no extension of the present stop to all positive signed-width
   outputs. No quotient inverse, width-order premise, span
   preservation, moment bound or unsmoothed Xi conclusion enters.

The canonical DAG inputs remain C032j/C033i/C033l; no new mathematical
input or edge was introduced. Retain the positive-quotient subclass
stop. The full positive-output question and the main RH gap remain open.

## Mathlib

Full matching coverage has not been checked and is unknown. Supporting
Laplace/convolution, positive-measure integration and exponential-order
APIs have not been assessed. No Mathlib result substitutes for the
qualified actual-zero inputs or the cited source theorem.
