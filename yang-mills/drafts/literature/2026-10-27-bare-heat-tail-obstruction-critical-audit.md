# Bare heat-tail obstruction audit: completed coverage comparison

TARGET: Critically audit L296's complete bare heat-tail obstruction, including the uniform high-spectrum remainder, source derivatives, Wilson bounds and dyadic subsequence.
CHECKED: 2026-10-28
DECISION: EXPLORE
SEARCH_EVIDENCE: Compared all of L296 with the ready shell and upstream-cubic assessments, L287 sections 1--3, history 528 and ATTEMPTS/047--050; searched primary matrix-function derivatives and Schatten product inequalities, then read the statements and proof cases identified below. No completed L296 audit was found in these selected records; no novelty inference.
SOURCE_EVIDENCE: Read Higham--Lin MIMS 2013.73 section 3.1.3/Definition 3.3 and section 3.3.2; Schweitzer arXiv:2203.03930v1 section 2.1, Lemma 1/Theorem 2 and proofs, pp. 2--3; Al-Mohy--Higham (2009) Theorems 2.1/3.1, pp. 1641--1642; Ponge Summer 2025 chapter 4 slides 53--57, especially the Schatten Holder proposition on slide 56; Watrous 2018 draft section 1.1, Norms of operators, (1.165)--(1.175), pp. 32--33. Reuse the recorded Wilson/relative-mode/density source scope.
COMPARISON: The inspected results cover fixed-matrix analytic calculus, ordered mixed derivatives and dimension-independent Schatten inequalities; they do not supply L296's mesh-uniform contour estimates, Wilson bounds or negative complete response. The explicit local arguments are accessible to a separate audit without an essential unread theorem; fixed-N analyticity alone supplies no uniformity.
GAP: Independently audit L296(8)--(24), including the complex source polydisc, high-spectrum trace remainder, both differentiated heat lines, weighted cubic tensor, all source terms, constants and ordinary dyadic passage. This comparison verifies none of those Wilson-specific claims.
REASON: Admit one later RESEARCH / REPRODUCTION conceptual audit of exactly TARGET. Reuse adequate shell/upstream coverage and the standard matrix results by citation; audit only the claimed uniform specializations. Any essential stronger theorem requires a separate source gate.
LITERATURE_REASON: The newly registered REVIEW_REQUIRED audit adds complex-source uniform trace and heat-derivative obligations beyond the ready shell assessment; the present turn checks those supporting sources rather than reopening the shell search.
SCOPE: Exact L296 with essential L003 L279 L280 L282 L287; SU(2), even N>=2, a=8/N, counting measure, all-face pins/fixed gauges, both variable normal endpoints, exact reflected product bump, own-slice jets/full density, both source orders and the stated open real source domain. No effective-action replacement or uncut growth estimate.
COVERED_TARGET: Critically audit L296's complete bare heat-tail obstruction, including the uniform high-spectrum remainder, source derivatives, Wilson bounds and dyadic subsequence.

## Original registration (2026-10-27; retained)

The original registration required a literature-only invocation to approve or amend this exact
audit scope, reusing adequate prior coverage rather than searching
again for the original shell target. No new source theorem is presumed
essential merely because it might be relevant. If the standard
finite-matrix estimates are adequately covered, record that comparison
and admit a later proof_audit/conceptual_audit, deep_research/xhigh.

The exact mathematical input is L296 under SU(2), even N>=2, a=8/N,
counting measure, all-face pins, fixed boundary gauges, every normal
endpoint, the exact reflected product bump, own-slice Wilson jets,
the full D_N and both derivatives in the real source domain. Its
essential supporting results are L003, L279, L280, L282 and L287.
L291 is a contrast with the uncut coefficient, not a shell estimate;
L294--L295 and any continuum boundary replacement are not inputs.

The proposed audit should inspect the complete high-spectrum trace
bound in L296(11)--(14), the rank-four compression and its sign,
every differentiated covariance in (16)--(17), the sharper one-heat-leg
entry estimate, the bounded-weight use of L287 and all cubic/quartic
terms, the three-color and lambda_0 factors, and the dyadic passage.
Check the quantitative comparison (23) against the required O(1)
threshold and preserve both normal endpoint cases. A missing uniform
bound or source term requires a precise repair or withdrawal of the
affected claim, not promotion of a density-only calculation to a
complete obstruction. Full/supporting Mathlib coverage is not checked.

If accepted, the result stops only the specified bare simultaneous
heat-tail path. An effective-action replacement would change the
mechanism and requires its own exact target and source assessment.
The uncut logarithmic estimate, uniform higher remainder, interacting
lower bound, continuum nonzero sector and finite positive mass remain
unresolved. No lemma, proof audit, or new mathematical result is
established by this future-work registration.

## Completed comparison, 2026-10-28

The main target gap remains the interacting continuum construction and
finite positive mass. The immediate coefficient gap is quantitative
control beyond the audited uncut o(N^2) cancellation. The intermediate
target is independent scrutiny of the complete obstruction in L296;
its downstream use is a justified decision about this particular bare
shell route, rather than a bound for the uncut coefficient. No new
lemma or stronger asymptotic is sought in this literature step.

### Primary statements and applicability

N. J. Higham and L. Lin, *Matrix Functions: A Short Course*,
[MIMS EPrint 2013.73](https://eprints.maths.manchester.ac.uk/2067/1/paper.pdf),
2013 version, section 3.1.3, Definition 3.3 (printed p. 6), gives
the Cauchy integral definition for a complex square matrix when the
function is analytic on and inside a closed contour enclosing its
spectrum. Section 3.3.2 (p. 9) states the Frechet derivative definition.
These are fixed finite-dimensional statements, with no uniform claim
for an increasing matrix dimension or a closing spectral gap.

M. Schweitzer, *Integral representations for higher-order Frechet
derivatives of matrix functions: Quadrature algorithms and new results
on the level-2 condition number*,
[arXiv:2203.03930v1](https://arxiv.org/pdf/2203.03930v1),
8 March 2022, section 2.1, pp. 2--3, Lemma 1 and Theorem 2,
(2)--(8), supplies the ordered-resolvent formula for every derivative
order. Theorem 2 requires analyticity on and inside a contour winding
once around the spectrum; it sums over all permutations of the
directions. Its proof uses Lemma 1's Neumann-series/product-rule
argument and differentiation of the Cauchy representation. Read both
proof cases, including the base derivative and induction. At order two
the theorem retains both orders even for noncommuting directions.
Its statement imposes neither self-adjointness nor simple eigenvalues.
It gives no N-uniform remainder or spectral-count estimate.

A. H. Al-Mohy and N. J. Higham, *Computing the Frechet Derivative of
the Matrix Exponential, with an Application to Condition Number
Estimation*, SIAM J. Matrix Anal. Appl. **30** (2009), 1639--1657,
[author PDF, MIMS 2008.26](https://eprints.maths.manchester.ac.uk/1218/1/alhi09.pdf),
Theorem 2.1, p. 1641, requires 2n-1 continuous derivatives on the
specified open domain and places the first derivative in an upper
block of a matrix function. Theorem 3.1, p. 1642, gives the ordered
power-series derivative when ||A|| is inside the convergence radius.
For the exponential that radius is infinite. These support ordinary
finite matrix differentiation; they are not uniform heat bounds or
an integral proof of L296(17). The latter is a written finite Duhamel
identity to check directly in the audit, with its conjugations and
both source orders retained. No numerical algorithm is an input.

R. Ponge, *Introduction to Noncommutative Geometry*, Sichuan University,
Summer 2025, [chapter 4: Singular Values and Schatten Classes](https://raphaelponge.org/wp-content/uploads/2025/07/summer-chap4-1.pdf),
slides 53--57, defines Schatten classes, states their ideal property,
and gives the Holder product proposition on slide 56 and its
multi-factor version. For 1/p+1/q=1/r it bounds ||ST||_r by
||S||_p ||T||_q; the p,q,r>=1 cases suffice here. Read the full
proposition and adjacent definitions/qualifications; these slides
state, rather than prove, the general Holder theorem. This standard
named inequality may be cited, without reproving it. Finite matrices
are a specialization on a separable finite-dimensional Hilbert space,
and the displayed constant is independent of its dimension.

J. Watrous, *The Theory of Quantum Information*,
[2018 prepublication draft](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf),
section 1.1, Norms of operators, printed pp. 32--33, (1.165)--(1.175), supplies the
finite Schatten definition, singular-value identification, norm
duality, trace Holder inequality and ideal bound. These statements
apply to arbitrary complex finite matrices, including nonnormal
source perturbations; positivity must not be imposed on those
perturbations. The dual trace bound alone is not the general product
inequality; the latter is separately covered by the Ponge statement.
No full trace-ideal theorem is being replaced by a dimension-dependent
entrywise estimate.

Applicability comparison, not a proof of L296: its fixed space H and
matrix functions fall within finite matrix calculus, provided the
chosen contours avoid zero and the perturbed spectra. The function
e^(-theta z)/z requires that exclusion. The complex source polydisc,
contour deformation/closure, weighted resolvent bounds and uniform
Schatten control in (12)--(14) remain local audit obligations. The
spectral counting and density convergence are local L003/L282 inputs,
not conclusions of these references. No general matrix theorem
imports the rank-four sign or disposes of high modes for this family.

### Reuse, failures and source-access qualifications

Reuse `2026-10-27-complete-coefficient-dyadic-shell-test.md` and
`2026-10-26-upstream-cubic-critical-audit.md`, including their versioned
primary readings and exclusions. Bałaban's subtracted small-field
effective action and Bauerschmidt's finite-range decomposition do not
estimate this unchanged bare heat tail. Their coverage need not be
refreshed for an audit of L296's written finite argument. The official
Clay statement/version was checked in the prior shell assessment;
no new route or target version is selected here.

The bounded notebook check read all of L296, L287 sections 1--3 and
the selected failure records. L287(9)--(11) concerns the unweighted
curl polynomial; extension to bounded plaquette weights in L296(20)
is an explicit audit obligation, not a previously imported weighted
theorem. Source derivatives, normal endpoint modes and full density
must be kept. L291 is contrast only, and L294/L295 do not supply
full-box replacements. History 528 records an unaudited obstruction;
ATTEMPTS/050 makes its stop conditional on that audit. Neither is a
duplicate completed verification. ATTEMPTS/047--049 preserve distinct
integration-by-parts, absolute-norm and orbit-identity failures.

Queries included `Higham Lin matrix functions Frechet derivative
Cauchy integral theorem 2013 pdf`; `Schatten Holder inequality trace
ideals matrix p q r`; `matrix exponential derivative Duhamel Wilcox
1967 exponential operators parameter differentiation`; exact-title
searches for Schweitzer's higher-derivative paper; and `Schatten
Holder inequality product Theorem pdf norm`. Search results were
discovery only. The Wilcox DOI/publisher PDF was inaccessible; it is
an unread lead, not an essential premise. Khalkhali, *Basic
Noncommutative Geometry*, second edition (2013), was located, but
targeted retrieval of Appendix B stalled; its search excerpt is not
used as source evidence. The readable Ponge proposition covers the
needed standard Holder statement. Other search hits, including
Sutter--Berta--Tomamichel's introduction and Fehr's normal-matrix
proof sketch, are not used to certify the general product inequality.
There is no essential source blocker after these substitutions.

### Separate audit and decision threshold

Admit exactly TARGET for a later conceptual audit, classified
REPRODUCTION: independently checking a written local proof claims
no new mathematical mechanism or certified originality. Do not reprove
the general matrix-function or Schatten theorems. Audit L296's
claimed specializations and every estimate needed for its conclusion.
Full and supporting Mathlib coverage remain **not checked**; neither
absence nor an exact formal theorem is claimed.

The bounded test is acceptance of the complete response in (6), with
(11)--(14)'s high-spectrum remainder uniform in N and complex sources,
(16)--(18)'s differentiated heat estimates, (19)--(22)'s complete
Wilson terms, rank-four compression/sign, three colors and lambda_0
normalization, and (24)'s fixed-origin dyadic subsequence. Check the
actual bounds in (23) against the required uniform O(1) shell threshold,
without first replacing the complete response by a density-only one.
Retain all inherited input hypotheses and both source orders. If a
uniform estimate or source contribution fails, isolate the first
failure and withdraw or qualify the affected claim; a repair outside
this exact audit scope requires separate coverage before development.
This review neither approves nor rejects the completed step 528.

Completed outcome: EXPLORATION, kind LITERATURE, classification
NOVELTY_UNCHECKED, actual task literature_comparison. This supplies
supporting citations and scope approval, not a mathematical advance
beyond the checked sources. Mathematical exploration usage is zero.
No lemmas, mathematical scripts, DAG or PROOF.md argument were changed.
The next action stays exactly TARGET, with proof_audit/conceptual_audit,
deep_research/xhigh: mesh-uniform noncommuting analytic and tensor
estimates need scrutiny before the recorded route stop is relied on.
