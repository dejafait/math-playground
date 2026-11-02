# Three-moment contour transfer — completed source comparison

TARGET: Assess the exact n-dependence of the boundary residual certificate obtained by transferring C645e's three moments through a zero-avoiding residue contour on |z|=R.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the parent residue and finite-Blaschke assessments; checked C645d/C645e statements, the scalar stop, C645b's envelope stop and C645c's qualification. Searched contour interpolation remainders and inverse-Blaschke weighted moments; inspected the exact primary statements and relevant proofs below. No novelty claim follows from the bounded search.
SOURCE_EVIDENCE: Beck et al., A First Course in Complex Analysis, Theorems 8.1.5/8.1.7 and 6.2.18/6.2.19 with proofs; Zakeri, author Notes and Comments, Section 8.3 after Example 8.33; Calvi, Lectures on Multivariate Polynomial Interpolation (2005), Theorems 1.17/1.18 and Section 4.4 proof, printed pp.20–22; NIST DLMF 1.2.8, (3.3.1)/(3.3.6); Bello Hernandez–de la Calle Ysern, arXiv:1211.5573v1, Section 2.3 and complete Lemma 2.3 proof, pp.5–8; Austin–Kravanja–Trefethen revised manuscript, Sections 3.2/4.3. URLs and applicability below.
COMPARISON: Standard residue calculus and ML bounds cover the analytic tools for a synthetic weighted contour specialization. Hermite and multipoint Pade bounds concern constrained approximants and cannot remove an arbitrary holomorphic P from the boundary integral. The exact grid cancellation and n-dependent cost of combining these tools with C645e remain a separate calculation.
GAP: Derive the full weighted identity under the stipulated complete pole census and interpolation, verify all grid removals and rational-factor poles, and evaluate the polynomial-weight cost with the exact anchor factor. No inspected source supplies an actual-Xi boundary upper bound or a complete detector.
REASON: Essential source coverage is complete for the bounded synthetic specialization, permitting a subsequent calculation after separate continuation approval. Reprove neither residue calculus nor Hermite/Pade theory; justify only the local rational factors, interpolation cancellations, normalization and weight norm.
LITERATURE_REASON: The new target introduced polynomial-weight boundary norms and grid cancellation outside C645e's ready finite-family scope. This turn inspected those missing source cases; unchanged follow-up browsing is unnecessary apart from separate approval of the newly written continuation.
SCOPE: The exact TARGET and the COVERED_TARGET below retain the invocation-start synthetic hypotheses. SPECIALIZE covers only the explicit contour/weight calculation; no enlarged cluster, weakened boundary regularity, actual-Xi pole census or height-uniform norm is covered.
COVERED_TARGET: Derive C645e's synthetic boundary residual certificate with every grid term and the exact n-dependent polynomial-weight cost.

## Invocation-start nomination retained

The pending-source instructions below record the original scope. The
completed comparison following them supersedes their pending status;
no synthetic contour estimate was derived in this literature turn.

## Proposed bounded scope, not a proved claim

Retain C645e (1)--(3), including fixed delta in (0,1/2), n>=5,
the exact complex B_n, anchor x and at most two additional distinct
unit-residue poles in Z. For this synthetic test only, take F
meromorphic on a neighborhood of the closed disk |z|<=R, with precisely
the poles Z there, all simple and of residue one. Take P holomorphic
on such a neighborhood with P(it_j)=F(it_j) for every grid node.
Thus contour regularity and a complete enclosed-pole list are
explicit hypotheses to review, not claims about Xi. Do not add a
derivative lower bound or silently discard grid residues. Record what
boundary regularity could be weakened only if the literature covers it.

The question is what quantitative boundary residual information about
F-P these three moments actually yield, with all dependence on n,
delta and the polynomial weights visible. A possible later application
to a positive-real interpolant and actual Xi would still need its
own pole census, multiplicity treatment, contour clearance and
height-uniform boundary control. None is assumed established.

Essential local inputs for the source comparison are the audited C645e,
C645d's definitions, and the residue/boundary hypotheses in
`drafts/literature/2026-11-01-derivative-free-pick-contour-detector.md`.
Retrieve the precise primary residue theorem and relevant contour
moment cases from its recorded sources, then compare with standard
meromorphic interpolation remainder bounds. Reuse actual inspected
coverage; search only the missing polynomial-weight/n-dependent part.
Check the existing scalar, normalization and envelope stops before
approving a quantitative target. No cross-notebook input is proposed.

Continuation test: approve only an exact, source-compared boundary
norm target retaining every grid and pole term. A result that merely
rephrases the finite moment bound must identify its explicit cost and
why that cost could help a later detector. If the available theorem
requires an unproved separation, boundary norm or pole census, retain
that gap rather than claiming a certificate for actual Xi. This pending
assessment contains no new mathematical derivation. Mathlib coverage
for the changed target is not checked.

## Completed comparison — 1 November 2026

### Relevance and exact scope

Main gap: actual-Xi signs at unbounded heights/all-degree mixed positivity.
The intermediate target is the saved TARGET. A boundary certificate
could turn C645e's vector noncancellation into a necessary residual size,
avoiding evaluation through a small derivative at a pole. A later
contradiction still needs an independent upper bound below that size,
plus the actual pole census, multiplicities, realization and clearance.
This review establishes source coverage, not that certificate or an RH
advance beyond the sources.

Retain precisely C645e (1)–(3): fixed 0<delta<1/2,
d=3/2-delta, R=3/2-delta/2, x=-d, n>=5, t_j=j/n and the exact
complex B_n. The set Z has at most three distinct unit-residue points,
contains x and satisfies its stated small-cluster conditions. F is
meromorphic on a neighborhood of the closed disk, with exactly these
poles there; P is holomorphic on such a neighborhood, may depend on n,
and matches F at every it_j. No PSD, derivative lower bound, symmetry,
pole separation or actual-Xi assertion is added.

### Standard calculus to import, with all singularities retained

M. Beck et al., *A First Course in Complex Analysis*, online unversioned
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html),
accessed 1 November 2026. Read both statements and proofs. The residue
theorem assumes a simple positively oriented closed contour in a
simply connected domain, analyticity on the contour and analyticity
inside except for finitely many isolated singularities. Its integral
is 2pi i times the sum of **all** enclosed residues. The simple-pole
rule is the limit of (z-a)h(z); the higher-order rule retains derivatives
of the pole-cleared integrand. Removable singularities have zero residue.
These are imported standard theorems. No local grid cancellation follows
just from naming the theorem: it must be verified for the chosen h.

The same text, [Section 6.2, Theorems 6.2.18 and 6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html),
with complete proofs, gives the absolute integral inequality and the
ML bound |integral_C h dz|<=length(C) sup_C|h| for continuous h on a
contour. The proof retains the integrand's entire modulus. It has no
sample-count parameter or interpolation-dependent constant. Thus any
n-dependence in a later use must be exhibited in its chosen integrand
and multiplier norm; the theorem itself supplies no residual upper bound.

S. Zakeri, *A Course in Complex Analysis*, unversioned author
[Notes and Comments, Section 8.3, after Example 8.33](https://zakerimath.com/CAbook/COM.html),
accessed 1 November 2026. Reused the ready finite-division coverage and
checked its complete argument. Dividing a bounded disk-holomorphic
function by a finite Blaschke product of its zeros removes those zeros;
the proof uses boundary modulus one and the maximum principle. This
does not make a meromorphic residual holomorphic at its genuine poles.
Only local removal at the grid and the finite product's circle modulus
are relevant here. The disk rescaling and rational denominators still
need a local applicability check in the calculation. No weaker boundary
regularity is approved: retain the closed-disk neighborhood hypotheses.

### Interpolation remainder comparison and its restrictions

J.-P. Calvi, *Lectures on Multivariate Polynomial Interpolation*, Hanoi,
summer 2005, [author PDF](https://www.math.univ-toulouse.fr/~calvi/res_fichiers/MPI.pdf),
Chapter 1, Sections 4.1–4.4, printed pp.20–22 (PDF pp.20–22).
Read Theorems 1.17 and 1.18 with their proof arguments and the complete
contour estimate in Theorem 1.19. Hermite's remainder formula (1.39)
assumes f holomorphic in a simply connected domain, with a piecewise
C^1 contour winding once positively about the nodes and evaluation
point. The approximant is the specified Lagrange–Hermite polynomial.
The remainder contains a ratio of nodal products and a Cauchy kernel.
The Section 4.4 estimate explicitly retains contour length, boundary
norm and geometric distance factors. It is not a theorem for arbitrary
holomorphic interpolating P or a meromorphic f without pole terms.

NIST DLMF, version 1.2.8 (15 September 2026),
[Section 3.3(i), (3.3.1) and (3.3.6)](https://dlmf.nist.gov/3.3#i),
confirms the unique polynomial degree bound and analytic-domain
hypotheses of this formula. Neither statement identifies P here with
that polynomial. Merely sharing n values is insufficient for such an
identification. This is source comparison, not a reproof of Hermite's
formula or a proposed import of its error bound into the Xi argument.

M. Bello Hernandez and B. de la Calle Ysern, *Meromorphic continuation
of functions and arbitrary distribution of interpolation points*,
[arXiv:1211.5573v1](https://arxiv.org/pdf/1211.5573v1), 23 November 2012,
Section 2.3, Theorem 2.2 and complete Lemma 2.3 proof, pp.5–8.
Checked the prescribed numerator/denominator degrees, weak convergence
of node measures, pole-exclusion sets and contour choice. The proof
clears all poles; its subtraction integral vanishes using behavior at
infinity provided by those degree bounds. Estimate (12) has the factor
n^(2m), a nodal-polynomial ratio and a constant depending on the fixed
function, compact set, exclusion and contour parameters. This factor
is not a universal contour-moment penalty and must not be attached to
our arbitrary P. Nor may that proof's vanished integral be silently
dropped here. The result is a comparison, not an imported bound.

A. P. Austin, P. Kravanja and L. N. Trefethen, *Numerical algorithms
based on analytic function values at roots of unity*, SIAM J. Numer.
Anal. 52 (2014), 1795–1821,
[author revised manuscript](https://people.maths.ox.ac.uk/trefethen/austin_kravanja_trefethen_revised.pdf),
Sections 3.2 and 4.3, manuscript pp.14–17. Rechecked (3.9) and the
complete equivalence argument (4.1)–(4.2). The derivative-free 1/f
moment identity still has weights 1/f'(w_j) at simple roots. The later
discrete contour identities concern roots-of-unity samples and use
degree constraints; their bilinear form lacks positive definiteness
and conjugate symmetry. They supply no positive residual certificate
on this interior vertical grid. No numerical quadrature or algorithmic
error estimate is being imported.

### Bounded specialization now covered, but not executed

For the separate calculation, use the proposed weighted integrands

    H_(n,k)(z) = B_n(x) [n(z-x)]^k (F(z)-P(z))/B_n(z), k=0,1,2.

For k=0 the weight is identically one. This line specifies the objects
to test; no contour identity for them is proved in this review. The
calculation must inspect every it_j, every point of Z, every rational
factor denominator and the circle itself. First display any grid terms,
then justify their removal from interpolation and the local zero orders.
Retain F-P on the boundary; do not discard P by an unassumed degree or
condition at infinity. Do not replace B_n by its modulus inside residues.

The certificate sought concerns E_n=max_(|z|=R)|F(z)-P(z)|. It must
evaluate the cost of all three polynomial weights, the contour
normalization and the exact |B_n(x)| factor explicitly, so that its
threshold can be compared with a later proposed upper bound. Test
whether the polynomial-weight loss is at most quadratic in n for
fixed delta after retaining that exact factor. This is a proposed
threshold, **not an established estimate**. An unevaluated multiplier
norm or a restatement of C645e alone does not complete the target.
No sharpness or optimality claim is required.

Continue if a complete synthetic identity and quantitative cost can
be established under precisely these hypotheses. If an additional
grid term, boundary singularity or uncontrolled factor survives,
record it and stop the proposed certificate rather than removing it
by assumption. Even a successful synthetic bound warrants no Xi
transfer without new coverage for the separate realization/control
gaps. This is routine specialization of named theorems, not a new
central mechanism or a claim of originality. Full matching Mathlib
coverage remains unchecked; no formalization input is used.

### Search, duplicate and failure record

The local scoped search covered the named Pick/contour/Blaschke
assessments and their relevant histories/stops. It found the explicit
deferred weighted-boundary gap, not a completed local certificate.
C645d's scalar exact cancellation and C645b's factorwise-envelope stop
remain in force in their stated scopes. C645c improves only its rate
benchmark; its derivative-direction qualification is retained. The
new vector transfer is not a repetition of the stopped scalar premise.
No cross-notebook theorem is used. The parent assessment's selected-
height Gonek estimate is reused only as an already recorded limitation:
it does not certify this prescribed circle for Xi. No fresh zeta
estimate or zero-free region is proposed, so the parked arithmetic
routes and their external-input baseline are not reopened.

Queries: `interpolation Hermite contour integral remainder formula
meromorphic polynomial omega bound`; `site.complexanalysis.org
estimation lemma contour integral removable singularity theorem`;
`finite Blaschke product modulus one circle interpolation remainder
meromorphic contour integral`; `"Blaschke" "residue" "interpolation"
"error" contour moments`; `meromorphic interpolation residual
polynomial weighted contour moments boundary norm finite Blaschke`.
Search results beyond the inspected sources above remain unread leads,
including boundary interpolation and norm-constrained rational Pick
papers. No stronger applicable conclusion or novelty is inferred from
snippets. One guessed path-independence URL failed; it was nonessential
because the exact ML theorem and proof were accessible. There is no
persistent essential-source blocker.

Outcome: EXPLORATION, completed source scope with a concrete subsequent
specialization. No lemma, new mathematical result, mathematical script,
PROOF.md assembly change or DAG change was made. The newly recorded
COVERED_TARGET requires separate continuation approval before research.
