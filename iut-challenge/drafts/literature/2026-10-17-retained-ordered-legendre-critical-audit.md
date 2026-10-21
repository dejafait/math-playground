# Retained ordered-root Legendre calculation — audit coverage approved

TARGET: Critically audit L071's six ordered-root twist classes and its retained 30-versus-4 radical-membership boundary.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step276's exact-statement and stronger-result searches in drafts/literature/2026-10-17-retained-legendre-normalization-square-classes.md and step274's odd-torsion audit comparison. Read canonical L071, relevant L070 and L045/L048 ranges, foundations/05 step272, history/276-277 and ATTEMPTS/027,028,031,032. Step278 retrieved the primary passages below for the distinct audit cases; no renewed discovery search or novelty claim.
SOURCE_EVIDENCE: Milne, Elliptic Curves, second edition (2021), II Theorem 2.4(b) pp.52-53; Auer–Top, J. Number Theory 95 (2002), pp.303-305, Introduction, Lemmas 2.1-2.2 and six-parameter discussion; Yelton arXiv:1704.06190v2 (2 August 2017), degree-three definitions and Theorem 1(a) p.1; Sutherland Lecture 21 (6 May 2024), section 21.2 p.2; Gonzalez-Jimenez/Lozano-Robledo/York arXiv:2408.04159v1 (8 August 2024), Lemma 3.4 statement and coordinate proof p.12. Continuous primary text inspected; screenshot calls supplied no readable image. Reuse L045/L070's full-coordinate torsion and Galois-correspondence coverage.
COMPARISON: The inspected general-field coordinate, twist-classification, transported-basis and full 4-division statements cover the audit's standard inputs. SPECIALIZE authorizes checking their application to L071's six rows and field identities, including trivial radicals and the whole restricted kernel; it does not certify the calculation or supply an intersection theorem.
GAP: Source coverage for the saved audit is adequate; its separate mathematical verification remains undone. The three retained memberships, full-30 forcing verdict, native T/model, exact generation and original numerical comparison remain unresolved.
REASON: This separate literature turn supplies the case-specific audit coverage missing at invocation start. Proceed next to the mathematical audit on the same target; further source work requires a changed hypothesis or a specific uncovered input.
SCOPE: Same L045/L048 curve, F, roots and full-coordinate torsion conventions; no new curve, radical adjunction to the retained base, general independence theorem or native identification.

LITERATURE_REASON: The new critical-audit target was REVIEW_REQUIRED; its essential theorem cases and formula-hypothesis boundary needed separate approval. Construction coverage is reused, not repeated to meet a scheduling quota.

## Essential inputs and intended review boundary

L045 and L048 are the direct mathematical inputs of L071. L070 is
comparison context for the already inspected character formula;
its conditional native T hypothesis is not applied to these F-models.
Foundations/05 step272 retains the independent specified-native-model
and exact-generation obligations.

Assess coverage for the actual written proof, including the inverse
coordinate map, all six ordered differences, i=zeta_60^15, the sign
character on the entire G_F, and the cyclic root differences in
Yelton's general degree-three theorem. Check the full-coordinate
identity F=K(E_0[15]) and that J=K(E_0[4]) intersect F is an
unevaluated intersection, not an independence assumption or a
failure verdict. The all-six test must not be imposed as necessary
for one row. No finite-field conclusion of Auer-Top is used over F.

Independent initial data, specified native T and E_L/T, exact global
generation, source-marked all-image factorization and essentiality
remain unresolved. This approves source coverage only; no mathematical
audit verdict, retained membership or new theorem is claimed here.

## Primary statement comparison and essential cases

[Milne, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf),
II Theorem 2.4(b), pp.52-53, treats origin-preserving isomorphisms
of general Weierstrass equations over an arbitrary field. It gives
both necessity and sufficiency of the coordinate transformation,
with nonzero scaling and translation/shear parameters in that field.
The entire statement and its converse were inspected. This is the
input for auditing L071's affine maps, their inverse and extension
at infinity. The intermediate equation with leading coefficient d
must be distinguished from the monic geometric comparison; the audit
must match the actual scaling over the radical field. No general
coordinate theorem needs reproving, and no integral-model claim is used.

[Auer–Top, publisher version](https://pure.rug.nl/ws/portalfiles/portal/14410242/2002JNumberThAuer.pdf),
Introduction p.303, gives the split-cubic Legendre-isomorphism criterion
over fields of characteristic different from 2. Lemma 2.1 p.304
characterizes halving a root 2-torsion point by two square differences;
its descent-map proof was inspected. Lemma 2.2 and its proof handle
nontrivial self-twists, and the discussion p.305 gives the six geometric
parameters. The following Proposition 2.1 assumes a finite field.
These passages cover the known square-class and parameter mechanisms,
but do not certify L071's row assignment. The audit must check each
ordering, sign and denominator directly and must not transfer that
finite-field proposition to the number field F.

[Yelton, arXiv:1704.06190v2](https://arxiv.org/pdf/1704.06190v2),
p.1, defines the full-coordinate division fields over any field of
characteristic different from 2. Its degree-three setup uses a monic
cubic with distinct roots. Theorem 1(a) gives the full 4-division field
by adjoining the fourth roots of unity and square roots of the three
cyclic root differences to the 2-division field. The definitions and
complete relevant theorem clause were inspected. This is not confined
to the later generic-field reduction. It covers both base fields in
L071 once the audit verifies their retained hypotheses and sign
conversions. It gives no intersection with an odd-division field;
no 8-division result or independence assumption is needed or approved.

[Sutherland, Lecture 21](https://math.mit.edu/classes/18.786/2024/LectureNotes21.pdf),
section 21.2 p.2, treats twists in the appropriate category, including
abelian varieties. At nonexceptional j the pointed geometric
automorphisms are the two signs, and twist classes are continuous
quadratic characters, including the trivial character. The short-form
description assumes characteristic other than 2,3. The audit must
check the retained j exclusion and pointed category; an arbitrary
unpointed curve automorphism is not this input. The source supplies
classification, not rational torsion on the second model.

[Gonzalez-Jimenez, Lozano-Robledo and York, v1](https://arxiv.org/pdf/2408.04159v1),
Lemma 3.4 p.12, assumes a number field, a nonsingular short equation
and torsion level greater than 2. Its proof writes the twist coordinates
and the scalar-sign representation in transported bases. That formula
is written after the additional assumption that the radical is outside
the original division field. The coordinate equalities precede its
subsequent use to select a nontrivial Galois element. Following the
already approved L070 audit coverage, the mathematical audit must
check the elementary formula in both character cases, rather than
import part (2)'s stronger general field equality. Short equations are
available only after an appropriate pointed characteristic-zero change;
this applicability check belongs in the audit, not a new source theorem.

The full-coordinate convention and finite torsion module/Galois
correspondence remain covered by L045/L070's inspected Yvon
Introduction p.2 and Sutherland Lecture 20 section 20.1 pp.1-2.
No refresh of those unchanged standard inputs is necessary.

## Audit test and continuation limits

The main gap is still finite B>=A. The intermediate target is a
critical check of L071's conditional six-row criterion, which may
support a later specified-native-model compatibility test. Even a
passing audit does not identify that model or supply its exact field
generation. Foundations/05 step272 keeps that distinction and the
retained April 2020 source-version qualification.

The mathematical review should check the whole G_F action, not one
sign or x-coordinate field; the separate exact full-coordinate identity
F=K(E_0[15]); and the two applications of the cited 4-division theorem.
The CRT decomposition and rational group-law argument are elementary
applicability details already written in L071, not an unassessed new
mechanism. Check both inclusions, including infinity. The review must
retain the possibility of trivial or dependent quadratic tests and
must not replace a single passing row by the stronger all-six test.

Continue if every claimed equivalence and field identity withstands
these checks. If a source hypothesis or proof step fails, identify and
repair that precise defect within the stated audit scope, preserving
the original work. If a forcing verdict still requires the unevaluated
intersection J, stop that assertion there; this is a valid limited
audit outcome, not evidence for either forcing or failure. A new
intersection theorem or changed target requires REVIEW_REQUIRED.

L070 is a conditional character criterion, not a duplicate six-row
result or a source of native identification. The four recorded failures
concern exact-curve globalization, model quantifiers, marked coordinates
and the tensor enclosure, respectively; this audit reopens none of
them. No cross-notebook result is used. Keep the same E_0,F,K_glob,
Omega,embedding,u,w,H,N, precision and q_0 as specified above.
Full matching and supporting Mathlib coverage remains unchecked;
no absence or formal-verification claim is made. No lemma or
mathematical script is written during this literature-only step.
