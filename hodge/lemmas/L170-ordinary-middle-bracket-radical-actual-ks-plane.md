# L170 — Ordinary-middle bracket radical is the actual KS plane

## Hypotheses

Retain the entire conditional family of L164, including L071's actual
connection and L116's framework through its hypotheses. Thus the
identical marked projective K3 factors S_1 and B carry the fixed common
hyperkähler metric, real Kähler class, ordered triple and holomorphic
two-forms. The hypothetical locally free rank-two product-polystable
bundle F has integral c_1(F)=0 and

\[
 \operatorname{ch}(F)=2-14e_1-21e_2-\tau_D+62e_1e_2.
\]

Put V=End_0(F), C=Rp_*V and M=R^1p_*V. Fix a point z of the finite
reduced split set Z. Its fibre is L direct sum L^{-1}, with
c_1(L)^2=-14 and h.c_1(L)=0. Write

\[
 E_z=H^1(S_1,V_z),\qquad
 Q_z=e_z(M(z))\subset E_z,\qquad
 K_z=\kappa_z(T_zB)\subset E_z.
\]

Here e_z is L164's actual derived pullback of the truncation inclusion
j, and kappa_z is L111's actual determinant-fixed KS map. Use L111's
actual alternating trace form Omega_z and incoming differential, L094's
necessary obstruction on the actual base tangent, and L164's symmetric
form B_z with h_0=diag(1,-1). No ordinary middle-base-change isomorphism,
integrability of arbitrary sections, genericity, endpoint, or existence
of F or z is assumed. For Z empty every assertion below is vacuous.

## Conclusion

With orthogonal complements taken in E_z for the indicated form,

\[
 Q_z=K_z^{\perp_{B_z}},\qquad
 Q_z^{\perp_{B_z}}=K_z\subset Q_z,\qquad
 \operatorname{rad}(B_z|_{Q_z})=K_z.                 \tag{1}
\]

In particular the radical has dimension two, the restricted rank is
exactly 48, and the induced symmetric form on Q_z/K_z is nondegenerate
of dimension 48. This identifies the actual radical, rather than only
bounding its dimension as in L164.

For an isotropic subspace T of Q_z one has

\[
 \dim T-\dim(T\cap K_z)\leq24,\qquad \dim T\leq26.   \tag{2}
\]

Apply this to T=rho_z(H) only if its actual bracket pairing vanishes.
Since L164 gives dim rho_z(H)=t, vanishing then requires
t<=24+dim(rho_z(H) intersect K_z). Without identifying that intersection,
this recovers L164's t>26 conditional nonvanishing test and supplies no
unconditional improvement. This lemma does not identify K_z with the
image of the extended tangent summand i(T_zB), evaluate any section
quadric, or establish vanishing or nonexistence of F.

The derivation is a local ADVANCE / REPRODUCTION of the inspected
standard tools. The separate step 567 critical audit below preserves
it (EXPLORATION / REPRODUCTION), without a substantive correction or
stronger conclusion. It gives no primitive Hodge
realization, transport, split-cardinality exclusion or progress beyond
the general sources checked.

## Proof

**Imported identities and exact specialization.** The prior assessment
`drafts/literature/2026-10-26-ordinary-middle-bracket-radical.md` has
DECISION SPECIALIZE for exactly this target. Import finite-dimensional
orthogonal-complement and double-orthogonal identities from Keith
Conrad, *Bilinear Forms*, author-hosted 63-page version, Theorem 3.12
and proof, pp. 18–19
([primary text](https://kconrad.math.uconn.edu/blurbs/linmultialg/bilinearform.pdf#page=18)).
The restricted radical identity is also explicitly recorded in the
arbitrary-field opening section of Akihiro Munemasa, *The geometry of
orthogonal groups over finite fields*, Section 1 and Proposition 1.1,
pp. 3–4
([primary text](https://www.math.is.tohoku.ac.jp/~munemasa/documents/polar.pdf#page=4)).
Only these arbitrary-field identities are imported, not finite-field
results. Both ambient forms here are nondegenerate on a finite-dimensional
complex vector space, and all restrictions and quotients below are in
that space. These general identities need no reproof. The required
specialization is to match the actual maps and check inclusion of K_z.

The actual-family obstruction input is L094, with its precise
Buchdahl–Schumacher citation: *Polystable bundles and representations
of their automorphisms*, Complex Manifolds 9 (2022), 78–113,
DOI 10.1515/coma-2021-0131, Lemma 2.5, Proposition 2.6/(2.4),
Corollary 5.3/(5.1), pp. 83–84,92–93
([primary text](https://d-nb.info/1262812674/34)).
Its fixed real Kähler scope and actual ASD-family bridge are already
established in L094; no algebraic-polarization slice or quadratic
normal form is substituted here.

**Identify the ordinary image using the actual incoming plane.** Fix
regular parameters x,y at z with dual tangent basis u_1,u_2. Write
a_i=kappa_z(u_i) and A=ad(h_0). L111 (7) identifies the actual linear
incoming coefficients with v_i=-A a_i. Its (8) gives

\[
 \Omega_z(a_1,a_2)=2\lambda\sigma_B(u_1,u_2)\ne0.     \tag{3}
\]

In particular K_z has dimension two. Its (9) says the incoming plane
P_z=span(v_1,v_2) is also nondegenerate for Omega_z. L111's actual
local free complex has middle-term decomposition
P_R direct sum P_R^{perp_omega}, with residues of the basis of P_R
equal to v_1,v_2. The ordinary middle module is precisely the second
summand. L164's actual-j comparison identifies its inclusion with j,
before reduction. Thus reduction gives

\[
 Q_z=P_z^{\perp_{\Omega_z}},\qquad P_z=A K_z.         \tag{4}
\]

This equality uses the actual incoming map and the actual reduction of
j, not the dimensions 50 and 52 alone. The unit pairing on P_R makes
its orthogonal decomposition survive reduction. Derived base change
identifies the reduced trace form with the same Omega_z as in (3).
The remaining Koszul directions are retained in E_z; ordinary R^1
base change is not asserted.

L164's stabilizer comparison, with exactly these normalizations, is

\[
       \Omega_z(A\xi,\eta)=2 B_z(\xi,\eta).           \tag{5}
\]

The action is +2 on H^1(L^2) and -2 on H^1(L^{-2}); these are the
same h_0 and split identification used to obtain v_i. Equations
(4)–(5) imply, for q in E_z,

\[
 \begin{aligned}
 q\in Q_z
 &\Longleftrightarrow \Omega_z(Aa,q)=0\ \text{for every }a\in K_z\\
 &\Longleftrightarrow B_z(a,q)=0\ \text{for every }a\in K_z.
 \end{aligned}
                                                               \tag{6}
\]

This proves Q_z=K_z^{perp_B}. Nondegeneracy of the full B_z, established
in L164, and the imported double-orthogonal identity now give
Q_z^{perp_B}=K_z. To find the restricted radical it remains to prove
K_z is contained in Q_z; dimension counting alone would not do so.

**Use integrability only on the actual KS plane.** For a real tangent
t at z, L094's actual-family slice supplies a real harmonic derivative
c(t) and a second derivative d along an actual parameter curve. Its
curvature expansion (2) reads

\[
 \tfrac12 d_A^+ d+(c(t)\wedge c(t))^+=0.             \tag{7}
\]

Here d_A is the covariant differential of the central split connection;
the A in (5) instead denotes the stabilizer operator. On a Kähler
surface, the complex (0,2) component is self-dual.
Taking that component of (7) gives

\[
 c(t)^{0,1}\wedge c(t)^{0,1}
            =-\tfrac12\bar\partial_A d^{0,1}.        \tag{8}
\]

For u=(t-iIt)/2, the actual-family and real/Dolbeault comparisons in
L094 and L111 identify the class of c(t)^{0,1} with kappa_z(u).
Every complex tangent u arises from a real t this way. Hence (8)
says the Yoneda square of every a=kappa_z(u) is zero in H^2(V_z),
and its graded bracket [a,a], which is twice that square, is zero.
L164's split trace computation identifies B_z(a,a) with the normalized
trace of [a,a] paired with h_0. Therefore B_z(a,a)=0 for every a in
K_z. Complex polarization gives B_z(a,b)=0 for all a,b in K_z.

This uses the second derivative of an actual family only on its base
tangent plane. It asserts no extension of a first-order global section
of M. It also does not set the alternating pairing (3) to zero: the
symmetric obstruction form and the alternating Serre form are related
by A, not identified. From (6), B_z|K_z=0 gives K_z subset Q_z.

**Radical, rank and the limit of the test.** The imported restricted
radical identity and (6) now give
rad(B_z|Q_z)=Q_z intersect Q_z^{perp_B}=K_z. Since dim Q_z=50 and
dim K_z=2, the restricted rank is exactly 48. The quotient form on
Q_z/K_z is well defined and nondegenerate because precisely the
radical has been divided out.

For an isotropic T subset Q_z, its image in Q_z/K_z has dimension
dim T-dim(T intersect K_z). It is isotropic for the nondegenerate
48-dimensional quotient. The imported complementary dimension
formula bounds that dimension by 24, proving (2). As dim K_z=2,
the unconditional estimate from this calculation is still 26.
In particular no t<=24 bound follows without controlling the actual
section-image intersection, and even a nonzero bracket does not
contradict existence of the central F. The actual section pairings,
their square length and the complementary global operation remain
undetermined. The exclusions parked in ATTEMPTS/092–094 are not
reopened by this radical identification.

**Separate critical audit, 2026-10-26 (step 567).** The unchanged
invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-26-ordinary-middle-radical-critical-audit.md`
covers this exact audit. Reuse its inspected primary statements and
the canonical input proofs in L094, L111 and L164. In particular the
unitary slice input is Diez--Rudolph, *Normal form of equivariant maps
in infinite dimensions*, Annals of Global Analysis and Geometry 61
(2022), 159--213, DOI 10.1007/s10455-021-09777-2,
[Theorems 4.13, 5.3, 5.8 and Section 5.3, (5.14)--(5.21)](https://link.springer.com/article/10.1007/s10455-021-09777-2#Sec12).
It applies to SU(2) on the compact oriented K3, including its reducible
connection. Buchdahl--Schumacher's cited complex gauge construction is
not substituted for that unitary slice. The real coefficient harmonic
bridge remains L094's audited one for the fixed hyperholomorphic
connection and its parallel skew-adjoint real structure. No new slice
or formality theorem is being proved.

First, check the image of the actual j, not only its dimension. In
L111's stalk complex, write the full incoming column as xa+yb. The
residues of a,b are the actual v_1,v_2, and omega(a,b) is a unit.
Its orthogonal projector onto Ra+Rb is therefore defined over the
stalk. Reduction preserves this projector, so the reduction of its
kernel is exactly span(v_1,v_2)^{perp_Omega}. The complementary
Koszul complex has zero middle cohomology; thus this kernel identifies
with M_R. Because M_R is projective,

\[
 \operatorname{Hom}_{D(R)}(M_R[-1],C_R)
       =\operatorname{Hom}_R(M_R,H^1(C_R)).
\]

The kernel inclusion and the truncation inclusion both induce the
identity on M_R and consequently are the same derived morphism.
Derived restriction of that morphism gives L164's e_z. This proves
(4) with the actual arrows. Different choices of a,b leave the
residual plane fixed. The two residual Koszul middle directions are
still in E_z; this is an injection of dimension 50 into dimension 52,
not an ordinary-base-change isomorphism or a multiplicative splitting.

Second, the incoming sign is fixed by deforming the Dolbeault
differential to bar-partial+epsilon[a_i,-]. Applied to the degree-zero
generator h_0 it gives [a_i,h_0]=-ad(h_0)a_i. Thus the plane is
P_z=A K_z despite the minus signs on its chosen basis. Write
mathcal P for L164's scalar Serre pairing, to distinguish it from
the incoming plane P_z. In split coordinates xi=(x,y), eta=(x',y'),
the same normalized trace gives

\[
 \Omega_z(A\xi,\eta)
   =\mathcal P(2x,y')-\mathcal P(x',-2y)
   =2\bigl(\mathcal P(x,y')+\mathcal P(x',y)\bigr)=2B_z(\xi,\eta).
\]

There is no odd sign from the degree-zero h_0.
The normalized Omega is exactly L111's reduced cup/trace form by
derived base-change compatibility. Its nonzero restriction (3)
makes K_z two-dimensional. These checks give Q_z=K_z^{perp_B} and
Q_z^{perp_B}=K_z by the imported nondegenerate-space identities.
They alone would not give K_z contained in Q_z.

Third, check that the necessary obstruction vanishes on every vector
of this same complex KS plane. L094's unitary gauge fixing applies
to the already smooth actual family: on the complement of the
parallel gauge generators the gauge derivative is d_A^*d_A and is
invertible. The remaining U(1) stabilizer does not prevent a smooth
local gauge choice or a second derivative along an actual real base
curve. Its harmonic first derivative c(t) represents the actual
family deformation. Since (0,2) forms on the Kähler surface are
self-dual, the (0,2) component of the ASD curvature expansion is
exactly (8), including its factor 1/2. The determinant-fixed second
derivative is adjoint-valued. Moreover the square of an odd
endomorphism-valued one-form has zero trace by graded trace cyclicity,
so this exactness is in the trace-free coefficient complex as needed.

The real-to-complex comparison introduces no extra factor. L094's
harmonic bridge gives c(It)^{0,1}=i c(t)^{0,1}; its complex-linear
extension at u=(t-iIt)/2 therefore has (0,1) component c(t)^{0,1}.
L111's actual mixed-curvature comparison identifies its class with
kappa_z(u); a horizontal gauge correction is a Dolbeault coboundary.
Conversely every u in T_z^{1,0}B has t=u+bar(u), so all vectors of
K_z, not just one real subspace of it, are covered. Equation (8)
therefore kills each Yoneda square in H^2(V_z). The graded bracket
is twice that square, and L164's normalized trace against h_0,
with Tr(h_0^2)=2, gives B_z(a,a)=0. Complex polarization gives
B_z(a,b)=0 for every a,b in K_z. This verifies the missing inclusion
K_z subset K_z^{perp_B}=Q_z. It is consistent with nonzero
Omega_z|K_z: the symmetric obstruction uses A in (5), not Omega
alone. No section of H was asserted to integrate.

Finally, the restricted radical is Q_z intersect Q_z^{perp_B}=K_z;
its dimension is exactly two, so the rank is 50-2=48. For isotropic
T subset Q_z, passage to the quotient has kernel T intersect K_z
and isotropic image in a nondegenerate 48-dimensional space. The
imported orthogonal dimension formula gives twice its dimension at
most 48. This verifies (2) and the precise conditional section
inequality using L164's injective evaluation of the full trivial
section summand. It does not replace the unknown intersection by
zero or identify the KS plane with the extended tangent summand.
With that intersection bounded only by two the threshold remains
26. For t=0 the section claim is vacuous, and for Z empty there is
no local radical claim to test. Even a nonzero section bracket
obstructs a deformation, not the central F.

All direct mathematical inputs remain L094, L111 and L164. The audit
finds no substantive error, stronger section bound or evaluated
quadric, and changes no argument or dependency. Its outcome is
EXPLORATION / REPRODUCTION, not a new mathematical advance. The
unknown intersection, section values, complementary operation,
minimum square length and global realization gaps remain open;
ATTEMPTS/092–094 remain in force for their respective mechanisms.

## Mathlib

Full matching coverage of the actual KS/base-change/radical comparison
has not been checked; no absence is claimed. General orthogonal-space
identities are imported by the precise citations above. The application
is an informal exact-map specialization, with no numerical certificate
or formal proof-assistant certification. The separate critical audit
above verifies the stated conditional specialization informally;
it supplies neither formal certification nor a resolution of the main
target.
