# L172 — The actual section image avoids the KS radical

## Hypotheses

Retain the entire conditional family and actual maps of L164 and
L171, and the radical identification of L170. Thus S_1 and B are the
identical marked projective K3 factors with the fixed common
hyperkähler metric, real Kähler class, ordered triple, holomorphic
forms and actual compatible connection. The hypothetical locally free
rank-two product-polystable bundle F on X=S_1 x B has integral
c_1(F)=0 and

\[
 \operatorname{ch}(F)=2-14e_1-21e_2-\tau_D+62e_1e_2.
\]

Put V=End_0(F), p:X -> B, C=Rp_*V, M=R^1p_*V and
W=R^2p_*V. The split set Z is finite and reduced. Keep L108's
specific extended inclusion i:T_B -> M and retraction r:M -> T_B,
with ri=id and N=ker r, so M=i(T_B) direct sum N. By L116,
N=O_B^t direct sum A, H^0(B,A)=0 and H=H^0(B,M) has dimension t.
The rank of M is 50. Use L164's actual truncation inclusion j,
the injection e_z:M(z) -> E_z=H^1(S_1,V_z) at z in Z, and
rho_z(u)=e_z(u(z)). Here M(z) is the ordinary residue fibre, while
E_z is the full 52-dimensional derived middle space. Use the same
actual KS map kappa_z and symmetric obstruction form B_z as in
L170/L171, with Q_z=e_z(M(z)) and K_z=kappa_z(T_zB).

No ordinary middle-base-change isomorphism, generic position,
integrability of arbitrary sections, multiplicative splitting,
endpoint s,t, existence of F, or nonemptiness of Z is assumed.

## Conclusion

For every z in Z,

\[
 \rho_z(H)\cap K_z=0.                                  \tag{1}
\]

Consequently, if rho_z(H) is totally isotropic for B_z at a split
point, then t<=24. In particular, when Z is nonempty, vanishing of
L164's actual projected bracket beta:Sym^2 H -> H^0(B,W) requires
t<=24; if t>24, beta is nonzero. This sharpens the previous
conditional threshold 26 to 24. It gives no converse for t<=24,
no unconditional upper bound on t, and no exclusion of F or a split
cardinality. For empty Z the point assertions and test are vacuous;
for t=0 the section image is zero.

This is a local ADVANCE / REPRODUCTION of the previously assessed
standard tools, not a claim of progress beyond the sources checked.
The separate step 575 audit below preserves the conclusion
(EXPLORATION / REPRODUCTION), with no substantive correction or
stronger result. Actual section quadrics,
the complementary global operation, minimum square length, existence
of F, transport and primitive realization remain unresolved.

## Proof

**Imported tools and scope.** The invocation-start SPECIALIZE
assessment is
`drafts/literature/2026-10-26-section-image-ks-radical-intersection.md`.
Import ordinary pullback of module sheaves and its stalk/tensor
description from Stacks Project, Section 6.26, Definition 6.26.1
and Lemmas 6.26.2/6.26.4
([tag 0094](https://stacks.math.columbia.edu/tag/0094)).
For the ordinary point fibre this is tensoring the stalk with its
residue field. Functoriality preserves split inclusions and their
retractions; no flatness of the point map is required. The orthogonal
dimension argument is already specialized in L170 (2), using Keith
Conrad, *Bilinear Forms*, author-hosted 63-page version, Theorem 3.12
and proof, pp. 18–19
([primary text](https://kconrad.math.uconn.edu/blurbs/linmultialg/bilinearform.pdf#page=18)).
We apply L170's inequality without reproving its radical calculation
or these general tools. The remaining work is to compare the actual
section and summand maps; an arbitrary subspace of dimension t would
not have the needed position.

**Place sections in the fixed normal summand.** By L164's K3
section input H^0(B,T_B)=0. Thus the map H^0(r) sends every u in H
to the zero section. Naturality of ordinary evaluation gives

\[
 r(z)(u(z))=(r u)(z)=0.                                 \tag{2}
\]

Apply ordinary point pullback to L108's actual splitting and to
ri=id. This gives

\[
 M(z)=i(z)(T_zB)\oplus N(z),\qquad r(z)i(z)=id,
 \qquad \ker r(z)=N(z).                                 \tag{3}
\]

In particular u(z) lies in N(z). This uses a split sequence, not
left exactness of tensor on a nonsplit sequence. L116 further
identifies H with the sections of the full trivial summand O_B^t:
H^0(T_B)=H^0(A)=0 and H^0(O_B)=C. Its inclusion remains split on
every ordinary fibre. Evaluation therefore identifies H with its
t-dimensional fibre image inside N(z), as already used in L164.
The identification with that trivial summand is not needed to choose
a new normal complement; N remains precisely ker r.

**Pass through the same injective derived map.** Let w lie in
rho_z(H) intersect K_z. Write w=e_z(u(z)) for u in H. L171 gives
K_z=e_z(i(z)(T_zB)), so w=e_z(i(z)v) for some v in T_zB.
L164's injectivity of this same e_z implies u(z)=i(z)v. Applying
r(z), equations (2)–(3) give 0=v. Hence w=0, proving (1).
The argument only injects the ordinary fibre into E_z; it does not
identify that fibre with E_z or remove either extra derived middle
direction.

**Apply the existing isotropy inequality.** Put T=rho_z(H) subset
Q_z. L164 gives dim T=t. By L170, rad(B_z|Q_z)=K_z and, if T is
isotropic,

\[
 \dim T-\dim(T\cap K_z)\le24.
\]

Equation (1) makes the left side t, proving the claimed t<=24.
L164 identifies beta=0 exactly with total isotropy of every actual
rho_z(H). If Z is nonempty and t>24, choose a split point; isotropy
there is impossible, so beta cannot vanish. No isotropy is inferred
from the section splitting itself. In particular, a nonzero beta
obstructs some first-order deformation but does not contradict
existence of its central F. This stops at the unknown actual bracket
values and preserves the failures recorded in ATTEMPTS/092–094.

**Separate critical audit (2026-10-26, step 575).** The unchanged
invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-26-section-ks-intersection-critical-audit.md`
approves precisely this audit. Reuse its inspected Stacks 0094
pullback tools and Conrad Theorem 3.12, with the citations and
hypotheses above. The actual geometric comparisons are the audited
conditional inputs L108, L116, L164, L170 and L171, not new
consequences asserted from the general sources. No source hypothesis,
coefficient, KS convention or base-change square changes.

First, fix the summands before evaluating. L108 extends the actual
stable-open inclusion and retraction as maps into the same bundle
M, with ri=id and N=ker r. L116's (8) decomposes this N, rather
than an independently chosen complement, as O_B^t direct sum A
with H^0(A)=0. On the connected projective K3 base,
H^0(O_B)=C and H^0(T_B)=0. Thus H^0(r)(u)=0 for every u in
the full H, and H is exactly the section space of that trivial
summand. Naturality of stalk reduction gives (2). Tensor pullback
preserves the displayed direct sum and the identity ri=id;
consequently (3) holds at every point, including Z. This does not
use preservation of a nonsplit kernel under tensor. The trivial
summand inclusion has a retraction after reduction as well, so
evaluation of its constant sections is injective at each point.
Hence the dimension used below is the full t, not a generically
evaluated subspace or an assumed position of arbitrary sections.

Second, check the identity of the derived arrows. In L164,
e_z is H^1 of the derived pullback of the actual truncation
j:M[-1] -> C. L171 uses precisely this j and L108's same i:
its stalk equality alpha_R=j_R i_R[-1] gives
e_z i(z)=kappa_z with the fixed first-order convention. L164's
local free-complex argument makes this e_z injective. The source
is the ordinary 50-dimensional M(z); the target remains the full
52-dimensional E_z, including both residual Koszul directions.
For an element in the proposed intersection, injectivity therefore
really gives u(z)=i(z)v. Applying the same reduced r gives
0=r(z)u(z)=r(z)i(z)v=v. This verifies (1) with the actual maps;
neither a scalar comparison nor equality of dimensions is being
used in place of the map comparison.

Third, L170 identifies the radical of B_z on this same Q_z as
K_z, and the quotient form on Q_z/K_z is nondegenerate in
dimension 48. If T=rho_z(H) is isotropic, its image in that
quotient has dimension dim T-dim(T intersect K_z)=t by (1)
and the preceding injectivity. L170's inequality therefore gives
2t<=48. L164's bracket/base-change identity and its nonzero
normalized trace test identify total isotropy with vanishing of
every residue of beta. The reduced length-one support of W
makes those residues detect the global value. Thus beta=0 implies
t<=24 whenever Z is nonempty; conversely t>24 at any split point
forces beta nonzero. There is no reverse implication for t<=24.
If Z is empty there is no pointwise dimension test, and W=0;
if t=0 both the section image and bracket source vanish.

This audit finds no substantive error, new bound or evaluated
section quadric. It preserves the conditional specialization and
its existing dependencies; it is not a fresh
audit of their entire ancestry. No section was assumed to
integrate, no additive splitting was made multiplicative, and
nonzero beta does not exclude its central F. Actual quadrics,
the complementary operation, minimum square length, F existence,
transport and primitive realization remain open. ATTEMPTS/092–094
remain preserved. The outcome is EXPLORATION / REPRODUCTION,
not a new mathematical advance beyond the inspected sources.

## Mathlib

Full matching coverage of this actual section/KS/radical comparison
has not been checked; no absence is claimed. The proof imports the
cited ordinary pullback tools and L170's previously established
finite-dimensional inequality. It is an informal conditional
specialization, not a Lean verification or a Hodge-conjecture solution.
The separate audit above checks only this informal specialization;
full matching Mathlib coverage remains unchecked.
