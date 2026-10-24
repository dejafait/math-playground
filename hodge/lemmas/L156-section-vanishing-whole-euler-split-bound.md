# L156 — Whole-Euler bound from twisted section vanishing

## Hypotheses

Retain L147's identical marked smooth projective complex K3 factors
S_1 and B, common hyperkähler metric g, real Kähler class h, fixed
numerical chamber and full integral mixed tensor tau_D. Suppose F on
S_1 x B is locally free, rank two and slope-polystable for
Omega=p_1^*h+p_2^*h, with integral c_1(F)=0 and
ch_2(F)=-14e_1-21e_2-tau_D. Put k=(-4,-2,1,2), k.h=0,
k^2=-14 eta, integral_B eta=1, and let L on S_1 have class k.
Use the preferred dual HE twisting metric of L153 and set
M=R^1p_{2*}(F tensor p_1^*L^{-1}). Let Z be the finite, possibly
empty, split-parameter set and z=|Z|. Use the audited conclusions
of L147, L153 and L155 for this same bundle and metric:

\[
 \operatorname{ch}(M)=24-4k+(z-167)\eta,\qquad
 M\text{ locally free and }h\text{-polystable of slope zero},
 \qquad H^0(B,M)=0.
\]

No existence of F or nonempty Z, simplicity, self-duality or
acyclicity of M, or independent lower count is assumed.

## Conclusion

The actual ordinary bundle satisfies

\[
 H^0(B,M^\vee)=H^2(B,M)=0,\qquad
 (h^0,h^1,h^2)(B,M)=(0,119-z,0),
 \qquad \boxed{0\leq z\leq119}.
\]

This improves L155's necessary upper bound 146. At z=119 the
conclusion would force M to be acyclic; no surviving count or bundle
is asserted to occur. This is ADVANCE / REPRODUCTION of assessed
known tools; the separate critical audit below preserves the conclusion.
It supplies no
contradictory lower count, F, cycle, transverse transport or resolution
of universal primitive rational Hodge realization.

## Proof

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-24-section-vanishing-euler-split-bound.md`.
Import Huybrechts, *Lectures on K3 Surfaces*, author draft,
[Chapter 9, Section 3.1(iii)–(iv), pp. 175–176](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175),
for dual stability, and
[Theorem 4.9, p. 182](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182)
for the HE/polystable decomposition. Equal-slope stable-Hom and
parallel-morphism coverage at a real Kähler metric is also recorded
in Perego, *Kobayashi–Hitchin corrispondence for twisted vector
bundles*, Complex Manifolds **8** (2021), Propositions 3.9–3.12 and
3.15 with proof, pp. 36–38
([source](https://unige.iris.cineca.it/retrieve/e268c4cd-97f6-a6b7-e053-3a05fe0adea1/10.1515_coma-2020-0107.pdf#page=36)).
Use ordinary bundles, trivial cocycle, zero B-field and equal zero
Einstein factors. L153 verifies applicability at the original h.
These general results are imported, without reproof.

Decompose the actual M as a finite holomorphic direct sum
\(\bigoplus_i A_i^{\oplus m_i}\), where the A_i are stable of slope
zero and m_i>0. The factors are locally free as direct summands of M.
The trivial line O_B is stable of slope zero. Equal-slope stable-Hom
vanishing says that both Hom(O_B,A_i) and Hom(A_i,O_B) vanish unless
A_i is isomorphic to O_B. Such a trivial factor would contribute
m_i>0 to h^0(M), contradicting L155. Hence every factor is
nontrivial, both ordered Hom groups vanish for every i, and

\[
 H^0(B,M^\vee)=\operatorname{Hom}(M,O_B)
       =\bigoplus_i\operatorname{Hom}(A_i,O_B)^{\oplus m_i}=0.
\]

Equivalently the stable dual factors also have no trivial type.
This controls the whole dual without identifying it with M or
restricting the ranks, first classes or multiplicities of its factors.

Import K3 Serre duality and RR from Huybrechts,
[Chapter 1, (2.5)–(2.6), Proposition 2.4, pp. 11–13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11).
Here B is smooth projective, K_B=O_B and M is locally free, so
H^2(B,M)=H^0(B,M^vee)^*=0. The Todd class is 1+2 eta. Using the
full signed ordinary character of L147 gives

\[
 \chi(B,M)=\int_B\operatorname{ch}(M)(1+2\eta)
            =48+(z-167)=z-119.
\]

The degree-two term -4k contributes nothing to this integral because
the K3 Todd class has zero degree-two part. Its square is already
included in ch_2(M); there is no extra c_1-square term to add.
Both endpoint groups now vanish, so z-119=-h^1(B,M)<=0.
Finiteness of Z gives z>=0. Thus the achieved threshold 119 is
strictly below the previous necessary upper bound 146, by 27.

Only the ordinary M enters this Euler sign. The point sheaf
R^2p_{2*}(F tensor p_1^*L^{-1}) remains present in L147's derived
pushforward; its contribution is already included in z-167.
No whole-base twisted IT, opposite-image acyclicity transferred to M,
scalar self-duality, simple-bundle index or positive lower count is
used. ATTEMPTS/087's formal compatibility without independent section
vanishing is preserved. Empty Z remains allowed. The one approved
whole-Euler test succeeds; independent lower control remains open.

**Separate critical audit, 2026-10-24 (step 509).** Use the unchanged
invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-24-whole-euler-split-bound-critical-audit.md`.
The verdict is EXPLORATION / REPRODUCTION: the conditional bound and
cohomology formula survive without substantive repair or strengthening.
The general stable-Hom, HE decomposition, Serre-duality and RR theorems
are imported at the precise locators above, using their recorded
primary-proof coverage; this audit does not reprove them.

First match all three direct inputs. L147 and its step-471 audit use
exactly the coefficient F tensor p_1^*L^{-1}, the original common
metric and fixed negative tensor, and the ordinary R^1 image on B.
They establish local freeness at every point, no hull correction,
and the displayed character, including +z eta from the ordinary top
image W. L153 and its step-497 audit identify the preferred smooth
ASD Chern connection on that very M, including its unitary centre.
They supply polystability at the original real h, with Einstein
factor zero and slope c_1(M).h/24=0. No polarization change or
replacement by an abstract bundle occurs. L155 and its step-505
audit use the same coefficient and ordinary M. Their actual section
vanishing is proved before invoking the z=147 endpoint comparison;
it is not restricted to that endpoint. Thus its use here is valid
for every hypothetical F in the stated scope, including Z empty.
These previously audited inputs are retained, not independently
reaudited through their earlier dependencies in this step.

Next check the two ordered morphisms separately. In the actual
polystable decomposition all stable summands have slope zero and
are locally free direct summands; there are finitely many, with
positive integral multiplicities. O_B is a stable line of the same
slope. The cited equal-slope stable-Hom result applies to
Hom(O_B,A_i), and says that a nonzero morphism requires A_i=O_B
up to isomorphism. Each such summand contributes a nonzero section
to the direct-sum cohomology of M, so L155 excludes every one.
Apply the same cited result with the source and target reversed:
Hom(A_i,O_B)=0 for each remaining type. Summing these latter groups
is Hom(M,O_B)=H^0(B,M^vee), so the dual-section vanishing follows.
The real-h hypotheses are covered by the inspected Kahler-class
theorem; alternatively the recorded parallel-morphism theorem has
equal zero Einstein functions on both sides. The argument requires
neither a rational polarization nor simplicity or self-duality of M,
and makes no restriction on the ranks or determinants of its factors.

Serre duality now applies to a locally free ordinary bundle on a
smooth projective K3: K_B is trivial and H^2(M) is the dual of
Hom(M,O_B), hence zero. For RR, the only top-degree terms of
(24-4k+(z-167)eta)(1+2eta) are 48eta and (z-167)eta.
Therefore chi(M)=z-119. Independently, retaining the nonzero first
class gives c_1(M)^2/2=-112eta and c_2(M)=(55-z)eta, so the
Chern-class form of RR reads 48-112-(55-z)=z-119 as well.
This is the same calculation in two conventions, not an additional
c_1-square correction to ch_2. The actual endpoint vanishings give
h^1(M)=119-z. Nonnegativity excludes z=120 already, and every larger
integer, while z=119 forces acyclicity and z=0 would give h^1=119.
Neither boundary is asserted realizable.

Finally, W remains in derived degree two. The Euler sign above is
for M, with W's contribution already included in its character;
no whole-base twisted IT or transfer of opposite-image acyclicity
is used. ATTEMPTS/087's compatible formal endpoint lacked L155's
independent vanishing and remains a valid stop for its narrower
numerical test. Direct mathematical inputs remain L147, L153 and
L155; L154 enters only the comparison with the older bound. No DAG
edge or argument assembly changes. This audit supplies no lower
split count, nonempty Z, F, reconstruction, transport, algebraic cycle
or universal Hodge realization, and no progress beyond the checked
known tools is claimed.

## Mathlib

Full matching coverage of the real-Kähler polystable decomposition,
stable-Hom, K3 duality/RR and this conditional specialization is
**not checked**. Unknown availability is not evidence of absence.
The general results are cited above; only their necessary application
to the actual M and signed Euler bookkeeping are proved here.
No mathematical script, existence claim or originality claim is made.
