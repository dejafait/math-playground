# Positive annular gluing — first boundary-moment discriminator

TARGET: Assess the first nonconstant boundary-moment obstruction to gluing an L855 positive germ to a prescribed smooth positive outer collar in its primitive chart, testing whether positive total Stokes flux can coexist with impossibility of any smooth interpolation having nonnegative full density and positive original angular determinant.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed bounded searches for Cauchy-Green on multiply connected domains, positive complex first moments, truncated moment cones, and prescribed-boundary positive/symplectic annuli; inspected the primary sources below and the local free-germ/fixed-cutoff stops. No inspected theorem supplies the joint prescribed-collar and original-angle conclusion; search failure is not novelty evidence.
SOURCE_EVIDENCE: Lebl, Tasty Bits of Several Complex Variables v4.4 (31 May 2026), Theorem B.2 p206, orientation convention p205, Theorem4.1.1 and punctured-domain proof pp130-131, Theorem4.2.1 pp132-133, https://www.jirka.org/scv/scv.pdf ; di Dio–Schmudgen, arXiv:1809.00584v1 (3 September 2018), Definition5 p5, positivity (5) pp4-5, Theorem19/proof pp9-10, Proposition24(i),(vii)/proof p12, https://arxiv.org/pdf/1809.00584v1 ; reuse L855's already inspected local-coordinate inputs.
COMPARISON: Green–Stokes supplies boundary integral identities for smooth planar annuli, and positive-measure theory supplies necessary affine moment tests. These known inputs cover the general method, not admissible actual-chart collar data or positive angular projection. L855's free outer data and the exhausted fixed-cutoff linear route do not settle this relative test; no new gluing result or counterexample was derived.
GAP: Specialize the identities with correct primitives/signs for only the constant and first holomorphic moment; determine whether collars satisfying all chart, full-density and angular hypotheses can violate the necessary affine moment test while passing total flux. If no such independently certified test emerges, stop this discriminator; passing moments is not an existence theorem.
REASON: Essential source coverage for this finite necessary-condition test is now available. A separate mathematical attempt may apply these known tools; neither the source review nor a moment-measure representation approves smooth interpolation or global contour assembly.
LITERATURE_REASON: Prescribed outer collars and simultaneous original-angle transversality changed the hypotheses beyond the ready free-germ assessments; this completes the missing comparison rather than repeating ready-target browsing.
SCOPE: Exactly TARGET, for one fixed pair and finite n>=1 from L855, on a small annulus inside its common inverse chart; no fixed L849 cutoff, L853 crossing, full torus, other order/shift, or new zero-location input.

## Precise proposed boundary problem

Essential local inputs are L855, with G,R,C and the full form as in
L775/L847. Keep the explicit hypotheses zeta,eta nonzero,
G(zeta)=0 of finite multiplicity n>=1, G(eta)(zeta-eta)!=0.
Use L855's jointly holomorphic coordinate v=V(w,z_2) and inverse h;
the full form in this chart is w^n dw wedge dv. Fix small radii
0<r_0<r_1 so the proposed data remain in this inverse chart.

The inner collar data are the already audited L855 surface. The
outer collar data are a prescribed C-infinity surface of the form
(zeta+w,h(w,v_out(w))), defined near |w|=r_1. Hypothesize that
these data remain in the chart, have strictly positive real full
density, and positive determinant of the original angular projection.
These are input hypotheses, not claims about any particular existing
global contour. An interpolant must agree on open collars at both
ends, stay in the chart, and have nonnegative real full density and
positive angular determinant everywhere between them. C-infinity
regularity is allowed; analyticity across fixed open collars is not
imposed. Every zero remains in the original full-form convention.

The bounded proposed discriminator is the constant and first
nonconstant holomorphic boundary moment only. Source review should
first specify the relevant primitive, boundary orientations, and
moment identity from an inspected primary theorem, including its
regularity and annular-domain hypotheses. Then identify whether
positivity imposes a first-moment constraint stronger than a positive
real total Stokes boundary period. The later mathematical test would
seek admissible collar data passing that scalar period test but
failing the first-moment constraint, or an applicable extension
theorem showing this proposed obstruction cannot distinguish them.
Neither identity nor inequality nor such data are derived here.

Continue only with a precise known theorem application or a separately
approved finite moment test. A compatible integral alone is not an
interpolation proof; numerical or formal boundary data are not a
certified counterexample. If the first moment adds no independently
checkable constraint, stop this discriminator rather than automatically
escalating through an unbounded list of higher moments.

## Relevance, comparison and unresolved assumptions

A positive germ cannot yet be inserted into a larger contour with
fixed boundary data. A genuine boundary obstruction could rule out
an otherwise unjustified local-to-global patching rule; a sufficient
relative result could supply a component for later assembly. Either
outcome leaves actual global matching, exchange compatibility, all
orders/shifts and L030–L032/C032a mixed positivity unresolved.

Three continuations were compared when nominating this target:

1. Repeating free primitive/monomial germs: L855 now passes its first
   audit, but varying the same free model does not address outer data.
2. Returning to fixed-cutoff pointwise inversion, jets or narrow-strip
   barriers: the preserved third-exploration stop remains applicable;
   this nomination supplies no new exterior barrier or range inverse.
3. Testing prescribed annular data through boundary moments: selected.
   It changes the controlled quantity and boundary quantifiers, uses
   the exact nonlinear form, and can fail or succeed independently of
   solving the parked full-torus linear equation.

At nomination no central creative mechanism was approved. The completed
comparison below prepares a known-tool specialization only; it does not
nominate a creative proof mechanism. Full matching Mathlib coverage is
unchecked. No cross-notebook input, mathematical script or lemma was
added in this source-review turn.

## Completed primary-source review — 6 November 2026

The nomination above is retained as the problem specification, not as
an established obstruction. The following source review changes its
gate from REVIEW_REQUIRED to SPECIALIZE; all mathematical application
obligations remain for a separate turn.

### Boundary identity and annular hypotheses

Inspected Lebl's [Theorem B.2 and orientation convention,
pp205-206](https://www.jirka.org/scv/scv.pdf#page=205), and
[Theorem 4.1.1 with its proof, pp130-131](https://www.jirka.org/scv/scv.pdf#page=130),
in v4.4. For a bounded open planar set U with positively oriented
piecewise-C1 boundary, continuous coefficients with bounded continuous
first partials satisfy

\[
 \int_{\partial U}(f\,dw+g\,d\bar w)
 =\int_U(g_w-f_{\bar w})\,dw\wedge d\bar w,
 \qquad dw\wedge d\bar w=-2i\,dx\wedge dy.
\]

No simply connected hypothesis occurs. Boundary winding is one inside
U and zero outside its closure. The punctured-domain proof explicitly
subtracts the counterclockwise inner-circle integral. Smooth collar
data and a smooth interpolant on the closed annulus satisfy the
regularity requirement. The prospective application is to the
coefficient of a one-form f dw formed from the prescribed chart data;
its primitive and sign for each of the two weights must still be
checked. No specialized moment identity is proved here.

Also inspected [Theorem 4.2.1, pp132-133](https://www.jirka.org/scv/scv.pdf#page=132):
its compact-support existence conclusion assumes complex dimension
at least two. It is not an existence theorem for our planar unknown.

### Positive-measure input, not a surface extension theorem

Inspected di Dio and Schmudgen's author preprint
[*The multidimensional truncated Moment Problem: The Moment Cone*,
arXiv:1809.00584v1](https://arxiv.org/pdf/1809.00584v1).
Definition 5 (p5) treats finite real measurable functions and positive
measures for which they are integrable. Positivity (5) and
Proposition 24(i) (p12) require a representing functional to be
nonnegative on every nonnegative function in their real span.
The relevant proof integrates such a function against a positive
measure. Proposition 24(vii) additionally assumes a locally compact
Hausdorff space, continuous functions and a strictly positive member
of the span; its proof uses a positive lower bound on a neighborhood
to locate support when an integral vanishes.

Theorem 19 (pp9-10) gives at most m atoms for m measurable test
functions. Its proof treats interior points by separation and boundary
points by dimension reduction. This does not produce a smooth density.
For the intended later test, use the closed annulus with its Borel
sets and test functions 1, Re(w), Im(w). These are bounded and
continuous. A hypothetical smooth nonnegative full density would be
a finite positive measure. Application to boundary data is still due;
no first-moment violation is established here.

### Bounded search, duplicates and unimported leads

Queries actually submitted included:

- `Cauchy Green formula multiply connected domain smooth boundary dbar integral theorem`;
- `positive measures complex first moment convex hull truncated moment problem theorem`;
- `prescribed boundary symplectic surface annulus positive area extension obstruction graph`;
- `symplectic surfaces prescribed boundary relative h principle positive graph annulus`;
- `Cauchy Green positive density holomorphic boundary moments prescribed dbar`.

The first searches located the inspected Green and moment-cone sources.
Boyd–Vandenberghe's author-hosted convex optimization PDF was a
barycenter lead, but both direct fetches timed out; its search excerpts
are not imported. This is not an essential blocker because the
inspected moment-cone source supplies the needed positivity input.
The prescribed-boundary searches also returned h-principle discussions
and Haskins–Pacini, arXiv:math/0609352v4. Only the latter's landing page
was opened: no theorem or proof from it was read or imported. A generic
relative h-principle cannot be substituted on the strength of a snippet.
No claim of an exhaustive extension-theorem classification is made.

Read L855's hypotheses, full-form primitive chart, monomial model and
original-angle calculation, and L847's full pullback convention.
The local comparison also checked
`ATTEMPTS/2026-11-06-free-germ-boundary-scope-stop.md` and
`ATTEMPTS/2026-11-06-collar-transition-inverse-stop.md`, together with
the existing free-germ/transverse-divisor assessments. These preserve
both the valid local result and prior transition singularities; no
source comparison turns them into a prescribed-boundary solution.

### Authorized specialization and decisive test

The unchanged TARGET is covered only for one finite constant/first
moment test on the specified small annulus. The later attempt must
check its primitive and both orientations, then apply the imported
positive-functional condition. Its useful success would be actual
smooth collar data with positive total flux but a certified violation
of a necessary first-moment condition. Every such construction must
retain the L855 inner germ, stay inside one fixed inverse chart, and
prove strict full-density and original angular-determinant positivity
on the prescribed outer collar. Formal moments or an atomic measure
do not certify these requirements. No uniform radius is assumed.

The complementary outcome is that the proposed first moment supplies
no independently certified discriminator under these collar hypotheses.
In that case stop this test, preserve the evidence, and do not nominate
an automatic sequence of higher moments. Even all necessary conditions
passing would leave smooth interpolation, chart confinement, angular
transversality, global matching, exchange compatibility, other orders
and actual-Xi all-degree mixed positivity unresolved.

No general theorem is reproved. A mathematical turn would derive only
the stated application difference, under REPRODUCTION unless an
additional independently assessed mechanism becomes necessary. Full
matching Mathlib coverage was not checked; this is not evidence of
absence. This review completes source coverage, not the finite test.
