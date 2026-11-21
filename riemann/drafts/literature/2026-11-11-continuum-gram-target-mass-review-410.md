# Exact continuum Gram target-mass test — completed source comparison, step411

TARGET: Assess primary-source coverage for a continuum L2 Schur-complement lower certificate for C997s's capped E_n at regularization lambda_n=exp(-n/16), using the exact complete-kernel Gram matrix and target spectral mass.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Step411 searched Tikhonov target spectral distribution, converse/source-condition rates, complex quadratic relaxation, exact Laguerre moving-window Gram terms, and target-weighted inverse-form quadrature; inspected the primary contracts below and reused reviews369/390 and stop341. No matching growing-n target-mass estimate was identified; no novelty inference.
SOURCE_EVIDENCE: Clason arXiv:2001.00617v2, Lemma6.3/Theorem6.5 and complete proofs, printed pp59-62; Hohage-Weidling arXiv:1603.05133v4, Section3/(7)-(8), Assumption3.2, Theorem3.3 and its supplied converse proof; Flemming-Hofmann-Mathe Inverse Problems27(2011)025006, Section1/(3), Example1 and Proposition1 with proof, pp2,5-6. Li-Sra-Jegelka ICML2016 Theorems6/8 and supplement opening are an inspected new quantitative lead, with essential proof/degeneracy cases still unread.
COMPARISON: Quadratic minimization is covered generically, with local complex-cap and supremum conversions still to be written in a research turn. Fixed-operator bias/source theorems require target spectral information and do not supply a uniform rate for the growing finite-rank complete kernel; extremal eigenvalues alone do not control the target. A distinct finite target-weighted quadrature test is nominated separately, not an all-n estimate.
GAP: No inspected source bounds the actual target-resolvent mass at lambda_n=exp(-n/16), proves positive F_n with exp(n/32)F_n unbounded, or pays complete-kernel exponential integration error. Generic regularization alone is parked. The new Gauss-Radau finite-certificate scope requires a separate assessment of proof cases and exact-arithmetic applicability.
REASON: The source comparison supplies a scoped negative import decision, not an obstruction to E_n or a new lemma. Do not spend the next turn deriving only a ridge identity. Preserve the proposed asymptotic test, and separately review the new target-specific finite enclosure method before any calculation.
SCOPE: Integer n>=64; exact C997c/C997s kernel, I=[7/4,9/4], z_star=1+i/8, gamma_j=15/8+j/(4n), 0<=j<=n, original complex coefficient cap B_n=exp(sqrt(n)); ordinary Lebesgue L2(I), without quadrature or a pointwise spectral replacement.
LITERATURE_REASON: Changed object: exact continuum quadratic regularization and target spectral mass, whose quantitative hypotheses and original-cap conversion are outside the approved endpoint audit and stopped sampled-generator assessments.

## Proposed object and discriminating test

Define t_n(c)=k_n(c,z_star), b_(j,n)(c)=k_n(c,gamma_j), with the
complete kernel of C997s. Use the inner product integral conjugate(f)g
and the finite quantities

    G_(ij,n)=integral_I conjugate(b_(i,n)(c))*b_(j,n)(c)dc,
    h_(i,n)=integral_I conjugate(b_(i,n)(c))*t_n(c)dc,
    d_n=integral_I |t_n(c)|^2 dc,
    lambda_n=exp(-n/16),
    F_n=d_n-h_n^*(G_n+lambda_n Id)^(-1)h_n-lambda_n B_n^2.

These are definitions of a PROPOSED certificate object, not a derived
lower bound or a claim of a useful sign. No inverse, spectral mass or
asymptotic estimate has been calculated. Source review must first check
whether ordinary complex quadratic duality yields the needed lower
certificate for the original continuum supremum and pays every norm
conversion. The quantitative research threshold would be positive F_n
with exp(n/32)F_n unbounded on a specified unbounded integer sequence.
Any claim relating that threshold to E_n must be justified after coverage;
no finite sample can establish it.

The exact kernel retains both windows, both beta terms, K's subtraction,
every closed endpoint and every grid column. Do not form G from C999d's
leading approximation and silently neglect its remainder. The selected
lambda is fixed here, not to be optimized through an unreported sweep.
The test needs the target's spectral mass, including small eigenvalues;
large condition numbers or an extremal-eigenvector example do not suffice.

## Recovery comparison: three mechanisms

1. More fixed-order endpoint asymptotics: the audited C999d formula is
   reliable, but its capped allowance does not pay the desired rate.
   No growing-order or exponentially small remainder input is available
   in the approved scope. Park this completion attempt, retain the formula.
2. Oscillatory or exact-annihilator densities: C997e's large-curvature
   Gaussian leaks; the scoped endpoint-packet stops347/359 and determinant
   stop381 remain in force. No changed phase or paid action/L1 estimate
   is supplied, so none is reopened.
3. Exact continuum Gram target mass: selected for separate source review.
   This measures the actual integrated target against all complete columns
   with a finite regularization penalty. Its intended evidence is a
   quantitative continuum spectral statement, not more iterations or
   degrees of the two stopped discrete generators. This is a different
   test, not an assumption that the older numerical failures disappear.

Read primary hypotheses and relevant proof cases for the quadratic
certificate, constrained approximation and any claimed target-mass
estimate. Reuse C997s's existing convex assessment and review390's
norm/data mismatch instead of repeating their searches. Compare with
the operator-specific unpaid target-tail limitation in stop341. A general
ridge-regression identity alone would cover only the certificate algebra,
not the required rate. Continue only with a precisely covered bounded
subtarget and its quantitative test; if no usable target-mass input or
independently testable estimate is found, document that mismatch and park
this mechanism rather than repeat the same generic theorem review.

Essential local inputs are C997c and C997s. C999d is comparison evidence
for the error restriction, not exponential-precision Gram data. There is
no cross-notebook input. A lower certificate could decide whether this
fixed-grid capped bridge is viable; it would not settle general band
measures, selected/both-sign transfer, C997a(8), reconstruction,
complements/regulators, arithmetic output control after L993, L984(H),
L966/L968 forcing or L030-L032/C032a actual-Xi positivity. Full matching
Mathlib coverage is unchecked. No new mathematics is approved or proved
by writing this continuation.

## Completed source comparison — step411, 11 November 2026

This is LITERATURE / literature_comparison / NOVELTY_UNCHECKED, with
outcome NEGATIVE for direct quantitative import. It changes the route:
generic regularization is not a source-backed completion mechanism.
No lower certificate, complex specialization, norm-conversion formula,
new spectral estimate, lemma or mathematical script was derived.
The proposal above remains a requested test, not an established result.

### Primary contracts inspected

**Quadratic minimization.** Christian Clason, *Regularization of Inverse
Problems*, arXiv:2001.00617v2, 8 February2021, notes dated9 February2021,
[Lemma6.3 and Theorem6.5, printed pp59-62](https://arxiv.org/pdf/2001.00617v2#page=62).
For compact K between Hilbert spaces, arbitrary y in the data space and
alpha>0, the regularized solution is the unique solution of the normal
equation and unique minimizer of the quadratic Tikhonov functional.
Read both proofs: the singular-system argument retains the coefficient
nullspace, and the functional difference gives the minimizer for arbitrary
data, without requiring y in the range. This covers the generic quadratic
problem. It gives neither an original coefficient-l1 constraint nor a
continuum supremum conclusion. The prospective local application still
must verify the complex realification, Gram convention, relaxation
direction, penalty and interval-length conversion. No reproof of the
general theorem is needed. The data component outside the column range
must not be removed merely because the normal equation uses K* y.

**Converse/source-condition rates.** T. Hohage and F. Weidling,
*Characterizations of variational source conditions, converse results,
and maxisets of spectral regularization methods*, arXiv:1603.05133v4,
18 April2016; journal reference SIAM J. Numer. Anal.55(2017),598-620.
Read [Section3, (7)-(8), Assumption3.2, Theorem3.3 and its converse
proof](https://arxiv.org/html/1603.05133v4#S3).
The setting is a fixed injective bounded operator between real Hilbert
spaces. The theorem equates bounded weighted target spectral distribution
and a bias rate, under the filter bounds, monotonicity, nonzero diagonal
residual bound and qualification (15) for an index function kappa and
nu>1. The supplied proof establishes bias-to-spectral-mass using a
spectral projection; the harder direction is referred to Albani et al.,
Proposition2.3, and was not independently read. Tikhonov is explicitly
included. This is not an unconditional rate theorem or a full matching
import: our operator and target change with n, and the output operator
has a kernel. Restricting to its range would discard a target component
unless separately retained. No uniform source norm is supplied. Also,
the theorem concerns a bias norm, not directly the proposed minimized
quadratic value. The referred proof is nonessential to this rejection;
no direction of this theorem is applied locally.

**Target distribution versus regularization.** J. Flemming, B. Hofmann
and P. Mathe, *Sharp converse results for the regularization error using
distance functions*, Inverse Problems27(2011),025006,
[Section1/(3), Example1, Proposition1 and proof, printed pp2,5-6](https://www.tu-chemnitz.de/mathematik/ip/fulltext/fhm.pdf).
The setting assumes a fixed bounded injective A with nonclosed range.
The spectral distribution belongs to the particular vector; the
regularization residual is integrated against that distribution.
Proposition1 bounds low-spectral target mass by a constant times the
bias, using a pointwise residual lower bound on a short spectral
interval. Read that complete integral proof and the Tikhonov filter
example. It supplies no mass lower rate for our target and no growing-n
uniformity. Its injectivity assumption excludes silently copying the
zero-mode convention to the finite-rank output operator. No theorem
from this source is applied here. Its distribution function is unrelated
to the proposal's symbol F_n.

### Exact applicability obligations, not a new specialization

C997c and C997s define continuous columns and a target on a compact
slope interval. Thus ordinary finite-column Hilbert approximation is
the relevant framework, not a stochastic covariance or sampled design.
A future certificate proof must retain the original complex-modulus cap;
a coordinatewise real/imaginary budget or a reverse l1/l2 inclusion would
change the problem. It must pay the ordinary Lebesgue L2-to-sup factor,
retain the penalty sign and account for target mass outside the span.
A negative proposed F_n would mean that this certificate is inconclusive,
not that E_n is small. No positive sign or norm conversion is asserted
by this literature turn.

The inspected rate theorems do not determine the proposed exponential
threshold. In particular one cannot substitute an extreme eigenvector,
a condition number or an unweighted eigenvalue distribution for the
actual target. Clason's arbitrary-data theorem avoids a missing-range
hypothesis for the algebra, but does not resolve the quantitative gap.
The exact original lambda and cap remain fixed; no parameter sweep was
performed. No essential mathematical claim is based on a search snippet.

### Duplicates, failures, search scope and a new lead

Read C997s's exact kernel, cap and finite-certificate method; C997c's
complete representation; review390's Ferreira-Kempf norm/data mismatch;
stop341 and C997k's exact target-tail limitation; and review369's existing
complex support-function coverage. C999c's stronger two-window objective
and C999d's audited additive-error restriction remain contrasts, not
exponentially accurate Gram data. No stopped sampled generator, endpoint
packet, fixed-order expansion or scalar regularization was reopened.

Queries included `Tikhonov regularization spectral source condition
residual target spectral measure Schur complement inverse problems`,
`Tikhonov regularization spectral distribution function lower bounds
converse theorem residual spectral tail`, `Laguerre oscillatory moving
window integral kernel singular values target spectral mass approximation
complex frequency`, `Laguerre Schur complement approximation complex
exponential`, and `Gauss Radau upper bound u transpose inverse A u
Lanczos primary theorem matrix inverse quadratic form pdf`.
The exact-kernel searches located no matching primary rate theorem;
this is not evidence of absence or novelty. Stanford's book PDF repeatedly
timed out. Existing norm-source coverage is reusable and Clason's full
quadratic proof is accessible, so this is not an essential access blocker.
The Stanford slides' opening was accessible; their duality sections were
not retrieved and are not claimed as inspected coverage.

A materially different finite test emerged: C. Li, S. Sra and S. Jegelka,
*Gaussian quadrature for matrix inverse forms with applications*, ICML2016,
PMLR48, [primary paper](https://proceedings.mlr.press/v48/lig16.pdf),
Theorems6/8, PDF pp4-5, and
[primary supplement](https://proceedings.mlr.press/v48/lig16-supp.pdf).
Inspected the positive-definite real-matrix setup, target inverse form,
left-Radau upper-bound comparison, condition-number-dependent rate and
the explicit qualification about simple eigenvalues and AppendixC.
Read only supplement A.1-A.2's opening and theorem/proof openings in B;
complete remainder, termination, AppendixC and upper-bound proof cases
are not yet inspected. This source provides a concrete enclosure lead,
not an n-uniform rate or floating-point certificate. Its generic geometric
rate must not be advertised as effective at our exponentially small
regularization without paying its condition-number constants.

A local search of the 10-11November literature assessments and relevant
spectral/Gram stop files found no prior Radau/Lanczos/lig16 assessment.
This is a bounded duplicate check. The exact finite target, missing
source cases and continuation test are saved in review411. The aim is
an enclosure of the actual target-weighted inverse form at two fixed
degrees, without an eigenvalue surrogate or a fit. No such enclosure
was computed. Even a positive result would leave the unbounded-sequence
threshold above unresolved. The generic asymptotic regularization route
is parked pending a concrete quantitative input; this new method must
pass its separate source gate before a bounded finite attempt.

Full matching Mathlib coverage for the local certificate is unchecked.
No cross-notebook input is used. Actual-Xi positivity, capped E_n,
C997a(8), selected/both-sign transfer, reconstruction, complements,
regulators, L993's arithmetic output, L984(H), and forcing remain open.
No RH candidate is proposed.
