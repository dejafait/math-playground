# Enclosure detector with certified coefficient errors — nomination1259

TARGET: Review sufficient certified error tolerances for C032b's enclosure-only detector when both its degree-M polynomial coefficients and the logarithmic moments ell_k=-S_k/k (2<=k<=2M+2) are approximated, retaining a rigorous full Q<0 conclusion under the unchanged support and mass hypotheses.
CHECKED: 2026-11-17
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: During the approved C032b audit, read L030/L032, L895's statement and generic convergence proof, and the existing nomination1255/review1256 comparisons. L895 explicitly assumes an exact basis in its coefficient-error certificate. No separate search or theorem-level comparison for an inexact constructed polynomial was performed; this is a nomination, not coverage approval.
SOURCE_EVIDENCE: C032b's full Runge construction has now passed its independent conceptual audit1259. L895, Conclusion (2)-(3), provides moment/logarithmic-coefficient tolerances for an exact polynomial basis and names Higham's 9March2021 Courant-Fischer/perturbation formulas; that external source was not newly inspected for this proposed inexact-basis target. Reuse relevant existing source evidence before any new retrieval.
COMPARISON: The existing exact-basis moment certificate is the closest local input and may cover much of the requested specialization. C032b supplies an enclosure-only exact polynomial, degree, coefficient bound and negative margin; it explicitly does not certify numerical rounding. Simultaneous certified polynomial and moment errors require a separate applicability comparison. No novelty or missing-theorem claim follows from the present limited read.
GAP: Sufficient jointly valid tolerances for the supplied approximate polynomial and finite logarithmic data have not been derived or source approved here. Actual-Xi support, a nonreal cluster, mass/coefficient data and all-degree signs remain separate unresolved inputs.
REASON: Prepare the detector's stated downstream certificate use without repeating its completed proof audit. This changed target is outside the exact saved audit and requires a separate literature-only gate. Determine what can be imported from L895 and standard finite quadratic-form perturbation before deriving any difference.
SCOPE: Keep C032b's full support, mass, conjugation, nonzero-node, boundary and multiplicity hypotheses. Supply a real degree-at-most-M approximate polynomial with a certified coefficient-l1 error bound relative to the exact constructed q, and finite real approximate ell_k with certified uniform errors. Seek rigorous sufficient tolerances and a complete Q<0 conclusion; do not assume actual-Xi data, change support, infer internal separation or promise feasible complexity.

## Proposed continuation, with no new derivation

The [canonical C032b audit](../../lemmas/C032b-enclosure-only-cluster-polynomial-detector.md)
retains the complete conditional Q(q)<=-3/2 estimate. Its role is negative
detection for supplied enclosures; it supplies no actual-Xi sign. Its
explicit constants can be very large, and exact real formulas do not
alone certify floating-point or rational approximations to q.

The proposed finite-data question retains the same multiset and geometry.
Use S_k=sum_j beta_j^k and define the generic logarithmic data by
ell_k=-S_k/k. A later Xi interpretation would separately require L024/L025
and the underlying L018/L026 conventions; none is used or imported here.
The approximate polynomial is real and has degree at most the C032b bound
M. Supply a certified coefficient-l1 distance from the exact q, rather
than silently assuming that an implementation already computed that
distance. Supply errors for all moments through 2M+2 via ell_k. Both
sorts of errors must be included in a rigorous negative certificate.

The downstream use is a finite certificate that remains valid after
polynomial rounding, including when nodes collide within a cluster.
The relevant question is the tolerance needed in terms of the supplied
C032b parameters and bounds. This does not assert the availability of
any Xi instance or that the resulting tolerance is practical.

The next review should first compare L895's exact-basis bounds, including
its explicitly excluded basis errors, and L030's finite Hankel expansion.
Inspect only the essential primary perturbation statement or proof case
if those ready records do not suffice. Avoid repeating Runge searches,
Li-criterion conversions, or the stopped direct-constants import. No
new tolerance formula, lemma, implementation or source approval is
claimed in this nomination.

Continue only if that comparison covers or approves one concrete
simultaneous-error certificate under the supplied bounds. If it requires
uncertified polynomial accuracy or strengthened node data, record that
limitation instead of asserting an implementable certificate. Unknown
Mathlib coverage is not evidence of absence. No cross-notebook input is
proposed.

No justified creative theta-signing mechanism follows from this audit.
The unresolved need is a theta-specific signed estimate, whereas this
detector is a conditional consequence of generic summable-node geometry.
The continuation is therefore a bounded literature comparison for an
application of the audited tool, not a renamed central creative attempt.
