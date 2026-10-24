# Same-selected-prime rank-one cover and cusps — source coverage

TARGET: Test a rank-one factor of [ell] on L105's unchanged E_o over K_C for a geometrically connected degree-ell punctured cover, K_C-rational cusps and the inversion quotient square.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step428 compared L053's original algebraic proof and separate audit, both saved cover assessments and ATTEMPTS/029,030,034,035; searched elliptic curve rational torsion subgroup quotient isogeny factor multiplication rational kernel finite etale cover; inspected the general-primary inputs listed below rather than inferring coverage from search snippets.
SOURCE_EVIDENCE: Sutherland MIT 18.783 Lecture 5 (2023-09-26), Corollaries 5.2,5.10, Theorems 5.8,5.11,5.25, printed pp.2-6,14; Milne EC2 second edition, II.1.7 p.49 and II.6.3 p.70; Stacks tags 0BND,03SF,04GK,04UV,04ZP,04XD,04XB, live statements inspected 2026-10-23; direct URLs, hypotheses and proof cases below. No new native PDF retrieval is needed for this algebraic-only target.
COMPARISON: Quotient/factorization and prime-to-characteristic torsion results are general in the prime and base field; monodromy, henselian splitting and quotient-stack descent inputs have no level-seven restriction. L053's audited algebraic method therefore covers the proposed application obligations, but its old-member conclusion and Tate-selected line are not transferred. General source theorems are sufficient; a general reproof or novelty claim is unwarranted.
GAP: The actual same-member application must still choose U over K_C, identify the complementary factor and its whole origin fiber, prove connectedness and the whole cusp decomposition assertion, and check the 2-cartesian square and degree by the cited methods. No such construction is performed in this literature turn; local Tate-line choice, graph labels and native compatibility remain outside coverage.
REASON: This completes the separately requested comparison for the invocation-start target with changed member/base/prime; it permits one bounded known-method mathematical specialization next, without repeating coricity approval or authentication retrieval.
SCOPE: One rank-one algebraic factor over unchanged K_C=C_o(E_o[ell]), including puncturing, constant deck action, geometric monodromy, rational cusps, original-cusp decomposition and inversion quotient stacks; no local line, graph label, native clause-(d) application, theta splitting, field repair or numerical conclusion.

Proposed inputs: L089,L090,L092,L105 fix one member, order o and
ell>=7; L106 supplies the audited unadorned core if subsequently needed.
Retain G_o, C_o and full K_C in the fixed closure. Proposed construction
only: choose a one-dimensional subgroup U of E_o[ell], form E_o/U and
test the factor psi of [ell], removing its entire origin fiber. Check
geometric connectedness, degree ell, constant deck action, all rational
cusps, original-cusp decomposition image and the actual inversion square.
None of these conclusions for the new objects is derived in step427.

Do not substitute full multiplication (degree ell^2), identify K_C with
the old N, prescribe a local mu_ell line, or infer a graph label from
rationality. ATTEMPTS/030's rank-two/full-cover obstruction survives.
Assess the existing general methods before any new proof; cite them
and justify only their changed application, with no duplicate theorem.
The step427 proposal alone did not approve this target. The separate
step428 source comparison below now approves its stated algebraic scope.

Main gap remains finite B>=A. A passing construction could provide a
basic global cover for a later clause-(d) test over C_o, leaving local
compatibility with all selected places independent. Continue if the
known quotient/factorization results cover the actual objects and the
degree/cusp/stack tests pass; narrow or stop on a precise failed
hypothesis. Native graph/splitting/section conditions, III/P7, exact
generation/full repair, relative factor-four excess, source/def=
qualifications, input/action/pilot and essentiality remain unresolved.
Full matching Mathlib coverage is unchecked. No new mathematics or
native initial-data conclusion is derived here.

## Step428 — inspected general inputs and applicability boundary

This is the separate literature approval requested at invocation start.
It changes the proposed assessment to SPECIALIZE; it does not execute
the proposed construction. The exact TARGET and retained inputs above
are unchanged. L106 is an available core input for later work, not an
essential premise of this algebraic construction. The characteristic-zero
elliptic curve and full-coordinate field are fixed by L089,L090,L092,L105;
no identification with L053's old E_0,K,N or prime seven is permitted.

[Sutherland, Lecture 5, 26 September 2023](https://math.mit.edu/classes/18.783/2023/LectureNotes5.pdf):
read Corollary 5.2, Theorem 5.8 and its fiber argument, Corollary 5.10,
Theorem 5.11 with its complete quotient proof sketch and field-of-definition
qualification (printed pp.2-6), and Theorem 5.25/proof (p.14). Finite
subgroups of geometric elliptic points give separable quotient isogenies;
definition over the base requires subgroup Galois invariance, not merely
an abstract subgroup order. The quotient proof checks the free translation
orbits, absence of ramification, genus one and the rational image of the
origin. The kernel size equals separable degree, degrees multiply, and
multiplication by a nonzero n has degree n^2 and is separable when n is
prime to characteristic. These statements cover arbitrary ell. The
lecture's equation restrictions in small characteristic do not obstruct
this characteristic-zero application. They are imported, not reproved.

[Milne, Elliptic Curves, second edition](https://www.jmilne.org/math/Books/EC2.pdf):
read II.1.7 (printed p.49, PDF p.54), including the distinction between
geometric point-kernels in prime-to-characteristic degree and group-scheme
kernels otherwise. It gives factorization of two isogenies with common
source when the first kernel is contained in the second. Read II.6.3
(printed p.70, PDF p.75) and its characteristic-zero proof case: geometric
m-torsion is free of rank two over Z/mZ when m is prime to characteristic.
K_C has characteristic zero and, by its definition, contains both
coordinates of every geometric ell-torsion point. These are the precise
premises to use; no local Tate uniformization or global field normality
is a premise of these source theorems. Factorization is not a claim that
the quotient curve has its entire ell^2-point torsion rational. The later
application needs only the particular fiber of its complementary map.

For the punctured cover and cusp test, read the live statements of
[Stacks Theorem 58.6.2, 0BND](https://stacks.math.columbia.edu/tag/0BND),
including pullback compatibility and basepoint conjugacy, and
[Section 58.7, 03SF](https://stacks.math.columbia.edu/tag/03SF), including
the connected-cover/regular-fiber criterion. They require a connected
scheme and a geometric basepoint, not a special prime. Read
[Lemma 10.153.7, 04GK](https://stacks.math.columbia.edu/tag/04GK), the
equivalence between finite-etale algebras over a henselian local ring
and its residue field, with its local-factor proof case. The application
must use the henselization at the K_C-rational origin, whose residue
field is K_C, and must check the full split fiber. Rationality of one
cusp or vanishing inertia alone would not check the whole decomposition
group. These are application obligations, not conclusions of this review.

For inversion, read [Stacks Situation 95.15.1 and Proposition 95.15.3,
04UV](https://stacks.math.columbia.edu/tag/04UV), including the torsor
objects, their arrows and the identification with the quotient stack.
The source allows a group algebraic space acting on an algebraic space
over a base. Its torsor description, as used in L053's audited proof,
covers a common constant order-two group on both sides of an equivariant
map without requiring free actions. The next application must retain
the isomorphism of induced torsors in the fiber product and check arrows;
coarse quotients cannot replace these stacks.
Read [Lemma 100.3.1, 04ZP](https://stacks.math.columbia.edu/tag/04ZP) and
[Lemma 100.3.3, 04XD](https://stacks.math.columbia.edu/tag/04XD), with their
proofs: a surjective flat locally finitely presented algebraic-space
presentation tests representability, then the listed morphism properties.
[Section 100.3, 04XB](https://stacks.math.columbia.edu/tag/04XB) lists
finite, etale and finite locally free among the permitted properties.
Degree must be checked on the same presentation. This covers the stack
descent obligation and retains stabilizers, rather than removing them.

## Duplicates, failures and decision

Reused `drafts/literature/2026-10-12-native-rank-one-cover-cusp-application.md`,
`drafts/literature/2026-10-15-retained-global-cover-clause-application.md`
and `drafts/2026-10-12-native-cover-cusp-source-notes.md`, and read
L053's original algebraic proof and separate audit through its stack
descent check. Its later global clause-(d), point-group exponent, graph
and splitting applications are not part of the present construction.
The search lead Achter-Wong, *Quotients of elliptic curves over finite
fields*, concerns full torsion on the quotient and was not inspected
beyond the returned abstract; it is not an input or an obstruction to
the narrower complementary-kernel target. No absence or novelty claim
is inferred from the search. Full matching Mathlib coverage remains
unchecked; a non-Mathlib Lean project returned by search is not coverage.

ATTEMPTS/029 bars redundant unchanged core approval, not this different
cover test. ATTEMPTS/030 preserves the rank-two full-multiplication stop;
the proposed factor must have degree ell, not ell^2. ATTEMPTS/034's
cyclic Frobenius separator and ATTEMPTS/035's authentication mechanism
remain parked and are not needed here. The May/April 2020 native-source
and def= qualifications remain unchanged; algebraic cover coverage does
not authenticate those sources or verify their complete initial data.

Continue with the exact TARGET once, using these general imports and
L053's audited proof as a method, not as a conclusion on new objects.
Record the same-member applicability proof canonically if the tests pass;
do not reprove the general quotient, monodromy or descent theorems.
Abandon or narrow this construction on failure of rational subgroup
definition, the full fiber test, connectedness or the actual stack
square. Any added local/native assertion needs its own scope review.
This coverage approval supplies no mathematical advance beyond known
sources, actual cover over K_C, or reduction of the main finite B>=A gap.
