# L150 — Preferred twisted metric and the actual central weight planes

## Hypotheses

Retain the conditional equality kernel and identical marked hyperkähler
K3 factors of L094/L095: F is locally free of rank two and
Omega-polystable, with integral c_1(F)=0 and
ch_2(F)=-14e_1-21e_2-tau_D. Use its supplied compatible Hermitian
connection, the ordered structures I,J,K, and sigma=omega_J+i omega_K.
Let L have c_1(L)=k=(-4,-2,1,2), k.h=0 and k^2=-14. Fix the
Hermite--Einstein line metric h_L used in L094. Give the auxiliary
twisting line L^{-1} exactly the dual metric h_L^{-1}. On
G=F tensor p_1^*L^{-1} use the tensor product metric.

Retain L146's actual incoming and outgoing maps, L148's natural
central harmonic comparison, and L149's intrinsic central spaces.
The split set Z is finite and may be empty. At an arbitrary z in Z,
write the actual KS classes, before the stabilizer quotient, as

\[
 a_i=\begin{pmatrix}0&p_i\\q_i&0\end{pmatrix},\qquad
 p_i\in H_+=H^1(L^2),\quad q_i\in H_-=H^1(L^{-2}),
 \quad i=1,2.
\]

Here the tangent basis is the same in both projections. Put

\[
 A_z=\operatorname{span}(p_1,p_2),\quad
 P_z=\operatorname{span}(q_1,q_2),\quad
 J_z=\{c\in H_-:T(p_i\wedge c)=0\ (i=1,2)\},
 \qquad T(d)=(2\pi i)^{-2}\int_{S_1}\sigma\wedge d.
\]

No real structure on G, nonempty Z, or existence of F is assumed.

## Conclusion

For the central harmonic Hermitian product h_{G,z} determined by this
preferred metric, with first slot anti-linear,

\[
                       J_z=P_z^{\perp_{h_{G,z}}}.             \tag{1}
\]

Consequently the central cross block B(0) of L149 is zero at every
actual split parameter for this metric and L148's specified natural
comparison. If Z is empty the statement is vacuous. This is a
conditional local input, classified REPRODUCTION; the separate critical
audit below preserves it. It selects no assertion about an arbitrary other
twisting-line metric. No curvature estimate, metric or connection
extension, positivity, split-set bound, F, algebraic cycle or transport
is proved here; applying the curvature criterion is a later step.

## Proof

**Known inputs and scope.** Reuse the pre-invocation SPECIALIZE
assessment `drafts/literature/2026-10-23-twisted-preferred-metric-central-test.md`.
Import coefficient harmonic quaternionic invariance from Verbitsky,
*Hyperholomorphic bundles over a hyperkähler manifold*,
[alg-geom/9307008v1, Section 4, Proposition 4.2, Theorem 4.1 and
Corollary 4.3, PDF pp. 13--16](https://arxiv.org/pdf/alg-geom/9307008v1#page=13).
Its parallel-real coefficient here is End_0(F_z), with the actual
split compatible connection and skew-adjoint real form. L094 checks
these hypotheses, including reducibility. We do not apply that theorem
to G or invoke a constant-rank transform theorem across Z.

L094/L095 supply the actual quaternionic injective derivative. L113's
oriented coefficient-frame identity compares its adjoint harmonic
Serre and Hermitian products. L146 supplies the defining-coefficient
weight maps, and L148 supplies the natural derived-fibre metric
identification using Bismut--Gillet--Soulé, *Analytic torsion and
holomorphic determinant bundles III*, Comm. Math. Phys. 115 (1988),
301--351, DOI 10.1007/BF01466774, Section 1(b)--(c), Theorem 3.5
and Lemmas 3.6--3.8. These general results are imported without
reproof. The remaining specialization must compare the two projected
planes and the actual twisted metric; an adjoint complement alone
does not do this.

**Both actual weight projections.** Use first a unitary central
marking. Let phi(a)=a^{0,1} be L094's identification from real
skew-adjoint ASD-harmonic forms to the adjoint Dolbeault harmonic
space H_+ direct sum H_-. Transport I_c,J_c,K_c through phi,
writing script-J for phi J_c phi^{-1}. The operator script-J is
anti-complex-linear, isometric for the adjoint harmonic product, and
has square -1. It exchanges H_+ and H_-: it commutes with the real
compact stabilizer action, and its anti-linearity conjugates the
circle characters of weights +2 and -2.

Let W be the image of the actual complex KS map in this harmonic
space. L094/L095 identify it with the same real quaternionic line;
therefore script-J(W)=W. Its weight projections are exactly A_z and
P_z. If pi_+,pi_- denote those projections, weight exchange gives
script-J pi_+=pi_- script-J. Hence

\[
             \text{script-J}(A_z)
              =\pi_-(\text{script-J}(W))=P_z.                \tag{2}
\]

This uses the actual entire KS plane, not L094's illustrative plane.
Both projections have dimension two by the actual rank input retained
in L146/L149. An allowed constant complex central marking multiplies
the two weight blocks by inverse nonzero scalars. Their image
subspaces, and therefore the equality of subspaces in (2), are
unchanged. Metric identities below are evaluated in the unitary marking
and transported with the metric, rather than declaring that marking
unitary after a nonunitary change.

**The cross-weight Serre product.** Let h_ad be the ordinary
Dolbeault L2 product of the actual adjoint connection and let
g_0(a,b)=-integral Tr(a wedge *b). L113's coefficient-frame identity,
with these unscaled products and the same sigma and orientation, is

\[
 \Omega(\phi(a),\phi(b))
  =\frac{g_0(J_ca,b)+i g_0(K_ca,b)}{4\pi^2},\qquad
 \operatorname{Re}h_{ad}(\phi(a),\phi(b))=g_0(a,b)/2,
                                                               \tag{3}
\]

where Omega(b,c)=T(Tr(b wedge c)). Since K_c=I_c J_c,
phi I_c=i phi, and the first Hermitian slot is anti-linear,
Re h_ad(iu,v)=Im h_ad(u,v). Thus (3) gives on the full harmonic
space

\[
             \Omega(b,c)=\frac1{2\pi^2}
                              h_{ad}(\text{script-J}b,c).     \tag{4}
\]

For b the upper off-diagonal form p and c the lower off-diagonal
form c, their matrix product has trace p wedge c. Restricting (4)
therefore gives, for every p in H_+ and c in H_-,

\[
        T(p\wedge c)=\frac1{2\pi^2}
                          h_{ad,-}(\text{script-J}p,c).       \tag{5}
\]

Here h_ad,- is the actual negative-weight product, not a putative
scalar self-duality of G. Combining (2) and (5) proves

\[
                         J_z=P_z^{\perp_{h_{ad,-}}}.          \tag{6}
\]

In particular this step does not require the projected positive plane
itself to be quaternionic. The full W is quaternionic; script-J maps
its two distinct projected planes onto one another.

**Actual twisted metric and harmonic representatives.** In the
central holomorphic splitting F_z=L direct sum L^{-1}, the supplied
compatible connection is the orthogonal direct sum of its HE line
connections, as in L094/L095. Under any such fixed holomorphic
identification, its line metrics have the form

\[
                 h_{+,z}=\alpha_z h_L,\qquad
                 h_{-,z}=\beta_z h_L^{-1},
                 \qquad \alpha_z,\beta_z>0,                 \tag{7}
\]

where the scalars are constant on S_1. To justify specifically this
metric comparison, both metrics on each line have zero HE contraction:
the restricted connection is ASD and k.h=0. The logarithm of their
positive ratio has scalar Laplacian zero. The maximum principle on
the connected compact S_1 makes that logarithm constant. This is the
line-metric uniqueness specialization; no analytic existence theorem
or harmonic-action theorem is being reproved. No relation between the
two constants, or between constants at different split points, is needed.

On Hom(L,L^{-1}) the adjoint coefficient metric is
(beta_z/alpha_z)h_L^{-2}. On the negative summand of
G_z=O direct sum L^{-2}, the preferred tensor metric is
beta_z h_L^{-2}. The summands are orthogonal, and H^1(O)=0.
Consequently the entire central middle metric is obtained from that
negative summand, with coefficient metric exactly alpha_z times the
adjoint negative-weight metric. Multiplying a coefficient metric by a
positive constant leaves the Dolbeault adjoints and Laplacians unchanged:
the same constant multiplies the products in both degrees in the
defining adjoint identity. Its harmonic representatives therefore
coincide, and their L2 products satisfy

\[
                         h_{G,z}=\alpha_z h_{ad,-}.           \tag{8}
\]

This verifies the actual metric identification, not just equivalence
of norms. Unlike an arbitrary nonconstant weight, the scalar in (8)
requires no elliptic correction. Combining (6) and (8) proves (1).

Finally, L148's central residual differential is zero and its specified
spectral comparison is the natural identification with all of H^1(G_z).
L146/L149 identify the central incoming plane with P_z and the entire
central free complement with J_z. Thus (1) makes their actual harmonic
cross block zero in that very comparison. No arbitrary automorphism
of the derived middle fibre is inserted. The proof uses no property
special to the selected z and hence applies at every z in Z, for the
single globally fixed twisting metric h_L^{-1}. All arbitrary-metric
failures in ATTEMPTS/086 retain their scope. L149's curvature criterion
remains pending separate critical audit; this proof establishes only
the approved central orthogonality input.

**Separate critical audit — 2026-10-23, step 482.** The unchanged
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-23-preferred-twisted-central-critical-audit.md`
authorizes exactly this audit. Reuse its inspected Verbitsky Section 4
and BGS III theorem/proof coverage, and the standard scalar maximum
principle. No new primary retrieval or stronger source theorem is
claimed. The verdict is EXPLORATION / REPRODUCTION: the conditional
conclusion survives, with no substantive error, necessary repair or
stronger conclusion found. The following checks concern this existing
specialization, not a new lemma or a curvature application.

First, all weight spaces use the actual restricted connection. For a
real base tangent t, its (1,0) tangent is u=(t-iIt)/2. L095 gives
r_{It}^{0,1}=i r_t^{0,1}, hence r_u^{0,1}=r_t^{0,1}. Thus the actual
complex KS image is precisely phi of the real quaternionic image;
there is no factor two, conjugation or replacement by L094's example.
For the compact stabilizer C_theta and p of weight +2,
script-J(C_theta p)=exp(-2i theta) script-J(p), while commutation
with C_theta makes this C_theta script-J(p). This proves negative
weight, and the reverse case is identical with the signs reversed.
Since script-J is bijective and preserves the entire KS image W,
projecting script-J(W)=W proves (2) as equality, not containment.
Neither projected plane is being asserted quaternionic. L146's
actual weight ranks supply their complex dimensions two.

Second, check the Riesz identity with the stated convention. In L113's
oriented frame, omega_I squared divided by two is dVol; the six
coefficients for J are (0,1,0,0,-1,0), and those for K are
(0,0,1,1,0,0). Their negatives under reversal and zero diagonals
verify its real wedge identity for every ordered covector pair.
Multiplication by -Tr(XY) allows arbitrary skew-adjoint coefficient
matrices; matrix commutativity is unnecessary. Only the (0,2) part
survives against sigma, and the negative factor (2pi i)^(-2) converts
the negative-trace identity into the positive 1/(4pi^2) in (3).
The inverse real/Dolbeault map b -> b-b^* gives norm squared twice
the Dolbeault norm squared, proving the second identity in (3).
If h_ad(script-J b,c)=x+iy, then
Re h_ad(i script-J b,c)=y, since its first slot is anti-linear.
Using K_c=I_c J_c in (3) consequently gives exactly (x+iy)/(2pi^2).
This verifies (4), including its sign, coefficient and complex
bilinearity: anti-linearity of script-J cancels that of the first
Hermitian slot. The upper matrix p followed by the lower matrix c
has trace p wedge c, with no additional two or reversed odd product.
Thus (5) represents the actual outgoing functionals in L146, and
their common kernel is exactly (6).

Third, the two line constants must remain separate. At the split
fibre the actual HE connection preserves the two nonisomorphic
stable line summands; its orthogonal holomorphic splitting is the
one supplied in L094/L095. There is no off-diagonal holomorphic
change of splitting, since H^0(L^{2})=H^0(L^{-2})=0. Both the
restricted positive line metric and h_L have zero HE contraction;
the same is true on the negative line and h_L^{-1}. Applying the
scalar maximum principle to each logarithmic ratio separately
gives the two positive constants alpha_z and beta_z in (7).
The Hom metric divides the negative metric by the positive one,
whereas the defining twist multiplies the negative metric by
the fixed h_L^{-1}. Their ratio is alpha_z, not beta_z or an
unspecified function. In every Dolbeault degree the whole negative
coefficient inner product is multiplied by this same constant, so
the defining adjoint identities, Laplacians and harmonic kernels
are unchanged. Orthogonality of the coefficient splitting makes
the differential and Laplacian block diagonal, and H^1(O)=0 removes
the other middle block. This proves the exact metric equality (8)
on all 26 central middle classes. No uniform constant across Z,
determinant normalization alpha_z beta_z=1, or real structure on G
is needed.

Fourth, check the actual complex and comparison. L146 identifies
the incoming derivatives with q_1,q_2 by the boundary of (1,0),
and its outgoing derivatives with c -> T(p_i wedge c), in one
specified minimal complex. For its full complement J, rho(j)=0
forces these two functionals to kill j(0). Their restrictions to
span(q_1,q_2) form L146's invertible alternating matrix. Their
common kernel therefore has dimension 24 and equals the residue
of J. L148's already audited central comparison is the specified
derived-fibre identification, and both residual differentials are
zero. Pulling back the harmonic metric through that comparison
retains precisely these planes and hence their zero cross block.
The ordinary middle fibre of dimension 24 is never substituted for
the derived middle space of dimension 26. Changing a constant
nonunitary marking rescales the two weight coordinates inversely;
the planes and Serre annihilator are unchanged as subspaces, and
the Hermitian product and quaternionic operator are transported
with the marking. Their coordinate matrices need not stay fixed.

These checks hold at any selected actual z, using the single fixed
twisting metric h_L^{-1}; empty Z remains vacuous. L149 is used
only to identify its central cross block, not to import or verify
its curvature dichotomy. That criterion still needs independent
audit. ATTEMPTS/086's nonconstant-metric obstruction remains intact.
No metric extension, positivity, split-count bound, F or nonempty Z,
cycle, transport or universal primitive Hodge realization follows.
The direct mathematical inputs and the argument are unchanged.

## Mathlib

Full matching coverage for this actual-family projected-weight and
preferred-metric specialization is **not checked**. The harmonic-action
and spectral tools are imported from the precise sources above; the
weight projection and constant-metric comparison are the stated
specializations. Unknown coverage is not evidence of absence. No
mathematical script or originality claim is used. The separate critical
audit above preserves the conditional result within these hypotheses.
