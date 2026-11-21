# Actual theta-average degree-three Favard test

TARGET: Test the necessary monic three-term recurrence through degree three for the actual L795 sequence using L791's audited coefficient enclosures, and certify an obstruction to common positive-measure orthogonality or report the prefix inconclusive.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step503's exact-sequence Favard/Brenke/Jensen comparison in 2026-11-05-theta-average-favard-interface.md; no earlier actual-prefix certificate was found locally. No novelty claim.
SOURCE_EVIDENCE: https://dlmf.nist.gov/18.2#E11_5 and https://dlmf.nist.gov/18.2#E11_6 give the necessary monic recurrence/positivity; Dimitrov–Ben Cheikh, JCAM233(3)(2009),703–707, Theorem1 p706, DOI10.1016/j.cam.2009.02.039, primary text https://www.researchgate.net/publication/223123039_Laguerre_polynomials_as_Jensen_polynomials_of_Laguerre-Polya_entire_functions ; L019/L021/L795 fix the sequence and L791/step478 supplies audited actual coefficients.
COMPARISON: Recurrence and Jensen classification are known; the exact theta-prefix evaluation remains an uncomputed reproduction/specialization. Failure rejects common nondegenerate positive-measure orthogonality only, leaving individual root signs and RH unresolved.
GAP: The actual monic expansion, forbidden coefficient and required beta signs have no certificate yet. A prefix pass establishes no infinite recurrence, positive support or all-degree transfer.
REASON: One finite necessary-condition certificate can settle this stronger sufficient realization before a global construction. Reuse known theorems and actual data; do not reprove classification or develop a fresh evaluator.
SCOPE: P_0 through P_3 only, with L795's exact scaling and audited gamma(0..3) intervals from L791. No degree, shift, family or measure change. Newly saved coverage requires separate next-turn approval; this source turn executes none of the calculation.

Read the completed [source comparison](2026-11-05-theta-average-favard-interface.md).
Essential inputs are L019/L021/L795 and the actual-coefficient portion
of L791 with its step478 audit. L778's evaluator/software contracts
remain inherited qualifications, not fresh audits. The gamma intervals
are in scripts/central-jacobi/fixed-model-certificate-476.json and their
audit/provenance in scripts/central-jacobi/audit-478/audit-report.json.
Inspect complete selected load-bearing values with the shared JSON
inspector before use; previews and rounded decimals are not inputs.
No model parameters or model-root signs are premises.

Use L791's gamma(j)=j!m_j/(2j)! and divide by gamma(0) to recover
L795's convention, retaining (-1)^j and binomial factors. Check this
normalization against the canonical definitions before deriving anything.
Monic normalization divides by each actual nonzero leading coefficient;
L021 supplies nonvanishing. Record denominator bounds. Do not substitute
arbitrary positive moments or a fitted Jacobi family.

For the monic Q_0,...,Q_3 expand xQ_n in this basis at n=0,1,2 and
compare with the cited Favard form. At n=2 test the Q_0 coefficient,
which that known form forbids, and the required positive beta_1,beta_2.
Derive formulas only in the approved mathematical turn. Preserve exact
symbolic formulas and full outward rational-enclosure certificates.
Print actual intervals, required values/signs, failures and output path.

Bound work to one symbolic expansion and one outward rational evaluation
of the audited input intervals. If dependency overestimation obscures
a sign, allow at most one algebraic rearrangement; no fresh moment
calculation, precision campaign or degree extension. A forbidden
coefficient interval disjoint from zero proves necessary-condition
failure. A proved beta<=0 excludes nondegenerate positive-measure
orthogonality. An interval merely meeting zero is not an equality or
sign certificate. A passing or undecided prefix ends this bounded test
with the infinite problem unresolved.

Canonicalize any established specialization with hypotheses, full
certificate, inherited qualifications and Mathlib status. Cite the
published criterion/classification without reproof. Intended completed
kind is RESEARCH, classification REPRODUCTION. Common measure/support,
all-degree recurrence and transfer remain unpaid. This is a conventional
finite test, not a creative proof attempt.
