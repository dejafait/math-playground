# L074 — Sign-reversed six-charge direct-image character and surface filter

## Hypotheses

Retain L071's marked projective complex K3 surface S, its real Kähler
class h and the identical hyperkähler metric on both factors of
X=S x S. Put Omega=p_1^*h+p_2^*h, e_1=eta tensor 1,
e_2=1 tensor eta and P=e_1e_2, where integral_S eta=1.
Use the full integral mixed class tau_D of L071, including both
divisor and transcendental components; tau_D^2=156P.

Let b be any L071-admitted integer for a=-10:

\[
b\leq-9,\qquad -6(b+4)\equiv6\pmod{12}.                 \tag{1}
\]

Suppose F is a locally free rank-two holomorphic bundle on X,
slope-polystable at Omega, with

\[
c_1(F)=0,\qquad \operatorname{ch}_2(F)
 =-6e_1+(b+4)e_2-\tau_D.                               \tag{2}
\]

Initial higher characters and the initial K-class are unrestricted.
Use L073's actual G=R^1p_2*F, locally free of rank two and
slope-zero polystable at this same h, with p_2![F]=-[G].
L073's separate critical audit of 2026-10-08 preserves that input;
the character calculation itself does not strengthen preservation. No existence,
gluing, opposite-projection stability, equivalence or transport is assumed.

## Conclusion

The actual transform has cohomological character and integral first class

\[
\operatorname{ch}(G)=2-(b+17)\eta,\qquad
c_1(G)=0,\qquad \int_S c_2(G)=b+17.                     \tag{3}
\]

Exactly the following admitted integers pass this relative-GRR
character and the stable Euler or split-line tests at h:

\[
\boxed{b\in\{-9,-11,-13,-17\}.}                         \tag{4}
\]

The stable alternative admits b=-9,-11,-13, with charges 8,6,4
respectively. The split alternative admits only b=-17 and forces
G=O_S^2. Every other integer in (1) fails both alternatives and is
excluded as a realization of (2), subject to the retained L073 input.
The four values are necessary non-exclusions, not assertions of
stable G or product F existence, reconstruction or transport.

This is a NEGATIVE local filter, classified as REPRODUCTION under
the prior SPECIALIZE assessment. Its numerical answer agrees with
L057's different positive-sign input, but is derived here from L071
and L073 rather than imported from that input. No new general theorem,
originality, algebraic cycle or Hodge-conjecture resolution is claimed.

## Proof

**Actual transform and complete input character.** L073 applies to
precisely (1)--(2), before any GRR computation. It gives every-fibre
cohomology concentration, the actual locally free G, unchanged-h
polystability and Rpi_*F=G[-1] for pi=p_2. Consequently pi_![F]=-[G].
This negative alternating sign cannot be replaced by positive rank.

Put t=b+4. In L071, p=a+4=-6. Factor degrees give
e_1^2=e_2^2=e_i tau_D=0 and e_1e_2=P, so the full square is

\[
(-6e_1+t e_2-\tau_D)^2=(-12t+156)P.                    \tag{5}
\]

The mixed square includes 36P from divisors and 120P from the
transcendental component, as verified in L071. Reversing tau_D
changes neither contribution. L071's rank-two character identities,
importing [Stacks Section 42.45, Tag 02UM](https://stacks.math.columbia.edu/tag/02UM),
force ch_3(F)=0 and ch_4(F)=ch_2(F)^2/12. Thus

\[
\operatorname{ch}(F)=2-6e_1+t e_2-\tau_D+(13-t)P.        \tag{6}
\]

Higher terms are forced by actual rank two and c_1=0, rather than
chosen to imitate a former virtual K-class.

**Relative GRR specialization.** Import Fulton, *Intersection Theory*,
second edition (1998), Theorem 15.2, pp. 286--287, and Example 15.2.8,
pp. 291--292, in the [scan qualified by the saved assessment](https://djvu.online/file/87GFN2nbfbdF7).
GAGA algebraizes F; pi is a proper smooth projection of nonsingular
projective varieties. These meet the cited hypotheses. The smooth
relative formula after the rational cycle-class map is

\[
\operatorname{ch}(\pi_![F])
 =\pi_*\bigl(\operatorname{ch}(F)\operatorname{td}(T_{X/S})\bigr).
                                                               \tag{7}
\]

[Stacks Section 42.66, Tag 02UO](https://stacks.math.columbia.edu/tag/02UO)
also states this formula with finite locally free input and higher
direct images, supplied here by L073; its deferred-proof qualification
is retained and Fulton is the proof citation. No reproof of GRR is
needed. Its hypotheses impose no mixed-sign condition and do not
require rationality of the real metric h.

Here td(T_{X/S})=1+2e_1. The only terms in the product (6) that
have first-factor top degree are -6e_1+4e_1 and
(13-t)P+2tP. Indeed pi_*tau_D=0 because its first-factor degree
is two, and e_1 tau_D=0 by dimension. Also pi_*e_1=1 and
pi_*P=eta. It follows that

\[
\operatorname{ch}(\pi_![F])=-2+(13+t)\eta.              \tag{8}
\]

There is no first-character contribution: ch_1 and ch_3 of F
are zero, and multiplication by the degree-four relative Todd
term creates no degree-six term. Negating (8) gives (3) rationally,
using ch_2(G)=-c_2(G) once c_1(G)=0. Since H^2(S,Z) is
torsion-free, its rational vanishing implies integral c_1(G)=0.
Pic^0(S)=0 then also makes det(G) trivial. Precisely, Huybrechts,
*Lectures on K3 Surfaces*, author-hosted prepublication draft,
[Chapter 1, Section 3.2, equation (3.1), printed p. 15](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=15),
gives Pic(S) injecting into integral H^2 and proves its torsion-freeness
using Remark 2.5. These checks precede the surface alternatives;
slope zero alone would not give them.

**Complete exact-h surface filter.** L071's surface test applies to
any locally free rank-two polystable bundle at this same h with
integral c_1=0, irrespective of its origin as a factor restriction.
The general inputs are Huybrechts, *Lectures on K3 Surfaces*,
author-hosted draft, Chapter 1 equations (2.5)--(2.6) and
Proposition 2.4, [pp. 11--13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11),
and Chapter 9 Section 3.1, [pp. 175--176](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175),
for K3 RR, Serre duality and dual stability. The exact-h line
lattice is inherited through L071 from L052; no chamber change
or lattice reproof is required for this specialization.

If G is stable, those inputs give H^0(G)=H^2(G)=0 and
chi(G)=4-c_2(G)=-h^1(G). Hence c_2(G)>=4. By (3) this requires
b>=-13. Congruence (1) is equivalent to t odd, hence b odd.
The whole stable numerical domain is therefore exactly
b=-9,-11,-13. Its prescribed h^1 values are respectively 4,2,0;
the equality case c_2=4 remains admitted by this test.

If G is nonstable, polystability and rank two make it a sum of
two zero-slope lines. Integral c_1=0 and Pic^0(S)=0 identify it
as L direct sum L^{-1}. L071's exact lattice gives
c_1(L)=r(-4,-2,1,2) and c_2(G)=14r^2 for r in Z.
But (1) and (3) give c_2(G)=b+17<=8. Thus r=0, b=-17,
and L is trivial. This b is odd and satisfies (1); O_S^2 is
an actual split surface bundle, without implying any kernel F.
Negative charges and charge two satisfy neither alternative.
The two cases exhaust polystable rank two over the entire
infinite domain, proving (4) without finite sampling.

**Independent index check and scope of the stop.** L071's full
product HRR gives

\[
\chi(X,F)=8+2(-6+t)+(13-t)=9+t=b+13.
\]

Surface RR applied to (3) gives chi(S,G)=4-(b+17)=-b-13,
as required by Rpi_*F=G[-1]. The scalar index is integral
for every input b and supplies no replacement for the exhaustive
surface test. All signs and bounds are exact symbolic identities;
no mathematical script or numerical certificate is needed.

This directional character filter is exhausted. The separate
critical audit of 2026-10-08 below preserves this specialization
and L073's preservation input; the four non-excluded inputs need
a different construction or obstruction mechanism. Product F
existence, gluing, transverse transport and universal primitive
rational Hodge-class algebraicity remain unresolved. The positive
tensor's recorded curvature obstruction is not transferred to this
negative tensor by agreement of the square or character.

**Separate critical audit, 2026-10-08.** The character and complete
necessary filter survive without a substantive repair. This audit
is REPRODUCTION and EXPLORATION; it supplies no additional excluded
input and no existence conclusion.

The input to GRR is the full actual rank-two character. With t=b+4,
c_1=0 and c_3=c_4=0, the degree-eight term is c_2(F)^2/12,
not zero. L071's audited full mixed square is 156P, comprising
36P+120P, so ch_4(F)=(13-t)P. Terms e_i tau_D vanish by factor
degree, and sign reversal cannot change the mixed square. Multiplying
by the relative Todd class 1+2e_1 gives first-factor top-degree
terms -2e_1+(13+t)P. The mixed degree-(2,2) term itself cannot
push forward to a nonzero class, and no degree-six term is present.
Thus ch(pi_!F)=-2+(13+t)eta, and L073's negative alternating
class gives precisely ch(G)=2-(b+17)eta. Absolute HRR gives
chi(X,F)=b+13=-chi(S,G), independently checking this index sign.
No initial higher-character freedom survives the rank-two identities.

The vanishing first character is initially rational. The cited
integral H^2 torsion-freeness upgrades it to integral c_1(G)=0;
the exponential-sequence injection Pic(S) into H^2 then makes
det(G) trivial. This implication uses the K3 hypotheses, not slope
zero, a fractional determinant normalization, or a chosen trivialization.

The inherited exact-h lattice is unchanged by the mixed sign. L052's
three independent coefficients in lambda, 1 and 1/lambda force
(x,y,z,w)=r(-4,-2,1,2) with square -14r^2 in the actual integral
basis; L044 supplies the same h. Its use for G requires only the
surface and metric, not the old positive-sign product hypotheses.
Local freeness and polystability leave precisely a stable rank-two
bundle or a sum of two zero-slope line bundles. In the stable branch,
RR and vanishing give c_2(G)>=4. Congruence (1) says b is odd,
so -13<=b<=-9 gives exactly -13,-11,-9, including the equality
case. In the split branch c_2(G)=14r^2, while b<=-9 gives
c_2(G)<=8; hence r=0 and b=-17. Integral determinant triviality
identifies the two lines as inverses and r=0 makes each trivial.
For b<-17 the charge is negative; b=-15 has charge two. These
fail both branches. This proves exhaustion of the infinite domain
without treating a finite list of sampled b as evidence.

The statement concerns only these particular tests: compatible
charges four, six and eight do not establish stable G, and even
the actual surface bundle O_S^2 does not reconstruct F. No
positive-sign curvature obstruction or other unapproved necessary
condition is added by this audit. The universal Hodge gap is unchanged.

## Mathlib

Full matching coverage of this changed-sign filter, relative GRR
and real-metric surface inputs: **not checked**. Unknown coverage
is not evidence of absence. The precise Fulton, Stacks and
Huybrechts citations above supply the named general inputs;
L071 supplies the full signed character and exact-h alternatives,
and L073 supplies the actual polystable transform. This is a
known-tool specialization, not a theorem of kernel existence.
