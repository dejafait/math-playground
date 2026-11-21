# Resummed Perron-Cauchy construction: bounded continuation

TARGET: Construct a locally convergent, explicitly degree-resummed Perron-Cauchy representation of the actual G_1 and G_2, retaining every endpoint jump and continuum compensator, or isolate the failed uniform-limit step.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step280's exact-target, stronger-result and moving-cutoff searches in review279; no matching four-endpoint representation was inspected. No novelty claim. Separate source approval completed in recovery step281; direct primary URLs are recorded below.
SOURCE_EVIDENCE: Montgomery-Vaughan MNT I section5.1 Theorems5.1-5.2/Corollary5.3 pp137-140 https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/09.0_pp_137_167_Dirichlet_series_II.pdf ; DLMF https://dlmf.nist.gov/18.12.E13 and https://dlmf.nist.gov/18.14.E8 ; Lagarias2007 AppendixA pp1737-1738 https://www.numdam.org/article/AIF_2007__57_5_1689_0.pdf ; reuse review279, canonical Gorodetsky input and L985/L989. Direct URLs checked step281; no essential unread source for this bounded construction.
COMPARISON: Known tools give fixed-argument extraction and finite-height complex-coefficient inversion with near/far errors and half weights. They do not state the degree resummation or uniform height limit; import the tools and justify only their joint specialization.
GAP: Prove a nonzero initial analytic domain and an explicit degree kernel coupled to actual -zeta'/zeta, with a locally uniform cutoff limit and all endpoint/compensator terms. Continuation, zero singularity survival, signs and RH transfers remain outside this approval.
REASON: This testable analytic interface may expose where signed cancellation is lost before another prime estimate. It is known-route development, not creative discovery or repeated direct interval payment. No mathematical result is derived here.
SCOPE: Actual Lambda including all powers, n>=2, r=1,2, exactly G_r below; full-right/excluded-left endpoints; fixed coefficient contour and initially an absolute-convergence Perron line. No RH, rightmost zero, simplicity, nonresonance, clearance or infinite-zero exchange.

## Exact object, inputs and intended use

Use exactly L985's polynomial, equivalently

    K_m(t)=[L_(m-1)^(2)(t)-1]/(m-1),
    T(f;u,v)=sum_(exp(u)<q<=exp(v)) Lambda(q)*f(log q)/q
                                                   -integral_u^v f(t)dt,
    D_(n,r)=T(K_(n+r);n+r,2*(n+r))-T(K_(n+r);n,2*n),
    G_r(z)=sum_(n>=2) D_(n,r)*z^n, r=1,2.

These are definitions; G_r remains formal. No disk or contour
identity has been proved in the literature turn. L985 supplies the
definitions and existing kernel estimates; L989 supplies global
normalization and endpoint conventions. Its finite-zero identity
does not replace D. Precise primary citations and proof-case scope
are in [review279](2026-11-10-moving-band-degree-germ-review-279.md).
Cauchy's coefficient formula, geometric power series and dominated
convergence are standard named tools; verify their hypotheses for
the actual family. General Perron/Laguerre reproof is unnecessary.

The main gap remains actual-Xi positivity L030-L032/C032a and signed
forcing L966/L968. The interface could support a later singularity
test of actual corrections before L993 recovery. All three outputs,
other zeros, both complements and L984(H) remain unpaid.
L990/C990a/L993 are context only; pull no n-dependent matrix through
the series. No cross-notebook input. Full matching Mathlib coverage
is unchecked and unknown.

## One bounded construction attempt

Retain finite degree and finite Perron height first. Use a fixed
Laguerre coefficient contour; verify a common absolute-convergence
line for its complex arithmetic coefficients. Sum the degree
dependence explicitly on a justified small domain, retaining the
normalization, -1 and all four endpoints. Then justify the locally
uniform limiting operation, including near-prime-power terms and
both full-weight corrections. Keep the continuum compensator exact.
This is a proposed method, not a formula or asserted estimate.

Exhibit an explicitly degree-resummed kernel coupled to actual
-zeta'/zeta (or an equivalent justified contour interface), not the
original degree series disguised under an integral. Give a checkable
nonzero disk, order of limits and complete bounds. A finite-height
contour requires its full remainder and an exact limiting statement
recovering G_r. Do not identify Perron height with a closed spectral
cutoff without proving that passage.

Continue only if the test succeeds or a concrete uniform-limit
obstruction changes the route. Save partial reasoning if incomplete;
do not erase the difficult term or infer impossibility from a failed
bound. Do not start all-zero singularity detection in this attempt:
it needs a later assessment for the actual representation, including
remainder analyticity and cancellation. A small disk alone gives no
RH estimate. Expected classification is REPRODUCTION.

Creative routing remains unjustified without the explicit signed
interface and a discriminating remainder-analyticity test. Recommend
proof_attempt/development, deep_research/xhigh, for the joint uniform-
limit construction; the separate source approval is recorded below.

## Recovery source approval — step281, 10 November 2026

LITERATURE_REASON: Supervisor identified missing direct primary-source URLs
in this ready assessment. Repair provenance and approve the unchanged target;
no expanded literature search or new mathematics is needed.

The direct [author-hosted Montgomery–Vaughan chapter](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/09.0_pp_137_167_Dirichlet_series_II.pdf#page=2)
was accessible. Rechecked printed pp138-140: Theorem5.1 requires
c>max(0,sigma_c), x>0 and a symmetric height limit with half endpoint
weight. Theorem5.2 requires c>max(0,sigma_a). Its two near ranges
exclude equality with x; Corollary5.3 retains that exclusion. The
far-range estimates and the near-range indentation are retained from
review279. None is a degree-uniform theorem for this moving family.

Rechecked the live [Laguerre generating function](https://dlmf.nist.gov/18.12.E13),
valid for |w|<1, and [global inequality](https://dlmf.nist.gov/18.14.E8),
valid for real t>=0, alpha>=0 and nonnegative integral degree.
Their alpha=2 use is within scope; they do not justify moving-endpoint
resummation. Reuse the source versions and precise formulas recorded
in review279 and L989; no general reproof is proposed.

The [Lagarias primary PDF](https://www.numdam.org/article/AIF_2007__57_5_1689_0.pdf#page=49)
is accessible; reuse review279's inspected AppendixA regularization
comparison unchanged. The finite weighted input remains
[Gorodetsky v6, Lemma5.2 and AppendixA](https://arxiv.org/pdf/2211.08973v6#page=15),
with its exact hypotheses and s=1-only notebook use recorded in
[the canonical source input](../../foundations/2026-11-10-finite-weighted-landau-input.md).
No complex-parameter extension of that specialization is approved.

Approval: SPECIALIZE for precisely TARGET/SCOPE above. The known-tool
coverage is sufficient to attempt the construction and isolate any
unpaid uniform limit. No representation, convergence disk, sign or
RH consequence was established here. This is a STALLED process repair,
not new mathematical or bibliographical evidence changing the route.
The next invocation can attempt the same target under this assessment;
all-zero continuation and singularity survival still require later review.
Full matching Mathlib coverage remains unchecked.
