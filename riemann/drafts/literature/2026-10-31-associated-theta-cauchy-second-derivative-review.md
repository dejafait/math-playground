# Real-axis associated-theta Cauchy derivative: completed source review

TARGET: Assess primary coverage for the second-derivative sign of C_A(iy), where C_A(z)=(2pi i)^(-1) integral_R A(t)/(t-z) dt for L596's exact real-axis A, for every y>0, and compare with the recorded complete-monotonicity stops.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed exact Cauchy/second-derivative, even-decreasing/Poisson-convexity and associated-theta searches listed below; no inspected theorem states the exact requested sign. Csordas's known associated-kernel admissibility provides a concrete shape input for a bounded calculus replay. No novelty inference follows.
SOURCE_EVIDENCE: Csordas arXiv:1309.0055v2 (2014), Definition 1.2, Theorem 3.5 with both proof cases, (4.2), Theorems 4.1/4.5; Norvidas arXiv:2009.04449v1 (2020), Theorem 2 and both proof directions, Corollary 3, (1.3), (2.2)-(2.16); Norvidas arXiv:2009.04492v1, Theorems 1/3, (1.6)-(1.7), (2.1)-(2.7) and both proof directions. Direct primary links and qualifications below; prior 2015 distributional comparison reused.
COMPARISON: The exact associated kernel has a cited decreasing-shape input after normalization. The finite Cauchy sign is not itself asserted by these sources. For real-even normalized data, Norvidas's harmonic Theorem 2 uses the upper Poisson hierarchy alone; treating lower-half-plane reconstruction as an independent missing condition overstates the gap in this case. A second derivative still cannot replace the full hierarchy.
GAP: Replay the second-y-derivative identity from the defining integral, its boundary terms and sign using admissibility; the derivative-sign chain in Norvidas's Corollary 3 must be independently checked before import. No exact derivative formula, finite sign, or full hierarchy is proved in this literature turn.
REASON: Coverage now supports one routine specialization/audit using a named shape theorem, with no Fourier-positivity premise. This is a finite necessary-sign test, not a new central mechanism or an RH resolution.
LITERATURE_REASON: Changed operation and missing essential coverage: real-axis A is the input to an auxiliary Cauchy transform, with a specified second-derivative target, rather than an unknown boundary distribution of A. Separate source approval is required before calculations.
SCOPE: Completed review of the saved assessment target only. The proposed mathematical continuation is specified separately in 2026-10-31-associated-theta-cauchy-second-derivative-audit.md and receives the supervisor's separate next-turn approval. No mathematics was invoked here.

## Exact target and local applicability

Use exactly A(t)=integral_R s^2 k(s+t)k(s-t) ds from L596,
on real t, with k from L019/L239. This is not the auxiliary theta
function also denoted A in those inputs. The relevant Fourier
normalization is L233: Ahat(2x)=Xi'(x)^2-Xi(x)Xi''(x).

The proposed C_A is the usual upper-half-plane Cauchy transform
with the explicitly written normalization. It is not A evaluated at
z=iy. All y>0 are proposed, without an upper strip cutoff.
The target is only its second y-derivative sign. L233's complete proof
supplies continuity, evenness and all weighted absolute integrability;
L019 supplies strict positivity of k. L239 supplies the even continuation
used to identify the same kernel on the whole line. These inputs permit
comparison with ordinary integrable-data Cauchy transforms without any
boundary distribution or assumption about A at Im z=pi/4. Reality,
normalizing factors and differentiated integrals remain part of the
mathematical replay; no derivative formula was derived here.

## Primary shape input and precise normalization

George Csordas, *Fourier transforms of positive definite kernels and the
Riemann xi-Function*, arXiv:1309.0055v2, 21 February 2014:
[primary text](https://arxiv.org/html/1309.0055v2),
[PDF](https://arxiv.org/pdf/1309.0055v2).
Definition 1.2 (printed p.2) includes smoothness, strict positivity,
evenness, negative first derivative on the positive axis, and decay of
every derivative faster than a specified super-Gaussian. Theorem 3.5
(pp.6-7), (3.7)-(3.9), assumes admissibility and strict logarithmic
concavity of the original kernel and concludes admissibility of every
associated kernel. Both intervals 0<s<t and s>t in its monotonicity proof
were inspected; the latter uses the decreasing logarithmic derivative
and evenness. This is a theorem about real-axis shape, not its spectrum.

Theorem 4.5 (p.11), (4.6), gives that conclusion for the exact Jacobi
theta kernel Phi of (4.2), using Theorem 4.1 and Theorem 4.2/Remark 4.3(a).
The source's (4.2) and L019's series agree under the already recorded
normalization k(u)=4 Phi(u/2), extended evenly. This positive factor and
positive rescaling must be carried through the associated integral in
the mathematical replay; no source Xi-transform constant is substituted.
There is no reason to reprove theta logarithmic concavity. Reuse also
the prior inspected assessment 2026-09-27-first-associated-theta-lattice.md.

## Primary Cauchy criteria, scope correction, and formula caution

S. Norvidas, *A note on harmonic continuation of characteristic function*,
[arXiv:2009.04449v1](https://arxiv.org/html/2009.04449v1),
[PDF](https://arxiv.org/pdf/2009.04449v1), 9 September 2020, Theorem 2
(p.2), states: a bounded continuous real-even f with f(0)=1 is a
characteristic function iff its Poisson extension u_f(0,y) is completely
monotonic on [0,infinity). Read (1.2)-(1.3), (2.2)-(2.10) and both proof
directions (pp.4-5). Necessity uses the positive-measure representation;
sufficiency uses Bernstein-Widder, evenness to identify the analytic
extension on the imaginary axis, analytic uniqueness, and boundary
limits of positive-definite functions. Thus evenness removes the need
to establish two unrelated half-plane hierarchies. It does not produce
the upper hierarchy. The source's endpoint definition and bounded
continuous extension at y=0 should not be silently omitted if this full
criterion is eventually applied; our finite test asks only y>0.

Corollary 3 (p.3), (1.5)-(1.7), assumes in addition that every derivative
is bounded and continuous. Its proof (pp.6-7), especially the integration
by parts immediately before (2.15), is sign-sensitive: (1.7) has factor
(-1)^n, and (2.15) has factor (-1)^(n+1). Both extracted PDF and HTML
show these signs. Do not adopt an affirmative or negative finite sign
from these displays. Independently replay the second-derivative case
from (1.3) and the notebook's defining C_A; no corrected identity or
counterexample to the source is asserted in this literature-only step.
This verification of a potentially suspect specialization is the reason
to permit a short reproof instead of quoting a formula without checking.

The companion *A note on analytic continuation of characteristic
functions*, [arXiv:2009.04492v1](https://arxiv.org/html/2009.04492v1),
Theorem 1 (p.2), repeats the real-even criterion, citing the author's
2010 paper, *On harmonic continuation of characteristic functions*,
Lithuanian Math. J. 50(4), 418-425, Theorem 2,
[DOI](https://doi.org/10.1007/s10986-010-9096-y).
The 2010 original is an identified reference, not newly read here.
The companion's (1.6)-(1.7), Theorem 3 and proof (pp.3-5) treat an
ordinary Cauchy transform when integral |f(t)|/(1+|t|) dt is finite.
Its transform k_f uses i/pi times integral f(t)/(z-t) dt, twice our C_f.
This normalization follows directly from the two definitions, not from
a sign convention inferred from a theorem title. L233 supplies the
required absolute-integrability hypothesis. Theorem 3 for complex data
needs both half-plane sign hierarchies; it must not obscure the stronger
real-even specialization above. Neither version proves signs from
pointwise positivity of f. The previously inspected 2015 distributional
theorem remains correct within its more general scope.

## Duplicate and failure comparison

Read the full proofs of L232, L247, L233 and L253. L232 rules out a
positive Laplace representation of x^(-5/4)K(log(x)/2), a different
function and variable. L247's completely monotone squared-axis
logarithmic derivative with nonreal zeros does not concern the Cauchy
transform of A. L233 identifies the exact Fourier obstruction and shows
that positivity of k alone does not supply it. L253's signed remainder
cannot be assigned its own positive spectrum. The originally nominated
"L253 first-sign masking" description was imprecise: the explicit
finite-Laguerre masking stop is L257, as recorded in the narrowly read
2026-09-23-finite-laguerre-multiplicity-masking-test.md. None is a proof
or refutation of this Cauchy second derivative. The finite-part stop is
preserved, and its boundary operation is not reopened.

## Search record and bounded decision

Queries actually issued included:

- `Cauchy transform even decreasing function completely monotone second derivative Norvidas`
- `"associated kernel" "Cauchy" theta`
- `"Norvidas" "completely monotonic" "Cauchy"`
- `"Cauchy transform" "unimodal" "convex"`
- `"Poisson integral" "decreasing" "convex" even`
- `"Norvidas" "Cauchy transform" "characteristic functions"`
- `"Cauchy transform" "second derivative" "decreasing"`
- `"Poisson transform" "convex" "even"`
- `"unimodal" "arctan" "mixture" density`
- `Norvidas "On harmonic continuation of characteristic functions" pdf`

No exact finite-sign theorem was identified. Unimodal-Cauchy geometric
results and uniform-mixture references were search leads only, not
inspected or imported theorems. The named Csordas shape input offers an
independently testable integration-by-parts discriminator, without any
assumption on Ahat. Permit one mathematical replay using it. Continue
only if all factors, derivative interchanges and endpoint terms can be
checked and the sign isolated from this shape information; otherwise
record the exact obstruction and park this test. If it works for the
whole admissible class, record it as a known-shape specialization and
do not promote it to a theta-specific full-hierarchy mechanism.

The main gap is all-degree actual-Xi signs at unbounded heights. The
possible downstream use is one controlled necessary member of the first
associated-kernel hierarchy and an honest test of whether this operation
adds theta-specific information. Full first-level Fourier positivity and
higher associated kernels/mixed forms remain unproved. A generic finite
sign supplies no complete solution. Mathlib matching coverage was not
checked; no absence claim or new theorem is recorded.
