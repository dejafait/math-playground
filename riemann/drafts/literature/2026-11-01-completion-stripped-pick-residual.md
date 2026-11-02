# Completion-stripped Pick residual — source assessment

TARGET: Determine whether the completion-stripped residual E/G avoids C645a's forced failure at logarithmic grid size, using L645's unchanged disk and nodes.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read L018/L258/L645/C645a and the two specific cutoff/fixed-reserve stops; reused the ready finite-Pick assessment. Searched normalized logarithmic-derivative residuals, zeta/Pick interpolation and weighted Blaschke/Schwarz bounds. Inspected the primary statements and needed cases below; no inspected theorem decides this exact normalized-grid comparison, and no novelty is inferred.
SOURCE_EVIDENCE: NIST DLMF 1.2.8 (2026-09-15), 5.2(i)/5.2.2 and 5.11.2 with sector and complex remainder paragraph 5.11(ii); Zakeri, author Notes and Comments Section 8.3, complete finite-Blaschke argument after Example 8.33; Gonek (1984), Section 2 (20), printed p.127, including sigma>1 and the following Cauchy proof paragraph. Reuse Bolotnikov (2010) Theorem 1.1 and the frozen Borel–Caratheodory coverage in the existing L645 assessment.
COMPARISON: L258 prices an entire paired Taylor witness by its circle maximum and deflated center coefficient; it neither uses this finite positive-real interpolant nor strips its completion. The ordinary finite-Blaschke theorem covers an analytic bounded quotient once its hypotheses are checked; it supplies no zeta-derivative lower bound or residual estimate. C645a's completed maximum and C644a's fixed reserve remain distinct stopped mechanisms.
GAP: A separate mathematical step must justify the quotient and its sample/zero values, bound its full disk norm uniformly over the admissible finite interpolants, and compare the resulting derivative-normalized bound with the unchanged contraction at floor(log gamma). No improved cutoff, avoided obstruction, derivative lower bound or signs are established by this review.
REASON: The missing analytic-factor/digamma and right-of-one derivative cases are now covered, and exact local overlap has been checked. A bounded standard specialization is justified after separate approval of this changed assessment; sources do not resolve its outcome, and the normalization is not a creative sign mechanism.
SCOPE: Fixed delta in (0,1/2), stipulated simple rho and L645's unchanged disk, grid and finite positive-real interpolant. No actual signs, off-line zero existence, derivative lower bound, multiple-zero extension, uniform small-delta limit or effective onset is assumed.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED assessment lacked essential coverage for the changed E/G residual; existing growth coverage alone did not assess completion drift or the full residual disk. This turn fills that source gap rather than repeating the accepted C645a audit.

## Completed review — 1 November 2026

This turn imports standard source inputs and compares their scope. It
does not derive a residual identity, norm bound, new lemma or cutoff.
The main gap is actual-Xi signs at unbounded heights and all-degree
mixed positivity. The intermediate target remains exactly the TARGET
above. Its plausible use is to decide whether removing the completion
factor warrants any later signed-estimate work.

### Primary inputs and their applicability limits

NIST DLMF, version **1.2.8**, release **2026-09-15**, accessed
1 November 2026:

- [5.2(i), 5.2.2](https://dlmf.nist.gov/5.2#i): gamma is meromorphic,
  has no zeros and has poles at the nonpositive integers;
  psi=Gamma'/Gamma away from those poles. For the proposed use,
  separately check every polynomial and gamma factor of C645a's G
  on a neighborhood of L645's high disk. Do not claim G is entire
  and nonzero globally.
- [5.11.2](https://dlmf.nist.gov/5.11.E2):
  psi(z)~log z-1/(2z)-sum_{k>=1} B_{2k}/(2k z^{2k}), as
  |z| tends to infinity in |arg z|<=pi-epsilon, fixed epsilon>0.
  [5.11(ii)](https://dlmf.nist.gov/5.11#ii), first paragraph, bounds
  the complex remainder after k=n-1 by the first omitted term in
  magnitude times sec^{2n+1}(arg(z)/2).
  Read the sector condition and complete relevant remainder paragraph.
  Applying these to s/2 requires a uniform sector and modulus check
  over the disk, with a different symbol from the zero displacement.
  The real-positive remainder sign is not a complex-plane sign bound.

The previously read vertical gamma modulus formula 5.11.9 remains
covered by the prior growth assessment; no reproof is proposed.
Use the digamma expansion directly, rather than differentiating an
uncontrolled asymptotic remainder. These sources do not estimate P.

S. Zakeri, *A Course in Complex Analysis*,
[author Notes and Comments, Section 8.3](https://zakerimath.com/CAbook/COM.html),
unversioned page, accessed 1 November 2026, paragraph following
Example 8.33: read its complete finite-Blaschke division argument.
For a bounded disk-holomorphic function, division by a finite product
of its zeros, with multiplicity, extends holomorphically and retains
the bound. The proof uses removable zeros, boundary modulus one of
the finite product and the maximum principle. Extra zeros do not
invalidate division by a selected finite subset. Apply the ordinary
theorem only after proving that E/G is holomorphic and bounded on
the prescribed disk. A separate weighted Bergman zero-set theorem is
unnecessary for this proposed finite-disk use. The source does not
give a bound on E/G, its dependence on P, or its value at rho.

S. M. Gonek, *Mean values of the Riemann zeta-function and its
derivatives*, Invent. Math. **75** (1984), 123–141,
[author-hosted published PDF](https://sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf),
Section 2, equation **(20)**, printed **p.127** (PDF page 5).
Reuse the already assessed unconditional critical-strip estimate for
nu=0,1 and fixed epsilon>0. Read the additional sigma>1 case needed
by the disk: |zeta^(nu)(sigma+it)| << |t|^epsilon for |t|>=1/2.
The critical-strip case includes sigma=1. Read the full following
paragraph: obtain derivative estimates from nu=0 on a small complex
disk by Cauchy's estimate, citing Titchmarsh pp.81–82. Any uniform
estimate across the bounded real-part range must retain the epsilon
slack and explain the junction at one; fixed-point estimates alone
do not justify a circle supremum. Equation (20), unlike the nearby
log-derivative formula (18), does not require selected heights or RH.
It is an upper estimate, not a lower bound at a simple zero.
No successful visual screenshot was supplied by the tool; the primary
PDF text and complete relevant proof paragraph were available. The
older critical-strip coverage is reused, not newly established here.

For anchor estimates, reuse the previously inspected DLMF 25.2.6 and
27.4.3/5 absolute series only on Re(s)=2. No reciprocal series in the
critical strip is licensed. No new zero-free-region result is proposed.

### Reused finite-interpolation coverage

The ready
[L645 assessment](2026-11-01-vertical-pick-quantitative-pole-detection.md)
already inspected V. Bolotnikov, *A multi-point degenerate interpolation
problem for generalized Schur functions*, Operators and Matrices **4**
(2010), 151–191, definitions (1.1)–(1.7), Theorem 1.1, pp.151–153
([publisher PDF](https://files.ele-math.com/articles/oam-04-08.pdf)).
It also inspected `Complex.borelCaratheodory`, lines 37–110, at
Mathlib commit `0d3fb85496130669f472d62be6f25999ca085c59`
([frozen source](https://raw.githubusercontent.com/leanprover-community/mathlib4/0d3fb85496130669f472d62be6f25999ca085c59/Mathlib/Analysis/Complex/BorelCaratheodory.lean)).
This scope is unchanged: finite distinct interior nodes, PSD including
singularity, modulus-one data, and positive-real interpolation after
the checked Cayley transform. Borel–Caratheodory requires a positive
real-part upper-bound constant, and a smaller disk inside its domain.
Retain L645's finite P and anchor, including purely imaginary constant
cases. No source licenses treating P minus the completion logarithmic
derivative as a positive-real function. Any control of that difference
must be justified, not obtained by reusing positivity after subtraction.

These standard results are imported. Only the normalization, analytic
domain and quantitative comparison need proof; redoing finite Pick,
Blaschke division, Stirling or convexity would not help this target.
Supporting Borel–Caratheodory Mathlib coverage is as cited. Full matching
coverage for this normalized test and for the new gamma/digamma inputs
has not been checked; no absence is claimed. No Lean replay occurred.

### Exact overlap and recorded failures

Read L258 completely. Its variable is an entire real F at real a,
with H(y)=F(a+iy)F(a-iy), central multiplicity m and positive deflated
coefficient c. Its finite negative coefficient is priced by B/c and
the geometric tail q=b^2/R^2. It assumes a specified nonreal zero,
not finite PSD data. It has no positive-real interpolant, no residual
xi'-P xi and no gamma division. Thus it does not directly give this
normalized Pick comparison. Both mechanisms still price witnesses by
analytic growth; merely introducing another unspecified norm would
repeat the unresolved estimate rather than establish a useful difference.

Audited C645a and its
[stop](../../ATTEMPTS/2026-11-01-l645-logarithmic-growth-threshold-stop.md)
concern exactly L645's completed M_rho/H_rho and sufficient cutoff.
Do not apply its lower bound to a different residual without proof.
Conversely, dividing by G is not evidence that its obstruction has
been removed. The
[C644a stop](../../ATTEMPTS/2026-11-01-vertical-pick-uniform-fixed-reserve-stop.md)
refutes an eventual fixed reserve; it does not settle an actual sign,
a vanishing margin or the normalized analytic test. Neither stop is
a global ban or an input granting positivity.

### Search record and unread leads

Queries: `"Nevanlinna Pick" "zeta" "logarithmic derivative"`;
`weighted Blaschke product zero bound analytic function zero free factor
outer function`; `DLMF digamma asymptotic expansion log z 5.11.2`;
`"zeta" "Pick" "normalized" "logarithmic"`;
`"weighted" "Blaschke" "zero-free" "majorant" analytic`;
`"positive real" "interpolation" "logarithmic derivative" zeta`;
`"Riemann xi" "Nevanlinna" "Pick"`;
`"zeta" "positive real interpolation"`;
`"logarithmic derivative" "normalized" "Pick matrix"`;
`"weighted Schwarz lemma" holomorphic nonvanishing weight Blaschke`.
The sources actually used are specified above. Searches returned
qualitative xi/Nevanlinna criteria, general factorization and unrelated
weighted-space results; none of the inspected statements provides this
exact residual estimate. This bounded search does not establish novelty.
Suzuki's screw-function paper, a self-weighted Hamburger-rigidity
preprint and general weighted-factorization surveys were search leads,
not newly inspected or imported here. The existing qualitative Pick
overlap is reused through the ready assessment; no cross-notebook
theorem was read. Two initial DLMF 5.2 timeouts were resolved through
its equation URL; essential source access is not blocked.

### Licensed later test and decision threshold

After separate approval of this changed assessment, one mathematical
attempt may specialize these inputs on the unchanged L645 disk/nodes.
It must check G's analytic nonvanishing domain, the quotient's exact
sample values and its nonzero value at the stipulated simple zero.
Keep P dependent on the chosen n and the temporary PSD assumption.
Produce an explicit full-circle bound valid for every such admissible
P, or state precisely which additional estimate is needed. Compare its
derivative-normalized size against L645's unchanged contraction at
N=floor(log gamma), including strict inequality and fixed-delta constants.
Do not assert a derivative lower bound or interchange a maximum and
division without checking the relevant factors.

Continue only if that test supplies a discriminating exponent/constant
comparison or identifies a quantitatively different, usable missing
estimate. A finite renamed norm alone is no advance. Stop this
normalization attempt if it retains a forced insufficient exponent or
only repeats L258's growth price; an inconclusive upper envelope is
not a theorem of forced failure. Actual positivity, least witness size,
multiple specified zeros, small-delta uniformity and RH remain independent.
Essential continuation inputs: L018, L645 and C645a; L258 and C644a
are comparisons, not premises. No new signed mechanism with a bounded
test has emerged, so creative routing is not justified by this review.

## Original nomination (preserved; superseded source status)

The following text records the proposal before this review. Its earlier
REVIEW_REQUIRED conclusion is superseded by the SPECIALIZE assessment
above; it is not a second current action.

## Proposed bounded test, not an approved calculation

Use the symbols E of L645 and G of C645a to nominate E/G as an
alternative analytic residual. First assess its analytic domain, the
available estimates for the completion's logarithmic derivative, finite
positive-real interpolation constraints, and relevant weighted analytic
zero bounds. Read the primary statements and essential proof cases needed
for any proposed bound. Reuse unchanged growth coverage where applicable.

Compare the exact L258 normalization and the recorded L645/C644a stops;
do not infer novelty or adequacy from the narrow search above. Search
standard terminology for normalized logarithmic-derivative residuals,
finite Pick pole detection and weighted Blaschke bounds. The present
audit did not perform that search or inspect L258's proof anew.

The eventual mathematical test would ask whether the new sufficient
condition at N=floor(log gamma) is still forced to fail by the same
standard estimates, or instead isolates a precise additional bound on
the normalized residual/first nonzero derivative. Merely replacing one
undefined growth quantity by another is not an advance. Stop this
nomination if it reproduces L258 without a useful difference or retains
the same unavoidable growth obstruction. No such outcome is asserted.

Potential use: decide whether C645a's deterministic completion cost can be
removed before pursuing an actual signed estimate. Actual matrix signs,
derivative control and all-degree positivity remain independent gaps.
Essential proposed inputs are L018, L645 and C645a; L258 is initially an
overlap check, not an assumed premise. No cross-notebook input is proposed.
Matching Mathlib coverage is unchecked, with no absence claim.

This is a fresh uncovered continuation, not approval of new mathematics.
The next invocation must perform literature review only. A genuinely new
signed mechanism, if one emerges, needs its own precise bounded target
and creative routing justification; this normalization proposal alone
does not justify labeling a routine specialization creative.
