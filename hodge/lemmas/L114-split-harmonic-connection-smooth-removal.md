# L114 — Smooth removal for the actual split harmonic connection

## Hypotheses

Retain audited L111/L113's conditional family on p:S_1 x B -> B,
with identical marked projective K3 factors, their original smooth
hyperkähler metrics and ordered structures I,J,K. In particular F is
hypothetical, locally free of rank two, polystable at the real product
polarization, with integral c_1(F)=0 and
ch_2(F)=-14e_1-21e_2-tau_D. Retain the full negative tensor, its action
D[sigma]=2lambda[sigma], 1<lambda<5/4, and its given compatible unitary
connection. Set M=R^1p_*End_0(F)=M**, a holomorphic bundle of rank fifty
by L111. The split locus Z is finite and possibly empty; put U=B minus Z.

Give M|_U its actual fibrewise harmonic Hermitian L2 metric G from the
given coefficient and fibre metrics, as in L113, and let nabla be its
Chern connection. Use L100's audited actual stable coarse/connection
charts, quaternionic classifying map and fixed positive L2 normalization,
and L108's natural whole relative-Ext descent. No extension, differential
Yang--Mills equation, group reduction, semistability, bound on |Z|,
existence of F or nonempty Z is assumed.

## Conclusion

The metric G and its Chern connection extend smoothly across every
z in Z on the specific holomorphic bundle M. The extended metric is
positive definite and agrees with G on U. The extended connection is
ASD for the original base metric, hence is of type (1,1) for every
induced complex structure on B. The extension on M is unique.

This is a conditional ADVANCE / REPRODUCTION of the previously assessed
removal theorem and tangent inputs. The separate critical audit below
preserves the result (EXPLORATION / REPRODUCTION), finding no substantive
error or stronger conclusion.
It proves no semistability statement, cardinality bound, existence of F,
algebraic cycle or transverse transport. Universal primitive rational
Hodge realization remains unresolved. For empty Z no removal is needed.

## Proof

**Imported results and the bounded specialization.** Use the unchanged
prior SPECIALIZE assessment
`drafts/literature/2026-10-16-split-harmonic-connection-removability.md`.
Import Thomas H. Parker, *Gauge theories on four dimensional Riemannian
manifolds*, Comm. Math. Phys. **85** (1982), 563--602,
DOI 10.1007/BF01403505,
[Theorem 8.1 and proof, p. 600](https://users.math.msu.edu/users/parker/GaugeTheories_parker.pdf#page=38).
It removes an isolated singularity of a smooth finite-energy solution
of his equations (2.5) or (2.6) on a smooth four-dimensional Riemannian
base, with the stated mass regularity p>2. We use zero particle field
and identically zero mass, so the remaining equation is differential
Yang--Mills, D_A^*F_A=0, and the energy is curvature-square energy.
Retain his section 2 compact-simple structure-group scope, pp. 574--577,
Definition 3.1/(3.5), p. 581, and the curved-metric regularity cases
in Theorem 5.3 and Theorems 7.7--7.8, pp. 586, 598--600.
No gauge-removal theorem is reproved here.

Import Verbitsky, *Deformations of trianalytic subvarieties of
hyperkahler manifolds*,
[alg-geom/9610010v1, section 2.2, Example 2.9(i), Theorem 2.7,
Proposition 2.13/Lemma 2.14, and section 5.1](https://arxiv.org/html/alg-geom/9610010).
These supply the hyperholomorphic Levi--Civita tangent connection,
its restriction and smooth integrability from (1,1) curvature.
The surface orthogonality input is also
[Verbitsky, *Hyperholomorphic bundles*, alg-geom/9307008v1,
section 2, Lemma 2.1 and Theorems 2.3--2.4](https://arxiv.org/html/alg-geom/9307008).
For extending holomorphic matrix entries import the named Hartogs
extension theorem, in the precise ball-minus-point case of
[Demailly, *Complex Analytic and Differential Geometry*, 21 June 2012,
Chapter I, section 3.D, (3.28)](https://www.ime.usp.br/~cordaro/wp-content/uploads/2022/03/Jean-Pierre-Demailly-Complex-Analytic-and-Differential-Geometry-1.pdf).
The work below checks the actual connection, group and holomorphic
identification required by these imports.

**The whole Hermitian holomorphic tangent pullback.** Fix a parameter
in U and shrink to a neighborhood O in U as needed. L100 constructs
an actual smooth hyperkähler connection-moduli chart T with metric
G_T and a natural holomorphic comparison with the common-H stable
coarse germ. The actual family map phi:O -> T is holomorphic for I
and has dphi L=L_T dphi for L=I,J,K. This concerns the actual restricted
connections, not merely their abstract deformation spaces.

The stable Quot slice in L100 carries a locally free holomorphic
family Q. Pull it back along the actual local classifying map. On
each fibre Q and F are isomorphic stable bundles. As in L108's
descent proof, the relative Hom has constant h^0=1, so base change
makes its degree-zero direct image a line bundle ell. Evaluation
gives an isomorphism Q tensor p^*ell -> F on this local product:
on every fibre it is a nonzero map between isomorphic stable bundles,
hence an isomorphism; the determinant is therefore nowhere zero.
Conjugation cancels ell and scalar choices. Natural relative Ext
and the actual slice tangent theorem give a holomorphic isomorphism

\[
              Psi:M|_O\ \simeq\ phi^*T^{1,0}_I T.       \tag{1}
\]

This is an isomorphism on all fifty complex directions, not only
on the two-complex-dimensional KS image. Its holomorphicity is the
relative-Ext comparison for the actual local family; a pointwise
choice of harmonic representatives alone would not establish it.

The End metric in this comparison is also the actual one. The
restricted given coefficient connection is HE at the fixed h.
HE uniqueness for each stable fibre identifies its metric with
the one used in the connection chart up to a positive scalar on
that fibre. Scalars cancel in the induced End_0 metric. The fibre
metric and its volume are unchanged. Thus the entire harmonic
pairing on M, and not just its KS restriction, equals the pullback
tangent metric up to one fixed positive normalization c:

\[
                   Psi^*h_T=cG,\qquad c>0.              \tag{2}
\]

The constancy is explicit in L100: for a real skew-adjoint harmonic
one-form a and b=a^{0,1}, the real norm is twice the ordinary
Dolbeault norm and its normalized tangent norm is
(2pi^2)^(-1) integral |b|^2. Passing to a chosen associated Hermitian
tangent convention contributes only a fixed numerical factor.
There is no parameter-dependent metric rescaling in (2).

The Levi--Civita connection of the Kähler metric on T is its tangent
Chern connection. Pulling it back along the I-holomorphic phi gives
the Chern connection of (phi^*T^{1,0}_I T,phi^*h_T). Chern uniqueness
and constant c in (2) identify this pullback with nabla on M|_O.
This does not identify nabla with an unproved coefficient pushforward
connection or with a connection defined only on the KS image.

**Parallel compact-simple reduction and the actual equation.** On the
hyperkähler tangent bundle of T, J_T is parallel and antiunitary for
I, with J_T^2=-1. Through (1)--(2) it yields a nabla-parallel
antiunitary operator on all of M|_O. These operators agree on overlaps:
the charts classify the same unitary connections and their tangent
changes preserve the natural harmonic quaternionic structure and
the fixed L2 normalization. The relative-Ext transitions just used
are the same natural tangent transitions. Base-line twists and
scalars act trivially on End_0. Thus this produces a global parallel
quaternionic Hermitian structure on M|_U.

Its unitary quaternionic frames form a principal Sp(25) bundle.
Equivalently, the compatible complex symplectic form obtained from
J_T,K_T and the actual metric is parallel; any constant change in
(2) scales this form compatibly. Compact Sp(25) has simple Lie algebra
and is a compact simple group in the Lie-group sense of Parker's
scope. No irreducibility of nabla is needed. We have not applied his
theorem to U(50) or to an arbitrary reductive group.

The imported tangent connection is hyperholomorphic. For its
curvature R_T and real base vectors u,v, quaternionic linearity of
dphi gives, for each L,

\[
 F_{\nabla}(Lu,Lv)
 =R_T(L_Tdphi(u),L_Tdphi(v))
 =R_T(dphi(u),dphi(v))=F_{\nabla}(u,v).                  \tag{3}
\]

Consequently the actual curvature is of type (1,1) for I,J,K on
the source. On its hyperkähler four-manifold with complex orientation,
the three Kähler forms span the self-dual two-forms. Being (1,1)
for J and K makes an I-(1,1) form orthogonal to omega_I as well;
equivalently the intersection of these three (1,1) spaces is the
anti-self-dual space. Applying this coefficientwise to (3) gives

\[
                    *_g F_{\nabla}=-F_{\nabla}.         \tag{4}
\]

This is stronger than merely naming the Hermitian contraction
equation Yang--Mills. Bianchi gives D_nabla F_nabla=0, so in real
dimension four D_nabla^*F_nabla=-*D_nabla*F_nabla=0.
It is the differential equation Parker requires, with the original
smooth curved base metric g.

**Apply removal.** Fix z in Z and choose a full ball D about it
containing no other split point. On D*=D minus {z}, nabla is a smooth
Sp(25) connection satisfying that differential equation. L113 gives

\[
 \int_{0<|b-z|<\epsilon}|F_{\nabla}|^2\,dVol_g
                    \le K\epsilon^4<\infty.             \tag{5}
\]

The standard representation trace norm and any invariant positive
Lie-algebra norm used by Parker differ only by a constant on the
simple compact Lie algebra, so finiteness is unchanged. Choose zero
particle and zero mass; the mass has every required Sobolev regularity
for any p>2. This checks the field, equation, energy, dimension,
smooth metric and group hypotheses, rather than importing removal
from boundedness of G alone.

There is no local principal-bundle obstruction if a punctured
trivialization is used in expressing Parker's theorem. The punctured
ball retracts onto S^3; the clutching classification gives principal
Sp(25) bundles there by pi_2(Sp(25))=0. For completeness this last
group is zero from Sp(1)=S^3 and the usual sphere fibrations
Sp(n-1) -> Sp(n) -> S^(4n-1): their homotopy exact sequence preserves
pi_2=0 for n>=2. This elementary group-scope check supplies no new
removal theorem.

Parker Theorem 8.1 now gives a smooth extended principal bundle and
connection on a smaller D, together with a smooth unitary gauge
isomorphism over D*. Let (E_tilde,G_tilde,nabla_tilde) be its associated
complex Hermitian bundle. The metric is smooth positive definite
and the gauge isometry identifies its connection and metric with
the original ones on D*. By continuity (4) remains true at z.

**Identify the extension with the specific holomorphic M.** ASD implies
F_nabla_tilde^(0,2)=0 for I everywhere on D. Smooth integrability
(the imported Theorem 2.7, equivalently Koszul--Malgrange) equips
E_tilde with the holomorphic structure nabla_tilde^(0,1). The gauge
isomorphism over D* intertwines the two (0,1) operators, because
nabla was the Chern connection of M. It is therefore a holomorphic
bundle isomorphism there, not just a smooth isomorphism.

Shrink D again to choose holomorphic frames of E_tilde and of L111's
locally free M, both through z. In these frames the isomorphism has
a holomorphic matrix A on D*, and its inverse has a holomorphic
matrix B on D*. Hartogs extends every entry of both matrices across
the point, since D has complex dimension two. On D* one has AB=BA=I.
The identity theorem extends these equalities to D. Thus the extended
A is invertible at z and gives a holomorphic isomorphism on D.
Extending only A, without its inverse identities, would not suffice.

Transfer G_tilde and nabla_tilde by this holomorphic isomorphism to M.
The metric remains smooth and positive and equals the original G
on D*. The transferred connection remains unitary, has the given
holomorphic (0,1) operator and equals nabla on D*. By Chern uniqueness
it is exactly the Chern connection of the extended metric on M.
ASD is preserved under this transfer and, on a hyperkähler surface,
implies type (1,1) for every induced structure. Smooth metric
extensions on the fixed M agreeing on D* agree by continuity; their
Chern connections therefore agree. The local extensions consequently
glue uniquely to the original metric and connection on U.

The exact local threshold is met: smooth positive metric and smooth
actual connection on M, not an unidentified gauge bundle. Neither
ordinary middle base change at a split point nor extension of a
jumping harmonic projection has been used. ATTEMPTS/063/066/067
retain their scopes; the new input beyond their stops is L113's
actual energy together with the verified equation and group. No
semistability or numerical Chern inequality is asserted in this step.

**Separate critical audit, 2026-10-17 (step 328).** Use the unchanged
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-16-split-connection-removal-critical-audit.md`.
The target is the extension on the specified M, conditional on the
stated inputs, not existence of F or a fresh audit of every ancestor.
The following verifies the four bridges independently of the eventual
normal-summand application.

First, fix a stable parameter and distinguish the slice family Q on
the full moduli chart from its pullback Q_O to S_1 x O. The slice KS
map is an isomorphism from its tangent bundle to relative Ext^1:
it is the natural tangent map of Huybrechts--Lehn 4.5.1--4.5.4,
applied at every point of the smooth stable chart. L100's actual
analytic comparison carries this same map into the harmonic tangent.
For Hom(Q_O,F), stable-fibre isomorphism gives h^0=1 on all of O.
Proper cohomology and base change gives the line of relative maps;
evaluation identifies Q_O tensor that line with F. The induced
End_0 isomorphism and its relative degree-one cohomology are canonical:
replacing an evaluation by a scalar does not change conjugation.
This identifies the entire fifty-dimensional Ext^1, whereas the
derivative of O into the chart has only two complex dimensions.
No surjectivity of that latter derivative is claimed or needed.

At each stable fibre an isomorphism of the holomorphic coefficient
bundles carries one HE metric to a positive scalar multiple of the
other. Even if this scalar varies with the parameter, it cancels
pointwise in the End_0 metric and hence in its fibrewise Laplacian
and harmonic pairing. A base line has no vertical connection term.
For every real skew-adjoint harmonic a, not only for a in the KS
image, a=b-b^*, b=a^(0,1), gives ||a||^2=2||b||^2. L100 uses the
same trace, fibre volume and fixed real normalization on every chart.
Thus (2) has one numerical constant c; there is no residual function
whose derivatives could change the Chern connection. Holomorphicity
of (1) comes from relative Ext, so equality of Hermitian metrics up
to this constant really does identify their Chern connections.

For the overlap check, a coefficient identification can be made
unitary at each fibre by a scalar; its conjugation on End_0 is
unchanged by that adjustment. On real harmonic forms the quaternionic
operator is L_c a=-a composed with L, for the fixed ordered triple
on S_1. Unitary coefficient conjugation commutes with L_c and carries
the covariant differential and its adjoint to those of the other
connection. It therefore carries harmonic representatives to harmonic
representatives while preserving L_c and the trace norm. These are
the actual tangent transition maps just obtained from relative Ext.
They do not admit an additional rotation of the ordered triple or
a scalar phase on Ext^1. Via the real/complex tangent identification,
J_c is anti-linear for I_c, squares to -1 and is antiunitary.
Its chartwise parallelness for the tangent Chern connection therefore
descends to M|_U. This checks a genuine Sp(25) reduction of the full
connection, including any reducible holonomy, rather than a reduction
only on the KS subbundle.

Next check curvature and removal separately. Pullback of the tangent
Chern connection along the I-holomorphic map has curvature phi^*R_T.
The quaternionic differential and the imported type (1,1) identity
for R_T give (3) coefficientwise. In complex orientation on a
hyperkähler surface the self-dual space is the span of omega_I,
omega_J,omega_K; the simultaneous real (1,1) subspace is its
orthogonal complement. Thus the same connection is ASD for g.
The covariant Bianchi identity then gives D_nabla^*F_nabla=0, with
the curved Hodge star of g. There is no flat-coordinate assumption
or substitution of the Hermitian contraction equation for the
differential Yang--Mills equation.

Rechecked Parker's section 2, equations (2.5)--(2.6), Theorem 7.8
and Theorem 8.1 with its proof in the cited published paper. Use
the boson case with zero field, zero mass and zero quartic coefficient;
its field equation is identically satisfied and its connection
equation is exactly the one just verified. The required mass-square
regularity holds for every p>2. Compact Sp(25) has simple Lie algebra;
its finite center is not a forbidden connected normal factor.
L113 bounds curvature in the faithful standard-representation norm,
which is a fixed positive multiple of the invariant Lie-algebra norm.
Its K epsilon^4 bound therefore supplies the required finite energy
on the original smooth four-manifold. No irreducibility or uniform
constant over different hypothetical families is required.

The punctured topology is also consistent with that application:
bundles on S^3 are classified by pi_2(Sp(25)). In the sphere fibration
used above, pi_2 and pi_3 of S^(4n-1) both vanish for n>=2.
The exact sequence therefore identifies successive pi_2 groups,
starting with pi_2(S^3)=0. This is a triviality check on the puncture,
not a choice of instanton number or an assumption that its given
connection already extends in its original smooth frame.

Finally, Parker initially expresses removal in a continuous gauge
with smooth extended connection coefficients. On any relatively
compact coordinate patch of D*, the gauge intertwines two smooth
connections. Its first-order gauge equation has smooth coefficients;
the weak gauge from the removal proof consequently bootstraps there
to a smooth isomorphism. Equivalently it intertwines smooth local
parallel transports. No regularity of this gauge at z in the original
frame is needed. The compact-group gauge is unitary, so its associated
Hermitian metric is precisely G on D*.

ASD of the extended connection persists by continuity and implies
vanishing (0,2) curvature. The cited Verbitsky Theorem 2.7 provides
its holomorphic structure. The punctured gauge then intertwines
the (0,1) operators, so it and its inverse are holomorphic. Choose
a smaller complex coordinate ball inside the removal neighborhood
on which both holomorphic bundles have frames; L111 supplies the
frame of M through z. Hartogs applies to every entry of both
matrices, with no boundedness hypothesis. Their products extend
as holomorphic matrices and equal the identity on the puncture,
hence everywhere. In particular no determinant can acquire a zero
at z. If A denotes the extended map from M to E_tilde, the transported
metric has matrix A^* G_tilde A; invertibility of A at z proves
positive definiteness there. The transported connection has M's
(0,1) operator and is unitary, so is its Chern connection. Equality
on the dense puncture gives uniqueness and local gluing.

These checks preserve the original conditional conclusion and direct
inputs L100, L108, L111 and L113. No repair, stronger obstruction or
existence statement was found; the audit is EXPLORATION / REPRODUCTION,
not a second advance or a new theorem beyond the cited tools.
For Z empty the original smooth stable-open connection is already
global. ATTEMPTS/063/066/067 retain their separate failed mechanisms.
No semistability, cardinality bound, F, cycle or transport is proved
by this audit, and the universal primitive Hodge gap is unchanged.

## Mathlib

Full matching Mathlib coverage for this actual harmonic tangent
comparison, Sp(25) gauge removal and holomorphic metric identification
has not been checked. The named analytic inputs are the precise
Parker, Verbitsky and Hartogs results cited above. This is an informal
specialization of known tools preserved by the separate audit above,
not a formal verification, a novelty
claim or a candidate resolution of the Hodge conjecture.
