# L157 — Double line twists restrict the full line spectrum of M

## Hypotheses

Retain the identical marked projective K3 factors S_1 and B=S_2,
common hyperkähler metric g, real Kähler class h and fixed full tensor
of L071 and L147. Normalize integral_S eta=1, put e_1=eta tensor 1,
e_2=1 tensor eta and P=e_1e_2, and let L and L_B be the lines of class
k=(-4,-2,1,2) on the respective factors. Thus k.h=0, k^2=-14 eta
and Dk=4k. Use their preferred HE line connections. Suppose F is
locally free, rank two and Omega-polystable, where Omega=h_1+h_2,
with integral c_1(F)=0 and

\[
 \operatorname{ch}(F)=2-14e_1-21e_2-\tau_D+62P.
\]

Use L071's actual compatible connection, L093's actual untwisted
concentrations, L147's ordinary twisted images, L153's same-h
polystability, L154's stable-type inequalities and audited L156:

\[
 M=R^1p_{2*}(F\otimes p_1^*L^{-1}),\quad
 \operatorname{ch}(M)=24-4k+(z-167)\eta,\quad
 W=R^2p_{2*}(F\otimes p_1^*L^{-1})=\bigoplus_{x\in Z}\mathbb C_x,
\]

where Z is finite, possibly empty, z=|Z|, and 0<=z<=119.
M has no trivial stable summand, H^0(M)=H^2(M)=0 and h^1(M)=119-z.
Write m_t for the full multiplicity of the line L_B^t in the
h-polystable decomposition of M. L052's exact integral perpendicular
Picard lattice is Zk. No existence of F or nonempty Z is assumed.

## Conclusion

Every nontrivial line summand is among t=+/-1,+/-2,+/-3,+/-4, and

\[
 \sum_{t\ne0}(7t^2-2)m_t\le119-z.                    \tag{1}
\]

For every nonzero integer r, independently checked opposite
concentration and preservation give an actual h-polystable bundle

\[
 H_r=R^1p_{1*}(F\otimes p_2^*L_B^r),\qquad
 \operatorname{ch}(H_r)=(17+14r^2)+4rk-(34+98r^2)\eta, \tag{2}
\]

with H^0(H_r)=H^2(H_r)=0, h^1(H_r)=70r^2 and
H_r^vee isomorphic to H_{-r}. Its full L and L^{-1} multiplicities
are respectively m_{-r} and m_r. This is cross-power duality, not a
scalar self-duality assertion for H_r or M.

For r=1,2,3,4, set a=m_{-r}, b=m_r and q=a+b. The complete selected
line-versus-residual tests give

\[
 \begin{split}
 q&\le14r^2,\\
 7q+5|4r-a+b|&\le34+98r^2,\\
 12q+14|4r-a+b|&\le119+168r^2.                         \tag{3}
 \end{split}
\]

In particular they sharpen to

\[
 \boxed{m_{-1}+m_1\le14,\qquad m_{-1}\le12,
                         \qquad m_1\le8.}            \tag{4}
\]

For |t|=2,3,4 the selected tests add no restriction beyond (1) and
the existing M constraints. Formal numerical stable decompositions
retain each of these exponents. Formal branches also attain both
individual bounds in (4) and their sum bound; no such formal branch
is asserted to exist as a bundle or image.

This is an ADVANCE / REPRODUCTION specialization of the assessed
general results. It supplies additional necessary multiplicity control,
not progress beyond the sources checked, a better bound on z, a lower
count, F existence, a cycle, transport or universal primitive Hodge
realization. The separate critical audit below preserves these claims.

## Proof

**Imported inputs and relevance.** Reuse the invocation-start SPECIALIZE
assessment `drafts/literature/2026-10-24-double-line-twist-summand-spectrum.md`.
The target is its unchanged all-line spectrum test. A restriction on
these actual summands could support a later common-kernel/decomposition
test; independent lower control and existence remain unresolved.
The stopping test is an additional necessary restriction, or a finite
compatibility verdict parking this filter. ATTEMPTS/087's single-image
endpoint compatibility and the October 12 forward-IT stop are retained.

Import Bartocci–Bruzzo–Hernandez Ruiperez, *A hyperkahler Fourier
transform*, Differential Geometry and its Applications **8** (1998),
239–249, Definition 2 p. 244, Section 3.3 Lemmas 1–2 and Theorem 3,
pp. 245–246
([published scan](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=6)).
For the degree-one comparison use Pareschi–Popa, *GV-sheaves,
Fourier-Mukai transform, and generic vanishing*, American Journal of
Mathematics **133** (2011), 235–271, author-hosted version, Lemma 2.1
and proof p. 5 and Lemma 2.2 and proof p. 6
([source](https://people.math.harvard.edu/~mpopa/papers/GV.pdf#page=5)).
These apply to two bounded coherent inputs and a perfect product kernel;
neither an equivalence nor a universal kernel is required.

Also import perfect pushforward/base change and one-degree concentration
from [Stacks 36.30.1, 0A1H](https://stacks.math.columbia.edu/tag/0A1H)
and [36.31.3, 0BDK](https://stacks.math.columbia.edu/tag/0BDK), projection
formula from [20.54.2–3, 01E6](https://stacks.math.columbia.edu/tag/01E6),
Leray from [20.13.4, 01F2](https://stacks.math.columbia.edu/tag/01F2),
and smooth proper relative duality with p^!O=omega_p[2] from
[48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT).
The projections are smooth projective of relative dimension two;
all coefficients here are locally free and base-flat, and their
pushforwards are perfect. These hypotheses give the stated scopes.

The stable-Hom, dual-stability, K3 RR/Serre-duality and simple Mukai
inputs are Huybrechts, *Lectures on K3 Surfaces*, author draft,
Chapter 1 (2.5)–(2.6), Proposition 2.4 pp. 11–13; Chapter 9
Sections 1.2–1.3 pp. 169–170, Section 3.1 pp. 175–176 and Theorem
4.9 p. 182
([source](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=169)).
For the original real h, reuse the ordinary-bundle scope of Perego,
*Kobayashi–Hitchin corrispondence for twisted vector bundles*, Complex
Manifolds **8** (2021), Propositions 3.9–3.12 and 3.15 pp. 36–38,
as assessed and applied in L154. No theorem needs reproof; the work
below is the data-specific concentration, signed character and finite
multiplicity specialization.

**A justified finite exponent range.** Every stable summand of M is
locally free of slope zero. L156 excludes O. Stable-Hom vanishing
against O, applied also to its stable dual, gives vanishing H^0 and
H^2 separately for every remaining summand. Its Euler characteristic
is therefore nonpositive. The same is true for every residual direct
sum. A nontrivial line L_B^t has no section because a nonzero effective
divisor has positive h-degree; its inverse has no section either.
Serre duality and RR give

\[
 (h^0,h^1,h^2)(L_B^t)=(0,7t^2-2,0)\quad(t\ne0).
\]

Direct-sum cohomology and h^1(M)=119-z prove (1). If m_t>0 then
7t^2-2<=119, hence |t|<=4. This covers every line by L052; there is
no sampling cutoff or omitted integral first class. In particular
q_r=m_{-r}+m_r<=floor((119-z)/(7r^2-2)).

**Opposite endpoints and rotation-IT for each power.** Every p_1 fibre
of F is a charge-21 h-polystable rank-two bundle with determinant O.
The split alternative would require 21=14u^2, u integral, by L071
and L052, so every such fibre is stable. Tensor by L_B^r preserves
stability and slope zero. Its stable dual is also rank two of slope
zero, so equal-slope stable-Hom vanishing against O gives both endpoint
vanishings. Its character and Euler characteristic on the fibre are

\[
 (2-21\eta)e^{rk}=2+2rk-(21+14r^2)\eta,
 \qquad\chi=-17-14r^2.
\]

Thus every derived fibre is concentrated in degree one of dimension
17+14r^2. Perfect base change/concentration gives H_r locally free on
the whole S_1 and Rp_{1*}(F tensor p_2^*L_B^r)=H_r[-1].

The preferred HE connection of L_B has factor zero: its curvature
is primitive (1,1), hence ASD on this hyperkähler surface, including
its unitary centre. All its powers are quaternionic instantons.
Each restricted connection of F is ASD and irreducible, the latter
following from its stability at the original h and HE uniqueness.
Tensoring with a line preserves irreducibility. The same connections
remain ASD under every induced complex structure, so they remain
stable there and the same endpoint argument applies. This checks
rotation-IT independently for this new source coefficient. BBHR
Theorem 3 applies to compact source B, compatible spheres and L071's
actual quaternionic product kernel. It preserves the natural transform
connection, allowing reducibility of H_r. On S_1 its compatible unitary
curvature is ASD and HE of factor zero, so H_r is polystable at the
original h. This is a whole-base opposite assertion; it does not give
whole-base forward IT for F tensor p_1^*L^{-1}.

**Full signed GRR and actual cohomology.** Import Fulton, *Intersection
Theory*, second edition, Theorem 15.2 pp. 286–287 and Example 15.2.8
pp. 291–292, with the primary coverage recorded in the assessment.
For p_1 the full source factor is

\[
 e^{rk_2}(1+2e_2)=1+rk_2+(2-7r^2)e_2.
\]

In p_{1*}(ch(F)e^{rk_2}(1+2e_2)), fibre degree four gives rank
2(2-7r^2)-21=-17-14r^2, first class -rDk=-4rk and second
character 62-14(2-7r^2)=34+98r^2. Self-adjointness identifies the
opposite action with D. All other terms have the wrong fibre degree;
ch_3(F)=0 and the full mixed square has already entered 62. The
alternating class is -[H_r], proving (2) with its R^1 sign.
Torsion-free integral H^2 upgrades this first-class equality to the
integral one. RR gives chi(H_r)=-70r^2.

Endpoint vanishing of H_r itself requires another argument. Put
G_0=R^1p_{2*}F, the untwisted forward image, not M. L093 at (14,21)
makes G_0 polystable and acyclic, since chi(X,F)=0. It contains no
nontrivial zero-slope line: each such line has positive h^1, which
cannot occur in a direct summand of an acyclic bundle. Nor does it
contain O. Therefore for every integer r both ordered Hom groups
between G_0 and L_B^{-r} vanish, by the full stable decomposition.
The untwisted concentration and projection formula give

\[
 \begin{split}
 H^0(S_1,H_r)&=H^1(X,F\otimes p_2^*L_B^r)
             =H^0(B,G_0\otimes L_B^r)=0,\\
 H^2(S_1,H_r)&=H^3(X,F\otimes p_2^*L_B^r)
             =H^2(B,G_0\otimes L_B^r)=0.
 \end{split}
\]

The last zero is Serre duality and the other ordered Hom vanishing.
Only now does RR give h^1(H_r)=70r^2. In particular a nonzero-power
image is not acyclic. Polystability and H^0=0 exclude every trivial
stable summand of H_r.

**Cross-power duality and the actual double-twist comparison.** Fix
det(F)=O and a holomorphic K3 two-form on the p_1 fibre. Determinant
wedge identifies F^vee with F. Relative Serre duality and the proved
concentrations give a perfect pairing H_r tensor H_{-r}->O and
H_r^vee isomorphic to H_{-r}. The alternating coefficient sign and
odd cohomological sign cancel upon interchanging the two powers.
For r!=0 this does not assert a form H_r tensor H_r->O.

Set Q_r=F tensor p_1^*L^{-1} tensor p_2^*L_B^r. Forward projection
has ordinary images 0, M tensor L_B^r, W tensor L_B^r. In Leray,
the only total-degree-one term is (p,q)=(0,1). It has no incoming
differential; its outgoing d_2 has target (2,0)=0, and all later
outgoing targets have negative second index. Consequently

\[
 H^0(B,M\otimes L_B^r)=H^1(X,Q_r)
       =H^0(S_1,H_r\otimes L^{-1})=\operatorname{Hom}(L,H_r).
                                                               \tag{5}
\]

The second equality uses the independently proved opposite
concentration and the base line L^{-1}. This is the same coefficient
through both actual projections. W remains in degree two and can
have its later Leray differential; (5) does not remove it or assert
degeneration in all degrees.

Full stable-Hom vanishing identifies the left side of (5) with the
full multiplicity m_{-r}; hence H_r contains exactly that many L's.
Dualizing the complete decomposition of H_{-r} identifies the full
L^{-1} multiplicity in H_r with m_r. No image block or kernel
projector was independently selected.

**All selected stable-isotypic constraints.** For r>0 remove both
complete line isotypic pieces and write

\[
 H_r=L^{\oplus a}\oplus(L^{-1})^{\oplus b}\oplus R_r,
 \quad
 \operatorname{ch}(R_r)=R+Tk+d\eta,
\]

where

\[
 R=17+14r^2-q,\quad T=4r-a+b,\quad
 d=-34-98r^2+7q,\quad q=a+b.                         \tag{6}
\]

R_r has no O, L or L^{-1} stable type. Its endpoint cohomology
vanishes. Since either displayed line contributes five middle
dimensions, h^1(H_r)=70r^2 gives 5q<=70r^2, the first inequality
in (3). For a stable type with character u+vk+w eta, L154's general
simple-Mukai argument gives w<=-5|v|. Summing it over every type
with its multiplicity in R_r gives d<=-5|T|. This is the second
inequality in (3); it does not impose simplicity on R_r.

Finally both ordered Hom groups between either L^{+/-1} and every
stable type of R_r vanish; Serre duality removes Ext^2. RR therefore
requires, for both signs epsilon,

\[
 \chi(L^\epsilon,R_r)=d-5R+14\epsilon T\le0.
\]

Using (6), these are exactly the third inequality in (3). Full
multiplicities and all matrix Hom groups of repeated types remain
present. No distinct-type test is applied to repeated copies.

For r=1 the first two inequalities give q<=14,
6a+b<=76 and a+6b<=56. Thus a<=12 and b<=9. If b=9, the last
bound forces a<=2; the third inequality, using T=4-a+b, gives
-2a+26b+56<=287 and hence a>=2. Therefore a=2. The residual would
then have character 20+11k-55 eta. It saturates d<=-5|T|.
Equality in L154's uniform argument forces each nonzero-first-class
stable type to have |v|=1, w=-5 and rank two or three. Rank three
has chi=1 and contradicts its endpoint vanishings, so its rank must
be two. Equality also forces all first classes to have the positive
sign of T=11. A type with v=0,w=0 would be O by the simple bound
and Picard injection, and O has been excluded. Thus this residual
would have rank exactly 2*11=22, against its actual rank 20. This
excludes b=9 and proves all of (4). No independent stable existence
claim enters this equality exclusion.

**The remaining finite cases and the limit of the test.** For r=2,3,4,
(1) gives q<=4,1,1 respectively. Uniformly q<=4. Then

\[
 \begin{split}
 7q+5|T|&\le48+20r<34+98r^2,\\
 12q+14|T|&\le104+56r<119+168r^2,
 \end{split}
\]

and q<=14r^2. Thus (3) adds no restriction for these six exponents.
There is also no hidden residual simple-index obstruction in these
cases: assign the whole R_r in (6) to one formal stable type.
It has positive rank, negative chi=-70r^2+5q, satisfies both line
pairwise indices just checked, and its simple bound holds because

\[
 \begin{split}
 R^2+Rd+7T^2
 &\le(13+14r^2)(7-84r^2)+7(4r+4)^2\\
 &=-1176r^4-882r^2+224r+203<1\quad(r\ge2).
 \end{split}
\]

Here R>=13+14r^2 and R+d<=7-84r^2<0 justify the product bound;
the displayed polynomial is negative for r>=2. Choose the opposite
residual to be its dual. This is numerical compatibility with the
selected self, line-versus-residual and cross-power tests, not a
construction. For completeness, a lone line of exponent t=+/-2,
+/-3 or +/-4 in M at z=0 leaves a formal stable residual

\[
 (u,v,w)=(23,-4-t,-167+7t^2).
\]

Its chi=-121+7t^2 is negative even at |t|=4. Its simple bound
u^2+uw+7v^2=-3200+168t^2+56t is at most -288, and its pairwise
index against the removed line is -121-168t^2-56t<0. This retains
each exponent without claiming any actual residual existence.

The new restrictions in (4) are substantive additions to the old
M-only constraints. At z=0, the M-only formal choices
(a,b)=(13,0), (2,9), (12,3) leave single stable residual characters
(u,v,w)=(11,9,-76), (13,-11,-90), (9,5,-62), respectively.
They have nonpositive Euler characteristics, satisfy the simple
bound and every line-versus-residual index. They violate, respectively,
the new a bound, b bound and q bound. This comparison asserts formal
numerical feasibility only.

Conversely (a,b)=(12,2) and (6,8) give compatible formal branches
at z=0. Their M residuals have (u,v,w)=(10,+/-6,-69), respectively;
their H_1 residuals have (17,-/+6,-34). The M residual has chi=-49
and Mukai square 676, while the H_1 residual has chi=0 and square
74. Every residual-line index is -35 or -203; the distinct line-pair
index is -26 and each line self-index is 2. Assign scalar endpoints
to a stable residual, its required Ext^1 dimension v^2+2, zero
endpoints to distinct-type pairs and middle dimension -chi there.
This checks all self/pairwise indices; repeating the lines retains
their full matrix endpoint morphisms. Direct-sum cohomology gives
h^1(M)=70+49=119 and h^1(H_1)=70+0=70, with both endpoints zero.
Ranks and both Chern-character coefficients sum to the required
whole characters. Taking duals supplies H_{-1}; the other finite
powers have the compatible residuals above. Thus the selected tests
leave nonzero line summands, including branches attaining a=12,
b=8 and q=14. They neither exclude F nor imply these formal objects
exist. Park the completed bounded filter after separate critical
audit; a further restriction would require a different input.

The reproducible arithmetic check is
`python3 scripts/double_line_twists/check_spectrum.py`. Its full
certificate `scripts/double_line_twists/spectrum_certificate.json`
records all 21 higher-power (a,b) cases, the eight signed characters,
both surviving branches' complete ordered index/Ext matrices, the
three strict M-only comparisons and the excluded b=9 rank mismatch.
All checks pass. These exact finite checks support the arithmetic;
the analytic concentration, source applicability and equality argument
are the written proof above, checked by the separate critical audit below.

**Separate critical audit, 2026-10-24 (step 515).** Reuse the
invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-24-double-line-twist-spectrum-critical-audit.md`
and its already inspected primary theorem/proof cases. The outcome is
EXPLORATION / REPRODUCTION: no substantive error, stronger bound or
existence statement was found. This audits the specialization, without
reproving a general theorem or claiming progress beyond the sources.

The input is the actual ordinary M, rather than its derived fibre at a
split point. L147 proves its local freeness and full character with
+[W] in [M]=-[Rp_*G]+[W]. L153 supplies slope-zero polystability for
this same M and original h; L156 supplies both endpoint vanishings and
h^1=119-z. Each stable direct summand is therefore locally free and
has zero endpoints. L052's determinant lattice calculation depends
only on the marked Picard lattice and h, not on the old positive
mixed-sign hypothesis: rational independence of lambda,1,1/lambda in
its slope formula forces y=-w, x=-2w, z=w/2. Integral w is even,
giving exactly Zk. The rank-one character is exp(tk), so its middle
cohomology is 7t^2-2. Additivity gives (1) without a rank or exponent
cutoff assumption; |t|>=5 would cost at least 173>119.

For every p_1 fibre, the actual compatible restricted connection is
ASD. Its charge 21 cannot equal 14u^2 for integral u, so it is
irreducible. The preferred line curvature is ASD because its HE
factor is zero on a Kähler surface; its powers have the same property.
Tensoring by a line changes no invariant subspaces. Thus the tensor
connection remains irreducible ASD in every induced complex structure.
The compact-Kähler HE correspondence gives stability of slope zero
in each rotation. Both ordered stable-Hom groups against O vanish
because the rank is two, including for the stable dual. Fibre RR gives
middle rank 17+14r^2. These are the actual endpoint and rotation-IT
hypotheses of BBHR, not an inference from its preservation conclusion.
Perfect base change supplies the whole-base opposite image; BBHR
preserves its natural compatible connection and permits reducibility.
No forward twisted IT or inverse transform is used.

Independently expand the relative GRR integrand. On the integrated
B factor the Todd-weighted exponential is
1+rk_2+(2-7r^2)e_2. The three surviving coefficients of the pushforward
are -17-14r^2, -rD^*k=-4rk, and 34+98r^2. Here D^*=D, the degree-two
Künneth flip has sign +1, and the full rank-two ch_4 is
(2*14*21+156)/12=62. Negating these coefficients for R^1 gives (2)
and chi=-70r^2. This calculation alone supplies no endpoint vanishing.
Instead L093's untwisted equality image G_0 is actually acyclic.
Every nontrivial zero-slope line has positive middle cohomology and
O has sections, so none can occur as a direct summand of G_0.
Both ordered Hom groups with every L_B^{-r} vanish. The two single-row
Leray calculations and Serre duality in the proof therefore give both
endpoints of H_r. This verifies the all-power cohomology statement
without transferring acyclicity to a nonzero-power transform.

For relative duality put E_r=F tensor p_2^*L_B^r. Fixing det F and
the fibre K3 form gives E_r^vee=E_{-r} and omega_p=O. With
Rp_*E_r=H_r[-1], the smooth-proper duality isomorphism reads
RHom(H_r[-1],O)=Rp_*(E_{-r}[2])=H_{-r}[1]. The left side is
H_r^vee[1], proving the claimed duality with its shift. Equivalently
fibre Serre trace pairs the two degree-one groups perfectly. It is a
cross-power pairing, with the odd cup and alternating determinant
signs cancelling; it is not a form on H_r alone. In the forward
Leray sequence of Q_r, (0,1) has no incoming differential and its only
possible nonnegative-index outgoing target is (2,0), which is zero.
The top W survives as a separate term and need not have a vanishing
later differential. This proves exactly (5). Stable-Hom then measures
the full L isotypic multiplicity. Apply the same argument to -r and
dualize the full decomposition to obtain the full L^{-1} multiplicity.
This checks both powers and both line types using one actual kernel.

For the residual in (6), the three inequalities follow respectively
from its nonnegative middle dimension, from summing the stable-type
bounds, and from the two ordered line-versus-residual RR indices.
Explicitly chi(L^epsilon,R)=d-5R+14epsilon T: the minus in the
first class of the dual line is already included in this sign.
The residual has neither of the two removed line types. Stable-Hom
and Serre duality therefore justify a nonpositive Euler value for
both signs, while repeated stable types retain matrix endomorphisms.
For r=1, the first-class inequalities become 6a+b<=76 and a+6b<=56.
At b=9 they give a<=2; the positive-T pairwise bound gives
290-2a<=287, hence a>=2 by integrality. The forced residual is
(20,11,-55). Equality in the summed uniform inequality forces zero
deficit for every stable type and no cancellation of nonzero first
classes. L154's completed-square bound then permits only |v|=1,
w=-5 and rank 2 or 3, or v=w=0 and rank 1. The latter is O and is
excluded. Rank 3 has chi=1 and is excluded by the already proved
endpoint vanishings. All remaining v have positive sign and total
11 with multiplicities, so the rank must be 22. This contradicts
20. The certificate stores this rank mismatch; its validity comes
from this equality argument, not a hardcoded certificate value.

Finally the finite and uniform compatibility claims retain precisely
their stated scope. For r=2,3,4 the budget gives q<=4,1,1. The displayed
bounds on |T| and R(R+d) have the correct directions because R+d is
negative. Their polynomial is negative for every r>=2: bound
224r<=112r^2 and 203<=51r^2 to leave a strictly negative expression.
Thus the formal single-residual simple test is not based on finite
sampling. There are 15+3+3=21 enumerated pairs in the relevant finite
range. Beyond |r|=4, both multiplicities are zero by (1); the same
uniform inequalities cover that zero-line case as well.

Read the complete selected certificate values with the JSON inspector:
all eight signed transform characters, all 21 higher-power cases,
both surviving models' ordered Euler and Ext^1 matrices, all three
M-only comparisons, all six remaining signed exponents and the b=9
record. Re-ran `python3 scripts/double_line_twists/check_spectrum.py`:
PASS, no failures. Its generator computes the K3 pairing
chi((u,v,w),(u',v',w'))=2uu'+uw'+u'w+14vv', correctly retaining
ordered pairs and multiplicities. For (a,b)=(12,2), full End Ext
dimensions are (149,6938,149) for M and (149,6336,149) for H_1;
for (6,8) they are (101,6842,101) and (101,6240,101). Their Euler
values are respectively -6640 and -6038 in both branches, agreeing
with the whole characters. Cohomology sums remain 119 and 70.
These are complete numerical checks of the selected indices, not
joint geometric realizations or verification of every possible
common-kernel condition.

The conditional spectrum and the b=9 exclusion survive. The two
extremal formal branches and the higher exponents remain compatible
with the selected tests, so the bounded filter is parked. No better
z bound, contradictory lower count, nonempty Z, F, transport or new
Hodge class is established. Direct mathematical inputs and DAG edges
remain unchanged. The main argument in PROOF.md does not change.

## Mathlib

Full matching coverage for this K3 double-transform specialization,
real-h stable decompositions and cross-power multiplicity statement
is **not checked**. Unknown coverage is not absence. The cited
general theorems are imported; all character and multiplicity
specializations above are REPRODUCTION, with no novelty, actual
stable-image existence or Lean-verification claim.
