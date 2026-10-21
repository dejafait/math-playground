# L060 — Nonflat opposite projection forces a compatible stable rank-three image

## Hypotheses

Retain L044's smooth projective complex K3 surface S, its exact real
Kahler class h and common hyperkahler metric, and the full integral
mixed tensor tau_D on X=S x S. Write eta for the integral point
class with integral one, e_1=eta tensor 1, e_2=1 tensor eta and
P=eta tensor eta. Let Omega=p_1^*h+p_2^*h.

Suppose F is locally free holomorphic of rank two, slope-polystable
at Omega, with cohomological Chern data

\[
c_1(F)=0,\qquad ch_2(F)=-6e_1-7e_2+\tau_D.
\tag{1}
\]

This is the correction pair (a,b)=(-10,-11). Its initial higher
characters and K-class are unrestricted. No existence of F,
transform equivalence, inverse, faithfulness, pairing on a transform,
spin lift or transverse transport is assumed.

## Conclusion

The actual opposite direct image H=R^1p_1*F is locally free of rank
three, commutes with base change, and is slope-stable of slope zero
at h. Necessarily

\[
R^ip_1*F=0\ (i\ne1),\quad Rp_1*F\simeq H[-1],\quad
ch(H)=3-8\eta,\quad c_1(H)=0,\quad c_2(H)=8\eta.
\tag{2}
\]

Its cohomology dimensions are (0,2,0). The first-direction image
G=R^1p_2*F is stable rank two with c_1=0,c_2=6eta and the same
cohomology dimensions. Global cohomology of F in degrees 0 through
4 has dimensions (0,0,2,0,0).

These character, cohomology and polystable-summand tests produce no
contradiction: the forced stable rank-three branch has chi(H)=-2
and requires the nonnegative middle dimension two. This is consistency
of precisely these necessary tests, not existence of H or F or
sufficiency of the tested conditions. Stop the bounded two-projection
mechanism for this pair. The result is an informative NEGATIVE and
REPRODUCTION under the prior SPECIALIZE assessment, without a claim
of originality, an additional cycle or a complete Hodge candidate.

## Proof

**First-direction data and the actual kernel.** The correction sum
is -21 and (-6)(-7)=42 is 6 modulo 12. Thus L052 applies to F,
and supplies its compatible hyperholomorphic connection and the
polystability of every factor restriction at the same h. This
coefficient-independent argument retains the full invariant mixed
tensor; it excludes product line splitting, makes F stable and
applies the cited hyperholomorphic criterion to its actual holomorphic
structure. It is not a deduction from topological bundle existence.
L056 and L057 apply to b=-11 and give the actual locally free
polystable G=R^1p_2*F, ch(G)=2-6eta, and no other higher images.
Its integral first Chern class is zero. The exact line lattice of
L052 makes a split rank-two image have charge 14r^2. Since six
is not such a charge, G is stable. L052's stable surface RR,
section vanishing, dual stability and Serre duality give

\[
(h^0,h^1,h^2)(G)=(0,2,0).
\tag{3}
\]

**Check opposite IT at every point before invoking preservation.**
For every x in S, L052 gives a locally free slope-polystable
rank-two E_x=F|_({x} x S), with c_1=0 and second Chern number
seven. Seven is not 14r^2, so each E_x is stable. The same
surface test gives h^0(E_x)=h^2(E_x)=0 and
chi(E_x)=4-7=-3, hence h^1(E_x)=3. This establishes odd IT
on every fibre, rather than merely a generic index.

Import [Stacks Lemma 36.30.1, 0A1H](https://stacks.math.columbia.edu/tag/0A1H)
and [Lemma 36.31.3, 0BDH](https://stacks.math.columbia.edu/tag/0BDH)
as in L056. GAGA makes F algebraic; p_1 is smooth projective,
F is perfect and flat over the target and has proper support.
Thus Rp_1*F is perfect and base-changing. Its derived fibre is
concentrated in degree one with dimension three at every closed
point. The open locus of rank-three concentration therefore contains
every closed point and is all S. This gives an actual locally free,
base-changing H, the vanishing in (2), and p_1![F]=-[H].

Import Bartocci, Bruzzo and Hernandez Ruiperez, *A hyperkahler
Fourier transform*, Differential Geometry and its Applications
**8** (1998), 239--249,
[Definition 2, p. 244, Theorem 3, p. 246, with Lemmas 1--2,
pp. 243--246](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=6).
Its hypotheses are the compact hyperkahler factors, an actual
hermitian quaternionic-instanton kernel, a quaternionic-instanton
source and IT. Interchanging the identical fixed-metric factors
preserves these hypotheses. Use F with its L052 connection as kernel
and the flat O_S as source. The preceding even-degree vanishings
verify IT. The theorem identifies the compatible connection with
the actual holomorphic higher image H; no equivalence or universal
kernel is required. It permits arbitrary rank and reducibility.
The invariant-curvature zero-contraction and real-metric
Hermite--Einstein argument of L056 gives slope-zero polystability
of H at exactly h. Stability will be proved below, not inferred
from preservation.

**Evaluate the full signed relative character.** L048 forces

\[
ch(F)=2-6e_1-7e_2+\tau_D+20P,\qquad ch_1=ch_3=0.
\tag{4}
\]

Indeed tau_D^2=156P, including 120P from the transcendental part;
ch_2(F)^2=(84+156)P=240P. Rank-two truncation gives ch_4=20P.
The former flat branch's value 26P is not used.

Import smooth relative GRR: Fulton, *Intersection Theory*, second
edition (1998), Theorem 15.2, pp. 286--287, Example 15.2.8,
pp. 291--292; also
[Stacks Section 42.66, 02UO](https://stacks.math.columbia.edu/tag/02UO).
Here p_1 is proper smooth between nonsingular projective varieties,
F is algebraic by GAGA, and its higher images are locally free
by the preceding all-fibre argument. The relative Todd class is
1+2e_2. Factor degrees give p_1*e_2=1, p_1*P=eta,
p_1*tau_D=0 and e_2 tau_D=0. The remaining terms integrate to

\[
ch(p_1![F])=p_{1*}(ch(F)(1+2e_2))
 =(4-7)+(20-12)\eta=-3+8\eta.
\tag{5}
\]

The alternating class is -[H]; negating (5) gives ch(H)=3-8eta.
No degree-two term survives. Torsion-free H^2(S,Z) promotes c_1=0
to integral cohomology. Then ch_2=-c_2 gives the charge in (2).
The general GRR theorem is imported without reproof; this changed
coefficient/projection application is the approved specialization.

**Use both single-row Leray sequences.** Import
[Stacks Lemma 20.13.4, 01F2](https://stacks.math.columbia.edu/tag/01F2).
Each projection is a morphism of ringed spaces and F[0] is bounded
below. In each direction only R^1 is nonzero, so the Leray spectral
sequence has no possible nonzero differential. It gives
H^j(X,F)=H^{j-1}(S,G) and H^j(X,F)=H^{j-1}(S,H), with groups
outside surface degrees 0..2 interpreted as zero. Equation (3)
therefore proves the stated global dimensions and

\[
(h^0,h^1,h^2)(H)=(0,2,0).
\tag{6}
\]

The independent index check is chi(X,F)=8+2(-6-7)+20=2,
while surface RR gives chi(H)=2(3)-8=-2, as required by
p_1![F]=-[H].

**Exclude every reducible polystable alternative.** Decompose H
into h-slope-stable locally free summands of slope zero. Do not
assign c_1=0 to each summand. A line summand L has c_1(L)=rk
for an integer r, by L052's exact lattice, where
k=(-4,-2,1,2) and k^2=-14. If r=0, Pic^0(S)=0 and injectivity
of the Picard Chern class make L=O_S, contradicting h^0(H)=0.
For r nonzero, neither L nor L^{-1} has a nonzero section:
a nonzero effective divisor has strictly positive h-degree,
whereas both classes have zero h-degree. Serre duality gives
h^2(L)=0 as well. Line RR yields

\[
\chi(L)=2+\tfrac12(rk)^2=2-7r^2,\qquad
h^1(L)=7r^2-2\geq5.
\tag{7}
\]

Additivity of cohomology for a direct sum contradicts h^1(H)=2
if such an L occurs. Thus H has no line summand. Every partition
of rank three into at least two positive ranks has a rank-one
part; all reducible alternatives are excluded. H is stable.

The RR, Serre-duality and stability inputs used here are Huybrechts,
*Lectures on K3 Surfaces*, author-hosted prepublication draft,
[Chapter 1, (2.5)--(2.6), Proposition 2.4, pp. 11--13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11)
and [Chapter 9, Section 3.1, pp. 175--176, Theorem 4.9,
p. 182](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175).
Their general statements are imported; L052 supplies the actual
irrational-metric line lattice. No rank-two charge bound is imposed
on H or on an arbitrary-rank summand.

The surviving formal stable rank-three character has c_1=0,c_2=8,
chi=-2 and required cohomology (0,2,0), so no dimension is negative.
This reaches the specified stopping test. It supplies no stable
holomorphic realization, symmetric form or reconstruction theorem.
Global F and transverse transport, other representatives, and the
universal primitive Hodge-class gap remain unresolved. Exact symbolic
identities and exhaustive rank partitions suffice; no numerical
sampling or mathematical script is needed.

## Mathlib

Coverage of the full specialization, preservation theorem and
stable-image conclusion: **not checked**. No matching declaration
or absence from checked sources is asserted. The precise primary
citations above supply the general tools; the evaluated character,
cohomology and summand comparison are a scoped REPRODUCTION.
No additional algebraic class, transverse surface or solution of
the rational Hodge conjecture is supplied.
