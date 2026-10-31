# Genuine rectangle-positive witnesses: quantitative approximation coverage needed

TARGET: Review fixed-bandwidth Runge approximation with global weighted-L1 control as a way to construct genuine H_a functions with Q_a(f)/(a M(f)) unbounded.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded fixed-bandwidth/Runge, complex-approximation, superoscillation-energy and weighted-L1 searches; inspected four primary sources below and reused the parent positive-class and signed-gap assessments. No matching moving-rectangle weighted-L1 theorem identified; no novelty inference.
SOURCE_EVIDENCE: Chremmos--Fikioris arXiv:1504.04822v1 Section II (2)--(4), pp. 4--5 and Section V p. 8; Karmakar--Jordan arXiv:2306.03963v1 Section III A (24)--(27), p. 5; Ferreira--Kempf IEEE TSP 54 (2006), Sections III--IV/Theorem 2, pp. 3736--3738 (formula extraction qualified below); Ruland--Salo author manuscript Theorems 2--3, pp. 1--2 and Section 4, pp. 6--8. Exact scope and read proof cases below.
COMPARISON: Inspected methods provide real-interval approximation, finite real interpolation with L2 cost, or bounded-domain elliptic approximation with boundary Sobolev cost. None supplies simultaneous H_a positivity and the required global weighted-L1 ratio. The bump-envelope construction explicitly permits smooth spectra and shrinks bandwidth under dilation; this identifies a separate quantitative norm test, not an admissible counterexample.
GAP: Genuine H_a nonemptiness, uniform continuum complex-rectangle control and an upper bound for M relative to positive Q remain unproved. Qualitative Runge is parked; a separately nominated slow-dilation norm calculation tests one explicit source family only.
REASON: The required new coverage was reviewed without deriving mathematics. The search did not settle the target; it replaces the qualitative approximation lead with an independently testable bandwidth/norm tradeoff. No essential inaccessible theorem is assumed.
SCOPE: Completed literature comparison only; no new lemma, construction, mathematical script, L503 application, arbitrary-measure optimization or actual-Xi transfer. The original H_a target is unchanged; the new narrower calculation has a separate assessment and requires later approval.

## Exact proposed mathematical target, not an established result

Use L504 for definitions only. Fix R>0 independently of T, with
L=log T, a=log L/pi, b=a/4, B=L/(4pi), lambda=pi/(2a) and
K(x)=1-(sin(pi x)/(pi x))^2, K(0)=0. V_R consists of even entire
functions real on R, with C_c^infinity inverse Fourier data supported
in [-R,R], using exp(2pi i v z). There is no uniform bound on Fourier
derivatives. Set

    M(f)=integral_R |f(x)|K(x)dx,
    Q_a(f)=-integral_0^b exp(-lambda y)
                       [Re f(a+iy)+Re f(-a+iy)]dy.

Genuine H_a membership means

    Re f(x+iy)>=1 for |x|<=a and b<|y|<B.

No sign in the gap or outside this rectangle may be added. A future
counterexample test would seek a sequence of real T_j tending to
infinity, a_j=log log T_j/pi, and f_j in H_{a_j}, for one fixed R,
with Q_{a_j}(f_j)/(a_j M(f_j)) tending to positive infinity.
This sequence would refute the geometric one-sided Q bound, not RH.
No such sequence or finite approximation step has been derived here.

The proposed mechanism is simultaneous approximation: enforce the
positive rectangle and a negative side-gap profile while controlling
the full real-axis weighted L1 cost. Ordinary qualitative density on
compact sets is insufficient. Its constants may explode with B or
with the prescribed gap transition and destroy the ratio. The future
review must test this issue rather than treat Runge's name as coverage.
Evenness, reality, smooth Fourier support and the normalization 1
must all survive; nonemptiness of each admissible class is not assumed
without justification. A slightly larger closed positive rectangle
may be useful in a theorem comparison, but any change requires an
explicit applicability argument and cannot silently weaken H_a.

## Comparison of three possible continuations

1. Further scalar or arbitrary-measure certificates: L505 closes the
   two-scalar family; no positivity-sensitive quantitative replacement
   is currently justified. Do not repeat the coefficient search or
   infer that arbitrary measures are excluded.
2. Direct admissible-function approximation: selected. This changes
   the object tested from a full-space dual norm to genuine H_a
   witnesses and targets Q directly rather than the stronger E bound.
   The prior Runge lead has no inspected quantitative theorem; review
   that missing input before attempting a construction.
3. Actual-zeta signed Green covariance: the L501 failure record says
   harmonic replacement annihilates the prime-log main terms and leaves
   an uncontrolled centered covariance. No independently justified
   nonharmonic estimate was supplied in this audit, so this is not a
   ready alternative. L501 is historical contrast, not a theorem input.

## One bounded source-review test

Retrieve exact primary theorem hypotheses and relevant proof cases for
fixed-bandwidth approximation with simultaneous complex-domain and
global real-axis L1 control. Compare stronger weighted extremal results
and known impossibility bounds, reusing the parent reviews instead of
repeating their Poisson/duality searches. Record precise statements,
versions, applicability and whether they preserve the smooth Fourier
class. In particular distinguish unrestricted entire-function Runge
approximation from approximation within this fixed V_R.

Continue to a separately gated construction only if the review finds
an applicable quantitative theorem or an explicit, independently
testable uncovered norm tradeoff. If it yields only compact density,
no continuum control, or no global norm estimate, park this Runge lead;
do not spend repeated turns invoking qualitative approximation. An
obstruction must be stated with its actual hypotheses and cannot be
promoted to an H_a estimate without proof. No new mathematical claim
is approved by this nomination. Matching Mathlib coverage is unchecked.

The audited L505 stop remains intact. Actual-Xi signs, weighted zero
contributions, detector realization and all-height transfer remain
independent unresolved gaps. No justified creative central proof attempt
is ready until the proposed positivity-sensitive mechanism has essential
source coverage and a concrete discriminating norm test.

## Completed bounded source comparison, 2026-10-30

LITERATURE_REASON: The supplied REVIEW_REQUIRED target changes the earlier
full-space certificate question to genuine admissible approximation, with
essential unread quantitative complex-domain and global-norm coverage.
This review reuses the inspected parent Poisson/duality assessments;
it does not repeat or reapprove their stopped certificate mechanisms.

The main RH gap is still actual-Xi all-degree positivity, particularly
initial signs at unbounded height. The intermediate target here is the
unchanged genuine H_a sequence specified above. Such a sequence would
refute the proposed geometric Q bound and redirect the detector route;
it would not refute RH or realize an actual-Xi detector. The continuation
threshold is quantitative control of both the full rectangle and M,
not existence on a compact set. Independent arithmetic/sign gaps remain.

### Search and local comparison actually performed

Queries included `bandlimited functions approximation compact complex plane
norm control superoscillations quantitative Runge`, `Paley Wiener simultaneous
approximation weighted L1 norm compact complex plane fixed exponential type`,
`"bandlimited" "Runge" approximation norm`, `superoscillations minimum
energy interpolation Ferreira Kempf 2006 norm bandlimited arbitrary points`,
`Chremmos Fikioris superoscillations arbitrary polynomial shape 2015 Paley
Wiener envelope`, `"Paley-Wiener" "approximation" "complex" "norm" "Runge"`,
`"bandlimited" "weighted L1" approximation`, and `"quantitative Runge
approximation" Salo Ruland theorem 2019`. Search results are leads only.
No exact matching theorem was identified, which does not show nonexistence.

Read the L504 definitions and identities, the parent positive-class and
signed-gap assessments, and the clipped/two-height failure records. The
scoped working notes and latest L505 history contain no prior polynomial
bump-envelope cost test. The L503 paragraph entitled "Real-axis integrability
and the zero of K" was read narrowly to check overlap: an unweighted-to-M
conversion is already recorded there. No L503 theorem was applied or audited;
its first-mode stop is preserved. No cross-notebook theorem is used.

### Inspected primary sources and qualifications

1. I. Chremmos and G. Fikioris, *Superoscillations with arbitrary polynomial
   shape*, [arXiv:1504.04822v1](https://arxiv.org/pdf/1504.04822v1),
   Section II (2)--(4), printed pp. 4--5, and Section V p. 8.
   Read the Fourier-differentiation/support and smoothness/decay arguments,
   followed by dilation. For a real polynomial of degree N, the envelope
   spectrum is C^(N-1) with Nth derivative of bounded variation; the paper
   constructs p(t)e(t/D), D>=1, in PW_pi and approximates p on a real
   interval by flattening e, e(0)=1. Section V explicitly allows a compactly
   supported C-infinity bump spectrum for arbitrary polynomial degree.
   Dilation narrows the spectrum. These passages give no moving complex-
   rectangle sign guarantee or weighted-L1 cost estimate. The angular
   Fourier convention must be reconciled with exp(2pi i v z) in any later
   specialization. The retrieved v1 PDF footer says 19 April 2015 but its
   title page says 6 July 2021; this identifies the retrieved artifact,
   rather than claiming a newer arXiv version. This is the actionable source.

2. P. J. S. G. Ferreira and A. Kempf, *Superoscillations: Faster Than the
   Nyquist Rate*, IEEE Transactions on Signal Processing 54(10) (2006),
   3732--3740, [author PDF](https://sweet.ua.pt/pjf/PDF/Ferreira2006a.pdf),
   DOI 10.1109/TSP.2006.877642, Section III and Theorem 2, pp. 3736--3738.
   The stated interpolation data are finitely many arbitrary real amplitudes
   at distinct real times, in the finite-energy fixed-bandwidth class.
   Read the variational sinc-span construction, its Fourier-support
   argument and the matrix-energy discussion. This is an L2 minimization
   problem, not continuum complex positivity or M control. The text after
   Theorem 2 expressly distinguishes the worst-data upper bound from a
   lower bound valid for all data. PDF text extraction drops many formula
   symbols; screenshot calls exposed no inspectable image here, and a
   shell download failed DNS. Consequently no exact matrix formula,
   asymptotic constant or quantitative energy inequality is imported or
   marked verified. This limitation is nonessential to the chosen next
   calculation, which uses neither this theorem nor its formulae.

3. T. Karmakar and A. N. Jordan, *Beyond superoscillation: General theory
   of approximation with bandlimited functions*,
   [arXiv:2306.03963v1](https://arxiv.org/pdf/2306.03963v1),
   Section III A (24)--(27), printed p. 5. Read the finite spherical-Bessel
   expansion and variation of the squared real-interval error, giving
   a Gram-matrix linear system; its ill-conditioning qualification was
   also inspected. It controls neither the continuum complex rectangle
   nor the global M cost. Section IV's energy discussion was located but
   its Appendix D proof was not read; no energy inequality from it is
   used. The generic finite expansion does not assert a globally smooth
   compact Fourier spectrum, so membership in V_R must not be inferred.
   The failed v2 HTML URL was replaced by the accessible v1 PDF.

4. A. Ruland and M. Salo, *Quantitative Runge Approximation and Inverse
   Problems*, IMRN 2019(20), 6216--6234, DOI 10.1093/imrn/rnx301,
   [author manuscript](https://users.jyu.fi/~salomi/pub/Classical_Runge_L12.pdf),
   Theorems 2--3, pp. 1--2, Section 4 pp. 6--8. Read the singular-value
   cutoff, dual residual, logarithmic-continuation estimate and the
   enlarged-domain proof case. Hypotheses: nested bounded Lipschitz
   domains in R^n, n>=2, connected outer-minus-inner closure, an open
   boundary patch, symmetric uniformly elliptic bounded leading
   coefficients (Lipschitz for n>=3), bounded potential, and no zero
   Dirichlet eigenvalue. Theorem 2 gives relative interior L2 error with
   exponential boundary H^(1/2) cost; Theorem 3 gives polynomial cost
   when the target solution extends to an intermediate domain. Constants
   depend on the domains. These are solutions on a bounded larger domain,
   without fixed Fourier bandwidth or global real-axis weighted-L1
   control. Thus even the stronger extended-target case does not cover
   this problem. No PDE specialization is claimed.

Other surfaced weighted Paley--Wiener and interpolation leads were not
inspected at theorem level and supply no mathematical input. The parent
Brevig et al., Goberna--Volle and ABR comparisons remain reusable with their
recorded hypotheses; no broader conclusion is imported from them. Full
matching Mathlib coverage remains unchecked.

### Decision and one concrete continuation

Outcome EXPLORATION: this source search does not establish or refute the
H_a ratio, and is not mathematical progress beyond the checked sources.
Park qualitative Runge as a sufficient construction argument. Do not
repeat it without a new quantitative theorem or a different controlled
family. The two full-space stops remain intact.

The inspected bump-envelope method offers a sharply scoped alternative:
calculate the weighted flux cost of its slowly dilated family D>=B,
allowing arbitrary polynomial degree and coefficients. This changes the
test to the source's explicit bandwidth/dilation tradeoff, not sampled
positivity or a renamed full-space dual-certificate search. No need to
assume that flattening on a real interval preserves positivity on the
complex rectangle. The proposed uniform O_R(a M/B) threshold, including
the zero of K, is specified only as an unproved test in
[the separate nomination](2026-10-30-slow-dilation-weighted-gap-cost.md).
The extra D>=B restriction belongs solely to that family; it is not a
hypothesis on all H_a or a necessary approximation condition.

A proved family bound would stop that simple dilation construction even
if some members are admissible; its failure would require an explicit
witness and fresh comparison before a genuine H_a construction. Neither
outcome would settle the unrestricted ratio. This is a known-method
specialization suitable for a bounded calculation, not a justified central
creative attempt. The missing complex positivity/norm tradeoff is the
current blocker to such an attempt; no creative mechanism is invented
for scheduling. The new ready assessment requires separate next-turn
approval. No theorem application, new derivation, lemma or mathematical
script was completed in this literature-only turn.
