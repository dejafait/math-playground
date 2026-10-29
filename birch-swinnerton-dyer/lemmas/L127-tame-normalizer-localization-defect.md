# L127 — Bad-prime Hecke exchange and the normalizer localization defect

## Hypotheses

Retain L123 and L126, including the original CM list, rational n,
factorization w=psi(a)W, full tame Eichler-unit levels, coefficient maps,
and all conductor, residual-image and incoherence assumptions. Thus
F=Q, K is imaginary quadratic, p>=5 is inert and split multiplicative
for A, the CM conductor and character are trivial, and W_p=1.
At a prime q dividing the split conductor n^+, write e=v_q(n^+);
the permitted values are 1 and 2. Such a prime is different from p.
Statements about this local case require n^+ to have such a divisor.
No existence assertion for q is made when n^+=1.

Let N be the p-adic completion of the **unlocalized** pullback direct
limit of J_m(K^ab) tensor Z_p in Fornea's construction. Write P_m for
the idempotent cutting out the source's chosen residual maximal ideal
at level m, and P for the resulting continuous projector on N.
Then M=PN is L123's actual completed residual-localized module.
Let tilde-Phi and tilde-J denote its measure and complete norm moment
before applying P. In particular J=P tilde-J. These are auxiliary
objects for comparing the original maps, not replacements for them.
Use calligraphic W for the covariant action of right translation by W
on Jacobians, the direct limit and N.

The construction inputs are Michele Fornea, *Plectic Heegner classes*,
[arXiv:2603.28327v2, 13 April 2026](https://arxiv.org/html/2603.28327v2),
Section 2.1.2/(14)--(15), Definitions 2.6 and 2.8, Proposition 2.9,
Corollary 2.10, (21)--(23), the residual localization immediately before
Proposition 2.18, Corollary 2.21 with its normalized-pushdown diagram,
Corollary 3.9, Lemma 4.12 and (63). The local calculation and defect
identity below are explicit specializations; they are not attributed to
an unprinted W-equivariance theorem in that source.

## Conclusion

At every q|n^+ the actual local normalizer has Atkin--Lehner coset
K_q A_e K_q, where in coordinates adapted to the integral CM embedding

\[
 K_q=\operatorname{im}\left\{
 \begin{pmatrix}a&b\\q^e c&d\end{pmatrix}\in\mathrm{GL}_2(\mathbf Z_q)
 \right\},\qquad
 A_e=\begin{pmatrix}0&1\\q^e&0\end{pmatrix}.
\]

For the **abstract** local Hecke algebra with Haar measure vol(K_q)=1,
write U_q=[K_q diag(1,q) K_q] and
U_q^op=[K_q diag(q,1) K_q]. Then

\[
 [W_q]U_q[W_q]^{-1}=U_q^{op}\ne U_q.                 \tag{1}
\]

Thus degree-one normalization does not give a full-Hecke-linear action
by formal double-coset identities. This is not a claim that the two
operators remain distinct on the physical Jacobian, its residual
summand, or its A quotient. At the conductor newvector line a scalar
normalizer action is compatible with (1).

The geometric action does commute with the unlocalized p-level maps,
p-diamonds, U_p, the ordinary projector, and the exact auxiliary-good-
Hecke normalization. At the level of complete raw moments one has

\[
 J_W=P\mathcal W\widetilde J
     =(P\mathcal W P)J+E_W,\qquad
 E_W=P\mathcal W(1-P)\widetilde J\ \in M.             \tag{2}
\]

The equality uses inversion of the full original CM list after
integration; it does not assert equality of inverted raw measures.
To extend F=P W P on M to an I-linear operator by
F(x tensor i)=F(x) tensor i, the balancing condition is

\[
 \big(P(\mathcal W T-T\mathcal W)P x\big)\otimes1=0
       \quad (x\in M,\ T\in\mathbb T_{\bar\rho}).     \tag{3}
\]

Here W in the definition of F means calligraphic W. A base-algebra
operator T on M is extended by zero on (1-P)N when writing (3);
for a physical Hecke generator its geometric action on N gives the
same sandwiched commutator. For T=U_q the
expression in (3) is
P(U_q^op-U_q) W P x, where U_q^op acts geometrically on N.
No vanishing of (3), E_W, or their relevant specialized images has
been proved. In particular (1) does **not** prove their nonvanishing.
Individual terms in (2) have not been put in the domain of pr_A.
Only J and J_W have the complete-integral domain statements from
L123/L126. No scalar b_W=epsilon b, eigenvalue epsilon, residual value,
rational Kummer membership or BSD assertion follows.

This is an informative obstruction to the direct full-Hecke-linear
extension argument, with the actual scalar question unresolved. It is
a known-method specialization (REPRODUCTION), accepted by the separate
step-530 conceptual audit below under the retained source inputs.

## Proof

**Adapted coordinates, including squared level.** At q|n^+, K_q is
split as a quadratic algebra and its maximal order is Z_q times Z_q.
In standard Eichler coordinates the order is
R_e=End(L_0) intersect End(L_e), where
L_0=Z_q e_1+Z_q e_2 and L_e=Z_q e_1+q^e Z_q e_2.
The two embedded integral idempotents preserve both lattices. They
split L_0 as the direct sum of rank-one lattices Lambda_1,Lambda_2
on the two eigenlines, and split L_e as
q^r Lambda_1 plus q^s Lambda_2 for r,s>=0.
Since L_0/L_e is cyclic of order q^e, {r,s}={0,e}.
Order the lines accordingly and choose generators. The basis change
preserves both L_0 and L_e, hence belongs to R_e^times. The embedded
split algebra is now diagonal. This also allows either labeling of
its idempotents; neither orientation was discarded.

The chosen W_q normalizes R_e and exchanges these two lines. Up to a
scalar its matrix is [[0,u],[v,0]] with u,v nonzero. Conjugating R_e
by this matrix gives upper-right ideal (u/v)q^e Z_q and lower-left
ideal (v/u)Z_q. Equality with R_e implies v_q(v/u)=e.
After scalar rescaling W_q is [[0,1],[q^e eta,0]] with eta a unit.
It therefore has coset K_q A_e=A_e K_q. Conjugation of a double coset
by the preceding R_e-unit basis change does not change U_q.
This proves the assertion for the actual W_q, for e=1 and e=2,
including q=2. It uses no global normalizer or choice of a new CM list.

**Exact Hecke exchange.** A_e diag(1,q) A_e^{-1}=diag(q,1).
Because A_e normalizes K_q, conjugating the Hecke characteristic
function gives (1) with no degree factor. In fact A_e^2 is central,
and its degree-one Hecke element is invertible.

To check inequality of the cosets rather than just of the displayed
matrices, choose GL_2(Z_q) representatives k_1,k_2 of K_q. Both their
diagonal entries are units and their lower-left entries lie in q^e Z_q.
The upper-left entry of k_1 diag(1,q) k_2 is a unit, while its
lower-right entry is divisible by q. For k_1 diag(q,1) k_2 these
properties are reversed. All these matrices have determinant valuation
one. A central scalar relating two such representatives must have
valuation zero, so cannot change the two entry properties. The cosets
in PGL_2(Q_q) are therefore disjoint. Their characteristic functions
are distinct in the abstract Hecke algebra over Z_p or Q_p. The
inequality may disappear in a representation quotient; no faithfulness
of the physical Hecke action has been assumed.

**The action before residual localization.** The automorphisms
rho_m:[z,g] -> [z,gW] are over Q and compatible with forgetting
p-level. The squares for those level maps are cartesian: translation
by W gives a bijection on every fiber, with its inverse giving the
inverse bijection. Thus rho_m commutes with pullback on divisor classes
as well as with pushforward. It also commutes with the second
degeneracy maps, since their translating adeles are supported at p
and W_p=1. This proves compatibility with both p-level directions,
U_p and its powers. It also proves commutation with p-diamonds.
Taking the defining limits proves commutation with the ordinary
idempotent; on an ordinary domain the inverse powers of U_p commute
as well. This does not yet assert that W preserves P_m.

At every good tame prime the order is maximal and the projective
normalizer lies in the level group: if g normalizes End(L_0), elementary
divisors for gL_0 relative to L_0 have equal exponents, since otherwise
their two off-diagonal endomorphism ideals differ. Thus gL_0 is
homothetic to L_0 and g is a scalar times an integral unit.
Consequently W commutes with
each good spherical double coset: at its own prime its class is the
unit coset, and the other components have disjoint support.
In particular it commutes with T_l-l-1 and the unchanged scalar unit
(a_l(A)-l-1)^{-1} in the source's (22). Thus
varphi_m(rho_m x)=W varphi_m(x) before residual localization.
The compatible integral automorphisms pass to the direct limit and
then its p-adic completion N. They are continuous because they
preserve p^nN for every n. Hence they commute with integration of
continuous Z_p-valued functions. The log norm kernel here is
Z_p-valued: its two conjugate linear factors and determinant coordinate
are units on X, and its logarithm lies in p Z_p.

For clarity about P, each physical finite-level Hecke algebra is a
finite Z_p-algebra, hence complete and a product of its local factors.
One can obtain the product idempotents by first taking those of its
Artinian reduction modulo p and then uniquely lifting them: for an
idempotent the derivative of X^2-X is a unit modulo p. Projection to
the chosen factor equals localization at its maximal ideal. The
compatible Hecke maps and the fixed full residual eigensystem make these
projectors compatible with the pullback maps. They therefore give a
split projector on the direct limit. Completion preserves this split
decomposition, proving M=PN. This construction does not show that
W commutes with P. The factors are the actual compatible choices of
the source tower, not a replacement using only good-prime eigenvalues.

**Complete-list inversion and (2).** Before localization, Corollary
3.9 and the commutation with varphi_m just proved give, cell by cell,

\[
 \widetilde\Phi(hW)(z)=\mathcal W\widetilde\Phi(h)(z).
                                                               \tag{4}
\]

The representatives h_t^{-1} must still be compared with h_t. The
complete norm integral
F_1(t)=integral q_tau d tilde-Phi(psi(t))(z) factors through the same
finite quotient C as in L126. Indeed a tame unit changes no point;
for a rational torus element r, left rational equivalence changes
the p-cell to r_p^{-1}xi and absorbs the discarded division components
in the unit level. Thus the measure is pushed forward by r_p.
L126's exact identity q_tau(r_p s)=q_tau(s) makes the integrated
value unchanged. All of these are equalities of points before P,
and their continuous integrals exist in N. This justifies this use
of the L126 argument in N without postulating representative invariance
of measures. Since inversion permutes C and the source list counts
each class once,

\[
 \sum_t\int_X q_\tau\,d\widetilde\Phi(h_t^{-1})(z)
       =\widetilde J.
\]

Apply (4), then P, to obtain J_W=P W tilde-J. Write
tilde-J=P tilde-J+(1-P)tilde-J and use J=P tilde-J. This proves (2).
No pr_A or localization has been passed through an infinite integral.

**The first unsupported handoff.** The proposed rule on the tensor
product must respect (Tx) tensor i=x tensor Ti. Since P commutes
with T, the difference after applying that rule is exactly
P(WT-TW)P x tensor i. Vanishing for i=1 implies vanishing for every i;
these balanced relations are precisely what is needed to define the
I-linear rule. This proves (3), not its vanishing. On the unlocalized
geometry W U_q=U_q^op W, so its displayed specialization follows.
Equation (1) rules out proving it by equality in the abstract Hecke
algebra. The physical quotient or the specialization might kill it;
this possibility has neither been excluded nor established.

Even a well-defined operator on M tensor I would not by itself remove
E_W from (2). This records both the information lost before projection
and the balancing issue afterwards. Conversely it is not necessary
for every possible proof of b_W=epsilon b to construct this I-linear
operator: an argument on the appropriate cohomological quotient might
avoid it. The completed attempt stops at this unsupported handoff,
before using any local newvector eigenvalue. There is no asserted
counterexample to the scalar identity or to the source construction.

**Separate conceptual audit, step 530 (2026-10-28).** PASS for
(1)--(4), with the original hypotheses and all stated qualifications.
No premise or conclusion is strengthened. The following checks spell
out the load-bearing domains and conventions of the existing proof.

The integral idempotents split both lattices even at q=2; cyclicity of
L_0/L_e forces the elementary exponents to be 0,e, so the adapted
basis preserves the actual Eichler order. For e=1 or 2 the diagonal
entries of every integral K_q representative are units. Multiplication
on either side of diag(1,q) leaves the top-left entry a unit and the
bottom-right entry in q Z_q; multiplication around diag(q,1) reverses
these properties. Determinant valuation one forces any identifying
projective scalar to be a unit. This verifies distinct supports, not
faithfulness in a representation. Covariant right translation does not
reverse the conclusion: both W_q^{-1} diag(1,q) W_q and
W_q diag(1,q) W_q^{-1} are diag(q,1), since W_q is antidiagonal.
Thus the operator-composition convention also gives W U_q=U_q^op W.

Here is an explicit completion check requiring no torsion-freeness or
exactness of nonsplit completion. Put
A_0=colim_m(J_m(K^ab) tensor Z_p), with the original pullbacks and m>=1.
The physical Hecke algebras are finite commutative Z_p-algebras. Their
transition maps in Proposition 2.9 are surjective: all the target
generators, including diamonds and p-operators, are images of the same
generators at the next level. The fixed full residual characters are
compatible with these maps. For a surjection of these algebras, the
idempotent of the corresponding local factor maps to that factor's
idempotent, as is seen by reducing in every residue field. Uniqueness
of idempotent lifting then gives compatibility integrally. Hecke
equivariance of pullback gives P_0 on A_0 with
A_0=P_0 A_0 direct-sum (1-P_0)A_0. Consequently

\[
 N=\varprojlim_r A_0/p^rA_0
  =\widehat{P_0A_0}\ \oplus\ \widehat{(1-P_0)A_0},
 \qquad PN=\widehat{P_0A_0}=M.
\]

Fornea's Corollary 3.9, using (22), constructs the cell values already
in A_0, before residual localization or ordinary control. Thus tilde-Phi
is available without an unproved lift of a localized measure. The
completion of its norm integral can be defined modulo each p^r: the
Z_p-valued continuous kernel q_tau modulo p^r is locally constant on
compact X, and its integral is the finite cell sum in A_0/p^rA_0.
Refinement and reduction are compatible by finite additivity. Taking
the inverse limit gives tilde-J in N. Both W and P_0 act at each of
these quotients and commute with those finite sums; no identification
of a completion kernel with p^rN is needed. This proves the integration
compatibilities used in (2) and (4) in the inverse-limit topology.

The complete-list argument uses the same rational p-cell pushforward
as L126: a rational torus element r replaces xi by r_p^{-1}xi, hence
pushes the measure forward by r_p. The exact norm-kernel invariance
removes that action only after integration. Tame units and the discarded
inert division factors are absorbed in the original level. Inversion
then permutes the entire original quotient list, with multiplicity one.
These point and finite-sum statements hold before P, so (2) has exactly
the incoming term P W (1-P) tilde-J, not an outgoing complement term.

Finally let R=mathbb T_{bar rho} and F=P W P on M. The additive map
(x,i) mapped to F(x) tensor i descends to the algebraic tensor product
M tensor_R I exactly when
(F(Tx)-T F(x)) tensor i=0 for all T,x,i. These are precisely its
balancing relations. Since multiplication by i is an endomorphism of
the target I-module, testing i=1 is necessary and sufficient, giving
(3). This does not assume F is R-linear before tensoring. Physical
Hecke generators commute with P, so their sandwiched commutators agree
with those of the zero extensions from M. Neither the abstract support
calculation nor this criterion decides vanishing on the specialized
module. Flat base change in Lemma 4.12 identifies the diamond-invariant
domain of (63); it supplies no projection for either separated term of
(2). Only the complete J and J_W retain the audited L123/L126 domains.

## Mathlib

Full tower/localization-defect statement and its Fornea construction:
**not checked**. Supporting local double-coset, idempotent-lifting and
tensor-balancing statements: **not checked**. No absence or formal
verification claim is made. The primary source is an imported informal
input; the displayed specialization passed the separate step-530
informal critical review, not formal verification.
