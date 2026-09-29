# Higher-genus Prym determinants with Lefschetz degree-lowering

Tested 2026-09-27. Outcome: NEGATIVE. Stop this channel for the
very-general rank-eighteen cubic-RM Kuga--Satake variety.

## Proposed use

Transfer the known algebraic determinant classes of higher-genus
etale abelian-cover Prym factors to beta_U in H^4(A^4,Q), using
divisor-generated correspondences and algebraic Lefschetz lowering.
The source may be special, have arbitrary dimension and share
isogeny factors with A. Algebraic kappa remains a separate input.

## WHY IT FAILS

[L034](../lemmas/L034-prym-determinant-lefschetz-transfers-miss-cubic-tensor.md)
places every such image in the full target divisor algebra, which
misses beta_U by L031. The source determinant space is a sum of
characters of the joint Lefschetz group. Its connected derived
group surjects onto the target SL(64)^4, so every image is fixed
by that group. The whole target polarization centralizer is
GL(64)^4, and degree four is too small for a nontrivial determinant
character: each scalar weight has magnitude at most four and must
be divisible by 64. Thus derived invariance is full invariance.
This treats mixed divisors, all target multiplicities, special
sources, lowering, rational descent and sums of transfers. It is
a reproduction of known tools, not an originality claim or an
obstruction to arbitrary algebraic correspondences. Source classes
with nontrivial derived-group action remain outside this test.
