# Corrected weak-cutoff Li residual — bounded specialization coverage

TARGET: Prove S_f(n)+lambda_n(sqrt(n))=O(sqrt(n) log n) for actual zeta with the weak finite cutoff, using L978-L979 and the inspected smooth/arithmetic identities.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed exact assembly comparison in review218, its narrow local duplicate/failure screen and recorded queries; no additional search or novelty claim.
SOURCE_EVIDENCE: Arias de Reyna31Jan2011, https://personal.us.es/arias/56-2RHB.pdf (Thm1/proof pp.4-5; divided normalization pp.1-2); Lagarias AIF57(2007), https://www.numdam.org/item/10.5802/aif.2311.pdf ((1.1)-(1.5), Definition4.3/Lemma4.4/proof, Thm5.1/(5.1)-(5.4), weak-cutoff definition(6.1)); full inspected scope in review218, counting/integration coverage in review216, and local L978/L979. Both primary URLs retrieved successfully on 2026-11-10.
COMPARISON: Known smooth and archimedean trends have matching constants; the ordinary exact arithmetic identity includes delta=1. The finite-height corrected residual still requires the listed cutoff/convergence specialization; the printed Section6 proof is not imported.
GAP: Normalize J1 to K_n, bound the removed lower smooth interval, reconcile radial star summation with absolute conjugate-paired height summation, and assemble exact weak-head/tail errors uniformly in n>=2. No such assembly is derived in this assessment.
REASON: Source scope is sufficient for one standard mathematical calculation after separate approval of this newly written continuation. Reprove only the identified specialization, importing the precise known identities and smooth estimate.
SCOPE: Fixed actual zeta; all multiplicities; integer n>=2; S_f from L977/(4.5)/(4.8); lambda_n(T)=sum_(|Im rho|<=T)[1-(1-1/rho)^n]; no RH, simplicity, head sign, zero table or effective constant required.

Use [review218](2026-11-10-li-smooth-arithmetic-assembly-review-218.md)
for the primary citations, hypotheses, essential proof cases, source
versions and comparison. Do not refresh adequate coverage without a
changed hypothesis or essential new source.

Essential inputs are L013 (no real zeros), L018 (orders/conjugation),
L977 (eta convention and historical contour stop), L978 (displacement
and absolute paired convergence), L979 (counting-error integral and
global kernel bound), and the inspected Lagarias/Arias identities.
L964/L968 supply existing completion normalization context; L968 is
the downstream whole-Li benchmark, not a sign premise.

The attempt must write the radial-to-height summation justification,
the full smooth-integral normalization, both improper endpoints, the
lower smooth interval, the exact complementary weak cutoff and the
delta term. Retain the actual complex finite head, including cutoff
atoms with full orders. No inference from the normalized l2 theorem
to a pointwise rate is licensed. Do not reprove the full source J1
estimate or repair the stopped Section6 contour argument.

Continue only on a uniform O(sqrt(n)*log n) bound with constants
independent of n; record any failed matching or convergence obligation.
An effective numeric constant is outside scope. The finite head's
lower bound and L030-L032/C032a positivity remain unresolved even
if this target succeeds. L976 and Coffey2007 stops remain unchanged.
Mathlib matching coverage is unchecked and unknown.

## Separate source-readiness approval, step220

The recovery report concerned missing direct URLs in this assessment,
not missing theorem coverage. On 10 November 2026 both linked primary
PDFs were retrieved successfully. The author PDF identifies its version
as 31 January 2011; the journal PDF identifies volume 57(5), 2007,
pp.1689-1740, DOI 10.5802/aif.2311. Reuse review218's inspected proof
cases and comparison without redoing its mathematics or source search.

Direct locations for the already inspected inputs are
[Arias Thm1 and proof, pp.4-5](https://personal.us.es/arias/56-2RHB.pdf#page=4),
[Lagarias Lemma4.4, pp.1708-1709](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=21),
[Lagarias Thm5.1, pp.1712-1713](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=25),
and [weak cutoff (6.1), p.1721](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=34).
The inherited counting/integration source comparison remains in
[review216](2026-11-10-truncated-li-model-stieltjes-review-216.md).
No theorem-level scope, hypotheses, target or decision changed.
SPECIALIZE is approved for the exact TARGET in a later mathematical
turn; the listed convergence and normalization obligations are still
unproved. This URL repair establishes no mathematical result and does
not remove the recorded Section6 contour stop or finite-head sign gap.

Classification if successful: REPRODUCTION; task: calculation,
standard/high. No lemma or mathematical script is written in this
literature-only approval turn. Mathlib coverage remains unchecked.
