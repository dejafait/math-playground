# Ordinary rational descent versus the retained normal closure — proposed test

TARGET: Test whether C_o can equal Q(iota,E'[30]) for a Q-defined quadratic twist E' of L118's original E, retaining the full-coordinate convention.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step503 searched quadratic twist elliptic curve torsion Galois representation quadratic character division fields; quadratic twists elliptic curves division fields equality; quadratic twist division field degree 2 elliptic curves; and 2408.04159 Lemma 3.4 correction. Scoped local searches covered L090–L092, L118, the 2026-10-20/21 ordinary-model assessments and ATTEMPTS/031,035–036; foundations/05's located twist/kernel ledger was reused. No inspected source settles this exact embedded C_o equality; this is not a novelty conclusion.
SOURCE_EVIDENCE: Inspected Sutherland MIT 18.786 Lecture 21 (6 May 2024), section 21.2 p.2; Gonzalez-Jimenez–Lozano-Robledo–York arXiv:2408.04159v1 (8 August 2024), Lemma 3.4 statement and complete proof pp.12–13; Yvon arXiv:2407.14370v1 (19 July 2024), Introduction p.2 kernel convention; Sutherland Lecture 20 (1 May 2024), section 20.1 pp.1–2; and Milne Fields and Galois Theory v5.10 (September 2022), Theorem 3.17 and proof pp.39–40, Remark 3.18(a) p.40. Only the twist-action formula and containment from Lemma 3.4 are imported, not part (2)'s stronger equality.
COMPARISON: Standard twist classification, full-coordinate action/containment and embedded-field Galois correspondence cover the mechanism. L091's nonnormality verdict concerns G_o, not C_o. The remaining specialization must compare the ordinary twist field with L090/L092's actual core, allowing arbitrary quadratic characters. No new general twisting or Galois theorem requires reproof.
GAP: The target equality or a uniform obstruction remains unproved. A later attempt must handle characters outside the ambient quotient, iota and complete 30-torsion, and compute actual kernels or a strict uniform degree obstruction. Normality, equal degrees or abstract group types alone do not prove equality.
REASON: Essential source coverage is now ready for one mathematical specialization on the unchanged L118 witness. This literature turn approves the test, not its result; it contains no new lemma or numerical specialization.
LITERATURE_REASON: Changed target from ordinary divisor coefficients to rational-descent division fields; the step500/501 assessment does not cover quadratic-twist field comparisons. Step503 completes that missing coverage; no further refresh is requested.
SCOPE: One L118 original E/Q with j neither 0 nor 1728, one ordering o and its literal E_o,F=G_o,C_o in the fixed closure, iota^2=-1; E' ranges over Q-defined quadratic twists of this E. All division fields adjoin both coordinates of every geometric torsion point. Do not replace C_o, change the integral witness or assert the two source readings are equivalent.

## Why this target, and how to discriminate

The main gap remains finite B>=A under the original hypotheses.
L103's completed arithmetic audit leaves exact field prescription
and native identification unresolved. One possible use of this test
is to delimit whether an ordinary rational descent can account for
the retained normal closure, before considering any broader repair.
Equality here would not by itself repair the literal Legendre
prescription or establish initial data; nonexistence would exclude
only this particular explanation, not IUT or all field repairs.

L091's normality obstruction already settles the analogous question
with G_o as the proposed ordinary division field. Repeating it would
be redundant. C_o is Galois, so that obstruction does not settle this
new target. Do not merely repeat its degree-four conclusion. The
comparison must either give a necessary and sufficient field criterion
for these quadratic twists or a rigorous uniform obstruction, using
actual fixed fields. If existing results settle the exact claim,
import them and restrict later work to applicability. If the question
duplicates an existing local result, cite it and stop this test.

Essential local inputs for a later permitted attempt would be L089's
full images and nonexceptional j, L090's actual ambient group and
full pointwise stabilizers, L092's normal-closure core/degrees, and
L118's retention of that same member. L091 is the precise comparison
boundary, not an assumed field equality. Read only the needed ranges.
Step503 supplies source coverage for the full torsion action and
the relevant fixed-field method; their same-witness application remains future work. Arbitrary
quadratic characters must not be silently assumed to factor through
L090's finite ambient group. Equal abstract Galois groups or equal
degrees are not equality of embedded fields.

## Source leads and limits

- [IUT IV, April 2020 reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf):
  pp.22 and 42 are recorded in L091's completed audit. Reuse that
  qualified reading; no new endpoint authentication is requested.
- [Silverman, The Arithmetic of Elliptic Curves, second edition](https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf):
  the twisting/isomorphism classification and its torsion-action
  consequences are leads for the next review, not inspected inputs
  of this proposed test. Determine exact theorem locators before use.
- [Milne, Fields and Galois Theory](https://www.jmilne.org/math/CourseNotes/FT.pdf):
  L091 records Theorem 3.17/Remark 3.18 for normality. Exact fixed-field
  and kernel-comparison applicability here still requires assessment;
  no new source version or theorem reading is claimed.

ATTEMPTS/031,035–036 remain preserved; this target uses neither a
guessed theta-coordinate repair, another authentication retry nor the
failed scalar pole budget. Directed (*) remains parked. Full initial
data/III/P7, native action/factorization/pilot, source interpretation,
essentiality and finite B>=A remain unresolved. Mathlib coverage for
this new target is unchecked. Step502 proposed the target without approval; step503 supplies a ready
SPECIALIZE assessment, with no mathematical attempt yet completed.


## Step503 inspected inputs and approval boundary

Sutherland, [Lecture 21](https://math.mit.edu/classes/18.786/2024/LectureNotes21.pdf),
section 21.2, printed p.2, classifies pointed twists for nonexceptional
j over a perfect field by continuous characters to {+1,-1}, including
the trivial character. In characteristic other than 2,3 it gives the
short model d*y^2=x^3+A*x+B for d nonzero. Q and L118's original
nonexceptional E meet this scope; no assertion that d is a square in
M is included. This supplies all Q-defined twists in the target.

[Gonzalez-Jimenez–Lozano-Robledo–York v1](https://arxiv.org/pdf/2408.04159v1),
Lemma 3.4, pp.12–13, is stated for a number field F, a nonsingular
short equation, N>2 and a nonzero twisting parameter. Its proof uses
(x,y) mapped to (x,y/sqrt(d)) and gives rho_twist=chi_d*rho in
transported bases. Part (1) supplies containment of the full twist
N-division field in F(sqrt(d),E[N]). These are approved inputs at
F=Q,N=30. Part (2)'s stronger equality is excluded, as already in
foundations/05: the printed inference from a minus-identity image to
square-root membership is not certified. No counterexample or reproof
of that stronger claim is attempted here. The approved containment
and coordinate action suffice for the planned comparison.

[Yvon v1](https://arxiv.org/pdf/2407.14370v1), Introduction p.2,
identifies the full division field with the field fixed by the
representation kernel for an elliptic curve over a number field.
This uses coordinates of whole points, rather than just x-coordinates.
The paper's coincidence problem concerns levels on one curve; no
claim that it settles the present twist/core equality is imported.

[Sutherland, Lecture 20](https://math.mit.edu/classes/18.786/2024/LectureNotes20.pdf),
section 20.1 pp.1–2, gives the continuous full torsion representations
and the closed-subgroup correspondence for the absolute Galois group.
[Milne FT v5.10](https://www.jmilne.org/math/CourseNotes/FT.pdf),
Theorem 3.17, pp.39–40, gives the finite Galois bijection, index/degree
relation and conjugation/normality criteria; Remark 3.18(a), p.40,
relates composita to subgroup intersections. Apply these inside a
common finite Galois overfield, or use the closed absolute subgroups;
do not assert an arbitrary twist character descends to Gal(M/Q).

Approved future procedure: retain the embedded C_o and M from L090
and L092. First use the cited containment to test a uniform degree
obstruction, tracking iota and the original full level-30 image.
If that does not separate the fields, use the cited character formula
and fixed-field correspondence, adjoining the twist's quadratic field
to M when necessary. Explicitly identify the ordinary field's fixing
subgroup and compare it with the pulled-back core defining C_o.
A strict upper bound below [C_o:Q] suffices for nonexistence; matching
bounds do not suffice for equality. Stop if an input fails or a local
duplicate is found. These are permitted future checks, not conclusions.

The search also returned abelian-division-field classifications and
CM-specific twist results. Their inspected search descriptions do not
match the retained full-image core problem; their theorem proofs were
not read and are not inputs. Silverman's AEC link above remains an
unread lead in this step; Sutherland supplies the needed classification.
There is no essential source blocker. Mathlib coverage is not checked;
no absence or formal-verification claim is made.
