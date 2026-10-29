# Uniform reflected-error bound — completed source comparison

TARGET: Assess existing source coverage for L003's bound |Q_(a,g(a))(f)-q_a(f)|<=c_box/2 uniformly in the cutoff along a bare-coupling trajectory tied to a fixed physical scale.
CHECKED: 2026-10-25
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused existing MRS, curvature, Ward/flow, physical-box and partition-function stability assessments; searched uniform weak-coupling plaquette correlations, connected continuum correlations and reflected small-coupling bounds; followed the closer generating-function lead to arXiv:2205.07376v2, Theorem 4 and its proof. No adequate match established; no novelty claim.
SOURCE_EVIDENCE: Newly read Faria da Veiga–O'Carroll, arXiv:2205.07376v2 (26 August 2024), section V, pp. 30–32, (82)–(84), Remark 16 and Theorem 4; section VI.5, pp. 34–35, complete proof; section IV, Theorem 3, p. 29. Reused the precise primary readings recorded below. Rechecked the current Clay-linked Jaffe–Witten description, section 4, p. 6.
COMPARISON: The new source bounds differently scaled periodic plaquette generating functions above, without Gaussian-error matching or a physical-scale trajectory. Existing MRS and perturbative Ward/renormalization inputs likewise give neither this exact centered comparison nor the allowance c_box/2.
GAP: L003's exact bare composite, possible mixing/renormalization, relative pinned boundaries, physical-scale prescription and uniform smaller remainder remain unmatched. No nonperturbative theorem is imported and the bound is not disproved.
REASON: The bounded comparison fails the stated import test. Park direct import and register the actual reflected observable's fixed-mesh correction as an independently testable normalization diagnostic requiring separate coverage approval; do not repeat the MRS or Ward audit.
LITERATURE_REASON: Essential missing coverage for the changed exact interacting reflected difference and physical-scale trajectory; ready assessments concern different observables or formal/fixed-mesh quantities.
SCOPE: Completed comparison for TARGET; no uniform-error proof or new trajectory is approved, and no lemma or mathematical script is changed.

## Original registration scope retained

The main gap is an interacting continuum theory with positive finite
infinite-volume mass for every compact simple group. The intermediate
target is source coverage for the exact reflected-error bound already
stated in L003 section 6. Its downstream use would be retention of a
positive centered physical sector in this fixed box, subject to all
remaining field and continuum requirements. It would not establish
the mass gap or the other groups.

Essential input: L003's complete hypotheses, definitions of Q_(a,g)(f)
and q_a(f), and its positive c_box. L002 supplies the free-field context
if needed. L011 and C278a are scope contrasts, not estimates for this
exact difference: Gamma is a Ward-response coefficient. Do not identify
it with a Taylor coefficient of Q without a separately justified bridge.
The unused L221 continuation was screened only at statement/audit-header
level: it already has a separate conditional audit, and no discrepancy
was found that would justify repeating it.

First locate relevant existing local coverage and recorded failed
uniformity/diagonal-limit routes. Reuse adequate primary assessments.
For any proposed theorem, compare its precise observable, centering,
boundary conditions, normalization, coupling regime, cutoff dependence
and physical-scale prescription with L003. The source comparison must
state whether further composite renormalization changes the requested
quantity. Do not invent a running trajectory or infer interaction from
arbitrarily small couplings chosen independently at each mesh.

Continuation test: a matching theorem or a precise independently
testable specialization must identify an admissible trajectory, its
physical-scale meaning and a uniform error allowance meeting c_box/2.
If sources provide only fixed-mesh asymptotics, formal perturbation
theory or a diagonal small-coupling choice, record that failure of
coverage and select a materially different concrete intermediate target.
Do not repeatedly browse a persistently blocked source. No new lemma,
mathematical script or correctness verdict is authorized by this
registration. Matching Mathlib coverage is not checked. Continuum
convergence, full positivity/axioms, nonzero renormalized interaction,
box removal and finite positive physical mass remain unresolved.

## Completed comparison: reused evidence

The exact observable is L003's centered (4/g^2) sum_p f(z_p)P_p,
without an extra a^4 or an assumed composite counterterm. Its model has
beta=4/g^2, fixed boundary-contained links, variable normal end links,
even a=8/N, and the relative Hodge Gaussian coefficient q_a. Section 6
and history/004 already distinguish its fixed-mesh limit from a physical
trajectory. This review makes no diagonal-coupling choice.

- [MRS scope audit](../../foundations/03-mrs-ultraviolet-scope.md):
  Magnen–Rivasseau–Sénéor, *Construction of YM4 with an infrared cutoff*,
  CMP 155 (1993), 325–383,
  [DOI 10.1007/BF02097397](https://doi.org/10.1007/BF02097397),
  unnumbered statement p. 327 and section VIII, pp. 377–378. Reuse the
  recorded axial-gauge/trivial-sector SU(2) scope, different infrared
  regulator and outstanding positivity step. It supplies no normalized
  composite lower bound or exact lattice comparison. ATTEMPTS/002
  already stops direct physical-nontriviality import; no repeat audit.
- [Ward assessment](2026-09-26-current-target.md) and
  [physical-box locality assessment](2026-09-27-fixed-box-one-loop-locality.md):
  reuse Lüscher–Weisz [1101.0963v2](https://arxiv.org/pdf/1101.0963v2),
  sections 7–8, and Del Debbio–Patella–Rago
  [1306.1173v1](https://arxiv.org/pdf/1306.1173v1), section 6.
  Their renormalized perturbative flow correlations and translation
  identities do not give this unflowed exact comparison. Flow-time-zero
  boundaries are not the physical faces. L011(5)–(6) and C278a concern
  a different Ward response; Gamma is not a proved Taylor coefficient
  of Q. L011 proof section 2 has only mesh-dependent remainder constants.
- [Curvature audit](../../foundations/04-perturbative-curvature-renormalization.md):
  Suzuki [1304.0533v6](https://arxiv.org/pdf/1304.0533v6), section 2,
  (2.7)–(2.22), gives formal contracted scalar/tensor identities. L004
  already excludes the common single-factor prescription but expressly
  leaves the full reflected correction undetermined. A pole in one
  projection gives neither its sign nor divergence/cancellation.
  drafts/2026-09-25-plaquette-ultraviolet-normalization.md preserves
  this unfinished issue. No mixing computation is repeated here.
- [Other/other scale assessment](2026-10-10-other-other-cubic-leading-scale.md):
  reuse its reading of Faria da Veiga–O'Carroll
  [1903.09829v2](https://arxiv.org/pdf/1903.09829v2), Theorem 1,
  Remark 1 and section IV. Partition-function/free-energy stability
  does not give the requested observable matching. The new lead below
  was inspected because it goes further by including sources.

ATTEMPTS/030 and /032 remain intact: their factorwise Ward-remainder
failures are not bans on studying Q. No existing assessment located here
supplies the missing exact nonperturbative bound.

## New primary theorem and essential proof cases

P. A. Faria da Veiga and M. O'Carroll,
[*On Yang–Mills Stability Bounds and Plaquette Field Generating Function*,
arXiv:2205.07376v2](https://arxiv.org/pdf/2205.07376v2), 26 August 2024,
54 pages. Read section V, pp. 30–32, and VI.5, pp. 34–35, before
the larger context. This is a scope comparison, not an independent audit
of all estimates in the paper.

Theorem 4 uses periodic hypercubes of even side count, d=2,3,4,
a in (0,1], and 0<g^2<=g0^2<infinity. Its displayed group formulas are
for U(n); the introduction discusses SU(n) modifications. Equation (82)
uses (a^(d-4)/g^2)^(1/2) Im Tr(U_p-1). Bounds (83)–(84) control
source generating functions above. The proof uses Hölder, periodic
multireflection, single-link stability, Weyl integration and Gaussian
majorization. Remark 16 mentions action-density fields with a different
normalization; no identification with L003 is established here.

Consequently this theorem supplies neither pinned-box matching,
centering and Gaussian-error smallness, nor a physical-scale trajectory.
Its position-independent upper estimates are not the required separated
comparison. Theorem 3, p. 29, concerns subsequential scaled free energies,
not that comparison. No SU(2) specialization or field rescaling repairs
these missing conclusions by citation. No result from this paper is
inserted into the mathematical argument.

## Search record and qualifications

Queries actually run:

- `Yang Mills Wilson lattice connected plaquette correlation continuum limit small coupling fixed physical scale rigorous ultraviolet stability`
- `"Yang-Mills" "plaquette" "Gaussian" "uniform" "weak coupling" correlation rigorous`
- `"Wilson" "Yang-Mills" "connected" "plaquette" "continuum limit" rigorous bound`
- `"Yang-Mills" "reflection" "small coupling" "continuum" bound curvature`
- `site:arxiv.org Yang Mills weak coupling Gaussian approximation plaquette correlations continuum rigorous uniform`

Numerical, two-dimensional, large-color and claimed complete-construction
hits were discovery aids, not inspected matching theorems or inputs.
No correctness verdict on those claims follows from snippets. The
Balaban lead recorded as unread in the 2026-10-12 coordinate-Haar
assessment remains unread, not evidence for an observable estimate.
This bounded review asserts neither exhaustive coverage nor absence of
stronger results. There was no essential access failure for the theorem
actually compared. No mathematical novelty is claimed.

On 2026-10-25 the current Clay page still links to Jaffe–Witten's
14-page [*Quantum Yang–Mills Theory*](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf).
Section 4, p. 6, retains the continuum target, compact simple groups,
axiomatic strength and finite positive mass. No target version changed.

## Decision and boundary of this step

The new evidence is the closer generating-function source's mismatch,
also recorded in ATTEMPTS/046. No inspected statement passes the
registered continuation test. This parks immediate source import; it
does not show that the desired bound is false. It is local source
progress, not mathematics beyond the sources checked.

The proposed different diagnostic is the fixed-mesh coefficient of g^2
in Q-q, with both exact centered insertions and every action/Haar term.
L003 and L011's method are plausible inputs, not an already established
coefficient formula. L004 supplies a normalization warning. No existence
proof, coefficient, cutoff rate, sign or bridge to Gamma is derived here.
The separate target registration remains REVIEW_REQUIRED. Even a valid
finite coefficient will leave the nonperturbative remainder and physical
trajectory unresolved. Full matching Mathlib coverage is **not checked**.
