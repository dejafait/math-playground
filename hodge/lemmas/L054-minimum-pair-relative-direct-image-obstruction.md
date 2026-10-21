# L054 — Relative direct image excludes the minimum correction pair

## Hypotheses

Let S, h and the full integral mixed tensor tau_D be exactly those
of L044 and L052. Thus S is the specified smooth projective complex
K3 surface, h its real Kahler class, and on X=S x S the product
polarization is Omega=p_1^*h+p_2^*h. Write eta for the integral
point class on S with integral one, e_1=eta tensor 1,
e_2=1 tensor eta, and P=eta tensor eta. The operator associated
with tau_D is 2A_c+4pi_K on NS(S)_Q and 2U on T(S), with the
common-metric invariance verified in L052.

Suppose F is holomorphic locally free of rank two, slope-polystable
at Omega, with the cohomological data

\[
c_1(F)=0,\qquad
\operatorname{ch}_2(F)=-5e_1-6e_2+\tau_D.                 \tag{1}
\]

These are precisely L048's corrections (a,b)=(-9,-10). Higher
characters and the K-class are initially unrestricted. No
Fourier--Mukai equivalence, presentation or transverse deformation
is assumed.

## Conclusion

No such F exists. More specifically, with pi=p_2, the hypothetical
bundle would give a line bundle G=R^1 pi_*F satisfying

\[
\operatorname{ch}(G)=1-6\eta,\qquad c_1(G)=0,              \tag{2}
\]

contradicting the character identity for a line bundle.

This is an informative fixed-pair NEGATIVE, classified as
REPRODUCTION of the assessed base-change, relative GRR and Chern
tools. It does not exclude other correction pairs, holomorphic
bundles without the polystability hypothesis, or L053's individual
stable factors. L050's topological realization is preserved.
No new algebraic Hodge class or transverse surface is supplied.

## Proof

**All-fibre cohomology.** The pair in (1) lies in L052's hypotheses:
a+b=-19<=-13 and (a+4)(b+4)=30 is 6 modulo 12. Its
coefficient-independent hyperholomorphic restriction argument
therefore applies to every embedding j_y:S -> X, z -> (z,y).
Each E_y=j_y^*F is a locally free rank-two slope-polystable
bundle at h, with c_1(E_y)=0 and second Chern number five.
L052's exact zero-slope line lattice makes the second Chern
number of a split polystable factor equal to 14r^2 for an
integer r. Since five is not of this form, every E_y is stable.
This is an all-fibre assertion, not an ordinary generic stable
restriction theorem.

Apply L052's equation (4), including its section, dual-stability
and Serre-duality argument:

\[
H^0(S,E_y)=H^2(S,E_y)=0,\qquad
\chi(S,E_y)=4-5=-1,\qquad h^1(S,E_y)=1.                  \tag{3}
\]

Surface cohomology above degree two vanishes. Thus every closed
fibre has cohomology in exactly degree one, with dimension one.
Individual existence in L053 is not a premise of (3) and is not
turned into existence of the hypothesized product bundle.

**Actual locally free direct image.** Serre's GAGA theorem makes
F an algebraic vector bundle on the projective complex X; its
restrictions and cohomology agree with the analytic ones. The
morphism pi is smooth projective of finite presentation, and F
is coherent and flat over S with proper support. Import
[Stacks Lemma 36.30.1, Tag 0A1H](https://stacks.math.columbia.edu/tag/0A1H),
using its perfect input O_X and its bounded flat coherent input
F[0]. It gives a perfect complex K=Rpi_*F on S and arbitrary
derived base change. In particular, its derived fibre at each
closed y is R Gamma(S,E_y), so (3) identifies that fibre as a
one-dimensional vector space placed in degree one.

Import [Stacks Lemma 36.31.3, Tag 0BDH](https://stacks.math.columbia.edu/tag/0BDH)
with i=1,r=1. The open locus where K is a rank-one locally free
module placed in degree one contains every closed point by
(3) and derived base change. Its closed complement must be
empty: any nonempty closed subset of the finite-type complex
variety S contains a closed point. Hence

\[
K\simeq G[-1],\qquad G=R^1\pi_*F\ \text{locally free of rank one},
\qquad R^i\pi_*F=0\ (i\ne1).                              \tag{4}
\]

These statements also retain derived base change. In particular,
the alternating coherent pushforward is pi_![F]=-[G].
Perfectness or a virtual rank of one alone would not imply (4);
the concentration at every fibre is essential.

**Full forced character and relative GRR.** L048 applies to the
actual rank-two F with c_1=0, independently of its initial
higher-character choices. At p=4+a=-5 and t=4+b=-6 it gives

\[
\operatorname{ch}(F)=2-5e_1-6e_2+\tau_D+18P.              \tag{5}
\]

In particular ch_1=ch_3=0. To retain the load-bearing full mixed
square, L048 gives tau_D^2=156P, with 36 from the divisor part
and 120 from T. The pure/mixed cross products vanish by factor
degree, and the pure square is 2(-5)(-6)P=60P. Thus
ch_2(F)^2=216P and rank-two truncation gives ch_4(F)=216P/12=18P.
Discarding the transcendental contribution would change this
coefficient and invalidate the test.

Import Fulton, *Intersection Theory*, second edition (1998),
[Theorem 15.2, pp. 286–287, and Example 15.2.8, pp. 291–292](https://djvu.online/file/87GFN2nbfbdF7).
Its proper nonsingular quasi-projective setting covers pi:X -> S.
The smooth relative formula, passed through the rational cycle-class
map, is

\[
\operatorname{ch}(\pi_![F])
 =\pi_*\bigl(\operatorname{ch}(F)\operatorname{td}(T_{X/S})\bigr).
                                                               \tag{6}
\]

No general theorem is reproved. The evaluated application is needed
because the inspected results do not themselves decide (1).
Here T_{X/S}=p_1^*T_S, and the K3 Todd class gives
td(T_{X/S})=1+2e_1. Only terms with degree four on the first
surface survive pi_*. We have pi_*e_1=1, pi_*P=eta,
pi_*1=pi_*e_2=0 and pi_*tau_D=0. Also e_1^2=0 and
e_1 tau_D=0, since these products exceed the first factor's
top degree. Therefore:

- The rank component in (6) is 4-5=-1.
- The degree-two component is zero: ch_3(F)=0, and the other
  candidate term ch_1(F) times 2e_1 is also zero.
- The degree-four component is (18-12)eta=6eta, where -12P
  is the term (-6e_2)(2e_1).

Consequently

\[
\operatorname{ch}(\pi_![F])=-1+6\eta,\qquad
\operatorname{ch}(G)=1-6\eta                            \tag{7}
\]

by the negative sign in (4). As a consistency check rather than
another obstruction, HRR on S gives chi(G)=2-6=-4, so
chi(X,F)=-chi(G)=4, agreeing with L048's
8+2(-5-6)+18=4. Thus the contradiction is stronger than the
already-passed scalar index test.

**Compare with finite rank.** For an actual line bundle G,
ch(G)=exp(c_1(G)). This is the standard character identity in
[Stacks Section 42.45, Tag 02UM](https://stacks.math.columbia.edu/tag/02UM),
already inspected for L048. Equation (7) makes c_1(G)=0 in
H^2(S,Q). Hence ch_2(G)=c_1(G)^2/2=0 in H^4(S,Q).
But (7) makes this character -6eta, which is nonzero since
integral_S eta=1. This contradiction proves the conclusion.
It needs neither integral triviality of G nor its stability.

The cohomological data and metric of (1) are fixed throughout.
The test stops with this exclusion; it does not evaluate a
variable-coefficient family or its reversed pair. Global bundle
construction at other corrections, transverse transport, and
algebraicity of arbitrary primitive rational Hodge classes remain
unresolved.

## Mathlib

Coverage of the full fixed-pair obstruction and of its coherent
base-change and relative-GRR inputs: **not checked**. No matching
declaration or absence from checked Mathlib sources is asserted.
The precisely linked Stacks and Fulton results are supporting
theorems; L048 supplies forced characters and the full mixed
square, and L052 supplies all-fibre stability and cohomology at
the exact real metric. The local evaluated contradiction is a
REPRODUCTION under the prior SPECIALIZE assessment, with no
originality or Hodge resolution claim.
