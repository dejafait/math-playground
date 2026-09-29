# Higher-genus Prym determinant transfer by Lefschetz correspondences — assessment

TARGET: Test whether divisor-generated correspondences from higher-genus etale abelian-cover Prym factors can send their determinant classes to beta_U in H^4(A^4,Q), allowing Lefschetz degree-lowering.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched higher-genus Prym determinant transfers, Weil classes under Lefschetz correspondences, primitive lowering and determinant representations; inspected the primary passages and author correction recorded below. No inspected theorem decides this exact image.
SOURCE_EVIDENCE: Patel-Zhang, arXiv:2506.13729v2, Theorem 1.2 and section 2.6, https://arxiv.org/pdf/2506.13729v2#page=3; Milne, Proposition 5.7 and Theorem 5.9, https://www.jmilne.org/math/articles/1999aP.pdf#page=26, with author erratum https://www.jmilne.org/math/articles/1999a.html; Moonen-Zarhin, arXiv:alg-geom/9612017v1, sections 3, 7 and Criterion 13, https://arxiv.org/pdf/alg-geom/9612017v1#page=2.
COMPARISON: Known results give an equivariance criterion for the allowed operators and a determinant-space framework, including decomposable special cases; their application to the full target representation and degree-four image remains unwritten. Neither algebraic lowering alone nor source exceptionality certifies the required image.
GAP: Compare the source determinant subspace and H^4(A^4,Q) under one joint Lefschetz group, retaining rational descent, extra endomorphisms, mixed divisors and all L032 constituents; decide whether the image can contain the whole beta_U.
REASON: Import the general theorems and reserve this specific representation comparison for a separate research invocation. It is a bounded specialization of known tools, expected to be REPRODUCTION, with no transfer or exclusion asserted by this review.

## Hypotheses

Keep the very-general A, T, E and beta_U of L031--L033 and the
separate unresolved algebraicity of kappa. Thus dim_Q T=18,
End_Hdg(T)=E=Q(zeta_7+zeta_7^(-1)), dim_E T=6, and
H^1(A,Q)=C^+(T,q). The tensor beta_U occupies multidegree
(1,1,1,1) in H^4(A^4,Q); A^4 denotes a fourth power, not an
abelian fourfold.

Let P be a nontrivial irreducible rational representation factor
of a connected etale abelian cover C -> C_0, with g(C_0)>=4.
The group order and dimension of P are unrestricted. The source
is an actual cover factor, possibly special and with additional
endomorphisms. Its determinant subspace lies in H^(2g-2)(P,Q).
The proposed operators belong to the rational divisor algebra
of P x A^4, with the degree and Tate twist appropriate to an
image in H^4(A^4,Q). Retain Lefschetz degree-lowering and all
mixed divisors; cover-equivariance of a transfer is not assumed.

Reuse the [broader assessment](2026-09-27-cubic-rm-generalized-prym-transfer.md),
the [genus-three assessment](2026-09-27-genus-three-prym-homomorphisms.md),
and the [primary target audit](../../foundations/01-target-and-scope.md).
The rational Hodge target and these very-general hypotheses have
not changed.

## Conclusion

The assessment is complete: SPECIALIZE. A joint Lefschetz-group
comparison is supported by inspected theorems, but the exact
image has not been determined. No essential source-access gap
remains for that test. This is LITERATURE / NOVELTY_UNCHECKED /
EXPLORATION; no mathematical result is derived in this turn.

The source statements are retained by citation. The proposed
application needs a proof because neither an operator theorem
nor a classification of source Weil classes states whether this
specific beta_U lies in the image. A later specialization should
be classified as REPRODUCTION, without an originality claim.

## Proof

This section records sources and applicability obligations;
it is not a derivation of an image theorem.

### Determinant input and special sources

Rechecked Patel--Zhang, *Algebraicity of Hodge classes on some
generalized Prym Varieties*, [arXiv:2506.13729v2, 23 May 2026](https://arxiv.org/abs/2506.13729v2),
whose version record still lists v2. Read [Theorem 1.2, p. 3](https://arxiv.org/pdf/2506.13729v2#page=3),
and [Lemma 2.9, Corollary 2.10 and section 2.6, pp. 6--7](https://arxiv.org/pdf/2506.13729v2#page=6).
The determinant space is algebraic and, over C, is the sum of
the top exterior lines of the nontrivial character spaces of
dimension h=2g-2. The rational-factor scope and section 4 transfer
are already covered by the broader assessment. Keep the trivial
Jacobian summand excluded; do not apply Remark 2.11 to it.

Read Moonen--Zarhin, *Weil classes on abelian varieties*,
[arXiv:alg-geom/9612017v1, 19 December 1996](https://arxiv.org/pdf/alg-geom/9612017v1):
[sections 2--7, pp. 2--3](https://arxiv.org/pdf/alg-geom/9612017v1#page=2),
[sections 10--11 and Tables 1--2, pp. 4--5](https://arxiv.org/pdf/alg-geom/9612017v1#page=4),
and [Lemma 12 and Criterion 13 with its proof, pp. 6--8](https://arxiv.org/pdf/alg-geom/9612017v1#page=6).
These describe field determinant spaces, their behavior under
isogeny decomposition, and when their Hodge classes are generated
by divisors. Criterion 13 assumes a power of a simple variety;
section 7 explains the reduction. Section 10's G_div fixes the
divisors of one variety and is defined using the algebra generated
by Rosati-symmetric endomorphisms. It must not be silently equated
with the group fixing divisors on every power. These results do
not compute a transfer between P and the saved A.

Consequently the proposed test must include special Pryms; a
generic-source assumption, assumed primitivity for every
polarization, or the presence of exceptional source classes
would leave part of the saved target untreated. No claim about
their actual primitives or contractions is made here.

### The operator criterion and its correction

Read Milne, *Lefschetz classes on abelian varieties*, Duke Math.
J. 96 (1999), author PDF: [Proposition 1.1, p. 5](https://www.jmilne.org/math/articles/1999aP.pdf#page=5),
[section 2, type IV and summary, pp. 12--14](https://www.jmilne.org/math/articles/1999aP.pdf#page=12),
[Theorem 3.2 and Proposition 3.6, pp. 15--17](https://www.jmilne.org/math/articles/1999aP.pdf#page=15),
[Proposition 4.1 through Corollary 4.7, pp. 20--22](https://www.jmilne.org/math/articles/1999aP.pdf#page=20),
and [Proposition 5.7 through Remark 5.11, pp. 26--28](https://www.jmilne.org/math/articles/1999aP.pdf#page=26).

Proposition 5.7 characterizes Lefschetz correspondences by
equivariance for the joint Lefschetz group. Theorem 3.2 gives
the full divisor-invariant criterion on powers. Corollary 4.7
describes the group through simple isogeny factors; Proposition
4.1 and Corollary 4.2 cover the absence of mixed divisors.
Theorem 5.9 includes lowering operators, with explicit
correspondences in Remark 5.11. These are supporting results,
not a decision about the value of an operator on beta_U's source.

Read the [author's erratum to the proof of Theorem 5.9](https://www.jmilne.org/math/articles/1999a.html).
It corrects the assertion that Lambda inverts L on all cohomology:
the repair uses equivariance of the primitive-decomposition maps.
The operator theorem remains available. Record this qualification
in any later use; algebraic lowering is not a certificate that
an arbitrary high-degree class has a nonzero lower-degree image.
This is a source correction, not a reproof or a claimed repair
of a mathematical error in a notebook lemma.

### Exact difference reserved for research

The concrete specialization is to compare the determinant input
with degree-four cohomology under the **same full Lefschetz
group**. It must address all of the following as one image test:

1. Determine the action on the rational determinant subspace
   through the actual cover field, allowing extra endomorphisms.
   Use complex determinant lines only with a rational descent
   argument. Distinguish the action of a field element on
   cohomology from scalar multiplication on its determinant line.
2. Justify the projection of the joint group for P x A^4 to the
   target group, including common isogeny factors and mixed
   divisors. Do not assume that it is a product of unrelated
   source and target groups.
3. Recover the target polarization centralizer from the complete
   L032 representation and compare its one-dimensional
   representations with the source determinant action. Check
   whether any non-invariant such representation occurs in
   H^4(A^4,Q), retaining all eight spin types and multiplicities.
   L031's scalar rescaling witness alone does not answer this
   representation question.
4. Apply the cited operator criterion with the correct degree,
   Tate twist, Kunneth summand and allowed lowering operations.
   Test the whole rational beta_U, including rational linear
   combinations of allowed transfers, rather than one component.

These are proof obligations, not established conclusions. No
centralizer classification for this target, character exclusion,
genus bound, contraction value or transfer vanishing is asserted.
The supporting theorems need no reproof; this particular
application and its hypotheses do need to be checked.

Continue toward a geometric source only if the image test leaves
a possible image outside the target divisor algebra compatible
with beta_U. Such survival would still require an actual cover
and the full rational image certificate. Stop this channel if
the comparison forces every allowed image into a subspace that
misses beta_U. Both outcomes are useful for the missing algebraic
tensor; neither settles arbitrary algebraic correspondences.

L031 already excludes the target divisor algebra, L032 the
selected small-factor supply, and L033 genus-three homomorphisms.
None is substituted for this higher-genus image test. The
broader review's CM-generation comparison and the earlier
Weil/secant assessments are reused with their stated hypotheses.
They supply no unconditional shortcut for the very-general A.

Algebraic kappa, transverse transport beyond the Dickson locus,
arbitrary primitive fourfold classes and higher dimensions remain
separate gaps. The attained span remains 21 on the known family,
with three RM directions against four required. This assessment
adds no cycle and produces no complete candidate.

### Search and access record

Queries on 2026-09-27 included:

- "Prym" "determinant" "Lefschetz" "Hodge"
- "higher genus" "Prym" "Lefschetz" Hodge
- "Weil classes" "Lefschetz correspondences"
- "Weil classes" "primitive" polarization
- "Weil classes" "Lefschetz group" determinant
- "Weil classes" "decomposable" "Lefschetz"
- "determinant" "Kuga-Satake" "Hodge classes"
- "Weil classes" "characters" "Lefschetz"

The searches led to the exact operator criterion, its author
correction, and the determinant/decomposability comparison above.
No inspected source states the full saved transfer answer.
This is a coverage statement, not evidence of novelty or
impossibility. Search snippets and claims of general resolutions
were not used as theorem evidence.

The primary passages listed above were accessible and read.
Previously completed source comparisons are reused where their
hypotheses are unchanged. Kleiman 1968 and Scholl 1994 were not
independently reread; the operator input here is Milne's explicit
theorem together with his inspected correction and Remark 5.11.
There is no unresolved access dependency for the proposed test.
One exploration turn is used after L033's informative negative
result; this specialization shares that three-turn window.

## Mathlib

Coverage of the full statement: **not checked**. The named and
linked theorems support the proposed specialization; none is
identified as a match for its full conclusion. No Mathlib theorem
name, absence claim or progress beyond checked literature is
asserted.
