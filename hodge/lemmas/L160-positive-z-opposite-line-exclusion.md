# L160 — Opposite line multiplicities cannot coexist with W retained

## Hypotheses

Retain L157's conditional data, including L071's identical marked
projective K3 factors X=S_1 x B, their common hyperkähler metric and
ordered triple (I,J,K), real class h, full integral tensor tau_D and
preferred dual HE lines L,L_B of class k=(-4,-2,1,2). Thus k.h=0,
k^2=-14 eta, integral eta=1, and Dk=4k. Suppose F is locally free,
rank two, Omega-polystable for Omega=h_1+h_2, with integral c_1(F)=0
and ch(F)=2-14e_1-21e_2-tau_D+62e_1e_2. Use its actual compatible
connection from L071, rather than an independently chosen cup map.

Set P_e=Rp_{2*}(F tensor p_1^*L^e), e in {-1,1}.
L147 gives H^0(P_-)=0, H^1(P_-)=M locally free of rank 24, and
H^2(P_-)=W, with W the sum of one residue field at each point of a
finite set Z. Retain L153's polystability and L156's endpoint bounds
as incorporated in L157: 0<=z=|Z|<=119 and H^0(M)=H^2(M)=0.
Let m_t be the full multiplicity of L_B^t in M. Use L157's actual
opposite concentrated transforms H_d for d=+1,-1. No F or nonempty
Z is known to exist. In particular W is not assumed zero.

## Conclusion

Under these hypotheses,

    m_-1 * m_1 = 0.                                      (1)

The positive forward ordinary middle sheaf E_+=H^1(P_+) embeds in
M^vee and agrees with it away from Z. For each of the four signed
coefficients Q_(e,d)=F tensor p_1^*L^e tensor p_2^*L_B^d, every nonzero
class in H^1(X,Q_(e,d)) has nonzero restriction to some fibre in each
direction. Consequently L159's same normalized actual two-trace
inequality is strict for all these classes, even with W retained.

The original attempt was ADVANCE / REPRODUCTION, a local specialization
of the assessed tools. The separate critical audit below preserves it. It
narrows a conditional spectrum, not the bound z<=119, and proves
neither existence nor nonexistence of F. Other stable summands, lower
control on z, transport and universal primitive Hodge realization
remain unresolved. No progress beyond the sources checked is claimed.

## Proof

**Scope and imported inputs.** The invocation-start SPECIALIZE review
is `drafts/literature/2026-10-24-positive-z-opposite-coefficient-trace-obstruction.md`.
The discriminating test is fibre detection for the positive forward
coefficient, followed by actual strict traces and the quartic identity.
L158's z=0 concentration and perfect-section-pairing claims are not
imported at positive z. ATTEMPTS/069,/089,/090 remain valid for their
weaker tests; no unspecified matrix is assigned.

Import Leray from [Stacks Lemma 20.13.4, 01F2](https://stacks.math.columbia.edu/tag/01F2),
perfect pushforward and derived base change from
[Lemma 36.30.1, 0A1H](https://stacks.math.columbia.edu/tag/0A1H),
and the concentration criterion from
[Lemma 36.31.3, 0BDK](https://stacks.math.columbia.edu/tag/0BDK).
Our projections are smooth projective of relative dimension two over
Noetherian complex surfaces. Q_(e,d) is locally free, base-flat, with
proper support; take the theorem's other perfect input to be O_X.
Thus these are the actual perfect derived images and coefficient
base-change maps. Use relative duality and its trace as in
[Stacks 48.12.4, 0AAB](https://stacks.math.columbia.edu/tag/0AAB),
[48.7.1, 0B6J](https://stacks.math.columbia.edu/tag/0B6J), and the smooth
identification p^!O=omega_p[2] in
[48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT).
These are precisely the general inputs whose hypotheses the saved
assessment checked. No new source or general reproof is required.

**Dual truncation retains the point term.** Integral c_1(F)=0 and
H^1(O_X)=0 imply det F=O_X by the exponential sequence. Fix the same
unit parallel determinant wedge as in L159 and the fixed K3 forms.
Write D_B=RHom_B(-,O_B). Relative duality gives

    D_B(P_-)=P_+[2],       P_+=D_B(P_-)[-2].             (2)

The canonical cohomology truncation triangle, using L147, is

    M[-1] -> P_- -> W[-2] -> M.

Apply D_B contravariantly and then shift by -2. Since M is locally
free, this gives the actual distinguished triangle

    D_B(W) -> P_+ -> M^vee[-1] -> D_B(W)[1].            (3)

Here and below H^j denotes cohomology sheaves for complexes on B.
For clarity the small local calculation needed in (3) is explicit.
At a point of Z the stalk is W_a=R/(u,v), where R=O_(B,a) is regular
local of dimension two and u,v are regular parameters. Its Koszul
resolution is

    0 -> R --(-v,u)--> R^2 --(u,v)--> R -> R/(u,v) -> 0.

Applying Hom_R(-,R) gives zero cohomology in degrees zero and one
and R/(u,v) in degree two: the first map is injective, and the
middle kernel equals its image by regularity of u,v; the last
cokernel is R/(u,v). There are no higher terms. This computes the
specific point contribution, not a reproof of relative duality.
Consequently D_B(W)=W^dagger[-2], where
W^dagger=mathcal Ext^2_B(W,O_B) is the sheaf Ext, supported on Z, with one-dimensional
residue-field stalks. No canonical identification W^dagger=W is needed.

The cohomology sequence of (3) therefore gives

    H^0(P_+)=0,
    0 -> E_+ -> M^vee --delta--> W^dagger
        -> H^2(P_+) -> 0.                              (4)

The unknown delta is retained. We claim neither that it is zero nor
that P_+=M^vee[-1]. In particular (4) makes E_+ torsion-free, and on
U=B minus Z it identifies E_+ with M^vee. On that open set (3)
identifies P_+ with M^vee[-1]; P_-=M[-1] there as well. No ordinary
base-change assertion at a point of Z has been used.

**The two forward edges detect classes away from Z.** Put E_-=M.
Projection formula gives the actual forward image of Q_(e,d) as
P_e tensor L_B^d. Both e signs have ordinary degree-zero image zero,
by L147 and (4). In Leray, the only term of total degree one is
H^0(B,E_e tensor L_B^d). There is no incoming differential. Its
d_2 target is H^2(B,H^0(P_e) tensor L_B^d)=0, and subsequent
targets have negative second index. Thus the natural edge is an
isomorphism

    H^1(X,Q_(e,d)) = H^0(B,E_e tensor L_B^d).           (5)

A nonzero section on the right remains nonzero on U. For e=- this
is local freeness of M; for e=+ it follows from the injection into
M^vee tensor L_B^d in (4). A section of a vector bundle vanishing
on a dense open of the integral surface B is zero. Choose a closed
point of U where the section evaluates nontrivially. On U the
derived image is a vector bundle in degree one, so derived base
change identifies this evaluation with the restriction of the
original global class to that fibre. This is nonzero.

The identification is the actual restriction map: restrict the
canonical degree-one edge and the counit Lp_2^*Rp_{2*}Q -> Q to
the fibre. Their base-change composite is the coefficient restriction
of the original class. This is the same functorial comparison as in
L158, now used only on U, where its concentration hypothesis holds.
General counit/product compatibility is
[Stacks 20.31.7, 0FP6](https://stacks.math.columbia.edu/tag/0FP6) and
[20.31.8, 0H99](https://stacks.math.columbia.edu/tag/0H99), reused from
the recorded source assessment. In particular no class supported
only at Z can hide in the degree-one space (5).

For the other projection L157 already proves, for both d signs,

    Rp_{1*}Q_(e,d)=(H_d tensor L^e)[-1].

Its whole-base degree-one edge and base-change isomorphisms therefore
detect every nonzero class on some p_1 fibre as well. The two chosen
fibres need not meet at a prescribed point. Finally L157's negative
forward comparison (which already retained W) gives

    dim H^1(X,Q_--)=m_1,    dim H^1(X,Q_-+)=m_-1.       (6)

This uses the full stable line multiplicities, not selected summands.

**The actual harmonic map and both strict signs.** Reuse the operator
construction of L159, checking its scope rather than importing its
z=0 conclusion. Its harmonic theorem is Verbitsky,
*Hyperholomorphic bundles over a hyperkähler manifold*,
[alg-geom/9307008v1, 29 July 1993](https://arxiv.org/pdf/alg-geom/9307008v1),
Section 4, Theorem 4.1 and Corollary 4.3, pp. 15–16, and the
doubled-dual proof of Theorem 4.2.A, p. 17. These apply to the
compact hyperkähler product and the parallel real coefficient
Q_s direct sum Q_s^vee; they do not assume projection IT. L071's
actual F and L157's preferred tensor-power line connections are
hyperholomorphic at the same triple. Thus every hypothesis of the
operator construction survives positive z.

More explicitly, for the fixed unit determinant wedge A define
b_s:Q_-s -> Q_s^vee by b_s(u)(v)=A(v,u), with line evaluation,
and tau_s(v)(w)=H(w,v), for H linear in its first argument. Set
r_s=b_s^-1 tau_s and j(a)=J(bar(a)) on scalar (0,1)-forms. L159's
construction gives the anti-linear harmonic map

    R_s(v tensor a)=r_s(v) tensor j(a),
    R_-s R_s=Id.

Indeed r_-s r_s=-Id and j^2=-Id. Harmonic preservation follows by
the cited doubled-dual construction for the triple (-I,J,-K) and
the parallel holomorphic isometry b_s^-1, as checked in L159. No
individual twist is assigned a real structure. Fibre inclusions
commute with J and these actual coefficient operations, so restriction
commutes with R_s on the raw smooth forms.

Let alpha be the harmonic representative of a nonzero v in H^1(Q_s).
Both alpha and R_s alpha are globally closed, and their fibre
restrictions are closed. With sigma_i=omega_J+i omega_K on each
factor, set x=p_1^*[bar(sigma_1)], y=p_2^*[bar(sigma_2)] and write

    C_(s,-s)(v,R_s v)=f_s(v)x+g_s(v)y.

The local frame identity L159 (9), independent of any direct image,
is A(alpha_i wedge R_s alpha_i)=-(|alpha_i|^2/2)bar(sigma_i)
on a fibre in direction i. The Serre-integral comparison is Demailly,
*L2 vanishing theorems for positive line bundles and adjunction theory*,
[alg-geom/9410022v3](https://arxiv.org/pdf/alg-geom/9410022v3),
Section 4.A (4.3)–(4.4'), pp. 27–28. Its coefficients are locally
free here. It gives the actual normalized component

    c_i(v)=- integral_(S_i) |alpha_i|^2 dvol_i
                         / (2 Vol(S_i)).               (7)

Here c_1=f_s and c_2=g_s. The denominator normalizes by the trace
of bar(sigma_i)sigma_i; integration constants cancel. Equation (7)
uses raw restrictions, not hypothetical fibre harmonic representatives.
It computes the restriction of the same global cup class, so its
scalar is independent of the chosen fibre. The detection just proved
supplies in each direction a fibre on which alpha_i represents a
nonzero class, hence has strictly positive norm integral. Therefore

    f_s(v)<0,                 g_s(v)<0.                (8)

This is the replacement for L159's concentrated-forward strictness
step. Neither perfection of a pairing nor an assigned cup matrix
is used to deduce (8).

**The four actual inputs contradict simultaneous multiplicities.**
Suppose m_1>0 and m_-1>0. By (6) choose nonzero v in H^1(Q_--)
and w in H^1(Q_-+), and use R_--v and R_-+w as their opposite
coefficient partners. They are nonzero by the square identity.
L158's adjacent-target vanishing and local polarized rank-two
determinant identity depend on the coefficient lines and rank of F,
not on z, dimensions of the four spaces, or concentration.
Specifically nonzero powers of either line have H^0=H^2=0, while
H^1(O_(S_i))=0. Kunneth therefore kills each adjacent H^2 target.
For four coefficient-valued one-forms the determinant self-cup has
square zero (locally it is 2a wedge b); polarization gives
C_12 C_34+C_13 C_24+C_14 C_23=0, with three plus signs.
These are the same actual Dolbeault products as in L158, with
[Stacks 20.31.3, 0FP3](https://stacks.math.columbia.edu/tag/0FP3)
and [36.23.1, 0FLN](https://stacks.math.columbia.edu/tag/0FLN)
providing the coefficient product and Kunneth comparisons.

For the four chosen inputs the two adjacent partitions vanish,
leaving C_(--,++)(v,R_--v) C_(-+,+-)(w,R_-+w)=0. But (8) writes
these two cups as f x+g y and f' x+g' y with all four scalars
strictly negative real. Since x^2=y^2=0 and xy is nonzero, their
product is (fg'+gf')xy, which is nonzero because fg'+gf'>0.
This contradiction proves (1).

The required bridge succeeds with the full point term in (3)–(4).
We do not determine delta, assert global positive concentration,
or improve the split-count bound. The conclusion is a restriction
under the full retained hypotheses; the separate audit below checks
the new dual-truncation and strictness extension.

**Separate critical audit — 2026-10-25, step 528.** This is
RESEARCH / EXPLORATION / REPRODUCTION, actual task proof_audit, using
the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-24-positive-z-trace-critical-audit.md`.
The audit finds no substantive error or stronger conclusion. It checks
this conditional specialization, not the existence of F or a complete
Hodge argument. The explicit sheaf-Ext notation above clarifies the
existing meaning; no global Ext vector space replaces a point sheaf.

The relevant actual-connection passage of L071, ordinary-image proof
of L147, negative forward and opposite comparisons of L157, coefficient
targets and polarized identity of L158, and full operator/raw-trace
proof and audit of L159 were checked. L158's forward concentration and
perfect section pairings at z=0 are not positive-z inputs. The ready
source coverage is reused; this audit does not claim a new source
search, a new full Mathlib match or a read of the previously omitted
proof of Stacks 0H99. ATTEMPTS/069,/089,/090 still describe valid limits
of their weaker tests.

First check the duality shifts independently. Smooth-proper relative
duality for relative dimension two, with the fixed fibre form, says
D_B(P_-)=Rp_{2*}(Q_-^vee)[2]=P_+[2], where here
Q_-=F tensor p_1^*L^{-1}. The determinant identification uses the
actual parallel wedge. Contravariance sends the truncation triangle
to D_B(W)[2] -> D_B(P_-) -> M^vee[1] -> D_B(W)[3].
Shifting every term by -2 gives exactly (3), including its last term.
This does not split the original triangle or kill its connecting map.

For the point calculation, regular parameters form a regular sequence
by [Stacks 10.106.3, 00NQ](https://stacks.math.columbia.edu/tag/00NQ);
its Koszul resolution is justified by
[15.31.2, 062F](https://stacks.math.columbia.edu/tag/062F).
The smooth surface stalk is a regular local ring of dimension two,
so these hypotheses hold. Its dual complex, in degrees 0,1,2, is

    R --c |-> (uc,vc)--> R^2 --(a,b) |-> -va+ub--> R.

Its degree-zero kernel is zero since u is a nonzerodivisor. If
-va+ub=0, reduction modulo u and regularity of v modulo u give
a=uc. Then u(b-vc)=0 gives b=vc, proving exactness in degree one.
The degree-two cokernel is R/(u,v). Finite locally free resolutions
compute sheaf Ext stalkwise; away from Z these stalks vanish. Thus
D_B(W) has exactly the sheaf W^dagger in degree two, and no choice
of local parameters identifies it canonically with W. Taking the
cohomology sequence of (3) gives (4) with delta retained. In particular
E_+ is a subsheaf of M^vee, not an asserted positive IT bundle.

For each sign, Leray has only (p,q)=(0,1) in total degree one:
the ordinary R^0 is zero, including for P_+ by (4). No differential
enters (0,1); the d_2 target (2,0) is zero and higher targets have
negative q. A possible differential out of W in total degree two
has no bearing on this edge. Tensoring by L_B^d is exact, so (5)
holds for both d signs with the same ordinary sheaves as stated.
The inclusion E_+ tensor L_B^d -> M^vee tensor L_B^d is injective.
On the integral base, a section of that vector bundle vanishing on
the dense open U vanishes everywhere. Thus a nonzero section of
either E_e tensor L_B^d stays nonzero on U, and some closed point
there has nonzero evaluation.

On U the actual perfect image has just a locally free degree-one
cohomology sheaf. Consequently derived pullback at such a point has
H^1 equal to this ordinary fibre; derived base change identifies it
with the fibre cohomology of Q_(e,d). This evaluation is the original
class restriction, not merely an isomorphism of dimensions: the
section maps by truncation to P_e tensor L_B^d[1], hence defines
O_B -> P_e tensor L_B^d[1]; adjunction followed by the counit gives
the original global class. Pulling back that composite gives exactly
the fibre restriction under base change. No such assertion is made
at a point of Z. For p_1, L157 supplies the whole-base concentration
(H_d tensor L^e)[-1] independently for each d. Its analogous edge
therefore detects every nonzero class in that direction as well.
Finally stable-Hom in the negative forward edge measures the full
L_B^{-d} multiplicity, so d=-1 gives m_1 and d=1 gives m_-1 in (6).

The harmonic part has no hidden projection-IT hypothesis. L071
supplies F's actual invariant-curvature unitary connection; tensoring
the preferred ASD line connections preserves that property. Integral
c_1=0 and Picard injection trivialize det F, and the zero HE factor
makes its trivialization parallel after a constant normalization, as
proved in L159. Thus its same b_s and r_s apply. In a unit determinant
frame r_s(a f_1+b f_2)=bar(a)f_2-bar(b)f_1 in the dual line frame;
r_-s r_s=-Id. On scalar forms j(a)=J(bar a) has square -Id.
The balanced anti-linear tensor formula therefore has square +Id.
Verbitsky's cited real-coefficient harmonic theorem is applied to
Q_s direct sum Q_s^vee with the parallel Hermitian-exchange real
structure, using (-I,J,-K) to pass from its positive Dolbeault
convention to the present negative one. The parallel b_s^-1 then
intertwines the actual dual and opposite Laplacians. These arguments
depend on the smooth connections, not on W or positive concentration.

For each fibre inclusion, pullback commutes with J and with r_s.
Thus the raw restrictions of alpha and R_s alpha are related by the
same operator and both are closed. Independently using L159's unit
coframe, j(a_1 bar(zeta_1)+a_2 bar(zeta_2)) equals
bar(a_2)bar(zeta_1)-bar(a_1)bar(zeta_2). The wedge with the original
form is -(|a_1|^2+|a_2|^2)bar(zeta_1) wedge bar(zeta_2).
The two coefficient rows add with the same sign because A is
alternating and the second row of r_s carries a minus sign.
Since sigma_i=2 zeta_1 wedge zeta_2 and
sigma_i wedge bar(sigma_i)=4 dvol_i, the normalized trace has
numerator -2 integral |alpha_i|^2 dvol_i and denominator 4 Vol(S_i).
This verifies (7), with the same sign for both projections and all
four s. The line and its dual evaluate to one in paired unit frames;
no relative phase may be selected for a different twist or factor.

The restricted cup is the restriction of one global H^2(O_X) class.
Kunneth gives its constant coefficients in x and y, so the normalized
coefficient computed on any fibre is the same f_s or g_s. Detection
in each direction supplies a fibre where alpha_i represents a nonzero
cohomology class. Its raw norm integral is then positive. Apply this
separately in both directions to obtain both strict inequalities (8).
Neither harmonicity of the fibre restriction nor perfection of a
global section pairing is used for strictness.

For the final contradiction order the inputs as
(v,R_--v,w,R_-+w). The two adjacent partitions have a zero degree-two
target: one line exponent is zero and the other is +2 or -2, so
the endpoint vanishings of nonzero line powers and H^1(O)=0 kill
every degree-two Kunneth term. The remaining partition is the two
opposite cups. Locally the determinant self-cup of f_1 a+f_2 b is
2a wedge b, whose square vanishes. Polarization gives coefficient
+8 for each pair partition, since the determinant degree-one cup
is symmetric and the resulting degree-two products commute. Every
term has total line weight zero, so this identity glues and forces
the remaining product to vanish. But its xy coefficient is
fg'+gf'>0 by the two independently strict pairs of signs, while
x^2=y^2=0 and xy!=0. This proves the stated conditional contradiction
without assigning any unknown cup map or changing a quartic sign.

All these checks remain valid at z=0 and at every allowed positive z;
they use finiteness of Z rather than silently assuming it empty.
The audited restriction is still only m_-1*m_1=0 under the full
hypotheses. No lower control on z, elimination of the other stable
decompositions, existence of F, transport or primitive Hodge realization
has been obtained. No numerical certificate or mathematical script
is needed for this audit, and no new mathematical input is added.

## Mathlib

Full matching coverage for this positive-z derived-edge and harmonic
trace specialization is **not checked**. The elementary Koszul and
sign calculations support the proof but do not replace the imported
analytic or derived comparison theorems. Unknown coverage is not
evidence of absence. This is a specialization of assessed sources,
not a certified originality claim.
