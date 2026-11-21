# Corollary C034o: exact positive range for the oriented two-width output

## Hypotheses

Retain exactly C032j/q/t/u's actual-zero Gaussian half-variance
normalization and external-input qualifications. In particular the
positive-ordinate actual divisor counts multiplicities, retains
conjugate pairs, excludes ordinate zero and satisfies the strict strip,
gamma>14 and counting inputs. Keep verification through height100,
the retained real zero, reciprocal-square tail, heat positivity and
separate fixed-j error inputs through order2 used in C032t, and both
fixed-v1 preprint qualifications. Their source-wide correctness and
finite-zero data are not independently certified here.

On X=[0,infinity), C032j supplies probability laws nu_1,nu_2 with
finite real exponents B_1(s),B_2(s) and transforms

    k_i(s)=integral_X exp(-s*u) dnu_i(u)=exp(-B_i(s)), s>0.

C032u supplies the positive finite measure Pi(dt)=D(t)dt on
(0,infinity), M=Pi((0,infinity)) in (0,infinity), and its probability
factor pi on X, with

    q=exp(-M) in (0,1), pi({0})=q, nu_2=nu_1*pi.

For a finite real a>=0 set eta_a=(1+a)delta_2-a*delta_1 on W=[1,2].
C032q defines its finite signed output
mu_a=nu_eta_a=(1+a)nu_2-a*nu_1. No density, finite moments,
RH, positivity of the profiles p_sigma, full J_eta=0, or unsmoothed
Xi realization is assumed.

## Conclusion

Under those qualifications,

    mu_a>=0 on every Borel set of X
       iff 0<=a<=q/(1-q)=1/(exp(M)-1).                    (1)

Every positive output in (1) has mass one. The endpoints are
mu_0=nu_2 and

    mu_(q/(1-q))=nu_1*((pi-q*delta_0)/(1-q)).              (2)

For each a>q/(1-q), a bounded continuous positive test exp(-s*u)
has strictly negative integral against mu_a for every sufficiently
large finite s. In particular, C032u's sufficient range is sharp
in this orientation. No assertion about the reverse orientation,
additional widths, the full positive-output approximation distance,
cancellation, moments, signed height or actual-Xi positivity follows.
This is a known-tools specialization (REPRODUCTION), not a claim of
novelty beyond the sources checked. Critical audit1897 passes under
exactly the retained qualifications; it does not certify those external
inputs independently.

## Proof

### Imported inputs and scope of the specialization

Reuse the unchanged SPECIALIZE assessment1894 and its inspected
source notes1552/1562/1565. The finite-activity construction is Jean
Bertoin, *Subordinators, Levy processes with no negative jumps, and
branching processes*, Maphysto2000,
[Theorem1.2, pp7-8, finite-activity case p9](https://www.maphysto.dk/oldpages/events/LevyBranch2000/notes/bertoin.pdf).
The convolution transform is Ante Mimica, *Laplace transform*,
Dresden2015,
[Proposition1.4(iv), pp6-7](https://web.math.pmf.unizg.hr/~amimica/lt.pdf).
C032u has already specialized these results to the actual laws,
checked finite positive Pi with zero drift and killing, identified
the factor on the entire closed half-line, computed its exact zero
atom and proved all-Borel positivity in the sufficient range.
None of those theorems or that construction is reproved here.

The remaining argument uses the standard Lebesgue dominated
convergence theorem for the finite positive measure pi and the
bounded signed integration identity of C032q. The sources do not
compute the necessary coefficient for this qualified actual pair;
this is the precise specialization performed below. Generic
mixture-proportion characterizations from notes1562/1565 are not
used as a substitute for its computation.

### Ratio limit and the necessary coefficient

For each finite s>0, k_1(s)=exp(-B_1(s)) is strictly positive,
because B_1(s) is finite and real. The existing positive
convolution identity therefore gives

    r(s):=k_2(s)/k_1(s)=integral_X exp(-s*v) dpi(v).       (3)

For every v in X, exp(-s*v) tends as s tends to infinity to
1_{\{0\}}(v); its value at v=0 stays one. The integrand is
bounded by the pi-integrable constant function one. Dominated convergence
against the probability pi proves

    lim_(s->infinity) r(s)=pi({0})=q.                    (4)

This includes the atom at zero and requires no density or moment
assumption. It does not divide two limiting transforms: the division
in (3) is performed only at finite s. Dominated convergence may
equivalently be applied along every sequence s_n tending to infinity,
which establishes the full real-parameter limit in (4).

Suppose mu_a is nonnegative on all Borel sets. For finite s>0,
f_s(u)=exp(-s*u) is bounded, continuous and strictly positive on X.
C032q's bounded integration identity, here just a two-term finite
sum, gives

    0<=integral_X f_s dmu_a
      =(1+a)k_2(s)-a*k_1(s)
      =k_1(s)*[(1+a)r(s)-a].                            (5)

Division by the strictly positive k_1(s), followed by (4), yields
q-a*(1-q)>=0. Since 1-q>0, this is a<=q/(1-q).

More explicitly, if a>q/(1-q), put
delta=a/(1+a)-q>0. By (4) there is a finite S such that for all
s>S, r(s)<q+delta/2<a/(1+a). Equation(5), without its initial
nonnegativity assumption, then gives integral_X f_s dmu_a<0.
These are actual finite-parameter witnesses to failure of positivity;
the argument does not claim an effective numerical value of S.

### Sufficiency, total mass and endpoints

For 0<a<=q/(1-q), import C032u's all-Borel positivity proof and
endpoint identity(2). For a=0, mu_0=nu_2 is already a probability.
For every finite a, C032q or direct integration of the constant one
gives mu_a(X)=(1+a)-a=1. Thus (1) and both endpoint assertions hold.
At the upper endpoint (4) makes the bracket in (5) tend to zero;
no strict limiting sign is asserted there. Its positivity comes
from C032u's positive residual measure, not from the Laplace tests.

The only necessity used is that a positive finite measure integrates
bounded nonnegative functions nonnegatively. No converse saying
that Laplace nonnegativity implies measure positivity is used.
The sharp range decides this pair only; all independent main-gap
requirements remain unresolved. ∎

### Critical audit1897 — 20 November 2026

The complete argument passes the unchanged SPECIALIZE scope of
assessment1895, separately source-approved in1896. This is local
validation of the existing classification, with no changed theorem,
new coefficient range or independent certification of the actual-zero
inputs. The inspected primary construction and transform proof cases
recorded in source notes1552/1562/1565 are reused. No general
compound-Poisson, uniqueness or dominated-convergence theorem is
reproved.

First check the exact imported measure identity, including its endpoint.
C032t supplies finite strictly positive M, and C032u applies the cited
finite-activity construction with jumps supported in (0,infinity) and
zero drift and killing. Every positive-jump convolution term of positive
order gives zero mass to {0}; only its zero-jump term contributes.
Consequently the comparison probability, not necessarily either original
law, has pi({0})=exp(-M)=q exactly. In particular 0<q<1 and
R=pi-q*delta_0 is positive of mass 1-q. C032u identifies nu_2=nu_1*pi
as finite positive Borel measures on the entire closed half-line by
finite-measure Laplace uniqueness. No atom is discarded. C032t's
sign and mass conclusion is used through this C032u factorization.

For finite s>0, the integrands defining B_1(s),B_2(s) are integrable
by the imported Levy-integrability input. Their exponents are finite
and real, so k_1(s)>0 and the convolution transform can legitimately
be divided by k_1(s). This gives (3) before any limit is taken, even
if k_1(s) tends to zero. Against the finite positive measure pi,
0<=exp(-s*v)<=1 and its pointwise limit on X is exactly 1_{\{0\}}.
The constant-one dominator is integrable. Lebesgue dominated convergence
along every sequence tending to infinity therefore proves the full
real-parameter limit (4). This step requires neither a density nor a
moment nor a positive atom of nu_1. It does not form a ratio of limiting
transforms.

C032q's bounded integration interface applies to exp(-s*u), a real
continuous function of norm one on X. For the two input atoms its
identity is simply the finite signed sum in (5); there is no infinite
width sum or unbounded-test exchange. If mu_a is positive on all
Borel sets, its integral is nonnegative. Division by k_1(s)>0 and
passage to the just-checked limit give (1+a)*q-a>=0, hence precisely
a<=q/(1-q), since 1-q>0. Conversely, for a above this threshold,
delta=a/(1+a)-q is strictly positive. The definition of the full limit
gives a finite S>0 with r(s)<q+delta/2<a/(1+a) for every finite
s>S. Equation (5), now used only as an equality for the signed measure,
then has strictly negative right side. These are legitimate bounded
positive witnesses, although no effective S or numerical M is supplied.
No converse from nonnegative Laplace tests to all-Borel positivity is
used.

Finally the sufficient direction is independent of that necessity test:
C032u's measure identity is
mu_a=(1+a)*(nu_1*R)+[q-a*(1-q)]*nu_1. Both terms are positive within
the stated interval. At a=0 the original definition gives nu_2; at
a=q/(1-q) the second coefficient is zero and the first is 1/(1-q).
Since R(X)=1-q, the displayed endpoint (2) is a probability convolution.
For every finite a the total mass of mu_a is exactly (1+a)-a=1.
The limiting bracket is zero at the upper endpoint and cannot itself
prove its sign; the positive residual supplies that sign. All divisions
and both endpoint substitutions are justified by 0<q<1.

No defect was found. This establishes the reliability of this qualified
pair obstruction, not progress beyond the known tools used to obtain it.
The reverse-order/one-jump and finite-mixture full-cancellation stops
are unaffected. Additional widths, positive-output approximation to the
exact residual, full cancellation, moments, signed height and actual-Xi
realization remain outside the audit. Full matching Mathlib coverage
remains unchecked and unknown.

## Mathlib

Full matching coverage for this qualified actual-law classification
has not been checked and remains unknown. The dominated-convergence,
finite-measure convolution and bounded-integration APIs have not been
assessed here. No formal theorem replaces the external fixed-v1
inputs or independently verifies the actual divisor/finite-zero data.
