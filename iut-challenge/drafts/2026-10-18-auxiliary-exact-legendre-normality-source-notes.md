# Exact auxiliary Legendre field: normality source review — step313

Literature-only work on the saved normality target. No normality verdict,
new kernel computation, lemma or mathematical script is established here.
Main gap: original finite B>=A. Intermediate target: decide G/Q normality
for the unchanged L073/L074/L077/L078/L079 auxiliary witness. A pass would
close one independent initial-data prerequisite; a failure would stop that
exact field's use under the prerequisite, without refuting IUT. The test
requires invariance under every Q-conjugation or a verified changing
conjugation. If the witness data do not decide this, isolate the missing
information instead of enlarging G or presuming a global image.

## Inspected sources and limits

[Antieau–Meier, arXiv:1608.00851v3, 5 May 2020](https://arxiv.org/pdf/1608.00851v3),
Proposition 4.5, Corollary 4.6 and following discussion, printed pp.14–15,
were already covered for L079. Freshly read the subsequent construction
and Lemma 4.7 with its complete proof, pp.15–16. The base is Z[1/2].
The corrected S_3-action on B C_2 over the parameter scheme changes the
torsor by the square-root torsor of

    g(p)/p = (e_(g(2))-e_(g(1)))/(e_2-e_1),

where p=e_2-e_1. The coarse action alone omits this factor. Lemma 4.7
gives equivariance for this corrected action; its proof compares the
torsors and their compatible isomorphisms. This is an inspected known
input for conjugate ordered-root comparisons, not a theorem that their
15-division fields coincide. Applying it to this particular G remains
mathematical work. Keep the source's right-action convention when matching
L074's row labels; do not identify conventions by name alone.

[Milne, *Fields and Galois Theory*, v5.10, September 2022](https://www.jmilne.org/math/CourseNotes/FT.pdf),
Definitions 3.7/3.9 and Theorem 3.10, pp.37–38; Theorem 3.17(c,d),
pp.39–40, including both proof directions; Remark 3.18(a,b), p.40,
were inspected. In a finite Galois ambient extension, conjugate subfields
correspond to conjugate subgroups, and an intermediate field is normal
exactly when its subgroup is normal. The normal closure is the compositum
of its conjugates. These are general criteria, not a computed subgroup
for G. Characteristic zero gives separability here. A later use of a
finite Galois ambient field must actually identify one containing the
necessary generators; do not silently assert that F' is such a field.

[Gonzalez-Jimenez–Lozano-Robledo–York, arXiv:2408.04159v1,
8 August 2024](https://arxiv.org/pdf/2408.04159v1), Lemma 3.4 statement
and full proof, pp.12–13, were retrieved. For a number field, nonsingular
short equation, nonzero quadratic-twist parameter alpha and N>2, its
transported-basis calculation gives rho_(E^alpha,N)=chi_alpha rho_(E,N).
Reuse only this formula and part (1)'s inclusion. Keep the pre-existing
step272 qualification: part (2)'s stronger division-field equality is
not certified or imported. Its argument from an element acting as -Id
to radical membership does not supply the full-kernel check required
by this review. No new disproof or repair of part (2) is attempted.

[Sutherland, MIT 18.786 Lecture 20, 1 May 2024](https://math.mit.edu/classes/18.786/2024/LectureNotes20.pdf),
section 20.1, pp.1–2, was inspected for the number-field full-torsion
representation, choice-of-basis convention, continuity and closed-subgroup
correspondence. Reuse the precise full-coordinate kernel convention in
step272 and L074 rather than replacing it by an x-coordinate field or
abstract matrix-image group. The known twist formula must be checked on
the entire relevant subgroup, not merely on L073's one tau.

Reuse the source-version qualifications of foundations/05 step272 and
the L079 source review. Fresh retrieval of the author-hosted April 2020
[IUT IV](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf)
confirmed Theorem 1.10's field prescription p.22 and Corollary 2.2's
definition and repeated prescription pp.41–42. Corollary 2.2(ii) asserts
existence of initial data subject to its compact-boundedness and finite
exceptional-set conditions. It is not an independently checked
normality theorem for this particular witness: those additional
hypotheses have not been verified here. Import neither that conclusion
nor a Galois property of G from the abbreviated F_mod/30 notation.
The independently required Galois condition remains the inspected
IUT I Definition 3.1(b), pp.61–62, with the May 2020 reproduction and
unverified author-endpoint byte-identity qualification already recorded.

## Scoped overlap and failure check

Read L073's hypotheses and witness/scalar conclusions; L074's six-row
coordinate and full restricted-kernel calculations; L077/L078's exact
field hypotheses and imported methods; L079's source/stabilizer scope;
foundations/05 step272; the relevant normalization and exact-subfield
assessments; history/308 and history/312. Targeted searches in the
auxiliary source notes, assessments and history/304–312 found the
normality question expressly unresolved. L074 excludes radicals from
F_aux, not from G. L078 does not identify G with F' or transfer
F_aux/Q normality to it. L079's coefficient-field equality does not
identify the full conjugate division fields. These are input limits,
not a new mathematical obstruction or normality verdict.

Checked ATTEMPTS/027,028,031,032,033. Their stops concern exact-curve
globalization, broad model quantifiers, marked coordinates, the tensor
enclosure objection and unnecessary classification retrieval. None
settles this independent normality test; all remain preserved.
The warning against importing Lemma 3.4(2) already appears in
drafts/2026-10-17-retained-global-model-source-comparison.md and the
odd-torsion assessment. This review preserves it instead of auditing
that different theorem.

## Search and comparison record

Searches on 2026-10-18 included `Legendre elliptic curve division field
conjugate lambda quadratic twist Galois normal field`, `Antieau Meier
Brauer group moduli elliptic curves Corollary 4.6 Legendre S3 equivariant`,
`"Legendre" "division fields" "Galois" quadratic twists`,
`"Antieau" "Meier" "Legendre" "equivariant"`,
`"Legendre" "field" "Galois" "Mochizuki"`,
`"Legendre" "torsion" "normality" field`,
`"Legendre" "division field" "conjugate"`, and
`"quadratic twist" "division fields" "normal"`.
No inspected theorem directly decides this exact specialized G/Q.
Some searches returned unrelated uses of Legendre or normality; these
provide no evidence of novelty. Search leads concerning division-field
coincidences, maximal images, CM lambda invariants, Masser–Wustholz and
finite-field Legendre results were not inspected as normality theorems
and are not imported. The changed-scope primary input actually obtained
is Antieau–Meier Lemma 4.7; the general Galois and twist methods are
covered without resolving any of those leads.

## Ready scope for the next mathematical turn

SPECIALIZE is appropriate: the known corrected permutation action,
coordinate comparisons, twist representation formula and Galois
correspondence cover the proposed methods; no source supplies a ready
yes/no verdict. No general theorem needs reproving. The required work
is their application to the same embedded generators and the actual
conjugations of the auxiliary witness. The six equations are a list of
possible ordered-root models, not an assumption that all six parameters
occur as Q-conjugates. Do not assume full mod-two image, independent
radicals, a joint-image condition beyond L073, or G=F'.

Essential inputs: L073,L074,L077,L078 and audited L079, with the same
E_aux,F_aux,F',D,s,t,E_L,G,H,N and embedding. Preserve retained
E_0,F,K_glob,q_0 separately. Continue only on the exact saved target.
A normality proof must cover all actual conjugations and both torsion
coordinates; a negative result must exhibit a changing conjugation.
If undecided, record the precise remaining radical/kernel or witness
information rather than a passing verdict. Other independent initial
data, retained memberships/scalar occurrence, source-marked all-image
factorization, pilot transport, essentiality and finite B>=A remain open.
Full matching and supporting Mathlib coverage for this combined target
is not checked; this says nothing about absence from Mathlib.
