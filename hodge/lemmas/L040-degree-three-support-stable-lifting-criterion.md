# L040 — Stable lifts of degree-three support morphisms

## Hypotheses

Let X be a smooth projective complex K3 surface, and let H be
general in the sense of Yoshioka's section 0.2. Retain that
polarization hypothesis. Set M=M_H(2,0,-1), and choose an
untwisted universal sheaf P on M x X. The existence criterion
for P is recalled below; it does not supply a parameter map.
Let B be a smooth connected projective complex surface, and
let g:B -> Y=X^{(3)} be an algebraic morphism. The intended
application is B=X=S.

Let Psi:M -> X^[3] be the specific isomorphism constructed
in Yoshioka's Proposition 3.4 by the reflection-and-dual
transform, and let rho:X^[3] -> Y be Hilbert--Chow. Let
J be Ekedahl--Skjelnes' ideal sheaf of norms on Y, defined in
their section 7.24, with its full scheme structure. Write

\[
\mathcal R=\bigoplus_{n\geq0}J^n,\qquad C=V(J).
\]

Do not replace J by an unspecified reduced collision ideal.
For a stable sheaf E, its weighted support means the cycle
of Q_E=E^{**}/E, using the length at every support point.
For a pulled-back universal family F on B x X, use the
quotient Q, support morphism Phi_Q and cycle Gamma_Q of L039.

## Conclusion

The morphism

\[
\Phi_M=\rho\circ\Psi:M\longrightarrow X^{(3)}
\tag{1}
\]

is the actual weighted-support morphism. For every f:B -> M
and F=(f x id_X)^*P,

\[
\Phi_Q=\Phi_M\circ f.
\tag{2}
\]

These assertions hold on all collision strata, including a
family whose entire image lies there.

Stable maps f:B -> M with Phi_M f=g are in bijection with
isomorphism classes of pairs (L,lambda), where L is a line
bundle on B and

\[
\lambda:g^*\mathcal R\longrightarrow
             \bigoplus_{n\geq0}L^{\otimes n}
\tag{3}
\]

is a unital graded O_B-algebra map whose degree-one component
g^*J -> L is surjective. Isomorphisms of L must intertwine
all the maps in (3). In particular all Rees relations are
required. This is a necessary and sufficient criterion,
including maps into C; it is not automatic lift existence.

If g(B) is not contained in C, put

\[
K=J O_B=\operatorname{im}(g^*J\longrightarrow O_B).
\]

Then a stable lift exists exactly when K is an invertible
ideal, equivalently when g^{-1}(C) is an effective Cartier
divisor, allowing the empty divisor. The lift is unique.
If g(B) is contained in C, this invertible-image-ideal test
does not apply: use (3). Boundary maps can have lifts even
when K=0.

Every resulting family is B-flat with stable fibres and,
by L039, its normalized universal action is the positive
weighted-support action

\[
f^*\theta_v(0,t,0)
 =p_*\bigl(q^*t\smile[\Gamma_Q]\bigr),\quad t\in H^2(X,Q).
\tag{4}
\]

Here p and q are the product projections from B x X.
Base-line-bundle twists preserve the support and this action.
No independent support map, non-scalar action, transverse
surface or general Hodge resolution is constructed.

## Proof

**Known global model and the particular isomorphism.**
Import [Yoshioka, *Irreducibility of moduli spaces of vector
bundles on K3 surfaces*, arXiv:math/9907001v2, 7 February 2000,
Proposition 3.4 and equations (3.42)--(3.47), PDF p. 16](https://arxiv.org/pdf/math/9907001v2#page=16),
under the [section 0.2 polarization assumption, PDF p. 2](https://arxiv.org/pdf/math/9907001v2#page=2).
With v_0=v(O_X)=(1,0,1) and l=2, its vector is (2,0,-1).
It constructs Psi, not merely a birational equivalence.
In two copies of X with projections r_1,r_2, its transform is

\[
G(E)=Rr_{2*}R\mathcal Hom(r_1^*E,I_\Delta),\qquad
\mathcal H^1(G(E))=I_Z,\quad Z=\Psi(E).
\tag{5}
\]

The other cohomology sheaves vanish, and Z has length three.
Use these all-fibre conclusions by citation. Their reproof,
or a classification of punctual rank-two quotients, is
unnecessary for the identified support difference.

**Support comparison at every fibre.**
L039's pointwise calculation gives

\[
E^{**}=O_X^2,\quad E^\vee=O_X^2,\quad
\bigl(\dim\operatorname{Ext}^i(E,O_X)\bigr)_{i=0,1,2}
 =(2,1,0).
\tag{6}
\]

Dualize 0 -> E -> O_X^2 -> Q_E -> 0. A finite-length module
over a regular local ring of dimension two has Ext only in
degree two. This follows first for the residue field from
the Koszul resolution and then for all finite-length modules
by a composition series and the long exact Ext sequence.
Consequently

\[
\mathcal Ext^1(E,O_X)=\mathcal Ext^2(Q_E,O_X)=:D(Q_E),
\qquad \mathcal Ext^2(E,O_X)=0.
\tag{7}
\]

At every support point the same composition-series argument
gives length(D(Q_E))=length(Q_E). In fact Ext^2 is an exact
contravariant functor on these finite-length modules and
sends the residue field to a one-dimensional residue-field
module. It preserves every punctual multiplicity, not only
the total length. No assumption that Q_E is cyclic is used.

Apply Rr_{2*}RHom(r_1^*E,-) to the diagonal sequence. Since E
is perfect on X, the resulting triangle is

\[
G(E)\longrightarrow
 R\operatorname{Hom}_X(E,O_X)\otimes O_X
 \longrightarrow R\mathcal Hom_X(E,O_X)
 \longrightarrow G(E)[1].
\tag{8}
\]

For the last identification restrict r_1^*E to the diagonal;
its derived dual can be moved through this restriction
because E is perfect. The degree-zero middle map is the
evaluation Hom_X(E,O_X) tensor O_X -> E^vee. By (6) it is
the isomorphism from the two constant sections of O_X^2.
The cohomology sequence of (8), using (5)--(7), therefore gives

\[
0\longrightarrow I_Z\longrightarrow
 \operatorname{Ext}^1_X(E,O_X)\otimes O_X
 \longrightarrow D(Q_E)\longrightarrow0.
\tag{9}
\]

The middle coefficient is a one-dimensional vector space.
After choosing its nonzero basis, (9) has quotient O_Z.
To identify its kernel with the particular ideal defining Z,
take double duals of the injection: both are O_X, and the
resulting nonzero endomorphism is a nonzero constant. Thus
rescaling changes no ideal. Equivalently D(Q_E) is O_Z
tensored with the coefficient line. This identifies the
dual module, not Q_E itself; at a non-Gorenstein punctual
subscheme those two modules need not be isomorphic.

The punctual lengths of Q_E consequently equal those of O_Z.
Hilbert--Chow sends Z to exactly these weighted points, so
(1) has the stated actual support on every stable fibre.
It in particular supplies an algebraic support morphism on M.

For a parameter map f, L039 supplies the flat length-three
quotient Q and its morphism Phi_Q. The two maps in (2) agree
at every closed point by the fibre calculation just made.
They agree as morphisms: B is reduced of finite type over C
and Y is separated. Indeed their equalizer is closed and its
ideal vanishes at every closed point, hence vanishes on this
reduced Jacobson scheme. This argument uses every closed
point, rather than requiring distinct support on a dense
subset of B. It includes an image wholly inside any boundary
stratum.

**The full lifting data.**
Import [Ekedahl--Skjelnes, *Recovering the good component of
the Hilbert scheme*, Annals of Mathematics 179 (2014),
Definition 2.7, section 7.24, Theorem 7.25 and Corollary 7.28,
printed pp. 811,834--837](https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n3-p01-p.pdf#page=30).
Their Proposition 7.23(4) identifies the divided-power base
with X^{(3)} in characteristic zero. Their norm map is the
weighted-cycle Hilbert--Chow map, and the surface corollary
covers the whole Hilbert scheme, not just a good component
of a possibly higher-dimensional Hilbert scheme. It gives
the following identification over Y:

\[
(X^{[3]},\rho)=\bigl(\operatorname{Proj}_Y\mathcal R,
                          \text{structure map}\bigr).
\tag{10}
\]

Since R is generated in degree one, import the functorial
description in [Stacks, Lemma 27.16.11, Tag 01O4](https://stacks.math.columbia.edu/tag/01O4).
It classifies maps h:B -> Proj_Y R over g by exactly (3).
The equivalence is strict equivalence of the line-bundle data,
as stated in that theorem. The map corresponding to (3) is
therefore h:B -> X^[3] with rho h=g; set f=Psi^{-1}h.
Conversely every stable lift f supplies h=Psi f and those
same Proj data. Equations (1)--(2) prove that these are lifts
of the prescribed actual support, establishing the bijection.
No ordering of the support points or quotient-line descent
has been assumed; the global morphism h includes the descent.

**Necessity and uniqueness away from an entirely exceptional image.**
B is integral because it is smooth and connected. Suppose
first that a lift h exists and g(B) is not contained in C.
On the blowup, J O_(X^[3]) is an invertible ideal with its
canonical inclusion into O_(X^[3]); this is the usual
tautological ideal of a blowup. Pulling back gives a line
bundle L and a map L -> O_B. It is an isomorphism over
the nonempty open U=B minus g^{-1}(C), hence is nonzero at
the generic point. On an integral B a map from a line
bundle to O_B which is generically nonzero is injective:
locally its defining nonzero element is a nonzerodivisor.
The quotient g^*J -> L is surjective. The image of the
composition to O_B is consequently exactly K=J O_B,
so K is an invertible ideal. This checks a necessity that
the usual sufficient Cartier criterion alone would not give.

Conversely, if K is an invertible ideal, g^{-1}(C) is an
effective Cartier divisor. Import [Stacks, Lemma 31.33.5,
Tag 0806](https://stacks.math.columbia.edu/tag/0806) to obtain
the unique map h over g. By (1)--(2) its inverse image under
Psi is the required stable lift f. This also gives uniqueness
among all lifts. Alternatively every lift agrees with the
unique inverse of rho on U, and separatedness extends the
agreement across the integral B.

If g(B) is contained in C, that argument has no nonempty U
and its pulled-back inclusion can be zero. Replacing g^*R
by the Rees algebra of its image ideal would then lose the
exceptional fibres. In particular g^*(J^n) is not in general
(J O_B)^n. The general criterion remains (3).
For a concrete consistency check, take g constant at 3x,
choose any length-three subscheme Z supported at x, and let
h be the constant map to Z in X^[3]. It has rho h=g and
g(B) lies in C, but J O_B=0. Its stable map Psi^{-1}h
exists by the imported global theorem. Thus the excluded
blanket no-lift inference from a zero image ideal is false.

**Stable family and downstream action.**
Existence of P follows by the determinant-of-cohomology
criterion in [Huybrechts--Lehn, *The Geometry of Moduli
Spaces of Sheaves*, the online 281-page text, Theorem 4.6.5
and Corollary 4.6.7, printed pp. 107--108](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=119):
chi(E)=1 already gives Euler-pairing gcd one. For any f
constructed above, (f x id_X)^*P is B-flat by base change
and has the prescribed stable fibres. A change by a base
line bundle retains the same moduli map. L039, applied to
this actual family, proves (4) and its twist qualification.
Nothing in the Proj criterion makes that action non-scalar.

This completes the saved support-preserving lifting test.
The global model and Proj/blowup criteria are known imports;
the dual-quotient comparison and their correct applicability
are the scoped specialization. Classification is REPRODUCTION,
with no originality or progress beyond the checked literature
claimed. A non-scalar support map meeting the criterion and
its transverse use remain unresolved.

## Mathlib

Coverage: **not checked** for this full statement, the
moduli isomorphism, punctual duals, ideal of norms, relative
Proj, blowup lifting or universal sheaves. No absence from
checked Mathlib sources is asserted. The direct Yoshioka,
Ekedahl--Skjelnes, Stacks and Huybrechts--Lehn references
match the imported portions, not a Mathlib theorem for the
full support-preserving statement. The Koszul resolution,
long exact Ext sequence and perfect-complex adjunction are
standard supporting inputs to the fibre comparison.
