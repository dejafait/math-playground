# Higher-genus Prym determinant transfer — working proof notes

Started 2026-09-27 under the saved SPECIALIZE assessment in
drafts/literature/2026-09-27-higher-genus-prym-lefschetz-transfer.md.
The initial outline below was completed in
[L034](../lemmas/L034-prym-determinant-lefschetz-transfers-miss-cubic-tensor.md).
Outcome: NEGATIVE; classification: REPRODUCTION.

The exact gap is algebraicity of beta_U beyond the Dickson family.
The present test asks only whether divisor-generated operators,
including Lefschetz lowering, can transfer the known determinant
classes of higher-genus etale abelian-cover Prym factors to it.
Algebraic kappa and the universal Hodge target remain separate.

L031 excludes the target divisor algebra; L032 supplies all eight
64-dimensional complex spin types with multiplicity 256. L033
only rules out genus-three homomorphisms. Its dimension comparison
does not decide the present higher-genus, degree-changing test.

Initial candidate argument and checks to discharge:

1. The eight types in L032 are pairwise inequivalent, paired by
   duality as epsilon and -epsilon. Hence the Hodge commutant is
   the product of their full multiplicity matrix algebras. Its
   polarization centralizer should be GL(64)^4 over C.
2. The full joint Lefschetz group of P x A^4 projects onto the
   target group even when P has common isogeny factors with A.
   This must use the simple-factor theorem, not assume a product.
3. Each complex top cover-character exterior line is preserved
   by that joint group and therefore carries a character. The
   determinant input is killed by its derived group.
4. Divisor correspondences are equivariant for this joint group,
   and thus their degree-four images are fixed by SL(64)^4.
5. In four tensor factors, SL(64)^4 has the same invariants as
   GL(64)^4: a determinant character needs weight magnitude 64,
   while every factor's weight here has magnitude at most four.
   Prove this in all of H^4(A^4), with all multiplicities, using
   the central 64th roots of unity and the scalar torus.
6. If these checks hold, every allowed image is a divisor class
   product and misses beta_U by L031. Rational descent, correct
   degree/Tate twists, special sources and lowering must be kept.

The stopping test is exact containment of the whole image in the
target divisor algebra. A surviving nondivisor representation
would instead require an actual geometric source and full tensor
image certificate. No novelty was presumed in this outline.

## Completed checks

All six obligations are resolved in the full proof. Opposite
central volume eigenvalues distinguish all eight irreducibles
and pair them by duality; Schur's lemma and the full commutant
give GL(64)^4, including its entire group. Milne's simple-factor
description handles common isogeny factors in the joint group.
Its projection maps the connected derived group onto SL(64)^4.
Each source determinant line is a character, even at special
Pryms, so its image is fixed by this target derived group.

In degree four every scalar exponent lies between -4 and 4.
Derived invariance forces divisibility by 64 via the central
64th roots of unity, hence exponent zero. Full invariance follows,
and Milne's criterion places the image in the divisor algebra.
The proof explicitly descends this containment to Q and handles
finite sums, mixed divisors, compositions and lowering. L031
then excludes the whole rational beta_U.

Reconsulted the already assessed Milne source at Proposition 1.1
and its immediate group consequence Proposition 1.5, Theorem 3.2,
Corollary 4.7, Proposition 5.7 and the author's lowering erratum.
This checks precise applicability of the saved inputs; it is not
a new target assessment. The Prym theorem and the earlier spin
assessment were reused. No source-access gap was found.

An exact integer bookkeeping check enumerated 8^4=4096 ordered
choices of standard/dual block, with 225 distinct central weights.
Exactly 168 words have weights divisible by 64 in every factor;
all have zero weight. Multiplicities introduce no new weights.
This is only a sanity check of the elementary inequality, not
evidence replacing the representation or rational descent proofs.
No persistent mathematical script was needed or changed.

The image is zero in H^4(A^4,Q)/D^2(A^4), whereas beta_U has a
nonzero image there. Stop this exact determinant-transfer channel.
No cycle, transverse RM direction or complete candidate results;
algebraic kappa and the universal target remain unresolved.
