# L128 — The tame normalizer on the completed A branch

## Hypotheses

Retain L123, L126 and L127, with all their conductor, residual-image,
incoherence and integral-CM hypotheses and their original n, indexed CM
list, W, levels, measures and maps. Thus A/Q is modular, p>=5 is inert
in K and split multiplicative for A, and the quaternion algebra has
finite ramification set Delta minus {p}. Its tame split Eichler level
is n^+, with exponents at most two; the inert conductor is square-free.
The level after taking p-diamond invariants at level one is exactly
the conductor level of A under Jacquet--Langlands. No extra old level
or tame orientation subgroup is introduced.

Use L127's N, P, M=PN and unlocalized complete moment tilde-J. Write
W also for its covariant geometric action. Put J=P tilde-J and
J_W=P W tilde-J, as established in L127. Let R_0 be the source's full
residual physical Hecke ring, and I its localization at A's classical
augmentation prime. The images J tensor 1 and J_W tensor 1 in
M tensor_{R_0} I have L123/L126's complete diamond-invariant domains.
The symbol R below remains L123's localized residual, not a Hecke ring.

Imported inputs, with the scope already assessed at step 527:

- Fornea, *Plectic Heegner classes*,
  [arXiv:2603.28327v2, 13 April 2026](https://arxiv.org/html/2603.28327v2),
  Definitions 2.6/2.8, Proposition 2.9, Corollary 2.10, (21)--(23),
  Remark 2.12, Lemma 2.22, Corollary 2.23, Proposition 2.24 and the
  finite-etale augmentation assertion of Proposition 2.25, pp.11--18;
  Corollary 2.21, Lemma 4.12 and (63) for the original projection.
  The ordinary homology and physical-Hecke control inputs are imported,
  not reproved. We use the finite algebra over the weight ring and its
  completion, not an identification of an uncompleted local branch with
  that weight ring.
- Schmidt, *Some remarks on local newforms for GL(2)*, J. Ramanujan
  Math. Soc. 17 (2002), 115--147,
  [author PDF](https://sites.math.unt.edu/~schmidt/papers/gl2.pdf),
  Theorem 1.2.1 and Theorem 3.2.2, with Section 3.1 normalizations.
  These give the conductor newvector and its Atkin--Lehner sign for
  infinite-dimensional irreducible admissible representations of
  GL_2(Q_q) with trivial central character, including exponent two.
- Jacquet--Langlands, *Automorphic Forms on GL(2)*, LNM 114 (1970),
  [IAS edition](https://publications.ias.edu/sites/default/files/automorphic-forms-on-gl2-rpl_1.pdf),
  Theorems 4.2, 4.3(i), 15.1, including the one-dimensional division
  case; the standard strong multiplicity-one theorem for cuspidal
  GL_2 representations and Eichler--Shimura decomposition. Only the
  conductor-level A constituent is identified, not every oldspace.
- The standard Hensel factorization lemma for complete local rings,
  Nakayama's lemma, and faithful flatness of completion of a Noetherian
  local ring. The projector application and its coefficient action are
  justified below; no inverse-limit/localization interchange is used.

## Conclusion

For q dividing n^+, let pi_q be A's unitarily normalized local
GL_2 representation and set epsilon_q=epsilon(1/2,pi_q), with the
Atkin--Lehner matrix [[0,1],[q^{v_q(n^+)},0]] of Schmidt's convention.
For q in Delta minus {p}, write pi_q=St tensor chi_q, where chi_q is
unramified quadratic (possibly trivial), and set eta_q=chi_q(q).
Equivalently eta_q=a_q(A) in the usual weight-two elliptic normalization.
Define the sign

\[
 \epsilon_W=\prod_{q\mid n^+}\epsilon_q
             \prod_{q\in\Delta\setminus\{p\}}\eta_q
             \ \in\{1,-1\}.                              \tag{1}
\]

Empty products are one. The division factors in (1) are eta_q, not
-eta_q. There is no p-factor because W_p=1, and no archimedean factor
because this is finite right translation fixing the archimedean variable.
Then the complete moments satisfy

\[
 J_W\otimes1=\epsilon_W(J\otimes1)
              \quad\hbox{in } M\otimes_{R_0}I.             \tag{2}
\]

Consequently the original, unchanged projection and descent give

\[
 b_W=\epsilon_W b,\qquad
 R=(1+\epsilon_W)\operatorname{loc}_p(b),\qquad
 D^{++}=\frac{1+\epsilon_W}{4}\,
                   u_1\otimes\operatorname{loc}_p(b).     \tag{3}
\]

**Audit status (step 534): HOLD.** Equations (2) and (3) are proposed
known-method specializations (REPRODUCTION), not accepted results.
The separate audit below stops at Step 1's identification of the
controlled homology action with the dual physical action. The original
argument is preserved for repair; its later comparisons are not certified.
These proposed equations do not assert the value of epsilon_W
for an unspecified A, the value or nonvanishing of b, rational Kummer
membership, the second-factor finite local condition, suitable K,p for
arbitrary A, or a rank/order comparison. This is not a BSD candidate.
The raw equality J_W=epsilon_W J in M is not asserted. L127's abstract
bad-Hecke inequality and ATTEMPTS/061's formal-extension stop remain valid.

## Proof

Steps 1--5 preserve the step-531 proposed argument. The step-534 audit
following them withholds its essential action comparison and conclusion.

**1. A finite operator algebra which also acts on the coefficients.**
Let e_0 be the ordinary projector times the projector onto the trivial
character of the prime-to-p diamond group. These are the source's
projectors, and W commutes with them by L127. Put N_0=e_0N. Write
Lambda=Z_p[[Gamma]] for the remaining diamond algebra; since F=Q and
there is one p-place, Gamma is isomorphic to Z_p. Let H_m be the
source's ordinary, trivial-finite-diamond homology at level m, and
H=lim_m H_m under the source's pushdowns. Lemma 2.22 and Corollary 2.23
give H finite free over Lambda and H tensor_Lambda Lambda_m=H_m.
Write T for the physical ordinary, trivial-finite-diamond Hecke algebra
acting faithfully on H. It is finite over Lambda.

The dual-action convention matters. One can use the identifications in
Remark 2.12 and regard H_m as the Z_p-dual of the corresponding Tate
module for its Hecke action; a choice of the Tate twist does not change
these underlying endomorphisms. For a covariant endomorphism a of the Jacobian, its operator
on this dual is a^vee, defined by a^vee(f)=f composed with a.
Thus (ab)^vee=b^vee a^vee. This is an action of the opposite algebra;
on the commutative T it gives the same labeled Hecke algebra. The
transition map dual to pullback is the pushdown defining H. All
commutation assertions and the identities W^2=1 and W e=e W=epsilon e
below are unchanged on reversing products. This fixes the convention
for enlarging T without assuming that the larger algebra is commutative.

W preserves the dual tower, commutes with Lambda and acts on H. Let B
be the Lambda-subalgebra of End_Lambda(H) generated by T and W^vee.
It is finite as a Lambda-module: End_Lambda(H) is finite, Lambda is
Noetherian, and B is a Lambda-submodule. Its opposite algebra acts on
N_0. Here is the verification of the last, essential assertion.

Represent an element of B by a finite sum of words in T and W^vee.
If that sum is zero on H, its induced operator is zero on every H_m,
since the projections H -> H_m are surjective and equivariant.
Dualizing, the reversed sum of the corresponding physical operators
is zero on the ordinary, trivial-finite-diamond Tate module at level m.
Sandwich it by the finite-level idempotent e_{0,m}. It is then zero on
the entire Tate module. The action of End(J_m) tensor Z_p on T_p(J_m)
is faithful: after an embedding into C, an endomorphism of the complex
torus is determined by its action on the integral homology lattice;
this gives an injection of finite free Z-modules, which stays injective
after tensoring with the flat Z-module Z_p. The usual comparison with
the Tate module respects these endomorphisms. Hence the sandwiched
physical operator is zero in End(J_m) tensor Z_p, and kills
 e_{0,m}(J_m(K^ab) tensor Z_p).

This holds for every m. The original pullbacks commute with these
operators (for W this is L127). The relation therefore kills their
direct limit and then its p-adic completion. Completion of the split
idempotent decomposition identifies that completion with N_0. Each
operator preserves every p-power filtration, so this last passage is
continuous. Thus a relation detected on H really is a relation on N_0,
with products reversed. This proves the required B^op action; it does
not postulate a faithful action on N_0 or a full-Hecke-linear W.

**2. The common completed A component.**
Let a be the augmentation prime of Lambda and S=Lambda_a. Its residue
field is Q_p. Choose a generator t=gamma-1 of a; the completion of S is
S_hat=Q_p[[t]]. The algebra T tensor_Lambda S_hat is finite etale over
S_hat by the imported augmentation control and semisimplicity input.
Its special fiber is the classical conductor-level ordinary Hecke
algebra of Proposition 2.24. Idempotents of this finite reduced fiber
lift uniquely over the complete local base. In particular its A
character, whose residue field is Q_p, gives an idempotent e_A and

\[
 e_A(T\otimes_\Lambda S_{\rm hat})\simeq S_{\rm hat}.
                                                               \tag{4}
\]

For completeness, the finite etale factor on the left is finite free
and has one-dimensional special fiber, so it has rank one. The unit
map from S_hat is an isomorphism by Nakayama. The other factors may
have larger residue fields and are retained; they are not discarded
before constructing e_A.

The localization I from the hypotheses is T localized at the classical
A prime (the preceding residual and ordinary projectors do not change
this localization). Its maximal-ideal completion I_hat is exactly the
factor (4). This follows by completing the finite algebra T over S:
the lifted special-fiber idempotents give the product of the completions
at its finitely many maximal ideals over a. The A factor is I_hat.
In particular I -> I_hat is faithfully flat; no assertion that
I itself equals S is needed.

Let P also denote the residual projector acting on N_0 and on H. It
belongs to the compatible physical Hecke algebra. On e_A its reduction
is the identity, because A has the selected residual eigensystem.
Unique idempotent lifting gives e_A P=e_A. Consequently, for the
original localized coefficient module X=M tensor_{R_0} I, there is a
canonical identification

\[
 X\otimes_I I_{\rm hat}
       \simeq e_A(N_0\otimes_\Lambda S_{\rm hat}).          \tag{5}
\]

Indeed localization at A kills 1-e_0 and 1-P, and tensoring T with
S_hat splits it into the factors just described. Tensor associativity
then identifies its A factor on any T-module with the RHS of (5).
This works for arbitrary N_0; neither finite generation of N_0 nor
commutation of completion with its defining limits is claimed. In (5)
only the coefficient ring is completed, by an algebraic tensor product.

**3. Why W preserves this component.**
In the classical fiber H tensor_Lambda Q_p, the A eigensystem is
separated from every other constituent by good Hecke operators. To
check this without conflating new and old spaces, Jacquet--Langlands,
Eichler--Shimura and strong multiplicity one identify equal good-prime
eigenvalues with the same cuspidal representation as A. At every split
prime the level is exactly its conductor; the conductor newvector line
has dimension one. At the division primes the local transfer is the
one-dimensional character of the maximal-order-unit quotient. At p,
A has conductor exponent one, and its ordinary conductor vector is
unique. Hence there is only one A Hecke character at this level; its
homology constituent has dimension two over Q_p. There are no extra
refinements of A at a larger old level in this fiber.

There are finitely many other characters after extending scalars to
Qp-bar. For each choose a good prime distinguishing it from A. An
integer linear combination h of these finitely many T_l separates A
from all of them: the forbidden coefficient vectors lie in finitely
many proper hyperplanes, and an integer vector outside their union
exists (for example test vectors (1,k,...,k^{r-1}); each nonzero
polynomial has finitely many roots). Write a_A for h's value at A.
Then the characteristic polynomial of h on the classical fiber has
coprime factors (Z-a_A)^2 and g(Z), with g(a_A) nonzero.

Hensel factorization lifts these two factors to S_hat[Z]. Bezout's
identity for the lifted coprime factors and Cayley--Hamilton give a
polynomial E in h projecting onto the first factor. It is an
idempotent in B tensor_Lambda S_hat, commutes with W^vee because all
the good T_l do (L127), and reduces to the A projector. It equals e_A
as an operator on H tensor S_hat: it commutes with every Hecke factor;
on each finite free factor its reduction is zero or the identity,
and Nakayama applied to its image or the image of 1-E gives exactly
zero or the identity. Thus W^vee commutes with e_A.

These are identities in B tensor S_hat, not merely on one classical
fiber. Indeed B injects into End_Lambda(H), and flatness of S_hat over
Lambda preserves that injection. Step 1 therefore transfers them,
with order reversed, to N_0 tensor S_hat. This is the point that a
classical scalar comparison by itself would not establish.

**4. The scalar and its normalization.**
At every tame place, W_v induces the nontrivial automorphism of the
embedded quadratic algebra. Its square centralizes that algebra and
is fixed by its nontrivial automorphism, since W_v commutes with its
own square. Hence W_v^2 is central. Together with W_p=1, this proves
W^2=1 in the projective adelic group and on every Jacobian and H.

At q|n^+, L127 identifies its actual coset with the matrix used in
(1). Schmidt Theorem 3.2.2 applies to A's conductor line, giving
 epsilon_q. It covers both allowed exponents and q=2. At a good tame
prime W_v lies in the projective maximal compact group (L127), so
its action on the spherical vector is one.

At a division prime q, the conductor exponent is one. The local
Jacquet--Langlands transfer of St tensor chi_q is chi_q composed with
reduced norm, by Theorems 4.2/4.3(i). The embedded quadratic extension
is unramified. An element inducing its nontrivial automorphism has odd
reduced-norm valuation: an element of even valuation can be multiplied
by a central q-power to become a maximal-order unit, whose conjugation
acts trivially on the commutative residue field F_{q^2}; it cannot
induce the nontrivial Frobenius on the embedded unramified quadratic
residue field. Therefore chi_q(nrd(W_q))=chi_q(q)=eta_q. This argument
also works in residue characteristic two. The weight-two local Euler
factor identifies eta_q with a_q(A). No split-place minus sign is
inserted on the division side.

The tensor product of the local vectors has eigenvalue (1). Both
Eichler--Shimura copies have the same sign: the sign is rational and
real, and taking a dual or inverse preserves a sign. Thus the
reduction of W^vee on e_A(H tensor S_hat) is epsilon_W times the
identity. Since W^2=1 and 2 is a unit, the operator

\[
 Q=e_A(1-\epsilon_W W^\vee)/2
\]

is an idempotent on a finite free S_hat-module, with zero reduction
modulo t. Its image is finite and its reduction is zero, so Nakayama
gives Q=0. We have proved both equalities

\[
 W^\vee e_A=e_AW^\vee=\epsilon_W e_A.                     \tag{6}
\]

By Step 1 and flatness, the reversed equalities act on N_0 tensor
S_hat. Degree one supplies no degree multiplier. The auxiliary good
Hecke operator and its unchanged unit denominator in (22), p-level
pullbacks and normalized ordinary pushdowns all commute with W by
L127. In particular the maps U_p^{1-m}(pi_2)_*^{m-1} in Corollary
2.21 retain their original normalization. No new choice of CM list,
local coordinate, invariant domain or projection has been made.

**5. Comparison of the complete moments and descent.**
Under (5), the two elements in (2) map respectively to

\[
 e_A e_0 P W\widetilde J
   =e_A W e_0\widetilde J
   =\epsilon_W e_A e_0\widetilde J,
 \qquad
 e_A e_0 P\widetilde J=e_A e_0\widetilde J,
\]

each implicitly tensored with 1 over Lambda. The first equality uses
e_A P=e_A and W e_0=e_0 W, not commutation of W with P. Step (6)
provides the second equality. Faithful flatness of I -> I_hat now
gives (2) in X itself, including when X is not finitely generated.

Only now use the established complete-integral domain. Both sides of
(2) lie in X^D, identified with M^D tensor I by Lemma 4.12. Applying
the original linear map (63) yields B_W=epsilon_W B. The unique lift
to H^1(L_1,V), its trivial-character descent to K and localization
are the unchanged L123/L126 operations; their linearity gives (3).
Neither separated term of L127's defect formula was independently
fed to pr_A. L126's complete-list inversion is retained in the input
J_W=P W tilde-J, so equality of inverted raw measures is never used.

**Separate conceptual audit, step 534 (2026-10-28): first comparison
not established.** The issue is the sentence identifying the source's
controlled ordinary homology with the dual physical Tate-module action,
followed by the claim that commutativity gives the same labeled Hecke
algebra. Opposite multiplication and the identification of the operators
in a particular representation are different obligations.

Here is the finite-level naturality check. Write H_cov for the singular
homology of X_m with covariant actions of geometric correspondences,
and write V_m=T_p(J_m). Ignore only the scalar Tate twist when comparing
underlying Z_p-modules. For a diamond automorphism d of X_m, let a=d_*
be its covariant endomorphism on the Jacobian. On divisor classes,

\[
             d_*=(d^{-1})^*.
\]

Thus Kummer's identification of V_m with degree-one cohomology carries
a to (d^{-1})^*. Under the universal-coefficient evaluation pairing
between cohomology and H_cov, naturality says

\[
 \langle (d^{-1})^*\alpha,v\rangle
       =\langle\alpha,(d^{-1})_*v\rangle.
\]

Consequently a^vee, defined exactly as in Step 1 by precomposition on
the dual of V_m, corresponds to (d^{-1})_* on H_cov, not to d_*.
A Tate twist does not remove this inverse: these are geometric
endomorphisms acting trivially on the scalar twist. For correspondences
the same distinction is between a correspondence and its adjoint;
it is not eliminated because the algebra of the selected operators
is commutative.

This is visible before augmentation, which is where Step 1 needs its
relation test. The trivial finite-diamond projector removes only the
prime-to-p part. On the nonzero ordinary homology modules of the
retained tower, Corollary 2.15 and Lemma 2.22/Corollary 2.23 give a
nonzero free module over Z_p[Gamma_m]. Choose a level at which Gamma_m
has order greater than two and a generator gamma_m. The group-ring
elements gamma_m and gamma_m^{-1} are distinct, and their difference
does not act as zero on a nonzero free module: apply it to a basis
vector. Nonzero rank follows already from the conductor-level A
constituent. Thus the inverse cannot simply be suppressed on this
homology tower. This observation does not assert nontriviality of the
same difference on N_0 or on its A localization.

The source locations used in this check are Fornea v2, Section 2.1.2
and Definition 2.8 for the physical covariant convention; Remark 2.12,
printed pp.13--14, for Kummer and universal coefficients; and Section
2.4, Lemma 2.22/Corollary 2.23, printed pp.17--18, for the controlled
homology tower. Both the
[HTML](https://arxiv.org/html/2603.28327v2) and the
[PDF text](https://arxiv.org/pdf/2603.28327v2) were inspected, including
the latter's control diagram. The screenshot tool returned no visible
page and is not evidence. This is a check of the already assessed
inputs, not a new literature assessment or a reproof of Hida control.

There are two possible readings of Step 1, and neither supplies the
missing comparison as written. If H_m retains the covariant homology
operators, the natural duality above changes their labels. If its
operators are instead defined by transporting the dual physical
action, the proof must identify this transported ordinary summand,
Lambda action and tower with the one to which the imported control
theorems apply, including every bad-U label. Remark 2.12 gives the
underlying natural duality; it does not equate a covariant correspondence
with its adjoint. A simultaneous intertwiner or an explicit transport
of the control statements is not written in L128. Reversing words
alone does not provide it. This does not exclude such an intertwiner
or a covariant replacement of the relation test.

In particular, the assertion that a relation in B becomes the
corresponding reversed physical relation on the required ordinary
Tate summand is not yet justified for the original labeled H. Faithful
Tate-module detection is a valid subsequent input: Milne,
[*Abelian Varieties*, v2.0 (2008)](https://www.jmilne.org/math/CourseNotes/AV.pdf),
Chapter I, Theorem 10.15 and Lemma 10.16, printed pp.49--50, applies
to these characteristic-zero Jacobians. It detects a relation once
the correct Tate action has been identified; it does not identify
that action. Likewise the previously assessed completion and faithful
flatness theorems cannot repair a wrong or unestablished module action.

The bounded audit therefore withholds (2), (3), the asserted B^op
action on N_0, and the use of (5) for transferring the scalar. It stops
at this first comparison; it does not certify Steps 2--5 or their
normalized signs. It does not disprove (2), prove nonscalarity, or
invalidate L123, L126, L127 or the imported control theorems. L127's
abstract bad-U exchange is consistent with this finding and is not
being promoted to a physical or localized inequality. A repair must
retain the original R_0, I, CM list, maps and complete invariant domain.
No rationality, nonvanishing, local-finiteness or BSD assertion follows.

## Mathlib

Full completed-Hecke/coefficient comparison, Fornea construction,
local normalizer scalar and resulting complete-moment identity:
**not checked**. Supporting completion flatness, Hensel factorization,
Nakayama and newvector theorems: **not checked**. No absence claim or
formal verification is made. This is a proposed informal known-source
specialization held by the step-534 audit at Step 1's action comparison;
Step 2's identification (5) and the downstream scalar remain uncertified.
