# L084 — The combined primitive supported space has codimension at least three

## Hypotheses

Use L033's entire degree-twelve field K and curve

    E0: y²+y=x³−x²−10x−20,
    g(X)=X³−4X²−160X−1264,     D=K[θ]=K[X]/(g).

Use precisely L074–L076's support S_F consisting of ALL maximal-ring
primes above two and eleven in F=K,D, their rings R_F=O_F[1/22], and
their supported norm-square spaces W_S and V_S. Put

    k_S=dim_F2 ker(n_S),
    n_S:Cl(R_D)[2] -> Cl(R_K)[2].

Thus dim W_S=16+k_S and dim V_S=16. No value of k_S is assumed.
All square-class groups below are written multiplicatively but regarded
as vector spaces over F2; their identity is denoted 1.

Fix the rational dyadic place v_2 and the two rational eleven-adic
places v_11,1 and v_11,2 of L077. For any of these places let

    G_v=(D tensor_K K_v)*/(D tensor_K K_v)*²,
    H_v=δ₂,v(E0(K_v)) subset G_v.

Use the entire cubic algebras, including both factors at each rational
eleven-adic place, and the same distinguished θ. Let

    R:W_S -> (G_v2/H_v2) × (G_v11,1/H_v11,1)
                              × (G_v11,2/H_v11,2)

be localization followed by these full-image quotient maps, and put
U=ker R. For the ENTIRE dyadic base algebra use L082's fixed

    K tensor_Q Q2=Q2 × H,     H=Q2(π), π^11=2,
    C=Q2[θ],     J=H[θ],
    G_2=(C*/C*²) × (J*/J*²),
    I_prim={(1,1),(1,ξ)},
    ξ=[64+4π^5+4π^10−θ] in J*/J*².

Let loc_2:W_S -> G_2 be localization at both dyadic places together.
Retain L062's fixed σ and point P_σ, and L083's
β_σ=δ₂(P_σ); this is not the five-isogeny class of L062.

## Conclusion

The exact intersection of the stated four conditions,

    T=U intersect loc_2^(-1)(I_prim),

is an F2-subspace of W_S. Its quotient has at least three independent
classes, represented by L077's v,w and β_σ. Consequently

    codim_W_S(T)>=3,       dim T<=13+k_S.

More specifically codim_U(T)>=1, whereas codim_W_S(U)>=2.
The space U contains the full global two-descent image; T contains the
two-descent classes of transported positive primitive integer solutions
in the 54a1 branch of L033. But β_σ belongs to U and not T, so T does
NOT contain the full global point image. No Mordell–Weil rank bound
is asserted. This assembly does not improve the supported-unit upper
bound fourteen to eleven or determine k_S. It excludes no branch.

## Proof

### Imported interfaces and scope

The pre-existing SPECIALIZE assessment is
`drafts/literature/2026-10-17-combined-primitive-supported-codimension.md`.
The canonical local arithmetic and support results are reused without
new enumeration or reproof. The general Kummer interface is Barrera
Salazar–Pacetti–Tornaría, *On 2-Selmer groups and quadratic twists of
elliptic curves*, [arXiv:2001.02263v3, 17 September 2020](https://arxiv.org/pdf/2001.02263v3),
Section 1, printed p.3: the multiplication-by-two Kummer injection
and its norm-square algebra realization over a field of characteristic
different from two, for a monic square-free cubic. Its affine formula
is X−θ where invertible. Here all fields have characteristic zero,
g is monic with discriminant −256·11^5 nonzero, and the SAME
origin-preserving model change is X=4x, Y=8y+4. In particular this
is a group map over K and each completion, with the prescribed θ.
Polynomial evaluation commutes with localization. At O both evaluations
are 1, and at any local two-torsion exception naturality follows from
the connecting map itself, rather than evaluating a zero component.

Simon, *Computing the rank of elliptic curves over number fields*,
LMS J. Comput. Math. **5** (2002), 7–17,
[DOI](https://doi.org/10.1112/S1461157000000668), Propositions 1.1–1.4,
printed pp.8–9, is imported in L075 for the full supported containment,
including coordinate denominators. The localization/intersection method
is also described by Bruin–Stoll, *Two-cover descent on hyperelliptic
curves*, Math. Comp. **78** (2009), 2347–2370,
[14 March 2008 author manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
Section 6, printed pp.11–12, algorithm steps 7–17 and explanation.
These sources supply the interfaces, not this specialized rank-three
test. Only standard first isomorphism and rank–nullity theorems are
needed in addition to the canonical inputs below. No general restricted
point image is assumed to be a subgroup.

### Well-defined quotients and the two containing spaces

L074 embeds V_S in W_S as field square classes. Localization of an
invertible element of D is invertible in every field factor, and a
square localizes to a square. Thus all the localization maps used
above are well-defined homomorphisms on W_S. Each H_v is a subgroup
because δ₂,v is a group homomorphism. L082 proves ξ nontrivial and
gives the exact two displayed classes of I_prim. Square-class groups
have exponent two, so that particular set contains the identity and
is closed under products and inverses: it is an order-two subgroup.
This justifies the quotient G_2/I_prim, independently of any assumed
closure property of primitive points themselves.

Define the homomorphism

    τ:W_S -> G_2/I_prim,     τ(a)=loc_2(a) I_prim,
    Q=(R,τ).

Then T=ker Q. Both U and T are therefore linear subspaces. The
rational projection of loc_2 is exactly the map at v_2 in R,
with the same C and θ; it is not another embedding. In particular
I_prim has trivial rational projection, so the primitive condition
already implies that one full-local condition. We retain it in R
as prescribed but do not count the number of tests as their rank.

L075 puts δ₂(E0(K)) in W_S. Naturality of the same Kummer map
puts its localization in H_v at each of the three places. Hence
δ₂(E0(K)) is contained in U. In particular L062's actual global
point P_σ gives β_σ in W_S with R(β_σ)=0. This uses neither
S-unit membership of β_σ nor information about its ideal class.

For a hypothetical positive primitive integer solution in L033's
54a1 branch, that lemma's transported degree-twelve point P has
j(P)=1728 A³/C^11, B odd, C even and A=7 modulo eight.
The integers give one common nonzero primitive triple over Z2.
The point has degree twelve and lies in the whole degree-twelve
fiber, so its evaluation identifies that fiber algebra with K.
Tensoring this identification with Q2 gives exactly a whole-fiber
isomorphism into L082's fixed Q2 × H. L082 therefore puts
loc_2(δ₂(P)) in I_prim. Together with the preceding full-local
memberships this gives δ₂(P) in T. There is no inference in the
reverse direction: a T-class need not lift to an integer solution.

### The three witnesses and the rank test

L077 proves that v=−1/t and w=2−t−6t² belong to V_S inside W_S,
where t³−t²+t+1=0 and θ=8−14t+6t², and that on their span R
has the following quotient-image coordinates:

    rational dyadic:       1 1
    first rational 11:    0 1
    second rational 11:   0 1.

The coordinates here identify the one-dimensional images of THIS
family, not each entire local quotient with F2. In particular R(v)
and R(w) are independent, since the first two rows have determinant
one. The duplicate eleven-adic row creates no extra direction.

L083 uses the same fixed P_σ and θ and proves
loc_2(β_σ) not in I_prim. Thus τ(β_σ) is nonzero, while we have
already proved R(β_σ)=0. To check independence without computing
τ(v) or τ(w), suppose for a,b,c in F2 that

    Q(v)^a Q(w)^b Q(β_σ)^c=1.

Projecting to the R factors gives R(v)^a R(w)^b=1. The matrix
forces a=b=0. The remaining relation τ(β_σ)^c=1 forces c=0.
Therefore Q(v), Q(w), Q(β_σ) are three independent vectors.
By the first isomorphism theorem W_S/T is isomorphic to im Q,
so its dimension is at least three. Also β_σ in U\T proves
codim_U(T)>=1, while L077's two witnesses prove
codim_W_S(U)>=2. Rank–nullity and L076's finite dimension give
dim T<=16+k_S−3=13+k_S, as claimed.

### Meaning, verification and limitations

This is a REPRODUCTION of assessed localization and linear-algebra
methods with existing field-specific witnesses. It adds a local
notebook bound, with no claim of a new general theorem beyond the
sources checked. The complete witness calculation is the preceding
relation argument; no mathematical script or numerical sample is
needed. The achieved quotient rank is at least THREE, meeting the
approved intermediate threshold three. It is not asserted to be
exactly three. The bound 13+k_S still exceeds eleven even at k_S=0.

In particular β_σ is deliberately used in W_S, not asserted in V_S.
The third direction could involve the class contribution; the argument
does not establish a third removed unit direction. On T intersect V_S
the already certified bound remains at most fourteen. The class norm
kernel is uncomputed. A filter that removes β_σ cannot bound the full
Mordell–Weil image or justify an elliptic Chabauty rank hypothesis.
Other candidate point classes, global primitive power lifting, the
other modular twists and the full Beal target remain unresolved.
L062/L065's distinct five-isogeny survivor is untouched. No exhausted
unit search or parked class backend in ATTEMPTS/034–037 is reopened.
The separate critical application review below confirms this assembly;
no complete candidate resolution is proposed.

### Independent critical application audit — 2026-10-17

**Verdict: confirmed without correction.** The pre-existing SPECIALIZE
assessment `drafts/literature/2026-10-17-combined-primitive-codimension-audit.md`
covers exactly this audit. The canonical L033, L062, L074–L077,
L082 and L083 statements and relevant proofs, including their separate
critical audits, were checked at the interfaces used here. This review
reuses their local arithmetic; it does not claim a fresh replay of
their certificates or a new general descent theorem.

**Same spaces and quotient maps.** Here D always means the cubic
extension K[theta], not the canonical fiber algebra also called D in
L062. The latter is used only to define P_sigma. The support is all
primes over two and eleven in the maximal rings. L074's field-square
injection identifies V_S with a subspace of W_S, and L076's audited
dimension formula applies to precisely these spaces. No support above
five from the different five-isogeny map enters this definition.

Tensoring D=K[X]/(g) at each selected base place gives the entire
cubic algebra, with X mapping to the same theta. In particular its
rational dyadic factor is the C used by L077 and L082, and its other
dyadic factor is J, not a selected subfactor. Localization takes any
nonzero field element and any field square to units and squares in
every factor. Thus it induces the displayed maps on W_S, without
requiring its classes to be S-units. BPT Section 1's general-field
Kummer map makes every H_v a subgroup; its characteristic and
square-free hypotheses hold for this monic g. The model change fixes
the origin and transports multiplication by two, so the maps used by
L075, L077, L082 and L083 agree. Exceptional local torsion values
are those of the connecting map, not zero-valued affine expressions.

L082 proves the exact set I_prim={1,(1,xi)} and xi nontrivial in
this same J. In an exponent-two group the product of its nonidentity
element with itself is identity. Hence I_prim is indeed a subgroup
and tau is a linear quotient map. This verifies T=ker(R,tau) and
T subset U. The rational projection of I_prim is identity, hence in
H_v2; its condition implies the rational dyadic condition already
present in R. This redundancy is real but does not affect the
witness argument below.

**Supported witnesses and the full relation.** L077's norm and
integrality argument puts v,w in this V_S: their norms are 1 and
121, squares of S_K-units. Its two independent quotient coordinates
are (a+b,b) on v^a w^b. Those coordinates refer to the images of
this two-dimensional family; there is no assumption that a whole
local quotient is one-dimensional. The two rational eleven-adic
rows agree on the family and are counted only once.

L062 fixes an actual K-point P_sigma independently of any primitive
integer solution. L075 therefore gives beta_sigma in W_S. Kummer
naturality, with the same theta in every completion, places its image
in each full H_v, so R(beta_sigma)=0. L083's audited exclusion uses
exactly the localization of that fixed point and proves
tau(beta_sigma) nonzero. It does not merely reject its scalar.
If v^a w^b beta_sigma^c lies in T, applying R first forces
(a+b,b)=(0,0), whence a=b=0. Applying tau then forces c=0.
This proves independence in W_S/T of all three displayed classes,
even though tau(v) and tau(w) have not been calculated. In particular
beta_sigma in U outside T gives the strict additional condition on
U; counting four quotient factors was never the rank argument.

**Containment of transported primitive points.** The unconditional
FNS Section 7.2 transport used in L033 supplies P in E0(K) of degree
twelve over Q, with the same modular scalar s=1728 A^3/C^11.
For the hypothetical positive solution, 0<s<1728, so it is finite
and avoids the branch values. Write B_s for the coordinate algebra
of the entire modular fiber. The degree-twelve modular map gives
dim_Q B_s=12, as in the L082 interface. Evaluation at P gives a
Q-algebra map B_s -> K. Its image is the residue field Q(P): P
defines a closed point of the finite fiber, and quotient by its
maximal ideal has precisely that field. Since [Q(P):Q]=12=[K:Q],
the image is K. Equality of dimensions makes evaluation an
isomorphism. This argument uses the entire fiber, not only one
chosen completion or a necessary elimination polynomial.

By Stacks Lemma 26.17.2, Tag 01JQ, affine base change is tensor
product, so tensoring this evaluation with Q2 gives an isomorphism
B_s tensor_Q Q2 -> K tensor_Q Q2. Its tautological point is the
localization of P. The SAME integer triple A,B,C is nonzero in Z2,
satisfies both scalar and power identities, and has minimum valuation
zero: otherwise two would divide their common gcd. L033's retained
row gives B odd, C even and A=7 modulo eight. These are every
primitive hypothesis in L082. Its theorem quantifies over every
whole-fiber isomorphism, so the evaluation identification is included;
it need not be the canonical sigma used for the different point
P_sigma. Consequently loc_2(delta_2(P)) belongs to I_prim.
L075 and naturality also put delta_2(P) in U, establishing containment
in T without choosing local witnesses independently at different factors.

**Bound and limits.** The first isomorphism theorem identifies W_S/T
with the image of (R,tau), of dimension at least three by the complete
relation test. L076 gives dim W_S=16+k_S, so dim T<=13+k_S.
This confirms the claimed intermediate threshold, not an improvement
of it. Neither beta_sigma in V_S nor any value of k_S was used.
The supported-unit upper bound therefore remains fourteen. Even
k_S=0 leaves 13>11, and excluding the actual global point class
beta_sigma means T cannot bound the full Mordell–Weil image.
Primitive integer emptiness, other point classes and modular twists
remain unresolved; the five-isogeny survivor is unaffected.

This is REPRODUCTION: independent verification of the local notebook
assembly using assessed known methods, not progress beyond the cited
general results. No mathematical script is needed for this relation
and interface audit. The eight direct DAG inputs remain exactly those
already listed; no new dependency, corrected argument or complete
Beal candidate results from the review.

## Mathlib

The full matching combined primitive supported-space bound and its
field-specific witnesses: **not checked**. Supporting square-class
quotients, Kummer localization, subspace intersections, first
isomorphism and finite-dimensional rank–nullity coverage: **not
checked**. Unknown coverage is not evidence of absence. No Lean
verification is claimed.
