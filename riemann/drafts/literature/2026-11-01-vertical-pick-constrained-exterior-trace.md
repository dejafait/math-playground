# Vertical Pick block — constrained signed exterior trace source assessment

TARGET: Test whether the signed exterior-zero trace on L641's local-zero interpolation nullspace is o(ell_X dim U_T) along suitable heights, retaining the complete zero tail and using the constraint-sensitive orthogonal projection.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the ready zero-expansion/count/concentration assessment; searched constrained RKHS projections, Moore--Penrose inverses, finite model-space operator/Clark representations, rational quadrature and zeta-zero signed traces. Inspected primary theorem statements and relevant proof cases below; no matching constrained actual-Xi asymptotic was identified. This is a bounded comparison, not an absence or novelty theorem.
SOURCE_EVIDENCE: Penrose (1955), Theorem 1 and proof, pp.406--407, following generalized-inverse lemma/proof p.408; Cima--Ross--Wogen, author manuscript, Section 1, Theorems 1.4/1.18, Section 2 proof and Section 3 Lemma 3.1/Theorem 1.18 proof. Reused Suzuki 2206.03682v4 Section 2.2/(2.6), Bellotti--Wong 2412.15470v2 Theorem 1.1, and the model-space/spectral sources inspected in the prior concentration assessment.
COMPARISON: Standard finite complex linear algebra and rational kernels provide machinery for a projection formula with dependent constraints; boundary Toeplitz/Clark representations and the assessed Szego limit do not give the signed exterior-zero trace on E_N intersect ker(evaluations). No inspected theorem supplies the required moving-grid, zero-dependent, full-tail little-o estimate. L641's unconstrained exterior test pair does not decide this target.
GAP: Write the actual constrained projection inside E_N with rank-deficient evaluations allowed, justify its mixed complex-evaluation trace and complete-tail interchange, then prove or quantitatively obstruct |trace|=o(ell_X dim U_T) at admissible heights. Fixed-family convergence, boundary leakage and unconstrained trace bounds do not meet this scale.
REASON: The separate literature-only comparison leaves a precise quantitative constrained-trace test, with standard machinery accessible and no essential source blocker. One bounded research attempt is approved on the unchanged target; the projection computation alone is reproduction and is not the sought advance.
SCOPE: Exact L640 distinct grid/full C and K, N=floor(log T), L641's E_N and actual local evaluation nullspace U_T; finite spectral theory, rank-deficient orthogonal projections and rational kernel estimates with explicit applicability arguments. Retain both half-planes, multiplicities and the infinite exterior tail; no RH, simplicity, positive zero measure, nested grid or theorem about arbitrary configurations is assumed.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED identified a changed projection/trace scope not covered by the ready concentration assessment; this turn supplies that comparison. No unchanged-target source refresh or quota browsing is proposed.

## Completed review — 1 November 2026

This turn is LITERATURE, EXPLORATION, NOVELTY_UNCHECKED. It establishes
source coverage for an attempt, not a new lemma, trace bound or RH result.
No lemmas or mathematical scripts were changed. The original nomination
below is retained, with this completed assessment controlling its gate.

### Standard projection input and remaining specialization

R. Penrose, *A generalized inverse for matrices*, Proc. Cambridge Philos.
Soc. **51** (1955), 406--413,
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/5F4516D6B9989BB6563A4B267CC7D615/S0305004100030401a.pdf/div-class-title-a-generalized-inverse-for-matrices-div.pdf),
Theorem 1, pp.406--407, treats arbitrary complex rectangular matrices:
there is a unique X satisfying AXA=A, XAX=X, (AX)*=AX and (XA)*=XA.
Read the full existence/uniqueness proof, including its zero/singular
case, and p.408's following lemma/proof and unitary-diagonal computation.
These supply the finite generalized-inverse machinery without assuming
independent evaluation rows. The extraction garbles some starred symbols;
no unparsed numbered identity is imported. No condition-number or
growing-dimension estimate is supplied by this citation.

The next attempt must choose orthonormal coordinates in **E_N**, form
the actual evaluation map there, and justify the nullspace projection
and its kernel. This is a necessary specialization of known finite
linear algebra, not a new projection theorem. Projection in H_N followed
by projection in E_N is not licensed as the intersection projection.
Local repeated zeros impose repeated value constraints, not automatic
derivative constraints; dependence must not be removed by an unjustified
inverse. Complex evaluations are legitimate finite rational functionals
away from the prescribed poles; their growth with N still needs bounds.

### Model-space representations and their domain of applicability

J. A. Cima, W. T. Ross and W. R. Wogen, *Truncated Toeplitz operators on
finite dimensional spaces*, Operators and Matrices **2** (2008), 357--369,
[author manuscript](https://facultystaff.richmond.edu/~wross/pdf/truncated-revised.pdf),
Section 1, Theorems 1.4 and 1.18, and proofs in Sections 2--3 (manuscript
pp.5--8) were inspected. For finite Blaschke B, the first characterizes
truncated Toeplitz matrices in the kernel basis when B's zeros are
distinct. Its proof uses rank-one kernel representations, partial
fractions and a dimension comparison. The second expresses each
truncated Toeplitz operator with L2 boundary symbol as p(U_alpha)+q(U_beta)
for distinct unimodular alpha,beta and polynomials of degree at most n.
Read Lemma 3.1 and its proof and the boundary-kernel spectral proof of
Theorem 1.18. This is a boundary-operator representation, not a bound
on coefficients or an arbitrary compression to a zero-nullspace.
Membership of our signed operator or its compression in that class
would need a proof; Clark boundary nodes are not the actual complex
Xi zeros. The source provides no quantitative cancellation for them.

Reuse the exact source evidence in
[the concentration assessment](2026-11-01-vertical-pick-zero-count-concentration.md):
Baranov--Zarouf 1310.1182v1 Section 1.1 and
Baranov--Jaming--Kellay--Speckbacher 2304.02385v2 Section 3.1 give the
finite rational kernels; the latter's Theorem 5.1 assumes a **positive
Borel measure on the real boundary**. Its proof was already inspected.
It is not a signed complex-zero sampling theorem. Miheisi--O'Loughlin
2404.03087v1 Theorem 2.1 and Sections 4.1--4.2 cover normalized traces
of boundary-symbol truncated Toeplitz operators for products built from
one nested zero sequence. The saved proof comparison includes its
symbol approximation and trace-norm defect cases. Neither its domain
nor its regularity assumptions automatically extend to this
zero-dependent intersection and moving triangular grid. Reuse is
adequate for this distinction; these sources were not browsed again.

### Signed zeros, tail and duplicate/failure comparison

Reuse Suzuki 2206.03682v4 Section 2.2/(2.6), with the complete compensated
expansion proof and the previously assessed complex-bilinear versus
modulus-square distinction. It supplies a convergent zero expansion;
it does not assert the proposed constrained trace asymptotic. The full
pair expression is locally written in L641 (1)/(6); its separate audit
remains open. Bellotti--Wong v2 Theorem 1.1 and audited L467 supply all-zero
counts with multiplicity/endpoints. They do not select a height favorable
for both the local count and a signed exterior trace.

Read L641 in full, L640's definitions/conclusions, the prior assessment's
source/failure comparisons and the precise boundary-transfer attempt
record. The arithmetic reductions in L640 remain parked; their full
proofs were unnecessary for this review. L641's test pair is not an
asserted Xi pair, and its countervectors need not lie in U_T. Thus it is
neither a constrained trace counterexample nor grounds for reapproving
generic boundary transfer. No duplicate constrained-trace result was
found in the scoped local vertical-block search. No other notebook was
read; no cross-notebook input is used.

### Search record, unread leads and access qualifications

Queries included `reproducing kernel Hilbert space vanishing interpolation
orthogonal projection kernel Moore Penrose inverse`, `finite model space
compressed multiplication trace formula zeros rational functions truncated
Toeplitz trace`, `Penrose 1955 generalized inverse matrices original pdf`,
`rational quadrature reproducing kernel complex nodes signed measure model
spaces trace`, and exact combinations of zeta, zeros, constrained trace,
interpolation and model space. Broad searches returned substantial
irrelevant material; search snippets were not treated as theorem evidence.
No exact matching asymptotic was identified in this bounded review;
originality and exhaustive coverage are not claimed.

Aronszajn (1950), *Theory of reproducing kernels*, subspace/restriction
kernel theory, was an additional lead. AMS returned 403; the Wisconsin
copy exposed no readable lines and screenshot calls yielded no readable
page, while another mirror timed out. A local download also failed DNS.
Only an indexed passage was visible: this lead is **not fully inspected
and not imported**. It is nonessential here because finite coordinates
and Penrose's inspected theorem suffice for the proposed projection
computation. The inaccessible duplicate is not an essential source
blocker. No retry of it is a prerequisite for research. Full matching
Mathlib coverage is unchecked, not asserted absent.

### Bounded attempt licensed by this assessment

Keep the exact saved TARGET. First specialize the known projection
machinery to U_T, retaining the E_N restriction, dependent constraints
and conjugations. Then test the **signed** complete exterior trace,
with fixed-family convergence distinguished from the uniform bounds
needed as N and X grow. Every truncation must include a proved remainder
for both signs of the ordinates, off-real conjugate pairs and multiplicity.
Do not replace a mixed evaluation by a modulus square or import positivity.

The required absolute trace scale is o(ell_X dim U_T), along heights
meeting L641's local-count condition; obtaining just an exact formula,
a small boundary integral or an unconstrained trace does not pass.
Continue with a quantitative cancellation mechanism meeting that scale,
or an informative obstruction that respects the actual constraints.
If only the old arithmetic majorant or the old test pair remains,
record no advance and park this mechanism rather than repeat the reduction.

The proposed use is a small normalized **Rayleigh quotient**, to test a
fixed reserve below one in the full normalized Gram diagnostic. It does
not by itself assert a near-zero eigenvalue, a negative eigenvalue or
RH. Its exact finite Hermitian application must be justified in research.
Even success leaves global initial signs and other realization gaps open.

## Concrete proposed test

Use the same C, K, ell_X, N=floor(log T), X in [T,2T] as L640 and
the actual Xi normalization of L018. L641 constructs, at suitable X,
U_T by intersecting the high boundary-concentration eigenspace with
the kernels of evaluations at **all** local Xi zeros in
|Re(zeta)-(X+1/2)|<=1. Its dimension is linear in N. Its separate
critical audit remains open. No critical-line-only replacement,
simplicity assumption or sign of the zero-pair form is permitted.

The proposed bounded test is the signed trace, on this finite subspace,
of the exterior part of K's exact zero-pair form. The target is an
absolute o(ell_X dim U_T) bound along a sequence of admissible heights.
Such a trace bound could supply a small normalized Rayleigh quotient
by finite Hermitian spectral reasoning. Neither the trace identity in
the desired projection coordinates nor its asymptotic is established
here. The full exterior set includes off-line zeros, negative ordinates,
multiplicities and arbitrarily distant zeros.

This continuation is independently testable: derive the exact
constraint-sensitive kernel and bound or obstruct its full signed
trace. It is not another assertion that boundary leakage controls
complex evaluations. L641's countervectors have not been shown to
lie in U_T, so they do not answer this test. Conversely its dimension
surplus and the existing kernel trace on the *unconstrained* space do
not supply the desired constrained estimate.

The source review should first compare precise projection/interpolation
theorem hypotheses and relevant proof cases with this finite rational
family, then check whether a known signed trace or quadrature identity
already supplies or obstructs the target. Reuse the prior zero-count
and logarithmic-derivative coverage. Standard finite linear algebra is
available, but no source may be used to assume RH, positivity or a
uniform bound outside its domain. Full matching Mathlib coverage is
unchecked. No cross-notebook input is proposed.

Continue only if the comparison leaves a quantitative, independently
testable constrained-trace inequality; otherwise choose a different
mechanism. Global initial signs, arbitrary configurations and boundary
transfer remain unresolved even if this fixed-family witness succeeds.
