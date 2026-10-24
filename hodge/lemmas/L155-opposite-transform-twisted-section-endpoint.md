# L155 — Opposite transform excludes the twisted sixteen-section endpoint

## Hypotheses

Retain L147's identical marked projective complex K3 factors S_1 and
B=S_2, original common hyperkähler metric g, real Kähler class h and
fixed full integral tensor tau_D. Write e_1=eta tensor 1, e_2=1 tensor
eta, P=e_1e_2, with integral_S eta=1. Suppose F is locally free of rank
two, slope-polystable for Omega=p_1^*h+p_2^*h, with integral c_1(F)=0
and ch_2(F)=-14e_1-21e_2-tau_D. Let L on S_1 have class
k=(-4,-2,1,2), k.h=0 and k^2=-14 eta. Put

\[
 T=F\otimes p_1^*L^{-1},\qquad
 M=R^1p_{2*}T,\qquad W=R^2p_{2*}T,
 \qquad H=R^1p_{1*}F.
\]

Here H is the **untwisted opposite** image on S_1, distinct from both
the twisted coefficient T and the untwisted forward image. Use L093's
audited conclusions for this F at (m,n)=(14,21), L147's whole-base
twisted images, and L154's audited conditional endpoint classification
with its preferred dual HE twist. Z is the finite, possibly empty,
split-parameter set and z=|Z|. No F or member of Z is known to exist.

## Conclusion

There are actual natural degree-one comparison isomorphisms

\[
 H^0(B,M)\simeq H^1(S_1\times B,T)
       \simeq H^0(S_1,H\otimes L^{-1})
       =\operatorname{Hom}(L,H).                       \tag{1}
\]

The opposite image has full cohomological character

\[
                 \operatorname{ch}(H)=17-34\eta,       \tag{2}
\]

integral c_1(H)=0, and is acyclic and h-polystable with a perfect
symmetric form. If a and b are its full stable-type multiplicities of
L and L^{-1}, respectively, that form forces a=b. Rank alone gives
a<=8; actual acyclicity sharpens this to a=b=0. Consequently

\[
                         \boxed{h^0(B,M)=0.}           \tag{3}
\]

L154's z=147 endpoint requires h^0(B,M)=16 and is therefore impossible.
Combining this exclusion with its integer bound gives the necessary
restriction 0<=z<=146. This is a scoped endpoint consequence, not an
optimization of all remaining split counts.

This is a local ADVANCE / REPRODUCTION of assessed general tools; no
progress beyond the inspected sources or originality is claimed. The
separate critical audit below preserves this result. It neither excludes all smaller
counts nor supplies F, nonempty Z, an independent lower count, a cycle,
transverse transport or universal primitive rational Hodge realization.

## Proof

**Imported comparison and applicability.** Use the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-24-opposite-transform-twisted-section-endpoint.md`.
Pareschi–Popa, *GV-sheaves, Fourier-Mukai transform, and generic
vanishing*, American Journal of Mathematics 133 (2011), 235–271,
[author-hosted version, Section 2, Lemma 2.1 and proof, printed p. 5](https://people.math.harvard.edu/~mpopa/papers/GV.pdf#page=5),
gives the arbitrary-perfect-kernel two-projection hypercohomology
comparison. Both factors here are smooth projective over C, F is a
vector bundle and hence perfect, and the inputs L^{-1} and O_B are
bounded coherent and perfect. This is a projection-formula comparison;
neither transform is required to be an equivalence.

For its concrete ordinary-cohomology specialization import the derived
projection formula for a finite locally free base input,
[Stacks Section 20.54, Lemmas 20.54.2–3](https://stacks.math.columbia.edu/tag/01E6),
and composition of derived global sections and the higher-image
spectral sequence,
[Section 20.13, Lemmas 20.13.1 and 20.13.4](https://stacks.math.columbia.edu/tag/01EY).
The coefficient T in degree zero is bounded below, and the projections
are proper. Only the following degree-one edge calculation is needed;
the general theorems are not reproved.

**The twisted edge retains W.** L147 gives

\[
 R^0p_{2*}T=0,\quad R^1p_{2*}T=M,\quad
 R^2p_{2*}T=W=\bigoplus_{x\in Z}\mathbb C_x,
\]

and no higher images. In the first-quadrant Leray spectral sequence
E_2^{p,q}=H^p(B,R^qp_{2*}T), the only possibly nonzero term of total
degree one is E_2^{0,1}=H^0(B,M). For every r>=2 an incoming
d_r would have negative first index. The outgoing d_2 lands in
E_2^{2,0}=0, while every outgoing d_r with r>=3 has negative second
index. Thus E_infinity^{0,1}=E_2^{0,1}; the other graded piece of
H^1 is zero. The natural edge is an isomorphism. W is retained in
degree two: it can have a differential from E_2^{0,2} to E_2^{2,1},
but neither position changes this total-degree-one calculation.
No degeneration in all degrees or whole-base twisted IT is asserted.

**The opposite edge and the same class.** The charges correspond to
a=-18,b=-25 in L071, so both are at most -9 and
(a+4)(b+4)=294=6 modulo 12. One factor charge is 14, so L093 applies
in its split-charge domain. Its actual opposite concentration is
Rp_{1*}F=H[-1], with H locally free of rank 21-4=17. Since L^{-1}
is pulled back from the base of p_1, the projection formula gives

\[
                  Rp_{1*}T=(H\otimes L^{-1})[-1].
\]

Derived global sections now identify H^1(X,T) with
H^0(S_1,H tensor L^{-1}). Combining this identification with the
preceding natural edge proves (1). Both maps come from the same
coefficient T and the actual projections. They compare vector spaces
without an inverse-transform assertion or any choice of image blocks.

**Full opposite signed GRR.** L071's rank-two character, also checked
in L147, is

\[
 \operatorname{ch}(F)=2-14e_1-21e_2-\tau_D+62P,
 \qquad \tau_D^2=156P,\qquad \operatorname{ch}_3(F)=0.
\]

Indeed ch_4(F)=(14\cdot21+78)P/6=62P retains the full mixed square.
Import Fulton, *Intersection Theory*, second edition, Theorem 15.2,
pp. 286–287, and Example 15.2.8, pp. 291–292. For the smooth proper
projection p_1 its relative Todd factor is 1+2e_2. The fibre-degree-four
terms in

\[
 p_{1*}\big[(2-14e_1-21e_2-\tau_D+62P)(1+2e_2)\big]
\]

are -21e_2+4e_2 for rank, and 62P-28P for base degree four.
The mixed tensor has second-factor degree two, so its untwisted
pushforward is zero, and multiplying it by e_2 exceeds the fibre
dimension. There is no degree-six character to produce a base
degree-two contribution. Therefore

\[
 \operatorname{ch}(Rp_{1*}F)=-17+34\eta
                      =-\operatorname{ch}(H),
\]

proving (2) with the negative R^1 sign. Torsion-free H^2(S_1,Z)
upgrades c_1(H)=0 to integral equality; c_2(H)=34 eta. Surface RR
gives chi(H)=2\cdot17-34=0, consistently with L093. Specifically,
L093's actual image cohomology is (0,chi(X,F),0), and here

\[
             \chi(X,F)=((14-12)(21-12)-18)/6=0.
\]

Hence H is acyclic, a conclusion about every actual hypothetical
image, not an inference from a zero index alone. L093 also supplies
its same-h polystability and perfect symmetric coefficient-Serre
form, permitting reducibility. No such form is transferred to M.

**Full paired line multiplicities.** Import the same-slope stable-Hom
criterion and dual stability from Huybrechts, *Lectures on K3 Surfaces*,
[author draft, Chapter 9, Section 3.1(iii)–(iv), pp. 175–176](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175),
and the polystable decomposition from
[Theorem 4.9, p. 182](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182).
Their real-Kähler scope is also covered by Perego, *Kobayashi–Hitchin
corrispondence for twisted vector bundles*, Complex Manifolds 8 (2021),
Propositions 3.9–3.12 and 3.15, pp. 36–38, in the ordinary-bundle
case with trivial cocycle and zero B-field. L093 has already verified
applicability at exactly h; no new preservation theorem is invoked.

L and L^{-1} are stable slope-zero lines. They are distinct: otherwise
2k=0 in the torsion-free integral H^2, contrary to k^2=-14 eta.
Decompose the entire polystable H into its full isotypic pieces

\[
 H=L^{\oplus a}\oplus(L^{-1})^{\oplus b}\oplus R,       \tag{4}
\]

where R has neither line type. Stable-Hom vanishing implies
Hom(L,H)=C^a. It also kills both same-line blocks and the blocks
between either displayed type and R in the symmetric form H->H^vee.
For example the same-line block is Hom(L,L^{-1})=0, and a nonzero
block with R would require a stable summand isomorphic to L or
L^{-1}. Thus the form pairs the two full line isotypic pieces
perfectly, forcing a=b, with no restriction to selected sections.
Their total rank is 2a<=17, so a<=8 already suffices to contradict
sixteen. Their combined character is 2a-14a eta; the residual has
character (17-2a)+(-34+14a)eta, retaining the complete (2).

For the stronger actual bound, a nonzero section of either L or its
inverse would give an effective divisor of h-degree zero. Positivity
of h on every nonzero effective divisor and nontriviality of the line
exclude such a section. Serre duality gives H^2(L)=H^2(L^{-1})=0.
Import surface RR and Serre duality from Huybrechts,
[Chapter 1, (2.5)–(2.6), Proposition 2.4, pp. 11–13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11).
For either sign,

\[
 \chi(L^{\pm1})=2+k^2/2=-5,
 \qquad h^1(L^{\pm1})=5.                              \tag{5}
\]

Since (4) is a direct sum of actual bundles, its cohomology is a
direct sum. The already established H^1(H)=0 therefore gives
0=5a+5b+h^1(R), so a=b=0. This uses acyclicity, not merely
chi(H)=0 or a sign bound on chi(R). Equation (1) proves (3).

**Endpoint verdict and limits.** L154's conditional z=147
classification is M=O_B^{16} direct sum E^{4}, with E stable of
rank two, slope zero and character 2-k-5eta. Stable-Hom vanishing
gives h^0(E)=0, so that endpoint has h^0(M)=16. This contradicts
(3). The actual bound zero is strictly below the required sixteen;
even the independent paired-rank bound eight would suffice. The
integer combination with L154's z<=147 yields z<=146.

The selected same-kernel endpoint filter succeeds and is complete
for this turn. This does not invalidate ATTEMPTS/087's formal
single-image compatibility: it supplies the additional independent
section comparison that its numerical constraints lacked. The old
whole-base twisted IT failure is retained, and W was never deleted.
No lifted kernel projector, equivalence, existence theorem or twisted
self-duality is used. Smaller counts and independent lower control
are not settled by the scoped endpoint verdict. The separate critical
audit below verifies this comparison for downstream use in its stated scope.

**Separate critical audit, 2026-10-24 (step 505).** Use the unchanged
invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-24-opposite-twisted-section-critical-audit.md`.
The outcome is EXPLORATION / REPRODUCTION: the proof survives without
a substantive repair or stronger conclusion. Reuse the primary
statements and proof cases at the locators above, in particular Stacks
20.13.4 ([01F2](https://stacks.math.columbia.edu/tag/01F2)) and
20.54.2–3, rather than reprove their general results.

First match the actual objects. The admitted parameters are
(a,b)=(-18,-25); their shifted product is 294, congruent to 6 modulo
12. The charge 14 is a split charge, while all charges are at least
five, so the audited L093 applies, including its cohomology statement.
L147 uses precisely T=F tensor p_1^*L^{-1}, the same fixed numerical
chamber and finite set Z. Its vanishing R^0 is an ordinary sheaf
statement even though its derived fibres at Z have nonzero degree
zero. The audit uses that sheaf statement, not false ordinary base
change at a split point. Empty Z also meets every hypothesis.

For p_2, the first-quadrant E_2 page in total degree one consists of
(0,1) and the zero (1,0) term. The latter remains zero on later pages.
No differential enters (0,1); the only outgoing differential with
nonnegative target indices is d_2 to (2,0), whose target is zero.
The filtration therefore has exactly one nonzero graded piece and
its edge is a natural isomorphism, not a choice of splitting. The
term H^0(W) sits at (0,2); its possible d_2 to (2,1) changes neither
of these assertions. For p_1, L093 gives the actual H[-1], and the
finite locally free base input L^{-1} satisfies the projection
formula with no higher tensor terms. Taking derived sections yields
H^1(X,T)=H^0(S_1,H tensor L^{-1}), with the displayed shift in the
correct direction. The two identifications use the same coefficient
and global cohomology group. No multiplicative comparison, inverse
transform or self-duality of the twisted coefficient is required.

Independently recompute the character before applying any line test.
The full square of ch_2(F) is (2*14*21+156)P=744P, and actual rank
two forces ch_4(F)=744P/12=62P and ch_3(F)=0. The relative Todd
factor for p_1 is 1+2e_2, not the first-factor Todd class. Its rank
terms give 4-21=-17, and its base point terms give 62-28=34.
No mixed or degree-six term contributes a base first class. The
alternating class is -[H], so ch(H)=17-34eta; torsion-free integral
H^2 justifies integral c_1=0. Absolute HRR provides an independent
sign check: chi(X,F)=8-28-42+62=0, whereas chi(H)=34-34=0 and
chi(X,F)=-chi(H). Crucially this index check alone proves no vanishing.
The needed vanishing is L093's actual cohomology (0,chi(X,F),0),
proved there from its determinant-cup argument and both actual
concentrations. Thus all three cohomology groups of H are zero.

At the unchanged real h, L093's polystability decomposes H into
actual locally free stable summands. Duality preserves stable types
and their slope zero. Since k is nonzero in torsion-free H^2, the
types L and L^{-1} are distinct. Let their full multiplicities be
a,b. Stable-Hom vanishing removes every form block except the
cross-pairing between these two types and the block on R: the dual
of any other type is again different from these two lines. Thus a
perfect form yields an invertible pairing of their multiplicity
spaces, forcing a=b without a multiplicity-one assumption. Their
rank is 2a, so rank 17 bounds a by eight. Their combined character
is 2a-14a eta, consistent with the residual character in the proof;
no residual existence or Euler-sign assumption enters this bound.

For the stronger vanishing, an effective nonzero Cartier divisor
has positive degree against the real Kähler class h. A nonzero
section of L or L^{-1} either has such a divisor or trivializes its
line; both alternatives are impossible. A section cannot instead
have only isolated zeros on this smooth integral surface. Serre
duality removes degree two, and RR gives chi=2-7=-5, hence h^1=5
for each line. Direct-sum cohomology of the actual decomposition
now gives 0=5a+5b+h^1(R), so both multiplicities vanish. Stable-Hom
identifies Hom(L,H) with the full multiplicity space, proving
h^0(B,M)=0. This last argument does not require transferring H's
form to M.

Finally L154's audited endpoint is the same M, with its preferred
dual HE metric and same-h polystability. At z=147 its rank-two stable
type E is not O, so stable-Hom gives H^0(E)=0. All sixteen trivial
summands contribute, giving h^0(M)=16. Thus zero is strictly below
the required sixteen, and the integer bound remains z<=146.
ATTEMPTS/087's single-image compatibility and the whole-base twisted
IT failure are preserved. Direct inputs remain L071, L093, L147
and L154; the dependency graph and argument assembly do not change.
No smaller-count optimization, independent lower bound, existence
of F or a split point, transport or new Hodge realization is obtained.

## Mathlib

Full matching coverage of this conditional endpoint comparison and
its supporting geometric transform results is **not checked**. The
precisely cited general theorems are imported; the degree-one edge,
signed opposite character and stable-line multiplicity specializations
are the local proof. Unknown Mathlib coverage is not evidence of
absence. No mathematical script or numerical preview is used.
