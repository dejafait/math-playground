# Three-adic realization — application-audit coverage

TARGET: Critically audit L047's common three-adic witnesses, canonical scalar and entire-fiber base change.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-target queries and duplicate/failure comparison in 2026-10-10-three-adic-whole-fiber-realization.md; narrowly read L047, L033's field definition, L034's map/base-change passages, L032's residue interface, ATTEMPTS/015 and history/120–121; no new witness search.
SOURCE_EVIDENCE: Reopened FNS June 10, 2019 final manuscript Section 5 pp.17–18 and Section 7.2 p.25 through the GRH boundary, Table 5 p.27; reopened Clark Theorem 1.79 p.58 and read Stacks Section 26.17, Lemma 26.17.2 and its proof (tag 01JO).
COMPARISON: The inspected sources cover the lifting theorem, explicit pair, covariant criterion, canonical twelve-subgroup field and affine base change; L047's square-coordinate/common-c specialization still needs an independent application audit rather than citation alone.
GAP: Audit L047's exact hypotheses, two strict inequalities, shared witnesses, invariant cancellation, branch avoidance and entire-fiber identification; no missing essential source blocks that audit, and no independent correctness verdict is given here.
REASON: Separate approval now covers the unchanged audit target; reuse existing literature and perform mathematics next, without another source discovery turn.
SCOPE: One REPRODUCTION critical application audit of L047 with inputs L032, L033 and L034; inspect exact arithmetic and the intrinsic entire-fiber argument. No new factorization, witness search, connecting-image classification or global class computation.

Approved scope is only a critical audit of L047. Review the precise input
hypotheses and application, not a new factorization or class-image
classification. Essential inputs are L032 (three-adic branch residues),
L033 (the exact field K), L034 (the entire degree-twelve projective map),
and L047's completed application. No cross-notebook theorem is needed.

The existing source assessment records exact primary evidence and should
be reused if adequate. FNS's displayed pair and covariant criterion,
the entire twelve-subgroup canonical fiber and the boundary before GRH
are load-bearing. Clark's strict inequality must be checked at 1 and -1;
no unit cube lifting at three is allowed. Matching dimensions without
the field identification, or a selected point without whole base change,
would be insufficient.

Retain one common c and scalar across every factor; distinguish the
invariant of 54a1 from the modular map on E0; check that branch and
exceptional-coordinate cases are handled by the intrinsic fiber.
Exact local factorization is unnecessary if that argument is valid.
Passing confirms local nonemptiness only; failure must identify a
concrete correction or missing premise.

L045's quotient classes remain unevaluated, global intersections are not
computed, and other twists and signatures remain open. No GRH, rank,
Sha or Selmer/point equality is used. Mathlib coverage is not checked.
This assessment approves a later audit, not additional mathematics in
this literature turn or a retroactive verification of the completed proof.

## Source coverage and applicability boundaries

Primary locators and source versions remain those in the reused
[realization assessment](2026-10-10-three-adic-whole-fiber-realization.md).
The [FNS final manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf)
explicitly supplies (13,7,54a1) and the scaling criterion in Section 5.
Section 7.2 identifies the canonical fiber's twelve-subgroup Galois set
and its irreducible degree-twelve field. Table 5 supplies the 54a1
polynomial; its Selmer column is outside scope. The subsequent GRH
assumption concerns Selmer computation, which the audit must not import.
These are inspected source claims, not independent reruns of their
field computation. The canonical point, rather than a hypothetical
integer solution, is the source interface to inspect.

[Clark's notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
161-page accessible version, revision unidentified, Theorem 1.79 p.58,
require completeness, integral coefficients and approximation, and
the strict inequality |f(r)|<|f'(r)|^2. The conclusion includes an
integral root within |f'(r)| of r. This covers checking the two
applications already written in L047; it grants no cube or fourth-root
surjectivity at three. The audit must check the actual derivative and
residue assertions rather than invoke a generic unit-root assertion.

[Stacks Lemma 26.17.2 and its proof](https://stacks.math.columbia.edu/tag/01JO)
identify an affine fiber product with the spectrum of the tensor product
of its rings. This directly covers the affine base-change interface
after identifying the entire rational fiber. It does not identify that
fiber with K by dimension alone. L034's previously audited projective
map interface is reused, including exceptional charts; its hypotheses
still require scrutiny in the audit. No new base-change theorem is
reproved or new specialization established in this source review.

The existing search found no inspected theorem stating the complete
added-power/common-witness application. This is not a novelty claim.
The unread arXiv:2512.10781 lead retains its earlier unread status and
is not essential to this fixed audit. L047 is the completed local result
being reviewed, not a duplicate result to create. ATTEMPTS/015 records
the local-nonexistence stop; ATTEMPTS/008–014's distinct stops remain
preserved. Their conclusions at other primes are not imported here.

Main gap and downstream use: global 54a1 class intersections, L045's
unevaluated quotient classes, other twists and signatures remain open.
An independently valid L047 would justify retiring this local
nonexistence mechanism and returning attention to a different global
condition. Passing requires all stated witness and whole-fiber claims;
failure must isolate a concrete correction or missing interface, rather
than trigger more witness enumeration. Mathlib matching and supporting
coverage remain not checked; unknown does not establish absence.
