# L115 — Global normal connection and conditional split-fibre bound

## Hypotheses

Retain L108/L111/L114's entire conditional equality family. Thus S_1 and
B are the identical marked projective K3 factors with the original common
hyperkähler metric g, Kähler form omega_I and ordered structures I,J,K.
The hypothetical locally free rank-two F on S_1 x B is polystable at the
real product polarization, has integral c_1(F)=0 and

\[
 \operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D.
\]

Retain the full negative mixed tensor and the given compatible unitary
connection; no replacement tensor or metric is allowed. The split set Z
is finite, possibly empty, and U=B minus Z. Put
M=R^1p_*End_0(F). L111 identifies M with its reflexive hull E, as the
specific holomorphic bundle, and gives its rank fifty.

Use L108's actual holomorphic retraction r:E -> T_B and inclusion
i:T_B -> E, with ri=id, P=ir and N=ker r of rank 48. On U their
splitting is the actual parallel metric tangent/normal splitting.
Use L111's integral c_1(N)=0 and corrected budget

\[
 c_2(N)=(800-s)\eta,\qquad s=|Z|,\qquad \int_B\eta=1.
 \tag{1}
\]

Use audited L114's unique smooth positive extension G of the actual
harmonic metric to this M=E and its smooth Chern connection nabla,
ASD for g and equal to the given harmonic connection on U. Do not
assume global parallelness of P, normal semistability, a bound on s,
nonemptiness of Z or existence of F.

## Conclusion

The very projector P is globally parallel and G-orthogonal. Its actual
kernel N inherits a smooth positive Hermitian metric whose Chern connection
is the restriction of nabla and is ASD for the original metric g.
In particular N is slope-polystable, hence semistable, at the unchanged
real Kähler class h, and

\[
                    0\le |Z|\le800.                     \tag{2}
\]

This is a conditional ADVANCE / REPRODUCTION of the assessed known tools.
The separate critical audit below preserves it, with outcome
EXPLORATION / REPRODUCTION and no substantive repair or stronger bound.
The attained threshold is the requested
upper bound. It is compatible with Z empty and supplies no positive lower
bound, exclusion or existence of F, reconstruction, transverse transport,
algebraic cycle or universal Hodge resolution. No equality-case
strengthening is claimed.

## Proof

Use the unchanged prior SPECIALIZE assessment
`drafts/literature/2026-10-17-equality-normal-summand-global-chern-bound.md`.
The necessary standard inputs are Arvid Perego, *Kobayashi-Hitchin
corrispondence for twisted vector bundles*,
[arXiv:1910.01867v1, 4 October 2019](https://arxiv.org/pdf/1910.01867v1):
Lemmas 2.40 and 2.42 and section 2.7, pp. 28--30, for induced Chern
connections and invariant subbundles; Theorem 4.21, p. 65, for HE implying
polystability; Definition 4.20 for semistability of a polystable bundle;
and Corollary 6.42, p. 118, for the arbitrary-rank Chern inequality on a
compact Kähler manifold. Set the twist to one and the auxiliary B-field
to zero. These are ordinary Hermitian metric statements and permit the
given real Kähler form. We only specialize them; no new general extension
or stability theorem is needed.

**The same global projector and connection.** Via the canonical equality
M=E in L111, regard L108's P as a holomorphic, hence smooth, section of
End(M). It is defined at Z before any metric argument. L114 provides
the smooth connection nabla on this same M, not merely on an abstract
gauge extension. Thus its induced covariant derivative

\[
                 \nabla^{End}P\in
                 C^\infty(B,T^*B\otimes End(M))
\]

is a smooth tensor on all B. On U, L114's connection is the actual
harmonic Chern connection. L108 identifies P there with the projector
for L100's parallel tangent/normal splitting under that very connection.
Consequently nabla^End P=0 on U. Since a finite set has dense complement
in B, continuity gives nabla^End P=0 on B.

Likewise P is G-self-adjoint on U. In any smooth frame the entries of
the tensor G(Pv,w)-G(v,Pw) are smooth on B and vanish on U, hence
everywhere. The identities P^2=P and ri=id hold holomorphically on B
by L108. Therefore the global decomposition
M=i(T_B) direct sum N is the G-orthogonal decomposition for this same
P, not a newly selected splitting.

**The actual restricted curvature.** Let n be a smooth local section
of N=ker P. Differentiating Pn=0 gives

\[
 P\nabla n=\nabla(Pn)-(\nabla^{End}P)n=0.
\]

Hence nabla preserves N; it also preserves im P by the analogous
identity. Both second fundamental forms of the orthogonal splitting
are zero. Restriction gives a unitary connection nabla_N for the
smooth positive metric G_N=G|_N. Since N is the holomorphic subbundle
ker r, its restricted (0,1) operator is its given Dolbeault operator.
By Chern uniqueness (equivalently the cited induced-connection result),
nabla_N is exactly the Chern connection of (N,G_N).

There is no residual second-fundamental curvature term: applying nabla
twice to a section of the invariant N gives

\[
               F_{\nabla_N}=F_\nabla|_N.
\]

The base Hodge star acts only on the two-form component, so L114's
ASD identity restricts to *_g F_nabla_N=-F_nabla_N. In the original
complex orientation on the Kähler surface B, omega_I is self-dual.
Thus contraction with omega_I annihilates this curvature,
i Lambda_omega_I F_nabla_N=0. This is the HE equation at the original
metric. Its zero constant also agrees with deg_h(N)=0 from integral
c_1(N)=0. Neither irreducibility nor strict stability is required.
Theorem 4.21 now gives slope-polystability of this N on compact B;
Definition 4.20 gives semistability.

**Compare with the required threshold.** Corollary 6.42 states for a
semistable rank-r bundle on a compact Kähler n-fold that

\[
 \int_B\big((r-1)c_1^2-2r c_2\big)
                  \wedge\omega_I^{n-2}\le0.
\]

Here n=2, r=48>0 and c_1(N)=0 integrally; omega_I^0=1 introduces
no volume or polarization factor. Substitution of (1), retaining its
minus defect sign and normalized point class, gives exactly

\[
       -96(800-s)\le0,\qquad 800-s\ge0,
       \qquad s\le800.
\]

The lower bound s>=0 is only cardinality. If Z is empty the density
arguments are immediate global identities, and the same calculation
has s=0. This completes the bounded conditional application. The
actual smooth-connection input distinguishes it from the reflexivity
shortcut in ATTEMPTS/066, and the curvature inequality is independent
of ATTEMPTS/067's duality-only constraints. ATTEMPTS/063's singular
coarse-metric/degree bridge is unused. All three stops remain intact.
No lower bound contradicting (2), F or Hodge-class realization follows.

**Separate critical audit, 2026-10-17 (step 332).** Use the unchanged
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-17-equality-global-normal-chern-critical-audit.md`.
This is an audit of the application conditional on its direct inputs,
not another proof of removal or an independent audit of every ancestor.
The cited source scope is reused: Perego Lemmas 2.40/2.42, section 2.7,
Theorem 4.21, Definition 4.20 and Corollary 6.42, at the version and
pages specified above. No equality-case theorem is invoked.

First check the identification at the missing points, where an arbitrary
bundle isomorphism would not suffice. L111 proves that the canonical
map M -> M** is an isomorphism; its choice of a local free basis does
not change that map. L108 extends both i and r as morphisms of these
specific bundles, with ri=id. In particular ker P=ker r: one inclusion
is immediate, and Pn=0 implies rn=rPn=0. Thus the bundle denoted N
in the Chern budget is exactly the kernel used for connection restriction.
The rank of P is two everywhere, not just generically, since it is a
retraction onto T_B. There is no rank jump at Z.

L114's audited Hartogs step transports the extended metric and connection
back to this very M using the holomorphic extension of the given punctured
gauge and its inverse. On U it gives the original harmonic metric and
Chern connection. In its stable-chart comparison any parameter-dependent
scalar in a coefficient HE metric cancels in End_0, while the remaining
real/Dolbeault norm factor is one constant on the entire tangent bundle.
It therefore changes no Chern connection. This checks that L108 and
L114 refer to the same whole rank-fifty connection, not merely connections
agreeing on the two-dimensional KS image.

Next check orthogonality rather than identifying a symplectic complement
with a metric complement without hypotheses. L108 constructs its
projector from the actual KS map and nondegenerate Serre form. Its audited
stable comparison identifies that form with a fixed nonzero multiple
of the L2 holomorphic symplectic form. The tangent image is quaternionic
by L100. Consequently its symplectic orthogonal is its Hermitian
orthogonal: pairing with Jw, which remains in the tangent image, recovers
the Hermitian pairing with w. Scalar normalization of the symplectic
form does not affect this kernel. Total geodesy and the metric connection
make the tangent and its orthogonal complement parallel on U. Therefore
the projector in question is both parallel and self-adjoint there.

These identities extend as smooth tensor identities, not by holomorphic
continuation of a possibly singular metric. In a smooth frame on B,
nabla^End P has entries dP+[A,P], with P and A smooth by the preceding
bundle comparison. The adjoint identity has entries in P and the smooth
positive metric matrix G. Both tensors are continuous through Z and
zero on its dense complement. Their values at Z are therefore zero.
No derivative of an unextended harmonic projection, inverse vanishing
Koszul column, or boundedness-to-smoothness inference occurs here.

For the restriction check, write the unitary connection in the now
orthogonal smooth splitting im P plus ker P. For sections t and n in
the two summands, differentiating Pt=t and Pn=0 with nabla P=0 gives
(1-P)nabla t=0 and P nabla n=0 respectively. These are both off-diagonal
connection blocks; hence both second fundamental forms in the cited
Gauss--Codazzi formulas vanish. The lower diagonal block is unitary
for G|_N and has the original holomorphic (0,1) operator because
N=ker r is a holomorphic subbundle. Chern uniqueness identifies it
with nabla_N. Squaring this block gives precisely F_nabla|_N, with
no omitted positive or negative second-fundamental contribution.

The original complex orientation is essential to the next implication.
On this Kähler surface omega_I is self-dual and the Hodge star acts
only on the base-form factor. Restricting the already ASD full curvature
therefore gives an ASD End(N)-valued two-form, orthogonal coefficientwise
to omega_I. Thus i Lambda F_nabla_N=0. Compactness of B, positivity
and smoothness of G|_N, and holomorphic local freeness supply the actual
hypotheses of the cited HE-to-polystability theorem. Ordinary bundles
are its trivial-twist, zero-B-field case. The real Kähler form need
not be integral. Reducible normal holonomy is allowed; strict stability
is neither assumed nor used.

Finally the integral first-class vanishing is inherited from L108's
extended nondegenerate alternating form, not inferred merely from degree
zero. L111's actual hull equality and length-one stalk computation give
w=s and q=0 in the corrected budget. The Chern inequality for n=2 and
r=48 is therefore -2(48) integral_B c_2(N)<=0, since c_1(N)=0 and
omega_I^(n-2)=1. With integral_B eta=1 this is -96(800-s)<=0.
Dividing by the negative coefficient reverses the inequality and yields
s<=800; it cannot yield a lower bound on s. Cardinality supplies s>=0.
No volume factor, exceptional-point multiplicity beyond L111's length
one, or sign from the virtual relative-Ext complex remains to insert.
Z empty satisfies every step; the case s=800 receives no enhancement.

The audit finds no substantive error, new obstruction or stronger result.
Its outcome is EXPLORATION / REPRODUCTION, not another ADVANCE for the
already proved conditional bound and not progress beyond the inspected
known tools. The direct inputs remain L108, L111 and L114. This does
not establish F, exclude F, construct a cycle or close the universal
primitive Hodge gap. ATTEMPTS/063/066/067 remain intact.

## Mathlib

Full matching coverage for this actual relative-Ext projector,
smooth-extension and arbitrary-rank real-Kähler specialization has not
been checked in Mathlib. Unknown coverage is not absence. The proof
uses the precise classical inputs cited above and L108/L111/L114,
with no formal verification claim and no novelty claim beyond the
sources assessed. The separate critical audit above preserves this
conditional specialization; it is not a formal verification claim.
