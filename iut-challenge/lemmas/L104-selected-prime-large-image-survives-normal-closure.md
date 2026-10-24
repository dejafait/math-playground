# L104 — Conditional selected-prime large image survives normal closure

## Hypotheses

Fix one same-member/order/prime choice from L101, retaining L089's
fixed family, domains and algebraic closure through L090. In that
closure put

    F=G_o=Q(t_o)(iota,E_o[15]),
    E_o: V^2=X(X-1)(X-t_o), C=C_o=G_o^nor over Q.

All division fields use both coordinates of every geometric torsion
point. L090 identifies the actual normal closure and L092 gives
[C:F]=4. Use exactly L101's selected prime ell>=7, without changing
the member, ordering, prime or downstairs height H.

For K in {F,C}, write G_K=Gal(Q-bar/K). Fix an F_ell-basis of the
usual full geometric torsion module E_o[ell] and let rho denote its
G_F-representation. Assume, as an additional unproved premise,

    SL_2(F_ell) subset R_F=rho(G_F).

L101's P1–P3 and the original Q-curve's mod-seven image do not
establish this premise for the selected ell. No initial theta-data
or native III situation over either field is assumed here.

## Conclusion

In the same basis, the actual restricted image R_C=rho(G_C) is
normal in R_F, its index divides four, and

    SL_2(F_ell) subset R_C.

Thus the assumed downstairs containment transfers to the same curve
over C. The assertion holds in every torsion basis. It is a
known-method specialization validated by the separate step418 critical
audit below. It does not establish the downstairs premise or complete
a field repair.

## Proof

### Imported inputs and bounded scope

Reuse the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-23-selected-prime-large-image-normal-closure-transfer.md`.
Import J.S. Milne, [*Fields and Galois Theory*, v5.10, September
2022](https://www.jmilne.org/math/CourseNotes/FT.pdf), Theorem
3.17(b,d), pp.39–40 (indices and normal quotients), Propositions
3.19 and 3.21, pp.40–42 (compositum restriction and Galois
intersections), Proposition 7.3, p.95 (intermediate bases), and
Propositions 7.4 and 7.7, pp.95–96 (extension of embeddings and
surjective absolute restriction). Import Keith Conrad,
[*Simplicity of PSLn(F)*](https://kconrad.math.uconn.edu/blurbs/grouptheory/PSLnsimple.pdf),
undated nine-page author version inspected 2026-10-23, Theorem 3.3,
p.4: upper and lower elementary unipotents generate SL_2 over every
field. Use the standard finite-group Lagrange theorem. These general
results are cited rather than reproved.

L047 and L083 are method comparisons for different witnesses, not
mathematical premises here. ATTEMPTS/034 stops a cyclic Frobenius
normality separator, not this conditional restriction argument. The
main gap remains finite B>=A. This target isolates large-image
preservation in a proposed normal-closure repair from independent
same-prime occurrence downstairs. The test is actual full-coordinate
restriction, a normal quotient with index dividing four, and the
elementary-generator test for every ell>=7. A failed obligation
would stop this specialization.

### The actual finite images and quotient

The equation E_o is defined over F, since t_o lies in F. Put
D=F(E_o[ell]). Its finite set of geometric torsion points is
G_F-stable: the curve, origin and multiplication-by-ell map are
F-defined. Adjoining both coordinates of every such point therefore
gives a finite normal extension; characteristic zero gives
separability. Thus D/F is finite Galois. An automorphism of D/F
acts trivially on the full torsion module if and only if it fixes
every coordinate generator. The origin is already F-rational.
Surjective absolute restriction therefore identifies Gal(D/F)
faithfully with the actual matrix subgroup R_F, using the fixed basis.

C is the finite normal closure of F/Q by L090, hence is Galois over
Q in characteristic zero. Since Q subset F subset C, Milne's
intermediate-base result gives C/F Galois, whether or not F/Q is
normal. Its degree is exactly four by L092. Consequently
I=D intersect C is Galois over F, and [I:F] divides [C:F]=4 by
the tower formula.

No coordinates change under extension from F to C, so CD is exactly
the full field C(E_o[ell]). Compositum restriction and surjective
absolute restriction give

    Gal(CD/C) -> Gal(D/I) subset Gal(D/F)=R_F,
    R_C=rho(G_C)=Gal(D/I)

as identifications with the actual matrix actions on all torsion
points, not just abstract groups of equal order. Since I/F is
Galois, Galois correspondence now gives

    R_C normal in R_F,
    R_F/R_C isomorphic to Gal(I/F),
    [R_F:R_C]=[I:F] divides 4.

This includes I=F and imposes no inclusion C subset D, no
disjointness, and no full GL_2 image assumption.

### Elementary generators at the same selected prime

For a in F_ell let U(a)=Id+a E_12 and V(a)=Id+a E_21. Both
families lie in SL_2(F_ell), hence in R_F by the explicit premise.
The matrix units square to zero, so for every nonnegative integer n,

    U(a)^n=Id+n a E_12, V(a)^n=Id+n a E_21.

For a nonzero, n=ell gives identity, while 1<=n<ell gives a
nonzero off-diagonal entry. Thus each nonidentity generator has
exact order ell; the a=0 case is identity. Its image in the actual
quotient R_F/R_C has order dividing ell and, by Lagrange, the
quotient's order, which divides four. Since ell>=7 is prime these
orders are coprime, so every such image is identity. Both elementary
families lie in R_C. Conrad's Theorem 3.3 now gives the asserted
SL_2 containment. A basis change conjugates both images by the
same GL_2 matrix and preserves SL_2, proving basis independence.

All proposed obligations pass. This reproduces a known restriction
method in the exact approved fields; it is no progress beyond the
checked general methods. It supplies neither same-prime downstairs
large image, P4–P7, native initial theta-data/III, exact generation
after repair, nor a cure for L092's relative factor-four excess.
Ell-integrality is neither used nor proved. Native input/action/
factorization/pilot, authentication and essentiality remain unresolved,
as does original finite B>=A. The inherited April/May 2020 source and
def= qualifications remain; the finite-group implication itself
requires only the explicit field and representation hypotheses above.

### Separate critical audit — 2026-10-23, step418

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-23-selected-prime-large-image-transfer-critical-audit.md`.
The audit reuses its primary readings and the precise Milne/Conrad
citations above. No new source theorem or stronger image claim is
imported. L090's actual conjugate/core identification and L092's
audited degree calculation give C/F Galois of degree four; L101's
audited selection gives the same prime ell>=7. The following checks
validate the conditional application, not those inputs afresh.

**Full coordinates and absolute restriction.** Characteristic zero
and t_o distinct from 0,1 give a nonsingular elliptic curve with its
full rank-two geometric ell-torsion module. Every affine torsion
point has both coordinates in D by definition. Thus the kernel of
rho on G_F is exactly G_D: fixing all points fixes all generators,
and fixing the generators fixes all points, including the rational
origin. The finite coordinate set is G_F-stable, so D/F is normal
and separable. Milne's surjective absolute restriction identifies
R_F with Gal(D/F) in the chosen basis. Over C the kernel is exactly
G_C intersect G_D=G_(CD); the same coordinate generators give
C(E_o[ell])=CD. This checks the full linear representation rather
than the action on x-coordinates or projective torsion lines.

**Intermediate base, intersection and actual quotient.** C is a
finite normal separable extension of Q containing F. Milne
Proposition 7.3 applies to this tower even though F/Q is nonnormal;
it gives C/F Galois. With D/F also Galois, I=D intersect C is
Galois over F. Both fields lie in the one fixed algebraic closure,
as required for Proposition 3.19. Restriction from Gal(CD/C) to D
is injective because C and D generate CD, and that proposition
makes its image exactly Gal(D/I). Surjective restriction from G_C
onto Gal(CD/C), followed by this map, is precisely rho restricted
to G_C. Consequently R_C is this subgroup of R_F with the actual
matrix action. The restriction map Gal(D/F) onto Gal(I/F) is
surjective and has kernel Gal(D/I); its quotient is therefore
R_F/R_C. Finally, since F subset I subset C,

    4=[C:F]=[C:I][I:F],  [R_F:R_C]=[I:F] in {1,2,4}.

No equality of that index with four is needed or asserted. In
particular the case D intersect C=F passes. There is no assumption
that C lies in D, that the two extensions are disjoint, or that
normality of successive arbitrary extensions is transitive.

**Every generator and every allowed prime.** Both U(a) and V(a)
have determinant one for every a in F_ell, so the explicit downstairs
premise puts them in the domain of the quotient map R_F -> R_F/R_C.
For either matrix unit N, N^2=0 gives (1+aN)^n=1+naN. If a is
nonzero, this is identity exactly when ell divides n, because the
coefficient field has characteristic ell. Their orders are exactly
ell; at a=0 their images are already identity. An image in the
quotient has order dividing both ell and one of 1,2,4, hence is
identity for every prime ell>=7. This checks both elementary
families, not just conjugates under an unproved larger image.
Conrad Theorem 3.3 now gives SL_2(F_ell) subset R_C. Conjugation
by a change-of-basis matrix preserves determinant one and transports
both actual images together, so the basis-independent conclusion
also passes. Neither perfectness nor simplicity is required.

**Verdict and boundary.** All approved audit obligations pass without
mathematical correction. The argument and its direct inputs are
unchanged; this canonical audit supersedes the overview's pending
wording for L104 only. This is validation of a known-method conditional
input, not a new general theorem or progress beyond the checked
sources. It proves no occurrence of the downstairs premise at L101's
selected prime; the original mod-seven image and P1–P3 cannot be
substituted for that premise in this proof. Native initial theta-data/
III, P4–P7, exact generation/full repair, the relative factor-four
excess, native input/action/factorization/pilot, authentication/def=
qualifications, essentiality and original finite B>=A remain open.
Ell-integrality is unused. No complete-solution candidate is asserted.

## Mathlib

Full matching and supporting Mathlib coverage for this exact-field
specialization has not been checked. Unknown coverage is not evidence
of absence; no formal verification is claimed. The general inputs are
precisely cited above, and the full-coordinate, intermediate-base,
index and elementary-order specializations are proved here.
