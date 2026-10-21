# L040 — Enlarged field excluded as a finite tensor component

## Hypotheses

Fix the exact field L=Q_3(zeta_20,pi), with zeta_20 of order 20 and
pi^27=3. Use L031's audited field data, in particular
v_3(L^times)=(1/27)Z with v_3(3)=1, and only L032's
“Torsion and the genuine all-unit logarithm” paragraph: L contains no
primitive third root. No presentation, logarithm basis or action is
assumed here.

Use **Dupuy–Hilado, arXiv:2004.13228v1 (28 April 2020)**,
**section 2.4.5**, printed p. 7, and **Definitions 3.6.1/3.6.3**,
pp. 11–13 ([versioned HTML](https://arxiv.org/html/2004.13228v1),
[versioned PDF](https://arxiv.org/pdf/2004.13228v1)). At p=3 take a
nonempty finite packet

    R = D_0 tensor_(Q_3) ... tensor_(Q_3) D_r,  r>=0,

where each D_i is an individual selected division-field completion in
that setup. In particular each is a finite extension of Q_3 and satisfies
L039's audited primitive-third-root conclusion. This conclusion uses
the full geometric 30-torsion prerequisite of Definition 5.3.1(3),
not the selected cyclic subgroup. The source role tested here is a
field factor C of the finite Q_3-algebra CRT decomposition of R.
It is not an arbitrary additive summand or an invariant subfield.

Import **William Stein, “Tensor Products”**, author-hosted HTML dated
2004-05-06, **section 18.2, Lemma 18.2.1 and equation (18.1)**
([primary theorem and proof](https://www.williamstein.org/papers/ant/html/node76.html)).
For fields A,B over k with B/k finite separable, the tensor A tensor_k B
is a finite product of fields, each with injective unital maps from A
and B. The ready assessment is
`drafts/literature/2026-10-10-enlarged-field-tensor-component-role.md`.
The CRT theorem and Weil pairing are imported, not reproved. Only the
finite multi-factor specialization and exact order transfer are checked.

## Conclusion

Every nonzero CRT field component C of R contains an element of exact
order three. Consequently no such C is isomorphic as a Q_3-field to L.
This excludes the exact enlarged finite-component realization in the
specified exposition, independently of any radius or action calculation.

This is a known-theorem application (REPRODUCTION), with no claim of
progress beyond the sources checked. It does not exclude native IUT
objects, invariant subfields, additive summands or algebraic-closure
variants, and does not demonstrate an essential IUT flaw or a failure
of original finite B>=A. The separate critical audit below confirms
only this stated exclusion.

## Proof

All D_i/Q_3 are finite separable because Q_3 has characteristic zero.
For r=0 the packet is the field D_0. Inductively suppose the tensor of
D_0,...,D_(j-1) is a finite product of finite extensions C_t/Q_3.
Finite-product tensor distribution gives

    (product_t C_t) tensor_(Q_3) D_j
        isomorphic to product_t (C_t tensor_(Q_3) D_j).

Here distribution uses a finite product only: its underlying vector
space is the finite direct sum of the C_t; tensoring the coordinate
projections and inclusions gives mutually inverse linear maps.
The coordinate map sends (c_t)_t tensor d to (c_t tensor d)_t,
respects multiplication and sends 1 to 1, hence is an algebra
isomorphism. Stein's lemma applies to each C_t,D_j over Q_3.
Every resulting field remains finite over Q_3, since the tensor algebra
is finite dimensional. This completes the induction without any
linear-disjointness assumption or a new CRT proof.

Now fix any nonzero field component C and its unital projection
pr_C:R -> C. For each i let u_i:D_i -> R send x to the pure tensor
whose ith factor is x and whose other factors are 1. The map u_i is
a unital Q_3-algebra homomorphism by the tensor multiplication rule.
Thus phi_i=pr_C composed with u_i is a unital field homomorphism
D_i -> C. Its kernel is an ideal of D_i. Since phi_i(1)=1_C!=0,
that ideal is proper and therefore zero. In particular, although
pr_C may have a kernel on R, its restriction along u_i is injective.
This verifies the factor maps for every component, not only a chosen
component obtained in the induction.

By L039's audited full-torsion application, choose rho_i in D_i with
rho_i^3=1 and rho_i!=1. Multiplicativity gives phi_i(rho_i)^3=1_C.
Injectivity gives phi_i(rho_i)-1_C=phi_i(rho_i-1)!=0. Since 3 is prime,
phi_i(rho_i) has exact order three. No equality between roots arriving
from distinct factors is needed; any single factor suffices.

If C were Q_3-isomorphic to L, that isomorphism would preserve the
cube equation and inequality with 1, giving a primitive third root
in L. This contradicts the specified paragraph of L032, using L031's
value group rather than the total degree 108. This proves the exclusion.

Section 2.4.5's normalization of the tensor integer ring does not
replace its ambient field components by invariant subfields. The proof
uses only those ambient finite algebra components, with their unital
projections; reduction to residue fields and nonunital additive
projections would not satisfy this test. Actual/native input and action,
global data, pilot transport, essentiality and the original numerical
comparison remain unestablished. L038's auxiliary radius is not an input.

### Separate critical audit, 2026-10-10

Verdict: the finite-component exclusion passes under exactly the stated
hypotheses. Reuse the separately approved coverage in
`drafts/literature/2026-10-10-enlarged-tensor-component-critical-audit.md`.
This is an audit of the existing specialization, with no fresh source
access, stronger conclusion or mathematical correction claimed.

The source objects are finite tensors over Q_3 of selected completions,
and the tested components are nonzero fields in their algebra CRT
decomposition. Stein's Lemma 18.2.1 applies at each induction step:
both arguments are fields over Q_3, and the new factor D_j is finite
separable in characteristic zero. The finite dimensionality of the
tensor implies finite dimensionality of each quotient component, so
the induction retains finite extensions. It does not assert the whole
tensor is a field or assume linear disjointness.

For completeness, the distribution map's inverse as a linear map is
obtained by summing the coordinate inclusions tensored with id_(D_j).
Indeed projections followed by inclusions sum to the identity on the
finite direct sum, while projection onto a different coordinate gives
zero. These two identities check both composites on pure tensors,
which span the tensor product. Coordinate inclusions need not be
unital: only their linear properties are used in this inverse.
The displayed forward map respects products on pure tensors and sends
1 tensor 1 to the tuple of units. By bilinearity and its bijectivity
it is the claimed algebra isomorphism. Finite product, rather than an
infinite-product interchange, is essential here.

For r=0 no induction or tensor distribution is needed: R=D_0, with
its single field component. In every case, including repeated factors,
the map u_i sends 1_(D_i) to 1_R, and pr_C sends 1_R to 1_C!=0.
Thus pr_C composed with u_i has proper kernel in the field D_i and
is injective. This argument checks every component directly; a kernel
of pr_C on the product algebra is harmless. Nonunital additive
projections would not meet these hypotheses. Nonemptiness supplies
at least one i; the zero-factor tensor Q_3 is not an admitted packet.

L039's audited application of Silverman III.8.1.1 supplies an element
rho_i of exact order three in each D_i. Its proof uses full rational
geometric 30-torsion over the number field, not residue-field torsion.
The field map preserves rho_i^3=1 and rho_i-1!=0, so its image has
order three, rather than merely order dividing three. Different
factors need not give the same primitive root. A Q_3-field isomorphism
C -> L is also unital and injective and preserves these two statements.
L031's valuation range is (1/27)Z, whereas L032's specified paragraph,
using Clark Proposition 2.9/Corollary 2.10, forces valuation 1/2 for
zeta_3-1. Since 2k=27 has no integral solution, this is a contradiction.
Neither total degree 108 nor reduction modulo 3 is used for that step.

Normalization of the tensor integer ring does not change the ambient
field-component role under audit. No claim about an invariant subfield,
an additive summand, a closure-field construction or native IUT follows.
L031, the torsion paragraph of L032 and L039 remain the direct local
inputs; no action, logarithm basis or L038 radius is used. The audit
accepts the pending local route stop without establishing actual input/
action, global data, pilot transport, essentiality or finite B>=A.
Full matching and supporting Mathlib coverage remains not checked.

## Mathlib

Full matching source-role exclusion: **not checked**. Supporting finite-
separable tensor decomposition, unital field-map injectivity and root-
order preservation: **not checked**. Unknown coverage is not evidence
of absence. The result specializes the cited standard algebra and
L039's audited known-result application, without a novelty claim.
