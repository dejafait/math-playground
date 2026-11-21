# Central Hermite trace form — completed source comparison

TARGET: Test whether the Hermite trace matrix of the actual central degree-six Jensen polynomial has a direct theta-moment Gram representation with explicitly nonnegative weights and no root-location premise.
CHECKED: 2026-11-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Step495 searched Hermite-Sylvester/Newton-sum trace forms, Jensen degree-six hyperbolicity, Andreief/Gram integration and their theta combinations; inspected the primary cases below and reused step389/391/456 scope and stop evidence. No matching noncircular theta Gram identity found; no novelty inference.
SOURCE_EVIDENCE: Nathanson 1911.01745v2 (24Nov2019), pp.1–4, Lemmas1–2 and Theorem1 with both proof cases; Griffin–Ono–Rolen–Zagier 1902.07321v2 (31Mar2019), (1)–(2), Theorems1–2 and Section5.2 p.9; Forrester 1806.10411v1 (27Jun2018), (1.2)–(1.3),(1.7), Sections2.2–2.3 pp.3–5. Exact hypotheses, links, proof qualifications and local inputs below.
COMPARISON: Degree-six central hyperbolicity is already covered. Hermite's real-root square formula and Andreief's bilinear determinant identity do not supply functions realizing the nonlinear Newton sums as theta Gram entries. A finite product-moment kernel is a distinct, source-covered algebraic diagnostic, not an imported positive identity.
GAP: No explicit nonnegative theta Gram representation or theta-specific sign mechanism is established. Constructing and signing the precisely nominated symmetric product-moment kernel remains unpaid; all-degree signs and degree-uniform control remain open.
REASON: Park automatic criterion-to-Gram and low-degree-sign imports; retain only the narrow coefficient-to-product-kernel difference for a later bounded test. Coverage permits that conventional algebraic attempt, not an unspecified Gram factor or a claimed new hyperbolicity theorem.
LITERATURE_REASON: The invocation-start target was REVIEW_REQUIRED and lacked essential Hermite/Gram coverage; L793 and the earlier Toeplitz-integral assessment do not identify this Newton-sum matrix.
SCOPE: Completed literature-only step495 for the unchanged TARGET. The original nomination below is preserved; its pending coverage language is superseded by the completed comparison. No new identity, sign calculation, lemma, mathematical script or argument change. The exact narrower continuation has its own newly written assessment and requires separate next-turn approval.

## Exact proposed input and test

Use the actual normalization in L018/L021/L776 and L791/L792:
G(w)=xi(1/2+sqrt(w)/2)/8=sum a_j w^j,
gamma(j)=8*4^j*j!*a_j and R_j=gamma(j)/gamma(0).
Define

    P_6(x)=sum_(j=0)^6 (-1)^j binom(6,j) R_j x^j.

This fixes shift zero, unlike an eventual-shift theorem. Its leading
coefficient is nonzero since gamma(6)>0. Normalize P_6 to be monic and
let s_m be its formal Newton sums, with s_0=6, calculated from its
coefficients rather than assuming a real root list. The object to
review is H=(s_(i+j))_(i,j=0)^5. These are proposed definitions, not a
claim of positive definiteness or of an integral representation.

Seek an exact formula for v^T H v as an explicitly nonnegative theta
integral, using the actual positive theta density and specified real
functions. Positivity of a weight, the allowed function class and all
interchanges must be proved or precisely imported. A Gram factor
defined using the desired matrix's positive square root, unknown real
roots or unproved principal-minor signs is circular and fails this
test. A generic real-rootedness equivalence alone is not progress.
Before algebra, inspect the primary Hermite trace-form criterion and
relevant moment-determinant/integral identities and compare known
central Jensen hyperbolicity results, including degree six. Reuse ready
source assessments if an exact match is found rather than browse again.

## Three mechanisms and decision

1. Relative root disks: L793 now passes its separate audit, but its
   actual model/mesh/error premises are unpaid. Do not repeat tolerance
   estimates without those inputs.
2. Universal or same-mesh diagonal transfer: the stops C792a and C792b
   retain their scopes and prefix obstruction; changing a later degree
   does not reopen the same fixed-prefix fallback.
3. Direct actual theta-moment trace form: select this independently
   testable structural mechanism for source comparison. It has no
   model-root separation premise and does not assume the failed
   preserver condition. Its essential theorem/identity coverage is
   missing, so mathematical execution is not yet authorized.

Continue only if source comparison supplies a precise noncircular
identity or a narrow, source-covered algebraic difference that can
be tested at degree six. If it merely restates hyperbolicity, requires
the unknown signs as inputs, or reproduces a recorded identical
failure, record that obstruction and park this particular mechanism.
Even a successful degree-six identity is only a diagnostic for a
possible degree-uniform construction; it does not prove all degrees,
all shifts, mixed positivity or RH. A later creative attempt requires
separate ready coverage and a bounded identity/sign test; it must not
be disguised as routine specialization or approved in this turn.

Essential continuation inputs: L018/L021's actual theta moments and
L776's coefficient normalization; L791/L792 fix the Jensen convention
and supply finite-degree context only. No model solution, L778 software
certificate, L793 tolerance, C792a/C792b conclusion, or zero-location
assertion is a mathematical premise of the proposed representation.
The exact Hermite criterion, applicability of integral identities,
actual Gram representation and all degree-uniform signs are unresolved.
Mathlib coverage is unchecked. No cross-notebook result is used.

## Completed source comparison — step495, 5 November 2026

The main gap is still actual-Xi all-degree mixed positivity. The proposed
intermediate target was a theta Gram identity for the central degree-six
Hermite form, usable as a diagnostic for an eventual degree-uniform
construction. The source comparison rules out importing such an identity
from the two standard criteria alone; it does not prove that no such
identity exists. No mathematical attempt was performed this turn.

### Exact Hermite criterion, including multiplicities

Melvyn B. Nathanson, *The Hermite-Sylvester criterion for real-rooted
polynomials*, [arXiv:1911.01745v2](https://arxiv.org/pdf/1911.01745v2),
24 November 2019, pp.1–4, Theorem1 and Lemmas1–2. Read the full
conjugation/interpolation arguments and both theorem proof cases;
the [HTML proof](https://arxiv.org/html/1911.01745v2) is also accessible.
For any nonconstant real polynomial of degree n, form its power sums
with roots counted with multiplicity, starting with s_0=n. Newton's
identities compute them from the coefficients. The theorem says that
the real symmetric matrix (s_(i+j))_(i,j=0)^(n-1) is positive
semidefinite exactly when every root is real. Monicity is an innocuous
normalization, not a real-root premise. Repeated roots are allowed;
the conclusion is semidefiniteness, not automatic strict definiteness.

The positive proof writes the quadratic form as the sum of p(lambda)^2
over roots, and uses their reality to make those squares nonnegative.
The converse uses real interpolation on the distinct root set: a
nonreal conjugate pair receives values i,-i and the remaining distinct
roots receive zero. Their equal multiplicities give a strictly negative
quadratic-form value. Thus a complex algebraic square is not a modulus
square, even though the resulting form has real coefficients. This
precise proof identifies why its root evaluation formula is not the
requested independent theta Gram representation. No reproof is needed.

The proposed P_6 has real coefficients and nonzero leading coefficient
by L021's positive sixth moment and the normalization in L776/L791.
The source therefore applies to its coefficient-computed H without
assuming any root location. The missing step is positivity, or a
specified root-independent integral identity that proves it. Merely
using the criterion does not establish that step.

### Known degree-six overlap and exact normalization

M. Griffin, K. Ono, L. Rolen and D. Zagier, *Jensen polynomials for the
Riemann zeta function and other sequences*,
[arXiv:1902.07321v2](https://arxiv.org/pdf/1902.07321v2),
31 March 2019, (1)–(2), pp.1–2, Theorems1–2; published in
PNAS116(23) (2019),11103–11110,
[DOI10.1073/pnas.1902572116](https://doi.org/10.1073/pnas.1902572116).
Theorem2 states hyperbolicity for 1<=d<=8 and every integer shift n>=0.
This includes d=6,n=0. Theorem1's eventual-shift assertion is weaker
for this particular task and is not a shift-zero premise.

Their (1) expands (4z^2-1)Lambda(1/2+z)=8xi(1/2+z) with coefficients
gamma_source(j)/j!. L776 and L791 define gamma_local(j) as the
coefficients of xi(1/2+z) in that exponential convention. Consequently
gamma_source(j)=8 gamma_local(j), and normalization by gamma(0)
removes that constant. Their (2), with X=-x and n=0, is exactly the
proposed P_6 after that division. This is only the applicability check
for a cited result, not a fresh sign proof.

Read Section5.2, p.9, including its finite Hermite-criterion checks
through shift10^6, coefficient neighborhoods of Hermite polynomials,
effective tail bounds and the d=4 example. The authors explicitly call
this section a proof sketch. Their computations, constants and full
asymptotic proof were not independently replayed here; the theorem is
used for literature overlap, not as a newly audited certificate. The
Hermite-polynomial model concerns eventual shift. Neither its Gaussian
orthogonality nor the finite verification supplies an exact theta Gram
identity for the central polynomial. Computing central PSD again would
reproduce a known qualitative conclusion and would miss this target.

### What determinant integration actually supplies

P. J. Forrester, *Meet Andreief, Bordeaux 1886, and Andreev, Kharkov
1882–83*, [arXiv:1806.10411v1](https://arxiv.org/pdf/1806.10411v1),
27 June 2018, (1.2)–(1.3),(1.7), pp.1–2, Sections2.2–2.3, pp.3–5;
the [complete permutation proof](https://arxiv.org/html/1806.10411v1#S2.SS2)
was read. Two supplied families f_j,phi_j on a common domain give
the integral of their two evaluation determinants as N! times the
determinant of their bilinear integral matrix. The proof expands one
determinant, permutes variables, and integrates rows. The discrete
Cauchy–Binet comparison fixes the same orientation and factorial.

For a noncompact application, require absolute integrability of each
expanded product, not just individual integrability of f_j and phi_j.
Matched real families under a nonnegative measure produce a Gram
matrix and a squared evaluation determinant. The identity does not
find those families for an arbitrary matrix. Its positive Vandermonde
example concerns raw moments of a positive weight. The s_j here are
nonlinear Newton sums of factorial-normalized polynomial coefficients,
not the theta moments M_(2j). Nothing inspected identifies these two
moment sequences. No Cholesky construction from unknown principal
minors, root measure, or matrix positive square root is admissible as
that missing identification.

Reuse the earlier complete integration assessment in
`2026-11-04-actual-toeplitz-signed-integral-review.md` only for finite
expansion, Fubini and symmetrization methods. L019/L021 give positivity
of actual K and finiteness of every moment; they can justify finite
polynomial product integrals once an identity is written. They do not
sign its kernel. A finite denominator-clearing/product-moment test is
the narrow algebraic difference left after this comparison. It is
specified, without being executed, in
[the next assessment](2026-11-05-central-hermite-product-kernel-test.md).

### Duplicate and failure comparison

Read L018/L021, L019's actual K formula and decay, and only the needed
normalization/context ranges of L776/L791/L792. No numerical evaluator,
model root solution, L793 tolerance or actual-root assertion is an
input. The step389 assessment, L766's full representation and sign
argument, its step390 ATTEMPTS record, and step391's compensation
source limit were checked. L766 refutes pointwise signing of one
factorial Toeplitz row-integrand. It neither identifies nor refutes
the new nonlinear Newton-sum kernel. Reusing its *result* here would
be an invalid change of matrix; reusing finite moment expansion as a
method is appropriate. The prospective test must construct its own
exact kernel and cannot infer integrated negativity from pointwise
negativity.

Step456's ready rational Bezoutian/Hankel comparison was reused:
Heinig–Rost Proposition7.15 is a rational congruence, while its positive
residue cases impose real poles/sign hypotheses. No new read of those
external sources was needed. Their coefficient elimination does not
supply the theta sign. C792a/C792b's universal/same-mesh stops and
L793's unpaid actual-model transfer are contrasts, not premises or
global bans. This review creates no new dependency graph or node.

### Search and access qualifications

Queries included `Hermite Sylvester criterion real rooted polynomials
trace form Newton sums Nathanson theorem`; `Jensen polynomials Riemann
xi degree 6 hyperbolic Griffin Ono Rolen Zagier 2019 theorem`;
`Andreief integration formula determinants positive measure Gram
Forrester history identity`; `Forrester Meet Andreief Bordeaux 1886
2019 arxiv integration formula`; `Jensen theta Hermite matrix Gram
integral`; `Jensen polynomials Hankel moment positivity`;
`"Jensen" "Hermite matrix" "integral"`; `"Jensen" "trace form" theta`;
and `"Riemann" "Newton sums" "Gram" Jensen theta`. The broader search
also returned a 2026 Stieltjes/Painleve article and a classical-polynomial
trace-form article. Their full theorems/proofs were not read, and they
are unread leads, not evidence or adopted inputs. No novelty or
nonexistence claim follows from the negative exact searches.

Local searches were restricted to named November4/5 assessments and
ATTEMPTS, then their relevant canonical inputs. An initial status/search
output was oversized; later bounded exact reads provide the evidence
used here. No sibling proofs, other problem checkpoint, runtime state
or API credentials were read. Existing unfinished changes are retained.
The PMC published copy returned a browser challenge; the MPG copy
returned403. The primary versioned arXiv sources supplied the essential
statements/cases, so there is no essential source blocker. HTML generated
dates are not source revision dates; use the pinned PDF version labels.
Full matching Mathlib coverage remains unchecked, not asserted absent.

### Decision, scope and continuation test

The negative outcome is source-level: discard automatic Hermite-plus-
Andreief signing and a repeat of already known degree-six hyperbolicity.
No theorem has ruled out the requested representation. Keep the broad
Gram question open, with only one bounded noncircular diagnostic
prepared: form the canonical symmetrized product-moment kernel and
test pointwise PSD. The source-covered methods are Newton identities,
finite polynomial expansion, absolute Fubini and finite permutation
averaging; the kernel and its sign are not supplied by any citation.

A negative quadratic value on a positive-variable open set parks this
specific direct kernel. Failure of a symbolic construction is
inconclusive, not a negative sign. A positive one-parameter test alone
does not establish global PSD; a proved global factorization would
still concern degree six only. No parameter/degree sweep, Gram square
root, new model fit or numerical hyperbolicity recheck is justified.
This is conventional finite algebra, not a protected creative attempt.
Independently controlled theta compensation or another structural input
is still missing before a justified creative all-degree mechanism can
be nominated. No mathematical exploration budget is reset.
