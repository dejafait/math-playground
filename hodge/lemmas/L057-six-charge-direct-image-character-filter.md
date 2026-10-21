# L057 — Six-charge direct-image character and surface filter

## Hypotheses

Retain L044's smooth projective complex K3 surface S, exact real
Kahler class h, and full integral mixed tensor tau_D on X=S x S.
Use the product class Omega=p_1^*h+p_2^*h. Write eta for the
point class with integral_S eta=1, e_1=eta tensor 1,
e_2=1 tensor eta, and P=eta tensor eta.

Let b be an integer in the a=-10 L052 survivor slice:

\[
b\leq-9,\qquad -6(b+4)\equiv6\pmod{12}.                 \tag{1}
\]

Suppose F is rank-two locally free holomorphic and slope-polystable
at Omega, with c_1(F)=0 and

\[
\operatorname{ch}_2(F)=-6e_1+(b+4)e_2+\tau_D.            \tag{2}
\]

Higher characters and the initial K-class are unrestricted. Use
L056's actual rank-two locally free slope-zero polystable bundle
G=R^1 p_2*F at the same h; its stability is not assumed. No
stability of other-factor restrictions, equivalence, global existence
or transport is assumed. All character equalities are cohomological.

## Conclusion

The actual direct image necessarily has

\[
\operatorname{ch}(G)=2-(b+17)\eta,\qquad
c_1(G)=0,\qquad \int_S c_2(G)=b+17.                     \tag{3}
\]

Exactly the following integers in (1) pass relative GRR together
with L052's stated stable Euler and split-line tests on G:

\[
\boxed{b\in\{-9,-11,-13,-17\}.}                         \tag{4}
\]

For the stable alternative the values are -9,-11,-13, with second
Chern numbers 8,6,4 respectively; equality in the bound is retained.
The split alternative is only b=-17 and forces G to be O_S^2.
Hence all other integers in (1) are excluded as realizations of (2).
The word "pass" means only numerical non-exclusion by these tests;
it asserts neither existence of G in the stable cases nor existence
of any global F. Separate recorded obstructions are not undone.

This is an informative NEGATIVE, classified as REPRODUCTION of
the assessed GRR and surface tools. It adds a finite necessary
filter to the earlier infinite slice, without an originality claim,
new cycle, transverse surface or complete Hodge candidate.

## Proof

**Use the actual bundle before comparing its character.** L056's
hypotheses are exactly (1)–(2). It gives G locally free of rank two,
slope-zero polystable at h, all other higher direct images zero,
and p_2![F]=-[G]. In particular the negative alternating sign must
be retained. We use its complete all-fibre IT, base-change and
preservation argument as an established input; virtual rank alone
would not suffice. L044 fixes the metric and invariant mixed tensor.

**Force the complete character from rank two.** Put t=b+4 and
p=-6. The bound in (1) implies a+b=-10+b<=-19, so L048's
weaker sum hypothesis holds. L048 gives

\[
\operatorname{ch}(F)=2-6e_1+t e_2+\tau_D+(13-t)P,
\qquad \operatorname{ch}_1(F)=\operatorname{ch}_3(F)=0.   \tag{5}
\]

Its computation retains tau_D^2=156P, including 36 from divisors
and 120 from T. Indeed ch_2(F)^2=(-12t+156)P, and rank-two
truncation with c_1=0 forces ch_4=ch_2^2/12=(13-t)P.
The corrected higher characters are not inherited from an old
virtual class or selected as independent parameters.

**Import relative GRR with its actual hypotheses.** Use Fulton,
*Intersection Theory*, second edition (1998),
[Theorem 15.2, pp. 286–287, Example 15.2.8, pp. 291–292](https://djvu.online/file/87GFN2nbfbdF7).
The linked scan is the version qualified in the prior source
assessment. GAGA makes the holomorphic bundle F algebraic;
the projection pi=p_2 is proper smooth between nonsingular
projective varieties. Passing the smooth relative GRR identity
through the rational cycle-class map gives

\[
\operatorname{ch}(\pi_![F])
 =\pi_*\bigl(\operatorname{ch}(F)\operatorname{td}(T_{X/S})\bigr).
                                                               \tag{6}
\]

These hypotheses also meet the relative formulation in
[Stacks Section 42.66, Tag 02UO](https://stacks.math.columbia.edu/tag/02UO),
including local freeness of higher images from L056. The real h
is irrelevant to applying GRR. Import the theorem, without a
reproof; this coefficient substitution is the assessed specialization.

Here td(T_{X/S})=1+2e_1. Factor degrees give pi_*e_1=1,
pi_*P=eta, pi_*tau_D=0, and e_1 tau_D=e_1^2=0.
The terms pi_*1 and pi_*e_2 also vanish. Thus (5)–(6) yield

\[
\operatorname{ch}(\pi_![F])=-2+(13-t+2t)\eta
                          =-2+(t+13)\eta.              \tag{7}
\]

There is no first character: neither ch_3(F) nor ch_1(F)
contributes, and no degree-six term is produced by the relative
Todd factor. Negating (7) by L056 gives (3), using ch_2(G)=-c_2(G)
when c_1=0, the Chern-character identity in
[Stacks Section 42.45, Tag 02UM](https://stacks.math.columbia.edu/tag/02UM).
The mixed tensor contributes through its full square in (5).

**Apply both fixed-metric alternatives and solve the entire slice.**
The first character is zero in rational cohomology by (7), hence
also integrally since K3 second integral cohomology is torsion-free.
G is locally free rank two and polystable at the exact h by L056.
Thus L052's surface argument applies, without requiring G to be a
factor restriction. Its cited surface RR, dual stability and Serre
duality inputs are Huybrechts, *Lectures on K3 Surfaces*, author-hosted
draft, [Chapter 1 equations (2.5)–(2.6), Proposition 2.4,
pp. 11–13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11)
and [Chapter 9 Section 3.1, pp. 175–176](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175).
We reuse the proved surface test and exact lattice rather than
reprove the general results or recompute the chamber.

For stable G, L052 requires c_2(G)>=4 and gives h^1(G)=c_2(G)-4.
Equation (3) therefore requires b>=-13. Congruence (1) is equivalent
to t being odd: -6t is 6 modulo 12 exactly when t is odd. Since
t=b+4, the complete input set is all odd b<=-9. Intersecting with
b>=-13 gives exactly b=-9,-11,-13. Their required h^1 values
are respectively 4,2,0, so none fails this cohomological test.
In particular charge four is not discarded as a strict inequality.

If G is not stable, rank-two polystability makes it a sum of two
zero-slope line bundles. The zero determinant class, Pic^0(S)=0
and torsion-free Picard group give G=L direct sum L^{-1}.
L052's exact lattice is c_1(L)=r(-4,-2,1,2), r an integer, and
c_2(G)=14r^2. Since b<=-9 gives c_2(G)=b+17<=8, this equation
forces r=0. It then forces b=-17, which does satisfy (1).
For r=0, L is trivial by Pic^0(S)=0, so G=O_S^2. This actual
split surface bundle demonstrates non-exclusion by the surface
tests; it provides no kernel F. No negative charge or charge two
can meet either alternative. The two exhaustive polystable cases
prove (4) for the infinite input slice, without numerical sampling.

As an independent sign check, product HRR in L048 gives
chi(X,F)=8+2(-6+t)+(13-t)=9+t=b+13. Surface RR applied to (3)
gives chi(S,G)=4-(b+17)=-b-13, agreeing with pi_![F]=-[G].
The scalar index is integral for every input b and does not replace
the stable/split test. Exact symbolic identities and inequalities
suffice; no mathematical script or finite enumeration is needed.

The filter is now exhausted. The stable numerical survivors and
the flat split exception require other tests or constructions;
compatible global realization, transport and universal primitive
Hodge algebraicity remain independent gaps.

## Mathlib

Coverage of this complete filter and of the full relative-GRR and
surface-stability inputs: **not checked**. No matching declaration
or absence from checked sources is asserted. The precise Fulton,
Stacks and Huybrechts citations supply the general tools, L048
the forced full character, L052 the surface tests/lattice, and
L056 the actual locally free polystable direct image. This is a
REPRODUCTION under prior SPECIALIZE coverage, with a local
necessary-condition improvement and no certified originality claim.
