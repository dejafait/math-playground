# Generalized Prym transfer for the cubic tensor — literature assessment

TARGET: Review whether Patel-Zhang's generalized Prym determinant cycles admit an algebraic transfer whose image contains beta_U for the rank-eighteen cubic-RM Kuga-Satake variety, allowing higher-dimensional sources and retaining the L032 factor bound.
CHECKED: 2026-09-27
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched the exact Patel-Zhang/Kuga-Satake transfer, cubic-RM Prym realizations, determinant transfers and stronger Weil-class generation results; queries and primary statements actually read are recorded below.
SOURCE_EVIDENCE: Patel-Zhang, arXiv:2506.13729v2 (23 May 2026), Theorems 1.1--1.2, Lemma 2.9, Corollary 2.10, Remark 2.11 and Theorem 4.3, https://arxiv.org/pdf/2506.13729v2#page=3; Milne, Lefschetz classes on abelian varieties, Proposition 5.7 and Theorems 5.9--5.10, https://www.jmilne.org/math/articles/1999aP.pdf#page=26; additional scoped comparisons below.
COMPARISON: The inspected construction ends in the specified Prym determinant space, with no identified map to this A or image containing beta_U. Known algebraic Lefschetz operators supply allowable operations, not the required image; the broader Weil-generation theorem inspected assumes CM type.
GAP: Identify a qualifying cover and rational representation factor, an algebraic transfer of the correct degree, and a certificate that its image contains the whole beta_U. L032's bound remains in force; it does not settle higher-dimensional sources or arbitrary correspondences.
REASON: Complete the review without importing algebraicity of beta_U or claiming an exclusion. Isolate the genus-three homomorphism prerequisite as a bounded first test; its separate assessment remains REVIEW_REQUIRED before any calculation.

## Hypotheses

Keep the full very-general data of L031 and L032: dim_Q T=18,
End_Hdg(T)=E=Q(zeta_7+zeta_7^(-1)), dim_E T=6, and
H^1(A,Q)=C^+(T,q). The target beta_U lies in the multidegree
(1,1,1,1) part of H^4(A^4,Q). A^4 is a fourth power, not an
abelian fourfold. The separate Kuga--Satake correspondence kappa
is still an unproved algebraicity input.

Reuse the [exceptional-cycle review](2026-09-27-cubic-rm-exceptional-weil-cycles.md)
for Schoen, its correction, and the later fourfold/sixfold and
conditional secant results; their scope has not changed. Reuse the
[small-factor assessment](2026-09-27-cubic-rm-kuga-satake-small-factors.md)
and L032 for the representation theory. In particular, each
nonzero abelian subquotient of a power of A has dimension at least
32; no dimension-32 factor is asserted to exist. No discarded
support, bundle or divisor recipe is reopened.

The [primary target audit](../../foundations/01-target-and-scope.md)
is reused: the goal concerns rational cycles on smooth projective
complex varieties. No change of conjecture or coefficient field
is part of this review.

## Conclusion

The saved review is complete. None of the inspected statements
identifies a qualifying Prym source and an algebraic transfer
containing beta_U under these hypotheses. This is noncoverage in
the checked literature, not a theorem that such a transfer cannot
exist and not an originality claim.

The result is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION.
Named source results are retained by citation. No result is
reproved, no representation test is executed, and no new lemma
or cycle is asserted. EXPLORE records the unresolved applicability
problem; it does not itself solve that problem.

## Proof

This section records source statements and their comparison with
the saved target, rather than a new mathematical derivation.

### The Prym theorem and the destination of its transfer

Read Patel--Zhang, *Algebraicity of Hodge classes on some generalized
Prym Varieties*, [arXiv:2506.13729v2](https://arxiv.org/abs/2506.13729v2),
submitted 23 May 2026 (PDF dated 22 May), 14 pages:
[Theorems 1.1--1.2, pp. 2--3](https://arxiv.org/pdf/2506.13729v2#page=2),
[section 2.2 and Theorem 2.4, pp. 4--5](https://arxiv.org/pdf/2506.13729v2#page=4),
[Lemma 2.9, Corollary 2.10, Remark 2.11 and (2.11.2), pp. 6--7](https://arxiv.org/pdf/2506.13729v2#page=6),
and [section 4, especially Theorem 4.3 and Lemma 4.4,
pp. 10--13](https://arxiv.org/pdf/2506.13729v2#page=10).

For an etale abelian cover C -> C_0, with base genus g>=2,
put h=2g-2 and R=Q[G]_nt. The cited result makes
W_P=exterior_R^h H^1(P,Q), contained in H^h(P,Q), algebraic.
Rational representation factors are included. Each nontrivial
character has multiplicity h. Section 4 uses the covering
symmetric product, Abel--Jacobi, the Jacobian's Prym projection
and inverse Lefschetz to obtain W_P. These maps concern that
cover and its Jacobian/Prym; they do not specify a map to our A.

Thus a field action, a large enough dimension, or the description
of beta_U as exceptional does not supply the missing applicability
data. No assertion that every Prym Hodge class is a determinant
class is imported. The paper's auxiliary variety called A must
not be identified with our Kuga--Satake variety by notation alone.

### Available algebraic operators do not certify their image

Read Milne, *Lefschetz classes on abelian varieties* (1999),
[Proposition 5.7, Corollary 5.8 and Theorems 5.9--5.10,
author PDF pp. 26--27](https://www.jmilne.org/math/articles/1999aP.pdf#page=26).
These give the Lefschetz nature of the relevant correspondence
operators, Kunneth projectors, Lefschetz lowering operators and
graphs of maps between abelian varieties. This supplies known
algebraic operations for a proposed transfer, including operations
changing degree. It is not an image theorem for W_P and beta_U.

In particular, L031 cannot exclude a transfer merely because the
operator is Lefschetz: its input here would be an exceptional
class. Conversely, knowing that an operator is algebraic does
not establish that its value on that input is nonzero or is the
required tensor. No contraction or image is computed in this review.

### Stronger-looking generation and Kuga--Satake comparisons

Read Milne, *Hodge classes on abelian varieties*,
[v1.1, 12 July 2022, Theorem 1, p. 3](https://www.jmilne.org/math/articles/HAV.pdf#page=3),
and [section 5, Theorems 3--4 and Proposition 1,
pp. 4--6](https://www.jmilne.org/math/articles/HAV.pdf#page=4).
Theorem 1 expresses Hodge classes as pullbacks of split Weil
classes when the target abelian variety is of CM type. That
hypothesis is not supplied by the saved very-general cubic-RM
data. The broader accessibility result allows deformation;
replacing accessibility by algebraicity requires an additional
variational input. Theorem 4 assumes the Lefschetz standard
conjecture for algebraic varieties over C, not just for individual
abelian fibres. None provides the missing transfer here.

Also inspected van Geemen--Verra, *Quaternionic Pryms and Hodge
classes*, [arXiv:math/0103111v1, 17 March 2001,
Proposition 6.2, p. 14](https://arxiv.org/pdf/math/0103111v1#page=14),
and [Theorem 6.9, pp. 16--17](https://arxiv.org/pdf/math/0103111v1#page=16).
Its Kuga--Satake examples use different weight-two ranks and
eight-dimensional abelian varieties; Theorem 6.9 assumes a
specified isogeny to a square of a Weil variety and algebraicity
of the source degree-four classes. No such identification for
our full A is stated. This is a scope comparison, not a new
factor calculation or a replacement for L032.

### Applicability obligations and bounded continuation

The unsupplied data for the exact target are:

1. An actual etale abelian curve cover and a rational representation
   factor P meeting the cited theorem, together with its relationship
   to the saved A. Complex eigenspaces alone are not rational factors.
2. Algebraic operations from its known cycles to H^4(A^4,Q), with
   any change in degree and every Kunneth projection specified.
3. Membership of the whole rational beta_U in the resulting image.
   Reaching L031's nonzero detected component is necessary but would
   not by itself establish this membership.

Three possible channels remain distinguishable: pullback of
degree-four determinant classes along homomorphisms; higher-degree
determinants with algebraic degree-changing operators; and other
explicit algebraic correspondences. The review has not supplied
the data above for any of them. An arbitrary Hodge correspondence
cannot fill item 2 without an algebraicity argument.

The first bounded prerequisite is the genus-three homomorphism
channel, corresponding to the determinant degree of the target.
The finite abelian covering group is unrestricted, so this test
must allow source dimensions beyond L032's cutoff. It is not the
old search for an abelian variety of dimension at most six.
The proposed comparison concerns the source character modules and
the full rational Hodge representation in L032, with homomorphisms
in either direction. Its answer is not inferred here from comparing
individual complex blocks; rational descent and any joint Hodge
group argument still need justification.

Continue this channel if a nonzero rational homomorphism survives
the representation test, then require geometric realization and
the actual tensor image. Stop just this channel if all such maps
vanish. Neither outcome would settle transfers from higher genus
using degree-changing correspondences. The
[separate prerequisite assessment](2026-09-27-genus-three-prym-homomorphisms.md)
is pending; this review does not perform its calculation.

Supplying beta_U would discharge one input of the conditional
Kuga--Satake transfer. Algebraic kappa, transport beyond the
Dickson locus, and the universal Hodge target remain separate.
The achieved span is still 21 on the known family and only three
directions are attained against four required. No complete candidate
exists. This is the first consecutive exploration turn after L032's
informative negative result; the follow-up shares that window.

### Search and access record

Queries on 2026-09-27 included:

- "Patel" "Zhang" "Prym" "Kuga"
- "Algebraicity of Hodge classes on some generalized Prym varieties"
- "generalized Prym" "Kuga-Satake"
- "Prym" "cubic real multiplication" Kuga Satake
- "Weil classes" "Kuga-Satake" "real multiplication"
- Prym determinant classes homomorphism abelian variety Hodge classes Lefschetz algebra
- "Kuga-Satake" "determinant" "Weil classes"

The exact-transfer searches supplied no inspected theorem matching
the saved target. The Patel--Zhang version record was checked, and
the primary PDF passages above were read, including the actual
destination of the section 4 transfer. The related Milne and
van Geemen--Verra results were read at theorem level. Search
snippets, abstracts and claimed general resolutions were not used
as proof of coverage. Failure to find a match is not evidence of
novelty or impossibility.

Schoen and the later Weil/secant results were reused from the
completed assessment, not searched again mechanically. The original
Kleiman 1968, Lange--Rodriguez 2022 and Macdonald 1962 references
inside Patel--Zhang were not independently read in this turn;
the present scope comparison uses the displayed primary statements
and Milne's explicit operator theorem. No essential inaccessible
statement prevents this assessment; the missing transfer is a
mathematical applicability problem, not a source-access claim.

## Mathlib

Coverage: **not checked**. The named Prym, Lefschetz and generation
theorems above are supporting or conditional statements, not a
match for the whole transfer target. No Mathlib theorem name,
absence claim or result beyond the checked literature is asserted.
