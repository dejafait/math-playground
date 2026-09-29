# L036 — No CM action on an inherited direct sum gives an effective half twist

## Hypotheses

Let S have the very-general cubic-RM data of the
[family audit](../foundations/05-cubic-rm-family.md), or be an
NS-fixed RM deformation with the same full endomorphism field.
Write T=T(S), E=Q(zeta_7+zeta_7^(-1)), and assume
End_Hdg(T)=E, dim_Q T=18 and dim_E T=6. Its weight-two Hodge
numbers are (1,16,1). In particular E is totally real.

For any integer m>=1, give W=T^{oplus m} the inherited rational
Hodge structure and product polarization. Let K be any CM field
with a unital Q-algebra embedding

\[
\rho:K\hookrightarrow\operatorname{End}_{\rm Hdg}(W)=M_m(E).
\]

K need not contain E; rho may mix the copies of T. No compatibility
between rho and the adjoint for the product polarization is assumed.
For any CM type Sigma of K, use van Geemen's positive half-twist
convention. Effective weight one requires only types (1,0) and
(0,1) on the whole underlying rational space W.

## Conclusion

If such an action exists, m is even. For every such action and
every CM type,

\[
\dim_{\mathbb C}W_{\overline\Sigma}^{2,0}
 =\dim_{\mathbb C}W_{\Sigma}^{0,2}=m/2>0.             \tag{1}
\]

Hence no finite inherited direct sum admits an effective polarized
weight-one positive half twist under any allowed CM field action.
For odd m there is no allowed action at all. For even m the
forbidden top-piece dimension is exactly m/2 against zero required.

This closes the entire tested direct-sum recipe, including fields
not containing E and actions mixing copies. It does not exclude
different Hodge structures or nonlinear auxiliary constructions,
and it gives no nonalgebraicity result for U or any Hodge class.

## Proof

**Imported criterion and scope.** Reuse the unchanged prior
[SPECIALIZE assessment](../drafts/literature/2026-09-27-cubic-rm-direct-sum-cm-half-twists.md).
Van Geemen, *Half twists of Hodge structures of CM-type*,
[arXiv:math/0008076v1, sections 1.3--1.4, p. 2, and 2.5, p. 4](https://sites.unimi.it/vangeemen/0008076.pdf#page=2),
gives the positive half-twist rule

\[
(W_{1/2})^{p,q}
 =W_{\Sigma}^{p+1,q}\oplus
  W_{\overline\Sigma}^{p,q+1}.                       \tag{2}
\]

For an effective weight-two structure this is effective on all
of W exactly when W_overlineSigma^{2,0}=0. Its conjugate condition
is W_Sigma^{0,2}=0. This convention and the missing-piece warning
are also explicit in van Geemen--Izadi, *Half twists and the
cohomology of hypersurfaces*,
[arXiv:math/0008170v1, sections 1.3--1.5, pp. 3--4](https://sites.unimi.it/vangeemen/halfhyper.pdf#page=3).
Section 1.5 was reread on 2026-10-02; it agrees with the saved
assessment. These are supporting general statements, not a cited
evaluation of the arbitrary matrix actions in this lemma. Import
the criterion; only that evaluation is reproduced here.

**The action on the top piece has real matrices.** Choose a nonzero
omega in T^{2,0}. Every e in E acts by a scalar sigma_0(e) on
this line. The scalar action is a unital Q-algebra homomorphism
E -> C. Its kernel is a proper ideal in a field, hence zero.
Since E is totally real, sigma_0(E) is contained in R.

The copies of omega give W^{2,0} the basis omega_1,...,omega_m.
An entry e_ij in a Hodge endomorphism matrix is a map from copy j
of T to copy i. On these lines it acts by sigma_0(e_ij). Thus
for every k in K the restriction of rho(k) to W^{2,0} is

\[
A(k)=\sigma_0(\rho(k))\in M_m(\mathbb R),             \tag{3}
\]

where sigma_0 is applied entrywise. This description does not
require an inclusion E in K or a simultaneous diagonalization
of rho over E.

Define an antilinear involution on this one Hodge piece by

\[
J\left(\sum_j z_j\omega_j\right)
       =\sum_j\overline{z_j}\omega_j.                \tag{4}
\]

This is conjugation of the coefficients in the chosen basis;
it fixes the omega_j. It is not the conjugation of W_C that
interchanges Hodge types. Equation (3) proves
J A(k)=A(k) J for every k. This is a real form of the complex
K-representation on W^{2,0}; it is not an assertion that
W^{2,0} is a rational Hodge substructure.

**Conjugate embeddings have equal top-piece multiplicities.**
Since K is a number field, it is separable over Q and
K tensor_Q C is the product of C over all embeddings tau:K -> C.
Its idempotents decompose the representation as

\[
W^{2,0}=\bigoplus_{\tau:K\hookrightarrow\mathbb C}H_\tau,
\quad
H_\tau=\{v:A(k)v=\tau(k)v\text{ for every }k\in K\}. \tag{5}
\]

Some H_tau may be zero; no claim that every embedding occurs is
needed. If v is in H_tau, equations (3)--(4) give

\[
A(k)Jv=J(A(k)v)=\overline{\tau(k)}Jv.
\]

Thus J takes H_tau to H_bar_tau. Applying J twice proves this
is an antilinear bijection, so their complex dimensions agree.
Let d_tau denote that common multiplicity. A CM field has no
real embeddings, and Sigma selects exactly one member from
each conjugate pair. Consequently

\[
m=\dim_{\mathbb C}W^{2,0}
 =\sum_{\tau\in\Sigma}(d_\tau+d_{\bar\tau})
 =2\sum_{\tau\in\Sigma}d_{\bar\tau}.
\]

This proves both evenness of m and
dim_C W_overlineSigma^{2,0}=m/2, uniformly over every action
and CM type. The argument includes pairs of multiplicity zero.

**The bottom piece and effectivity.** The actual Hodge conjugation
of W_C commutes with every rational rho(k), and takes the
tau-eigenspace in W^{2,0} to the bar_tau-eigenspace in W^{0,2}.
It therefore takes W_overlineSigma^{2,0} to W_Sigma^{0,2}.
Their dimensions agree, completing (1). The imported criterion
now excludes effectivity, so no polarization construction can
give the effective weight-one structure required here.

Retaining all pieces in the formal rule (2) produces types
(2,-1) and (-1,2), each of dimension m/2. Restricting the rule
to nonnegative indices omits m complex dimensions from the
original dimension 18m. That restriction does not define the
requested half twist on W; deleting complex pieces supplies
neither a rational replacement nor an auxiliary abelian variety.

For m=2 and the multiplication action of E(i) on
T tensor_E E(i), the defect in (1) is one, agreeing with L035.
This is a consistency comparison: the present proof independently
treats arbitrary actions and does not use that special case.

This result is classified as REPRODUCTION. The half-twist
criterion is imported, and the equal-multiplicity argument for
real matrices is the required specialization. It gives a new
scoped negative conclusion in this notebook, without a claim
of progress beyond the checked literature or certified originality.

## Mathlib

Coverage of the full statement and supporting half-twist theory:
**not checked**. No declaration or absence claim is made. The
named van Geemen and van Geemen--Izadi sections support the
effectivity criterion; they are not a Mathlib match or a worked
instance of the all-multiplicity statement proved here.
