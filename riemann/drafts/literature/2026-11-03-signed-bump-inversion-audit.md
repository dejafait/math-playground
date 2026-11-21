# Nominated audit of the finite inverse-density and signed decomposition

TARGET: Critically audit L714's inverse-density identity (2) and signed decomposition (3), including the transform normalization, pole sign and fixed-bump interchange.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 184 reused the step-174 signed-bump assessment and L708 source record; compared L714 Sections 1--2, L713 Hypotheses/Section 1, and the signed-rate/absolute-contour ATTEMPTS records. Targeted primary-source lookup verified the cited finite-complex-measure statement, Fourier inversion conventions and residue theorem; no broad asymptotic search or novelty claim.
SOURCE_EVIDENCE: Kallsen--Kruehner arXiv:1607.02998v1 (11 July 2016), Appendix A definitions and Lemma A.1(6),(8)--(11),(14), pp.29--30, https://arxiv.org/pdf/1607.02998v1 ; NIST DLMF 1.14(i), (1.14.1),(1.14.3)--(1.14.5), https://dlmf.nist.gov/1.14.i ; 1.14(iii), (1.14.17)--(1.14.19), https://dlmf.nist.gov/1.14.iii ; 1.10(iv), (1.10.8), https://dlmf.nist.gov/1.10.iv . Exact scope and reading limits below.
COMPARISON: Known finite-complex-measure uniqueness/convolution, pointwise Fourier inversion under its hypotheses, and the residue theorem supply the general tools. They do not identify this family-specific continuous inverse or its signed contour decomposition. DLMF (1.14.17)--(1.14.18) is a definition/growth condition, not the exponential transform pair attributed to it locally; the audit must verify that elementary integral and the h scaling explicitly.
GAP: Audit the finite family-specific applicability: coefficients and j=0 term, absolute integrability/first moment, continuous representative at zero, Fourier normalization, rational pole locations/orientation and vanishing vertical sides, and the unchanged compact real bump interchange. No signed rate, nonvanishing of K_n/R_n, or L713 envelope bound is covered.
REASON: Essential source scope for the unchanged audit is now complete; SPECIALIZE authorizes checking the existing application, not accepting identities (2)--(3). General results should be imported, with only family-specific hypotheses and the elementary exponential integral verified. No mathematical audit or new result is performed in this literature-only step.

SCOPE: Exactly TARGET, with unchanged U=121/64, n=12q+3, N=n-1, A=27/10, h=A/n, d=5/4, c_0=1/8, c=3/20, u=(3+4i)/10, original chi and 0<delta=2*pi*w<1/3000. No signed rate, nonvanishing of K_n or R_n, endpoint asymptotic or Xi assertion is nominated.

## Original nomination and exact inputs (preserved)

The main gap remains actual-Xi all-degree mixed positivity and the
unpaid complementary spatial Jensen defect. L716 now supplies an
audited uniform nonzero standalone ratio on the entire fixed bump.
To use it in the actual signed observable, the finite inverse-density
identification and signed decomposition in L714 still need checking.
That audit is a necessary input check, not a new signed-cancellation
mechanism. No justified central creative target was obtained in the
L716 audit; the arbitrary fixed Gevrey endpoint and possible outer
cancellation remain explicit blockers to such a nomination.

Use the exact coefficients, scalar prefactor and root part of L714,
its definitions of p_n, B_n, K_n and R_n, and the narrowly needed
definitions and contour identity in L713. L703/L708 supply the original
fixed real bump, widths and transform convention if recovery is needed.
L715/L716 explain the downstream use, not a premise that can certify
L714's inverse identities. The L713 absolute-envelope estimate is not
needed unless the audit actually uses it; its separate unaudited
qualifications must not be silently imported. No other notebook is
an input.

First reuse the exact finite-complex-measure and transform source
evidence already saved in the signed-bump assessment and its named
local source records. Check the cited primary statements and relevant
proof cases only where required coverage is missing. Record whether
the pointwise continuous inverse and contour sign are covered or are
the family-specific assertions for audit. Do not reprove general
Fourier uniqueness, inspect unrelated asymptotics or derive and
approve the application in the source turn. No full matching Mathlib
theorem has been checked; this is not evidence of absence.

## Audit continuation test after approval

Accept only if (2)--(3) refer to the actual L713 continuous inverse
and signed R_n with the same positive-exponent transform and scaling,
including the j=0 term, both physical endpoints and unchanged fixed
bump. Every finite partial fraction, convolution/Fubini step, value
at zero, pole sign, and finite bump interchange must be justified.
No analytic continuation of chi is available. A specific failed
normalization, sign or unaudited essential premise warrants repair or
a qualified rejection of that inference; a sampled inverse is not
enough. The mathematical audit itself is not performed here.

Even acceptance leaves outer signed cancellation and its exponential
rate, other response terms, angular persistence, complementary defect,
amplitude/full charge, H/support, Xi realization and positivity open.
Keep the signed-bump inconclusive record and the absolute-contour and
positive-blend stops. They concern different claims and are neither
global bans nor permission to reuse their failed certificates.

## Completed source comparison — 3 November 2026, step 184

The original nomination above is retained as the record of what needed
review. Its instruction to complete source comparison is discharged here;
the application audit remains the next action, subject to the supervisor's
separate approval of this changed assessment.

### Exact target, duplicate and failure comparison

The main gap is actual-Xi all-degree mixed positivity, with the complementary
spatial Jensen defect still unpaid. This audit is an intermediate input check:
it would connect the accepted standalone L716 ratio to the original signed
bump observable through L714, without settling its cancellation. Relevant
local material read was L714's Hypotheses, Conclusion and Sections 1--2;
L713's Hypotheses and Section 1; L708's source interface (lines 65--108);
the step-174 assessment through its exact-data/source comparison and its
working record; and the signed-bump-rate and spatial-boundary-absolute-contour
ATTEMPTS records. The later root argument and envelope arithmetic were
not re-audited. No cross-notebook input is used.

The root/coefficient audit, polynomial log limit and L716 ratio audit do not
certify the inversion application. The absolute-contour stop concerns an
absolute envelope, while the signed-rate attempt explicitly leaves outer
cancellation unpaid. Neither is a duplicate proof or a reason to abandon
this narrower input audit. No new saddle literature is needed here.

### Inspected primary statements and applicability boundaries

Kallsen--Kruehner, *On uniqueness of solutions to martingale problems —
counterexamples and sufficient criteria*, arXiv:1607.02998v1, Appendix A,
printed pp.29--30, uses the unnormalized positive-exponent Fourier transform
of finite complex Borel measures. Lemma A.1(6) controls complex integrals
by total variation; (8)--(11) give convolution integration, variation
and product bounds; (14) states injectivity and multiplication under
convolution. Positivity/probability hypotheses are unnecessary. The
Appendix states these standard facts without individual proofs; this is
an import of the stated results, not an independent audit of their
underlying reference [6]. No infinite-convolution result is needed.

NIST DLMF, inspected 3 November 2026, §1.14(i), (1.14.1),(1.14.3)--(1.14.5),
uses positive exponent and symmetric normalization. Pointwise inversion
in (1.14.3) assumes L1 and local bounded variation, returning the mean
of one-sided limits; (1.14.4)'s continuous-derivative case is stronger.
Its convolution is normalized too. §1.14(iii), (1.14.17)--(1.14.19), gives
the Laplace definition and analyticity for piecewise-continuous data of
exponential growth in the indicated half-plane. Equations (17)--(18)
do not tabulate an exponential transform pair. These are statements,
not proofs of the present inverse identities.

DLMF §1.10(iv), (1.10.8), is the residue theorem for a positively
oriented simple closed contour with finitely many interior singularities,
analyticity otherwise and continuity to the contour. It supplies the
finite-rectangle theorem only; the infinite-horizontal-line passage
requires a separate vanishing-side bound in the audit. No general
contour shift with an unevaluated boundary remainder is imported.

Direct primary URLs are in SOURCE_EVIDENCE. The arXiv parsed statements
were fully available, including all selected subparts. One screenshot
request timed out; the complete selected statements were inspected in
the parsed PDF, so there is no essential source-access blocker. DLMF
hyperlinks redirect to the complete section pages; the numbered equations
and their surrounding hypotheses, not the page previews alone, were read.
No uninspected search snippet supplies a premise.

### What remains to specialize, and why this is not a reproof

Use the unnormalized complex-measure convention for the main argument;
if DLMF is used, explicitly reconcile its normalization and the variable
scaling by h. Retain positive exponent in the forward transform and
negative exponent in inversion. Verification of the elementary decaying
exponential integral is warranted because the local equation attribution
is incomplete and its sign/scaling are load-bearing. It does not justify
reproving general Fourier uniqueness or complex-measure convolution.

The audit must verify finite total variation and the absolute integrability
required by Tonelli--Fubini for the specific densities, rather than assume
positivity of a complex density. Equality of finite measures identifies
densities only almost everywhere. Pointwise identity with L713 therefore
requires a continuous representative, including the value at zero; if using
DLMF (1.14.3), local bounded variation must also be checked. It cannot be
replaced by continuity alone under that stated theorem. Alternatively the
standard L1-transform inversion theorem may be imported by precise citation
if needed; that alternative has not been source-assessed here.

For the contour step, inspect the rational kernel and finite rectangles
in L713 Section 1. Check every possible pole and contour orientation,
then justify passage to the horizontal integrals for each fixed n and
real v. A compact-bump uniform majorant or the appropriate absolute
Fubini bound is needed for any exchange involving the contour variable.
Finite sums commute with integrals only after each term's integrability
is established. No estimate uniform as n tends to infinity is supplied
by these sources, and none should be silently added to an exact finite-n
identity. The bump remains real and fixed; no analytic extension is used.

The necessary L713 premises are its finite complex convolution,
continuous inverse, integrable rational transform and signed contour
identity. Its absolute-envelope asymptotic, numerical certificates,
complete-family tail sizes and rate comparisons are outside this audit.
L714's partial fractions may be checked as needed without reopening its
already audited root theorem. L715/L716 remain downstream context only.
Full matching Mathlib coverage has not been checked; this is not evidence
of absence.

### Decision and bounded continuation test

SPECIALIZE covers exactly TARGET under the unchanged SCOPE. Accept
L714 (2)--(3) only after the actual continuous inverse, all normalization
factors, pole sign and real fixed-bump interchange pass, including j=0
and the value at zero. Otherwise repair a concrete failure or leave the
particular inference conditional. No rate calculation or sampled inverse
can substitute for this test. This turn has neither derived nor accepted
those equations. Source clearance changes local readiness only; it is
not progress beyond the cited general theorems or toward an RH resolution.
The earlier stops and all independent gaps remain.
