# L152 — Smooth positive extension of the preferred twisted harmonic metric

## Hypotheses

Retain L147's identical marked projective K3 factors S_1 and B, their
original smooth common hyperkähler metric g and real Kähler class h.
Suppose F on S_1 x B is locally free of rank two, slope-polystable for
Omega=p_1^*h+p_2^*h, with integral c_1(F)=0 and

\[
                 \operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D.
\]

Use its supplied compatible Hermitian connection. Let L have class
k=(-4,-2,1,2), with k.h=0 and k^2=-14. Fix the HE metric h_L specified
in L150 and give L^{-1} exactly the dual metric h_L^{-1}. Give
G=F tensor p_1^*L^{-1} the tensor product metric. Set

\[
 M=R^1p_{2*}G,\qquad U=B\setminus Z,
\]

where Z is the finite, possibly empty, split set. Use L147's ordinary
locally free rank-24 M, L148's natural harmonic L2 metric H on M|_U,
and the audited conclusions of L149, L150 and L151. Neither F nor a
nonempty Z is known to exist. No metric extension is a hypothesis.

## Conclusion

The specified H extends uniquely to a smooth positive definite
Hermitian metric H_ext on the same holomorphic bundle M on B. Its
Chern connection extends the original Chern connection nabla_H and
is smooth and ASD for the original g and complex orientation on B.
At each z in Z, in a sufficiently small coordinate ball D_epsilon,

\[
 \sup_{D_\epsilon\setminus\{z\}}|F_{\nabla_H}|_{H,g}<\infty,
 \qquad
 \int_{D_\epsilon\setminus\{z\}}|F_{\nabla_H}|_{H,g}^2\,
                 d\operatorname{vol}_g\le C_z\epsilon^4.
                                                        \tag{1}
\]

The constants and neighborhoods may depend on the hypothetical F and
z. No uniform estimate over all F is claimed. If Z is empty, the
global extension is simply the already defined smooth H on B.

This is a conditional ADVANCE / REPRODUCTION, a specialization of
known removal and holomorphic extension theorems. The separate critical
audit below preserves the result without a substantive repair or stronger
conclusion. No Chern inequality or split-count bound is evaluated
here. F existence, nonempty Z, a new algebraic Hodge class, transverse
transport and universal primitive Hodge realization remain unresolved.

## Proof

**Imported theorems and scope.** Reuse the unchanged pre-invocation
SPECIALIZE assessment
`drafts/literature/2026-10-23-preferred-twisted-surface-removal.md`.
The removal input is the named Uhlenbeck removable-singularity theorem:
K. Uhlenbeck, *Removable singularities in Yang–Mills fields*,
Comm. Math. Phys. **83** (1982), 11–29,
[Theorem 4.1, p. 24](https://doi.org/10.1007/BF01947068), in the explicit
smooth-curved-metric compact-Lie-group formulation of D. Platt,
*G2-instantons on Resolutions of G2-orbifolds*, Comm. Math. Phys.
**405**, article 81 (2024),
[Appendix A, Theorem A.10](https://link.springer.com/article/10.1007/s00220-024-04947-2#appendices).
The latter formulation assumes a compact Lie group, a trivial principal
bundle over a punctured four-ball, a locally W^{1,2} connection, ASD
for a smooth metric on the whole ball, and finite squared-curvature
integral. It supplies a smooth connection over the ball and a
connection-intertwining principal-bundle embedding from the punctured
bundle. This is the curved-metric theorem used here; the original
flat-coordinate estimates are not substituted for the K3 metric.
Import this standard theorem without reproof. Its compact-group scope
includes U(24). Parker's compact-simple-group formulation and L114's
rank-50 symplectic reduction are not inputs to this application.

For integrability import the named Koszul–Malgrange theorem, in the
smooth Hermitian formulation stated in M. Verbitsky, *Deformations of
trianalytic subvarieties of hyperkahler manifolds*,
[alg-geom/9610010v1, Section 2.2, Theorem 2.7](https://arxiv.org/html/alg-geom/9610010).
A smooth connection whose (0,2) curvature is zero defines a holomorphic
structure by its (0,1) operator. For scalar holomorphic extension use
the named Hartogs theorem in J.-P. Demailly, *Complex Analytic and
Differential Geometry*, version 21 June 2012, Chapter I, Section 3.D,
[(3.28)](https://www.ime.usp.br/~cordaro/wp-content/uploads/2022/03/Jean-Pierre-Demailly-Complex-Analytic-and-Differential-Geometry-1.pdf).
Its ball-minus-point case in complex dimension two imposes no growth
bound. The remaining argument checks these imported inputs on the
actual metric and the specified bundle, rather than reproving them.

**The same preferred metric in every input.** L148 permits one fixed
smooth positive twisting metric and defines H by its natural harmonic
higher-image identification. Choose precisely h_L^{-1}. L149 also
permits that choice and expresses its actual harmonic metric in the
extending rank-24 frame as

\[
 H(w)=C(w)-\frac{B(w)^*ww^*B(w)}{w^*A(w)w}.
                                                        \tag{2}
\]

The full cutoff metric with blocks A,B,C is smooth positive at zero.
L150, including its natural central comparison, says B(0)=0 at every
actual split point for exactly this twisting metric. Its comparison
is an equality up to a positive constant on each split fibre, not a
replacement by an arbitrary weight or a varying base metric. Thus
L149's already audited sufficient direction applies to (2): all first
and second derivatives of the actual H are bounded on a full punctured
ball and its actual Chern curvature is uniformly bounded there. L148
identifies the frame and the harmonic metric and supplies the uniform
inverse bounds used in that criterion. No new quotient estimate or
assumption of a metric limit is needed.

L151 uses the very same h_L^{-1}, tensor metric on G, natural harmonic
identification and base metric. Its conclusion is ASD for this Chern
connection, including its full unitary central part. It is not merely
an ASD equation for an abstract isomorphic holomorphic bundle.

Fix z and shrink a complex coordinate ball containing no other member
of Z so that all these estimates hold. Write its coordinate radius
as epsilon. If the curvature bound is K_z and the smooth volume
density of g is at most V_z relative to Euclidean volume on the ball,

\[
 \int_{D_\epsilon\setminus\{z\}}|F_{\nabla_H}|_{H,g}^2\,
  d\operatorname{vol}_g
 \le K_z^2 V_z\operatorname{vol}_{\mathbb R^4}(D_\epsilon)
 =K_z^2 V_z\frac{\pi^2}{2}\epsilon^4.
                                                        \tag{3}
\]

This proves (1) and finite energy; shrinking also makes this energy
arbitrarily small if needed. On U the connection is smooth and
Bianchi gives d_nabla F_nabla=0. Since *_g F_nabla=-F_nabla,

\[
 d_\nabla^*F_\nabla=-*_g d_\nabla *_gF_\nabla
                         =*_g d_\nabla F_\nabla=0.
                                                        \tag{4}
\]

Thus differential Yang–Mills holds as well; no HE terminology is used
in place of that equation. Away from the finitely many balls the
connection is smooth on a compact set, so its energy on U is finite.

**Unitary removal on the original curved ball.** Trivialize the actual
holomorphic M on a smaller ball by L147. In that frame H is a smooth
positive Hermitian matrix on the puncture. Its unique positive square
root and inverse are smooth there. Multiplying the holomorphic frame
by H^{-1/2} gives a smooth H-unitary frame on the entire punctured ball:
(H^{-1/2})^*H H^{-1/2}=I. No value of that frame at z is asserted.
This explicitly trivializes its principal U(24)-bundle without a
clutching or determinant-triviality assumption.

In this unitary frame nabla_H is a smooth u(24)-valued connection, hence
locally W^{1,2} on the puncture. The actual curvature norm there is the
standard invariant unitary norm used in (3), up to a fixed harmless
normalization. The metric g is smooth on the whole four-ball. ASD is
L151's equation for that g, and (3) is its finite curvature energy.
Every hypothesis of Platt A.10 is therefore met with G=U(24). Obtain
a smooth extended principal U(24)-bundle and connection on a smaller
ball, and a connection-intertwining principal-bundle embedding on its
puncture. Over each punctured base point, equivariance makes that map
an isomorphism of U(24)-torsors. Its associated complex bundle E_tilde
has a smooth positive Hermitian metric H_tilde and a smooth unitary
connection nabla_tilde, with a punctured isometric isomorphism

\[
 \Phi:(M,H,\nabla_H)|_{D^*}\longrightarrow
               (E_{\rm tilde},H_{\rm tilde},\nabla_{\rm tilde})|_{D^*}.
                                                        \tag{5}
\]

The embedding is understood in the smooth principal-bundle category.
The weak/continuous gauge representatives in the removal proof cause
no punctured regularity problem either: in any relatively compact
punctured patch with smooth connection matrices a,a_tilde their
intertwining matrix u satisfies
du=u a-a_tilde u. A continuous solution has continuous weak first
derivatives, hence is C^1; the same equation then inductively gives
all derivatives. Starting with the bounded unitary Sobolev gauge,
this equation first gives W^{1,p}_loc for all finite p and continuity
for p>4, followed by the same induction. This is a local regularity
check for the comparison, not a reproof of removal or an assertion
about its limit in the original frame at z.

ASD of nabla_tilde holds on D^* by (5) and therefore at z by smooth
continuity of its curvature and the original Hodge star. In particular
F_nabla_tilde^{0,2}=0: on a Kähler surface an ASD two-form is primitive
(1,1), coefficientwise. Koszul–Malgrange supplies the holomorphic
structure bar-partial_E=nabla_tilde^{0,1} on E_tilde. Its metric and
connection remain smooth positive and unitary. Intertwining in (5)
now shows that Phi and Phi^{-1} are holomorphic on D^* for the given
holomorphic structure on M and this one on E_tilde.

**Both inverse matrices and positivity on M.** Shrink to a complex
coordinate ball on which both holomorphic bundles have frames through
z. The punctured isomorphism Phi is a holomorphic 24 by 24 matrix Q;
its inverse is a holomorphic matrix R on the same puncture. Apply
Hartogs entrywise to both, obtaining holomorphic Q_ext and R_ext on
the ball. Their products restrict to the identity off z, so the
identity theorem gives

\[
              Q_{\rm ext}R_{\rm ext}=I,
              \qquad R_{\rm ext}Q_{\rm ext}=I
                                                        \tag{6}
\]

everywhere. Thus the extended map Phi_ext:M -> E_tilde is invertible
at z as well. This step requires both matrices; a single extended
matrix alone would not establish positivity of the transported metric.

Define H_ext=Phi_ext^*H_tilde and transport nabla_tilde by Phi_ext.
In the chosen frames its metric matrix is Q_ext^* H_tilde Q_ext,
which is smooth and strictly positive at every point by (6). The
transported connection is smooth, unitary for H_ext and has the
original bar-partial_M operator because Phi_ext is holomorphic. Chern
uniqueness identifies it with the Chern connection of (M,H_ext).
Equation (5) says that both metric and connection agree with the
original H and nabla_H on D^*. The transported connection is ASD for
the same g by the already proved ASD of nabla_tilde.

Perform this construction at each of the finitely many z. Any two
smooth extensions on an overlap agree on its dense complement of Z
and therefore agree everywhere, for both metrics and connections.
They glue with H on U and are unique. If Z is empty no construction
is necessary. Nonzero c_1(M)=-4k is retained throughout; local U(24)
removal requires no global determinant trivialization.

**Scope of the result.** The required threshold is met conditionally:
the specified harmonic metric extends smoothly and positively onto
the specified ordinary M. This uses actual central orthogonality,
curvature energy and an applicable surface theorem, so it does not
revive the reflexivity-only inference in ATTEMPTS/066 or the singular
coarse-metric inference in ATTEMPTS/063. ATTEMPTS/086 still concerns
the arbitrary other twisting metric. No real or symplectic reduction
of G or M, whole-base IT, extension of a jumping harmonic projector,
limit of the original removing gauge, nonempty Z or kernel existence
has been used. A later Chern inequality is outside this result. The
separate critical audit is recorded below; the universal Hodge gap remains
unchanged.

**Separate critical audit, 2026-10-23 (step 493).** Reuse the unchanged
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-23-preferred-twisted-removal-critical-audit.md`.
The verdict is EXPLORATION / REPRODUCTION: the specified metric extension
and (1) survive. No substantive error, necessary repair or stronger
conclusion was found. This checks a known-theorem specialization, not
progress beyond the inspected sources. The imported removal theorem,
Koszul–Malgrange and Hartogs retain the precise citations above. The
published Platt A.10 statement was rechecked for this application; no
new source coverage or general removal reproof is asserted.

First, the metric choices match as actual metrics. L148 allows any one
fixed smooth positive metric on the twisting line. Substituting exactly
h_L^{-1} leaves its natural cohomology identification and extending frame
unchanged. Audited L150 identifies the central P and J as orthogonal for
this choice through that same comparison; it does not merely choose a
new Hermitian complement. Its positive constant comparison is on each
central fibre and is sufficient for B(0)=0 there. No base-dependent
rescaling of H enters. Audited L149's sufficient direction then bounds
the first and second derivatives of (2) on a whole punctured ball.
L148 gives c I <= H <= C I in the extending frame, hence also
C^{-1} I <= H^{-1} <= c^{-1} I. The original smooth g and its inverse
are uniformly bounded relative to the coordinate Euclidean metric
on a smaller closed ball. Consequently bounded matrix curvature
coefficients imply bounded curvature in the actual End(M,H) tensor
exterior-two-cotangent norm. In detail, for each endomorphism coefficient
T its H-Hilbert–Schmidt norm is the Euclidean Hilbert–Schmidt norm of
H^{1/2} T H^{-1/2}; both factors are uniformly bounded. The form-slot
norm comparison is supplied by g. These checks include the full central
unitary curvature, not only its trace-free part.

L151 explicitly identifies the transform connection with the Chern
connection of this very (M|_U,H), using the same tensor metric and fibre
volume. Its ASD equation is for the original g, with complex orientation.
Thus the bound and the ASD equation hold for one connection. Fixing a
ball on which the curvature bound K_z and volume-density bound V_z hold
makes both constants independent of every smaller radius epsilon.
The four-real-dimensional Euclidean volume is pi^2 epsilon^4/2, so
(3) proves the stated O(epsilon^4) energy with the actual metric and
volume. The removed point has measure zero. Smoothness on the compact
complement of finitely many smaller balls proves the remaining energy
is finite. No global uniform constant over hypothetical kernels is used.

Second, the unitary trivialization and theorem hypotheses match.
For the anti-linear first Hermitian slot, the frame change H^{-1/2}
has Gram matrix exactly I and is smooth everywhere on the puncture.
It trivializes the actual U(24) bundle without extending that frame
through z. In this frame the connection is smooth, so its coefficients
are W^{1,2} on each relatively compact punctured patch. Platt A.10
requires precisely this local Sobolev condition, finite curvature
energy, compact G, and ASD for a metric smooth on the entire ball.
It does not require finite connection-coefficient norm in this frame
at the missing point, a simple group, or zero determinant class.
All its hypotheses therefore hold. Its bundle homomorphism covers the
identity; a nonempty equivariant map between U(24)-torsors is onto and
one-to-one on each fibre. The associated vector-bundle map (5) is
accordingly an isometric isomorphism on the puncture.

The alternative weak-gauge paragraph is also valid locally on the
puncture. In smooth unitary frames the intertwining equation is
u a=du+a_tilde u. A unitary weak representative has bounded matrix
entries. On a relatively compact punctured patch, a and a_tilde are
smooth and bounded; the equation therefore makes every distributional
first derivative of u bounded, in particular in L^p for every finite p.
Sobolev embedding with p>4 gives a continuous representative. The same
equation now gives continuous first derivatives, hence C^1 regularity;
induction gives smoothness. This argument uses no estimate at z and no
extension or limit of the original removing gauge. The smooth-category
interpretation of A.10 already suffices for (5); neither A.11 nor A.12
adds a missing hypothesis.

Third, smoothness and the same Hodge star extend the ASD identity to
the center. With the retained Kähler complex orientation, the
anti-self-dual real two-forms are exactly the primitive real (1,1)
forms. Complexifying coefficientwise gives zero (0,2) curvature of
the extended unitary connection, so Koszul–Malgrange applies. The
punctured intertwiner then commutes with both (0,1) operators, and its
inverse does too. This verifies holomorphicity for the given M and
the newly integrable E_tilde before Hartogs is invoked.

Finally, both bundles admit holomorphic frames on a sufficiently small
ball about z. Hartogs extends every entry of Q and R with no growth
hypothesis in complex dimension two. Each entry of Q_ext R_ext-I and
R_ext Q_ext-I is holomorphic and zero on the puncture, hence zero on
the ball. In particular Q_ext is invertible at z. For every nonzero
vector v there, (Q_ext v)^* H_tilde (Q_ext v)>0, which verifies strict
positivity of the transported metric on the specified M. Unitarity
and the unchanged holomorphic (0,1) operator identify the transported
connection as its Chern connection. Agreement with H on the puncture
is an isometry statement, not just a holomorphic-bundle identification.
Density proves uniqueness and compatibility of all local constructions;
empty Z requires none. No reflexivity-only inference is used.

The direct mathematical inputs remain L147, L148, L149, L150 and L151;
no dependency or argument change is needed. ATTEMPTS/063/066/086 remain
valid within their recorded scopes. This audit evaluates no Chern
inequality or split count and supplies no F, nonempty Z, cycle or
transport. Universal primitive Hodge realization remains unresolved.

## Mathlib

Full matching Mathlib coverage of compact-unitary ASD point removal
on a smooth curved four-ball and this natural metric extension on the
specified higher image is **not checked**. No matching theorem or
absence is asserted. Uhlenbeck/Platt, Koszul–Malgrange and Hartogs
are imported known inputs with the precise scope above; the energy,
frame, gauge and two-inverse transport checks are their local
specialization. This is an informal REPRODUCTION with no claim of
originality or Lean verification. The separate critical audit above
preserves the conditional extension with no stronger conclusion.
