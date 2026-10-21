# L078 — The exactly generated auxiliary Legendre field retains H and N

## Hypotheses

Fix the same L073 auxiliary witness E=E_aux/Q and the same choices
in audited L077. All number fields lie in the fixed Q-bar inside
Omega, with places induced by that embedding. In particular,

    F_aux=Q(zeta_60,E[30]),
    (F_aux)_u=H=Q_3(zeta_60),
    H(E[7])=N=Q_3(zeta_420,3^(1/7)).

Here zeta_60 is the specified primitive sixtieth root. Let r_i,r_j
be roots of the original monic cubic with different residues, let
r_k be its remaining root, and retain the actual choices

    D=r_j-r_i, s in H with s^2=D,
    t=(r_k-r_i)/D,
    E_L: V^2=X(X-1)(X-t),
    F'=F_aux(s), iota=zeta_60^15.

By L077, t!=0,1, F' is a number field with induced completion H,
and E_L has full F'-rational geometric 15-torsion. Define exactly

    T_0=Q(t), G=T_0(iota,E_L[15]), M=G(E_L[7]).

Division-field notation includes both affine coordinates of every
geometric torsion point; the origin is rational and adds no generator.
Let u_G,w_M denote the induced places on G,M respectively.

## Conclusion

G is a number field, E_L is a nonsingular pointed elliptic curve
over T_0, its full geometric 15-torsion is G-rational, and

    G_(u_G)=H, M_(w_M)=N

as embedded completions. These assertions hold for every stated
cross-residue choice and either sign of s. They concern the literal
field G=Q(t)(iota,E_L[15]), without asserting G=F' or native T=T_0.
This is a known-method specialization, validated by the separate
step307 critical audit below, not an IUT counterexample or a complete
candidate resolution.

## Proof

### Imported results and specialization scope

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-18-exactly-generated-auxiliary-legendre-local-packet.md`.
Import Silverman, *The Arithmetic of Elliptic Curves*, second edition
(2009), [III Proposition 8.1(c,d), pp.94–96 and Corollary 8.1.1,
p.96](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=114):
over a field whose characteristic does not divide m, full rational
geometric m-torsion implies that the field contains a primitive
m-th root of unity. Import Milne, *Fields and Galois Theory*, v5.10
(September 2022), [Proposition 5.8(a,b), pp.64–65](https://www.jmilne.org/math/CourseNotes/FT.pdf),
for cyclicity of the full group of m-th roots when the characteristic
does not divide m. Thus the primitive root generates all these roots.
The hypotheses here are field characteristic zero and m=15, including
its factor 3; residue characteristic 3 does not violate them.

Import Milne, *Algebraic Number Theory*, v3.08 (19 July 2020),
[section 8, p.135 and Propositions 8.1–8.2 with proofs p.136](https://www.jmilne.org/math/CourseNotes/ANT.pdf).
For a finite separable extension A(alpha)/A with the chosen extended
place, its embedded completion is A-hat(alpha), using that same
root image. Iterating gives this identity for a finite coordinate
list. No Galoisness, disjointness or degree equality is required.

Use the complete pointed coordinate maps and their group-law
compatibility already established in L077, importing Milne,
*Elliptic Curves*, second edition (2021), [II Theorem 2.4(b),
pp.52–53](https://www.jmilne.org/math/Books/EC2.pdf).
None of these general theorems is reproved. The necessary additional
work is the particular cyclotomic lower inclusion, the generator
upper inclusion, and both directions of the local full-torsion transfer
for this exactly generated subfield.

### Actual coefficient field, torsion and upper inclusion

All r_m belong to F_aux, and D!=0. Thus t belongs to F_aux,
is algebraic over Q and avoids 0 and 1 by distinctness of the roots.
Consequently T_0 is a number field and the displayed Legendre cubic
defines a nonsingular pointed elliptic curve over T_0. L077 gives
every geometric E_L[15] point both coordinates in F'. Also
iota belongs to Q(zeta_60) subset F_aux subset F'. Hence every
generator in the definition of G belongs to F', so

    T_0 subset G subset F' subset H.

Since F'/Q is finite, G/Q is finite. The same full coordinate
definition gives E_L[15] subset E_L(G), including its rational origin.
This rationality concerns all geometric points, not just a chosen
subgroup. It is available before applying the pairing theorem.

### Cyclotomic lower inclusion and first embedded completion

Apply the imported Weil-pairing corollary over G to E_L and m=15.
It puts a primitive fifteenth root eta in G. Its fifteen powers are
distinct and exhaust all roots of X^15-1 in our fixed algebraic
closure. The particular element alpha=zeta_60^4 has exact order 15,
because 60/gcd(60,4)=15; it is therefore one of these powers and
belongs to G. The specified iota has exact order four and belongs
to G by definition. In the same embedding the exact identity

    alpha^4 iota^(-1)=zeta_60^(16-15)=zeta_60

shows that k=Q(zeta_60) is a subfield of G. No identification of eta
with a preselected generator, or independence of cyclotomic fields,
has been assumed.

The completion of k at this place is Q_3(zeta_60)=H, by the imported
completion theorem applied to k/Q. Write S_15 for the finite set of
all affine E_L[15] coordinates. We have G=k(t,S_15): the right
side is contained in G by the lower inclusion just proved, and
contains all original generators since iota lies in k. Every member
of {t} union S_15 already lies in H by the upper inclusion. Applying
the theorem successively to this finite list gives

    G_(u_G)=k_v(t,S_15)=H(t,S_15)=H.

All extensions are finite separable in characteristic zero, and every
place is induced by the original embedding. This proves both
inclusions for the first completion, rather than inferring equality
merely from G subset H. It makes no assertion about other G-places.

### Both directions of full seven-torsion transport over H

L077's complete pointed isomorphism and inverse are

    phi(x,y)=((x-r_i)/D, y/(Ds)),
    phi^(-1)(X,V)=(r_i+DX, Ds V).

Each r_m lies in F_aux subset H, D!=0 lies in H, and this very s
lies in H with s!=0. Thus both maps are defined over the same H.
They extend to the origins and commute with multiplication by seven.
In particular phi maps every geometric E[7] point into E_L[7],
and its inverse maps every geometric E_L[7] point into E[7]. Their
composites are the identity, so these maps cover both entire torsion
sets. The coefficients need only lie in H here; no assertion that
they lie in G is used.

Set A=H(E[7]) and B=H(E_L[7]) inside the same Omega. For any
nonorigin P=(x,y) in E[7], the forward formulas give both coordinates
of phi(P) in A. Every nonorigin E_L[7] point arises this way, since
the pointed inverse preserves seven-torsion and the origin. Hence
B subset A. For any nonorigin Q=(X,V) in E_L[7], the inverse
formulas put both coordinates of phi^(-1)(Q) in B. These exhaust
the nonorigin E[7] points, so A subset B. Therefore, using L073,

    H(E_L[7])=H(E[7])=N.

This is equality of embedded local fields generated by all coordinates.
It is not a claim that the two global division fields coincide.

### Completion of the exactly generated seven-division extension

E_L is defined over G. Its finite geometric seven-torsion coordinate
list S_7 is algebraic over G. The global and local lists can be
identified in Omega: the division equations are the same equations,
and all their geometric coordinates are algebraic over the number
field T_0. Characteristic zero makes the torsion finite etale;
passing to the chosen local algebraic closure supplies no additional
geometric torsion points. The full coordinate convention used in
L077 is thus the same one here.

M=G(S_7) is a finite separable number-field extension of G. Apply
the completion theorem at w_M, restricting to u_G, to all these
coordinates. The first equality already proved and the two local
transport inclusions give

    M_(w_M)=G_(u_G)(S_7)=H(E_L[7])=N.

No global Galois property, disjointness, x-only field or cyclic
subgroup has been substituted for this argument. Both requested
embedded completion equalities pass for the same model and embedding.

### Relevance and remaining limitations

The main gap is still the original finite B>=A assertion. This
specialization supplies an auxiliary field with the literal
torsion-generation prescription while retaining the chosen local
packet. It removes the specific subfield-completion uncertainty left
by L077. It is local progress using assessed known methods, without
a claim of mathematics beyond the literature checked.

T_0 has not been identified with native T=F_tpd, G has not been
identified with F' or the retained F, and no independent initial-data
condition has been transferred to G. L074/L075's exclusion concerns
unchanged F_aux and is consistent with G subset F'. The retained
E_0,F,K_glob,Omega,embedding,u,w,H,N,q_0 are unchanged; the new
auxiliary places have their own names. No equality q_aux=3^30 or
q_aux=q_0 is asserted. Native T/model, retained memberships/scalar
occurrence, marked all-image factorization, pilot transport,
essentiality and the original finite comparison remain unresolved.
The foundations/05 step272 source qualifications and
ATTEMPTS/027,028,031,032,033 remain in force. The separate critical
audit below validates only the stated specialization.

### Separate critical audit — 2026-10-18, step 307

The invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-18-exactly-generated-auxiliary-legendre-critical-audit.md`
covers precisely this audit. Reuse the primary results, versions and
locations cited above. Checked L073's same-witness packet clauses and
retention proof/audit, the complete L077 proof and audit, and the
inherited L074 coordinate formulas and L076 local-root construction.
Both asserted embedded equalities pass, with no added hypothesis or
correction to the argument. The following checks concern the literal
G and its own division extension, not just L077's larger field.

**Field and pairing hypotheses.** The three distinct roots are in
F_aux, so D is nonzero and t is algebraic and different from 0,1.
The chosen s is nonzero, belongs to H, and is algebraic over Q
because s^2=D. Thus F'=F_aux(s) is the embedded number field
used in L077. Its pointed isomorphism transports every geometric
15-torsion point of E to E_L, with both coordinates in F'. Together
with t and iota in F_aux this proves G subset F' subset H. In
particular G is a number field and E_L/G is an elliptic curve with
full geometric 15-torsion rational over G by G's definition. These
facts precede the use of Silverman III.8.1(c,d)/8.1.1. Its invertibility
condition concerns characteristic zero, not residue characteristic 3;
the composite level 15 is allowed.

**The specified cyclotomic field, not an abstract isomorphic copy.**
The pairing import puts a primitive fifteenth root eta in this G.
Its powers exhaust all fifteen distinct roots of X^15-1 in the fixed
closure, by the cited Milne FT5.8. The specified alpha=zeta_60^4
has order 15, so alpha belongs to G regardless of which eta the
pairing supplies. Also iota=zeta_60^15 is a defining generator of
G. The exponent computation 4*4-15=1 proves
alpha^4/iota=zeta_60 in that same embedding. Hence k=Q(zeta_60)
is actually contained in G. No choice of a primitive root has been
silently identified with a different one, and no disjointness or
cyclotomic degree assertion is required.

**First completion and its place.** Restrict u_G to k and then Q;
these are the places induced by the original embedding into Omega.
Milne ANT section 8 gives k_v=Q_3(zeta_60)=H. The two generator
inclusions prove the exact identity G=k(t,S_15), where S_15 is
the full finite affine coordinate list, not a selected torsion basis
or x-coordinate list. Each generator lies in H. Every intermediate
number-field extension is finite separable, with place obtained by
restriction of u_G. Successive applications of that theorem therefore
give G_(u_G)=H(t,S_15)=H. The upper ambient-field inclusion alone
would not prove this; the verified k inclusion supplies the lower
completion. No Galoisness or claim about other places is used.

**Both complete local seven-torsion transports.** All r_m,D,s are
in H, with D s nonzero. The actual inverse change is
x=r_i+D X, y=D s V, with s^2=D and s^3=D s; substitution gives
g_aux(r_i+D X)=D^3 X(X-1)(X-t). The projective changes displayed
in L077 are invertible over H and fix [0:1:0]. The cited pointed
group-law compatibility therefore applies over H in both directions.
For every nonorigin P in E[7], both coordinates of phi(P) belong
to H(E[7]); every nonorigin point of E_L[7] is such an image,
since the pointed inverse commutes with [7]. Thus
H(E_L[7]) subset H(E[7]). Conversely that inverse puts both
coordinates of every E[7] point in H(E_L[7]), using its preimage
in E_L[7]. The origins are rational and add no generators. Hence
the local division fields are equal, and L073 supplies their value
N. The maps need to be defined over H, not over G; no global
division-field equality is inserted.

**Second completion and the complete coordinate list.** The model
E_L is defined over T_0 subset G. Its seven-torsion is finite etale
in characteristic zero. Every geometric coordinate is therefore
algebraic over T_0 and lies in the fixed Q-bar inside Omega; base
change to the local algebraic closure introduces no extra geometric
points. Thus the finite list S_7 defining M=G(E_L[7]) is exactly
the list used in H(E_L[7]). The place w_M restricts to the very
u_G already checked. Applying the same completion theorem to this
finite separable coordinate adjunction gives
M_(w_M)=G_(u_G)(S_7)=H(E_L[7])=N. It is not enough merely to
embed M in N or compare degrees; the displayed generator identity
and its induced place establish the equality.

**Verdict and limits.** Each check holds for every allowed
cross-residue choice. Changing s to -s composes the isomorphism
with inversion, preserving both full torsion transports. Both
thresholds therefore pass for the same choices simultaneously.
This is local verification of a known-method specialization, with
no claim beyond the checked sources. Direct inputs remain L073 and
L077, with the root and coordinate inputs inherited through L077;
no new DAG edge is needed. Native T=F_tpd has not been identified
with Q(t); independent initial data and the original finite B>=A
gap remain open. Neither G=F' nor any transfer of the retained
witness's global data has been proved. The original argument is
unchanged, so this canonical audit supersedes its pending-audit
description in the overview without rewriting that overview.

## Mathlib

Full matching and supporting Mathlib coverage for this combined
specialization has not been checked. No absence or formal-verification
claim is made. The general pairing, cyclotomic, coordinate and
completion results are precisely cited above; only their explicit
same-model specialization is supplied here.
