# Simultaneous five/six-shell extension — source scope approved

TARGET: Test whether L060's minimizing columns admit a simultaneous PSD extension to the complete distance-six shell while preserving every represented unordered triple and forbidden-distance zero.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 201 searched mixed-layer Terwilliger reduction, constant-weight coupled-shell SDP and prescribed/nonnegative PSD completion; compared foundations/04,09,10,12, the one-column assessments, L059/L060, step 200 and ATTEMPTS/035,038–042. Primary Schrijver passages cover unequal layers; no inspected theorem supplies this fixed prescription's verdict.
SOURCE_EVIDENCE: Schrijver DOI 10.1109/TIT.2005.851748, eight-page author manuscript, (7), Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59) and III.B (64), printed pp. 2,5–7; new canonical coverage in foundations/09. Reuse foundations/04,10,12; rechecked Sano Theorem 2.6/full proof and Dreyer arXiv:2112.03758v1 Theorem 5.2/full proof for block rather than scalar scope.
COMPARISON: Known mixed-layer algebra and singular-Schur criteria cover the necessary tools, including a rectangular cross block and singular retained shell. They do not decide simultaneous compatibility, entrywise nonnegativity or prescribed unordered moments. The difference is an exact finite application, without a novelty claim or need to reprove these theorems.
GAP: Verify all prescribed unordered-triple presentations, constraint-preserving symmetry, complete mixed-layer normalization/range reduction and the full generalized-Schur remainder; obtain an exact witness or obstruction. No coefficient evaluation or feasibility verdict was performed in this literature turn.
REASON: The formerly uncovered whole-shell scope is now covered at theorem level. Preserve the exact saved target and proceed to its finite mathematical test, retaining all fixed entries instead of invoking an unconstrained completion.
LITERATURE_REASON: The entire new distance-six shell changes the one-column hypothesis; essential unequal-layer block coverage and prescribed-cross-entry comparison were missing. Existing singular-Schur, Johnson and moment coverage was reused.
SCOPE: Exactly TARGET at unchanged L053 rho,p_5,p_6, audited L056 full five-shell and audited L060 minimizing parameter; one fixed anchor, all distance-six indices, nonnegative remaining triples, every represented unordered moment and forbidden-distance zero. No changed columns, pairs, labels, additional scalar inequalities or global PSD claims.

## Preserved finite scope

Fix a 68-subset D of the same 1024-point ground set. Retain L053's positive
rho and fixed pairs p_5,p_6, L054's full-region dictionary, L056's entire
anchored five-shell, and L059/L060's minimizing column for every G at
half-distance six from D. Add all indices {D,G} simultaneously. Every
new diagonal and entry against {D} stays rho*p_6. Require one value for
each unordered triple represented by the L056/L060 prescriptions at any
eligible anchor, and zero when any pair has half-distance 1,...,4.
All remaining new triple entries may be nonnegative real variables.
No extra scalar upper inequalities or actual-label constraints are added.

Essential inputs are L053,L054,L056,L059,L060 and the complete energy
certificates, including step 200's critical audit. Existing coverage
must be reused where adequate, but the full rectangular cross block and
simultaneous generalized-Schur remainder are not covered by the saved
one-column assessments. A prospective invariant reduction must justify
all retained constraints and full-space modes before it is used.

Main gap: arbitrary-center safety at 67/68 agreements in the 955–957
bracket. Plausible downstream use: an obstruction would exclude this
fixed simultaneous extension; a feasible exact extension would park a
larger necessary PSD diagnostic. Neither outcome would itself give a
uniform support bound, global moments, representing measure or RS list.

The initial proposal required separate source approval. Step 201 below
provides that approval only; it supplies no extension, obstruction,
calculation or novelty claim. Preserve ATTEMPTS/035,038–042.

## Completed theorem comparison — step 201

The canonical mixed-layer citation is now in
[foundations/09](../../foundations/09-global-pair-johnson-source.md).
Schrijver's [author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf)
retains unequal row/column layer indices in (58); (64) supplies its
congruent beta normalization. The inspected proof cases include the
orthogonal change of basis and tensor extension/reset argument. This
supports a complete layer restriction, rather than a distance-only
quotient or a collection of independent column norms. Use the already
canonical beta convention in foundations/04. The suspect complement
prefactor and impossible scalar orbits remain outside the application.

The source parameters w=68,v=956 meet the stated ground-set hypotheses.
Represent a support relative to D by its removed subset in D and added
subset outside D. The retained layers are 0,5,6, of equal cardinality
in those two factors. Select exactly those source layer coordinates
and retain every admissible representation block that meets them;
do not keep only trivial modes. An exact implementation must verify
the normalization for unequal layers and recover L056's known five-shell
block. This is an applicability plan, not an evaluated reduction.

The general block criterion is already canonical in
[foundations/10](../../foundations/10-psd-completion-source.md):
[Sano](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2 Theorem 2.6 and its complete necessity/congruence proof,
Corollary 2.2 and Lemma 2.7. For retained C, cross block T and new
block A, its imported test is C PSD, T^T annihilating ker C, and
A-T^T C^dagger T PSD. It permits a whole finite new block, including
singular C, without a maximal-rank assumption. Application must transport
the entire matrix through the anchor congruence before using this test.
L059/L060 provide each column's range and scalar energy inputs; checking
only the remainder's diagonal cannot establish its PSD. All interactions
between different new indices remain mathematical work.

[Dreyer v1](https://arxiv.org/pdf/2112.03758v1), Theorem 5.2 and proof,
printed pp. 10–11, chooses an unrestricted cross block to cancel a
Schur interaction. Its hypothesis does not enforce this target's zeros,
nonnegative entries or equal-union equations. The chordal theorem in
foundations/10 has the same extra-constraint limitation. Neither supplies
a ready extension here. Albert's original proof remains an unread,
nonessential lead because Sano provides the required proof.

Reuse Polak v1 Section 1.1 (1)–(3), Proposition 1.1's indicator proof
and Section 1.2 averaging in foundations/12, with Brouwer–Polak's
explicit nonnegative formulation. The present indices are allowed in
the singleton-conditioned order-three matrix. The full source hierarchy
also imposes omitted matrices/constraints; approving this slice asserts
no full hierarchy feasibility or uniform bound. No new proof of the
hierarchy, algebra or completion theorem is needed.

## Specialization obligations and continuation test

The ordinary group of point permutations preserving D acts on both
complete shells. The proposed data depend on full-region cardinalities
and one fixed L060 minimizing parameter. Thus the available averaging
theorem is relevant to this unlabeled slice. Research must verify its
equivariance for every retained presentation and identify one variable
per unordered triple before relying on averaging. Actual subgroup-label
rank exclusions are absent, so none may be transported by this argument.

Start by enumerating every full-region type and every eligible anchor
presentation carrying an L056 or L060 value. Compare the actual moment
values with their proper rho,p_5 normalizations. Do not drop a conflicting
presentation or replace a prescribed minimizing column. Include Boolean
diagonals/anchor entries, all forbidden pair distances and nonnegativity.
The simultaneous hypothesis can fail already at this consistency stage;
no agreement between independently constructed columns is assumed.

If the prescribed values agree, verify all source blocks for the complete
coupled matrix, including new-only modes, the anchor/constant interaction
and zero modes. A rational extension needs exact coefficient checks and
complete PSD certificates; a rejection needs an exact entry conflict,
negative quadratic form, or independently checkable dual contradiction.
A numerical infeasibility report, failed solver or inability to find a
rational point is not an obstruction. No strong-duality hypothesis is
assumed. Save complete evidence rather than a preview of a few modes.

Continue only if the retained prescription has a complete exact witness
or a useful unresolved finite test after this bounded attempt. An exact
conflict or obstruction parks this fixed simultaneous prescription;
a complete extension parks its exclusion diagnostic. Either decision
leaves the independent global, scalar, label, measure, RS-realization and
67/68-agreement gaps unresolved. A materially changed prescription needs
its own assessment; failure does not license moving the saved target.

## Search record, duplicates and qualifications

Queries on 2026-10-14 included: "Schrijver Terwilliger algebra constant
weight mixed layers block diagonalization rectangular matrices";
"positive semidefinite matrix completion prescribed cross block
nonnegative equal union moment Schur complement"; "constant weight
Schrijver mixed shell semidefinite"; "Terwilliger two layers semidefinite
positive"; "matrix completion prescribed Schur complement nonnegative";
"Schrijver constant weight semidefinite programming block diagonalization
beta i j k unequal weights"; and "Schrijver constant weight two shells
positive semidefinite extension prescribed triple distribution".
Some queries returned irrelevant results; those are not theorem evidence.
The useful leads were the original Schrijver algebra, Polak's hierarchy,
general symmetry reduction and semidefinite completion. The primary
passages above, rather than snippets or search failure, support approval.

Broader Gijswijt block-algebra constructions, Laurent's symmetry exposition,
Polak's stronger four-point hierarchy and doubly-nonnegative completion
results appeared as leads; no new theorem from these was inspected or
imported. They are nonessential given the direct Schrijver reduction and
Sano block criterion. No search establishes originality or an optimum.
The author manuscript was retrieved 2026-10-14; no new version date is
asserted. Sano's publisher publication date is 2026-02-27; Dreyer is
arXiv:2112.03758v1, submitted 2021-12-03, manuscript dated 2021-12-08.
Readable formula text was inspected; screenshot requests returned only
references, so no visual inspection or local PDF is claimed.

ATTEMPTS/035,038–042 establish smaller necessary-test passes only, and
L054/L055 concern different fixed zero restrictions. None settles this
complete coupled target. The older Kim–Toan Theorem 17 route in
ATTEMPTS/017 fails its maximum-distance hypothesis; its historical stop
does not apply to the present Terwilliger/generalized-Schur mechanism.
No existing proof was altered or new lemma/script written. Mathlib's
full matching mixed-layer, singular-block and constrained-completion
coverage is not checked; this is unknown availability, not absence.
