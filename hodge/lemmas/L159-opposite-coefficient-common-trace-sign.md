# L159 — Opposite-coefficient harmonic maps exclude the two extremal branches

## Hypotheses

Retain exactly L158's conditional data and z=0. Thus X=S_1 x S_2 has
identically marked projective K3 factors, the common hyperkähler metric
and triple (I,J,K), real class h, and preferred HE lines L_1,L_2 of
class k=(-4,-2,1,2), with k.h=0 and k^2=-14 eta, integral eta of degree
one. The hypothetical locally free Omega-polystable rank-two F has
integral c_1=0 and

    ch(F)=2-14e_1-21e_2-tau_D+62e_1e_2,
    Omega=h_1+h_2.

Use L071's actual compatible unitary hyperholomorphic connection on F,
L157's preferred dual line connections, and L158's actual degree-one
edges in both directions, determinant cups and quartic identity. In
particular these retain L147's M,W, with W=0 at z=0; no positive-z
concentration is assumed. Write

    T_s=p_1^*L_1^e tensor p_2^*L_2^d,
    Q_s=F tensor T_s,    V_s=H^1(X,Q_s),    s=(e,d) in {+1,-1}^2.

The tested formal branches have (a,b)=(m_-1,m_1)=(12,2) or (6,8).
They give dim(V_--)=dim(V_++)=b and dim(V_-+)=dim(V_+-)=a.
No twist Q_s is assumed to have its own parallel real structure.

## Conclusion

There are natural anti-linear isomorphisms, for the fixed metric and
one normalized determinant trivialization,

    R_s:V_s -> V_-s,             R_-s R_s=+Id.

The square is positive: these extracted maps are not quaternionic
structures on the individual twists. Let sigma_i=omega_J+i omega_K
on the i-th factor, and x=p_1^*[bar(sigma_1)], y=p_2^*[bar(sigma_2)].
For every nonzero v in V_s its actual determinant cup satisfies

    C_(s,-s)(v,R_s v)=f_s(v)x+g_s(v)y,
    f_s(v)<0,                   g_s(v)<0.                 (1)

Both signs use the same determinant and the same hyperkähler triple.
Equivalently these are the two Serre traces divided by the respective
nonzero traces of bar(sigma_i) sigma_i. Thus the ratio of the two
components has positive real sign for both opposite pairs.

L158's four-distinct-input identity contradicts (1) when a and b are
both positive. In particular neither of the two tested z=0 extremal
branches can arise from F. This NEGATIVE / REPRODUCTION is a new local
restriction obtained by specializing known harmonic and cup tools;
it is not a claim of progress beyond the sources checked. The separate
critical audit below preserves this scoped conclusion. It does not exclude every equality kernel,
construct F or a cycle, improve z<=119, establish a nonempty split set
or a contradictory lower count, or resolve universal primitive Hodge
realization or transport.

## Proof

**Scope and imported harmonic input.** Reuse the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-24-dual-coefficient-quaternionic-trace-sign.md`.
The discriminating target is the actual two-trace sign, left free by
L158's relaxation. ATTEMPTS/069, /089 and /090 remain valid in their
stated scopes. No unspecified cup matrix is assigned here.

Import Verbitsky, *Hyperholomorphic bundles over a hyperkähler manifold*,
[alg-geom/9307008v1, 29 July 1993](https://arxiv.org/pdf/alg-geom/9307008v1),
Section 4, Theorem 4.1 and Corollary 4.3, pp. 15–16: the conjugate-J
operator for a parallel real hyperholomorphic coefficient preserves
harmonic forms. Use the Hermitian exchange real structure on E direct
sum E-dual in the proof of Theorem 4.2.A, p. 17. These are preprint
page/theorem numbers. We need neither the printed endpoint-injection
claim nor the scalar cohomology-ring display there. The compact
hyperkähler product is allowed; irreducibility of the base is not a
hypothesis of these harmonic identities.

L158 supplies the actual cup/counit/base-change comparisons and all
quartic signs. Its coefficient Hodge/Serre input is Demailly,
[L2 vanishing theorems for positive line bundles and adjunction theory,
alg-geom/9410022v3](https://arxiv.org/pdf/alg-geom/9410022v3), Section 4.A,
(4.3)–(4.4'), pp. 27–28. We specialize these imported tools, without
reproving Hodge theory, duality or transform preservation.

**The determinant and the actual dual connections.** As in L158,
integral c_1(F)=0 and H^1(X,O_X)=0 give det(F)=O_X. The connection
from L071 is Hermite–Einstein of slope zero. Its determinant Chern
connection is the one on the actual trivial holomorphic determinant
line. In a nonvanishing holomorphic trivialization the logarithm of
the determinant metric has zero scalar Laplacian: its complex Hessian
is the curvature and the curvature contraction is zero. Compactness
makes this function constant. The trivialization is therefore parallel.
Normalize its resulting alternating wedge A:F tensor F -> O to have
unit norm, once on the whole X. This is one choice for all four cups.
A constant change of this choice rescales every cup together and cannot
alter the quartic contradiction.

Use Hermitian products H linear in the first argument. On a Hermitian
bundle E define tau_E(v)(w)=H(w,v). This is an anti-linear isometry
E -> E^vee, parallel for the actual connection and its dual. For Q_s
there is also the parallel complex-linear isometry

    b_s:Q_-s -> Q_s^vee,
    b_s(u tensor t^-1)(v tensor t)=A(v,u),                 (2)

with line evaluation understood for arbitrary t and t^-1. The dual
of the preferred metric/connection on T_s is exactly the chosen one
on T_-s: all lines are constructed by tensor powers and pullback of
the preferred HE lines. The coefficient connection in the target
of (2) is consequently the actual connection on Q_-s, not an
independently chosen holomorphic identification. Put

    r_s=b_s^-1 tau_(Q_s):Q_s -> Q_-s.                    (3)

In a local smooth unitary frame f_1,f_2 with A(f_1,f_2)=1 and a unit
line frame t_s with dual t_-s, its values are

    r_s(f_1 tensor t_s)= f_2 tensor t_-s,
    r_s(f_2 tensor t_s)=-f_1 tensor t_-s.

These follow directly from A(w,r_s v)=H(w,v), with the paired line
factors included. Hence r_s is parallel and anti-unitary and

    r_-s r_s=-Id.                                      (4)

No parallel involution on either Q_s alone has been asserted.

Each Q_s is hyperholomorphic for the diagonal product triple. L071
supplies this for F. On a K3 surface the preferred HE line curvature
is primitive (1,1), hence ASD and invariant under the surface triple;
this was checked for all powers in L157. Pullback, tensor product and
dualization preserve this invariant-curvature property. Thus all
connections in (2)–(4) meet the harmonic theorem's hypotheses.

**Extracting the map in ordinary Dolbeault convention.** Let J act on
complexified covectors by pullback, J a(ξ)=a(Jξ), extended exteriorly.
On ordinary scalar (0,1)-forms put j(a)=J(bar a). It is anti-linear,
isometric and has j^2=-Id. Define on Q_s-valued (0,1)-forms

    R_s(v tensor a)=r_s(v) tensor j(a).                 (5)

Both factors on the right are anti-linear, so the formula is balanced
over C and defines an anti-linear map on the complex tensor product.
It does not define a complex-linear map: multiplying the original
simple tensor by c multiplies its image by bar(c). Equations (4) and
j^2=-Id give R_-s R_s=+Id already on forms.

For harmonic preservation, apply the imported real-coefficient theorem
to B_s=Q_s direct sum Q_s^vee with its orthogonal direct-sum metric
and parallel anti-unitary involution

    T(u,lambda)=(tau_(Q_s)^-1(lambda), tau_(Q_s)(u)).

The theorem is written for (p,0)-forms and the (1,0) connection part.
Apply it with the equally valid triple (-I,J,-K). Its (1,0)-forms
are our (0,1)-forms and its partial operator is our bar-partial.
Its conjugate-J operator on the Q_s summand is

    v tensor a -> tau_(Q_s)(v) tensor J(bar a)

in the Q_s^vee summand, up to one overall minus sign if the covector
action is defined by the dual action -J^* instead of our pullback J^*.
Such a sign does not change harmonic preservation; (5) fixes our sign
for both projections. The direct-sum Laplacian preserves each summand,
so a harmonic Q_s-valued form is sent to a harmonic dual-valued form.
Composing with b_s^-1 preserves harmonicity because (2) is a
parallel holomorphic isometry for the actual connections. This is
precisely (5). Compact coefficient Hodge theory therefore defines R_s
on V_s by its unique harmonic representative, and the square identity
on forms gives inverse R_-s on cohomology. We have used only diagonal
rotation, not independent rotations of the two factors.

**Restriction commutes with this form operator.** For a fibre inclusion
i of either projection, its tangent map commutes with the fixed J.
Restriction of the coefficient Hermitian duality and determinant in
(2)–(3) is their actual fibrewise duality and determinant. Therefore

    i^*(R_s alpha)=R_(s,i)(i^*alpha)                    (6)

as smooth coefficient forms, with the fixed base-line fibre and its
dual retained. If alpha represents v harmonically, both alpha and
R_s alpha are bar-partial closed globally, hence their pullbacks are
closed. No statement that i^*alpha is fibrewise harmonic is needed.
In particular (6) does not replace the global representative with an
independently chosen fibre harmonic representative or discard an exact
correction. The following norm calculation uses the raw pullbacks.

**One frame calculation fixes both trace signs.** On either factor
choose an oriented real orthonormal quaternionic frame
(u,Iu,Ju,Ku), and let its dual real coframe be epsilon_0,...,epsilon_3.
The complex orientation is epsilon_0 epsilon_1 epsilon_2 epsilon_3.
Set

    zeta_1=(epsilon_0+i epsilon_1)/sqrt(2),
    zeta_2=(epsilon_2+i epsilon_3)/sqrt(2).

These are orthonormal (1,0)-covectors for the convention I^*zeta=i zeta.
The definitions of the triple and sigma=omega_J+i omega_K give

    J zeta_1=-bar(zeta_2),       J zeta_2=bar(zeta_1),
    sigma=2 zeta_1 wedge zeta_2,
    sigma wedge bar(sigma)=4 dvol.                     (7)

For a=a_1 bar(zeta_1)+a_2 bar(zeta_2), direct exterior multiplication
then gives

    a wedge j(a)=-(|a_1|^2+|a_2|^2)
                    bar(zeta_1) wedge bar(zeta_2).      (8)

In a unit determinant frame and paired unit line frames as above,
write alpha_i=i^*alpha=f_1 tensor t_s a+f_2 tensor t_s b. Equations
(3), (5), (6) give R_(s,i)alpha_i=f_2 tensor t_-s j(a)
-f_1 tensor t_-s j(b). The same A as in every global cup therefore
satisfies

    A(alpha_i wedge R_(s,i)alpha_i)
       =a wedge j(a)+b wedge j(b)
       =-(|alpha_i|^2/2) bar(sigma_i).                 (9)

The cross coefficient terms have zero determinant; the second diagonal
term is positive before (8), because its explicit minus sign cancels
A(f_2,f_1)=-1. Formula (9) includes the full coefficient norm and the
base-line fibre metric. Evaluating that line against its dual gives
one, so no twist-dependent phase remains. Smooth unitary frames are
sufficient for this pointwise calculation. Closedness was supplied
separately above.

Both factors have the same ordered triple and complex orientation.
Thus (7)–(9) hold with exactly the same signs on both factors, for all
four s. No factor is assigned an independent determinant or a reversed
symplectic form. This is the required comparison beyond abstract
perfection of the relative forms.

**The normalized actual traces are strictly negative.** Let

    C_(s,-s)(v,R_s v)=f_s(v)x+g_s(v)y.

L158's actual cup restriction and coefficient/counit comparison identify
its restriction to a first-factor fibre with f_s(v)[bar(sigma_1)],
and to a second-factor fibre with g_s(v)[bar(sigma_2)]. Denote the
relevant one of these coefficients by c_i(v). The Serre-integral
comparison, normalized by the nonzero trace of bar(sigma_i) sigma_i,
gives

    c_i(v)
      = Tr([A(alpha_i wedge R_(s,i)alpha_i)] sigma_i)
           / Tr([bar(sigma_i)] sigma_i)
      = integral (A(alpha_i wedge R_(s,i)alpha_i) wedge sigma_i)
           / integral (bar(sigma_i) wedge sigma_i)
      = - integral |alpha_i|^2 dvol_i / (2 Vol(S_i)).   (10)

Any universal normalization between analytic integration and Serre
trace cancels in this ratio. Both forms in the numerator are closed,
so it computes the actual cup class; an exact change integrates to
zero against sigma_i. The even-degree reordering of sigma_i and its
conjugate introduces no sign. Equation (7) makes the denominator
strictly positive. Thus (10) gives nonpositivity without assuming
fibrewise harmonicity or using positivity of an unspecified trace.

For strictness use the actual degree-one edge in each direction from
L158. For nonzero v the associated section of the locally free middle
image is nonzero, since that edge is an isomorphism. At some point of
its base its evaluation is nonzero. Actual coefficient base change
identifies this evaluation with the restriction of the same class v,
including the fixed base-line fibre. Thus alpha_i represents a nonzero
class on at least one fibre in that direction, and is not the zero
form there. Its squared norm integral is strictly positive. The
coefficient c_i(v) is the scalar of one global H^2(O_X) class; it is
independent of the chosen fibre. Applying this reasoning separately
to both projections proves f_s(v)<0 and g_s(v)<0. There is no need to
assume an everywhere nonzero section or that the two chosen fibres
meet at a prescribed point. This proves (1).

**The two branches contradict the four-input identity.** Both tested
branches have a>0 and b>0. Choose nonzero v in V_-- and w in V_-+.
Their images R_--v in V_++ and R_-+w in V_+- are nonzero by the
square identity. Substitute these four actual classes into L158's
polarized determinant identity. The other two pair partitions consist
of adjacent sign vertices, whose cup targets vanish. The remaining
term is therefore

    C_(--,++)(v,R_--v) C_(-+,+-)(w,R_-+w)=0.            (11)

Writing these cups as f x+g y and f' x+g' y, (1) makes all four
numbers strictly negative real. But x^2=y^2=0 and xy is nonzero, so

    (f x+g y)(f' x+g' y)=(f g'+g f')xy != 0,           (12)

since f g'+g f'>0. Equations (11) and (12) contradict each other.
This excludes the registered branches (12,2) and (6,8).

L158's abstract witness used opposite signs between the two pairs;
its validity as a relaxation is unchanged. The actual map (5), its
restriction identity and (10) supply the additional constraint that
witness omitted. No self-cup value or multiplicative harmonic
projection has been used. The result is restricted here to the
approved z=0 test. Other decompositions, positive-z coefficient
behaviour, existence of F, independent lower split control and
transport remain unresolved. The separate critical audit below checks
the harmonic convention, determinant normalization and both actual trace
comparisons within exactly these hypotheses.

**Separate critical audit — 2026-10-24, step 524.** This is
RESEARCH / EXPLORATION / REPRODUCTION, actual task proof_audit, under
the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-24-dual-coefficient-trace-sign-critical-audit.md`.
The entire proof above and the relevant actual-connection, preferred-line
and four-edge passages of L071, L157 and audited L158 were checked.
ATTEMPTS/069,/089,/090 remain valid in their stated scopes. The audit
finds no substantive error, changes no mathematical input and makes
no stronger exclusion claim. The following records the load-bearing
checks rather than treating source coverage as a proof verdict.

The source operator was checked directly again in Verbitsky's cited
v1: the real extension to coefficient forms on printed p. 12, the
conjugate-J setup on p. 13, Theorem 4.1 on p. 15, Corollary 4.3 and
its harmonic-preservation proof on p. 16, and the doubled-dual proof
of Theorem 4.2.A on p. 17. These are the same assessed primary cases,
not additional literature discovery. The source's real operator on a
simple coefficient form is T(v) tensor bar(a). Composing with J
therefore gives T(v) tensor J(bar(a)); on the Q_s summand of B_s
its coefficient is exactly tau_(Q_s)(v). The source's possible dual
cotangent sign multiplies this whole degree-one map by -1, and does
not select different signs on the two factors. Its harmonic theorem
applies to a compact hyperkähler base with a parallel real
hyperholomorphic coefficient; no irreducibility hypothesis is used
in these cases. The present B_s satisfies those hypotheses.

To check the change of Dolbeault convention explicitly, the triple
(-I,J,-K) satisfies (-I)J=-K. Its positive-type covectors are the
original negative-type covectors. Its connection's positive-type
component is consequently the original bar-partial, on the same
smooth coefficient connection. Thus the source harmonic statement
is about the precise Laplacian used for V_s. It does not require a
holomorphic identification of the coefficients for I and -I.
Orthogonal direct-sum connections make the Laplacian block diagonal.
The parallel b_s^-1 carries the actual dual connection to Q_-s and
intertwines its Dolbeault Laplacian. This proves harmonic preservation
for precisely (5), with no individual real structure on Q_s.

For the metric bridge, det(F) is holomorphically trivial by the
exponential sequence and H^1(O_X)=0. In a global holomorphic generator
its determinant metric is a positive function. Zero HE contraction
sets the scalar Laplacian of its logarithm to zero, so compactness
makes that logarithm constant. Its Chern connection is therefore
trivial. Choose a unit determinant generator, so that in a smooth
unitary frame A(f_1,f_2)=1. This also fixes the norm convention for
the determinant wedge, viewed as a section of Lambda^2 F^vee.
For v=a f_1+b f_2, equation (3) reads
r_s(v)=bar(a) f_2-bar(b) f_1, with the dual line frame attached.
Applying r_-s gives -v. On the covector factor j^2=J^2=-1 since
J is real. Both factors are anti-linear: the two representatives
(cv) tensor a and v tensor (ca) have the same image, multiplied
by bar(c), so (5) is balanced and anti-linear, and its square is
indeed +1. Tensor, pullback and dual connections on the preferred
HE lines are exactly those in this calculation; no line-metric
phase is available to change only one trace.

For the independent sign computation, J applied to the four real
dual covectors is (-epsilon_2,epsilon_3,epsilon_0,-epsilon_1).
It follows that

    j(a)=bar(a_2) bar(zeta_1)-bar(a_1) bar(zeta_2),
    a wedge j(a)=-(|a_1|^2+|a_2|^2) bar(zeta_1) wedge bar(zeta_2).

Also zeta_1 wedge zeta_2 wedge bar(zeta_1) wedge bar(zeta_2)=dvol,
so sigma wedge bar(sigma)=4 dvol. For the two coefficient rows of
alpha_i, the determinant gives a wedge j(a)+b wedge j(b), with
no cross terms. This verifies (9) and its factor 1/2 independently.
Exactly the same oriented calculation holds on the other factor:
both triples and complex orientations are retained. Neither factor
exchange nor a convention for a relative trace is being used to
guess the second sign.

Both fibre inclusions are quaternionic, hence their pullbacks commute
with J on covectors and with the actual restricted r_s. The globally
harmonic alpha and R_s alpha are closed for their respective
Dolbeault operators; pullback preserves that closedness. Thus the
raw restricted determinant product computes the restriction of the
same global cup, even though its two factors need not be fibrewise
harmonic. Demailly's cited coefficient Serre-integral comparison
and L158's actual counit/trace comparisons give the numerator of
(10); division by the generator's own trace cancels the integration
constant independently for each fibre. The denominator is 4 Vol,
and the numerator is -2 integral |alpha_i|^2 dvol. Both normalized
coefficients are therefore real and nonpositive with the stated
negative factor. Holomorphicity of the scalar H^2 class makes each
coefficient independent of the selected fibre.

Strictness was checked in each direction, rather than transferred
from one to the other. At z=0 the forward coefficients have actual
middle bundles M and M^vee and no other images; L157 supplies the
opposite concentration for both signs. Each of L158's four rows
therefore has an injective degree-one edge and an actual middle
base-change isomorphism for both projections. A nonzero v gives a
nonzero holomorphic section in each direction. Some fibre evaluation
of that section is nonzero, hence the restriction of v to that fibre
is nonzero. Its raw representative has positive norm integral there.
Formula (10) then makes the corresponding global coefficient strictly
negative. This uses two possibly different fibres, which suffices
for the two constant coefficients of one global cup. It does not
assume global-section perfection alone implies pointwise nonvanishing.

Finally, order the four inputs as (v,R_--v,w,R_-+w). All their line
coefficients cancel in total. The two other pair partitions consist
entirely of adjacent sign vertices, whose degree-two target groups
vanish by L158. The polarized determinant identity has three plus
signs: in a local determinant frame C(alpha,alpha)=2a wedge b has
square zero, and polarization gives coefficient +8 for each pair
partition. Thus it forces exactly (11). In the surviving product
x and y both have even degree, x^2=y^2=0 and xy!=0; its coefficient
is f g'+g f'>0. Both registered branches have nonzero v and w, so
the contradiction applies to each. No self-cup target, unknown matrix
assignment, independently selected coefficient class or multiplicative
harmonic projection enters this final step.

The conditional exclusion survives this separate audit. It neither
invalidates L158's weaker formal witness nor asserts existence or
nonexistence for other branches. Positive-z behaviour, independent
lower split control, common-kernel existence and transport remain
unresolved, as does universal primitive Hodge realization. No
mathematical script or numerical approximation was needed.

## Mathlib

Full matching coverage for this opposite-coefficient harmonic map and
two-projection trace-sign specialization is not checked. The ordinary
complex/quaternionic frame algebra is only supporting material and
would not formalize the imported analytic theorems or actual coherent
comparison maps. Unknown coverage is not absence. The result is a
REPRODUCTION/specialization of the precisely cited tools, with no
certified originality claim.
