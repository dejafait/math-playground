# Repaired rank-two certificate audit — completed source comparison

TARGET: Critically audit L779's repaired (3,2048) certificate, including enlarged evaluator, contour counts, independent phases and signed determinant/norm transfer.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step438 compared the three ready assessments named below with L779's changed proof obligations, L777's hypotheses/error scope, L778's earlier audit scope, the repair implementation and steps435/437 failure/history. Targeted primary retrieval checked Bornemann's general versus selfadjoint perturbation cases, Johansson's analytic-box/Cauchy/counting scope and DLMF's integer De Moivre case. No general Fredholm rediscovery or certificate execution.
SOURCE_EVIDENCE: Reuse the inspected Duits AppendixA Lemmas66/69, NIST Taylor/periodicity identities and Python/mpdecimal contracts from steps432/434/436. Directly rechecked Bornemann 0804.2543v2 Section2 p.7 and Section4 (4.1) p.12/Lemma4.1 p.13; Johansson 1802.07942v1 Section2 p.2 and Section4 pp.7–8; DLMF 4.21.2–3/34 including integer n. Exact applicability and read limits below; no essential source is blocked.
COMPARISON: Existing general methods cover independent scrutiny of the enlarged compact-domain evaluator, two counted/grouped zeros, all integer-index phases, finite-rank signed pairing and original-norm/trace transfer. The new domain and second pole require fresh audit of constants and hypotheses, not a new theorem. Sources and L778's radius1600 audit do not certify L779's repaired numerical intervals.
GAP: Source scope is ready for the exact conceptual audit; the analytic/implementation audit remains unpaid. Check every enlarged tail/domain, complete homotopy/count, removable derivative/residue, factor lower bound, both negative modes, all phase/alias errors, full HS-to-trace cross term, both Grams and separate trace-norm bounds. Installed backend attestation and full Mathlib matching remain unchecked.
REASON: The starting source-review action is completed. A later bounded conceptual audit can decide whether the first fixed signed separation is trustworthy before mechanism development; no new estimate or mathematical derivation is claimed here. Preserve the completed repair and earlier failure evidence.
LITERATURE_REASON: Critical review of the radius4096 rank-two repaired certificate is a changed target from its implementation and the earlier radius1600 rank-one audit. This step compares those changed obligations with ready primary coverage; no repeat general literature search is needed.
SCOPE: One later independent proof_audit/conceptual_audit at the unchanged (3,2048), sigma=9/8, L=2048, N=512, precision75 settings. No sweep, refinement, new sign theorem, growing-order result or RH candidate audit. This newly readied continuation is available for the supervisor's separate approval; it was not executed in this literature turn.

## Completed source comparison — step438

The reviewed starting action was: Assess source coverage for critically auditing L779's repaired (3,2048) certificate, including enlarged evaluator, contour counts, independent phases and signed determinant/norm transfer.
The TARGET above names the resulting ready mathematical continuation.
This is source-scope approval only; no saved endpoint was reverified.

The main gap remains actual-Xi all-degree mixed positivity. The intermediate
target tests whether the fixed positive determinant with original norm>1
survives independent analytic scrutiny. Its downstream use is deciding
whether signed interaction estimates have a trustworthy local benchmark.
Growing-order signed bounds, actual reciprocal-factor budgets, admissible
indices/multiplicities and exceptional signs remain independent open gaps.

### Reused primary coverage and precise qualifications

Read the complete ready assessments in this directory:
`2026-11-04-independent-phase-rank-two-repair.md`,
`2026-11-04-signed-rank-two-fredholm-diagnostic.md`, and
`2026-11-04-actual-fixed-pair-certificate-audit.md`.
Their prior searches and inspected theorem/proof cases are reused while
the corresponding assumptions remain unchanged. No novelty is inferred.

1. F. Bornemann, *On the numerical evaluation of Fredholm determinants*,
   [arXiv:0804.2543v2](https://arxiv.org/pdf/0804.2543v2), Section2 p.7,
   Section4 (4.1) p.12 and Lemma4.1 p.13, directly read. The product
   of two Hilbert–Schmidt operators is trace class with product norm
   control; bounded projections obey the ideal inequalities. Formula
   (4.1) bounds determinant differences for arbitrary trace-class
   operators on the same Hilbert space using their trace-norm difference
   and the maximum of their two trace norms. This covers the intended
   T=-A, S=-Ahat comparison if all those inputs are certified. Lemma4.1's
   positive-selfadjoint base with largest eigenvalue<1 and small-perturbation
   assumptions are excluded; its proof was located to check that distinction.
   Neither an operator-norm error nor the asymptotic (4.2) suffices here.
2. M. Duits, *Determinantal point processes*,
   [author DPP2 PDF](https://people.kth.se/~duits/static/media/DPP2.44e051d148b79af222fa.pdf),
   AppendixA Lemma66 p.51 and Lemma69 p.52/proof: reuse step434's inspected
   finite-dimensional reduction, including dependent columns. Apply only
   its finite-dimensional algebra to the factors in L777/L779; do not
   extend a finite-measure point-process premise to counting measure.
   Retain the adjoints required by the opposite inner-product convention.
   This source was not downloaded again in step438.
3. F. Johansson, *Numerical integration in arbitrary-precision ball arithmetic*,
   [arXiv:1802.07942v1](https://arxiv.org/pdf/1802.07942v1), Section2 p.2
   and Section4 pp.7–8, directly read. A valid complex box evaluation
   encloses the function on the whole box, and analyticity must hold on
   the region used for the error estimate. Section4 gives Cauchy-coefficient
   and argument-principle applications. L779 uses elementary Taylor
   integration and a polygon homotopy, so its own Cauchy disks, remainders
   and nonvanishing boxes must be proved; the paper's Gaussian algorithm
   is not being imported as an unexplained implementation guarantee.
4. NIST DLMF, [4.21.2–3 and 4.21.34](https://dlmf.nist.gov/4.21), directly
   checked for the addition formulas and integer n case, including
   negative integers. Reuse step436's inspected 4.14.3/8–9,
   4.19.1–2, 4.20.1–2 and 1.4.35–37 real Taylor hypotheses/remainders.
   They cover real rational-angle phases and exact integer periodic
   indexing, with finite arithmetic errors retained. Fractional/complex
   exponent qualifications supply no needed input. Step436's v1.2.8
   source identification is retained; no new release-specific claim is made.
5. Reuse step432's Python3.15.2 Decimal, mpdecimal4.0.1 and pinned CPython
   context/exp/sqrt contracts, as detailed in the ready audit assessment.
   The repair imports the old directed primitives and adds exact integer
   modular indexing and interval arithmetic, with the same exp/sqrt
   operations for final transfers. It introduces no new transcendental
   primitive requiring another backend source search. Correct rounding
   still depends on the stated contracts, exponent/finiteness conditions
   and allcr=1; neither source coverage nor a checker PASS attests the
   installed executable. No formal backend proof is claimed.

The named Cauchy integral formula/estimates, argument principle,
winding homotopy invariance, intermediate value theorem and finite
Fourier orthogonality already cover the remaining standard machinery.
Only their application and elementary estimates need auditing. A general
source for each numerical constant is not required and would not verify it.
No source reproof or stronger theorem discovery is justified.

### Changed obligations mapped to the existing methods

- **Enlarged evaluator:** L017/L018/L021 fix actual-G normalization.
  Johansson's scope and the named Cauchy estimates cover inspection of
  the radius4096 evaluator, all moment/cosh/theta/infinite-u tails,
  coefficient errors, contour Taylor disks and derivative disks.
  L778's radius1600 estimates are implementation experience only; none
  is an error bound on the enlarged domain. All new constants remain
  to be checked against the actual code and full evidence.
- **Two contours and true grouping:** both complete circles2048/2304
  require whole-segment enclosures, common polygon endpoints and a
  zero-free homotopy. The argument principle counts multiplicity;
  disjoint strict real brackets must be combined with those counts
  before concluding simple real grouping. A width goal or approximate
  root list is not a grouping hypothesis. Check the removable derivative
  normalization and complete root/residue uncertainty at both roots.
- **Reciprocal and Fourier input:** the larger zero-free factor disk and
  positive whole-circle lower bound are inputs, not consequences of
  samples. Check both negative Laurent indices -2,-1, the actual Laurent
  annulus and absolute convergence before finite Fourier averaging.
  The NIST identities cover exact modular phase indices; every reduced
  angle, trig enclosure and shared uncertainty must still be enclosed.
  All512 complex coefficient intervals, aliases and the infinite weighted
  tail matter, even though phase uncertainty was the repaired mechanism.
- **Signed determinant and norm:** reuse L776's audited conditional
  identity and L777's audited factorization/error scope. Duits covers
  the signed finite pairing; both Gram metrics are needed for the
  original norm, including singular-support cases. Bornemann covers
  the full trace-class transfer only after the separate HS factor
  bounds, retained cross term and both trace-norm bounds are checked.
  L777's operator-error statement alone is insufficient. Recheck the
  directed exponential in the final determinant radius, not just the
  rational finite-data checks.

These are explicit obligations for the later audit, not new lemmas or
mathematical deductions from step438. The unchanged actual conditional
inputs and complete evidence are listed in the preserved nomination below.

### Duplicates, failures and decision test

Read L779's relevant proof and repair in full, L777's hypotheses and
full-product/audit scope, L778's earlier audit ranges, the repair's
`fourier` implementation, steps435/437 histories, and
`ATTEMPTS/2026-11-04-signed-rank-two-recursive-power-certificate-failure.md`.
The earlier recursive implementation's wrapping failure remains stopped;
its independently indexed replacement does not reopen that same mechanism.
The root-width assertion and checker typo remain recorded, with no earlier
failure silently promoted to proof. A finite-data PASS is not an analytic audit.

Step434's inspected Michalowski 2607.16795v1 Section1.2 already records
low-order nonnegativity covering order3. Reuse that overlap assessment;
this audit cannot claim a new low-order sign theorem. The shifted-boundary
and q-Pascal stops have the different scopes already compared there and
are not global bans on this fixed signed diagnostic. No cross-notebook
input was read; full matching Mathlib coverage remains unchecked.

The audit passes only if all essential analytic and implementation
hypotheses are valid AND the actual determinant lower endpoint>0 and
original norm lower endpoint>=1 survive. A concrete tail/domain,
contour/grouping, residue, phase/alias or trace/determinant-transfer defect
reopens the affected claim; crossing a threshold is inconclusive.
Preserve the completed calculation and every earlier certificate. No
precision, radius, degree, resolution sweep or automatic refinement.

Coverage is SPECIALIZE, not IMPORT of the actual numerical conclusion:
the sources supply methods, while the certificate-specific proof audit
is still required. No essential source remains blocked. No lemma, script,
new estimate, numerical replay, DAG or PROOF change was made this turn.
The source-scope comparison is EXPLORATION, without a mathematical advance
or a charge to the mathematical exploration budget. It changes a pending
coverage decision into one concrete ready audit, rather than repeating
an already completed audit decision.

A protected creative central nomination is not justified by this source
review: the fixed benchmark is still independently unaudited and no
independently paid growing-order signed/reciprocal budget has been supplied.
Complete this essential audit before choosing a new central mechanism;
do not label the present established-method scrutiny creative.
The next mathematical task is proof_audit/conceptual_audit,
deep_research/xhigh, because domain/tail, homotopy, Laurent and trace-ideal
logic interact. It is not a complete-solution candidate audit.

Retrieval record: direct primary URLs and within-source searches for
Bornemann `(4.1)`/`Hilbert–Schmidt`, Johansson `d = 1`/`argument principle`,
and DLMF `4.21.34`; the relevant statement ranges and excluded cases
were opened. No search snippet, new broad web query, unread lead or
numerical preview is evidence for approval. Other primary coverage is
explicitly reused from the three named ready assessments.

## Original nomination — step437 (historical requirements preserved)

The proposed mathematical audit, after its source gate, should examine
L779's complete repaired proof and all essential analytic hypotheses.
Its inputs are L017/L018/L021/L776/L777/L778/L779, the radius4096 entire
evaluator, both complete count2 contours, strict simple grouping and
residues, all2048 samples/phases and all512 complex coefficient/error
records. Preserve the inherited step435 width-assertion failure and
recursive-power route stop. No zero list, RH, desired sign, hidden
reciprocal estimate or cross-notebook theorem is permitted.

The exact mathematical threshold remains actual determinant lower>0
and original norm lower>=1. Current complete arithmetic checks support
both, but acceptance as audited requires the enlarged tails and domains,
whole-contour homotopy/counts, removable derivative normalization, F lower
bound, both negative-mode exclusions, uniform trig/phase-index containment,
all aliases and tails, full HS-to-trace product with cross term, signed
pairing and both Gram metrics. Check Bornemann's nonselfadjoint hypotheses
and the two separate trace-norm bounds, not its excluded sharper lemma.
An actual defect reopens the affected conclusion; crossing thresholds
is inconclusive. No precision/radius/degree/resolution sweep is authorized.

Complete calculation artifacts are
`scripts/actual-fredholm/independent-phase-certificate-437.json` and
`scripts/actual-fredholm/independent-phase-check-437.json`.
They are evidence for scrutiny, not substitute proofs. The full matching
Mathlib theorem is unchecked. A later successful critical audit would
validate known-method local progress, not imply any all-degree result.
When approved, route that delicate analytic scrutiny as
proof_audit/conceptual_audit, deep_research/xhigh; this nomination itself
routes the immediately next source comparison as standard/high.
