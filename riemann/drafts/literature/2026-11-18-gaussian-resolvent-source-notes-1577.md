# Gaussian resolvent source review1577

18 November 2026. Literature-only checkpoint for assessment1576's exact
target. No new representation, estimate, lemma or mathematical program
has been derived. Source comparison is complete within the scope below.

Main gap: L030-L032/C032a actual-Xi all-degree positivity. The bounded
intermediate target is an alternative E_sigma evaluator on real widths
[1,2] and the closed disk |w|<=2. Its possible downstream use is the
unchanged variation-at-most-2 residual test1570; that leaves unrestricted
variation, full odd cancellation and unsmoothed realization unresolved.

Inspected C032m's Gaussian normalization, entire/removable proof and
audit; C032w's formula, evaluator and relevant audit; C032q's hypotheses
and cone conclusion; source-notes1572/1555; calculation1564's stated
inputs and tail; calculation1571 and stop1576. Reuse those source
assessments rather than reopening their external inputs. Narrow local
searches for Faddeeva/complex-erfc/Gaussian-resolvent/Fried-Conte in
C032 and Gaussian literature/attempt/history paths found only the new
continuation record. This is a scoped duplicate check, not novelty.

Primary sources now read: NIST DLMF 7.2.3, 7.4.3, 7.7.2, 7.7.6 and
7.12(i); Ivanov-Adkins (2023), Section3.1 and Figure2's three-case
contour explanation, printed p.10; Hasanalizade-Shen-Wong,
arXiv:2107.06506v1, Corollary1.2 and its complete proof, pp.2,15,
with N(T)'s definition p.1. Precise statements and comparison follow.

## Exact source statements and qualifications

**NIST DLMF**, Version1.2.8, released 15 September2026, Chapter7.
Read the displayed hypotheses and equations, rather than inferring
domains from the names of the functions. To avoid confusing the
notebook variable w with the special function, write W_F for the
source's Faddeeva function.

[7.7.2](https://dlmf.nist.gov/7.7.E2) states, for Im(z)>0,

    W_F(z)=(1/(pi*i))*integral_R exp(-t^2)/(t-z) dt
          =(2*z/(pi*i))*integral_0^infinity
                                exp(-t^2)/(t^2-z^2) dt.

This is the precise Gaussian Cauchy-transform input. Its stated domain
is not all complex z. [7.7.6](https://dlmf.nist.gov/7.7.E6) gives

    integral_x^infinity exp(-(a*t^2+2*b*t+c)) dt
      =(1/2)*sqrt(pi/a)*exp((b^2-a*c)/a)
                         *erfc(sqrt(a)*x+b/sqrt(a)),
    Re(a)>0, x real.

Here b,c are complex. This covers complex linear shifts of the
Gaussian primitive; it does not cover a denominator or a pole crossing.
No specialization to a zeta zero has been performed. Section7.7's
notes refer the Cauchy-transform formula to van der Laan-Temme (1984),
pp.185-186; that book was not read. The equation itself is imported
from DLMF, without reproof.

[7.2.3](https://dlmf.nist.gov/7.2.E3) defines
W_F(z)=exp(-z^2)*erfc(-i*z); Section7.2(i) states that both functions
are entire. [7.4.3](https://dlmf.nist.gov/7.4.E3) states
W_F(-z)=2*exp(-z^2)-W_F(z).
These supply entire continuation and reflection, not equality of
uncorrected real-line integrals in both half-planes.

[7.12(i)](https://dlmf.nist.gov/7.12.i), equation7.12.1 and its full
remainder paragraph, were read. The erfc asymptotics hold in
|arg(z)|<=3*pi/4-delta, delta>0. Its first-neglected-term bound is
stated for |arg(z)|<=pi/4; in the intermediate sector
pi/4<=|arg(z)|<pi/2 it has the additional csc(2*|arg(z)|) factor.
That factor gives no uniform estimate on the imaginary axis. Thus a
generic large-argument asymptotic is not a ready error bound for the
full requested disk. Real-variable inequalities in Section7.8 were
screened and are not used for complex arguments. Wider-sector proofs
in Olver are unread leads, unnecessary if the next attempt estimates
the original removable quotient instead.

**P.G. Ivanov and T. Adkins**, *An analytical form of the dispersion
function for local linear gyrokinetics in a curved magnetic field*,
J. Plasma Phys.89 (2023), 905890213,
[doi:10.1017/S0022377823000077](https://doi.org/10.1017/S0022377823000077),
[author/institution PDF](https://scientific-publications.ukaea.uk/wp-content/uploads/an-analytical-form-of-the-dispersion-function-for-local-linear-gyrokinetics-in-a-curved-magnetic-field.pdf).
Read Section3.1, equations(3.1)-(3.3), and Figure2's complete
three-case contour explanation, printed p.10. The real-line definition
requires Im(zeta)>0. Continuation to the boundary and lower half-plane
deforms the contour below the pole without crossing it. Consequently
an unchanged contour cannot simply be declared to have the same
continued value. Only this contour convention is used; the paper's
plasma approximations and two-dimensional branch formulas are irrelevant.
Its references identify Fried-Conte (1961); that book was not read,
and its catalog page is not theorem coverage. No residue formula is
derived in this review.

**E. Hasanalizade, Q. Shen and P.-J. Wong**, *Counting zeros of the
Riemann zeta function*, [arXiv:2107.06506v1, 14 July2021](https://arxiv.org/pdf/2107.06506),
Corollary1.2/(1.5), printed p.2:

    |N(T)-T/(2*pi)*log(T/(2*pi*e))|
      <=0.1038*log(T)+0.2573*log(log(T))+9.3675, T>=e.

Read N(T)'s positive-ordinate definition p.1, Section2's
N_Q(T)=2*N(T) argument-principle normalization pp.3-4, the entire
corollary statement and complete proof p.15. The normalization counts
multiplicity; RH is not assumed. The proof uses Theorem1.1/Table2
above 30,610,046,000 and the cited finite S(T) verification below it.
Neither that database nor the general theorem's full proof was audited
here. Import the named corollary with those source qualifications;
it supplies no individual coordinates. Retain the inclusive upper
endpoint in N(T), and handle cutoff-zero endpoints explicitly in any
subsequent tail summation. It provides an explicit counting input for
a future tail argument, not that argument itself. This review does not
assert that its bound improves the notebook's other counting estimates.

## Applicability comparison and bounded specialization

C032m retains |Im(z_rho)|<1/2, positive real ordinates >14,
multiplicities and real widths in[1,2]. The transform source has a
nonempty pole-free initial domain, but transferring it to complex
centres and the full w disk is still mathematical work. A permitted
approach is to establish the paired, subtracted identity first in a
safe domain and then justify continuation using C032m's entire
removable integral. Every contour displacement, residue, apparent
1/w term and origin limit must be accounted for. This is a proposed
specialization strategy, not a derived identity or proof of readiness
of an evaluator.

In particular the notebook integrates a removable combined quotient,
not a principal value or a chosen Landau contour. Those objects may
not be substituted for it. The even zero pair must preserve C032m's
factor1/2 and the complete off-line divisor. The paired Gaussian
numerator can be split into terms only with the relevant domination;
the separate constant subtraction has its own apparent singularity.
C032m's existing entire-integral theorem coverage is sufficient as
a tool, but its application must be checked for each new expression.

C032m's spatial envelope already gives integrability. Its displayed
bound(3) contains a fixed S_2 term, so it is not a decreasing truncation
certificate. Calculation1564's <10^-100 compact profile tail controls
neither the full spatial resolvent integral nor the unknown finite
divisor. The imported explicit count is an available tool to prove
a new effective spectral tail; no such tail is established here.
One must bound the omitted zero-pair contributions uniformly, sum the
bound effectively, and propagate it along the complete primitive path.
Exponential compact-profile tails may not be relabeled resolvent tails.

The independent bounded analytic target is therefore a source-based
representation and an explicit uniform tail error tending to zero
with spectral cutoff, together with a certified finite-divisor input
interface. It can be proved or fail without obtaining zero coordinates.
Actual numerical evaluation remains parked until the finite input is
available and validated; this target authorizes no coordinate search,
optimizer, new dictionary or accuracy claim. Its success threshold is
the analytic truncation statement, not residual<1/2. No favorable cost
bound or absence of catastrophic cancellation is yet known.

Continue only if both the removable full-disk identity and a decreasing
explicit uniform spectral tail are proved. Stop this specialization
at a failed pole/interchange/tail obligation; preserve a partial
identity as unfinished rather than certifying an evaluator. No automatic
repeat attempt or larger cutoff follows. A successful analytic interface
would still need a critical audit and finite data before numerical use.

## Search record, classification and route

Queries included `site.dlmf.nist.gov 7.7 Faddeeva integral representation`,
`Fried Conte plasma dispersion function analytic continuation pole
integral upper lower half plane 1961`, `Gaussian shifted Cauchy transform
erfc complex shift contour Faddeeva integral`,
`site.maths.nottingham.ac.uk "Faddeeva" "pole" integral`, and
`Riemann von Mangoldt explicit bound N(T) Trudgian 2014 0.112 0.278`.
Only primary statements listed above are inputs; search snippets,
MathWorld, Wikipedia and software descriptions were leads, not evidence.
The arXiv HTML attempt for2212.02654v3 returned404; the institution PDF
supplied the needed Section3.1. There is no persistent essential source
blocker. No claim of novelty follows from these searches.

DECISION SPECIALIZE: source coverage now supports the bounded analytic
application just identified. DLMF already covers the general transform;
reproving it is unnecessary. The missing work is its application to
the actual paired removable primitive and the explicit tail, which
no inspected theorem supplies verbatim. This review approves no result
derived during the review. New continuation1577 must receive its
separate supervisor approval before research invocation.

Creative routing is not justified by this evaluator specialization.
No source here provides a bounded mechanism for full odd cancellation,
all-order residual decay or unsmoothed realization at the central gap.
Keep that blocker explicit instead of labeling a transform application
creative. Full matching Mathlib coverage is unchecked/unknown;
C032m's existing supporting analytic coverage is reused. No all-degree
sign, positive-output witness, unrestricted cone exclusion or complete
RH candidate has been established. PROOF and DAG need no change.
