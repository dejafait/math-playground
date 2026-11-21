# Signed theta quadrature remainder — completed source comparison

TARGET: Assess whether an actual-weighted Gaussian remainder can supply a degree-uniform root-sign barrier for the theta Jensen family beyond common interlacing, identifying one nonduplicate independently testable bound or a precise obstruction.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step543 searched Gaussian/Peano remainders on infinite intervals and theta Jensen root barriers; inspected Gautschi's primary Hermite-remainder proof and finite-support contour theorem, DLMF derivative formulas, and reused the recorded interlacing, root-disk and Jensen-wedge assessments. Exact queries and read limits below; no novelty inference.
SOURCE_EVIDENCE: Gautschi, Orthogonal Polynomials: Computation and Approximation (OUP2004), Theorem1.48 and corollary, pp23–24,(1.4.10)–(1.4.16), complete proofs; Theorem2.48, pp116–117,(2.3.21)–(2.3.25), complete proof and bounds; DLMF3.5(v),(3.5.19)–(3.5.20),18.9.23; reused Laguerre zero and finite exactness coverage. Primary links and applicability limits below.
COMPARISON: The derivative remainder locates no evaluation point and supplies no actual-weighted cancellation estimate. The inspected contour alternative explicitly assumes finite support, unlike nu. Existing root-disk and wedge comparisons still require missing actual sign/margin inputs. Only a narrow symbolic derivative-hypothesis test is covered, not the requested degree-uniform barrier.
GAP: Determine the exact degree/node regimes in which the standard whole-support derivative-sign premise is available. Actual-weighted cancellation, a reference with controlled roots, alternating barrier margins and all-degree mixed positivity remain unresolved.
REASON: Informative source-scope negative: park automatic signed-barrier import from positive Gaussian weights or a finite-support contour formula. Nominate one independently testable analytic hypothesis classification, separately specified and requiring next-turn approval; do not rerun or enlarge the cubic pair.
SCOPE: Literature-only step543. SPECIALIZE covers only the separate derivative-sign hypothesis test, not a general Peano theorem on unbounded support or a theta root-sign bound. No new theorem, lemma, mathematical script or specialization was derived here. Original nomination below is retained; its unread-source language is superseded only to the extent documented below.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED changed the target from finite cubic replay to signed varying-degree remainders; essential remainder hypotheses were unread. This step supplies the primary comparison, not a theta cancellation bound.

## Original nomination, retained

Keep L795's actual law nu, the pushforward of K(u)du/m_0 under v=u^2,
and its P_d and F_(d,sqrt(v)) normalizations. L019/L021 supply positivity
and finite moments, and the audited L805 rule supplies one fixed
two-node reference. A possible question for source review is whether
the remainder of this rule, integrated against the actual law, gives
signs at specified barriers for P_d as d varies. No such sign, barrier
choice, reference hyperbolicity or estimate is asserted here. No
derivation of a new remainder identity was undertaken in step542.

Read the relevant primary remainder hypotheses and proof cases before
large extracts: unbounded support, integrability, derivative-sign versus
actual-weighted cancellation, and degree dependence all matter. Search
the precise statement and standard Gaussian/Peano-kernel terminology;
compare stronger known Jensen results and relevant local failures.
Reuse the source comparisons already completed for exactness and MSS;
do not browse them again merely to renew a gate. The prior comparison
explicitly did not assess smooth-function remainders.

Use L019/L021/L795/L805 as exact local inputs. L791 gamma provenance
and inherited L778 analytic/software contracts matter only if a later
finite certificate needs them. L796's Favard stop and L772's generic
positivity countermodel are contrasts, not assumptions. Preserve all
existing stops. No cross-notebook input is proposed.

Continue only if the review isolates a concrete sufficient inequality
with an independently testable threshold that does not merely restate
RH or known finite-degree hyperbolicity. An unsigned error bound,
positive quadrature weights or the already failed common-interlacing
premise alone do not meet that test. If standard remainder hypotheses
fail or the proposal duplicates a recorded stop, record the exact
obstruction and park that dependent mechanism. Do not repeat the
unchanged Gaussian pair or expand its precision/degree as a substitute.

The central bottleneck is still actual-Xi all-degree mixed positivity.
The downstream use would be a sufficient degree-uniform sign-transfer
mechanism, if one can be specified. No justified creative proof target
is ready: unread essential source coverage and missing reference/sign
control are the blockers. Source comparison is the next task; a newly
specified research continuation must receive separate approval. Full
matching Mathlib coverage is unchecked.

## Completed comparison — step543, 5 November 2026

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
source coverage for a signed quadrature error small enough, in the
required direction, at independently specified real root barriers.
Downstream use would be sign transfer from a reference polynomial;
that reference's root geometry and its margins must also be proved.
The review's continuation test was a concrete sufficient estimate with
an independently testable threshold, or an exact source obstruction.
No such actual-weighted estimate was found. This is a source-scope
negative, not a theorem that every quadrature approach fails.

### Primary statements and relevant proof cases

Walter Gautschi, *Orthogonal Polynomials: Computation and Approximation*,
OUP2004, first edition, ISBN0198506724,
[primary book scan](https://csclub.uwaterloo.ca/~pbarfuss/Walter_Gautschi_-_Orthogonal_Polynomials_-_Computation_and_Approximation_%282004%29.pdf),
Theorem1.48 and corollary, pp23–24, (1.4.10)–(1.4.16): the Gaussian
sum integrates the Hermite interpolant matching values and first
derivatives at its n nodes. The corollary expresses the error using
f^(2n) at an unspecified interior point and the positive squared norm
of the monic node polynomial. Read both complete proofs: exactness
integrates the Hermite basis, interpolation supplies a squared node
factor, and a weighted mean-value step finishes the remainder formula.
On unbounded support, integrability must be checked; smoothness alone
is not an integrability assertion. The later polynomial-only test
avoids any general extension to arbitrary smooth functions.

Theorem2.48, pp116–117,(2.3.21)–(2.3.25), explicitly requires finite
support inside an analytic domain. Its proof uses Cauchy's formula,
interchange and the Cauchy-transform error kernel. The subsequent
bounds are unsigned contour estimates. They cannot be imported
directly for the full theta pushforward or as cancellation estimates.
The general Gaussian existence/exactness results are already covered
by step539; their proofs were not browsed again.

Directly inspected NIST [DLMF3.5(v)](https://dlmf.nist.gov/3.5#v),
[3.5.19](https://dlmf.nist.gov/3.5.E19)–[3.5.20](https://dlmf.nist.gov/3.5.E20),
accessed 5November2026. It permits finite or infinite support intervals
for the orthogonal-polynomial setup and displays the derivative
remainder with its squared-norm coefficient. This confirms the
normalization, but does not locate the derivative's evaluation point,
bound an oscillatory derivative, or supply a theta cancellation estimate.
Do not infer a global supremum bound merely from finite moments.

For the bounded hypothesis test, directly inspected
[DLMF18.9.23](https://dlmf.nist.gov/18.9.E23):
d L_k^(alpha)(z)/dz = -L_(k-1)^(alpha+1)(z), for k>=1;
the page cites Szego (1975),(5.1.14). Reuse L795's inspected
DLMF18.5.12 normalization and Table18.3.1/18.2(vi) zero theorem:
Laguerre degree k with alpha>-1 has k simple zeros in (0,infinity).
These standard statements cover the later degree-lowering calculation,
including a parameter that changes with the derivative order. No
theta derivative formula, sign classification or new consequence is
proved in this literature turn. Boundary cases and every chain-rule
factor belong to the separate mathematical test.

### Actual hypotheses and what the citations do not pay

L019/L021 and L795 already give a positive law nu on the full positive
half-line, all finite moments, and the exact normalized average. Thus
fixed-degree polynomial integrands and Hermite interpolants have
finite integrals. The raw-moment Gaussian node polynomial remains
different from Jensen P_d. L805 supplies only the particular exact
cubic rule and its independently audited failed interlacer premise.
Its nodes/weights do not create a signed remainder theorem for other
degrees. No new use of L791/L778 numerical contracts is needed here.

A root barrier needs specified points and a nonzero reference value
at each point, together with a remainder inequality in the direction
preserving that value's sign. The derivative theorem leaves its
interior evaluation point unspecified. Therefore its statement alone
does not discharge the required sign or margin hypotheses for the
oscillatory integrand. No whole-support derivative sign, signed
actual integral estimate, reference hyperbolicity or alternating
barrier was supplied by the inspected sources. This distinguishes
an unpaid premise from a proof that the actual error has the wrong
sign. In particular sign changes of a derivative, if later proved,
would not themselves imply sign changes of its weighted integral.

Three versions of the proposal were screened within this source step:
the derivative/Hermite sign premise; actual-weighted Peano cancellation;
and a contour remainder bound. The first permits a precise bounded
hypothesis test. The second has no identified theta estimate and is
parked, rather than approved with an unnamed kernel. The third has
the finite-support mismatch above; truncating nu would require its
own changing rule and signed tail/error analysis. No truncation or
limiting contour argument is asserted.

### Known overlap, duplicates and source limits

Reuse `2026-11-05-theta-gauss-compressed-interlacing-scope.md` for
finite exactness and MSS. Read L795's full proof, L805's finite
construction/interlacer proof and its existing audit qualifications,
and L019/L021. Preserve the pair stop in
`../../ATTEMPTS/2026-11-05-theta-gauss-two-node-interlacing-stop.md`.
Reuse the Favard and generic-Turan comparisons recorded by step539;
neither is a premise of the new hypothesis test. The new test changes
the mechanism to derivative-sign applicability for arbitrary n,d;
it is not another root computation of the unchanged Gaussian pair.

Reuse `2026-11-05-central-hermite-theta-gram.md` for GORZ,
1902.07321v2, Theorem2 (degrees1–8, all nonnegative shifts), and
`2026-11-05-polynomial-jensen-wedge-central-scope.md`, step473,
for Holland 2608.08682v1, Theorem1.1 and Proposition2.2. The latter
requires n^3 log^2(n+2)>=K d^5 and an eventual onset; its conditional
stability result retains independent model/derivative hypotheses.
Those inspected assessments already exclude automatic central-shift
transfer. The arXiv HTML landing text was opened to identify the
search hit, then the ready assessment was reused instead of rereading
its theorem proofs. Also read
`../../ATTEMPTS/2026-11-05-relative-root-disk-transfer-unpaid.md`:
L793's completed tolerance tool still requires actual model, mesh
and residual inputs. Another general perturbation inequality would
duplicate that unpaid transfer. No new low-degree root claim is sought.

Bounded searches included `Gauss quadrature error unbounded interval
derivative 2n Peano kernel Gautschi theorem`, `Jensen polynomials
Riemann xi Gaussian quadrature remainder hyperbolicity sign`,
`"Jensen" "Gauss" "remainder" theta polynomials`,
`"Gaussian quadrature" "Peano kernel" "positive" unbounded interval
polynomial`, and `"Gautschi" "Theorem 1.48" remainder`.
Notebook-local searches checked Gaussian/Peano/Hermite-remainder
phrases and the specific theta assessments/ATTEMPTS, then the exact
derivative-sign/Laguerre phrases. No matching recorded all-n,d
derivative-hypothesis classification was located; this is not a
novelty claim. Broader hits about unrelated Gaussian asymptotics
were not loaded as mathematical inputs.

Gautschi's 1981 author-hosted survey 074.pdf was accessible initially
only in introductory text; targeted Section4 requests repeatedly
timed out. A shell download failed DNS resolution. It is not proof
authority here; the accessible 2004 book supplies the needed proof.
Stroud–Chen, *Peano Error Estimates for Gauss–Laguerre Quadrature
Formulas*, SIAM J. Numer. Anal.9(1972),333–340,
[DOI10.1137/0709033](https://doi.org/10.1137/0709033), was read only
at its publisher abstract: its stated weight is exp(-x). Its full
theorems are unread and are not imported for nu. Moving the theta
density into the integrand would change derivative hypotheses and
is not justified here. Other search snippets, including recent
finite-strip claims, supply no theorem input. No source-access retry
is necessary for the selected polynomial derivative test.

### Decision and bounded continuation

The original desired actual-weighted degree-uniform barrier remains
uncovered; park its automatic import. SPECIALIZE permits only the
separate analytic test specified in
[the continuation assessment](2026-11-05-theta-gauss-derivative-sign-test.md).
Classify the standard derivative-sign premise as a function of node
count and degree, including exactness and degenerate cases. Continue
this sufficient mechanism only if the classification leaves a
nontrivial growing-degree regime capable of supporting the needed
alternating root signs; otherwise preserve its exact cutoff and stop
it. Do not mistake failure of a sufficient derivative premise for
failure of actual-weighted cancellation or RH.

There is no justified creative root-barrier target yet: no specified
signed theta estimate with independent reference margins is ready.
The proposed conventional symbolic specialization isolates that
obstruction without relabeling it creative. It receives separate
approval next turn. No mathematical exploration budget was spent or
reset. PROOF and DAG need no change because the argument has not
changed. Mathlib full matching coverage remains unchecked. No
cross-notebook input, lemma or mathematical script was used or written.
