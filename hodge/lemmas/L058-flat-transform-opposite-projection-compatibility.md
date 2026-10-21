# L058 — Opposite projection of the flat six-charge exception

## Hypotheses

Retain L044's smooth projective complex K3 surface S, its exact real
Kahler class h, and its full mixed tensor tau_D on X=S x S. Write
eta for the integral point class, e_1=eta tensor 1, e_2=1 tensor eta,
and P=eta tensor eta. Suppose F is locally free holomorphic of rank
two, slope-polystable at p_1^*h+p_2^*h, with

\[
c_1(F)=0,\qquad ch_2(F)=-6e_1-13e_2+\tau_D.
\]

This is exactly (a,b)=(-10,-17) in L056--L057. Thus the actual
G=R^1p_2*F is O_S^2 and all other p_2 direct images vanish.
No existence of F, transform equivalence, reconstruction theorem,
or stability of an opposite transform is assumed.

## Conclusion

The actual opposite transform H=R^1p_1*F is locally free, commutes
with base change, and is slope-zero polystable at h, with

\[
R^ip_1*F=0\ (i\ne1),\quad
ch(H)=9-14\eta,\quad c_1(H)=0,\quad c_2(H)=14\eta.
\tag{1}
\]

Its cohomology dimensions are (h^0,h^1,h^2)(H)=(2,0,2).
Its polystable decomposition necessarily has the form

\[
H\simeq O_S^2\oplus K,\qquad
\operatorname{rank}K=7,\quad c_1(K)=0,\quad c_2(K)=14\eta,
\quad H^i(S,K)=0\text{ for every }i.
\tag{2}
\]

Every stable summand of K has rank at least two, slope zero, zero
cohomology, and second character -2 times its rank times eta.
The possible rank partitions are 7, 5+2, 4+3, and 3+2+2.
Individual summands need not have zero first Chern class.

These necessary character, cohomology and summand tests give no
contradiction: already the formal single stable rank-seven branch
has chi(K)=14-14=0, compatible with zero cohomology. This does
not construct K or F. In particular it neither proves nor refutes
flat-image rigidity, and it does not force tau_D=0. The bounded
two-projection/cohomology mechanism stops here. This informative
NEGATIVE is a REPRODUCTION of the covered tools, with no claim
of a new theorem beyond the sources checked or a Hodge resolution.

## Proof

**Every opposite fibre is stable and satisfies odd IT.** The pair
(-10,-17) meets L052's hypotheses: its sum is -27 and
(-6)(-13)=78 is 6 modulo 12. L052 supplies the compatible
hyperholomorphic connection on F and polystability on every factor
restriction by curvature pullback. For each x, F|_({x} x S) has
rank two, first Chern class zero and second Chern number thirteen.
A split zero-slope rank-two bundle at this exact h has charge
14r^2 by L052, so none of these fibres splits. They are all stable.
L052's stable-section, dual-stability, Serre-duality and surface-RR
argument gives H^0=H^2=0 and h^1=13-4=9 at every x.

Import the perfect base-change and single-degree local-freeness
statements, [Stacks Lemma 36.30.1, 0A1H](https://stacks.math.columbia.edu/tag/0A1H)
and [Lemma 36.31.3, 0BDH](https://stacks.math.columbia.edu/tag/0BDH).
The smooth projective p_1 and vector bundle F satisfy precisely the
properness, perfectness and flatness hypotheses checked in L056.
The derived fibre is concentrated in degree one with dimension nine
at every closed point; the open concentration locus is consequently
all S. Thus Rp_1*F=H[-1], with H locally free of rank nine and
base-changing, and p_1![F]=-[H]. This uses actual fibre cohomology,
not just a virtual rank.

Import Bartocci--Bruzzo--Hernandez Ruiperez, *A hyperkahler Fourier
transform*, Differential Geometry and its Applications 8 (1998),
239--249, [Definition 2, p. 244, Theorem 3, p. 246](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=6).
As in L056, use F with its actual unitary quaternionic-instanton
connection as the hermitian kernel and O_S with its flat connection
as the source. Interchanging the factors preserves the simultaneous
product metric and all compactness and connection hypotheses.
The new all-fibre even-degree vanishings verify odd IT. The theorem
therefore gives the actual holomorphic H a compatible quaternionic-
instanton connection. The zero-contraction and real-metric
Hermite--Einstein argument of L056 then gives slope-zero polystability
at h. It permits reducibility and arbitrary transform rank.

**Relative GRR retains the full character and sign.** L048 forces

\[
ch(F)=2-6e_1-13e_2+\tau_D+26P.
\tag{3}
\]

Here ch_1=ch_3=0, and ch_4=(((-6)(-13)+78)/6)P=26P;
the mixed square is the full 156P, including the transcendental
120P. Import the smooth relative GRR used in L057: Fulton,
*Intersection Theory*, second edition (1998), Theorem 15.2,
pp. 286--287 and Example 15.2.8, pp. 291--292; also
[Stacks 42.66, 02UO](https://stacks.math.columbia.edu/tag/02UO).
GAGA makes F algebraic, and p_1 is proper smooth between smooth
projective varieties. Its relative Todd class is 1+2e_2. Only terms
with top degree on the second factor survive its pushforward:

\[
ch(p_1![F])=p_{1*}(ch(F)(1+2e_2))
 =(4-13)+(26-12)\eta=-9+14\eta.
\]

The mixed tensor has zero direct pushforward and e_2 tau_D=0
by factor degrees; its square contribution in (3) remains essential.
Negation gives (1). There is no degree-two term. Torsion-free
H^2(S,Z) promotes c_1=0 from rational to integral cohomology;
the character identity ch_2=-c_2 then gives the stated charge.

**Leray gives exact global cohomology in both directions.** Import
[Stacks Lemma 20.13.4, 01F2](https://stacks.math.columbia.edu/tag/01F2).
Each projection is a morphism of ringed spaces and F[0] is bounded
below. Since each projection has only R^1 nonzero, its Leray
spectral sequence has a single row and no possible nonzero
differentials. It gives H^j(X,F)=H^{j-1}(S,G) for p_2 and
H^j(X,F)=H^{j-1}(S,H) for p_1, with groups outside degrees
0..2 on S interpreted as zero. A K3 has cohomology dimensions
(1,0,1) for O_S. Thus dimensions of H^j(X,F), j=0..4,
are (0,2,0,2,0), and those of H are (2,0,2).
The sign check is chi(X,F)=8+2(-6-13)+26=-4=-chi(S,H).

**Keep all stable summands.** Write H as a sum of h-slope-stable
bundles of slope zero, possible since H is locally free polystable.
For a stable summand E of rank greater than one, a nonzero section
would give a saturated rank-one subsheaf with effective determinant
and nonnegative h-degree, contradicting strict slope stability.
Thus h^0(E)=0; dual stability and K_S=O_S give h^2(E)=0.
For a line summand L of slope zero, a nonzero section has an
effective zero divisor. Every nonzero effective divisor has strictly
positive h-degree, so such a section forces L=O_S. Its dual has
the same property. Consequently h^0(H)=2 forces exactly two
trivial line summands, and the remaining K in (2) has h^0=h^2=0.
Additivity and h^1(H)=0 give zero cohomology for K and each of
its summands. Subtracting ch(O_S^2)=2 from (1) proves its full
character and Chern assertions.

There are no nontrivial line summands in K. Indeed L052 gives
c_1(L)=r k for a zero-slope line, with k=(-4,-2,1,2), k^2=-14.
For r nonzero, K3 line RR gives chi(L)=2-7r^2<0, whereas a
summand of K must be acyclic. For r=0, Pic^0(S)=0 makes L
trivial, already excluded from K. All remaining stable summands
therefore have rank at least two. For each such E, arbitrary-rank
surface RR gives 0=chi(E)=2 rank(E)+integral_S ch_2(E).
These are exactly the character assertions and rank partitions above.
No individual c_1(E)=0 is imposed: its zero-slope class may be a
multiple of k, with the multiples summing to zero. The RR, duality
and stability inputs are Huybrechts, *Lectures on K3 Surfaces*,
author-hosted draft, [Chapter 1, (2.5)--(2.6), Proposition 2.4,
pp. 11--13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11)
and [Chapter 9, Section 3.1, pp. 175--176](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175),
as inspected in the approved assessment and applied in L052.

Taking the formal rank-seven stable branch with c_1=0 and c_2=14
satisfies every derived character and cohomology equality in this
test: no negative cohomology dimension is required. This is solely
consistency of the tested necessary conditions, not a proof that a
stable acyclic K with those data exists. Additional geometric
structure on H, realization of F, and flat-image rigidity are not
decided by these equalities. They require a different test.

## Mathlib

Coverage of this full specialization, transform preservation and
summand conclusion: **not checked**. No matching theorem or absence
from checked Mathlib sources is asserted. The precise named primary
theorems above supply the general tools; the opposite-projection
substitution and summand comparison are their scoped reproduction.
No additional algebraic cycle, transverse surface or solution of the
universal rational Hodge conjecture is supplied.
