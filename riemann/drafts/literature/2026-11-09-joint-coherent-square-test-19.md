# Coupled pole operator — coherent-square source comparison

TARGET: Test whether retaining the cross-endpoint products in L930's coherent square V_pole^* H_-^(-1) V_pole yields a uniform deficit below H_+ large enough to pay the regular-zeta and arithmetic errors.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Step20 searched exact logarithmic/complex GCD inverse and shifted-moment coercivity terminology and polynomial inverse error bounds; reused scope-8/test-9, coverage-11 and L930/L931 stops. Read the primary statements identified below; no matching quantitative contraction theorem was found in this bounded search, and no novelty claim follows.
SOURCE_EVIDENCE: Embree--Henningsen--Jackson--Morgan, Polynomial Approximation to the Inverse of a Large Matrix, author manuscript Section2.2 Theorems1-2/proofs pp6-7 and Section2.3 Proposition3(1) p7, https://vtechworks.lib.vt.edu/server/api/core/bitstreams/09f4a247-175e-4f0d-9eec-2cce887a9e9f/content (publication DOI10.1137/24M1677599); Barrett et al., Templates, polynomial-preconditioner section https://netlib.org/linalg/old_html_templates/section2.7.5.html; Guillot--Wu arXiv:1901.01947v1 Theorems1.5/1.12; existing Mattila/Bhatia/de Boor/moment coverage reused.
COMPARISON: Primary spectral-functional-calculus coverage permits a scalar polynomial approximation to the full inverse with a dimension-independent operator residual, retaining the combined endpoint products. It neither proves a deficit nor turns a single right-hand-side residual into a collective bound. Ordinary GCD/Green-matrix inverse results concern different matrices.
GAP: One bounded analytic test must verify a uniform spectral enclosure, propagate the inverse-approximation error in the two full metrics, and estimate the retained coherent polynomial square. Its deficit must pay that error, L930(12) and L928(5); none of these new estimates is derived here.
REASON: This separate literature-only review completes coverage for the saved target and approves only the fixed-degree residual test below. A cited quantitative residual tool makes one attempt actionable; the contraction remains unproved. Stop if the test gives only the equivalent block criterion or stopped absolute majorants.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED gate lacked essential coverage of full inverse-metric endpoint products; the prior scalar audit and first-difference assessment did not cover this residual technique.
SCOPE: Keep L930's exact V_pole, H_-, H_+, fixed w, exact Hardy phase, N=floor(T^(1/5)), and T<=X<=2T. No matrix grid, profile optimization, changed dictionary length, L925/L929 theorem or cross-notebook input.

The following is the preserved step19 nomination. Its REVIEW_REQUIRED
status and last paragraph describe that earlier turn; the completed
step20 comparison and current decision are below.

The main gap is L030–L032/C032a actual-Xi all-degree mixed positivity.
The intermediate target is a collective estimate for the already
defined pole operator, with plausible use in the unpaid L928 joint
projection comparison. Signed realization and Xi transfer remain
independent requirements even if this estimate succeeds.

Essential local inputs are audited L930(4),(7)–(8),(12) for the
complete metrics, exact pole operator and uniform regular residual;
L737 for finite divisor identities; and audited L928(3)–(5) for the
arithmetic charge. L931's audited scalar test only removes the one
totient-profile witness. It is motivation, not a premise bounding
other vectors. No assumption about an infinite limiting operator or
positivity of complex Jordan factors is authorized.

For the future source comparison, the proposed test seeks one
dimension-independent delta>0 with

    V_pole^* H_-^(-1) V_pole <= (1-delta) H_+,

uniformly in X at a common onset. This is an unproved target. If only
a shrinking delta(T) is plausible, the proposed mechanism must retain
the explicit threshold

    1-sqrt(1-delta(T))-||R_reg||

positive and sufficiently larger than L928's relative arithmetic charge
O(T^(-9/80)/log T). A fixed positive delta would suffice after the
existing residual estimates; no such delta is supplied here.

Retain the mixed W_+^* H_-^(-1) W_- terms and their conjugates
when comparing sources. Independently bounding every endpoint product
by its modulus returns to the stopped loss. The full H_- inverse
cannot be replaced by a diagonal inverse without paying the resulting
operator error. The one-vector limit from L931 cannot control this
collective expression.

Continue only if inspected primary hypotheses support a concrete
cross-product estimate or a specified independently checkable residual
test. If the comparison yields only the equivalent Schur-complement
criterion, an assumed positive Gram kernel, or the earlier absolute
majorants, abandon this proposed mechanism rather than repeat coverage
or rename the missing contraction. No new source access is currently
known blocked. Mathlib matching coverage has not been checked.

Preserve L930's parameter-norm certificate floor and the termwise
stop, as well as L931's now-audited single-profile exclusion. The
actual-Xi de Branges construction and canonical-system boundary stops
were checked narrowly for possible overlap: they concern different
actual-function positivity data, and supply no input to this finite
square estimate. This nomination neither reopens them nor assumes
their missing signed data. No justified central creative Xi-sign
mechanism is presently supplied by these unsigned moment inputs;
that is the blocker to recommending a protected creative attempt now.

This is a new REVIEW_REQUIRED continuation, not a completed source
assessment or mathematical attempt. Next-turn work is literature-only,
reusing all adequate prior coverage and examining only the missing
coherent-square mechanism. No lemma or mathematical script is to be
written during that source comparison.

## Completed source comparison — 9 November 2026, step20

This is LITERATURE / NOVELTY_UNCHECKED, outcome EXPLORATION.
No new lemma, inverse formula for the local matrices, contraction bound,
or mathematical program was derived. The change is a checked tool and
a bounded test specification, not mathematical progress beyond sources.
The target text and all physical/arithmetic parameters are unchanged.

### Local overlap and search scope

Read L930's exact definitions (3)–(9), bounds (10)–(13), and its
parameter-norm floor and threshold discussion; L928's hypotheses and
(1)–(5); and the relevant finite-form scope in L737. Reused the
scope-8/test-9 and coverage-11 assessments, including their inspected
Mattila, Bhatia, de Boor and moment interfaces. The completed L931 audit
is accepted as supplied; its proof is not reopened or used as a norm
bound. No mathematical certificate was needed or inspected.

Targeted searches in these assessments and the joint attempt/history
files found no previous polynomial full-inverse test. This is a local
duplication check, not a claim of mathematical originality. Preserve
the termwise Schur stop, L930's parameter-norm floor, the two-shift
unpaid-coercivity stop, step226 and the conditioning approval-loop stop.
None supplies an upper bound on the coherent square. The proposed test
does not optimize those majorants or recheck a successful scalar input.

Queries included `"GCD matrices" "inverse" complex logarithmic`,
`"gcd matrices" "logarithmic" "inverse"`,
`"twisted second moment" "positive definite" shifts`,
`"twisted second moment" "coercivity"`,
`"GCD matrices" "complex" "singular"`,
`"twisted second moment" "Gram matrix"`,
`matrix inverse polynomial approximation positive definite residual
Neumann series theorem`, `"matrix inverse" "polynomial" "Loewner"
approximation`, and `Demko Moss Smith 1984 decay rates inverses band
matrices polynomial approximation pdf`. General control/observability
and M-matrix searches supplied no inspected matching contraction result.
Search snippets, unrelated GCD acronym hits and online research logs
were not evidence for a theorem. No exhaustive absence claim is made.

### Primary statements and applicability

* Embree, Henningsen, Jackson and Morgan, *Polynomial Approximation
  to the Inverse of a Large Matrix*, [served author manuscript](https://vtechworks.lib.vt.edu/server/api/core/bitstreams/09f4a247-175e-4f0d-9eec-2cce887a9e9f/content),
  26 pages, retrieved 9 November 2026; [publication record](https://doi.org/10.1137/24M1677599).
  Numbering here is the manuscript's. Read Section2.2 Theorems1–2
  and their complete proofs, pp6–7, and Section2.3 Proposition3,
  p7. Proposition3(1) assumes invertible diagonalizable A and any
  polynomial p; its bound is
  `||A^(-1)-p(A)|| <= kappa(Z) max_(lambda in spectrum(A)) |1/lambda-p(lambda)|`,
  where A=Z Lambda Z^(-1). For the real symmetric positive H_- in
  L930(4), orthonormal diagonalization gives kappa(Z)=1; a proved
  spectral enclosure would make the scalar maximum independently
  checkable. No approximation to the nonnormal endpoint matrix is
  authorized this way. Theorem2's right-hand-side bound also divides
  by the smallest eigenvector coefficient of that right-hand side;
  it does not justify a dimension-uniform claim from a sampled vector.
  Only Proposition3(1), the standard spectral-theorem case, is needed.
  No local inverse estimate or source theorem reproof is performed.
* Barrett et al., *Templates for the Solution of Linear Systems*,
  [polynomial-preconditioner section](https://netlib.org/linalg/old_html_templates/section2.7.5.html),
  inspected as the authors' online book section. It describes inverse
  polynomials, Neumann truncation and uniform scalar polynomial choice;
  both spectral endpoints are needed for the Chebyshev approach.
  Several equations render as image links; no hidden equation or exact
  error constant is imported from them. This is context for choosing
  a polynomial, not the load-bearing error theorem.
* Guillot and Wu, *Total nonnegativity of GCD matrices and kernels*,
  [arXiv:1901.01947v1](https://arxiv.org/pdf/1901.01947v1),
  7 January 2019, pp3–5, Theorems1.5 and1.12, compared for scope.
  Their total-nonnegativity/Green-matrix and tridiagonal-inverse
  conclusions concern ordinary GCD matrices with the specified ordered
  integer hypotheses. H_- is the logarithmic divisor-coordinate energy
  in L930(4); neither this identification nor those hypotheses follow
  from its positive definiteness. These results are not imported for
  H_- or for complex W_±. Their proofs are unnecessary to an input
  that is not used. The earlier ordinary-GCD positive-definiteness
  comparison remains unchanged.

The Demko–Moss–Smith AMS PDF and Georgia Tech report mirror returned
403; they remain unread leads, not imported band-decay theorems.
The Utah numerical-analysis PDF was inaccessible to the web tool.
Yang's UC Merced Lecture21 was accessible: the spectral-polynomial
argument on slides12–13 and Neumann statement on slide25 were inspected
as supporting exposition only, with no local estimate imported.
These access failures do not block the needed spectral residual tool,
whose complete statement is available in the author manuscript above.
The other branches of Proposition3 (numerical range/pseudospectrum),
adaptive GMRES experiments, and banded-inverse decay are not needed.
No essential input is being inferred from their abstracts or previews.

### One bounded test approved for the unchanged target

Use the exact V_pole, H_- and H_+ of L930. First verify a common
positive scalar spectral enclosure [a,b] for H_-/L, uniform in X and
eventually T. L930(3)–(4) supplies the available finite norm and lower
metric inputs; the upper endpoint and all constants must be checked in
the mathematical attempt, not assumed as a new result of this review.

Prescribe one degree-16 scalar polynomial p_16 minimizing the uniform
absolute approximation error to 1/x on that enclosure. This defines a
bounded pilot, not an assertion that degree16 is sufficient. Apply
Proposition3(1) to the scaled metric, and test the coherent surrogate
obtained by substituting L^(-1) p_16(H_-/L) for H_-^(-1) between
V_pole^* and V_pole. Both endpoint products and their conjugates must
remain together. The scalar approximation error is an independent,
non-positivity input; its propagation through V_pole and the H_+ metric
is a mathematical obligation, not a result recorded here.

This specifies more than the equivalent Schur-complement criterion:
it prescribes an inverse surrogate, a scalar uniform error to certify,
and a finite coherent polynomial whose deficit can be compared with
that error. Nevertheless, merely constructing this surrogate, proving
its convergence, or restating its positivity is not an advance. A
useful result must estimate its full coherent defect analytically or
identify a quantitative obstruction to this chosen test. Do not sample
the growing matrices or replace the inverse by a diagonal inverse
without a charge. No endpoint-modulus or parameter-norm majorant may
be advertised as a new mechanism. No automatic increase in degree or
profile/dictionary optimization is authorized after an inconclusive
test; first record its actual loss and reassess the mechanism.

The success threshold remains the nomination's delta(T): the resulting
upper bound on the true square must leave
`1-sqrt(1-delta(T))-||R_reg||` positive and larger in scale than
L928(5)'s O(T^(-9/80)/log T). The inverse-approximation error must
already have been paid in that square bound. No value or sign of
delta(T), and no collective endpoint-product sign, is inferred here.
A fixed positive delta would suffice, but is not imported. Abandon
this test if it reduces to the unpaid equivalent criterion or the
stopped absolute losses, or if its certified residual consumes the
putative deficit; preserve any unfinished finite reasoning.

DECISION EXPLORE completes this separate source gate for exactly TARGET,
restricted to this one analytic residual test. It is ready for one
mathematical attempt; no further unchanged source search is needed.
Essential inputs are L737, audited L928(3)–(5), L930(3)–(4),(7)–(8),
(12)–(13), and the cited finite spectral theorem. L931 only removes
one prescribed witness; L925/L929 and cross-notebook inputs are excluded.
Uniform surrogate-defect control, a paid joint margin, signed realization
and Xi transfer remain unresolved. Full matching Mathlib coverage has
not been checked. This unsigned established-route test supplies no
new signed input justifying a central creative Xi-sign mechanism; that
remains the blocker to nominating proof_attempt/creative in this step.
