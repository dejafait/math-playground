# Proposed bounded diagonal charge test

TARGET: Compute the full diagonal Chern pullback of the hypothetical equality kernel and test its charge against the exact-metric rank-two stable/split alternatives.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the targeted notebook duplicate/failure search and primary-source discovery recorded in 2026-10-18-equality-diagonal-restriction.md; no matching fixed-tensor diagonal test was identified.
SOURCE_EVIDENCE: Verbitsky math/0107182v10 (24 June 2010), Theorem 3.1, Proposition 3.7, Lemma 3.8 and Theorem 3.9, https://arxiv.org/html/math/0107182v10#S3; Huybrechts author-hosted Lectures on K3 Surfaces, Chapter 9 Definition 4.7, Remark 4.8 and Theorem 4.9, printed pp. 181–182, https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182; Stacks Lemma 42.38.9(2), https://stacks.math.columbia.edu/tag/02UA, and character formula, https://stacks.math.columbia.edu/tag/02UM; exact-h K3 tools reused from the 2026-10-04 factor assessment.
COMPARISON: Known results cover the connection and Chern-naturality framework and L052 supplies the stable/split thresholds; only the specified diagonal metric/curvature specialization and full-tensor contraction remain to be checked.
GAP: Determine the integer diagonal second Chern number and compare with stable c>=4 and split c=14r^2, without inferring existence from a passing value.
REASON: A single independent smooth-restriction calculation can decide whether this necessary test excludes the fixed equality kernel; the separate 2026-10-18 step 394 source-URL repair preserves the target and supporting-tool approval for the next mathematical invocation.
SCOPE: Only diagonal restriction for identical marked K3 factors, common ordered quaternionic structures, exact real h, hypothetical locally free rank-two Omega-polystable F with integral c_1=0 and ch_2=-14e_1-21e_2-tau_D.

Full primary hypotheses, inspected proof cases, direct citations and
qualifications are in [the completed source comparison](2026-10-18-equality-diagonal-restriction.md).
This is supporting-tool SPECIALIZE coverage, not a matching theorem or
certified originality. No diagonal result has been derived.

Essential inputs: L071's actual compatible connection and full tensor
convention; L025/L044's divisor and transcendental operators and exact h;
L052's proved exact-h stable/split numerical alternatives. Verify the
induced metric and curvature explicitly before invoking the surface
criteria. Pull back integral c_1 and the complete mixed tensor; retain
reducibility of the restricted bundle. Justify any cup/trace contraction
in a complete rational basis; no integral NS/T splitting is assumed.

Continue only to this one calculation. Exclude the recipe only if the
computed charge fails both justified alternatives (or another explicitly
cited necessary Chern condition); otherwise park the diagonal filter as
nondiscriminating. Passing does not supply F, image separation, compact
ambient extension, reconstruction or transverse transport. Universal
primitive Hodge realization remains open. No arbitrary graph test is
covered. Expected classification is REPRODUCTION. Mathlib is not checked.

## Separate source approval and process repair — step 394

LITERATURE_REASON: Supervisor recovery identified missing direct source URLs in the ready assessment; repair that evidence field without repeating discovery or calculating the charge.

The exact target, assumptions and SPECIALIZE decision are unchanged. Reuse
the completed comparison's discovery, duplicate/failure search and
Huybrechts/factor-source inspection. In this separate literature-only
step, reopened the primary Verbitsky Section 3 statements and the two
Stacks pages directly. Proposition 3.7 and Lemma 3.8 concern invariant
curvature and zero contraction; Theorem 3.9 retains stability and invariant
first two Chern classes. It does not assert arbitrary restriction stability.
Stacks 02UA(2) retains a locally finite-type map and a finite locally free
bundle, with bivariant compatibility; its projective-bundle proof was
already inspected in the source comparison. Stacks 02UM supplies the
Chern-character polynomial. These statements match the previously recorded
scope; no new theorem or diagonal computation is claimed. The Huybrechts
passages were reused from the prior inspection, not newly fetched here.

The source field now contains direct primary URLs as required. This is a
STALLED metadata/source-evidence repair, not a mathematical advance or new
literature discovery. Separate approval is complete for this exact bounded
calculation; no expanded graph, existence or transport target is approved.
The downstream purpose and continue/park test above remain unchanged.
