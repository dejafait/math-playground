# L154 — Stable-summand bound for the twisted rank-24 image

## Hypotheses

Retain the identical marked projective K3 factors, original common
hyperkähler metric g and real Kähler class h of L147 and audited L153.
Suppose F is their locally free Omega-polystable rank-two bundle with
integral c_1(F)=0 and ch_2(F)=-14e_1-21e_2-tau_D, with exactly their
full tensor and fixed numerical chamber. Use the preferred dual HE
twisting metric of audited L152, as in L153. Write
M=R^1p_{2*}(F tensor p_1^*L^{-1}) and z=|Z|, where Z is the finite,
possibly empty, split-parameter set. Normalize integral_B eta=1.

Use L147's actual locally free character and L153's polystability:

\[
 \operatorname{ch}(M)=24-4k+(z-167)\eta,
 \qquad k=(-4,-2,1,2),\quad k^2=-14\eta,
 \qquad \mu_h(M)=0.
\]

Use L052's exact perpendicular integral Picard lattice
NS(B) intersect h-perp = Zk. No simplicity or self-duality of M,
nonempty Z, existence of F, or independent lower count is assumed.

## Conclusion

The conditional bound sharpens L153 to

\[
                         \boxed{0\leq z\leq147.}       \tag{1}
\]

If z=147, the stable decomposition necessarily has the form

\[
                 M\simeq O_B^{\oplus16}\oplus E^{\oplus4},
 \qquad \operatorname{ch}(E)=2-k-5\eta,                \tag{2}
\]

for one locally free h-stable type E. A formal assignment (2) passes
all the assessed stable-type character, simple-index, section/dual-section
and pairwise Hom/Serre-dual index constraints. Thus these selected
constraints alone cannot improve 147. This is a formal compatibility
claim, not an existence theorem for E, M, F or any split set.

This ADVANCE / REPRODUCTION specializes known K3 index tools. It improves
necessary upper control only; an independent contradictory lower bound,
common-kernel existence, cycles and transverse transport remain absent.
The separate critical audit below preserves the bound, equality
classification and formal endpoint without repair or strengthening.
The universal primitive rational Hodge realization gap remains open.

## Proof

**Sources, relevance and scope.** Reuse the unchanged invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-23-twisted-stable-summand-index-bound.md`.
Import Daniel Huybrechts, *Lectures on K3 Surfaces*, author-hosted
prepublication draft, Chapter 9, Sections 1.2–1.3, equations (1.2)–(1.4)
and Remark 1.5, printed pp. 169–170
([source](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=169)),
for v(A)=(r,c_1,r+ch_2), chi(A,C)=-<v(A),v(C)> and the simple bound
<v(A),v(A)> >= -2. Stable implies simple and dual stability for a
Kähler-class slope are Section 3.1(iii)–(iv), pp. 175–176
([source](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175)).
For the HE stable decomposition use Theorem 4.9, p. 182
([source](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182)),
with L153 already establishing the actual same-metric applicability.

The assessed equal-slope stable-Hom input is also covered by Arvid
Perego, *Kobayashi–Hitchin corrispondence for twisted vector bundles*,
Complex Manifolds 8 (2021), Propositions 3.9–3.12 and 3.15, pp. 36–38
([source](https://unige.iris.cineca.it/retrieve/e268c4cd-97f6-a6b7-e053-3a05fe0adea1/10.1515_coma-2020-0107.pdf#page=36)).
Use ordinary bundles, trivial cocycle and zero B-field, with zero HE
factors. In particular, nonisomorphic stable types of the same slope
have no Hom in either direction. Serre duality uses K_B=O_B.
These are imported general theorems, without reproof. No generic ample
polarization, primitivity or stable existence theorem is used in reverse.

The intermediate threshold is a necessary upper bound below 162,
potentially usable with independent lower control. The continuation
test is a uniform bound or a justified exhaustive search, followed by
full compatibility checks at its endpoint. ATTEMPTS/043, /047 and /053
retain compatible arbitrary-rank or repeated branches in different
characters: their numerical verdicts are not inputs here. They require
retaining multiplicities and distinguishing compatibility from existence.

**Uniform bound with no omitted ranks or first classes.** Write the
actual polystable decomposition as

\[
                  M=\bigoplus_i A_i^{\oplus m_i},
 \qquad \operatorname{ch}(A_i)=r_i+t_i k+d_i\eta,       \tag{3}
\]

where the A_i are pairwise nonisomorphic stable locally free types and
m_i are positive integers. They are locally free because they are
direct summands of the locally free M. Their ranks are positive and
their slopes are zero. Each determinant has integral zero-slope first
class, so L052 gives its class t_i k with t_i integral. Also
ch_2(A_i)=c_1(A_i)^2/2-c_2(A_i), so d_i=-7t_i^2-c_2(A_i) is integral.
The character sums are exactly

\[
 \sum_i m_i r_i=24,\qquad \sum_i m_i t_i=-4,
 \qquad \sum_i m_i d_i=z-167.                          \tag{4}
\]

For one stable type abbreviate (r_i,t_i,d_i) to (r,t,d). Its simple
Mukai bound is

\[
 -14t^2-2r(r+d)\geq-2,
 \qquad\text{equivalently}\qquad r^2+rd+7t^2\leq1.   \tag{5}
\]

If t=0, (5) implies d<=0: any integer d>=1 would make
r^2+rd>=r^2+r>=2. If a=|t|>=1, suppose instead d>=-5a+1.
Since r>0, (5) would imply

\[
                r^2-(5a-1)r+7a^2-1\leq0.             \tag{6}
\]

The discriminant of this monic quadratic is

\[
       (5a-1)^2-4(7a^2-1)=-3a^2-10a+5<0
                         \quad(a\geq1).
\]

The quadratic is strictly positive for every real r, contradicting (6). Thus for
every rank, arbitrary integral t and arbitrary multiplicity,

\[
                              d\leq-5|t|.             \tag{7}
\]

Summing (7) in (4) gives

\[
 z-167\leq-5\sum_i m_i|t_i|
          \leq-5\left|\sum_i m_i t_i\right|=-20,
\]

which proves (1). There is no cutoff on individual t, no partition
sampling and no assumption that M is simple. The uniform proof covers
all the assessed stable decompositions. Rank-one factors satisfy the
stronger exact identity d=-7t^2, consistent with (7).

**Equality classification.** Suppose z=147. Equality in both finite
sums forces d_i=-5|t_i| for every type and all nonzero t_i to be negative.
For t=0 and d=0, (5) gives r=1. A line of integral first class zero
on a K3 is O_B: Pic^0(B)=0 and the first-Chern map is injective.

For a=|t|>=1 and d=-5a, (5) becomes

\[
                  (r-5a/2)^2+3a^2/4\leq1.            \tag{8}
\]

Hence a=1; for a=1 its positive integral solutions have r=2 or r=3.
A stable rank-greater-than-one bundle of slope zero has H^0=0:
a section would give a nonzero Hom from the stable slope-zero O_B
to a nonisomorphic stable type. Its dual is likewise stable, so
Serre duality gives H^2=0. Surface RR then requires 2r+d<=0.
Here d=-5, which excludes r=3. Thus every nonzero-first-class type
has character 2-k-5eta.

Two distinct stable types with this character would have
chi(A_i,A_j)=2 by their common Mukai vector's square -2. Distinct-type
Hom vanishing and Serre duality would instead give
chi(A_i,A_j)=-dim Ext^1(A_i,A_j)<=0, a contradiction. Therefore there
is only one such isomorphism type E. Equations (4) force multiplicity
four and then sixteen trivial lines, proving the conditional (2).
Distinct numerical types have not been identified without this test.

**Complete formal endpoint check.** Assign two stable types O and E,
with multiplicities 16 and 4 and Mukai vectors

\[
                    v(O)=(1,0,1),\qquad v(E)=(2,-k,-3).
\]

Their ranks total 24; their first classes total -4k; their second
characters total -20eta=(147-167)eta. The line O has exactly its
required character. The formal E has integral c_2=-2eta, since
c_1(E)^2/2=-7eta, and its Mukai square is
-14-2(2)(-3)=-2. A negative c_2 is not prohibited for this nonzero
first class; its discriminant is 4(-2)-(-14)=6>0.

Every self and pairwise index among the chosen types is:

| Ordered type pair | Mukai pairing | chi | (dim Ext^0, dim Ext^1, dim Ext^2) |
| --- | ---: | ---: | --- |
| O,O | -2 | 2 | (1,0,1) |
| E,E | -2 | 2 | (1,0,1) |
| O,E | 1 | -1 | (0,1,0) |
| E,O | 1 | -1 | (0,1,0) |

The mixed pairing is -1(-3)-2(1)=1; both mixed endpoint Hom groups
are zero because the types are nonisomorphic and stable of slope zero.
The E row against O gives cohomology (0,1,0), consistent with
chi(E)=2(2)-5=-1 and the section/dual-section test. The dual has the
same second character and endpoint vanishings. O has cohomology
(1,0,1). Thus the full formal M has cohomology (16,4,16), Euler
characteristic 28=48-20, with no independent value for its sections
assumed. Repeated copies do not receive the distinct-type Hom test:
their full matrix endomorphisms remain present.

For an additional multiplicity check, the whole formal End(M) has
Ext dimensions (272,128,272): 16^2+4^2=272 in each endpoint and
2(16)(4)=128 in the middle. Its Euler value is 416. Independently
v(M)=(24,-4k,4) has square -224-2(24)(4)=-416, giving the same RR
value. The full M is therefore not incorrectly subjected to the
simple bound. Its c_2 is -112+20=-92=55-147, and L153's signed
discriminant is 48(147)-7792=-736<=0, retaining every point correction
and the nonzero first-class square.

All selected constraints admit this formal endpoint. Since these
constraints are only necessary, neither the table nor the conditional
equality classification constructs E or identifies any actual image
with (2). No symmetric or alternating form on M is assumed; none is
available from the stated inputs. The bounded numerical filter stops
at 147. A stronger global count would require additional information.

**Separate critical audit, 2026-10-24 (step 501).** Reuse the
invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-24-twisted-stable-summand-index-critical-audit.md`
and its inspected Huybrechts and Perego theorem/proof coverage. The
verdict is EXPLORATION / REPRODUCTION: no substantive error or stronger
conclusion was found. This checks the specialization, not a new general
theorem or an existence assertion.

First check that the stable-type inputs concern this actual M. L147
gives its ordinary locally free R^1 image and the full character on B;
audited L153 gives its slope-zero polystability for the same original
real h and preferred dual HE metric through L152. The decomposition is
therefore a holomorphic direct sum of positive-rank locally free stable
bundles of slope zero. Each determinant is an integral Picard class.
L052's lattice calculation is independent of that lemma's positive
mixed-sign bundle hypothesis: it uses only the retained marked NS
basis, determinant -7 and fixed h. In its displayed slope formula,
the rational independence of lambda, 1, 1/lambda forces
y=-w, x=-2w, z=w/2; hence w is even and the class is an integral
multiple of k. This checks applicability to the present negative
mixed tensor without transferring L052's bundle conclusions.
The stable factors have integral d because k^2/2=-7eta and c_2 is
integral. No integral NS/transcendental splitting is used.

For the all-rank step, the Mukai vector of a type is (r,tk,r+d).
Simplicity gives 2-dim Ext^1=-v^2, so (5) has the stated direction.
For t=0 it in fact gives rd<=1-r^2<=0, and thus d<=0.
For a=|t|>=1, failure of (7) means d>=-5a+1 by integrality.
The quadratic in (6) has minimum
(3a^2+10a-5)/4>0 over all real r. Thus no omitted positive rank or
large first class evades it. All sums in (4) are finite with positive
multiplicities. Equality at z=147 forces every nonnegative deficit
-5|t_i|-d_i to vanish, and equality in the triangle inequality forces
all nonzero t_i to have the negative sign of their total -4.

For t=0 equality in (5) forces rank one and trivial first class;
Picard injection on a K3 identifies that line with O. For nonzero t,
(8) gives a^2<=4/3, hence a=1, and then
(r-5/2)^2<=1/4 gives exactly r=2,3. Both are nonisomorphic to O;
equal-slope stable Hom vanishing and dual stability give H^0=H^2=0.
The rank-three option has chi=1, which is impossible, whereas rank
two has chi=-1. The remaining vector has square -2. If two
nonisomorphic stable types had this vector, both ordered Hom groups
would vanish, Serre duality would remove Ext^2, and their Euler value
2 would be impossible. The unique type consequently occurs four
times, and the rank equation leaves exactly sixteen trivial lines.
This does not assert that the unique numerical possibility exists.

Finally recompute every endpoint index with multiplicities. For O and
E the Mukai Gram matrix is ((-2,1),(1,-2)). Self Hom and Ext^2 each
have dimension one; the resulting self Ext^1 dimensions are zero.
Both ordered mixed pairs have Ext dimensions (0,1,0), so the complete
matrix-multiplicity sum is

    Ext^0(M,M) = Ext^2(M,M) = 16^2 + 4^2 = 272,
    Ext^1(M,M) = 16*4 + 4*16 = 128.

Its Euler value 416 agrees with -v(M)^2 for v(M)=(24,-4k,4).
The section and dual-section indices give (h^0,h^1,h^2)(M)=(16,4,16)
and chi(M)=28; 2*24+ch_2(M)=48-20 also equals 28. For E,
c_2=-7-(-5)=-2 and discriminant 4c_2-c_1^2=6, while for M,
c_2=-112-(-20)=-92 and 23c_1^2-48c_2=-736.
Thus neither negative c_2 contradicts the retained nonzero first
class. The dual E has the same Euler characteristic and endpoint
vanishings; it is not assumed to occur in M. No scalar self-duality,
orthogonal multiplicity rule or simplicity of the whole M enters.

The conditional bound and endpoint compatibility therefore survive
the independent audit. ATTEMPTS/087's stop remains in force for these
selected numerical constraints. No actual section count independent
of that formal endpoint, lower split count, nonempty Z or F existence
has been established. Direct mathematical inputs remain L052, L147
and L153; neither the argument assembly nor its DAG edges change.

## Mathlib

Full matching coverage of real-Kähler polystable decomposition, these
K3 index tools and their rank-24 specialization is **not checked**.
Unknown availability is not evidence of absence. The cited general
results are imported; the uniform arithmetic specialization and formal
compatibility check are a REPRODUCTION, with no novelty, existence or
Lean-verification claim.
