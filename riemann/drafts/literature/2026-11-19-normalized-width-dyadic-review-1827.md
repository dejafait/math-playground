# Normalized-width rounding: source comparison1828, URL recovery1829

TARGET: Assess a one-time dyadic rounding of C033z's normalized width before its eight exact Newton steps, seeking error<=2^-60, at most322 operations per width including clamps, and an explicit Newton-iterate denominator bound independent of the input denominator.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1828 searched once-rounded coefficients, rational Newton denominator growth, stronger fixed-point reciprocal-root algorithms and charged rounding; compared local1802/1810/1823/1825/1827 contracts and failure evidence. Queries and inspected cases are in drafts/literature/2026-11-19-normalized-width-source-notes-1828.md; no novelty is inferred.
SOURCE_EVIDENCE: Brent-Zimmermann v0.5.9 Lemma3.14,p112 https://members.loria.fr/PZimmermann/mca/mca-cup-0.5.9.pdf#page=128 ; WPI MA3257 Spring2023 lecture23,p2 https://users.wpi.edu/~bgu/sp23/ma3257/lecture_notes/MA3257_L23.pdf ; Korzilius-Schoenmakers(2023),Sections5.1-5.3 Algorithm5/Theorems4-5 and Remark6 https://www.mdpi.com/2410-387X/7/3/43 ; GMP6.3.0 Chapter6 https://gmplib.org/manual/Rational-Number-Functions.html ; reused1809 Johansson arXiv1611.02831v1 Sections3.1.1-3.2,5-5.1 https://arxiv.org/abs/1611.02831v1 . Inspected coverage and access qualifications: drafts/literature/2026-11-19-normalized-width-source-notes-1828.md, recovery1829 appendix.
COMPARISON: Known bisection/error propagation and exact Newton theory cover the ingredients; the stronger fixed-point algorithm rounds within iterations, uses a different seed/domain and different primitives. No inspected theorem supplies this one-time rational conversion, complete322-operation count or iterate-denominator certificate. C033z1810 is a local conversion precedent, not this width theorem.
GAP: No essential source gap remains for one bounded specialization. Choose and charge an explicit fixed-grid conversion; prove closed-range containment/equality cases, full coefficient/input/Newton/clamp error, every iterate's denominator bound and all operations. No precision, bound or passing construction has been derived or certified.
REASON: The changed coefficient and denominator requirement needed this separate source turn. Import general numerical results and derive only the finite local contract in later research; the newly saved continuation requires separate next-turn approval. Do not import a fixed-point or library cost as a rational primitive.
SCOPE: Exact rational W in[1,2^30], the same rational +,-,*,/,comparison model and supplied panel flag. One fixed dyadic grid is proposed before the eight Newton steps; no free floor, bit access, library rounding or large runtime constants. Preserve1802 input perturbation and original panel clamps.
COVERED_TARGET: Construct and prove C033z's one-time dyadic rounding of the normalized width before eight exact Newton steps, with total error<=2^-60, at most322 operations per width including clamps, and an explicit bound on every Newton-iterate denominator independent of the input denominator.

## Purpose and bounded test for the later review

The completed audit is canonical in C033z, application audit1827, with
`scripts/smoothed-law/width_newton_audit_1827.json` as exact evidence.
It leaves practical denominator control open. A proposed single rounding
of the normalized coefficient is a distinct implementation mechanism,
not a repetition of the stopped unrounded evaluator. No proposed grid
precision or resulting denominator formula has been derived or approved,
including in this source review1828.

The original width-bisection allowance in1802 is322 operations per width;
use322 here as an explicit proposed local ceiling, including the clamps.
This is not a new global cost ledger. Continue only if source coverage
supports an independently testable simultaneous error/cost/denominator
contract; otherwise record the exact unmet requirement. A bounded iterate
denominator would not itself certify runtime, rounded later arithmetic,
all scalar execution or a full evaluator improvement.

Essential mathematical inputs for a later attempt are C033z1825/1827,
1802(11),(14)-(17), C033y's real panel map, and the cited exact Newton
theorem. Interpretation downstream still uses C033w/u and C032s/q/w/j.
Retain divisor/conjugation/multiplicity, excluded ordinate0, strict strip
and gamma>14, counting/real-zero/tail, heat positivity/separate errors,
both fixed-v1 qualifications, zero drift/killing and Gaussian half-variance.
Full matching Mathlib and source-wide correctness remain unverified.
Conditioning, weights, TV<=2, observation coverage, signed-height
cancellation and actual-Xi realization remain independent unresolved gaps.
Preserve1816/1823/a/b, all saved suffixes and their existing replay boundaries.

No concrete central signed-height/actual-Xi mechanism is justified by the
bounded width audit. This proposed numerical specialization is not labeled
creative; an overdue creative nomination does not waive source coverage
or turn an arithmetic implementation change into an RH mechanism.

## Review1828 decision and specialization boundary

The primary statements, hypotheses, relevant proof cases, access failures
and exact nonimports are recorded in the source notes above. The bisection
theorem has strict endpoint sign hypotheses; it cannot silently cover an
endpoint coefficient or an equality branch. Their treatment, grid membership
and denominator arithmetic are finite implementation obligations, not a
reason to reprove a general rootfinding or rounding theorem. Mean-value
propagation must use a valid derivative bound on the entire coefficient
segment. Eight-step convergence must be checked for the rounded coefficient,
not inferred by replaying samples from the unrounded constructor.

The denominator claim is specifically for the Newton iterates after the
single conversion (and, if reported, rescaling/clamps). Normalizing and
comparing the original W can still involve its arbitrary input denominator.
No input-independent bit cost or runtime is included. The fixed-point paper's
approximate higher-order expansion in(13)/Remark6 is not an exact error
bound to import. No additional arithmetic source is essential: explicit
denominator induction through the specified rational expressions is the
remaining local proof obligation. No such induction was performed today.

Continue only if a later fully specified construction passes all three
requirements simultaneously, including1802 perturbation, normalization
boundaries and original clamps. A failed candidate is recorded without
loosening322 or2^-60 and without declaring all once-rounded schemes
impossible. No lemma, mathematical script, global ledger, scalar or
actual-Xi statement changes in this literature-only review.

## URL recovery1829: separate approval of the saved continuation

This literature-only recovery makes the direct primary URLs explicit in
SOURCE_EVIDENCE. It reuses review1828's theorem-level comparison; no target,
hypothesis, numerical precision or cost allowance changes. The saved
COVERED_TARGET is approved for one subsequent research attempt under
SPECIALIZE. This approves source coverage, not the proposed construction.

Recovery1829 opened the author-hosted MCA PDF and located Lemma3.14's
statement and complete Taylor proof on printed p112 (PDF page128); opened
the two-page WPI source and publisher HTML and located Theorem4. These
URLs resolve to the previously recorded sources. Both GMP URL forms
returned502 today; reuse1828's inspected canonical-form contract rather
than claim a fresh successful retrieval. No new GMP or fixed-point theorem
is imported and no essential source blocker is introduced. Johansson
coverage is reused from1809, not newly inspected. See the source-note
appendix for the bounded recovery record. No new mathematical conclusion
is claimed; Mathlib availability remains unverified.
