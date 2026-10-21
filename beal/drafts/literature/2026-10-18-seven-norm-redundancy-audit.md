# Seven-adic norm redundancy — critical-audit source approval

TARGET: Critically audit L091's seven-adic norm redundancy on L084's T.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-target discovery queries and primary-source comparison in 2026-10-18-seven-filter-on-t.md; read L091 and the input statements in L084/L088/L090, and compared ATTEMPTS/039–041 and history/300. No separate L091 application audit appears in these records; no new broad discovery search was needed for the unchanged norm machinery.
SOURCE_EVIDENCE: Reinspected Stacks Lemma 31.18.6 tag 0BD2 statement/full proof; Milne CFT III Proposition 1.2, Lemmas 1.3–1.5 and full proof p.98; Conrad Theorem 4.6 with proof pp.9–10 and Section 5 through Theorem 5.7 pp.10–11. Reused the construction assessment's Milne ANT v3.08 Proposition 8.2/Corollary 8.4 p.136 and Clark Corollary 1.77/Theorem 1.79 pp.57–58 coverage.
COMPARISON: The cited results cover determinant base change, complete local norm products, unramified unit reduction, finite norms over a nonprime residue base and odd-characteristic square lifting. They do not certify L091's ordered specialization or redundancy conclusion; those remain the work of the later audit.
GAP: Independently verify or correct L091's ordered completion maps, both V-actions, treatment of arbitrary even valuations, exact character kernel and identification invariance; no audit verdict is issued here.
REASON: The separate audit-scope comparison is complete and the exact saved target is ready for one REPRODUCTION proof audit, without redoing the already audited L088/L090 inputs or reproving general norm theorems.
SCOPE: Exactly TARGET on unchanged K,D,F,T,U,J7, importing audited L088/L090; no new global witnesses, enlarged probes, class arithmetic or rank target.
LITERATURE_REASON: The supervisor requires separate approval of the newly proposed L091 critical-audit scope; reuse construction coverage and check its applicability to the audit's essential proof cases.

The main gap is positive primitive integer emptiness. The intermediate
target is to verify or correct the new redundancy proof. Acceptance
would make the specific seven-filter stop trustworthy and permit a
different independently testable mechanism later. Reject the claimed
containment if any essential norm factor, valuation case or field
identification is missing, preserving the valid preceding inputs.

Essential input IDs: L069, L074, L084, L088, L090, and the new L091.
The later audit should check F tensor Q7=Q7 times V, U tensor V=U times U
with its two distinct V-actions, every degree in both norm directions,
inverse embedding placement, removal of local square factors for
negative as well as positive even valuations, the residue norm formula
over F49 as well as F7, and invariance under every field identification.
There is no new mathematical script or calculation certificate to
replay: the new proof is an exact symbolic envelope computation.
The previously audited field/image and global norm certificates need
not be rerun without a concrete discrepancy.

Unresolved assumptions are unchanged: no S-unit basis, localized
class-kernel value, global realization of an arbitrary envelope tuple,
rank or integer lift is available. Both dimension bounds remain
unchanged. Full/supporting Mathlib coverage is not checked. This file
records ready source scope, not a critical audit verdict. No cross-notebook
input is involved.

## Source comparison completed 2026-10-18

This approval supersedes the proposed REVIEW_REQUIRED scope above as it
stood at invocation start. The mathematical target and assumptions have
not changed. The construction assessment is reused rather than treated
as evidence of correctness of the construction itself.

The following primary passages were inspected again for the audit scope:

- [Stacks, Lemma 31.18.6, tag 0BD2](https://stacks.math.columbia.edu/tag/0BD2),
  statement and entire proof: finite locally free morphisms of positive
  degree admit the determinant norm, compatible with arbitrary base change.
  This covers the algebraic norm's transport to completions. It does not
  choose the ordered factors or identify their scalar actions for L091.
- J.S. Milne, [Class Field Theory](https://www.jmilne.org/math/CourseNotes/CFTc.pdf),
  v4.03, 6 August 2020, III Proposition 1.2 and Lemmas 1.3–1.5 with proof,
  printed p.98 (zero-based PDF page 106). The finite unramified local
  hypothesis and the unit-to-residue norm diagram are explicit. The proof
  uses residue norm surjectivity and successive trace corrections, then
  convergence. The audit needs the diagram, not just surjectivity. It must
  check the actual base and domain of each local factor before using it.
- Keith Conrad, [Finite fields](https://kconrad.math.uconn.edu/blurbs/galoistheory/finitefields.pdf),
  no version date identified, accessed 2026-10-18: Theorem 4.6 and full
  proof pp.9–10; Section 5 and Theorems 5.5–5.7 pp.10–11. Theorem 5.7
  explicitly covers arbitrary finite base F_q and gives the norm exponent
  (q^n−1)/(q−1). Section 5 leaves analogous proofs to the reader; the
  inspected prime-base proof uses conjugates and multiplicative cyclicity.
  Thus the quadratic residue base is covered by a stated theorem, without
  pretending that a separate written proof of Theorem 5.7 was inspected.

The following precise coverage is reused without another source read:

- Milne, [Algebraic Number Theory](https://www.jmilne.org/math/CourseNotes/ANTc.pdf),
  v3.08, 19 July 2020, Proposition 8.2/Corollary 8.4, printed p.136:
  all extending completions and their product norm for finite separable
  extensions. The construction assessment records the full proofs.
  Characteristic zero and the fixed fields meet the general source scope;
  the later audit must verify the particular factors and multiplicities.
- Pete L. Clark, [Algebraic Number Theory II](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
  161-page notes, Corollary 1.77 and proof p.57, Theorem 1.79 p.58:
  complete discretely valued fields and integral simple-root lifting.
  The construction assessment records these passages. Audit every use
  for a unit and nonzero residue root in odd characteristic. No new
  lifting theorem or field-specific square test is proved in this review.

## Audit boundaries, duplicates and discriminating test

L084 defines T using the entire supported W_S, not only S-units or
global point classes. L088's conclusion explicitly covers this same T,
including negative valuations and localized class lifts. L090 fixes the
same generator and the ordered rational root followed by the conjugate
pair, and supplies the entire unramified field and exact local image.
Those statement interfaces lie within the reused source scope. This
comparison does not reverify their proofs or infer L091's conclusion.

The later audit must independently reconstruct the maps rather than
accept L091's displayed character equations. In particular, verify each
V-action and its inverse identification, the degree over each base,
square removal for every integer valuation half, and the distinction
between norm on units and scalar inclusion of base units. Even relative
degree is not a reason to replace a norm by a power on arbitrary units.
Check both directions of the claimed local envelope equality and the
effect of every allowed identification. An outside local tuple, if one
is found, is not automatically a global T-class.

ATTEMPTS/039 is the audited thirteen-specific stop, ATTEMPTS/040 the
audited insufficient eleven-adic envelope, and ATTEMPTS/041 the new
seven-specific stop awaiting audit. None is a duplicate independent
verification of L091. History/300 explicitly defers that verification.
The discovery queries and unread leads recorded in the construction
assessment are reused with their original qualifications; no novelty
claim or new source lead is asserted here.

Continue only with the exact application audit. Accept the stop if every
essential map and implication passes; otherwise record the first failure
and its consequence, preserving preceding valid results. No numerical
script or rerun of prior certificates is justified absent a concrete
discrepancy. Both dimension bounds and all global/integer gaps remain.
This literature comparison is EXPLORATION/NOVELTY_UNCHECKED, not a new
mathematical input, independent proof audit or progress beyond the sources.
