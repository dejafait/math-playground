# Fixed three-width output: first-coefficient source review1905

TARGET: Assess source coverage for deciding the sign of c=sum_i a_i*p_(sigma_i)(0) for C034k's fixed interpolant via its exact cofactors, and for using c<0 as a small-parameter output-sign obstruction.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1905 narrowly compared C034k exact cofactors/attempt1904, C032j/l/m/q, C033l and failures1562/1564/1566/1894; reused reviews1562/1903 and searched signed-mixture Laplace complete monotonicity, square-root coefficients and Xi smoothing interpolation. No inspected result decides this exact three-width coefficient; search failure is not a novelty claim. Queries and inspected scope are recorded below.
SOURCE_EVIDENCE: Ante Mimica, Laplace transform, Dresden course27April-1May2015, Proposition1.4(i)-(ii), printed pp6-7, https://web.math.pmf.unizg.hr/~amimica/lt.pdf ; statement and complete necessity/endpoint proof directly revisited. Suvrit Sra, Some positivity properties of Riemann Xi under smoothing, fixed2611.00345v1,11November2026, Definition2.1, Theorem4.1 Gaussian case and AppendixA.7 PropositionA.8 with complete proof, https://hexagonmath.org/pdf/2611.00345v1 ; individual cusp, not a signed-mixture sign theorem. C032l and C032m supply the existing derivative interface and analytic majorants.
COMPARISON: Classical necessity and the individual square-root coefficient are covered; C034k supplies the fixed mass-one coefficients and determinant orientation. Their signed coefficient sum and a quantitative remainder for this exact output remain application work. Stop1564 imposed zero first coefficient for widths1,2; attempt1904 tested a third difference. Neither decides the present statistic. Tail and one-jump imports1562/1566 do not supply a sign or a remainder here.
GAP: Obtain a rigorous sign enclosure for c using the exact cofactors and complete profiles; if strictly negative, supply the finite analytic remainder and bounded positive-parameter test rejecting this output. No coefficient sign, new profile inequality, explicit margin or signed-tail conclusion is established by this review.
REASON: Essential source comparison for the changed three-width target is now complete. One bounded analytic application is covered in assessment1905; no general Hausdorff reproof, optional blocked-source retry or new mathematical derivation is needed in this literature turn. The newly written continuation remains subject to the supervisor separate approval.
SCOPE: Exactly C034k's existing coefficients and widths1,3/2,2; no added widths, coefficient fitting, higher-order sequence, scan in s or h, signed-tail inversion, or assumed positive quotient.

Main gap remains L030-L032/C032a actual-Xi all-degree positivity.
A negative first-coefficient obstruction, if justified, could reject
this fixed building block for positive-output approximation. A
nonnegative coefficient or unresolved enclosure would not prove
positive output, and would end that one proposed sign diagnostic.
The proposed research threshold is c<=-epsilon with epsilon>0 and a
controlled analytic remainder connecting it to a bounded output test.
This review licenses attempting that specialization, not its result.
Do not infer signed-tail asymptotics.

Essential inputs to inspect narrowly: C034k's exact cofactors/count,
C032j/m/q's law/lift/signed interfaces, C032l's stated first-derivative
formula, and C033l's residual identification. C033i identifies the
same residual. Use the earlier two-width first-odd calculation only
as a duplicate/failure comparison; do not rebuild it or add widths to
that stopped construction. Any heat-profile comparison needed for
the present coefficient must have its own source scope identified.

Retain the actual complete divisor, conjugation and multiplicities;
no ordinate zero; strict strip and gamma>14; counting; displacement
zero through100 and the retained real zero; reciprocal-square tail;
heat positivity and separate fixed-j error contracts; zero drift and
killing; Gaussian half-variance; both fixed-v1 qualifications. Their
independent validity is not established here. Output sign, uniform
accuracy, moments, full cancellation, signed height, actual-Xi
realization and a full matching Mathlib theorem remain unresolved.

No central creative construction is nominated: a span-preserving
sign/error operation or a concrete continuum-separation mechanism
with a decisive bounded test has not been identified. This source
question is a classical necessary-sign specialization, not a creative
mechanism and not progress beyond the inspected literature.

## Primary-source scope completed1905

Mimica's Proposition1.4 assumes a nonnegative Borel measure on
[0,infinity) whose Laplace transform is finite at every positive
parameter. Part(i) gives smoothness there and
(-1)^n L^(n)(s)=integral u^n exp(-s*u) dmu(u)>=0.
Its proof dominates difference quotients by an exponential at a
smaller positive parameter; higher derivatives use the same argument.
Part(ii) uses monotone convergence at the endpoint and identifies
finite endpoint derivatives with finite moments. That endpoint claim
is not a theorem for signed measures. In particular c concerns the
w=sqrt(s) analytic lift, not a finite first moment in u. For a
mass-one nonnegative law, the defining bounded kernel also gives
L(s)<=1. No density or exclusion of an atom at zero is required.
Only this necessity is needed; the complete-monotonicity converse
from Theorem2.4 is stronger and its existing review is reused.

Sra's PropositionA.8 assumes Theorem4.1's admissible even entire
probability kernel with the horizontal-strip decay of Definition2.1,
H_K>=0 and H_K not identically zero (or the stated strip-Poisson
case), and additionally p_K(0)>0. Its conclusion includes
B_K(s)=2*pi*p_K(0)*sqrt(s)+O(s) as s decreases to zero.
The proof splits the absolutely integrable Stieltjes profile into
p_K(0)*r^(-1/2) and a remainder, controls the latter using even C^2
regularity near zero and the profile growth at infinity, and
integrates the resulting derivative asymptotic. Its final
characteristic-function argument excludes a first absolute moment.
The Gaussian case and p_sigma(0)>0 are explicitly included in
Theorem4.1; C032j records their exact normalization and qualifications.
This review does not independently verify the source-wide heat or
finite-zero inputs. It does not apply Theorem4.1 to a signed sum of
kernels: a signed width output need not be a single reciprocal law.

The required ingredients for a separate local application are already
canonical: C032l records b_sigma'(0)=2*pi*p_sigma(0); C032m provides
the entire finite-sum lift and common disk bounds (8)-(9), allowing
a finite Taylor/Cauchy remainder; C032q supplies bounded signed
integration; C033l fixes the residual; C034k fixes the coefficients,
their cofactors, negative determinant and paid count. The research
step must assemble these for this output and decide the signed sum.
No reproof of the imported Laplace theorem or individual cusp is
justified. Effective cofactor/profile comparisons and the output
remainder are the identified difference; they are not imported from
an O(s) term with an unspecified constant.

## Search and duplicate limits

Queries used: `"Laplace transform" "signed" "square root" "coefficient"
positivity measure`; `"Gaussian" "Riemann Xi" "smoothing" "signed"
mixture`; `"signed mixtures" "Laplace" "complete monotonicity"
positivity`; `"Riemann Xi" "smoothing" "interpolation"`.
These located the existing smoothing paper and unrelated or broader
mixture/transform leads. Only the primary statements identified above
are evidence for this assessment. Search snippets, indexes and unread
leads are not imported theorems; no exact-sign or novelty conclusion
is inferred from them. Ready domination, signed-Tauberian and
convolution-tail comparisons in notes1562 are reused without new
claims about their missing hypotheses.

The local search was confined to the three-width assessments and
attempt, the named positive-output reviews and the named first-odd
failures. C032l's all-finite-family non-evenness and moment obstruction
does not decide this one coefficient or all-Borel output positivity.
The third-difference enclosure and stops1798/1894/1900 remain parked.
Full matching Mathlib coverage is unchecked/unknown; no new search of
Mathlib was needed for this source comparison. No lemma or mathematical
script was written and no scalar evaluator or coefficient calculation
was run. The bounded research specification is saved separately in
drafts/literature/2026-11-20-three-width-first-coefficient-test-1905.md.
