# Exact-product comparison — audit source assessment

TARGET: Critically audit C645c's fixed-delta rate gap, Euler–Maclaurin remainder, floor bounds and envelope-direction conclusion.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the bounded exact-product search recorded in 2026-11-01-exact-blaschke-product-envelope.md; scoped checks of C645c, L645 (6), C645b, the completion-stripped stop and exact-product histories found the pending audit, not an earlier audit or matching imported comparison. No fresh discovery search or novelty claim.
SOURCE_EVIDENCE: Inspected primary NIST DLMF Section 2.10(i), hypothesis paragraph and full equation 2.10.1 including the finite integral remainder on 2026-11-01; reuse version 1.2.8 citation and the inspected Zakeri Section 8.3 after Example 8.33 plus audited C645b envelope recorded in 2026-11-01-exact-blaschke-product-envelope.md and 2026-11-01-completion-stripped-pick-residual.md.
COMPARISON: The sources cover finite-zero division, the inherited analytic envelope and finite summation with remainder. C645c claims a grid-specific rate above delta/4 and finite-error control; no inspected source certifies that comparison. Its independent elementary specialization audit is within the reused coverage, with no new analytic theorem needed.
GAP: Source scope is ready; independent checking of the scalar kernel comparison, exact rational margin, rescaling, constants and inequality directions remains undone. Actual derivative lower bounds and signs are independent unresolved gaps.
REASON: The separate literature-only review finds the reused coverage sufficient for this unchanged audit target. SPECIALIZE permits a REPRODUCTION audit only; no source reproof or new result is justified. This is gate completion, not acceptance of C645c or a mathematical advance.
SCOPE: Audit only C645c under its unchanged fixed-delta hypotheses and L645/C645b inputs; no new estimate, small-delta uniformity, multiple-zero claim or sign mechanism is proposed.

The completed calculation, still awaiting independent audit, is canonical in C645c; the working note records
its exploratory diagnostics, which are not proof evidence. The main gap
remains actual-Xi signs at unbounded heights and all-degree positivity.
This audit should accept, repair or reject only the claimed removal of
the factorwise rate obstruction. It must not interpret a lower bound
tending to zero as an upper bound on the actual normalized envelope.

Check the identity expressing f(t) as an integral in the d-slot with R
held fixed, the signs on the entire auxiliary rectangle, monotonicity
of 2 arctan(1/R)-1/R, and the exact rational arctangent margin. Replay
DLMF 2.10.1 at m=1, including the removed j=n endpoint, absolute
remainder and n=1 case, then both floor inequalities and the cancelled
epsilon exponents. No endpoint equality in the rate should be assumed.

Essential inputs are L645 (6), audited C645b and the assessed DLMF
formula. L018 is inherited through those inputs; C645a and C644a are
contrasts and must not supply a residual lower bound. No cross-notebook
input. Mathlib coverage of the full comparison remains unchecked.

Continuation test: accept only if the whole fixed-delta interval and
finite-product conclusion survive replay and the final statement leaves
the actual envelope undecided. Any incorrect inequality direction or
uncontrolled error requires correction or rejection. No creative sign
mechanism is nominated merely to satisfy scheduling preferences.

## Completed source-scope review — 1 November 2026

The main gap is actual-Xi signs at unbounded heights/all-degree mixed
positivity. The intermediate target is exactly TARGET above: audit the
claimed removal of one factorwise rate obstruction. A sound comparison
could support later reconsideration of the residual certificate, but
would not supply the missing derivative lower bound or signed control.
This step approves source scope only and performs no mathematical replay.

### Primary statement and applicability obligations

Read [NIST DLMF Section 2.10(i), equation 2.10.1](https://dlmf.nist.gov/2.10#E1),
hypothesis paragraph and entire formula, accessed 1 November 2026.
The existing assessment identifies version 1.2.8 (15 September 2026).
The statement uses integer endpoints with the upper strictly larger,
a positive integer truncation index, and an absolutely integrable even
derivative. It includes both endpoints and a finite integral remainder
involving the periodic Bernoulli polynomial. The remainder is an exact
term, not permission to assume a favorable sign. The unrelated example's
first-omitted-term bound is not an input here.

C645c invokes this formula at index one for F(x)=f(x/n), on [0,n].
Its positive logarithm arguments and smoothness are stated in the proof;
the later audit must check them under the precise fixed-delta hypotheses,
then check derivative scaling, the removed endpoint and n=1. This is a
finite-interval specialization, with no limit interchange or uniformity
as delta approaches zero. The generic source does not evaluate the
specific rate integral or certify the displayed rational margin.

Reuse the already inspected bounded-holomorphic finite-Blaschke division
statement in S. Zakeri, *A Course in Complex Analysis*, author
[Notes and Comments, Section 8.3](https://zakerimath.com/CAbook/COM.html),
complete argument after Example 8.33 (unversioned; previous access
1 November 2026). Its inspected proof handles a selected finite zero set,
removable factors and the maximum principle without boundary continuity.
The precise theorem scope is recorded in the completion-stripped
assessment, lines in its Zakeri source paragraph. L645 (6) supplies the
existing disk/grid specialization; audited C645b supplies the holomorphic
quotient, simple-zero value and envelope uniform in n and P. No renewed
Gonek/digamma review is needed because neither the analytic domain nor
its growth hypotheses change. Do not reprove these imported results.

### Overlap, failures and pending audit

Read the C645c statement and proof, L645's finite-Blaschke input and (6),
C645b's exact-product and audit qualifications, the completion-stripped
attempt stop, and the exact-product source/calculation histories. The
prior exact-product assessment already records its bounded searches and
unread leads; they are reused rather than represented as newly read
sources. The q_delta stopping argument explicitly leaves the exact
product open. C645c is the pending local comparison, not an independently
verified theorem imported from the literature. No duplicate audit was
found in these relevant records. No novelty follows from this check.
C645a's completed maximum and C644a's reserve remain contrasts; neither
is an input bounding this residual from below.

The full mathematical replay remains for a separate research turn:
fixed-R auxiliary integration, signs on the entire parameter rectangle,
strict rational margin, finite-grid error and floors, and the direction
of the normalized benchmark. Accept only the stated qualified result;
repair or reject a failed sign, error bound or inequality direction.
A benchmark below the actual envelope cannot establish its smallness.
This criterion is the bounded continuation/abandonment test, not an
audit verdict. No effective onset, small-delta uniformity, multiple-zero
extension, off-line zero existence or matrix sign is licensed.

Essential continuation inputs: C645c, L645 (6), audited C645b and DLMF
2.10.1; L018 is inherited. Temporary PSD and a stipulated simple rho are
conditional hypotheses, and delta remains fixed in (0,1/2). No
cross-notebook input. Full matching Mathlib coverage remains unchecked;
supporting Borel–Caratheodory coverage is as qualified in L645/C645b.
No lemma, mathematical script, PROOF.md or DAG.md is modified here.

LITERATURE_REASON: The invocation-start REVIEW_REQUIRED nomination needed a separate source-scope decision for the audit of newly written C645c. Existing coverage is reused; the brief primary-formula check resolves that gate without reopening analytic discovery. Further literature on this unchanged target is unnecessary absent a specific new source issue.
