# Finite-covariance relaxation of the resonant-packet obstruction

TARGET: Assess the finite-K-only relaxation of L578: can a positive even single-wave remainder on [-1/2,1/2] match all of L473 (6) while the same uniform resonant packet attains clipped mean at least 1/288?
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact/terminology searches located general nonpolynomial finite-moment atomization and compact-cone separation, but no inspected theorem decides this coherent packet's finite-K/1/288 question; exact queries and local failure comparisons are below. No novelty claim follows.
SOURCE_EVIDENCE: Bayer--Teichmann, Proc. AMS 134 (2006), 3035--3040, author manuscript pp. 2--4, Theorem 1, Corollaries 1--2, Remark 2 and proof of Corollary 2; di Dio--Schmuedgen arXiv:1703.01497v2 pp. 2--4, Proposition 4, Lemma 8 and its proof; arXiv:1809.00584v1 Sections 3/10, pp. 5--6/28--29, Definition 9, Proposition 75, proof and subsequent compactness statement. Reuse Rahimi--Recht Section 3 only after positive-measure representation.
COMPARISON: General moment theorems cover continuous weighted functions, not just polynomial or ordinary Fourier moments, and supply atomization and separation with their exact hypotheses. They do not evaluate the residual or nonlinear clipped observable. L578 (5) remains justified only by full spectral completion; finite-K matching does not license importing it.
GAP: Decide the residual's supported positive even moment feasibility and the same clipped threshold over the fixed amplitude/selector family; no feasibility, separation coefficients, new parameter bound or clipped integral has been computed in this literature-only step.
REASON: Missing representation coverage has been supplied by primary theorems, so one bounded mathematical test is now justified. The unresolved finite-data/nonlinear application remains separate from the known spectral construction and the original full-spectrum stop.
LITERATURE_REASON: The incoming REVIEW_REQUIRED target changes full spectral equality to finite derivative-covariance constraints; this first review fills the essential supported-representation gap without rereading adequate spectral coverage.
SCOPE: Same packet U uniform [-1/4,1/4], independent uniform B, deterministic A,C,D in [0,4], fixed phi, and selector independent of (U,B,V,E) and constant along paths. Remainder D cos(Vx+E), V even on [-1/2,1/2], E independent uniform. Require only E JJ^T=K from L473 (6), not equality of the entire covariance spectral measure. No extra harmonic, fourth-tensor realization or actual-Hardy transfer is covered.
COVERED_TARGET: Test whether the finite-K-only L578 mixture can attain clipped mean at least 1/288, certifying all L473 (6) entries with a positive even remainder on [-1/2,1/2].

This was nominated for a separate literature-only turn; the completed
review below now supplies bounded research coverage. Essential local inputs are L473 (6) and audited
L578, including its phase expansion, bounds, selector repair and exact
full-spectrum hypothesis. L576/L577 are contrasts only. There is no
cross-notebook input. The prior ready audit assessment is unchanged.

The main gap is actual-Xi all-degree positivity and unbounded-height
initial signs. This intermediate could either supply a stationary
bounded bulk unavailable under full spectral completion, or eliminate
a larger class of proposed bulks. Its downstream use would be limited
to the stationary moment-feasibility route. All 126 fourth constraints,
derivative-preserving correction, actual-Hardy nonlinear-law comparison
and Xi transfer remain independent unresolved requirements.

The nomination required exact positive-measure moment/extension
terminology and stronger-obstruction searches, primary hypotheses and
essential proof cases, and comparison with the existing stationary-process
import stop. That comparison is completed below. A positive semidefinite six-by-six residual alone must
not be equated to an even supported spectral representation without a
theorem or proof. Conversely, L578's density inequality (5) must not
be treated as necessary after its full-spectrum premise is removed.
No statement here asserts either implication or computes its failure.

Continuation test: approve only a bounded feasibility/separation test
with coverage for the actual weighted moment constraints and the
unchanged 1/288 threshold. Import a deciding theorem if one exists.
Abandon a proposed matrix-only method if its representing-measure
condition cannot be justified, or park the target if it merely repeats
the recorded full-spectrum obstruction without new finite-data input.
No numerical preview can certify the uniform stop or a passing law.

This is not yet a justified creative attempt at the central Xi gap:
the missing fourth-law and actual-Hardy transfer remain the blocker.
Full matching Mathlib coverage for this changed target is unchecked;
unknown coverage is not evidence of absence.

## Completed primary-source comparison, 2026-10-31

### Known representation results and their scope

Christian Bayer and Josef Teichmann, *The proof of Tchakaloff's Theorem*,
Proc. Amer. Math. Soc. 134 (2006), 3035--3040,
[author manuscript, file tchakaloff120405.pdf](https://people.math.ethz.ch/~jteichma/tchakaloff120405.pdf),
Theorem 1, Corollaries 1--2 and Remark 2, manuscript pp. 2--4:
Corollary 2 assumes a positive measure concentrated on measurable A
and a measurable R^N-valued map with integrable first absolute moment.
Positive weights on at most N points of A represent its integrals.
Remark 2 includes a constant coordinate to preserve mass; handle zero
mass separately. Read Theorem 1's lower-dimensional/supporting-hyperplane
cases and Corollary 2's pushforward proof. This atomizes an existing
measure; it does not infer existence from matrix positivity. Continuous
weighted functions on the closed interval meet its integrability
hypothesis for a finite remainder. No local atoms are constructed.

Philipp J. di Dio and Konrad Schmuedgen, *The multidimensional truncated
Moment Problem: Atoms, Determinacy, and Core Variety*,
[arXiv:1703.01497v2, 28 March 2017](https://arxiv.org/pdf/1703.01497v2),
Section 2, pp. 2--4: X is locally compact Hausdorff and E is a
finite-dimensional space of continuous real functions on X. Proposition
4 is the Richter--Tchakaloff theorem. Lemma 8 identifies the dual of
the pointwise nonnegative cone E_+ with the **closure** of the cone of
representing functionals. Read its separating-functional proof, including
evaluation at every x. This requires positivity on every nonnegative
function in E, not merely selected squares. Proposition 9's strict
positivity result is not a license to assume an unproved strict margin.
These hypotheses cover the continuous weighted-frequency setting;
checking the residual functional, its linear relations, and the full
support restriction remains the later application. We do not identify
a six-coordinate covariance Gram test with E_+ positivity.

The same authors, *The multidimensional truncated Moment Problem: The
Moment Cone*, [arXiv:1809.00584v1, 3 September 2018](https://arxiv.org/pdf/1809.00584v1),
Section 3, Definition 9 and discussion, pp. 5--6, distinguish the
representing cone from its closure. Section 10, Proposition 75 and the
paragraph immediately following its proof, pp. 28--29, state closedness
and pointedness for continuous functions on compact X whose span contains
a strictly positive function. Read the proof and compactness paragraph.
Together with Lemma 8 above this supports a representation/separation
method including boundary cases. Its maximal-atom-mass formula is not a
formula for subtracting the entire packet distribution, and will not be
used as one. The bounded frequency interval and explicitly included
constant supply the relevant compactness/positive-function hypotheses.

The inspected Rahimi--Recht (2007) Section 3, Theorem 1, (2) and
real-phase formula remain adequate for turning an already positive
normalized even spectral measure into an independent-phase single wave.
Reuse the precise citation and qualifications in
`2026-10-31-resonant-stationary-packet-review.md`; do not repeat its proof
or infer a measure from that construction. Atoms are allowed by the new
target's measure hypothesis; absolute continuity is not required.

### Local comparison and search evidence

Read L473 (6)--(7) and the complete L578 proof and application audit,
including its 21-entry display, endpoint cases and selector repair.
Read `ATTEMPTS/2026-10-31-resonant-packet-mixture-stop.md` and the scoped
stationary/resonant source-assessment passages. L578 supplies the packet
spectral density (3), its phase formula (6), the upper bound (9), and
zero clipping for a single wave. These are reusable local results.
Its decisive (5) uses equality of full measures and is not an available
finite-data inequality. L576/L577 and the stationary-process import stop
remain contrasts, as already assessed; no sibling notebook was read.
No existing finite-K feasibility certificate was found in these scoped
records. That statement is a duplicate check, not certified novelty.

Queries actually used:

- `Tchakaloff theorem continuous functions compact space Richter moment cone positive measures finite atoms`
- `generalized moment problem compact support duality separation positive measures continuous functions derivatives covariance`
- `Bayer Teichmann proof Tchakaloff theorem pdf corollary 2 measurable mapping 2006`
- `di Dio Schmudgen moment cone closed constant function compact continuous functions proposition 2018 pdf`
- `"resonant" "clipped" "moment" covariance Laguerre stationary packet`
- `"derivative covariance" "truncated moment" compact spectral measure`
- `"truncated" "moment" "derivatives" "spectral" "covariance" positive measure`
- `"trigonometric" "moment problem" "derivatives" compact support positive measure`
- `"stationary" "Laguerre" "positive part" random trigonometric`
- `"resonant" "two harmonic" "covariance" random phase positivity`

Search hits for polynomial-only cubature, standard circle trigonometric
moments, entropy reconstruction and coupled-oscillator variance do not
establish the required derivative-weighted/clipped assertion. Curto--Fialkow
duality, Putinar's cubature paper and Schmuedgen's book were discovery
leads, not inspected theorem inputs. The three primary passages above
provide the essential coverage without relying on those unread leads.
No source-access blocker remains for this bounded target. Searches found
no inspected stronger theorem deciding the stated threshold; that is not
evidence of originality or of feasibility.

### Approved bounded application and decisive test

Work only on the COVERED_TARGET with all SCOPE restrictions. Reuse the
L578 phase bound; first seek a finite-moment necessary inequality strong
enough to settle the unchanged threshold. A negative proof may use a
subset of K entries if its necessity for every supported remainder is
proved; no unsupported density domination is allowed. A constructive
alternative must certify every one of the 21 entries, including the
cross-height entries and exact odd zeros, with a positive even remainder.
Do not stop at a successful residual Gram matrix or a sampled curve.

For any moment-cone application retain the exact real integrands from
L473 (6), the mixture/amplitude weights from L578 (3), total mass and
all linear identities. To enforce evenness, use symmetric atomic pairs
or verify reflection symmetrization against every integrand. Passing to
an independent basis must also check consistency of discarded relations.
The mass-zero case, p=0, p=1 and zero amplitudes need explicit handling;
never divide by a vanishing remainder mass. A finite atomic search
requires certified equalities/positivity, not approximate residuals.
A dual certificate requires nonnegativity on the whole closed interval
and the correct residual sign, not a grid check. These are future
application obligations, not certificates produced by this review.

Continue only upon a certified feasible law attaining >=1/288 or a
rigorous uniform upper bound that resolves the comparison. A bound
strictly below 1/288 stops the entire stated family; equality needs its
own endpoint analysis. An inconclusive bound or numerical suggestion is
EXPLORATION and must preserve the remaining inequalities. The bounded
attempt may report failure without creating a lemma. No enlarged family
or repeated full-spectrum parameter search is approved.

This resolves source coverage, not the finite-K question or any RH gap.
Even a passing bulk leaves all 126 fourth constraints, a derivative-
preserving correction, actual-Hardy comparison and Xi transfer open.
Those missing central mechanisms prevent justified creative routing;
the present task remains a covariance specialization with a nonlinear
threshold check. Full matching Mathlib coverage remains unchecked.
