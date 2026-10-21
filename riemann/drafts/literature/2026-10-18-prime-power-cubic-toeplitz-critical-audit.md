# Proposed coverage: audit of the fixed log-2 cubic prefix

TARGET: Critically audit L432's fixed-harmonic cubic coefficients, complete-response passage and exact 5-by-5 Toeplitz certificate.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 223 reused step 221's completed fixed-character/moment discovery, step 213's primary-source comparison and the L409/L430/L431 audit records; compared L432's full statement and source applications with that coverage. No changed hypothesis or new lead requires external discovery; no novelty inference is made.
SOURCE_EVIDENCE: Reused inspected primary records: Milinovich--Ng Lemma 6.1 p. 9 https://home.olemiss.edu/~mbmilino/Lower_Bounds.pdf#page=9; Gonek (1984) section 3 Lemma 2 p. 130 https://www.sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf#page=8; Fazzari 2306.15553v1 (3.5) https://arxiv.org/html/2306.15553v1#S3; DLMF 25.11(i) https://dlmf.nist.gov/25.11#i and 25.11.5 https://dlmf.nist.gov/25.11.E5; Helton--Putinar (2007) Theorem 3.3 pp. 245--246 https://mathweb.ucsd.edu/~toal/READ07/hpSurvey07.pdf#page=17; Yang--Xie 1605.02431v3 Theorem 1 (5)--(15) https://arxiv.org/html/1605.02431v3#S2. Direct locators restored from step-221/213 records in step 224; no fresh retrieval or mathematical verification.
COMPARISON: The ready coverage includes precisely the fixed positive rational parameters and finite Hermitian Toeplitz moment theorem used by L432. The infinite Herglotz theorem only delimits the conclusion. Source scope is adequate for an independent audit, but neither sources nor this comparison validate the changed denominator-grid argument, arithmetic tails or certificate.
GAP: Independently check fixed-rational numerator dependence, every denominator-2^j resonance, both sharp endpoints, response summation, H-first quantifiers, exact local tails and all 31 minors. This source approval is not a mathematical audit of L432.
REASON: Separate source-scope approval is complete for the saved bounded audit; proceed to mathematics using ready coverage, preserving step 222 and stopping at harmonic 4 with no law redesign.
LITERATURE_REASON: The supervisor requires separate approval of the newly proposed audit assessment; reuse adequate coverage rather than repeat discovery or derive mathematics during this literature-only turn.
SCOPE: Only L432 at j=0,1,2,3,4 with the complete actual physical product; finite-prefix compatibility, not positivity of the infinite sequence, bounded density, a new law, actual clipping or RH.

The main gap remains global mixed positivity. The intermediate audit
would validate or delimit the finite-prefix input and its analytic
specialization. Its plausible downstream use is to record exactly why
the bounded positive-measure obstruction test is inconclusive, without
spending another turn increasing its cutoff. Continue to validate the
claimed scope if every source application and exact check holds; repair
or delimit any specific defect. Finite positive minors never settle the
infinite Herglotz condition.

Essential canonical inputs are L406--L409, L421, L429--L431. Read only
the relevant input proof ranges after the overview and DAG. The pending
result is `lemmas/L432-fixed-log-two-cubic-toeplitz-prefix.md`; its exact
script and full certificate are
`scripts/discriminant/prime_power_cubic_toeplitz.py` and
`scripts/discriminant/prime_power_cubic_toeplitz_certificate.json`.
The proof's infinite-tail reduction, not a finite numerical sample,
must justify its rational B_j values. Check the transition indices in
(12), c_0 and the audited c_1, the odd-factor cancellation, field-pair
determinants and independent rational congruence computation.

For the analytic part, check fixed j before H, normal convergence on
the full contour rectangle, explicit response-summable frequency errors,
the minimum nonzero denominator-grid distance, every integer resonance,
both connectors, absolute physical replacement and sequential limits.
Check reflection of cosine measures without assuming actual sine
coefficients vanish. The high and complete signed bulk comparisons use
different absolute bounds; no expectation-of-absolute-cubic replacement
is permitted. L427/L428/L430's narrower stops and audited L431 remain
valid; C426c/core-tail stays parked.

Actual/global critical-function realization, actual clipping, capped
nondegeneracy, L413's full-error regulator margin and global mixed
positivity remain unresolved. Full matching Mathlib coverage is
unchecked. This proposal supplies no fresh mathematics,
independent verification or claim of originality. The completed source
approval below supersedes the proposal's pending approval language.

## Completed source-scope comparison — 2026-10-18, step 223

This LITERATURE / NOVELTY_UNCHECKED / literature_comparison step is
STALLED: it confirms ready coverage and makes the audit actionable,
without new mathematical or source evidence. No lemma or mathematical
script is written or replayed. Mathematical exploration usage stays
0 of 3. The completed step-222 result is preserved pending audit.

### Reused evidence and exact applicability

Read the complete step-221 assessment and step-213 comparison, the
step-221/222 histories, L432 and the relevant L408 rational-interface,
L409 step-119 and L430 step-216 audit passages. Step 220 records the
independent L431 audit. These cover the unchanged source versions and
parameters; the present task does not seek a new theorem or expand
the target. No cross-notebook result is used.

The direct primary locators, hypotheses and proof cases are retained in
[step 221's assessment](2026-10-18-prime-power-cubic-positive-measure-test.md)
and [step 213's comparison](2026-10-18-prime-twisted-cubic-counterlaw-comparison.md).
They are inspected-source records being reused, not sources freshly
read this turn and not unread leads. In particular:

- Milinovich--Ng Lemma 6.1 allows x>0 with abscissa in a fixed compact
  subinterval of (0,2], including the endpoint-transition denominator.
  Gonek section 3 Lemma 2 supplies the interior, endpoint and exterior
  saddle cases. The later GRH application is excluded. The audit must
  verify the response-summed application and both connectors; the
  primitive theorem alone does not supply them.
- Fazzari v1 (3.5) supplies the finite progression identity with coprime
  additive numerator/modulus and all residue classes. DLMF's residue-one
  pole and continuation require positive progression parameter, with
  Re s>0 away from 1 for the cited continuation formula. L408 supplies
  the local ordinary-jet and smooth-first sharp-transfer application.
  No sharp indicator is inserted in Fazzari's Schwartz-weight theorem,
  and the previously excluded expanded polar display stays excluded.
- For j=0,...,4 the source parameters listed by L432 are fixed positive
  rationals before H grows. The original analytic weights and derivative
  orders are unchanged. Constants may depend on j. Coverage does not
  import a theorem uniform in growing j, or license summing arbitrary
  fixed-rational error constants. L430's frequency-level bounds are the
  relevant existing interface, whose changed application needs audit.
- Yang--Xie v3 Theorem 1 covers finite Hermitian PSD Toeplitz matrices,
  including full rank by its rank-one-subtraction proof (5)--(15).
  Full rank does not give a unique measure. Its Fourier convention and
  mass c_0 must be matched, and cosine reflection must be justified
  without assuming vanishing actual sine coefficients. Helton--Putinar
  Theorem 3.3 requires every finite section for the infinite sequence;
  it cannot upgrade the single 5-by-5 section.

### Remaining audit and decision test

The sources do not calculate B_j, check transition indices in L432 (12),
or certify any determinant. Exact geometric-tail algebra and finite
rational/field arithmetic are local verification obligations, not a
general moment-theorem reproof. The next audit may inspect the saved
script and complete load-bearing certificate fields and replay its
finite checks; this turn deliberately does none of those checks.

Compare c_0 and c_1 with audited L409/L431, check the positive finite
odd factor before cancellation, all j and -j tails and both determinant
methods. Analytically check normal convergence, every denominator-grid
resonance, full-tail majorants, both sharp endpoints and fixed-head
sequential limits. Retain L406's absolute physical replacement. For
relevance retain L421's high absolute bound and L430's absolute value
of the complete conditional signed bulk; they are different bounds.

Recorded failures are already compared in step 221: L427's fixed
mixture, L428's uniformly bounded bulk and L430's unchanged-law mismatch
do not rule out all positive measures. Audited L431 matches the first
harmonic. The prefix passing in step 222 ends the bounded search; an
audit is not permission to raise the cutoff. C426c/core-tail stays parked.

Continue only to the exact saved critical audit. If every obligation
holds, record validation of finite-prefix compatibility alone; if an
error or uncontrolled contribution is found, repair or restrict that
specific claim and preserve the original evidence. No infinite measure,
bounded density, new law, actual clipping, capped nondegeneracy,
critical-function realization, full-error regulator margin or RH
conclusion follows. Full matching Mathlib coverage remains unchecked.


## Direct-source metadata recovery — 2026-10-18, step 224

The supervisor reported that the ready assessment lacked a direct source
URL. Restored the primary URLs above from the narrowly reread step-221
and step-213 source records, retaining their exact versions, theorem
locations and applicability qualifications. These are reused inspected
sources, not freshly retrieved sources or unread leads. No discovery,
new theorem comparison, derivation or certificate check was performed.
The scope and SPECIALIZE decision are unchanged. The prior approval's
missing direct locators were a documentation defect, not evidence that
L432 is valid or invalid.

This LITERATURE / NOVELTY_UNCHECKED step has ACTUAL_TASK_TYPE metadata
and outcome STALLED: it repairs the reported process issue without
mathematical progress or new source evidence. LITERATURE_REASON is the
required direct-URL recovery, not additional discovery on a ready target.
The main gap, bounded intermediate audit, downstream use, continuation
and defect-delimitation tests above remain unchanged. In particular,
retain essential inputs L406--L409, L421 and L429--L431, all unresolved
realization/clipping/regulator assumptions, and the harmonic-4 stop.
Mathematical exploration usage stays 0 of 3. The exact next action
remains the independent L432 proof audit; no lemma, mathematical script,
DAG or PROOF change is authorized by this metadata repair.
