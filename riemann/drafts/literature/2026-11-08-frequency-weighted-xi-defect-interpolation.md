# Frequency-weighted normalized Xi-defect interpolation — source comparison

TARGET: Assess primary coverage for a uniform bound |C_y(x)/A_0(y)-C_v(x)/A_0(v)|<=K(1+|x|)^5 exp(-pi|x|/2)|y^2-v^2| for real x and 0<=v,y<=1/2, comparing standard Xi strip estimates and recorded failures.
CHECKED: 2026-11-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched Riemann Xi defect Lipschitz, xi sinhc bound, normalized Xi-defect exponential interpolation, and uniform zeta derivative/convexity terminology; checked the primary defect manuscript and targeted local strip/normalization/ordering records. No inspected source states the exact normalized two-height bound; this does not establish novelty.
SOURCE_EVIDENCE: NIST DLMF v1.2.8 (2026-09-15), 25.4.3/4, 5.11.9 with its bounded-real-part uniformity sentence and 5.11(i)/(ii) conditions, 1.9.30/31 and 1.10.1; Gonek (1984), Section2 (20), p.127 and its complete Cauchy proof paragraph, with its use before (22), p.128. Existing L320 (4)/(6) already supplies the required uniform completed-Xi strip/product envelope; details and source-access qualifications below.
COMPARISON: Exponential decay and analytic derivative control are standard and partly already local. The precise remaining specialization is uniform squared-height division at zero and normalization by A_0 on the real interval. L899's full-L1 estimate alone has no frequency decay; fixed-y source bounds alone do not supply this closed-square assertion. No new growth theorem or sign mechanism is needed.
GAP: A separate mathematical step must prove the displayed bound using the existing enlarged-strip envelope, justify the even-parameter removable case, bound the real normalizer and its squared-height variation, and retain one finite K independent of x,v,y. That result, an effective numerical K, reference margins and all-degree signs are not established by this review.
REASON: Essential source scope is now covered, with L320 reusable instead of reproving strip interpolation or chasing an inaccessible alternate theorem. The result has a plausible absolute interpolation use on frequency bands, conditional on separately proved margins; this licenses a bounded standard specialization, not a creative or signed advance.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED coverage omitted uniform exponential-frequency growth and analytic removal of the squared-height endpoint; L899's ready assessment did not cover these changed hypotheses.
SCOPE: Actual Phi=K_theta(|u|)/2 and C_y,A_0(y) of L898; real x, all 0<=v,y<=1/2, coincident heights and both endpoints, one finite unspecified K. Fixed enlarged complex-height neighborhoods are allowed. No RH, zero simplicity, zero-free strip, logarithmic derivative at Xi zeros, positive reference margin, or complex nonvanishing of A_0 is assumed.
COVERED_TARGET: Specialize L320's uniform Xi strip bound and Cauchy's formula to prove |C_y(x)/A_0(y)-C_v(x)/A_0(v)|<=K(1+|x|)^5 exp(-pi|x|/2)|y^2-v^2| for real x and 0<=v,y<=1/2 with one finite K, including the removable zero-height case.

## What was actually checked

The main unresolved claim is L030–L032/C032a actual-Xi all-degree
mixed positivity. This review addresses only the TARGET. The kernel
constant K_theta and proposed estimate constant K are unrelated.

Read L019/L020's normalization and decay, L898's definitions,
domination, P_y=y C_y and C_0 identity, and L899's statement and
normalization context. No further audit of L899 was undertaken.
After searching for the specific growth claim, read L320's strip
proof through (6), and L461's relevant whole-strip comparison only.
L461's conditional subcritical-strip improvement is unnecessary here;
no new zero-free or reciprocal-series target is being proposed.

Local overlap is substantial: L320 already proves, for fixed R>1/2,

    |xi(sigma+it)| <= B_R (2+|t|)^(7/4+R/2) exp(-pi|t|/4),
    1/2-R <= sigma <= 1/2+R, t real,                       (L320 (4))

and bounds the whole complex-height circle of
H_x(z)=Xi(x+iz)Xi(x-iz) in (6). Its proof explicitly controls the
strip interior by a damped maximum-modulus argument, handles both
signs of t and absorbs bounded heights by entirety. Reuse this
established portion; do not reprove it as a new lemma. Neither its
safe-half-plane anchor nor its witness-cutoff conclusion is needed.
L320's fixed-radius hypotheses allow an enlarged neighborhood of the
closed height interval. No limit R down to 1/2 is requested.

## Primary inputs and exact scope

[NIST DLMF 25.4.3/4](https://dlmf.nist.gov/25.4) states
xi(s)=xi(1-s) and
xi(s)=s(s-1) Gamma(s/2) pi^(-s/2) zeta(s)/2.
These agree with L018/L020 and the normalization in L898. Use the
entire completion at s=0,1; separate singular factors there cannot
be bounded by their individual values.

[DLMF 5.11.9](https://dlmf.nist.gov/5.11.E9) states
|Gamma(a+ib)|~sqrt(2pi)|b|^(a-1/2)exp(-pi|b|/2) as
b tends to either infinity, **uniformly for bounded real a**.
Read that sentence, the sector condition before 5.11.1–3 and the
complex remainder paragraph in [5.11(ii)](https://dlmf.nist.gov/5.11#ii).
This covers fixed real-part intervals at large heights, not gamma
poles at bounded heights. It supplies no sign, zeta lower bound or
permission to differentiate an uncontrolled real asymptotic error.
The existing L320 envelope already combines these standard inputs.

S. M. Gonek, *Mean values of the Riemann zeta-function and its
derivatives*, Invent. Math. **75** (1984), 123–141,
[author-hosted published PDF, p.127](https://sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf#page=5),
Section2, equation **(20)**: for fixed integer nu>=0 and epsilon>0,
|t|>=1/2, the three upper powers for |zeta^(nu)(sigma+it)| are
1/2-sigma+epsilon for sigma<0, (1-sigma)/2+epsilon for
0<=sigma<=1, and epsilon for sigma>1. Read the complete following
paragraph applying Cauchy's derivative estimate to the nu=0 bound
on a small disk, referring to Titchmarsh pp.81–82. The use of (20)
in the three maxima before (22), p.128, also checks its bounded-strip
role. Unlike adjacent log-derivative estimates, (20) requires neither
selected heights nor RH. Reuse the earlier Gonek assessments; this
review fills the additional strip/endpoint comparison. Titchmarsh's
pages were not separately inspected. This is supporting classical
coverage; the future specialization can use L320 without needing
any new zeta-derivative estimate.

[DLMF 1.9.30/31](https://dlmf.nist.gov/1.9#iii) gives Cauchy's
integral formula and its nth-derivative formula for a function
continuous within/on a simple closed contour and analytic inside,
with the evaluation point inside. [1.10.1](https://dlmf.nist.gov/1.10.E1)
gives the Taylor expansion on an analytic disk, of at least that
radius of convergence. These are the needed fixed-order and
removable-parameter tools. A modulus-square expression is not itself
a holomorphic complex-parameter extension; the entire product H_x
must be used. Evenness and the division at zero still need their
local quantitative proof. No new such proof is supplied here.

All DLMF inputs were inspected as version **1.2.8**, release
15 September 2026, accessed 8 November 2026. The standard results
are to be cited, not reproved. Mathlib coverage for the full displayed
bound and its analytic supporting tools remains **not checked**;
no absence claim is made.

## Duplicates, failures and limits of the comparison

The inspected primary raw manuscript by Leonard van Hemert,
*Finite Positivity Certificates and a Cross-Endpoint Obstruction for
a Riemann Xi-Defect Kernel*, title date 20 July 2026,
[Sections2–3](https://raw.githubusercontent.com/LeonardSEO/certified-riemann-xi-positivity/main/paper/main.tex),
labels `lem:defect`, `eq:Py`, `eq:C0`, provides the same defect
identity and zero-height value. Its domination and endpoint arguments
are already covered by L898. Exact-text checks for Lipschitz and
Stirling found no match; the searched exponential passages concern
moments/compact convergence, not this estimate. This unversioned raw
source has 868 browser lines; no immutable commit or review status
was verified. Its result is not evidence for a uniform frequency
interpolation constant.

Reused the ready Planat source assessment in
[the paired-tail comparison](2026-10-31-nonlocal-paired-tail-remainder-comparison.md),
especially its inspected Lemma7/proof: it gives a fixed-y polynomial
exponential upper bound with a Cauchy radius shrinking with y, and
no signed remainder. It does not settle the uniform y=0 difference.
No further Planat source extraction is necessary for this contrast.

Read L309/L312's stated ordering results and relevant failure proof:
variance ordering does not sign an oscillatory covariance; L312's
qualified negative derivative does not refute the present absolute
interpolation target. L898's fixed cross-endpoint polynomial stop
remains intact. The completion-stripped absolute-envelope stop is
about a different residual/contraction budget; an exponential upper
bound here supplies no improvement to that stopped mechanism.
The targeted local search located no existing normalized two-height
frequency estimate. This is not a novelty certification.

## Bounded mathematical continuation and decision test

The COVERED_TARGET is a standard specialization, classified as
REPRODUCTION if completed. Its essential local inputs are L019,
L020 through L898, the strip/product-envelope portion of L320,
and audited L899 as the unweighted benchmark. No cross-notebook
input is used.

Future proof obligations, not results of this literature turn:

1. Use one fixed enlarged height disk and L320's existing envelope.
   Check that the product power and every fixed-radius Cauchy loss
   fit the stated power 5 while preserving exp(-pi|x|/2), including
   negative and bounded x. Do not silently weaken either threshold.
2. Use the entire even product H_x, the existing identity P_y=y C_y
   and Taylor/Cauchy control to justify squared-height regularity
   uniformly through zero. Merely dividing an estimate by y or
   citing pointwise removability is insufficient.
3. Normalize on the real height interval only. Use A_0>=A_0(0)>0
   and the theta moment domination to bound its squared-height
   variation; do not assume A_0 has no complex zeros. Prove one K
   common to x,v,y, retaining both numerator and denominator terms.

Continue only if these obligations give the **original** bound.
Preserve a failed estimate and abandon this proposed envelope if
fixed-radius control cannot retain its power/rate or if an unproved
sign/nonvanishing hypothesis becomes necessary. No numerical K or
finite certificate is requested. The anticipated use is comparison
with a separately paid positive reference margin on frequency bands;
without that margin even a successful absolute estimate yields no
sign, relative control near small values, all-degree theorem or RH.

The source comparison is now complete and SPECIALIZE is ready for
the exact COVERED_TARGET. This file does not prove that target.
The supervisor may separately approve this newly written continuation;
no extra approval loop is requested on mathematical grounds. A
creative central mechanism is not nominated: this is routine analytic
specialization and this bounded review has not supplied an independent
signed margin mechanism.

## Access record and unused leads

The first Gonek open timed out; a later primary PDF text retrieval
succeeded, including all three cases of (20) and its proof paragraph.
A screenshot request yielded no usable displayed image and another
timed out; shell retrieval failed DNS. No claim rests on a screenshot.

Rademacher (1959), Theorem4 was located through a secondary lead,
but the original EuDML endpoint returned 403, the Springer PDF route
returned a subscription page, and the GDZ route was inaccessible.
Its theorem was **not inspected or imported**. This is a nonessential
alternate lead because the canonical L320 envelope is available;
do not begin a dependent retrieval loop or use the secondary formula
as primary evidence.
