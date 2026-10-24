# Selected-prime large-image transfer — source comparison

TARGET: Assess whether SL_2(F_ell) containment for E_o over G_o, if supplied for L101's same selected prime, transfers to C_o through [C_o:G_o]=4.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step415 compared the ready 2026-10-11/18 restriction assessments, L047/L083 restriction proofs, L090/L092/L101 field and prime passages, and ATTEMPTS/034; targeted external searches below found no stronger exact application used here.
SOURCE_EVIDENCE: Reused the inspected restriction/generation coverage and freshly read Milne Fields and Galois Theory v5.10 (September 2022), Theorem 3.17(b,d), Propositions 3.19,3.21 pp.39–42 and 7.3,7.4 p.95, plus 7.7 p.96; Conrad Simplicity of PSLn(F), undated nine-page author PDF, Theorem 3.3 and complete proof p.4, retrieved 2026-10-23.
COMPARISON: These general-field inputs cover a later conditional restriction application with base G_o, the same curve and prime, and degree-four normal closure. Full downstairs GL_2 image and G_o/Q normality are not required by the selected method; the actual finite images and normal quotient still require proof.
GAP: Source coverage is ready; the conditional transfer is not proved here. A research turn must verify full-coordinate restriction, Galois hypotheses over G_o, quotient index divisibility, elementary-generator orders and generation; downstairs SL_2 containment remains an independent unproved premise.
REASON: The changed variable-prime and degree-four scope is now assessed using known general theorems; approve only its explicit specialization as REPRODUCTION, without a new general theorem or a containment verdict in this literature turn.
SCOPE: Same L101 survivor/order/prime and fixed L089 family/domains/closure; L090 full-coordinate E_o,G_o and L092 C_o=G_o^nor with [C_o:G_o]=4; characteristic-zero elliptic curve and prime ell>=7; no change to the original downstairs H or selected prime.

LITERATURE_REASON: Invocation-start REVIEW_REQUIRED changes the fixed-seven applications to L101's selected prime, assumes only downstairs SL_2 containment and uses the actual degree-four normal closure. This turn supplies the missing hypothesis comparison and does not repeat an already approved target.

## Inspected primary coverage — step415

[Milne, *Fields and Galois Theory*, v5.10, September 2022](https://www.jmilne.org/math/CourseNotes/FT.pdf),
Theorem 3.17(b,d), pp.39–40, supplies index/degree and normal
quotient correspondence. Proposition 3.19, pp.40–41, identifies
compositum restriction over an intersection, assuming a common field
and one Galois extension. Proposition 3.21, pp.41–42, covers the
intersection when both extensions are Galois over the same base.
Reuse the previously inspected normality and compositum proof cases;
freshly read the index argument and restriction injectivity/surjectivity.
Proposition 7.3, p.95, covers Galoisness over an intermediate base;
read its complete minimal-polynomial proof. Proposition 7.4, p.95,
and Proposition 7.7, p.96, cover extension of embeddings and absolute
restriction onto finite Galois groups; their surjectivity arguments
were read. These statements impose no rational-base hypothesis.

[Conrad, *Simplicity of PSLn(F)*](https://kconrad.math.uconn.edu/blurbs/grouptheory/PSLnsimple.pdf),
undated nine-page version retrieved 2026-10-23, Theorem 3.3, p.4,
generates SL_2 over every field by upper and lower elementary
unipotents. Rechecked the upper/lower conjugation and all three
factorization cases: nonzero upper entry, nonzero lower entry and
diagonal matrices. Import this theorem without reproof. Its hypothesis
has no field-size exception; the following perfectness and simplicity
theorems are unnecessary. The proposed application uses Lagrange's
standard finite-group theorem and must check the particular generator
orders itself in the later research turn.

## Hypothesis comparison and bounded continuation

L090's statement and conjugate/core passage fix the literal E_o/G_o
and identify C_o as its normal closure over Q in the common closure.
L092 supplies the exact degree four; L101 fixes the same selected
prime ell>=7 and explicitly does not supply P4–P7. Thus the new
field data are available, while the downstairs image assumption is
not. Applying the cited intermediate-base theorem is an obligation
of the later specialization; nonnormality of G_o/Q must not be
mistaken for failure of that theorem's hypothesis about the top field.

The ready assessments
`drafts/literature/2026-10-11-mod7-image-after-torsion-adjunction.md`
and `drafts/literature/2026-10-18-exact-legendre-mod7-large-image.md`
already inspect the general method. L083's second restriction is
particularly relevant: its starting image only contains SL_2, rather
than being all of GL_2. Neither old witness's conclusion is imported.
Here E_o is unchanged on both sides of the field extension, so no
new pointed-coordinate transport or twisting theorem is needed.

The later proof must use the full field G_o(E_o[ell]) and its actual
image, not a projective or x-coordinate field. It must establish the
restricted image and a normal quotient of index dividing four before
performing the elementary-generator test for every prime ell>=7.
The cited generation theorem is uniform in the field. Continue only
if all those application obligations pass; otherwise record the
exact failed hypothesis or subgroup obstruction. Do not silently
strengthen the downstairs premise to surjectivity, change ell, or
assert that C_o lies in the old downstairs division field.

The main gap remains finite B>=A. This bounded conditional target
could isolate large-image preservation from the independent task of
establishing large image downstairs for the same selected prime.
It leaves native initial theta-data/III, P4–P7/full repair, exact
generation, the relative factor-four excess, native input/action/
factorization/pilot, source authentication and essentiality open.
No ell-integrality is assumed or supplied. Full matching and
supporting Mathlib coverage remains unchecked; this is not evidence
of absence. No lemma or mathematical script is written this turn.

## Duplicate and failure screen

The scoped restriction search located L047 and L083 for different
curves/fields, not this selected-prime implication. ATTEMPTS/034
stops a cyclic Frobenius normality separator, whereas this target
uses a conditional full representation and makes no new normality
verdict. That stop and the parked source-authentication route remain
unchanged. No cross-notebook input is used.

External queries on 2026-10-23 were `"SL_2" "Galois" "prime to"
"extension" image restriction` and `"SL_2" "unipotent" "Theorem
3.3" Conrad`. Results included unrelated large-image deformation,
IUT exposition and group-theory leads; none of their theorem texts
was imported. The primary theorem comparison above, with reused
assessments, supplies coverage. Failed search is not a novelty claim.
This is source-coverage progress only, with zero mathematical
exploration attempts and no conditional containment result yet.

## Invocation-start proposal retained — step414

The following proposal records the earlier unapproved state. The
step415 assessment above supersedes its coverage/routing statements.

This is an unapproved continuation, not a theorem or a completed
literature assessment. The exact main gap remains finite B>=A.
The proposed intermediate target tests preservation of a large-image
premise through this specific field change. Such a conditional result
could isolate the independent task of proving the premise for the
same selected prime; it need not resolve every native-data obligation.

First locate and compare the exact source assessments used by L047
and L083 and their relevant canonical restriction arguments. Reuse
any adequate general theorem coverage; their fixed-seven conclusions
are not imported for this different prime and witness. Retrieve only
missing primary hypotheses or essential proof cases. Check the actual
Galois/restriction hypotheses and any small-prime exceptions. Do not
replace a full mod-ell representation by a projective image or assume
that the original Q-curve's mod-seven image supplies the premise.

Continuation test: approve a later conditional transfer only if a
precise cited theorem or assessed specialization covers this extension
and every prime ell>=7. Otherwise record the exact failed hypothesis
or subgroup obstruction and choose an independently testable target.
This review must not prove and approve the new implication in one turn.

Essential inputs are L090,L092,L101, with L089's inherited fixed-family
conventions. SL_2(F_ell) containment over G_o is an unresolved extra
premise, not an outcome of L101's P1–P3 construction. Native initial
theta-data/III situation, P4–P7/full repair, exact generation, relative
factor-four excess, actual input/action/factorization/pilot,
authentication/def= limits, essentiality and finite B>=A remain open.
The source-authentication retry route in ATTEMPTS/035 stays parked.
Mathlib coverage is unchecked. No mathematical result is derived here.
