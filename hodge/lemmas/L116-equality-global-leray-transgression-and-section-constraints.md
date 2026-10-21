# L116 — Actual global Leray differential and normal-section constraints

## Hypotheses

Retain the entire conditional equality family of L108/L109/L111/L115.
Thus p:S_1 x B -> B projects the identical marked projective K3
surfaces with their original common hyperkähler metric and full negative
mixed tensor. The hypothetical locally free rank-two F is polystable
at the real product polarization, has integral c_1(F)=0 and

\[
 \operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D.
\]

Put V=End_0(F), C=Rp_*V, M=R^1p_*V and W=R^2p_*V. Use the actual
normalized cup/trace adjoint of L109 and the actual truncation maps,
not an arbitrarily chosen complex with the same cohomology. L108/L111
give H^0(C)=0, M=E locally free of rank fifty, and the extended
nondegenerate alternating Serre form b:M -> M^vee. The sheaf W has
length one at each point of the finite, possibly empty split set Z.
Write s=|Z|. Retain L108's specific splitting M=T_B direct sum N,
with rank(N)=48, determinant O_B and a perfect alternating form.
L111 gives c_2(N)=(800-s)eta, with integral_B eta=1. L115 makes this
same N slope-polystable of slope zero at the original real Kähler
class and gives 0<=s<=800.

Neither F, a point of Z, acyclicity, strict normal stability nor a
section multiplicity is assumed. Fix the nonzero holomorphic K3
forms when trivializing the canonical bundles in duality.

## Conclusion

The actual truncation triangle splits globally in D^b_coh(B):

\[
 M[-1]\xrightarrow{j}C\xrightarrow{a}W[-2]
      \xrightarrow{k}M,\qquad k=0,
 \qquad C\simeq M[-1]\oplus W[-2].                       \tag{1}
\]

The isomorphism can respect the displayed inclusion and projection;
no uniqueness of its choice is needed. In particular the actual coherent
Leray differential and its global Serre adjoint are zero:

\[
 d_2^{0,2}:H^0(B,W)\longrightarrow H^2(B,M),
                    \qquad d_2^{0,2}=0.                  \tag{2}
\]

The target space H^2(B,M) need not vanish. Its adjoint is the zero
map H^0(B,M^vee) -> H^0(B,W)^*.
It is distinct from L109's local isomorphism gamma:W^dagger -> W.

With t=h^0(B,N), the complete resulting dimensions are

\[
 \begin{aligned}
 h^0(X,V)&=h^4(X,V)=0,\\
 h^1(X,V)&=h^3(X,V)=t,\\
 h^2(X,V)&=724+2t,\\
 h^1(B,N)&=704-s+2t.                                    \tag{3}
 \end{aligned}
\]

Polystability implies that t is the multiplicity of the full trivial
direct summand of N. Consequently 0<=t<=48, t!=47, and t=48 forces
s=800. Equations (3) exclude s=797,798,799 and sharpen the conditional
cardinality constraint to

\[
                    s\in\{0,1,\ldots,796\}\cup\{800\}.  \tag{4}
\]

At s=800 these constraints force N=O_B^48, t=48 and h^1(N)=0;
they do not exclude that possibility. For every integer 0<=s<=796
the displayed rank, character and cohomology constraints have a formal
compatible assignment described below. Such assignments assert no
bundle or kernel existence. The upper bound itself remains 800.

This is a conditional local ADVANCE / REPRODUCTION of the assessed
known tools. The separate critical audit below preserves the result,
with outcome EXPLORATION / REPRODUCTION and no substantive error or
stronger conclusion found. It identifies an actual
global map and excludes three cardinalities, rather than producing a
new cycle or progress beyond the inspected general theorems. It supplies
no F, transport, reconstruction or universal primitive Hodge realization.

## Proof

**Imported framework and its specialization.** Use the prior SPECIALIZE
assessment `drafts/literature/2026-10-17-equality-global-leray-transgression.md`.
Import coherent Leray and derived-global-section comparison from
[Stacks 20.13.1--4, 01EY](https://stacks.math.columbia.edu/tag/01EY),
the canonical truncation triangle from
[13.12.4, 08J5](https://stacks.math.columbia.edu/tag/08J5), and the
spectral-sequence construction and differential conventions from
[13.22.2, 015N](https://stacks.math.columbia.edu/tag/015N),
[13.21.3, 015J](https://stacks.math.columbia.edu/tag/015J) and
[12.24, 012K](https://stacks.math.columbia.edu/tag/012K).
Here p is a morphism of ringed spaces, V is in degree zero, and C is
perfect and bounded with only its stated degree-one and degree-two
cohomology. These are the applicable coherent hypotheses; smooth
properness alone is not a degeneration theorem with coefficient V.

Use the actual derived relative trace adjoint of L109. Its global
construction is the smooth-proper relative duality theorem
[48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT), together with
the perfect-pairing pushforward and actual cup/evaluation map in
[48.12.6, 0G81](https://stacks.math.columbia.edu/tag/0G81).
The coefficient V is locally free and its trace form is perfect in
characteristic zero. The chosen fibre form trivializes omega_{X/B}.
Thus the construction is global before taking the stalks used in L109.
Use triangle-compatible global Serre duality, including the evaluation
and trace description, from
[48.27.1--4,6, 0FVU](https://stacks.math.columbia.edu/tag/0FVU) and
[0FVV](https://stacks.math.columbia.edu/tag/0FVV).
B and X are smooth projective over C, their canonical bundles have
the fixed trivializations, and all complexes used are bounded coherent
and perfect. L109's finite-length local duality applies to W without
ordinary local freeness of W. These general results are imported,
not reproved. The work is to compare their actual arrows for this family.

**A retraction from the actual trace adjoint.** Write D=RHom_B(-,O_B).
L109's normalization gives the global adjoint isomorphism

\[
                    \alpha:C[2]\xrightarrow{\sim}DC.
\]

Because M is locally free, D(M[-1])=M^vee[1]. Therefore the specific
map j in (1) has a dual Dj:DC -> M^vee[1]. Form

\[
 f=(Dj)[-2]\circ\alpha[-2]:C\longrightarrow M^vee[-1].    \tag{5}
\]

The composite fj is a morphism M[-1] -> M^vee[-1], hence a genuine
sheaf morphism shifted by -1: there are no extra derived components
in this Hom group. It is exactly b[-1]. To check the global
identification, on U=B minus Z it is the adjoint of the actual
degree-one Serre form, with the normalization fixed in L109. L108's
extended form b has that same restriction. Two maps between these
locally free sheaves which agree on dense U agree on B. Equivalently,
L109 identifies this composite at every stalk with the canonical hull
inclusion followed by the extended form; L111 makes that inclusion
an isomorphism. Neither comparison chooses a new self-duality.

Since b is invertible, the actual map

\[
                  r=b^{-1}[-1]\circ f:C\longrightarrow M[-1]
\]

satisfies rj=id. The consecutive arrows in the truncation triangle
give j[1]k=0. Applying r[1] and using r[1]j[1]=id gives k=0.
The split-triangle criterion now gives (1), respecting j and a.
This establishes global splitting using actual morphisms. No gluing
of arbitrarily chosen local decompositions, ordinary base change at a
split point, or vanishing of a locally invisible extension is assumed.

**The global boundary and its adjoint.** Apply RΓ(B,-) to (1).
The boundary H^0(W) -> H^2(M) is induced by k. In the canonical
truncation construction of coherent Leray it is d_2^{0,2}, up to
the common choice of boundary sign. This comparison can also be read
from its low-degree exact sequence: H^2(X,V) maps to H^0(W), with
boundary to H^2(M), followed by H^3(X,V). The standard construction
cited above identifies this very boundary, not an arbitrary map of
those spaces. Since k=0, both sign conventions give d_2^{0,2}=0.

For clarity the dual comparison is also made on the actual arrows.
Finite-length duality gives DW=W^dagger[-2], where
W^dagger=Ext^2_{O_B}(W,O_B) as a sheaf. Dualizing k gives

\[
           Dk:M^vee\longrightarrow D(W[-2])=W^dagger.    \tag{6}
\]

This is the dual-truncation connecting map denoted delta in L109,
up to the triangle sign. It vanishes there because b is an
isomorphism, and also vanishes by (1). With omega_B trivialized,
global Serre duality identifies H^2(M)^* with H^0(M^vee) and
H^0(W)^* with Ext^2_B(W,O_B)=H^0(W^dagger). The last equality uses
the concentration of DW just specified; finite support has no higher
cohomology. Evaluation followed by trace, compatibly with triangles,
identifies the transpose of the boundary with H^0(Dk), up to the
same harmless boundary sign. This proves the adjoint assertion.
By contrast gamma is H^0(alpha^{-1}Dt) in L109's stalkwise dual
triangle (where its t is the projection a here); gamma is an
isomorphism by L111. It is neither (2) nor (6).

**Full cohomology bookkeeping.** The only nonzero rows of coherent
Leray are H^a(M) in row one and H^0(W) in row two. Higher cohomology
of W vanishes by finite support; cohomology on the surface B vanishes
above degree two. Thus there is no other possible nonzero differential.
In fact (1) already gives

\[
 \begin{aligned}
 H^1(X,V)&\simeq H^0(B,M),\\
 H^2(X,V)&\simeq H^1(B,M)\oplus H^0(B,W),\\
 H^3(X,V)&\simeq H^2(B,M),
 \end{aligned}                                           \tag{7}
\]

and zero cohomology in degrees zero and four. The direct-sum
identification need not be canonical. Here dim H^0(W)=s, by L111's
actual length-one computation.

On a K3 surface h^0(T_B)=h^2(T_B)=0: contraction with its nonzero
two-form identifies T_B with Ω_B^1, and h^{1,0}(B)=0, together with
Serre duality, gives both vanishings. Its character 2-24eta gives
chi(T_B)=-20 and h^1(T_B)=20. L108/L111 give

\[
 \chi(M)=100-824+s=s-724,\qquad
 \chi(N)=96-800+s=s-704.
\]

The perfect forms identify M with M^vee and N with N^vee. Hence
Serre duality gives h^2(M)=h^0(M)=t and h^2(N)=h^0(N)=t.
Consequently h^1(M)=724-s+2t and h^1(N)=704-s+2t.
Substitution into (7) proves (3). In particular chi(X,V)=724
as in L108, and fourfold Serre duality also matches h^1 with h^3.
No inference that either M or N has no sections has been made.

**What polystability adds without prescribing t.** Decompose the
polystable N into its slope-zero stable locally free factors. They
are locally free because each is a direct summand of a vector bundle.
A stable factor A of rank greater than one has no nonzero section:
the saturated image of O_B from a section is a rank-one torsion-free
subsheaf whose first class is that of an effective divisor, of
nonnegative degree for the real Kähler form. This contradicts strict
slope stability at slope zero. A rank-one factor is a line bundle;
a nonzero section has an effective zero divisor of degree zero, hence
has no zero divisor because every nonzero effective divisor has
positive Kähler degree. That line bundle is O_B. This is the elementary
stable-section consequence at the real class used here; it needs no
new existence or stability theorem and no rational polarization change.
It is the same section-count issue retained in ATTEMPTS/047, now with
an explicit unknown multiplicity rather than an assumed value.

It follows that

\[
               N\simeq O_B^t\oplus A,\qquad H^0(B,A)=0,
               \qquad\operatorname{rk}(A)=48-t.          \tag{8}
\]

Thus t<=48. If t=47, A is a line bundle with
det(A)=det(N)=O_B, contradicting H^0(A)=0. If t=48, N is trivial,
so c_2(N)=0 and s=800. Nonnegativity in (3) gives

\[
                         s\le704+2t.                    \tag{9}
\]

For s=797,798,799, (9) requires t>=47. Both possible values 47
and 48 are ruled out for those s by (8). This proves (4).
For s=800, (9) requires t=48, and the values of (3) are compatible:
h^1(N)=0, h^1(M)=20, and h^2(X,V)=820. In particular (9) cannot
lower the overall upper bound below 800.

For a precise limit on this bounded test, for any 0<=s<=796 assign
t=46 and a formal determinant-trivial rank-two residual A with
c_2(A)=(800-s)eta, h^0(A)=h^2(A)=0 and h^1(A)=796-s.
Its surface Euler identity is chi(A)=4-(800-s)=s-796, as required.
Taking a formal O_B^46 summand satisfies (8), the alternating-form
rank condition and every displayed dimension/character equation.
These are formal compatible assignments only. They do not claim an
actual stable residual at the original h, identify the actual t, or
realize the actual relative complex of F. Likewise the compatible
s=800 assignment does not construct F. The kernel and universal
Hodge gaps persist. Park the global differential/section-number
mechanism here: a further exclusion of the remaining cases needs an
independently tested constraint on the actual normal bundle or family,
not another evaluation of this now zero differential. Preserve
ATTEMPTS/047/063/066/067 and all their scoped failure evidence.

**Separate critical audit (2026-10-17).** This checks the exact prior
SPECIALIZE target in
`drafts/literature/2026-10-17-equality-global-leray-critical-audit.md`.
The direct inputs remain L108, L109, L111 and L115; their hypotheses,
including the hypothetical F, original metrics, full negative tensor
and possibly empty Z, are retained. Their conclusions are inputs to
this bounded audit, not claims re-established for arbitrary families.
General truncation and duality theorems cited above are imported.
For the surface numerical inputs use Huybrechts, *Lectures on K3
Surfaces*, Chapter 1, (2.6), and Hartshorne, *Algebraic Geometry*,
III, Theorem 7.6, with the fixed trivialization of the canonical line.

First check the actual global retraction. Under cohomological shifts,
H^i(K[a])=H^{i+a}(K). Thus alpha[-2] has target (DC)[-2],
and (Dj)[-2] has target M^vee[-1]. Their composite f has precisely
the source and target in (5). Moreover
Hom_D(M[-1],M^vee[-1])=Hom_B(M,M^vee); the composite fj cannot
contain an additional higher-Ext component invisible on U. On U,
L109's fixed flat-map convention v -> (u -> omega_E(v,u)) and
L108's fixed scalar normalization identify it with b[-1]. The
difference is a sheaf map between locally free sheaves, zero on dense
U of the integral B, and is therefore zero globally. Invertibility of
b now gives the actual left inverse r, before any decomposition of C
is chosen. Applying r[1] to j[1]k=0 proves k=0 in the global derived
category. This is stronger than checking that each local truncation
class vanishes: locally split extensions need not in general glue.
Here the single global trace construction supplies the needed gluing.

Second check the boundary and transpose. The only cohomology rows of
C are one and two. The truncation boundary on derived global sections
is H^0(W) -> H^2(M); its placement is exactly bidegree (2,-1) in
coherent Leray, and the cited truncation construction identifies it
with d_2, up to sign. Finite support kills H^a(W) for a>0; the
surface dimension kills H^a(M) for a>2. There is no other possible
nonzero differential. Duality gives
D(W[-2])=(DW)[2]=W^dagger, so Dk is a genuine morphism
M^vee -> W^dagger. No ordinary dual Hom(W,O_B) is being substituted
for the finite-length dual.

The global transpose can also be tested directly on a section
w:O_B -> W and q:M -> O_B. The Serre pairing of the boundary of w
with q is the trace of the degree-two composite

\[
 O_B\xrightarrow{w}W\xrightarrow{k[2]}M[2]
                        \xrightarrow{q[2]}O_B[2].
\]

By evaluation-duality functoriality this is the Serre pairing of w
with the class H^0(Dk)(q) in Ext^2_B(W,O_B), with the same possible
boundary sign. The local-to-global Ext identification here is valid:
DW has only the sheaf Ext^2 term, so Ext^2_B(W,O_B)=H^0(W^dagger).
This verifies both domains and the actual adjoint, which is zero.
The neighboring arrow gamma in L109's dual triangle instead maps
W^dagger to W; its isomorphism when M=E is fully consistent with
Dk=0. In particular no local isomorphism has been declared zero.

Third check every numerical term. The K3 Todd class is 1+2eta, so
ch(M)=50+(-824+s)eta gives chi(M)=s-724; subtracting
ch(T_B)=2-24eta gives chi(N)=s-704. The tangent bundle contributes
(0,20,0). The symplectic self-dualities and Serre duality give t in
both endpoint degrees of N and M, hence h^1(M)=724-s+2t and
h^1(N)=704-s+2t. The additional length-s summand contributes only
to H^2(X,V), giving 724+2t, not 724-s+2t. The alternating total
is -t+(724+2t)-t=724, agreeing with L108. Degrees zero and four
vanish; no assertion of acyclicity occurs.

Finally check that t counts all trivial factors. Each stable summand
of the actual polystable vector bundle N is locally free. For a
summand of rank greater than one even the nonsaturated injection
O_B -> A from a nonzero section has slope zero and smaller positive
rank, contradicting stability; saturation only strengthens this test.
For a line summand the zero divisor of a nonzero section has Kähler
degree zero, so is empty and trivializes the line. This uses positivity
for effective divisors at the actual real Kähler class. It imports none
of the unqualified printed slope-Hom assertions excluded by the source
assessment. The full sum of trivial stable factors therefore has rank
t, with section-free complementary bundle A. At t=47, its rank-one
complement has determinant O_B and hence a section, a contradiction.
At t=48, c_2(N)=0 forces s=800.

For each s=797,798,799 the lower bound
ceil((s-704)/2) on t is respectively 47,47,48. The first two
allow only t=47 or 48, and the last only 48; the preceding determinant
and Chern checks exclude each case. At s=800 the sole possible value
is t=48 and the dimensions are consistent. For 0<=s<=796 the stated
formal t=46 assignment has residual rank two, determinant O_B,
charge 800-s>=4 and h^1=796-s>=0. Its total normal middle
cohomology equals 704-s+92=796-s. The ranks allow alternating forms;
no odd-rank residual is being smuggled into the compatibility claim.
These are only the displayed formal constraints, not realizations of
stable bundles, the actual relative complex or a common F.

The audit therefore finds no substantive error or stronger exclusion.
It is EXPLORATION / REPRODUCTION, not a second ADVANCE for the original
specialization and not progress beyond the inspected general tools.
ATTEMPTS/068's bounded mechanism remains parked. No actual value of t,
F existence or nonexistence, new cycle, transverse transport or universal
primitive Hodge realization is established.

## Mathlib

Full matching Mathlib coverage for the actual-family derived retraction,
global boundary/Serre comparison and normal-section specialization has
not been checked. The precise primary inputs are cited above; unknown
coverage is not absence. This is an informal specialization of known
derived, duality and stability tools, not a formal verification or a
novelty claim. The separate audit preserves the conditional notebook conclusions
and the unchanged Mathlib coverage status. Neither the original result
nor this audit gives a complete candidate for the Hodge conjecture.
