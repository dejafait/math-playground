# Direct norm-relation applicability — approved normality-test coverage

TARGET: Test whether L96/Q is normal using L052's local ramification data, as the first applicability condition for direct norm-relation certification.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched primary Galois prime-degree and tower terminology; checked L051,L052, the prime-two assessment, relevant histories 137-143 and ATTEMPTS/018-019 for duplication and stops; no saved normality decision found in these checked paths.
SOURCE_EVIDENCE: Milne ANT v3.08 Theorem 3.34 pp.59-60; Sutherland 18.785 Fall 2021 Lecture 5 Lemmas 5.28,5.30 pp.8-9; Milne FT v5.10 Proposition 2.20 p.32 and Definitions 3.6-3.9 p.37; prior inspected BFHP normal-extension interface reused.
COMPARISON: Known theorems supply prime existence, ramification multiplicativity and the Galois efg degree constraint; L051-L052 supply field-specific inputs, but neither those inputs nor the sources already record this exact normality decision.
GAP: Apply the inspected tower and Galois constraints to the saved fields and local ramification; normality remains undecided in this literature turn, and all global arithmetic/exclusion obligations remain unresolved.
REASON: Essential missing source coverage is now supplied for one bounded specialization of known results, without enumeration, theorem reproof or deriving the field-specific answer.
SCOPE: Exactly the TARGET using L051 and audited L052; direct-over-Q applicability only, with no relative-base, normal-closure or class-certificate test approved.
LITERATURE_REASON: Changed norm-method target needs essential Galois/ramification comparison outside saved ready discriminant and saturation scopes.

Main gap: unconditional emptiness of L032's surviving branches and other
residual signatures. Intermediate target: decide the direct norm method's
normality premise. Downstream use: reject that framework before expensive
arithmetic or justify reviewing its remaining certificate obligations.

Essential inputs: L051 and audited L052; L032 identifies the eventual
branch and L050 supplies local-nonemptiness context. No L033/L045 or
cross-notebook arithmetic is proposed. Inspect exact Galois and tower
hypotheses and relevant proof cases before attempting the test. Preserve
ATTEMPTS/013–019 and unfinished work. Check duplicates against L052 and
the completed prime-two review; do not repeat the discriminant audit.

Continue only with ready coverage for one exact normality test using the
saved fields and local data. Stop direct-over-Q certification if its
premise fails. Success establishes no norm relation, class/unit
completeness, Selmer containment or disk exclusion. Failure says nothing
about relative-base or normal-closure methods without separate comparison.
Mathlib coverage is not checked. The separate source approval is now
complete; the field-specific mathematical test is reserved for the next
research turn. No new field-specific conclusion is derived here.

## Inspected primary results

Milne, [Algebraic Number Theory](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
v3.08, July 19, 2020, Theorem 3.34, printed pp.59-60, assumes a
Dedekind domain A, its fraction field K, a finite separable extension
L/K and the integral closure B. It states sum e_i f_i=[L:K]; if L/K
is Galois, all e_i and all f_i coincide and efg=[L:K]. Inspected the
entire proof, including the general dimension argument and the
Galois case's conjugacy argument. No unramified or monogenic premise
is present.

Sutherland, [18.785 Lecture 5](https://math.mit.edu/classes/18.785/2021fa/LectureNotes5.pdf),
September 22, 2021, Lemma 5.28 and following paragraph, p.8, give
contraction and existence of a prime above each nonzero base prime
in the Dedekind integral-closure setup. Lemma 5.30, p.9, assumes a
tower M/L/K of finite separable extensions with integral closures;
it states e(r/p)=e(r/q)e(q/p) and f(r/p)=f(r/q)f(q/p).
Read its full proof: transitivity of integral closure, refinement of
ideal factorization and the tower of residue-field embeddings.
It needs no Galois hypothesis.

Milne, [Fields and Galois Theory](https://www.jmilne.org/math/CourseNotes/FT.pdf),
v5.10, September 2022, Proposition 2.20, printed p.32, excludes
inseparable irreducible polynomials in characteristic zero; read its
derivative proof. Definitions 3.6-3.9, printed p.37, define separable,
normal and finite Galois extensions. These cover the finite
characteristic-zero normal-to-Galois interface, without a new reproof.

## Applicability, overlap and bounded continuation

Use the maximal integer rings, which are the integral closures of Z
and of one another. The fields in L051 are finite over Q, so the
separability assumptions above are met. The source of the local
ramification indices is audited L052's complete completion argument,
not a repeated residue polynomial or a nonmaximal power order.
Prime existence and tower multiplicativity can transport those data;
the Galois degree constraint is to be applied only under a normality
assumption during the future test. No normality of K96 or of the
cubic subfield is assumed, and a nonnormal subfield alone would not
decide normality of its containing field.

The exact query was `site.jmilne.org ANT Galois extension ramification
efg tower prime transitive`. Primary Milne statements were inspected,
then the Sutherland tower statement and its proof. Stein's primary
web exposition was a corroborating lead; its image-rendered equations
are not needed as evidence. The failed LectureNotes05.pdf URL was
resolved by the working LectureNotes5.pdf above. Search snippets and
third-party restatements were not imported. No novelty claim follows
from this bounded search.

The prime-two assessment already inspected BFHP Proposition 3.7 and
Section 4's normal-extension framework; that adequate coverage is
reused. L051-L052 address cutoff bounds, and ATTEMPTS/018-019 park
enumeration only. This test does not reopen them. Existing exact
models and local data suffice for its input interface; a class backend,
GRH, norm relation and certified subfield groups are not premises.

Continue with one proof attempt: transport a saved ramification
index along Q subset K96 subset L96 and test the Galois degree
constraint. If this disproves normality, park direct-over-Q BFHP
certification; if no contradiction is obtained, record the limitation
without inferring normality from passing one necessary condition.
A positive normality decision requires sufficient evidence, not merely
absence of this obstruction. Relative-base and normal-closure variants
remain unassessed. The same essential inputs, unresolved assumptions,
downstream use and stop test above bind this approved continuation.
