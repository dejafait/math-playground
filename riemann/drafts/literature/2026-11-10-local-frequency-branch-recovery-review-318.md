# Local recovery of one competitor frequency branch — source assessment

TARGET: Assess whether local positive-frequency branch recovery for C997a's competitor response admits subexponential operator norm and exponentially small error relative to slope-measure TV on the interior band [15/8,17/8].
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step319 searched finite-window analytic-signal recovery, local Hilbert projection, entire sign approximation, truncated Fourier/Hilbert stability and localized regularized sampling; compared the exact target with the primary contracts and recorded failures below. No inspected result supplies or excludes this operator; this is not a novelty finding.
SOURCE_EVIDENCE: Eremenko–Yuditskii math/0604324 Theorems2–3 and relevant proofs pp3,5,7–8,11–12; Kircheis–Potts–Tasche author manuscript Some remarks on regularized Shannon sampling formulas, (1.4),(1.6), Theorems2.1/4.2 and proof pp2–4,14–15; Lederman–Steinerberger 1605.03866v1 Theorem3 p3/Section6 pp10–11; Alaifari–Katsevich 1302.6295v2 Proposition5.2/Theorem5.4 pp18–20. Exact versions, inspected cases and limitations are below; reuse review312 on its original scope.
COMPARISON: Entire sign approximation controls multiplier error but not representing-kernel TV or access to Gamma. Localized Shannon reconstruction gives exponential error relative to global L2 for reconstruction of the same signal, not branch extraction. Truncated-transform instability concerns different operators and does not furnish bad inputs in this Laguerre range. None pays the two simultaneous contracts below; C997a's exponential envelope is not a lower bound.
GAP: Construct a bounded complex-linear recovery sequence on the full C(Gamma) space with one positive absolute slope-TV error exponent and every positive exponential norm allowance, or prove these requirements incompatible on the exact response range. Quantitative realization and costs are now mathematical questions, not an essential unread theorem assumed here.
REASON: The source comparison completes approval for one bounded attempt on the unchanged nomination after reassessing trials314/315/318. This is literature EXPLORATION/NOVELTY_UNCHECKED, not an operator construction, impossibility theorem, new lemma or mathematical advance; no supervisor counter reset is asserted.
LITERATURE_REASON: The new target asks for a bounded operator from a finite observed ordinate interval to one frequency branch on an interior interval, with error measured against original slope TV; this is not an approved subtarget of review312's unchanged complete-quartet assay.
SCOPE: The exact operator question and quantifiers below, including every finite complex Borel slope measure, both short intervals, both beta-reflected contributions, K's -1 and the closed output interval. Approves one construction or exact-range obstruction attempt with explicit access, norm and TV-error accounting; it does not approve replacement by arbitrary unrelated bandlimited data or infer impossibility from one failed filter.

## Exact proposed source-review target

Keep n>=2, I=Gamma=[7/4,9/4], Gamma_in=[15/8,17/8],
the original K_(n+2) including its -1, and every quartet term.
Let mu be ANY finite complex Borel measure on I. Write
R_n(gamma;mu)=integral_I q_n(c;3/8,gamma)dmu(c), with q_n
exactly C997a(1). The proposed branch observable is defined by

    H_n^+(gamma;mu)=-2*integral_I exp(-cn/4)*[
       integral_(cn)^(c*(n+2)) K_(n+2)(t)*exp(-t/2)
                               *cosh(3t/8)*exp(i*gamma*t)dt
       -integral_n^(n+2) K_(n+2)(t)*exp(-t/2)
                               *cosh(3t/8)*exp(i*gamma*t)dt]dmu(c).

This is a nomination by an explicit finite integral, not a claimed
recovery formula. The source review must check its normalization and
relation to the complete response before using a Fourier model.
Both beta-reflected terms remain in cosh(3t/8); the negative-ordinate
branch, the lower interval and the constant subtraction may not be
discarded without a proved error relative to ||mu||_TV.

The question is whether there are bounded complex-linear operators

    A_n:C(Gamma,C) -> C(Gamma_in,C)

independent of mu and actual unknown zeros, and fixed C<infinity,
kappa>0, such that for every sufficiently large integer n and every mu,

    ||A_n(R_n|Gamma)-(H_n^+|Gamma_in)||_infinity
                                  <=C*exp(-kappa*n)*||mu||_TV,
    ||A_n||_(sup->sup)<=C_epsilon*exp(epsilon*n)
                         for EVERY epsilon>0.

Each C_epsilon must be finite and independent of n and mu. The same
operator sequence must meet all these allowances. The input is the
full continuous function on Gamma, not samples or a single ordinate;
the output is required uniformly on the closed interior interval.
Operators may depend on n and the stated fixed interval/kernel data.
No bound is assumed for unobserved ordinates or the unknown branch.

## Relevance and discriminating test

A passing recovery estimate would provide complex branch information
from the observed band and could permit a separate test of one-sided
analytic continuation, avoiding step318's whole-boundary truncation.
It does not itself normalize the selected quartet, suppress a competitor,
construct slope measures, or pay C997a(7). All those implications would
need later justification. A lower bound forcing exponential operator
norm or preventing any fixed positive TV-relative error rate would stop
this local recovery target. Failure of one projector or an estimate in
the wrong norm would remain inconclusive.

Search primary work on local analytic-signal/Hardy projection,
separation of positive and negative Fourier bands, quantitative local
reconstruction and norm-controlled finite-window filters. Compare
the exact finite support, the growing carrier, the finite observation
interval and the TV-relative absolute error. A global Hilbert transform,
ordinary bandlimited uniqueness or finite-point interpolation alone is
insufficient. Check recorded local failures before selecting a tool.
This paragraph requests discovery; it imports none of those theorems.

Essential local inputs are L997's exact finite response and bound,
C997a's exact phase reduction and the step318 growth estimate. C997b
and stops293/314/315/316/318 are scope comparisons, not hypotheses.
The named later source review must distinguish inspected theorems from
unread leads and approve only a covered exact target. Mathlib coverage
is unchecked and unknown. No cross-notebook input is proposed.

Actual-Xi positivity L030-L032/C032a, L966/L968 signed forcing,
actual spectral reconstruction, signed recovery, infinite-zero
complements, regulator uniformity, use of L993 and L984(H) remain unpaid.
No mathematics on this new recovery target was attempted in step318.

## Completed literature-only comparison — step319, 10 November 2026

The TARGET and displayed operator requirements above are unchanged.
This review approves an attempt, not the desired conclusion. No operator,
new response estimate, spectral-density realization or obstruction has
been proved in this literature turn. Review312 is reused for its
functional-analytic, approximation and propagation inputs; the following
comparison addresses the previously uncovered local observable.

### Normalization and available local evidence

Read L997's hypotheses and (4)–(7), C997a's (1)–(2), exact quartet/phase
reduction and (18)–(20). Comparing the proposed integrand with C997a(1)
using cos(x)=(exp(ix)+exp(-ix))/2 checks its factor -2: the two nominated
sign branches together are the original -4 cosine response. H_n^+ is the
positive-exponential component, not the twice-normalized analytic signal
often used for real signals. This is a definition check, not a recovery
formula. For complex mu the other component cannot be replaced by the
complex conjugate of H_n^+. Both cosh terms, the lower-interval subtraction
and the original K remain in each component.

C997a(19) already records evenness in the ordinate, including for complex
mu, and the full entire-growth estimate with T_n=9(n+2)/4 and B_n from
(18). Any construction may use that structure, but may not assume
unobserved values beyond it. Its real-axis upper envelope has order
(n+2)exp(9n/32) times slope TV. Therefore an error estimate relative to
a signal norm is not yet the required absolute slope-TV estimate.
Nor does a signal sup norm bound alone identify the TV of its Fourier
measure. The necessary realization and quantitative comparison are left
for the mathematical attempt; no new bound is asserted here.

### Inspected primary results

**Entire sign approximation.** A. Eremenko and P. Yuditskii,
[*Uniform approximation of sgn x by polynomials and entire functions*](https://arxiv.org/pdf/math/0604324),
Theorem2 p3 and Theorem3 p5; representation/uniqueness proof pp7–8,
asymptotic proof pp11–12. For A>0, L(A) is the best uniform error for
sgn on (-infinity,-A] union [A,infinity) among entire functions of
exponential type at most one. Theorem2 states
sqrt(A)exp(A)L(A) -> sqrt(2/pi). Theorem3 describes the extremal by a
conformal map. Read the reflection/type argument, alternation/interlacing
uniqueness case and the comparison-map asymptotic. Only the exponential
rate is proposed as a tool; no sharp-prefactor proof audit is claimed.
The served PDF is 15 pages, labelled arXiv v1 but with body date
26 November2024; a June2006 author-paper copy at
[CiteSeerX](https://citeseerx.ist.psu.edu/document?doi=cabfabe2e25787daf7a10a5e7dc6cd0d4a8bd891&repid=rep1&type=pdf)
has the same theorem statements. Neither contract supplies a finite-measure
convolution kernel with controlled TV. A bounded local operator and its
accessible support still require justification. The theorem's optimality
on two rays is not optimality for this structured finite-band response.

**Localized sampling with a proved exponential rate.** M. Kircheis,
D. Potts and M. Tasche,
[*Some remarks on regularized Shannon sampling formulas*](https://www-user.tu-chemnitz.de/~potts/paper/ShannonOpt.pdf),
unversioned 24-page author manuscript accessed 10 November2026,
(1.4)/(1.6) pp2–3, Theorem2.1 pp3–4 and Theorem4.2 with proof pp14–15.
For integer m>=2 and f in L2(R) intersect C(R) with angular bandwidth
0<delta<=(m-1)pi/m, the sinh window with beta=m(pi-delta) gives

    ||f-R_sinh,m f||_infinity
       <=(4+9*sqrt(m*(pi-delta)))*exp(-m*(pi-delta))*||f||_2.

The sum (1.4) uses only integers k with |t-k|<=m. Read the compact-support
truncation case, the I1 interior contribution and the oscillatory J1
contribution, including the beta>=pi hypothesis. This manuscript repairs
earlier numerically justified assumptions; no parameter-optimality claim
is imported. It reconstructs the same signal from its samples, not one
branch from their sum. Rescaling must retain accessible samples; L2 and
operator-cost comparisons with slope TV are unpaid. The theorem is a
tool, not a ready solution to this target.

**Truncated Fourier stability.** R. R. Lederman and S. Steinerberger,
[*Stability Estimates for Truncated Fourier and Laplace Transforms*](https://arxiv.org/pdf/1605.03866v1),
v1, 12 May2016, Theorem3 p3 and Section6 pp10–11. For real nonzero
f in H1[-1,1], extended by zero for its Fourier transform, the squared
L2 mass of its transform on [-1,1] is bounded below by
c1*(c2*||f'||_2/||f||_2)^(-c2*||f'||_2/||f||_2)*||f||_2^2,
with positive universal constants; the zero-derivative case is interpreted
separately. Read the differential-operator argument and both proof cases:
a root permits derivative control; a fixed sign permits the positive
sinc-kernel estimate. This is an inverse-stability inequality in Sobolev/L2
norms. It neither constructs local branch extraction nor supplies an
admissible slope measure with exponentially bad branch/data ratio.
Its real-valued hypothesis cannot be silently extended to every complex
measure. No specialization is imported for the present operator.

**Truncated Hilbert inverse scope.** R. Alaifari and A. Katsevich,
[*Spectral Analysis of the Truncated Hilbert Transform with Overlap*](https://arxiv.org/pdf/1302.6295v2),
v2, 26 November2013, operator (1.1), Proposition5.2 and Theorem5.4
pp18–20. For a1<a2<a3<a4 the operator is the Hilbert transform of
L2(a2,a4) functions, restricted to (a1,a3). It has trivial kernel and
dense nonsurjective range; its singular values accumulate at zero and
one. Read the proposition's injectivity/nonsurjectivity/adjoint-range
cases and the theorem's exclusion of endpoint eigenvalues using Lemma5.1.
This concerns inversion of a truncated Hilbert transform, not positive
frequency projection from values of the original even response.
The unrestricted L2 bad directions have not been realized by our slope
operator; neither the range defect nor small singular values establish
the requested n-dependent lower cost. No such impossibility is imported.

Lyubarskii–Ortega-Cerda,
[*Bandlimited Lipschitz functions*](https://diposit.ub.edu/server/api/core/bitstreams/9d281d96-e409-4af9-86a9-e4ec187946e8/content),
author-paper opening pp1–2 and Theorems1–2 p4 were screened. Their
global Bernstein/Lipschitz sampling discussion and warning about the
unrestricted L-infinity Hilbert transform do not decide our separated,
n-dependent finite response range. No theorem or impossibility from
that paper is used here.

### Search record, duplicates and access qualifications

Queries included `local Hilbert transform exponential accuracy bandlimited`,
`positive frequency finite interval recovery operator approximation`,
`analytic signal finite window error bound reconstruction`,
`Hilbert transform bandlimited local reconstruction error bound`,
`Eremenko Yuditskii uniform approximation sgn x entire functions`,
`truncated Hilbert transform bandlimited stability`,
`Hilbert transform regularized sampling exponential error`,
`finite impulse response Hilbert error exponential approximation`,
and the exact primary-paper titles above. Search snippets, engineering
examples and general spectral-gap sign-change results were not used as
theorem evidence. A search returning no match does not establish novelty.

Notebook-local searches in drafts/literature and ATTEMPTS found review312,
the earlier angular/Hardy localization assessments and the recorded
prolate material. The latter concerns different trial observables;
no prolate theorem or sibling-notebook input is imported. Reused review312
instead of repeating its literature assessment. Read stops293/314/315/316/318
and the step317 audit status: fixed positive-bump leakage, unpaid dual rates,
equidistant interpolation bounds, a prescribed Chebyshev normalization cost
and whole-boundary propagation do not exclude this local operator.
The audited subclass stops stay intact; no route is reopened by renaming.

The attempted math/0604324v2 URL returned 404 and the guessed author
sgn.pdf URL failed. The actual arXiv PDF and June2006 paper copy were
accessible; this is not a persistent source blocker. The current
ShannonOpt manuscript is used instead of assuming the older sampling
papers' numerical inequalities. Some PDF screenshot calls exposed only
reference labels through the tool; no visual inspection is claimed.
The theorem evidence above is the extracted primary text. No essential
source remains inaccessible for the bounded attempt approved here.
Full matching Mathlib coverage is unchecked and unknown.

### Bounded mathematical continuation

One proof_attempt/creative may now test the unchanged TARGET. Save partial
reasoning first. Start from the exact finite response and examine a local
sign-multiplier/filter construction, paying its representation as an
operator on all C(Gamma), its accessible data and its norm. Known results
above are cited, not reproved. A frequency-multiplier estimate is only a
component: compare its complete response error with original slope TV,
uniformly over all mu and every point of the closed interior interval.
Keep both branches until their treatment is justified, both short intervals,
the beta reflection and K's -1. No limiting Laguerre model is approved
without a quantitative remainder in that same norm.

The decisive passing evidence is the displayed fixed kappa>0 error bound
and one operator sequence meeting every epsilon>0 norm allowance for all
sufficiently large n. An exact-range lower bound incompatible with those
requirements would instead stop this target. A positive fixed exponential
norm rate, an error relative only to a growing signal norm, finitely many
ordinates, an unbounded derivative/Hilbert operator on C(Gamma), or failure
of one filter is insufficient. Record an inconclusive construction as
such; do not promote a scalar-multiplier optimum to an all-operator bound.

This is reassessment of the broader assay after its three inconclusive
tests through an independently testable observable. It is not a reset of
the recorded mathematical-exploration usage. A successful recovery result
would only supply branch information before a later continuation or
localization test. Selected normalization, uniform competitor suppression,
subexponential slope TV for that original assay, actual reconstruction,
signed recovery, infinite-zero complements, regulator uniformity, L993,
L984(H) and actual-Xi positivity all remain separate unpaid obligations.
