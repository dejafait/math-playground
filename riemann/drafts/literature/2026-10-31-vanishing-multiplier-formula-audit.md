# Vanishing-multiplier coefficient formula: bounded audit nomination

TARGET: Audit Flajolet--Sedgewick's Note VIII.37 vanishing-multiplier coefficient formula at A(z)=z-1, B(z)=exp(z), N=n, comparing exact coefficients with O'Sullivan v2 Corollary 5.1 before any actual-Xi transition application.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed vanishing-amplitude review's exact theorem/stronger-expansion searches and primary reading; narrow saddle assessment/attempt/history searches found no prior audit of VIII.37 or O'Sullivan 1702.03777. Checked the author's June 2010 errata for the relevant page/note; no matching entry found, without an exhaustive errata claim.
SOURCE_EVIDENCE: Flajolet--Sedgewick, https://ac.cs.princeton.edu/home/AC.pdf, running date 3 October 2008, conditions L1--L3/Proposition VIII.7/Theorem VIII.8 and proof pp.586--588, signed extension/Note VIII.37 p.589 (prior primary reading reused); O'Sullivan https://arxiv.org/html/1702.03777v2, Assumptions 1.1, (1.7), Corollary 5.1 and proof, Section 4 (primary hypotheses/coefficient rule and Corollary rechecked 2026-10-31).
COMPARISON: The known complete expansion and elementary exponential-series coefficients supply an independent test of the short fixed-multiplier formula. This is verification of a suspect source input, not a new expansion or an actual-Xi theorem. The original nonnegative-A hypothesis must be distinguished from the note's explicit vanishing/signed extension.
GAP: Determine whether the stated short formula, its intended extension and the exact model agree; if not, isolate the mismatch without deriving a general replacement. No coefficient computation or correctness verdict was made in preparing this nomination.
REASON: A bounded exact-model test is independent of the unavailable Xi quotient estimates and can prevent a false signed-leading-term import. The separate literature recovery turn has now repaired direct source attribution and checked readiness; the exact mathematical audit remains unperformed.
SCOPE: One fixed elementary coefficient model, integer n tending to infinity, a simple amplitude zero, and the stated source formula only. No arbitrary-multiplicity or moving-height uniformity theorem, no changed Xi assumptions and no sign claim for Xi.

The main RH gap is actual-Xi all-degree mixed positivity, especially
initial indices at unbounded heights. The intermediate target is the
correctness of a candidate source coefficient formula at a vanishing
amplitude. Its downstream use is a reliable source basis for a later
signed transition; the Xi remainder and contour bounds remain wholly
independent and unproved. This audit is justified by the formula found
in the completed review, not by an audit or lemma quota.

Read the cited primary formula and its extension language using the
[completed source comparison](2026-10-31-vanishing-amplitude-saddle-review.md),
which also records access limits. Check amplitude, phase, degree/power,
saddle and orientation conventions. The original L1 positivity condition
on A cannot silently be retained while testing a multiplier with a
positive root: the audit addresses the note's stated extension. Treat
the displayed formula as unverified. Resolve xi/zeta glyphs in the web
extraction by their source definitions; do not manufacture a contradiction
from OCR. No formula depending on an unresolved glyph is imported.

Compute the exact coefficient for the fixed A,B,N from the standard
exponential power series and compare its large-n behavior with the
source prediction. Use O'Sullivan's known rule (1.7) and Corollary 5.1
only if needed to distinguish an arithmetic mismatch from a hypothesis
or branch error. Do not reprove the general saddle theorem or derive an
arbitrary-multiplicity transition formula. No new source is essential
to this elementary check. This future test has not been calculated in
the literature turn that prepared this assessment.

Continue reliance on the short formula only if exact and predicted
coefficients agree under its intended hypotheses. On disagreement,
record a precise qualified counterexample or nonapplicability and park
that formula; retain the general O'Sullivan theorem with its original
hypotheses. Do not infer anything about Xi or RH from an auxiliary
source-formula failure. A generic expansion with unsupported Xi bounds
still fails the original actual-Xi admission test.

Essential theorem input is O'Sullivan v2 as precisely cited in the
parent review; local IDs L018/L463 are context only, with L461/L462
contrasts, not premises of the coefficient calculation. Unresolved Xi
assumptions are not used. No cross-notebook input. Full matching Mathlib
coverage is unchecked. Recommended completed task: RESEARCH /
REPRODUCTION / proof_audit / routine_audit, standard / high. Creative
Xi work is blocked by actual uniform amplitude/contour bounds; this
routine check is not labeled creative.

## Separate literature gate repair, 31 October 2026

This completes the requested separate approval of the saved target, with
DECISION SPECIALIZE unchanged. The defect was missing direct source URLs
in this assessment, not missing coverage of a newly changed target. The
parent comparison's exact-statement/stronger-result searches, duplicate
checks and recorded actual-Xi failure are reused; no repeated general
search or fresh theorem is claimed.

Primary sources and precise scope:

- Flajolet--Sedgewick, *Analytic Combinatorics*,
  [author-hosted book](https://ac.cs.princeton.edu/home/AC.pdf), printed
  pp.586--589, especially the signed-multiplier relaxation and Note
  VIII.37. The parent assessment records full primary reading of the
  theorem hypotheses, proof and note. Initial nonnegative A is distinct
  from the extension being audited; applicability must be tested under
  that extension. Today's direct book request returned HTTP 403; the
  alternate author-hosted https://algo.inria.fr/flajolet/Publications/book.pdf
  exceeded the web tool's size limit. Neither response is a new reading
  or a new source blocker: the retained primary evidence is reused.
  Formula glyphs must still be resolved from their definitions during
  the audit; no signed formula is certified here.
- Cormac O'Sullivan, *Revisiting the saddle-point method of Perron*,
  [arXiv:1702.03777v2](https://arxiv.org/html/1702.03777v2),
  Assumptions 1.1 and (1.7), Corollary 5.1 and its proof, Section 4.
  Rechecked the fixed-data holomorphy and bounded contour requirements,
  nonconstant phase, even saddle order and strict real-phase maximum,
  incoming/outgoing opposite sectors and orientation. The coefficient
  rule includes amplitude derivatives and phase corrections. The
  remainder is absolute, proportional to the amplitude supremum;
  nonvanishing of the amplitude at the saddle is not required.
  The parent assessment's full proof-case reading remains applicable.

The planned elementary calculation is needed to verify a suspect
short formula, not to reprove the general expansion. Source readiness
permits that calculation only; it does not establish its outcome, a
replacement expansion, Xi uniformity or RH. No lemma or mathematical
script was written. Full matching Mathlib coverage remains unchecked.

Completed work is LITERATURE / NOVELTY_UNCHECKED / literature_comparison.
This is an honest STALLED process repair: no new mathematical evidence
or changed mathematical route. The repaired assessment is ready for
the exact saved research target next turn.
