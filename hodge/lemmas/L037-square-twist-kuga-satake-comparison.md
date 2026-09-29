# L037 — The square-twist comparison retains the missing cubic action

## Hypotheses

Let S be a projective complex K3 surface in the cubic-RM locus
under consideration, with T=T(S), its nondegenerate cup-product
form q, and the full Hodge endomorphism field

\[
E=\operatorname{End}_{\rm Hdg}(T)
 =\mathbb Q[u]/(u^3+u^2-2u-1),\qquad
\dim_{\mathbb Q}T=18,\quad \dim_E T=6.
\]

Let U be multiplication by u. The polarization adjoint on the
totally real field E is the identity, so every element of E is
q-self-adjoint. Put a=2 id+U and q_a(x,y)=q(ax,y). Write T_a
for the same rational Hodge structure equipped with q_a.
For the Kuga--Satake constructions use -q and -q_a consistently;
q itself remains the actual cup product for all correspondences
on S. Changing both signs does not change the isometry test.

Let A=KS(T,-q), A_a=KS(T_a,-q_a), B=A^2 and B_a=A_a^2.
Use compatible standard embedding vectors and abelian
polarizations, as specified in the proof, to obtain

\[
\kappa:T\hookrightarrow H^2(B,\mathbb Q),\qquad
\kappa_a:T_a\hookrightarrow H^2(B_a,\mathbb Q).
\]

An embedding is called algebraic here if its extension to
H^2(S,Q), zero on NS(S)_Q, is induced by a rational algebraic
correspondence from S, using the actual source cup product q.
Similarly, an endomorphism of T is algebraic if an algebraic
self-correspondence of S induces it. Algebraicity of kappa is
an explicit conditional hypothesis below, not an established
fact on the transverse RM locus.

## Conclusion

The specified twist is a square:

\[
b=U^2+U-\mathrm{id},\qquad b^2=a,\qquad
b^{-1}=U^2-\mathrm{id}.
\]

Consequently a is totally positive, -q_a is a polarization, and
b:(T_a,q_a) to (T,q) is a Hodge isometry. Known Kuga--Satake
functoriality supplies an algebraic abelian cohomology
isomorphism I:H^2(B_a,Q) to H^2(B,Q), with algebraic inverse,
such that

\[
I\kappa_a=\kappa b.                                      \tag{1}
\]

Fix an ample class h on B and let d be kappa's q-adjoint for
the pairing R_h(alpha,beta)=integral_B alpha beta h^{dim B-2}.
Then s=d kappa is a nonzero element of E and

\[
d I\kappa_a=s b,\qquad
(I\kappa_a)^{\dagger_q}(I\kappa_a)=s a.                  \tag{2}
\]

No scalar assertion about s is needed. If kappa is algebraic,
r=s^{-1}d is algebraic, r kappa=id_T, and

\[
r I\kappa_a=b,\qquad
\kappa_a\text{ is algebraic}\ \Longleftrightarrow\
U\text{ is algebraic}.                                  \tag{3}
\]

The readily transported cycle I^{-1}kappa instead equals
kappa_a b^{-1}; its normalized return acts as id_T. If the
modified embedding is encoded as a tensor using q_a rather
than q, its action on this same geometric S is kappa_a a^{-1},
and the normalized return acts as b^{-1}. Under the same
ordinary-kappa hypothesis, algebraicity of this alternative
tensor is also equivalent to algebraicity of U.

Thus the functorial square comparison and transport of the
ordinary cycle alone do not supply the required non-scalar
self-correspondence. This stops that supply recipe unless an
independent modified cycle is constructed. It does not exclude
such a construction, other comparisons, or arbitrary cycles.

## Proof

**Imported framework and the precise specialization.**
van Geemen, *Real multiplication on K3 surfaces and Kuga Satake
varieties*, arXiv:math/0609839v1,
[Lemma 4.2 and Example 4.3, PDF p. 13](https://arxiv.org/pdf/math/0609839v1#page=13),
give the total-positivity and square-twist criteria. Varesco,
*Hodge similarities, algebraic classes, and Kuga--Satake varieties*,
arXiv:2304.02519v3,
[Proposition 3.1 and Lemmas 3.4--3.5, pp. 11--14](https://arxiv.org/pdf/2304.02519v3#page=11),
give the compatible abelian comparison. Its
[section 1 preceding Definition 1.2, p. 5](https://arxiv.org/pdf/2304.02519v3#page=5)
states the polarization adjoint on a totally real endomorphism
field. These known results are imported, not reproved.

The conditional algebraic retraction framework is also known:
Varesco, *The Hodge conjecture for powers of K3 surfaces of
Picard number 16*, arXiv:2203.09778v3,
[Lemma 1.6 and proof, p. 5](https://arxiv.org/pdf/2203.09778v3#page=5).
The specialized calculation below retains the actual geometric
adjoint and its invertible normalization, rather than transferring
the scalar conclusion of Lemma 4.4 of the first Varesco paper
to a changed input form. This is a reproduction/application
of known tools, not an originality claim or a new unconditional
algebraic correspondence.

**Exact square and applicability.** The field relation gives

\[
U^3=-U^2+2U+\mathrm{id},\qquad
U^4=3U^2-U-\mathrm{id}.
\]

Hence

\[
(U^2+U-\mathrm{id})^2=U+2\mathrm{id},\qquad
(U^2+U-\mathrm{id})(U^2-\mathrm{id})=\mathrm{id}.
\]

Thus b is nonzero. For every real embedding sigma of E,
sigma(a)=sigma(b)^2>0. Lemma 4.2 applies to -q. Since b is
q-self-adjoint,
q(bx,by)=q(b^2x,y)=q_a(x,y); it preserves Hodge types because
b belongs to E. Example 4.3 therefore applies, with multiplier
one. Neither the identity on the underlying vector space nor
b as a geometric self-map of S has been declared an isometry
for q on both sides: b's q-based squared norm is a, not id.

**Compatible embeddings and cohomological direction.**
Choose the embedding vector v_a in T_a, and take v=b v_a
on T. Choose the abelian polarization vectors on the target
to be the b-images of the source vectors. These are exactly
the compatible choices in Varesco's Lemmas 3.4--3.5 for
multiplier one. Proposition 3.1 gives the weight-one Hodge
isomorphism
Phi=C^+(b):H^1(A_a,Q) to H^1(A,Q), compatible with those
polarizations and the embeddings.

To fix the contravariant cohomology convention, choose an
integer n>0 and an actual isogeny g:A to A_a with
g^*=n Phi on H^1. Rational weight-one Hodge isomorphisms
between abelian varieties have this realization; clearing
the lattice denominators gives g. Put G=g times g:B to B_a.
On H^2 define

\[
I=n^{-2}G^*,\qquad I^{-1}=n^2(\deg G)^{-1}G_*.
\]

The formulas are inverse: for an isogeny the usual pullback
and pushforward compose to its degree on rational cohomology.
Both are algebraic correspondences. On the cross H^1 tensor
H^1 summand, I=Phi tensor Phi, so the imported commuting
diagram is precisely (1). This argument uses no algebraic
map from S to either abelian square.

**Geometric transpose and an algebraic normalization.**
Let p_T be the rational cohomology projector of S onto T.
It is algebraic. Explicitly, for a point o, rational divisor
basis D_i of NS(S)_Q and intersection matrix Q_N, the cycle

\[
\pi_T=\Delta_S-[o]\mathbin{\times}S-S\mathbin{\times}[o]
 -\sum_{i,j}(Q_N^{-1})_{ij}D_i\mathbin{\times}D_j
\]

acts as p_T on H^2 and kills the other cohomology groups.
Nondegeneracy of Q_N follows from the Hodge index theorem.
The divisors are algebraic by Lefschetz (1,1).

Set m=dim B. Via Poincare duality let gamma_kappa be the
rational cohomology correspondence inducing kappa p_T,
with only the T tensor H^2(B) Kunneth component. Define

\[
d=p_T\,{}^t\!\gamma_{\kappa,*}
       \circ(h^{m-2}\smile -):H^2(B,Q)\longrightarrow T.
\]

Transposition and the projection formula give, for x in T,

\[
q(x,d\alpha)=R_h(\kappa x,\alpha).                         \tag{4}
\]

Thus d is the actual q-adjoint. Its Hodge compatibility
implies s=d kappa belongs to E. It is nonzero: if omega spans
T^{2,0}, injectivity makes kappa(omega) a nonzero (2,0)-class
on B. Such a class is primitive for h, since multiplication
by h^{m-1} would have type (m+1,m-1) in the top degree.
The Hodge--Riemann bilinear relations give
R_h(kappa(omega),overline{kappa(omega)}) nonzero. Equation
(4) then implies
q(omega,s overline{omega}) nonzero. As E is a field, s is
invertible.

If kappa is algebraic, gamma_kappa can be represented by
an algebraic cycle composed with pi_T. Its transpose,
multiplication by h^{m-2}, and p_T are algebraic, so d and
s are algebraic maps. Write the characteristic polynomial
of s on T as
P(z)=z^{18}+c_{17}z^{17}+...+c_1z+c_0, with c_0 nonzero.
Cayley--Hamilton expresses its inverse on T as

\[
s^{-1}=-c_0^{-1}
(s^{17}+c_{17}s^{16}+\cdots+c_1\mathrm{id}_T).
\]

In this expression the identity is represented by pi_T;
composition and rational sums preserve algebraicity. Thus
s^{-1} and r=s^{-1}d are algebraic under this hypothesis.
This construction uses only forward Lefschetz and has no
algebraic-inverse-Lefschetz assumption.

**Return action and the algebraicity equivalence.**
Equation (1) gives d I kappa_a=s b and r I kappa_a=b.
The q-adjoint of kappa b is b d, since b is q-self-adjoint.
Consequently its geometric Gram operator is b s b=s a;
s and b commute in E. These are exactly (2).

Assume kappa algebraic. If kappa_a is algebraic, composing
it with I and r realizes b algebraically on T. Squaring
that correspondence and subtracting twice the diagonal
realizes U=b^2-2 id. Conversely, algebraicity of U realizes
b=U^2+U-id, and (1) writes kappa_a=I^{-1}kappa b as a
composition of algebraic correspondences. This proves (3).
The projector pi_T allows all these equalities to be used
on the actual S cohomology without introducing other-degree
or divisor components into the composition.

Transporting only the ordinary embedding gives
I^{-1}kappa=kappa_a b^{-1}. Its return r I I^{-1}kappa is
id. Equality of its image subspace with that of kappa_a
therefore does not give the missing parametrized map.

For completeness, if e_i is a rational basis of T and
e^i its q-dual, the tensor inducing a map eta:T to H^2(B_a)
on this S is sum_i e_i tensor eta(e^i). Its q_a-dual basis
is a^{-1}e^i, so a tensor formed using q_a instead induces
eta a^{-1} with the actual cup product. Taking eta=kappa_a
gives normalized return b a^{-1}=b^{-1}. An algebraic
invertible endomorphism has algebraic inverse by the same
polynomial argument, so algebraicity of b^{-1} is equivalent
to that of b and hence U, proving the alternative claim.
More generally an abstract q_a-adjoint satisfies
eta^{dagger_{q_a}}=a^{-1}eta^{dagger_q}; it is not the
transpose furnished by cycles on S unless that correction
has been supplied algebraically.

**Effect on the gap.** The actual threshold is an algebraic
non-scalar action on the transverse cubic-RM surfaces, not
an isogeny or an identification of Hodge subspaces. The square
test succeeds, but the resulting supply retains both the
unproved ordinary cycle and a modified-cycle requirement
equivalent to U under that ordinary-cycle hypothesis. An
independent proof of modified-cycle algebraicity would still
be useful; none is supplied by the functorial transport.
The existing 21-dimensional span on the Dickson family and
three attained RM directions against four required do not
increase. Arbitrary primitive fourfold classes and higher
dimensions remain unresolved. This is an informative negative
decision for one supply recipe, not a Hodge counterexample
or a complete informal candidate.

## Mathlib

Coverage of the full statement: **not checked**. No full or
supporting Mathlib match, or absence from Mathlib, is asserted.
The named van Geemen statements match the polarization and
square-isometry criteria; Varesco's Proposition 3.1 matches
the compatible abelian comparison, and Lemma 1.6 supports
conditional algebraic retraction. They do not assert this
full q-based specialized equivalence or supply its missing
cycles. Hodge--Riemann, Poincare duality, cycle functoriality
and Cayley--Hamilton are supporting standard inputs. All
source links, versions and theorem qualifications are retained
above; no progress beyond the checked literature is claimed.
