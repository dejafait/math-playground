# Split-charge determinant cup/Euler extension — source comparison

TARGET: Test whether L092's determinant-cup Euler exclusion extends to L071-admitted pairs with a factor charge 14r^2, allowing stable and split fibres in the same family.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 231 searched hyperkahler Fourier-transform IT, K3 split/polystable degree-zero fibre cohomology and rank-two hyperholomorphic determinant cup obstructions; compared L071/L092, ready uniform assessments and ATTEMPTS/042/043/051/059. No matching full enlarged-domain exclusion was identified in inspected results; no novelty claim follows.
SOURCE_EVIDENCE: Freshly read BBHR (1998) Definition 2, Section 3.3, Lemmas 1–2 and Theorem 3 with their proofs, pp. 244–246; Huybrechts author draft Chapter 1 (2.5), Chapter 9 Sections 1.2/3.1 and Theorem 4.9; Thomas math/9912179v2 Lemma 1.5 and its complete proof, p. 5; Stacks 36.31.3 (0BDK), statement and full proof, live 2026-10-11. Reuse the prior uniform audit's remaining qualified base-change/duality/cup coverage.
COMPARISON: BBHR preservation assumes every-parameter IT, not irreducible fibre restrictions or a moduli-space base; the published degree-zero line section criterion covers the nontrivial split-line endpoint check. Perfect concentration is fibrewise and imposes no constancy of stable/split type. No inspected source states the full split-charge cup/Euler exclusion.
GAP: No essential source blocker remains for this exact target; research must justify endpoint vanishings in both fibre cases, constant derived concentration despite type variation, actual preservation and both same-class section forms, then delimit the strict Euler exclusion without assuming existence on its complement.
REASON: Approve one separate REPRODUCTION specialization of the unchanged TARGET; cite the general inputs and prove only their enlarged-domain application, with the nontrivial split-line check explicit. No extension is proved or audited by this literature turn.
LITERATURE_REASON: The saved REVIEW_REQUIRED target changes fibre stability hypotheses; fresh reads settle that changed source scope while reusing the audited actual-map machinery.
SCOPE: L071's identical marked projective K3 factors, fixed h and Omega, full negative tensor -tau_D, hypothetical locally free rank-two Omega-polystable F with integral c_1=0, a,b<=-9 and (a+4)(b+4)=6 modulo 12; at least one charge m=-(a+4), n=-(b+4) has the form 14r^2. Higher characters are unrestricted subject to rank two; no inverse or prescribed image is assumed.

## Proposed comparison and bounded test

The universal gap is algebraic realization of arbitrary primitive
rational Hodge classes. The intermediate target is whether the retained
split-charge portion of the common-kernel recipe admits the same
cohomological obstruction. A valid extension or a precise failure of
concentration would delimit which common-kernel data warrant further
construction work. No such extension or failure is proved here.

Essential local inputs for the next comparison are L071's actual
connection and exact-h factor classification, L090's coefficient
square-zero/actual-map method, L091's arbitrary-rank section-form method,
and audited L092. These retain one actual F, both actual projections
and the same determinant cup. L072 is only an overlap comparison;
no L079 branch, individually chosen block or cross-notebook input is
proposed. No new direct dependency is recorded before a result exists.

The unresolved application is all-fibre concentration when the stable
fibre hypothesis is removed at the split charges. Check both possible
fibre types, possible change of type over the base, actual derived
base change and the precise BBHR preservation hypotheses. Only then
can both actual image forms and the same-class comparisons be tested.
The numerical threshold sought is an exclusion on the strict
negative-Euler region already written in L092, now in this omitted
charge domain; its applicability is not assumed. Preserve the equality
and positive side without an existence inference.

Continue only if the primary-source comparison covers these changed
hypotheses and identifies a justified mathematical test. If concentration
or preservation has an essential uncovered hypothesis, record that
specific obstacle and narrow or replace the target. Do not retry the
old compatible character/parity filters in ATTEMPTS/042/043/051.
ATTEMPTS/059 retires the covered nonsplit-charge negative-Euler recipe;
it does not decide this excluded domain. The independent analytic
SOURCE_BLOCKED route remains parked. Kernel construction, prescribed
mixed action, transport and universal Hodge realization stay unresolved.

Reuse the primary locators in
[the uniform audit assessment](2026-10-11-uniform-euler-cup-critical-audit.md)
where their hypotheses match. Additional literature has the specific
reason of changed fibre stability hypotheses, not a quota requirement.
At proposal time a separate source comparison was required. The completed
comparison below grants source-scope approval only; no split-charge
exclusion is derived or verified. Full matching Mathlib coverage is not
checked, not absent.

## Completed source comparison, step 231

The unchanged TARGET is approved as **SPECIALIZE** for one separate
**REPRODUCTION** attempt. The substantive difference from the ready
uniform assessment is possible reducibility of fibre restrictions, not
a changed metric, tensor, rank, determinant or chosen image.

**Primary preservation input.** Read Bartocci–Bruzzo–Hernandez Ruiperez,
*A hyperkahler Fourier transform*, Differential Geometry and its
Applications **8** (1998), 239–249,
[Definition 2, Section 3.3, Lemmas 1–2 and Theorem 3, pp. 244–246](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=6),
including the complete proofs. The source is compact hyperkahler; the
spheres are compatible; the kernel is a hermitian quaternionic instanton;
the source instanton must satisfy odd or even IT at every parameter.
There is no fibre-irreducibility or moduli-space-base hypothesis. The
proof retains induced-complex-structure cohomology invariance and the
natural twistor base-change isomorphism. Use flat O as source in both
directions and L071's actual conditional connection, only after the
changed all-fibre IT check. Section 4.1's invertibility and irreducibility
results have extra assumptions and are not imported. Reducible images
remain permitted; agreement of indices supplies no kernel.

**Endpoint source and its qualification.** Read R. P. Thomas,
*Examples of bundles on Calabi-Yau 3-folds for string theory
compactifications*, Adv. Theor. Math. Phys. **4** (2000), 231–247,
[math/9912179v2, 19 April 2001, Lemma 1.5 and proof, p. 5](https://arxiv.org/pdf/math/9912179v2#page=5).
Its proof explicitly uses the criterion that a line of nonpositive
Kahler degree has a section only in the trivial degree-zero case.
The constructed surface, bundles and numerical slope calculation are
special and are not imported. For the criterion at real h, the separate
application must invoke positivity of h on a nonzero effective divisor;
it needs no integral-degree rounding. Verify nontriviality of both lines
using L071's nonzero split charge, and apply Serre duality separately.
Do not include the trivial zero-charge split or claim split fibres are
stable. Publisher retrieval failed; the full primary arXiv version was
successfully read, so this is no persistent source blocker.

Rechecked Huybrechts, *Lectures on K3 Surfaces*,
[author prepublication draft](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf),
Chapter 1 (2.5), pp. 11–12; Chapter 9 Section 1.2, pp. 168–169;
Section 3.1(i)–(iv), pp. 175–176; Theorem 4.9, p. 182.
These cover line RR, coefficient Serre duality, real-Kahler slope
stability and dual stability, line stability and HE/polystability.
The split case requires the cited line criterion above; simplicity
alone is not a section-vanishing theorem. The stable-case and
arbitrary-rank stable-Hom applications retain their audited local
arguments. No new cohomology dimension or exclusion is computed here.

**Type variation and actual maps.** Rechecked
[Stacks 36.31.3, 0BDK](https://stacks.math.columbia.edu/tag/0BDK),
statement and complete proof. A perfect complex has an open locus of
fixed-rank concentration in a specified degree; its universal condition
is derived pullback to a bundle in that degree. The proof uses fibre
dimensions and open rank decomposition, not a constant stability type.
Reuse 36.30.1's inspected Noetherian proper/base-flat case from the
uniform audit for perfect pushforward and derived coefficient base
change. Research must check every fibre, then the closed-point
complement argument and fixed rank. No global choice or gluing of
split lines, no fixed split locus and no generic-only IT are allowed.

Reuse the [uniform audit assessment](2026-10-11-uniform-euler-cup-critical-audit.md)
for the bounded coherent/perfect duality qualification in 0A9Q,
smooth-proper right-adjoint base change, actual cup/counit/trace maps,
Kunneth and finite Euler bookkeeping. Fibre simplicity does not enter
these statements. L090's coefficient identity and L091/L092's full
trivial-part method are audited local inputs, not known conclusions for
this enlarged domain. Both forms and both actual maps still require
the application check on the same coefficient class and determinant.

**Search, overlap and stopping boundary.** Exact/stronger queries used
`"hyperkahler Fourier transform" "IT" quaternionic instanton`,
`K3 polystable split bundle degree zero cohomology Fourier Mukai IT families`,
`"rank two" "Hodge" "cup" "hyperholomorphic"`,
`"hyperholomorphic" "split" "cup" K3 bundle cohomology`, and
`"K3" "polystable" "no sections" "degree zero"`.
The Thomas source was followed to its primary proof. Search leads for
BBHR's special K3 equivalence and Verbitsky's moduli-kernel stability
paper were not imported as statements about arbitrary kernels.
The latter full theorem/proof is unread and nonessential to Theorem 3's
inspected scope. Other search snippets, including claimed Hodge
resolutions, provide no mathematical input. Failure to find a matching
full exclusion does not establish novelty or absence.

ATTEMPTS/042/043/051 stop compatible index/character mechanisms.
ATTEMPTS/059 and audited L092 stop the nonsplit-charge strict region;
they explicitly omit the present domain. Do not redo their arithmetic
as an advance. Retain the parked analytic SOURCE_BLOCKED route.

The next attempt must test every-fibre concentration with either type,
then compatible preservation, full trivial-part perfection and both
actual same-class maps. The sought threshold is exactly L092's strict
region `(m-12)(n-12)<18`, intersected with the admitted split-charge
domain; no new region or implication is asserted in this assessment.
Continue if all essential bridges survive and report the precise
extension; narrow or abandon on a failed bridge. Keep equality and
positive Euler without an existence inference. Essential IDs are L071,
L090, L091 and audited L092. Common F, prescribed mixed action,
transport and universal Hodge realization remain independent gaps.
No general theorem needs reproof. Full matching and supporting Mathlib
coverage are not checked. No lemma, mathematical script, DAG or PROOF
argument changes are made in this source turn.
