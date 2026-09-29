# L022 — Direct-summand recovery for all positive complete-intersection degrees

## Hypotheses

Retain the very general cubic family, X=S x S, reduced correspondence
support C, and marked NS-fixed tangent spaces V_N, V_RM and V_D of
L008. Thus dim V_RM=4 and dim V_D=3. Put I=I_C. Fix the original ample
line bundle L on S and H=p_1^*L tensor p_2^*L, and write Q(k)=Q tensor
H^k. Let A=C[epsilon]/(epsilon^2) and let X_A=S_A x_A S_A be the
product deformation in a direction kappa in V_N. NS-fixedness extends
H to H_A.

Let m,n>0, with no ordering imposed, and put

\[
F=I(-m),\qquad G=O_X(-n),\qquad E=F\oplus G.
\]

For the union assertion choose f in H^0(X,I(n)) and
g in H^0(X,O_X(m)), with (f,g) a regular sequence defining a smooth
surface B and g a nonzerodivisor on O_C, as in L018. Put Y=C union B
scheme-theoretically and J=I_Y. These are conditional admissibility
hypotheses; existence for every positive pair is not asserted. L018
already supplies actual smooth examples in sufficiently high degrees.

## Conclusion

1. Any A-flat coherent lift E_A of E implies the existence of an
   A-flat coherent lift of I, and hence an embedded flat lift of C
   in X_A. Neither the central inclusion G -> E nor the decomposition
   of E is required to lift inside that particular E_A.
2. Every flat embedded first-order lift of the admissible Y gives
   such an E_A. Consequently its lifting locus in V_N is contained
   in V_D for **every m,n>0**, including m=n and m<n. In particular
   no direction in V_RM outside V_D admits a lift of Y.
3. If additionally H^1(X,I(n))=0, then Y lifts if and only if C lifts.
   Its lifting locus is then exactly V_D. Without this extra
   hypothesis only the containment is asserted.

The cycle identity [Y]=[C]+mn c_1(H)^2 and action U on T(S) from
L018 remain valid. Thus the unrestricted positive-degree exclusion
still permits at most three of the four required RM directions;
under the converse hypothesis it permits exactly three. It does not
extend the 21-dimensional algebraic span to a transverse surface or
resolve the universal rational Hodge conjecture. It makes no claim
about ramified higher-order lifts or other representatives.

## Proof

**The imported obstruction criterion.** Use Huybrechts--Thomas,
*Deformation-obstruction theory for complexes via Atiyah and
Kodaira--Spencer classes*,
[arXiv:0805.3527v2 (15 September 2013), Corollary 3.4, p. 14](https://arxiv.org/pdf/0805.3527v2#page=14),
in its absolute setting over C. The
[2014 erratum, pp. 561--562](https://link.springer.com/content/pdf/10.1007/s00208-013-0999-x.pdf#page=1)
retains that setting; the relative flatness correction is incorporated
in v2. For a perfect P on X, the full obstruction

\[
o_P=(\mathrm{id}_P\otimes\kappa_X)\circ\operatorname{At}(P)
\in\operatorname{Ext}^2_X(P,P)
\tag{1}
\]

vanishes exactly when P has a perfect lift on X_A with derived central
restriction P. Here the square-zero ideal is identified with O_X.
The smooth central X allows the usual Atiyah class with values in
Omega_X^1. Definition 2.6, Theorem 2.10 and equation (3.6) of the same
version construct (1) from a universal kernel morphism. In particular
it is natural in P. This is the full Ext obstruction, before taking
any trace or Chern-character image.

All ambient hypotheses hold. X is smooth projective and X_A is
projective over A since H_A is ample. An embedding in P^N_A followed
by P^N_A -> P^N_C x A^1_C embeds X_A in a smooth complex scheme.
I is perfect even at its three double points: L012 gives local
projective dimension at most two. Thus F, G and E are perfect.
No simplicity or lci hypothesis on C is used.

**A given flat lift is a perfect lift.** Work locally with
R_A=O_(X_A), R=R_A/(epsilon). Flatness of X_A over A gives, for any
complex K of R_A-modules,

\[
K\otimes^{\mathbf L}_{R_A}R
\simeq K\otimes^{\mathbf L}_A\mathbb C.
\tag{2}
\]

For the given A-flat E_A, (2) is its ordinary central fibre E in
degree zero. Since E is perfect over R, nilpotent reduction detects
perfectness by [Stacks Lemma 15.80.4, tag 07LU](https://stacks.math.columbia.edu/tag/07LU).
Applying it to R_A -> R makes E_A perfect locally, hence perfect on
X_A. It is therefore a lift in the sense of the cited criterion,
and o_E=0.

Let a:F -> E and b:E -> F be the central inclusion and retraction,
so ba=id_F. Naturality gives o_E a=a[2] o_F. Consequently

\[
o_F=b[2]\,o_E\,a=0.
\tag{3}
\]

The maps a and b occur only on X. Equation (3) makes no assertion
that they extend to maps involving the specified E_A. By the same
criterion there is some perfect P_A on X_A with Li^*P_A=F.

**The recovered complex is a flat coherent sheaf.** Applying (2)
to P_A gives P_A tensor^L_A C=F, a complex in degree zero. Over the
field C this has Tor amplitude [0,0].
[Stacks Lemma 15.68.20, tag 0H75](https://stacks.math.columbia.edu/tag/0H75)
detects that same amplitude over the nilpotent surjection A -> C.
[Stacks Lemma 15.68.3, tag 0654](https://stacks.math.columbia.edu/tag/0654)
then says P_A is represented by an A-flat module in degree zero.
These statements apply on each affine chart; the cohomology sheaf
P_A^0=H^0(P_A) is consequently A-flat and all its other cohomology
sheaves vanish. P_A^0 is coherent because P_A is perfect on the
noetherian X_A. Thus Q_A=P_A^0 tensor H_A^m is an A-flat coherent
sheaf with central fibre I.

In this argument perfectness is a property over R_A, while the
[0,0] amplitude is over A. No [0,0] amplitude over R_A is claimed:
the singular ideal I is not locally free on X.

**From the abstract ideal lift to an embedded lift.** Apply the
ideal-reconstruction argument of L012 to Q_A. Its hypotheses depend
on I and X_A, not on a chosen resolution map or summand inclusion.
For completeness, Q_A is perfect, so has a determinant line D_A.
On U_A with underlying open U=X minus C it is a line bundle, because
it is A-flat with rank-one locally free central fibre. There it is
canonically identified with D_A. The central determinant is
det(I)=O_X, with the trivialization specified off C. The equality
H^1(X,O_X)=0 implies Pic(X_A) -> Pic(X) is injective, so D_A has a
trivialization compatible with that central one.

For u:U_A -> X_A, L012's two-layer Hartogs argument gives
u_*O_(U_A)=O_(X_A): on a smooth affine chart the ambient deformation
is trivial and ordinary Hartogs applies to both O_X summands across
the codimension-two C. Adjunction therefore gives

\[
Q_A\longrightarrow u_*(Q_A|_{U_A})
\simeq O_{X_A}.
\tag{4}
\]

Its reduction is I -> O_X, since the maps agree on U and O_X is
torsion-free. A map between A-flat modules with injective reduction
is injective with A-flat cokernel, as proved in L012. Hence (4)
defines an embedded flat C_A, including at all three singular
points. This proves the first assertion.

**The union recovers the middle sheaf for arbitrary positive degrees.**
The ideal identity and full basic-double-link sequence verified in
L018 use only the regular sequence and nonzerodivisor hypotheses:

\[
J=(f)+gI,\qquad
0\longrightarrow M=O_X(-m-n)
\xrightarrow{a\mapsto(-af,ag)} E
\xrightarrow{(v,w)\mapsto gv+fw}J\longrightarrow0.
\tag{5}
\]

They hold at every point, including the non-Cohen--Macaulay points
of C. No degree inequality occurs in this ideal calculation.
L019 gives H^1(C,O_C(n))=0 for every positive n and this fixed H.
Kodaira vanishing, Kunneth and the ideal sequence, as in L018, give

\[
H^2(X,I(n))=0,\qquad H^2(X,O_X(m))=0,
\qquad H^3(X,O_X)=0.
\]

Twisting (5) by m+n then gives H^2(X,J(m+n))=0. Serre duality on
the smooth fourfold with omega_X=O_X yields

\[
\operatorname{Ext}^2_X(J,M)
\simeq H^2(X,J(m+n))^*=0.
\tag{6}
\]

This calculation requires positive m and n, with no comparison
between them. It uses the support vanishing from L019, not the
potentially nonzero group H^1(X,I(n-m)).

Now let J_A be the ideal of any embedded flat Y_A and put
M_A=H_A^(-m-n). Both are A-flat. For the closed immersion
i:X -> X_A, equation (2) gives Li^*J_A=J. Derived adjunction thus
identifies Ext^q_(X_A)(J_A,i_*M) with Ext^q_X(J,M). Applying
RHom_(X_A)(J_A,-) to
0 -> i_*M -> M_A -> i_*M -> 0 gives the exact segment

\[
\operatorname{Ext}^1_{X_A}(J_A,M_A)
\longrightarrow\operatorname{Ext}^1_X(J,M)
\longrightarrow\operatorname{Ext}^2_X(J,M)=0.
\tag{7}
\]

The first map is reduction of extensions under these identifications:
extension middle terms are A-flat because both ends are A-flat,
so derived and ordinary restriction agree. In particular the class
of (5) lifts to an exact sequence

\[
0\longrightarrow M_A\longrightarrow E_A
\longrightarrow J_A\longrightarrow0
\tag{8}
\]

with A-flat E_A and reduction E. The first assertion now recovers
C_A. L008 forces kappa into V_D. This proves the all-positive-degree
containment, without choosing a summand map in (8).

**The separate converse.** If H^1(X,I(n))=0 and C_A exists, f lifts
to a section of I_(C_A) tensor H_A^n. Kodaira vanishing lifts g to
H_A^m. The construction in L018 then gives the flat ideal
(f_A)+g_A I_(C_A) with central ideal J. Its flatness proof uses the
lifted two arrows of (5), injective reduction, and A-flat cokernels;
none uses m>n. Hence the converse extends to every positive pair
under the stated extra vanishing. L008 identifies the resulting
lifting locus with V_D. The cycle computation in L018 also uses
only the complete-intersection degrees and absence of a common
surface component, so [Y]=[C]+mn c_1(H)^2 and its action remains U.

**Effect on the previous cohomology tests and scope.** L020 and L021
are unchanged. A nonzero H^1(X,I(n-m)) can prevent the sufficient
vanishing test for extending a specified summand inclusion; it
cannot evade the existence argument (3). Thus further classification
of that group for L.F>=4 is unnecessary for this first-order union
exclusion. A nonzero H^1(X,I(n)) still leaves the particular
containing section f's lift undecided and does not imply the
converse fails.

This is a reproduction and application of standard obstruction
naturality and the reviewed perfectness/flatness criteria. The
all-positive-degree conclusion checks their applicability in this
geometry and strengthens the notebook's exclusion. No originality
is claimed; the saved review did not identify a source stating
the full specialized union assertion. Neither (3) nor (8) lifts a
chosen central splitting to a specified first-order deformation.
They therefore do not settle a further extension with prescribed
nonconstant first-order data, as can occur after ramification.

## Mathlib

Coverage of the full statement and supporting obstruction/perfectness
results: **not checked**. No full matching Mathlib theorem, supporting
Mathlib identifier, or absence from checked Mathlib sources is
asserted. The linked Huybrechts--Thomas Corollary 3.4, its universal
construction and erratum, and Stacks tags 07LU, 0H75 and 0654 are
supporting named results, not matches for the full union statement.
Kodaira vanishing, Kunneth, Serre duality and derived adjunction are
standard inputs already used in L018; ideal reconstruction is the
argument from L012 with its hypotheses checked above. The distinction
between some flat sheaf lift and a specified inclusion is essential.
