# Sign-adapted chirped leakage: completed source comparison

TARGET: Assess source coverage for C_U(T)=integral_T^(2T) Re(exp(2i theta(t))V_T(t)) sgn(U_T(t)) dt=o(T(log T)^3) along an unbounded sequence, for the exact U_T,V_T of L481 and sgn(0)=0.
CHECKED: 2026-10-29
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded exact/stronger-result searches for sign-weighted Dirichlet-polynomial oscillatory integrals, bounded-variation amplitudes and exponential-polynomial zero counts; inspected the primary statements/proof cases below. Reused the Hardy-L1 comparison, L481's finite mean-square interface and the actual stationary-involution failure; no matching leakage theorem or duplicate was located, and no novelty is inferred.
SOURCE_EVIDENCE: Tao, 247B Lecture Notes 8 (2007), Section 2, Lemmas 2.4--2.6 and (4)--(7), pp. 4--6; Nazarov, Algebra i Analiz 5(4) (1993), Lemma 4.2 and proof, p. 58; Friedland--Yomdin, Studia Math. 218(1) (2013), Theorem 1.1, Lemma 2.4 and the sublevel-component proof, pp. 27--32. Direct primary URLs and qualifications are below; no exact sign-adapted finite-height theorem is imported.
COMPARISON: Scalar nonstationary estimates retain amplitude derivative/variation costs, and the inspected exponential-polynomial theorem retains frequency/count/radius costs. Neither supplies cancellation at this multiplier's sign boundaries or its V_T-weighted smoothing error. The existing Haar, finite-polynomial and stationary-involution limitations remain; this is a source-scope mismatch, not a mathematical obstruction theorem for C_U.
GAP: No inspected source or specified covered extension establishes C_U=o(T(log T)^3), its failure, or a complexity bound sufficient for that scale. The independent full-scale integral |U_T| lower bound on a common sequence also remains unproved.
REASON: The bounded review is complete but does not pass the nomination's continuation test. Park direct sign-adapted leakage evaluation; EXPLORE records the completed search, not approval to assume a missing multiplier estimate. Choose an independently testable target with existing source coverage rather than repeat this source search or derive uncovered mathematics.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED coverage lacked an essential actual-height nonlinear-multiplier input; the present review checks that changed hypothesis rather than repeats ready scalar-moment literature for scheduling balance.
SCOPE: Actual L481 U_T,V_T,theta and M=floor(sqrt(T/(2pi))); real T along an unbounded sequence; sign is zero at every zero of U_T. No RH, simplicity, phase independence, Haar replacement, unproved sign-variation bound, removed exceptional set or conclusion about the nonchirped L1 norm.

The main gap is actual-Xi all-degree mixed positivity. The intermediate
target isolates chirped interference with a bounded dual adapted to
the ratio residual. It could help a separate nonchirped absolute-norm
bound support a complete-residual defect test. That other bound, the
defect threshold, negative mass, initial signs and higher signs remain
open. This nomination supplies neither a new estimate nor a solution.

This changes the mechanism: there is no short resonator, saturation
or polynomial approximation. It does not assume theta is random or
ratio and product phases independent. Zeros of U_T cannot be discarded
and the variation of its sign cannot be bounded without proof. Any
smoothing needs its complete weighted transition error, not merely
a small transition set in Lebesgue measure.

Reuse the primary Hardy-space comparison rather than repeating its
searches. Seek exact theorems or proof mechanisms for finite-height
chirped integrals with the sign of a growing real Dirichlet polynomial,
including overlapping frequencies and multiplier complexity. Retrieve
primary hypotheses and essential proof cases before approval. Check
the specific stationary-involution failure and ratio-frequency grouping
records for duplicates; do not reopen that exhausted involution or
infer novelty from failed searches. Model memory is only a lead.

Pass requires source coverage for one bounded attack on the exact
little-o leakage or an informative obstruction at that scale. A theorem
for U_T alone, a global moment, a fixed smooth multiplier without
complexity control or torus phase averaging does not pass. If these
are all that is available, park this dependent mechanism instead of
approving an uncovered calculation.

Essential inputs are L477's reduction and L481's exact U_T,V_T,theta.
L481's interpolation obstruction and L482's stop are contrasts, not
premises. No cross-notebook input. Mathlib matching is unchecked.
Missing source-to-mechanism coverage blocks a justified creative
invocation; this source-review nomination is not itself creative work
or authorization to derive and approve new mathematics in one turn.

## Completed comparison, 29 October 2026

The nomination above records the original scope and test. This section
discharges its source-review request without approving a mathematical
estimate. The main gap is still actual-Xi all-degree positivity. The
intermediate target was the exact sign-adapted leakage, with potential
use alongside an independent nonchirped L1 lower bound in a residual
defect test. Neither component, the defect threshold, negative-mass
saving nor the missing signs is established by this review.

### Primary statements and essential proof cases

**Tao, _Lecture Notes 8 for 247B_, 2007, Section 2, printed pp. 4--6.**
[Author-hosted primary notes](https://www.math.ucla.edu/~tao/247b.1.07w/notes8.pdf#page=4).
Lemma 2.4 bounds the integral of exp(i lambda phi) over an interval
by an absolute multiple of 1/(c lambda), assuming a smooth real phase,
monotone phi' and |phi'|>=c>0. Its proof uses (4), retaining both
boundary terms and the variation of 1/phi'. Read that complete proof,
the higher-derivative split in Lemma 2.5, and the smooth-amplitude
identity (5). In (5)--(6) the amplitude derivative is retained and the
constant depends on the amplitude. Lemma 2.6 assumes a compactly
supported smooth amplitude and has amplitude/phase-dependent constants.
It is not a uniform theorem for arbitrary bounded multipliers. No
extension of these statements to the target sign is proved here.

**Nazarov, _Local estimates for exponential polynomials and their
applications to inequalities of the uncertainty principle type_,
Algebra i Analiz 5(4) (1993), 3--66, Lemma 4.2, printed p. 58.**
[Primary Russian article, PDF p. 56](https://m.mathnet.ru/php/getFT.phtml?jrnid=aa&option_lang=eng&paperid=397&what=fullt#page=56).
For a nonzero exponential polynomial with n terms and complex exponents
lambda_k, put Lambda=max |lambda_k|. Any disk of radius r has at most
4(n-1)+7 Lambda r zeros, retaining multiplicity. The proof compares
maxima on concentric disks using Turan's interval inequality and a
Blaschke-factor bound for every enclosed zero, then chooses the larger
radius to be 6r. Read the statement and this proof on the primary page;
the English restatement below confirms its notation and constants.
This counts zeros; it supplies no signed correlation of another function
evaluated at those zeros. No count for U_T, or application at a selected
radius, is derived in this literature turn.

**Friedland--Yomdin, _An observation on the Turan--Nazarov inequality_,
Studia Math. 218(1) (2013), 27--39.**
[Publisher primary article](https://www.impan.pl/shop/publication/transaction/download/product/89801).
Theorem 1.1, p. 27, controls the supremum of an exponential polynomial
on an interval from its supremum on a positive-measure subset, with
the number of terms in the exponent of the measure ratio. Lemma 2.4,
p. 31, restates Nazarov's zero bound. Read also the component-count
argument in the proof of Theorem 1.3, pp. 29--30, and the comparison
with level-set counts, pp. 31--32. These are sup-norm/sublevel-set
results, not estimates for the target weighted signed integral. The
paper's sin(lambda t) example on pp. 29--30 explicitly retains frequency
dependence when discrete zero sets enter. It provides no uniform
transition-error bound in the growing-degree regime needed here.

### Exact applicability comparison and stop

L481 defines U_T by the ordered ratio sum with coefficients
log(n/m)^2/sqrt(nm), V_T by the corresponding product sum, and the
actual gamma phase theta. L477's unweighted nonstationary endpoint
calculation is already available; its bound does not contain the
new sign multiplier. Finite mean-square estimates in L481 apply to
finite polynomial coefficients, whereas the sign in this target has
not been given an admissible finite expansion with a controlled error.
The Hardy-L1 comparison's distinction between actual intervals and
Haar averages is reused without another discovery search.

A sign-interval decomposition would have to retain every new boundary
and its total cost, or establish cancellation between those costs.
A smooth substitute would have to retain its derivative constants
and the error weighted by the actual |V_T| on the transition set.
Boundedness of the multiplier, a bound on the number of zeros, or a
small unweighted transition measure does not itself supply either
missing estimate in the inspected theorems. No sign-change bound,
zero simplicity or weighted exceptional-set estimate is asserted here.

Thus the review has not supported the required o(T(log T)^3) test
or a mathematical obstruction at that scale. Park this direct route.
The failure is of this source-to-mechanism match, not a proof that
the desired leakage estimate is false or that no future method works.
Reopening requires a new quantitative multiplier/weighted-transition
input with an explicit finite-height error, or a different bounded dual
with independently controlled complexity. Repeating scalar stationary
phase or the old involution is not that input.

### Search, provenance and continuation

Queries included `"Dirichlet polynomial" "sign" "oscillatory"`,
`"oscillatory" "sign" "Dirichlet polynomials"`,
`"Dirichlet polynomials" "bounded variation" integral`,
`oscillatory integral sign exponential polynomial number zeros uniform
bounds`, `"Nazarov" "exponential polynomials" "zeros" disk lemma`,
and `van der Corput lemma bounded variation amplitude Tao lecture notes`.
The exact/stronger-result searches found the primary statements above,
not a matching leakage theorem. Broad unrelated PDE/Abelian-integral
hits were screened out. The initial primary-page screenshot timed out;
the theorem/proof text was accessible. No essential access blocker or
successful image inspection is claimed. The 2026 disk-growth Remez
preprint surfaced as an unread lead; it is not an imported estimate
for this sign-weighted integral or evidence of novelty.

The working checkpoint is preserved in
[the source-review note](../2026-10-29-sign-adapted-leakage-source-review-working.md).
No new lemma, mathematical script, theorem specialization or sign
estimate was produced. Full matching and supporting Mathlib coverage
remain unchecked. No cross-notebook input was used.

For subsequent routing, the independent fixed-displacement
aggregate-kernel target already has a saved SPECIALIZE assessment in
`2026-10-29-fixed-sector-aggregate-kernel-test.md`. Its recorded stop
was procedural: no mathematical aggregation attempt or failed exponent
was established. Selecting its concrete calculation after parking this
different mechanism is not another readiness repair or a claim to have
overcome L475's growing-disk obstruction. Preserve the historical stop
and the existing assessment unchanged; the current Next action lives
only in PROGRESS.md. This known-tool specialization is not a justified
creative invocation. The latter still lacks a concrete covered central
arithmetic or sign-multiplier mechanism.
