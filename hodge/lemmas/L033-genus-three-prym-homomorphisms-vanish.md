# L033 — Genus-three abelian-cover Pryms have no maps to the cubic Kuga--Satake variety

## Hypotheses

Retain the very-general cubic-RM hypotheses of L032. Thus S is a
projective K3 surface, T=T(S) has rational dimension eighteen,

\[
\operatorname{End}_{\rm Hdg}(T)=E=
\mathbb Q(\zeta_7+\zeta_7^{-1}),\qquad \dim_E T=6,
\qquad V=H^1(A,\mathbb Q)=C^+(T,q),
\]

and A is the full Kuga--Satake variety. The field E is the full
Hodge endomorphism algebra, as in L032; specializations with a
larger algebra are not included.

Let C -> C_0 be a connected finite etale Galois cover of smooth
projective complex curves with finite abelian group Gamma and
g(C_0)=3. Let e be the central idempotent of Q[Gamma] belonging to
a nontrivial irreducible rational representation. Define P to be
the abelian isogeny factor e J(C), concretely the image of N e
on J(C) for a positive integer N clearing denominators. There is
no generality assumption on the cover or upper bound on dim P or
the order of Gamma. Put W=H^1(P,Q).

## Conclusion

For every positive integer r,

\[
\operatorname{Hom}(P,A^r)=0=
\operatorname{Hom}(A^r,P).                              \tag{1}
\]

In fact both spaces of rational Hodge morphisms between W and
V^(direct sum r) are zero. The assertion is invariant under
isogenies of P and A^r. It also holds with P replaced by a finite
product of such factors, including repetitions.

Thus genus-three determinant classes cannot be transferred to A^4
by homomorphisms between these factors and powers of A.
This excludes that prerequisite even when their total dimension
exceeds the bound in L032. It does not exclude arbitrary algebraic
correspondences, higher-genus sources with degree-changing
operations, or special K3 points outside the hypotheses. Neither
algebraicity of beta_U nor of the separate Kuga--Satake
correspondence kappa follows.

## Proof

**Imported inputs and the difference being checked.** The prior
[assessment](../drafts/literature/2026-09-27-genus-three-prym-homomorphisms.md)
is SPECIALIZE for this exact question. The argument applies its
known character and Hodge-group statements to L032's full
representation. This is REPRODUCTION, not a claim beyond the
checked literature. L032's total-dimension bound alone cannot
decide (1), since dim P is unrestricted.

Patel--Zhang, *Algebraicity of Hodge classes on some generalized
Prym Varieties*, [arXiv:2506.13729v2, Theorem 2.4 and Example 2.5,
PDF p. 5](https://arxiv.org/pdf/2506.13729v2#page=5), give the
rational idempotent factors and their cohomology representations.
Their [Lemma 2.9 and Corollary 2.10, PDF pp. 6--7](https://arxiv.org/pdf/2506.13729v2#page=6)
give multiplicity 2g(C_0)-2 for each nontrivial complex character.
These statements apply to the actual cover, not only a general
member. Consequently, for the Galois orbit Omega of characters
selected by e,

\[
W_{\mathbb C}=\bigoplus_{\chi\in\Omega}W_\chi,
\qquad \dim_{\mathbb C} W_\chi=2\cdot3-2=4.             \tag{2}
\]

Every character in Omega is nontrivial. The invariant Jacobian
summand, to which this multiplicity formula does not apply, is
not part of P. The factor is Gamma-stable and its cover action
consists of algebraic endomorphisms. On H^1 use their pullbacks;
the opposite-action convention is immaterial for the abelian
group Gamma. No W_chi is asserted to be rational or an abelian
factor.

**One joint group and its invariant character spaces.** Put
H=Hg(A x P), acting on V direct sum W by cohomology. The projections
to Hg(A) and Hg(P) are surjective. This is
Moonen--Zarhin, *Hodge classes on abelian varieties of low dimension*,
[arXiv:math/9901113v1, section 3.1, PDF p. 7](https://arxiv.org/pdf/math/9901113v1#page=7);
the same formal assertion has no dimension restriction.
We do not assume H is the full product.

Borovoi, *The Hodge group and endomorphism algebra of an Abelian
variety*, [Proposition (a),(d), English translation, pp. 1--2](https://www.math.tau.ac.il/~borovoi/papers/Hodge-eng.pdf#page=1),
says that the Hodge group is connected reductive and that its
commutant on rational H_1 is End^0. Dualizing gives the needed
commutation on H^1. In particular, every element of the cover
algebra acting on W commutes with Hg(P), hence with H.

For chi in Omega its complex projector is

\[
e_\chi=\frac1{|\Gamma|}\sum_{\gamma\in\Gamma}
                    \chi(\gamma)^{-1}\gamma^*.
\]

It therefore commutes with H_C, as do the inclusion and projection
maps in (2). All four-dimensional spaces W_chi are H_C-invariant,
even if Hg(P) has additional endomorphisms or is smaller than its
generic value. The projector need not descend to Q. We use it
only after complexifying an actual rational morphism.

**The target remains irreducible in dimension 64.** L032 gives
the complete Hg(A)_C representation after pullback to the
surjective spin cover:

\[
V_{\mathbb C}\simeq
 \bigoplus_{\epsilon\in\{+,-\}^3}R_\epsilon^{\oplus256},
\qquad
R_\epsilon=S_1^{\epsilon_1}\boxtimes
             S_2^{\epsilon_2}\boxtimes S_3^{\epsilon_3},
\qquad \dim R_\epsilon=4^3=64.                         \tag{3}
\]

These are all eight half-spin tensor types for the three
six-dimensional quadratic factors. Because the spin action
surjects onto Hg(A)_C, the submodules in (3) descend as complex
Hg(A)_C modules and remain irreducible. Surjectivity of
H_C -> Hg(A)_C now makes every one irreducible for H_C as well:
an H_C-invariant subspace would be invariant under the whole
image Hg(A)_C. Thus (3), with H_C acting by this projection, is
also a direct sum of irreducible H_C modules. The same holds
for V_C^(direct sum r), with all multiplicities multiplied by r.
No individual complex block is asserted to descend rationally.

**Both possible directions of a morphism.** A rational Hodge
morphism between V^(direct sum r) and W is H-equivariant. One
may apply Moonen, *An introduction to Mumford--Tate groups*,
[version 11 May 2004, Corollary 4.5 and Lemma 4.6,
PDF pp. 8--9](https://www.math.ru.nl/~bmoonen/Lecturenotes/MTGps.pdf#page=8),
to V direct sum W and then restrict from its Mumford--Tate group
to H. The power uses the diagonal group action. Equivalently,
the rational stabilizer of the morphism contains the Hodge
circle and hence H. This does not impose cover-equivariance.

Suppose f:V^(direct sum r) -> W is a rational Hodge morphism.
For each irreducible copy R in (3) and each chi in Omega,

\[
e_\chi f_{\mathbb C}|_R:R\longrightarrow W_\chi
\]

is H_C-equivariant. If nonzero, its kernel is a proper invariant
subspace of the irreducible R, so it is injective. This would
embed a space of dimension 64 into one of dimension 4, which is
impossible. All these component maps vanish, so f_C and f vanish.

Conversely let u:W -> V^(direct sum r) be a rational Hodge
morphism. Choose the H_C-equivariant projection pi_R onto each
individual summand in (3). For each chi the composite

\[
\pi_R u_{\mathbb C}|_{W_\chi}:W_\chi\longrightarrow R
\]

is equivariant. A nonzero image would be the whole irreducible
R, impossible because the domain has dimension 4. Every component
is zero, so u_C and u vanish. Reducibility of W_chi is harmless.
Crucially, neither argument assumes f or u commutes with the
cover action: postcomposing or restricting by its invariant
projectors is sufficient.

**Contravariance, isogenies and the transfer threshold.** If
a:P -> A^r is an abelian homomorphism, its pullback is a rational
Hodge map V^(direct sum r) -> W and is therefore zero. For
b:A^r -> P, pullback instead goes from W to V^(direct sum r),
so it too is zero. The rational H_1 functor on abelian varieties
up to isogeny is faithful, as recalled in
[Moonen, sections 1.5--1.6, PDF pp. 3--4](https://www.math.ru.nl/~bmoonen/Lecturenotes/MTGps.pdf#page=3).
Duality gives the same faithfulness for H^1. Thus a and b are
zero in Hom tensor Q. The abelian homomorphism group is
torsion-free: if N a=0 its connected image lies in finite
N-torsion, so its image is the identity. This proves (1) for
actual homomorphisms.

Isogenies identify rational Hodge structures, so the proof
persists under the stated replacements. Maps to or from finite
products are determined by their restrictions or projections to
each factor, proving the final extension without assuming any
individual W_chi is rational.

The required threshold was a common constituent of the joint
representation supporting a nonzero rational map. Each source
constituent has dimension at most 4, while every target one has
dimension 64; there is no such constituent. Unbounded character
orbit size increases dim P, not the bound in (2). This is the
new exclusion beyond L032's small-total-dimension test. It says
nothing about maps between higher tensor powers of cohomology
induced by arbitrary correspondences. The 21-dimensional cycle
span on the Dickson family, three attained RM directions against
four required, and the universal rational Hodge gap are unchanged.

## Mathlib

Coverage of the full statement: **not checked**. No Mathlib
theorem name or absence claim is asserted. The named Prym,
centralizer, group-projection and Hodge-morphism results are
supporting inputs; none is cited as an exact theorem stating (1).
The joint-group specialization is the proof above, using all
of L032's complex constituents and retaining rational descent.
