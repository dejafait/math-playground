# L108 — Algebraic equality-family splitting and signed point defects

## Hypotheses

Retain L071/L097's identical marked smooth projective complex K3
surfaces S_1 and B=S_2, their common hyperkähler metric g and real
Kähler class h, and the full integral mixed tensor tau_D. Suppose F
is an actual locally free rank-two bundle on X=S_1 x B,
slope-polystable for p_1^*h+p_2^*h, with integral c_1(F)=0 and

\[
 \beta=\operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D,
 \quad e_1=\eta\otimes1,\quad e_2=1\otimes\eta,
 \quad \int_S\eta=1.
\]

Use L071's compatible connection, forced higher characters and full
mixed square tau_D^2=156e_1e_2. Use audited L097: the nonstable
fibre set Z is finite, possibly empty, each fibre there is
L direct sum L^{-1}, and all fibres over U=B minus Z_red are stable.
Use audited L095's actual harmonic KS derivative and its full
normalized pairing 2lambda g, and audited L100's natural stable-open
comparison and parametrized total geodesy. Here 1<lambda<5/4 and
D[sigma]=2lambda[sigma], with the identical fixed holomorphic forms
sigma=omega_J+i omega_K. No F or point of Z is asserted to exist.

Put p:X -> B and V=End_0(F). All coherent sheaves and morphisms below
are algebraic. Write C=Rp_*V and A_i=R^i p_*V. Let eta also denote
the normalized point class on B. Chern characters are in rational
cohomology; point lengths are algebraic lengths over C.

## Conclusion

One has A_0=0, A_i=0 for i>2, and A_2 is supported in Z. The middle
sheaf A_1 is torsion-free, restricts on U to a rank-fifty vector
bundle E_U with C|_U=E_U[-1], and has a locally free reflexive hull
E=A_1**. There is a unique extension of the actual algebraic
stable-open symplectic splitting to an algebraic splitting on B:

\[
 E=T_B\oplus N,\qquad \operatorname{rk}N=48.                 \tag{1}
\]

Both summands have nondegenerate algebraic alternating forms. On U
the second summand is also the metric normal summand of L100.
Statement (1) extends algebraic objects and maps, not their chosen
metrics or connections.

The quotient Q=E/A_1 is supported in Z. With the unknown nonnegative
integers w=length(A_2), q=length(Q), the complete signed budget is

\[
 \begin{aligned}
 \operatorname{ch}(C)&=-50+824\eta,\
 \operatorname{ch}(E)&=50+(-824+w+q)\eta,\
 \operatorname{ch}(N)&=48+(-800+w+q)\eta,\
 c_1(E)=c_1(N)&=0\quad\hbox{integrally},\
 c_2(N)&=(800-w-q)\eta.                                  \tag{2}
 \end{aligned}
\]

More precisely w and q are the sums of the lengths of the indicated
stalks at z in Z. A middle-sheaf torsion correction would enter with
a minus sign in ch(E), but that torsion is zero here. There is no
omitted degree-zero or higher direct image. When Z is empty, w=q=0
and (1)--(2) hold with E=A_1 globally.

No value or upper bound for w or q, no relation between them, and no
semistability or metric extension of E or N is established by this
argument. Thus this budget gives no Chern-inequality obstruction.
It identifies what further local control and independent analytic
input an obstruction would need. This is a conditional ADVANCE /
REPRODUCTION of the assessed algebraic tools; the separate critical
audit below corrects the hull-quotient sign and preserves the splitting.
It supplies neither F, a cycle, transverse
transport nor universal primitive Hodge realization.

## Proof

**Imported tools and their scope.** Use the prior SPECIALIZE assessment
`drafts/literature/2026-10-15-equality-relative-ext-algebraic-defect-budget.md`.
The primary tangent/KS and trace/cup descent inputs are Huybrechts--Lehn,
*The Geometry of Moduli Spaces of Sheaves*, Aspects of Mathematics E31
(1997), [Section 10.1.8/Example 10.1.9 and Theorem 10.2.1 with its
preceding construction, pp. 220--223](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=232).
They apply on the positive-rank stable surface locus with vanishing
trace-free Ext^2. For a stable fibre here, Hom is the scalar line;
trace duality and K_{S_1}=O make trace-free Ext^2 zero. Also
H^1(O_{S_1})=0, so removing trace changes no degree-one tangent.
The common-H stable locus is supplied by L097. These general results
are imported, not reproved; only their actual-family application is
made below. L068 is a methodological comparison for these tools,
not an input of its charge-seven characters or global concentration.

Import [Stacks Lemma 36.30.4, 0B91](https://stacks.math.columbia.edu/tag/0B91)
for proper flat finitely presented perfect pushforward with arbitrary
derived base change, and [Lemma 36.31.3 in 0BDH](https://stacks.math.columbia.edu/tag/0BDH)
for fixed-rank single-degree concentration. The map p is smooth
projective of relative dimension two and V is locally free, so the
hypotheses hold. Import [Stacks 0EBJ](https://stacks.math.columbia.edu/tag/0EBJ)
for reflexive restriction/extension across a complement with ambient
depth at least two, and [0B3N](https://stacks.math.columbia.edu/tag/0B3N)
for reflexive equals finite locally free on a regular scheme of
dimension at most two. B is smooth of dimension two and each removed
point has a regular local ring of depth two. In particular morphisms
between the resulting bundles extend uniquely. None of these results
extends a Hermitian metric.

Use Fulton, *Intersection Theory*, second edition (1998), Theorem
15.2, pp. 286--287, for coherent/perfect signed GRR, and
[Stacks 02UM](https://stacks.math.columbia.edu/tag/02UM) for additive
Chern characters. The elementary character identities and rank-two
truncation are already applied with these hypotheses in L071.
[Stacks 02UO](https://stacks.math.columbia.edu/tag/02UO) is supporting
relative GRR coverage; its finite-locally-free-higher-image version
alone would not justify applying it to A_2 here. We use Fulton's
coherent K-theory statement. The applicability and signed
specialization, rather than a general reproof, are the present work.

**Ordinary images and the finite corrections.** The trace projection
(tr/2)id splits End(F), so V is locally free and self-dual by its
nondegenerate trace form. All these data algebraize by GAGA on the
projective X. On a stable fibre V has H^0=H^2=0. For charge fourteen,
ch(V_y)=3-56eta, so surface RR gives chi(V_y)=6-56=-50 and h^1=50.
The perfect concentration theorem gives C|_U=E_U[-1] with E_U locally
free and base-changing, and A_2|_U=0. Relative cohomological dimension
two gives A_i=0 for i>2. Thus the coherent A_2 has finite support in Z.

The sheaf A_0=p_*V is torsion-free: on an integral affine base open,
multiplication by a nonzero base function is injective on V, since
p is flat and V locally free; the same is true on its sections.
It is generically zero by stable-fibre concentration. Hence A_0=0.
A pointwise trace-free Hom at a split fibre does not contradict this
ordinary-sheaf vanishing.

Initially let T be the torsion subsheaf of A_1. Since A_1|_U is
locally free, T is supported in Z. In fact T=0. Here is a local
argument retaining the difference between ordinary and derived
fibres. At z in Z, put R=O_{B,z}, a regular local domain of dimension
two. Perfectness and the derived-fibre amplitude [0,2] give a local
finite free representative

\[
          K^0\xrightarrow{d^0}K^1\xrightarrow{d^1}K^2
                                                               \tag{3}
\]

for C. More precisely import [Stacks Lemmas 15.77.6, 0BCC](https://stacks.math.columbia.edu/tag/0BCC)
and [15.77.7, 0BCD](https://stacks.math.columbia.edu/tag/0BCD): a perfect
complex has a finite free local representative with residue-field
Betti ranks. Such amplitude follows because derived base change identifies
every residue-field fibre with the cohomology of V on a surface;
one cancels invertible differential blocks in a finite free perfect
representative outside degrees 0,1,2. The equality A_0=0 makes d^0
injective. A section of T_z lifts to v in ker(d^1) and is zero in
H^1 of (3) on the punctured Spec R. There v=d^0 a for a unique
section a of K^0 on that puncture: local preimages exist and glue
because d^0 is injective. Apply [Stacks Lemma 31.5.11, 0E9I](https://stacks.math.columbia.edu/tag/0E9I)
to the free module K^0: its depth at the omitted closed point is two,
so its sections on the puncture extend uniquely across z.
Then v-d^0 a is a section of
the free K^1 vanishing on the puncture, so is zero. The torsion
section was zero. This proves A_1 torsion-free without ordinary
base change at z.

A torsion-free coherent sheaf on this smooth surface injects into
its reflexive hull, which is locally free by 0B3N; the quotient is
zero wherever the original sheaf is locally free. Thus E=A_1** is
a bundle, E|_U=E_U and Q=E/A_1 has finite support in Z. This also
constructs the needed extension without assuming arbitrary analytic
objects on U algebraize.

**The algebraic symplectic tangent projector on U.** The actual
algebraic family defines its algebraic KS morphism

\[
                \kappa:T_U\longrightarrow E_U.
\]

Relative cup product, matrix trace and Serre trace, with the fixed
nonzero algebraic two-form sigma on S_1, give an alternating algebraic
form omega_E on E_U. Fibrewise Serre duality and trace self-duality
make it nondegenerate. Normalize this form by the constant (2pi i)^(-2)
so its value on Dolbeault representatives a,b is

\[
       \omega_E(a,b)=\frac1{(2\pi i)^2}
                         \int_{S_1}\sigma\wedge\operatorname{Tr}(a\wedge b).
                                                               \tag{4}
\]

Multiplication of an algebraic morphism over C by this fixed complex
constant preserves algebraicity. Formula (4) specifies the order
and normalization, not an additional hypothesis.

The natural tangent theorem identifies kappa with the actual family
derivative. To make descent explicit, use local stable Quot families
for the common-H classifying map. Locally a representing family and
F differ by a base line: their fibrewise Hom is one-dimensional,
base change gives a line of Hom maps and evaluation is a fibrewise
isomorphism. Conjugation by scalar automorphisms, and tensoring by
a base line, act trivially on End_0, its trace, cup product and KS.
Thus these natural comparisons glue to the actual E_U and kappa.
No universal sheaf or embedding of the image is used. L100's audited
actual-slice comparison identifies this with the same Dolbeault
classes represented by L095's mixed curvature.

For completeness the nondegeneracy of the pulled-back form can be
checked with that actual curvature, including its exterior sign.
At a stable parameter write the mixed (base-(1,0), fibre-(0,1))
part of R as sum dz_i wedge a_i. The a_i represent kappa(partial_i);
the horizontal correction is a fibrewise Dolbeault coboundary and
trace integration with sigma kills it. Total integrability makes
R of type (1,1). To obtain base type (2,0) and fibre type (0,2),
only two of these mixed terms contribute to Tr(R wedge R). For i<j
their coefficient is

\[
 -\operatorname{Tr}(a_i\wedge a_j)
       +\operatorname{Tr}(a_j\wedge a_i)
       =-2\operatorname{Tr}(a_i\wedge a_j).
\]

Moving the fibre one-form past the base one-form gives the first
minus sign; graded cyclicity gives the last equality. The two
ordered terms cancel the 2! in ch_2=Tr(R wedge R)/(2(2pi i)^2).
The complex fibre orientation and the even degree of sigma introduce
no extra sign. Thus, as actual forms on U,

\[
 \kappa^*\omega_E
   =-p_*\left(\frac{\operatorname{Tr}(R\wedge R)}{2(2\pi i)^2}
                                  \wedge p_1^*\sigma\right)
   =2\lambda\sigma_B|_U.                                  \tag{5}
\]

The last equality is L095's actual-form identity (8)--(9), valid
on every fibre, not just a cohomological calculation on nonproper U.
This small normalization check is necessary for the specialization;
it imports neither L062's charge-seven conclusion nor a signed
metric scale. In particular (5) is nowhere degenerate.

Let omega_T=kappa^*omega_E. The unique map pi:E_U -> T_U specified by

\[
        \omega_T(\pi e,v)=\omega_E(e,\kappa v)
                         \quad(e\in E_U,\ v\in T_U)
\]

is algebraic, since omega_T is an invertible algebraic pairing.
It satisfies pi kappa=id. Hence P=kappa pi is an algebraic idempotent,
with kernel N_U the symplectic orthogonal complement of kappa(T_U).
This yields E_U=T_U direct sum N_U. L100 makes the tangent image
quaternionic and parallel on U. In a hyperkähler Hermitian space
the orthogonal complement of a quaternionic subspace equals its
holomorphic-symplectic orthogonal complement: if x is symplectically
orthogonal to W, pairing with Jw (also in W) shows its Hermitian
pairing with w is zero. Thus this is also L100's actual metric
normal splitting on U; that observation asserts no extension of
its connection.

**Extension of the splitting and forms.** Reflexive full faithfulness
across Z extends kappa to i:T_B -> E and pi to r:E -> T_B. Their
composition equals id since it does on U. Consequently P=ir is an
idempotent on the bundle E; its kernel N=ker r is locally free and
E=i(T_B) direct sum N. All ranks are constant and give (1).
The form omega_E and its inverse extend as morphisms between E and
E^vee by the same full faithfulness. Their inverse identities and
alternation extend from U, so this is a nondegenerate alternating
form on E. Orthogonality and the forms on T_B and N extend likewise.
Taking the top exterior power of either symplectic form trivializes
the determinant, proving integral c_1(E)=c_1(N)=0. These are algebraic
extension statements only; GAGA on arbitrary holomorphic data on U
has not been invoked.

**Signed GRR and every point contribution.** Put P_X=e_1e_2. L071's
rank-two identities and the full integral tensor give

\[
 \beta^2=(2\cdot14\cdot21+156)P_X=744P_X,
 \qquad \operatorname{ch}(F)=2+\beta+62P_X.
\]

Both odd characters vanish. Multiplicativity, duality and subtraction
of the actual scalar summand give

\[
 \operatorname{ch}(V)
    =(2+\beta+62P_X)^2-1
    =3+4\beta+992P_X.                                    \tag{6}
\]

The top coefficient is 248+744, including the entire 156 from the
mixed square, not a divisor-only contraction. The relative Todd
class is 1+2e_1 because S_1 is the fibre. In fibre integration the
mixed tensor and its product with e_1 vanish by factor degrees,
p_*e_1=1 and p_*P_X=eta. Therefore coherent GRR yields

\[
 \operatorname{ch}(C)
 =p_*(\operatorname{ch}(V)(1+2e_1))
 =(6-56)+(992-168)\eta=-50+824\eta.                        \tag{7}
\]

The number -168 is 2 times the pure base coefficient -84. No
single-degree concentration on B was used in (7).

To show explicitly where a discarded torsion term would enter,
for a hypothetical torsion subsheaf T supported in Z the exact
sequences with A=A_1/T would give

\[
 [C]=-[A_1]+[A_2],\qquad
 [A_1]=[A]+[T],\qquad [E]=[A]+[Q],
 \quad [E]=-[C]+[A_2]-[T]+[Q].                            \tag{8}
\]

We proved T=0 above. The actual identities are thus
[C]=-[A_1]+[A_2] and [E]=-[C]+[A_2]+[Q]. A finite-length
sheaf of length ell on B has character ell eta, since all complex
points have that cohomology class. Taking characters in these
actual identities proves the E formula in (2). Subtracting
ch(T_B)=2-24eta proves the N formula, and c_1(N)=0 converts its
second character to -c_2(N). A scalar HRR check is
chi(C)=-100+824=724; direct product HRR in (6) gives
12-8(14+21)+992=724. This checks the alternating sign independently.

Nothing in (8) sets either finite length to a derived-fibre dimension
or computes a relation between them. Both contributions must be retained:
A_2 and the hull quotient each lower c_2(N). When Z is empty both
sheaves are zero and no correction remains. With Z nonempty, this
argument stops at the budget (2). Local multiplicities and metric
admissibility are distinct further questions, outside this attempt.
In particular the codimension-two metric obstruction recorded in
ATTEMPTS/066 is not removed by an algebraic bundle decomposition.

**Separate critical audit, 2026-10-15 (step 304).** This audit uses the
prior SPECIALIZE scope in
`drafts/literature/2026-10-15-equality-algebraic-defect-budget-critical-audit.md`.
It finds and repairs a substantive sign error in (2) and (8). The
previous version wrote [E]=[A]+[Q] but then substituted -[Q]; it also
reversed the hypothetical torsion sign. The corrected formulas above
follow from the actual short exact sequences. The splitting survives.
The following checks concern the stated conditional family only.

First, L097 gives an algebraic locally free family on the projective
product and a finite possibly empty closed complement of U. Thus p is
proper, flat and finitely presented and V is perfect; 0B91 applies to
the actual coefficient. Stable-fibre trace-free H^0 and H^2 vanish by
simplicity and Serre duality, and RR gives h^1=50. This justifies
concentration only on U. Since multiplication by each nonzero base
function remains injective on V, its pushforward A_0 is torsion-free;
its generic vanishing therefore proves A_0=0. Coherence and relative
dimension two leave only A_1 and the finite-length A_2. No assertion
about ordinary base change at a split point is needed.

At each omitted point the derived residue-field cohomology lies in
degrees zero through two. The minimal free representative supplied by
0BCC/0BCD therefore has exactly the permissible degrees in (3), even
when the degree-zero derived fibre is nonzero. Ordinary H^0(C)=0,
rather than a fibre vanishing, makes d^0 injective. For a putative
torsion class, the preimage of its representative v exists locally on
the puncture because its cohomology class is zero there. Injectivity
makes these preimages agree on overlaps. The free source has depth two,
so 0E9I extends that same preimage; the equality d^0 a=v then extends
in the free target by injectivity of restriction. This checks the
load-bearing preimage step and proves that no torsion correction remains.
The locally free hull and finite-length Q follow without identifying
either length with a derived Betti number.

Next, the relative KS, cup and trace maps are algebraic maps for F.
Trace-free degree-one cohomology is the entire tangent space since
H^1(O_{S_1})=0. In the local stable-family comparison, scalar
conjugation and a base-line twist cancel in End_0 and its cup/trace
maps; on relative degree-one tangent classes a base-line twist has no
fibre deformation. The comparisons therefore descend through the
local Quot charts. They do not require a global universal sheaf.
The same-extension comparison in L100 identifies these KS classes
with the mixed-curvature representatives of L095, with no factor from
passing between real harmonic and complex Dolbeault tangent vectors.

For base vectors partial_i,partial_j the ordered mixed terms in
Tr(R^2) contribute -2Tr(a_i wedge a_j). A pure base or pure fibre
term cannot have the required base type (2,0), fibre type (0,2),
because R is of total type (1,1). The factor 2 cancels the Chern
character factorial. Thus (4) pulls back to minus the actual curvature
integral, whose value on the whole compact B is -2lambda sigma_B
by L095 (8)--(9). Restricting this identity gives (5); it is not an
inference from cohomology on U. The nonzero constant and nowhere-zero
sigma_B make omega_T invertible. Consequently pi kappa=id by
nondegeneracy, and the algebraic projector has the asserted kernel.
Under L100's harmonic comparison, the Serre form is the fixed scalar
normalization of the holomorphic symplectic form of the L2 structure;
scalar normalization does not change its orthogonal complement.
The quaternionic tangent image therefore has the same symplectic and
metric normal complement on U.

For extension, the omitted points have ambient depth two, and both
E and T_B are reflexive bundles on the regular surface. Apply 0EBJ to
both maps, not merely to their images. Their retraction identity
extends uniquely, so the kernel is a bundle direct summand of rank 48.
Applying full faithfulness to the pairing and its inverse proves
nondegeneracy at Z as well as on U. Its restrictions to the orthogonal
summands remain nondegenerate, and their top wedge forms trivialize
their determinants integrally. No inverse metric, metric bound or
semistability assertion is furnished by this algebraic argument.

Finally, the independent numerical check gives beta^2=588+156=744,
ch_4(F)=744/12=62 and ch_4(V)=4(62)+744=992. The fibre Todd term
gives rank 6-56=-50 and point coefficient 992-168=824, with no
degree-two contribution. The two HRR checks both give 724. These
virtual computations in the original proof were correct. The error
occurs only when passing from the virtual class to the actual hull:

\[
 0\longrightarrow A_1\longrightarrow E\longrightarrow Q
       \longrightarrow0,
 \qquad [E]=-[C]+[A_2]+[Q].
\]

Hence ch_2(E)=-824+w+q, ch_2(N)=-800+w+q and
c_2(N)=800-w-q in units of eta. As a separate additivity check,
chi(A_1)=-724+w and chi(E)=chi(A_1)+q=-724+w+q,
which equals 2(50)-824+w+q. The previously printed negative Q
contribution fails this exact-sequence check. With hypothetical
torsion T, passing from A_1 to A_1/T subtracts [T], as in corrected
(8). In the actual situation T=0, so w and q have the same sign.

When Z is empty, both corrections vanish and c_2(N)=800 eta.
In general their nonnegativity only gives the numerical upper bound
c_2(N)/eta<=800; it gives no lower bound, no computed defect and no
contradiction. In particular no positivity of c_2(N) is available
without further hypotheses. This audit is an ADVANCE / REPRODUCTION
because it repairs a real error in an essential budget; it claims
no progress beyond the checked general tools. Unknown local lengths,
kernel existence and transport remain unresolved, and the parked
metric inference in ATTEMPTS/066 remains parked.

## Mathlib

Full coverage of this actual-family algebraic relative-Ext splitting,
surface reflexive extension and defect specialization: **not checked**.
No matching theorem or absence is asserted. The precise primary
algebraic inputs above are imported; the family-specific application
and numbers are a REPRODUCTION under the approved assessment.
The separate critical audit above corrects the point-defect signs.
Algebraic extension and conditional sheaf bookkeeping do not prove F exists or resolve the
rational Hodge conjecture.
