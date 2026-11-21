# Cosh base and one three-factor block: prospective test1689

TARGET: Test whether F(s)=((1+s)((s+2)^2+1)/5)cosh(sqrt(s)) is the normalized entire reciprocal of order 1/2 with strictly positive Taylor coefficients of one smooth positive self-decomposable density whose translation minors of every fixed order are positive near zero but which is not globally PF.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1689 searched the combined entire/self-decomposable/local-PF conditions, rational complex-pole constructions, exact cosh reciprocal terminology and the narrow local PF/reciprocal/stable/Schoenberg assessment/attempt paths; reused1685/1686 and compared1247 and the October31 strict-PF256 scopes. Full query and duplicate record: source-notes1689. No complete matching construction or novelty claim.
SOURCE_EVIDENCE: Direct sources: https://dlmf.nist.gov/4.28#E2 , https://dlmf.nist.gov/4.33#E2 , https://dlmf.nist.gov/4.36#E2 ; https://arxiv.org/pdf/2101.02129v2 ; https://arxiv.cnoctave.top/pdf/2611.02944 ; https://arxiv.org/pdf/1302.0956v1 . DLMF4.28.2/4.33.2/4.36.2 supplies the cosh definition/series/product; BGKP2101.02129v2 Theorem1.2 pp1-2 supplies the one-sided real-product law/smoothness and conditional global-PF obstruction; Sra2611.02944v1 C.17 proof pp38-39 supplies the positive three-factor inverse template, C.25 pp44-45 supplies the saddle/differential-determinant method, and C.1/C.16 pp20/37-38 the interval transfer; Simon1302.0956v1 Section3.2 pp9-10 supplies the spectral self-decomposability criterion. Exact readings, hypotheses and qualifications are in source-notes1689.
COMPARISON: None of these sources asserts the full fixed-object conclusion. Known results cover the base, finite inverse template, spectral criterion and transfer tools. The missing work is the ordinary analytic specialization to this same fixed factor, including its changed complex asymptotic and spectral monotonicity; reproducing general PF or self-decomposable theory is unnecessary.
GAP: Prove or refute every stated obligation for this single F; in particular do not replace all fixed orders for one law by a family depending on m, use weak Gaussian convergence for derivative determinants, or infer a law from positive coefficients/nonreal poles. No construction has been proved yet.
REASON: A successful fixed-object test would rule out the stronger generic bridge left open by C028m's lack of an entire reciprocal, while leaving actual-Xi realization and S_F=0 unresolved. The cited methods cover all essential tools without a blocked source.
SCOPE: One fixed factor q=1,A=2,b=1 multiplying the cosh entire-series base. No parameter search, actual-Xi theorem application, global-log-concavity hypothesis, or global PF2 failure claim. Source-link recovery1690 completed the separate literature approval; no mathematical invocation occurred in either review1689 or recovery1690.

## Exact obligations and bounded test

Read [source-notes1689](2026-11-19-entire-reciprocal-conjugate-source-notes-1689.md)
for the inspected primary locators and their scope. C028m/stop1686
are motivation and an audited method contrast, not a premise that
the present density exists. C028g supplies the target analytic
hypotheses only; none of its actual-Xi conclusions is assumed here.

Interpret cosh(sqrt(s)) by its entire series. The proposed F must
satisfy F(0)=1, exact order1/2 and strictly positive coefficients
in its ordinary Taylor series. Establish a single probability
density p, positive on (0,infinity), with a C-infinity zero
extension, whose Laplace transform is 1/F(s) for s>=0. Verify all
transform, convolution, convergence and normalization hypotheses
when importing the product and three-factor inverse results.

For self-decomposability, identify the real spectral representation
using the cited complex Frullani case, justify every interchange,
and prove its spectral function nonnegative and nonincreasing with
the required integrability. Positivity of a candidate Levy density
alone is insufficient. This test is for the complete fixed object;
a finite-block criterion can be used only with its hypotheses paid.

For each integer m>=1 prove the existence of epsilon_m>0 such that
all ordered translation minors of sizes 1<=k<=m are strictly
positive whenever every cross difference belongs to (0,epsilon_m).
One possible assessed method is to prove the centered standardized
negative-tilt density derivatives converge through every fixed
degree to the Gaussian derivatives, and then use the signed Gram
determinant, tilt/scale congruences and C.16. For this new cosh law
the large-frequency dominator and whole-interval coverage by the
tilted mean must be proved anew. There is no order-uniform interval
requirement. No finite sampling, continuity in b for each m, or
unstated differentiation under an integral suffices.

Finally use the cited Schoenberg theorem only after identifying
the same law/transform to test global PF. Verify analytic uniqueness
on the appropriate common domain and the nonreal-zero obstruction;
an explicit negative minor is an alternative, not a required size-two
witness. Failure of global PF need not mean failure of PF2.

Continue this object only if every obligation can be met. On a
failed obligation preserve its exact evidence and reject this fixed
construction, without claiming the generic enriched bridge is true.
Changing the factor requires a new assessed target. A completed
countermodel remains pending independent critical review. The full
actual-Xi sign gap, realization and arithmetic input remain open.
No numerical sweep or mathematical script is needed to invoke this
analytic test. Matching Mathlib coverage has not been checked.

Recommended classification for the later mathematical step:
REPRODUCTION. This is difficult development of a reviewed analytic
method, not a new creative mechanism at the actual-Xi central gap.

## Direct-source recovery1690 (19 November 2026)

LITERATURE_REASON: Supervisor required direct source URLs in this ready
assessment; the target and its mathematical hypotheses are unchanged.

The URLs now appear in SOURCE_EVIDENCE itself. Opened the exact BGKP v2
and Simon v1 PDFs and the same 53-page Sra manuscript mirror recorded
in source-notes1689; confirmed titles, versions where displayed, and
the load-bearing statement locations: BGKP Theorem1.2 printed p2,
Simon Section3.2 printed pp9-10, Sra C.17 printed pp38-39 and C.25
printed pp44-45. Rechecked the three DLMF formula pages. The Sra URL
is a mirror of the primary manuscript, not an independent source or
a newly inferred author version. Reused the already inspected full
proof cases in source-notes1689; did not repeat their proof review.

The comparison is unchanged: C.17's finite-window law varies with
order/window; C.25 concerns the actual Xi law. They supply methods,
not the claimed combined fixed-object theorem. BGKP's positivity and
smoothness interface and Simon's nonincreasing spectral function
criterion retain all their recorded hypotheses. Bakan-Ruscheweyh is
an inspected comparison, not an essential positive-density input.
No essential source blocker remains for the exact SPECIALIZE test.

This is a valid metadata/source-link repair, honestly STALLED as
mathematical evidence: no new theorem, counterexample or source-scope
change. The same bounded test is approved for the next mathematical
turn. All obligations and unresolved actual-Xi assumptions above
remain open. Mathlib coverage remains unchecked.
