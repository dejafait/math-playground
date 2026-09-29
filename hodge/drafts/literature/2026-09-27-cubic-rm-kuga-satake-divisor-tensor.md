# Cubic RM tensor and divisor products on a Kuga--Satake power — literature assessment

TARGET: Determine whether the transported cubic tensor (kappa tensor kappa)(u_U) lies in the rational span of products of divisor classes on A^4 for A=KS(T(S)) at a very general point of the four-dimensional cubic RM locus.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched Kuga--Satake divisor products, Lefschetz groups, exceptional Hodge tensors and RM spin representations; the queries and inspected primary statements are recorded below. No inspected statement decides this particular cubic tensor.
SOURCE_EVIDENCE: Milne, Lefschetz classes on abelian varieties, Theorem 3.2 and Lemma 3.1, pp. 14--15 of the author-hosted PDF, https://www.jmilne.org/math/articles/1999aP.pdf#page=15; Schlickewei, arXiv:0907.2503v1, Theorem 3.3.1, p. 9, https://arxiv.org/pdf/0907.2503v1#page=9; embedding and spin references are detailed below.
COMPARISON: Milne gives the exact full-group invariant criterion for the divisor algebra on every abelian power, and Schlickewei gives the RM Hodge group and its endomorphism representation. Their specialization still requires locating the whole beta_U under the full Lefschetz-group action; Hodge invariance alone does not settle it.
GAP: Compute the polarization centralizer for the stated rank-18, dim_E T=6 representation and test whether it fixes beta_U, retaining all factor-mixing divisor classes, embedding choices and any disconnected components.
REASON: Import the general theorems and calculate only this specific tensor's invariance in a separate research turn. A membership certificate would supply beta_U algebraically while leaving kappa unresolved; non-invariance would stop only this divisor recipe.

## Hypotheses

Retain the [completed realization review](2026-09-27-cubic-rm-kuga-satake-realization.md)
and [family audit](../../foundations/05-cubic-rm-family.md): at a very
general point of the four-dimensional NS-fixed RM locus, rho=4,
dim_Q T=18, End_Hdg(T)=E=Q(zeta_7+zeta_7^(-1)), and dim_E T=6.
Use the inherited rational polarization q on T and the full
Kuga--Satake variety A=KS(T,q), up to a specified isogeny. No claim
about every specialization is made.

Let u_U in T tensor T be the tensor for L006's cubic generator U
under the existing cup-product identification. Fix the standard
embedding kappa:T -> H^1(A,Q) tensor H^1(A,Q) inside H^2(A^2,Q),
including its auxiliary choices. The target is the whole rational
class beta_U=(kappa tensor kappa)(u_U) in H^4(A^4,Q).
The divisor span includes all divisors of A^4, including mixed ones;
a single polarization or factorwise pullbacks give a smaller test.
The universal rational target in the [scope audit](../../foundations/01-target-and-scope.md)
is unchanged; its primary-source check from the preceding review is reused.

## Conclusion

The literature gate for the exact saved target is complete. SPECIALIZE
authorizes only the remaining representation/tensor test in a later
turn. The criterion and construction below are imported known results;
no membership answer, new representation calculation or cycle is
claimed here. This review is LITERATURE / NOVELTY_UNCHECKED /
EXPLORATION, the second exploration turn in the same Kuga--Satake
window. Failure to locate a full match does not establish originality.

The exact membership criterion is available, so there is no essential
unread source blocking that test. The conditional tensor-transfer
criterion is reused, not reproved. Even a positive answer would leave
algebraicity of kappa on the intended surfaces and the universal
fourfold/higher-dimensional target unresolved. The attained
21-dimensional span on the Dickson family and three directions
against four required are unchanged. No complete candidate appears.

## Proof

This is source evidence and applicability comparison, not a proof of
the tensor's membership or nonmembership.

### The exact divisor-algebra criterion

Read Milne, *Lefschetz classes on abelian varieties* (1999),
[author-hosted 31-page PDF, section 1, pp. 4--6](https://www.jmilne.org/math/articles/1999aP.pdf#page=4),
[Lemma 3.1 and Theorem 3.2, pp. 14--15](https://www.jmilne.org/math/articles/1999aP.pdf#page=14),
and [Corollary 4.5, Proposition 4.8 and Remark 4.9, pp. 21--23](https://www.jmilne.org/math/articles/1999aP.pdf#page=21).
Pagination here is that PDF's, not the journal's.

Milne defines C(A) as the centralizer of End^0(A) on rational
homology, with the polarization adjoint dagger, and S(A) by
g in C(A)^times with g^dagger g=1. Theorem 3.2 identifies its
invariants on all powers with the divisor algebra. Use Betti
cohomology and the contragredient action; no Tate twist is needed
for this S(A) formulation. Lemma 3.1 permits a splitting-field test.
Section 1 records isogeny invariance and compatibility with powers.
The theorem retains the whole group, including disconnected components.
The similitude formulation instead acts on Tate-twisted cohomology.
Proposition 4.8 compares whole rings of Hodge and Lefschetz classes;
Remark 4.9 illustrates why the identity component can miss classes.

Thus this theorem matches the requested *criterion*, with r=4 and
degree four. It neither computes S(A) here nor tests beta_U. A
dimension comparison or invariance under the Hodge group alone would
not answer the individual membership question.

### RM representation data

Read Schlickewei, *The Hodge conjecture for self-products of certain
K3 surfaces*, [arXiv:0907.2503v1, 15 July 2009, Theorem 3.3.1 and its hypotheses, p. 9](https://arxiv.org/pdf/0907.2503v1#page=9),
and [section 3.5, pp. 11--17](https://arxiv.org/pdf/0907.2503v1#page=11).
For irreducible K3-type T with totally real full endomorphism field E,
the theorem identifies the special Mumford--Tate group of the
Kuga--Satake Hodge structure as the image of Res_(E/Q) Spin(Q_E).
It also gives its decomposition through Cores_(E/Q) C^0(Q_E) and
its Hodge endomorphism algebra. The proof specifies the factorwise
left spin action and right-multiplication commutant after splitting.
These hypotheses cover the saved very-general T; no dim_E T=3
restriction occurs in this theorem. It does not identify the full
polarization centralizer with that spin image.

The exact divisor test still needs this representation with its
polarization, not merely the abstract endomorphism algebra. The
earlier comparison of Corollary 3.7.1, Theorem 2 and section 4.5 is
reused: the cubic example of E-dimension three and the six-line/Weil
fourfold application do not give a theorem for this E-dimension-six
tensor. No simple-factor dimensions or Albert types are calculated here.

### Spin model and embedding choices

Followed Schlickewei's reference and read van Geemen,
*Kuga-Satake varieties and the Hodge conjecture*,
[arXiv:math/9903146v1, 24 March 1999, Proposition 5.9, p. 11](https://arxiv.org/pdf/math/9903146v1#page=11),
and [sections 6.3--6.6, pp. 13--15](https://arxiv.org/pdf/math/9903146v1#page=13).
These give the Clifford polarization, the vector-to-endomorphism
embedding, the right-multiplication commutant (Lemma 6.5), and the
split half-spin model (Example 6.6). The latter uses the even and
odd exterior powers of a maximal isotropic space. They provide
explicit standard models for a later test. The generic full-CSpin
group assertion in Proposition 6.3 has a generic Mumford--Tate
hypothesis; it is not a replacement for Schlickewei's RM group.
No cubic tensor position in the divisor algebra is asserted there.

Read Varesco, *Hodge similarities, algebraic classes, and Kuga--Satake
varieties*, [arXiv:2304.02519v3, 2 November 2023, section 3, especially the definition preceding Lemma 3.5 and its proof, pp. 12--14](https://arxiv.org/pdf/2304.02519v3#page=13),
and [Remark 4.3, PDF p. 16](https://arxiv.org/pdf/2304.02519v3#page=16).
The embedding into End(C^+(T)) sends v to the map w -> v w v_0,
where q(v_0) is nonzero; a polarization supplies the tensor
identification. Remark 4.3 describes the effect of changing v_0
or the polarization and states independence of *algebraicity* from
these choices. It does not state the requested divisor-membership
answer. Track these identifications explicitly before changing
models in the test. The similarity theorem's restriction and the
separate algebraicity of kappa were already assessed and are reused.

### Search, reuse and source limits

Queries on 2026-09-27 included:

- `"Kuga-Satake" "divisor" "Lefschetz" group`
- `"Kuga-Satake" "real multiplication" "spin" "Hodge classes"`
- `"Kuga-Satake" "divisors" "tensor"`
- `abelian varieties divisor algebra invariants Lefschetz group theorem Hodge classes`
- `"Kuga-Satake" "divisor classes"`
- `"Kuga-Satake" "Lefschetz group"`
- `"Kuga-Satake" "real multiplication" "spin" "divisor"`
- `"Kuga-Satake" "exceptional" "Hodge"`
- `"Kuga-Satake" "tensor" "Lefschetz"`
- `"Kuga-Satake" "divisor" "products" "real"`
- `"Kuga-Satake varieties and the Hodge conjecture"`
- `"Kuga-Satake" "Lefschetz group" divisor tensor cubic`
- `"Kuga-Satake" "Spin(6)"`
- `"Kuga-Satake" "divisor algebra"`

Exact-terminology searches did not locate a full matching theorem.
The inspected primary statements above support the comparison;
search snippets are not treated as proofs. This is a bounded search.
The preceding review's conditional transfer, recent geometric
algebraicity results and rank/similarity limits remain sufficient
and are not mechanically reassessed.

Moonen--Zarhin's low-dimensional classification, Milne's CM/Weil-class
paper, Schlickewei's thesis, Poon's Picard-rank-14 construction and
general Hodge-conjecture claims also appeared as leads. Their relevant
theorem texts were not inspected in this step; none is used to decide
beta_U or to assert nonexistence. Weyl and Fulton--Harris are references
inside the inspected sources, not separately read originals. The
needed invariant theorem and explicit spin model were read directly,
so these unread leads are not essential dependencies of the selected test.

### Relevance, redundancy and bounded specialization

The main local gap is a supply of algebraic representatives beyond
the Dickson locus. L004's isometry limitation and L008--L030's
scoped representative failures remain intact. None tests this
auxiliary abelian divisor algebra; the closed doubled-source recipe
is not reopened. The previous Kuga--Satake review supplied only a
conditional transfer and left exactly the present test unscreened.

The downstream use is Varesco's previously imported Lemma 1.6:
a positive divisor certificate would supply the beta_U input, while
algebraicity of kappa would still be needed to transfer it back.
Membership, rather than any positive lower bound on a divisor span,
is the required threshold. Nonmembership would not imply that beta_U
is nonalgebraic or that U cannot have another algebraic representative.

One bounded research test is now justified:

1. Fix the Clifford embedding and polarization, and use the cited RM
   representation to specify the endomorphism action and its full
   polarization centralizer. If passing to a split or isogenous
   model, retain the actual tensor and the induced identifications.
2. Test beta_U under that centralizer, using Milne's criterion for
   all divisors of A^4. A single certified element moving beta_U
   gives a negative certificate. A positive result must verify
   invariance under the whole group, including components; it cannot
   rely solely on Lie-algebra invariance or known Hodge invariance.
3. Record the certificate and its exact scope. Continue this divisor
   supply if membership is proved; stop it upon non-invariance. If
   the test remains inconclusive, record the precise unsolved part
   and complete the window's continuation/stop assessment by the
   third exploration turn without restarting its count.

These are specifications for later work, not calculations performed
in this literature turn. No Clifford block decomposition for this
T, group dimension, tensor coefficient, or invariance claim has
been added. A proof of the general criterion would duplicate the
cited theorem; only its uncomputed specialization is warranted.

## Mathlib

Coverage: **not checked** for the full tensor-span statement or the
supporting Lefschetz-group and Clifford results. No Mathlib theorem
name or absence is asserted. Milne's Theorem 3.2 is a full criterion
for the divisor algebra; the other citations give supporting data,
not a full match deciding beta_U. No new lemma or script was produced.
