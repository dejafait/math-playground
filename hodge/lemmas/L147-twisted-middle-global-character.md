# L147 — Global character of the ordinary twisted middle image

## Hypotheses

Retain L071's identical marked projective K3 factors S_1 and B=S_2,
fixed common hyperkähler metric, real Kähler class h, and full integral
mixed tensor tau_D. Use its fixed numerical chamber from L044. Write
e_1=eta tensor 1, e_2=1 tensor eta and P=e_1e_2, with integral_S eta=1.
Let k=(-4,-2,1,2), k.h=0 and k^2=-14, and let L and L_B be the line
bundles of class k on the two marked factors. Suppose F is locally
free of rank two, slope-polystable for Omega=p_1^*h+p_2^*h, with
integral c_1(F)=0 and

\[
             \operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D.
\]

Put p=p_2, G=F tensor p_1^*L^{-1}, M=R^1p_*G and W=R^2p_*G.
Let Z be the finite, possibly empty, split-parameter set of L096 and
put z=|Z|. Use the audited conditional local conclusions of L145/L146
at every actual member of Z. Neither F nor any member of Z is known
to exist. No positivity, polystability or scalar self-duality of M
is a hypothesis.

## Conclusion

The ordinary degree-zero image is zero, W is one residue field at
each split parameter, and M is locally free of rank twenty-four:

\[
 p_*G=0,\qquad W\simeq\bigoplus_{a\in Z}\mathbb C_a,
 \qquad M\text{ locally free of rank }24.
                                                        \tag{1}
\]

The sum in (1) is zero when Z is empty. In rational cohomology,

\[
 \boxed{\operatorname{ch}(M)=24-4k+(z-167)\eta.}           \tag{2}
\]

In integral cohomology and in Pic(B), respectively,

\[
 c_1(M)=-4k=(16,8,-4,-8),\qquad
 \det M\simeq L_B^{-4},\qquad c_2(M)=(55-z)\eta.          \tag{3}
\]

The canonical map M -> M^{**} is an isomorphism, so no hull correction
occurs. This conditional ADVANCE / REPRODUCTION specializes known
tools; it is not a claim of progress beyond the checked sources.
It supplies global bookkeeping only. In particular, (3) supplies no
bound on z without a further geometric input on M. Kernel existence,
split-locus nonemptiness, positivity, reconstruction, transport and
universal primitive Hodge realization remain unresolved. The separate
critical audit below preserves this whole-base specialization without
a substantive repair or stronger conclusion.

## Proof

**Imported theorems and scope.** Reuse the invocation-start SPECIALIZE
assessment `drafts/literature/2026-10-22-twisted-middle-global-character.md`.
For perfect pushforward and arbitrary derived base change use
[Stacks Lemma 36.30.1, 0A1H](https://stacks.math.columbia.edu/tag/0A1H).
The smooth projective projection is finitely presented, G is locally
free and base-flat with proper support, and the first perfect input
is O_X. Thus Rp_*G is perfect and its derived fibres are R Gamma(G_a).
Use [Lemma 36.31.3, 0BDK](https://stacks.math.columbia.edu/tag/0BDK)
for one-degree concentration and finite local freeness. Minimal
finite-free representatives, as used in L145, are covered by
[Lemmas 15.77.6–7, 0BCC](https://stacks.math.columbia.edu/tag/0BCC)
and [0BCD](https://stacks.math.columbia.edu/tag/0BCD).

The surface stability, duality and RR inputs are Huybrechts,
*Lectures on K3 Surfaces*, author-hosted prepublication draft,
[Chapter 1, (2.5)–(2.6) and Proposition 2.4, pp. 11–13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11),
and [Chapter 9, Section 3.1, pp. 175–176](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175).
The slope arguments below use the actual real h. They do not require
an integral polarization or a transform-preservation theorem.

For GRR use the general coherent theorem: Fulton, *Intersection Theory*,
second edition (1998), Theorem 15.2, pp. 286–287, and Example 15.2.8,
pp. 291–292. Its coherent alternating pushforward and relative-tangent
form are also stated in Grothendieck, SGA 6, Expose 0, Section 1,
[(1.1)–(1.3)](https://grothendiecksga.com/read/sga6/fr/0.html).
Both varieties here are smooth projective over C and p is proper.
This theorem permits coherent point-sheaf higher images. The
locally-free-higher-images version of Stacks 02UO alone would not
suffice when Z is nonempty. No general theorem is reproved here;
the necessary family specialization follows.

**Endpoints on the stable open.** By L071 and L096, every F_a is
h-polystable of charge fourteen; outside Z it is stable, while at
a in Z it is L direct sum L^{-1}. Tensoring a stable bundle with
the slope-zero line L^{-1} preserves stability and slope zero.
Thus for a outside Z, a nonzero section of G_a would inject O into
a rank-two stable slope-zero bundle, contradicting stability. The
dual is stable of slope zero as well, so Serre duality and K_{S_1}=O
give H^2(G_a)=H^0(G_a^vee)^*=0. Hence both endpoints vanish there.

On every fibre, including a split one,

\[
 \operatorname{ch}(G_a)
 =(2-14\eta)e^{-k}=2-2k-28\eta,
 \qquad \chi(G_a)=4-28=-24.                              \tag{4}
\]

Consequently h^1(G_a)=24 on U=B minus Z. Perfect concentration makes
M|_U locally free of that rank and kills both ordinary endpoints on U.
At a split point G_a=O direct sum L^{-2}; L094 gives derived-fibre
dimensions (1,26,1). Those dimensions are not ordinary base-change
dimensions for M or W.

**Ordinary sheaves on the whole base.** All derived fibres have
cohomology only in degrees 0,1,2. Minimality therefore gives, near
each point, a finite-free representative of Rp_*G in those degrees.
Its degree-zero cohomology is a submodule of its finite-free degree-zero
term. Since B is integral, this kernel is torsion-free. It vanishes
on the dense open U by the preceding endpoint test, so it is zero.
This proves p_*G=0 without asserting base change at a split point.

The top sheaf vanishes on U, so its support is contained in Z. At
each actual a in Z, L145 identifies its entire ordinary algebraic stalk
with O_{B,a}/m_a, not just its derived fibre. These stalks are nonzero
and annihilated by m_a. A coherent sheaf with finite support is the
sum of its point-supported pieces; the stated stalks identify each
piece with a single residue field. This proves the second assertion
of (1), including all multiplicities and the empty case.

At every a in Z, L146 makes the ordinary middle stalk free of rank 24
over the original algebraic local ring and proves its canonical hull
map is an isomorphism. Together with the U calculation, M is free of
rank 24 at every closed point. Coherence over the Noetherian base
makes it finitely presented, so each such stalk has an open neighborhood
of local freeness of that rank. The closed complement of their union
has no closed point and must be empty on this finite-type C-scheme.
Thus M is locally free everywhere. These are the same intrinsic
cohomology sheaves on overlaps; local basis choices need no extra
compatibility. Local freeness proves the global canonical hull claim.

**Full signed GRR.** L071's rank-two character and full mixed square
give, for these pure coefficients,

\[
 \operatorname{ch}_3(F)=0,\qquad
 \operatorname{ch}_4(F)=\frac{(-14)(-21)+78}{6}P=62P,
 \qquad \tau_D^2=156P.                                 \tag{5}
\]

The number 78 retains half the entire mixed square, including its
transcendental part; no former virtual K-class is substituted for F.
Write k_1=p_1^*k. Since k_1^2=-14e_1 and k_1e_1=0,

\[
 e^{-k_1}\operatorname{td}(T_p)
 =(1-k_1-7e_1)(1+2e_1)=1-k_1-5e_1.                     \tag{6}
\]

The relative coherent GRR formula, after passing to rational
cohomology, is therefore

\[
 \operatorname{ch}(Rp_*G)
 =p_*\big[(2-14e_1-21e_2-\tau_D+62P)(1-k_1-5e_1)\big]. \tag{7}
\]

Only terms of first-factor cohomological degree four survive.
The rank contribution is -10-14=-24. The base degree-two term is
p_*(tau_D k_1)=Dk: both minus signs cancel, and the degree-two
Kunneth factors introduce no odd exterior sign. The base degree-four
term is (105+62)eta=167eta, from (-21e_2)(-5e_1) and 62P.
All other products have the wrong first-factor degree, or vanish
there by degree. In particular there is no omitted ch_3 term.
Thus

\[
                  \operatorname{ch}(Rp_*G)=-24+Dk+167\eta.
                                                               \tag{8}
\]

In coherent K-theory, (1) gives [Rp_*G]=-[M]+[W]. A length-one
point sheaf on the smooth surface has character eta, so

\[
          \operatorname{ch}(M)=24-Dk+(z-167)\eta.          \tag{9}
\]

The point correction has positive sign in (9). There is no hull
quotient to add or subtract. This is cohomological bookkeeping;
the input cohomological character does not determine a Chow class.

**Integral first class and the numerical chamber.** The fixed chamber
of L044 has im(A_c)=W_0 and K=ker(A_c)=W_0^perp=Q k.
This uses its numerical chamber construction only, not existence of
its tested presentation. L071 gives D|_N=2A_c+4pi_K, hence Dk=4k.
The correspondence action is in any event integral on k, since
Dk=p_*(tau_D k_1) with integral tau_D and k_1.

Equation (9) gives c_1(M)=-4k rationally. Integral H^2(B,Z) is
torsion-free, and Pic(B) injects into it: use Huybrechts, cited draft,
[Chapter 1, Section 3.2, (3.1), printed p. 15](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=15),
from the exponential sequence and H^1(O_B)=0. The difference of
c_1(M) and the integral class -4k therefore vanishes integrally.
Picard injection then identifies det M with L_B^{-4}. This also
checks the sign in the nonzero first class; slope zero alone would
not determine it.

Finally c_1(M)^2=16k^2=-224eta. The surface character identity gives
ch_2(M)=c_1(M)^2/2-c_2(M)=-112eta-c_2(M). Comparing with (9)
proves c_2(M)=(55-z)eta. H^4(B,Z)=Z eta is torsion-free, so this
equality also holds integrally. This proves (2)–(3).

The continuation test passes: ordinary support, every split stalk,
whole-base freeness, signed coherent GRR and integral recovery are
justified. None supplies a Hermite–Einstein metric, polystability or
an effective-cycle inequality for M. The earlier IT, automatic-index-
effectivity, strict untwisted Euler and necessary-jet stops remain
unchanged. The separate whole-base critical audit is recorded below.

**Separate critical audit, 2026-10-23 (step 471).** Use the unchanged
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-23-twisted-middle-global-character-critical-audit.md`
and its inspected theorem statements and proof cases. This audit is
EXPLORATION / REPRODUCTION: no substantive error or stronger conclusion
is found. It checks the family specialization of the cited standard
results; it does not reprove GRR or duplicate L145/L146's local audits.

First check that the local inputs apply to the same sheaves. The
coefficient is the fixed twist G=F tensor p_1^*L^{-1} in both local
lemmas. Their hypotheses retain the identical marking and common
metric, integral first class, full negative tensor and an arbitrary
selected actual split parameter. L096 supplies exactly the finite
set where F_a is L plus L^{-1}; it supplies no scheme multiplicity.
Outside that set, tensor stability and dual stability apply at the
actual real h. A section gives an injective map O -> G_a (the source
is a line and the target is torsion-free on an integral surface),
contradicting strict slope stability. Apply the same argument to
G_a^vee before Serre duality. At a split point the O summand contributes
one to each endpoint, and L094's L^{-2} contributes 26 only in degree
one. Thus the derived ranks (1,26,1) and generic middle rank 24 agree
with the fibre Euler value -24 without asserting ordinary base change.

For whole-base assembly it suffices to use minimal representatives
at closed points and spread them to neighborhoods, by the cited
0BCC/0BCD. Derived fibre amplitude [0,2] makes their degree-zero
cohomology a kernel inside a free module. Every such nonempty open
meets U, so torsion-freeness on the integral base forces this kernel
to vanish. The entire top stalk in L145 is R/m, not merely a
one-dimensional tensor product; it determines the point-sheaf length
and kills any hidden thickness. Finite support therefore gives exactly
the asserted sum W. L146 gives the entire ordinary middle stalk free
over R itself. The open free locus of this finitely presented sheaf
contains every closed point, so its closed complement is empty by
the Jacobson property. This also treats nonclosed points and identifies
the canonical hull map. If Z is empty, concentration on all of B
gives the same conclusions with W=0. No gluing of chosen local bases
or twisted scalar self-duality is needed.

Next recompute the signed character from the lower data, not from
the asserted answer. The full square is
2(14)(21)+156=744 times P. Rank two and c_1=0 give ch_4=744P/12=62P
and ch_3=0. The factor exp(-k_1)td(T_p) is 1-k_1-5e_1: the
line-square coefficient is -7 and the relative Todd coefficient is
+2. Among all products, the fibre-degree-four terms contributing
base degrees zero, two and four are respectively
(-10-14), tau_D k_1, and (105+62)P. A rational q-dual pair of bases
v_i,v^i writes tau_D as sum v_i tensor Dv^i; contraction with k in
the first factor gives sum q(v_i,k)Dv^i=Dk. Equivalently the reverse
convention gives D^*k=Dk. Degree two is even, so there is no exterior
minus sign in this contraction. No integral NS/T decomposition is
required. The coherent alternating class is -[M]+[W], hence the
length contribution is +z eta in ch(M), not -z eta.

An additional absolute Euler consistency check retains the base Todd
factor: GRR gives chi(X,G)=-48+167=119. The proposed ordinary character
gives chi(B,M)=48+z-167=z-119, while chi(B,W)=z. The actual alternating
coherent identity therefore gives -(z-119)+z=119. This is a sign check,
not an effectivity or cohomology-vanishing argument.

Finally the fixed numerical chamber, rather than any presentation,
controls the first class. L044's matrix (9) fixes k and preserves W_0;
its A_c=gA_0g^{-1} has image W_0 and kernel W_0^perp=Qk. L071's
operator is 2A_c+4pi_K on N, so its value at k is 4k. Rational GRR
therefore gives -4k with the stated sign. The kernel of
H^2(B,Z) -> H^2(B,Q) is torsion and H^2(B,Z) is torsion-free, so
the equality is integral. Picard injection then gives precisely
L_B^{-4}, without a residual flat or torsion line. Squaring the first
class gives -224eta; the surface character identity consequently
recovers (55-z)eta as c_2, integrally because H^4(B,Z)=Z eta.

The six direct inputs remain L044, L071, L094, L096, L145 and L146.
The audit establishes neither positivity nor polystability of M,
nor a bound on z, F or split-locus existence, reconstruction, transport
or universal primitive Hodge realization. The recorded IT,
automatic-effectivity, strict-Euler and necessary-jet stops remain.

## Mathlib

Full matching coverage of this conditional global twisted-family
specialization is **not checked**. The precise general inputs above
are imported; unknown Mathlib coverage is not evidence of absence.
The endpoint and coherent-sheaf assembly, signed degree calculation
and integral recovery are the local specialization written here.
No mathematical script or originality claim is needed.
