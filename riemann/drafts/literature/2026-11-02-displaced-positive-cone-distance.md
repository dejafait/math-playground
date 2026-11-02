# Displaced positive-cone distance — completed bounded source comparison

TARGET: Test whether kappa_e=inf_(b_a>=0 real)||1+sum_(a!=x)b_a*W_a||_(L2(T),normalized) satisfies kappa_e>=exp(-n/100)*n^(-C) with absolute C and onset for every L666 displacement vector, or give an admissible sequence with (-log kappa_e-n/100)/log n unbounded above.
CHECKED: 2026-11-02
DECISION: EXPLORE
SEARCH_EVIDENCE: On 2026-11-02 searched nonnegative rational approximation, positive-residue noncancellation, Blaschke positive combinations, cone projection and quantitative NNLS separation; exact queries and inspected primary ranges are below. Reused the positive-mass and complex-span assessments and inspected the relevant L666/L647/L672 proofs and scalar/Gram failure records. No matching evaluated rate was identified; this bounded search does not certify novelty.
SOURCE_EVIDENCE: Moreau (1965), Sections 1.a, 3.a/d, Proposition 4.a and Corollary 4.b, pp.273,278-281, including both proof directions; Slawski--Hein arXiv:1205.0953v2, normalization, Sections 2.1--2.3 and Appendix B, pp.4--6,34--35; Parikh--Boyd, Sections 2.5/3.2, pp.133--134,137--138; Yu--Zhou (2008), definition and Theorem 2.1, pp.576--577 (statement-level scope screen only). Precise links, qualifications and reading boundaries follow.
COMPARISON: Moreau covers real Hilbert cone projections but gives no n-dependent separation. The NNLS margin is a design hypothesis to establish, not a consequence of coefficient positivity. Positive polynomial coefficients on a real interval and Biro's integer pure-power sums do not supply the exact rational estimate. L672's phased unrestricted interpolant and L647's different growing-residue, zero-relative-rate example do not decide this affine nonnegative cone. No target theorem or countersequence is imported.
GAP: Establish or refute the exact rate-1/100 sign-constrained distance, with no mass cap and uniformity in every allowed displacement. A quantitative separating functional, an evaluated applicable margin, or a complete nonnegative asymptotic approximation remains missing. Qualitative projection and finite nonsingularity do not fill that gap.
REASON: Essential bounded theorem-level comparison is complete for one family-specific sign-sensitive attempt on unchanged TARGET; no necessary source is blocked. EXPLORE permits that later test without assuming its outcome or a new general cone theorem. This newly completed assessment is left for separate next-invocation approval before mathematics.
LITERATURE_REASON: The coefficient set changes from a complex linear span to an affine real nonnegative cone with a fixed anchor coefficient and no mass cap. A theorem-level comparison for positive-coefficient rational noncancellation and quantitative cone separation is needed; existing ready targets are not being reopened by another generic search.
SCOPE: Exactly TARGET and the full L666 family below; one bounded sign-sensitive rational/cone proof attempt or a nonnegative-coefficient asymptotic witness, retaining continuous angular L2 and all factors. Moreau is a named theorem to cite within its hypotheses; quantitative application, sign orientation, norm costs, any exact finite representation and Jensen applicability require proof. No positive-real/kernel identification, mass cap, exponential replacement, favorable Gram spectrum or positivity of cross terms is preapproved.

## Exact proposed scope and downstream use

Use exactly L666: q>=1, n=12q+3, M=4q+1, x=-5/4, R=11/8,
U=121/64, h=27/(10n), t_j=j/n for every 0<=j<n, and

    Z_e={x} union {x+i*h*(r+1/2+e_r): -2q<=r<2q},
    e_r real, |e_r|<=1/8,
    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),                  |u|=1.

The same displacement vector and the same real coefficients b_a>=0
must serve every angle. The infimum permits unbounded coefficients;
no normalization of their sum, symmetry or attainment is assumed.
The coefficient of W_x=1 is fixed at one. All original residues in
L666's G remain one; b_a are auxiliary comparison coefficients only.
Normalized angular L2, the j=0 factor and denominator angle 1/u are
retained. Use -log(0)=+infinity if needed in the discriminator.

The intended application is the choice b_a=1, then the existing c_0
and full-spatial Jensen interpretation. That application must be
justified in a later approved mathematical turn; no H estimate is
proved here. H, other spatial moments, general support, Xi realization
and actual mixed signs remain independent gaps.

## Preserved review requirements

Check the exact statement, standard terminology and stronger results
for positive-coefficient rational sums and distance to real convex cones
in a complex Hilbert space. Retrieve primary hypotheses and essential
proof cases for any proposed quantitative separation result. Qualitative
separation or finite-dimensional closedness alone does not evaluate the
required rate. Distinguish a theorem for exponential sums, a mass-capped
cone or positive kernels from this exact rational family. Reuse relevant
ready source readings when their actual hypotheses match.

Compare the recorded positive-mass angular-propagation assessment and
L647's qualified cluster stop, the exhausted scalar-sampling derivative
route, and L672's explicit interpolation coefficients. Do not assume
that a real part, conjugation or coefficient rescaling preserves the
complete angular approximation error. The scalar route was parked after
two unproductive attempts; merely writing its Gram form or repeating
its diagonal deformation bound does not reopen it. The new test must
use the specified sign constraint in a quantitatively discriminating way.
L670/L671's clearing stops and L669's fixed-angle stop remain intact.

Continuation threshold, if coverage later becomes ready: a uniform
rate-1/100 bound with absolute C/onset, or a full admissible sequence
with nonnegative coefficients and a rigorous continuous angular upper
error making the stated loss unbounded. A sampled conic optimization,
finite nonsingularity or the old unrestricted complex interpolant alone
does not pass. If a known result or matching countersequence already
decides this cone, import it with its exact hypotheses instead of
reproving it; if the scope is merely a duplicate, stop the nomination.

Essential continuation inputs: L666's exact family and L672's audited
obstruction; the other named local results are comparisons to inspect,
not assumed inputs. No full matching Mathlib coverage has been checked.
No new lemma or calculation accompanies this completed source comparison.
The newly ready assessment receives separate approval before research under
the supervisor's gate. The nomination above is retained as scope, not a result.

## Completed source comparison — 2 November 2026, step 37

### Primary cone theorem and its proof cases

J.-J. Moreau, *Proximité et dualité dans un espace hilbertien*,
Bulletin de la Société Mathématique de France 93 (1965), 273--299,
[original paper](https://www.numdam.org/article/BSMF_1965__93__273_0.pdf),
[DOI](https://doi.org/10.24033/bsmf.1625).
Read Sections 1.a, 3.a/d, Proposition 4.a with both proof directions,
and Corollary 4.b, pp.273,278--281. For mutually polar closed convex cones
P,Q in a real Hilbert space, z=x+y with x in P, y in Q and (x,y)=0
is equivalent to x=proj_P(z), y=proj_Q(z). Section 1.a explicitly allows
a complex Hilbert space through its underlying real structure. Proposition
4.a's forward proof uses conjugacy and a quadratic minimum; its converse
uses convex interpolation and a parameter tending to zero. Section 4.b
uses cone indicators. Projection existence is established in 3.a.
This supplies no quantitative rate. Any family-specific use must retain
the real inner product, closedness hypotheses and polar sign convention.
No target projection or separator is evaluated here.

N. Parikh and S. Boyd, *Proximal Algorithms*, Foundations and Trends in
Optimization 1(3), 123--231, author PDF bearing 2013,
[Sections 2.5/3.2](https://web.stanford.edu/~boyd/papers/pdf/prox_algs.pdf),
pp.133--134,137--138. Read the decomposition (2.4), negative-polar
definition, and resolvent (3.4) with its proof. The source assumes closed
proper convex functions; the cone case assumes a closed convex cone.
It corroborates the polar sign convention and characterizes projections,
without a lower margin. Its resolvent proof states a convenience
subdifferentiability assumption. The original Moreau paper, rather than
that convenient proof, is the available named-theorem input.

### Quantitative NNLS geometry: the margin is an extra hypothesis

M. Slawski and M. Hein, *Non-negative least squares for high-dimensional
linear models: consistency and sparse recovery without regularization*,
Electronic Journal of Statistics 7 (2013), 3004--3056,
[arXiv:1205.0953v2, 12 February 2014](https://arxiv.org/pdf/1205.0953v2),
[DOI](https://doi.org/10.1214/13-EJS868).
Read column normalization, Sections 2.1--2.3, Condition 1,
Proposition 1 and its complete Appendix B proof, preprint pp.4--6,34--35.
For real X with squared column norms equal to the row count N,
(2.2)--(2.3) identify the maximal unit-normal separating margin tau_0
with dist(0,conv{X_j/sqrt(N)}). Condition 1 requires a positive uniform
lower bound on tau_0. Proposition 1 assumes that condition and independent
zero-mean finite-variance noise. Appendix B projects along a separating
normal, rescales columns and controls the stochastic remainder; the
margin is assumed at its first step. No statistical conclusion is imported.
The source concerns a normalized convex hull, while TARGET fixes one
anchor coefficient and leaves auxiliary mass unbounded. No conversion
with controlled normalization or evaluated margin has been established.

### Positive-coefficient terminology and reused mass-sensitive sources

D. Yu and S. Zhou, *An inequality for polynomials with positive coefficients
and applications in rational approximation*, J. Mathematical Inequalities
2(4) (2008), 575--585,
[publisher PDF](https://files.ele-math.com/articles/jmi-02-52.pdf).
Screened the definition of Pi_n(+) on p.576 and Theorem 2.1 on p.577:
the coefficient basis is x^k(1-x)^l on [0,1], and the theorem constructs
a positive polynomial denominator for prescribed real zeros. Those
hypotheses/conclusions do not match a nonnegative combination of prescribed
complex angular rational functions. No proof or application is imported;
its full proof was not read.

Reuse `2026-11-02-positive-mass-angular-propagation.md`, including its
inspected Biro theorem (p.344), Newton--Girard proof portions and the
Friedland--Yomdin propagation comparison. Biro's fixed-anchor pure powers
have positive integer multiplicities; the present b_a are arbitrary
nonnegative reals and the W_a retain rational angle dependence. Neither
integer repetition nor positive original residues removes those weights.
The earlier review already leaves the exact full-sum transfer open.
No stronger conclusion for this cone is supplied by that assessment.

Reuse `2026-11-02-displaced-angular-anchor-distance.md`: the inspected
Bultheel--Cruz-Barroso--Lasarow space representation and Fricain kernel
criterion do not identify a positive cone or evaluate its distance.
They need not be browsed again. Exact rational quadrature is available
with the qualifications in the reused sampling assessment, but it does
not establish coercivity of its signed samples.

### Duplicates and recorded failures

Read L666's hypotheses/conclusion and Section 4, plus Section 6's setup
and final insufficiency calculation; L672's hypotheses/conclusion,
Sections 1--2 and 5; L647's hypotheses/conclusion, Sections 1,3--4,6--7;
and the scalar, entrywise-Gram and joint-angular failure records.
These are scope comparisons, not fresh audits of unaudited local proofs.

L672 gives a residual 1-sum lambda_a W_a. Its explicit formula (4)
has interpolation factors and complex phases, and asserts no condition
lambda_a=-b_a with real b_a>=0. Neither conjugate pairing nor taking real
parts is a supplied error-preserving conversion to that constraint.
Thus its audited upper distance bound cannot be imported as a cone witness.
No conversion has been proved or excluded here.

L647 cancels near maximizers using positive coefficients, but its poles
and growing integer residues are different from the complete prescribed
L666 displacement grid. Its relative loss has zero exponential rate and
its absolute response grows exponentially. It does not give the required
nonnegative angular approximant with small absolute error. In particular,
positivity alone cannot be cited as a reason to drop cross terms: the
entrywise-Gram failure record already warns against that shortcut.

The scalar-sampling route has two recorded unproductive attempts; its
absolute derivative fallback remains parked. The cone target must use
the sign constraint in a discriminating way. Rewriting a Gram minimum,
repeating the diagonal deformation bound or assuming a favorable cone
angle would not do so. The spatial joint-moment screen supplies no
certified asymptotic witness. L669--L671's recorded stops remain intact;
they were not independently re-audited in this source review.

### Search record, access and reading boundaries

Queries included `"positive coefficients" "rational functions" lower bound
norm cancellation`, `"positive linear combinations" rational functions cone
approximation noncancellation`, `Moreau decomposition projection polar cone
nonnegative least squares Boyd pdf`, `Slawski Hein non-negative least squares
self regularizing tau convex hull 2013 pdf`, `"rational functions" "positive
residues" noncancellation norm`, `"positive coefficients" "rational
approximation" lower bounds cone`, `"rational functions" "nonnegative"
"distance" "cone" approximation unit circle`, `"Blaschke" "positive
coefficients" "sum" lower bound`, and `"rational functions" "positive
residues" "norm" lower bound`. The primary Moreau paper was located by
`Moreau 1965 Proximité dualité espace hilbertien numdam décomposition théorème
1962 pdf`. None of the search snippets is theorem evidence.

Soltan, arXiv:1810.04206v1, Theorem 1.1 and its Moreau bibliography were
screened before retrieving the original 1965 proof; its later theorems are
not inputs. Moreau's separate 1962 note is cited by that original paper
but was not retrieved; it is not an essential blocker. Positive-real,
Stieltjes, de Bruijn--Springer and older Borwein restricted-rational
results remain uninspected leads, not matching theorems or dependencies.
No identity placing W_a in those classes is assumed. No source blocker
prevents the exact-family test using the material actually inspected.
Text retrieval succeeded. PDF screenshot requests supplied no usable
images; the relevant text was read, and Moreau's polar convention was
cross-checked against the clear Parikh--Boyd formula.

### Decision, quantitative test and continuation inputs

DECISION is EXPLORE: bounded source comparison has not found an evaluated
uniform bound or an admissible nonnegative countersequence for TARGET.
This is coverage for a later attempt, not evidence that the target is true,
false or original. No family-specific duality formula, new inequality,
coefficient transformation or mathematical script was produced this turn.

After separate approval, test exactly TARGET with L666's complete family
and L672's audited complex-span obstruction as essential starting inputs.
A sign-sensitive dual approach must justify its real polar orientation,
anchor action and entire norm uniformly in displacements; a primal approach
must supply admissible, angle-independent nonnegative coefficients and a
continuous asymptotic error estimate. Moreau may be cited within its
hypotheses, but no general projection theorem needs reproof. The missing
work is quantitative and family-specific. Additional source-dependent
theorems outside this assessed scope require a new gate.

Continue on a proved absolute-C/onset rate-1/100 bound, a complete
countersequence passing the stated logarithmic discriminator, or a concrete
intermediate identity with a separately bounded decisive cost. Abandon
this sufficient cone mechanism on a certified countersequence; park a
proposed dual/representation subroute if its fully paid cost demonstrably
misses the threshold. A finite optimizer, qualitative separator, positive
distance for each n, or the old complex interpolant alone is inconclusive.

The intended b_a=1 application to c_0 and the existing full-spatial Jensen
bridge still needs its applicability argument. No H bound, uniform onset,
Xi realization or mixed-sign conclusion is assumed. Full matching Mathlib
coverage for TARGET or the source theorems was not checked; supporting
Hilbert projection results would not evaluate this quantitative distance.
