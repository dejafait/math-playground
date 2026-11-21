# Higher-order diagonal source comparison665

This is a literature-only completion of nomination664. No numerical
order, shift, finite error bound, cost certificate or new lemma is derived.
The exact assessed target is retained in review664; continuation665 is a
separate bounded specialization, subject to next-turn supervisor approval.

## Scope and local comparison

The main gap is L030-L032/C032a actual-Xi positivity, locally including
the signed S3 remote-plus-induced coupling. The intermediate target is an
affordable certified diagonal for the unchanged C998a residuals. This
could remove one prerequisite for a complete residual Gram and C999
inverse comparison; it supplies neither one, nor the later signed estimate.

Read C998a's exact frozen-data hypotheses, C999 Section4(19) and its
audit qualification, C744v Section3's definition of h, and C744w
Section3's scalar recurrence. The input is h(k)=Re psi(1/4+ik/2)-log(pi),
k_n=n*pi/ell, ell=log(3)/2, n=0,...,255. No approximate matrix defines it.
The inherited analytic/arithmetic/source-to-Xi/whole-core/unreplayed c_*
contracts are retained; no original source computation was replayed.

Scoped searches in the 12November literature/history/attempt records for
digamma, Bernoulli and higher-order found C999(19)'s first-order rule,
ready elementary inclusion coverage655/656/658, and661's positive-real
Euler-constant bridge. Neither that bridge nor generic effective
computability is the requested complete complex-diagonal cost certificate.
Preserve the prescription-specific stop in C998e/attempt664: at least
711200254 divisions under its first-order absolute-envelope allocation.
That evidence does not rule out higher order or prove necessary complexity.
C998e's full Gram product/error argument remains unaudited and is not
needed to compare the independently defined scalar target here.

## Primary source evidence

NIST [DLMF5.11.2 and5.11(ii)](https://dlmf.nist.gov/5.11#ii),
version1.2.8,15September2026: read the expansion, principal-log sector
condition and first remainder paragraph. Truncation through index N-1
has a first-omitted-term bound with multiplier
sec(arg(w)/2)^(2N+1) for digamma. Positive-real sign control is a separate
case and is not available for complex arguments. This is a finite
remainder statement, not merely the displayed asymptotic symbol.
[DLMF5.5.2](https://dlmf.nist.gov/5.5#E2) gives
psi(z+1)=psi(z)+1/z; recurrence must avoid poles.
[DLMF24.2.1](https://dlmf.nist.gov/24.2#E1) fixes the Bernoulli convention
by t/(exp(t)-1)=sum B_j t^j/j!, |t|<2pi. Read its definition and signs.

Johansson, *Arbitrary-precision computation of the gamma function*,
[arXiv:2109.08392v1](https://arxiv.org/pdf/2109.08392v1),17September2021,
Sections3.1-3.2, printed pp12-14, (25)-(32), Theorems3.1-3.2 and the
complete proof of3.2: for integer N>=1 and w outside (-infinity,0],

    psi(w)=log(w)-1/(2w)-sum_(j=1)^(N-1) B_(2j)/(2j w^(2j))+R'_N(w),
    |R'_N(w)|<=sec(arg(w)/2)^(2N+1) |B_(2N)|/(2N |w|^(2N)).

These are the cited (28),(30),(32), not a new local remainder proof.
The proof uses (27)'s periodic-Bernoulli integral, the denominator
comparison |w+x|^-1<=sec(arg(w)/2)(|w|+x)^-1, and Theorem3.1 on |w|.
Thus the derivative case is covered explicitly; differentiating an
uncontrolled log-gamma asymptotic is unnecessary. Read Algorithm4's
error-enclosure and backup-termination cases on pp11-12, and Section3.3
on pp15-16: increasing order at fixed argument need not improve its
bound. Its log-gamma examples and asymptotic work estimates are not
absolute digamma error/work certificates. Theorems3.3-3.4 were inspected
as comparisons only; they are not imported for this continuation.

External searches: “site.dlmf.nist.gov digamma remainder Bernoulli complex
sec phase 5.11”, “digamma asymptotic expansion rigorous remainder complex
right half plane Bernoulli Johansson”, “site.fredrikj.net gamma function
digamma remainder Bernoulli algorithm”, and “site.arxiv.org Johansson
gamma function arbitrary precision Stirling digamma error bounds 2021”.
Retrieved DLMF statements first, then Johansson's exact derivative formula,
theorem and proof. The arXiv record contains only v1; an attempted v3 HTML
URL failed, then v1 PDF and HTML were read successfully. An author PDF
guess failed; there is no remaining essential source-access blocker.
Other search results, including Spouge and implementation pages, are leads
only and supply no mathematical input. No novelty inference is made.

## Applicability and remaining difference

For each fixed argument and any nonnegative integer right shift, its
real part remains positive. The recurrence encounters no pole, and the
shifted point lies in the theorem's cut-plane domain, with principal
logarithm unambiguous. This checks the source scope for every mode,
including n=0. It does not choose an order or certify a tolerance.
The real part and subtraction of log(pi) must retain all numerical error;
no complex sign assertion is imported. C999's existing real-log reduction
is available if an implementation avoids a complex logarithm call.

Reuse the inspected scalar inclusion and elementary-function assessments
in review655/comparison656 and source-notes658, particularly its
“Elementary calls and finite precision” passage. Inclusion under composition
does not supply truncation bounds, a target radius or an operation count.
A future elementary implementation may use explicit rational/Taylor
enclosures instead of reproducing optimized library code. Any changed
special-function formula or unassessed remainder returns to source review.

DECISION SPECIALIZE: sources cover recurrence plus higher-order remainder
on the entire finite input set. The missing part is a finite prescription
and its certified absolute arithmetic/error/work ledger, not a new
asymptotic theorem. Citation alone cannot establish <=10000000 operations.
Continue only after separate approval of continuation665, then one bounded
calculation. Require analytic error<=2^-45 and elementary/rounding
error<=2^-47 for each h(k_n), with all constants, coefficients,256 values
and shared assembly paid. Preserve the100000000 full-Gram ceiling.
If that test fails, distinguish a genuine lower-bound cost obstruction
from an insufficient upper estimate; do not repeat the first-order route.

No mathematical script, lemma, proof overview or DAG changed in this
source review. Mathlib full matching coverage was not checked; this is
not evidence of absence. Independent full scalar/quadrature/projection,
inverse-debt and sign obligations remain, as do higher/mixed endpoint,
C744q/H2, non-neutral and global assembly gaps. No cross-notebook input.

## Direct-source approval666

Recovery666 reopened the direct DLMF5.11(ii),5.5.2,24.2.1 and pinned
v1 PDF URLs above. Read the derivative formulas (25)-(29) on printed
p12, remainder definition and Theorem3.1 on p13, and Theorem3.2 with
its complete proof on p14. This corrects the prior pp13-14 shorthand
for the combined derivative/error passages. The direct URL evidence is
now also in continuation665 SOURCE_EVIDENCE. Its unchanged SPECIALIZE
scope is approved for the saved bounded test; no new literature claim,
parameter calculation, complexity certificate or mathematical result is
asserted. Mathlib matching coverage remains unchecked.
