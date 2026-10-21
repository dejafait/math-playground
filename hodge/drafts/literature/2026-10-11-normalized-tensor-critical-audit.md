# Normalized tensor construction — critical-audit source coverage

TARGET: Critically audit L089's normalized tensor construction, including determinant cancellation, the proper and linked projective-holonomy cases, and exact-h stability and acyclicity.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L089's complete proof with the ready construction assessment, L080/L088 hypotheses, ATTEMPTS/056 and histories 215/216; every audit bridge falls within the previously inspected analytic/group/cohomology scope. No fresh external search was needed or performed.
SOURCE_EVIDENCE: Reused primary-text evidence in 2026-10-11-nonspin-normalized-tensor-realization.md: Perego 1910.01867v1 Propositions 3.10,3.15,4.15, Corollary 4.16 and Theorem 4.19; Nomizu (1955) Section I.1 and Proposition 2; Bauer–Sen–Zvengrowski 1109.0024v3 Theorem 2.1; Huybrechts Chapter 9 Section 4.2 and Chapter 1 (2.6); standard Serre duality, Hartshorne III Theorem 7.6.
COMPARISON: These known tools cover a separate independent audit at the unchanged real metric, but do not themselves assert the exact normalized-tensor theorem; determinant normalization, compact-group cases, parallel adjoint identification and tensor irreducibility remain specialization checks for the mathematical turn.
GAP: Independently audit L089's essential bridges and actual cohomology; this source comparison neither verifies its proof nor constructs an actual image or common F.
REASON: The audit has the same hypotheses and techniques as the adequate construction assessment; explicit theorem-level scope comparison removes REVIEW_REQUIRED without repeating browsing or deriving mathematics.
SCOPE: L089 and its essential inputs L052, L080 and audited L088, on the same simply connected projective K3 with real h, L=O_S(k), k.h=0, k^2=-14, ordinary stable locally free rank-two E and B with determinant L and c_2=-2 eta and -eta respectively. Audit only the individual normalized tensor.

## Main gap, intermediate target and decision test

Algebraic realization of arbitrary primitive rational (2,2)-classes
remains unresolved, as do higher-dimensional cases. The intermediate
target is independent verification of L089's individual stable acyclic
symmetric rank-four charge-eight block at exact h. A verified block
could be an input to the common-kernel route, but actual image
identification, a common F with the full negative tensor and transverse
transport remain independent gaps. No such realization is assumed.

Continue with one separate proof audit under this SPECIALIZE coverage.
Check every essential bridge; repair or qualify a failed bridge. A
forced parallel summand, incompatible determinant normalization or
nonzero actual endpoint cohomology would invalidate the corresponding
construction claim. A clean audit verifies only individual K_4
existence. If a repair needs a theorem outside this scope, save that
unresolved assumption and route it to REVIEW_REQUIRED before research.

## Reused primary evidence and applicability comparison

The full ready [construction assessment](2026-10-11-nonspin-normalized-tensor-realization.md)
records the queries, source versions, precise pages, inspected proof
cases and failed access attempts. This turn read that assessment and
L089's full proof; it did not newly retrieve the external primary texts.
Reuse is justified because the exact S, h, ranks, determinants and
connection techniques have not changed. Its earlier failed book-scan
extracts remain unread leads, not evidence or essential blockers.

Perego, [1910.01867v1](https://arxiv.org/pdf/1910.01867v1),
Proposition 3.10 (p. 47) and Proposition 3.15 (pp. 49–50), including
their previously inspected complete proofs, supply tensor Einstein
functions and parallel morphism/splitting statements. Theorem 4.19
(pp. 63–65), including both slope cases and extension across the
singular set, supplies the saturated-subsheaf equality criterion.
The ordinary twist-one, zero-B-field case at a compact real Kähler
metric is the applicable scope. The audit must still establish
irreducibility before strict stability; tensor HE alone is insufficient.
Proposition 4.15 and Corollary 4.16 (pp. 61–62) cover stable Hom
constraints, with actual ranks and equal real slopes retained.

Huybrechts, [Lectures on K3 Surfaces, author draft](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf),
Chapter 9 Section 4.2, Remark 4.8(i) and Theorem 4.9 (pp. 181–182),
provide the line metric and compact-Kähler HE correspondence. The
line-metric uniqueness argument and global determinant identifications
are elementary applicability checks, not a new existence theorem.
Chapter 1 Section 2.4, (2.6) (p. 13), supplies K3 RR. Standard Serre
duality (Hartshorne III Theorem 7.6) applies to the actual locally free
bundle with trivial canonical line. Audit actual Hom endpoints before
using an Euler identity; no genericity or semicontinuity replacement
is covered.

Nomizu, [Nagoya Math. J. 9 (1955), 57–66](https://doi.org/10.1017/S002776300002328X),
Section I.1 (pp. 58–59) and Proposition 2 (pp. 60–61), covers general
principal connections, connected restricted holonomy and reduction;
the previously read reduction proof uses radial trivializations and
horizontal tangency. The smooth unitary/projective frame bundles meet
its scope. Full/restricted equality uses simple connectedness. Taking
compact closures, classifying proper connected SO3 subgroups and
constructing parallel subbundles are explicit audit checks, not an
assumption that all holonomy groups are closed.

Bauer–Sen–Zvengrowski, [1109.0024v3](https://arxiv.org/pdf/1109.0024v3),
Theorem 2.1 (p. 2), with previously inspected forward and converse
proofs, supplies Goursat's subgroup description. The audit must check
closed normal kernels, continuity of the graph isomorphism and its
adjoint intertwiner before using unequal Chern classes. The elementary
SO3 Lie-algebra cases, smooth Lie-group automorphism passage, joint
Lie-algebra surjectivity and C^2 tensor C^2 irreducibility are within
the original low-rank specialization scope. They are not verified by
this source-comparison turn. No algebraic/differential-holonomy
identification or generic independence theorem is imported.

L080 and audited L088 supply the exact ordinary factors; their
hypotheses and conclusions were inspected narrowly here. Their K3
existence theorems need not be reproved in this tensor audit. L052
supplies the unchanged S,h,k input. The audit must check determinant
connection equality, the global symmetric form, integral determinant,
full character and actual Hom-bundle identification in L089.

## Duplicates, failures and qualifications

ATTEMPTS/056 stops a necessary half-adjoint index filter, not this
individual constructive route. Histories 215/216 distinguish source
coverage and the still-unaudited construction. This audit does not
repeat that filter or assume the construction's report is verification.
Balaji–Kollár's algebraic-holonomy results remain comparison only;
they do not settle this joint connection at irrational h. No full
matching theorem or novelty claim follows from the recorded search.
No cross-notebook result is used. Full matching and supporting Mathlib
coverage remains not checked, rather than claimed absent.

This literature-only step approves the bounded audit scope. It adds
no lemma, calculation, mathematical script or proof-audit conclusion.
The newly ready continuation receives separate supervisor approval
before the mathematical invocation.
