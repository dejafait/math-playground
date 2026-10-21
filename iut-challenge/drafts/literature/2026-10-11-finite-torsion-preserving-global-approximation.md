# Different-curve finite-torsion realization — completed source review

TARGET: Assess local-constancy and approximation theorems for a curve over Q(zeta_60) whose completion at 3 has full rational 30-torsion and the exact 7-torsion coordinate field N of L042.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped local searches found only prior scope exclusions; searches for elliptic finite-torsion local constancy, Krasner stability and Kisin Theorem 5.1 led to the inspected primary Bisatt–Dokchitser Theorem 2.2, including its complete proof paragraph. Kisin's author-hosted DVI was inaccessible to the available reader; it is not treated as inspected.
SOURCE_EVIDENCE: Bisatt–Dokchitser, Tame torsion and the tame inverse Galois problem, Math. Ann. 381 (2021), 1439–1453, version of record 2021-04-27, Theorem 2.2 and proof p.1441, https://doi.org/10.1007/s00208-021-02173-y, also https://d-nb.info/1235382842/34 PDF p.3; Milne EC2 (2021), III.3 (23)–(26) pp.102–103 and I.4 Picard-groups discussion (8) p.36, https://www.jmilne.org/math/Books/EC2.pdf; audited L042 and L043 supply the unchanged local packet and exact-curve exclusion.
COMPARISON: The inspected theorem preserves the complete m-torsion Galois module for every m under sufficiently close fixed-degree integral-polynomial approximation over Q_ell. Its scope covers the planned m=210, ell=3 application over Q_3; Milne explicitly defines the rational-q Tate curve over Q_3. Restriction to H and a rational-coefficient approximation avoid needing an unread extension of the theorem to H.
GAP: A later specialization must verify the squarefree integral cubic model, rational approximation with degree retained, Jacobian identification, restriction to G_H and equality of full torsion kernels as embedded fields. No such curve or equality is established here; all original global/native/input/action/pilot/essentiality and finite B>=A obligations remain independent.
REASON: Adequate primary coverage replaces the uncovered approximation lead by a standard finite-torsion local-constancy application. Import the inspected theorem without reproof; only its elementary applicability and full-field specialization remain for a separate mathematical turn.
SCOPE: L042's exact q=3^30, k=Q(zeta_60) in the fixed Q_3 closure, completion H and N unchanged; approximation of a Q_3 model by rational coefficients, followed by base change to k. No general H-coefficient constancy theorem, effective congruence radius, global rational 30-torsion or IUT realization is covered.
COVERED_TARGET: Specialize Bisatt–Dokchitser Theorem 2.2 at m=210 to construct a nonsingular E'/Q(zeta_60) with full H-rational 30-torsion and H(E'_H[7])=N as embedded fields.

LITERATURE_REASON: The startup gate required this separate assessment of the changed finite-torsion invariant, which was expressly outside the ready exact-curve transcendence coverage. This is the first source comparison for approximation, not additional literature on an already-ready target.

## Preserved proposal (source-status statements superseded below)

Fix L042's algebraic closure of Q_3, the embedded k=Q(zeta_60),
its induced place v and completion H=Q_3(zeta_60), and
N=Q_3(zeta_420,3^(1/7)) in that closure. The proposed mathematical
test is existence of a nonsingular elliptic curve E'/k with
E'_H[30] entirely H-rational and H(E'_H[7])=N as embedded fields,
using all coordinates of all geometric points. A conjugacy statement
about complete Galois representations may suffice, but equality of
degrees, a cyclic subgroup or an x-coordinate field does not suffice.
No exact equality with E_(3^30) or with its transcendental j is sought.

Inspect primary statements about local constancy of finite etale
torsion, Krasner-type stability or finite-level modular covers and
coefficient approximation. These are unread leads, not imported
inputs. In particular distinguish characteristic-zero separability
from a theorem that might require torsion order prime to residue
characteristic. Retain nonsingularity and the specified base field;
state any needed finite extension rather than silently replacing H.

Continue only if an inspected theorem covers both torsion levels
over H, or isolates a concrete independently testable gap. Otherwise
record the exact failed hypothesis and park this mechanism rather
than repeat the exact-q transcendence search. Do not construct E'
or approve an uncovered specialization during the source review.

Downstream use would be a global-curve replacement for L042's local
packet, not initial IUT data. Global rational 30-torsion, the global
F/F_0 degree restriction, selected places, native/actual input/action,
pilot transport, essentiality and original finite B>=A remain separate
obligations. Preserve ATTEMPTS/022,025,026,027. No cross-notebook input
or Mathlib matching coverage is asserted. This proposal requires a
separate literature turn and is not ready for mathematical work.

## Completed comparison — 2026-10-11

The main gap remains the original finite B>=A comparison. The intermediate
target retains only L042's two finite torsion fields while allowing a
different curve. A global-curve replacement could support a later
initial-data applicability screen; it would not itself supply initial
IUT data or an essential flaw. No lemma or mathematical script is
written in this literature-only step, and PROOF.md and DAG.md are unchanged.

### Inspected primary theorem and scope

Bisatt–Dokchitser Theorem 2.2 assumes a prime ell and a hyperelliptic
curve y^2=f(x) for squarefree f in Z_ell[x]. For each integer m>=1 it
provides a positive congruence precision such that every integral
polynomial of the same degree sufficiently close to f defines a curve
whose Jacobian m-torsion is isomorphic to the original as a G_Q_ell-module.
This is a full-module conclusion, not a degree or inertia-only assertion.
No good-reduction or prime-to-ell condition occurs. The complete proof
paragraph invokes Kisin Theorem 5.1(1) and notes that sufficient closeness
preserves squarefreeness and hence a same-genus family. Import the stated
primary theorem; do not claim a new proof or an inspected Kisin argument.

Milne EC2 III.3 (23)–(26), pp.102–103, gives the standard Tate equation,
integer-coefficient series for its coefficients, nonzero discriminant,
and the curve over Q_p for q in Q_p with 0<|q|_p<1. These passages,
including the integer-coefficient qualification, were inspected again
for this changed application. They cover Q_3-definition for L042's
parameter; no general-H theorem is needed for the proposed method.
Milne I.4, p.36, (8) explicitly identifies a pointed genus-one curve's
geometric point group with Pic^0 Galois-equivariantly. This supports
passing between the theorem's Jacobian torsion and elliptic torsion.
Q is dense in Q_3 by the definition of completion; no multi-place weak
approximation theorem or extension of the base field is required here.

### Applicability obligations reserved for the mathematical turn

The covered continuation must put this standard curve into the theorem's
integral squarefree cubic form, checking the coordinate change over Q_3
and the rational point at infinity. At residue characteristic 3,
completing the square has a unit denominator; nevertheless the complete
model and nonsingularity check must be written in the later proof.
Use the theorem at m=210, retain the cubic degree during rational
coefficient approximation, and verify that the resulting pointed curve
over Q, then over the specified k, meets the exact stated goal.
An existential precision suffices; no explicit coefficients or bound
are promised by this assessment.

The later proof must restrict the complete G_Q_3-module isomorphism to
the subgroup G_H inside the fixed closure and recover both requested
levels. It must compare the pointwise-fixing kernels for all torsion
points and their full coordinates, rather than identifying fields from
their degrees. This checks equality of embedded fixed fields even if
the torsion-module isomorphism uses a different basis. Abstract field
isomorphism, a cyclic subgroup and x-coordinates alone remain insufficient.
These are standard specialization obligations, not results derived here.

The covered attempt continues if it proves both full rational 30-torsion
and the exact embedded 7-torsion field N. A failed model hypothesis or
failure to preserve the full kernel must be recorded precisely and
stops this mechanism; a degree match alone does not pass. After a pass,
global rational 30-torsion and F/F_0 degree conditions still require
separate source assessment. No effective approximation radius is needed
for the present existential target.

### Search, overlap and access record

Queries inspected on 2026-10-11 included `Kisin local constancy finite
etale morphism p-adic families Galois representations Proposition 1.1
pdf`, `elliptic curves local constancy mod n Galois representation
p-adic close coefficients Krasner lemma`, `Kisin local constancy pdf
1999`, `Tame torsion Kisin Theorem local constancy`, `locconstpap pdf`
and `Kisin Theorem 5.1 finite local constancy`. Search failures imply
no novelty. The resulting journal HTML and repository PDF supply the
inspected theorem and complete short proof paragraph.

Kisin, Math. Z. 230 (1999), 569–593, DOI 10.1007/PL00004706, remains
an uninspected underlying reference. The publisher page supplied only
subscription metadata. His Harvard papers page links
https://people.math.harvard.edu/~kisin/dvifiles/locconstpap.dvi;
the web reader rejected its content type, guessed PDF/PS alternatives
were inaccessible, and a direct unauthenticated curl failed DNS.
No purchase or credential use occurred. The needed special case is
available as the inspected primary Bisatt–Dokchitser theorem, so that
DVI blocker is parked and does not block the covered continuation.
Unrelated crystalline-weight and rational ell-adic-cohomology local
constancy leads were not imported as finite-torsion results.

Scoped searches of drafts/literature/2026-10-10-*.md and ATTEMPTS/02*.md,
followed by the needed L042 and ATTEMPTS/022,025,026,027 passages, found
no duplicate finite-torsion approximation proof. L043 and ATTEMPTS/027
exclude the exact geometric curve, not this invariant. The earlier
root-of-unity exclusions concern different fixed fields; they remain
intact. No cross-notebook mathematical input is used. Full matching
Mathlib local-constancy/approximation coverage was not checked, and no
absence claim is made.

This assessment supplies known-source coverage only. The COVERED_TARGET
is a newly written ready continuation, subject to the supervisor's
separate next-turn approval. Existence and exact field preservation
remain unproved in the notebook until the mathematical specialization.
