# Base quadratic family applicability — working record

Approved target and prior gate:
`drafts/literature/2026-10-31-family003-base-quadratic-family-audit.md`.
Task: conceptual proof audit, reproducing the pinned specialization.

Main gap is actual-Xi all-degree positivity. Intermediate target is L543
(1), with fixed S containing primes above 6. A successful exact
(UV)^epsilon(U+V) bound would replace that retained base input; cubic,
reflection, global closure and sign gaps remain independent. Stop or
narrow for a conductor, global class-map, primitive-product, zero-value
or extra-length mismatch. No numerical script is needed.

Existing source coverage and duplicate/failure searches were reused.
L543 is a downstream conditional result, not a proof of its base input.
Primary statements are available at the pinned TeX and GL v2 URLs in
the assessment. The cited quadratic reciprocity formula remains an
input; the Gaussian proof is not being independently certified.

The audit has passed at the retained-input scope. For a squarefree good
ideal a, the finite character on generators is
Q_a(x) epsilon_lambda(x)^e(a); when e(a)=0 the lambda factor and its zero
extension are omitted. Unit invariance follows from Q_a(omega)=1 and
Q_a(-1)=(-1)^e(a). CRT isolates every prime of a and, when e(a)=1,
lambda, proving exact conductor. The global group is the square-class
group of units modulo 4, using the multiplicative primary generator on
all ideals avoiding the fixed modulus with support S. Norm modulo 4
shows equal classes have equal e(a). Their primitive product therefore
has conductor ab. This is equality of inducing characters, not equality
of zero-extended products at lambda. Good matrix indices avoid lambda.

Apply GL Theorem 1.1 with swapped lengths to the matrix
A_(b,a)=theta_a(b). It is real, so the required transpose is its adjoint;
the operator norm and arbitrary complex coefficient norm are unchanged.
Collisions match because every prime of a belongs to its conductor.
The unit ideal gives the trivial character of conductor one. The target
bound is exact, with no extra length or logarithmic factor.

Full proof and source qualifications are saved in
`lemmas/L544-primary-quadratic-hecke-family-specialization.md`.
This is a reproduction, not an improvement beyond the checked sources.
The original Gaussian proof and GL's general sieve proof remain imported.
A local curl retrieval failed DNS; the primary web tool supplied all
load-bearing statements and cases, so this was not a source blocker.

The next independent contract is L542 (2). Its existing hybrid source
assessment explicitly leaves Heath-Brown Theorem 2 unread. A separate
REVIEW_REQUIRED source comparison has been prepared; no cubic
specialization was attempted in this step. The retained reciprocity
proof, cubic/reflection/global closure and Xi signs remain unresolved.
