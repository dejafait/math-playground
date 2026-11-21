# Zero-inclusive compression: source comparison727 after audit726

TARGET: Assess primary coverage for a certified compressed exponential approximation of C998u's G on [0,ell], including zero, with B^2 sup|G-Gtilde|<=1e-7 and explicit rank and construction cost against10^8 operations.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Comparison727 searched finite completely monotonic functions, positive exponential approximation at zero, Gaussian construction from moments and its conditioning; read the primary items below and searched narrowly in remote-image assessments/attempts for overlap. No existing complete certificate for this G was located; this is not a novelty claim.
SOURCE_EVIDENCE: Koyama arXiv:2301.08931v3 Lemma2.2/proof p3,Lemma2.6/proof p5,Theorem2.14/proof pp7-8,AppendixB pp40-41,AppendixC.1 pp41-42,Section4.4.2 pp34-35; Golub--Welsch1969 Sections2/4 pp222-223/226-227; DLMF2.10.1 and24.4.9; Gautschi Section2.2 pp8-9; archived Arb2.23.0 polynomial root-finding contract. Precise links and qualifications below; reuse723/719 for sweeps and ball arithmetic.
COMPARISON: Bounded positive spectral measures have a zero-inclusive Gaussian exponential approximation with an explicit uniform bound; discrete measures are allowed. This removes the positive-distance mismatch for individual finite blocks, not the infinite-spectrum tail or certified preparation cost. Existing numerical implementations and asymptotic complexity do not pay our ledger.
GAP: Specialize to disjoint spectral blocks of the unchanged discrete G; certify their tail, total rank, moment preparation, positive nodes/weights, coefficient/rate errors, precision, bytes and finite construction work. These are deliberately unproved applicability/effectivity tests, not missing general approximation hypotheses. Density quadrature and a full scalar remain outside scope.
REASON: Essential general approximation and construction tools are now inspected. A bounded standard-method specialization can test the effective ledger without reproving Gaussian quadrature or claiming novelty. The completed literature step establishes source scope only; the newly ready continuation requires separate approval next turn.
LITERATURE_REASON: Changed approximation hypothesis: replace the raw geometric prefix by a certified zero-inclusive compressed sum; the inspected power-kernel theorem excludes zero and cannot supply this essential input.
SCOPE: The unchanged kernel G(r)=sum_(j>=0)exp[-(2j+1/2)r]/(2j+1/2)^2 on [0,ell],ell=log(3)/2; seek a finite sum with real nonnegative rates and weights. No scalar evaluation, density replacement, witness change, sign inference or inverse estimate.
COVERED_TARGET: Test one dyadic spectral-block Gaussian compression of C998u's unchanged G, including zero, with B^2 sup|G-Gtilde|<=1e-7 and a certified coefficient/rate construction ledger against10^8 operations.

The nomination726 below is preserved as historical scope and stopping
evidence. Its statements that coverage is pending are superseded only by
completed comparison727 below. No proposed finite rank or construction
has been established in this literature-only step.

The main gap is L030-L032/C032a actual-Xi positivity and signed S3.
The proposed intermediate target is a certified compressed kernel usable
in C998u(3)/(9), including its diagonal and density interactions. Its
plausible use is to replace stop724's enormous per-exponential outer loop
in a later aggregate scalar evaluator. It does not itself pay the density
quadrature, local d0 term, rounding, preparation of h or a full scalar.

Use the audited C998u identity and B=2^23, together with C998t's full-form
bridge, C998s's complete image and projection, C744z(1), C999l(1), and
the unchanged C998r witness SHA256
99ebc79ed3d82771ad0b5567356ba953e0d123d86aecdfe07d8e57f6fb9c634a.
All334 shifts, identity2187,512 modes, full K14 and exact P0 remain.
The uniform signed-measure error bound B^2 sup|G-Gtilde| is already in
C998u Section2; no new error-transfer lemma is derived here. The
remaining9e-7 allowance remains unpaid, and the10^8 cap is for all
eventual work, not a free allowance for each stage.

The next review should locate and inspect a primary constructive theorem
for this continuous Laplace-series kernel or a demonstrably applicable
class, including the zero-distance case, before proposing a calculation.
An approximation valid only for r>=delta>0 needs a separately covered
near-diagonal treatment; simply deleting that interval is not admissible.
Record finite rank and construction obligations rather than infer them
from an asymptotic count or an empirical fit. No specific compressed
rank, coefficient rule or feasible implementation is claimed726.

Continuation test: proceed to a separately gated mathematical attempt
only if source coverage supports a concrete uniform construction and
an independently testable rank/cost bound. Park the dependent construction
if the sources only cover positive separation with an unpaid near-field,
or cannot give a checkable bound; choose an independent target if the
source obstruction persists. A construction requiring over10^8 operations
would already miss the eventual cap, while being below it would leave
all other costs to be paid. Do not reopen the unchanged prefix rule.

Preserve stops617/603/635/640/652/705/712/716/720/722/724. In particular,
stop722 concerns separately assembled resonant piece-pair products,
whereas this target concerns the scalar distance kernel before density
discretization. It is not that FFT prescription under a new name.
The earlier stops are evidence about their specified implementations,
not a ban on a different, testable kernel construction.

The analytic-response, neutral-core, IEEE754/Decimal and unreplayed c_*
qualifications persist. Signed coupling, other entries and endpoints,
C744q/H2 and actual-Xi/global assembly are unresolved. No new creative
sign-producing mechanism is justified by this representation audit;
the missing signed remote-plus-induced domination remains that blocker.
This continuation is standard theorem comparison, not creative work.

Mathlib coverage for this proposed compressed approximation is not checked.
The completed audit remains valid independently of this uncovered target;
this file does not approve new mathematics in the same invocation.

## Completed source comparison727 — 13 November2026

### Primary results and essential qualifications

**Uniform approximation.** Yohei M. Koyama, *Exponential sum
approximations of finite completely monotonic functions*,
[arXiv:2301.08931v3](https://arxiv.org/pdf/2301.08931v3),
22July2023. Inspected the passages listed in SOURCE_EVIDENCE, including
the endpoint and ellipse proof cases. For0<a<b<infinity, bounded
nondecreasing W with at least m+1 points of increase, and continuous
strictly increasing phi:[-1,1]->[a/b,1], Lemma2.2 gives m positive
weights and interior nodes, polynomial exactness through2m-1 and
sum(weights)=f(0). No density W' is required. For analytic phi,
Theorem2.14(48) gives uniform absolute error

    (16/pi) rhohat^(-2m) f(0), 0<=x<infinity.

For linear phi, AppendixC.1(C.1)-(C.3) gives
rhohat=(1+sqrt(a/b))/(1-sqrt(a/b)). At zero, mass exactness applies;
Lemma2.6 bounds the exponential on a complex ellipse. Section4.4.2's
numerical construction uses smooth W' and convergence comparisons;
it supplies no certified discrete-measure preparation cost.

This is an applicable block tool, not a theorem for the entire unbounded
spectral support of G. Whether a finite block construction meets the
specified tolerance and cap is the next mathematical question.

**Construction from moments.** G.H. Golub and J.H. Welsch,
*Calculation of Gauss Quadrature Rules*, Math.Comp.23(106)(1969),
221-230, [primary published paper](https://www.ams.org/journals/mcom/1969-23-106/S0025-5718-69-99647-1/S0025-5718-69-99647-1.pdf),
Section2/(2.1)-(2.6) pp222-223 and Section4/(4.1)-(4.3) pp226-227,
including the moment-matrix orthogonalization argument. With a positive
moment matrix, Cholesky orthogonalization yields recurrence coefficients;
Jacobi eigenvalues give nodes and mu_0 times squared first normalized
eigenvector components give weights. Section4 uses moments through2m
for its displayed construction. Although written using weight functions,
the finite-matrix algebra uses only inner products and their positive
definiteness; discrete-measure positivity and sufficient support must
be checked in the specialization. No convergence rate, precision or
finite work bound for our moment matrices is imported. PDF text has
inconsistent intermediate signs in the recurrence display; use the
positive Cholesky identities(4.3) or derive the recurrence from the
orthogonality equations, not the suspect intermediate line. No source
error is asserted without inspecting a page image.

Walter Gautschi, *Orthogonal Polynomials, Quadrature, and Approximation:
Computational Methods and Software (in Matlab)*,
[author-hosted chapter](https://www.cs.purdue.edu/homes/wxg/selected_works/section_11/179.pdf),
Section2.2 pp8-9, including Algorithm1, inspected13November2026.
Ordinary-moment reconstruction can be severely ill-conditioned;
modified moments may improve it but do not guarantee conditioning.
This is a warning relevant to certification, not a quantitative lower
bound for our blocks. The source's update frequency/version date was
not independently established. Only the inspected archived text is used.

**Finite moment preparation.**
[DLMF2.10.1](https://dlmf.nist.gov/2.10.E1),
Section2.10(i), inspected13November2026: integer endpoints n>a,
m>0, and absolutely integrable f^(2m) on[a,n] give the exact
Euler--Maclaurin formula with endpoint corrections through s=m-1 and
remainder integral (B_(2m)-Btilde_(2m)(x))f^(2m)(x)/(2m)!.
Read this remainder rather than treating an asymptotic series as a
certificate. A later use must enclose the periodic Bernoulli factor and
derivative integral, retaining both endpoints and all rounding.
[DLMF24.4.9](https://dlmf.nist.gov/24.4.E9), inspected on the same date,
gives finite arithmetic-progression power sums by Bernoulli polynomial
differences, for nonnegative integer power and positive integer count
(the displayed quotient requires nonzero progression step). This
supports a non-enumerative moment recipe; its inverse-power cases,
precision, cancellation and complete operation count must still be
specified and checked locally. No such recipe or bound is derived727.

**Validated roots.** Archived
[Arb2.23.0 acb_poly Root-finding](https://arblib.org/acb_poly.html#root-finding),
inspected13November2026, documents rigorous root enclosures and the
isolated-root return count. Complete isolation requires that count to
equal the degree; real-root validation is a separate check. The routine
assumes a squarefree polynomial. Durand--Kerner correction sizes alone
are not rigorous errors. Read the displayed root-inclusion proof and
the find_roots/validate_real_roots contracts. General quadrature gives
simple exact roots only after its support hypotheses are verified.
No successful run, library availability or strict arithmetic cap is
inferred from these interfaces. Reuse719's ball-arithmetic qualifications.

### Bounded specialization proposed, not performed

The one candidate construction is Gaussian compression of disjoint
dyadic spectral blocks of the original positive discrete measure,
with sparse initial blocks retained exactly and a separately bounded
infinite tail. Keep every spectral atom exactly once: place artificial
block boundaries away from atoms, or prove the endpoint ownership.
The finite-block theorem is applied before summing block errors. It
does not require a differentiable G at zero. Do not replace the
discrete spectral measure by a smooth density to use a sample code.

The test must first choose finite block/order/tail parameters and pay
the uniform budget using the inspected bound and C998u Section2.
Then it must specify a finite moment/orthogonal-polynomial construction
that avoids visiting all original spectral atoms. Sources above cover
the standard ingredients; the effective fixed-instance estimates are
the work to be attempted, not certified consequences of their names.
If constructing coefficients, isolating nodes or enclosing weights
needs excessive precision/work, preserve that failure. Numerical fits,
successive-precision agreement and formal small rank are insufficient.

Acceptance needs B^2 sup_[0,ell]|G-Gtilde|<=1e-7 with B=2^23,
including tail and all coefficient/rate errors, positive certified
weights/rates, finite rank, precision/byte bounds, and construction work
within10^8. Count preparation and validation; an eigensolver or root
routine is not one elementary operation. Above-cap work abandons this
construction. Below-cap work pays only kernel preparation and leaves
density quadrature, full h preparation, C(0)/d0 and scalar accumulation
to later work under the same total cap and remaining9e-7 allowance.
An unavailable essential algorithm/hypothesis stops dependent research
and requires a new source gate; it cannot be filled by an unassessed
algorithm during the next attempt.

### Search, overlap, access and routing

Queries included `Koyama exponential sum approximation finite completely
monotonic functions zero interval Gaussian quadrature error bound`,
`exponential sum approximation completely monotone functions bounded
at zero positive weights uniform absolute error`, `Golub Welsch1969
calculation Gauss quadrature rules pdf moments positive measure`, and
`Gautschi orthogonal polynomials discrete measure moments Gaussian
quadrature construction ill conditioned modified Chebyshev pdf`.
The exact series and constants were compared with the canonical local
definition, not inferred from search snippets. No novelty is established.

Plonka--Riebe--Cuyt arXiv:2606.03855 was located as an abstract-level
lead for different kernels; its theorem/proof was not inspected and
it is not an input. No larger survey or best-approximation existence
result is used in place of constructive coverage. The2010 power-kernel
source remains mismatched at zero; the2005 sweep remains reusable only
after kernel/density preparation. Stops724/722 concern different loops,
and all earlier stops617/603/635/640/652/705/712/716/720 are preserved.

The source PDFs were readable through web text. Shell download failed
DNS resolution; arXiv HTML follow-ups timed out, and screenshot calls
returned no visible images. No visual verification or cached PDF is
claimed. DLMF rendered equations were readable despite unsupported TeX
endpoints. These access limits do not block the stated source scope.

This is a local source-coverage advance using known methods, with no
new mathematical lemma, specialized rank, script or scalar. The next
bounded calculation is newly ready for separate approval; it is not
executed727. Mathlib coverage for the full compressed approximation
and supporting general-measure construction was not checked. The
missing justified signed remote-plus-induced S3 domination mechanism
still blocks a creative central-gap nomination; numerical kernel
compression is not that mechanism. STATUS remains IN_PROGRESS.
