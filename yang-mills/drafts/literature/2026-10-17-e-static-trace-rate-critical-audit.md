# E static trace rate — critical-audit source scope

TARGET: Critically audit L224's O(N^2) static-trace continuum rate, including the signed dipole decomposition, relative projection cutoffs, actual modal estimates and full heat sum.
CHECKED: 2026-10-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the unchanged parent static-rate assessment, read all of L224, compared the relevant L008/L028/L097/L101/L222/L223 statements and proof ranges, checked history 292 and ATTEMPTS/024–025/030, and performed the five bounded searches recorded below; no matching full-trace theorem was established.
SOURCE_EVIDENCE: Reinspected Lawler–Limic Theorem 4.3.1, Corollary 4.3.3 and Theorem 6.3.8(a), including the harmonic-measure proof on printed p. 131; reused the parent's source versions and the existing DLMF assessment underlying L222. Exact local input ranges and applicability boundaries follow.
COMPARISON: The scalar source supplies the whole-space Green and harmonic difference inputs; the local results supply the actual cumulative stencil, relative domains and quantitative probe/mode inputs. They do not certify L224's signed dipole decomposition, nested relative projections or ordered-trace rate. These are accessible proof obligations for a separate mathematical audit, with no identified missing essential external theorem.
GAP: Independently check L224's coefficient row sums, relative extension and projection ranges, cutoff exponents, actual Bb/Bq normalization and mode envelopes, full heat sum and physical trace normalization; the claimed O(N^2) rate remains unaudited.
REASON: The exact audit scope is now source-ready within the already assessed fixed-box hypotheses. Approve one later critical proof audit, preserving the original rate claim and all pending proof obligations; this source review neither validates that rate nor establishes novelty.
LITERATURE_REASON: Mandatory separate approval of the newly proposed L224 audit continuation; its relative-projection cutoff and actual-path specialization had not received theorem-level source comparison, even though the parent static-rate target was ready.
SCOPE: L224 only, for the fixed relative SU(2) cube, admitted even N, a=8/N, tau=1/16 and actual probes i=3,6; no upstream audit of all imported results, complete-response rate, interacting estimate or Yang–Mills construction.

## Review and source comparison, 2026-10-17

This is the separate literature-only approval requested after history
292. The former REVIEW_REQUIRED decision is superseded by EXPLORE for
the unchanged TARGET. No new mathematical result is derived, no proof
verdict is given, and no lemma or mathematical script is changed.
The parent [static-rate assessment](2026-10-17-e-static-trace-continuum-rate.md)
remains unchanged. Its inspected Gurevich, Adams–Lee and scalar interval
comparisons are reused with their recorded restrictions; none is an
additional input to L224. Unread leads remain unread.

Lawler and Limic, [*Random Walk: A Modern Introduction*](https://www.math.uchicago.edu/~lawler/srwbook.pdf)
(2010; same 289-page author-hosted text inspected on 2026-10-17):
Theorem 4.3.1, printed pp. 81–84, treats transient symmetric finite-range
walks and explicitly includes simple random walk. Corollary 4.3.3,
p. 84, supplies its coordinate first differences. Theorem 6.3.8(a),
p. 131, bounds bounded-step differences of signed harmonic functions
in a ball by their supremum and inverse radius; positivity is not
required. Its proof uses an interior cube and harmonic measure, with
constants uniform in the exit point. The nearest-neighbor walk in
dimension three satisfies these hypotheses. L224 uses the normalization
Delta=6(I-P_walk), so its scalar inverse is G_walk/6. The audit must
check the translated balls avoid both dipole sources, and that the
finite set of stencil displacements permits common constants. These
are scalar inputs, not a relative vector Green theorem or a trace rate.

The parent's killed-Green Proposition 4.6.2 is unnecessary for L224's
chosen proof: its finite-volume comparison is through energy
projections. No unread mixed-source or Neumann theorem is needed merely
to inspect that argument. Conversely, the scalar citations do not
establish that its proposed relative extension and projection spaces
are correct. Those assertions must be audited as locally proved claims.
Reproving the scalar estimates would not address this distinction.

For calculus, reuse the inspected NIST DLMF v1.2.8 (2026-09-15),
section 1.4(vi), (1.4.35)–(1.4.37), in the
[diagnostic assessment](2026-10-17-finite-diagnostic-continuum-rate.md).
The smooth closed-interval hypotheses there match the pre-retraction
product modes and fixed cutoff. No Taylor claim about a rough
projection kernel or the upper-pinned forest field is imported.
Orthogonal projection/best approximation and Fourier Plancherel are
standard named inputs; their concrete spaces and multipliers remain
part of the audit. Full matching and supporting Mathlib coverage are
not checked; unknown coverage is not absence.

## Exact local scope of the later audit

Essential inputs remain L008 L028 L097 L101 L222 L223. The following
map locates coverage; it does not verify L224's deductions.

| Obligation | Inspected local coverage and remaining check |
| --- | --- |
| Signed dipole coefficients and cumulative stencil | L101 section 3, (13)–(14), and section 4, (15), fix the quarter layer, transport/shear, triplet and moving-cut terms. L028(4) gives coefficient C^r consistency. Check the exact zero row sums, symmetry, support and coefficientwise O(a) error in L224(2)–(4); qualitative form convergence alone is insufficient. |
| Relative spaces and finite projections | L097(1) identifies S_T as the projection onto im D_T; L101 fixes T and G. L003's relative-cell definition, inspected narrowly as the inherited domain, pins cells contained in each face and keeps normal end edges. Check extension through every face and corner in each degree and the exact finite curl range before using L224(7). No scalar Dirichlet condition on every link is available. |
| Whole-space dipoles and cutoff projections | The scalar citations cover L224's proposed decay mechanism. Audit its harmonic specialization, membership in closures of compact gradients/curls, finite second spatial l2 moment, and both O(N^(-3/2)) cutoff errors. They are new local proof claims, not source imports. |
| Both actual Bb/Bq paths | L097 hypotheses and section 5 identify Zeta=M_b Bq-M_q Bb and its frozen symbol. L028(9) gives the actual interior forest lift; its stated scope alone excludes some boundary rows. L222(2)–(3) supplies smooth product modes for all retained labels and (9) controls transverse derivatives of the prefix for all s<N. L224 must use those explicit formulas to cover its additional path/end rows, rather than enlarge L028 by assertion. |
| Actual probe and heat coefficients | L008(1)–(2) fixes the triplet average of squares and polarized clover shear. L222(7) bounds those same whitened forms, and L097 section 5 supplies the heat framework. Audit L224(13)'s normalization and summable polynomial error envelope for every retained label and both probes; the diagnostic value D_(i,a) is not an input to this trace. |
| Ordered contraction and continuum density | L101(3) and (16) define the static expression and its a^4 normalization. L101(4)–(5) specifies m_E and K_(i,E). Check L224(14)–(17) without commuting multipliers, its finite curl projection bilinear error, and the final Fourier identification and endpoint-strip quadrature. |
| Separate replacement error | L223's conclusion defines T_(i,N) and bounds R_E-T_(i,N). It does not certify L224 or its continuum rate; the combination is only a later triangle inequality if the static rate passes. |

L222 now contains a separate diagnostic audit in section 6; its
supporting estimates may be imported relative to the stated upstream
inputs. That audit covers the diagnostic, not L224's path/projection
application. No recursive audit of all upstream results is claimed.
The actual constant axial labels, lower prefix, upper cumulative tail
and all relative source rows must survive every comparison. Nothing
here authorizes extending the potential smoothly across its upper pin.

## Search, duplicates and recorded failures

In addition to reusing the parent's bounded searches, the audit-specific
queries were:

- `"discrete" "Hodge" "projection" "dipole" boundary Green trace`
- `"lattice" "Green" "dipole" "projection" finite volume estimate`
- `"discrete Green" "dipole" "Dirichlet" projection`
- `"lattice" "orthogonal projection" "Green" "boundary" dipole energy`
- `"dipole" "Green" "finite volume" lattice projection estimates discrete`

These did not establish a matching actual-probe trace theorem.
Results included *Lattice Green functions for pedestrians: Exponential
decay* and conforming discrete de Rham work; their theorems were not
inspected and they supply no input or obstruction here. Unrelated
electromagnetic dipole and lattice-phenomenology hits are not evidence
about this target. No novelty conclusion follows from these searches.

The narrow local check used L224, its existing attempt record, history
292, the parent assessment, and the quantitative input/audit sections
listed above. L224 is the completed proof awaiting review, not a
duplicate independently verified result. L101 gives a qualitative
limit; L222 and L223 concern different errors. No ready assessment
was reopened for more research on its already covered target.

ATTEMPTS/024 retains a real upper Dirichlet correction in another
axial inverse, 025 stops an absolute-profile gain there, and 030 stops
using fixed-mass limits at varying mass. They remain valid obstructions
to those shortcuts. L224 proposes subtracting its own continuum term
using finite-N energy cutoffs with no mass schedule; its correctness
does not follow from being different. In particular, absolute first
kernel moments and arbitrary smoothness of a projection-side prefix
are not substituted for its claimed squared moment and actual exterior
coefficient estimates.

## Continuation and abandonment test

Perform exactly the TARGET as one separate mathematical proof audit.
Continue with the claimed O(N^2) rate only if its complete signed
decomposition, finite relative ranges, cutoff errors, per-mode estimates
and full heat-summed normalization hold under the existing hypotheses.
The required static threshold is O(N^(5/2)log(eN)^2); the claimed result
is stronger. Record any failed statement or missing boundary/mode case
explicitly and withhold acceptance if it is essential. A failure of
this proof mechanism is not signed growth of the trace or a disproof
of the rate. No new lemma is needed merely to fill an audit gap.

Plausible downstream use is a validated E-component O(N^(5/2)) remainder
after combining with L223. Other component rates, the complete-response
remainder, L220 audit and coupling-uniform interacting control remain
independent gaps. The main target still requires cutoff removal, the
continuum axioms and finite positive mass; reflected error <=c_box/2
is unproved. The official target interpretation is reused from the
parent's recorded primary-statement comparison; this review selects
no new construction route. No cross-notebook input is used.

This review spends no mathematical exploration turn. The one prior
static-rate attempt ended in reported ADVANCE; its proof is still
pending independent audit. No essential source blocker is identified,
so the exact next task is mathematics, with no further literature
needed unless a concrete missing essential input emerges.
