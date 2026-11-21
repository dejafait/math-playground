# Fixed-w theta-family zero: bounded reproduction test

TARGET: Attempt one rigorous Krawczyk certificate for a zero of Lagarias–Rains's xi_Q(3/2,s) in a rational disk contained in 40<Im(s)<45 and 0<|Re(s)-3/4|<2, retaining all integration and theta-tail errors and making no branch-connectivity or w=1 transfer claim.
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step423 completed the exact finite-certificate source gate in 2026-11-11-two-variable-fixed-slice-zero-certificate-review-422.md; its scoped duplicate/failure comparison and unsuccessful exact-certificate searches are reused without a novelty claim.
SOURCE_EVIDENCE: Lagarias-Rains https://arxiv.org/pdf/math/0104176v5 Theorem2.1/(2.9), printed pp8-9 and Section8 numerical lead p44; Rump https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf corrected author version, Theorem13.3/(13.8)/proof internal p89; Johansson https://arxiv.org/pdf/1802.07942v1 Sections2/2.1/3.2 and https://arxiv.org/pdf/1806.06725v1 Section1.4.2/(1.18)-(1.20)/Algorithm1; archived Arb2.23.0 https://arblib.org/acb_calc.html and python-flint callback contract https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.integral (0.9.0 inspected in step423; latest URL is mutable). Detailed hypotheses and prior inspection evidence remain in the completed source gate.
COMPARISON: Existing methods cover a conventional finite validated calculation, not a certificate for this slice. The family theorem supplies the exact function; Krawczyk supplies a sufficient existence criterion. Effective tail constants, a valid evaluator and a strict inclusion must be established in mathematics rather than assumed from numerical tracking.
GAP: No root, rational disk, tail constant, backend or Jacobian enclosure is certified. Analytic callback branch checks and uniformity in complex s are mandatory. A failure of the sufficient test will not exclude zeros in the domain.
REASON: One independently testable fixed-family geometry check can limit universal center-line-preservation proposals. It does not pay L984(H), prove an actual zeta zero off the line, or justify transporting zeros to w=1.
SCOPE: Step424 completed separate literature approval and repaired direct source URLs for the unchanged target; source methods are ready, calculation/backend remain unverified. One fixed w=3/2 calculation with a bounded locator stage and one certified candidate; no parameter sweep, connectivity analysis, global zero census or signed Li estimate. Preferred classification REPRODUCTION, task calculation.

Use the [completed step423 source gate](2026-11-11-two-variable-fixed-slice-zero-certificate-review-422.md)
for precise source statements, proof cases and qualifications. Reuse ready
inclusion/integration coverage; no further generic literature turn is
needed after separate approval while this target and its hypotheses stay
unchanged. Essential local inputs: L018 for the distinct w=1 RH target;
L019 for the theta convention only. The two-variable theorem is an
external input, not an installed local lemma. L984/C984a and C997s are
motivation/contrast, not premises. No cross-notebook input.

The exact function is F(s)=xi_Q(3/2,s). Import Theorem2.1 and equation(2.9)
with both rational pole terms and the stated completion factor. If a
different integral coordinate is used, justify the change and its
Jacobian. If a nonzero rescaling is used to reduce cancellation, prove
zero equivalence on the entire proposed disk. Keep the full completion
and theta normalization. Use s->3/2-s, not Section8's printed 1-s.

One attempt has the following finite boundary:

1. First establish an accessible rigorous arithmetic backend, recording
   its actual versions and exact input conversion. Default python3 has
   no flint module. A temporary environment is allowed; no credentials,
   key use or changes to shared infrastructure. If unavailable, save the
   concrete failure and stop this attempt without numerical substitution.
2. Optional locator work is limited to the 16 starting values
   Re(s) in {1,3/2,2,5/2}, Im(s) in {41,42,43,44}, with at most20
   iterations each and at most128-bit locator precision. These are
   proposed search seeds, not certified approximations. Select at most
   one candidate in the stated domain. Retain failed and out-of-domain
   locators; do not infer nonexistence if none is usable.
3. For that candidate use exact rational center c, rational real box X
   containing0, and exact rational preconditioner R for the two real
   components of F. Permit at most three enclosure refinements and
   precision at most384 bits. Save finite-integration ranges, theta
   truncation choices, callback analytic domains and the complete
   effective endpoint/infinite tail bounds. The source's O-term alone
   is not an error bound. Uniform bounds for F and its first derivative
   on c+X, including the logarithmic factors from differentiation, are
   needed. Justify differentiation using compact domination. Enclose
   every Jacobian matrix on c+X; do not replace that set by the derivative
   at its midpoint. Gaussian acceleration must reject branch-cut boxes
   for both the integration variable and theta's fractional power.
4. Apply exactly Rump Theorem13.3's strict interior inclusion, keeping
   all rational/rounding/truncation/integration errors. Save f(c), the
   complete Jacobian enclosure, X, R, the Krawczyk image and positive
   distances to every face. Certify a rational disk containing c+X
   whose closure stays strictly in the stated off-center domain; save
   all four geometric margins. Existence is sufficient. State only the
   uniqueness/multiplicity consequences actually justified by the test;
   no count outside the certified box or branch identification follows.
5. Save full proof/error/certificate evidence on disk and print actual
   versus required margins, failures and artifact paths. A prospective
   lemma requires canonical hypotheses, proof/citation, qualifications
   and Mathlib section; never treat structural validation as mathematics.

Continue only on an exact-function inclusion with positive analytic and
geometric margins. If the bounded attempt cannot obtain those margins,
record it as inconclusive, preserve the numerical leads and specific
failure, and stop this implementation. Do not repeat unchanged locator
or precision sweeps. A repeated attempt needs a materially improved
evaluator or independently testable mechanism. A certified negative
result requires an actual exclusion theorem/certificate, not failure of
Krawczyk. A source or package availability failure is not such a result.

The main RH gap is still actual-Xi positivity, forcing and unpaid H.
Even success here supplies only a finite limitation at w=3/2. Signed
Li-cost control, collision-aware transport and arithmetic information at
w=1 remain unresolved. No justified creative central target is supplied:
those missing inputs are not repaired by a root enclosure. Full matching
Mathlib coverage is unchecked and unknown.


## Separate approval and direct-link repair — step424

On 2026-11-11 the four primary PDF URLs now present directly in
SOURCE_EVIDENCE resolved. Rechecked Rump Theorem13.3 and its complete
proof on internal p89: the strict inclusion uses the full Jacobian set,
and gives a root in the translated image and injectivity on the box.
Rechecked Lagarias–Rains (2.6)–(2.10), especially both rational terms,
completion and reflection by w. Rechecked Johansson 1802.07942v1
Section3.2's manual-tail requirement and 1806.06725v1 Section1.4.2's
positive-denominator conditions and distinction between z-derivatives
and the needed s-derivatives. These checks confirm the recorded scope;
they add no effective constant, evaluator or root certificate.

The exact-statement/stronger-result and duplicate/failure comparisons
from step423 are reused, not rerun: the target and assumptions have not
changed. This is a process repair, honestly STALLED mathematically,
not a new source advance. The unchanged SPECIALIZE target is approved
for one bounded REPRODUCTION calculation under the existing limits.
Backend unavailability or failed inclusion ends that attempt inconclusively.
No generic browsing, lemma, mathematical script or numerical test was
performed in this approval turn. Mathlib coverage remains unchecked.
