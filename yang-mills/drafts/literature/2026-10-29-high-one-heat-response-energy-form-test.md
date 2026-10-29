# High one-heat-line response: energy-form source comparison

TARGET: Test whether L301's full-H form estimate makes L297's complete high one-heat-line response o(1) at r_N.
CHECKED: 2026-10-29
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 551 completed the bounded searches below, inspected primary matrix statements/proof cases and the Boulton--Dimoudis norm-ideal comparison, and screened L296/L297/L301, saved complementary/low assessments, ATTEMPTS/047--050 and the older first-pair weighted-high draft. No inspected theorem supplies this complete weighted relative-cube response; no novelty inference.
SOURCE_EVIDENCE: Higham--Lin, MIMS 2013.73, Definition 3.3/section 3.1.4, p. 6, https://eprints.maths.manchester.ac.uk/2067/1/paper.pdf ; Schweitzer 2203.03930v1, section 2.1, Lemma 1/Theorem 2 with proofs, PDF pp. 2--3, https://arxiv.org/pdf/2203.03930v1 ; Watrous 2018 draft, section 1.1, pp. 32--33, (1.165)--(1.175), https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf ; Ponge Summer 2025 chapter 4, slides 54--57, https://raphaelponge.org/wp-content/uploads/2025/07/summer-chap4-1.pdf ; Boulton--Dimoudis, JFA 284 (2023) 109784, Definition 2.1/Theorems 3.1--3.2, https://pure.hw.ac.uk/ws/portalfiles/portal/76279343/1_s2.0_S0022123622004049_main.pdf . Readings and exclusions below.
COMPARISON: Finite holomorphic calculus, ordered resolvent derivatives and dimension-independent Schatten product/duality bounds cover the standard tools. L296/L297 supply the local spectral count and admitted contours; L301 supplies the signed full-H form bound. The missing weighted high trace is a quantitative specialization to prove, not a consequence already contained in L297(20) or general semigroup analyticity.
GAP: Establish mesh-uniform two-sided scaled-energy trace bounds through empty, first and mixed source order on the entire high contour, retaining both noncommuting orders and every inverse/contour derivative; pair all four scalar terms with L301(4) and compare with o(1) at fixed r_N. No such bound or rate is established here.
REASON: Essential source coverage is adequate for one bounded mathematical specialization of the unchanged target. Cite the standard calculus and ideal inequalities; develop only the weighted uniform estimate and its application. This literature-only step derives no new result and does not approve the estimate as true.
LITERATURE_REASON: High-sector energy weights and their mixed source orders are outside the saved low-cluster scope; reuse applicable matrix and Gaussian sources while checking this precise difference.
SCOPE: L301 L297 L296 with their upstream premises, including L003 L279 L280 L282 L283 L287 L289 L298 L299 L300; exact SU(2), even N, a=8/N, counting measure, reflected 12-bumps, fixed unweighted H and Q, ambient own-slice jets, full Haar/both-determinant density, boundary-fixed gauges and every variable normal endpoint.

The proposed target is the complete high part of L297's one-heat-line
term, with exactly the registered complementary covariance and fixed
r_N. It has the same four source-product placements as L301(29),
with H^lo replaced by H^hi. Both source orders, all external colors
and source derivatives of the high spectral split must be retained.

The source-review task registered at step 550 was to compare the already cited
finite holomorphic calculus, resolvent derivative and Schatten-ideal
results with the two-sided Ahat^(1/2) weights needed for pairing
against L301(4). In particular, analytic continuation in a fixed
finite dimension does not by itself supply a bound uniform in N.
The growing high spectrum and noncommuting insertions cannot be
replaced by scalar derivatives. Read the relevant primary hypotheses
and proof cases before approving a specialization; the full-spectrum
hypothesis of Schweitzer's Theorem 2 is still distinct from a spectral
subcontour. No high-residue proof or improved rate is asserted here.

Plausible downstream use: with the accepted low response and L297's
multiple-heat-line result, a successful complete high estimate could
remove the terminal complementary-tail bottleneck at this r_N.
It would not give shell control at other scales, the uncut estimate,
uniform higher remainder, interacting lower bound, continuum axioms
or positive mass. A terminal result must keep that limitation explicit.

Continue only after separate source approval and only if the full
high scalar admits the o(1) estimate, or a refined controlled estimate
isolates a concrete remaining threshold. Preserve any failed weight
placement or uncontrolled spectral sum precisely. A poor absolute
bound alone does not disprove the target. The bare all-heat stop in
ATTEMPTS/050 does not settle this different complementary-covariance
test. Full matching Mathlib coverage is not checked.

## Completed literature-only comparison: step 551, 2026-10-29

### Local input and duplicate screen

Read L301's hypotheses and (4)--(5), sections 6--7, L297's
hypotheses, (9)--(12), section 4 and its high-spectrum audit,
and L296 section 3 and its matrix-source audit. Reuse the completed
complementary/low assessments for unchanged Gaussian and projector
coverage. The official Jaffe--Witten target version remains the one
in foundations/01-target-and-scope.md, checked there on 2026-10-28;
this review selects no different continuum target or route.

L301(4) controls every required zero-source Wtilde derivative on
the full fixed H. Its low trace uses finite-rank residues. L297(20)
controls an unweighted high trace and was paired with an unweighted
W bound. Neither imports the desired weighted-high statement.

The specifically named older draft
drafts/2026-10-08-first-pair-weighted-high-trace.md concerns the
axial first-pair trace L076/L077 and a frozen diagnostic, not this
complementary polynomial or its high spectral derivative. No old
proof was imported. ATTEMPTS/047--049 stop particular rearrangement,
norm and gauge-identity mechanisms; ATTEMPTS/050 stops the bare
all-heat response. None decides this different scalar. All prior
evidence and unfinished work are retained.

### Primary matrix statements actually inspected

Higham--Lin, *Matrix Functions: A Short Course*, Definition 3.3,
assumes an analytic scalar function on
and inside a closed contour enclosing the matrix spectrum; section
3.1.4 states equivalence with the other definitions. It supplies
finite holomorphic calculus, not uniform constants. For the high
subcontour use L297's defined spectral piece and L296's contour
justification. Retain exclusion of zero and justify any closing
arc before using open rays. No reproof of the standard theorem is needed.

Schweitzer, *Integral representations for higher-order Frechet derivatives
of matrix functions*, Lemma 1, requires the contour point outside the spectrum
and sums all ordered permutations of resolvent insertions. Read its
Neumann-series induction through the second-order case and Theorem 2's
integral proof. Theorem 2 requires a full-spectrum contour and an
analytic function; it is not a selected-cluster theorem. Use Lemma 1
on L297's admitted fixed high contour with directions -B_- and -B_+,
retaining both mixed orders. The printed intermediate sign discrepancy
is already qualified in the saved moving-low review; use the lemma
statement and the signed directions. Outside Ahat^(1/2) weights here
are fixed zero-source matrices, not differentiated square roots.

Watrous, *The Theory of Quantum Information*, (1.173)--(1.175),
gives finite complex-matrix Schatten duality,
trace pairing and the two-sided ideal inequality, without dimension
constants, positivity or commutation assumptions. Ponge,
*Introduction to Noncommutative Geometry*, chapter 4, slide 56,
states general product Holder with reciprocal exponents adding,
and its multi-factor version; slides 54--55 give the ideal property
and slide 57 the trace pairing. These supply the required standard
inequalities, without reproof. Applying them still requires explicit
uniform Schatten norms for the actual factors; an unweighted bound
does not automatically control an energy-weighted product.

### Stronger semigroup comparison and hypotheses

Read Boulton--Dimoudis, *Norm-ideal perturbations of one-parameter
semigroups and applications*, version of record at the direct repository
PDF above: section 2, printed pp. 3--5, Definition 2.1; Theorem 3.1
with its n=1 and n=2 proof cases, printed p. 10; Theorem 3.2 and
proof, printed pp. 10--12. Their framework assumes an immediately
norm-continuous semigroup. Membership B in B_q(A) requires the
Hille--Phillips conditions, including relative operator boundedness,
Schatten membership of Btilde exp(-tA) for each t>0, and integrable
Schatten norm on (0,1). Theorems 3.1/3.2 give Schatten regularity of
Dyson terms and trace-norm convergence of the sufficiently late tail.
The proofs use convolution bounds depending on those norm integrals.
They do not supply the proposed uniform weighted spectral-subcontour
estimate or its two-source scalar. The registered relative form
bound is not a verification of those hypotheses uniformly in N.
No application, failure of applicability or divergence is proved here;
this source is a comparison, not an additional mathematical premise.

Zagrebnov's monograph and 1989 Gibbs perturbation paper were search
leads only; their theorem texts were not inspected or imported.
No essential source is blocked: the finite tools above suffice
for the direct test. The publisher DOI redirect failed, but the
repository supplied the actual Boulton--Dimoudis version of record.

### Bounded search record

Queries included:

- `"matrix functions" "Fréchet" "Schatten" derivatives relative perturbations heat semigroup`
- `"energy" "weighted" "Schatten" "resolvent" semigroup perturbation`
- `"heat semigroup" "form bounded" "trace norm" derivatives`
- `"Schatten" "two-sided" "resolvent" perturbation heat`
- `"Yang-Mills" "high" "heat" "complementary covariance"`
- `"Schatten" "form perturbations" "semigroups"`
- `"heat" "relative perturbations" "trace ideals"`
- `"holomorphic" "Gibbs semigroups" perturbations forms`
- `"lattice gauge" "heat" "source" "trace" Wilson boundary perturbation`
- `"Integral representations for higher-order Fréchet derivatives" Schweitzer 2203.03930`
- `Boulton Dimoudis "Norm-ideal perturbations" arxiv`

Generic resolvent, Schrodinger and thermal lattice hits supplied no
matching inspected theorem. Only the primary statements above support
the decision; snippets, abstracts and unread leads are not theorem
evidence. This bounded search does not establish novelty or absence.

### Approved difference, threshold and downstream use

The saved TARGET is unchanged. A mathematical specialization must
retain the entire high part of H=A(s,t)^(-1) exp(-r_N A(s,t)), with
r_N and the contour fixed in source differentiation, and all four
registered terms Wtilde H^hi_-+, Wtilde_- H^hi_+, Wtilde_+ H^hi_-,
Wtilde_-+ H^hi inside the one-color trace, with final factor three.
The threshold is the complete signed scalar o(1), not one selected
term, a ground-mode statement or normalized leading cancellation.

A direct attempt may use L296's scaled spectral count and relative
resolvent bounds, with enough inverse-power regularization to test
two-sided weighted trace control. Retain derivatives of every
regularizing factor. No weighted factorization, uniform trace bound
or improved rate has been derived here. Preserve noncommuting factor
order and account for the growing spectrum; source radii must come
from admitted local estimates or be explicitly justified. Multiplying
an unweighted estimate by the growing norm of the outside weights
may lose the threshold and would not settle the signed scalar.

Continue if a complete estimate reaches o(1), or a controlled bound
isolates a precise remaining threshold. Save any uncontrolled weight
placement, source order or spectral sum and stop that attempt without
calling the target false. A rigorous nonvanishing complete scalar
would refute this intermediate target; a poor upper bound would not.
No source-family Wilson cancellation, new boundary identification
or spectral-branch regularity is assumed.

Together with L301's low scalar and L297's multiple-heat-line result,
success could control the terminal complementary response at this
r_N only. Other scales/shells, the uncut coefficient, uniform higher
remainder, interacting lower bound, continuum axioms and positive
mass remain separate gaps. Full matching Mathlib coverage for this
weighted relative-cube statement is not checked; standard supporting
matrix inequalities are not a matching theorem for the target.

This step completes source coverage only: no lemma or mathematical
script, new bound, or exploration-budget reset. Recommend one bounded
calculation as specialization/reproduction using the cited tools,
not a creative mechanism or an originality claim. The supervisor
owns subsequent approval and routing.
