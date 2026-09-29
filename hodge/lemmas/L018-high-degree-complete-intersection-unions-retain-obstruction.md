# L018 — High-degree complete-intersection unions retain the cubic obstruction

## Hypotheses

Let S, X=S x S, C, V_N, V_RM and V_D satisfy L008. Thus C is the reduced
cubic correspondence support, with precisely three transverse surface
double points. Fix an ample line bundle L on S and put
H=p_1^*L tensor p_2^*L. Write F(k)=F tensor H^k, I=I_C, and h=c_1(H).
Work over A=C[epsilon]/(epsilon^2), with the same NS-fixed deformation
S_A in both factors of X_A. In particular H extends to H_A.

Choose integers m>n>0 and sections

\[
f\in H^0(X,I(n)),\qquad g\in H^0(X,O_X(m)).
\]

Assume (f,g) is a regular sequence defining a smooth surface B, and g
is a nonzerodivisor on O_C. Set Y=C union B scheme-theoretically and
J=I_Y. For the recovery assertion assume

\[
H^1(C,O_C(n))=0.                                      \tag{1}
\]

For the equality of lifting loci assume in addition

\[
H^1(X,I(n))=0.                                       \tag{2}
\]

These hypotheses do not require V(f) to be smooth. They hold for
admissible choices with n sufficiently large and then m sufficiently
large relative to n, as proved below. No effective value of the degree
threshold is claimed.

## Conclusion

Under (1), every flat embedded first-order lift of Y in X_A yields a
flat embedded lift of C. The lift of Y need not preserve either
component, either defining section, or the basic-double-link extension.
It follows that Y has no embedded lift along any
kappa in V_RM outside V_D.

Under (1) and (2) one has the equivalence

\[
Y\text{ lifts in }X_A\quad\Longleftrightarrow\quad
C\text{ lifts in }X_A.
\tag{3}
\]

Consequently the first-order ideal-gluing obstruction for Y has kernel
V_D on V_N, and its kernel on V_RM has dimension three and rank one,
against four RM tangent directions required. Its cycle class satisfies

\[
[Y]=[C]+mn h^2,
\tag{4}
\]

so its transcendental correspondence action is still U.

This rules out the sufficiently high-degree regime of the saved
complete-intersection target, and more generally every admissible n
satisfying (1). It does not decide whether a smaller n with
H^1(C,O_C(n)) nonzero admits a transverse lift. The original existential
target, the extension to transverse surfaces, and the universal rational
Hodge conjecture remain unresolved.

## Proof

**Admissible smooth added surfaces exist in high degrees.** Serre global
generation and vanishing allow n to be chosen so that I(n) is globally
generated and H^i(X,I(n))=0 for i>0. Increase the threshold to apply
[Stacks Lemma 33.47.1, tag 0FD5](https://stacks.math.columbia.edu/tag/0FD5):
the sections vanishing on C define an immersion away from C. A general
f consequently gives a divisor Q=V(f) smooth away from C, by
[Stacks Lemma 33.47.3, tag 0FD6](https://stacks.math.columbia.edu/tag/0FD6).
These are the Bertini inputs already inspected in the saved assessment.

Along C_sm the conormal bundle I/I^2 has rank two. Global generation
of I(n) makes evaluation onto its fibre surjective at each point. For
fixed p in this smooth surface, df(p)=0 imposes two independent linear
conditions on f. The incidence of these zero values therefore has
dimension equal to that of the section parameter space. The fibre
dimension theorem shows that its fibre over a general section has
dimension at most zero (or is empty). Thus Q has only finitely many
singular points on C_sm. Its remaining possible singular points are
the three old double points of C; f has zero differential at them
because their ideals lie in the squares of the ambient maximal ideals,
by L007. In particular this argument has not asserted that Q is smooth.

Choose m>n sufficiently large that mH is very ample. A general g avoids
the finite singular locus of Q and cuts its smooth part transversely.
It also avoids C_sing and cuts C_sm transversely. These finitely many
open conditions are simultaneous: generation avoids each specified
point, and Bertini applies on the two smooth loci. It also avoids
vanishing on a component of Q or on C. Hence B=V(f,g) is a smooth
complete-intersection surface, g is a nonzerodivisor on O_C, and
D=C intersect B=V(g|_C) is a smooth ample curve in C_sm. At D, both Q
and C are smooth and local coordinates can be chosen with

\[
I_C=(f,z),\quad I_B=(f,g),\quad I_Y=(f,gz).
\tag{5}
\]

Thus these choices have the intended crossing, while Y retains C's
three old singular points. The argument below uses the full ideals and
does not replace Y by its lci open part.

**The standard union sequence and the degree comparison.** Locally,
if a f+b g belongs to I, then b g belongs to I. Since g is a
nonzerodivisor on O_C, b belongs to I. This proves

\[
J=I\cap(f,g)=(f)+gI.
\]

The resulting exact sequence is

\[
0\longrightarrow O_X(-m-n)
\xrightarrow{\ a\mapsto(-af,ag)\ }
I(-m)\oplus O_X(-n)
\xrightarrow{\ (u,v)\mapsto gu+fv\ } J
\longrightarrow0.
\tag{6}
\]

For its kernel, a relation gu+fv=0 and regularity of (f,g) give
v=ga and u=-fa; multiplication by g is injective in O_X. This
verifies exactness at every point, including the non-Cohen--Macaulay
points of C. This is the sheaf form of the known basic double linkage
construction, compared with Migliore--Nagel,
[*Applications of Liaison*, Theorem 2.7, pp. 5--6](https://academicweb.nd.edu/~jmiglior/MN14-webpg.pdf#page=5).
Its projective-space theorem is not being invoked with an unverified
ambient hypothesis; the displayed local verification supplies precisely
the needed sheaf identity on X.

Kodaira vanishing on S, Serre duality, and Kunneth give

\[
\omega_X=O_X,\quad H^1(O_X)=H^3(O_X)=0,
\quad H^i(O_X(k))=0\ (k>0,\ i>0),
\quad H^i(O_X(-k))=0\ (k>0,\ i<4).
\tag{7}
\]

Here one can compute each assertion for nonzero k on the two K3 factors:
L^k has only H^0 for k>0 and L^(-k) only H^2. The ideal sequence and
(7) identify H^2(X,I(n)) with H^1(C,O_C(n)). Thus (1) gives
H^2(X,I(n))=0. Twisting (6) by m+n gives

\[
0\longrightarrow O_X\longrightarrow I(n)\oplus O_X(m)
\longrightarrow J(m+n)\longrightarrow0.
\]

Its degree-two cohomology, using H^3(O_X)=0, now gives
H^2(X,J(m+n))=0. Serre duality on the smooth fourfold yields

\[
\operatorname{Ext}^2_X(J,O_X(-m-n))
\simeq H^2(X,J(m+n))^*=0.
\tag{8}
\]

The Ext form of duality for perfect complexes is supported by
[Stacks Lemma 57.4.1, tag 0FY7](https://stacks.math.columbia.edu/tag/0FY7);
coherent sheaves on the smooth X are perfect. No normal-bundle duality
on the singular Y is used.

Put E=I(-m) direct sum O_X(-n), the middle sheaf of (6). Since n-m<0,
one also has

\[
\operatorname{Ext}^1_X(O_X(-n),E)
=H^1(X,I(n-m))\oplus H^1(X,O_X)=0.
\tag{9}
\]

Indeed H^0(C,O_C(n-m))=0: its pullback to the smooth normalization in
L008 is antiample and has no nonzero section, and O_C injects into its
normalization sheaf. The ideal sequence and H^1(O_X(n-m))=0 then
give H^1(I(n-m))=0. This is the precise use of m>n.

**Recovering the forgotten extension and summand.** Suppose Y_A is
any flat embedded lift, with A-flat ideal J_A. Let
M_A=H_A^(-m-n), with reduction M=O_X(-m-n). The reduction sequence
0 -> M -> M_A -> M -> 0 and derived restriction give an exact segment

\[
\operatorname{Ext}^1_{X_A}(J_A,M_A)
\longrightarrow \operatorname{Ext}^1_X(J,M)
\longrightarrow \operatorname{Ext}^2_X(J,M).
\tag{10}
\]

To justify the restriction in (10), for the closed inclusion
i:X -> X_A, A-flatness gives Li^*J_A=J, so
RHom_(X_A)(J_A,i_*M)=RHom_X(J,M). This can equally be checked by
restricting a locally free resolution: its restriction stays exact
because the higher base Tor groups of J_A vanish. The last group in
(10) is zero by (8). Hence the central extension (6) lifts to

\[
0\longrightarrow M_A\longrightarrow E_A\longrightarrow J_A
\longrightarrow0.
\tag{11}
\]

E_A is A-flat and reduces to E. Its original decomposition is not
assumed to lift. Instead (9), applied to the reduction sequence for
E_A, lifts the central summand inclusion O_X(-n) -> E to a morphism
H_A^(-n) -> E_A. A morphism of A-flat modules with injective reduction
is injective and has A-flat cokernel. For example, the equality
ker(epsilon)=epsilon M on each flat module proves both assertions
directly by reducing a putative relation and dividing by epsilon.
Consequently the cokernel Q_A is A-flat and reduces to I(-m).
The sheaf P_A=Q_A tensor H_A^m is therefore an A-flat coherent lift of I.

This has recovered an abstract ideal sheaf, not yet its embedding.
No containment of a lifted B in Y_A has been claimed or is needed.

**Recovering an embedded ideal, including the three singular points.**
Apply the ideal-reconstruction argument proved in L012. Its applicability
here can be checked without any chosen presentation of P_A. L012 shows
that I has local projective dimension at most two, including at the
three double points. On the projective X_A, take two successive
surjections from finite sums of negative powers of H_A onto P_A and
its first kernel. Their kernels are A-flat. The second kernel has
locally free reduction by that projective-dimension bound, so is locally
free over X_A by Nakayama and A-flatness. This supplies a finite locally
free resolution and hence a determinant line D_A for P_A.

On U=X minus C the sheaf P_A is a line bundle and identifies canonically
with D_A. The reduction of D_A is det(I)=O_X: its standard trivialization
off C extends over the smooth X across codimension two. Since
H^1(X,O_X)=0, the kernel of Pic(X_A) -> Pic(X) is zero, and D_A is
trivial. Choose the trivialization compatibly with the central one.

Writing u:U_A -> X_A, Hartogs gives u_*O_(U_A)=O_(X_A). On a smooth
affine chart the ambient deformation is trivial, so this follows from
ordinary Hartogs for each of the two O_X summands of O_X[epsilon].
The central supporting reference is
[Stacks Lemma 15.24.18, tag 0AVB](https://stacks.math.columbia.edu/tag/0AVB);
the two-summand argument checks its use over the nonreduced base.
Adjunction therefore gives

\[
P_A\longrightarrow u_*(P_A|_{U_A})
\simeq u_*O_{U_A}=O_{X_A}.
\tag{12}
\]

The reduction is the ordinary inclusion I -> O_X: it agrees on U,
and a morphism into the torsion-free O_X is determined there.
Injective reduction and A-flatness again imply that (12) is injective
with flat cokernel. Its image is the ideal of an embedded lift C_A.
This proves the recovery assertion under (1) alone, with no lci or
normality hypothesis on C.

**The converse under (2).** If C_A is an embedded lift with ideal I_A,
(2) lifts f to f_A in H^0(X_A,I_A(n)). Equation (7) lifts g to a
section g_A of H_A^m. Form the analogue of the first two arrows in
(6), using f_A and g_A. The first arrow has injective reduction, so
its cokernel is A-flat and reduces to J. The second arrow induces a
map from that cokernel to O_(X_A), reducing to J -> O_X. It too is
injective with flat cokernel. Its image is (f_A)+g_A I_A and defines
a flat embedded lift of Y. Regularity of g on O_C also persists on
the flat O_(C_A); locally the same elementary intersection argument
identifies it with the union of C_A and V(f_A,g_A).

This proves (3). Serre vanishing ensures (1) and (2) for all
sufficiently large n, and the earlier Bertini argument supplies actual
smooth B for all sufficiently large m relative to such n. Thus the
negative regime is nonempty and includes the proposed ample smooth
double curves; it is not a vacuous obstruction.

**The main-gap comparison and scope.** L007's ideal-gluing criterion
applies to Y using Hom(I_Y,O_Y); it characterizes the first-order
embedded lifting locus without requiring Y lci. Under (1)--(2), (3)
and L008 identify that locus with V_D, of dimension three in the
four-dimensional V_RM. Under (1) alone it is contained in V_D, which
already excludes every transverse RM direction.

There is no common surface component in C and B, and both have
multiplicity one, so (4) follows from the complete-intersection cycle
class. For h=p_1^*ell+p_2^*ell, its square acts trivially on T(S): the
pure-factor terms vanish by degree and the mixed term pairs with ell,
which is orthogonal to T(S). L006 and L007 identify the action of [C]
with U. Thus the class still passes the Hodge and non-scalar-action
tests, but the recovery obstruction prevents the needed transverse lift.

This specializes known double-linkage, duality and sheaf-deformation
tools. The saved assessment did not match the full recovery statement
to a theorem; this is a local informative negative result, not certified
originality. The known 21-dimensional cycle span and the set of surfaces
covered have not increased. The degree threshold is qualitative; no
claim about all positive n or all representatives is made. Higher-order
lifts and the universal target are not consequences of this calculation.

## Mathlib

Coverage of the full statement: **not checked**. No full match,
supporting Mathlib name, or absence from checked Mathlib sources is
claimed. The directly linked Stacks Bertini, Serre-duality and Hartogs
statements, and Migliore--Nagel Theorem 2.7, are supporting mathematical
references, not matches for the relative union-lifting assertion.
Serre generation and vanishing, Kodaira vanishing on K3 surfaces,
Kunneth, derived restriction adjunction, and Nakayama are further named
standard inputs. The specialized extension recovery, the two relevant
Ext vanishings, their singular-point applicability and the scoped
three-versus-four lifting comparison are proved above.
