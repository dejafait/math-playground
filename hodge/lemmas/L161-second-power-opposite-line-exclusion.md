# L161 — Second-power opposite line multiplicities cannot coexist

## Hypotheses

Retain L157's identical marked projective K3 factors X=S_1 x B,
common hyperkahler metric g, ordered triple (I,J,K), real Kahler
class h, full integral tensor tau_D, and preferred dual HE lines
L,L_B of class k=(-4,-2,1,2). Thus k.h=0, k^2=-14 eta,
integral_S eta=1, and Dk=4k. Put e_1=eta tensor 1,
e_2=1 tensor eta and P=e_1e_2. Suppose F is locally free, rank two,
Omega-polystable for Omega=h_1+h_2, with integral c_1(F)=0 and

    ch(F)=2-14e_1-21e_2-tau_D+62P.

Use L071's actual compatible connection and the actual tensor-power
line connections. Use L147's ordinary images

    P_-=Rp_{2*}(F tensor p_1^*L^{-1}),
    H^0(P_-)=0, H^1(P_-)=M, H^2(P_-)=W,

where M is locally free, h-polystable as in L157, and W is a sum
of one residue field at each point of a finite set Z. Retain
0<=z=|Z|<=119 and let m_t be the full multiplicity of L_B^t in M.
Use L157's independently concentrated opposite transforms H_2,H_-2
and L160's audited dual-truncation framework. No existence of F or
Z is asserted; W and its connecting map are not discarded.

## Conclusion

Under these conditional hypotheses,

    m_-2 * m_2 = 0.                                      (1)

This is a REPRODUCTION specialization of the assessed tools, locally
narrowing the possible line spectrum beyond L160's first-power
restriction. It is not a claim of progress beyond the sources checked.
The separate critical audit below preserves this second-power proof.
There is no improved bound on z, construction or nonexistence proof
of F, exclusion of other stable types, transport, or universal
primitive Hodge realization.

## Proof

**Approved scope and source applicability.** Use the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-25-second-power-opposite-line-trace.md`.
The test is precisely the second-power exclusion (1), with all point
terms retained. L157's additive compatibility and ATTEMPTS/089,/090
remain valid limits of their weaker tests. The argument evaluates the
actual harmonic partners, rather than assigning cups.

Set T_(e,d)=p_1^*L^e tensor p_2^*L_B^d,
Q_(e,d)=F tensor T_(e,d), and V_(e,d)=H^1(X,Q_(e,d)),
where e=+1,-1 and d=+2,-2 only. Write
P_+=Rp_{2*}(F tensor p_1^*L).
All these coefficients are locally free on the smooth projective
product. The projections are smooth projective of relative dimension
two, hence proper and flat, and the coefficients are base-flat with
proper support. The derived projection formula, Leray, perfect
pushforward/base change and relative duality therefore have exactly
the hypotheses used in L160: Stacks
[20.54.2-3, 01E6](https://stacks.math.columbia.edu/tag/01E6),
[20.13.4, 01F2](https://stacks.math.columbia.edu/tag/01F2),
[36.30.1, 0A1H](https://stacks.math.columbia.edu/tag/0A1H),
[36.31.3, 0BDK](https://stacks.math.columbia.edu/tag/0BDK), and
[48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT).
For 0A1H take O_X as the other perfect input. No general theorem
is reproved and no positive-forward IT is asserted.

**Four actual edges and full multiplicities.** Fix the same parallel
unit determinant wedge as in L159. L160's dual truncation gives the
ordinary sheaves, with W^dagger=mathcal Ext^2_B(W,O_B),

    H^0(P_+)=0,
    0 -> E_+ -> M^vee --delta--> W^dagger
        -> H^2(P_+) -> 0,                              (2)

and E_+|_U=M^vee|_U on U=B minus Z. Put E_-=M.
This is the established sheaf-Ext calculation of L160, with its
unknown delta retained, not a splitting of P_+.
Tensoring (2) by either L_B^2 or L_B^{-2} is exact.
In Leray the only term of total degree one is (0,1), with no
incoming differential and zero d_2 target (2,0), since H^0(P_e)=0.
Higher outgoing targets have negative second index. Thus the
forward edge is the actual natural isomorphism

    V_(e,d)=H^0(B,E_e tensor L_B^d).                    (3)

L157 independently supplies, for each d=+2,-2,

    Rp_{1*}Q_(e,d)=(H_d tensor L^e)[-1],
    V_(e,d)=H^0(S_1,H_d tensor L^e).                   (4)

For e=-1, the forward edge identifies V_(-1,d) with
Hom(L_B^{-d},M), of dimension m_-d by full stable-Hom vanishing.
For e=+1, use (4): Hom(L^{-1},H_d) has dimension m_d by L157's
full L^{-1} multiplicity, not by presuming surjectivity on sections
in (2). The four dimensions are therefore

    (e,d)       (-1,-2)  (-1,+2)  (+1,-2)  (+1,+2)
    dim V          m_2     m_-2     m_-2      m_2.      (5)

Every nonzero class in (3) is detected on a forward fibre over U.
Indeed its nonzero section stays nonzero on U: E_- is locally free
and E_+ injects into M^vee. A section of either ambient vector
bundle that vanishes on the dense open U vanishes everywhere.
At some closed point of U the section therefore evaluates nontrivially.
There P_e has just its locally free degree-one sheaf; derived base
change identifies evaluation with restriction of the original class.
This is the counit-compatible edge used in L160: pulling the global
class's adjunction composite back to the fibre is precisely its
restriction. No ordinary base change is claimed at Z. Likewise (4)
and whole-base concentration detect every nonzero class on some
opposite fibre. This checks both directions for all four rows.

**Actual harmonic partners and both strict signs.** Apply L159's
operator construction, with the changed coefficient lines checked
explicitly. The actual Q_s and Q_-s are hyperholomorphic: L071 gives
this for F and the preferred HE line curvatures are ASD, with tensor
powers, duals and pullbacks preserving invariant curvature. Their
metrics and connections are dual under line evaluation. The parallel
unit wedge A gives b_s:Q_-s -> Q_s^vee, b_s(u)(v)=A(v,u).
With the Hermitian metric linear in its first argument put
r_s=b_s^{-1}tau_s, where tau_s(v)(w)=H(w,v), and
j(a)=J(bar a) on scalar (0,1)-forms. Then

    R_s(v tensor a)=r_s(v) tensor j(a),
    r_-s r_s=-Id, j^2=-Id, R_-s R_s=Id.                (6)

The tensor formula is balanced and anti-linear. Harmonic preservation
is the same doubled-dual application of Verbitsky,
*Hyperholomorphic bundles over a hyperkahler manifold*,
[alg-geom/9307008v1, 29 July 1993](https://arxiv.org/pdf/alg-geom/9307008v1),
Section 4, Theorem 4.1 and Corollary 4.3, pp. 15-16, and the proof
of Theorem 4.2.A, p. 17, as in L159. Namely Q_s direct sum Q_s^vee
has the parallel Hermitian-exchange real structure; use (-I,J,-K)
for ordinary (0,1)-forms and compose with the parallel isometry
b_s^{-1}. This verifies its hypotheses without giving an individual
twist a real structure or assuming projection IT.

Let alpha represent a nonzero v in V_s harmonically. Both alpha and
R_s alpha are globally closed. On either factor fibre their raw
restrictions commute with (6), since the inclusion commutes with J
and the coefficient operations restrict. Put sigma_i=omega_J+i omega_K,
x=p_1^*[bar(sigma_1)], y=p_2^*[bar(sigma_2)]. Write the actual cup as

    C_(s,-s)(v,R_s v)=f_s(v)x+g_s(v)y.

The same paired unit line frames, including the squared line and
its dual, evaluate to one. Thus L159's pointwise determinant identity
holds unchanged on each fibre:

    A(alpha_i wedge R_s alpha_i)
        =-(|alpha_i|^2/2)bar(sigma_i).

In particular the exponent two introduces no phase. In the common
oriented unit quaternionic coframe sigma_i wedge bar(sigma_i)=4dvol_i.
The normalized Serre-integral comparison is Demailly,
*L2 vanishing theorems for positive line bundles and adjunction theory*,
[alg-geom/9410022v3](https://arxiv.org/pdf/alg-geom/9410022v3),
Section 4.A (4.3)-(4.4'), pp. 27-28, for these locally free coefficients.
It gives, independently for the two factor directions,

    f_s(v)=-integral_(S_1)|alpha_1|^2 dvol_1/(2 Vol(S_1)),
    g_s(v)=-integral_(B)|alpha_2|^2 dvol_2/(2 Vol(B)).    (7)

These compute the restriction of one global H^2(O_X) class, so each
coefficient is independent of the chosen fibre. The detection from
(3)-(4) gives a fibre in each direction with a nonzero restricted
cohomology class; its raw representative has strictly positive norm
integral. Therefore both numbers in (7) are strictly negative for
every nonzero v. Fibrewise harmonicity is neither asserted nor needed.
One determinant and one ordered triple fix both signs for all four s.

**Changed targets and quartic contradiction.** For every nonzero n,
L157 gives H^0(L^n)=H^2(L^n)=0 and h^1(L^n)=7n^2-2, and the same
for L_B. For n=0 the dimensions are (1,0,1). The line-valued Kunneth
theorem, [Stacks 36.23.1, 0FLN](https://stacks.math.columbia.edu/tag/0FLN),
applies: the projective factors are quasi-compact and quasi-separated,
Tor-independent over the affine base Spec(C), and the lines are
locally free. Hence

    H^2(T_(+/-2,0))=H^2(T_(0,+/-4))=0.                 (8)

For example the degree-two terms for T_(0,4) are H^0(O) tensor
H^2(L_B^4), H^1(O) tensor H^1(L_B^4), and H^2(O) tensor
H^0(L_B^4), all zero. The other cases are identical with the
nonzero factor specified in (8). Self targets T_(+/-2,+/-4) have
H^2 dimension 26*110=2860 and are not assumed zero.
Opposite targets are H^2(O_X)=Cx+Cy, with x^2=y^2=0 and xy!=0.

If m_2,m_-2>0, (5) supplies nonzero
v in V_(-1,-2) and w in V_(-1,+2). Order four actual inputs as

    alpha_1=v, alpha_2=R_(-1,-2)v,
    alpha_3=w, alpha_4=R_(-1,+2)w.

Their weights are (-1,-2),(1,2),(-1,2),(1,-2). The rank-two
polarized determinant identity of L158, for actual Dolbeault cups, is

    C_12 C_34 + C_13 C_24 + C_14 C_23=0.              (9)

For clarity its signs do not depend on the exponents: determinant
and degree-one interchange both contribute minus signs, making C
symmetric. Locally a self-cup is 2a wedge b and its square is zero.
The coefficient of four distinct commuting labels in its square is
eight times each of the three displayed pair partitions, all plus.
Every term here has total weight (0,0), so the identity glues and
passes to cohomology by [Stacks 20.31.3, 0FP3](https://stacks.math.columbia.edu/tag/0FP3).

The targets of C_13,C_24 are T_(-2,0),T_(2,0), and those of
C_14,C_23 are T_(0,-4),T_(0,4). Thus (8) leaves C_12 C_34=0.
But (7) writes these cups as f x+g y and f' x+g' y with all
four scalars strictly negative real. Their product is
(fg'+gf')xy!=0, since fg'+gf'>0. This contradiction proves (1).
No self-cup target, point term, or unevaluated delta was suppressed.

**Separate critical audit — 2026-10-25, step 531.** This is
RESEARCH / EXPLORATION / REPRODUCTION, actual task proof_audit, under
the unchanged invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-25-second-power-opposite-line-trace.md`.
No substantive error or stronger conclusion was found. This checks
the exact second-power specialization; it does not certify originality
or the existence of the hypothetical kernel. The source coverage is
reused, not newly discovered or independently re-extracted this turn.

The audit read the complete proof above, L160's dual-truncation proof
and audit, L159's operator, raw-trace proof and audit, and the relevant
actual-connection, ordinary-image, full-multiplicity and polarized-cup
passages of L071, L147, L157 and L158. It also checked the recorded
limits in ATTEMPTS/069,/089,/090 and the preceding attempt's working
record. The freely assigned cup witnesses and additive spectrum stop
remain valid for their weaker tests. No z=0 perfect-section pairing
is used here at positive z.

For the derived bridge, independently track the shifts in L160:
relative dimension two gives D_B(P_-)=P_+[2]. Dualizing
M[-1] -> P_- -> W[-2] -> M and shifting by -2 gives
D_B(W) -> P_+ -> M^vee[-1] -> D_B(W)[1]. The sheaf-Ext
calculation on a smooth surface gives D_B(W)=W^dagger[-2],
so its cohomology is exactly (2), including the unevaluated delta.
This imports L160's proved framework, not a splitting of P_+.
Tensoring by either invertible L_B^d preserves that sequence. The
degree-one Leray term (0,1) has no incoming differential, its only
possible nonnegative outgoing target (2,0) is zero, and the other
total-degree-one term (1,0) is zero. Thus (3) is an actual edge
isomorphism for each of the four coefficients.

For the two negative e rows, stable-Hom vanishing computes
H^0(M tensor L_B^d)=Hom(L_B^{-d},M), giving m_-d. For the two
positive e rows, L157's whole-base opposite concentration computes
H^0(H_d tensor L)=Hom(L^{-1},H_d), giving m_d. That latter
multiplicity follows in L157 by dualizing the full decomposition
of H_-d; it is not a chosen subspace or a consequence of assumed
surjectivity through delta. Substitution of d=-2,2 gives respectively
m_2,m_-2,m_-2,m_2 in the order of (5).

The positive forward section embeds in a section of the vector
bundle M^vee tensor L_B^d. If it vanished on the dense open U it
would vanish everywhere. The negative row uses the vector bundle
M tensor L_B^d itself. A nonzero section therefore evaluates
nontrivially at some closed point of U. There the actual derived
image is a locally free sheaf shifted by -1. Under derived base
change, evaluation agrees with restriction of the global class:
the edge identifies it with a map O_B -> (P_e tensor L_B^d)[1],
and adjunction followed by the counit gives its original class on X.
Pulling this composite to the fibre is precisely restriction. For
the other direction apply the same comparison to (4), concentrated
on the whole S_1. These are two independent detection arguments;
neither discards W nor asserts ordinary base change on Z.

For the analytic bridge the actual F connection is invariant by
L071, and tensor powers of the preferred ASD lines and their duals
retain this property. L159 supplies a single parallel unit determinant
wedge: holomorphic determinant triviality follows from integral c_1=0
and H^1(O_X)=0, and its zero HE contraction makes the logarithm of
its metric constant. In paired unit line frames, including powers
two and minus two, the coefficient map is

    r_s(a f_1+b f_2)=bar(a)f_2-bar(b)f_1.

Hence r_-s r_s=-Id. Since j^2=-Id, the balanced anti-linear tensor
map has R_-s R_s=Id. Its harmonic preservation is exactly the
assessed doubled-dual case: Q_s direct sum Q_s^vee has the parallel
Hermitian-exchange real involution; (-I,J,-K) converts the source's
positive Dolbeault convention to the present negative convention.
The parallel holomorphic isometry b_s^-1 intertwines the dual and
opposite coefficient Laplacians. Neither a real structure on Q_s
alone nor projection IT enters this use of the cited theorem.

Independently check the local sign with L159's oriented unit coframe.
For a=a_1 bar(zeta_1)+a_2 bar(zeta_2),

    j(a)=bar(a_2)bar(zeta_1)-bar(a_1)bar(zeta_2),
    a wedge j(a)=-(|a_1|^2+|a_2|^2)bar(zeta_1) wedge bar(zeta_2).

For the two coefficient rows a,b of a restricted form, the determinant
therefore gives a wedge j(a)+b wedge j(b). The minus in the second
row of r_s cancels the alternating determinant sign. With
sigma_i=2 zeta_1 wedge zeta_2 and sigma_i wedge bar(sigma_i)=4dvol_i,
the numerator of the normalized integral is -2 integral |alpha_i|^2
dvol_i and the denominator is 4 Vol(S_i). This verifies (7) in
each direction separately. The squared unit line frame evaluates
against its dual to one; it contributes neither a factor nor a phase.

Fibre pullback commutes with J and the coefficient operations.
Consequently the raw restrictions of the two globally harmonic forms
are related by R_s and are closed, even without fibre harmonicity.
Their product computes the restriction of one global H^2(O_X) class,
whose x,y coefficients are independent of the fibre. Detection gives
a fibre in each direction where the restricted class is nonzero,
hence its raw norm integral is strictly positive. This proves both
strict negative inequalities with one common determinant normalization.

For the algebraic end of the audit, H^0 and H^2 of every nonzero
line power vanish by slope zero and nontriviality, while H^1(O)=0.
These facts kill all degree-two Kunneth terms for T_(+/-2,0) and
T_(0,+/-4). They do not kill the self targets: their degree-one
factor dimensions are 7*2^2-2=26 and 7*4^2-2=110, giving 2860.
In the chosen input order the (13,24) targets are (-2,0),(2,0)
and the (14,23) targets are (0,-4),(0,4). No self target is used
in these two vanishing partitions.

Finally, the coefficient determinant and odd-form interchange make
C_ij symmetric. Locally C(alpha,alpha)=2a wedge b has square zero.
For four distinct commuting labels the coefficient in its square
is +8 times each of the three pair partitions; the degree-two
products commute. All terms have total line weight zero, so this
identity glues. It forces C_12 C_34=0, whereas the independently
checked strict traces make its xy coefficient fg'+gf' strictly
positive. Since xy is nonzero, the contradiction is valid. No
harmonic-projection multiplicativity or freely assigned cup is used.

Thus (1) survives the separate audit with exactly its stated
hypotheses and direct mathematical inputs. The audit introduces
no new lemma or stronger bound, and requires no numerical script.
F existence, other stable types, lower control on z, transport and
primitive Hodge realization remain unresolved.

## Mathlib

Full matching coverage for this second-power derived-edge, harmonic
trace and determinant-cup specialization is **not checked**. General
supporting algebra would not by itself supply the actual analytic
comparison. Unknown coverage is not absence. This conditional local
specialization has passed the separate audit above and asserts no
certified originality or solution of the Hodge conjecture.
