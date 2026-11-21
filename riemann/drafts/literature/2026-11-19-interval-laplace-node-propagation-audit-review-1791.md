# C033v conceptual-audit source coverage1791

TARGET: Audit C033v's signed-transform holomorphy, Joukowski seed and finite disk-chain exponent, including all boundary and zero-error cases, against the approved Trefethen hypotheses.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse assessment1790 and source-notes1790's exact signed-Laplace/analytic-continuation searches and duplicate/failure comparison; the audit concerns the same finite signed half-line measure and finite positive-node scope. No changed hypothesis or fresh discovery claim requires a new search.
SOURCE_EVIDENCE: Trefethen, BIT60(2020), DOI10.1007/s10543-020-00802-7, https://people.maths.ox.ac.uk/trefethen/trefethen_ac.pdf, Lemma2.1 and full proof p904, Theorem3.1 and full proof pp904-905, already inspected1790. Dominated convergence, absolute-variation Fubini, Morera, bounded-domain maximum modulus and the identity theorem are the other named inputs.
COMPARISON: The source supplies the strip and concentric-disk inequalities; C033v supplies the explicit ellipse seed, uniform boundary argument and finite chain. The audit must verify that application rather than reprove the imported theorems or assume the source already states C033v.
GAP: Independently check C033v's entire signed-transform argument, uniform strip boundary, ellipse interior/disk inclusion, radius endpoints, iteration count/exponent ordering and zero/trivial-error cases; no audit verdict is supplied in1791.
REASON: This is a distinct critical review of the completed specialization using unchanged adequate source coverage. Newly saved ready continuation requires separate approval next turn; it is not an audit performed during the derivation turn.
SCOPE: Same generic finite real signed Borel measures on [0,infinity), prescribed finite positive node set, positive finite TV allowance, atoms and unbounded support. Audit only; no cap-V witness, original-residual rate, observable evaluation, actual-Xi transfer or external-zero-data verification.

The canonical object is
[C033v](../../lemmas/C033v-explicit-interval-to-finite-node-laplace-propagation.md).
Source coverage and initial duplicate checks are in
[assessment1790](2026-11-19-interval-laplace-node-propagation-review-1790.md)
and [source-notes1790](2026-11-19-residual-variation-cost-source-notes-1790.md).
Those precise primary statements and proof cases remain the inspected
coverage; the literature is not being refreshed for a quota.

The decisive test is whether the stated exponent follows from the exact
source hypotheses for every allowed S,M,epsilon, including nodes tending
toward zero through positive values and arbitrarily distant finite nodes.
The audit must check complete evidence in the canonical proof, especially
uniformity in the imaginary strip coordinate and that no outer disk
touches Re z=0. If a defect appears, correct or limit the application
with explicit evidence. No independent critical verdict has been claimed.

Numerical stops1571/1576/1781/1782 remain parked; this audit is not an
evaluator reopening. Full matching Mathlib coverage remains unchecked
and unknown. Any later use of C033i/j/l/p/r must separately retain all
its actual-divisor, conjugation/multiplicity, excluded-zero-ordinate,
strict-strip/gamma>14, counting, through100/retained-real-zero,
reciprocal-square-tail, heat positivity/separate fixed-j errors,
Gaussian half-variance and both fixed-v1 qualifications.
