# Genus-three abelian-cover Prym determinant transfer through homomorphisms

Tested 2026-09-27. Outcome: NEGATIVE. Stop this channel for the
very-general rank-eighteen cubic-RM Kuga--Satake variety.

## Proposed use

Use homomorphisms between powers of A and genus-three etale
abelian-cover Prym factors to transfer determinant classes already
in degree four toward beta_U. Unlike the earlier small-factor
recipe, the covering group and source dimension are unrestricted.
Algebraic kappa and a certificate for the whole tensor image
would still be required.

## WHY IT FAILS

[L033](../lemmas/L033-genus-three-prym-homomorphisms-vanish.md)
shows that every such homomorphism in either direction is zero,
including powers, isogenies and finite products of these factors.
Under the joint Hodge group, cover-character projectors preserve
four-dimensional source spaces, whereas all eight target spin
types remain irreducible of dimension 64. Invariant component maps
cannot connect them. Rational descent and cohomological
contravariance are retained; no cover-equivariance or generality
of the source is assumed. This is a reproduction of the reviewed
tools with a new scoped notebook consequence, not an originality
claim. It leaves higher-genus degree-changing transfers and
arbitrary algebraic correspondences unresolved and does not imply
nonalgebraicity of beta_U.
