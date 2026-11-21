# Prospective actual-theta Gram companion metric

TARGET: Assess the fixed actual-theta Gram similarity for C028h's centered companion as a possible o(d) imaginary-part trace-norm bound, comparing orthogonal-polynomial companion theorems and the recorded reference-metric obstructions.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Source review1694 completed comrade-companion discovery and the narrow reference-family comparison; queries, actual reads and unread leads are in drafts/literature/2026-11-19-actual-theta-gram-source-notes-1694.md. No exact theta cost estimate was located; no novelty is inferred.
SOURCE_EVIDENCE: Schmeisser2002 Lemmas1/4/5 pp211-213 and full Theorem1 proof pp213-214 https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf ; Noferini-Robol-Vandebril ETNA54 Definition2.1/Theorem2.2 and Section2.2 pp422-425 https://acris.aalto.fi/ws/portalfiles/portal/65515241/Structured_backward_errors_in_linearizations.pp420_442.pdf ; DLMF18.2(iv),(vii),(viii) https://dlmf.nist.gov/18.2 ; Simon2011 Proposition1.3.6/Theorems1.3.7-8 pp16-17 https://assets.press.princeton.edu/chapters/s9377.pdf ; reuse1523 for Higham's characteristic identity.
COMPARISON: The general orthogonal-polynomial companion method is known; its full-cost interface is relevant once the nominated Cholesky correspondence is verified. C028c requires a specified Hermite-prefix recurrence and matching, not all positive measures; no established stop has yet been verified to cover this metric. This does not prove escape from those stops.
GAP: Verify positive-Gram applicability and the precise basis correspondence, then test the quadratic residual with exact recurrence norm ratios and fixed degree scaling. Neither that residual nor a sublinear bound or linear floor has been derived. All-degree actual signs remain unpaid.
REASON: Essential coverage permits a bounded conventional specialization before a large Cholesky/asymptotic search. Assessment1694 specifies the later calculation and awaits separate next-turn approval; this completed turn contains no new mathematics.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED coverage lacked the orthogonal-polynomial full-cost representation and support/recurrence comparison; reused matrix majorization alone did not settle them.

## Original nomination1693; completion1694 below supersedes pending coverage

## Exact prospective object; no calculation performed

Use the full kernel K of L019, not a finite theta truncation. Define

    Z = 2 integral_0^infinity K(u) du,
    dmu(u) = K(|u|) du / Z on R,
    G_d = [integral_R (d u)^(i+j) dmu(u)]_(0<=i,j<d), d>=3.

This fixes a single measure and a prescribed degree scaling; no
parameter fitting, finite-node surrogate or coefficient truncation is
part of the target. The prospective matrix construction must justify
normalization, every moment and positive definiteness from L019's
actual kernel. Set S_d to the real upper-triangular Cholesky factor
with positive diagonal, G_d=S_d^T S_d, once those premises are checked.
Use C028h's exact centered monomial companion A_d and define

    B_d = S_d A_d S_d^(-1),
    K_d^theta = ||(B_d-B_d^*)/(2i)||_1.

These are proposed definitions, not a proved estimate or a claim that
G_d symmetrizes A_d. The metric is not the Newton-sum matrix of Q_d,
and is not constructed from its roots. Positivity of an external
moment matrix alone says nothing about the companion's spectrum.

The literature turn should check exact terminology, stronger general
orthogonal-polynomial companion bounds and known obstructions, reusing
the inspected Schmeisser interface where applicable. In particular
determine whether the construction is already an instance of a stopped
reference-family theorem. If so, import the precise obstruction rather
than recompute it. Otherwise identify one source-covered test of the
full multiplication-compression defect and its degree scale. No new
defect formula, Cholesky asymptotic, norm estimate or script belongs to
the present nomination or its literature-only approval.

## Relevance, alternatives and stopping test

The main gap is L030-L032/C032a, equivalently the unpaid C028b height
condition H_d=o(d); C028g identifies its limiting functional S_F.
If the general matrix majorization applies and K_d^theta=o(d) can be
proved, it would pay that height condition. This is a proposed use,
not evidence for the bound. A positive degree-linear lower floor would
stop this particular metric only, not lower-bound actual root heights.

Three alternatives were compared during continuation selection:

1. Further generic local-PF propagation: the now-audited C028n already
   blocks the entire/self-decomposable/positive-coefficient premises.
   No new distinguishing premise is ready; preserve stop1691.
2. An actual-density low-order or scalar propagation test: review884
   records a huge existing global finite-PF range, so eventual D2
   positivity would duplicate a known conclusion. The retained-zero
   contact and generic scalar stops886/898 separately exclude bare
   scalar propagation. No new signed input was supplied here.
3. The specified dense full-theta metric: choose this for source review
   because it uses the actual measure without assuming the failed
   real-rooted finite reference, Newton-sum positivity, diagonal metric
   or single terminal shear. Its viability is untested, not certified.

The two-node degree-five stop551 and finite-summand stop571 prevent
silently replacing this measure by a reference claimed to have only
real roots. The Gaussian coefficient floor C028a and the diagonal/
shear floors C028h/i remain evidence; their proofs must be compared
with this precise metric before reopening any height-budget mechanism.
The pending audit of C028i is not treated as an audited theorem here.

Continue only if source review supplies a noncircular, bounded test
that can distinguish an o(d) full cost from a positive linear floor.
An entrywise estimate, finite-degree sample, or merely an equivalent
unknown height criterion is insufficient. If the same general reference
obstruction applies, record that overlap and abandon this metric. Do
not vary the scaling, reference law or shear after failure within the
same target. Compact root-height mass, actual all-degree positivity
and any required uniform control remain unpaid.

Essential prospective inputs: L019 for the measure, C028h for the exact
A_d convention, C028b for the downstream criterion; C028g and
C028a/i are orientation and comparisons. Review exact dependencies
when and only when writing a mathematical result. Mathlib coverage
of this combined construction is unchecked. No cross-notebook input.

This is a new uncovered continuation after a completed mathematical
audit, not an extra literature turn or an approved mathematical claim.
Next turn is literature_comparison/standard/high. No creative attempt
is ready: the dense metric needs source/overlap screening, and a
general known-method specialization must not be labeled creative.
If a genuinely new central mechanism survives that comparison, its
later proof_attempt/creative nomination must name the bounded defect
test and decisive evidence separately.

## Completion1694 — literature only

The source comparison and its qualifications are saved in
[source-notes1694](2026-11-19-actual-theta-gram-source-notes-1694.md).
The general mechanism is covered by the literature; the specified
Cholesky correspondence and degree cost still need specialization.
No theorem supplying the theta bound was located, and no restricted
reference-family stop was shown applicable. This is source coverage,
not a new norm result.

The bounded continuation in
[assessment1694](2026-11-19-actual-theta-gram-quadratic-cost-test-1694.md)
verifies the representation and tests its quadratic residual at the
exact scale. It requires separate approval next turn. No creative
mechanism is nominated: the remaining task is conventional specialization.
The original proposed scope above is preserved as historical context.
