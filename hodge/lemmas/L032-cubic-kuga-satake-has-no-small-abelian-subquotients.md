# L032 — No small abelian subquotients of the cubic Kuga--Satake variety

## Hypotheses

Let S be a projective K3 surface at a very general point of the
four-dimensional cubic real-multiplication locus under consideration.
Let T=T(S), with its rational cup-product polarization q, and assume

\[
\dim_{\mathbb Q}T=18,\qquad
\operatorname{End}_{\rm Hdg}(T)=E=
\mathbb Q(\zeta_7+\zeta_7^{-1}),\qquad \dim_E T=6.
\]

Here E is the full Hodge endomorphism field. Let A be the full
Kuga--Satake variety with the weight-one Hodge structure

\[
V=H^1(A,\mathbb Q)=C^+(T,q).
\]

A nonzero abelian subquotient means a positive-dimensional quotient
of an abelian subvariety, considered up to isogeny. These hypotheses
are the saved very-general data; no assertion is made for special
points with a different Hodge endomorphism algebra.

## Conclusion

Every nonzero abelian subquotient B of A satisfies

\[
\dim_{\mathbb Q}H^1(B,\mathbb Q)\ge64,
\qquad \dim B\ge32>6.                                  \tag{1}
\]

The same lower bound holds for every positive power A^r and for
varieties isogenous to those powers. In particular, for any complex
abelian variety C with dim C at most six and any r>=1,

\[
\operatorname{Hom}(C,A^r)=0=
\operatorname{Hom}(A^r,C).                               \tag{2}
\]

This excludes the selected transfer of low-dimensional Weil cycles
through abelian homomorphisms. It supplies a sufficient lower bound,
without asserting that a dimension-32 factor exists or classifying
the rational simple factors. Higher-dimensional sources and general
algebraic correspondences remain outside the exclusion. Algebraicity
of beta_U and of the separate Kuga--Satake correspondence kappa is
unresolved.

## Proof

**Known inputs and scope of the specialization.** Schlickewei,
*The Hodge conjecture for self-products of certain K3 surfaces*,
[Theorem 3.3.1(i)--(ii), arXiv:0907.2503v1, p. 9](https://arxiv.org/pdf/0907.2503v1#page=9),
identifies the Hodge group of V with the image of
Res_(E/Q) Spin(Phi), where Phi is the E-valued polarization, and
gives V isomorphic to 2^([E:Q]-1) copies of
W=Cores_(E/Q) C^+(T,Phi). Its
[section 3.5, pp. 16--17](https://arxiv.org/pdf/0907.2503v1#page=16)
identifies the action after scalar extension as factorwise left
Clifford multiplication. The irreducible K3-type hypothesis holds
for the transcendental Hodge structure T, and the full totally real
endomorphism field is assumed explicitly.

Van Geemen, *Real multiplication on K3 surfaces and Kuga Satake
varieties*, [section 5.4 and Lemma 5.5, arXiv:math/0609839v1,
PDF pp. 16--17](https://arxiv.org/pdf/math/0609839v1#page=16),
gives the half-spin dimensions and the restriction of the full
spin module to the product of even-dimensional orthogonal factors.
These general representation statements are imported. The argument
below applies them to the dimension threshold in (1), retaining the
whole Clifford representation. This is REPRODUCTION, with no claim
to a result beyond the checked representation theory.

**All complex constituents and their multiplicities.** The three
embeddings of the self-adjoint field E give an orthogonal splitting

\[
(T,q)_{\mathbb C}=(T_1,q_1)\perp(T_2,q_2)\perp(T_3,q_3),
\qquad \dim_{\mathbb C}T_i=6.
\]

Each q_i is nondegenerate. Pull the Hodge-group action back along
the surjection from

\[
G=\operatorname{Spin}(T_1,q_1)\times
  \operatorname{Spin}(T_2,q_2)\times
  \operatorname{Spin}(T_3,q_3).
\]

The finite kernel does not change invariant subspaces or dimensions.
The corestriction formula gives, equivariantly for this action,

\[
W_{\mathbb C}=C_1^+\otimes C_2^+\otimes C_3^+,
\qquad V_{\mathbb C}\simeq W_{\mathbb C}^{\oplus4},
\qquad C_i^+=C^+(T_i,q_i).                               \tag{3}
\]

For a six-dimensional complex quadratic space the split even
Clifford algebra is

\[
C_i^+\simeq\operatorname{End}(S_i^+)\oplus
             \operatorname{End}(S_i^-),
\qquad \dim S_i^+=\dim S_i^-=2^{3-1}=4,                 \tag{4}
\]

where S_i^+ and S_i^- are its half-spin modules. In the usual
split Clifford model these are the even and odd parts of the
exterior algebra of a three-dimensional maximal isotropic space.
Their dimensions are 1+3 and 3+1, respectively; the even algebra
acts as the full matrix algebra on each parity. Under left
multiplication, each matrix algebra has four column modules.
Consequently (4) reads as a spin representation

\[
C_i^+\simeq (S_i^+)^{\oplus4}\oplus(S_i^-)^{\oplus4}.
                                                               \tag{5}
\]

The column index is a trivial multiplicity space for this action.
Thus no conjugation action on End(S_i^+) or End(S_i^-) is used.

For each sign triple epsilon define the external tensor product

\[
R_\epsilon=S_1^{\epsilon_1}\boxtimes
             S_2^{\epsilon_2}\boxtimes S_3^{\epsilon_3}.
\]

It is irreducible of dimension 4^3=64. To see irreducibility
directly in the Clifford model, choose orthonormal Clifford
generators in each T_i. Their even basis monomials belong to
Spin(T_i,q_i) and span C_i^+. The linear span of the product-group
action on R_epsilon therefore contains
Mat_4(C) tensor Mat_4(C) tensor Mat_4(C)=Mat_64(C). A nonzero
invariant subspace is consequently the whole R_epsilon.

Expanding (3) and (5) now gives the full decomposition

\[
V_{\mathbb C}\simeq
 \bigoplus_{\epsilon\in\{+,-\}^3}
              R_\epsilon^{\oplus256},
\qquad 256=4\cdot4^3.                                   \tag{6}
\]

In particular all eight sign types occur. The dimension check

\[
8\cdot64\cdot256=131072=2^{17}=\dim_{\mathbb Q}C^+(T,q)
                                                               \tag{7}
\]

confirms that no part of H^1 has been omitted. Equivalently, the
branching formula in the cited Lemma 5.5 decomposes the full
512-dimensional spin module S(18) into these eight types; the
regular even Clifford representation contains 256 copies of it.

**Rational subquotients.** A rational Hodge subspace of V is
preserved by its Hodge group: its rational algebraic stabilizer
contains the Hodge circle and hence contains the smallest rational
algebraic group containing that circle. Quotients inherit the
action. Thus a nonzero rational Hodge subquotient M, after extension
to C, is a nonzero G-subquotient of (6).

Finite-dimensional representations of the complex semisimple group
G are completely reducible. Every irreducible constituent of M_C
is therefore one of the 64-dimensional R_epsilon, and

\[
\dim_{\mathbb Q}M=\dim_{\mathbb C}M_{\mathbb C}\ge64.       \tag{8}
\]

This starts with an actual rational subquotient. No individual
R_epsilon is asserted to descend to Q or to be a Hodge structure.
Galois descent and division-algebra multiplicities can require
larger rational factors; they cannot create a smaller complex
constituent inside (6).

**Abelian subquotients and contravariance.** Poincare complete
reducibility is used in the form of Milne, *Abelian Varieties*,
v2.00 (March 2008),
[Chapter I, Proposition 10.1, printed pp. 42--43,
PDF pp. 48--49](https://www.jmilne.org/math/CourseNotes/AV.pdf#page=48).
If P is an abelian subvariety of A and B a quotient of P, this
theorem makes B an isogeny factor of P and then of A. Pullback
along an isogeny is an isomorphism of rational Hodge structures,
so H^1(B,Q) is a direct summand of H^1(A,Q).

More explicitly, the inclusion P -> A induces a surjection
H^1(A,Q) -> H^1(P,Q), while the quotient P -> B induces an
injection H^1(B,Q) -> H^1(P,Q). Complete reducibility splits the
first map rationally. This verifies the direction of both
cohomology maps rather than treating every abelian map as an
injection on H^1. Applying (8) and using dim_Q H^1(B,Q)=2 dim B
proves (1).

For A^r, H^1(A^r,Q)=V^(direct sum r), so the same constituents
occur and the same proof applies. Isogenies preserve this rational
Hodge structure. A nonzero homomorphism C -> A^r has a positive-
dimensional abelian image of dimension at most dim C; a nonzero
homomorphism A^r -> C has such an image as a quotient of A^r.
Both contradict (1) when dim C<=6. A zero-dimensional image of a
connected abelian variety is the identity point, so these are
indeed the zero homomorphisms, proving (2).

The required H^1 threshold was at most twelve. The achieved lower
bound is 64, so the selected small-factor prerequisite fails.
The conclusion also prevents transfers through homomorphisms from
products of the reviewed small varieties, since each homomorphism
restricts to zero on every factor. It does not address arbitrary
correspondences or the higher-dimensional generalized Prym supply.
No new class, surface or transverse RM direction is produced; the
attained span 21 on the Dickson family, three directions against
four required, and the universal Hodge gap remain unchanged.

## Mathlib

Coverage of the full statement: **not checked**. No library theorem
name or absence is asserted. Schlickewei's Theorem 3.3.1 and van
Geemen's Lemma 5.5 supply the general representation inputs; Milne's
Proposition 10.1 supplies complete reducibility. These supporting
results are distinguished from the threshold specialization (1),
which is proved here without a rational simple-factor classification.
