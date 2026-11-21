# Target-weighted Radau enclosure — completed source comparison, step412

TARGET: Assess Li-Sra-Jegelka's Gauss-Radau bounds for rigorous eight-step enclosures of C997s's exact continuum target inverse form at n=64,128 and fixed lambda_n=exp(-n/16).
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step412 reused review410 and review369; searched Li-Sra-Jegelka repeated-eigenvalue/normalization cases and rigorous complex integration, and narrowly checked the local Gram assessments, C997c/C997s and stops341/410. Primary proof cases were accessible; no growing-n target estimate or prior local Radau certificate was identified. No novelty inference.
SOURCE_EVIDENCE: Li-Sra-Jegelka ICML2016 PMLR48 Section3/Theorem2 and Theorems6/8; supplement A.1-A.2, Lemmas11/15, complete Theorem21 proof including parity cases, Lemmas23/25/26 and Theorem27 proofs, and AppendixC through Corollary31, PDF pp1-10. arXiv:1512.01904v2 Section5.4 and Algorithm5 cross-check normalization/rounding. Johansson arXiv:1802.07942v1 Sections2/2.1, PDF pp2-4, supplies rigorous-integration contract. Clason/cap assessments reused.
COMPARISON: Exact-arithmetic Gauss/left-Radau bounds support a finite known-result specialization, not a guaranteed eight-step width or an all-n mass rate. AppendixC retains simple eigenvalues, and printed pseudocode has inconsistent norm factors; direct black-box import is rejected. A later research turn must justify cyclic compression, complex normalization, exact continuum products and outward arithmetic before using a sign.
GAP: No G,h,d, inverse form, F_n sign or E_n bound was computed. Local applicability and the original-cap conversion remain proof obligations, with a bounded precision/abort contract below; quantitative unbounded-n target mass remains entirely open.
REASON: Newly inspected source qualifications rule out copying the published algorithm without a normalization and degeneracy audit. The defining quadrature forms and accessible rigorous-integration input nevertheless support the separately nominated bounded reproduction. No new mathematical specialization is proved during this literature turn.
SCOPE: C997s's complete kernel, integer degrees exactly64 and128, I=[7/4,9/4], z_star=1+i/8, gamma_j=15/8+j/(4n), 0<=j<=n, original complex cap exp(sqrt(n)), ordinary Lebesgue Gram G_n, target h_n and d_n as proposed in review410; lambda_n=exp(-n/16) fixed. At most eight nonterminated Lanczos steps per degree; no regularization, node or degree sweep.
LITERATURE_REASON: At invocation start, primary Gauss-Radau sign, degeneracy and termination cases and rigorous continuum-input scope were essential unread coverage for a changed finite test; step412 completes that source comparison without reopening generic regularization.

## Original nomination retained: precise proposed test and relevance

The main gap remains L030-L032/C032a actual-Xi positivity, L966/L968
forcing and unpaid L984(H). The intermediate target here is SOURCE
COVERAGE for a bounded quantitative test of the capped point bridge.
It is a new lead, not ready mathematics or a claim that a favorable
finite target form has been found.

Use exactly review410's proposed G_n,h_n,d_n and F_n. The prospective
finite test would enclose the actual scalar

    h_n^*(G_n+lambda_n Id)^(-1)h_n

by target-started Gauss and left Gauss-Radau quantities, retaining the
original kernel and all its terms. It would seek a strictly positive,
outward-certified lower endpoint for the corresponding proposed F_n
at each of n=64 and128, after all matrix integration and arithmetic
uncertainties. This is a requested sign test, not a derived certificate
for E_n. A later research turn must first justify that relation and
pay the original cap and ordinary L2-to-sup conversion.

Eight steps is a fixed cap, not a convergence claim. Exact breakdown
must be treated by the correct invariant-subspace/termination case;
interval uncertainty is not exact breakdown. If the resulting lower
endpoint is nonpositive or the enclosure is too wide, the finite test
is inconclusive and the chosen short quadrature mechanism is parked.
Do not increase iterations, optimize lambda, fit a rate, or infer that
F_n itself is nonpositive. A positive result is only a finite relevant
input. The all-n target of positive F_n with exp(n/32)F_n unbounded
remains separate and would need an analytic estimate on an unbounded
sequence before refuting any big-O assertion for E_n.

## Original source-work request, resolved below

Primary paper: C. Li, S. Sra and S. Jegelka, *Gaussian quadrature for
matrix inverse forms with applications*, ICML2016, PMLR48,
https://proceedings.mlr.press/v48/lig16.pdf ; primary supplement:
https://proceedings.mlr.press/v48/lig16-supp.pdf . Read the exact
inverse-form setup, the left-Radau sign/remainder argument, relevant
recurrences and full proof cases. In particular inspect AppendixC's
support/cyclic-subspace treatment and the finite termination case,
rather than assuming a simple full spectrum or excluding a zero target.
The main text's condition-number rate is not exponential-precision
coverage for this application.

Determine whether realification of the complex Hermitian Gram problem
preserves the target quadratic form and correct normalization. The
realified matrix has repeated eigenvalues; the main text's initial
simple-spectrum statement cannot simply be quoted without its general
case. A local applicability proof may be approved for a later turn,
but must not be derived and approved during this source review.
Inspect whether the prescribed left endpoint must strictly precede the
spectrum, and select a justified positive lower endpoint from the fixed
regularization without assuming strict positivity of G_n itself. Any
interval recurrence must enclose the exact target-weighted quantities;
ordinary floating-point Lanczos bounds alone are not certificates.

Exact integration is an essential part of the proposed data. C997s(2)'s
finite polynomial-exponential antiderivative is available for kernel
values. Products needed for G_n and h_n require their own finite
integration and rounding justification, or a rigorous quadrature error.
Do not form G_n from sampled slopes or C999d's leading endpoint formula.
Do not assert that a primary theorem about exact matrix inputs already
certifies interval-computed entries. Identify these obligations before
approving any script. Full proof/replay evidence must later be saved
locally rather than replaced by a numerical preview.

Continue only if the inspected source cases and available exact-kernel
tools support this specified finite certificate with a concrete error
budget. Otherwise record the precise hypothesis or precision blocker
and park this method; no repeat generic-theorem review is authorized.
Reuse the completed Clason/cap comparison. No new asymptotic mass
bound, eigenvalue law or complete RH mechanism is preapproved.

## Inputs and prior failures

Essential inputs: C997c complete representation and C997s exact kernel,
cap and antiderivative method. C999d is comparison only: its error does
not pay this exponential precision. C997k/stop341 concern a different
operator and unpaid asymptotic target tail; they do not decide these
finite exact inverse forms. C997s's previous projected generators do
not calculate certified continuum Gram target forms. No stop is erased.

The downstream use, if a finite positive certificate survives, is a
reliable target-specific diagnostic for deciding whether a genuinely
new analytic mass estimate is worth preparing. It supplies no finite
fit, all-n obstruction, general-band theorem, selected/both-sign
transfer, C997a(8), reconstruction, complements/regulators, L993
arithmetic output, L984(H), signed forcing or actual-Xi sign.

Full matching Mathlib coverage is unchecked. No cross-notebook input.
The primary proof cases are accessible leads, not a persistent access
blocker. No mathematical attempt has been made on this finite test.
A future task after coverage would ordinarily be implementation/standard/
high, not a creative proof attempt. No justified central creative target
is ready: target mass remains unpaid, and a numerical theorem application
must not be relabeled creative to satisfy scheduling preference.

## Completed comparison — step412, 11 November 2026

LITERATURE / literature_comparison / NOVELTY_UNCHECKED; outcome NEGATIVE
for direct black-box import. The new evidence changes the implementation
contract, not the prescribed mathematical object. SPECIALIZE authorizes
only the later local applicability work and two finite tests nominated in
[review412](2026-11-11-target-radau-certificate-review-412.md), subject to
the supervisor's separate approval. No lemma or mathematical script was
created or edited; PROOF and DAG require no change.

### Primary contracts and proof cases actually inspected

**Li–Sra–Jegelka.** *Gaussian quadrature for matrix inverse forms with
applications*, PMLR48 (2016), pp1766–1775,
[Section3/Theorem2 and Theorems6/8](https://proceedings.mlr.press/v48/lig16.pdf#page=3).
The setup uses a real SPD matrix with simple eigenvalues and a positive
left endpoint strictly below its spectrum. Gauss is a lower bound;
left Radau is an upper bound. Theorem6 compares upper rules; Theorem8's
rate depends on conditioning and does not promise eight-step accuracy.

[Supplement](https://proceedings.mlr.press/v48/lig16-supp.pdf): A.1–A.2,
pp1–3, gives the remainder formula with derivative order 2r+m and
factor I[rho_m pi_r^2]; for 1/x its signs yield Lemma11's bounds.
Theorem21, pp6–7, treats both parities and reduces its final comparison
to a nonnegative expression. Lemma15, p4, treats exact termination by
zero coupling and vanishing remainder. AppendixC, pp9–10, retains simple
eigenvalues and positive active support; Corollary29 gives restricted
exactness. It does not explicitly cover repeated eigenspaces or u=0.
The k-step statement needs actual active support, not just an enclosing
span. Lemmas23/25/26 and Theorem27's complete proofs were inspected;
no rate is used here.

[arXiv:1512.01904v2](https://arxiv.org/html/1512.01904v2#S5.SS4),
28 May2016, Section5.4, discusses loss of orthogonality and leaves
numerical stability beyond scope. Algorithm5 prints norm factors
inconsistent with the normalized Jacobi identities and Theorem12's
squared norm. Treat pseudocode as unsafe for direct transcription.

**Rigorous continuum integration.** F. Johansson, *Numerical integration
in arbitrary-precision ball arithmetic*, arXiv:1802.07942v1,
22 February2018, [Sections2/2.1, PDF pp2–4](https://arxiv.org/pdf/1802.07942#page=2).
The supplied integrand must enclose values and validate analyticity on
complex rectangles. The algorithm uses a direct box enclosure or a
Gauss rule with an analytic-ellipse error bound, then bisects.
Requested tolerances are guidelines; output radii, including parameter
uncertainty and cancellation, decide achieved accuracy. This is an
available alternative, not a certificate for our products. A conjugating
callback cannot simply assert holomorphy.

The narrowly followed Bai–Fahey–Golub 1996 author PDF was readable only
through the opening algorithm, printed pp73–75; later requests timed
out. Its remaining proof cases are an unread, nonessential lead, not an
import. PMLR and the arXiv v2 HTML supplied the essential cases above.
Direct shell downloads failed DNS; this did not prevent web inspection.
Searches used the paper title with repeated eigenvalues/Lanczos
normalization, and Johansson rigorous complex integration. Other search
hits, book previews and stability papers are not assessed inputs.

### Local differences to justify later, not results derived here

Use C997c/C997s and review410's exact G,h,d,F definitions, original
complex cap and ordinary Lebesgue measure. Reuse review410's inspected
Clason Lemma6.3/Theorem6.5 and review369's cap assessment; a citation
alone does not establish their local relaxation and sup conversion.
There is no reason to reprove a general regularization or quadrature
theorem. The following applicability checks are the identified difference:

- Verify the standard real block representation of a Hermitian matrix
  and a complex vector, preservation of the inverse form and squared
  norm, and absence of any factor two. Use the finite-dimensional
  spectral theorem to justify compression to the target's cyclic
  subspace, retaining one active direction per distinct eigenvalue.
  Do not claim AppendixC already proves that reduction. Handle zero
  target and exact early termination separately, before division.
- Establish PSD of the exact integral Gram matrix and a certified
  strictly positive left endpoint strictly below the regularized
  spectrum. A proposed endpoint is half a certified positive lower
  bound for the fixed lambda, not equality with the possibly attained
  spectral floor. Prove this choice locally before using Radau.
- Normalize the starting vector, evaluate the defining Jacobi inverse
  entries, and restore the squared norm once. Use r ordinary Lanczos
  steps for J_r and the r+1 left-Radau augmentation with its prescribed
  endpoint; the artificial last diagonal is not another Lanczos step.
  At most eight matrix-vector steps per degree. Never divide by an
  interval containing zero or confuse uncertain breakdown with exact
  termination. Interval loss of orthogonality requires enclosure of the
  exact recurrence, not a floating reorthogonalization heuristic.
- Obtain G,h,d from complete continuum products. C997s(2)'s primitive
  covers kernel values, not automatically their products. A future
  proof must expand the finite endpoint expressions, multiply before
  slope integration, and check conjugation and every combined exponent,
  including a possible zero exponent. Use exact polynomial primitives
  for that case. Outward polynomial/exponential evaluation may reuse
  audited C997s arithmetic; all new product/integration identities need
  their own proof. Alternatively use Johansson's contract with a
  justified analytic extension and certified error. No sampled slopes,
  leading endpoint approximation, or empirical precision agreement.

These are routine known-result applicability questions approved for a
later reproduction, not new source-free lemmas declared true here.
They leave no essential inaccessible theorem; implementation precision
and successful sign remain tests, not assumptions of the assessment.

### Concrete finite certificate and abandonment contract

Keep n=64,128, lambda=exp(-n/16), every prescribed column and B=exp(sqrt(n)).
Use one fixed 2048-bit arithmetic run (or directed Decimal precision at
least equivalent); no precision, degree, node or regularization sweep.
Require absolute coordinate widths <=2^-256 for continuum entries,
lambda and B. Require each computed Gauss/Radau endpoint's arithmetic
enclosure width <=2^-64; their mutual gap is separate quadrature error.
After propagating all d and penalty uncertainty, require endpoint
arithmetic widths <=2^-60 for the proposed F enclosure. These are
acceptance budgets, not asserted achieved errors or sufficient a priori
entry perturbation estimates. Full interval propagation must verify
them; cancellation or small Lanczos denominators may defeat them.

The later proof must justify which inverse-form endpoint gives the
lower F endpoint, and the relation to the original capped E_n. Seek a
strictly positive certified lower F endpoint at BOTH degrees, retaining
the entire quadrature gap. Nonpositive lower endpoint, oversized gap,
failed precision budget, uncertain termination or denominator failure
parks this eight-step method and saves all evidence. It does not prove
F<=0 or small E_n. Do not spend another turn merely tuning this test.
Exact termination may give an earlier exact Jacobi form only after its
invariance is proved; interval containment of zero is not that proof.

Save complete continuum inputs, recurrence enclosures, spectral endpoint,
normalization, step counts, all scalar intervals and failures to a local
certificate in the later research turn. A positive finite sign would
motivate a separate analytic target-mass assessment; it establishes no
unbounded-sequence rate or RH input. Preserve stops341/410 and all
independent gaps listed above. Full matching Mathlib coverage remains
unchecked. No cross-notebook theorem is used.
