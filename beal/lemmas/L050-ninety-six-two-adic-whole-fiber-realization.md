# L050 — A primitive two-adic realization of the entire 96a1 fiber

## Hypotheses

Let E0 be the smooth projective modular curve X0(11), with its degree-twelve modular map j:E0 -> P1 as in the structural part of L034. Set k=Q2 and let B_s be the coordinate algebra of the entire scheme-theoretic fiber over a finite scalar s in k outside {0,1728}. No original integer solution or 54a1 hypothesis of L034 is assumed.

Let E96 be the rational elliptic curve with source label 96a1. Define

    m96(U)=U^12-4U^11-264U^7+66U^6-132U^5-2112U^4
           -1320U^3-660U^2-6240U-8007,
    K96=Q[U]/(m96),     A96=K96 tensor_Q k.

The field and fiber identification is imported from Freitas–Naskręcki–Stoll (FNS), *The generalized Fermat equation with exponents 2, 3, n*, **Compositio Mathematica 156 (2020), 77–113**, [DOI](https://doi.org/10.1112/S0010437X19007693), [final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf), internally June 10, 2019: Section 7.2, printed pp.25–27, canonical fiber paragraph and Table 5. The canonical fiber at j(E96) is the degree-twelve field K96, with geometric points indexed by all cyclic order-eleven subgroups of E96[11]. The polynomial generator is not assumed to be the modular x-coordinate. The adjacent GRH-dependent Selmer dimensions and eliminations are not inputs.

Use FNS Lemma 5.2, printed pp.18–19, with Table 1, printed p.9, and the Hensel–Newton theorem in foundation 17: Clark, *Algebraic Number Theory II*, [author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf), Theorem 1.79, printed p.58. The former compares the full local torsion modules up to an unramified quadratic twist; it is not just an inertia statement. These named results are imported without reproof or rerunning their source computations.

## Conclusion

There are common nonzero a,b,c in Z2 and an isomorphism of entire k-algebras B_1536 -> A96 such that

    a=2,  b=1,  c^11=9,
    a^3+b^4=c^11,     1536*c^11=1728*a^3,
    min(v2(a),v2(b),v2(c))=0,
    a=2 modulo 8,     b,c odd,
    1536 in -512+2048 Z2.

Thus the exact local feasibility question in the saved assessment has a positive answer. Local nonexistence under these conditions cannot exclude 96a1. No connecting image, global class intersection, integer solution or signature exclusion follows. The independent critical application audit below confirms this conclusion without mathematical correction.

## Proof

### One common witness and both scalar identities

In the complete field Q2 apply Clark Theorem 1.79 to h(V)=V^11-9 in Z2[V], at V=1. Here h(1)=-8 has valuation three, whereas h'(1)=11 has valuation zero. Thus

    v2(h(1))=3 > 2*v2(h'(1))=0.

Hensel gives an exact c in Z2 with c^11=9 and |c-1|2<1. Hence c is odd and nonzero. Fix a=2 and b=1. They are integral and nonzero, with valuations (1,0,0) for (a,b,c), and a=2 modulo 8. In particular b^4=1 is constructed explicitly; no fourth-root surjectivity at two is assumed.

The same c satisfies

    a^3+b^4=8+1=9=c^11,
    s=1728*a^3/c^11=1728*8/9=1536,
    s*c^11=1536*9=13824=1728*8.

The complementary identity also holds: (1728-s)c^11=192*9=1728*b^4. Finally s=-512+2048, so s is in the retained L032 disk and differs from 0 and 1728. These are exact identities, not approximations to a root.

### The full local torsion comparison applies

Use source square/cube coordinates (X,Y)=(b^2,a)=(1,2), which are coprime ordinary integers. Their Frey curve is

    F: v^2=u^3+3Yu-2X=u^3+6u-2.

Its discriminant is -16(4*6^3+27*(-2)^2)=-1728*9, which is nonzero, and its j-invariant is 1728*8/9=s. The local c constructed above makes X^2+Y^3=c^11. The curve itself depends only on the integer pair X,Y, so there is no need to extend a theorem about integer pairs by a continuity assertion.

Specifically, X=1 modulo 4 and Y=2 modulo 8 place this pair in Table 1's i2=5 row. Choose its allowed twist d=6, also the d retained by L032's 96a1 branch. The nonzero squares modulo 11 are {1,3,4,5,9}, so (2/11)=-1 and 11>=3. FNS Lemma 5.2 therefore supplies a full G_k-module isomorphism, symplectic up to the stated qualification,

    F^(6)[11] isomorphic to E96[11] tensor chi,

where chi is either trivial or the unramified quadratic character allowed in that lemma. Its proof explicitly extends the inertia comparison to the full local group before introducing this ambiguity. We import that conclusion, not a new extension of inertia representations. The lemma's second assertion assumes coprime integer X,Y in the indicated row; our pair meets that assertion literally, and the local right-hand witness is already supplied.

For a quadratic twist in characteristic different from two, the standard torsion identification over a separable closure changes the Galois action by the twisting character: F^(6)[11] identifies with F[11] tensor chi_6. This is the quadratic-twist convention used by FNS. Consequently F[11] and E96[11] differ, after a linear isomorphism, by the scalar character psi=chi*chi_6. There is no assertion that psi is unramified: chi_6 need not be. Scalar twisting is all that is needed below.

### All twelve subgroups, hence the entire algebra

For any two-dimensional F11-space V, write P(V) for its set of one-dimensional subspaces. It has (11^2-1)/(11-1)=12 elements, exactly the cyclic subgroups of order eleven. If a representation rho is replaced by psi*rho for a scalar character psi, then for every sigma in G_k and line L,

    (psi(sigma)*rho(sigma))(L)=rho(sigma)(L),

since multiplication by a nonzero scalar preserves each line. The preceding module isomorphism therefore induces a G_k-equivariant bijection

    P(F[11]) -> P(E96[11]).

This verifies the quadratic-twist ambiguity directly for every subgroup. It neither removes an unramified character by fiat nor uses only inertia or one selected factor. The Weil-pairing sign is consistent with the retained row, but a subgroup-set bijection itself does not require choosing a pairing normalization.

The modular interpretation of the complete map, used in FNS Section 7.2, identifies the geometric points of the fiber at j(F)=s with P(F[11]). Because s is not 0,1728 or infinity, F has only the generic automorphisms ±1 over the algebraic closure, and these preserve each subgroup. The fiber is finite etale of degree twelve, with the stated Galois action. This is the projective fiber, so no affine coordinate denominator or reconstruction chart deletes a point.

By the cited canonical identification, the geometric points of Spec(K96) are P(E96[11]) as a G_Q-set. Base change to k restricts this action to G_k and gives Spec(A96). Both Spec(B_s) and Spec(A96) are thus finite etale k-schemes with equivariantly bijective twelve-point sets.

Import the standard finite-etale/Galois-set equivalence, [Stacks Project, Lemma 58.2.2, tag 03QR](https://stacks.math.columbia.edu/tag/03QR), in Section 58.2 (tag 04JI). Its hypotheses are a field and its separable closure; take k=Q2 and an algebraic closure, since characteristic zero is perfect. Restricting the equivalence to finite sets identifies the two finite etale schemes. On coordinate algebras it gives an isomorphism B_s -> A96 (taking its inverse if necessary). Every orbit corresponds to its actual finite separable field; all twelve points and all their orbits are retained, including repeated isomorphic factors. There is no need to guess local ramified fields from their degree or residue invariants. This proves the entire-algebra conclusion.

### Scope and route decision

The specialization uses L032 only for its row and required local conditions, and L034 only for the complete modular-map interface. L033's 54a1 field is not an input. No three-adic or positivity condition is imposed on a Q2 witness, and no global modular reduction is proved by this local argument.

This is REPRODUCTION under the prior SPECIALIZE assessment: the local torsion comparison, canonical field and general lifting theorem are known inputs; the common fourth-power witness and scalar/Galois-set applicability are the bounded specialization. No claim of progress beyond the sources checked is made. The positive realization meets the stopping test and retires this local nonexistence target, not local arithmetic on all twists. Since 1<9<2^11, c is not an integer, so the construction is not an integer counterexample. Global 54a1 intersections, L045's quotient classes, other twists and infinitely many residual signatures remain open. STATUS stays IN_PROGRESS.

### Independent critical application audit — 2026-10-10

This audit uses the previously approved SPECIALIZE scope in
`drafts/literature/2026-10-10-ninety-six-realization-critical-audit.md`.
It tests the existing proof rather than constructing a second realization.
The result is confirmation, not a new mathematical restriction. The precise
source statements cited above are imported; their general proofs and
published computations are not independently reproduced.

**Simultaneous witnesses.** For the normalized valuation v2(2)=1,
h(1)=-8 and h'(1)=11 give 3>0, the strict Hensel inequality.
The complete field, integral coefficients and integral approximation meet
Clark Theorem 1.79. Its root is integral and differs from 1 by an element
of 2Z2, hence is a nonzero unit. Fixing that root once gives valuations
(1,0,0) and both exact products 1536*9=1728*8=13824 and
192*9=1728. Thus neither identity uses a separately chosen c.
The equality 1536+512=2048 verifies the disk, and the explicitly chosen
b=1 supplies the fourth power. No root extraction for arbitrary fourth
powers at two occurs. L032 is used for its two-adic row only: its
three-adic and positive-integer conditions are not conclusions about this
Q2 witness. In particular this does not assert an integer solution with
a unit base.

**Literal source applicability.** The source pair is the ordinary
coprime integer pair (X,Y)=(1,2), distinct from (a,b)=(2,1) in this lemma.
Direct computation gives 4*6^3+27*(-2)^2=972,
Delta(F)=-16*972=-15552=-1728*9 and
j(F)=1728*864/972=1536. The curve is smooth. Source Table 1,
printed p.9, permits d=6 in row i2=5. At p=11, the complete nonzero
square set is {1,3,4,5,9}, so 2 is a nonsquare. The literal second
clause of FNS Lemma 5.2, printed pp.18–19, concerns coprime integer
pairs in that row, not the existence of an integer eleventh root.
Its full proof and subsequent qualification were rechecked: the claimed
comparison is for the whole local group, with an unramified quadratic
ambiguity that can be necessary for Frey curves. That ambiguity is
retained. No invocation of the global level-lowering assertion is needed.

**Twist and moduli transport.** An isomorphism over the separable closure
between a quadratic twist and F has descent cocycle in {+1,-1}.
On 11-torsion this cocycle acts by scalar multiplication, so composing
the twist identification with the source module isomorphism changes
the action only by the product character psi. Its ramification is
irrelevant for lines: if theta intertwines the two representations up
to psi, then theta(rho_F(sigma)L)=rho_96(sigma)theta(L) for every line L,
since psi(sigma) is nonzero. This proves equivariance for every sigma,
not only inertia. There are exactly 12 lines. Pairing normalization
cannot change this line-set calculation.

The map L -> [(F,L)] identifies these lines with the geometric modular
fiber: since j(F) is neither 0 nor 1728, the only automorphisms of F
are ±1, which fix each subgroup. For sigma in G_k, the curve F is
defined over k, so this assignment sends sigma L to sigma[(F,L)].
The identification is therefore G_k-equivariant, including its descent
action, rather than just a count of geometric points. The finite map
has degree 12 and is unramified away from 0,1728,infinity by the cited
complete modular-map interface. The scalar 1536 is distinct from all
three in Q2. Its reduction modulo two being zero does not make this
generic-field fiber a branch fiber. Hence B_1536 is finite etale of
dimension 12; no assertion of etaleness over Z2 is required.

**Entire target algebra.** Every coefficient of m96 was compared with
FNS Table 5, printed p.27, including its zero coefficients in degrees
10,9,8 and its constant -8007. Section 7.2, printed p.25, supplies the
canonical degree-twelve fiber identification. Thus base change restricts
that same twelve-point G_Q-set to G_k; it does not select a local factor.
K96 is a characteristic-zero number field, so its base change is finite
etale. Applying Stacks Lemma 58.2.2 to the verified bijection gives a
scheme isomorphism. Contravariance gives the asserted algebra direction
by inverting if needed. The orbit/stabilizer description preserves every
factor, including multiple isomorphic factors. No polynomial-factor or
ramification-invariant matching is substituted for this equivalence.

All load-bearing interfaces pass. Only the Stacks locator was clarified:
03QR is the lemma tag and 04JI the section tag. No hypothesis, conclusion,
mathematical argument or direct lemma input changes. The local stop is
confirmed, while the connecting image and every global emptiness claim
remain outside the conclusion. This canonical audit supersedes the
overview's pending-review wording for L050.

## Mathlib

Full matching 96a1/common-fourth-power/entire-two-adic-fiber realization: **not checked**. Supporting local torsion comparisons, modular-fiber interpretation, quadratic-twist action, Hensel and finite-etale/Galois-set equivalence: **not checked**. Unknown availability is not evidence of absence. Precise primary citations above support this informal specialization; the independent application audit is recorded above.
