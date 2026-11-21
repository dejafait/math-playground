# Ordinary probability moments at the audited formal contacts: source comparison

TARGET: Test whether each of C874b's two positive-flux contacts admits some S_1>0 for which both ordinary Stieltjes matrices A_3=(m_(i+j)) and B_3=(m_(i+j+1)), 0<=i,j<=3, are positive definite, with m_j=(-1)^j(2j)![z^(2j)]exp(-sum_(k=1)^7 S_k z^(2k)/k).
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step2131 searched exact contact/Stieltjes, truncated cumulant, prescribed-cumulant and Gaussian-variance terminology; compared C874b,L044,L057,L058,L874,L936 and the September20/November9 stops and assessments. No inspected theorem or local result decides these two fixed-prefix curves; search scope and unread leads below, with no novelty claim.
SOURCE_EVIDENCE: Reused November9's inspected Curto-Fialkow1991 Theorem5.1 p625 and relevant Theorem4.1/Corollary3.4 proof cases; reopened the primary odd-Stieltjes statement, its explicit nonsingular-case remark and support argument pp622-625 at https://www.math.uh.edu/~hjm/v017n4/0603CURTO.pdf . L058/L874 supply normalization; C874b supplies the audited contacts. No new moment theorem or feasibility result was derived.
COMPARISON: The known odd-Stieltjes criterion covers the proposed matrices and explicitly suffices when both are positive and invertible; singular PSD also requires (m_4,m_5,m_6,m_7) in Ran A_3. L936's different fixed-panel positive-flux tuple has singular B_3 and different logarithmic prefixes, so is not an answer. L044/L057 do not prescribe either prefix.
GAP: Determine a positive S_1 for each prescribed prefix with A_3,B_3 positive definite, or prove the requested strict feasibility impossible for a specified contact. The theorem does not decide this one-variable restriction; no witness, density, actual-theta realization or actual flux sign is established.
REASON: Essential source coverage is complete for one exact finite-moment specialization using the known representation criterion and Sylvester's criterion; reproduce those tools by citation and calculate only the prescribed-prefix difference. The completed review authorizes no mathematics in step2131.
SCOPE: Only C874b's two contacts, m_0=1 and moments through m_7, with S_1>0 chosen separately for each; no actual-theta interval enclosures, higher-degree sweep, all-order completion or new signed mechanism.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED concerned the changed ordinary-moment constraint and its overlap with the fixed-panel seventh-moment work; this step completes that comparison and reuses existing source coverage.

Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
Intermediate use: determine whether an independent necessary condition
for a positive u^2 law removes these particular formal obstructions.
A positive-definite witness for each contact stops this finite
probability restriction as a way to exclude them. An exact
infeasibility argument would justify pursuing the identified restriction;
failure to find a witness alone is inconclusive. Neither outcome is
an actual-theta result.

Essential inputs: C874b,L058,L874. Use S_k=2, 2<=k<=7, or S_2=3
and S_k=2, 3<=k<=7, with S_1>0 free. The truncated exponential
specifies only coefficients through z^14, not a global characteristic
function. Retain singular range conditions if a moment sufficiency
theorem is used. Actual theta, tilt relations across parameters,
contact existence, initialization, equality and global/all-degree
closure remain unresolved. Mathlib coverage is unchecked.

## Primary theorem, applicability and proof coverage

Raul E. Curto and Lawrence A. Fialkow, *Recursiveness, Positivity, and
Truncated Moment Problems*, Houston Journal of Mathematics **17**(4)
(1991), 603-635, [Theorem 5.1, printed p625](https://www.math.uh.edu/~hjm/v017n4/0603CURTO.pdf),
characterizes real data gamma_0,...,gamma_(2k+1), gamma_0>0,
represented by a positive Borel measure on [0,infinity). In its
notation A(k)=(gamma_(i+j)), B(k)=(gamma_(i+j+1)), and
v(k+1,k)=(gamma_(k+1),...,gamma_(2k+1)). The equivalent conditions
are A(k)>=0, B(k)>=0 and v(k+1,k) in Ran A(k); a finite atomic
representing measure can be chosen. Here gamma_j=m_j, k=3 and
gamma_0=1, giving exactly A_3,B_3 and the displayed range column.
These are moments of x=u^2; gamma_j is not S_(j+2).

The paragraph immediately following Theorem 5.1 explicitly states
solubility when both A(k) and B(k) are positive and invertible. This
is precisely the requested positive-definite branch. Its range is
then the full space, so no singular inverse or missing range
condition is being suppressed. If either matrix is only PSD, the
original criterion and its range qualification must be retained.
Importing this statement does not supply an S_1 on either prescribed
curve. Conversely, failing strict definiteness would not by itself
prove absence of a singular representing measure.

Theorem 5.1 refers to Theorem 4.1 and its proof. Reused the full
November9 coverage of the singular reduction in Corollary 3.4,
pp615-616, and the finite-atomic support argument pp622-623;
reopened the latter relevant argument with the primary statement.
It first obtains an atomic Hamburger representation, then uses
polynomial interpolation to rule out atoms outside the interval
through the localizing inequality. Section5 specifies the lower
endpoint zero and drops the upper endpoint. The prior coverage
checked the printed inequality signs visually; this review reuses
that check rather than relying on OCR's ambiguous greater-than signs.
No representation theorem or singular-case argument needs reproof.

Use standard named Sylvester's criterion for real symmetric matrices
in the subsequent exact PD certificate. Checking positive leading
principal minors is valid for PD, not a substitute for all principal
minors when asserting PSD. No Schur reduction is essential here;
if one is used in a singular branch, retain the already assessed
range criterion rather than assuming invertibility.

L058's finite moments and L874's local logarithm justify the stated
cosine normalization for the actual law. In this target coefficient
extraction is only finite formal algebra through z^14, as already
specified in the nomination. A representing measure for x through
degree seven does not identify the actual kernel or assert that the
displayed truncated exponential is a global characteristic function.
The original C874b examples fix S_8=2 as well, giving their auxiliary
extension, but m_0,...,m_7 use no S_8 or higher coefficients. No new
coefficient formula, asymptotic argument or witness was calculated.

## Local duplicates and recorded failures

Read the exact hypotheses and conclusions of C874b and L874 and the
L058 normalization, then compared the following specific records:

- `ATTEMPTS/2026-09-20-theta-logarithm-relevance-audit.md`: ordinary
  Gram positivity does not survive the nonlinear logarithm. L044's
  canonical example already has a negative first logarithmic test;
  it does not prescribe either positive-S_2 obstruction prefix.
  L057's fixed-degree tests are strictly positive, with no prescribed
  null contact or coefficients. These are scope contrasts, not inputs
  proving feasibility or infeasibility here.
- `drafts/literature/2026-11-09-contact-conditioned-seventh-moment-scope-36.md`
  and `2026-11-09-contact-conditioned-seventh-moment-test-37.md`:
  reuse the odd-degree source coverage. Their class also fixes
  actual-theta panel moment boxes, a common mass and strict H1
  bounds; it permits raw singular PSD. It does not fix these prefixes.
- The nominated test was actually attempted: step38's midpoint tuple
  failed membership of the saved twelfth-moment interval, preserved
  in `ATTEMPTS/2026-11-09-contact-s7-midpoint-membership-stop-38.md`.
  The step39 refinement, recorded canonically in L936 and in
  `ATTEMPTS/2026-11-09-contact-s7-finite-data-sign-stop-39.md`, supplies
  a positive-flux member accepted by its later audit. Inspected L936's
  hypotheses, conclusion and construction through its raw matrices
  for this comparison, without replaying its certificate. It has
  S_2 between 0.00003717365974 and 0.00003717365975, whereas the
  present contacts fix S_2=2 or 3, and its B_3 is singular. Hence it
  is not either requested strict witness. It also does not assume
  C874b's positive H_3 extension. Preserve both earlier outcomes.
- `ATTEMPTS/2026-11-21-single-extension-contact-sign-stop-2128.md`
  and C874b's audited statement stop auxiliary-PSD-only signing,
  including further extensions of its atomic examples. They explicitly
  leave ordinary probability realization open. The present test adds
  a different necessary restriction rather than repeating extensions.

## Bounded external search and comparison limits

Queries actually issued on 2026-11-21 were `"truncated Stieltjes"
"cumulants"`; `"moment" "cumulants" "Gaussian" "positive definite"
Hankel`; `"S_2" "S_7" "contact" "Stieltjes"`; `"prescribed cumulants"
"Gaussian" moments`; `"truncated" "cumulants" "variance" "moment
problem"`; `"cumulants" "sufficiently large" "moment" Gaussian
positive`; `"prescribed cumulants" moment problem positive`;
`"truncated Stieltjes" "logarithmic"`; and `"truncated cumulant"
moment positive Hankel`.

No matching fixed-prefix result was inspected. The primary result
actually used is Curto-Fialkow above, not snippets or model memory.
Search leads about cumulant interiors (CausalSmith), coefficientwise
Hankel positivity under convolution (a secondary article index),
Marcinkiewicz/global cumulant truncation, and logarithmic Xi
inequalities remain unread and are not imported. None is essential
to using the established finite criterion and computing the exact
two curves; no theorem-level conclusion is attributed to these leads.
The finite-truncation scope explicitly avoids assuming all higher
cumulants vanish. This bounded comparison establishes no originality
claim and no general theorem about prescribed cumulants.

## Approved difference and continuation discriminator

SPECIALIZE authorizes one exact calculation of the unchanged TARGET
after this source-review turn. Existing source tools decide how to
certify a proposed tuple; the remaining task is the specific free-S_1
feasibility. An exact rational or rigorously certified algebraic S_1
for each contact, together with its complete moments and strict PD
certificate, would stop this degree-seven ordinary-moment exclusion
mechanism. A proof that the strict feasible class is empty for one
specified contact would decide that branch only, leaving singular
compatibility distinct. An unsuccessful bounded search is inconclusive.
If only one contact is decided, retain the other explicitly unresolved.

Save full exact evidence under the existing heat-script folder in
the research turn: normalization, the prescribed coefficient identities,
S_1>0, all leading-minor signs for both symmetric matrices, actual
values or rigorous bounds and required threshold zero. A floating
eigenvalue or preview is not a certificate. No new matrix degree,
parameter panel, actual-theta evaluator, all-order realization or
further auxiliary extension is authorized by this assessment.

Full matching Mathlib coverage is unchecked; supporting matrix or
moment results have not been inventoried and absence is not claimed.
No independent actual-kernel signed mechanism is justified yet;
this ordinary finite-moment specialization is not creative work.
