# L083 — The exact auxiliary Legendre field has mod-seven image containing SL_2

## Hypotheses

Fix L073's same auxiliary witness E=E_aux/Q in the fixed algebraic
closure Q-bar inside Omega. Retain precisely L077's choices

    A=F_aux=Q(zeta_60,E[30]), D=r_j-r_i,
    s^2=D, s in H, t=(r_k-r_i)/D, B=F'=A(s),
    E_L: V^2=X(X-1)(X-t), iota=zeta_60^15.

Retain L078's literal field G=Q(t)(iota,E_L[15]), so G subset B.
All division fields contain both coordinates of every geometric
torsion point. Absolute Galois groups are taken in this same Q-bar.
L073 gives the full image GL_2(F_7) for E/Q and gives A/Q finite
Galois of degree dividing 2^14*3^3*5. L077 gives D!=0 and the
actual pointed B-isomorphism

    phi(x,y)=((x-r_i)/D,y/(D s)),
    phi^(-1)(X,V)=(r_i+D X,D s V).

No normality of B/Q or G/Q is assumed.

## Conclusion

The full mod-seven image of E_L over this unchanged G contains
SL_2(F_7). This holds in every F_7-basis of E_L[7], for each of
the cross-residue choices and either sign of s allowed in L077.

More precisely, fixing a basis of E[7], its image R_1 over A is
normal in GL_2(F_7) with index dividing [A:Q]. Its image R_2 over
B is normal in R_1 with index dividing [B:A], which is at most
two. Both images contain SL_2(F_7). In the basis transported by
phi, the E_L image over B equals R_2 and is a subgroup of its
image over G.

This is a specialization of the cited known methods. The separate
step329 critical audit below validates it. It closes only this large-image prerequisite;
it gives no full GL_2 verdict over G, normality of G/Q, sufficient
initial data, essential IUT flaw or original finite B>=A comparison.

## Proof

### Imported results and scope

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-18-exact-legendre-mod7-large-image.md`.
Import J.S. Milne, *Fields and Galois Theory*, v5.10 (September
2022), [Theorem 3.10, pp.37–38; Theorem 3.17(b,d), pp.39–40;
Propositions 3.19 and 3.21, pp.40–42; Proposition 7.4,
p.95](https://www.jmilne.org/math/CourseNotes/FT.pdf).
These give the finite splitting-field criterion, Galois
correspondence with indices and normal quotients, compositum
restriction over an intersection, Galois intersections/composita,
and extension of embeddings. In particular, absolute restriction
onto the Galois group of a finite Galois extension is surjective.

Import Keith Conrad, *Simplicity of PSLn(F)*, undated nine-page
version inspected 2026-10-18, [Theorem 3.3/proof,
p.4](https://kconrad.math.uconn.edu/blurbs/grouptheory/PSLnsimple.pdf):
upper and lower elementary unipotents generate SL_2 over every
field. Use Lagrange's theorem for their images in finite quotients.
No generation, simplicity or perfectness theorem is reproved.

For the complete pointed coordinate change and its group-law
compatibility, import J.S. Milne, *Elliptic Curves*, second edition
(2021), [II Propositions 1.5 and 1.6, p.49, and II Theorem 2.4(b),
pp.52–53](https://www.jmilne.org/math/Books/EC2.pdf).
The actual maps and inverse are established in L077. L047 supplies
method context only: its different curve's image conclusion is not
an input here. The necessary specialization consists of the two
actual restriction applications and the full pointed transport.

### First restriction, with base Q

Put K=Q(E[7]) and I_1=K intersect A. The finite coordinate set of
E[7] is stable under the absolute Q-group because E and [7] are
Q-defined. Its coordinates are algebraic in characteristic zero,
so K/Q is a finite separable normal extension, hence finite Galois.
An automorphism acts trivially on E[7] exactly when it fixes all
these coordinates; the origin is rational and causes no exception.
Thus the representation identifies Gal(K/Q) with GL_2(F_7), by
L073's full-image conclusion for this same curve.

Both K/Q and A/Q are Galois, so I_1/Q is Galois. The full
seven-division field over A is M=AK=A(E[7]); no geometric points
or coordinates change on base extension. Compositum restriction
identifies Gal(M/A) with Gal(K/I_1). Restriction from the absolute
A-group onto Gal(M/A) is onto by extension of automorphisms to
Q-bar. In the fixed basis, therefore, the actual image is

    R_1=rho_E,7(G_A)=Gal(K/I_1) subset Gal(K/Q)=GL_2(F_7).

Galois correspondence makes R_1 normal and gives

    [GL_2(F_7):R_1]=[I_1:Q] dividing [A:Q] dividing 2^14*3^3*5.

In particular the quotient order is prime to seven. No assertion
that I_1=Q, or any linear-disjointness assertion, is needed.

For a in F_7, write U(a)=1+a E_12 and V(a)=1+a E_21. The two
matrix units square to zero, so their nth powers are respectively
1+n a E_12 and 1+n a E_21. For a!=0 their orders are exactly
seven: the powers with 1<=n<=6 are nonidentity and the seventh
power is identity. For a=0 the order is one. Their images in
GL_2(F_7)/R_1 have orders dividing both seven and that quotient's
prime-to-seven order. Lagrange's theorem makes all these images
trivial. Thus R_1 contains both elementary families, and Conrad's
generation theorem gives SL_2(F_7) subset R_1.

### Second restriction, with base A

Here the base is A, not Q. Since D lies in A and is nonzero,
T^2-D is separable and B=A(s) contains both its roots s and -s.
It is its splitting field over A. Thus B/A is finite Galois with
[B:A] in {1,2}. This argument neither assumes nor concludes that
B/Q is Galois.

The field M/A is finite Galois, with group faithfully identified
with R_1 as above. Put I_2=M intersect B. Both extensions are
Galois over A, so I_2/A is Galois. Compositum restriction gives

    Gal(MB/B)=Gal(M/I_2) subset Gal(M/A)=R_1.

Absolute restriction from G_B onto Gal(MB/B) is onto, and MB is
the full field B(E[7]). Hence the displayed subgroup is exactly
R_2=rho_E,7(G_B). It is normal in R_1 and its quotient has order

    [R_1:R_2]=[I_2:A] dividing [B:A] <= 2.

Every U(a) and V(a) already lies in R_1 by the first restriction.
Its image in R_1/R_2 has order dividing seven and a number at most
two, so is trivial. The same generation theorem yields
SL_2(F_7) subset R_2. The actual normal quotients at the two
bases are used separately; normality is not propagated up a tower.

### Full pointed seven-torsion transport and the exact G

L077's phi and inverse have all their coefficients in B, with
D s!=0. They extend to the origins and are inverse pointed
isomorphisms of complete elliptic curves. The imported group-law
result implies that both commute with [7]. Thus phi restricts to
an F_7-linear bijection E[7] -> E_L[7], not merely an injection
on a cyclic subgroup or a correspondence of x-coordinates.

For sigma in G_B and a nonorigin P=(x,y), sigma fixes r_i,D,s,
and therefore

    sigma(phi(P))=((sigma(x)-r_i)/D,sigma(y)/(D s))
                 =phi(sigma(P)).

The inverse formula has the same equivariance on both coordinates.
The origins are fixed and transported to one another, so the
equivariance holds on the full geometric torsion sets. If P_1,P_2
is the fixed basis of E[7], phi(P_1),phi(P_2) is a basis of
E_L[7]. In these bases, the two representations restricted to G_B
have identical matrices. Consequently

    rho_E_L,7(G_B)=R_2 contains SL_2(F_7).

Finally L078 gives the actual subfield inclusion G subset B for
this same E_L. The absolute groups have the reversed inclusion
G_B subset G_G inside Gal(Q-bar/Q). Restrict the representation
of E_L/G to this subgroup; it is the representation just computed.
Thus its image over G contains its image over B, establishing
the required containment over the literal G. No B-defined map is
asserted to be G-defined, and neither G=B nor G/Q normal is used.

Changing a basis conjugates by an invertible matrix C. Since
det(C^(-1) X C)=det(X), conjugation preserves the full subgroup
SL_2(F_7). The conclusion is therefore independent of basis.
All arguments apply to every permitted D and either sign of s:
the splitting-field argument remains valid and both pointed maps
retain their stated fields of definition.

### Threshold, relevance and limitations

The requested threshold is containment of the entire SL_2(F_7),
and it is reached after both restrictions and over G. All actual
images and quotient orders have been identified, rather than only
bounded by unrelated abstract groups. No mathematical script or
numerical evidence is used. This is local progress by assessed known
methods, with no result beyond the checked sources claimed.

It can supply one independent initial-data prerequisite for the
exactly generated auxiliary field. G/Q normality and its mixed
radical/15-torsion kernel, other initial data, retained-witness
radical/scalar questions, native input/action, all-image factorization,
pilot transport, essentiality and original finite B>=A remain open.
L078's local H,N packet is unchanged; neither its existence nor the
image result supplies these independent bridges. The retained and
auxiliary witnesses remain distinct. All existing route stops,
including ATTEMPTS/034's cyclic-Frobenius separator stop, are intact.
The separate critical audit below verifies this exact specialization.

### Separate critical audit — 2026-10-19, step329

**Verdict and scope.** The exact containment passes. This audit uses
the prior SPECIALIZE assessment
`drafts/literature/2026-10-18-exact-legendre-mod7-critical-audit.md`
and the primary inputs precisely cited above. No theorem about a
different curve is substituted, no mathematical repair is necessary,
and no stronger conclusion is asserted. This is independent checking
of a known-method specialization, not progress beyond the checked
sources. The following checks concern the whole argument, rather than
an image-order comparison or a finite sample of points.

**Same witness and actual fields.** L073's full-image and retention
proofs choose a single auxiliary member: the fixed congruences survive
the mod-seven selection, and its own full 30-coordinate field is A.
Thus both GL_2(F_7) over Q and the Galois degree divisibility concern
this E. L077 supplies the nonzero D in A and the algebraic s in the
fixed Q-bar, despite selecting s in H. In particular B=A(s) is an
actual number subfield of that same closure. L078's upper-inclusion
proof puts every generator t, iota and every full E_L[15] coordinate
in B. Consequently G subset B is an embedded field inclusion, and
E_L is defined over G since its coefficient t belongs to G. None of
these facts follows merely from the equal local completions.

**First finite image and quotient.** For K=Q(E[7]), the kernel of
the geometric representation is exactly the pointwise fixing group
of the full coordinate field. Stability of this finite coordinate
set under G_Q makes K/Q normal; characteristic zero gives separability.
The imported extension theorem therefore makes absolute restriction
onto Gal(K/Q) surjective. The faithful matrix action identifies this
group with L073's full GL_2(F_7). Since A/Q is Galois, the intersection
I_1=K intersect A is Galois over Q. Applying the cited compositum
restriction theorem to K/Q and A identifies Gal(AK/A) with
Gal(K/I_1), with the same action on every E[7] point. Absolute
restriction onto Gal(AK/A) is surjective as well. This verifies
R_1=rho(G_A), not merely an abstract subgroup isomorphic to it.
Normality and index are now legitimate Galois-correspondence
conclusions: [GL_2:R_1]=[I_1:Q], and the tower formula gives
[I_1:Q] dividing [A:Q]. The latter divides 2^14*3^3*5, which has
no factor seven. An upper bound on the degree alone would not suffice.

**Second finite image and quotient.** The polynomial T^2-D is
separable because D!=0 and the base has characteristic zero; both
roots are in B. Hence B/A is Galois of degree one or two, whether
or not B/Q is normal. Also M=AK is Galois over A. It follows that
I_2=M intersect B is Galois over A and that compositum restriction
identifies Gal(MB/B) with Gal(M/I_2). Here MB=B(E[7]) is the full
coordinate field, and surjective absolute restriction makes its
matrix image precisely R_2=rho(G_B). The identification of Gal(M/A)
with R_1 is faithful: an A-automorphism fixing E[7] fixes its generators
and hence all of M. Thus R_2 is normal in R_1 and
[R_1:R_2]=[I_2:A] divides [B:A]. The potentially trivial intersection
and degree-one extension cases satisfy the same formulas. No inference
of transitive normality or normality of R_2 in GL_2 is made or needed.

**Both generator tests.** For each nonzero a in F_7, the identity
(1+aE_ij)^n=1+naE_ij gives exact order seven: n=1,...,6 never
annihilates a, whereas n=7 does. The zero parameter gives identity.
In the first actual quotient each image has order dividing seven
and the prime-to-seven quotient order, so is identity. Conrad's
Theorem 3.3 therefore places all SL_2 in R_1. The second quotient
is defined only on R_1; the first test has already put every required
elementary generator in that domain. Its order is at most two,
so the same order test places these generators in R_2, and the
same cited generation theorem gives the entire SL_2 there. This
does not require simplicity, perfectness or a full-GL_2 conclusion.

**Complete pointed transport and subgroup direction.** The actual
maps from L077 have inverse coordinates x=r_i+DX, y=DsV. Their
substitution identity uses (Ds)^2=D^3 and the three roots to give
g_aux(r_i+DX)=D^3 X(X-1)(X-t). The invertible projective maps
extend over the origins and fix [0:1:0]. The cited pointed-map
theorem makes them group homomorphisms. In particular both commute
with [7]: every point in either seven-torsion group maps into the
other, and the inverse proves surjectivity on the whole group.
For sigma in G_B, r_i,D,s and the inverses of D and s are fixed, so the
displayed coordinate formulas commute with sigma on both coordinates;
the origin is covered separately. The resulting F_7-linear bijection
therefore conjugates the complete restricted representations and
gives identical matrices in transported bases. This establishes the
image equality over B, not just equality of cardinalities.

Every automorphism fixing B fixes G, hence G_B subset G_G. Since
E_L is defined over G, its G_B representation is the restriction
of this very G_G representation. Its image over G consequently
contains R_2. The B-defined comparison map need not be G-defined.
Changing basis conjugates SL_2 to itself by invariance of determinant;
changing the sign of s composes the comparison with inversion.
Every permitted nonzero cross-residue choice has the same verified
field and map hypotheses. These checks prove exactly the stated
uniform conclusion over unchanged G.

**Limits.** L047 is only method context, and ATTEMPTS/034's failed
cyclic separator contributes no premise. No argument change is
needed. In particular this audit supplies no
G/Q normality, mixed-kernel membership, full GL_2 image over G,
sufficient initial data, native input/action identification, pilot
transport, essentiality or original finite B>=A. The achieved
threshold is the full SL_2 containment alone. Mathlib coverage
remains unchecked as specified below.

## Mathlib

Full matching and supporting Mathlib coverage for this combined
exact-field application has not been checked. Unknown coverage is
not absence, and no formal-verification claim is made. The general
Galois, generation and pointed-coordinate inputs are precisely cited
above; their explicit two-stage application is the local result.
