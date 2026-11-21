# Fixed signed-energy mass test: nominated research scope

TARGET: Construct and justify a fixed signed-convolution density for M_0(lambda)^12 det H2(lambda), then seek a certified alternating triple of its masses on the 32 fixed energy cells (j/4,(j+1)/4), 0<=j<32, without refinement.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed step46 exact-object, Laplace/Descartes and duplicate searches in 2026-11-09-actual-h2-signed-convolution-discovery-45.md; no inspected source supplies the actual fixed-density oscillation premise. No new search or novelty inference is claimed here.
SOURCE_EVIDENCE: Tokarev, J.Aust.Math.Soc.91(2011),415–420, Definition5/Theorems1/7/Remark8, https://doi.org/10.1017/S144678871100156X ; Bhaskar–Song arXiv:1309.5056v3 Definition3/Theorem4 and proof pp7–9,14, https://arxiv.org/pdf/1309.5056v3 ; DLMF1.14.30–31, https://dlmf.nist.gov/1.14#E30 and https://dlmf.nist.gov/1.14#E31 . Direct sources reopened in step47; step46 detailed proof review and L019/L058/L874/L917 coverage reused with unchanged qualifications.
COMPARISON: Standard convolution and finite-log algebra cover the method, not the actual signed-mass obstruction. The energy variable retains the exact theta law and differs from L915's contact residual, L937's relaxed box and L922's stopped Taylor implementation.
GAP: Verify proposed M_0^12 clearing, construct the exact density, establish regularity and absolute exponential moments, and determine whether three fixed-cell masses have strictly alternating signs. No construction or sign has been derived. Absence of a finite obstruction cannot prove global one-crossing.
REASON: Method coverage supports nomination of one bounded actual-law proof attempt at the finite H2 parameter gap, with separate source-gate approval completed in step47. Bounded searches did not establish coverage of its signed-mass conclusion; originality is uncertified.
SCOPE: Exactly TARGET; separate source-gate approval completed in step47. One normalization and 32-cell test, without parameter/degree/cell/precision sweeps, optional positive factors, endpoint calculation or reopening stopped enclosures. Full/supporting Mathlib coverage is unchecked.

The separate literature-only source-gate review in step47 approves this
unchanged target for a later research turn. No mathematical identity is
established here. Supervisor scheduling remains external.

The main gap remains L030–L032/C032a actual-Xi all-degree mixed
positivity. The intermediate target tests a necessary premise of the
parameter zero-count mechanism. A full crossing bound and independent
endpoint signs could support degree-two contact exclusion; this test
can instead give a scoped obstruction. Higher degrees and RH remain open.

Essential inputs: L019, L058, L874 and L917's audited finite-log and
determinant formulas. Use M_k(lambda)=integral u^k exp(lambda*u^2)K(u)du
with the exact K and L874's local logarithm/H2 conventions. No contact,
PSD, RH, deformed real-zero law or arbitrary substitute law is allowed.
L915/L916/L922/L936/L937 are contrasts only. No cross-notebook input.

First verify whether M_0^12 clears the determinant using the existing
finite algebra and record the exact polynomial. The exponent is a
proposal to check, not an established input. Construct the signed measure
using one-sided convolutions of the square-coordinate moment measures
in this polynomial. Specify all coefficients, factorials and mass factors;
do not add an optional convolution or positive lambda-dependent factor
to improve signs. Report a defect instead of silently changing the target.

Prove the representation with the full actual K, a fixed continuous
density v on [0,infinity), and absolute bounds for
integral (1+E)^r exp(bE)|v(E)|dE for every finite b>=0 and integer r>=0.
Justify singular factor origins via Tonelli/Fubini and prove the final
density's regularity. Check nonzero density on an interval before any
zero-count invocation. Handle possible zero intervals, boundary atoms
or an identically zero result explicitly. The tilt is +lambda, so the
conventional Laplace variable would be x=-lambda. Retain step46's
dominated-differentiation qualification. No general source reproof is needed.

The sole finite obstruction test is

    I_j=(j/4,(j+1)/4), 0<=j<32,
    B_j=integral_(I_j) v(E)dE.

Seek i<j<k with certified nonzero B_i,B_j,B_k and alternating signs.
Prove why such a witness excludes the at-most-one-sign-change premise.
Point samples, uncontrolled numerical convolutions or zero-containing
enclosures are not witnesses. Any calculation must pay the full theta
sum, finite algebra and integration error. Existing univariate quadrature
code is not an imported theorem for a new singular/multidimensional code.

Stop after this fixed test. A certified alternating triple is decisive
negative evidence for this normalization's sufficient mechanism. Without
one, report achieved signs/uncertainties and the missing estimate; do
not infer low variation or enlarge the test. Preserve partial reasoning
and reassess before repeating. Global crossing control, endpoint signs,
other degrees, initialization, realization and continuation remain open.

The proof_attempt/creative recommendation concerns actual-law convolution
cancellations and the oscillation obstruction. Denominator clearing and
known convolution identities alone are routine specialization and do not
complete the test or establish progress beyond the sources checked.

## Step47 direct-source repair — 9 November 2026

LITERATURE_REASON: The supervisor reported missing direct URLs in this
ready assessment; this is a bounded citation/access repair, not a new
search for unchanged mathematics. The exact TARGET and EXPLORE decision
are preserved. Reused step46 duplicate/failure checks without reopening
L915/L916/L922/L937 or reading unrelated notebook material.

Reopened [Bhaskar–Song v3](https://arxiv.org/pdf/1309.5056v3),
Theorem4 (reprint p9) and full proof (p14). Its multiplicity assertion
and first-crossing induction match the previous comparison; explicit
absolute exponential domination remains mandatory for the improper
integral and its derivatives. No unconditional application is approved.
Reopened [Tokarev publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/CB397B7DDF0A79680D67334501C2ADDB/S144678871100156Xa.pdf/div-class-title-a-generalisation-of-descartes-rule-of-signs-div.pdf),
Definition5, Theorems1/7 and Remark8 (pp416–417); reused the prior proof
review. The continuous-density scope avoids importing its general
Hahn-decomposition wording as an arbitrary-null-set theorem.
Reopened [DLMF convolution section](https://dlmf.nist.gov/1.14#E30),
including E31 and its piecewise-continuity hypothesis. Singular factors
still require separate absolute-integrability/Fubini justification.
No essential source blocker remains; Jameson remains an unread antecedent.

This repairs the reported process defect only: STALLED as mathematical
outcome, no new sign, density, bound or theorem. The single fixed 32-cell
test remains the next action. No lemmas, mathematical scripts, DAG or
PROOF changes were made. Full/supporting Mathlib coverage remains unchecked.
