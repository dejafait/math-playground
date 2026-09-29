# Low-dimensional Weil cycles transferred by abelian homomorphisms

Tested 2026-09-27. Outcome: NEGATIVE. Stop this recipe for the stated
very-general rank-eighteen cubic RM Kuga--Satake variety.

## Proposed use

Find an abelian subquotient of dimension at most six to connect the
reviewed low-dimensional Weil-cycle supplies to A^4 by abelian
homomorphisms. This is a prerequisite for supplying beta_U; algebraic
kappa would remain a separate input.

## WHY IT FAILS

[L032](../lemmas/L032-cubic-kuga-satake-has-no-small-abelian-subquotients.md)
applies the known RM spin and complete-reducibility theorems to all
of H^1(A,Q). Every complex irreducible constituent has dimension 64,
so every nonzero rational Hodge subquotient has dimension at least
64 and every nonzero abelian subquotient has dimension at least
32, exceeding six. The same argument holds for every power of A;
homomorphisms in either direction with an abelian variety of
dimension at most six are zero. All spin types and their
multiplicities are retained, without assuming individual complex
blocks descend to rational factors. This is a reproduction of the
reviewed representation theory, not a novelty claim. It leaves
higher-dimensional Pryms and general algebraic correspondences
untested and does not imply that beta_U is nonalgebraic.
