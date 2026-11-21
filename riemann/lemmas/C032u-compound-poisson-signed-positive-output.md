# Corollary C032u: compound-Poisson comparison and a signed positive output

## Hypotheses

Retain exactly C032j and C032t's actual-zero normalization and external
input qualifications. In particular Z+ counts positive-ordinate zeta
zeros with multiplicity, z_rho=gamma-i*(beta-1/2), and

    H(u)=sum_(rho in Z+) exp(-u*z_rho^2),
    H_sigma(t)=H(t/(1+4*sigma*t))/sqrt(1+4*sigma*t),
    ell_sigma(t)=H_sigma(t)/t,
    B_sigma(s)=integral_0^infinity (1-exp(-s*t))*ell_sigma(t) dt.

C032j supplies Borel probability laws nu_sigma on X=[0,infinity)
with Laplace transforms exp(-B_sigma(s)), s>0, and no killing or
drift in these exponents. Use sigma=1,2. The actual divisor,
zero-ordinate exclusion, strip/counting, verified zeros through 100,
first-zero/tail and heat inputs, including the two fixed-v1 preprint
qualifications, are retained. Source-wide correctness and the finite
zero data are not independently certified here.

C032t, using C032s, supplies

    D(t)=ell_2(t)-ell_1(t)>0 for all t>0,
    M=integral_0^infinity D(t) dt in (0,infinity).

Use C032q's signed output convention on W=[1,2]:
nu_eta(A)=integral_W nu_sigma(A) deta(sigma), for Borel A in X.
There is no assumption of RH, positivity of p_sigma, a density of
nu_sigma, exponential moments, J_eta=0 or unsmoothed realization.

## Conclusion

There is a Borel probability pi on X such that, with q=exp(-M),

    pi({0})=q in (0,1),
    nu_2=nu_1*pi,
    nu_2(A)>=q*nu_1(A) for every Borel A in X.             (1)

For every real a satisfying

    0<a<=q/(1-q)=1/(exp(M)-1),                            (2)

the finite real signed width measure

    eta_a=(1+a)*delta_2-a*delta_1

has mass one, total variation 1+2*a and a strictly negative atom at
width 1. Its output

    nu_eta_a=(1+a)*nu_2-a*nu_1                            (3)

is a Borel probability measure. In particular the endpoint in (2)
is allowed, and gives

    nu_eta_a=nu_1*((pi-q*delta_0)/(1-q)).                 (4)

This is a sufficient coefficient range; its optimality is not claimed.
It establishes a genuinely signed input with positive output, under
the retained external inputs. The comparison and coefficient range
passed critical audit1561 under exactly these qualifications.
It neither asserts J_eta_a=0 nor
decides C032q's joint cancellation/positivity cone. It proves no
actual-Xi all-degree positivity or RH. This is a specialization of
known finite-activity probability results, not certified novelty.

## Proof

### Cited construction and its applicability

Reuse unchanged SPECIALIZE assessment1551 and its source-notes1552.
Import the finite-activity case of Jean Bertoin, *Subordinators, Levy
processes with no negative jumps, and branching processes*, Maphysto
2000 course, [Theorem 1.2, printed pp.7-8, and the finite-activity
case p.9](https://www.maphysto.dk/oldpages/events/LevyBranch2000/notes/bertoin.pdf).
With zero drift and killing, a finite positive Levy measure Pi of
mass M defines a compound-Poisson probability with Laplace transform
exp(-integral (1-exp(-s*t)) dPi(t)); its number of jumps at time one
is Poisson(M). The full relevant construction was inspected in the
reused source assessment. The conditional n-jump convolution formula
is also stated and proved in Steven P. Lalley, *Levy processes, stable
processes, and subordinators*, [Definition 5.1 and (5.2)-(5.4),
printed p.12](https://galton.uchicago.edu/~lalley/Courses/385/LevyProcesses.pdf).

For the convolution transform and uniqueness of finite positive
half-line measures import Ante Mimica, *Laplace transform*, Dresden
course, 27 April-1 May 2015, [Proposition 1.4(iv), pp.6-7, and
Proposition 1.8, pp.9-10](https://web.math.pmf.unizg.hr/~amimica/lt.pdf).
Only uniqueness is used, not an inversion formula at zero. The source
proof qualifications recorded in source-notes1552 remain applicable.

Here Pi(dt)=D(t)dt on (0,infinity) is a positive Borel measure, since
C032t gives positivity and continuity inherited from C032s. Its mass
M is finite and strictly positive. In particular
integral min(1,t) dPi(t)<=M, so Bertoin's Levy integrability hypothesis
holds. Zero drift and killing match C032j. These checks use the audited
actual difference; individual positivity of ell_sigma would not suffice.
No general compound-Poisson theorem is reproved. The remaining proof
checks the actual-law identification and coefficient range, which are
not supplied for this family by the general sources.

### Factorization and all-Borel domination

Let r=Pi/M be the probability measure on (0,infinity), considered as
a probability on X with no atom at zero. The cited construction gives

    pi=exp(-M)*sum_(n=0)^infinity (M^n/n!)*r^{*n},
    r^{*0}=delta_0.                                      (5)

This is an equality of positive measures; its weights sum to one.
For n>=1 a sum of n strictly positive jumps is strictly positive.
Thus (5) gives pi({0})=exp(-M)=q exactly, and

    R=pi-q*delta_0>=0,    R(X)=1-q.                      (6)

For s>0 the defining integrals B_1(s),B_2(s) are finite. Their
integrands are integrable by C032j, while D is integrable by C032t.
Consequently ordinary linearity of integrable functions gives

    B_2(s)-B_1(s)=integral_0^infinity (1-exp(-s*t))*D(t) dt.

The compound-Poisson transform and the cited convolution rule imply

    Laplace(nu_1*pi)(s)
       =exp(-B_1(s))*exp(-(B_2(s)-B_1(s)))
       =exp(-B_2(s))=Laplace(nu_2)(s).

Both nu_1*pi and nu_2 are finite positive Borel measures on X, so
finite-measure Laplace uniqueness identifies them on every Borel set.
In particular it retains any atom at zero. Distributing convolution
over the finite positive decomposition (6) now yields

    nu_2=q*nu_1+nu_1*R.                                 (7)

For every Borel A, (nu_1*R)(A) is the integral of
1_A(x+y) against the positive product measure nu_1(dx)R(dy).
It is nonnegative. This proves (1) on all Borel sets, not merely for
Laplace tests or distribution functions. No density is required.

### Signed coefficients and endpoint

The two input atoms have distinct widths, so their Jordan masses
are 1+a and a. Their difference has mass one and total variation
1+2*a, and eta_a({1})=-a<0. Its output (3) is precisely C032q's
setwise signed integral, here a finite sum. Substitution of (7) gives

    nu_eta_a=(1+a)*(nu_1*R)+[q-a*(1-q)]*nu_1.             (8)

The range (2) is nonempty because 0<q<1, and makes both coefficients
in (8) nonnegative. The masses in (8) sum to

    (1+a)*(1-q)+q-a*(1-q)=1.

Thus the output is a positive probability, including when the second
coefficient is zero. At that endpoint 1+a=1/(1-q), and (8) is (4);
R/(1-q) is a probability by (6). For example the strictly interior
choice a=q/(2*(1-q)) also works, with residual coefficient q/2>0.
No numerical estimate for M is necessary for either exact choice.

This completes the approved comparison and construction. The
identities used neither the full complex cancellation constraints
nor any exponential-moment extension. No such conclusion follows
from positivity of (8). The historical finite-width cancellation
obstruction and reverse-Levy-order stop remain intact. The separate
unsmoothed identification and main positivity gap also remain. ∎

### Critical audit1561 — 18 November 2026

The complete comparison passes under the unchanged SPECIALIZE
assessment1559. This audit reuses source-notes1552's inspected
finite-activity construction, convolution rule and finite-measure
uniqueness. It takes C032s/t's audited sign and integrability as
inputs; it does not recertify the finite-zero data or either entire
fixed-v1 preprint. The following checks concern precisely their
application here, rather than a new general probability theorem.

C032s makes D continuous and real on (0,infinity); C032t makes it
strictly positive there with finite integral M. Thus Pi is a positive
Borel measure of mass M>0 on the open positive half-line, with
integral min(1,t) dPi<=M. The cited construction applies with zero
drift and killing, matching the two exponents in C032j. Dividing
by M is legitimate. Each term r^{*n} for n>=1 gives zero mass to
{0}, because all n summands are strictly positive almost surely.
The n=0 term alone therefore gives pi({0})=exp(-M)=q, not merely
a lower bound. Nonnegative summation in (5) has mass one, so its
remainder R is positive with mass 1-q>0.

For every s>0, each function (1-exp(-s*t))*ell_sigma(t) is
integrable by C032j's Levy-integrability input. Also
|(1-exp(-s*t))*D(t)|<=D(t) is integrable. Subtracting the two
integrals is consequently ordinary integrable linearity, with no
subtraction of divergent total Levy masses. Its sign is B_2-B_1,
the exponent of pi. Multiplication of Laplace transforms therefore
gives nu_1*pi=nu_2, in the direction used in (7). Both sides are
positive finite measures on [0,infinity), so the cited uniqueness
theorem applies on that space. There is no restriction to (0,infinity)
that could lose an atom at zero, and no signed inversion formula or
exponential-moment hypothesis is used.

Convolution of the finite positive measures nu_1 and R is positive
on every Borel set, including arbitrary sets that contain zero.
Its mass is nu_1(X)*R(X)=1-q by integration of the constant one.
This verifies (7) and all-Borel domination, rather than only
inequalities for distribution functions or completely monotone tests.
The signed kernel formula in C032q reduces to the finite sum (3);
it requires no unbounded test function or interchange of moments.

For a>0 the distinct input atoms have disjoint supports, so their
Jordan masses really are 1+a and a. Substitution of (7) gives exactly
(8), whose residual coefficient is q-a*(1-q). The proposed range
0<a<=q/(1-q) is nonempty and finite since 0<q<1. Both terms in
(8) are positive measures within that range, and their total mass
is one by the displayed mass identity. At a=q/(1-q) the residual
coefficient vanishes and 1+a=1/(1-q); hence the output is precisely
the probability convolution in (4). This checks the equality case
without assuming that R has a density or excluding singular parts.

No defect, sharper range or new mathematical claim was found. The
DAG now records the directly used continuity input explicitly.
The conclusion is local
validation of the existing specialization. It imposes neither
J_eta=0 nor evenness, and it does not overcome the finite-mixture
obstruction, the continuum cancellation gap or Xi realization.

## Mathlib

Full matching coverage of this qualified actual-law comparison and
signed-width construction has not been checked and remains unknown.
No Mathlib theorem is used in place of the fixed-v1 inputs or the
cited finite-activity and Laplace-uniqueness theorems. Supporting
convolution/probability APIs have not been assessed in this step.
