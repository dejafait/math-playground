# Quantitative positive-strip Harnack test

TARGET: Apply disk Harnack to test whether every analytic majorant in the stated mesoscopic rectangle class satisfies integral_R f_T(x)K(x)dx>=c_* log T for one absolute c_*>0 and all sufficiently large T.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed exact-class search and primary-source comparison in drafts/literature/2026-10-30-positive-analytic-window-majorant-feasibility.md; this continuation is precisely its disk-to-strip necessary-bound test, with no new arithmetic hypothesis or search.
SOURCE_EVIDENCE: Axler--Bourdon--Ramey, Harmonic Function Theory, second edition, author PDF dated 17 July 2020, Theorem 3.4 and (3.5), printed pp. 47--48, https://axler.net/HFT.pdf#page=54. The complete disk proof and open-domain limiting case were read in the parent review; the same-kernel real-axis extremal comparison is recorded there.
COMPARISON: The source controls ratios of positive harmonic values on interior disks. The target additionally chooses uniform disks in the moving strip and integrates their real-axis lower bounds against K. This is an ordinary quantitative specialization, not a direct citation of the detector integral inequality or a claim of originality.
GAP: Check weak positivity, the strict rectangle cutoff, disk containment, a common large-T onset and a positive lower bound for K away from its central zero. The proposed order-log-T bound is not yet proved.
REASON: The test can decide feasibility of the everywhere-positive analytic detector without the stopped Green covariance or selected-amplitude moments. No reproof of Harnack or new zero theorem is needed.
SCOPE: Exactly the class and scale stated below; one necessary-bound calculation and decision, not construction, moving-test arithmetic transfer, other scales or RH.

## Exact hypotheses and threshold

Use L=log T, delta=log L/L, B_T=L/(4pi),
a_T=delta L/pi, b_T=delta L/(4pi), and
K(x)=1-(sin(pi x)/(pi x))^2 with K(0)=0.
For each sufficiently large real T the proposed f_T is even entire,
real on R, with smooth Fourier transform supported in [-R,R] for one
fixed R>0. Require

    Re f_T(x+iy)>=0     (x real, |y|<B_T),
    Re f_T(x+iy)>=1     (|x|<=a_T, b_T<|y|<B_T).

Seek an absolute c_*>0 such that the integral in TARGET is at least
c_* L, independently of f_T and R. This is a proposed conclusion only.
Compare any proved lower bound with the original required upper scale
C delta L exp(-c delta L), for arbitrary fixed positive C,c.

Use the cited disk inequality, whose constants depend only on the
relative interior radius. The calculation must explicitly choose an
interior rectangle point and a real interval, handle u=Re f_T>=0,
and establish integrability and the kernel comparison. Do not silently
replace strip positivity by positivity only at actual zeros. The Fourier
conditions remain in the class even if the necessary bound does not
need their full strength.

## Relevance, inputs and bounded decision

Main gap: actual-Xi all-degree positivity and initial signs at unbounded
heights. A small positive analytic main term could have supported the
weighted off-line-count route. Proving the proposed incompatible lower
bound would instead park this sufficient detector class and prevent
unjustified use of Bettin--Fazzari's fixed-test statistic.

The geometric calculation needs no local lemma input. For interpretation
only, L018 supplies zero coordinates and reflection pairing, and L501
records the different stopped Green implementation; neither is a premise
for the necessary bound. Reuse the Bettin--Fazzari theorem via the parent
and exact-amplitude assessments. RH, simplicity, spacing, independence,
external zero-free half-planes and weighted zero moments are not assumed.
Uniform moving-test errors, height-weight and kernel transfer, other
scales, complementary masses and individual signs remain unresolved.
Mathlib coverage is unchecked.

Continue only through this one quantitative test. If the lower bound is
proved, record the class obstruction without refuting signed detectors,
the weighted-count target or RH. If it fails, preserve the exact failed
hypothesis/geometry and reassess before constructing anything. This new
ready continuation is subject to the supervisor's separate approval;
no mathematics was performed when it was written.
