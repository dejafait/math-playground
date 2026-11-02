# Quantitative vertical Pick pole detection — source review

TARGET: Establish or obstruct an explicit n_0<=ceil(C_delta(1+log^+ H_rho)) forcing a negative eigenvalue of every vertical actual-Xi Pick matrix K_n(gamma) with n>=n_0, conditional on a specified simple off-line zero rho.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed signed-mechanism and growing-Pick assessments, checked L018/L258 and the specific fixed-reserve/Laguerre stop records, and searched exact quantitative pole/Pick/error terminology. Inspected primary finite interpolation, bounded zero-division and real-part growth statements with the relevant proof cases. No inspected source states this exact vertical-grid order bound; no novelty is inferred.
SOURCE_EVIDENCE: Bolotnikov, Operators and Matrices 4 (2010), 151–191, definitions (1.1)–(1.7) and full Theorem 1.1, pp.151–153; Zakeri, A Course in Complex Analysis, author Notes and Comments, Section 8.3, complete finite-Blaschke argument; Complex.borelCaratheodory and its full supporting proof at mathlib4 commit 0d3fb85496130669f472d62be6f25999ca085c59, lines 37–110. Reused Ball–Bolotnikov's scalar convention and the external qualitative overlap only.
COMPARISON: Standard finite PSD interpolation, bounded analytic zero division and Borel–Carathéodory cover the machinery, including singular finite data and interior norm control without a derivative lower bound. The remaining specialization is the explicit delta-only geometry, constants, strict threshold and every-n quantifier for the unchanged actual-Xi arrays. L258 is a different growth-dependent witness; external L-91904 is qualitative.
GAP: Derive or obstruct the nominated explicit threshold from these standard inputs, checking Cayley denominators, boundary data, all n and full completion. No inspected theorem establishes the threshold as stated, and no height-only bound for H_rho or actual matrix positivity is supplied.
REASON: Essential source coverage now supports a separate bounded specialization attempt. Cite the known tools rather than reprove them; prove only the array-specific applicability, quantitative constants and quantifiers. This completes the source gate, not the detector or any RH sign claim.
SCOPE: The exact TARGET and its stipulated simple-zero/local-growth hypotheses below are ready for a separate research turn. Allow the finite positive-real interpolation and bounded analytic residual/Blaschke implementation only. No finite actual-Xi negative index, truncated-zero replacement, height-only growth estimate, new positivity mechanism or RH implication beyond this conditional test is approved.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED nomination lacked essential analytic-error and finite-degenerate-case coverage. This turn supplies that coverage; reuse it for the unchanged next target without further browsing.

## Completed source comparison — 1 November 2026

The exact invocation-start target is unchanged. This is a literature-only
step: no detector estimate, constant or new lemma is proved here. Read
L018 and L258 completely and reused the completed post-C644a screen and
growing-vertical-Pick comparison. L258 is a different, already recorded
growth-dependent detector; C644a's fixed-reserve stop remains a contrast.

The essential source questions are resolved at the tool level below.
The UAB Nevanlinna–Pick notes timed out twice and their alternate host
failed; accessible primary sources replace that nonessential lead.
No access failure is being promoted to a mathematical obstruction.

### Finite sufficiency, singularity and the positive-real convention

V. Bolotnikov, *A multi-point degenerate interpolation problem for
generalized Schur functions*, Operators and Matrices **4** (2010),
151–191, [publisher PDF](https://files.ele-math.com/articles/oam-04-08.pdf),
pp.151–153, full Theorem 1.1 and definitions (1.1)–(1.7): distinct
interior disk nodes, finite prescribed jets, and the associated matrix
give Schur interpolation iff that matrix is positive semidefinite.
The class permits modulus one. Positive-definite data have infinitely
many interpolants; singular PSD data have a unique finite Blaschke
interpolant of degree the matrix rank. Simple-value data are explicitly
included. Import this standard theorem; no sufficiency reproof or
generalized-Schur finite-index hypothesis is needed.

Reuse Ball–Bolotnikov 1611.07097v1 Theorem 1.1/(1.6) for the saved
half-plane scalar convention. Here the source variable is s-1/2 and
the data value is F(s); its linear-data matrix is 2K. Under a temporary
finite-PSD hypothesis, the diagonal requires nonnegative real data.
The research applicability argument must check the output Cayley
denominator, exclude the forbidden constant-one inverse, and retain
unimodular constant solutions corresponding to purely imaginary data.
Singular PSD must not be replaced by positive definite. The cited
interpolant is for finite data only; it does not identify actual F
with a positive-real function on the half-plane.

### Bounded analytic functions with prescribed zeros

S. Zakeri, *A Course in Complex Analysis*, author
[Notes and Comments, Section 8.3](https://zakerimath.com/CAbook/COM.html),
paragraph following Example 8.33 (accessed 1 November 2026; page is
unversioned). Read the complete finite-Blaschke division argument.
For a disk-holomorphic function bounded by one, division by the finite
Blaschke product of its listed zeros, with multiplicities, is
holomorphic and remains bounded by one. The proof uses removable
zeros, the finite product's boundary modulus and the maximum principle;
it does not require boundary continuity of the original function.
The resulting pointwise product bound holds throughout the disk,
not only at the origin. This is an imported standard bound, not a new
analytic-error lemma. Its disk rescaling, applicability to the residual
and a factor uniform over these moving arrays remain for research.
No infinite interpolating-sequence separation theorem is needed.

### Interior control of a positive-real interpolant

The named Borel–Carathéodory theorem has a precise matching supporting
statement in [Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/BorelCaratheodory.html#Complex.borelCaratheodory)
and [frozen source](https://raw.githubusercontent.com/leanprover-community/mathlib4/0d3fb85496130669f472d62be6f25999ca085c59/Mathlib/Analysis/Complex/BorelCaratheodory.lean).
Read the full source proof, lines 37–110, including the nonzero
denominator, Schwarz transform and general nonzero-center case.
For f holomorphic on |z|<R, R>0, Re f<=M with M>0, and |z|<R:

    |f(z)| <= 2M|z|/(R-|z|) + |f(0)|(R+|z|)/(R-|z|).

Use the non-strict real-part hypothesis in the theorem, not the stricter
informal file introduction. The positive M condition is explicit;
substituting M=0 is not licensed by this statement. Translation and
application to the negative of a positive-real interpolant need a
disk contained in its half-plane and a positive upper bound. Thus the
source does not require a positive lower bound on the real part at
the anchor. Tracking the compact margin and anchor modulus is part
of the specialization. No local Lean replay was performed.

B.N. Örnek, *The Carathéodory Inequality on the Boundary for Holomorphic
Functions in the Unit Disc*, JMPAG **12** (2016), 287–301,
[publisher PDF](https://jmag.ilt.kharkiv.ua/index.php/jmag/article/download/jm12-0287e/768/781),
p.287 (1.1), also records the standard zero-center interior inequality.
Only that comparison is used; its later boundary derivative theorems
are irrelevant here and are not imported or audited.

### Exact scope left for the next mathematical attempt

The proposed disk, simple zero and normalized growth ratio below remain
unchanged. L018 supplies entirety, the exact normalization and safe-node
nonvanishing; the simple-zero derivative is a stipulated hypothesis.
No further zeta estimate or zero-free-region baseline is being changed.

The bounded next test is to apply the imported finite theorem under
temporary K_n>=0, control the xi-multiplied interpolation residual on
the prescribed disk, and test the source's finite-zero bound there.
An explicit delta-only contraction uniform in j/n and n, a controlled
prefactor using exactly H_rho, and a strict integer threshold must all
be written out before claiming the target. This is a research plan,
not a derivation or an assertion that these bounds have been attained.
Failure to close any of these conditions must remain visible; it does
not disprove the actual-Xi target via a generic countermodel.

Why SPECIALIZE rather than IMPORT: none of the inspected sources states
the nominated matrix/parameter/order conclusion. The standard machinery
is covered; its particular geometry, quantitative constants and uniform
quantifier require an applicability argument. Classify the subsequent
attempt as REPRODUCTION, not a new signed mechanism or certified novelty.
Any reproof should be limited to that difference. No new lemma, script,
DAG entry or assembly change occurs in this literature step.

### Search record, overlap, failures and Mathlib

Queries included `Nevanlinna Pick interpolation error estimate Blaschke
product analytic function zeros quantitative`, `Bolotnikov 2010
Nevanlinna Pick interpolation degenerate data Theorem 1.1`, `Caratheodory
inequality positive real part analytic function disk lecture notes`,
`analytic function zeros finite Blaschke product bound Schwarz lemma`,
`Nevanlinna Pick pole quantitative detection`, `xi Pick matrix witness
bound`, and `positive real interpolation Blaschke error estimate zeros`.
Search results alone support no theorem. Other leads on systems-theory
interpolation, uniformly separated infinite arrays and an external
one-point Xi criterion were not inspected as inputs. No exact matching
quantitative vertical-grid theorem was identified in the read sources;
this bounded search does not establish absence or novelty.

Reused the post-C644a screen's exact source comparisons, including the
frozen external qualitative L-91904, rather than reimporting it. Read
the canonical L258 and its quantitative-Laguerre attempt record, plus
the fixed-reserve stop. L258 already prices a different finite witness
by normalized growth. The C644a route forbids a fixed two-sided norm
reserve but supplies no eigenvalue sign; this conditional detector
does not reopen that budget. No sibling notebook was read or imported.

Mathlib: the supporting Borel–Carathéodory statement and implementation
are present at the frozen commit above. Full finite Pick interpolation,
finite-Blaschke division and the complete nominated detector were not
checked for matching Mathlib coverage; no absence is asserted.

Continue on the unchanged target next turn using this saved coverage.
The decisive evidence is an explicit valid threshold with no hidden
derivative estimate, or a precise failure of this implementation.
Compare any achieved threshold with floor(log gamma); H_rho has no
height-only control. Positivity, multiple zeros and RH remain open.

## Exact proposed test, not a result

Use L018's standard completed xi(s), with F=xi'/xi. Suppose, only
conditionally, that rho=beta+i gamma is a **simple** xi zero with
gamma>=e^5 and 1/2<beta<1. Put delta=beta-1/2, s_*=2+i gamma and

    R_delta=3/2-delta/2,
    M_rho=max_(|s-s_*|=R_delta) (|xi(s)|+|xi'(s)|),
    H_rho=(1+|F(s_*)|) M_rho / |xi'(rho)|,
    log^+ H=log(max(1,H)).

These are proposed input parameters, not height-uniform estimates.
The nonzero derivative is part of the simple-zero hypothesis. Do not
assume a lower bound for it, or that all Xi zeros are simple.

For every integer n>=1 use exactly

    s_j=2+i(gamma+j/n), 0<=j<n,
    K_n(gamma)_jk=(F(s_j)+conjugate(F(s_k)))
                         /(3+i(j-k)/n).

Seek an explicit finite C_delta depending only on delta, and a positive
integer n_0 with the bound in TARGET, such that K_n(gamma) has a strictly
negative eigenvalue for **every** n>=n_0. The arrays for different n
are not nested; a statement for one fixed finite configuration does
not imply this quantifier. This is an unproved proposed threshold,
not an established interpolation theorem or an assertion that an
off-line zero exists. Retain the exact matrix, including all completion
factors and conjugations. No norm estimate for K-I is sought.

The possible proof interface to assess is finite positive-real
interpolation followed by a quantitative analytic error estimate after
multiplying by xi. It would need to use positivity as a temporary
contradiction hypothesis for the **finite data**, not assume that F
has a positive-real continuation. Check all boundary, equality and
degenerate cases. A Cayley transform may not silently identify its
poles with xi zeros. No proof of this interface is supplied here.

## Relevance, exclusions and discriminating test

The main gap is actual-Xi initial signs at unbounded heights and then
all-degree mixed positivity. A quantitative detector could turn a
specific finite one-sided sign target into conditional exclusion of
a specified simple off-line zero. It would help the missing
restricted-configuration transfer, leaving the arithmetic signs open.
Compare the **derived** n_0, if any, with floor(log gamma); do not infer
that comparison from finiteness. Arbitrarily small delta, multiple zeros,
uniform control of H_rho and all-degree mixed positivity remain open.
No zero-free region or improvement to the supplied analytic baseline
is claimed or imported by this nomination.

Continue only if the source comparison leaves an explicit finite-order
bound with the stated normalized-growth dependence, or identifies a
precise informative obstruction to that proposed implementation.
If the entire bound is already known, IMPORT it with applicability
instead of reproving it. If standard theory covers only the machinery,
identify the difference before allowing a specialization. A purely
qualitative finite-witness criterion is already covered and is not the
test. A hidden bound for |xi'(rho)| or an assumed actual positive-real
function fails the continuation test. A model outside the actual-Xi
hypotheses could obstruct a generic method, but cannot refute TARGET.

## Continuation evidence and retained limitations

Reuse `2026-11-01-post-c644a-signed-mechanism-discovery.md` for the
completed screen, sources and query record, and
`2026-11-01-growing-vertical-pick-block-norm.md` for finite scalar-data
normalization. L018 must be read in the needed ranges before a later
actual-Xi application. L258 was read fully during discovery and is an
overlap comparison, not a premise for a matrix detector. C644a and
L641/L642/L644 retain the full-zero/multiplicity/tail and antilinear-map
qualifications; their norm/trace results are contrasts, not sign inputs.
No use of L640's parked arithmetic proof, RH, simplicity of other zeros,
positive paired measure, invariant U_X or effective onset is authorized.

The external original is L-91904 at frozen commit bb7327d21c47; its
real-axis countable criterion remains reused overlap evidence, not an
imported or independently certified theorem. The exact analytic-error
tool review is completed above. No cross-notebook input is proposed.
The partial Mathlib check above replaces the nomination's unchecked status.

This review supports a standard quantitative interpolation specialization,
not a creative positivity invocation. An independent actual-Xi signed
positivity estimate is still missing. Preserve the C644a fixed-reserve
stop and all earlier transfer, annulus, arithmetic and collision evidence.
