# Forced contact after L858 — completed source comparison

TARGET: Assess whether divisor linking or relative Maslov-index constraints force a common F=J zero for an L847 nonnegative radial torus extending the L849 collar, retaining L858 and allowing nonisolated F zeros with J nonzero.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded searches for divisor/Maslov linking, vanishing holomorphic forms, nonnegative full phase and totally real tori led to Auroux, Pacini and Cote-Dimitroglou Rizell; primary hypotheses and essential boundary-section cases were read. Scoped duplicate/failure comparisons and exact queries appear below. No adequate forced-common-contact theorem located; no novelty inferred.
SOURCE_EVIDENCE: Auroux arXiv:0706.3207v2 Section2.1 Definition2.1 p3 and Lemma3.1/proof/weaker-phase remark p7; Pacini arXiv:1711.07928v3 Sections2-4 pp3-6, equation(2), Theorem3.2/proof and equation(3); Cote-Dimitroglou Rizell arXiv:1909.04753v2 Theorem1.1/Corollaries1.2-1.3 pp1-2, Theorems1.8-1.9 p4 and Section4.2 p24. Hatcher Section1.3 Proposition1.33/proof pp61-62 supplies the separate phase-lift test. Precise links below; reuse Lai/Forstneric coverage without a new audit.
COMPARISON: The inspected divisor formula counts intersections of relative discs for a torus outside an anticanonical divisor; the general Maslov formula needs totally real boundary data and computes an index rather than forcing contacts. Linking results require Lagrangian tori and additional topology. None identifies a divisor intersection with F=J=0 or supplies existence for the full vanishing form and prescribed collar.
GAP: A nonzero contact obligation for the exact L847/L849 class remains unproved. First determine what phase extension and torus periods the accepted L858 plane field actually imposes, keeping the ambient determinant factor; the source formulas alone decide neither that calculation nor forced contact.
REASON: New hypothesis-level source evidence parks automatic divisor/Maslov/linking import. Nominate one bounded first-phase test instead of repeating the completed localization audit or assuming a positive surface perturbation. This is a source-scope negative, not nonexistence of a torus or a theorem that all linking mechanisms fail.
LITERATURE_REASON: The target changes from auditing the determinant localization to an unassessed forced-contact mechanism; existing class identities do not cover that implication.
SCOPE: Exactly L847's actual entire G and full r=2,k=1 form, real C2 periodic exchange-symmetric u, q=F(Phi_u)J globally real and nonnegative, and L849's strictly smaller exact collar with L848's analytic/trusted-software qualifications. L858 is an accepted conditional input. Original J and F zero sets may be nonisolated; no simple G zeros, RH, positive extension, integrated perturbed planes or forced contact is assumed.

## Completed comparison — 6 November 2026

The intermediate target is a forced common contact, which together with
L858 would exclude this prescribed contour class. The main gap remains
L030-L032/C032a actual-Xi all-degree mixed positivity. Even exclusion of
this contour class would not resolve that gap or determine a new Xi sign.

### Primary hypotheses and essential cases inspected

**Auroux.** Denis Auroux, *Mirror symmetry and T-duality in the complement
of an anticanonical divisor*, arXiv:0706.3207v2 (10 July 2007),
[Section2.1 p3; Lemma3.1 and its proof/remark p7](https://arxiv.org/pdf/0706.3207).
The setting is a smooth compact Kahler manifold with anticanonical
section sigma, divisor D, and nonvanishing volume form Omega=sigma^(-1)
on X minus D. For special Lagrangian L contained in that complement,
Lemma3.1 gives mu(beta)=2 beta.[D]. Its proof compares the squared
tangent-volume section with sigma squared along the disc boundary;
the subsequent remark allows a lifted phase instead of constant phase.
The counted intersections lie on a relative disc, not necessarily on L.
The proof does not assume simple intersection points for this algebraic
count, but does need the boundary sections to be nonzero. Our prescribed
torus meets the zero divisor along its entire exchange diagonal, and
the full form vanishes there rather than being an inverse anticanonical
section. Thus neither the complement hypothesis nor that section
comparison is supplied. No compactification, change to the reciprocal
form, or extension across the divisor is justified here. This lemma
cannot be imported as a forced common-contact result. No disc-counting
or wall-crossing claims from later sections are used.

**Pacini.** Tommaso Pacini, *Maslov, Chern-Weil and Mean Curvature*,
arXiv:1711.07928v3 (27 September 2018),
[Sections2-4 pp3-6](https://arxiv.org/pdf/1711.07928).
For an oriented compact surface Sigma and a complex bundle E, with an
orientable maximal totally real boundary subbundle B, equation(2) and
Theorem3.2 identify the Maslov index with (i/pi)(integral tr R minus
boundary integral theta). Here B is not our scalar F. Read the canonical
nonzero wedge section (1), the connection-change cancellation and the
axiomatic proof of Theorem3.2. Section4 obtains the geometric formula
(3) when B is the pullback of the tangent bundle of a totally real
boundary submanifold. The abstract theorem permits plane-bundle data
without an integrable surface deformation, so it is a relevant tool for
L858's perturbed planes. It supplies no nonzero index or contact
existence. Applying its tangent version to the original torus would
require total reality on the relevant boundary, not just q>=0.

**Linking.** Laurent Cote and Georgios Dimitroglou Rizell, *Linking of
Lagrangian tori and embedding obstructions in symplectic 4-manifolds*,
arXiv:1909.04753v2 (8 April 2020),
[Theorem1.1/Corollaries1.2-1.3 pp1-2; Theorems1.8-1.9 p4;
Section4.2 p24](https://arxiv.org/pdf/1909.04753).
Theorem1.1 classifies weakly exact rational Lagrangian tori in the
complement of the cotangent zero section; Corollary1.2 gives a
Lagrangian isotopy under its homology/disjointness assumptions.
Theorem1.8 unlinks disjoint Lagrangian tori in standard symplectic R4
under trivial complement fundamental-group maps; Theorem1.9 treats
rational symplectic four-manifolds. Section4.2 defines a relative Chern
count using a section nonzero along its totally real boundary.
These statements concern Lagrangian submanifolds for a specified
symplectic form, not arbitrary radial graphs and their divisor contacts.
Reality of our pullback makes Im(omega) vanish on its tangent planes,
but omega is zero on the prescribed diagonal: it does not provide a
global symplectic structure there. No identification with the source's
symplectic pair or admissible surface isotopy has been established.
None of these statements forces a common F=J zero. Their deeper
holomorphic-curve proof machinery is not imported.

**Phase-lift tool for the nominated test.** Allen Hatcher,
*Algebraic Topology* (2002), Section1.3,
[Proposition1.33 and proof, pp61-62](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf#page=70).
For a covering p and a based map a from a path-connected locally
path-connected space Y, a lift exists exactly when a_*(pi1 Y) is
contained in p_*(pi1 of the cover). Read the path-independence and local
continuity parts of the proof. With Y=T2 and the universal exponential
cover R -> S1, this is an available criterion once a continuous circle
map on the whole torus has been established. It says nothing about
whether F/|F| extends across a nonisolated zero set. The future work
must establish that extension before using this criterion; no such
extension or winding calculation is proved in this turn.

### Search and local overlap evidence

Queries actually issued included:

- `Maslov class holomorphic volume form zeros divisor linking totally real submanifold phase`;
- `special totally real vanishing holomorphic volume form divisor intersection Maslov index`;
- `Auroux mirror symmetry T duality anticanonical divisor complement lemma 3.1 Maslov index pdf`;
- `Pacini Maslov Chern Weil mean curvature theorem 2017 pdf`;
- `holomorphic volume form zeros totally real torus linking obstruction phase nonnegative`;
- `divisor linking Maslov class totally real tangencies zero holomorphic form prescribed boundary phase torus`;
- `"nonnegative" "holomorphic" "volume form" torus divisor`;
- `"totally real" "Maslov" "divisor" "zeros"`.

The Auroux and Pacini primary PDFs were accessible. The published
linking endpoint failed; its primary arXiv version supplied the exact
statements and boundary-section case. No essential source blocker
remains for the bounded phase test. Analytic-disc filling and thesis
search hits were leads only, not inspected existence theorems or
premises. Search-result snippets are not evidence of theorem scope.

Read the relevant L847/L849 hypotheses/full pullback and L858 statement,
then the L858 lift/exchange equations(8)-(11) and global-class paragraph
to separate what is already proved from the proposed periods. Reused
the named global-complex-point and Gauss-map assessments and searched
their phase/winding terms, the actual-G full-phase/product-audit and
transverse-divisor records. The full-phase comparison already parks
nonvanishing-volume calibration imports; the global-index comparison
and `ATTEMPTS/2026-11-06-automatic-global-index-import-limit.md` retain
the zero-total/generic-isolation limit. L858 resolves its own localization
gap, so that historical limit is not reapplied against L858. L855 is
consistency only; L853/L854 are not premises. No matching two-cycle
full-phase extension calculation was found in these scoped records.
This bounded comparison does not establish novelty.

### Decision and separate continuation

The new evidence is a hypothesis mismatch in the proposed automatic
source import, not a counterexample to the forced-contact statement.
Park that import. The remaining first-phase question can be tested
without requiring a positivity-preserving deformation of the surface:
use L858's already constructed planes, retain the full divisor, and
distinguish its scalar J_epsilon from its actual-frame determinant.
No phase formula beyond the existing lemma, period value, new lemma or
mathematical script is produced here.

The exact bounded continuation is nominated in
`2026-11-06-l858-full-phase-period-test.md` for separate approval.
Continue the first-phase forcing route only if a rigorously obtained
nonzero obligation contradicts the allowed data. If the full-phase
extension has compatible periods, retire this first-winding mechanism;
that would leave stronger relative obstructions and global assembly
open. Merely deleting the divisor or computing the ambient frame's
winding is not the required test. Full matching Mathlib coverage has
not been checked; no Mathlib absence is asserted.

## Original uncovered nomination — preserved

The main gap remains L030–L032/C032a actual-Xi all-degree mixed
positivity. A forced-contact theorem, combined with L858, could rule
out this prescribed positive-contour class. That would be a constraint
on the route, not an Xi minor sign or a proof or disproof of RH.

The exact next step is source comparison only. Search for the precise
statement, standard terminology, stronger results and known obstructions
for divisor linking and relative Maslov classes with a vanishing
holomorphic two-form. Read primary hypotheses and relevant proof cases
before deciding applicability. Reuse the ready index sources; do not
repeat generic complex-point isolation or the completed L858 audit.
The specific discriminator is whether the source imposes a nonzero
contact obligation under the full stated hypotheses, or instead
requires extra nonvanishing, transversality, simplicity or surface
deformation assumptions that this notebook cannot supply. Do not
replace the common-contact target by an ordinary divisor intersection.

Essential inputs: L847 fixes the full form and radial class; L849
fixes only the exact collar and inherits L848's qualifications; L858
excludes common contacts under the hypothetical global sign condition.
L855 is a consistency example, not an existence argument on the torus.
Neither L853 nor L854 is a premise. Global assembly and all-degree
transfer remain unresolved even if this contour class is excluded.
No cross-notebook input is proposed.

Relevant preserved comparisons and stop evidence are
`2026-11-06-actual-g-radial-graph-full-phase.md`,
`2026-11-06-global-complex-point-index-scope.md`,
`2026-11-06-gauss-map-divisor-localization-test.md`, and
`../../ATTEMPTS/2026-11-06-automatic-global-index-import-limit.md`.
They do not globally ban index methods. No new linking theorem,
local lemma, forced-contact calculation or approval is claimed here.
Full matching Mathlib coverage remains unchecked.
