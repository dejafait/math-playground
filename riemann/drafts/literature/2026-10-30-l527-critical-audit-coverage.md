# L527 critical audit: completed source-scope comparison

TARGET: Critically audit L527's common-pole generic increment, including the correlated band trace, uniform Hardy selector limit and exact coefficient enclosure.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed exact-target searches and overlap/failure screen in 2026-10-30-common-pole-generic-increment-coverage.md, then read L527 and the scoped common-pole working/history/stop records. A narrow Teschl spectral-theorem search and the author's primary PDF supplied the previously unspecified functional-calculus scope; details below. No new matching increment theorem or originality claim.
SOURCE_EVIDENCE: https://rstation.ai/problems/riemann_hypothesis/papers/2 , v2 (16 October 2026), Lemma 4.1 with (4.1)--(4.4), (5.2)--(5.4), (7.1)/(7.3); https://jordanbell.info/LaTeX/mathematics/traceclass/ , 18 April 2016, Theorems 15/18/23/25 and the Hilbert--Schmidt-factor cyclicity proof; https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf , Teschl, posted GSM 99 edition, Theorems 3.1/3.7/5.1 and (3.52), printed pp.90--91,96--97,123--124; reuse inspected Halmos (1969), p.381 and Theorem 2 pp.384--385, https://www.ams.org/tran/1969-144-00/S0002-9947-1969-0251519-5/S0002-9947-1969-0251519-5.pdf . Source scopes, not independently audited manuscripts.
COMPARISON: Known projection, localized-Hardy and trace-ideal tools cover the imported inputs; the spectral theorem covers bounded functional calculus on each self-adjoint conjugate. None supplies L527's correlated rL-scale expansion, moving-vector selector, discontinuity control or coefficient enclosure. These are explicitly local proof/certificate claims to audit, not missing source theorems to assume.
GAP: Independently audit L527 Sections 1--5 under these precise cited-input scopes, including all moving-family limits and the complete relevant certificate evidence. No conclusion of that audit is established by this literature turn.
REASON: Essential source coverage is sufficient for one bounded conceptual audit of the existing claim; citation alone cannot verify its new uniformity, trace manipulations or quadrature implementation. Retain the unaudited label until that mathematical audit.
LITERATURE_REASON: The newly nominated audit needed a separate scope comparison, especially for the self-adjoint functional calculus behind its discontinuous moving selector. This review reuses ready searches and fills that specific standard-input scope; no further literature turn is requested on unchanged assumptions.
SCOPE: Ready for the exact TARGET only, subject to the supervisor's separate next-invocation approval of this changed assessment. Audit the existing proof and certificate; do not repeat the creative mechanism, strengthen the theorem, assume a uniform spectral gap, or infer actual-Xi signs. Ordinary repairs within the stated claim are audit work; a materially changed mathematical target needs separate coverage.

Essential local inputs are L526 and L527. Preserve L526's exact h,
f_p, L=log p, r=p^(-1/2), common M=L+2, actual P_-/P_+, measure
dt/(2pi), reflection and corrected involution. The result to audit
is Gamma_p/(rL) -> -1-(4/pi)c_h, with the coefficient strictly
between -1.299 and -1.192 rather than at or below -2.

The full proof and exact arithmetic specifications are in L527;
the script and complete certificate are
`scripts/common-pole-generic/coefficient_certificate.py` and
`scripts/common-pole-generic/coefficient-certificate.json`.
Review the separate trace existence and intersection identification,
trace-norm control of the added factor's complete shift series,
the conjugated derivative/group sign, uniformity over |xi|<=2L,
the shrinking spectral transition/turning-set argument, the
Hilbert--Schmidt column integral and harmonic average. Check the
quadrature derivative, normalization and tail bounds together with
the exact interval implementation; a numerical preview is not audit.

An accepted audit must validate the asymptotic and strict threshold,
or identify and repair a concrete mathematical error. If unresolved,
retain the partial reasoning and unaudited label. The actual-Xi
positivity gap, collective negative overlap/remainder, missing
visible primes, full-Weil identity, nullvector/trace/nonresonance
premises, family bounds and Xi transfer remain open regardless.
Mathlib full coverage is unchecked; no cross-notebook input is used.

## Completed comparison, 30 October 2026

This is source review, not a proof audit or a replay of the calculation.
The original audit obligations above are retained. The main gap is
actual-Xi all-degree positivity; the intermediate target is a reliable
decision about this particular local absorption mechanism. Its plausible
use is to retain or correct the local stop before attempting a collective
signed comparison. An auxiliary negative coefficient is not RH progress
beyond the checked sources unless its stated local argument is validated.

### Primary inputs and their limits

Reopened [paper 2 v2](https://rstation.ai/problems/riemann_hypothesis/papers/2)
at Lemma 4.1 and its proof, (5.2)--(5.4), and (7.1)/(7.3).
The lemma requires a smooth unimodular symbol, polynomial growth of
its derivatives and phase derivative, bounded second phase derivative,
and a compact smooth physical test. Its proof includes localized
finiteness, the trace-class correction, and the exponential-symbol
sign check. The phase estimates are compact-uniform in t, with a
global second-derivative bound. Section 7 specifies the pole phase.
Its fixed-test asymptotic and fixed-cutoff perturbation do not give
the moving-test increment. These remain qualified external inputs.

Reuse the prior primary reading of Halmos, *Two subspaces*, Trans.
AMS 144 (1969), 381--389, p.381 and Theorem 2 pp.384--385, recorded
in the generic-increment coverage assessment. It separates all four
intersections before describing the generic block. It gives neither
localized trace finiteness nor a uniform angle gap. The earlier PDF
403 recorded in the working notes is not a new essential source
blocker: the completed primary assessment is reused without retry.

Reopened [Bell's 18 April 2016 notes](https://jordanbell.info/LaTeX/mathematics/traceclass/).
Theorems 15 and 25 give the Hilbert--Schmidt and trace-norm ideal
bounds. Theorem 18 gives the two-Hilbert--Schmidt-factor criterion.
Theorem 23 assumes a trace-class and a bounded factor; its proof
also records the Hilbert--Schmidt-factor trace identities. The
factor estimates must precede every cycling operation in L527.
These results do not turn operator-norm series convergence into
trace-norm convergence without the weighted summability estimate.

New essential scope reference: [Gerald Teschl, *Mathematical Methods
in Quantum Mechanics*, author's posted GSM 99 edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf).
Theorem 3.1, printed pp.90--91, gives bounded Borel functional
calculus for a projection-valued measure and its vector norm formula;
its strong-convergence assertion fixes that measure. Theorem 3.7,
p.96, gives the spectral measure of a self-adjoint operator; (3.52),
p.97, records transport under unitary equivalence, including domains.
Theorem 5.1, pp.123--124, describes the unitary group, derivative on
the generator domain, and domain invariance. Read these statements,
the simple-function/dominated-convergence proof of 3.1, the uniqueness
proof of 3.7 and the group/domain proof of 5.1. Their hypotheses fit
an audit of the stated unitary-conjugation construction, provided its
domain and Fourier conventions are checked. They do not prove L527's
uniform moving-vector limit, or justify exchanging p and epsilon.
This edition is identified by its posted title page and theorem/page
numbers; the current publisher edition linked there was not inspected.

Named Plancherel, Riemann--Lebesgue, dominated convergence and Tonelli
remain standard tools in their usual hypotheses. L527's elementary
smoothing identities, midpoint error estimates and derivative bounds
are written local calculations. Checking them is part of the nominated
audit, not a need to import a new unproved estimate. No replacement
proof or specialization was derived in this source review.

### Exact audit boundary and decision test

For Section 1 check the Fourier reflection, conjugated symbol,
intersection projection and each separate finite sandwiched trace.
For Section 2 check the band endpoints, shift signs, both localized
Hilbert--Schmidt factors, complete prime-power series and trace-norm
remainder at scale rL. Operator-norm convergence alone is insufficient.

For Section 3 check the conjugate operator domain, group sign and
uniformity over |xi|<=2L in (12); then the regularized functional
calculus, behavior at spectral zero, shrinking transition set, tails
and the ordered limits in (13)--(14). The new spectral reference
licenses the tools, not those estimates. Section 4 must check the
column measure, shifted column, commutator error and discontinuous
periodic averaging before concluding an o(L) trace error.

Section 5 needs the complete relevant integer-interval implementation
and certificate evidence, including normalization, all pointwise
enclosures, quadrature errors and signed tail. Read-only inspection
of the existing script's interface and bounded /grid and /comparison
previews was used solely to locate that evidence. The attempted
/parameters lookup was absent; /grid is the actual field. No script
was run, no certificate entry was independently verified, and a
preview's passed flag is not an audit. Reproduction during the audit
must inspect the load-bearing evidence and justify the analytic error
bounds, rather than accept the flag or floating-point approximations.

The decisive test remains the asymptotic and strict -2 comparison
in the nominated claim. Validate all load-bearing stages, or exhibit
a concrete error; if a stage remains unresolved, keep L527 unaudited
and record the exact remaining issue. A failed audit would withdraw
confidence in this stop, not establish local absorption or RH. No
repeat creative attempt is approved. The collective overlap/remainder,
missing primes, conditional trace/nullvector premises and Xi transfer
remain independent gaps even on a successful audit.

### Search and overlap record

Reused the completed generic-increment exact/terminology searches
and their known-result/failure comparison. Narrowly checked L526's
hypotheses/conclusion, all of L527, the common-pole generic working
notes and history, and the Sonin/generic stop records. The former
Sonin-only result is a different observable, not a duplicate audit
of this increment. L527's own derivation is the object of review,
not independent corroboration. No matching audited theorem was found
in the reused comparison; no novelty or global impossibility follows.

New query: `site.mat.univie.ac.at/~gerald/ftp/book-schroe "spectral
theorem" "Theorem 3."`. Its result did not supply theorem evidence;
the author's direct PDF did. Unrelated search results were not used.
No external broad search, sibling notebook or API credential was used.
Full matching Mathlib coverage remains unchecked and is not inferred
absent. This comparison approves source scope only; L527's mathematical
outcome and upstream manuscript proofs remain unaudited.
