# Fixed-band covariance payment — bounded first-input test

TARGET: Test the fixed-band sufficient estimate R(s_1)<=B_{1,2}(s_1) using the complete pole/prime correction and Zucca's covariance rectangle, certifying the sign of R(s_1)-B_{1,2}(s_1) at threshold zero without adding modes or changing the cap.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse completed comparison816/step817, including exact Weil/primitive covariance, quantitative stronger-result and local duplicate/failure searches. The known two-sine comparison does not evaluate this stronger sufficient payment test; no novelty inference follows.
SOURCE_EVIDENCE: Direct primary URLs https://zucca.faculty.polimi.it/papers/inequality/inequality.pdf (Lemma3.3/(3.6), pp5-6), https://dlmf.nist.gov/5.7.E6 and https://dlmf.nist.gov/5.15.E1 checked 2026-11-13; assessment816 supplies previously inspected Suzuki8.2/8.5 at https://arxiv.org/html/2606.09096v3#S8.SS2. C759a/d/f supply the local complete form and signed formulas. Coverage permits finite-input evaluation, not the proposed payment inequality.
COMPARISON: C759f already certifies the actual two-mode primitive defect. This test asks whether a specific proposed covariance resource pays the entire signed correction at s1, a necessary test before attempting that sufficient estimate on the full cap. Failure does not refute primitive lowering.
GAP: The fixed-band payment residual is unevaluated. Full-domain covariance specialization and signed domination, parity infima, even sign/simplicity, other windows and Xi realization remain open. No finite test settles these gaps.
REASON: An explicit source-based quantitative mechanism can be disqualified on an audited eligible input without adding modes or optimizing bands. Only one source-specialization calculation is nominated, subject to separate approval.
SCOPE: C759a's unchanged real Q on [-1,1]; only unit s1=sin(pi*x) and its actual primitive; both poles and n=2,3,4,5,7; fixed frequency boundaries1,2 and zero residual threshold. No universal comparison or sweep is approved.

## Proposed test definitions, not proved bounds

Use C759a's F, m and Fourier measure. Separate its prescribed correction:

\[
 E(u)=2F_u(i/2)F_u(-i/2)
       -2\sum_{n\in\{2,3,4,5,7\}}\frac{\Lambda(n)}{\sqrt n}
          C_u(\log n).
\]

For a unit odd f with nonzero primitive define h_f=||Pf||_2^2 and

\[
 R(f)=E(Pf)/h_f-E(f),\qquad
 p_1(f)=\int_{|t|\le1}|F_f(t)|^2\frac{dt}{2\pi},\qquad
 p_2(f)=\int_{|t|\ge2}|F_f(t)|^2\frac{dt}{2\pi}.
\]

The **candidate** resource to evaluate is

\[
 B_{1,2}(f)=\frac{p_1(f)p_2(f)}{h_f}
            (m(2)-m(1))(1-1/4).
\]

These definitions state a proposed estimate, not a covariance derivation
or an assertion that R<=B. The intended source specialization uses the
radial Fourier probability measure and increasing-factor rectangle in
[comparison816](2026-11-13-primitive-fourier-covariance-review-816.md).
Any claim that B is an archimedean lower resource must check those
hypotheses and frequency-zero integrability. The finite residual itself
is well-defined independently of that unproved general claim.

## One calculation and stopping rule

Use only s1. C759d(2) supplies Q(s1)<1/250; C759f(3) supplies
h_s1=3/pi^2 and the explicit primitive. C759d(4) supplies the Fourier
transform, interpreting removable values by the defining integral.
Use C759f's signed pole/correlation formulas, without recomputing the
complete gamma energy or replaying its certificate.

Certify intervals for R(s1), p1(s1), p2(s1), m(1), m(2), B and R-B.
Plancherel permits p2 from total mass minus the compact integral |t|<2,
with a proved integration error; otherwise pay the entire infinite
tail. Cite DLMF's series with a justified complete remainder. Retain
Lambda(4)=log2, the actual norm and the sign of every correction.
Full certificates must retain errors, threshold0 and failures on disk,
printing a short conclusion with actual/required bounds and paths.

A positive lower bound of R-B abandons this fixed-band sufficient
estimate on the cap, leaving C759f and primitive lowering intact. A
nonpositive upper bound passes only this necessary first-input test;
no other input or full-domain comparison is then approved. An undecided
interval is inconclusive; do not optimize regions or add modes. Further
work needs an informative target and matching gate.

This is calculation/REPRODUCTION under assessed standard methods, not
a creative full-domain proof or originality claim. The latter still
needs a correction-paying estimate. Matching Mathlib coverage of this
exact residual is unchecked. No lemma, script or number is produced
by this literature-only nomination.

## Direct-source gate repair — step818

LITERATURE_REASON: Supervisor recovery identified missing direct source URLs in this ready assessment; repair traceability for the identical target without extending its scope or repeating discovery.

Retrieved the author-hosted eight-page Zucca manuscript at the URL in
SOURCE_EVIDENCE on 2026-11-13 (no version/date printed in the inspected
passages). Read Lemma3.3 and its complete proof on p5 and the finite-integral
and separated-region cases on pp5-6. Its identity requires finite positive
measure and summable real factors; retain absolute integrability of their
product for the intended finite covariance. The displayed rectangle
estimate on p6 retains the total-mass factor. Use the probability case;
no general-measure normalization or full-domain specialization is approved.
PDF text was accessible; p5 screenshot succeeded, p6 screenshot timed out,
with its complete relevant displayed estimate available in extracted text.
No missing visual content is used as evidence.

Read NIST DLMF equations5.7.6 and5.15.1 at their direct permalinks above,
including both excluded-pole conditions. These are the partial-fraction
series for psi and the series for psi-prime, valid away from nonpositive
integers. The prescribed arguments1/4+it/2 avoid those poles. Neither
reference supplies this calculation's finite truncation/integration error;
the next calculation must justify the complete remainder, as required
above. No new series estimate or covariance specialization is derived here.

Reuse assessment816's primary-source comparison and duplicate/failure
searches unchanged. C759d(1)-(4) and C759f hypotheses/Proof1-2 were checked
for the actual metric, Fourier convention and scope: the accepted two-mode
comparison does not evaluate this payment residual. Suzuki's metric
observation is background coverage reused from816, not a new theorem
import or an essential extra source for evaluating the defined residual.
The inverse-frequency covariance interpretation, frequency-zero
integrability and full-domain signed domination remain unproved; evaluation
of the defined finite residual does not require assuming them. Matching
Mathlib coverage remains unchecked.

Decision remains SPECIALIZE, solely for the stated one-input calculation.
This is a process/source-traceability repair, outcome STALLED, with no new
mathematical evidence, no new discovery claim and no budget reset. Keep
the same zero threshold and stopping rule; the fixed-band test is not an
RH criterion or a proof of primitive lowering on the entire domain.
