# C997y independent conceptual audit — source scope approved in step394

TARGET: Critically audit C997y's exact germ extractor, contour-uniform propagation bound and fixed-disk scalar-prior obstruction, including all constants and the distinction from a bound on the optimal capped residual.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse review391's unchanged origin-moment source scope and step392's separate approval, together with review390's exact/stronger-result searches and scoped C997-family failure comparison; no new search or novelty claim is made for this audit.
SOURCE_EVIDENCE: Step394 directly rechecked Trefethen BIT60(2020) Lemma2.1/proof p904, Theorem3.1/proof pp904-905 and Theorems5.1-5.2/proofs p908, https://people.maths.ox.ac.uk/trefethen/trefethen_ac.pdf ; DLMF https://dlmf.nist.gov/1.9.E31 , https://dlmf.nist.gov/1.10.viii , https://dlmf.nist.gov/18.5.E12 ; prior contracts and comparisons remain reused.
COMPARISON: Standard analytic tools support an audit of C997y's kernel-specific derivation but do not supply its growing-order inverse norm, explicit propagation constant or scoped certificate limitation. C997w/x remain comparator/family stops, not all-coefficient inputs to C997y.
GAP: Independently check C997y's proof and complete relevant evidence, especially exact lower-window cancellation, local nonvanishing, all-n constants, uniform slit-disk/annular propagation, and whether the scalar-envelope comparison is stated only as a certificate limitation.
REASON: Separate literature-only step394 approves the unchanged audit target after rechecking primary contracts and the scope of C997y; no mathematical claim is validated. Further source review is unnecessary unless the audit identifies a changed hypothesis or essential missing input.
SCOPE: Exactly C997y's original n, complex cap, frequency grid, complete kernel, m=ceil(sqrt(n)), Omega=|c-1|<3/2 and |c|=1/n contour; independent audit only, with no changed gauge/domain, new inverse mechanism, general-band obstruction or actual-Xi conclusion.

## Reused primary contracts and audit cases

The pre-invocation source assessment
[review391](2026-11-11-slope-origin-moment-test-review-391.md), approved
separately in step392, supplies the complete primary-source contracts.
The DLMF live text was checked 11 November 2026; release identifier was
not independently verified. Trefethen is the published 2020 author PDF.
No essential source blocker is currently identified. Full matching
Mathlib coverage remains unchecked and is not inferred absent.

Audit the actual C997y statement, not merely its proof preview or its
finite rational diagnostics. In particular:

1. The fixed-parameter integral must justify entire extension before
   complex c is used. Check the sign and factor in D=-exp(nc/4)R/2,
   the constant lower window, every b_k and the Cauchy order.
2. Use the full finite Laguerre formula, including its subtraction.
   Check g(0), the local zero-free radius, the inverse coefficients,
   centered-frequency factorials and the original complex l1 cap gap.
3. Check the complex-t envelope against both windows, the target
   growth, both cosh terms and the gauge. The real-t Laguerre bound
   must not be used as a complex-t estimate.
4. Verify the slit-disk branch/barrier, endpoint continuity, all sixteen
   annular steps and coverage of the WHOLE shrinking contour. Trefethen's
   pointwise existential theorem cannot substitute for these constants.
5. For the unavoidable scalar prior, check the rotated negative-t phase
   interval, the lower-window subtraction, the n>=20 threshold and the
   passage from the boundary point to the supremum on open Omega.
6. Check that polynomial witnesses constrain the generic analytic
   exponent only, and that the comparison bounds the strength of the
   displayed certificate, not E_n from above. A=0's global growth is
   not automatically a growth lower bound for a minimizing residual.

The essential local mathematical inputs are C997c's exact complete kernel
and audited real-t bound, and C997s's original cap/grid/objective.
C997w/x are scope contrasts. No cross-notebook input is proposed. The
finite certificate at `scripts/adaptive-slope/slope-origin-check-393.json`
records diagnostic checks, not a rigorous all-n substitute for the proof.

Accept only with the weaker rate, the scoped stop and its hypotheses
intact; otherwise identify and repair the exact invalid claim or leave
it unresolved. All actual-Xi positivity, L966/L968 forcing, L984(H),
C997a(8), selected/both-sign transfer, assay/reconstruction,
complements/regulators and L993 remain open regardless of this audit.
This source-scope nomination does not reopen the parked scalar-prior
construction or authorize a repeated attempt to optimize the same bound.


## Separate source approval — step394, 11 November 2026

LITERATURE_REASON: The supervisor requires separate approval of the newly
prepared audit assessment; this is a source/scope gate, not renewed discovery.
The target and EXPLORE decision are unchanged. Outcome STALLED: this confirms
coverage already prepared in step393 and supplies no new mathematical evidence.

Directly rechecked the published author PDF cited above: Lemma 2.1 uses a
bounded analytic strip function and a uniform boundary limsup. Its proof
invokes bounded-strip Phragmen–Lindelof. Theorem 3.1 and its proof use a
logarithmic strip map for concentric disks, with exponent
1-log(r)/log(R); the sharpness examples are integer powers along a sequence
of data sizes. Theorems 5.1–5.2 and proofs retain the continuum and
non-enclosure assumptions; boundedness yields a point-dependent exponent.
These results justify the standard tools, not C997y's disk containment,
slit comparison, chain count or contour-uniform numerical constant.
In particular, audit every disk against the exact prescribed Omega before
using the scalar bound; entire extension alone does not extend that bound.

Rechecked DLMF 1.9.30–31 with the surrounding contour hypotheses and
positive orientation; the derivative factorial must be retained.
DLMF 1.10(viii), equation 18 and following text require joint continuity
and parameter analyticity on a fixed finite real segment; improper
integration additionally requires compact-uniform convergence.
DLMF 18.5.12 supplies a finite Laguerre polynomial expansion at integer
degree, applicable to degree n+1 and alpha=2. Complex-variable use of its
finite polynomial identity requires no asymptotic extension. None supplies
the local inverse norm or permits dropping the separate constant subtraction.
DLMF live pages were retrieved today; the release identifier remains unverified.

Read C997y's full hypotheses/conclusions, source paragraph and explicit
propagation section to match source scope, without auditing their correctness.
Reuse review390's searches and duplicate/failure comparison, review391's
approved scope, step392's source record and the preserved step393 stop.
No additional broad search is warranted for this unchanged audit. Unread
leads in review390 are not inputs. Full matching Mathlib coverage remains
unchecked; no absence claim is made. No lemma or mathematical script changed.

Approved continuation: perform the exact TARGET once as a conceptual audit,
using the six cases above and the complete relevant canonical proofs and
certificate evidence. Retain only claims surviving their exact hypotheses;
repair a demonstrated error or leave it unresolved. Do not optimize the parked
certificate or infer an upper bound on E_n. Main-gap and independent unresolved
inputs remain as recorded above. No PROOF or DAG update is warranted by this
gate approval. The preceding nomination text records the pre-approval state.
