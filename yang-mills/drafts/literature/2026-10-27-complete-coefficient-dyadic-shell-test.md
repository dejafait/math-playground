# Complete reflected coefficient: covariance-shell source comparison

TARGET: Test whether a dyadic heat-covariance interpolation of L280's exact two-source Gaussian coefficient has uniformly O(1) signed shell increments and O(1) base/infrared contributions.
CHECKED: 2026-10-27
DECISION: EXPLORE
SEARCH_EVIDENCE: Checked the October 25 complete-growth assessments, September 27 boundary comparison, L280(2),(4)--(7),(18)--(19), L291's statement and ATTEMPTS/047--049; searched multiscale Wilson effective actions, heat-covariance shells and composite plaquette responses. The primary readings below establish scope, not a matching bound or novelty.
SOURCE_EVIDENCE: Read Bałaban CMP 109 (1987) Theorems 1/3, pp. 259/264, small-field transformations pp. 254--256, (0.22)--(0.30), pp. 256--259, and (4.34)--(4.45),(5.1)--(5.8), pp. 289--293; Bauerschmidt arXiv:1206.2212v3 section 1.5/Theorem 1.2, pp. 7--8, Remarks 1.7--1.8, p. 12, and section 2.1 spectral proof, pp. 13--15. Reuse earlier one-loop/tensor/slab/boundary comparisons with their restrictions.
COMPARISON: Known scale decompositions and subtracted small-field effective-action bounds do not estimate this bare oriented two-source coefficient on the relative cube or each increment of the proposed heat interpolation. No source result is imported as that bound; L280 permits a direct finite-expression test without those transfers.
GAP: Source-dependent heat interpolation and endpoint identity, complete signed shell cancellation, all normal-link and boundary-stratum sums, and base/infrared estimates remain unproved. No rate, sign or divergence follows from this review.
REASON: The bounded source/scope comparison supports one separate direct Wilson-specific test of the unchanged target, using no unread renormalization theorem. EXPLORE admits an attempt, not a result; theorem-based replacements or changed targets need separate coverage.
LITERATURE_REASON: The registered target was REVIEW_REQUIRED and essential multiscale theorem-level coverage had not been inspected for its shell/source/relative-boundary hypotheses; fixed-mesh and one-face coverage does not cover those obligations.
SCOPE: Exact L279/L280 SU(2) coefficient on [-4,4]^4, even N>=2, a=8/N, counting measure, all-face pins/fixed boundary gauges, every variable normal link, own-slice Wilson jets/full density, exact real reflected bump, both source orders and the stated open real source domain. Only a direct heat-covariance test is admitted, without boundary replacement, counterterm change or source freezing.

## Initial registration retained (step 526)

The remaining coefficient gap is a quantitative bound on the complete
exact reflected coefficient, beyond L291's o(N^2) cancellation. A
decomposition with O(log(eN)) shells and bounded signed contribution
per shell, including bounded base and infrared terms, could supply a
logarithmic coefficient bound. No such decomposition or bound is
asserted here. The interacting higher remainder, nonzero sector,
continuum construction and positive mass would remain independent gaps.

The essential starting inputs are L279 and L280's complete finite-mesh
coefficient with both insertions, moving means, Wilson vertices and full
density, and L291's qualified leading cancellation. L294--L295 are
available only for their audited normal one-face scope, with inherited
L003/L282 conventions and L292--L293 regulator prescriptions. Preserve
SU(2), even N>=2, a=8/N, counting measure, all-face pins, fixed gauges,
every normal endpoint, the exact bump, real source domain and both
source orders. No other component, group or boundary stratum has been
settled by the completed audit.

The proposed mechanism is to retain the exact signed Wilson expression
while varying its relative transverse covariance by heat scale, rather
than estimating its groups by global norms. A future test must first
specify how that interpolation acts on the source-differentiated
Gaussian expression and prove its endpoints reproduce the exact
coefficient. Its discriminating threshold is an N- and scale-independent
absolute bound on each *complete signed increment*, with the base and
remaining infrared term bounded as well. An uncanceled power of the
shell length, an uncontrolled boundary term or a failure of the exact
endpoint identity is evidence against this formulation and must be
recorded before further development. Bounds for a selected group or
frozen source alone do not pass.

The separate literature turn must compare this precise proposal with
primary multiscale lattice-gauge/one-loop results, including their
boundary, zero-mode, source and renormalization assumptions, and search
the relevant local failure records. In particular, ATTEMPTS/048 stops
the insufficient absolute-norm estimate; ATTEMPTS/049 shows that generic
gauge identities alone cannot impose the desired growth bound. Neither
is evidence that the proposed Wilson-specific shell mechanism works.
No external source is silently imported and no theorem is declared
absent from Mathlib; full and supporting coverage is not checked.

Next-turn routing is literature_comparison, standard/high, because
essential coverage is missing. If that review admits this precise
mechanism, a later proof_attempt/creative would be justified by the
central obstruction of turning global leading-power cancellation into
a uniform scale bound. Its bounded test and decisive evidence are the
signed increment and endpoint/base/infrared checks above. No creative
attempt, lemma or mathematical script is authorized by this registration.

## Completed primary comparison (step 527)

T. Bałaban, *Renormalization group approach to lattice gauge field
theories. I. Generation of effective actions in a small field approximation
and a coupling constant renormalization in four dimensions*, CMP **109**
(1987), 249--301, [DOI 10.1007/BF01215223](https://doi.org/10.1007/BF01215223).
Read the original journal scan reproduced in this
[54-page PDF](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf),
not the host's generated summary. Theorem 1 (p. 259), made precise by
Theorem 3 (p. 264), assumes small effective couplings throughout the
specified small-field transformations. Its localized effective actions
include coupling and vacuum subtractions, (0.22)--(0.30). The setup
includes a torus (p. 251). Proof cases (4.34)--(4.45), pp. 289--292,
replace localized propagators and extend sums with controlled errors
before extracting the polarization term; (5.1)--(5.8), pp. 292--293,
use lattice symmetries and translation invariance. This is methodological
coverage, not a physical-cube source-pair theorem. Theorem 2's
coupling-flow proof is explicitly deferred (p. 259); it is not imported.
Project Euclid/Springer downloads failed, but the journal scan was accessible.

R. Bauerschmidt, *A simple method for finite range decomposition of
quadratic forms and Gaussian fields*, PTRF **157** (2013), 817--845,
[arXiv:1206.2212v3, 9 May 2019](https://arxiv.org/pdf/1206.2212v3).
Theorem 1.2, section 1.5 (printed pp. 7--8), starts with a regular closed
symmetric form and requires wave propagation or bounded-operator finite
propagation of powers. Kernel bounds additionally require the stated
diagonal heat-kernel estimate. Remark 1.7 (p. 12) groups positive forms
into geometric scales. Remark 1.8's parameter-family statement assumes
a common spectral representation and its stated lower bound. Section
2.1, (2.1)--(2.5), (2.7), (2.12)--(2.17), pp. 13--15, supplies the
spectral construction and heat-kernel comparison. This does not assert
finite range for proper-time heat slices themselves or Wilson-source
and boundary-trace bounds. No applicability of the parameter-family
hypothesis to L280's nonconstant plaquette weights is presumed.

Reuse the adequate assessments
`2026-10-25-exact-reflected-coefficient-log-growth.md`,
`2026-10-25-transverse-complete-coefficient-log-growth.md` and
`2026-09-27-fixed-box-one-loop-locality.md`. Adams--Lee 0709.0781v3,
section II (7)--(15) and Appendix A, treats a specified momentum-integral
class with infrared and denominator assumptions. Lüscher--Weisz
hep-lat/9504006v1, sections 5 and 7, treats renormalized background-field
vertices, retaining Haar/ghost terms. The Schrödinger-functional and
continuum relative-boundary readings retain their recorded slab/smooth-face
restrictions. These are comparisons, not new inputs to the local DAG.

Scope inference from these statements: a renormalized effective-action
bound or a bound for an entire momentum integral does not supply the
requested bound for each increment of this particular interpolation.
The following missing transfers are not assumed:

| Feature needed here | Missing comparison |
| --- | --- |
| Both bare oriented insertions | Composite/source matching and moving Gaussian means; a background field is a different source. |
| Exact L280 density | Both gauge-coordinate determinant terms and all-link Haar must survive scale organization. |
| Relative physical cube | Normal endpoints, faces, edges and corners need finite-domain estimates, not torus/slab replacement. |
| Heat interpolation on H | An ambient local-operator decomposition is not automatically a local transverse decomposition. |
| Signed increments and endpoints | Leading-power cancellation and covariance bounds alone give neither shell estimates nor base/infrared control. |

## Bounded discovery and duplicate/failure checks

Queries: `Balaban lattice gauge theory ultraviolet stability
renormalization group covariance multiscale theorem Wilson boundary
four dimensions`; `lattice Yang Mills one loop heat kernel multiscale
composite operators boundary renormalization covariance slice`;
`Bauerschmidt simple method finite range decomposition Gaussian processes
heat kernel positive self adjoint operator theorem 2013`;
`"lattice gauge" "heat kernel" "composite" "renormalization" shell`;
`"Wilson" "covariance" "multiscale" "plaquette" perturbation boundary`.
Exact-title/identifier searches located Bałaban's journal scan. Positive-flow
and other dimensional/boundary search hits were screened as leads, not
taken as matching theorems. Original Reisz all-orders papers and further
Bałaban large-field papers remain unread leads, not premises of this
direct test. No exact relative-box shell bound was located in this bounded
search; neither originality nor theorem absence is inferred.

ATTEMPTS/047 retains the uncontrolled internal expectation after
integration by parts; /048 retains the insufficient absolute-norm
estimate; /049 excludes inference from orbit identities alone and
leaves Wilson-specific locality open. The new mechanism seeks scale-local
control of the complete signed Wilson expression, rather than repeating
those rearrangements. L291's complete o(N^2) cancellation and L294--L295's
audited normal one-face results cannot be promoted to shell bounds.
No duplicate shell estimate was found in the specified records.

On 2026-10-27 the [current Clay page](https://www.claymath.org/millennium/yang-mills-the-maths-gap/)
still links the same [14-page Jaffe--Witten description](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf).
Section 4, p. 6, retains the exact target recorded in the foundation;
this source check changes neither the target nor the argument.

## Separate admitted mathematical test

The TARGET is unchanged. One later proof attempt may define and test a
dyadic proper-time heat-covariance interpolation of the *complete*
finite coefficient in L280(7)/(19), using essential L279, L280 and the
qualified cancellation L291. This review supplies no shell formula or
estimate. A direct finite Gaussian calculation need not import the
missing composite/boundary theorems; those transfers must not be used
silently. No general source theorem needs reproving.

First specify the precision/covariance on H for every allowed source,
its source dependence under the heat cutoff, scale endpoints and term
normalizations. Prove that the endpoints reproduce L280's mixed
derivative, including both derivatives of the Gaussian law and all
source-dependent cubic/quartic jets. Retain the complete density and
both normal-edge endpoint cases. An ambient Hodge-covariance replacement
needs an exact comparison retaining its longitudinal/projection correction.
Freezing sources inside the cutoff, transferring higher jets through the
quadratic curvature law, or replacing bare by renormalized insertions
is not approved.

Then attempt the threshold: an N- and scale-independent absolute bound
on every *complete signed* shell increment, bounded base and remaining
infrared contributions, and at most O(log(eN)) intermediate scales.
Retain all finite-domain sums before norms. L294/L295 can support only
their audited normal one-face scope, with inherited L003/L282 conventions
and L292/L293 regulator prescriptions. Other components/groups, boundary
strata and full-box errors remain open.

Continue if this threshold is proved or the attempt identifies a precise
complete residual and a new independently testable estimate. An uncanceled
scale power, endpoint mismatch, uncontrolled boundary sum or return to
the stopped norm/orbit estimates stops this formulation; preserve that
evidence before choosing another mechanism. A bad bound for one group
does not refute the signed target. Repeated formal reorganizations with
the same uncontrolled residual are not justified.

The plausible use remains logarithmic control of the first reflected
correction. Uniform higher remainder, interacting lower bound, continuum
axioms/nonzero sector and finite positive infinite-volume mass remain
independent gaps. No lemma, script, DAG edge or main-argument change is
made. Full/supporting Mathlib coverage is not checked; no library absence
is asserted.

Completed outcome: EXPLORATION; LITERATURE / NOVELTY_UNCHECKED. This
adds a source/scope comparison and admits a separate attempt; it proves
no coefficient estimate or progress beyond the sources. Mathematical
exploration usage this step is zero. Recommend proof_attempt/creative,
deep_research/max: the central obstruction is scale-uniform signed
cancellation with exact sources and relative boundaries; the bounded
decisive test is the endpoint, complete-increment and base/infrared test.
