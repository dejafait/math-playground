# Actual Mellin contour prerequisite: audit nomination1621

TARGET: Audit Kawano v1 Lemma5.1's fixed-height Mellin contour continuation on |p|>=e^12, Re p>=-|p|/(4 log|p|), including the principal Lambert branch and continued origin term; stop before saddle-error bounds.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Discovery1621 reused1177/1181/1344 and compared paper23's distinct map nomination508. Source-scope comparisons, but no independent audit of this exact contour step, were found in the inspected paths; no novelty claim.
SOURCE_EVIDENCE: Kawano, Preprints.org202611.0383v1 (4November2026), Section5.1/(25) and Lemma5.1's two contour paragraphs https://www.preprints.org/manuscript/202611.0383 ; NIST DLMF4.13.1/principal-branch analyticity https://dlmf.nist.gov/4.13 . Standard Cauchy deformation, identity theorem and normal-convergence theorems are named inputs; the source contour claim is the object of the audit.
COMPARISON: Known W_0 theory supplies its domain off the cut, not sector-to-strip applicability or continued contour equality. Independent verification of this unverified source prerequisite is justified; no general Lambert theorem or full saddle theorem is to be reproved.
GAP: Sector applicability, complex-strip convergence, continued origin terms and endpoint cases require proof. Full saddle errors, winding counts, inverse density and the mixed-sign bridge remain separate.
REASON: One analytic equality can be checked without certificate artifacts, fitting or scalar budgets. A defect stops this import; success supports only the prerequisite. Expected REPRODUCTION, not creative mathematics or a sign gain.
SCOPE: Exactly TARGET under the original kernel and p coordinate; no archive, quadrature regeneration, parameter sweep or source-theorem import. New ready coverage requires separate next-turn approval; no audit was performed in1621.

## Exact audit boundary

Use source (4)-(5) and its unaltered continuation (25). L019's kernel
is twice source Phi; check normalization explicitly. L016/L019/L048
give real-variable facts only. Establish the needed complex compact
normal convergence from the explicit series, without promoting those
real-variable decay statements into strip estimates.

Put r=|p|, L=log r and w=W_0(2p/pi)=U+iV. In the upper half of
TARGET's closed sector audit 0<=V<pi/2 and y=V/2. Handle y=0
without a shift and the lower half-plane by conjugation. Verify open
neighborhoods wherever holomorphy is used; an uncontrolled asymptotic
formula does not establish the sector claim.

The source fixes y before deforming from Re p>0, then continues the
origin primitive after splitting at min(y,1/4). Audit the small circular
arc, far vertical segment, branches, local uniformity and pole terms,
and equality with (25) also at negative Re p in the target sector.
Do not discard the origin segment or vary y inside an identity-theorem
argument without a fixed-height justification. Do not assume or prove
the quantitative saddle-error inequalities in this step.

The actual theta series is the input. RH, real Mellin zeros, simple
zeros, finite zero data and a positive inverse density are not premises.
Any additional analytic condition introduced by the audit must remain
explicit until justified. Do not import it from the advertised theorem.

## Use and discriminating test

The main gap is L030-L032/C032a. A valid contour is necessary before
assessing a source-supported actual-theta exterior remainder; the
independent Mellin-to-mixed-sign bridge still remains unpaid.

Accept only a complete sector/endpoint/continuation argument. A rigorous
failed branch or uncanceled term stops this source step. Save partial
reasoning if one attempt is inconclusive. Do not widen to constants,
archives or a replacement saddle. A repeat requires a specific new
input or refined test. Paper23's map and angular-collar stops are
contrasts, not mathematical premises or global bans.

Essential local inputs: L016/L019/L048; L030-L032/C032a give relevance
only. No cross-notebook input. Full matching Mathlib coverage is
unchecked/unknown. Recommend proof_audit/conceptual_audit with
deep_research/xhigh for the fixed-contour, moving-sector and meromorphic
origin interaction. No creative or candidate audit is nominated.
