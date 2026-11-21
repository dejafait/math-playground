# Ihat block-rounding audit: nomination1810

TARGET: Independently audit C033z's block-of-four Ihat rounding contract1810, including universal range, rational conversion cost and all-eight-scalar propagation under the10^6 cap.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse unchanged Ihat-only source assessment1809 and rounded-source-notes1809; today's scoped direct-positive-real drafts/history check found exact-prefix denominator growth and source review, with no earlier rounded contract or completed audit of1810. No new external search or novelty claim.
SOURCE_EVIDENCE: Reuse inspected Johansson1611.02831v1 Sections3.1.1-3.2/4/5-5.1, https://arxiv.org/pdf/1611.02831v1; Arb2.23.0 enclosure/quotient and exact-conversion cases, https://arblib.org/arb.html and https://arblib.org/arf.html; MPFR4.2.2 Sections4.4/4.6/5.2, https://www.mpfr.org/mpfr-4.2.2/mpfr.html . Detailed primary cases remain in source-notes1809. Analytic source coverage1799/1804/1805 is unchanged.
COMPARISON: General enclosure principles are known; the new local range induction, comparison-based conversion, ledger and propagation are written in C033z's1810 extension. An independent audit must verify this application rather than reprove general arithmetic facts. The inherited989767 ledger is not a completed-run count.
GAP: Independently check all56 block bounds, equality/endpoint branches, grid denominator, 43*3+2 conversion cost/shared negation, profile margin and computed-weight propagation to six full/two residual scalars. No source supplies those fixed constants; source/zero-data validity remains qualified.
REASON: Separate source-scope approval completed1811 in drafts/literature/2026-11-19-direct-positive-real-ihat-audit-scope-1811.md using unchanged inspected1809 coverage. Exact target ready for mathematical audit; no completed audit, scalar execution or changed rounding elsewhere is claimed.
SCOPE: Audit only1810's Ihat accumulation change with exact samples and all other constructors unchanged; check both2^-10 allowances, radius<2^-8 and total<=10^6 in the original rational +,-,*,/,comparison model. No bit-cost, interpolation, TV or actual-Xi claim.

The main gap is L030-L032/C032a actual-Xi all-degree positivity. The
intermediate audit would make a specific rounding modification reviewable
before attempting finite scalar execution. Stop or repair if a universal
range, rounding, denominator or full-cost/error obligation fails; passing
boundary tests alone is insufficient. A failure concerns this schedule,
not every rounded evaluator or the exact route.

Essential inputs: C033z's1810 canonical proof and new certificate/script;
C033y/u/w, C032s/q/w, C032j; audit1806 for the inherited construction;
execution1808 index/replay and source-notes1809 as preserved evidence.
Retain actual divisor/conjugation/multiplicity, excluded ordinate0,
strict strip/gamma>14, counting, real zeros through100/one in(14,15),
reciprocal-square tail, heat positivity/separate fixed-j errors, both
fixed-v1 qualifications, zero drift/killing and Gaussian half-variance.
Source-wide/zero-data validity and full matching Mathlib coverage remain
unverified. No cross-notebook input is used.

This is ordinary hypothesis/arithmetic/algorithm replay, not a creative
mechanism or an RH candidate audit. Source ingredients are covered, but
separate source-scope approval was completed1811. No
independent audit was performed during the construction1810 itself.
