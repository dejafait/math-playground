# Nomination655: certify the full residual after exact singular subtraction

TARGET: Assess graded-panel certification of all three full projected residual norms in C998a to enclosure width at most 1e-4 each, paying jump/log cross terms, forcing suffix and projection coefficients.
CHECKED: 2026-11-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review656 searched verified quadrature of logarithmic endpoints, graded meshes, Petras integration, Gaussian ellipse bounds and ball-arithmetic error propagation; read the primary statements and relevant proof cases below. Scoped local comparison reused652/653, C998a, C999 Sections3-4 and stop652; no completed matching norm certificate was found in those inputs. No novelty inference.
SOURCE_EVIDENCE: Trefethen, Approximation Theory and Approximation Practice (2013), Chapter19 Theorem19.3/(19.8) and full proof; Johansson arXiv:1802.07942v1 Sections2-2.1; Moczurad--Zgliczynski arXiv:1603.03945v1 Sections3.1-3.4, Lemma4, Definition5, Theorem5/Lemma7 with proofs; Johansson, Arb paper, Sections3.2,4,5-5.3. Exact URLs and version qualifications follow; retain652/653 and audited C998a/C999 operator inputs.
COMPARISON: Known validated quadrature covers bounded holomorphic interior panels with certified complex bounds and scalar evaluations. Its global boundedness and oracle/complexity hypotheses do not automatically cover the logarithmic full residual or follow from H1. Audited local endpoint and forcing-tail bounds supply assessed ingredients for a later specialization, not an executed norm certificate or practical work guarantee.
GAP: Specialize a complete error ledger to the three frozen full residuals: endpoint/interface neighborhoods, interior complex bounds, complete forcing suffix, scalar coefficients, projection and nonnegative square root. Give an explicit finite work estimate before a large run; include inner scalar work. No local error rule, analyticity proof, schedule, cost bound or norm enclosure is derived656.
REASON: Accessible primary error theorems and the already audited effective local action bounds suffice to license a separate bounded REPRODUCTION attempt on the unchanged target. The difference is quantitative local assembly and cost, not a missing general quadrature theorem. Newly ready coverage requires separate approval; do not repeat the uniform-action prescription.
LITERATURE_REASON: The target changes from existence of a finite H1 remainder to certified full residual-norm integration with scalar uncertainty and quantitative cost, which ready652/653 did not assess.
SCOPE: Unchanged complex H0, B0 with delta=.01,m=286,J=14, C999y's exact X, C999q's exact neutral completion and the pinned652 free middle dyadics. No parameter retuning, alternate reference, sign theorem or global positivity claim.

This is a nomination only. Audit655 established no new integration rule,
error bound, full residual norm or action pairing. The next turn should
inspect primary theorem hypotheses and relevant endpoint/error proof
cases, compare them with this exact function class, and assess the
stated TARGET. It must not implement or derive the uncovered mathematics
in the source-review turn.

The main gap is L030-L032/C032a actual-Xi positivity; S3's signed
remote-plus-induced block remains unpaid. A complete full-residual
enclosure could support C999's inverse-action error estimate and later
signed inverse pairings on this fixed three-column test. Even a successful
test on these three columns would leave the full endpoint family, mixed
and higher bands, C744q/H2, non-neutral coverage and global assembly open.
There is no justified new sign-producing central mechanism supplied by
this regularity audit. Its concrete blocker is the absence of a complete
quantitative residual certificate; routine numerical specialization is
not classified as creative research.

The objects are exactly r_j=P0(Tf_j+T*h_j)-B0q_j from C998a, j=0,1,2.
The representation r_j=sigma_j+J_j+R_j is an identity. Its components
must not be treated as orthogonal: a norm certificate must pay every
cross term or otherwise enclose the square of the complete residual.
The603 candidate interfaces are exact computable locations, not rounded
grid assignments. The endpoint logarithms are L2 but not H1, and their
coefficients, the finite jump values, the full forcing suffix and the
two projection moments need actual enclosures with propagated errors.
The large H1 bound is not a small residual bound. Its adequacy for a
useful panel rule is an open test, not an asserted benefit of this method.

The proposed width1e-4 measures uncertainty in each residual norm. It
does not assert ||r_j||<=1e-4, nor that this precision pays a later matrix
margin. Any eventual result must report both norm bounds and uncertainty,
the actual work/error ledger and all unresolved pairing errors. Primary
source comparison must justify endpoint handling, subdivisions at uncertain
interfaces, square-root/norm enclosure at zero, and scalar error propagation.
Avoid attributing a rate at an excluded endpoint to an interior theorem.

Continue only if primary coverage supports a complete finite error rule
and a discriminating work estimate for these fixed data. Missing endpoint
or scalar control blocks dependent computation. An impractical sufficient
work bound stops that prescription without proving a necessary complexity
barrier or a large residual. Preserve652's recorded uniform-action stop
(1.7e19 to1.3e20 sufficient output cells) and all598/600/603/635/640
failures; do not rerun that prescription at a changed tolerance.

Essential local inputs: C998a including audit655 and the complete654/655
rational certificates; C999/audit650 and C999z/audit646; C999y/audit642
exact X and C999q exact Z; C744v's complete operators and C744w/z,
C999k's retained arithmetic, analytic/source-to-Xi, whole-neutral-core
and unreplayed c_* contracts. The trial archive remains
`scripts/separation-seven/frozen-reference-proposal-652.npz`, SHA256
`2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6`.
No cross-notebook theorem input. Full matching Mathlib coverage remains
unchecked; unknown coverage is not evidence of absence.

## Completed source comparison656 — 12 November 2026

The nomination above records the question as it stood655. This completion
changes its source decision only. The target, three columns, exact neutral
completion and pinned trial archive are unchanged. There was no new lemma,
mathematical script, residual evaluation or derivation of a local error rule.
The local progress is removal of the essential source-coverage gate; no
progress beyond the inspected numerical-analysis methods is claimed.

### Search, local overlap and source access

Queries included `rigorous numerical integration logarithmic endpoint
singularities interval arithmetic Petras Johansson Arb`, `graded mesh
quadrature weakly singular endpoint logarithmic singularities error bound
theorem Sidi`, `Petras 2002 self validating integration piecewise analytic
functions theorem ellipse error bound pdf`, and `Trefethen approximation
theory approximation practice chapter 19 theorem 19.3 pdf quadrature
analytic ellipse 64`. Follow-up searches concerned ball-arithmetic error
propagation. Search snippets and abstracts were discovery aids only.

Read C998a's complete representation and audit655, especially Sections3-5;
C999 Sections3-4, including (12)-(22); assessment652/comparison653; and
stop652. A scoped search of the12November literature and attempt records
for graded integration, Petras, tanh-sinh and validated quadrature found
the current nomination and earlier unimplemented alternatives. This is
an overlap check in the relevant route, not an exhaustive novelty search.
C999 already proves effective full-action/norm computability. Repeating
that existence argument or its stopped uniform output rule would not
answer the changed quantitative target. The new test concerns a different
panel error prescription and its actual sufficient cost.

The original Petras2002 article (JCAM145,345-359,
[DOI](https://doi.org/10.1016/S0377-0427(01)00586-6)) was located,
but the direct full-text retrieval failed. Its complexity theorem is not
imported from a search extract. Accessible primary alternatives below
cover the required interior error statement and conditional termination.
Sidi's endpoint-asymptotic and BEM/product-integration papers were leads;
their full theorems were not inspected and are not inputs. No essential
source blocker remains for the bounded specialization specified here.

### Inspected primary statements and proof cases

**Interior error.** Trefethen, *Approximation Theory and Approximation
Practice* (2013), Chapter19 Theorem19.3, (19.8),
[book-content PDF hosted at ETH](https://people.math.ethz.ch/~hiptmair/Seminars/RAP_22/TRE13.pdf),
PDFpp153-154: an analytic continuation to the open Bernstein ellipse
E_rho, rho>1, with modulus bounded by M gives, for the **(n+1)-point**
Gauss rule and n>=1,

    |I-I_n| <= (64/15) M rho^(-2n)/(rho^2-1).

Read the complete proof, including positive weights, exactness through
degree2n+1 and the even Chebyshev tail. This is an interior theorem,
not an endpoint-singularity theorem. Retain its point-count convention
and the affine interval factor when applying it. The retrieved PDF has
chapter-local pagination; theorem/equation numbers identify the statement.
The [author's book page](https://people.maths.ox.ac.uk/trefethen/ATAP/)
identifies the2013 edition and later errata. Its differentiable-quadrature
errata do not replace this inspected analytic statement. No general
quadrature theorem needs reproof.

**Validated evaluator and stopping precision.** Johansson, *Numerical
integration in arbitrary-precision ball arithmetic*,
[arXiv:1802.07942v1](https://arxiv.org/pdf/1802.07942v1),
22February2018, Sections2-2.1, pp2-4: the evaluator must enclose values
on complex boxes and certify analyticity when requested. Read every
algorithm branch, including direct enclosures and bisection, then the
tolerance and evaluation-limit discussion. The returned radius, not
the requested tolerance, determines achieved accuracy; limits or uncertain
parameters can prevent the goal. The quoted typical complexity is not
a work bound for these residuals. This supports a certified implementation
interface, without supplying its missing local evaluator or analytic
neighborhoods. No timing from its benchmarks is transferred here.

**What a termination theorem actually assumes.** Moczurad--Zgliczynski,
*On the Petras algorithm for verified integration of piecewise analytic
functions*, [arXiv:1603.03945v1](https://arxiv.org/pdf/1603.03945v1),
Sections3.1-3.4, pp5-7: read the full algorithm, Lemma4 proof, Definition5,
Theorem5 proof and Lemma7 proof. Bounded piecewise-analytic input needs
valid real bounds and compatible analyticity/complex-bound oracles.
Lemma4 pays accepted-panel quadrature and discarded-panel mass separately;
Theorem5 gives termination under compatibility; Lemma7 uses compactness
for a fixed analytic subinterval. They supply neither explicit local
constants nor the cost of the oracles. The introduction explicitly
excludes subroutine costs from its evaluation-count analysis. Its raw
global boundedness assumption excludes an unpaid logarithmic endpoint.
The URL identifies v1,12March2016, while the retrieved PDF internally
says21September2018; pin this URL, section and statement numbering.
No generic logarithmic-squared complexity claim is imported.

**Scalar inclusion arithmetic.** Johansson, *Arb: Efficient
Arbitrary-Precision Midpoint-Radius Interval Arithmetic*,
[author PDF](https://fredrikj.net/math/arbpaper.pdf), Sections3.2,4,5-5.3,
pp6-9: read the radius/rounding assumptions, multiplication enclosure,
definition of interval extension, propagated plus rounding error, and
branch-cut handling. Composed interval operations preserve inclusion;
they do not automatically pay a discarded series, quadrature error or
wrong branch. Input uncertainty and cancellation can inflate the result.
The author-hosted file has no pinned revision identifier here; these
section/page locators describe the retrieved12-page text. This supports
error propagation only, not a tested build or completed scalar certificate.
The existing C999(19) digamma recurrence/sector remainder remains the
assessed diagonal rule, so a new special-function formula is unnecessary.

The current official [FLINT integration API](https://flintlib.org/doc/acb_calc/integrate.html)
and [evaluator contract](https://flintlib.org/doc/acb_calc/acb_calc_func_t.html)
were read as implementation guidance, not substitutes for the primary
theorem. They require the caller to truncate/transform improper endpoints
and report analyticity correctly. The documentation is marked3.7.0-dev
and warns of a major, partly generated revision. In particular use the
inspected primary theorem's point-count convention. The
[official tutorial](https://fredrikj.net/fdoc/html/tutorials/numerics/integrals.html)
states that its double-exponential example does not enclose heuristic
discretization/truncation errors. It cannot serve as this certificate.

### Exact applicability and difference left for the mathematical turn

The sources license testing **graded interior panels with explicit excluded
neighborhood bounds**, not feeding an unbounded or discontinuous residual
to an analytic quadrature theorem. C998a supplies the exact jump/log split,
all603 candidate interfaces and finite ordinary H1 bounds. H1 alone
does not imply holomorphic continuation or a useful high-order rate.
The later attempt must establish every local hypothesis it uses from
the explicit fixed operator formulas; none is inferred from the sources.

The approved specialization has the following complete set of obligations:

1. Enclose and separate the exact computable interfaces. Choose panels
   with certified endpoints lying in one formula branch, or isolate
   uncertain interfaces in neighborhoods with a paid integral bound.
   Merely splitting at a rounded event does not certify the omitted strip.
   Do not continue a branch through a jump or through the parity midpoint.
2. Pay both logarithmic endpoint neighborhoods explicitly, including their
   interaction with the regular part and all other residual terms. Reuse
   C999(14)'s exact logarithmic-square majorant and C998a Sections3-5's
   full bounds; any restriction or combination needed for the new norm
   rule is the local specialization still to prove. A global L2 bound
   alone cannot certify an arbitrarily short discarded interval. Neither
   a zero endpoint sample nor H1 for R makes the full residual bounded.
3. On every retained panel, give a complex neighborhood, analytic
   integrand and certified modulus bound. For a norm, pointwise complex
   conjugation is not holomorphic. Justify a real-valued formula for these
   frozen data or a holomorphic extension whose real trace is the full
   modulus square before using the imported theorem. Keep the complete
   square of sigma+J+R; if it is expanded, pay every cross term.
4. Provide certified point and box evaluations, including the Carleman
   input integral, finite neutral coefficients, all four finite E products,
   h_m, finite diagonal and translations. Pay any inner quadrature and
   argument uncertainty before claiming an outer quadrature enclosure.
   A complex bound for a truncated forcing prefix must not be presented
   as a bound for the full kernel. C998a(18) and its explicit real suffix
   bound are ready local inputs; extending them to each chosen complex
   neighborhood is part of the quantitative specialization.
5. Pay the two exact projection moments and the positive Gram determinant.
   C999(21)'s already assessed norm/projection identity is an available
   alternative to explicitly assembling projected scalar coefficients;
   justify its use on the full data and propagate interval uncertainty
   through the subtraction and two-by-two solve. Saved floating-point
   moment cancellations are not enclosures. C999's interval clipping to
   nonnegative squared norms and nonnegative square root supplies the
   existing zero-safe norm convention; verify the resulting norm width,
   not just the squared-integral tolerance.
6. Give a finite error/work ledger before a large computation: interface
   precision, endpoint cutoffs, panel count and degrees, inner scalar
   integration work, forcing cutoff, coefficient precision and projection
   work for all three columns. Count oracle work, not only calls. A later
   prototype must print achieved norm intervals and actual widths if it
   executes, and preserve complete certificates on disk. Requested
   tolerance, successive-grid agreement and sampled residuals do not pass.

These are approved questions, not newly established formulas, bounds or
claims of tractable execution. They identify the difference from the
standard theorems and justify a local REPRODUCTION attempt rather than a
reproof of quadrature or another literature-only search. The current
sources do not warrant importing a preexisting theorem that these exact
three norms have already been certified to width1e-4.

Continue if the complete ledger yields a proved refinable rule and a
discriminating finite work estimate. Execute only within a stated bounded
work plan. Missing local endpoint/scalar/analytic control stops that
application; an impractical sufficient estimate stops that prescription,
without proving necessary complexity or a large residual. No retuning of
the stopped652 uniform-output scheme is authorized by this assessment.
No full norm, inverse pairing or sign follows from approval of this test.

The essential input IDs and contracts are those in the nomination above;
in particular C998a/audit655, C999/audit650, C999z/audit646, C999y/audit642,
C999q's exact Z and C744v/w/z remain fixed. All source-to-Xi, whole-core,
arithmetic and unreplayed c_* qualifications remain. Full matching Mathlib
coverage was not checked; no absence claim is made. Canonical local proof
and citations belong in lemmas only if a later approved attempt establishes
them; this literature-only turn changes no lemma or mathematical script.

SPECIALIZE is newly written656 and needs the supervisor's separate approval
before research. The saved TARGET remains the sole next action. Once
approved, the default is a bounded proof attempt on this standard method,
not further browsing without a changed essential source question. This
review found no justified new sign-producing mechanism for the central S3
gap: regularity and numerical enclosure remain preparatory, and quantitative
residual/pairing control is still the blocker to a creative nomination.
