# Effective Gaussian primitive evaluator — nominated audit

TARGET: Critically audit C032w's explicit-formula normalization, uniform truncation bounds and removable primitive error propagation for dictionary1570.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Separate source-scope review1574 reused review1572 and notes1572/1555, inspected C032w(1)-(13) to identify its claimed inputs, and checked dictionary1570/stop1571. Exact scope comparison is recorded in drafts/literature/2026-11-18-effective-gaussian-audit-source-scope-1574.md; no new novelty search is needed for this unchanged audit.
SOURCE_EVIDENCE: Connes arXiv:2402.13082v1 Section2(4)-(7), p4, https://alainconnes.org/wp-content/uploads/heat-zeta.pdf; Chirre-Goncalves Math.Z.300(2022) Proposition5 p1044, https://link.springer.com/content/pdf/10.1007/s00209-021-02820-9.pdf; Haslinger Theorem2.39 pp67-68, https://www.mat.univie.ac.at/~has/scriptneu.pdf; C032m's audited removable quotient. Existing primary coverage is retained.
COMPARISON: These sources cover the general identity and integration tools; C032w's finite shifted approximation, explicit spatial tail and coefficient-error propagation are the new local application requiring independent scrutiny, not an imported sign theorem.
GAP: Source scope is approved separately in review1574; the next research turn must test every constant, factor of two, removable value and ordered limit in C032w(1)-(13). No critical audit or numerical performance assessment is completed by this literature review.
REASON: The noncompact analytic specialization is load-bearing for sharper dictionary evaluation. Existing primary coverage suffices for a conceptual audit of its application; no essential unread source was identified. Reuse general results by citation and audit only the local specialization.
SCOPE: Real sigma in[1,2], |w|<=3 covering the unchanged dictionary1570 and primitive paths, actual divisor and all inherited qualifications. No new optimizer, frequencies, zero coordinates, global signs, moment hypothesis or Xi realization.

Source-scope gate approved on 18 November 2026 in review1574. This
approves the audit target, not the correctness of C032w. The next
research turn is one conceptual proof audit:
reconstruct the Mellin normalization and all-zero/positive-ordinate
factor; verify the combined archimedean endpoint estimates; check the
prime tail, midpoint derivative bound, real-axis logarithmic bound,
spatial tail, radius-one Cauchy step, geometric derivative remainder,
finite polynomial integrations and coefficient amplification. Explicitly
test the origin and w=+/-ix. Inspect the ordered T, profile-cutoff and K
limits rather than treating a uniform error as independent of T.

Continue if the full claimed analytic interface survives or is repaired
within its stated hypotheses. Otherwise record the first load-bearing
error and narrow the conclusion. No finite residual or computational
feasibility claim follows from successful audit. Essential local input
is C032m; C032q and assessment1570 supply only downstream interpretation.
Retain divisor/multiplicity, zero-ordinate exclusion, strip/counting,
through100/first-zero/tail, heat and fixed-v1 qualifications; the evaluator
does not require individual zeros or independently certify the latter
inputs. Full matching Mathlib coverage remains unchecked and unknown.

Creative routing is deferred because this is established-route analytic
effectivity, not an all-order residual-decay or Xi-realization mechanism.
The new proof's noncompact error interface is an essential audit before
it can support either implementation or a changed central target.
