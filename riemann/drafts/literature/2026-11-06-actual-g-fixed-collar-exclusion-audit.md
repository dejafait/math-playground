# Approved source coverage for the actual-G fixed-collar exclusion audit

TARGET: Audit L844's eventual exclusion of nonzero stationary points for the actual-G angular density with k=r-1 in the closed collar, checking the coordinate-specific zero-sum identity, uniform complex derivative bound and both boundaries.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the unchanged exact-collar assessment 2026-11-06-actual-g-sector-collective-saddle.md and its collective-saddle/electrostatic comparisons. Read L844 and the exact L018/L775 input passages, plus the fixed-collar attempt and history records; no duplicate audit was located there. Opened primary DLMF 5.11, 5.2(i), 25.2(i) and 25.4 for the required analytic hypotheses. No new general-theorem search or novelty claim; this approves coverage, not the proof.
SOURCE_EVIDENCE: Inspected NIST DLMF v1.2.8 (2026-09-15), 5.11.2 with the shared closed-sector condition and the first paragraph of 5.11(ii), 5.2(i)/5.2.2, 25.2.1 and 25.4.4. These cover the digamma remainder, Gamma nonvanishing, Dirichlet-series domain and exact completion; L775 supplies the actual G and scalar-radius interface. Precise scope and unread references are below.
COMPARISON: Standard gamma and zeta inputs support L844's sector specialization but do not themselves state its coupled stationary-point exclusion. The audit must test the exact weighted identity and the uniform positive-real-part argument, rather than invoke generic electrostatics or a contour theorem.
GAP: L844's local proof is not independently audited; its coordinate convention, cancellations, analytic uniformity, common eventual threshold and boundary/nonzero qualifications require review. No Hessian estimate, sign transfer or conclusion outside the specified collar is claimed.
REASON: This separate source-gate review approves the unchanged conceptual-audit target: its essential analytic inputs are accessible and adequate. The local exclusion still needs independent mathematical verification before its route stop is treated as audited; no source states that exclusion.
SCOPE: One conceptual audit of L844's stated exclusion using L018/L775 and the cited standard analytic inputs. Do not widen the collar, change k, insert a measure Jacobian, replace G, or turn this into a minor-sign or contour-existence theorem.
COVERED_TARGET: Audit L844's eventual exclusion of nonzero stationary points for the actual-G angular density with k=r-1 in the closed collar, checking the coordinate-specific zero-sum identity, uniform complex derivative bound and both boundaries.

## Existing coverage and precise primary input

The preceding assessment is
`drafts/literature/2026-11-06-actual-g-sector-collective-saddle.md`.
Its exact object, factorials and collar are unchanged. The new target
is critical verification of the resulting local exclusion, not a new
existence search. Its Katkova/Pemantle–Wilson/Stieltjes comparisons are
reused only at their recorded scope; no generic-field or fixed-dimension
theorem is imported into L844.

[NIST DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2), together with
[the sector hypothesis](https://dlmf.nist.gov/5.11#i) and
[complex remainder bounds](https://dlmf.nist.gov/5.11#ii), gives the
digamma expansion in closed sectors away from the negative real axis.
The current attempt read the theorem-level formula, its shared sector
condition and the relevant remainder paragraph. The site cites
Olver (1997), pp. 87–88 and 293–295; that book was not separately read.
This is the only directly imported derivative asymptotic. L844 derives
the actual-G specialization from the exact completion, and bounds the
zeta term using the absolutely convergent Dirichlet series, with no
differentiated real-axis error term. These details are canonical in
L844, not independently verified by this assessment.

## Bounded audit and decision

Read L844 in full, then only needed L018/L775/source passages. Check
the angular derivative and sine-to-rational identity without a measure
change; the pairwise cancellation must give the printed zero sum
precisely when k=r-1. Check all constants/dilations in s=(1+sqrt(z))/2,
the nonvanishing conditions, principal logarithms, and uniformity of
the O(1) error through both angular boundary faces. Verify that the
lower radial face also tends uniformly to infinity, that one onset
works for all later r, and that collision points are outside the
nonzero premise. The claimed result excludes all such stationary
points, so a missing Hessian calculation is not by itself a gap.

Accept the scoped exclusion only if these obligations follow. Otherwise
record the first actual defect and either repair it within these
hypotheses or retain the unresolved estimate. This audit supplies no
sign of any minor and no assertion about a different measure, wider
sector or saddle outside the collar. Mathlib matching coverage is
unchecked; no cross-notebook input is needed. Source coverage is now approved for exactly TARGET under DECISION: EXPLORE.
The next turn should execute the conceptual audit, reusing this assessment
without another literature approval. The proof remains unaudited until
that mathematical step is completed.


## Separate source approval, 2026-11-06

This turn is literature-only. Reading the existing proof identifies its
source obligations; it does not verify its cancellations, estimates or
conclusion. The prior source comparisons remain adequate because neither
the target nor its hypotheses changed. The named attempt and history
record preserve the collar-existence stop pending audit; they are not
independent verification. No new mathematics or mathematical script is
part of this approval.

All DLMF pages inspected identify version 1.2.8, released 2026-09-15.
The directly inspected statements are:

- [5.11.2 and 5.11(i)](https://dlmf.nist.gov/5.11#i): the digamma
  Poincare expansion uses the principal logarithm and the shared fixed
  closed sector away from the negative real axis.
- [5.11(ii), first paragraph](https://dlmf.nist.gov/5.11#ii): after
  truncation at k=n-1, the complex digamma remainder is bounded by
  the magnitude of the first omitted term multiplied by
  sec^(2n+1)(arg(w)/2). The positive-real same-sign remainder case
  alone would not cover this target. The angular bound on w used
  in L844 must be checked in the audit; it is not supplied by DLMF.
- [5.2(i) and 5.2.2](https://dlmf.nist.gov/5.2#i): Gamma has no zeros,
  has poles only at the nonpositive integers, and psi=Gamma'/Gamma
  away from those poles.
- [25.2.1](https://dlmf.nist.gov/25.2.E1): the defining zeta Dirichlet
  series holds for Re(s)>1. This is not a source for L844's printed
  numerical reciprocal bound or its differentiated-series estimate;
  those remain local proof obligations.
- [25.4.4](https://dlmf.nist.gov/25.4.E4): the exact completion is
  xi(s)=s(s-1)Gamma(s/2)pi^(-s/2)zeta(s)/2. Local L018 states the
  needed right-half-plane identity.

Only theorem-level DLMF statements and the relevant real/complex
remainder cases were needed. Olver's book, cited by DLMF at pp.87–88
and 293–295, was not independently read; it is not an additional
verified premise. No proof cases from the unused electrostatic or
contour theorems are needed, since none is imported.

Local L775's scalar-radius paragraphs state existence, uniqueness and
R_k tending to infinity using the positive-coefficient interface. The
audit must inspect that argument as needed, without reopening its
independent absolute-complement bound. L844's uniform O(1), the exact
weighted zero sum, one eventual onset, all boundary qualifications and
the density-versus-measure convention remain explicitly unaudited.
No full matching Mathlib theorem was checked.

Decision: retain EXPLORE for the bounded conceptual audit. IMPORT would
misdescribe its scope: the standard sources provide supporting inputs,
not the coupled exclusion. Approval is process progress only and does
not establish a new theorem or novelty. Accept the exclusion only after
the stated audit tests succeed; on a genuine defect, preserve the
proof and record the first failed obligation for repair or rejection.
