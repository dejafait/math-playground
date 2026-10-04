# Nonpersistent sixteen-count equality: resultant assessment

TARGET: For the pinned RS[F_(97^20),H,8] model, test whether the resultant Res_X(X^16-1,L(T,X)) can be c*P(T)^4 with c nonzero and P split squarefree of degree sixteen while satisfying L010's sixteen-count equality criterion.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed the bounded exact-statement, Hankel/locator, perfect-power and resultant searches listed below; these located standard algebraic tests but no inspected theorem deciding the full sixteen-count compatibility. Reused adequate prior coding coverage and the July access stop.
SOURCE_EVIDENCE: Read Milne, Fields and Galois Theory v5.10 (September 2022), Proposition 4.35 and its resultant definition, Proposition 2.17 and the finite-field discussion on p. 53; Volkovich, APPROX/RANDOM 2017, Definition 22, Lemmas 23–24, Corollary 25, Lemma 48, Theorem 49 and proofs of Lemma 24/Theorem 49; Mathlib Resultant.Basic at commit 300d0e535721bc098547106fc297d8ba2a63f6bb, the product, evaluation and specialization declarations below; Artin's July 17, 2021 notes, Propositions 1.7.10 and 1.7.20. Reused local L010–L012 and the pinned event.
COMPARISON: Resultant products and perfect-power recognition are known supporting results; Volkovich also supplies a characteristic-qualified derivative identity test. They test a supplied polynomial or candidate root, rather than prove existence or exclusion of the constrained affine Hankel pencil. L010 already supplies the full coordinate equality criterion.
GAP: Determine compatibility of the fourth-power condition with L010's actual eight affine moments, simple coordinate roots, nonzero D at every relevant root and splitting over F_(97^20); no obstruction or witness for that full system was found in the inspected sources.
REASON: The changed nonpersistent equality target now has adequate ingredient coverage for a bounded mathematical test. Import those ingredients and investigate only their applicability and the remaining Hankel compatibility; a generic product identity or a reproof of a perfect-power test would not improve the fifteen-count gap.
SCOPE: The exact TARGET: arbitrary a,b over F_(97^20), H of order sixteen in F_97^*, eight affine moments and L010's determinant locator, D and every coordinate locator nonzero as polynomials, and the full original four-omission event. Approved tools are cited resultant products, monic squarefree decomposition/perfect-power recognition, and the stated characteristic-qualified identity test. No prime-subfield restriction, equality witness, impossibility proof or July correspondence is assumed.
COVERED_TARGET: For the pinned RS[F_(97^20),H,8] model, formulate and audit a coefficient feasibility system for Res_X(X^16-1,L(T,X))=c*P(T)^4 using L010's actual affine moments and all sixteen-count equality conditions.
COVERED_TARGET: For the pinned RS[F_(97^20),H,8] model, test actual nonpersistent moment pencils using the cited resultant and perfect-power checks, with full L010 equality validation and exact F_(97^20) splitting.

## Scope saved on October 3

The following motivation and stopping test were saved before this review;
their proposed mathematical calculation has not been performed here.

The remaining pinned-model gap is sixteen versus the allowed fifteen.
L010 already reduces equality to split squarefree coordinate quartics with
four incidences at every root and D nonzero there. L011 and L012 now cover
all polynomial degeneracies, so a successful obstruction to this remaining
equality would certify safety on the four-omission cell; an equality witness
would prove unsafety there. Neither would resolve all other codes and radii
or the still unread challenge definition.

The proposed test is whether the resultant power constraint can be used
with the actual affine Hankel entries and locator identities to yield a
contradiction or a concrete bounded candidate system. A generic resultant
formula or balanced abstract incidence pattern alone would be insufficient.
If the constraint merely restates L010 without restricting candidates,
record that limitation rather than report an advance or repeat the same
test. No derivation, new search or candidate computation on this future
target was performed during the singular-transfer step.

Reuse adequate ingredient coverage. Review only the changed target and
its essential source needs; July/Jo access remains parked and is not an
essential input to this independent pinned-model question. The existing
four-block source blocker and full-orbit obstruction are preserved, not
silently cleared. A future assessment may preapprove concrete bounded
subtargets after comparing their exact hypotheses.

At the pending October 3 checkpoint, Mathlib coverage was **not checked**.
The supporting lookup below updates that qualification without asserting
coverage of the full obstruction.

## October 4 source review

### Search record

The searches used the following exact strings, grouped by purpose:

- Exact event/result: `"Reed Solomon" "resultant" "mutual correlated agreement"`;
  `"mutual correlated agreement" "sixteen"`;
  `"mutual correlated agreement" "perfect power"`;
  `"mutual correlated agreement" "Hankel"`;
  `"Reed-Solomon" "97" "16" "MCA"`.
- Locator compatibility and stronger obstructions: `"Hankel" "resultant" "perfect power" finite field`;
  `"Hankel pencil" resultant`; `"Reed-Solomon" "locator" "resultant"`;
  `"Hankel" "norm" "perfect powers" polynomial`;
  `"Hankel" "quartic" "perfect power"`;
  `site.arxiv.org "Hankel" "correlated agreement"`;
  `"MCA" "resultant" polynomial Hankel`;
  `"Shortening Bounds for Reed–Solomon MCA" resultant`.
- Standard terminology/implementation: `"resultant" "product" "roots" monic polynomial theorem`;
  `"subresultant" "degree of the gcd" "field" theorem`;
  `"resultant" "monic" "any commutative ring" product evaluations`;
  `site.leanprover-community.github.io/mathlib4_docs "resultant_eq_prod"`.

The exact-target searches did not supply a readable matching theorem.
The broader searches supplied the primary algebra sources below, some
unrelated Hankel/Waring material, and the already known author MCA repository.
Search snippets, third-party summaries and repository descriptions were
not used as mathematical inputs. This is bounded coverage, not evidence
that the full feasibility question is original.

### Inspected theorem statements and applicability

**Resultant product.** J. S. Milne,
[*Fields and Galois Theory*, v5.10, September 2022](https://www.jmilne.org/math/CourseNotes/FT.pdf#page=58),
Appendix to Chapter 4, definition preceding Proposition 4.35 and
Proposition 4.35(b), printed p. 58, gives the leading-coefficient times
product-of-evaluations formula over a field. It permits a nonmonic second
polynomial. Proposition 2.17 (p. 31) preserves gcd under field extension;
the finite-field discussion (p. 53) identifies the elements of a field of
order q as the roots of X^q-X. These support evaluation and exact-field
root checks, not a constrained-pencil existence theorem.

Michael Artin's
[July 17, 2021 MIT notes](https://math.mit.edu/classes/18.721/ag-jul17-2021.pdf#page=25),
Proposition 1.7.10 (printed p. 24), also give the monic split product
formula. Proposition 1.7.20 (p. 25) explains extension of the displayed
polynomial identities to arbitrary coefficient rings. The geometric
development uses complex varieties; no characteristic-zero geometric
obstruction is imported. The ring-general Mathlib declarations below
remove the need for a new proof of the product identity over F[T].

**Perfect-power tests.** Ilya Volkovich,
[*On Some Computations on Sparse Polynomials*, APPROX/RANDOM 2017, Article 48](https://drops.dagstuhl.de/storage/00lipics/lipics-vol081-approx-random2017/LIPIcs.APPROX-RANDOM.2017.48/LIPIcs.APPROX-RANDOM.2017.48.pdf#page=8),
Definition 22 and Lemmas 23–24 (p. 48:8), give monic squarefree
decomposition and recognition of an e-th power by factor multiplicities;
Corollary 25 (p. 48:9) concerns root computation. Lemma 24's Appendix D
proof (p. 48:21) was read. Normalize the target's scalar separately:
c is unrestricted and need not itself be a fourth power.

[Lemma 48 and Theorem 49, with proof](https://drops.dagstuhl.de/storage/00lipics/lipics-vol081-approx-random2017/LIPIcs.APPROX-RANDOM.2017.48/LIPIcs.APPROX-RANDOM.2017.48.pdf#page=20)
(p. 48:20) test f^d=h^e using leading monomials and d*h*f'=e*f*h',
provided char(F)=0 or char(F)>delta*min(e,d) for degrees at most delta.
The proposed degrees 64 and sixteen with exponents one and four fit
the characteristic bound at 97. This tests supplied polynomials, not
pencil feasibility. Section 2.4 was read but its subresultants are unused.
The degree comparison is in T after the moment coefficients are fixed;
a symbolic use that treats those coefficients as additional variables
must recheck the theorem's total-degree hypothesis.

**Ring and specialization coverage.** Read the declarations and relevant
proofs in
[Mathlib's Resultant.Basic](https://github.com/leanprover-community/mathlib4/blob/300d0e535721bc098547106fc297d8ba2a63f6bb/Mathlib/RingTheory/Polynomial/Resultant/Basic.lean),
commit `300d0e535721bc098547106fc297d8ba2a63f6bb`:
`Polynomial.resultant_X_sub_C_left`, `Polynomial.resultant_mul_left`,
`Polynomial.resultant_prod_left`, `Polynomial.resultant_eq_prod_eval`
and `Polynomial.resultant_map_map`. The product/linear-factor statements
allow commutative coefficient rings and explicit degree bounds; the
product statement requires nonzero product of leading coefficients.
The root-evaluation statement uses a splitting hypothesis in a domain.
These support the nonmonic locator and coefficient specialization.
Preserve degree bounds when specializing: a leading coefficient can
vanish at a parameter. No Lean build or axiom audit was performed.

### Reuse, difference and bounded continuation test

Reuse the earlier
[puncturing assessment](2026-10-03-persistent-root-puncturing.md) for its
coding-source comparisons and the
[singular assessment](2026-10-03-identically-singular-distance-transfer.md)
for rank conventions. Their theorems do not decide the current
nonpersistent equality case; no new fifteen-count specialization is
claimed. L010 already contains the equality and same-support checks.
L011 and L012 control the other classes. The achieved interval remains
10/q–16/q; the required upper count is fifteen.

SPECIALIZE approves one bounded mathematical feasibility test on the
unchanged TARGET. Start from the actual affine moments and determinant,
import the standard product and power tests, and check what additional
constraint, if any, their application supplies beyond L010. A witness
must also pass L010's coordinate-degree, simple-root, four-incidence
and D-nonvanishing conditions over the specified field. The generic
resultant test measures multiplicity of the product; the source
statement does not itself establish these separate coordinate conditions.
Splitting over an unspecified extension is not the required splitting
over F_(97^20).

Continue this mechanism if the first test gives a complete equality
witness, an obstruction valid for arbitrary extension-field coefficients,
or a concrete restriction eliminating a nondegenerate class. If it only
repackages the existing incidence criterion and supplies no restriction
or tractable candidate system, record that limitation and change
mechanism. A failed sample or a prime-subfield search does not exclude
all extension-field inputs. No test, coefficient derivation, new bound
or candidate was produced in this literature turn.

The full-subgroup obstruction in ATTEMPTS/004 does not apply to arbitrary
moment pencils. The parked four-block/July source stop in ATTEMPTS/005
is preserved and was not retried. July correspondence is not an essential
input to this independently pinned-model test. Volkovich's cited textbook
reference for the decomposition algorithm was not separately read; its
Lemma 24 statement and proof and Theorem 49 statement and proof were.
No essential unread source is needed for the approved tests.

Outcome: **EXPLORATION**; STEP_KIND: **LITERATURE**;
STEP_CLASSIFICATION: **NOVELTY_UNCHECKED**. This adds source coverage
and a ready application test, without mathematical progress beyond the
checked sources. It spends and resets no mathematical exploration turn.

### Mathlib

Supporting resultant product/evaluation and coefficient-specialization
coverage: **present**, in the pinned declarations above. Direct declaration
links include
[Polynomial.resultant_prod_left](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Resultant/Basic.html#Polynomial.resultant_prod_left),
[Polynomial.resultant_X_sub_C_left](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Resultant/Basic.html#Polynomial.resultant_X_sub_C_left)
and
[Polynomial.resultant_map_map](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Resultant/Basic.html#Polynomial.resultant_map_map).
Full constrained sixteen-count feasibility theorem: **absent from the
Resultant.Basic source checked**; coverage elsewhere in Mathlib is
**not checked**. The power-recognition algorithm's library coverage is
**not checked**. Supporting statements are not a full target match.
